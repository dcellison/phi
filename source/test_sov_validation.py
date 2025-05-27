#!/usr/bin/env python3
"""
Test SOV validation functionality.
"""

from phi_validation import PhiSentenceValidator

def test_sov_validation():
    """Test SOV word order validation."""
    print("Testing SOV validation...")
    
    validator = PhiSentenceValidator()
    
    test_cases = [
        # Valid SOV sentences
        ("mia ta thihi", "Valid: I am"),
        ("mia nuthui ta shata", "Valid: I throw stone (shata=throw)"),
        
        # Invalid SOV sentences  
        ("thihi ta mia", "Invalid: verb before subject"),
        ("shata ta mia", "Invalid: verb before subject"),
        
        # Missing verb
        ("mia nuthui", "Invalid: missing verb"),
        
        # Multiple verbs
        ("mia thihi shata", "Invalid: multiple verbs"),
    ]
    
    for sentence, description in test_cases:
        print(f"\nTesting: '{sentence}' - {description}")
        result = validator.validate_sentence(sentence)
        
        print(f"Valid: {result['is_valid']}")
        if result['errors']:
            for error in result['errors']:
                if error.error_type.value in ['word_order', 'missing_verb', 'multiple_verbs']:
                    print(f"  SOV Error: {error.message}")
                elif error.error_type.value == 'unknown_word':
                    print(f"  Lexicon Error: {error.message}")
        print("-" * 50)

if __name__ == "__main__":
    test_sov_validation() 