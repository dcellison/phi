#!/usr/bin/env python3
"""
Lexicon Validation Module

Handles word existence checking, part-of-speech identification,
and basic lexical validation for Phi sentences.
"""

from typing import List, Optional
from .errors import SentenceError, SentenceValidationError


class LexiconValidator:
    """Validates word existence and basic lexical properties."""
    
    def __init__(self, word_validator):
        """Initialize with a PhiValidator instance for lexicon access."""
        self.word_validator = word_validator
        self.lexicon = word_validator.lexicon
        
        # Build reverse lookup for word -> part of speech
        self.word_to_pos = {}
        for pos, entries in self.lexicon.items():
            for entry in entries:
                if entry.word not in self.word_to_pos:
                    self.word_to_pos[entry.word] = []
                self.word_to_pos[entry.word].append(pos)
    
    def validate_words(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate that all words exist in the lexicon."""
        errors = []
        
        for i, word in enumerate(tokens):
            word_errors = self.validate_word_exists(word)
            for error in word_errors:
                error.position = i
                error.word = word
            errors.extend(word_errors)
        
        return errors
    
    def validate_word_exists(self, word: str) -> List[SentenceValidationError]:
        """Check if a word exists in the lexicon."""
        errors = []
        
        if word not in self.word_to_pos:
            errors.append(SentenceValidationError(
                SentenceError.UNKNOWN_WORD,
                f"Word '{word}' not found in lexicon"
            ))
        
        return errors
    
    def identify_word_type(self, word: str) -> Optional[str]:
        """Identify the part of speech of a word."""
        if word in self.word_to_pos:
            # Return the first (primary) part of speech
            return self.word_to_pos[word][0]
        return None
    
    def get_word_meanings(self, word: str) -> List[str]:
        """Get all meanings for a word across all parts of speech."""
        meanings = []
        
        for pos, entries in self.lexicon.items():
            for entry in entries:
                if entry.word == word:
                    meanings.append(f"{pos}: {entry.meaning}")
        
        return meanings
    
    def is_particle(self, word: str) -> bool:
        """Check if a word is a particle."""
        return word in self.word_to_pos and 'particle' in self.word_to_pos[word]
    
    def is_noun(self, word: str) -> bool:
        """Check if a word is a noun."""
        return word in self.word_to_pos and 'noun' in self.word_to_pos[word]
    
    def is_verb(self, word: str) -> bool:
        """Check if a word is a verb."""
        return word in self.word_to_pos and 'verb' in self.word_to_pos[word]
    
    def is_adjective(self, word: str) -> bool:
        """Check if a word is an adjective."""
        return word in self.word_to_pos and 'adjective' in self.word_to_pos[word]
    
    def is_adverb(self, word: str) -> bool:
        """Check if a word is an adverb."""
        return word in self.word_to_pos and 'adverb' in self.word_to_pos[word]
    
    def get_all_parts_of_speech(self, word: str) -> List[str]:
        """Get all parts of speech for a word."""
        return self.word_to_pos.get(word, []) 