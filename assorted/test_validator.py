#!/usr/bin/env python3
"""
Quick test script for phi_validator.py
"""

import phi_validator

def main():
    # Initialize validator (will warn if pos/ directory not found)
    validator = phi_validator.PhiValidator('.')
    
    print("=== PHI VALIDATOR TEST ===\n")
    
    # Test 1: Valid verb
    print("Test 1: Valid verb 'phawi'")
    result = validator.validate_word('phawi', 'verb', 'to fly')
    print(f"Status: {result['overall_status'].value}")
    print(f"Phonotactic errors: {len(result['phonotactic_errors'])}")
    print()
    
    # Test 2: Invalid verb (wrong pattern)
    print("Test 2: Invalid verb pattern 'palawi'")
    result = validator.validate_word('palawi', 'verb', 'to sing')
    print(f"Status: {result['overall_status'].value}")
    if result['phonotactic_errors']:
        print(f"Error: {result['phonotactic_errors'][0].message}")
    print()
    
    # Test 3: Valid adjective pattern
    print("Test 3: Valid adjective 'hashe'")
    result = validator.validate_word('hashe', 'adjective', 'green') 
    print(f"Status: {result['overall_status'].value}")
    print()
    
    # Test 4: Forbidden vowel pair
    print("Test 4: Forbidden vowel pair 'phiia'")
    result = validator.validate_word('phiia', 'verb', 'test')
    print(f"Status: {result['overall_status'].value}")
    if result['phonotactic_errors']:
        print(f"Error: {result['phonotactic_errors'][0].message}")
    print()
    
    print("✅ Validation tool tests completed!")

if __name__ == "__main__":
    main() 