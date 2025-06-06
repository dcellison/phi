#!/usr/bin/env python3
"""
Validate all newly generated phi words to ensure they follow strict patterns.
"""

import json

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
    print("🔍 Validating All Newly Generated Phi Words")
    print("=" * 60)
    
    # Load the new words
    try:
        with open('pattern_balance_words.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            new_words_by_pattern = data['new_words_by_pattern']
    except FileNotFoundError:
        print("❌ pattern_balance_words.json not found. Run balance_patterns.py first.")
        return
    
    # Collect all new words
    all_new_words = []
    for pattern, words in new_words_by_pattern.items():
        all_new_words.extend(words)
    
    print(f"📊 Validating {len(all_new_words)} newly generated words...")
    print()
    
    # Validate each word
    valid_count = 0
    invalid_count = 0
    pattern_counts = {'CVFP': 0, 'CPFP': 0, 'FVFP': 0, 'FPFP': 0}
    invalid_words = []
    
    for word in all_new_words:
        pattern, components, is_valid, issues = analyze_word_pattern(word)
        
        if is_valid:
            valid_count += 1
            pattern_counts[pattern] += 1
        else:
            invalid_count += 1
            invalid_words.append({
                'word': word,
                'pattern': pattern,
                'issues': issues
            })
    
    # Report results
    print("✅ VALIDATION RESULTS:")
    print(f"   Valid words: {valid_count}")
    print(f"   Invalid words: {invalid_count}")
    
    if invalid_count == 0:
        print("\n🎉 ALL NEWLY GENERATED WORDS ARE VALID!")
    else:
        print(f"\n❌ FOUND {invalid_count} INVALID WORDS:")
        for invalid in invalid_words:
            print(f"   {invalid['word']:12} | {invalid['pattern']:8} | {'; '.join(invalid['issues'])}")
    
    print("\n📊 PATTERN DISTRIBUTION OF NEW WORDS:")
    for pattern, count in pattern_counts.items():
        expected = len(new_words_by_pattern.get(pattern, []))
        match_status = "✅" if count == expected else "❌"
        print(f"   {pattern}: {count:3d} words (expected: {expected:3d}) {match_status}")
    
    # Verify against intended pattern distribution
    print("\n🔍 PATTERN VERIFICATION:")
    for pattern, expected_words in new_words_by_pattern.items():
        if not expected_words:
            continue
            
        actual_pattern_words = [w for w in expected_words if analyze_word_pattern(w)[2]]
        expected_count = len(expected_words)
        actual_count = len(actual_pattern_words)
        
        if actual_count == expected_count:
            print(f"   {pattern}: ✅ All {actual_count} words valid")
        else:
            print(f"   {pattern}: ❌ {actual_count}/{expected_count} words valid")
    
    # Sample validation details
    print("\n🔍 SAMPLE VALIDATION DETAILS:")
    for pattern in ['CVFP', 'CPFP', 'FVFP', 'FPFP']:
        words = new_words_by_pattern.get(pattern, [])
        if words:
            sample_word = words[0]
            pattern_result, components, is_valid, issues = analyze_word_pattern(sample_word)
            component_str = ' + '.join([f"{comp[0]}({comp[1]})" for comp in components])
            status = "✅" if is_valid else "❌"
            print(f"   {pattern}: {sample_word} = {component_str} {status}")

if __name__ == "__main__":
    main() 