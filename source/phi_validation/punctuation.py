#!/usr/bin/env python3
"""
Punctuation Validation Module

Validates punctuation usage in Phi sentences. Phi uses minimalist punctuation:
- Space (word separation)
- Full stop/period (sentence ending)
- Everything else is handled by grammar and is therefore an error
"""

import re
from typing import List
from .errors import SentenceError, SentenceValidationError


class PunctuationValidator:
    """Validates Phi's minimalist punctuation rules."""
    
    def __init__(self):
        """Initialize punctuation validation rules."""
        # Lexicon validator for word type identification
        self.lexicon_validator = None  # Will be set by core
        
        # Phi's allowed punctuation
        self.allowed_punctuation = {
            ' ',  # space (word separation)
            '.',  # full stop (sentence ending)
        }
        
        # All other punctuation is forbidden
        self.forbidden_punctuation = {
            ',', ';', ':', '!', '?', '"', "'", '(', ')', '[', ']', '{', '}',
            '-', '_', '/', '\\', '|', '@', '#', '$', '%', '^', '&', '*',
            '+', '=', '<', '>', '~', '`'
        }
        
        # Punctuation validation rules
        self.validation_rules = {
            'sentence_ending': {
                'required': '.',
                'logic': 'All Phi sentences must end with a full stop'
            },
            'forbidden_marks': {
                'not_allowed': self.forbidden_punctuation,
                'logic': 'Phi uses only spaces and full stops - grammar handles all other functions'
            },
            'space_usage': {
                'word_separator': True,
                'no_double_spaces': True,
                'logic': 'Spaces separate words, no multiple consecutive spaces'
            }
        }
    
    def set_lexicon_validator(self, lexicon_validator):
        """Set the lexicon validator for word type identification."""
        self.lexicon_validator = lexicon_validator
    
    def validate_punctuation(self, text: str, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate all punctuation aspects of the text."""
        errors = []
        
        if not text.strip():
            return errors  # Empty text handled elsewhere
        
        # 1. Check for forbidden punctuation
        errors.extend(self._validate_forbidden_punctuation(text))
        
        # 2. Check sentence ending
        errors.extend(self._validate_sentence_ending(text))
        
        # 3. Check space usage
        errors.extend(self._validate_space_usage(text))
        
        return errors
    
    def _validate_forbidden_punctuation(self, text: str) -> List[SentenceValidationError]:
        """Check for any forbidden punctuation marks."""
        errors = []
        
        # Find all punctuation characters in the text
        for i, char in enumerate(text):
            if char in self.forbidden_punctuation:
                errors.append(SentenceValidationError(
                    SentenceError.PUNCTUATION_ERROR,
                    f"Forbidden punctuation '{char}' found. {self.validation_rules['forbidden_marks']['logic']}",
                    position=i
                ))
        
        return errors
    
    def _validate_sentence_ending(self, text: str) -> List[SentenceValidationError]:
        """Check that sentence ends with a full stop."""
        errors = []
        
        stripped_text = text.strip()
        if not stripped_text:
            return errors
        
        if not stripped_text.endswith('.'):
            errors.append(SentenceValidationError(
                SentenceError.PUNCTUATION_ERROR,
                f"Sentence must end with a full stop. {self.validation_rules['sentence_ending']['logic']}",
                position=len(stripped_text)
            ))
        
        return errors
    
    def _validate_space_usage(self, text: str) -> List[SentenceValidationError]:
        """Check proper space usage."""
        errors = []
        
        # Check for multiple consecutive spaces
        if '  ' in text:  # two or more spaces
            double_space_pos = text.find('  ')
            errors.append(SentenceValidationError(
                SentenceError.PUNCTUATION_ERROR,
                f"Multiple consecutive spaces found. {self.validation_rules['space_usage']['logic']}",
                position=double_space_pos
            ))
        
        # Check for leading/trailing spaces (beyond normal stripping)
        if text.startswith(' ') or text.endswith(' '):
            errors.append(SentenceValidationError(
                SentenceError.PUNCTUATION_ERROR,
                f"Unnecessary leading or trailing spaces. {self.validation_rules['space_usage']['logic']}",
                position=0 if text.startswith(' ') else len(text) - 1
            ))
        
        return errors
    
    def clean_text_for_tokenization(self, text: str) -> str:
        """Clean text for tokenization, removing only the allowed full stop."""
        # Remove only the sentence-ending period for tokenization
        # Keep spaces as they are word separators
        cleaned = text.strip()
        if cleaned.endswith('.'):
            cleaned = cleaned[:-1]
        return cleaned
    
    def is_valid_phi_punctuation(self, text: str) -> bool:
        """Quick check if text contains only valid Phi punctuation."""
        for char in text:
            if not (char.isalnum() or char in self.allowed_punctuation):
                return False
        return True 