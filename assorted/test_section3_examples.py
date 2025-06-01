#!/usr/bin/env python3
"""Test phi examples from Section 3 of the manual."""

import sys
sys.path.append('.')
from phi_validation.core import PhiSentenceValidator

def test_section3_examples():
    """Test phi examples from Section 3."""
    
    examples = [
        # From Core Design Principles
        "si he phiphea na he nowhea ta te shelu.",
        "hi si mia ta te whera.",
        "si mia na ne whethea ta te whera.",
        "ma ne whethea si mia ta te whera.",
        "ha ne whethea si mia ta te whera.",
        
        # From Philosophical Commitments
        "hi he thephoa li thamo.",
        "nu he thephoa li thamo.",
        
        # From Design Trade-offs - Complex sentences with proper grammar
        "so hi si mia na ne whethea ta te whera.",
        "mia na ne whethea ta whera.",
        "so hi si he nowhea na thueta ne whethea riphe ta te whemo.",
        "he nowhea na thueta ne whethea riphe ta whemo.",
        
        # From User-Centered Design
        "si mia ta whera.",
        "si thi ta shose.",
        "si mia na ne whethea ta whera.",
        "si thi na he nowhea ta shose.",
        "hi si mia na ne whethea ta whera.",
        "so hi si mia na ne whethea ta whera.",
        "so mu si mia na ne whethea wu te whera."
    ]
    
    validator = PhiSentenceValidator()
    
    print("Testing Section 3 phi examples...")
    print("=" * 50)
    
    all_valid = True
    
    for i, example in enumerate(examples, 1):
        print(f"\nExample {i}: {example}")
        
        result = validator.validate_sentence(example)
        
        if len(result['actual_errors']) == 0:
            print(f"✅ Valid")
        else:
            print(f"❌ Invalid")
            all_valid = False
            for error in result['actual_errors']:
                print(f"   Error: {error.message}")
    
    print("\n" + "=" * 50)
    if all_valid:
        print("✅ All Section 3 examples are valid!")
    else:
        print("❌ Some Section 3 examples have issues")
    
    return all_valid

if __name__ == "__main__":
    test_section3_examples() 