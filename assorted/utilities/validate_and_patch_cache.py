#!/usr/bin/env python3
"""
Validate and patch phi noun cache - ensure all words follow strict [C/F][V/P][F][P] pattern.
Identifies problematic words and suggests fixes.
"""

import json
import re
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
        elif char in 'hlmnprstw':
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

def validate_all_nouns():
    """Validate all nouns in the database."""
    print("Validating all phi nouns...")
    print("=" * 60)
    
    # Load the database
    db = PhiWordDatabase("../source/pos")
    db.build_database()
    
    # Extract all nouns
    nouns = {word: info for word, info in db.word_db.items() if info['pos'] == 'noun'}
    
    valid_words = []
    invalid_words = []
    pattern_issues = defaultdict(list)
    
    for word, info in nouns.items():
        pattern, components, is_valid, issues = analyze_word_pattern(word)
        
        word_data = {
            'word': word,
            'translation': info.get('translation', ''),
            'category': info.get('category', ''),
            'reported_pattern': info.get('pattern', ''),
            'actual_pattern': pattern,
            'components': components,
            'issues': issues
        }
        
        if is_valid:
            valid_words.append(word_data)
        else:
            invalid_words.append(word_data)
            pattern_issues[pattern].append(word_data)
    
    # Generate report
    print(f"📊 VALIDATION RESULTS:")
    print(f"   Total nouns: {len(nouns)}")
    print(f"   ✅ Valid: {len(valid_words)}")
    print(f"   ❌ Invalid: {len(invalid_words)}")
    print()
    
    if invalid_words:
        print("❌ INVALID WORDS FOUND:")
        print("-" * 40)
        for word_data in invalid_words:
            word = word_data['word']
            pattern = word_data['actual_pattern']
            issues = word_data['issues']
            components = word_data['components']
            
            print(f"  {word:12} | {pattern:8} | {word_data['translation']}")
            print(f"               Components: {components}")
            for issue in issues:
                print(f"               Issue: {issue}")
            print()
    
    # Pattern distribution for invalid words
    if pattern_issues:
        print("📊 INVALID PATTERN DISTRIBUTION:")
        print("-" * 40)
        for pattern, words in pattern_issues.items():
            print(f"  {pattern}: {len(words)} words")
            for word_data in words[:3]:  # Show first 3 examples
                print(f"    - {word_data['word']} ({word_data['translation']})")
            if len(words) > 3:
                print(f"    ... and {len(words) - 3} more")
            print()
    
    # Check for pattern mismatches (reported vs actual)
    print("🔍 PATTERN MISMATCHES (reported vs actual):")
    print("-" * 50)
    mismatches = []
    for word_data in valid_words + invalid_words:
        reported = word_data['reported_pattern']
        actual = word_data['actual_pattern']
        if reported != actual:
            mismatches.append(word_data)
    
    if mismatches:
        for word_data in mismatches:
            word = word_data['word']
            reported = word_data['reported_pattern']
            actual = word_data['actual_pattern']
            print(f"  {word:12} | Reported: {reported:8} | Actual: {actual:8}")
    else:
        print("  ✅ No pattern mismatches found!")
    
    print()
    
    # Save detailed report
    save_validation_report(valid_words, invalid_words, mismatches)
    
    return valid_words, invalid_words

def save_validation_report(valid_words, invalid_words, mismatches):
    """Save detailed validation report to files."""
    
    # JSON report
    report_data = {
        'summary': {
            'total_words': len(valid_words) + len(invalid_words),
            'valid_count': len(valid_words),
            'invalid_count': len(invalid_words),
            'mismatch_count': len(mismatches)
        },
        'valid_words': valid_words,
        'invalid_words': invalid_words,
        'pattern_mismatches': mismatches
    }
    
    with open('noun_validation_report.json', 'w', encoding='utf-8') as f:
        json.dump(report_data, f, indent=2, ensure_ascii=False)
    
    # Markdown report
    with open('noun_validation_report.md', 'w', encoding='utf-8') as f:
        f.write("# Phi Noun Validation Report\n\n")
        f.write(f"**Total words analyzed**: {len(valid_words) + len(invalid_words)}\n")
        f.write(f"**Valid words**: {len(valid_words)}\n")
        f.write(f"**Invalid words**: {len(invalid_words)}\n")
        f.write(f"**Pattern mismatches**: {len(mismatches)}\n\n")
        
        if invalid_words:
            f.write("## Invalid Words\n\n")
            f.write("| Word | Pattern | Translation | Issues |\n")
            f.write("|------|---------|-------------|--------|\n")
            for word_data in invalid_words:
                word = word_data['word']
                pattern = word_data['actual_pattern']
                translation = word_data['translation']
                issues = '; '.join(word_data['issues'])
                f.write(f"| {word} | {pattern} | {translation} | {issues} |\n")
            f.write("\n")
        
        if mismatches:
            f.write("## Pattern Mismatches\n\n")
            f.write("| Word | Reported | Actual | Translation |\n")
            f.write("|------|----------|--------|-------------|\n")
            for word_data in mismatches:
                word = word_data['word']
                reported = word_data['reported_pattern']
                actual = word_data['actual_pattern']
                translation = word_data['translation']
                f.write(f"| {word} | {reported} | {actual} | {translation} |\n")
            f.write("\n")
    
    print("📁 VALIDATION REPORTS SAVED:")
    print("   - noun_validation_report.json")
    print("   - noun_validation_report.md")

def suggest_fixes_for_invalid_words(invalid_words):
    """Suggest fixes for invalid words."""
    print("\n🔧 SUGGESTED FIXES:")
    print("-" * 40)
    
    for word_data in invalid_words:
        word = word_data['word']
        pattern = word_data['actual_pattern']
        components = word_data['components']
        translation = word_data['translation']
        
        print(f"\n{word} ({translation}):")
        print(f"  Current: {pattern} - {[comp[1] for comp in components]}")
        
        # Try to suggest a fix based on the pattern
        if len(components) > 4:
            print(f"  Issue: Too many components ({len(components)})")
            print(f"  Suggestion: Remove excess vowels/consonants to get exactly 4 components")
        elif len(components) < 4:
            print(f"  Issue: Too few components ({len(components)})")
            print(f"  Suggestion: Add missing fricative or vowel pair")
        else:
            print(f"  Issue: Wrong pattern sequence")
            print(f"  Suggestion: Rearrange to match [C/F][V/P][F][P]")

def main():
    print("🔍 PHI NOUN VALIDATION AND PATCHING UTILITY")
    print("=" * 60)
    
    # Run validation
    valid_words, invalid_words = validate_all_nouns()
    
    # Suggest fixes for invalid words
    if invalid_words:
        suggest_fixes_for_invalid_words(invalid_words)
    else:
        print("🎉 ALL NOUNS ARE VALID!")
    
    print("\n" + "=" * 60)
    print("Validation complete. Check the report files for details.")

if __name__ == "__main__":
    main() 