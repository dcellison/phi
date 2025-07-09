#!/usr/bin/env python3
import re

# Test the extraction logic
with open('../source/pos/nouns/objects.md', 'r') as f:
    content = f.read()

lines = content.split('\n')
print('Debugging word extraction from objects.md')
print('=' * 50)

found_clothing_table = False
extracted_words = []

i = 0
while i < len(lines):
    line = lines[i].strip()
    
    # Look for table header
    if line.startswith('| phi word |') and 'english translation' in line:
        print(f"Found table header at line {i+1}: {line}")
        
        # Skip header and separator
        i += 1
        if i < len(lines) and '---' in lines[i]:
            print(f"Skipping separator at line {i+1}: {lines[i].strip()}")
            i += 1
        
        # Extract words from table
        table_words = []
        while i < len(lines):
            line = lines[i].strip()
            
            if not line.startswith('|') or '---' in line or not line:
                print(f"End of table at line {i+1}")
                break
                
            # Test regex match
            match = re.match(r'\|\s*([a-z]{2,})\s*\|\s*([^|]+?)\s*\|', line)
            if match:
                phi_word = match.group(1).strip()
                translation = match.group(2).strip()
                table_words.append((phi_word, translation))
                print(f"  Extracted: {phi_word} -> {translation}")
            else:
                print(f"  No match: {line}")
            
            i += 1
            
        if table_words:
            extracted_words.extend(table_words)
            print(f"Table complete: {len(table_words)} words extracted")
        print()
    else:
        i += 1

print(f"Total words extracted: {len(extracted_words)}")
print("Words found:", [word for word, translation in extracted_words]) 