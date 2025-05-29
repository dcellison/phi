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
        """Validate SOV word order requirements and sentence completeness."""
        errors = []
        
        # 1. Check sentence completeness first
        errors.extend(self._validate_sentence_completeness(tokens))
        
        # 2. Check for excessive repetition
        errors.extend(self._validate_repetition(tokens))
        
        # 3. Check SOV word order if we have enough tokens
        if len(tokens) >= 2:
            # Find the main verb (rightmost verb in basic SOV)
            main_verb_pos = self._find_main_verb(tokens)
            if main_verb_pos is not None:
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
                
                # 4. Check for SOV pattern violations
                errors.extend(self._validate_sov_pattern(tokens, main_verb_pos))
            
        return errors
        
    def _validate_sentence_completeness(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate that the sentence has minimum required structure."""
        errors = []
        
        if not tokens:
            return errors  # Empty sentences handled elsewhere
            
        # Find if we have a main verb
        main_verb_pos = self._find_main_verb(tokens)
        
        if main_verb_pos is None:
            # No verb found - check if this is a valid verbless construction
            has_valid_structure = self._is_valid_verbless_sentence(tokens)
            
            if not has_valid_structure:
                errors.append(SentenceValidationError(
                    error_type=SentenceError.MISSING_VERB,
                    message="Incomplete sentence: missing verb. Phi sentences require a verb or valid copular structure",
                    position=0
                ))
        else:
            # We have a verb - check if we have required elements for this construction
            errors.extend(self._validate_required_elements(tokens, main_verb_pos))
        
        return errors
    
    def _validate_required_elements(self, tokens: List[str], verb_pos: int) -> List[SentenceValidationError]:
        """Validate that required elements are present for specific constructions."""
        errors = []
        
        if not self.lexicon_validator:
            return errors
        
        # Use the clause parser to properly analyze sentence structure
        clause_parser = get_clause_parser(self.lexicon_validator)
        clauses = clause_parser.split_into_clauses(tokens)
        
        # Check each clause for tense marker requirements
        for clause_tokens, clause_start_idx in clauses:
            if not clause_tokens:
                continue
                
            # Check if this clause has tense markers that require a subject
            tense_particles = {'li', 'ta', 'su'}  # past, present, future
            has_tense_marker = any(token in tense_particles for token in clause_tokens)
            
            if has_tense_marker:
                # Check if this is an existential construction with the copula
                clause_verb_pos = self._find_main_verb(clause_tokens)
                if clause_verb_pos is not None and clause_verb_pos < len(clause_tokens):
                    main_verb = clause_tokens[clause_verb_pos]
                    is_existential = (main_verb == 'thilu')  # thilu = be (copula)
                    
                    if not is_existential:
                        # Non-existential tense markers require a subject within the clause
                        has_subject = self._has_subject(clause_tokens)
                        
                        if not has_subject:
                            # Find the position of the tense marker for error reporting
                            tense_pos = None
                            tense_marker = None
                            for i, token in enumerate(clause_tokens):
                                if token in tense_particles:
                                    tense_pos = clause_start_idx + i
                                    tense_marker = token
                                    break
                            
                            errors.append(SentenceValidationError(
                                error_type=SentenceError.MISSING_VERB,
                                message=f"Incomplete sentence: tense marker '{tense_marker}' requires a subject. "
                                f"Past, present, and future tense constructions must specify who performs the action, "
                                f"unlike bare verbs which can be valid imperatives.",
                                position=tense_pos if tense_pos is not None else clause_start_idx
                            ))
        
        return errors
    
    def _has_subject(self, tokens: List[str]) -> bool:
        """Check if the sentence has a subject (pronoun, noun, or noun phrase)."""
        if not self.lexicon_validator:
            return False
        
        subject_pronouns = {'mia', 'thi', 'sha'}  # I, you, they
        
        for i, token in enumerate(tokens):
            # Check for subject pronouns
            if token in subject_pronouns:
                return True
            
            # Check for derived noun subjects (ra + verb)
            if token == 'ra' and i + 1 < len(tokens):
                next_token = tokens[i + 1]
                next_word_type = self.lexicon_validator.identify_word_type(next_token)
                next_normalized_type = self._normalize_word_type(next_word_type)
                if next_normalized_type == 'verb':
                    # ra + verb creates a derived noun that can be a subject
                    return True
            
            # Check for regular nouns (which can be subjects)
            word_type = self.lexicon_validator.identify_word_type(token)
            normalized_type = self._normalize_word_type(word_type)
            if normalized_type == 'noun':
                return True
        
        return False

    def _is_valid_verbless_sentence(self, tokens: List[str]) -> bool:
        """Check if a sentence without a verb is still valid (very limited cases)."""
        # In Phi, virtually all valid sentences need a verb
        # The only exceptions might be very specific discourse contexts
        # For now, we'll be strict and require verbs
        
        # Special case: single interjections might be valid
        if len(tokens) == 1:
            token = tokens[0]
            if self.lexicon_validator:
                word_type = self._normalize_word_type(
                    self.lexicon_validator.identify_word_type(token)
                )
                if word_type == 'interjection':
                    return True
        
        # All other verbless constructions are invalid
        return False
        
    def _find_main_verb(self, tokens: List[str]) -> Optional[int]:
        """Find the position of the main verb in the sentence, including derivational verbs."""
        if not self.lexicon_validator:
            return None
            
        # Look for verbs from right to left (SOV pattern)
        for i in range(len(tokens) - 1, -1, -1):
            token = tokens[i]
            word_type = self.lexicon_validator.identify_word_type(token)
            
            # Normalize word type to handle plural forms
            normalized_word_type = self._normalize_word_type(word_type)
            
            # 1. Check for regular verbs
            if normalized_word_type == 'verb':
                return i
            
            # 2. Check for derivational verb constructions (se + noun)
            if token == 'se' and i + 1 < len(tokens):
                # Check if followed by a noun (making it a derivational verb)
                next_token = tokens[i + 1]
                next_word_type = self.lexicon_validator.identify_word_type(next_token)
                next_normalized_type = self._normalize_word_type(next_word_type)
                
                if next_normalized_type == 'noun':
                    # se + noun functions as a verb, return the position of 'se'
                    return i
                    
        return None
        
    def _find_content_words_after_verb(self, tokens: List[str], 
                                     verb_pos: int) -> List[str]:
        """Find content words that appear after the main verb."""
        if not self.lexicon_validator:
            return []
            
        content_words = []
        
        # Determine the actual end position of the verb construction
        verb_end_pos = verb_pos
        
        # Check if this is a derivational verb construction (se + noun)
        if verb_pos < len(tokens) and tokens[verb_pos] == 'se':
            if verb_pos + 1 < len(tokens):
                next_token = tokens[verb_pos + 1]
                next_word_type = self.lexicon_validator.identify_word_type(next_token)
                next_normalized_type = self._normalize_word_type(next_word_type)
                
                if next_normalized_type == 'noun':
                    # se + noun construction spans two positions
                    verb_end_pos = verb_pos + 1
        
        # Check all tokens after the complete verb construction
        for i in range(verb_end_pos + 1, len(tokens)):
            token = tokens[i]
            word_type = self.lexicon_validator.identify_word_type(token)
            
            # Normalize word type
            normalized_word_type = self._normalize_word_type(word_type)
            
            # Content words that shouldn't appear after verb in SOV
            if normalized_word_type in ['noun', 'verb', 'adjective', 'adverb']:
                content_words.append(token)
                
        return content_words
        
    def _normalize_word_type(self, word_type: str) -> Optional[str]:
        """Normalize word type from lexicon validator (no longer needed - lexicon validator now returns normalized forms)."""
        return word_type 

    def _validate_sov_pattern(self, tokens: List[str], verb_pos: int) -> List[SentenceValidationError]:
        """Validate strict SOV pattern compliance within clause boundaries."""
        errors = []
        
        if not self.lexicon_validator:
            return errors
            
        # Use the existing shared clause parser
        clause_parser = get_clause_parser(self.lexicon_validator)
        clauses = clause_parser.split_into_clauses(tokens)
        
        # Find which clause contains the main verb
        main_verb_clause = None
        for clause_tokens, clause_start_idx in clauses:
            clause_end_idx = clause_start_idx + len(clause_tokens) - 1
            if clause_start_idx <= verb_pos <= clause_end_idx:
                main_verb_clause = (clause_start_idx, clause_end_idx)
                break
        
        if main_verb_clause is None:
            return errors  # Can't determine clause structure
            
        clause_start, clause_end = main_verb_clause
        
        # Only validate SOV within the same clause as the main verb
        
        # 1. Check for verbs appearing before the main verb within the same clause
        for i in range(clause_start, verb_pos):
            token = tokens[i]
            word_type = self.lexicon_validator.identify_word_type(token)
            normalized_type = self._normalize_word_type(word_type)
            
            # Skip particles and functional words
            if normalized_type == 'verb' and i != verb_pos:
                # Check if this verb is part of a ra + verb (derived noun) construction
                if i > 0 and tokens[i - 1] == 'ra':
                    # This is ra + verb = derived noun, not a verb violation
                    continue
                    
                # Found another verb before the main verb in the same clause
                errors.append(SentenceValidationError(
                    error_type=SentenceError.WORD_ORDER,
                    message=f"SOV violation: verb '{token}' appears before main verb at position {verb_pos} within the same clause. In SOV order, verbs should be final.",
                    position=i
                ))
        
        # 2. Check for subject pronouns appearing after the main verb within the same clause
        subject_pronouns = {'mia', 'thi', 'sha'}  # I, you, they
        for i in range(verb_pos + 1, min(clause_end + 1, len(tokens))):
            if tokens[i] in subject_pronouns:
                errors.append(SentenceValidationError(
                    error_type=SentenceError.WORD_ORDER,
                    message=f"SOV violation: subject pronoun '{tokens[i]}' appears after verb within the same clause. Subjects must precede verbs in SOV order.",
                    position=i
                ))
        
        # 3. Check for scrambled patterns within the same clause only
        tense_particles = {'li', 'ta', 'su'}
        
        for i in range(clause_start, min(clause_end - 1, len(tokens) - 2)):
            if (i + 2 < len(tokens) and
                tokens[i] in tense_particles and
                self._normalize_word_type(self.lexicon_validator.identify_word_type(tokens[i + 1])) == 'verb' and
                tokens[i + 2] in subject_pronouns):
                
                errors.append(SentenceValidationError(
                    error_type=SentenceError.WORD_ORDER,
                    message=f"SOV violation: scrambled word order '{' '.join(tokens[i:i+3])}' within clause. Expected subject-object-verb order, not tense-verb-subject.",
                    position=i
                ))
        
        return errors
        
    def _validate_repetition(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate against excessive repetition of content words."""
        errors = []
        
        if not self.lexicon_validator:
            return errors
            
        # Count consecutive occurrences of the same content word
        word_counts = {}
        consecutive_count = 1
        last_word = None
        last_word_type = None
        
        for i, token in enumerate(tokens):
            word_type = self.lexicon_validator.identify_word_type(token)
            normalized_type = self._normalize_word_type(word_type)
            
            # Only check content words (not particles)
            if normalized_type in ['noun', 'verb', 'adjective', 'adverb', 'pronoun']:
                if token == last_word:
                    consecutive_count += 1
                    # Flag excessive repetition (3+ times in a row)
                    if consecutive_count >= 3:
                        errors.append(SentenceValidationError(
                            error_type=SentenceError.WORD_ORDER,
                            message=f"Excessive repetition: '{token}' appears {consecutive_count} times consecutively. This is likely an error in Phi.",
                            position=i - consecutive_count + 1  # Position of first occurrence
                        ))
                        # Only report once per sequence
                        consecutive_count = 0  # Reset to avoid multiple reports
                else:
                    consecutive_count = 1
                    last_word = token
                    last_word_type = normalized_type
            else:
                # Reset on particles
                consecutive_count = 1
                last_word = None
                last_word_type = None
        
        return errors 