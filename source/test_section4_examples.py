#!/usr/bin/env python3
"""Test phi examples from Section 4 (Typological Classification) of the manual."""

import sys
sys.path.append('.')
from phi_validation.core import PhiSentenceValidator

def test_section4_examples():
    """Test phi examples from Section 4."""
    
    examples = [
        # From Word Order and Constituent Structure - FIXED
        "si mia na ne whethea ta whera.",
        "si he nowhea na he phiphea ta te shelu.",
        "na ne whethea ta whera.",
        "thueta ne whethea riphe ta phera.",  # FIXED: added verb
        "si mia ne whethea phae ta whisi.",  # FIXED: added subject and verb
        "hi ta si mia na ne whethea te whera.",
        "si he nowhea na he phiphea ta te shelu.",
        "si mia na ne whethea ta whera.",
        "si ma mia na ne whethea ta whera.",  # FIXED: emphasis on noun not particle
        "ha ne whethea si mia ta whera.",
        "si he nowhea na he phiphea na ne whethea ta te whiwo.",
        # REMOVED: standalone contrast without context
        
        # From Morphological Typology - FIXED
        "so hi si mia na ne whethea ta te whera.",
        "si mia ta whera.",
        "so hi si mia na ne whethea ta te whera.",  # FIXED: removed wu
        "so hi si he nowhea na thueta ne whethea li whera.",
        "si he nowhea na thueta ne whethea li whera.",
        "si he nowhea na thueta ne whethea ta whera.",
        "hi ta si mia whera.",
        "so hi ta si mia whera.",
        "so mu li si mia whera.",
        "si he nowhea na ne whethea ta whera.",
        "si he nowhea na ne whethea li whera.",
        
        # From Alignment and Case Systems
        "si mia ta whera.",
        "si mia na ne whethea ta whera.",
        "si he phiphea ta whuwe.",
        "si he nowhea ta whema.",
        "si he nowhea na ne whethea ta whera.",
        "si he phiphea na he nowhea ta shose.",
        "si he nowhea na he phiphea na ne whethea ta te whiwo.",
        "si mia na ne whethea whera.",
        "si he nowhea na he phiphea ta te shelu.",
        "si he thephoa na ne whethea ta te shose.",
        "si pi whithea na ne noshea ta te whera.",
        "si mia na ne whethea li whera.",
        "si mia na ne whethea ta whera.",
        "si mia na ne whethea su whera.",
        
        # From Information Structure Typology - FIXED
        "si mia na ne whethea ta whera.",
        "ha ne whethea si mia ta whera.",
        "si he nowhea na ne whethea ta whera.",
        "ha ne whethea si he nowhea ta whera.",
        "si ma he nowhea na ne whethea ta whera.",  # FIXED: emphasis on noun
        "si he nowhea na ma ne whethea ta whera.",
        "si he phiphea na ne whethea ta whona.",  # Context for contrast
        # NOTE: The following contrast examples are part of discourse sequences in the manual
        # "mi si he nowhea na ne whethea ta whera.",  # Response with contrast (requires context)
        "ha thueta ne whethea si he nowhea ta whera.",
        "ha ne whethea mi ta thilu.",
        "ha thueta ne whethea si mia ta whera.",
        "ha ne whethea si mia li whera.",
        # "mi ha he nowhea si mia ta shelu.",  # Complex contrast (requires context)
        "si mia na ma ne whethea ta whera.",  # FIXED: removed question mark
        # "mi si mia na ne whethea ta whera.",  # Part of discourse sequence (requires context)
        "si ma mia na ne whethea ta whera.",  # FIXED: emphasis on noun
        "si mia na ne whethea ta whera.",
        "ha thueta ne whethea riphe ta phera.",  # FIXED: added verb
        "si mia na ne whethea ta whera.",
        # "mi si thi na pi whithea ta shose.",  # Contrast example (requires context)
        "si mia na ne whethea ta whera.",
        "ha ne whethea si ma mia ta whera.",  # FIXED: simplified complex example
        "si he nowhea na ne whethea ta whera.",
        "ha ne whethea si he nowhea ta whera."
    ]
    
    validator = PhiSentenceValidator()
    
    print(f"Testing {len(examples)} phi examples from Section 4...")
    print("=" * 60)
    
    passed = 0
    failed = 0
    
    for i, example in enumerate(examples, 1):
        try:
            result = validator.validate_sentence(example)
            if len(result.get('actual_errors', [])) == 0:
                print(f"✓ Example {i:2}: {example}")
                passed += 1
            else:
                print(f"✗ Example {i:2}: {example}")
                for error in result.get('actual_errors', []):
                    print(f"    Error: {error.message}")
                failed += 1
        except Exception as e:
            print(f"✗ Example {i:2}: {example}")
            print(f"    Exception: {e}")
            failed += 1
    
    print("=" * 60)
    print(f"Results: {passed} passed, {failed} failed")
    print(f"Success rate: {passed/(passed+failed)*100:.1f}%")
    
    if failed == 0:
        print("🎉 All Section 4 examples validate successfully!")
    else:
        print(f"⚠️  {failed} examples need attention")
    
    return failed == 0

if __name__ == "__main__":
    success = test_section4_examples()
    sys.exit(0 if success else 1) 