#!/usr/bin/env python3
"""
Semantic Roles Validation Module

Validates animacy agreement, classifier compatibility, and verb argument
structure requirements in Phi sentences.
"""

from typing import List, Dict, Optional, Tuple
from .errors import SentenceError, SentenceValidationError


class SemanticRoleValidator:
    """Validates semantic role consistency and argument structure."""
    
    def __init__(self):
        """Initialize semantic role validation rules."""
        # Animacy categories for nouns
        self.animacy_categories = {
            # Human animacy (he)
            'human': {
                'marker': 'he',
                'nouns': {
                    'thephoa', 'luthea', 'phethoa', 'phethui', 'lophui', 'phethea',
                    'luthui', 'phethui', 'lophea', 'phethoa'  # person, friend, family terms
                },
                'logic': 'Human animacy marker for people and human relationships'
            },
            
            # Animate non-human (pi)  
            'animate': {
                'marker': 'pi',
                'nouns': {
                    'thiphea', 'naphia', 'whiwhui', 'lophea', 'whaiwhea', 'mathai',
                    'muwhea', 'tephai', 'whithoa', 'whithea', 'sheuthui', 'liwhoa',
                    'phashia', 'lophoa', 'lophia', 'shewhoa', 'saphoa', 'wuphea', 'whuthoa'
                    # animals, insects, living creatures
                },
                'logic': 'Animate marker for living non-human entities'
            },
            
            # Inanimate (ne)
            'inanimate': {
                'marker': 'ne',
                'nouns': {
                    'hiwhea', 'lathia', 'pashia', 'mophui', 'pashui', 'phuthui',
                    'whethea', 'powhia', 'poshai', 'whoshia', 'phothea', 'tuphai',
                    'shoshai', 'tushai', 'hashia', 'hathia', 'naiphia', 'luthia',
                    'maphia', 'nethai', 'riwhea', 'latheo', 'shuwhia'
                    # objects, tools, natural phenomena, abstract concepts
                },
                'logic': 'Inanimate marker for non-living entities'
            }
        }
        
        # Classifier-noun compatibility
        self.classifier_compatibility = {
            'lea': {  # long objects
                'compatible_nouns': {
                    'lathia', 'naiphia', 'powhia', 'huphui', 'saphoa'  # axe, knife, bow, road, snake
                },
                'logic': 'Long objects classifier for elongated items'
            },
            'moi': {  # flat objects
                'compatible_nouns': {
                    'whethea', 'luthia', 'maphia', 'tushai'  # book, letter, map, dress
                },
                'logic': 'Flat objects classifier for thin, flat items'
            },
            'teo': {  # round objects
                'compatible_nouns': {
                    'mophui', 'tuphai', 'poshai', 'phothea'  # ball, cup, bowl, cannonball
                },
                'logic': 'Round objects classifier for spherical items'
            },
            'wau': {  # containers
                'compatible_nouns': {
                    'pashia', 'pashui', 'tuphai', 'poshai', 'nethai'  # bag, basket, cup, bowl, net
                },
                'logic': 'Container classifier for hollow objects'
            },
            'phi': {  # tools/instruments
                'compatible_nouns': {
                    'lathia', 'hashia', 'naiphia', 'powhia'  # axe, hammer, knife, bow
                },
                'logic': 'Tool classifier for implements and instruments'
            }
        }
        
        # Verb argument structure requirements
        self.verb_argument_structure = {
            # Verbs requiring animate subjects
            'animate_subject_verbs': {
                'verbs': {
                    'shuna', 'whomo', 'shero', 'shola', 'whumi', 'whepi', 'whawi',
                    'whuwe', 'phamu', 'whesa', 'shoro', 'sheho', 'thunu'
                    # call, like, carry, walk, run, jump, fly, sleep, spend, create, destroy, kill, ban
                },
                'logic': 'These verbs require animate (living) subjects'
            },
            
            # Verbs requiring human subjects
            'human_subject_verbs': {
                'verbs': {
                    'shuna', 'phamu', 'whesa', 'thunu', 'shuni', 'whupa'
                    # call, spend, create, ban, build, fix - typically human activities
                },
                'logic': 'These verbs typically require human subjects'
            },
            
            # Verbs requiring inanimate objects
            'inanimate_object_verbs': {
                'verbs': {
                    'shero', 'shute', 'shomo', 'whupa', 'thura', 'whuno'
                    # carry, put, raise, fix, cut, break - physical manipulation
                },
                'logic': 'These verbs typically take inanimate objects'
            },
            
            # Verbs that can take animate objects
            'animate_object_verbs': {
                'verbs': {
                    'shuna', 'whomo', 'sheho', 'shero', 'themu'
                    # call, like, kill, carry, follow - can act on living beings
                },
                'logic': 'These verbs can take animate objects'
            }
        }
        
        # Lexicon validator for word type identification
        self.lexicon_validator = None  # Will be set by core
    
    def set_lexicon_validator(self, lexicon_validator):
        """Set the lexicon validator for word type identification."""
        self.lexicon_validator = lexicon_validator
    
    def validate_semantic_roles(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate semantic role consistency including animacy, classifiers, and verb arguments."""
        errors = []
        
        # Find sentence structure elements
        nouns_with_particles = []
        classifiers_with_nouns = []
        verbs = []
        subjects = []
        objects = []
        
        # Parse sentence structure
        i = 0
        while i < len(tokens):
            token = tokens[i]
            word_type = self._identify_word_type(token)
            
            # Track animacy particles with their target nouns
            if token in ['he', 'pi', 'ne']:
                # Find the noun this animacy particle modifies
                for j in range(i + 1, min(i + 3, len(tokens))):  # Look ahead 2 positions
                    next_word_type = self._identify_word_type(tokens[j])
                    if next_word_type == 'noun':
                        nouns_with_particles.append((tokens[j], token, j, i))
                        break
            
            # Track classifiers with their target nouns
            elif word_type == 'classifier':
                # Find the noun this classifier modifies
                for j in range(i + 1, min(i + 3, len(tokens))):
                    next_word_type = self._identify_word_type(tokens[j])
                    if next_word_type == 'noun':
                        classifiers_with_nouns.append((token, tokens[j], i, j))
                        break
            
            # Track verbs and their arguments
            elif word_type == 'verb':
                verbs.append((token, i))
                
                # Find subject (before verb, not marked with 'na')
                # In SOV: Subject [Object na] Verb
                subject_found = False
                object_start = None
                
                # First, find where object starts (marked by 'na')
                for j in range(i):
                    if tokens[j] == 'na':
                        object_start = j
                        break
                
                # Subject is before the object (or before verb if no object)
                search_end = object_start if object_start is not None else i
                for j in range(search_end - 1, -1, -1):
                    prev_word_type = self._identify_word_type(tokens[j])
                    if prev_word_type == 'noun' and not subject_found:
                        subjects.append((tokens[j], j, token))
                        subject_found = True
                        break
                
                # Find object (immediately after 'na')
                for j in range(i):
                    if tokens[j] == 'na' and j + 1 < len(tokens):
                        next_word_type = self._identify_word_type(tokens[j + 1])
                        if next_word_type == 'noun':
                            objects.append((tokens[j + 1], j + 1, token))
                            break
            
            i += 1
        
        # 1. Validate animacy agreement
        for noun, animacy_particle, noun_pos, particle_pos in nouns_with_particles:
            expected_animacy = self._get_expected_animacy(noun)
            if expected_animacy and expected_animacy != animacy_particle:
                expected_category = self._get_animacy_category_name(expected_animacy)
                actual_category = self._get_animacy_category_name(animacy_particle)
                errors.append(SentenceValidationError(
                    SentenceError.ANIMACY_MISMATCH,
                    f"Noun '{noun}' ({expected_category}) incompatible with animacy marker '{animacy_particle}' ({actual_category})",
                    position=particle_pos
                ))
        
        # 2. Validate classifier compatibility
        for classifier, noun, classifier_pos, noun_pos in classifiers_with_nouns:
            if classifier in self.classifier_compatibility:
                compat_info = self.classifier_compatibility[classifier]
                if noun not in compat_info['compatible_nouns']:
                    errors.append(SentenceValidationError(
                        SentenceError.CLASSIFIER_INCOMPATIBILITY,
                        f"Classifier '{classifier}' incompatible with noun '{noun}'. {compat_info['logic']}",
                        position=classifier_pos
                    ))
        
        # 3. Validate verb argument structure
        # Check subject animacy requirements
        for subject_noun, subject_pos, verb in subjects:
            subject_animacy = self._get_expected_animacy(subject_noun)
            
            # Check if verb requires animate subject
            if verb in self.verb_argument_structure['animate_subject_verbs']['verbs']:
                if subject_animacy == 'ne':  # inanimate subject
                    errors.append(SentenceValidationError(
                        SentenceError.VERB_ARGUMENT_VIOLATION,
                        f"Verb '{verb}' requires animate subject but '{subject_noun}' is inanimate",
                        position=subject_pos
                    ))
            
            # Check if verb requires human subject
            if verb in self.verb_argument_structure['human_subject_verbs']['verbs']:
                if subject_animacy != 'he':  # non-human subject
                    errors.append(SentenceValidationError(
                        SentenceError.VERB_ARGUMENT_VIOLATION,
                        f"Verb '{verb}' typically requires human subject but '{subject_noun}' is not human",
                        position=subject_pos
                    ))
        
        # Check object animacy requirements
        for object_noun, object_pos, verb in objects:
            object_animacy = self._get_expected_animacy(object_noun)
            
            # Check if verb requires inanimate object
            if verb in self.verb_argument_structure['inanimate_object_verbs']['verbs']:
                if object_animacy in ['he', 'pi']:  # animate object
                    if verb not in self.verb_argument_structure['animate_object_verbs']['verbs']:
                        errors.append(SentenceValidationError(
                            SentenceError.VERB_ARGUMENT_VIOLATION,
                            f"Verb '{verb}' typically requires inanimate object but '{object_noun}' is animate",
                            position=object_pos
                        ))
        
        return errors
    
    def _identify_word_type(self, word: str) -> Optional[str]:
        """Identify the part of speech of a word."""
        if self.lexicon_validator:
            return self.lexicon_validator.identify_word_type(word)
        return None
    
    def _get_expected_animacy(self, noun: str) -> Optional[str]:
        """Get the expected animacy marker for a noun."""
        for category, info in self.animacy_categories.items():
            if noun in info['nouns']:
                return info['marker']
        return None
    
    def _get_animacy_category_name(self, marker: str) -> str:
        """Get the category name for an animacy marker."""
        marker_to_category = {'he': 'human', 'pi': 'animate', 'ne': 'inanimate'}
        return marker_to_category.get(marker, 'unknown') 