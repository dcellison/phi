#!/usr/bin/env python3
"""
Test Classifier Semantic Compatibility Fix

Test that semantic classifier compatibility validation now works.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from phi_validation.core import PhiSentenceValidator

def test_classifier_semantic_fix():
    """Test the semantic classifier compatibility fix."""
    print("Testing Classifier Semantic Compatibility Fix")
    print("=" * 50)
    
    validator = PhiSentenceValidator()
    
    # Focus on the semantic compatibility cases that were still failing
    test_cases = [
        # INVALID: Wrong semantic compatibility (should now be caught)
        ("sha na teo lathia ta shero", "wrong: round classifier with axe", False),
        ("he thephoa na moi mophui ta whuwa", "wrong: flat classifier with ball", False),
        ("pi mathai na lea tuphai ta shire", "wrong: long classifier with cup", False),
        
        # VALID: Correct semantic compatibility (should still work)
        ("sha na lea lathia ta shero", "correct: long classifier with axe", True),
        ("he thephoa na teo mophui ta whuwa", "correct: round classifier with ball", True),
        ("pi mathai na teo tuphai ta shire", "correct: round classifier with cup", True),
        
        # Also test the ones that were already fixed
        ("mia na moi moi whethea ta whupi", "double classifier (should still be invalid)", False),
        ("mia na lea liphai ta whona", "correct: long classifier with tree", True),
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
            
        # Show any relevant errors
        if result['errors']:
            print("   Errors found:")
            for error in result['errors']:
                if 'classifier' in error.error_type.value.lower():
                    print(f"     • {error.error_type.value}: {error.message}")
        else:
            print("   No classifier errors found")

if __name__ == "__main__":
    test_classifier_semantic_fix() 