#!/usr/bin/env python3
"""
Strict duplicate checker for Phi vocabulary.
This script will find ALL duplicates in the vocabulary and fail if any exist.
"""

import json
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).parent.parent
VOCABULARY_DIR = PROJECT_ROOT / "vocabulary"

def check_for_duplicates():
    """Check all JSON files for duplicate words or glosses."""
    
    # Track all words and glosses with their file locations
    words = {}  # word -> file path
    glosses = {}  # gloss -> file path
    errors = []
    
    # Find all JSON files
    json_files = list(VOCABULARY_DIR.rglob("*.json"))
    print(f"Checking {len(json_files)} vocabulary files for duplicates...")
    
    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                entry = json.load(f)
            
            if 'word' in entry and entry['word']:
                word = entry['word'].lower()
                if word in words:
                    errors.append(f"DUPLICATE WORD '{entry['word']}': {file_path.relative_to(PROJECT_ROOT)} and {words[word]}")
                else:
                    words[word] = str(file_path.relative_to(PROJECT_ROOT))
            
            if 'gloss' in entry and entry['gloss']:
                gloss = entry['gloss'].lower()
                if gloss in glosses:
                    errors.append(f"DUPLICATE GLOSS '{entry['gloss']}': {file_path.relative_to(PROJECT_ROOT)} and {glosses[gloss]}")
                else:
                    glosses[gloss] = str(file_path.relative_to(PROJECT_ROOT))
                    
        except json.JSONDecodeError:
            errors.append(f"INVALID JSON: {file_path.relative_to(PROJECT_ROOT)}")
        except Exception as e:
            errors.append(f"ERROR reading {file_path.relative_to(PROJECT_ROOT)}: {e}")
    
    # Report results
    if errors:
        print("\n❌ DUPLICATE CHECK FAILED!\n")
        for error in errors:
            print(f"  • {error}")
        print(f"\nFound {len(errors)} problems that must be fixed.")
        return False
    else:
        print(f"\n✅ NO DUPLICATES FOUND!")
        print(f"  • Checked {len(words)} unique words")
        print(f"  • Checked {len(glosses)} unique glosses")
        return True

if __name__ == "__main__":
    if not check_for_duplicates():
        sys.exit(1)  # Exit with error code if duplicates found