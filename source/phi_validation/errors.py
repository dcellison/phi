#!/usr/bin/env python3
"""
Error Definitions for Phi Sentence Validation

Defines error types and validation error classes used across all validation modules.
"""

from typing import Optional
from enum import Enum


class SentenceError(Enum):
    """Types of sentence validation errors."""
    INVALID_WORD = "invalid_word"
    WORD_ORDER = "word_order"
    PARTICLE_ORDER = "particle_order"
    PARTICLE_SCOPE = "particle_scope"
    MISSING_VERB = "missing_verb"
    MULTIPLE_VERBS = "multiple_verbs"
    SEMANTIC_MISMATCH = "semantic_mismatch"
    UNKNOWN_WORD = "unknown_word"
    TENSE_INCONSISTENCY = "tense_inconsistency"
    ASPECT_TENSE_CONFLICT = "aspect_tense_conflict"
    MODAL_TENSE_CONFLICT = "modal_tense_conflict"
    TEMPORAL_ADVERB_CONFLICT = "temporal_adverb_conflict"
    MULTIPLE_TENSE_MARKERS = "multiple_tense_markers"
    ANIMACY_MISMATCH = "animacy_mismatch"
    CLASSIFIER_INCOMPATIBILITY = "classifier_incompatibility"
    VERB_ARGUMENT_VIOLATION = "verb_argument_violation"
    MODAL_VERB_FORM_ERROR = "modal_verb_form_error"
    CONDITIONAL_STRUCTURE_ERROR = "conditional_structure_error"
    DESIDERATIVE_CONSTRUCTION_ERROR = "desiderative_construction_error"
    TEMPORAL_SEQUENCE_ERROR = "temporal_sequence_error"
    RELATIVE_CLAUSE_TENSE_ERROR = "relative_clause_tense_error"
    INTERROGATIVE_TENSE_ERROR = "interrogative_tense_error"
    QUESTION_CONTEXT_MISMATCH = "question_context_mismatch"
    EVIDENTIALITY_COMBINATION_ERROR = "evidentiality_combination_error"
    EVIDENTIALITY_TENSE_CONFLICT = "evidentiality_tense_conflict"
    EVIDENTIALITY_MODAL_CONFLICT = "evidentiality_modal_conflict"
    EVIDENTIALITY_DISCOURSE_CONFLICT = "evidentiality_discourse_conflict"
    REPORTED_SPEECH_NESTING_ERROR = "reported_speech_nesting_error"
    DERIVATIONAL_SCOPE_ERROR = "derivational_scope_error"
    DERIVATIONAL_SEMANTIC_ERROR = "derivational_semantic_error"
    DERIVATIONAL_PHONOTACTIC_ERROR = "derivational_phonotactic_error"
    DERIVATIONAL_CONTEXT_WARNING = "derivational_context_warning"
    DERIVATIONAL_CONFLICT_ERROR = "derivational_conflict_error"
    EMPHASIS_SCOPE_ERROR = "emphasis_scope_error"
    POLITENESS_CONTEXT_MISMATCH = "politeness_context_mismatch"
    POLITENESS_EVIDENTIALITY_COMBINATION_ERROR = "politeness_evidentiality_combination_error"
    POLITENESS_PRAGMATIC_MISMATCH = "politeness_pragmatic_mismatch"
    POLITENESS_REGISTER_INCONSISTENCY = "politeness_register_inconsistency"
    POLITENESS_REGISTER_INCOMPLETE = "politeness_register_incomplete"
    POLITENESS_MISSING_REQUIRED = "politeness_missing_required"
    POLITENESS_DISCOURSE_MISMATCH = "politeness_discourse_mismatch"
    POLITENESS_PRAGMATIC_INAPPROPRIATE = "politeness_pragmatic_inappropriate"
    DISCOURSE_SEQUENCE_ERROR = "discourse_sequence_error"
    TOPIC_CHAIN_VIOLATION = "topic_chain_violation"
    CONTRAST_SCOPE_ERROR = "contrast_scope_error"
    TOPIC_CONTRAST_INTERACTION_ERROR = "topic_contrast_interaction_error"


class SentenceValidationError:
    """Represents a sentence validation error."""
    
    def __init__(self, error_type: SentenceError, message: str, 
                 position: Optional[int] = None, word: Optional[str] = None):
        self.error_type = error_type
        self.message = message
        self.position = position
        self.word = word 