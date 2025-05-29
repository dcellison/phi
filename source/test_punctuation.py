#!/usr/bin/env python3
"""Test script for the punctuation validator."""

from phi_validation.core import PhiSentenceValidator

def test_punctuation():
    """Test the punctuation validator with various cases."""
    validator = PhiSentenceValidator()
    
    test_cases = [
        ("mia ta thilu.", True, "Valid sentence with period"),
        ("mia ta thilu", False, "Missing period"),
        ("wa mia ta thilu?", False, "Forbidden question mark"),
        ("mia, ta thilu.", False, "Forbidden comma"),
        ("mia ta thilu!", False, "Forbidden exclamation"),
        ('mia ta "thilu".', False, "Forbidden quotes"),
        ("mia  ta thilu.", False, "Double spaces"),
        (" mia ta thilu.", False, "Leading space"),
        ("mia ta thilu. ", False, "Trailing space"),
    ]
    
    print("🔍 TESTING PHI PUNCTUATION VALIDATOR")
    print("=" * 50)
    
    for sentence, expected_valid, description in test_cases:
        result = validator.validate_sentence(sentence)
        actual_valid = result['is_valid']
        status = "✅" if actual_valid == expected_valid else "❌"
        
        print(f"{status} {description}")
        print(f"   Sentence: '{sentence}'")
        print(f"   Expected: {'VALID' if expected_valid else 'INVALID'}")
        print(f"   Actual: {'VALID' if actual_valid else 'INVALID'}")
        
        if result['errors']:
            punctuation_errors = [e for e in result['errors'] if e.error_type.value == 'punctuation_error']
            if punctuation_errors:
                print(f"   Punctuation errors: {len(punctuation_errors)}")
                for error in punctuation_errors[:2]:  # Show first 2
                    print(f"     - {error.message}")
        print()

if __name__ == "__main__":
    test_punctuation() 