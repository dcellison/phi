#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Lexicon Management Tool for the Phi Language Project.

This tool provides a command-line interface to manage the Phi vocabulary,
using a SQLite database to store and query lexicon data, while keeping the
JSON files as the single source of truth.
"""

import argparse
import json
import sqlite3
from pathlib import Path
import sys

# --- Database Configuration ---
DB_FILE = "lexicon.db"
PROJECT_ROOT = Path(__file__).parent.parent
VOCABULARY_DIR = PROJECT_ROOT / "vocabulary"  # Changed to vocabulary
CONTENT_DIR = VOCABULARY_DIR / "content"
FUNCTION_DIR = VOCABULARY_DIR / "function"
DB_PATH = PROJECT_ROOT / DB_FILE

# --- Main Application ---

def main():
    """Main function to run the CLI."""
    parser = argparse.ArgumentParser(
        description="Phi Lexicon Management Tool",
        formatter_class=argparse.RawTextHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- Init Command ---
    init_parser = subparsers.add_parser(
        "init",
        help="Initialize or re-initialize the lexicon database from JSON files."
    )
    init_parser.set_defaults(func=init_db)

    # --- Find Command ---
    find_parser = subparsers.add_parser(
        "find",
        help="Find a lexicon entry by word or gloss."
    )
    find_parser.add_argument("term", help="The word or gloss to search for.")
    find_parser.set_defaults(func=find_entry)

    # --- Add Command ---
    add_parser = subparsers.add_parser(
        "add",
        help="Add a new lexicon entry from a JSON file."
    )
    add_parser.add_argument("json_file", help="Path to the JSON file containing the word definition.")
    add_parser.set_defaults(func=add_entry)

    # --- Update Command ---
    update_parser = subparsers.add_parser(
        "update",
        help="Update an existing lexicon entry."
    )
    update_parser.add_argument("word", help="The word of the entry to update.")
    update_parser.add_argument("--gloss", help="New gloss.")
    update_parser.add_argument("--ipa", help="New IPA.")
    update_parser.add_argument("--concept", help="New concept.")
    update_parser.add_argument("--description", help="New description.")
    update_parser.add_argument("--sound_symbolism", help="New sound symbolism.")  # Changed from rationale
    update_parser.add_argument("--grammatical_notes", help="New grammatical notes.")
    update_parser.add_argument("--syllables", nargs='+', help="New space-separated list of syllables.")
    update_parser.add_argument("--pos", nargs='+', help="New space-separated list of parts of speech.")
    update_parser.add_argument("--pillars", nargs='+', help="New space-separated list of pillars.")
    update_parser.add_argument("--tags", nargs='+', help="New space-separated list of tags.")
    update_parser.add_argument("--slot", type=int, help="New slot number.")
    update_parser.set_defaults(func=update_entry)

    # --- Delete Command ---
    delete_parser = subparsers.add_parser(
        "delete",
        help="Delete a lexicon entry."
    )
    delete_parser.add_argument("word", help="The word of the entry to delete.")
    delete_parser.set_defaults(func=delete_entry)

    # --- Status Command ---
    status_parser = subparsers.add_parser(
        "status",
        help="Check the status of the vocabulary against the master list."
    )
    status_parser.set_defaults(func=get_status)


    args = parser.parse_args()
    args.func(args)

# --- Command Functions ---

def get_status(args):
    """Audits the vocabulary against the global master list."""
    import re

    master_list_path = CONTENT_DIR / "PHI_CORE_VOCABULARY.md"  # Updated path
    
    if not master_list_path.exists():
        print(f"Error: Master list not found at {master_list_path.relative_to(PROJECT_ROOT)}", file=sys.stderr)
        sys.exit(1)

    # 1. Parse the master list to get all approved glosses
    approved_glosses = set()
    try:
        with open(master_list_path, 'r', encoding='utf-8') as f:
            for line in f:
                if '|' in line: # Only process lines that look like table rows
                    match = re.match(r"\|\s*([^|]+?)\s*\|", line)
                    if match:
                        gloss = match.group(1).strip().lower()
                        # Handle entries with slashes (e.g., "parent/guardian")
                        if '/' in gloss:
                            for part in gloss.split('/'):
                                approved_glosses.add(part.strip())
                        elif gloss and '---' not in gloss and 'word' not in gloss:
                            approved_glosses.add(gloss)
    except IOError as e:
        print(f"Error reading master list: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(approved_glosses)} approved concepts in the master list.")

    # 2. Get the actual state from the filesystem (content directory only)
    existing_files = {p.stem.lower() for p in CONTENT_DIR.glob("*.json")}

    # 3. Compare and categorize
    ok, missing, orphaned = [], [], []
    
    # Check master list against filesystem
    for gloss in sorted(list(approved_glosses)):
        if gloss in existing_files:
            ok.append(gloss)
        else:
            missing.append(gloss)

    # Check filesystem for orphaned files
    for gloss in existing_files:
        if gloss not in approved_glosses:
            orphaned.append(gloss)

    # 4. Generate Report
    print(f"\n--- Audit Report ---")
        
    if missing:
        print(f"\n[!] MISSING ({len(missing)}):")
        for item in missing: print(f"  - {item}")

    if orphaned:
        print(f"\n[!] ORPHANED ({len(orphaned)}):")
        for item in orphaned: print(f"  - {item}")

    print(f"\n--- Summary ---")
    print(f"Total Planned: {len(approved_glosses)}")
    print(f"Existing: {len(ok)}")
    print(f"Missing: {len(missing)}")
    print(f"Orphaned: {len(orphaned)}")
    print("---------------")

    if not missing and not orphaned:
        print("\nVocabulary is fully aligned. No action needed.")
    else:
        print("\nVocabulary needs attention.")


def update_entry(args):
    """Updates an existing entry in the database and its JSON file."""
    if not DB_PATH.exists():
        print("Database not found. Please run 'init' first.", file=sys.stderr)
        sys.exit(1)

    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
    except sqlite3.Error as e:
        print(f"Database error: {e}", file=sys.stderr)
        sys.exit(1)

    # 1. Find the existing entry
    cursor.execute("SELECT * FROM lexicon WHERE word = ?", (args.word,))
    row = cursor.fetchone()
    if not row:
        print(f"Error: No entry found for word '{args.word}'. Aborting.", file=sys.stderr)
        conn.close()
        sys.exit(1)
    
    entry = dict(row)
    updated_fields = {k: v for k, v in vars(args).items() if v is not None and k not in ['word', 'func']}

    # 2. Create the updated entry object for JSON output
    json_output_entry = {
        "word": entry['word'],
        "gloss": updated_fields.get('gloss', entry['gloss']),
        "ipa": updated_fields.get('ipa', entry['ipa']),
        "syllables": updated_fields.get('syllables', json.loads(entry['syllables'])),
        "pos": updated_fields.get('pos', json.loads(entry['pos'])),
        "concept": updated_fields.get('concept', entry['concept']),
        "description": updated_fields.get('description', entry['description']),
        "sound_symbolism": updated_fields.get('sound_symbolism', entry['sound_symbolism']),  # Changed
        "pillars": updated_fields.get('pillars', json.loads(entry['pillars'])),
        "tags": updated_fields.get('tags', json.loads(entry['tags'])),
    }
    
    # Conditionally add optional fields
    slot_val = updated_fields.get('slot', entry['slot'])
    if slot_val is not None:
        json_output_entry['slot'] = slot_val
    
    grammatical_notes = updated_fields.get('grammatical_notes', entry.get('grammatical_notes'))
    if grammatical_notes:
        json_output_entry['grammatical_notes'] = grammatical_notes

    # Add image_prompt if it exists
    image_prompt = updated_fields.get('image_prompt', entry.get('image_prompt'))
    if image_prompt:
        json_output_entry['image_prompt'] = image_prompt

    # 3. Update the JSON file (no array wrapper)
    file_path = PROJECT_ROOT / entry['source_file']
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(json_output_entry, f, indent=2, ensure_ascii=False)  # Changed: no array
        print(f"Successfully updated JSON file: {file_path.relative_to(PROJECT_ROOT)}")
    except IOError as e:
        print(f"Error writing JSON file: {e}", file=sys.stderr)
        conn.close()
        sys.exit(1)

    # 4. Update the database
    try:
        cursor.execute("""
        UPDATE lexicon SET
            gloss = ?, ipa = ?, syllables = ?, slot = ?, pos = ?, concept = ?,
            description = ?, sound_symbolism = ?, grammatical_notes = ?, 
            image_prompt = ?, pillars = ?, tags = ?
        WHERE word = ?
        """, (
            json_output_entry.get('gloss'), json_output_entry.get('ipa'), 
            json.dumps(json_output_entry.get('syllables')), json_output_entry.get('slot'),
            json.dumps(json_output_entry.get('pos')), json_output_entry.get('concept'), 
            json_output_entry.get('description'), json_output_entry.get('sound_symbolism'), 
            json_output_entry.get('grammatical_notes'), json_output_entry.get('image_prompt'),
            json.dumps(json_output_entry.get('pillars')), json.dumps(json_output_entry.get('tags')),
            args.word
        ))
        conn.commit()
        print(f"Successfully updated entry for '{args.word}' in the database.")
    except sqlite3.Error as e:
        print(f"Database error during update: {e}", file=sys.stderr)
    finally:
        conn.close()

def delete_entry(args):
    """Deletes an entry from the database and removes its JSON file."""
    if not DB_PATH.exists():
        print("Database not found. Please run 'init' first.", file=sys.stderr)
        sys.exit(1)

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
    except sqlite3.Error as e:
        print(f"Database error: {e}", file=sys.stderr)
        sys.exit(1)

    # 1. Find the entry to get the file path
    cursor.execute("SELECT source_file FROM lexicon WHERE word = ?", (args.word,))
    row = cursor.fetchone()
    if not row:
        print(f"Error: No entry found for word '{args.word}'. Aborting.", file=sys.stderr)
        conn.close()
        sys.exit(1)
    
    file_path = PROJECT_ROOT / row[0]

    # 2. Delete from database first
    try:
        cursor.execute("DELETE FROM lexicon WHERE word = ?", (args.word,))
        conn.commit()
        print(f"Successfully deleted entry for '{args.word}' from the database.")
    except sqlite3.Error as e:
        print(f"Database error during delete: {e}", file=sys.stderr)
    finally:
        conn.close()

    # 3. Delete the JSON file
    if file_path.exists():
        try:
            file_path.unlink()
            print(f"Successfully deleted JSON file: {file_path.relative_to(PROJECT_ROOT)}")
        except IOError as e:
            print(f"Error deleting JSON file: {e}", file=sys.stderr)
            print("Please delete it manually.")
    else:
        print(f"Warning: Source file not found at {file_path}, but DB entry was removed.")

    print(f"\nDeletion of '{args.word}' complete.")


def add_entry(args):
    """Adds a new entry to the lexicon from a JSON file."""
    if not DB_PATH.exists():
        print("Database not found. Please run 'init' first.", file=sys.stderr)
        sys.exit(1)

    # 1. Read the JSON file
    json_path = Path(args.json_file)
    if not json_path.exists():
        print(f"Error: JSON file not found: {json_path}", file=sys.stderr)
        sys.exit(1)
    
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            entry = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON file: {e}", file=sys.stderr)
        sys.exit(1)
    except IOError as e:
        print(f"Error reading JSON file: {e}", file=sys.stderr)
        sys.exit(1)

    # 2. Validate required fields
    if not all(k in entry for k in ['word', 'gloss']):
        print("Error: JSON must contain at least 'word' and 'gloss' fields.", file=sys.stderr)
        sys.exit(1)

    # 3. Uniqueness Check
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT word FROM lexicon WHERE LOWER(word) = ? OR LOWER(gloss) = ?", 
                      (entry['word'].lower(), entry['gloss'].lower()))
        existing = cursor.fetchone()
        if existing:
            print(f"Error: An entry with a similar word or gloss already exists: '{existing[0]}'. Aborting.", file=sys.stderr)
            conn.close()
            sys.exit(1)
    except sqlite3.Error as e:
        print(f"Database error during uniqueness check: {e}", file=sys.stderr)
        sys.exit(1)

    # 4. Determine source file path (relative to project root)
    if json_path.is_absolute():
        source_file = str(json_path.relative_to(PROJECT_ROOT))
    else:
        source_file = str(json_path)

    # 5. Insert into database
    try:
        cursor.execute("""
        INSERT INTO lexicon (
            word, gloss, ipa, syllables, slot, pos, concept, 
            description, sound_symbolism, grammatical_notes, image_prompt, 
            pillars, tags, source_file
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            entry.get('word'),
            entry.get('gloss'),
            entry.get('ipa'),
            json.dumps(entry.get('syllables')) if entry.get('syllables') else None,
            entry.get('slot'),
            json.dumps(entry.get('pos')) if entry.get('pos') else None,
            entry.get('concept'),
            entry.get('description'),
            entry.get('sound_symbolism'),
            entry.get('grammatical_notes'),
            entry.get('image_prompt'),
            json.dumps(entry.get('pillars')) if entry.get('pillars') else None,
            json.dumps(entry.get('tags')) if entry.get('tags') else None,
            source_file
        ))
        conn.commit()
        print(f"Successfully added entry for '{entry['word']}' ({entry['gloss']}) to the database.")
    except sqlite3.Error as e:
        print(f"Database error during insert: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        conn.close()

    print("\nLexicon entry added successfully!")



def find_entry(args):
    """Finds and displays a lexicon entry by word or gloss."""
    if not DB_PATH.exists():
        print("Database not found. Please run 'init' first.", file=sys.stderr)
        sys.exit(1)

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
    except sqlite3.Error as e:
        print(f"Database error: {e}", file=sys.stderr)
        sys.exit(1)

    # Case-insensitive search
    term = args.term.lower()
    cursor.execute("""
    SELECT * FROM lexicon WHERE LOWER(word) = ? OR LOWER(gloss) = ?
    """, (term, term))
    
    results = cursor.fetchall()
    conn.close()

    if not results:
        print(f"Success: No entry found for '{args.term}'. It is unique.")
    else:
        print(f"Error: Found {len(results)} existing entry/entries for '{args.term}':")
        for entry in results:
            # Recreate dict from tuple for pretty printing
            entry_dict = {
                'word': entry[0],
                'gloss': entry[1],
                'concept': entry[6],
                'source_file': entry[13]  # Adjusted index for new column
            }
            print(json.dumps(entry_dict, indent=2))
        sys.exit(1)


def init_db(args):
    """
    Scans the vocabulary directories (content and function subdirs),
    creates a new SQLite database, and populates it with all lexicon entries
    from the JSON files.
    """
    print("Initializing lexicon database...")
    
    # 1. Find all JSON files in both content and function directories
    json_files = []
    
    # Content directory
    if CONTENT_DIR.exists():
        json_files.extend(sorted(list(CONTENT_DIR.glob("*.json"))))
    
    # Function directory and all subdirectories
    if FUNCTION_DIR.exists():
        json_files.extend(sorted(list(FUNCTION_DIR.rglob("*.json"))))
    
    if not json_files:
        print("Error: No .json files found in the vocabulary directories.", file=sys.stderr)
        sys.exit(1)
        
    print(f"Found {len(json_files)} JSON files to process.")

    # 2. Connect to DB (deletes old one if it exists)
    if DB_PATH.exists():
        DB_PATH.unlink()
        
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
    except sqlite3.Error as e:
        print(f"Database error: {e}", file=sys.stderr)
        sys.exit(1)

    # 3. Create Table with updated schema (added image_prompt)
    cursor.execute("""
    CREATE TABLE lexicon (
        word TEXT PRIMARY KEY,
        gloss TEXT NOT NULL UNIQUE,
        ipa TEXT,
        syllables TEXT,
        slot INTEGER,
        pos TEXT,
        concept TEXT,
        description TEXT,
        sound_symbolism TEXT,
        grammatical_notes TEXT,
        image_prompt TEXT,
        pillars TEXT,
        tags TEXT,
        source_file TEXT NOT NULL
    )
    """)
    print("Database table 'lexicon' created successfully.")

    # 4. Parse and Insert Data
    entries_added = 0
    for file_path in json_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                entry = json.load(f)  # Changed: expect single object, not array
                
                # Ensure all required keys are present
                if not all(k in entry for k in ['word', 'gloss']):
                    continue

                cursor.execute("""
                INSERT INTO lexicon (
                    word, gloss, ipa, syllables, slot, pos, concept, 
                    description, sound_symbolism, grammatical_notes, image_prompt,
                    pillars, tags, source_file
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    entry.get('word'),
                    entry.get('gloss'),
                    entry.get('ipa'),
                    json.dumps(entry.get('syllables')),
                    entry.get('slot'),
                    json.dumps(entry.get('pos')),
                    entry.get('concept'),
                    entry.get('description'),
                    entry.get('sound_symbolism'),  # Changed from rationale
                    entry.get('grammatical_notes'),
                    entry.get('image_prompt'),  # New field
                    json.dumps(entry.get('pillars')) if entry.get('pillars') else None,
                    json.dumps(entry.get('tags')) if entry.get('tags') else None,
                    str(file_path.relative_to(PROJECT_ROOT))
                ))
                entries_added += 1
            except json.JSONDecodeError:
                print(f"Warning: Could not parse {file_path}", file=sys.stderr)
            except sqlite3.IntegrityError as e:
                print(f"Error adding entry from {file_path}: {e}", file=sys.stderr)
                print(f"Offending entry: {entry.get('word')} / {entry.get('gloss')}")


    conn.commit()
    conn.close()

    print(f"\nInitialization complete. Added {entries_added} entries to {DB_FILE}.")


if __name__ == "__main__":
    main()