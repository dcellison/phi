#!/usr/bin/env python3
"""
Narrative Validation Module

Validates narrative structures, relative clauses, and sequence logic in Phi.
Handles temporal conjunctions, relative clause tense consistency, and narrative coherence.
"""

from typing import List, Dict, Tuple, Optional
from .errors import SentenceError, SentenceValidationError


class NarrativeValidator:
    """Validates narrative structures and temporal sequences."""
    
    def __init__(self):
        """Initialize narrative validation rules."""
        # Lexicon validator for word type identification
        self.lexicon_validator = None  # Will be set by core
        
        # Tense particles for tense detection
        self.tense_particles = {'li', 'ta', 'su'}  # past, present, future
        
        # Temporal conjunction sequence logic
        self.temporal_sequence_rules = {
            'pimo': {  # before
                'temporal_relationship': 'precedence',
                'main_clause_time': 'reference_point',
                'subordinate_clause_time': 'after_reference',
                'logical_sequences': {
                    # Main clause tense → subordinate clause tense → validity
                    ('li', 'li'): True,   # "I walked before I ran" (both past, sequence clear)
                    ('li', 'ta'): True,   # "I walked before I walk" (past before present - logical!)
                    ('li', 'su'): True,   # "I walked before I will walk" (past before future)
                    ('ta', 'li'): False,  # "I walk before I walked" (present before past - illogical)
                    ('ta', 'ta'): True,   # "I walk before I walk" (habitual sequence)
                    ('ta', 'su'): True,   # "I walk before I will walk" (present leads to future)
                    ('su', 'li'): False,  # "I will walk before I walked" (future before past - illogical)
                    ('su', 'ta'): True,   # "I will walk before I walk" (future before present - can be logical)
                    ('su', 'su'): True,   # "I will walk before I will run" (future sequence)
                },
                'logic': 'Before-clauses establish temporal precedence relationships'
            },
            
            'matu': {  # after
                'temporal_relationship': 'subsequence',
                'main_clause_time': 'reference_point',
                'subordinate_clause_time': 'before_reference',
                'logical_sequences': {
                    ('li', 'li'): True,   # "I walked after I ran" (both past, sequence clear)
                    ('li', 'ta'): True,   # "I walked after I walk" (past after present)
                    ('li', 'su'): False,  # "I walked after I will walk" (past after future - impossible)
                    ('ta', 'li'): True,   # "I walk after I walked" (present result of past)
                    ('ta', 'ta'): True,   # "I walk after I walk" (habitual sequence)
                    ('ta', 'su'): True,   # "I walk after I will walk" (present after future)
                    ('su', 'li'): False,  # "I will walk after I walked" (future after past - impossible)
                    ('su', 'ta'): True,   # "I will walk after I walk" (future after present)
                    ('su', 'su'): True,   # "I will walk after I will run" (future sequence)
                },
                'logic': 'After-clauses establish temporal subsequence relationships'
            },
            
            'tura': {  # since/because (causal-temporal)
                'temporal_relationship': 'causation',
                'main_clause_time': 'result_time',
                'subordinate_clause_time': 'cause_time',
                'logical_sequences': {
                    ('li', 'li'): True,   # "I walked since I was tired" (past cause, past result)
                    ('li', 'ta'): False,  # "I walked since I am tired" (present cause, past result)
                    ('li', 'su'): False,  # "I walked since I will be tired" (impossible)
                    ('ta', 'li'): True,   # "I walk since I was tired" (past cause, present result)
                    ('ta', 'ta'): True,   # "I walk since I am tired" (present cause, present result)
                    ('ta', 'su'): False,  # "I walk since I will be tired" (impossible)
                    ('su', 'li'): True,   # "I will walk since I was tired" (past cause, future result)
                    ('su', 'ta'): True,   # "I will walk since I am tired" (present cause, future result)
                    ('su', 'su'): False,  # "I will walk since I will be tired" (circular)
                },
                'logic': 'Since-clauses establish causal-temporal relationships'
            }
        }
        
        # Relative clause tense consistency rules
        self.relative_clause_rules = {
            'markers': ['mi', 'lu'],  # relative clause markers
            'tense_relationships': {
                'simultaneous': {
                    # Main and relative clause refer to same time
                    'compatible_pairs': [('li', 'li'), ('ta', 'ta'), ('su', 'su')],
                    'logic': 'Simultaneous events use matching tenses'
                },
                'sequential': {
                    # Relative clause describes prior state/action
                    'compatible_pairs': [('ta', 'li'), ('su', 'li'), ('su', 'ta')],
                    'logic': 'Sequential events follow temporal logic'
                },
                'characterizing': {
                    # Relative clause describes general property
                    'main_tense': 'any',
                    'relative_tense': 'ta',  # present for general properties is usually OK
                    'logic': 'Characterizing relatives use present tense'
                }
            },
            'scope_rules': {
                'head_noun_agreement': True,  # relative must agree with head noun
                'tense_inheritance': False,   # relative clause has independent tense
                'aspect_inheritance': True,   # aspect can be inherited
                'logic': 'Relative clauses maintain referential consistency'
            }
        }
        
        # Additional temporal conjunctions for comprehensive coverage
        self.temporal_conjunctions = {
            'pimo', 'matu', 'tura',  # covered in temporal_sequence_rules
            'wetu', 'wane', 'lina', 'runa'  # additional conjunctions
        }
    
    def set_lexicon_validator(self, lexicon_validator):
        """Set the lexicon validator for word type identification."""
        self.lexicon_validator = lexicon_validator
    
    def validate_narrative_structure(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate narrative sequence logic and relative clause consistency."""
        errors = []
        
        # 1. Validate temporal conjunction sequences
        errors.extend(self._validate_temporal_sequences(tokens))
        
        # 2. Validate relative clause tense consistency
        errors.extend(self._validate_relative_clause_tenses(tokens))
        
        # 3. Validate narrative coherence patterns
        errors.extend(self._validate_narrative_coherence(tokens))
        
        return errors
    
    def _validate_temporal_sequences(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate logical temporal sequences with conjunctions."""
        errors = []
        
        for i, token in enumerate(tokens):
            if token in self.temporal_sequence_rules:
                sequence_rules = self.temporal_sequence_rules[token]
                
                # Find tenses in main clause (before conjunction) and subordinate clause (after)
                main_tense = self._find_clause_tense(tokens, 0, i)
                subordinate_tense = self._find_clause_tense(tokens, i + 1, len(tokens))
                
                if main_tense and subordinate_tense:
                    tense_pair = (main_tense, subordinate_tense)
                    
                    # Check if this tense combination is logical
                    if tense_pair in sequence_rules['logical_sequences']:
                        is_valid = sequence_rules['logical_sequences'][tense_pair]
                        if not is_valid:
                            errors.append(SentenceValidationError(
                                SentenceError.TEMPORAL_SEQUENCE_ERROR,
                                f"Illogical temporal sequence: '{token}' with main clause '{main_tense}' and subordinate clause '{subordinate_tense}'. {sequence_rules['logic']}",
                                position=i
                            ))
        
        return errors
    
    def _validate_relative_clause_tenses(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate relative clause tense consistency."""
        errors = []
        
        for i, token in enumerate(tokens):
            if token in self.relative_clause_rules['markers']:
                # Find the main clause tense (before relative marker)
                main_tense = self._find_clause_tense(tokens, 0, i)
                
                # Find the relative clause tense (after relative marker)
                relative_tense = self._find_clause_tense(tokens, i + 1, len(tokens))
                
                if main_tense and relative_tense:
                    tense_pair = (main_tense, relative_tense)
                    
                    # Check tense compatibility
                    is_compatible = self._check_relative_tense_compatibility(tense_pair)
                    
                    if not is_compatible:
                        errors.append(SentenceValidationError(
                            SentenceError.RELATIVE_CLAUSE_TENSE_ERROR,
                            f"Relative clause tense '{relative_tense}' incompatible with main clause tense '{main_tense}' after marker '{token}'",
                            position=i
                        ))
        
        return errors
    
    def _validate_narrative_coherence(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate overall narrative coherence and flow."""
        errors = []
        
        # Check for multiple temporal conjunctions that might create confusion
        temporal_conjunctions_found = []
        for i, token in enumerate(tokens):
            if token in self.temporal_conjunctions:
                temporal_conjunctions_found.append((token, i))
        
        # If multiple temporal conjunctions, check for coherent sequencing
        if len(temporal_conjunctions_found) > 1:
            errors.extend(self._validate_multiple_temporal_conjunctions(temporal_conjunctions_found, tokens))
        
        # Check for narrative consistency with evidentiality
        errors.extend(self._validate_narrative_evidentiality_consistency(tokens))
        
        return errors
    
    def _validate_multiple_temporal_conjunctions(self, conjunctions: List[Tuple[str, int]], 
                                               tokens: List[str]) -> List[SentenceValidationError]:
        """Validate coherence when multiple temporal conjunctions are present."""
        errors = []
        
        # For now, this is a basic check - could be expanded with more sophisticated logic
        if len(conjunctions) > 2:
            errors.append(SentenceValidationError(
                SentenceError.TEMPORAL_SEQUENCE_ERROR,
                f"Multiple temporal conjunctions may create narrative confusion: {[c[0] for c in conjunctions]}",
                position=conjunctions[1][1]  # Position of second conjunction
            ))
        
        return errors
    
    def _validate_narrative_evidentiality_consistency(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate consistency between narrative structure and evidentiality."""
        errors = []
        
        # Check for evidentiality particles that might conflict with temporal structure
        evidentiality_particles = ['hi', 'ro', 'nu', 'ti', 'mu', 'pe']
        temporal_conjunctions = [token for token in tokens if token in self.temporal_conjunctions]
        evidentiality_found = [token for token in tokens if token in evidentiality_particles]
        
        # If both temporal structure and evidentiality are present, check for consistency
        if temporal_conjunctions and evidentiality_found:
            # Memory evidentiality (mu) with future temporal conjunctions might be odd
            if 'mu' in evidentiality_found and any(conj in ['pimo', 'matu'] for conj in temporal_conjunctions):
                # Find future tense markers
                future_markers = [i for i, token in enumerate(tokens) if token == 'su']
                if future_markers:
                    errors.append(SentenceValidationError(
                        SentenceError.TEMPORAL_SEQUENCE_ERROR,
                        f"Memory evidentiality 'mu' with future temporal structure may be inconsistent",
                        position=tokens.index('mu') if 'mu' in tokens else 0
                    ))
        
        return errors
    
    def _find_clause_tense(self, tokens: List[str], start: int, end: int) -> Optional[str]:
        """Find the tense marker in a clause segment."""
        for i in range(start, end):
            if i < len(tokens) and tokens[i] in self.tense_particles:
                return tokens[i]
        
        # If no explicit tense found, default to present
        # But only if there's a verb in this segment
        for i in range(start, end):
            if i < len(tokens) and self._identify_word_type(tokens[i]) == 'verb':
                return 'ta'  # unmarked present
        
        return None
    
    def _check_relative_tense_compatibility(self, tense_pair: Tuple[str, str]) -> bool:
        """Check if a main-relative tense pair is compatible."""
        main_tense, relative_tense = tense_pair
        
        # Check simultaneous relationships
        if tense_pair in self.relative_clause_rules['tense_relationships']['simultaneous']['compatible_pairs']:
            return True
        
        # Check sequential relationships
        if tense_pair in self.relative_clause_rules['tense_relationships']['sequential']['compatible_pairs']:
            return True
        
        # Check characterizing relationships (relative clause describes general property)
        if relative_tense == 'ta':  # present tense for general properties is usually OK
            return True
        
        # Default: incompatible
        return False
    
    def _identify_word_type(self, word: str) -> Optional[str]:
        """Identify the part of speech of a word using the lexicon validator."""
        if self.lexicon_validator:
            return self.lexicon_validator.identify_word_type(word)
        return None 