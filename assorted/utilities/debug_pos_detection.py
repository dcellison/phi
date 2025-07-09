#!/usr/bin/env python3

# Debug POS detection for comprehensive validation
import sys
sys.path.append('.')
from phi_word_lookup import PhiWordDatabase

# Create database instance
db = PhiWordDatabase("../source/pos")

# Test the _extract_lexicon_words method directly
with open('../source/pos/nouns/objects-overhaul.md', 'r') as f:
    content = f.read()

print("Testing POS detection for objects-overhaul.md")
print("=" * 50)

# Extract words using the same method as comprehensive validation
words = db._extract_lexicon_words(content)

print(f"Found {len(words)} words:")
for word, pos in words:
    print(f"  {word} -> POS: {pos}")

print("\nDebugging POS detection logic...")
print("-" * 30)

# Test the filename matching logic
lines = content.split('\n')
first_lines = '\n'.join(lines[:5]).lower()
print(f"First 5 lines:\n{first_lines}")

# Test against pos_files mapping
print(f"\npos_files mapping:")
for filename, pos in db.pos_files.items():
    print(f"  {filename} -> {pos}")
    pos_name = filename.replace('.md', '')
    if first_lines.startswith(f'# {pos_name}'):
        print(f"    MATCH: {pos_name}") 