#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Simple Lexicon Management Tool for the Phi Language Project.

This tool provides a lightweight index for the Phi vocabulary,
using a minimal SQLite database for uniqueness checks and file lookups,
while keeping JSON files as the single source of truth.
"""

import argparse
import json
import sqlite3
from pathlib import Path
import sys

# --- Database Configuration ---
DB_FILE = "lexicon.db"
PROJECT_ROOT = Path(__file__).parent.parent
VOCABULARY_DIR = PROJECT_ROOT / "vocabulary"
CONTENT_DIR = VOCABULARY_DIR / "content"
FUNCTION_DIR = VOCABULARY_DIR / "function"
DB_PATH = PROJECT_ROOT / DB_FILE

# --- Main Application ---

def main():
    """Main function to run the CLI."""
    parser = argparse.ArgumentParser(
        description="Phi Lexicon Management Tool (Simplified)",
        formatter_class=argparse.RawTextHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- Init Command ---
    init_parser = subparsers.add_parser(
        "init",
        help="Initialize or rebuild the lexicon index from JSON files."
    )
    init_parser.set_defaults(func=init_db)

    # --- Find Command ---
    find_parser = subparsers.add_parser(
        "find",
        help="Check if a word or gloss exists."
    )
    find_parser.add_argument("term", help="The word or gloss to search for.")
    find_parser.set_defaults(func=find_entry)

    # --- View Command ---
    view_parser = subparsers.add_parser(
        "view",
        help="View the full definition of a word."
    )
    view_parser.add_argument("term", help="The word or gloss to view.")
    view_parser.set_defaults(func=view_entry)

    # --- Add Command ---
    add_parser = subparsers.add_parser(
        "add",
        help="Add a word to the index from its JSON file."
    )
    add_parser.add_argument("json_file", help="Path to the JSON file.")
    add_parser.set_defaults(func=add_entry)

    # --- Update Command ---
    update_parser = subparsers.add_parser(
        "update",
        help="Update a word's JSON file and refresh the index."
    )
    update_parser.add_argument("word", help="The word to update.")
    update_parser.add_argument("json_file", help="Path to the updated JSON file.")
    update_parser.set_defaults(func=update_entry)

    # --- Delete Command ---
    delete_parser = subparsers.add_parser(
        "delete",
        help="Delete a word from the index and optionally its JSON file."
    )
    delete_parser.add_argument("word", help="The word to delete.")
    delete_parser.add_argument("--keep-file", action="store_true", 
                              help="Keep the JSON file (only remove from index).")
    delete_parser.set_defaults(func=delete_entry)

    # --- List Command ---
    list_parser = subparsers.add_parser(
        "list",
        help="List all words in the index."
    )
    list_parser.add_argument("--type", choices=['all', 'content', 'function'],
                           default='all', help="Filter by word type.")
    list_parser.set_defaults(func=list_entries)

    # --- Sync Command ---
    sync_parser = subparsers.add_parser(
        "sync",
        help="Sync the index with JSON files (add missing, remove orphaned)."
    )
    sync_parser.set_defaults(func=sync_index)

    args = parser.parse_args()
    args.func(args)

# --- Command Functions ---

def init_db(args):
    """
    Initialize or rebuild the index from all JSON files.
    This creates a minimal index with just word, gloss, and file path.
    """
    print("Initializing lexicon index...")
    
    # 1. Find all JSON files
    json_files = []
    if CONTENT_DIR.exists():
        json_files.extend(sorted(list(CONTENT_DIR.glob("*.json"))))
    if FUNCTION_DIR.exists():
        json_files.extend(sorted(list(FUNCTION_DIR.rglob("*.json"))))
    
    if not json_files:
        print("Error: No JSON files found in vocabulary directories.", file=sys.stderr)
        sys.exit(1)
        
    print(f"Found {len(json_files)} JSON files to index.")

    # 2. Create fresh database
    if DB_PATH.exists():
        DB_PATH.unlink()
        
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
    except sqlite3.Error as e:
        print(f"Database error: {e}", file=sys.stderr)
        sys.exit(1)

    # 3. Create minimal table
    cursor.execute("""
    CREATE TABLE lexicon (
        word TEXT PRIMARY KEY,
        gloss TEXT UNIQUE NOT NULL,
        source_file TEXT NOT NULL
    )
    """)
    print("Database table created.")

    # 4. Index each file
    entries_added = 0
    errors = []
    
    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                entry = json.load(f)
                
            if 'word' in entry and 'gloss' in entry:
                cursor.execute("""
                INSERT INTO lexicon (word, gloss, source_file)
                VALUES (?, ?, ?)
                """, (
                    entry['word'],
                    entry['gloss'],
                    str(file_path.relative_to(PROJECT_ROOT))
                ))
                entries_added += 1
                
        except json.JSONDecodeError:
            errors.append(f"Could not parse: {file_path.name}")
        except sqlite3.IntegrityError as e:
            errors.append(f"{file_path.name}: {entry.get('word')}/{entry.get('gloss')} - duplicate")
        except Exception as e:
            errors.append(f"{file_path.name}: {e}")

    conn.commit()
    conn.close()

    # 5. Report results
    print(f"\n✓ Indexed {entries_added} entries successfully.")
    if errors:
        print(f"\n⚠ {len(errors)} errors:")
        for error in errors[:10]:  # Show first 10 errors
            print(f"  - {error}")
        if len(errors) > 10:
            print(f"  ... and {len(errors) - 10} more")

def find_entry(args):
    """Check if a word or gloss exists in the index."""
    if not DB_PATH.exists():
        print("Database not found. Please run 'init' first.", file=sys.stderr)
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    term = args.term.lower()
    cursor.execute("""
    SELECT word, gloss, source_file FROM lexicon 
    WHERE LOWER(word) = ? OR LOWER(gloss) = ?
    """, (term, term))
    
    result = cursor.fetchone()
    conn.close()

    if result:
        print(f"✓ Found: {result[0]} ({result[1]}) in {result[2]}")
        sys.exit(1)  # Exit with error code to indicate word exists
    else:
        print(f"✓ '{args.term}' is available.")
        sys.exit(0)  # Exit with success to indicate word is available

def view_entry(args):
    """View the full definition from the JSON file."""
    if not DB_PATH.exists():
        print("Database not found. Please run 'init' first.", file=sys.stderr)
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    term = args.term.lower()
    cursor.execute("""
    SELECT source_file FROM lexicon 
    WHERE LOWER(word) = ? OR LOWER(gloss) = ?
    """, (term, term))
    
    result = cursor.fetchone()
    conn.close()

    if not result:
        print(f"Error: '{args.term}' not found in index.", file=sys.stderr)
        sys.exit(1)

    # Load and display the full JSON
    json_path = PROJECT_ROOT / result[0]
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(json.dumps(data, indent=2, ensure_ascii=False))
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error reading {json_path}: {e}", file=sys.stderr)
        sys.exit(1)

def add_entry(args):
    """Add a single word to the index from its JSON file."""
    if not DB_PATH.exists():
        print("Database not found. Please run 'init' first.", file=sys.stderr)
        sys.exit(1)

    json_path = Path(args.json_file)
    if not json_path.exists():
        print(f"Error: File not found: {json_path}", file=sys.stderr)
        sys.exit(1)
    
    # Read the JSON file
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            entry = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}", file=sys.stderr)
        sys.exit(1)

    if 'word' not in entry or 'gloss' not in entry:
        print("Error: JSON must contain 'word' and 'gloss' fields.", file=sys.stderr)
        sys.exit(1)

    # Add to index
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Check for duplicates
    cursor.execute("""
    SELECT word FROM lexicon 
    WHERE LOWER(word) = ? OR LOWER(gloss) = ?
    """, (entry['word'].lower(), entry['gloss'].lower()))
    
    if cursor.fetchone():
        print(f"Error: '{entry['word']}' or '{entry['gloss']}' already exists.", file=sys.stderr)
        conn.close()
        sys.exit(1)

    # Determine relative path
    if json_path.is_absolute():
        source_file = str(json_path.relative_to(PROJECT_ROOT))
    else:
        source_file = str(json_path)

    # Insert into index
    try:
        cursor.execute("""
        INSERT INTO lexicon (word, gloss, source_file)
        VALUES (?, ?, ?)
        """, (entry['word'], entry['gloss'], source_file))
        conn.commit()
        print(f"✓ Added '{entry['word']}' ({entry['gloss']}) to index.")
    except sqlite3.Error as e:
        print(f"Database error: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        conn.close()

def update_entry(args):
    """Update a word's JSON file path in the index."""
    if not DB_PATH.exists():
        print("Database not found. Please run 'init' first.", file=sys.stderr)
        sys.exit(1)

    json_path = Path(args.json_file)
    if not json_path.exists():
        print(f"Error: File not found: {json_path}", file=sys.stderr)
        sys.exit(1)

    # Read the new JSON file
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            entry = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}", file=sys.stderr)
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Check if word exists
    cursor.execute("SELECT * FROM lexicon WHERE word = ?", (args.word,))
    if not cursor.fetchone():
        print(f"Error: Word '{args.word}' not found in index.", file=sys.stderr)
        conn.close()
        sys.exit(1)

    # Determine relative path
    if json_path.is_absolute():
        source_file = str(json_path.relative_to(PROJECT_ROOT))
    else:
        source_file = str(json_path)

    # Update the index
    try:
        cursor.execute("""
        UPDATE lexicon 
        SET gloss = ?, source_file = ?
        WHERE word = ?
        """, (entry['gloss'], source_file, args.word))
        conn.commit()
        print(f"✓ Updated '{args.word}' in index.")
    except sqlite3.Error as e:
        print(f"Database error: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        conn.close()

def delete_entry(args):
    """Delete a word from the index and optionally its JSON file."""
    if not DB_PATH.exists():
        print("Database not found. Please run 'init' first.", file=sys.stderr)
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Get file path before deleting
    cursor.execute("SELECT source_file FROM lexicon WHERE word = ?", (args.word,))
    result = cursor.fetchone()
    
    if not result:
        print(f"Error: Word '{args.word}' not found in index.", file=sys.stderr)
        conn.close()
        sys.exit(1)

    file_path = PROJECT_ROOT / result[0]

    # Delete from index
    try:
        cursor.execute("DELETE FROM lexicon WHERE word = ?", (args.word,))
        conn.commit()
        print(f"✓ Removed '{args.word}' from index.")
    except sqlite3.Error as e:
        print(f"Database error: {e}", file=sys.stderr)
        conn.close()
        sys.exit(1)

    conn.close()

    # Optionally delete the JSON file
    if not args.keep_file and file_path.exists():
        try:
            file_path.unlink()
            print(f"✓ Deleted file: {file_path.name}")
        except IOError as e:
            print(f"Warning: Could not delete file: {e}", file=sys.stderr)

def list_entries(args):
    """List all words in the index."""
    if not DB_PATH.exists():
        print("Database not found. Please run 'init' first.", file=sys.stderr)
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Build query based on type filter
    if args.type == 'content':
        query = "SELECT word, gloss FROM lexicon WHERE source_file LIKE 'vocabulary/content/%' ORDER BY word"
    elif args.type == 'function':
        query = "SELECT word, gloss FROM lexicon WHERE source_file LIKE 'vocabulary/function/%' ORDER BY word"
    else:
        query = "SELECT word, gloss FROM lexicon ORDER BY word"

    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()

    if not results:
        print("No entries found.")
        return

    print(f"\n{len(results)} entries ({args.type}):\n")
    for word, gloss in results:
        print(f"  {word:15} {gloss}")

def sync_index(args):
    """Sync the index with JSON files - add missing, report orphaned."""
    if not DB_PATH.exists():
        print("Database not found. Please run 'init' first.", file=sys.stderr)
        sys.exit(1)

    # Get all JSON files
    json_files = {}
    if CONTENT_DIR.exists():
        for f in CONTENT_DIR.glob("*.json"):
            json_files[str(f.relative_to(PROJECT_ROOT))] = f
    if FUNCTION_DIR.exists():
        for f in FUNCTION_DIR.rglob("*.json"):
            json_files[str(f.relative_to(PROJECT_ROOT))] = f

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Get all indexed files
    cursor.execute("SELECT source_file, word FROM lexicon")
    indexed_files = {row[0]: row[1] for row in cursor.fetchall()}

    # Find missing files (in filesystem but not in index)
    missing_from_index = set(json_files.keys()) - set(indexed_files.keys())
    
    # Find orphaned entries (in index but not in filesystem)
    orphaned_in_index = set(indexed_files.keys()) - set(json_files.keys())

    # Add missing files to index
    if missing_from_index:
        print(f"\nAdding {len(missing_from_index)} missing files to index:")
        for file_path_str in missing_from_index:
            file_path = json_files[file_path_str]
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    entry = json.load(f)
                if 'word' in entry and 'gloss' in entry:
                    cursor.execute("""
                    INSERT INTO lexicon (word, gloss, source_file)
                    VALUES (?, ?, ?)
                    """, (entry['word'], entry['gloss'], file_path_str))
                    print(f"  + {entry['word']} ({entry['gloss']})")
            except Exception as e:
                print(f"  ✗ Error with {file_path.name}: {e}")

    # Report orphaned entries
    if orphaned_in_index:
        print(f"\n⚠ {len(orphaned_in_index)} orphaned entries in index:")
        for file_path in orphaned_in_index:
            word = indexed_files[file_path]
            print(f"  - {word} ({file_path})")
        
        response = input("\nRemove orphaned entries from index? (y/n): ")
        if response.lower() == 'y':
            for file_path in orphaned_in_index:
                word = indexed_files[file_path]
                cursor.execute("DELETE FROM lexicon WHERE word = ?", (word,))
                print(f"  ✓ Removed {word}")

    conn.commit()
    conn.close()

    if not missing_from_index and not orphaned_in_index:
        print("✓ Index is already in sync with filesystem.")
    else:
        print("\n✓ Sync complete.")

if __name__ == "__main__":
    main()