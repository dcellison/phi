#!/usr/bin/env python3
"""
Generate a validated list of phi nouns.
Only includes words that follow strict [C/F][V/P][F][P] pattern and use valid characters.
"""

import json
from collections import defaultdict
import sys
sys.path.append('.')
from phi_word_lookup import PhiWordDatabase

def analyze_word_pattern(word: str) -> tuple:
    """
    Analyze a phi word and return detailed pattern breakdown.
    Returns: (pattern, components, is_valid, issues)
    """
    pattern = ""
    components = []
    issues = []
    i = 0
    
    while i < len(word):
        # Check for fricative digraphs first
        if i < len(word) - 1:
            digraph = word[i:i+2]
            if digraph in ['ph', 'wh', 'th', 'sh']:
                pattern += 'F'
                components.append(('F', digraph))
                i += 2
                continue
        
        # Check for vowel pairs
        if i < len(word) - 1:
            char1, char2 = word[i], word[i+1]
            if char1 in 'aeiou' and char2 in 'aeiou' and char1 != char2:
                pattern += 'P'
                components.append(('P', char1 + char2))
                i += 2
                continue
        
        # Single character
        char = word[i]
        if char in 'aeiou':
            pattern += 'V'
            components.append(('V', char))
        elif char in 'hlmnprstw':  # ONLY valid phi consonants
            pattern += 'C'
            components.append(('C', char))
        else:
            pattern += '?'
            components.append(('?', char))
            issues.append(f"Invalid character: {char}")
        
        i += 1
    
    # Check if pattern matches [C/F][V/P][F][P]
    valid_patterns = ['CVFP', 'CPFP', 'FVFP', 'FPFP']
    is_valid = pattern in valid_patterns
    
    if not is_valid:
        issues.append(f"Invalid pattern {pattern}, expected one of: {', '.join(valid_patterns)}")
    
    # Additional validation
    if len(components) != 4:
        issues.append(f"Wrong component count: {len(components)}, expected exactly 4")
    
    return pattern, components, is_valid, issues

def main():
    # Initialize database
    db = PhiWordDatabase("../source/pos")
    db.build_database()
    
    # Extract and validate all nouns
    all_nouns = {word: info for word, info in db.word_db.items() if info['pos'] == 'noun'}
    
    print(f"🔍 Validating {len(all_nouns)} phi nouns...")
    print("=" * 50)
    
    # Validate each noun - only keep valid ones
    validated_words = []
    excluded_count = 0
    
    for word, info in all_nouns.items():
        pattern, components, is_valid, issues = analyze_word_pattern(word)
        
        if is_valid:
            validated_words.append(word)
        else:
            excluded_count += 1
    
    print(f"✅ Valid words: {len(validated_words)}")
    print(f"❌ Invalid words excluded: {excluded_count}")
    print("=" * 50)
    
    # Sort alphabetically
    validated_words.sort()
    
    # Organize by pattern for statistics
    by_pattern = defaultdict(list)
    for word in validated_words:
        pattern, _, _, _ = analyze_word_pattern(word)
        by_pattern[pattern].append(word)
    
    # Create simple validated list
    validated_list = {
        'total_count': len(validated_words),
        'excluded_count': excluded_count,
        'words': validated_words,
        'pattern_counts': {
            'CVFP': len(by_pattern['CVFP']),
            'CPFP': len(by_pattern['CPFP']), 
            'FVFP': len(by_pattern['FVFP']),
            'FPFP': len(by_pattern['FPFP'])
        }
    }
    
    # Save to JSON
    with open('validated_phi_words.json', 'w', encoding='utf-8') as f:
        json.dump(validated_list, f, indent=2, ensure_ascii=False)
    
    # Save simple word list
    with open('validated_phi_words.txt', 'w', encoding='utf-8') as f:
        f.write("# Validated Phi Words\n")
        f.write(f"# Total: {len(validated_words)} words\n\n")
        
        for word in validated_words:
            f.write(f"{word}\n")
    
    print("✅ Validated word list generated!")
    print("📁 Files created:")
    print("   - validated_phi_words.json (with counts)")
    print("   - validated_phi_words.txt (simple list)")
    print()
    
    # Summary
    print("📊 SUMMARY:")
    print(f"   Total validated: {len(validated_words)}")
    for pattern in ['CVFP', 'CPFP', 'FVFP', 'FPFP']:
        count = len(by_pattern[pattern])
        percentage = (count / len(validated_words)) * 100
        print(f"   {pattern}: {count} words ({percentage:.1f}%)")
    
    if excluded_count > 0:
        print(f"\n⚠️  {excluded_count} invalid words excluded")

if __name__ == "__main__":
    main() 