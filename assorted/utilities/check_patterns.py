#!/usr/bin/env python3

def analyze_pattern(word):
    pattern = ''
    i = 0
    while i < len(word):
        if i < len(word) - 1 and word[i:i+2] in ['ph', 'wh', 'th', 'sh']:
            pattern += 'F'
            i += 2
        elif i < len(word) - 1 and word[i] in 'aeiou' and word[i+1] in 'aeiou' and word[i] != word[i+1]:
            pattern += 'P'
            i += 2
        elif word[i] in 'aeiou':
            pattern += 'V'
            i += 1
        elif word[i] in 'hlmnprstw':
            pattern += 'C'
            i += 1
        else:
            pattern += '?'
            i += 1
    return pattern

# Sample of new words to check
test_words = [
    'mouthae', 'whishoa', 'thauphie', 'raishow', 'seuphau', 
    'niotheai', 'pauthie', 'wheoshaw', 'thuiphae', 'maishuo',
    'rhauphei', 'phaiewho', 'whiophai', 'leishuth'
]

print("Pattern validation for new phi words:")
print("=" * 40)

for word in test_words:
    pattern = analyze_pattern(word)
    valid = pattern in ['CVFP', 'CPFP', 'FVFP', 'FPFP']
    status = "✓" if valid else "✗"
    print(f"{word:12} -> {pattern:6} -> {status}")

print("\nValid patterns: CVFP, CPFP, FVFP, FPFP") 