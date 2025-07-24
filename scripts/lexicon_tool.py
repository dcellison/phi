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
VOCABULARY_DIR = PROJECT_ROOT / "vocabulary"
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
        help="Add a new lexicon entry."
    )
    add_parser.add_argument("--category", required=True, help="The vocabulary subdirectory (e.g., 'natural-world-and-environment').")
    add_parser.add_argument("--word", required=True)
    add_parser.add_argument("--gloss", required=True)
    add_parser.add_argument("--ipa", required=True)
    add_parser.add_argument("--concept", required=True)
    add_parser.add_argument("--description", required=True)
    add_parser.add_argument("--rationale", required=True)
    add_parser.add_argument("--syllables", required=True, nargs='+', help="Space-separated list of syllables.")
    add_parser.add_argument("--pos", required=True, nargs='+', help="Space-separated list of parts of speech.")
    add_parser.add_argument("--pillars", required=True, nargs='+', help="Space-separated list of philosophical pillars.")
    add_parser.add_argument("--tags", required=True, nargs='+', help="Space-separated list of tags.")
    add_parser.add_argument("--slot", type=int, help="The grammatical slot number (optional).")
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
    update_parser.add_argument("--rationale", help="New rationale.")
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

    master_list_path = VOCABULARY_DIR / "VOCABULARY.md"
    
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
                        if gloss and '---' not in gloss and 'word' not in gloss:
                            approved_glosses.add(gloss)
    except IOError as e:
        print(f"Error reading master list: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(approved_glosses)} approved concepts in the master list.")

    # 2. Get the actual state from the filesystem
    existing_files = {p.stem.lower() for p in VOCABULARY_DIR.glob("*.json")}

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
        "rationale": updated_fields.get('rationale', entry['rationale']),
        "pillars": updated_fields.get('pillars', json.loads(entry['pillars'])),
        "tags": updated_fields.get('tags', json.loads(entry['tags'])),
    }
    
    # Conditionally add slot
    slot_val = updated_fields.get('slot', entry['slot'])
    if slot_val is not None:
        json_output_entry['slot'] = slot_val

    # 3. Update the JSON file
    file_path = PROJECT_ROOT / entry['source_file']
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump([json_output_entry], f, indent=2)
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
            description = ?, rationale = ?, pillars = ?, tags = ?
        WHERE word = ?
        """, (
            json_output_entry.get('gloss'), json_output_entry.get('ipa'), 
            json.dumps(json_output_entry.get('syllables')), json_output_entry.get('slot'),
            json.dumps(json_output_entry.get('pos')), json_output_entry.get('concept'), 
            json_output_entry.get('description'), json_output_entry.get('rationale'), 
            json.dumps(json_output_entry.get('pillars')), json_output_entry.get('tags'),
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
    """Adds a new entry to the lexicon and creates the corresponding JSON file."""
    if not DB_PATH.exists():
        print("Database not found. Please run 'init' first.", file=sys.stderr)
        sys.exit(1)

    # 1. Uniqueness Check
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT word FROM lexicon WHERE LOWER(word) = ? OR LOWER(gloss) = ?", (args.word.lower(), args.gloss.lower()))
        existing = cursor.fetchone()
        if existing:
            print(f"Error: An entry with a similar word or gloss already exists: '{existing[0]}'. Aborting.", file=sys.stderr)
            conn.close()
            sys.exit(1)
    except sqlite3.Error as e:
        print(f"Database error during uniqueness check: {e}", file=sys.stderr)
        sys.exit(1)

    # 2. Prepare data and file path
    new_entry = {
        "word": args.word,
        "gloss": args.gloss,
        "ipa": args.ipa,
        "syllables": args.syllables,
        "pos": args.pos,
        "concept": args.concept,
        "description": args.description,
        "rationale": args.rationale,
        "pillars": args.pillars,
        "tags": args.tags
    }
    if args.slot is not None:
        new_entry['slot'] = args.slot
    
    category_path = VOCABULARY_DIR / args.category
    category_path.mkdir(parents=True, exist_ok=True)
    # Use the gloss for the filename, per project convention.
    file_path = category_path / f"{args.gloss}.json"

    if file_path.exists():
        print(f"Error: JSON file already exists at {file_path}. Aborting.", file=sys.stderr)
        conn.close()
        sys.exit(1)

    # 3. Write JSON file first (as the source of truth)
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump([new_entry], f, indent=2)
        print(f"Successfully created JSON file: {file_path.relative_to(PROJECT_ROOT)}")
    except IOError as e:
        print(f"Error writing JSON file: {e}", file=sys.stderr)
        conn.close()
        sys.exit(1)

    # 4. Insert into database
    try:
        cursor.execute("""
        INSERT INTO lexicon (
            word, gloss, ipa, syllables, slot, pos, concept, 
            description, rationale, pillars, tags, source_file
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            new_entry.get('word'),
            new_entry.get('gloss'),
            new_entry.get('ipa'),
            json.dumps(new_entry.get('syllables')),
            new_entry.get('slot'),
            json.dumps(new_entry.get('pos')),
            new_entry.get('concept'),
            new_entry.get('description'),
            new_entry.get('rationale'),
            json.dumps(new_entry.get('pillars')),
            json.dumps(new_entry.get('tags')),
            str(file_path.relative_to(PROJECT_ROOT))
        ))
        conn.commit()
        print(f"Successfully added entry for '{args.word}' to the database.")
    except sqlite3.Error as e:
        print(f"Database error during insert: {e}", file=sys.stderr)
        print("Rolling back file creation...")
        file_path.unlink() # Attempt to clean up the created file
        sys.exit(1)
    finally:
        conn.close()

    print("\nNew lexicon entry added successfully!")



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
                'source_file': entry[11]
            }
            print(json.dumps(entry_dict, indent=2))
        sys.exit(1)


def init_db(args):
    """
    Scans the vocabulary directory, creates a new SQLite database,
    and populates it with all lexicon entries from the JSON files.
    """
    print("Initializing lexicon database...")
    
    # 1. Find all JSON files
    json_files = sorted(list(VOCABULARY_DIR.glob("**/*.json")))
    if not json_files:
        print("Error: No .json files found in the vocabulary directory.", file=sys.stderr)
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

    # 3. Create Table
    # Based on schema.json, but simplified for DB storage.
    # Arrays will be stored as JSON strings.
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
        rationale TEXT,
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
                data = json.load(f)
                for entry in data:
                    # Ensure all required keys are present
                    if not all(k in entry for k in ['word', 'gloss']):
                        continue

                    cursor.execute("""
                    INSERT INTO lexicon (
                        word, gloss, ipa, syllables, slot, pos, concept, 
                        description, rationale, pillars, tags, source_file
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        entry.get('word'),
                        entry.get('gloss'),
                        entry.get('ipa'),
                        json.dumps(entry.get('syllables')),
                        entry.get('slot'),
                        json.dumps(entry.get('pos')),
                        entry.get('concept'),
                        entry.get('description'),
                        entry.get('rationale'),
                        json.dumps(entry.get('pillars')),
                        json.dumps(entry.get('tags')),
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
