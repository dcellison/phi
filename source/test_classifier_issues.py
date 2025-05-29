#!/usr/bin/env python3
"""
Test Classifier Validation Issues

Debug the specific classifier issues that are not being caught.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from phi_validation.core import PhiSentenceValidator

def test_classifier_issues():
    """Test the specific classifier issues from the exercise validator."""
    print("Testing Classifier Validation Issues")
    print("=" * 40)
    
    validator = PhiSentenceValidator()
    
    # The specific failing test cases from the exercise validator
    test_cases = [
        # These should be INVALID but are being accepted as VALID
        ("mia na moi moi whethea ta whupi", "double classifier moi moi", False),
        ("thi na lea moi whethea ta whupi", "conflicting classifiers lea moi", False), 
        ("sha na teo lathia ta shero", "wrong classifier teo (round) for lathia (axe)", False),
        ("he thephoa na moi mophui ta whuwa", "wrong classifier moi (flat) for mophui (ball)", False),
        ("pi mathai na lea tuphai ta shire", "wrong classifier lea (long) for tuphai (cup)", False),
        ("mia na lea ta whona", "classifier lea without noun", False),
        
        # These should be VALID (control cases)
        ("mia na lea liphai ta whona", "correct: long classifier with tree", True),
        ("thi na moi whethea ta whupi", "correct: flat classifier with book", True),
        ("sha na teo mophui ta whuwa", "correct: round classifier with ball", True),
        ("thi na whethea ta whupi", "no classifier (optional)", True),
    ]
    
    for sentence, description, expected_valid in test_cases:
        print(f"\n🧪 Testing: '{sentence}'")
        print(f"   Description: {description}")
        print(f"   Expected: {'VALID' if expected_valid else 'INVALID'}")
        
        result = validator.validate_sentence(sentence)
        actual_valid = result['is_valid']
        
        print(f"   Got: {'VALID' if actual_valid else 'INVALID'}")
        
        if actual_valid == expected_valid:
            print(f"   ✅ CORRECT")
        else:
            print(f"   ❌ MISMATCH!")
            
        # Show any errors found
        if result['errors']:
            print("   Errors found:")
            for error in result['errors']:
                print(f"     • {error.error_type.value}: {error.message}")
        else:
            print("   No errors found")

if __name__ == "__main__":
    test_classifier_issues() 