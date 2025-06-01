#!/usr/bin/env python3

# Debug script to isolate digit validation issue

fricatives = {"ph", "wh", "th", "sh"}
vowels = set("iueoa")

def debug_digit_validation(word):
    print(f"\n=== Debugging: {word} ===")
    
    # Check basic conditions
    print(f"Length: {len(word)}")
    print(f"First two chars: '{word[:2]}'")
    print(f"Third char: '{word[2]}'")
    print(f"Fricative check: {word[:2] in fricatives}")
    print(f"Vowel check: {word[2] in vowels}")
    
    # Test digit pattern [F][V]
    digit_valid = len(word) == 3 and word[:2] in fricatives and word[2] in vowels
    print(f"Digit pattern valid: {digit_valid}")
    
    # Simulate the validator logic
    digit_errors = []
    magnitude_errors = []
    main_errors = []
    
    # Try digit pattern [F][V]
    if len(word) == 3 and word[:2] in fricatives and word[2] in vowels:
        print("✓ Digit pattern: PASS")
    else:
        digit_errors.append("Does not match digit pattern [F][V]")
        print("✗ Digit pattern: FAIL")
    
    # Try magnitude pattern [F][V][F][V]
    if (len(word) == 6 and 
        word[:2] in fricatives and 
        word[2] in vowels and
        word[3:5] in fricatives and
        word[5] in vowels):
        print("✓ Magnitude pattern: PASS")
    else:
        magnitude_errors.append("Does not match magnitude pattern [F][V][F][V]")
        print("✗ Magnitude pattern: FAIL")
    
    # Check final logic
    print(f"digit_errors: {digit_errors}")
    print(f"magnitude_errors: {magnitude_errors}")
    print(f"Condition (digit_errors and magnitude_errors): {bool(digit_errors and magnitude_errors)}")
    
    if digit_errors and magnitude_errors:
        main_errors.append("Number does not match digit [F][V] or magnitude [F][V][F][V] patterns")
        print("✗ FINAL RESULT: INVALID")
    else:
        print("✓ FINAL RESULT: VALID")
    
    return len(main_errors) == 0

# Test cases
test_words = ["phi", "sho", "thu", "whu", "pho", "the"]

for word in test_words:
    is_valid = debug_digit_validation(word)
    print(f"Final validation result: {'VALID' if is_valid else 'INVALID'}")
    print("-" * 40) 