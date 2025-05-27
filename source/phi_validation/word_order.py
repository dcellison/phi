#!/usr/bin/env python3
"""
Word Order Validation Module

Validates SOV (Subject-Object-Verb) word order compliance
and basic sentence structure in Phi.
"""

from typing import List, Optional
from .errors import SentenceError, SentenceValidationError


class WordOrderValidator:
    """Validates SOV word order and basic sentence structure."""
    
    def __init__(self):
        """Initialize word order validation rules."""
        # Import lexicon validator for word type identification
        self.lexicon_validator = None  # Will be set by core
        
        # Manually define all particles since particles.md uses different format
        self.all_particles = {
            # Slot 0 particles (sentence frame)
            'wa', 'ho', 'tu', 'hu',  # sentence type
            'hi', 'ro', 'nu', 'ti', 'mu', 'pe',  # evidentiality
            'ha', 'mi', 'lu',  # discourse and relative
            'so',  # politeness
            
            # Slot 1 particles (verb phrase)
            'li', 'ta', 'su',  # tense
            'we', 'la', 'ni', 'po', 'pu', 'ri', 'wi', 'wu',  # aspect
            'to', 'ru',  # mood (imperative, obligative)
            'me',  # negation
            
            # Slot 2 particles (core word)
            'si', 'na', 'te',  # POS markers
            'se', 'ra',  # derivation
            'he', 'pi', 'ne',  # animacy
            'pa', 'mo', 'sa', 'le', 're',  # comparison
            'wo', 'lo', 'no',  # number
            'ma'  # emphasis
        }
        
        # Particle categories and their ordering rules
        self.slot_0_particles = {
            # Sentence frame particles
            'wa', 'ho', 'tu', 'hu',  # sentence type
            'hi', 'ro', 'nu', 'ti', 'mu', 'pe',  # evidentiality
            'ha', 'mi', 'lu',  # discourse and relative
            'so'  # politeness
        }
        
        self.slot_1_particles = {
            # Verb phrase particles
            'li', 'ta', 'su',  # tense
            'we', 'la', 'ni', 'po', 'pu', 'ri', 'wi', 'wu',  # aspect
            'to', 'ru',  # mood
            'me'  # negation
        }
        
        self.slot_2_particles = {
            # Core word particles
            'si', 'na', 'te',  # POS markers
            'se', 'ra',  # derivation
            'he', 'pi', 'ne',  # animacy
            'pa', 'mo', 'sa', 'le', 're',  # comparison
            'wo', 'lo', 'no',  # number
            'ma'  # emphasis
        }
    
    def set_lexicon_validator(self, lexicon_validator):
        """Set the lexicon validator for word type identification."""
        self.lexicon_validator = lexicon_validator
    
    def validate_order(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate SOV word order compliance."""
        errors = []
        
        if len(tokens) == 0:
            errors.append(SentenceValidationError(
                SentenceError.WORD_ORDER,
                "Empty sentence has no word order"
            ))
            return errors
        
        # Main SOV validation
        errors.extend(self.validate_sov_order(tokens))
        
        return errors
    
    def validate_sov_order(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate Subject-Object-Verb word order."""
        errors = []
        
        # Filter out particles to focus on content words, but handle derivational constructions
        content_words = []
        i = 0
        while i < len(tokens):
            token = tokens[i]
            word_type = self.identify_word_type(token)
            
            # Handle derivational constructions
            if token == 'ra' and i + 1 < len(tokens):
                # ra + verb = derived noun
                next_token = tokens[i + 1]
                next_word_type = self.identify_word_type(next_token)
                if next_word_type == 'verb':
                    # Treat ra+verb as a noun
                    content_words.append((f"ra {next_token}", 'noun', i))
                    i += 2  # Skip both ra and the verb
                    continue
            elif token == 'se' and i + 1 < len(tokens):
                # se + noun = derived verb
                next_token = tokens[i + 1]
                next_word_type = self.identify_word_type(next_token)
                if next_word_type == 'noun':
                    # Treat se+noun as a verb
                    content_words.append((f"se {next_token}", 'verb', i))
                    i += 2  # Skip both se and the noun
                    continue
            
            # Regular content words
            if word_type and not word_type.endswith('_particle'):
                content_words.append((token, word_type, i))
            
            i += 1
        
        # Find verbs (including derived verbs)
        verbs = [(word, pos, idx) for word, pos, idx in content_words if pos == 'verb']
        
        if len(verbs) == 0:
            errors.append(SentenceValidationError(
                SentenceError.MISSING_VERB,
                "Sentence missing main verb"
            ))
        elif len(verbs) > 1:
            errors.append(SentenceValidationError(
                SentenceError.MULTIPLE_VERBS,
                f"Multiple main verbs found: {[v[0] for v in verbs]}"
            ))
        else:
            # Check if verb is at the end (SOV order)
            verb_word, verb_pos, verb_idx = verbs[0]
            
            # Find content words after the verb
            words_after_verb = [w for w in content_words if w[2] > verb_idx]
            
            if words_after_verb:
                errors.append(SentenceValidationError(
                    SentenceError.WORD_ORDER,
                    f"SOV violation: content words after verb: {[w[0] for w in words_after_verb]}",
                    position=verb_idx
                ))
        
        return errors
    
    def identify_word_type(self, word: str) -> Optional[str]:
        """Identify the part of speech of a word."""
        # Check if it's a particle first
        if word in self.all_particles:
            if word in self.slot_0_particles:
                return "slot_0_particle"
            elif word in self.slot_1_particles:
                return "slot_1_particle"
            elif word in self.slot_2_particles:
                return "slot_2_particle"
        
        # Check lexicon for content words
        if self.lexicon_validator:
            return self.lexicon_validator.identify_word_type(word)
        
        return None 