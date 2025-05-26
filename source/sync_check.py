#!/usr/bin/env python3

import re
import os

def extract_lookup_phi_words():
    """Extract phi words from phi-lookup-tools.md (phi → english section only)"""
    lookup_words = set()
    with open('phi-lookup-tools.md', 'r') as f:
        content = f.read()
    
    # Find the phi → english section
    lines = content.split('\n')
    in_phi_section = False
    
    for line in lines:
        if '## 1. phi → english lookup' in line:
            in_phi_section = True
            continue
        elif '## 2. english → phi lookup' in line:
            in_phi_section = False
            continue
        
        if in_phi_section and '|' in line and not line.startswith('#') and 'phi word' not in line and '---' not in line:
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 2 and parts[1] and not parts[1].startswith('*') and not parts[1].startswith('['):
                # Filter out pattern examples and English words
                word = parts[1]
                if not any(char in word for char in ['[', ']', ' ', 'begin', 'with']):
                    lookup_words.add(word)
    
    return lookup_words

def extract_pos_phi_words():
    """Extract phi words from all POS files"""
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
            
            lines = content.split('\n')
            in_phi_table = False
            
            for line in lines:
                # Check if we're entering a phi word table
                if '| phi word | english translation |' in line:
                    in_phi_table = True
                    continue
                
                # Check if we're leaving the table (empty line or new section)
                if in_phi_table and (not line.strip() or line.startswith('#') or (line.startswith('|') and '---' in line)):
                    if not line.strip() or line.startswith('#'):
                        in_phi_table = False
                    continue
                
                # Extract entries within phi word tables
                if in_phi_table and line.startswith('| '):
                    parts = [p.strip() for p in line.split('|')]
                    if len(parts) >= 3:
                        phi_word = parts[1].strip()
                        english_meaning = parts[2].strip()
                        
                        if phi_word and english_meaning:
                            file_words.add(phi_word)
                            all_pos_words.add(phi_word)
            
            pos_words[pos_file] = file_words
            print(f"{pos_file}: {len(file_words)} phi words")
    
    return all_pos_words, pos_words

def main():
    lookup_words = extract_lookup_phi_words()
    all_pos_words, pos_by_file = extract_pos_phi_words()
    
    missing_from_lookup = all_pos_words - lookup_words
    extra_in_lookup = lookup_words - all_pos_words
    
    print(f"\nSummary:")
    print(f"Phi words in POS files: {len(all_pos_words)}")
    print(f"Phi words in lookup: {len(lookup_words)}")
    print(f"Missing from lookup: {len(missing_from_lookup)}")
    print(f"Extra in lookup: {len(extra_in_lookup)}")
    
    if missing_from_lookup:
        print(f"\nWords missing from lookup (first 30):")
        for word in sorted(list(missing_from_lookup))[:30]:
            print(f"  {word}")
    
    if extra_in_lookup:
        print(f"\nExtra words in lookup (first 30):")
        for word in sorted(list(extra_in_lookup))[:30]:
            print(f"  {word}")

if __name__ == "__main__":
    main() 