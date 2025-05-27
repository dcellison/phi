#!/usr/bin/env python3
"""
Comprehensive Validation Test

Tests the modular phi_validation system against the original monolithic
phi_sentence_validator to ensure complete functionality parity.
"""

import sys
from pathlib import Path

# Import both validators
from phi_validation import PhiSentenceValidator as ModularValidator
sys.path.append(str(Path(__file__).parent))
from phi_sentence_validator import PhiSentenceValidator as OriginalValidator

def test_comprehensive_validation():
    """Test comprehensive validation functionality parity."""
    print("Testing comprehensive validation parity...")
    print("=" * 60)
    
    # Initialize both validators
    modular = ModularValidator()
    original = OriginalValidator()
    
    # Test cases covering different validation aspects
    test_cases = [
        # Basic SOV validation
        ("mia ta thihi", "Basic SOV: I am"),
        ("mia nuthui ta shata", "SOV with object: I throw stone"),
        
        # Word order violations
        ("thihi ta mia", "SOV violation: verb before subject"),
        ("shata ta mia", "SOV violation: verb before subject"),
        
        # Missing/multiple verbs
        ("mia nuthui", "Missing verb"),
        ("mia thihi shata", "Multiple verbs"),
        
        # Particle ordering
        ("mia li ta thihi", "Particle order: past before present"),
        ("mia ta li thihi", "Correct particle order"),
        
        # Derivational particles
        ("mia ta se nuthui", "Derivational: se + noun"),
        ("mia ta ra thihi", "Derivational: ra + verb"),
        
        # Emphasis particles
        ("ma mia ta thihi", "Emphasis on subject"),
        ("mia ma ta thihi", "Emphasis on tense"),
        
        # Complex sentences
        ("hi mia li shola", "Evidentiality + past tense"),
        ("so mia ta thihi", "Politeness particle"),
        ("ha mia mi thi ta thihi", "Discourse particles"),
        
        # Unknown words
        ("mia ta invalidword", "Unknown word test"),
        
        # Empty sentence
        ("", "Empty sentence"),
    ]
    
    mismatches = []
    
    for sentence, description in test_cases:
        print(f"\nTesting: '{sentence}' - {description}")
        
        # Get results from both validators
        modular_result = modular.validate_sentence(sentence)
        original_result = original.validate_sentence(sentence)
        
        # Compare basic validity
        modular_valid = modular_result['is_valid']
        original_valid = original_result['is_valid']
        
        print(f"  Modular valid: {modular_valid}")
        print(f"  Original valid: {original_valid}")
        
        if modular_valid != original_valid:
            mismatches.append({
                'sentence': sentence,
                'description': description,
                'modular_valid': modular_valid,
                'original_valid': original_valid,
                'modular_errors': len(modular_result['errors']),
                'original_errors': len(original_result['errors'])
            })
            print(f"  ❌ MISMATCH: Validity differs!")
        else:
            print(f"  ✅ Match: Both validators agree")
        
        # Compare error counts
        modular_error_count = len(modular_result['errors'])
        original_error_count = len(original_result['errors'])
        
        print(f"  Modular errors: {modular_error_count}")
        print(f"  Original errors: {original_error_count}")
        
        if modular_error_count != original_error_count:
            print(f"  ⚠️  Error count differs")
        
        # Show error details for debugging
        if modular_result['errors']:
            print(f"  Modular error types: {list(modular_result['error_summary'].keys())}")
        if original_result['errors']:
            print(f"  Original error types: {list(original_result['error_summary'].keys())}")
        
        print("-" * 50)
    
    # Summary
    print(f"\n{'='*60}")
    print(f"COMPREHENSIVE VALIDATION TEST SUMMARY")
    print(f"{'='*60}")
    print(f"Total test cases: {len(test_cases)}")
    print(f"Mismatches: {len(mismatches)}")
    
    if mismatches:
        print(f"\n❌ VALIDATION PARITY ISSUES FOUND:")
        for mismatch in mismatches:
            print(f"  - '{mismatch['sentence']}' ({mismatch['description']})")
            print(f"    Modular: {mismatch['modular_valid']} ({mismatch['modular_errors']} errors)")
            print(f"    Original: {mismatch['original_valid']} ({mismatch['original_errors']} errors)")
    else:
        print(f"\n✅ ALL TESTS PASSED: Modular system matches original functionality!")
    
    return len(mismatches) == 0

if __name__ == "__main__":
    success = test_comprehensive_validation()
    sys.exit(0 if success else 1) 