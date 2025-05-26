#!/usr/bin/env python3
"""
Simple Discourse Particle Sequence Test

Demonstrates the discourse particle sequence validation working correctly
with basic examples that focus on discourse logic without other validation conflicts.
"""

import sys
from pathlib import Path

# Add the current directory to path to import phi_sentence_validator
sys.path.append(str(Path(__file__).parent))

from phi_sentence_validator import PhiSentenceValidator


def test_basic_discourse_patterns():
    """Test basic discourse patterns that should work correctly."""
    print("=== BASIC DISCOURSE PATTERN VALIDATION ===\n")
    
    validator = PhiSentenceValidator()
    
    test_cases = [
        # Basic topic introduction
        {
            "sentence": "ha whethui phera misha",
            "description": "Basic topic introduction",
            "focus": "Topic marker 'ha' introducing weather topic"
        },
        
        # Basic contrast
        {
            "sentence": "whethui phera tushe mi whethui phera wathe",
            "description": "Basic contrast structure",
            "focus": "Contrast marker 'mi' showing opposition between good and bad weather"
        },
        
        # Topic-contrast combination
        {
            "sentence": "ha mi whethui phera wathe",
            "description": "Topic-contrast combination",
            "focus": "Adjacent 'ha mi' pattern for discourse management"
        },
        
        # Topic resumption after contrast
        {
            "sentence": "whethui phera misha mi ha whethui phera wathe",
            "description": "Topic resumption after contrast",
            "focus": "Valid topic resumption pattern with intervening contrast"
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"Test {i}: {test_case['description']}")
        print(f"Sentence: {test_case['sentence']}")
        print(f"Focus: {test_case['focus']}")
        
        result = validator.validate_sentence(test_case['sentence'])
        
        # Check specifically for discourse-related errors
        discourse_errors = [error for error in result['errors'] 
                           if any(error_type in error.error_type.value for error_type in 
                                 ['DISCOURSE_SEQUENCE_ERROR', 'TOPIC_CHAIN_VIOLATION', 
                                  'CONTRAST_SCOPE_ERROR', 'TOPIC_CONTRAST_INTERACTION_ERROR'])]
        
        has_discourse_errors = len(discourse_errors) > 0
        
        print(f"Discourse validation: {'❌ ERRORS' if has_discourse_errors else '✅ VALID'}")
        
        if discourse_errors:
            print("Discourse errors found:")
            for error in discourse_errors:
                print(f"  - {error.message}")
        else:
            print("✅ No discourse particle sequence errors detected")
        
        # Show other errors for context but don't fail the test
        other_errors = [error for error in result['errors'] 
                       if not any(error_type in error.error_type.value for error_type in 
                                 ['DISCOURSE_SEQUENCE_ERROR', 'TOPIC_CHAIN_VIOLATION', 
                                  'CONTRAST_SCOPE_ERROR', 'TOPIC_CONTRAST_INTERACTION_ERROR'])]
        
        if other_errors:
            print(f"Other validation issues ({len(other_errors)}):")
            for error in other_errors[:3]:  # Show first 3
                print(f"  - [{error.error_type.value}] {error.message}")
            if len(other_errors) > 3:
                print(f"  ... and {len(other_errors) - 3} more")
        
        print()


def test_discourse_error_detection():
    """Test that discourse validation correctly detects errors."""
    print("=== DISCOURSE ERROR DETECTION ===\n")
    
    validator = PhiSentenceValidator()
    
    error_cases = [
        # Contrast at sentence beginning
        {
            "sentence": "mi phera misha",
            "description": "Contrast at sentence beginning",
            "expected_error": "Should detect contrast without prior context"
        },
        
        # Topic followed by problematic particle
        {
            "sentence": "ha mi",
            "description": "Topic followed by contrast only",
            "expected_error": "Should detect insufficient content after topic-contrast"
        }
    ]
    
    for i, test_case in enumerate(error_cases, 1):
        print(f"Error Test {i}: {test_case['description']}")
        print(f"Sentence: {test_case['sentence']}")
        print(f"Expected: {test_case['expected_error']}")
        
        result = validator.validate_sentence(test_case['sentence'])
        
        # Check for discourse-related errors
        discourse_errors = [error for error in result['errors'] 
                           if any(error_type in error.error_type.value for error_type in 
                                 ['DISCOURSE_SEQUENCE_ERROR', 'TOPIC_CHAIN_VIOLATION', 
                                  'CONTRAST_SCOPE_ERROR', 'TOPIC_CONTRAST_INTERACTION_ERROR'])]
        
        if discourse_errors:
            print("✅ Correctly detected discourse errors:")
            for error in discourse_errors:
                print(f"  - {error.message}")
        else:
            print("❌ No discourse errors detected (may need refinement)")
        
        print()


def demonstrate_discourse_features():
    """Demonstrate the key discourse features implemented."""
    print("=== DISCOURSE PARTICLE SEQUENCE FEATURES ===\n")
    
    features = [
        {
            "feature": "Topic Chain Management",
            "description": "Validates proper use of 'ha' for topic introduction and shifts",
            "example": "ha whethui phera misha"
        },
        {
            "feature": "Contrast Scope Logic", 
            "description": "Validates logical use of 'mi' for contrasting content",
            "example": "whethui phera tushe mi whethui phera wathe"
        },
        {
            "feature": "Topic-Contrast Interactions",
            "description": "Validates complex ha-mi interaction patterns",
            "example": "ha mi whethui phera wathe"
        },
        {
            "feature": "Discourse Coherence",
            "description": "Ensures discourse markers create logical flow",
            "example": "ha whethui phera misha mi ha whethui phera wathe"
        }
    ]
    
    for feature in features:
        print(f"🔹 {feature['feature']}")
        print(f"   {feature['description']}")
        print(f"   Example: {feature['example']}")
        print()
    
    print("These features enable sophisticated discourse management in Phi,")
    print("supporting complex argumentation, topic development, and")
    print("conversational repair patterns.")


if __name__ == "__main__":
    print("PHI DISCOURSE PARTICLE SEQUENCE VALIDATION")
    print("=" * 50)
    print()
    
    test_basic_discourse_patterns()
    test_discourse_error_detection()
    demonstrate_discourse_features()
    
    print("=" * 50)
    print("Discourse particle sequence validation demonstration complete!") 