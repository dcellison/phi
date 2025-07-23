#!/usr/bin/env python3
"""
Scans the vocabulary/ directory for all .json files, extracts the
Phi word from each, and prints a complete, sorted list. This is used
by the AI to perform an anti-collision check before proposing new words.
"""
import json
from pathlib import Path

def main():
    """
    Main function to scan vocabulary and print the lexicon.
    """
    try:
        # The script is in scripts/, so the project root is its parent.
        project_root = Path(__file__).parent.parent
        vocabulary_dir = project_root / 'vocabulary'

        if not vocabulary_dir.is_dir():
            print(f"Error: Vocabulary directory not found at {vocabulary_dir}")
            return

        phi_words = []
        json_files = sorted(vocabulary_dir.rglob('*.json'))

        for file_path in json_files:
            with open(file_path, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    if data and isinstance(data, list) and isinstance(data[0], dict):
                        word = data[0].get("word")
                        if word:
                            phi_words.append(word)
                except json.JSONDecodeError:
                    print(f"Warning: Could not decode JSON from {file_path}")
                except (IndexError, KeyError):
                    print(f"Warning: Could not find 'word' key in {file_path}")

        phi_words.sort()

        print("--- Complete Phi Lexicon ---")
        print(f"Total words found: {len(phi_words)}")
        print(", ".join(phi_words))

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
