#!/usr/bin/env python3
"""
Temporal Validation Module

Validates tense, aspect, temporal logic, and temporal relationships
in Phi sentences.
"""

from typing import List, Dict, Tuple, Optional
from .errors import SentenceError, SentenceValidationError
from .clause_parser import get_clause_parser


class TemporalValidator:
    """Validates temporal structure and relationships."""
    
    def __init__(self):
        """Initialize temporal validation rules."""
        # Lexicon validator for word type identification
        self.lexicon_validator = None  # Will be set by core
        
        # Tense particles
        self.tense_particles = {'li', 'ta', 'su'}
        
        # Aspect particles
        self.aspect_particles = {'we', 'la', 'ni', 'po', 'pu', 'ri', 'wi', 'wu'}
        
        # Mood particles
        self.mood_particles = {'to', 'ru', 'me'}
        
        # Subordinate conjunctions with tense requirements
        self.subordinate_conjunctions = {
            'pimo': {
                'expected_tenses': ['li', 'ta', 'su'],  # More flexible: before can reference any time
                'logic': 'Before-clauses can reference past, present, or future events'
            },
            'matu': {
                'expected_tenses': ['li', 'ta', 'su'],  # More flexible: after can reference any time
                'logic': 'After-clauses can reference past, present, or future events'
            },
            'wetu': {
                'expected_tenses': ['ta', 'su'],
                'logic': 'Conditional clauses use present or future tense'
            },
            'wane': {
                'expected_tenses': ['ta', 'li'],
                'logic': 'Temporal clauses can use present or past tense'
            }
        }
        
        # Aspect-tense compatibility rules
        self.aspect_tense_compatibility = {
            'we': {
                'compatible': ['li', 'ta', 'su'],
                'logic': 'Perfective aspect compatible with all tenses including future perfect'
            },
            'la': {
                'compatible': ['ta', 'su'],
                'logic': 'Progressive aspect incompatible with past tense'
            },
            'ni': {
                'compatible': ['ta', 'su'],
                'logic': 'Inchoative aspect requires present or future tense'
            },
            'po': {
                'compatible': ['ta', 'su'],
                'logic': 'Habitual aspect requires present or future tense'
            },
            'pu': {
                'compatible': ['li', 'ta'],
                'logic': 'Perfective aspect incompatible with future tense'
            },
            'ri': {
                'compatible': ['li', 'ta'],
                'logic': 'Iterative aspect incompatible with future tense'
            },
            'wi': {
                'compatible': ['ta', 'su'],
                'logic': 'Inceptive aspect requires present or future tense'
            },
            'wu': {
                'compatible': ['li', 'ta'],
                'logic': 'Cessative aspect incompatible with future tense'
            }
        }
        
        # Modal-tense compatibility rules
        self.modal_tense_compatibility = {
            'ru': {
                'incompatible': ['li'],
                'logic': 'Obligative mood incompatible with past tense'
            },
            'to': {
                'incompatible': ['li'],
                'logic': 'Imperative mood incompatible with past tense'
            },
            'me': {
                'compatible': ['li', 'ta', 'su'],
                'logic': 'Negation compatible with all tenses'
            }
        }
        
        # Temporal adverb-tense compatibility
        self.temporal_adverb_tense = {
            'hamite': ['li', 'ta', 'su'],  # how (works with all tenses)
            'tapine': ['su'],  # soon
            'walime': ['li'],  # before
            'nolute': ['li'],  # already
            'pimate': ['su'],  # later
            'hulane': ['ta', 'su'],  # always (present/future)
            'mitelu': ['li', 'ta']   # sometimes (past/present)
        }
        
        # Temporal sequence rules for conjunctions
        self.temporal_sequence_rules = {
            'pimo': {
                'logical_sequences': {
                    ('li', 'ta'): True,   # past cause, present result
                    ('li', 'li'): True,   # past cause, past result
                    ('ta', 'ta'): False,  # present cause, present result (illogical)
                    ('su', 'ta'): False,  # future cause, present result (illogical)
                },
                'logic': 'Causal relationships must respect temporal order'
            },
            'matu': {
                'logical_sequences': {
                    ('ta', 'su'): True,   # present condition, future result
                    ('su', 'su'): True,   # future condition, future result
                    ('li', 'su'): False,  # past condition, future result (illogical)
                },
                'logic': 'Conditional relationships require logical temporal order'
            }
        }
        
        # Relative clause tense rules
        self.relative_clause_rules = {
            'markers': ['lu', 'ha'],
            'tense_relationships': {
                'simultaneous': {
                    'compatible_pairs': [
                        ('ta', 'ta'),  # present main, present relative
                        ('li', 'li'),  # past main, past relative
                        ('su', 'su')   # future main, future relative
                    ]
                },
                'sequential': {
                    'compatible_pairs': [
                        ('ta', 'li'),  # present main, past relative
                        ('li', 'li'),  # past main, earlier past relative
                    ]
                }
            }
        }
        
        # Obligative construction rules
        self.obligative_rules = {
            'prohibited_particles': ['li', 'ta', 'su'],
            'logic': 'Obligative ru requires base verb form without tense'
        }
        
        # Conditional structure rules
        self.conditional_rules = {
            'protasis_tenses': ['ta', 'su'],  # if-clause tenses
            'apodosis_tenses': ['ta', 'su', 'ru'],  # then-clause tenses
            'prohibited_combinations': [
                ('li', 'ta'),  # past if, present then
                ('li', 'su'),  # past if, future then
            ],
            'logic': 'Conditional structures must maintain logical temporal relationships'
        }
        
        # Desiderative construction rules
        self.desiderative_rules = {
            'logic': 'Desiderative constructions require complement verb with te marker'
        }
    
    def set_lexicon_validator(self, lexicon_validator):
        """Set the lexicon validator for word type identification."""
        self.lexicon_validator = lexicon_validator
    
    def validate_temporal_structure(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate all temporal aspects of the sentence."""
        errors = []
        
        # 1. Validate subordinate clause tense requirements
        errors.extend(self.validate_subordinate_tense(tokens))
        
        # 2. Comprehensive tense validation
        errors.extend(self.validate_comprehensive_tense(tokens))
        
        return errors
    
    def validate_subordinate_tense(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate tense requirements in subordinate clauses."""
        errors = []
        
        for i, token in enumerate(tokens):
            if token in self.subordinate_conjunctions:
                conjunction_info = self.subordinate_conjunctions[token]
                expected_tenses = conjunction_info['expected_tenses']
                logic = conjunction_info['logic']
                
                # Look for tense particles after this conjunction
                found_tense = None
                tense_position = None
                
                # Search for tense particles in the subordinate clause
                for j in range(i + 1, len(tokens)):
                    next_token = tokens[j]
                    
                    # Stop if we hit another conjunction (end of this clause)
                    if next_token in self.subordinate_conjunctions:
                        break
                    
                    # Check for tense particles
                    if next_token in ['li', 'ta', 'su', 'ru', 'we', 'la', 'ni', 'po', 'pu', 'ri', 'wi', 'wu']:
                        if next_token in ['li', 'ta', 'su', 'ru']:  # Primary tense/mood particles
                            found_tense = next_token
                            tense_position = j
                            break
                        elif not found_tense:  # Aspect particles if no primary tense found
                            found_tense = next_token
                            tense_position = j
                
                # Validate tense appropriateness
                if found_tense and found_tense not in expected_tenses:
                    # Special case: allow unmarked present tense for some conjunctions
                    if token in ['wetu', 'wane'] and not found_tense:
                        continue  # Unmarked present is often acceptable
                    
                    errors.append(SentenceValidationError(
                        SentenceError.TENSE_INCONSISTENCY,
                        f"Subordinate clause with '{token}' uses '{found_tense}' but expects {expected_tenses}. {logic}",
                        position=tense_position if tense_position else i
                    ))
                
                # Check for missing tense in clauses that should have explicit tense
                elif not found_tense and token in ['pimo', 'matu']:
                    errors.append(SentenceValidationError(
                        SentenceError.TENSE_INCONSISTENCY,
                        f"Subordinate clause with '{token}' missing explicit tense. {logic}",
                        position=i
                    ))
        
        return errors
    
    def validate_comprehensive_tense(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Comprehensive tense validation including all temporal relationships."""
        errors = []
        
        # Split sentence into clauses using shared clause parser
        clauses = get_clause_parser(self.lexicon_validator).split_into_clauses(tokens)
        
        # Validate each clause separately for tense consistency
        for clause_tokens, clause_start_idx in clauses:
            if clause_tokens:  # Skip empty clauses
                clause_errors = self._validate_clause_tense(clause_tokens, clause_start_idx)
                errors.extend(clause_errors)
        
        return errors
    
    def _validate_clause_tense(self, tokens: List[str], start_idx: int) -> List[SentenceValidationError]:
        """Validate tense consistency within a single clause."""
        errors = []
        
        # Find all temporal elements in this clause
        tense_markers = []
        aspect_markers = []
        mood_markers = []
        temporal_adverbs = []
        
        for i, token in enumerate(tokens):
            if token in self.tense_particles:
                tense_markers.append((token, start_idx + i))
            elif token in self.aspect_particles:
                aspect_markers.append((token, start_idx + i))
            elif token in self.mood_particles:
                mood_markers.append((token, start_idx + i))
            elif token in self.temporal_adverb_tense:
                temporal_adverbs.append((token, start_idx + i))
        
        # 1. Check for multiple tense markers within this clause
        if len(tense_markers) > 1:
            errors.append(SentenceValidationError(
                SentenceError.MULTIPLE_TENSE_MARKERS,
                f"Multiple tense markers found: {[t[0] for t in tense_markers]}",
                position=tense_markers[1][1]
            ))
        
        # Get the primary tense (or None if unmarked present)
        primary_tense = tense_markers[0][0] if tense_markers else 'ta'  # default present
        
        # 2. Validate aspect-tense compatibility
        for aspect, pos in aspect_markers:
            if aspect in self.aspect_tense_compatibility:
                compat_info = self.aspect_tense_compatibility[aspect]
                if primary_tense not in compat_info['compatible']:
                    errors.append(SentenceValidationError(
                        SentenceError.ASPECT_TENSE_CONFLICT,
                        f"Aspect '{aspect}' incompatible with tense '{primary_tense}'. {compat_info['logic']}",
                        position=pos
                    ))
        
        # 3. Validate modal-tense compatibility
        for mood, pos in mood_markers:
            if mood in self.modal_tense_compatibility:
                compat_info = self.modal_tense_compatibility[mood]
                if 'incompatible' in compat_info and primary_tense in compat_info['incompatible']:
                    errors.append(SentenceValidationError(
                        SentenceError.MODAL_TENSE_CONFLICT,
                        f"Modal '{mood}' incompatible with tense '{primary_tense}'. {compat_info['logic']}",
                        position=pos
                    ))
        
        # 4. Validate temporal adverb-tense compatibility
        for adverb, pos in temporal_adverbs:
            expected_tenses = self.temporal_adverb_tense[adverb]
            if primary_tense not in expected_tenses:
                errors.append(SentenceValidationError(
                    SentenceError.TEMPORAL_ADVERB_CONFLICT,
                    f"Temporal adverb '{adverb}' expects tense {expected_tenses} but found '{primary_tense}'",
                    position=pos
                ))
        
        return errors 