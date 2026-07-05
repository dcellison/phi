#!/usr/bin/env python3
"""
Scans the vocabulary/ directory for all .json files, extracts the
Phi word and English gloss from each, and prints a complete, sorted list.

This script is used by the AI to perform a robust anti-collision check
before proposing new words. It explicitly checks for and reports on:
1. Duplicate Phi words.
2. Duplicate English glosses (filenames).
"""
import json
from pathlib import Path
from collections import defaultdict

def main():
    """
    Main function to scan vocabulary, check for duplicates, and print the lexicon.
    """
    try:
        project_root = Path(__file__).parent.parent
        vocabulary_dir = project_root / 'vocabulary'

        if not vocabulary_dir.is_dir():
            print(f"Error: Vocabulary directory not found at {vocabulary_dir}")
            return

        lexicon = defaultdict(list)
        glosses = defaultdict(list)
        json_files = sorted(vocabulary_dir.rglob('*.json'))

        for file_path in json_files:
            gloss = file_path.stem
            glosses[gloss].append(str(file_path.relative_to(project_root)))

            with open(file_path, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    if data and isinstance(data, list) and isinstance(data[0], dict):
                        word = data[0].get("word")
                        if word:
                            lexicon[word].append(gloss)
                except json.JSONDecodeError:
                    print(f"Warning: Could not decode JSON from {file_path}")
                except (IndexError, KeyError):
                    print(f"Warning: Could not find 'word' key in {file_path}")

        # --- Report Duplicates ---
        print("--- Duplicate Check ---")
        has_duplicates = False
        
        duplicate_words = {word: glosses for word, glosses in lexicon.items() if len(glosses) > 1}
        if duplicate_words:
            has_duplicates = True
            print("\n[ERROR] Found Duplicate Phi Words:")
            for word, gloss_list in duplicate_words.items():
                print(f"  - '{word}' appears in: {', '.join(gloss_list)}")

        duplicate_glosses = {gloss: paths for gloss, paths in glosses.items() if len(paths) > 1}
        if duplicate_glosses:
            has_duplicates = True
            print("\n[ERROR] Found Duplicate Glosses (Filenames):")
            for gloss, path_list in duplicate_glosses.items():
                print(f"  - '{gloss}.json' found at: {', '.join(path_list)}")

        if not has_duplicates:
            print("No duplicates found. Lexicon is clean.")

        # --- Report Full Lexicon ---
        print("\n--- Complete Phi Lexicon ---")
        sorted_words = sorted(lexicon.keys())
        print(f"Total unique words found: {len(sorted_words)}")
        for word in sorted_words:
            print(word)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()