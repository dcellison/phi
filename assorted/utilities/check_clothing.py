#!/usr/bin/env python3

def analyze_pattern(word):
    pattern = ''
    i = 0
    while i < len(word):
        # Check for digraphs first
        if i < len(word) - 1:
            digraph = word[i:i+2]
            if digraph in ['ph', 'wh', 'th', 'sh']:
                pattern += 'F'
                i += 2
                continue
        # Check for vowel pairs
        if i < len(word) - 1:
            char1, char2 = word[i], word[i+1]
            if char1 in 'aeiou' and char2 in 'aeiou' and char1 != char2:
                pattern += 'P'
                i += 2
                continue
        # Single character
        char = word[i]
        if char in 'aeiou':
            pattern += 'V'
        elif char in 'hlmnprstw':
            pattern += 'C'
        i += 1
    return pattern

# Our corrected clothing words
words = [
    'mathuo', 'loushae', 'whitheo', 'thauphie', 'neshui', 
    'saipheo', 'whothae', 'phieshou', 'rithau', 'tuashoe', 
    'thuphai', 'sheowhui', 'pothae', 'miewhau', 'whasheo', 
    'thoaphue', 'leshai', 'naothue'
]

print("CORRECTED Clothing Word Pattern Analysis")
print("=" * 55)
print("Expected: [C/F][V/P][F][P] -> CVFP, CPFP, FVFP, or FPFP")
print()

valid_patterns = ['CVFP', 'CPFP', 'FVFP', 'FPFP']

for word in words:
    pattern = analyze_pattern(word)
    valid = pattern in valid_patterns
    status = "✓ VALID" if valid else "✗ INVALID"
    print(f"{word:10} -> {pattern:6} -> {status}")

print()
print("KEY CHANGES:")
print("- whithoa -> whitheo (avoid duplicate with 'dog')")
print("- thauphi -> thauphie (fix FPFV -> FPFP pattern)") 