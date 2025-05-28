#!/usr/bin/env python3
"""
Test script to verify the tense validation fix.

Tests that 'hi ta ne lowhai whuru' is now valid after fixing the 
particle scope validation to allow slot 2 particles between 
slot 1 particles and verbs.
"""

import sys
from pathlib import Path

# Add source directory to path
sys.path.append(str(Path(__file__).parent))

from phi_validation.particles import ParticleValidator
from phi_validation.lexicon import LexiconValidator

def test_tense_validation_fix():
    """Test that the tense validation fix works correctly."""
    print("🔧 TESTING TENSE VALIDATION FIX")
    print("=" * 50)
    
    # Initialize validators
    lexicon_validator = LexiconValidator()
    particle_validator = ParticleValidator()
    particle_validator.set_lexicon_validator(lexicon_validator)
    
    # Test the problematic sentence from the evidentiality report
    test_sentence = "hi ta ne lowhai whuru"
    tokens = test_sentence.split()
    
    print(f"Testing sentence: {test_sentence}")
    print(f"Tokens: {tokens}")
    print()
    
    # Check word types
    print("Word type identification:")
    for token in tokens:
        lexicon_word_type = lexicon_validator.identify_word_type(token)
        particle_word_type = particle_validator._identify_word_type(token)
        
        # Also check particle slot identification
        if token in particle_validator.slot_0_particles:
            slot_type = "slot_0_particle"
        elif token in particle_validator.slot_1_particles:
            slot_type = "slot_1_particle"
        elif token in particle_validator.slot_2_particles:
            slot_type = "slot_2_particle"
        else:
            slot_type = "not_in_slots"
        
        print(f"  {token}: lexicon={lexicon_word_type}, particle_validator={particle_word_type}, slot={slot_type}")
    print()
    
    # Test particle scope validation
    print("Particle scope validation:")
    scope_errors = particle_validator.validate_particle_scope(tokens)
    
    if scope_errors:
        print("❌ Scope validation failed:")
        for error in scope_errors:
            print(f"  - {error.message}")
    else:
        print("✅ Scope validation passed!")
    
    print()
    
    # Test overall particle validation
    print("Overall particle validation:")
    all_errors = particle_validator.validate_particles(tokens)
    
    if all_errors:
        print("❌ Particle validation failed:")
        for error in all_errors:
            print(f"  - {error.message}")
    else:
        print("✅ All particle validation passed!")
    
    print()
    
    # Summary
    print("SUMMARY:")
    print(f"Sentence: {test_sentence}")
    print(f"Expected: VALID (evidentiality + tense + SOV)")
    print(f"Actual: {'VALID' if not scope_errors else 'INVALID'}")
    
    if not scope_errors:
        print("🎉 TENSE VALIDATION FIX SUCCESSFUL!")
        print("The sentence 'hi ta ne lowhai whuru' is now correctly validated.")
    else:
        print("❌ TENSE VALIDATION FIX FAILED")
        print("The sentence is still being marked as invalid.")

if __name__ == "__main__":
    test_tense_validation_fix() 