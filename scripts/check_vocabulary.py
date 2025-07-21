#!/usr/bin/env python3
"""
Phi Vocabulary Checker
Helps prevent duplicate words when creating new vocabulary
"""

import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple

def load_all_words(words_dir: Path) -> Dict[str, List[str]]:
    """Load all existing Phi words from the vocabulary."""
    words = {}
    
    for category_dir in words_dir.iterdir():
        if category_dir.is_dir() and not category_dir.name.startswith('.'):
            for json_file in category_dir.glob('*.json'):
                if json_file.name not in ['SUMMARY.md', 'community-and-relationships.md']:
                    try:
                        with open(json_file, 'r', encoding='utf-8') as f:
                            data = json.load(f)
                            if isinstance(data, list) and len(data) > 0:
                                word_data = data[0]
                                phi_word = word_data.get('word', '')
                                gloss = word_data.get('gloss', json_file.stem)
                                
                                if phi_word not in words:
                                    words[phi_word] = []
                                words[phi_word].append(f"{gloss} ({category_dir.name})")
                    except Exception as e:
                        print(f"Error reading {json_file}: {e}")
    
    return words

def check_word(word: str, existing_words: Dict[str, List[str]]) -> bool:
    """Check if a word already exists in the vocabulary."""
    if word in existing_words:
        print(f"\n❌ DUPLICATE FOUND: '{word}' already exists as:")
        for usage in existing_words[word]:
            print(f"   - {usage}")
        return True
    return False

def find_similar_words(word: str, existing_words: Dict[str, List[str]], threshold: int = 1) -> List[Tuple[str, List[str]]]:
    """Find words that are similar (differ by only one character)."""
    similar = []
    for existing_word in existing_words:
        if abs(len(word) - len(existing_word)) <= 1:
            # Check for one character difference
            if len(word) == len(existing_word):
                diff_count = sum(1 for a, b in zip(word, existing_word) if a != b)
                if diff_count == threshold:
                    similar.append((existing_word, existing_words[existing_word]))
            # Check for one character insertion/deletion
            elif len(word) == len(existing_word) + 1:
                # Check if word contains existing_word
                for i in range(len(word)):
                    if word[:i] + word[i+1:] == existing_word:
                        similar.append((existing_word, existing_words[existing_word]))
                        break
            elif len(existing_word) == len(word) + 1:
                # Check if existing_word contains word
                for i in range(len(existing_word)):
                    if existing_word[:i] + existing_word[i+1:] == word:
                        similar.append((existing_word, existing_words[existing_word]))
                        break
    
    return similar

def interactive_mode(words_dir: Path):
    """Interactive mode for checking words."""
    existing_words = load_all_words(words_dir)
    print(f"\n📚 Loaded {len(existing_words)} unique Phi words from vocabulary\n")
    
    while True:
        word = input("Enter a Phi word to check (or 'quit' to exit): ").strip().lower()
        
        if word == 'quit':
            break
        
        if not word:
            continue
        
        # Check for exact duplicate
        is_duplicate = check_word(word, existing_words)
        
        # Check for similar words
        similar = find_similar_words(word, existing_words)
        if similar:
            print(f"\n⚠️  SIMILAR WORDS FOUND (differ by 1 character):")
            for sim_word, usages in similar:
                print(f"   '{sim_word}':")
                for usage in usages:
                    print(f"      - {usage}")
        
        if not is_duplicate and not similar:
            print(f"\n✅ '{word}' is available - no duplicates or similar words found!")
        
        print()

def batch_check(words_dir: Path, words_file: Path):
    """Check a batch of words from a file."""
    existing_words = load_all_words(words_dir)
    print(f"\n📚 Loaded {len(existing_words)} unique Phi words from vocabulary\n")
    
    with open(words_file, 'r') as f:
        words_to_check = [line.strip().lower() for line in f if line.strip()]
    
    duplicates = []
    available = []
    
    for word in words_to_check:
        if check_word(word, existing_words):
            duplicates.append(word)
        else:
            similar = find_similar_words(word, existing_words)
            if similar:
                print(f"\n⚠️  '{word}' has similar words:")
                for sim_word, usages in similar:
                    print(f"   '{sim_word}': {', '.join(usages)}")
            available.append(word)
    
    print(f"\n📊 Summary:")
    print(f"   - Checked: {len(words_to_check)} words")
    print(f"   - Duplicates: {len(duplicates)}")
    print(f"   - Available: {len(available)}")

def list_all_words(words_dir: Path):
    """List all words in the vocabulary, sorted alphabetically."""
    existing_words = load_all_words(words_dir)
    
    print(f"\n📚 All {len(existing_words)} Phi words in vocabulary:\n")
    
    for word in sorted(existing_words.keys()):
        glosses = ', '.join(existing_words[word])
        print(f"{word:15} - {glosses}")

def main():
    # Default words directory
    words_dir = Path(__file__).parent.parent / "words"
    
    if not words_dir.exists():
        print(f"❌ Words directory not found: {words_dir}")
        sys.exit(1)
    
    if len(sys.argv) > 1:
        if sys.argv[1] == '--list':
            list_all_words(words_dir)
        elif sys.argv[1] == '--batch' and len(sys.argv) > 2:
            batch_file = Path(sys.argv[2])
            if batch_file.exists():
                batch_check(words_dir, batch_file)
            else:
                print(f"❌ Batch file not found: {batch_file}")
                sys.exit(1)
        else:
            print("Usage:")
            print("  python check_vocabulary.py          # Interactive mode")
            print("  python check_vocabulary.py --list   # List all words")
            print("  python check_vocabulary.py --batch <file>  # Check words from file")
    else:
        interactive_mode(words_dir)

if __name__ == "__main__":
    main()