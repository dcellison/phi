#!/usr/bin/env python3
"""
Word Order Validation Module

Validates SOV (Subject-Object-Verb) word order compliance
and basic sentence structure in Phi.
"""

from typing import List, Optional, Tuple
from .errors import SentenceError, SentenceValidationError
from .clause_parser import get_clause_parser


class WordOrderValidator:
    """Validates SOV word order and basic sentence structure."""
    
    def __init__(self):
        """Initialize word order validation rules."""
        # Import lexicon validator for word type checking
        from .lexicon import LexiconValidator
        self.lexicon_validator = None
        
    def set_lexicon_validator(self, lexicon_validator):
        """Set the lexicon validator for word type checking."""
        self.lexicon_validator = lexicon_validator
        
    def validate_order(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate SOV word order requirements."""
        errors = []
        
        # Skip if sentence is too short to have order violations
        if len(tokens) < 2:
            return errors
            
        # Find the main verb (rightmost verb in basic SOV)
        main_verb_pos = self._find_main_verb(tokens)
        if main_verb_pos is None:
            return errors  # No verb found, other validators will catch this
            
        # Check for content words after the main verb
        content_words_after_verb = self._find_content_words_after_verb(
            tokens, main_verb_pos
        )
        
        if content_words_after_verb:
            error = SentenceValidationError(
                error_type=SentenceError.WORD_ORDER,
                message=f"SOV violation: content words after verb: {content_words_after_verb}",
                position=main_verb_pos
            )
            errors.append(error)
            
        return errors
        
    def _find_main_verb(self, tokens: List[str]) -> Optional[int]:
        """Find the position of the main verb in the sentence."""
        if not self.lexicon_validator:
            return None
            
        # Look for verbs from right to left (SOV pattern)
        for i in range(len(tokens) - 1, -1, -1):
            token = tokens[i]
            word_type = self.lexicon_validator.identify_word_type(token)
            
            # Normalize word type to handle plural forms
            normalized_word_type = self._normalize_word_type(word_type)
            
            if normalized_word_type == 'verb':
                return i
                
        return None
        
    def _find_content_words_after_verb(self, tokens: List[str], 
                                     verb_pos: int) -> List[str]:
        """Find content words that appear after the main verb."""
        if not self.lexicon_validator:
            return []
            
        content_words = []
        
        # Check all tokens after the verb
        for i in range(verb_pos + 1, len(tokens)):
            token = tokens[i]
            word_type = self.lexicon_validator.identify_word_type(token)
            
            # Normalize word type
            normalized_word_type = self._normalize_word_type(word_type)
            
            # Content words that shouldn't appear after verb in SOV
            if normalized_word_type in ['noun', 'verb', 'adjective', 'adverb']:
                content_words.append(token)
                
        return content_words
        
    def _normalize_word_type(self, word_type: str) -> Optional[str]:
        """Normalize word type from lexicon validator."""
        if not word_type:
            return None
            
        # Convert plural forms to singular
        if word_type.endswith('s') and word_type != 'pronouns':
            return word_type[:-1]
        elif word_type == 'pronouns':
            return 'pronoun'
        else:
            return word_type 