#!/usr/bin/env python3
"""
Lexicon Validation Module

Handles word existence checking, part-of-speech identification,
and basic lexical validation for Phi sentences.
"""

import sys
from pathlib import Path
from typing import List, Optional, Dict
from .errors import SentenceError, SentenceValidationError

# Add parent directory to path to import phi_lexicon_reader
sys.path.append(str(Path(__file__).parent.parent))
from phi_lexicon_reader import PhiLexiconReader


class LexiconValidator:
    """Validates word existence and basic lexical properties."""
    
    def __init__(self, word_validator=None):
        """Initialize with PhiLexiconReader for proper POS data loading."""
        # Use PhiLexiconReader to load the complete lexicon
        pos_dir = Path(__file__).parent.parent / "pos"
        self.lexicon_reader = PhiLexiconReader(str(pos_dir))
        self.lexicon = self.lexicon_reader.read_lexicon()
        
        # Build reverse lookup for word -> part of speech
        self.word_to_pos = {}
        for word, info in self.lexicon.items():
            pos = info['pos']
            if word not in self.word_to_pos:
                self.word_to_pos[word] = []
            self.word_to_pos[word].append(pos)
    
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
        
        if not self.lexicon_reader.word_exists(word):
            errors.append(SentenceValidationError(
                SentenceError.UNKNOWN_WORD,
                f"Word '{word}' not found in lexicon"
            ))
        
        return errors
    
    def identify_word_type(self, word: str) -> Optional[str]:
        """Identify the part of speech of a word."""
        word_info = self.lexicon_reader.get_word_info(word)
        if word_info:
            return word_info['pos']
        return None
    
    def get_word_meanings(self, word: str) -> List[str]:
        """Get all meanings for a word."""
        word_info = self.lexicon_reader.get_word_info(word)
        if word_info:
            return [f"{word_info['pos']}: {word_info['translation']}"]
        return []
    
    def is_particle(self, word: str) -> bool:
        """Check if a word is a particle."""
        word_type = self.identify_word_type(word)
        return word_type == 'particles'
    
    def is_noun(self, word: str) -> bool:
        """Check if a word is a noun."""
        word_type = self.identify_word_type(word)
        return word_type == 'nouns'
    
    def is_verb(self, word: str) -> bool:
        """Check if a word is a verb."""
        word_type = self.identify_word_type(word)
        return word_type == 'verbs'
    
    def is_adjective(self, word: str) -> bool:
        """Check if a word is an adjective."""
        word_type = self.identify_word_type(word)
        return word_type == 'adjectives'
    
    def is_adverb(self, word: str) -> bool:
        """Check if a word is an adverb."""
        word_type = self.identify_word_type(word)
        return word_type == 'adverbs'
    
    def get_all_parts_of_speech(self, word: str) -> List[str]:
        """Get all parts of speech for a word."""
        return self.word_to_pos.get(word, []) 