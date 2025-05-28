#!/usr/bin/env python3
"""
Test script to verify evidentiality nesting validation.

Tests the specific nesting issues mentioned in the evidentiality report:
1. nu ti should be valid (hearsay containing quote) but is marked invalid
2. ti ti should be invalid (nested quotes) but is marked valid
"""

import sys
from pathlib import Path

# Add source directory to path
sys.path.append(str(Path(__file__).parent))

from phi_validation.evidentiality import EvidentialityValidator
from phi_validation.lexicon import LexiconValidator

def test_nesting_validation():
    """Test evidentiality nesting validation."""
    print("🔗 TESTING EVIDENTIALITY NESTING VALIDATION")
    print("=" * 60)
    
    # Initialize validators
    evidentiality_validator = EvidentialityValidator()
    
    # Test cases from the evidentiality report
    test_cases = [
        # Case 1: nu ti should be valid (hearsay containing quote)
        {
            'tokens': ['nu', 'sha', 'li', 'phemo', 'ti', 'mia', 'ta', 'shola'],
            'description': 'nu ti - hearsay containing direct quote',
            'expected_valid': True,
            'explanation': 'Should be valid: "They say he said I walk"'
        },
        
        # Case 2: ti ti should be invalid (nested quotes)
        {
            'tokens': ['ti', 'sha', 'li', 'phemo', 'ti', 'mia', 'ta', 'shola'],
            'description': 'ti ti - nested direct quotes',
            'expected_valid': False,
            'explanation': 'Should be invalid: cannot nest direct quotes'
        },
        
        # Case 3: Simple nu ti without context (should be invalid due to structure)
        {
            'tokens': ['nu', 'ti', 'mia', 'ta', 'shola'],
            'description': 'nu ti - without proper context',
            'expected_valid': False,
            'explanation': 'Should be invalid: missing context between nu and ti'
        },
        
        # Case 4: Simple nu (should be valid)
        {
            'tokens': ['nu', 'mia', 'ta', 'shola'],
            'description': 'nu only - simple hearsay',
            'expected_valid': True,
            'explanation': 'Should be valid: simple hearsay'
        },
        
        # Case 5: Simple ti (should be valid)
        {
            'tokens': ['ti', 'mia', 'ta', 'shola'],
            'description': 'ti only - simple direct report',
            'expected_valid': True,
            'explanation': 'Should be valid: simple direct report'
        }
    ]
    
    print("Testing evidentiality nesting patterns:")
    print()
    
    for i, test_case in enumerate(test_cases, 1):
        tokens = test_case['tokens']
        description = test_case['description']
        expected_valid = test_case['expected_valid']
        explanation = test_case['explanation']
        
        print(f"{i}. {description}")
        print(f"   Tokens: {' '.join(tokens)}")
        print(f"   Expected: {'VALID' if expected_valid else 'INVALID'}")
        print(f"   Explanation: {explanation}")
        
        # Test evidentiality validation
        errors = evidentiality_validator.validate_evidentiality(tokens)
        
        # Show all evidentiality-related errors for debugging
        print(f"   All errors ({len(errors)}):")
        for error in errors:
            print(f"     - {error.error_type.value}: {error.message}")
        
        # Filter for nesting and combination errors
        nesting_errors = [e for e in errors if 'nesting' in e.error_type.value.lower()]
        combination_errors = [e for e in errors if 'combination' in e.error_type.value.lower()]
        all_ev_errors = nesting_errors + combination_errors
        
        actual_valid = len(all_ev_errors) == 0
        
        status = "✅" if actual_valid == expected_valid else "❌"
        print(f"   Actual: {'VALID' if actual_valid else 'INVALID'} {status}")
        
        if all_ev_errors:
            print("   Errors:")
            for error in all_ev_errors:
                print(f"     - {error.message}")
        
        print()
    
    print("SUMMARY:")
    print("The nesting validation needs to be fixed to:")
    print("1. Allow 'nu ti' when properly structured (hearsay containing quote)")
    print("2. Ensure 'ti ti' is properly blocked (nested quotes)")
    print("3. Validate proper context structure for nesting")

if __name__ == "__main__":
    test_nesting_validation() 