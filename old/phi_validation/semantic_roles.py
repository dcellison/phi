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
                    'thephoa', 'luthea', 'phethoa', 'phethui', 'phethea',
                    'luthui', 'phethui', 'phethoa', 'luphea', 'nowhea', 'hathai',
                    'hishui', 'phiphea', 'raushai'  # person, friend, family terms, artist, teacher, musician, parent, child, leader
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
                    'maphia', 'nethai', 'riwhea', 'latheo', 'shuwhia', 'lophui',
                    'lowhai', 'raoshea'  # answer - abstract concept, sun
                    # objects, tools, natural phenomena, abstract concepts, art
                },
                'logic': 'Inanimate marker for non-living entities'
            }
        }
        
        # Classifier-noun compatibility
        self.classifier_compatibility = {
            'lea': {  # long objects
                'compatible_nouns': {
                    'lathia', 'naiphia', 'powhia', 'huphui', 'saphoa', 'liphai'  # axe, knife, bow, road, snake, tree
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
            },
            'hau': {  # humans
                'compatible_nouns': {
                    'thephoa', 'phiphea', 'nowhea', 'hathai', 'luphea', 'raushai',
                    # Phase 3 expansion: remaining human nouns
                    'luthea', 'phethoa', 'phethui', 'phethea', 'luthui', 'hishui'
                    # person, child, teacher, musician, artist, leader, friend, family terms
                },
                'logic': 'Human classifier for people and individuals'
            },
            'rao': {  # animals
                'compatible_nouns': {
                    'mathai', 'lophea', 'whithea', 'thiphea', 'saphoa',
                    # Phase 3 expansion: remaining animate nouns
                    'naphia', 'whiwhui', 'whaiwhea', 'muwhea', 'whithoa', 
                    'sheuthui', 'lophoa', 'lophia', 'wuphea', 'whuthoa'
                    # cat, bird, dove, animal, snake + diverse animal types
                },
                'logic': 'Animal classifier for mammals, birds, and fish'
            },
            'peu': {  # plants
                'compatible_nouns': {
                    'liphai', 'roshai', 'lophui'  # tree, flower, art/plant
                },
                'logic': 'Plant classifier for all plant life'
            },
            'neo': {  # buildings
                'compatible_nouns': {
                    'hiwhea', 'wushia'  # house, market
                },
                'logic': 'Building classifier for structures'
            },
            'heu': {  # vehicles
                'compatible_nouns': {
                    'whoshia'  # car/vehicle
                },
                'logic': 'Vehicle classifier for transportation'
            },
            'wae': {  # clothing
                'compatible_nouns': {
                    'tushai', 'shoshai'  # dress, clothing
                },
                'logic': 'Clothing classifier for wearable items'
            },
            'sae': {  # food
                'compatible_nouns': {
                    'noshea', 'liwhai'  # food, drink
                },
                'logic': 'Food classifier for food items and dishes'
            },
            'tuo': {  # documents
                'compatible_nouns': {
                    'whethea', 'luthia', 'phuthui'  # book, letter, document
                },
                'logic': 'Document classifier for written works'
            },
            'pio': {  # rectangular objects
                'compatible_nouns': {
                    'whethea', 'phuthui'  # book, document
                },
                'logic': 'Rectangular objects classifier for books, bricks, boxes'
            },
            'sio': {  # tools and instruments
                'compatible_nouns': {
                    'lathia', 'hashia', 'naiphia', 'powhia'  # axe, hammer, knife, bow
                },
                'logic': 'Tool and instrument classifier'
            },
            # Phase 1 Physical Classifiers
            'siu': {  # small objects
                'compatible_nouns': {
                    'riwhea', 'nethai', 'phothea'  # grain/seed, net, small round objects
                },
                'logic': 'Small objects classifier for grains, beads, seeds'
            },
            'pao': {  # pointed objects
                'compatible_nouns': {
                    'naiphia', 'lathia', 'powhia'  # knife, axe, bow (pointed/sharp tools)
                },
                'logic': 'Pointed objects classifier for knives, needles, spears'
            },
            'roi': {  # flexible objects
                'compatible_nouns': {
                    'saphoa', 'nethai'  # snake, net (flexible items)
                },
                'logic': 'Flexible objects classifier for ropes, vines, snakes'
            },
            'hao': {  # hollow objects
                'compatible_nouns': {
                    'tuphai', 'poshai'  # cup, bowl (hollow containers)
                },
                'logic': 'Hollow objects classifier for tubes, pipes, bottles'
            },
            # Phase 1 Specialized Animal Classifiers
            'tio': {  # insects
                'compatible_nouns': {
                    'phashia', 'tephai'  # insect-type creatures
                },
                'logic': 'Insect classifier for ants, bees, flies'
            },
            'wiu': {  # birds specifically
                'compatible_nouns': {
                    'lophea', 'whithea'  # bird, dove (avian creatures)
                },
                'logic': 'Bird classifier for all avian creatures'
            },
            'seo': {  # aquatic animals
                'compatible_nouns': {
                    'liwhoa', 'shewhoa'  # aquatic creatures
                },
                'logic': 'Aquatic animal classifier for fish, aquatic mammals'
            },
            # Phase 2 Functional Classifiers
            'pai': {  # artworks and decorative objects
                'compatible_nouns': {
                    'lophui', 'nuthea', 'thaphao'  # art, sculpture, song
                },
                'logic': 'Artwork classifier for decorative objects and artistic creations'
            },
            'wou': {  # electronic and technological devices
                'compatible_nouns': {
                    'methuwa', 'whoshia'  # phone/electronic device, car (modern vehicles)
                },
                'logic': 'Electronic device classifier for technological items'
            },
            'pea': {  # places and locations
                'compatible_nouns': {
                    'hiwhea', 'wushia', 'latheo'  # house, market, place/location
                },
                'logic': 'Place classifier for locations and geographical areas'
            },
            # Phase 2 Temporal/Spatial Classifiers
            'tea': {  # time periods
                'compatible_nouns': {
                    'towhai', 'wethia'  # time-related concepts, periods
                },
                'logic': 'Time period classifier for days, months, years'
            },
            'lio': {  # distances and measurements
                'compatible_nouns': {
                    'huphui', 'shuwhia'  # road/distance, sand/measurement unit
                },
                'logic': 'Distance classifier for measurements and spatial extents'
            },
            'rae': {  # events and occurrences
                'compatible_nouns': {
                    'thaphao', 'lowhai'  # song/event, answer/occurrence
                },
                'logic': 'Event classifier for occurrences and happenings'
            },
            # Phase 2 Additional Container Classifier
            'weu': {  # container objects (bowls, cups, baskets)
                'compatible_nouns': {
                    'tuphai', 'poshai', 'pashia', 'pashui'  # cup, bowl, bag, basket
                },
                'logic': 'Container object classifier for bowls, cups, baskets'
            },
            # Phase 3 Abstract Classifiers
            'leu': {  # ideas and concepts
                'compatible_nouns': {
                    'lowhai', 'lophui'  # answer/idea, art/concept
                },
                'logic': 'Abstract concept classifier for ideas and thoughts'
            },
            'mie': {  # emotions and feelings
                'compatible_nouns': {
                    'thaphao'  # song (emotional expression)
                },
                'logic': 'Emotion classifier for feelings and emotional expressions'
            },
            'nua': {  # social groups and organizations
                'compatible_nouns': {
                    'wushia'  # market (social/economic organization)
                },
                'logic': 'Social group classifier for organizations and collectives'
            },
            # Phase 3 Natural Phenomena Classifier
            'rau': {  # natural phenomena
                'compatible_nouns': {
                    'raoshea', 'hathia'  # sun, specialized natural terms
                },
                'logic': 'Natural phenomena classifier for celestial and natural objects'
            }
        }
        
        # Verb argument structure requirements
        self.verb_argument_structure = {
            # Verbs requiring animate subjects
            'animate_subject_verbs': {
                'verbs': {
                    'shuna', 'whomo', 'shero', 'shola', 'whumi', 'whepi', 'whawi',
                    'whuwe', 'phamu', 'whesa', 'shoro', 'sheho', 'thunu',
                    'whemo', 'sheli', 'whipu', 'thume', 'shule', 'shire', 'phewa',
                    'sheme'  # teach - animals can be taught and can teach others
                    # call, like, carry, walk, run, jump, fly, sleep, spend, create, destroy, kill, ban
                    # think, believe, know, remember, understand, want, feel - cognitive verbs
                },
                'logic': 'These verbs require animate (living) subjects'
            },
            
            # Verbs requiring human subjects
            'human_subject_verbs': {
                'verbs': {
                    'shuna', 'phamu', 'whesa', 'thunu', 'shuni', 'whupa'
                    # call, spend, create, ban, build, fix - typically human activities
                    # NOTE: sheme (teach) moved to animate_subject_verbs for real-world usage
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
                # Look for nouns with animacy markers to identify the true subject
                search_end = object_start if object_start is not None else i
                
                # Find all noun phrases before the object/verb
                noun_phrases = []
                k = 0
                while k < search_end:
                    if tokens[k] in ['he', 'pi', 'ne']:
                        # Found animacy marker, look for following noun
                        for m in range(k + 1, min(k + 3, search_end)):
                            if self._identify_word_type(tokens[m]) == 'noun':
                                noun_phrases.append((tokens[m], m, tokens[k]))
                                k = m + 1
                                break
                        else:
                            k += 1
                    else:
                        k += 1
                
                # The subject is the first noun phrase (before any object)
                if noun_phrases and not subject_found:
                    subject_noun, subject_pos, animacy_marker = noun_phrases[0]
                    subjects.append((subject_noun, subject_pos, token))
                    subject_found = True
                
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