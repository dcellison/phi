#!/usr/bin/env python3
"""
Test Discourse Particle Sequences

Tests for validating discourse particle sequences in Phi:
1. Topic chains with 'ha' across multiple sentences/clauses
2. Contrast scope with 'mi' at different discourse levels  
3. Topic-contrast interaction patterns
4. Complex argumentative structures
"""

import sys
from pathlib import Path

# Add the current directory to path to import phi_sentence_validator
sys.path.append(str(Path(__file__).parent))

from phi_sentence_validator import PhiSentenceValidator


def test_topic_chain_coherence():
    """Test topic chain coherence and proper topic management."""
    print("=== TESTING TOPIC CHAIN COHERENCE ===\n")
    
    validator = PhiSentenceValidator()
    
    test_cases = [
        # Valid topic introduction
        {
            "sentence": "ha whethui phera misha",
            "description": "Basic topic introduction: 'speaking of weather, it is beautiful'",
            "expected_valid": True
        },
        
        # Valid topic shift with sufficient development
        {
            "sentence": "ha liphai phera tophe ha na seiwhea phera hashe",
            "description": "Topic shift with development: 'speaking of trees, they are tall. speaking of branches, they are green'",
            "expected_valid": True
        },
        
        # Invalid topic shift - too close
        {
            "sentence": "ha liphai ha seiwhea",
            "description": "Invalid topic shift - too close without development",
            "expected_valid": False
        },
        
        # Valid topic resumption after contrast
        {
            "sentence": "ha whethui phera misha mi ha whethui phera wathe",
            "description": "Valid topic resumption after contrast: 'speaking of weather, it's beautiful. however, speaking of weather, it's bad'",
            "expected_valid": True
        },
        
        # Topic marker followed by particle (invalid)
        {
            "sentence": "ha mi phera misha",
            "description": "Invalid: topic marker followed by particle instead of topic noun",
            "expected_valid": False
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"Test {i}: {test_case['description']}")
        print(f"Sentence: {test_case['sentence']}")
        
        result = validator.validate_sentence(test_case['sentence'])
        
        # Check for topic chain violations
        topic_errors = [error for error in result['errors'] 
                       if 'TOPIC_CHAIN_VIOLATION' in error.error_type.value]
        
        has_topic_errors = len(topic_errors) > 0
        is_valid = not has_topic_errors
        
        print(f"Expected: {'Valid' if test_case['expected_valid'] else 'Invalid'}")
        print(f"Actual: {'Valid' if is_valid else 'Invalid'}")
        
        if topic_errors:
            print("Topic chain errors found:")
            for error in topic_errors:
                print(f"  - {error.message}")
        
        status = "✅ PASS" if is_valid == test_case['expected_valid'] else "❌ FAIL"
        print(f"Status: {status}\n")


def test_contrast_scope_logic():
    """Test contrast scope and logical relationships."""
    print("=== TESTING CONTRAST SCOPE LOGIC ===\n")
    
    validator = PhiSentenceValidator()
    
    test_cases = [
        # Valid sentence-level contrast
        {
            "sentence": "thowai phera tapha mi phawhoa phera wathe",
            "description": "Valid sentence-level contrast: 'morning was peaceful, however afternoon was bad'",
            "expected_valid": True
        },
        
        # Invalid contrast at sentence beginning
        {
            "sentence": "mi phera misha",
            "description": "Invalid: contrast marker at sentence beginning with no prior context",
            "expected_valid": False
        },
        
        # Valid contrast with evidentiality
        {
            "sentence": "hi phera waphe mi nu phera nethi",
            "description": "Valid contrast with evidentiality: 'I see it's warm, however I hear it's cold'",
            "expected_valid": True
        },
        
        # Contrast with semantic opposition
        {
            "sentence": "whethui phera tushe mi sha phera wathe",
            "description": "Valid contrast with semantic opposition: 'weather is good, however it is bad'",
            "expected_valid": True
        },
        
        # Contrast without sufficient content
        {
            "sentence": "phera mi",
            "description": "Invalid: contrast without sufficient following content",
            "expected_valid": False
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"Test {i}: {test_case['description']}")
        print(f"Sentence: {test_case['sentence']}")
        
        result = validator.validate_sentence(test_case['sentence'])
        
        # Check for contrast scope errors
        contrast_errors = [error for error in result['errors'] 
                          if 'CONTRAST_SCOPE_ERROR' in error.error_type.value]
        
        has_contrast_errors = len(contrast_errors) > 0
        is_valid = not has_contrast_errors
        
        print(f"Expected: {'Valid' if test_case['expected_valid'] else 'Invalid'}")
        print(f"Actual: {'Valid' if is_valid else 'Invalid'}")
        
        if contrast_errors:
            print("Contrast scope errors found:")
            for error in contrast_errors:
                print(f"  - {error.message}")
        
        status = "✅ PASS" if is_valid == test_case['expected_valid'] else "❌ FAIL"
        print(f"Status: {status}\n")


def test_topic_contrast_interactions():
    """Test complex topic-contrast interaction patterns."""
    print("=== TESTING TOPIC-CONTRAST INTERACTIONS ===\n")
    
    validator = PhiSentenceValidator()
    
    test_cases = [
        # Valid ha-mi combination (adjacent)
        {
            "sentence": "ha mi whethui phera wathe",
            "description": "Valid ha-mi combination: 'speaking of that, however, weather is bad'",
            "expected_valid": True
        },
        
        # Valid topic then contrast with sufficient content
        {
            "sentence": "ha whethui phera misha mi sha phera wathe",
            "description": "Valid topic then contrast: 'speaking of weather, it's beautiful. however, it is bad'",
            "expected_valid": True
        },
        
        # Invalid: insufficient content between topic and contrast
        {
            "sentence": "ha whethui mi wathe",
            "description": "Invalid: insufficient content between topic and contrast markers",
            "expected_valid": False
        },
        
        # Valid contrast then topic (discourse repair)
        {
            "sentence": "mi ha whethui phera misha",
            "description": "Valid contrast then topic: 'however, speaking of weather, it is beautiful'",
            "expected_valid": True
        },
        
        # Invalid: topic too close after contrast
        {
            "sentence": "mi ha phera",
            "description": "Invalid: topic marker too close after contrast without development",
            "expected_valid": False
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"Test {i}: {test_case['description']}")
        print(f"Sentence: {test_case['sentence']}")
        
        result = validator.validate_sentence(test_case['sentence'])
        
        # Check for topic-contrast interaction errors
        interaction_errors = [error for error in result['errors'] 
                             if 'TOPIC_CONTRAST_INTERACTION_ERROR' in error.error_type.value]
        
        has_interaction_errors = len(interaction_errors) > 0
        is_valid = not has_interaction_errors
        
        print(f"Expected: {'Valid' if test_case['expected_valid'] else 'Invalid'}")
        print(f"Actual: {'Valid' if is_valid else 'Invalid'}")
        
        if interaction_errors:
            print("Topic-contrast interaction errors found:")
            for error in interaction_errors:
                print(f"  - {error.message}")
        
        status = "✅ PASS" if is_valid == test_case['expected_valid'] else "❌ FAIL"
        print(f"Status: {status}\n")


def test_complex_discourse_patterns():
    """Test complex discourse patterns including argumentative structures."""
    print("=== TESTING COMPLEX DISCOURSE PATTERNS ===\n")
    
    validator = PhiSentenceValidator()
    
    test_cases = [
        # Valid parallel topic development
        {
            "sentence": "ha pewhia na muphui phera teshe ha pewhia na showhia phera teshe ha pewhia na nithoa phera huphea",
            "description": "Valid parallel topic development: technology in education/healthcare/privacy",
            "expected_valid": True
        },
        
        # Valid discourse repair pattern
        {
            "sentence": "ha thiphui phera teshe ha mi thiphui na phi wuthai phera phuri teshe",
            "description": "Valid discourse repair: 'speaking of meeting, it was good. speaking of that, however, the first part was productive'",
            "expected_valid": True
        },
        
        # Invalid argumentative structure - markers too close
        {
            "sentence": "ha mi ha mi phera teshe",
            "description": "Invalid: discourse markers too close together in argumentative structure",
            "expected_valid": False
        },
        
        # Valid meta-discourse management
        {
            "sentence": "ha lo mia thiwhea phera riphe ha lawhui huphea phera",
            "description": "Valid meta-discourse: 'speaking of our discussion, it's important. speaking of time constraints, they exist'",
            "expected_valid": True
        },
        
        # Topic nesting too deep
        {
            "sentence": "ha whethui ha liphai ha seiwhea ha haiwhia phera hashe",
            "description": "Invalid: topic nesting too deep (level 4), may reduce clarity",
            "expected_valid": False
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"Test {i}: {test_case['description']}")
        print(f"Sentence: {test_case['sentence']}")
        
        result = validator.validate_sentence(test_case['sentence'])
        
        # Check for discourse sequence errors
        discourse_errors = [error for error in result['errors'] 
                           if any(error_type in error.error_type.value for error_type in 
                                 ['DISCOURSE_SEQUENCE_ERROR', 'TOPIC_CHAIN_VIOLATION'])]
        
        has_discourse_errors = len(discourse_errors) > 0
        is_valid = not has_discourse_errors
        
        print(f"Expected: {'Valid' if test_case['expected_valid'] else 'Invalid'}")
        print(f"Actual: {'Valid' if is_valid else 'Invalid'}")
        
        if discourse_errors:
            print("Discourse pattern errors found:")
            for error in discourse_errors:
                print(f"  - {error.message}")
        
        status = "✅ PASS" if is_valid == test_case['expected_valid'] else "❌ FAIL"
        print(f"Status: {status}\n")


def test_discourse_with_other_particles():
    """Test discourse particles in combination with other particle types."""
    print("=== TESTING DISCOURSE WITH OTHER PARTICLES ===\n")
    
    validator = PhiSentenceValidator()
    
    test_cases = [
        # Discourse with politeness
        {
            "sentence": "ha so whethui phera misha",
            "description": "Valid: politeness with topic marker",
            "expected_valid": True
        },
        
        # Discourse with evidentiality
        {
            "sentence": "ha hi whethui phera waphe mi ro sha phera nethi",
            "description": "Valid: evidentiality with discourse markers",
            "expected_valid": True
        },
        
        # Discourse with questions
        {
            "sentence": "wa ha whethui phera misha",
            "description": "Valid: question with topic marker",
            "expected_valid": True
        },
        
        # Complex combination
        {
            "sentence": "ha so hi whethui phera misha mi nu sha phera wathe",
            "description": "Valid: politeness + evidentiality + discourse markers",
            "expected_valid": True
        },
        
        # Discourse with emphasis
        {
            "sentence": "ha ma whethui phera misha mi ma sha phera wathe",
            "description": "Valid: discourse markers with emphasis particles",
            "expected_valid": True
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"Test {i}: {test_case['description']}")
        print(f"Sentence: {test_case['sentence']}")
        
        result = validator.validate_sentence(test_case['sentence'])
        
        # Check overall validity (should be valid for these combinations)
        is_valid = result['is_valid']
        
        print(f"Expected: {'Valid' if test_case['expected_valid'] else 'Invalid'}")
        print(f"Actual: {'Valid' if is_valid else 'Invalid'}")
        
        if not is_valid:
            print("Errors found:")
            for error in result['errors']:
                print(f"  - [{error.error_type.value}] {error.message}")
        
        status = "✅ PASS" if is_valid == test_case['expected_valid'] else "❌ FAIL"
        print(f"Status: {status}\n")


def run_all_tests():
    """Run all discourse particle sequence tests."""
    print("PHI DISCOURSE PARTICLE SEQUENCE VALIDATION TESTS")
    print("=" * 60)
    print()
    
    test_topic_chain_coherence()
    test_contrast_scope_logic()
    test_topic_contrast_interactions()
    test_complex_discourse_patterns()
    test_discourse_with_other_particles()
    
    print("=" * 60)
    print("All discourse particle sequence tests completed!")


if __name__ == "__main__":
    run_all_tests() 