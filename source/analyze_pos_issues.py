#!/usr/bin/env python3

import re
import os
from collections import defaultdict

def analyze_pos_files():
    """Analyze POS files for various types of invalid entries in proper phi word tables"""
    pos_files = [
        'pos/nouns.md', 'pos/verbs.md', 'pos/adjectives.md', 'pos/adverbs.md',
        'pos/particles.md', 'pos/determiners.md', 'pos/pronouns.md', 
        'pos/prepositions.md', 'pos/conjunctions.md', 'pos/interjections.md',
        'pos/classifiers.md', 'pos/numbers.md'
    ]
    
    issues = defaultdict(list)
    
    for pos_file in pos_files:
        if os.path.exists(pos_file):
            with open(pos_file, 'r') as f:
                content = f.read()
            
            lines = content.split('\n')
            in_phi_table = False
            line_num = 0
            
            for line in lines:
                line_num += 1
                
                # Check if we're entering a phi word table
                if '| phi word | english translation |' in line:
                    in_phi_table = True
                    continue
                
                # Check if we're leaving the table (empty line or new section)
                if in_phi_table and (not line.strip() or line.startswith('#') or (line.startswith('|') and '---' in line)):
                    if not line.strip() or line.startswith('#'):
                        in_phi_table = False
                    continue
                
                # Analyze entries within phi word tables
                if in_phi_table and line.startswith('| '):
                    parts = [p.strip() for p in line.split('|')]
                    if len(parts) >= 3:
                        phi_word = parts[1].strip()
                        english_meaning = parts[2].strip()
                        
                        # Skip empty entries
                        if not phi_word or not english_meaning:
                            continue
                            
                        # Categorize different types of issues
                        
                        # English phrases/sentences
                        if ' ' in phi_word and any(word in phi_word.lower() for word in ['tree', 'flower', 'ball', 'cup', 'bag', 'basket', 'bread', 'butter']):
                            issues['english_phrases'].append(f"{pos_file}:{line_num} - '{phi_word}'")
                        
                        # Example sentences (contain particles like 'li', 'lo', 'ma', 'mia')
                        elif ' ' in phi_word and any(phi_word.startswith(particle + ' ') for particle in ['li ', 'lo ', 'ma ', 'mia ', 'na ']):
                            issues['example_sentences'].append(f"{pos_file}:{line_num} - '{phi_word}'")
                        
                        # English words
                        elif phi_word.lower() in ['english', 'form', 'function', 'object', 'gloss', 'example']:
                            issues['english_words'].append(f"{pos_file}:{line_num} - '{phi_word}'")
                        
                        # Multi-word phi phrases (might be valid compounds)
                        elif ' ' in phi_word and not any(char in phi_word for char in ['/', '(', ')']):
                            # Check if it's a valid phi compound
                            words = phi_word.split()
                            if all(is_likely_phi_word(word) for word in words):
                                issues['phi_compounds'].append(f"{pos_file}:{line_num} - '{phi_word}' (might be valid)")
                            else:
                                issues['invalid_phrases'].append(f"{pos_file}:{line_num} - '{phi_word}'")
                        
                        # Words with slashes (alternatives)
                        elif '/' in phi_word:
                            issues['alternatives'].append(f"{pos_file}:{line_num} - '{phi_word}'")
                        
                        # Very long words (>8 chars, unusual for phi)
                        elif len(phi_word) > 8 and ' ' not in phi_word:
                            issues['long_words'].append(f"{pos_file}:{line_num} - '{phi_word}' ({len(phi_word)} chars)")
                        
                        # Words with non-phi characters
                        elif not is_likely_phi_word(phi_word):
                            issues['non_phi_chars'].append(f"{pos_file}:{line_num} - '{phi_word}'")
    
    return issues

def is_likely_phi_word(word):
    """Check if a word looks like it could be a phi word"""
    if not word:
        return False
    
    # Basic phi character set
    consonants = set('hlmnprstw')
    vowels = set('iueoa')
    valid_chars = consonants | vowels
    
    # Must contain only valid phi characters
    if not all(c in valid_chars for c in word.lower()):
        return False
    
    # Must contain at least one vowel
    if not any(c in vowels for c in word.lower()):
        return False
    
    return True

def main():
    print("Analyzing POS files for issues in phi word tables...")
    issues = analyze_pos_files()
    
    if not any(issues.values()):
        print("✅ No issues found in POS files!")
        return
    
    print(f"\nFound {sum(len(v) for v in issues.values())} total issues:\n")
    
    for category, items in issues.items():
        if items:
            print(f"📋 {category.replace('_', ' ').title()} ({len(items)} items):")
            for item in items[:10]:  # Show first 10 of each type
                print(f"   {item}")
            if len(items) > 10:
                print(f"   ... and {len(items) - 10} more")
            print()

if __name__ == "__main__":
    main() 