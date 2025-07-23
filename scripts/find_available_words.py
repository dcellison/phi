#!/usr/bin/env python3
"""Find all available Phi words that haven't been used yet."""

import json
import os
from pathlib import Path

# Phi phonological inventory
CONSONANTS = ['h', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w']
FRICATIVE_DIGRAPHS = ['ph', 'th', 'sh', 'wh']
ALL_CONSONANTS = CONSONANTS + FRICATIVE_DIGRAPHS
VOWELS = ['a', 'e', 'i', 'o', 'u']

def load_existing_words():
    """Load all existing Phi words from the vocabulary."""
    existing_words = set()
    
    # Define the directories to search
    vocab_dirs = [
        'lexicon',
        'grammar', 
        'words'
    ]
    
    for vocab_dir in vocab_dirs:
        if os.path.exists(vocab_dir):
            for root, dirs, files in os.walk(vocab_dir):
                for file in files:
                    if file.endswith('.json'):
                        try:
                            with open(os.path.join(root, file), 'r') as f:
                                data = json.load(f)
                                # Handle both single dict and list of dicts
                                if isinstance(data, dict):
                                    if 'word' in data:
                                        existing_words.add(data['word'])
                                elif isinstance(data, list):
                                    for item in data:
                                        if isinstance(item, dict) and 'word' in item:
                                            existing_words.add(item['word'])
                        except:
                            pass
    
    return existing_words

def generate_two_syllable_words():
    """Generate all possible two-syllable Phi words."""
    all_words = []
    
    # Pattern CV.CV
    for c1 in ALL_CONSONANTS:
        for v1 in VOWELS:
            for c2 in ALL_CONSONANTS:
                for v2 in VOWELS:
                    word = f"{c1}{v1}{c2}{v2}"
                    all_words.append(word)
    
    # Pattern CV.V
    for c in ALL_CONSONANTS:
        for v1 in VOWELS:
            for v2 in VOWELS:
                word = f"{c}{v1}{v2}"
                all_words.append(word)
    
    return all_words

def generate_three_syllable_words():
    """Generate all possible three-syllable Phi words."""
    all_words = []
    
    # Pattern CV.CV.CV
    for c1 in ALL_CONSONANTS:
        for v1 in VOWELS:
            for c2 in ALL_CONSONANTS:
                for v2 in VOWELS:
                    for c3 in ALL_CONSONANTS:
                        for v3 in VOWELS:
                            word = f"{c1}{v1}{c2}{v2}{c3}{v3}"
                            all_words.append(word)
    
    # Pattern CV.CV.V
    for c1 in ALL_CONSONANTS:
        for v1 in VOWELS:
            for c2 in ALL_CONSONANTS:
                for v2 in VOWELS:
                    for v3 in VOWELS:
                        word = f"{c1}{v1}{c2}{v2}{v3}"
                        all_words.append(word)
    
    # Pattern CV.V.CV
    for c1 in ALL_CONSONANTS:
        for v1 in VOWELS:
            for v2 in VOWELS:
                for c2 in ALL_CONSONANTS:
                    for v3 in VOWELS:
                        word = f"{c1}{v1}{v2}{c2}{v3}"
                        all_words.append(word)
    
    return all_words

def main():
    print("Loading existing Phi vocabulary...")
    existing_words = load_existing_words()
    print(f"Found {len(existing_words)} existing words")
    
    print("\nGenerating all possible two-syllable words...")
    two_syllable = generate_two_syllable_words()
    print(f"Total possible two-syllable words: {len(two_syllable):,}")
    
    print("\nFinding available two-syllable words...")
    available_two = [w for w in two_syllable if w not in existing_words]
    print(f"Available two-syllable words: {len(available_two):,}")
    
    # Show some examples
    print("\nFirst 50 available two-syllable words:")
    for i, word in enumerate(available_two[:50]):
        if i % 10 == 0:
            print()
        print(f"{word:8}", end="")
    print()
    
    # Save to file
    output_file = "available_two_syllable_words.txt"
    with open(output_file, 'w') as f:
        f.write(f"# Available Two-Syllable Phi Words\n")
        f.write(f"# Total: {len(available_two):,} words\n\n")
        for word in available_two:
            f.write(f"{word}\n")
    print(f"\nFull list saved to: {output_file}")
    
    # Also check three-syllable if requested
    check_three = input("\nCheck three-syllable words too? (y/n): ").strip().lower()
    if check_three == 'y':
        print("\nGenerating all possible three-syllable words...")
        three_syllable = generate_three_syllable_words()
        print(f"Total possible three-syllable words: {len(three_syllable):,}")
        
        print("\nFinding available three-syllable words...")
        available_three = [w for w in three_syllable if w not in existing_words]
        print(f"Available three-syllable words: {len(available_three):,}")
        
        # Show some examples
        print("\nFirst 50 available three-syllable words:")
        for i, word in enumerate(available_three[:50]):
            if i % 10 == 0:
                print()
            print(f"{word:10}", end="")
        print()
        
        # Save to file
        output_file_three = "available_three_syllable_words.txt"
        with open(output_file_three, 'w') as f:
            f.write(f"# Available Three-Syllable Phi Words\n")
            f.write(f"# Total: {len(available_three):,} words\n\n")
            for word in available_three:
                f.write(f"{word}\n")
        print(f"\nFull list saved to: {output_file_three}")

if __name__ == "__main__":
    main()