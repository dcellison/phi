#!/usr/bin/env python3
"""
Calculate the theoretical noun space for phi nouns.
Pattern: [C/F][V/P][F][P]
"""

# Phi phoneme inventory
consonants = ['h', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w']  # 9 consonants
fricative_digraphs = ['ph', 'wh', 'th', 'sh']  # 4 fricative digraphs
vowels = ['i', 'u', 'e', 'o', 'a']  # 5 vowels

# Generate all vowel pairs (two different vowels)
vowel_pairs = []
for v1 in vowels:
    for v2 in vowels:
        if v1 != v2:  # Must be different vowels
            vowel_pairs.append(v1 + v2)

print("=== PHI NOUN SPACE CALCULATION ===")
print()
print("Components:")
print(f"Consonants (C): {consonants} = {len(consonants)} options")
print(f"Fricative digraphs (F): {fricative_digraphs} = {len(fricative_digraphs)} options")
print(f"Vowels (V): {vowels} = {len(vowels)} options")
print(f"Vowel pairs (P): {vowel_pairs} = {len(vowel_pairs)} options")
print()

# Calculate theoretical noun space
# Pattern: [C/F][V/P][F][P]
pos1_options = len(consonants) + len(fricative_digraphs)  # [C/F]
pos2_options = len(vowels) + len(vowel_pairs)  # [V/P]
pos3_options = len(fricative_digraphs)  # [F]
pos4_options = len(vowel_pairs)  # [P]

print("Pattern: [C/F][V/P][F][P]")
print(f"Position 1 [C/F]: {pos1_options} options ({len(consonants)} C + {len(fricative_digraphs)} F)")
print(f"Position 2 [V/P]: {pos2_options} options ({len(vowels)} V + {len(vowel_pairs)} P)")
print(f"Position 3 [F]: {pos3_options} options")
print(f"Position 4 [P]: {pos4_options} options")
print()

total_theoretical = pos1_options * pos2_options * pos3_options * pos4_options
print(f"Total theoretical combinations: {pos1_options} × {pos2_options} × {pos3_options} × {pos4_options} = {total_theoretical:,}")
print()

# Load current noun count
import json
import sys
from pathlib import Path

try:
    with open('phi_words.json', 'r') as f:
        data = json.load(f)
    
    noun_count = sum(1 for word_info in data.values() if word_info.get('pos') == 'noun')
    
    print(f"Current nouns in use: {noun_count}")
    print(f"Remaining noun space: {total_theoretical - noun_count:,}")
    print(f"Percentage used: {(noun_count / total_theoretical) * 100:.3f}%")
    print()
    
    if noun_count / total_theoretical > 0.1:  # More than 10% used
        print("⚠️  WARNING: Using significant portion of noun space!")
    elif noun_count / total_theoretical > 0.05:  # More than 5% used
        print("📊 NOTICE: Notable usage of noun space")
    else:
        print("✅ SAFE: Very low usage of noun space")
        
except FileNotFoundError:
    print("📄 Note: phi_words.json not found, showing theoretical calculation only")
except Exception as e:
    print(f"Error reading database: {e}")

print()
print("=== ACTUAL NOUN EXAMPLES ===")
print("Verifying pattern understanding:")

# Show some example nouns to verify pattern
example_nouns = [
    ('whiphoa', 'eye', 'wh + i + ph + oa'),
    ('thephoa', 'person', 'th + e + ph + oa'),  
    ('whethea', 'book', 'wh + e + th + ea'),
    ('hiwhea', 'house', 'h + i + wh + ea'),
    ('miwhai', 'hair', 'm + i + wh + ai')
]

for word, meaning, breakdown in example_nouns:
    print(f"  {word} ({meaning}): {breakdown}") 