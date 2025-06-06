#!/usr/bin/env python3

import re

# Read the file and extract phi words
with open('source/pos/nouns-essential-objects.md', 'r') as f:
    content = f.read()

# Extract phi words from the table
phi_words = []
for line in content.split('\n'):
    if '|' in line and 'phi word' not in line and '----' not in line and line.strip().startswith('|'):
        parts = line.split('|')
        if len(parts) >= 3:  # Should have | word | translation |
            word = parts[1].strip()
            if word and word != 'phi word' and word != '':
                phi_words.append(word)

print(f'Found {len(phi_words)} phi words')

# Validate each word against [C/F][V/P][F][P] pattern
consonants = set('hlmnprstw')
fricatives = {'ph', 'wh', 'th', 'sh'}
vowels = set('iueoa')
vowel_pairs = {
    'ia', 'ie', 'io', 'iu', 'ua', 'ue', 'ui', 'uo',
    'ea', 'ei', 'eu', 'eo', 'oa', 'oi', 'ou', 'oe',
    'ae', 'ai', 'au', 'ao'
}

invalid_words = []

for word in phi_words:
    if not word:
        continue
        
    # Check if word follows [C/F][V/P][F][P] pattern
    i = 0
    components = []
    
    while i < len(word):
        # Check for fricative digraph first
        if i < len(word) - 1:
            digraph = word[i:i+2]
            if digraph in fricatives:
                components.append(('F', digraph))
                i += 2
                continue
        
        # Check for vowel pair
        if i < len(word) - 1:
            pair = word[i:i+2]
            if pair in vowel_pairs:
                components.append(('P', pair))
                i += 2
                continue
        
        # Single character
        char = word[i]
        if char in consonants:
            components.append(('C', char))
        elif char in vowels:
            components.append(('V', char))
        else:
            components.append(('?', char))
        i += 1
    
    # Check if pattern matches [C/F][V/P][F][P]
    pattern = ''.join([comp[0] for comp in components])
    valid_patterns = ['CVFP', 'CPFP', 'FVFP', 'FPFP']
    
    if pattern not in valid_patterns:
        invalid_words.append(f'{word}: {pattern} (components: {components})')

if invalid_words:
    print('\nInvalid words found:')
    for invalid in invalid_words:
        print(f'  {invalid}')
else:
    print('\nAll words are phonotactically valid!')

# Check for duplicates
word_counts = {}
for word in phi_words:
    word_counts[word] = word_counts.get(word, 0) + 1

duplicates = {word: count for word, count in word_counts.items() if count > 1}
if duplicates:
    print('\nDuplicate words found:')
    for word, count in duplicates.items():
        print(f'  {word}: appears {count} times')
else:
    print('\nNo duplicate words found!')

print(f'\nTotal valid unique words: {len(set(phi_words))}') 