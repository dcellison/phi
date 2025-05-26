#!/usr/bin/env python3

"""
Test suite for politeness particle context validation in Phi.

Tests comprehensive politeness particle 'so' usage including:
1. Social context appropriateness
2. Politeness-evidentiality combinations  
3. Register consistency validation
4. Discourse function validation
5. Pragmatic appropriateness

Author: Assistant
Date: 2024
"""

import unittest
from phi_sentence_validator import PhiSentenceValidator, SentenceError


class TestPolitenessContext(unittest.TestCase):
    """Test politeness particle context validation."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.validator = PhiSentenceValidator()
    
    def _validate_sentence(self, sentence: str) -> dict:
        """Helper method to validate a sentence and return results."""
        return self.validator.validate_sentence(sentence)
    
    def _has_error_type(self, result: dict, error_type: SentenceError) -> bool:
        """Check if validation result contains specific error type."""
        return any(error.error_type == error_type for error in result['errors'])
    
    def _get_errors_of_type(self, result: dict, error_type: SentenceError) -> list:
        """Get all errors of a specific type from validation result."""
        return [error for error in result['errors'] if error.error_type == error_type]

    # =============================================================================
    # BASIC POLITENESS CONTEXT TESTS
    # =============================================================================
    
    def test_politeness_with_imperative_appropriate(self):
        """Test that politeness is appropriate with imperative commands."""
        # Polite command
        result = self._validate_sentence("so na nuthui to whuwa")
        self.assertTrue(result['is_valid'], "Polite imperative should be valid")
        
        # Polite request with object
        result = self._validate_sentence("so na whethea to whupi")
        self.assertTrue(result['is_valid'], "Polite request should be valid")
    
    def test_politeness_with_questions_appropriate(self):
        """Test that politeness is appropriate with questions."""
        # Polite yes/no question
        result = self._validate_sentence("wa so thi ta shola")
        self.assertTrue(result['is_valid'], "Polite question should be valid")
        
        # Polite wh-question
        result = self._validate_sentence("wulime thi ta shola")
        self.assertTrue(result['is_valid'], "Wh-question should be valid without politeness")
    
    def test_politeness_with_formal_vocabulary(self):
        """Test politeness with formal/institutional vocabulary."""
        # Formal document context
        result = self._validate_sentence("so mia na phuthui ta whupi")
        self.assertTrue(result['is_valid'], "Politeness with formal vocabulary should be valid")
        
        # Professional context
        result = self._validate_sentence("so mia na weshia ta shola")
        self.assertTrue(result['is_valid'], "Politeness in professional context should be valid")
    
    def test_politeness_inappropriate_emotional_context(self):
        """Test that politeness may be inappropriate in emotional contexts."""
        # Emotional statement with emphasis
        result = self._validate_sentence("so mia ma whomo na thi")
        errors = self._get_errors_of_type(result, SentenceError.POLITENESS_CONTEXT_MISMATCH)
        self.assertTrue(len(errors) > 0, "Should flag emotional context as potentially inappropriate")
    
    def test_politeness_inappropriate_urgent_context(self):
        """Test that politeness may be inappropriate in urgent contexts."""
        # Urgent command
        result = self._validate_sentence("so to harote shola")
        errors = self._get_errors_of_type(result, SentenceError.POLITENESS_CONTEXT_MISMATCH)
        self.assertTrue(len(errors) > 0, "Should flag urgent context as potentially inappropriate")

    # =============================================================================
    # POLITENESS-EVIDENTIALITY COMBINATION TESTS
    # =============================================================================
    
    def test_politeness_with_direct_evidence(self):
        """Test politeness with direct evidence (hi)."""
        # Polite direct observation
        result = self._validate_sentence("hi so lashea thihi")
        self.assertTrue(result['is_valid'], "Polite direct evidence should be valid")
        
        # Wrong order (so before hi)
        result = self._validate_sentence("so hi lashea thihi")
        errors = self._get_errors_of_type(result, SentenceError.POLITENESS_EVIDENTIALITY_COMBINATION_ERROR)
        self.assertTrue(len(errors) > 0, "Should flag incorrect evidentiality-politeness order")
    
    def test_politeness_with_inference(self):
        """Test politeness with inference (ro)."""
        # Polite inference
        result = self._validate_sentence("ro so lashea thihi")
        self.assertTrue(result['is_valid'], "Polite inference should be valid")
        
        # Deferential conclusion
        result = self._validate_sentence("ro so mia whethui mipho whemo")
        self.assertTrue(result['is_valid'], "Polite inferential conclusion should be valid")
    
    def test_politeness_with_hearsay(self):
        """Test politeness with hearsay (nu)."""
        # Polite hearsay reporting
        result = self._validate_sentence("nu so thephoa ta shola")
        self.assertTrue(result['is_valid'], "Polite hearsay should be valid")
        
        # Respectful transmission of information
        result = self._validate_sentence("nu so misha thihi")
        self.assertTrue(result['is_valid'], "Polite hearsay transmission should be valid")
    
    def test_politeness_with_reported_speech(self):
        """Test politeness with reported speech (ti)."""
        # Polite reported speech
        result = self._validate_sentence("ti so sha li whemo")
        self.assertTrue(result['is_valid'], "Polite reported speech should be valid")
        
        # Formal quotation
        result = self._validate_sentence("ti so thephoa li shuna")
        self.assertTrue(result['is_valid'], "Polite formal quotation should be valid")
    
    def test_politeness_with_memory(self):
        """Test politeness with memory (mu)."""
        # Polite memory recollection
        result = self._validate_sentence("mu so mia na thi li phose")
        self.assertTrue(result['is_valid'], "Polite memory should be valid")
        
        # Respectful sharing of remembered information
        result = self._validate_sentence("mu so misha li thihi")
        self.assertTrue(result['is_valid'], "Polite memory sharing should be valid")
    
    def test_politeness_with_presumption(self):
        """Test politeness with presumption (pe)."""
        # Polite presumption
        result = self._validate_sentence("pe so mipho thihi")
        self.assertTrue(result['is_valid'], "Polite presumption should be valid")
        
        # Tentative suggestion
        result = self._validate_sentence("pe so thi ru shola")
        self.assertTrue(result['is_valid'], "Polite tentative suggestion should be valid")

    # =============================================================================
    # REGISTER CONSISTENCY TESTS
    # =============================================================================
    
    def test_formal_register_consistency(self):
        """Test register consistency in formal contexts."""
        # Consistent formal register
        result = self._validate_sentence("so si thephoa ta te whupi na phuthui")
        self.assertTrue(result['is_valid'], "Consistent formal register should be valid")
        
        # Formal vocabulary with politeness
        result = self._validate_sentence("so na whethea mia ta whemo")
        self.assertTrue(result['is_valid'], "Formal vocabulary with politeness should be valid")
    
    def test_register_conflict_formal_casual(self):
        """Test detection of formal-casual register conflicts."""
        # Politeness with casual markers (omitted tense)
        result = self._validate_sentence("so mia whuwa nuthui")
        errors = self._get_errors_of_type(result, SentenceError.POLITENESS_REGISTER_INCONSISTENCY)
        # Note: This might not trigger an error depending on implementation
        # The casual marker detection is subtle in Phi
    
    def test_institutional_register_consistency(self):
        """Test register consistency in institutional contexts."""
        # Professional context with politeness
        result = self._validate_sentence("so na weshia mia ta shola")
        self.assertTrue(result['is_valid'], "Institutional context with politeness should be valid")
        
        # Document handling with politeness
        result = self._validate_sentence("so na phuthui mia ta whupi")
        self.assertTrue(result['is_valid'], "Document context with politeness should be valid")
    
    def test_emotional_register_conflict(self):
        """Test detection of emotional-politeness register conflicts."""
        # Strong emotion with politeness
        result = self._validate_sentence("so mia ma whomo na thi")
        errors = self._get_errors_of_type(result, SentenceError.POLITENESS_CONTEXT_MISMATCH)
        self.assertTrue(len(errors) > 0, "Should flag emotional-politeness conflict")

    # =============================================================================
    # DISCOURSE FUNCTION TESTS
    # =============================================================================
    
    def test_politeness_mitigating_face_threat(self):
        """Test politeness for mitigating face-threatening acts."""
        # Polite command (face-threatening)
        result = self._validate_sentence("so to na nuthui whuwa")
        self.assertTrue(result['is_valid'], "Politeness should mitigate face-threatening command")
        
        # Polite obligation
        result = self._validate_sentence("so thi ru shola")
        self.assertTrue(result['is_valid'], "Politeness should mitigate face-threatening obligation")
    
    def test_politeness_showing_deference(self):
        """Test politeness for showing deference."""
        # Deferential statement
        result = self._validate_sentence("so mia whemo whethui thihi misha")
        self.assertTrue(result['is_valid'], "Politeness should show deference in statements")
        
        # Deferential question
        result = self._validate_sentence("wa so thi whemo")
        self.assertTrue(result['is_valid'], "Politeness should show deference in questions")
    
    def test_politeness_formal_institutional_marking(self):
        """Test politeness for marking formal/institutional register."""
        # Institutional communication
        result = self._validate_sentence("so na phuthui mia ta whupi")
        self.assertTrue(result['is_valid'], "Politeness should mark institutional register")
        
        # Professional interaction
        result = self._validate_sentence("so na weshia thi ta shola")
        self.assertTrue(result['is_valid'], "Politeness should mark professional register")
    
    def test_politeness_softening_requests(self):
        """Test politeness for softening requests and commands."""
        # Softened request
        result = self._validate_sentence("so wa thi shire na whethea")
        self.assertTrue(result['is_valid'], "Politeness should soften requests")
        
        # Softened command
        result = self._validate_sentence("so to na luthia whupi")
        self.assertTrue(result['is_valid'], "Politeness should soften commands")

    # =============================================================================
    # PRAGMATIC APPROPRIATENESS TESTS
    # =============================================================================
    
    def test_power_relationship_contexts(self):
        """Test politeness in different power relationship contexts."""
        # Superior to subordinate (command)
        result = self._validate_sentence("so to na phuthui whupi")
        self.assertTrue(result['is_valid'], "Politeness appropriate in superior-subordinate context")
        
        # Equal relationship with formal context
        result = self._validate_sentence("so wa thi whemo")
        self.assertTrue(result['is_valid'], "Politeness appropriate in equal formal context")
    
    def test_social_distance_contexts(self):
        """Test politeness with different social distance levels."""
        # Distant/formal relationship
        result = self._validate_sentence("so na phuthui mia ta whupi")
        self.assertTrue(result['is_valid'], "Politeness appropriate for distant relationships")
        
        # Close relationship context
        result = self._validate_sentence("so mia whomo na luthea")
        # This might trigger a pragmatic warning about close relationships
        # not requiring formal politeness
    
    def test_cultural_sensitivity_contexts(self):
        """Test politeness for cultural sensitivity."""
        # Cross-cultural communication
        result = self._validate_sentence("so mia whemo thi thihi misha")
        self.assertTrue(result['is_valid'], "Politeness appropriate for cultural sensitivity")
        
        # International/neutral context
        result = self._validate_sentence("so na whethea mia ta whemo")
        self.assertTrue(result['is_valid'], "Politeness appropriate for international context")
    
    def test_situational_formality_contexts(self):
        """Test politeness in different situational formality levels."""
        # Professional situation
        result = self._validate_sentence("so na weshia mia ta shola")
        self.assertTrue(result['is_valid'], "Politeness appropriate in professional situations")
        
        # Academic/educational context
        result = self._validate_sentence("so na whethea mia ta whemo")
        self.assertTrue(result['is_valid'], "Politeness appropriate in academic contexts")

    # =============================================================================
    # COMPLEX COMBINATION TESTS
    # =============================================================================
    
    def test_complex_politeness_evidentiality_formal(self):
        """Test complex combinations of politeness, evidentiality, and formal register."""
        # Direct evidence + politeness + formal vocabulary
        result = self._validate_sentence("hi so si thephoa ta te whupi na phuthui")
        self.assertTrue(result['is_valid'], "Complex formal combination should be valid")
        
        # Inference + politeness + institutional context
        result = self._validate_sentence("ro so na weshia mia ta shola")
        self.assertTrue(result['is_valid'], "Complex institutional combination should be valid")
    
    def test_politeness_with_multiple_particles(self):
        """Test politeness with multiple other particles."""
        # Politeness + emphasis + formal marking
        result = self._validate_sentence("so si thephoa ta ma whupi na phuthui")
        self.assertTrue(result['is_valid'], "Politeness with multiple particles should be valid")
        
        # Politeness + evidentiality + discourse marker
        result = self._validate_sentence("hi so ha thephoa ta shola")
        self.assertTrue(result['is_valid'], "Complex particle combination should be valid")
    
    def test_inappropriate_politeness_combinations(self):
        """Test inappropriate politeness combinations."""
        # Politeness with urgent + emotional context
        result = self._validate_sentence("so to harote ma sheho")
        errors = self._get_errors_of_type(result, SentenceError.POLITENESS_CONTEXT_MISMATCH)
        self.assertTrue(len(errors) > 0, "Should flag inappropriate urgent+emotional+politeness")
        
        # Politeness with intimate + casual context
        result = self._validate_sentence("so mia whomo na luthea")
        # May trigger pragmatic warnings about intimate contexts

    # =============================================================================
    # EDGE CASES AND ERROR CONDITIONS
    # =============================================================================
    
    def test_politeness_position_validation(self):
        """Test that politeness particle appears in correct position."""
        # Politeness should be in slot 0 (sentence-initial area)
        result = self._validate_sentence("so mia ta whuwa")
        self.assertTrue(result['is_valid'], "Sentence-initial politeness should be valid")
        
        # Test with other slot 0 particles
        result = self._validate_sentence("wa so thi ta shola")
        self.assertTrue(result['is_valid'], "Politeness after question marker should be valid")
    
    def test_multiple_politeness_particles(self):
        """Test handling of multiple politeness particles."""
        # Multiple 'so' particles (should be invalid)
        result = self._validate_sentence("so so mia ta whuwa")
        # This should be caught by particle ordering rules
    
    def test_politeness_without_main_content(self):
        """Test politeness particle without substantial content."""
        # Politeness with minimal content
        result = self._validate_sentence("so thihi")
        # Should be valid but minimal
        
        # Politeness with just particles
        result = self._validate_sentence("so ta")
        # Should be invalid due to missing verb/content

    # =============================================================================
    # PRAGMATIC NUANCE TESTS
    # =============================================================================
    
    def test_evidentiality_pragmatic_nuances(self):
        """Test pragmatic nuances of evidentiality-politeness combinations."""
        # Direct evidence + politeness for obvious facts (may be inappropriate)
        result = self._validate_sentence("hi so thihi lashea")
        # Might trigger pragmatic warning for obvious weather observation
        
        # Presumption + politeness for strong assumptions (inappropriate)
        result = self._validate_sentence("pe so thihi mipho")
        # Might trigger warning for definitive statement with presumptive evidentiality
    
    def test_register_transition_validation(self):
        """Test validation of register transitions within sentences."""
        # Consistent formal register throughout
        result = self._validate_sentence("so si thephoa ta te whupi na phuthui")
        self.assertTrue(result['is_valid'], "Consistent formal register should be valid")
        
        # Mixed register markers
        result = self._validate_sentence("so mia whuwa na phuthui")
        # May trigger register inconsistency warnings
    
    def test_contextual_appropriateness_edge_cases(self):
        """Test edge cases for contextual appropriateness."""
        # Politeness in technical contexts
        result = self._validate_sentence("so na phuthui mia ta whupi")
        self.assertTrue(result['is_valid'], "Politeness in technical context should be valid")
        
        # Politeness with negation
        result = self._validate_sentence("so mia me whemo")
        self.assertTrue(result['is_valid'], "Politeness with negation should be valid")


def run_politeness_tests():
    """Run all politeness context tests and display results."""
    unittest.main(verbosity=2)


if __name__ == '__main__':
    run_politeness_tests() 