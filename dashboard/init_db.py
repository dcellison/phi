#!/usr/bin/env python3
"""
Initialize the Phi Dashboard database from JSON vocabulary files.
Run this script to rebuild the database without needing FastAPI installed.
"""

import json
import sqlite3
from pathlib import Path

# Configuration
PROJECT_ROOT = Path(__file__).parent.parent
VOCABULARY_DIR = PROJECT_ROOT / "vocabulary"
CONTENT_DIR = VOCABULARY_DIR / "content"
FUNCTION_DIR = VOCABULARY_DIR / "function"
INTERJECTION_DIR = VOCABULARY_DIR / "interjection"
DB_PATH = Path(__file__).parent / "lexicon.db"


def init_db():
    """Initialize/rebuild the database from JSON files."""
    if DB_PATH.exists():
        DB_PATH.unlink()
        print(f"Removed old database: {DB_PATH}")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS words (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        word TEXT UNIQUE NOT NULL,
        gloss TEXT NOT NULL,
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
        source_file TEXT NOT NULL,
        category TEXT NOT NULL,
        subcategory TEXT
    )
    """)

    entries_added = 0

    # Process content words
    if CONTENT_DIR.exists():
        print(f"Processing content words from {CONTENT_DIR}...")
        for file_path in sorted(CONTENT_DIR.glob("*.json")):
            if add_entry(cursor, file_path, "content", None):
                entries_added += 1

    # Process function words
    if FUNCTION_DIR.exists():
        print(f"Processing function words from {FUNCTION_DIR}...")
        for subdir in FUNCTION_DIR.iterdir():
            if subdir.is_dir():
                for file_path in sorted(subdir.glob("*.json")):
                    if add_entry(cursor, file_path, "function", subdir.name):
                        entries_added += 1

    # Process interjections
    if INTERJECTION_DIR.exists():
        print(f"Processing interjections from {INTERJECTION_DIR}...")
        for file_path in sorted(INTERJECTION_DIR.glob("*.json")):
            if add_entry(cursor, file_path, "interjection", None):
                entries_added += 1

    conn.commit()
    conn.close()
    return entries_added


def add_entry(cursor, file_path, category, subcategory):
    """Add a single JSON entry to the database."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            entry = json.load(f)

        if not all(k in entry for k in ['word', 'gloss']):
            print(f"  Skipping {file_path.name}: missing word or gloss")
            return False

        cursor.execute("""
        INSERT INTO words (
            word, gloss, ipa, syllables, slot, pos, concept,
            description, sound_symbolism, grammatical_notes, image_prompt,
            pillars, tags, source_file, category, subcategory
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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
            str(file_path.relative_to(PROJECT_ROOT)),
            category,
            subcategory
        ))
        return True
    except json.JSONDecodeError as e:
        print(f"  Error parsing {file_path.name}: {e}")
        return False
    except sqlite3.IntegrityError as e:
        print(f"  Error inserting {file_path.name}: {e}")
        return False


if __name__ == '__main__':
    print("Phi Dashboard - Database Initialization")
    print("=" * 40)
    print(f"Project root: {PROJECT_ROOT}")
    print(f"Database path: {DB_PATH}")
    print()

    count = init_db()

    print()
    print(f"Successfully added {count} entries to the database.")
    print(f"Database saved to: {DB_PATH}")
