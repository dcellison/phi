#!/usr/bin/env python3

import re
import os

def extract_lookup_words():
    """Extract words from phi-lookup-tools.md"""
    lookup_words = set()
    with open('phi-lookup-tools.md', 'r') as f:
        content = f.read()
    
    for line in content.split('\n'):
        if '|' in line and not line.startswith('#') and 'phi word' not in line and '---' not in line:
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 2 and parts[1] and not parts[1].startswith('*'):
                lookup_words.add(parts[1])
    
    return lookup_words

def extract_pos_words():
    """Extract words from all POS files"""
    pos_words = {}
    pos_files = [
        'pos/nouns.md', 'pos/verbs.md', 'pos/adjectives.md', 'pos/adverbs.md',
        'pos/particles.md', 'pos/determiners.md', 'pos/pronouns.md', 
        'pos/prepositions.md', 'pos/conjunctions.md', 'pos/interjections.md',
        'pos/classifiers.md', 'pos/numbers.md'
    ]
    
    all_pos_words = set()
    
    for pos_file in pos_files:
        if os.path.exists(pos_file):
            file_words = set()
            with open(pos_file, 'r') as f:
                content = f.read()
            
            for line in content.split('\n'):
                if line.startswith('| ') and 'phi word' not in line and '---' not in line:
                    parts = [p.strip() for p in line.split('|')]
                    if len(parts) >= 2 and parts[1]:
                        file_words.add(parts[1])
                        all_pos_words.add(parts[1])
            
            pos_words[pos_file] = file_words
    
    return all_pos_words, pos_words

def main():
    lookup_words = extract_lookup_words()
    all_pos_words, pos_by_file = extract_pos_words()
    
    missing_from_lookup = all_pos_words - lookup_words
    extra_in_lookup = lookup_words - all_pos_words
    
    print(f"Words in POS files: {len(all_pos_words)}")
    print(f"Words in lookup: {len(lookup_words)}")
    print(f"Missing from lookup: {len(missing_from_lookup)}")
    print(f"Extra in lookup: {len(extra_in_lookup)}")
    
    if missing_from_lookup:
        print(f"\nFirst 20 words missing from lookup:")
        for word in sorted(list(missing_from_lookup))[:20]:
            print(f"  {word}")
    
    if extra_in_lookup:
        print(f"\nFirst 20 extra words in lookup:")
        for word in sorted(list(extra_in_lookup))[:20]:
            print(f"  {word}")

if __name__ == "__main__":
    main() 