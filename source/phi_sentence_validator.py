#!/usr/bin/env python3
"""
Phi Sentence Validator

Validates complete Phi sentences for:
- SOV word order compliance
- Particle placement and ordering
- Grammatical structure
- Lexical validity
- Semantic coherence
"""

import sys
import re
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from enum import Enum

# Add the current directory to path to import phi_validator
sys.path.append(str(Path(__file__).parent))

from phi_validator import PhiValidator, ValidationResult, ValidationError


class SentenceError(Enum):
    """Types of sentence validation errors."""
    INVALID_WORD = "invalid_word"
    WORD_ORDER = "word_order"
    PARTICLE_ORDER = "particle_order"
    PARTICLE_SCOPE = "particle_scope"
    MISSING_VERB = "missing_verb"
    MULTIPLE_VERBS = "multiple_verbs"
    SEMANTIC_MISMATCH = "semantic_mismatch"
    UNKNOWN_WORD = "unknown_word"
    TENSE_INCONSISTENCY = "tense_inconsistency"
    ASPECT_TENSE_CONFLICT = "aspect_tense_conflict"
    MODAL_TENSE_CONFLICT = "modal_tense_conflict"
    TEMPORAL_ADVERB_CONFLICT = "temporal_adverb_conflict"
    MULTIPLE_TENSE_MARKERS = "multiple_tense_markers"
    ANIMACY_MISMATCH = "animacy_mismatch"
    CLASSIFIER_INCOMPATIBILITY = "classifier_incompatibility"
    VERB_ARGUMENT_VIOLATION = "verb_argument_violation"
    MODAL_VERB_FORM_ERROR = "modal_verb_form_error"
    CONDITIONAL_STRUCTURE_ERROR = "conditional_structure_error"
    DESIDERATIVE_CONSTRUCTION_ERROR = "desiderative_construction_error"
    TEMPORAL_SEQUENCE_ERROR = "temporal_sequence_error"
    RELATIVE_CLAUSE_TENSE_ERROR = "relative_clause_tense_error"
    INTERROGATIVE_TENSE_ERROR = "interrogative_tense_error"
    QUESTION_CONTEXT_MISMATCH = "question_context_mismatch"
    EVIDENTIALITY_COMBINATION_ERROR = "evidentiality_combination_error"
    EVIDENTIALITY_TENSE_CONFLICT = "evidentiality_tense_conflict"
    REPORTED_SPEECH_NESTING_ERROR = "reported_speech_nesting_error"
    DERIVATIONAL_SCOPE_ERROR = "derivational_scope_error"
    DERIVATIONAL_SEMANTIC_ERROR = "derivational_semantic_error"
    DERIVATIONAL_PHONOTACTIC_ERROR = "derivational_phonotactic_error"
    DERIVATIONAL_CONTEXT_WARNING = "derivational_context_warning"
    DERIVATIONAL_CONFLICT_ERROR = "derivational_conflict_error"
    EMPHASIS_SCOPE_ERROR = "emphasis_scope_error"
    POLITENESS_CONTEXT_MISMATCH = "politeness_context_mismatch"
    POLITENESS_EVIDENTIALITY_COMBINATION_ERROR = "politeness_evidentiality_combination_error"
    POLITENESS_PRAGMATIC_MISMATCH = "politeness_pragmatic_mismatch"
    POLITENESS_REGISTER_INCONSISTENCY = "politeness_register_inconsistency"
    POLITENESS_REGISTER_INCOMPLETE = "politeness_register_incomplete"
    POLITENESS_MISSING_REQUIRED = "politeness_missing_required"
    POLITENESS_DISCOURSE_MISMATCH = "politeness_discourse_mismatch"
    POLITENESS_PRAGMATIC_INAPPROPRIATE = "politeness_pragmatic_inappropriate"
    DISCOURSE_SEQUENCE_ERROR = "discourse_sequence_error"
    TOPIC_CHAIN_VIOLATION = "topic_chain_violation"
    CONTRAST_SCOPE_ERROR = "contrast_scope_error"
    TOPIC_CONTRAST_INTERACTION_ERROR = "topic_contrast_interaction_error"


class SentenceValidationError:
    """Represents a sentence validation error."""
    
    def __init__(self, error_type: SentenceError, message: str, 
                 position: Optional[int] = None, word: Optional[str] = None):
        self.error_type = error_type
        self.message = message
        self.position = position
        self.word = word


class PhiSentenceValidator:
    """Validates complete Phi sentences for grammatical correctness."""
    
    def __init__(self):
        self.word_validator = PhiValidator()
        
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
        
        # Particle ordering within slots
        self.slot_0_order = [
            ['wa', 'ho', 'tu', 'hu'],  # sentence type
            ['hi', 'ro', 'nu', 'ti', 'mu', 'pe'],  # evidentiality
            ['ha', 'mi'],  # discourse
            ['so']  # politeness
        ]
        
        self.slot_1_order = [
            ['li', 'ta', 'su'],  # tense
            ['we', 'la', 'ni', 'po', 'pu', 'ri', 'wi', 'wu'],  # aspect
            ['me']  # negation
        ]
        
        self.slot_2_order = [
            ['si', 'na', 'te'],  # POS markers
            ['se', 'ra'],  # derivation
            ['he', 'pi', 'ne'],  # animacy
            ['pa', 'mo', 'sa', 'le', 're'],  # comparison
            ['wo', 'lo', 'no'],  # number
            ['ma']  # emphasis
        ]
        
        # Load lexicon for word validation
        self.lexicon = self.word_validator.lexicon
        
        # Subordinate clause tense validation rules
        self.subordinate_conjunctions = {
            'pimo': {  # before
                'expected_tense': ['su', 'ru'],  # future or obligative
                'logic': 'Events "before" something typically refer to future conditions'
            },
            'matu': {  # after
                'expected_tense': ['li', 'ni'],  # past or perfect
                'logic': 'Events "after" something typically refer to completed actions'
            },
            'wetu': {  # if
                'expected_tense': ['su', 'ta', 'ru'],  # future, present, or obligative
                'logic': 'Conditional clauses use present, future, or obligative'
            },
            'tura': {  # since
                'expected_tense': ['li', 'ni'],  # past or perfect
                'logic': 'Causal "since" typically refers to completed events'
            },
            'wane': {  # when
                'expected_tense': ['li', 'ta', 'su'],  # any basic tense
                'logic': 'Temporal "when" can use any basic tense'
            },
            'lina': {  # until
                'expected_tense': ['su', 'ta'],  # future or present
                'logic': 'Duration "until" typically uses present or future'
            },
            'runa': {  # while
                'expected_tense': ['ta', 'la', 'ri'],  # present, progressive, imperfective
                'logic': 'Simultaneous "while" uses present or ongoing aspects'
            }
        }
        
        # Comprehensive tense validation rules
        self.tense_particles = {'li', 'ta', 'su'}  # past, present, future
        self.aspect_particles = {'we', 'la', 'ni', 'po', 'pu', 'ri', 'wi', 'wu'}
        self.mood_particles = {'to', 'ru', 'me'}  # imperative, obligative, negation
        
        # Aspect-tense compatibility rules
        self.aspect_tense_compatibility = {
            'we': {  # perfective
                'compatible': ['li', 'ta', 'su'],
                'preferred': ['li'],  # perfective often with past
                'logic': 'Perfective aspect emphasizes completion'
            },
            'la': {  # progressive
                'compatible': ['ta', 'su'],
                'preferred': ['ta'],  # progressive typically present
                'logic': 'Progressive aspect indicates ongoing action'
            },
            'ni': {  # perfect
                'compatible': ['ta', 'su'],
                'preferred': ['ta'],  # perfect often present relevance
                'logic': 'Perfect aspect shows past action with present relevance'
            },
            'po': {  # inchoative (beginning)
                'compatible': ['ta', 'su'],
                'preferred': ['su'],  # beginning often future
                'logic': 'Inchoative aspect indicates action beginning'
            },
            'pu': {  # cessative (ending)
                'compatible': ['li', 'ta'],
                'preferred': ['li'],  # ending often past
                'logic': 'Cessative aspect indicates action ending'
            },
            'ri': {  # imperfective
                'compatible': ['li', 'ta', 'su'],
                'preferred': ['ta'],  # imperfective often present
                'logic': 'Imperfective aspect shows ongoing or habitual action'
            },
            'wi': {  # iterative
                'compatible': ['li', 'ta', 'su'],
                'preferred': ['ta'],  # iterative often present habit
                'logic': 'Iterative aspect indicates repeated action'
            },
            'wu': {  # experiential
                'compatible': ['li', 'ta'],
                'preferred': ['li'],  # experiential often past experience
                'logic': 'Experiential aspect indicates past experience'
            }
        }
        
        # Modal-tense compatibility rules
        self.modal_tense_compatibility = {
            'to': {  # imperative
                'compatible': ['ta', 'su'],  # present or future commands
                'incompatible': ['li'],  # can't command the past
                'logic': 'Imperatives cannot refer to past actions'
            },
            'ru': {  # obligative
                'compatible': ['ta', 'su'],  # present or future obligations
                'incompatible': ['li'],  # obligations are forward-looking
                'logic': 'Obligations refer to present or future requirements'
            },
            'me': {  # negation
                'compatible': ['li', 'ta', 'su'],  # can negate any tense
                'logic': 'Negation is compatible with all tenses'
            }
        }
        
        # Temporal adverb-tense compatibility
        self.temporal_adverb_tense = {
            # Past-oriented adverbs
            'pulime': ['li'],  # recently → past
            'nusupe': ['li'],  # lately → past
            'lutume': ['li', 'ta'],  # permanently → past/present
            
            # Present-oriented adverbs  
            'sipane': ['ta'],  # now → present
            'nowate': ['ta'],  # meanwhile → present
            'silane': ['ta'],  # still → present
            'harote': ['ta'],  # immediately → present
            'hotame': ['ta'],  # instantly → present
            
            # Future-oriented adverbs
            'somire': ['su'],  # soon → future
            'tumane': ['su'],  # finally → future
            
            # Multi-temporal adverbs
            'natume': ['li', 'ta', 'su'],  # again → any tense
            'potame': ['ta', 'su'],  # simultaneously → present/future
            'walito': ['ta', 'su'],  # forever/always → present/future
            'norate': ['ta', 'su'],  # continually → present/future
            'ralime': ['ta', 'su'],  # cyclically → present/future
            'rotame': ['ta', 'su'],  # temporarily → present/future
            'sutane': ['ta', 'su'],  # seasonally → present/future
            'tapahe': ['li', 'ta'],  # suddenly → past/present
            'parote': ['ta'],  # already → present
            'lutane': ['su']   # firstly → future
        }
        
        # Semantic role validation rules
        
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
        
        # Modal logic validation rules
        
        # Obligative modal rules (ru = must/should)
        self.obligative_rules = {
            'particle': 'ru',
            'verb_form': 'base',  # Must be followed by base verb (no tense markers)
            'prohibited_particles': ['li', 'ta', 'su'],  # No tense on the verb
            'allowed_aspects': ['we', 'la', 'ni'],  # Some aspects allowed
            'logic': 'Obligative ru requires base verb form without tense marking'
        }
        
        # Conditional modal rules (wetu = if)
        self.conditional_rules = {
            'conjunction': 'wetu',
            'protasis_tenses': ['ta', 'su'],  # if-clause: present or future
            'apodosis_tenses': ['su', 'ru'],  # then-clause: future or obligative
            'prohibited_combinations': [
                ('li', 'su'),  # past if-clause with future then-clause is odd
                ('su', 'li')   # future if-clause with past then-clause is impossible
            ],
            'logic': 'Conditional clauses follow logical temporal relationships'
        }
        
        # Desiderative rules (we = want - note: different from perfective we)
        self.desiderative_rules = {
            'particle': 'we',
            'context': 'desiderative',  # when we means "want" not "perfective"
            'complement_form': 'infinitive',  # wants infinitive-like construction
            'required_structure': ['subject', 'we', 'complement_clause'],
            'complement_markers': ['te'],  # te marks infinitive-like constructions
            'logic': 'Desiderative we requires infinitive complement with te marker'
        }
        
        # Modal scope and interaction rules
        self.modal_interactions = {
            'ru_scope': {
                'immediate': True,  # ru must immediately precede its verb
                'no_intervening': ['li', 'ta', 'su'],  # no tense between ru and verb
                'logic': 'Obligative ru has immediate scope over base verb'
            },
            'conditional_scope': {
                'clause_boundary': True,  # wetu creates clause boundary
                'tense_inheritance': False,  # each clause has independent tense
                'logic': 'Conditional clauses are temporally independent'
            },
            'desiderative_scope': {
                'complement_required': True,  # we (want) needs complement
                'subject_control': True,  # subject of want controls complement subject
                'logic': 'Desiderative constructions require controlled complements'
            }
        }
        
        # Narrative sequence validation rules
        
        # Temporal conjunction sequence logic
        self.temporal_sequence_rules = {
            'pimo': {  # before
                'temporal_relationship': 'precedence',
                'main_clause_time': 'reference_point',
                'subordinate_clause_time': 'after_reference',
                'logical_sequences': {
                    # Main clause tense → subordinate clause tense → validity
                    ('li', 'li'): True,   # "I walked before I ran" (both past, sequence clear)
                    ('li', 'ta'): False,  # "I walked before I walk" (illogical)
                    ('li', 'su'): False,  # "I walked before I will walk" (impossible)
                    ('ta', 'li'): True,   # "I walk before I walked" (present habit, past event)
                    ('ta', 'ta'): True,   # "I walk before I walk" (habitual sequence)
                    ('ta', 'su'): True,   # "I walk before I will walk" (present leads to future)
                    ('su', 'li'): False,  # "I will walk before I walked" (impossible)
                    ('su', 'ta'): False,  # "I will walk before I walk" (illogical)
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
                    ('li', 'ta'): False,  # "I walked after I walk" (illogical)
                    ('li', 'su'): False,  # "I walked after I will walk" (impossible)
                    ('ta', 'li'): True,   # "I walk after I walked" (present result of past)
                    ('ta', 'ta'): True,   # "I walk after I walk" (habitual sequence)
                    ('ta', 'su'): False,  # "I walk after I will walk" (impossible)
                    ('su', 'li'): True,   # "I will walk after I walked" (future after past)
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
        
        # Interrogative validation rules
        
        # Question type markers and their tense requirements
        self.interrogative_rules = {
            # Yes/no questions (wa particle)
            'yes_no_questions': {
                'marker': 'wa',
                'tense_logic': {
                    'li': 'asks_about_past_events',      # "Did you walk?"
                    'ta': 'asks_about_current_state',    # "Do you walk?" / "Are you walking?"
                    'su': 'asks_about_future_plans',     # "Will you walk?"
                    'ru': 'asks_about_obligations'       # "Must you walk?"
                },
                'contextual_appropriateness': {
                    'li': ['completed_actions', 'past_experiences', 'historical_events'],
                    'ta': ['current_habits', 'ongoing_states', 'general_truths'],
                    'su': ['future_intentions', 'predictions', 'planned_events'],
                    'ru': ['duties', 'requirements', 'necessities']
                },
                'logic': 'Yes/no questions must use contextually appropriate tenses'
            },
            
            # Wh-questions (interrogative adverbs)
            'wh_questions': {
                'markers': ['hamite', 'wamine', 'timane', 'wulime'],  # how, why, when, where
                'tense_constraints': {
                    'hamite': {  # how
                        'preferred_tenses': ['ta', 'su'],  # manner questions
                        'logic': 'Manner questions ask about methods or future plans'
                    },
                    'wamine': {  # why
                        'preferred_tenses': ['li', 'ta'],  # reason questions
                        'logic': 'Reason questions typically refer to past events or current states'
                    },
                    'timane': {  # when
                        'preferred_tenses': ['li', 'su'],  # past events or future plans
                        'avoid_tenses': ['ta'],  # "when do you walk?" is odd for habitual
                        'logic': 'Time questions typically ask about specific events'
                    },
                    'wulime': {  # where
                        'preferred_tenses': ['ta', 'li', 'su'],  # location can be any time
                        'logic': 'Location questions can refer to any timeframe'
                    }
                },
                'logic': 'Wh-questions must use tenses appropriate to their semantic type'
            },
            
            # Rhetorical questions (philosophical/literary)
            'rhetorical_questions': {
                'indicators': ['ru'],  # obligative often signals rhetorical questions
                'tense_patterns': {
                    'philosophical': ['ru'],  # "Must one walk?" (general obligation)
                    'existential': ['ta', 'ru'],  # present state or general obligation
                    'hypothetical': ['su', 'ru']  # future possibility or obligation
                },
                'logic': 'Rhetorical questions use tenses to convey philosophical meaning'
            }
        }
        
        # Question-answer tense consistency rules
        self.question_answer_consistency = {
            'tense_matching_rules': {
                # Question tense → appropriate answer tenses
                'li': ['li', 'ta'],  # past question → past answer or present result
                'ta': ['ta', 'li'],  # present question → present answer or past explanation
                'su': ['su', 'ta'],  # future question → future answer or present intention
                'ru': ['ru', 'ta', 'su']  # obligation question → obligation, present, or future
            },
            'contextual_shifts': {
                # When tense shifts are acceptable in answers
                'temporal_perspective': True,   # "Did you walk?" → "I am walking" (ongoing result)
                'causal_explanation': True,     # "Will you walk?" → "I walk daily" (habitual reason)
                'modal_response': True          # "Do you walk?" → "I must walk" (obligation explanation)
            },
            'logic': 'Answers should maintain temporal coherence with questions'
        }
        
        # Interrogative context validation
        self.interrogative_contexts = {
            'information_seeking': {
                'appropriate_tenses': ['li', 'ta', 'su'],
                'inappropriate_combinations': [
                    ('hamile', 'ta'),  # "when do you walk?" (habitual) is odd
                    ('hamite', 'su')   # "how many will you walk?" is semantically odd
                ],
                'logic': 'Information-seeking questions must be semantically coherent'
            },
            'confirmation_seeking': {
                'markers': ['wa'],
                'tense_appropriateness': {
                    'li': 'confirms_past_events',
                    'ta': 'confirms_current_states',
                    'su': 'confirms_future_plans'
                },
                'logic': 'Confirmation questions must match the temporal context'
            },
            'deliberative': {
                'markers': ['ru', 'su'],
                'purpose': 'decision_making',
                'logic': 'Deliberative questions focus on obligations and future actions'
            }
        }
        
        # Evidentiality validation rules
        
        # Evidentiality particles and their semantic requirements
        self.evidentiality_particles = {
            'hi': {  # direct observation
                'type': 'direct',
                'tense_compatibility': ['ta', 'li'],  # present or past observation
                'incompatible_tenses': ['su'],  # can't directly observe future
                'semantic_requirements': ['sensory_evidence', 'immediate_access'],
                'logic': 'Direct observation requires present or past sensory access'
            },
            'ro': {  # inference
                'type': 'inferential',
                'tense_compatibility': ['ta', 'li', 'su'],  # can infer about any time
                'semantic_requirements': ['evidence_based', 'logical_reasoning'],
                'logic': 'Inference can apply to any timeframe based on available evidence'
            },
            'nu': {  # hearsay
                'type': 'reported',
                'tense_compatibility': ['ta', 'li', 'su'],  # can report about any time
                'semantic_requirements': ['third_party_source', 'indirect_knowledge'],
                'nesting_allowed': ['ti'],  # can contain direct reported speech
                'logic': 'Hearsay reports information from unspecified third parties'
            },
            'ti': {  # direct reported speech
                'type': 'quotative',
                'tense_compatibility': ['ta', 'li', 'su'],  # can quote about any time
                'semantic_requirements': ['specific_source', 'direct_quotation'],
                'nesting_restrictions': ['nu'],  # cannot be nested within hearsay
                'logic': 'Direct reported speech cites specific sources'
            },
            'mu': {  # memory
                'type': 'memorial',
                'tense_compatibility': ['li'],  # memory typically of past events
                'preferred_tenses': ['li'],
                'semantic_requirements': ['personal_experience', 'temporal_distance'],
                'logic': 'Memory evidentiality typically refers to past personal experiences'
            },
            'pe': {  # presumption
                'type': 'presumptive',
                'tense_compatibility': ['ta', 'su'],  # presumptions about present/future
                'semantic_requirements': ['assumption_based', 'uncertain_knowledge'],
                'logic': 'Presumptions typically concern present states or future events'
            }
        }
        
        # Evidentiality combination rules
        self.evidentiality_combinations = {
            'prohibited_combinations': [
                ('hi', 'ro'),  # can't have direct observation AND inference
                ('hi', 'nu'),  # can't have direct observation AND hearsay
                ('hi', 'ti'),  # can't have direct observation AND reported speech
                ('hi', 'mu'),  # can't have direct observation AND memory
                ('hi', 'pe'),  # can't have direct observation AND presumption
                ('ro', 'nu'),  # can't have inference AND hearsay
                ('ro', 'ti'),  # can't have inference AND reported speech
                ('mu', 'pe'),  # can't have memory AND presumption
                ('nu', 'ti'),  # can't have hearsay AND direct reported (except nesting)
            ],
            'allowed_sequences': [
                ('ti', 'nu'),  # direct quote can be followed by hearsay context
                ('mu', 'ro'),  # memory can be followed by inference
                ('pe', 'ro'),  # presumption can be followed by inference
            ],
            'logic': 'Multiple evidentiality markers create contradictory epistemic stances'
        }
        
        # Reported speech nesting rules
        self.reported_speech_nesting = {
            'ti_within_nu': {
                'structure': 'nu [context] ti [quoted_content]',
                'semantic_logic': 'hearsay context containing direct quotation',
                'example': 'nu sha li phemo ti mia ta shola',
                'gloss': 'HRSY 3sg PST say REP 1sg PRS walk',
                'english': 'They say he said "I walk"',
                'validation_rules': {
                    'nu_scope': 'entire_sentence',
                    'ti_scope': 'quoted_portion',
                    'tense_independence': True,  # quoted content has independent tense
                    'source_hierarchy': 'nu < ti'  # ti is more specific than nu
                }
            },
            'prohibited_nestings': [
                'ti_within_ti',  # can't nest direct quotes
                'nu_within_ti',  # can't have hearsay within direct quote
                'hi_within_any',  # direct observation can't be nested
                'ro_within_reported'  # inference can't be within reported speech
            ],
            'logic': 'Reported speech nesting follows source specificity hierarchy'
        }
        
        # Evidentiality-tense interaction rules
        self.evidentiality_tense_interactions = {
            'hi_tense_logic': {
                # Direct observation tense constraints
                'hi_ta': 'valid',  # "I see it is raining"
                'hi_li': 'valid',  # "I saw it was raining"
                'hi_su': 'invalid',  # "I see it will rain" (contradiction)
                'hi_la': 'valid',  # "I see it is raining" (progressive)
                'hi_ni': 'valid',  # "I see it has rained" (present perfect)
                'logic': 'Direct observation requires temporal accessibility'
            },
            'mu_tense_logic': {
                # Memory evidentiality tense constraints
                'mu_li': 'preferred',  # "I remember it rained"
                'mu_ta': 'marginal',  # "I remember it rains" (habitual memory)
                'mu_su': 'invalid',  # "I remember it will rain" (contradiction)
                'mu_ni': 'valid',  # "I remember it has rained"
                'logic': 'Memory evidentiality primarily concerns past events'
            },
            'pe_tense_logic': {
                # Presumption evidentiality tense constraints
                'pe_ta': 'valid',  # "I assume it is raining"
                'pe_su': 'valid',  # "I assume it will rain"
                'pe_li': 'marginal',  # "I assume it rained" (less common)
                'pe_ru': 'valid',  # "I assume it must rain"
                'logic': 'Presumptions typically concern present or future states'
            },
            'ro_tense_logic': {
                # Inferential evidentiality (most flexible)
                'ro_li': 'valid',  # "I infer it rained" (based on evidence)
                'ro_ta': 'valid',  # "I infer it is raining"
                'ro_su': 'valid',  # "I infer it will rain"
                'ro_ru': 'valid',  # "I infer it must rain"
                'logic': 'Inference can apply to any timeframe with evidence'
            }
        }
        
        # Complex evidentiality discourse patterns
        self.evidentiality_discourse_patterns = {
            'evidentiality_chains': {
                # Sequences of evidentiality across multiple clauses
                'escalating_certainty': ['pe', 'ro', 'hi'],  # presumption → inference → observation
                'decreasing_certainty': ['hi', 'ro', 'pe'],  # observation → inference → presumption
                'source_specification': ['nu', 'ti'],  # hearsay → direct quote
                'temporal_progression': ['mu', 'hi'],  # memory → current observation
                'logic': 'Evidentiality chains show epistemic reasoning progression'
            },
            'evidentiality_conflicts': {
                # Contradictory evidentiality in discourse
                'direct_vs_reported': ['hi', 'nu'],  # "I see" vs "they say"
                'memory_vs_observation': ['mu', 'hi'],  # "I remember" vs "I see"
                'inference_vs_direct': ['ro', 'hi'],  # "I infer" vs "I observe"
                'logic': 'Conflicting evidentiality creates epistemic tension'
            }
        }
        
        # Derivational particle validation rules
        
        # Derivational particles and their transformation rules
        self.derivational_particles = {
            'se': {  # noun-to-verb derivation (NVERB)
                'type': 'noun_to_verb',
                'source_pos': 'noun',
                'target_pos': 'verb',
                'semantic_requirements': ['actionable_concept', 'process_potential'],
                'phonotactic_validation': True,
                'logic': 'Transforms nouns into verb constructs for temporary verbal usage'
            },
            'ra': {  # verb-to-noun derivation (VNOUN)
                'type': 'verb_to_noun',
                'source_pos': 'verb',
                'target_pos': 'noun',
                'semantic_requirements': ['nominalizable_action', 'abstract_concept'],
                'phonotactic_validation': True,
                'logic': 'Transforms verbs into noun constructs for gerund-like or abstract usage'
            }
        }
        
        # Semantic appropriateness rules for derivational particles
        self.derivational_semantics = {
            'se_appropriate_nouns': {
                # Nouns that can reasonably be used as verbs
                'tools_and_instruments': {
                    'lathia', 'hashia', 'naiphia', 'powhia', 'tuphai'  # axe, hammer, knife, bow, cup
                },
                'substances_and_materials': {
                    'riwhea', 'latheo', 'shuwhia', 'mophui'  # wind, water, sand, ball
                },
                'abstract_concepts': {
                    'lowhai', 'whethea', 'luthea'  # answer, book, friend
                },
                'body_parts_and_features': {
                    'whiphoa', 'phiwhai'  # eye, hill (metaphorical usage)
                },
                'logic': 'These nouns have clear potential for verbal interpretation'
            },
            'se_inappropriate_nouns': {
                # Nouns that are semantically odd as verbs
                'abstract_states': {
                    'mipho', 'hashe', 'sathi'  # blue, green, white (colors as nouns)
                },
                'inherent_properties': {
                    'tophe', 'niphe'  # big, small (size as nouns)
                },
                'logic': 'These nouns lack clear actionable or processual meaning'
            },
            'ra_appropriate_verbs': {
                # Verbs that can reasonably be nominalized
                'action_verbs': {
                    'shola', 'whumi', 'whawi', 'shero', 'shuni'  # walk, run, fly, carry, build
                },
                'mental_verbs': {
                    'whomo', 'phemo', 'whesa'  # like, think, create
                },
                'communication_verbs': {
                    'shuna', 'shuso'  # call, say
                },
                'process_verbs': {
                    'whuru', 'thunu', 'whupa'  # blow, ban, fix
                },
                'logic': 'These verbs represent actions/processes that can be conceptualized as things'
            },
            'ra_inappropriate_verbs': {
                # Verbs that are semantically odd as nouns
                'stative_verbs': {
                    'phera'  # be (copula) - being as a noun is philosophically complex
                },
                'auxiliary_verbs': {
                    # Any auxiliary constructions would be inappropriate
                },
                'logic': 'These verbs lack clear nominal conceptualization'
            }
        }
        
        # Contextual usage patterns for derivational particles
        self.derivational_contexts = {
            'se_usage_patterns': {
                'instrumental_usage': {
                    'pattern': 'se + tool_noun → use_as_tool',
                    'examples': [
                        ('se lathia', 'use as axe / axe (verb)'),
                        ('se naiphia', 'use as knife / knife (verb)'),
                        ('se tuphai', 'use as cup / cup (verb)')
                    ],
                    'logic': 'Tool nouns become verbs meaning "use X as tool"'
                },
                'metaphorical_usage': {
                    'pattern': 'se + abstract_noun → embody_concept',
                    'examples': [
                        ('se luthea', 'befriend / act as friend'),
                        ('se lowhai', 'answer (verb) / provide answer'),
                        ('se whethea', 'book (verb) / record/document')
                    ],
                    'logic': 'Abstract nouns become verbs meaning "act as X" or "provide X"'
                },
                'substance_usage': {
                    'pattern': 'se + substance_noun → apply_substance',
                    'examples': [
                        ('se riwhea', 'wind (verb) / blow like wind'),
                        ('se latheo', 'water (verb) / apply water'),
                        ('se shuwhia', 'sand (verb) / apply sand')
                    ],
                    'logic': 'Substance nouns become verbs meaning "apply X" or "act like X"'
                }
            },
            'ra_usage_patterns': {
                'gerund_usage': {
                    'pattern': 'ra + action_verb → gerund_form',
                    'examples': [
                        ('ra shola', 'walking / the act of walking'),
                        ('ra whumi', 'running / the act of running'),
                        ('ra shuni', 'building / the act of building')
                    ],
                    'logic': 'Action verbs become gerund-like nouns representing the activity'
                },
                'abstract_concept_usage': {
                    'pattern': 'ra + mental_verb → abstract_concept',
                    'examples': [
                        ('ra whomo', 'liking / affection'),
                        ('ra phemo', 'thinking / thought'),
                        ('ra whesa', 'creating / creation')
                    ],
                    'logic': 'Mental verbs become abstract nouns representing the concept'
                },
                'result_usage': {
                    'pattern': 'ra + process_verb → result_noun',
                    'examples': [
                        ('ra shuni', 'building / construction (result)'),
                        ('ra whupa', 'fixing / repair (result)'),
                        ('ra whesa', 'creating / creation (product)')
                    ],
                    'logic': 'Process verbs become nouns representing the result or product'
                }
            }
        }
        
        # Derivational particle scope and interaction rules
        self.derivational_scope_rules = {
            'se_scope': {
                'immediate_scope': True,  # se must immediately precede its target noun
                'no_intervening_particles': ['he', 'pi', 'ne'],  # animacy conflicts with derivation
                'allowed_intervening': ['ma'],  # emphasis can intervene
                'target_requirements': ['noun'],
                'logic': 'se has immediate scope over the following noun'
            },
            'ra_scope': {
                'immediate_scope': True,  # ra must immediately precede its target verb
                'no_intervening_particles': ['li', 'ta', 'su'],  # tense conflicts with derivation
                'allowed_intervening': ['ma'],  # emphasis can intervene
                'target_requirements': ['verb'],
                'logic': 'ra has immediate scope over the following verb'
            },
            'derivational_conflicts': {
                'se_animacy_conflict': {
                    'particles': ['he', 'pi', 'ne'],
                    'logic': 'Derived verbs from nouns inherit original animacy, explicit marking conflicts'
                },
                'ra_tense_conflict': {
                    'particles': ['li', 'ta', 'su'],
                    'logic': 'Derived nouns from verbs are atemporal, tense marking conflicts'
                },
                'double_derivation': {
                    'prohibited': ['se + ra', 'ra + se'],
                    'logic': 'Cannot derive from already derived forms'
                }
            }
        }
        
        # Phonotactic validation for derived forms
        self.derivational_phonotactics = {
            'se_derived_validation': {
                'source_pattern': 'noun_phonotactics',  # [C/F][V/P][F][P]
                'derived_usage': 'verb_context',
                'validation_rules': [
                    'source_noun_must_be_valid',
                    'derived_form_used_in_verb_position',
                    'no_verb_phonotactic_requirements'  # se+noun doesn't change phonotactics
                ],
                'logic': 'se+noun maintains noun phonotactics but functions as verb'
            },
            'ra_derived_validation': {
                'source_pattern': 'verb_phonotactics',  # [F][V][C][V]
                'derived_usage': 'noun_context',
                'validation_rules': [
                    'source_verb_must_be_valid',
                    'derived_form_used_in_noun_position',
                    'no_noun_phonotactic_requirements'  # ra+verb doesn't change phonotactics
                ],
                'logic': 'ra+verb maintains verb phonotactics but functions as noun'
            }
        }
        
        # Temporary vs. permanent derivation context
        self.derivational_permanence = {
            'temporary_derivation': {
                'indicators': ['single_use', 'contextual_meaning', 'creative_expression'],
                'appropriate_contexts': [
                    'poetic_language',
                    'metaphorical_expression',
                    'novel_concept_creation',
                    'contextual_word_shortage'
                ],
                'logic': 'Derivational particles create temporary, contextual word usage'
            },
            'permanent_lexicalization': {
                'indicators': ['frequent_use', 'conventional_meaning', 'lexicon_gap'],
                'recommendation': 'create_dedicated_lexical_entry',
                'logic': 'Frequently used derived forms should become permanent lexical entries'
            },
            'validation_approach': {
                'accept_creative_usage': True,
                'flag_potential_lexicalization': True,
                'maintain_phonotactic_integrity': True,
                'logic': 'Balance creative flexibility with systematic integrity'
            }
        }
        
        # Emphasis particle validation rules
        
        # Emphasis particle scope and semantic rules
        self.emphasis_particle_rules = {
            'ma': {
                'type': 'word_emphasis',
                'scope': 'immediate_single_word',
                'target_types': ['noun', 'verb', 'adjective', 'adverb', 'pronoun'],
                'semantic_function': 'contrastive_focus',
                'logic': 'ma emphasizes exactly one word immediately following it'
            }
        }
        
        # Emphasis scope validation rules
        self.emphasis_scope_rules = {
            'immediate_scope': {
                'distance': 1,  # ma must immediately precede its target
                'no_intervening': True,  # no words between ma and target
                'target_required': True,  # ma cannot appear without target
                'logic': 'ma has immediate scope over the single following word'
            },
            'target_restrictions': {
                'allowed_targets': ['noun', 'verb', 'adjective', 'adverb', 'pronoun'],
                'prohibited_targets': ['particle', 'conjunction', 'preposition'],
                'special_cases': {
                    'derived_words': True,  # can emphasize se+noun, ra+verb
                    'compound_constructions': False,  # cannot emphasize entire phrases
                },
                'logic': 'ma can only emphasize content words and derived constructions'
            },
            'multiple_emphasis': {
                'same_sentence': 'allowed',  # multiple ma particles allowed
                'same_word': 'prohibited',  # cannot double-emphasize
                'discourse_effect': 'contrastive_focus',
                'logic': 'Multiple emphasis creates contrastive focus patterns'
            }
        }
        
        # Emphasis-particle interaction rules
        self.emphasis_particle_interactions = {
            'ma_with_animacy': {
                'pattern': 'ma + animacy + noun',
                'validity': 'valid',
                'semantic_effect': 'emphasizes_animacy_distinction',
                'examples': [
                    ('ma he thephoa', 'emphasizes human nature of person'),
                    ('ma pi whiloa', 'emphasizes animate nature of dog'),
                    ('ma ne lowhai', 'emphasizes inanimate nature of answer')
                ],
                'logic': 'ma can emphasize animacy distinctions for contrastive effect'
            },
            'ma_with_comparison': {
                'pattern': 'ma + comparison + adjective',
                'validity': 'valid',
                'semantic_effect': 'emphasizes_degree',
                'examples': [
                    ('ma mo mipho', 'emphasizes comparative blueness'),
                    ('ma pa lophu', 'emphasizes superlative largeness'),
                    ('ma sa hashe', 'emphasizes equal greenness')
                ],
                'logic': 'ma can emphasize comparative and superlative degrees'
            },
            'ma_with_number': {
                'pattern': 'ma + number + noun',
                'validity': 'valid',
                'semantic_effect': 'emphasizes_quantity',
                'examples': [
                    ('ma wo nuthui', 'emphasizes fewness of pebbles'),
                    ('ma lo thephoa', 'emphasizes plurality of people'),
                    ('ma no whiloa', 'emphasizes multitude of dogs')
                ],
                'logic': 'ma can emphasize quantity distinctions for contrast'
            },
            'ma_with_derivational': {
                'pattern': 'ma + derivational + word',
                'validity': 'valid',
                'semantic_effect': 'emphasizes_derived_meaning',
                'examples': [
                    ('ma se lathia', 'emphasizes using-as-axe action'),
                    ('ma ra shola', 'emphasizes walking-as-concept')
                ],
                'logic': 'ma can emphasize the derived meaning of derivational constructions'
            },
            'ma_with_tense': {
                'pattern': 'ma + tense + verb',
                'validity': 'valid',
                'semantic_effect': 'emphasizes_temporal_aspect',
                'examples': [
                    ('ma li shola', 'emphasizes pastness of walking'),
                    ('ma su whuru', 'emphasizes futurity of blowing'),
                    ('ma ta phera', 'emphasizes presentness of being')
                ],
                'logic': 'ma can emphasize temporal distinctions for contrast'
            }
        }
        
        # Emphasis semantic patterns
        self.emphasis_semantic_patterns = {
            'contrastive_focus': {
                'function': 'highlight_contrast',
                'discourse_effect': 'creates_opposition',
                'examples': [
                    ('mia ta shola, ma thi ta whumi', 'I walk, but YOU run'),
                    ('ma mipho lowhai, me hashe', 'the BLUE answer, not green'),
                    ('ma li shola, me su', 'I WALKED, not will')
                ],
                'logic': 'ma creates contrastive focus to highlight differences'
            },
            'corrective_emphasis': {
                'function': 'correct_assumption',
                'discourse_effect': 'clarifies_misunderstanding',
                'examples': [
                    ('me, ma lathia', 'no, an AXE'),
                    ('ma phi whumi', 'ONE run (not multiple)'),
                    ('ma ta, me li', 'PRESENT, not past')
                ],
                'logic': 'ma corrects or clarifies previous statements'
            },
            'intensification': {
                'function': 'strengthen_meaning',
                'discourse_effect': 'adds_emotional_force',
                'examples': [
                    ('ma mipha lowhai', 'BEAUTIFUL answer'),
                    ('ma lophu phiwhai', 'HUGE mountain'),
                    ('ma teshe whomo', 'REALLY like')
                ],
                'logic': 'ma intensifies the meaning of the emphasized word'
            },
            'new_information_focus': {
                'function': 'highlight_new_info',
                'discourse_effect': 'draws_attention',
                'examples': [
                    ('ma whithea li whawi', 'a DOVE flew'),
                    ('ma luthea ta phema', 'a FRIEND comes'),
                    ('ma riwhea ta whuru', 'WIND is blowing')
                ],
                'logic': 'ma highlights new or important information'
            }
        }
        
        # Emphasis positioning rules
        self.emphasis_positioning_rules = {
            'sentence_initial': {
                'pattern': 'ma + [emphasized_word] + [rest_of_sentence]',
                'effect': 'topic_emphasis',
                'examples': [
                    ('ma mia ta shola', 'I (specifically) walk'),
                    ('ma lowhai ta whuru', 'the ANSWER is blowing')
                ],
                'logic': 'Sentence-initial ma creates topic emphasis'
            },
            'sentence_medial': {
                'pattern': '[context] + ma + [emphasized_word] + [continuation]',
                'effect': 'contrastive_focus',
                'examples': [
                    ('mia ta shola, ma thi ta whumi', 'I walk, YOU run'),
                    ('ne lowhai ma riwhea phia whuru', 'the answer in WIND blows')
                ],
                'logic': 'Medial ma creates contrastive focus within discourse'
            },
            'sentence_final': {
                'pattern': '[context] + ma + [emphasized_word]',
                'effect': 'climactic_emphasis',
                'examples': [
                    ('ne lowhai riwhea phia ma whuru', 'the answer in wind BLOWS'),
                    ('he thephoa ta ma shola', 'the person WALKS')
                ],
                'logic': 'Final ma creates climactic emphasis'
            }
        }
        
        # Emphasis discourse coherence rules
        self.emphasis_discourse_rules = {
            'emphasis_chains': {
                'pattern': 'multiple_ma_in_sequence',
                'effect': 'builds_contrast_series',
                'examples': [
                    ('ma mia ta shola, ma thi ta whumi, ma sha ta whawi', 
                     'I walk, YOU run, THEY fly'),
                    ('ma mipho, ma hashe, ma sathi', 'BLUE, GREEN, WHITE')
                ],
                'logic': 'Emphasis chains build contrastive series'
            },
            'emphasis_scope_conflicts': {
                'prohibited_patterns': [
                    'ma ma [word]',  # double emphasis on same word
                    'ma [particle] ma [word]',  # ma emphasizing particles
                    'ma [conjunction]'  # ma emphasizing conjunctions
                ],
                'logic': 'Certain emphasis patterns create semantic conflicts'
            },
            'emphasis_resolution': {
                'ambiguous_scope': 'immediate_word_only',
                'complex_constructions': 'first_content_word',
                'particle_sequences': 'skip_particles_to_content',
                'logic': 'Emphasis scope resolution follows immediate content word principle'
            }
        }
    
    def tokenize_sentence(self, sentence: str) -> List[str]:
        """Tokenize a Phi sentence into words."""
        # Remove punctuation and split on whitespace
        cleaned = re.sub(r'[^\w\s]', '', sentence.lower())
        return cleaned.split()
    
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
        for pos, entries in self.lexicon.items():
            for entry in entries:
                if entry.word == word:
                    return pos
        
        return None
    
    def validate_word_exists(self, word: str) -> List[SentenceValidationError]:
        """Check if a word exists in the Phi lexicon."""
        errors = []
        
        word_type = self.identify_word_type(word)
        if word_type is None:
            errors.append(SentenceValidationError(
                SentenceError.UNKNOWN_WORD,
                f"Unknown word: '{word}'"
            ))
        
        return errors
    
    def validate_particle_order(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate particle ordering within their slots."""
        errors = []
        
        # Track particle positions for each slot
        slot_0_found = []
        slot_1_found = []
        slot_2_groups = []  # Can have multiple slot 2 groups
        
        i = 0
        while i < len(tokens):
            token = tokens[i]
            
            if token in self.slot_0_particles:
                slot_0_found.append((token, i))
            elif token in self.slot_1_particles:
                slot_1_found.append((token, i))
            elif token in self.slot_2_particles:
                # Collect consecutive slot 2 particles
                slot_2_group = []
                while i < len(tokens) and tokens[i] in self.slot_2_particles:
                    slot_2_group.append((tokens[i], i))
                    i += 1
                if slot_2_group:
                    slot_2_groups.append(slot_2_group)
                i -= 1  # Adjust for the outer loop increment
            
            i += 1
        
        # Validate slot 0 ordering
        if len(slot_0_found) > 1:
            for i in range(len(slot_0_found) - 1):
                current_particle = slot_0_found[i][0]
                next_particle = slot_0_found[i + 1][0]
                
                current_order = self._get_particle_order_index(current_particle, self.slot_0_order)
                next_order = self._get_particle_order_index(next_particle, self.slot_0_order)
                
                if current_order > next_order:
                    errors.append(SentenceValidationError(
                        SentenceError.PARTICLE_ORDER,
                        f"Slot 0 particle order violation: '{current_particle}' should come after '{next_particle}'",
                        position=slot_0_found[i][1]
                    ))
        
        # Validate slot 1 ordering
        if len(slot_1_found) > 1:
            for i in range(len(slot_1_found) - 1):
                current_particle = slot_1_found[i][0]
                next_particle = slot_1_found[i + 1][0]
                
                current_order = self._get_particle_order_index(current_particle, self.slot_1_order)
                next_order = self._get_particle_order_index(next_particle, self.slot_1_order)
                
                if current_order > next_order:
                    errors.append(SentenceValidationError(
                        SentenceError.PARTICLE_ORDER,
                        f"Slot 1 particle order violation: '{current_particle}' should come after '{next_particle}'",
                        position=slot_1_found[i][1]
                    ))
        
        # Validate slot 2 ordering within each group
        for group in slot_2_groups:
            if len(group) > 1:
                for i in range(len(group) - 1):
                    current_particle = group[i][0]
                    next_particle = group[i + 1][0]
                    
                    # Special case: allow 'ma' to precede other slot 2 particles when emphasizing
                    if current_particle == 'ma':
                        continue  # ma can precede any other slot 2 particle for emphasis
                    
                    current_order = self._get_particle_order_index(current_particle, self.slot_2_order)
                    next_order = self._get_particle_order_index(next_particle, self.slot_2_order)
                    
                    if current_order > next_order:
                        errors.append(SentenceValidationError(
                            SentenceError.PARTICLE_ORDER,
                            f"Slot 2 particle order violation: '{current_particle}' should come after '{next_particle}'",
                            position=group[i][1]
                        ))
        
        return errors
    
    def _get_particle_order_index(self, particle: str, order_groups: List[List[str]]) -> int:
        """Get the ordering index of a particle within its slot."""
        for i, group in enumerate(order_groups):
            if particle in group:
                return i
        return 999  # Unknown particle gets lowest priority
    
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
    
    def validate_particle_scope(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate that particles are properly positioned relative to their targets."""
        errors = []
        
        for i, token in enumerate(tokens):
            if token in self.slot_1_particles:
                # Slot 1 particles should precede a verb
                verb_found = False
                for j in range(i + 1, len(tokens)):
                    next_word_type = self.identify_word_type(tokens[j])
                    if next_word_type == 'verb':
                        verb_found = True
                        break
                    elif next_word_type and not next_word_type.endswith('_particle'):
                        # Hit a non-verb content word
                        break
                
                if not verb_found:
                    errors.append(SentenceValidationError(
                        SentenceError.PARTICLE_SCOPE,
                        f"Slot 1 particle '{token}' not followed by verb",
                        position=i
                    ))
            
            elif token in self.slot_2_particles:
                # Slot 2 particles should immediately precede their target
                if i + 1 >= len(tokens):
                    errors.append(SentenceValidationError(
                        SentenceError.PARTICLE_SCOPE,
                        f"Slot 2 particle '{token}' at end of sentence",
                        position=i
                    ))
                else:
                    next_word_type = self.identify_word_type(tokens[i + 1])
                    if next_word_type and next_word_type.endswith('_particle'):
                        # Next word is also a particle, which is okay for slot 2
                        continue
                    elif not next_word_type or next_word_type.endswith('_particle'):
                        errors.append(SentenceValidationError(
                            SentenceError.PARTICLE_SCOPE,
                            f"Slot 2 particle '{token}' not followed by content word",
                            position=i
                        ))
        
        return errors
    
    def validate_subordinate_tense(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate tense usage in subordinate clauses."""
        errors = []
        
        for i, token in enumerate(tokens):
            if token in self.subordinate_conjunctions:
                conjunction_info = self.subordinate_conjunctions[token]
                expected_tenses = conjunction_info['expected_tense']
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
        
        # Find all temporal elements in the sentence
        tense_markers = []
        aspect_markers = []
        mood_markers = []
        temporal_adverbs = []
        
        for i, token in enumerate(tokens):
            if token in self.tense_particles:
                tense_markers.append((token, i))
            elif token in self.aspect_particles:
                aspect_markers.append((token, i))
            elif token in self.mood_particles:
                mood_markers.append((token, i))
            elif token in self.temporal_adverb_tense:
                temporal_adverbs.append((token, i))
        
        # 1. Check for multiple tense markers
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
            word_type = self.identify_word_type(token)
            
            # Track animacy particles with their target nouns
            if token in ['he', 'pi', 'ne']:
                # Find the noun this animacy particle modifies
                for j in range(i + 1, min(i + 3, len(tokens))):  # Look ahead 2 positions
                    next_word_type = self.identify_word_type(tokens[j])
                    if next_word_type == 'noun':
                        nouns_with_particles.append((tokens[j], token, j, i))
                        break
            
            # Track classifiers with their target nouns
            elif word_type == 'classifier':
                # Find the noun this classifier modifies
                for j in range(i + 1, min(i + 3, len(tokens))):
                    next_word_type = self.identify_word_type(tokens[j])
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
                    prev_word_type = self.identify_word_type(tokens[j])
                    if prev_word_type == 'noun' and not subject_found:
                        subjects.append((tokens[j], j, token))
                        subject_found = True
                        break
                
                # Find object (immediately after 'na')
                for j in range(i):
                    if tokens[j] == 'na' and j + 1 < len(tokens):
                        next_word_type = self.identify_word_type(tokens[j + 1])
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
    
    def validate_modal_logic(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate modal logic including obligative, conditional, and desiderative constructions."""
        errors = []
        
        # 1. Validate obligative constructions (ru + base verb)
        errors.extend(self._validate_obligative_constructions(tokens))
        
        # 2. Validate conditional structures (wetu clauses)
        errors.extend(self._validate_conditional_structures(tokens))
        
        # 3. Validate desiderative constructions (we + infinitive)
        errors.extend(self._validate_desiderative_constructions(tokens))
        
        return errors
    
    def _validate_obligative_constructions(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate obligative ru constructions."""
        errors = []
        
        for i, token in enumerate(tokens):
            if token == 'ru':
                # Find the verb that ru modifies
                verb_found = False
                intervening_tense = None
                
                for j in range(i + 1, len(tokens)):
                    next_token = tokens[j]
                    next_word_type = self.identify_word_type(next_token)
                    
                    # Check for intervening tense markers (prohibited)
                    if next_token in self.obligative_rules['prohibited_particles']:
                        intervening_tense = (next_token, j)
                    
                    # Found the verb
                    elif next_word_type == 'verb':
                        verb_found = True
                        
                        # Check if there was intervening tense
                        if intervening_tense:
                            errors.append(SentenceValidationError(
                                SentenceError.MODAL_VERB_FORM_ERROR,
                                f"Obligative 'ru' cannot have tense marker '{intervening_tense[0]}' before verb '{next_token}'. {self.obligative_rules['logic']}",
                                position=intervening_tense[1]
                            ))
                        break
                    
                    # Stop if we hit another content word or clause boundary
                    elif next_word_type and not next_word_type.endswith('_particle'):
                        break
                
                if not verb_found:
                    errors.append(SentenceValidationError(
                        SentenceError.MODAL_VERB_FORM_ERROR,
                        f"Obligative 'ru' not followed by verb. {self.obligative_rules['logic']}",
                        position=i
                    ))
        
        return errors
    
    def _validate_conditional_structures(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate conditional wetu clause structures."""
        errors = []
        
        for i, token in enumerate(tokens):
            if token == 'wetu':
                # Parse the conditional structure
                protasis_tense = None  # if-clause tense
                apodosis_tense = None  # then-clause tense
                
                # Find tense in protasis (if-clause) - after wetu
                for j in range(i + 1, len(tokens)):
                    if tokens[j] in self.conditional_rules['protasis_tenses'] + ['li']:
                        protasis_tense = tokens[j]
                        break
                    elif self.identify_word_type(tokens[j]) == 'verb':
                        # Reached verb without explicit tense (default present)
                        protasis_tense = 'ta'
                        break
                
                # Find tense in apodosis (main clause) - before wetu
                for j in range(i - 1, -1, -1):
                    if tokens[j] in self.conditional_rules['apodosis_tenses'] + ['li', 'ta']:
                        apodosis_tense = tokens[j]
                        break
                    elif self.identify_word_type(tokens[j]) == 'verb':
                        # Reached verb without explicit tense (default present)
                        apodosis_tense = 'ta'
                        break
                
                # Validate tense combinations
                if protasis_tense and apodosis_tense:
                    # Check for prohibited combinations
                    combination = (protasis_tense, apodosis_tense)
                    if combination in self.conditional_rules['prohibited_combinations']:
                        errors.append(SentenceValidationError(
                            SentenceError.CONDITIONAL_STRUCTURE_ERROR,
                            f"Illogical conditional: if-clause '{protasis_tense}' with then-clause '{apodosis_tense}'. {self.conditional_rules['logic']}",
                            position=i
                        ))
                    
                    # Check if protasis uses appropriate tense
                    if protasis_tense not in self.conditional_rules['protasis_tenses'] and protasis_tense != 'ta':
                        errors.append(SentenceValidationError(
                            SentenceError.CONDITIONAL_STRUCTURE_ERROR,
                            f"Conditional if-clause should use present or future tense, not '{protasis_tense}'",
                            position=i
                        ))
        
        return errors
    
    def _validate_desiderative_constructions(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate desiderative we constructions."""
        errors = []
        
        # Note: This is complex because 'we' can be perfective aspect OR desiderative
        # For now, we'll implement basic validation for desiderative patterns
        
        for i, token in enumerate(tokens):
            if token == 'we':
                # Determine if this is desiderative (want) or perfective aspect
                # Heuristic: if followed by 'te' marker, likely desiderative
                is_desiderative = False
                
                for j in range(i + 1, min(i + 4, len(tokens))):
                    if tokens[j] == 'te':
                        is_desiderative = True
                        break
                
                if is_desiderative:
                    # Validate desiderative structure
                    te_found = False
                    complement_verb = False
                    
                    for j in range(i + 1, len(tokens)):
                        if tokens[j] == 'te':
                            te_found = True
                        elif te_found and self.identify_word_type(tokens[j]) == 'verb':
                            complement_verb = True
                            break
                    
                    if te_found and not complement_verb:
                        errors.append(SentenceValidationError(
                            SentenceError.DESIDERATIVE_CONSTRUCTION_ERROR,
                            f"Desiderative 'we' with 'te' marker missing complement verb. {self.desiderative_rules['logic']}",
                            position=i
                        ))
                    elif not te_found:
                        # Could be perfective, but if context suggests desiderative...
                        # This would need more sophisticated analysis
                        pass
        
        return errors
    
    def validate_narrative_sequence(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate narrative sequence logic and relative clause consistency."""
        errors = []
        
        # 1. Validate temporal conjunction sequences
        errors.extend(self._validate_temporal_sequences(tokens))
        
        # 2. Validate relative clause tense consistency
        errors.extend(self._validate_relative_clause_tenses(tokens))
        
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
    
    def _find_clause_tense(self, tokens: List[str], start: int, end: int) -> Optional[str]:
        """Find the tense marker in a clause segment."""
        for i in range(start, end):
            if i < len(tokens) and tokens[i] in self.tense_particles:
                return tokens[i]
        
        # If no explicit tense found, default to present
        # But only if there's a verb in this segment
        for i in range(start, end):
            if i < len(tokens) and self.identify_word_type(tokens[i]) == 'verb':
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
    
    def validate_interrogative_constructions(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate interrogative constructions and question-answer tense matching."""
        errors = []
        
        # 1. Validate yes/no questions
        errors.extend(self._validate_yes_no_questions(tokens))
        
        # 2. Validate wh-questions
        errors.extend(self._validate_wh_questions(tokens))
        
        # 3. Validate rhetorical questions
        errors.extend(self._validate_rhetorical_questions(tokens))
        
        # 4. Validate question context appropriateness
        errors.extend(self._validate_question_context(tokens))
        
        return errors
    
    def _validate_yes_no_questions(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate yes/no question constructions with 'wa' particle."""
        errors = []
        
        for i, token in enumerate(tokens):
            if token == 'wa':
                # Find the tense used in this question
                question_tense = self._find_clause_tense(tokens, 0, len(tokens))
                
                if question_tense:
                    # Check if tense is contextually appropriate for yes/no questions
                    tense_logic = self.interrogative_rules['yes_no_questions']['tense_logic']
                    
                    if question_tense in tense_logic:
                        # This is a valid tense for yes/no questions
                        # Could add more sophisticated context checking here
                        pass
                    else:
                        # Unusual tense for yes/no questions
                        errors.append(SentenceValidationError(
                            SentenceError.INTERROGATIVE_TENSE_ERROR,
                            f"Yes/no question with unusual tense '{question_tense}'. Consider using li/ta/su/ru for clearer meaning",
                            position=i
                        ))
        
        return errors
    
    def _validate_wh_questions(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate wh-question constructions."""
        errors = []
        
        for i, token in enumerate(tokens):
            if token in self.interrogative_rules['wh_questions']['markers']:
                # Check for invalid wa + wh-question combination
                if 'wa' in tokens:
                    wa_position = tokens.index('wa')
                    if wa_position < i:  # wa comes before the wh-word
                        errors.append(SentenceValidationError(
                            SentenceError.QUESTION_CONTEXT_MISMATCH,
                            f"Cannot combine 'wa' (yes/no question) with wh-question word '{token}'. Use either 'wa' for yes/no questions or wh-words alone for information questions.",
                            position=wa_position
                        ))
                
                # Find the tense used with this wh-word
                question_tense = self._find_clause_tense(tokens, 0, len(tokens))
                
                if question_tense and token in self.interrogative_rules['wh_questions']['tense_constraints']:
                    constraints = self.interrogative_rules['wh_questions']['tense_constraints'][token]
                    
                    # Check if tense is preferred for this wh-word
                    if 'preferred_tenses' in constraints and question_tense not in constraints['preferred_tenses']:
                        errors.append(SentenceValidationError(
                            SentenceError.INTERROGATIVE_TENSE_ERROR,
                            f"Wh-question '{token}' with tense '{question_tense}' may be contextually odd. {constraints['logic']}",
                            position=i
                        ))
                    
                    # Check if tense should be avoided
                    if 'avoid_tenses' in constraints and question_tense in constraints['avoid_tenses']:
                        errors.append(SentenceValidationError(
                            SentenceError.QUESTION_CONTEXT_MISMATCH,
                            f"Wh-question '{token}' with tense '{question_tense}' is semantically problematic. {constraints['logic']}",
                            position=i
                        ))
                
                # Check for semantically problematic combinations
                inappropriate_combinations = self.interrogative_contexts['information_seeking']['inappropriate_combinations']
                for wh_word, tense in inappropriate_combinations:
                    if token == wh_word and question_tense == tense:
                        errors.append(SentenceValidationError(
                            SentenceError.QUESTION_CONTEXT_MISMATCH,
                            f"Semantically odd combination: '{wh_word}' with tense '{tense}'. {self.interrogative_contexts['information_seeking']['logic']}",
                            position=i
                        ))
        
        return errors
    
    def _validate_rhetorical_questions(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate rhetorical question patterns."""
        errors = []
        
        # Look for rhetorical question indicators
        has_rhetorical_indicator = any(token in self.interrogative_rules['rhetorical_questions']['indicators'] for token in tokens)
        has_question_marker = 'wa' in tokens or any(token in self.interrogative_rules['wh_questions']['markers'] for token in tokens)
        
        if has_rhetorical_indicator and has_question_marker:
            # This appears to be a rhetorical question
            question_tense = self._find_clause_tense(tokens, 0, len(tokens))
            
            if question_tense:
                # Check if tense pattern is appropriate for rhetorical questions
                rhetorical_patterns = self.interrogative_rules['rhetorical_questions']['tense_patterns']
                
                is_appropriate = False
                for pattern_type, tenses in rhetorical_patterns.items():
                    if question_tense in tenses:
                        is_appropriate = True
                        break
                
                if not is_appropriate:
                    errors.append(SentenceValidationError(
                        SentenceError.INTERROGATIVE_TENSE_ERROR,
                        f"Rhetorical question with tense '{question_tense}' may lack philosophical force. {self.interrogative_rules['rhetorical_questions']['logic']}",
                        position=0
                    ))
        
        return errors
    
    def _validate_question_context(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate overall question context and appropriateness."""
        errors = []
        
        # Check if this is a question (has question markers)
        is_question = ('wa' in tokens or 
                      any(token in self.interrogative_rules['wh_questions']['markers'] for token in tokens))
        
        if is_question:
            question_tense = self._find_clause_tense(tokens, 0, len(tokens))
            
            # Validate context appropriateness
            if question_tense:
                # Check for confirmation-seeking questions
                if 'wa' in tokens:
                    confirmation_rules = self.interrogative_contexts['confirmation_seeking']
                    if question_tense in confirmation_rules['tense_appropriateness']:
                        # This is contextually appropriate
                        pass
                    else:
                        # Could be improved but not necessarily wrong
                        pass
                
                # Check for deliberative questions
                if 'ru' in tokens or 'su' in tokens:
                    # This appears to be deliberative
                    if question_tense not in ['ru', 'su', 'ta']:
                        errors.append(SentenceValidationError(
                            SentenceError.QUESTION_CONTEXT_MISMATCH,
                            f"Deliberative question with tense '{question_tense}' may be contextually inappropriate. {self.interrogative_contexts['deliberative']['logic']}",
                            position=0
                        ))
        
        return errors
    
    def validate_sentence(self, sentence: str) -> Dict:
        """Comprehensive validation of a Phi sentence."""
        tokens = self.tokenize_sentence(sentence)
        
        if not tokens:
            return {
                "sentence": sentence,
                "tokens": tokens,
                "errors": [SentenceValidationError(
                    SentenceError.INVALID_WORD,
                    "Empty sentence"
                )],
                "is_valid": False,
                "error_summary": {"Empty sentence": 1}
            }
        
        all_errors = []
        
        # 1. Validate all words exist
        for i, token in enumerate(tokens):
            word_errors = self.validate_word_exists(token)
            for error in word_errors:
                error.position = i
                error.word = token
            all_errors.extend(word_errors)
        
        # 2. Validate particle ordering
        all_errors.extend(self.validate_particle_order(tokens))
        
        # 3. Validate SOV word order
        all_errors.extend(self.validate_sov_order(tokens))
        
        # 4. Validate particle scope
        all_errors.extend(self.validate_particle_scope(tokens))
        
        # 5. Validate subordinate tense
        all_errors.extend(self.validate_subordinate_tense(tokens))
        
        # 6. Validate comprehensive tense
        all_errors.extend(self.validate_comprehensive_tense(tokens))
        
        # 7. Validate semantic roles
        all_errors.extend(self.validate_semantic_roles(tokens))
        
        # 8. Validate modal logic
        all_errors.extend(self.validate_modal_logic(tokens))
        
        # 9. Validate narrative sequence
        all_errors.extend(self.validate_narrative_sequence(tokens))
        
        # 10. Validate interrogative constructions
        all_errors.extend(self.validate_interrogative_constructions(tokens))
        
        # 11. Validate evidentiality usage
        all_errors.extend(self.validate_evidentiality_usage(tokens))
        
        # 12. Validate derivational particles
        all_errors.extend(self.validate_derivational_particles(tokens))
        
        # 13. Validate emphasis particle scope
        all_errors.extend(self.validate_emphasis_particle_scope(tokens))
        
        # 14. Validate politeness particle context
        all_errors.extend(self.validate_politeness_particle_context(tokens))
        
        # 15. Validate discourse particle sequences
        all_errors.extend(self.validate_discourse_particle_sequences(tokens))
        
        # Summarize errors by type
        error_summary = {}
        for error in all_errors:
            error_type = error.error_type.value
            error_summary[error_type] = error_summary.get(error_type, 0) + 1
        
        return {
            "sentence": sentence,
            "tokens": tokens,
            "errors": all_errors,
            "is_valid": len(all_errors) == 0,
            "error_summary": error_summary
        }
    
    def generate_sentence_report(self, validation_result: Dict) -> str:
        """Generate a formatted sentence validation report."""
        sentence = validation_result["sentence"]
        tokens = validation_result["tokens"]
        errors = validation_result["errors"]
        is_valid = validation_result["is_valid"]
        
        report = f"""
PHI SENTENCE VALIDATION REPORT
==============================
Sentence: {sentence}
Tokens: {' | '.join(tokens)}

VALIDATION STATUS: {'✅ VALID' if is_valid else '❌ INVALID'}
"""
        
        if errors:
            report += f"\nERRORS FOUND ({len(errors)}):\n"
            for i, error in enumerate(errors, 1):
                position_info = f" (position {error.position})" if error.position is not None else ""
                word_info = f" [word: {error.word}]" if error.word else ""
                report += f"  {i}. [{error.error_type.value.upper()}]{position_info} {error.message}{word_info}\n"
            
            # Error summary
            report += f"\nERROR SUMMARY:\n"
            for error_type, count in validation_result["error_summary"].items():
                report += f"  {error_type}: {count}\n"
        else:
            report += "\n✅ No errors found - sentence follows all Phi grammar rules!\n"
        
        return report
    
    def validate_evidentiality_usage(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate evidentiality particle usage including combinations and nesting."""
        errors = []
        
        # Find all evidentiality particles in the sentence
        evidentiality_particles = []
        for i, token in enumerate(tokens):
            if token in self.evidentiality_particles:
                evidentiality_particles.append((token, i))
        
        if not evidentiality_particles:
            return errors  # No evidentiality particles to validate
        
        # Validate multiple evidentiality markers
        errors.extend(self._validate_evidentiality_combinations(evidentiality_particles, tokens))
        
        # Validate evidentiality-tense interactions
        errors.extend(self._validate_evidentiality_tense_interactions(evidentiality_particles, tokens))
        
        # Validate reported speech nesting
        errors.extend(self._validate_reported_speech_nesting(evidentiality_particles, tokens))
        
        return errors
    
    def _validate_evidentiality_combinations(self, evidentiality_particles: List[Tuple[str, int]], 
                                           tokens: List[str]) -> List[SentenceValidationError]:
        """Validate combinations of multiple evidentiality markers."""
        errors = []
        
        if len(evidentiality_particles) < 2:
            return errors  # No combinations to validate
        
        # Check for prohibited combinations
        for i in range(len(evidentiality_particles)):
            for j in range(i + 1, len(evidentiality_particles)):
                particle1, pos1 = evidentiality_particles[i]
                particle2, pos2 = evidentiality_particles[j]
                
                combination = (particle1, particle2)
                reverse_combination = (particle2, particle1)
                
                # Check if this combination is prohibited
                if (combination in self.evidentiality_combinations['prohibited_combinations'] or
                    reverse_combination in self.evidentiality_combinations['prohibited_combinations']):
                    
                    # Check if it's an allowed sequence (order matters)
                    if (combination not in self.evidentiality_combinations['allowed_sequences'] and
                        reverse_combination not in self.evidentiality_combinations['allowed_sequences']):
                        
                        errors.append(SentenceValidationError(
                            SentenceError.EVIDENTIALITY_COMBINATION_ERROR,
                            f"Prohibited evidentiality combination: '{particle1}' and '{particle2}' "
                            f"create contradictory epistemic stances",
                            position=min(pos1, pos2),
                            word=f"{particle1}+{particle2}"
                        ))
        
        return errors
    
    def _validate_evidentiality_tense_interactions(self, evidentiality_particles: List[Tuple[str, int]], 
                                                 tokens: List[str]) -> List[SentenceValidationError]:
        """Validate evidentiality-tense semantic compatibility."""
        errors = []
        
        # Find tense particles in the sentence
        tense_particles = []
        for i, token in enumerate(tokens):
            if token in self.tense_particles:
                tense_particles.append((token, i))
        
        # Validate each evidentiality-tense combination
        for evid_particle, evid_pos in evidentiality_particles:
            evid_info = self.evidentiality_particles[evid_particle]
            
            for tense_particle, tense_pos in tense_particles:
                # Check if this tense is incompatible with this evidentiality
                if 'incompatible_tenses' in evid_info and tense_particle in evid_info['incompatible_tenses']:
                    errors.append(SentenceValidationError(
                        SentenceError.EVIDENTIALITY_TENSE_CONFLICT,
                        f"Evidentiality '{evid_particle}' is incompatible with tense '{tense_particle}': "
                        f"{evid_info['logic']}",
                        position=evid_pos,
                        word=f"{evid_particle}+{tense_particle}"
                    ))
                
                # Check specific tense logic rules
                interaction_key = f"{evid_particle}_{tense_particle}"
                if evid_particle in ['hi', 'mu', 'pe', 'ro']:
                    logic_rules = self.evidentiality_tense_interactions.get(f"{evid_particle}_tense_logic", {})
                    validity = logic_rules.get(interaction_key, 'unknown')
                    
                    if validity == 'invalid':
                        errors.append(SentenceValidationError(
                            SentenceError.EVIDENTIALITY_TENSE_CONFLICT,
                            f"Invalid evidentiality-tense combination: '{evid_particle}' + '{tense_particle}' "
                            f"violates temporal logic - {logic_rules.get('logic', 'semantic contradiction')}",
                            position=evid_pos,
                            word=f"{evid_particle}+{tense_particle}"
                        ))
                    elif validity == 'marginal':
                        # Note: Could add warnings for marginal cases if desired
                        pass
        
        return errors
    
    def _validate_reported_speech_nesting(self, evidentiality_particles: List[Tuple[str, int]], 
                                        tokens: List[str]) -> List[SentenceValidationError]:
        """Validate reported speech nesting patterns."""
        errors = []
        
        # Find nu (hearsay) and ti (direct reported) particles
        nu_positions = [pos for particle, pos in evidentiality_particles if particle == 'nu']
        ti_positions = [pos for particle, pos in evidentiality_particles if particle == 'ti']
        
        if not (nu_positions and ti_positions):
            return errors  # No nesting to validate
        
        # Validate ti within nu nesting
        for nu_pos in nu_positions:
            for ti_pos in ti_positions:
                if ti_pos > nu_pos:
                    # Valid nesting: nu comes before ti
                    # Check that the structure follows the expected pattern
                    self._validate_ti_within_nu_structure(tokens, nu_pos, ti_pos, errors)
                elif ti_pos < nu_pos:
                    # Invalid: ti cannot contain nu
                    errors.append(SentenceValidationError(
                        SentenceError.REPORTED_SPEECH_NESTING_ERROR,
                        f"Invalid nesting: direct reported speech 'ti' cannot contain hearsay 'nu' - "
                        f"violates source specificity hierarchy",
                        position=ti_pos,
                        word="ti+nu"
                    ))
        
        # Check for prohibited nestings
        self._validate_prohibited_evidentiality_nesting(evidentiality_particles, tokens, errors)
        
        return errors
    
    def _validate_ti_within_nu_structure(self, tokens: List[str], nu_pos: int, ti_pos: int, 
                                       errors: List[SentenceValidationError]):
        """Validate the structure of ti within nu nesting."""
        # The structure should be: nu [context] ti [quoted_content]
        # where the quoted content has independent tense marking
        
        # Check that there's content between nu and ti (the context)
        if ti_pos - nu_pos <= 1:
            errors.append(SentenceValidationError(
                SentenceError.REPORTED_SPEECH_NESTING_ERROR,
                f"Invalid 'nu...ti' structure: missing context between hearsay marker 'nu' "
                f"and direct quote marker 'ti'",
                position=nu_pos,
                word="nu...ti"
            ))
            return
        
        # Check for independent tense marking in quoted portion
        quoted_portion = tokens[ti_pos + 1:]
        context_portion = tokens[nu_pos + 1:ti_pos]
        
        # The quoted portion should have its own tense marking
        quoted_has_tense = any(token in self.tense_particles for token in quoted_portion)
        context_has_tense = any(token in self.tense_particles for token in context_portion)
        
        if not quoted_has_tense and len(quoted_portion) > 1:
            # Note: This is a stylistic preference, not a hard error
            # Could add as a warning if desired
            pass
    
    def _validate_prohibited_evidentiality_nesting(self, evidentiality_particles: List[Tuple[str, int]], 
                                                 tokens: List[str], errors: List[SentenceValidationError]):
        """Check for prohibited evidentiality nesting patterns."""
        
        # Check for ti within ti (nested direct quotes)
        ti_positions = [pos for particle, pos in evidentiality_particles if particle == 'ti']
        if len(ti_positions) > 1:
            errors.append(SentenceValidationError(
                SentenceError.REPORTED_SPEECH_NESTING_ERROR,
                f"Prohibited nesting: multiple 'ti' (direct reported speech) markers - "
                f"cannot nest direct quotes within direct quotes",
                position=min(ti_positions),
                word="ti+ti"
            ))
        
        # Check for hi (direct observation) in any reported context
        hi_positions = [pos for particle, pos in evidentiality_particles if particle == 'hi']
        reported_positions = [pos for particle, pos in evidentiality_particles if particle in ['nu', 'ti']]
        
        for hi_pos in hi_positions:
            for rep_pos in reported_positions:
                if rep_pos < hi_pos:  # reported context before direct observation
                    errors.append(SentenceValidationError(
                        SentenceError.REPORTED_SPEECH_NESTING_ERROR,
                        f"Prohibited nesting: direct observation 'hi' cannot occur within "
                        f"reported speech context - contradicts evidential source",
                        position=hi_pos,
                        word="hi_in_reported"
                    ))
        
        # Check for ro (inference) within reported speech
        ro_positions = [pos for particle, pos in evidentiality_particles if particle == 'ro']
        for ro_pos in ro_positions:
            for rep_pos in reported_positions:
                if rep_pos < ro_pos:  # reported context before inference
                    errors.append(SentenceValidationError(
                        SentenceError.REPORTED_SPEECH_NESTING_ERROR,
                        f"Prohibited nesting: inference 'ro' within reported speech context - "
                        f"inference should be speaker's own reasoning, not reported",
                        position=ro_pos,
                        word="ro_in_reported"
                    ))
    
    def validate_derivational_particles(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate derivational particle usage including se and ra constructions."""
        errors = []
        
        # Find all derivational particles in the sentence
        derivational_particles = []
        for i, token in enumerate(tokens):
            if token in self.derivational_particles:
                derivational_particles.append((token, i))
        
        if not derivational_particles:
            return errors  # No derivational particles to validate
        
        # Validate each derivational particle
        for particle, position in derivational_particles:
            # Validate scope and target requirements
            errors.extend(self._validate_derivational_scope(particle, position, tokens))
            
            # Validate semantic appropriateness
            errors.extend(self._validate_derivational_semantics(particle, position, tokens))
            
            # Validate phonotactic consistency
            errors.extend(self._validate_derivational_phonotactics(particle, position, tokens))
            
            # Validate contextual usage
            errors.extend(self._validate_derivational_context(particle, position, tokens))
        
        # Validate derivational conflicts and interactions
        errors.extend(self._validate_derivational_conflicts(derivational_particles, tokens))
        
        return errors
    
    def _validate_derivational_scope(self, particle: str, position: int, 
                                   tokens: List[str]) -> List[SentenceValidationError]:
        """Validate derivational particle scope and target requirements."""
        errors = []
        
        particle_info = self.derivational_particles[particle]
        scope_rules = self.derivational_scope_rules.get(f"{particle}_scope", {})
        
        # Check if particle has a valid target
        target_found = False
        target_word = None
        target_pos = None
        
        # Look for target word after the particle
        for i in range(position + 1, len(tokens)):
            token = tokens[i]
            word_type = self.identify_word_type(token)
            
            # Check for intervening particles that conflict
            if token in scope_rules.get('no_intervening_particles', []):
                errors.append(SentenceValidationError(
                    SentenceError.DERIVATIONAL_SCOPE_ERROR,
                    f"Derivational particle '{particle}' cannot have '{token}' between it and target word. "
                    f"{self.derivational_scope_rules['derivational_conflicts'][f'{particle}_animacy_conflict' if particle == 'se' else f'{particle}_tense_conflict']['logic']}",
                    position=i,
                    word=f"{particle}+{token}"
                ))
            
            # Check for allowed intervening particles
            elif token in scope_rules.get('allowed_intervening', []):
                continue  # Skip allowed intervening particles
            
            # Found potential target
            elif word_type in scope_rules.get('target_requirements', []):
                target_found = True
                target_word = token
                target_pos = i
                break
            
            # Hit unexpected word type
            elif word_type and not word_type.endswith('_particle'):
                break
        
        # Validate target requirements
        if not target_found:
            expected_target = particle_info['source_pos']
            errors.append(SentenceValidationError(
                SentenceError.DERIVATIONAL_SCOPE_ERROR,
                f"Derivational particle '{particle}' not followed by {expected_target}. "
                f"{scope_rules.get('logic', particle_info['logic'])}",
                position=position,
                word=particle
            ))
        
        return errors
    
    def _validate_derivational_semantics(self, particle: str, position: int, 
                                       tokens: List[str]) -> List[SentenceValidationError]:
        """Validate semantic appropriateness of derivational constructions."""
        errors = []
        
        # Find the target word
        target_word = None
        for i in range(position + 1, min(position + 3, len(tokens))):
            if i < len(tokens):
                word_type = self.identify_word_type(tokens[i])
                expected_type = self.derivational_particles[particle]['source_pos']
                if word_type == expected_type:
                    target_word = tokens[i]
                    break
        
        if not target_word:
            return errors  # No target to validate semantics
        
        # Validate semantic appropriateness
        if particle == 'se':
            # Check if noun is appropriate for verbal usage
            is_appropriate = self._is_noun_appropriate_for_se(target_word)
            if not is_appropriate:
                errors.append(SentenceValidationError(
                    SentenceError.DERIVATIONAL_SEMANTIC_ERROR,
                    f"Noun '{target_word}' may be semantically inappropriate for verbal usage with 'se'. "
                    f"Consider if this noun has clear actionable or processual meaning.",
                    position=position,
                    word=f"se+{target_word}"
                ))
        
        elif particle == 'ra':
            # Check if verb is appropriate for nominal usage
            is_appropriate = self._is_verb_appropriate_for_ra(target_word)
            if not is_appropriate:
                errors.append(SentenceValidationError(
                    SentenceError.DERIVATIONAL_SEMANTIC_ERROR,
                    f"Verb '{target_word}' may be semantically inappropriate for nominal usage with 'ra'. "
                    f"Consider if this verb represents a conceptualizable action or process.",
                    position=position,
                    word=f"ra+{target_word}"
                ))
        
        return errors
    
    def _validate_derivational_phonotactics(self, particle: str, position: int, 
                                          tokens: List[str]) -> List[SentenceValidationError]:
        """Validate phonotactic consistency of derivational constructions."""
        errors = []
        
        # Find the target word
        target_word = None
        target_position = None
        for i in range(position + 1, min(position + 3, len(tokens))):
            if i < len(tokens):
                word_type = self.identify_word_type(tokens[i])
                expected_type = self.derivational_particles[particle]['source_pos']
                if word_type == expected_type:
                    target_word = tokens[i]
                    target_position = i
                    break
        
        if not target_word:
            return errors  # No target to validate
        
        # Validate that the source word follows correct phonotactics
        # For derivational validation, we check phonotactics without meaning
        phonotactic_errors = self.word_validator.validate_phonotactics(target_word, expected_type)
        if phonotactic_errors:
            error_messages = [error.message for error in phonotactic_errors]
            errors.append(SentenceValidationError(
                SentenceError.DERIVATIONAL_PHONOTACTIC_ERROR,
                f"Source word '{target_word}' for derivational particle '{particle}' has phonotactic errors: "
                f"{', '.join(error_messages)}",
                position=target_position,
                word=f"{particle}+{target_word}"
            ))
        
        # Validate positional usage (derived form used in correct syntactic position)
        if particle == 'se':
            # se+noun should be used in verb position
            is_in_verb_position = self._is_in_verb_position(position, tokens)
            if not is_in_verb_position:
                errors.append(SentenceValidationError(
                    SentenceError.DERIVATIONAL_PHONOTACTIC_ERROR,
                    f"Derived verb 'se {target_word}' not used in verb position. "
                    f"Derived verbs must follow SOV order requirements.",
                    position=position,
                    word=f"se+{target_word}"
                ))
        
        elif particle == 'ra':
            # ra+verb should be used in noun position
            is_in_noun_position = self._is_in_noun_position(position, tokens)
            if not is_in_noun_position:
                errors.append(SentenceValidationError(
                    SentenceError.DERIVATIONAL_PHONOTACTIC_ERROR,
                    f"Derived noun 'ra {target_word}' not used in noun position. "
                    f"Derived nouns must follow SOV order requirements.",
                    position=position,
                    word=f"ra+{target_word}"
                ))
        
        return errors
    
    def _validate_derivational_context(self, particle: str, position: int, 
                                     tokens: List[str]) -> List[SentenceValidationError]:
        """Validate contextual appropriateness of derivational usage."""
        errors = []
        
        # Find the target word
        target_word = None
        for i in range(position + 1, min(position + 3, len(tokens))):
            if i < len(tokens):
                word_type = self.identify_word_type(tokens[i])
                expected_type = self.derivational_particles[particle]['source_pos']
                if word_type == expected_type:
                    target_word = tokens[i]
                    break
        
        if not target_word:
            return errors  # No target to validate
        
        # Check for contextual appropriateness based on usage patterns
        if particle == 'se':
            usage_pattern = self._identify_se_usage_pattern(target_word)
            if usage_pattern:
                # Valid usage pattern identified - this is good
                pass
            else:
                # No clear usage pattern - flag for review
                errors.append(SentenceValidationError(
                    SentenceError.DERIVATIONAL_CONTEXT_WARNING,
                    f"Derivational usage 'se {target_word}' may need contextual clarification. "
                    f"Consider if this follows instrumental, metaphorical, or substance usage patterns.",
                    position=position,
                    word=f"se+{target_word}"
                ))
        
        elif particle == 'ra':
            usage_pattern = self._identify_ra_usage_pattern(target_word)
            if usage_pattern:
                # Valid usage pattern identified - this is good
                pass
            else:
                # No clear usage pattern - flag for review
                errors.append(SentenceValidationError(
                    SentenceError.DERIVATIONAL_CONTEXT_WARNING,
                    f"Derivational usage 'ra {target_word}' may need contextual clarification. "
                    f"Consider if this follows gerund, abstract concept, or result usage patterns.",
                    position=position,
                    word=f"ra+{target_word}"
                ))
        
        return errors
    
    def _validate_derivational_conflicts(self, derivational_particles: List[Tuple[str, int]], 
                                       tokens: List[str]) -> List[SentenceValidationError]:
        """Validate conflicts between derivational particles and other elements."""
        errors = []
        
        # Check for double derivation (se + ra or ra + se)
        if len(derivational_particles) > 1:
            particles_only = [particle for particle, _ in derivational_particles]
            if 'se' in particles_only and 'ra' in particles_only:
                errors.append(SentenceValidationError(
                    SentenceError.DERIVATIONAL_CONFLICT_ERROR,
                    f"Double derivation detected: cannot use both 'se' and 'ra' in same construction. "
                    f"{self.derivational_scope_rules['derivational_conflicts']['double_derivation']['logic']}",
                    position=min(pos for _, pos in derivational_particles),
                    word="se+ra"
                ))
        
        # Check for conflicts with animacy markers (for se)
        se_positions = [pos for particle, pos in derivational_particles if particle == 'se']
        for se_pos in se_positions:
            # Look for conflicting animacy markers near se
            for i in range(max(0, se_pos - 2), min(len(tokens), se_pos + 4)):
                if tokens[i] in ['he', 'pi', 'ne']:
                    # Check if this animacy marker is for the derived verb
                    if i > se_pos:  # animacy marker after se
                        errors.append(SentenceValidationError(
                            SentenceError.DERIVATIONAL_CONFLICT_ERROR,
                            f"Animacy marker '{tokens[i]}' conflicts with derived verb 'se'. "
                            f"{self.derivational_scope_rules['derivational_conflicts']['se_animacy_conflict']['logic']}",
                            position=i,
                            word=f"se+{tokens[i]}"
                        ))
        
        # Check for conflicts with tense markers (for ra)
        ra_positions = [pos for particle, pos in derivational_particles if particle == 'ra']
        for ra_pos in ra_positions:
            # Look for conflicting tense markers near ra
            for i in range(max(0, ra_pos - 2), min(len(tokens), ra_pos + 4)):
                if tokens[i] in ['li', 'ta', 'su']:
                    # Check if this tense marker is for the derived noun
                    if i < ra_pos:  # tense marker before ra (affecting derived noun)
                        errors.append(SentenceValidationError(
                            SentenceError.DERIVATIONAL_CONFLICT_ERROR,
                            f"Tense marker '{tokens[i]}' conflicts with derived noun 'ra'. "
                            f"{self.derivational_scope_rules['derivational_conflicts']['ra_tense_conflict']['logic']}",
                            position=i,
                            word=f"{tokens[i]}+ra"
                        ))
        
        return errors
    
    def _is_noun_appropriate_for_se(self, noun: str) -> bool:
        """Check if a noun is semantically appropriate for se derivation."""
        # Check appropriate categories
        for category, nouns in self.derivational_semantics['se_appropriate_nouns'].items():
            if category != 'logic' and noun in nouns:
                return True
        
        # Check inappropriate categories
        for category, nouns in self.derivational_semantics['se_inappropriate_nouns'].items():
            if category != 'logic' and noun in nouns:
                return False
        
        # Unknown noun - assume appropriate (creative usage allowed)
        return True
    
    def _is_verb_appropriate_for_ra(self, verb: str) -> bool:
        """Check if a verb is semantically appropriate for ra derivation."""
        # Check appropriate categories
        for category, verbs in self.derivational_semantics['ra_appropriate_verbs'].items():
            if category != 'logic' and verb in verbs:
                return True
        
        # Check inappropriate categories
        for category, verbs in self.derivational_semantics['ra_inappropriate_verbs'].items():
            if category != 'logic' and verb in verbs:
                return False
        
        # Unknown verb - assume appropriate (creative usage allowed)
        return True
    
    def _identify_se_usage_pattern(self, noun: str) -> Optional[str]:
        """Identify the usage pattern for se + noun construction."""
        # Check against known usage patterns
        for pattern_name, pattern_info in self.derivational_contexts['se_usage_patterns'].items():
            # This would need more sophisticated pattern matching
            # For now, return pattern if noun is in appropriate categories
            if pattern_name == 'instrumental_usage':
                if noun in self.derivational_semantics['se_appropriate_nouns'].get('tools_and_instruments', set()):
                    return pattern_name
            elif pattern_name == 'metaphorical_usage':
                if noun in self.derivational_semantics['se_appropriate_nouns'].get('abstract_concepts', set()):
                    return pattern_name
            elif pattern_name == 'substance_usage':
                if noun in self.derivational_semantics['se_appropriate_nouns'].get('substances_and_materials', set()):
                    return pattern_name
        
        return None
    
    def _identify_ra_usage_pattern(self, verb: str) -> Optional[str]:
        """Identify the usage pattern for ra + verb construction."""
        # Check against known usage patterns
        for pattern_name, pattern_info in self.derivational_contexts['ra_usage_patterns'].items():
            if pattern_name == 'gerund_usage':
                if verb in self.derivational_semantics['ra_appropriate_verbs'].get('action_verbs', set()):
                    return pattern_name
            elif pattern_name == 'abstract_concept_usage':
                if verb in self.derivational_semantics['ra_appropriate_verbs'].get('mental_verbs', set()):
                    return pattern_name
            elif pattern_name == 'result_usage':
                if verb in self.derivational_semantics['ra_appropriate_verbs'].get('process_verbs', set()):
                    return pattern_name
        
        return None
    
    def _is_in_verb_position(self, particle_position: int, tokens: List[str]) -> bool:
        """Check if a derivational construction is in verb position (SOV)."""
        # In SOV order, verbs should be at or near the end
        # This is a simplified check - would need more sophisticated analysis
        
        # Count content words after this position
        content_words_after = 0
        for i in range(particle_position, len(tokens)):
            word_type = self.identify_word_type(tokens[i])
            if word_type and not word_type.endswith('_particle'):
                content_words_after += 1
        
        # If this is one of the last content word constructions, likely verb position
        return content_words_after <= 2  # Allow for particle + target word
    
    def _is_in_noun_position(self, particle_position: int, tokens: List[str]) -> bool:
        """Check if a derivational construction is in noun position (SOV)."""
        # In SOV order, nouns (subjects/objects) should be before verbs
        # This is a simplified check
        
        # Look for verbs after this position
        verb_found_after = False
        for i in range(particle_position + 2, len(tokens)):  # Skip particle + target
            word_type = self.identify_word_type(tokens[i])
            if word_type == 'verb':
                verb_found_after = True
                break
        
        return verb_found_after  # If verb comes after, this is likely noun position
    
    def validate_emphasis_particle_scope(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate emphasis particle scope and usage patterns."""
        errors = []
        
        # Find all emphasis particles in the sentence
        emphasis_particles = []
        for i, token in enumerate(tokens):
            if token == 'ma':
                emphasis_particles.append((token, i))
        
        if not emphasis_particles:
            return errors  # No emphasis particles to validate
        
        # Validate each emphasis particle
        for particle, position in emphasis_particles:
            # Validate immediate scope and target
            errors.extend(self._validate_emphasis_immediate_scope(position, tokens))
            
            # Validate target appropriateness
            errors.extend(self._validate_emphasis_target(position, tokens))
            
            # Validate particle interactions
            errors.extend(self._validate_emphasis_particle_interactions(position, tokens))
            
            # Validate semantic appropriateness
            errors.extend(self._validate_emphasis_semantics(position, tokens))
        
        # Validate discourse-level emphasis patterns
        errors.extend(self._validate_emphasis_discourse_patterns(emphasis_particles, tokens))
        
        return errors
    
    def _validate_emphasis_immediate_scope(self, position: int, 
                                         tokens: List[str]) -> List[SentenceValidationError]:
        """Validate immediate scope requirements for emphasis particle."""
        errors = []
        
        # Check if ma has a target (not at end of sentence)
        if position >= len(tokens) - 1:
            errors.append(SentenceValidationError(
                SentenceError.EMPHASIS_SCOPE_ERROR,
                f"Emphasis particle 'ma' at end of sentence without target. "
                f"{self.emphasis_scope_rules['immediate_scope']['logic']}",
                position=position,
                word="ma"
            ))
            return errors
        
        # Find the target word (skip intervening particles to find content word)
        target_position = None
        target_word = None
        target_type = None
        
        # Look for the first content word after ma
        for i in range(position + 1, len(tokens)):
            word_type = self.identify_word_type(tokens[i])
            
            # Skip slot 2 particles (they can intervene)
            if word_type == 'slot_2_particle':
                continue
            
            # Found content word or other particle
            if word_type:
                target_position = i
                target_word = tokens[i]
                target_type = word_type
                break
        
        # Validate target existence and type
        if not target_word:
            errors.append(SentenceValidationError(
                SentenceError.EMPHASIS_SCOPE_ERROR,
                f"Emphasis particle 'ma' has no valid target word. "
                f"{self.emphasis_scope_rules['immediate_scope']['logic']}",
                position=position,
                word="ma"
            ))
        elif target_type in self.emphasis_scope_rules['target_restrictions']['prohibited_targets']:
            errors.append(SentenceValidationError(
                SentenceError.EMPHASIS_SCOPE_ERROR,
                f"Emphasis particle 'ma' cannot target {target_type} '{target_word}'. "
                f"{self.emphasis_scope_rules['target_restrictions']['logic']}",
                position=position,
                word=f"ma+{target_word}"
            ))
        
        return errors
    
    def _validate_emphasis_target(self, position: int, 
                                tokens: List[str]) -> List[SentenceValidationError]:
        """Validate emphasis target appropriateness."""
        errors = []
        
        # Find target word (immediate next word)
        if position + 1 >= len(tokens):
            return errors  # Already handled in immediate scope validation
        
        target_word = tokens[position + 1]
        target_type = self.identify_word_type(target_word)
        
        # Check if ma is directly targeting a tense particle
        if target_word == 'ta':
            # Check if 'ta' is followed by a verb
            verb_follows = False
            if position + 2 < len(tokens):
                next_word_type = self.identify_word_type(tokens[position + 2])
                if next_word_type == 'verb':
                    verb_follows = True
            
            # Special case: sentence-initial ma targeting ta is invalid
            if position == 0 and verb_follows:
                errors.append(SentenceValidationError(
                    SentenceError.EMPHASIS_SCOPE_ERROR,
                    f"Sentence-initial emphasis 'ma' cannot target present tense 'ta'. "
                    f"Use 'ma' before the verb instead.",
                    position=position,
                    word=f"ma+{target_word}"
                ))
                return errors
            elif not verb_follows:
                errors.append(SentenceValidationError(
                    SentenceError.EMPHASIS_SCOPE_ERROR,
                    f"Emphasis particle 'ma' targeting 'ta' not followed by verb",
                    position=position,
                    word=f"ma+{target_word}"
                ))
                return errors
        elif target_word in ['li', 'su']:
            # Check if this tense particle is followed by a verb
            verb_follows = False
            if position + 2 < len(tokens):
                next_word_type = self.identify_word_type(tokens[position + 2])
                if next_word_type == 'verb':
                    verb_follows = True
            
            if not verb_follows:
                errors.append(SentenceValidationError(
                    SentenceError.EMPHASIS_SCOPE_ERROR,
                    f"Emphasis on tense marker '{target_word}' not followed by verb",
                    position=position,
                    word=f"ma+{target_word}"
                ))
                return errors
        
        # Check for prohibited targets (direct targeting of particles)
        if target_type in ['slot_0_particle', 'slot_1_particle'] and target_word not in ['he', 'pi', 'ne', 'mo', 'pa', 'sa', 'wo', 'lo', 'no', 'se', 'ra', 'li', 'ta', 'su']:
            errors.append(SentenceValidationError(
                SentenceError.EMPHASIS_SCOPE_ERROR,
                f"Emphasis particle 'ma' cannot target {target_type} '{target_word}'. "
                f"{self.emphasis_scope_rules['target_restrictions']['logic']}",
                position=position,
                word=f"ma+{target_word}"
            ))
            return errors
        
        # Find the actual content word target (skip intervening particles)
        content_target_word = None
        content_target_type = None
        
        for i in range(position + 1, min(position + 4, len(tokens))):
            if i < len(tokens):
                word_type = self.identify_word_type(tokens[i])
                if word_type in self.emphasis_scope_rules['target_restrictions']['allowed_targets']:
                    content_target_word = tokens[i]
                    content_target_type = word_type
                    break
                elif word_type == 'slot_2_particle':
                    continue  # Skip slot 2 particles
                else:
                    break  # Stop at other particles or unknown words
        
        if not content_target_word:
            return errors  # Already handled in immediate scope validation
        
        # Check for special cases
        # 1. Derived words (se+noun, ra+verb) - these are allowed
        if position + 1 < len(tokens) and tokens[position + 1] in ['se', 'ra']:
            # This is emphasizing a derivational construction - allowed
            return errors
        
        # 2. Check for compound constructions (not allowed)
        # This would need more sophisticated analysis of phrase structure
        
        return errors
    
    def _validate_emphasis_particle_interactions(self, position: int, 
                                               tokens: List[str]) -> List[SentenceValidationError]:
        """Validate emphasis particle interactions with other particles."""
        errors = []
        
        # Check what comes immediately after ma
        if position + 1 >= len(tokens):
            return errors  # Already handled in scope validation
        
        next_token = tokens[position + 1]
        next_word_type = self.identify_word_type(next_token)
        
        # Validate specific interaction patterns
        if next_token in ['he', 'pi', 'ne']:
            # ma + animacy pattern
            self._validate_ma_animacy_interaction(position, tokens, errors)
        elif next_token in ['mo', 'pa', 'sa', 'le', 're']:
            # ma + comparison pattern
            self._validate_ma_comparison_interaction(position, tokens, errors)
        elif next_token in ['wo', 'lo', 'no']:
            # ma + number pattern
            self._validate_ma_number_interaction(position, tokens, errors)
        elif next_token in ['se', 'ra']:
            # ma + derivational pattern
            self._validate_ma_derivational_interaction(position, tokens, errors)
        elif next_token in ['li', 'ta', 'su']:
            # ma + tense pattern
            self._validate_ma_tense_interaction(position, tokens, errors)
        elif next_word_type == 'slot_1_particle':
            # ma + other slot 1 particles
            errors.append(SentenceValidationError(
                SentenceError.EMPHASIS_SCOPE_ERROR,
                f"Emphasis particle 'ma' targeting slot 1 particle '{next_token}' may be inappropriate. "
                f"Consider emphasizing the content word instead.",
                position=position,
                word=f"ma+{next_token}"
            ))
        
        return errors
    
    def _validate_ma_animacy_interaction(self, position: int, tokens: List[str], 
                                       errors: List[SentenceValidationError]):
        """Validate ma + animacy particle interaction."""
        if position + 2 >= len(tokens):
            errors.append(SentenceValidationError(
                SentenceError.EMPHASIS_SCOPE_ERROR,
                f"Emphasis on animacy marker incomplete - missing target noun",
                position=position,
                word=f"ma+{tokens[position + 1]}"
            ))
            return
        
        # Check if there's a noun after the animacy marker
        noun_word = tokens[position + 2]
        noun_type = self.identify_word_type(noun_word)
        
        if noun_type != 'noun':
            errors.append(SentenceValidationError(
                SentenceError.EMPHASIS_SCOPE_ERROR,
                f"Emphasis on animacy marker '{tokens[position + 1]}' not followed by noun",
                position=position,
                word=f"ma+{tokens[position + 1]}+{noun_word}"
            ))
    
    def _validate_ma_comparison_interaction(self, position: int, tokens: List[str], 
                                          errors: List[SentenceValidationError]):
        """Validate ma + comparison particle interaction."""
        if position + 2 >= len(tokens):
            errors.append(SentenceValidationError(
                SentenceError.EMPHASIS_SCOPE_ERROR,
                f"Emphasis on comparison marker incomplete - missing target adjective",
                position=position,
                word=f"ma+{tokens[position + 1]}"
            ))
            return
        
        # Check if there's an adjective after the comparison marker
        adj_word = tokens[position + 2]
        adj_type = self.identify_word_type(adj_word)
        
        if adj_type != 'adjective':
            errors.append(SentenceValidationError(
                SentenceError.EMPHASIS_SCOPE_ERROR,
                f"Emphasis on comparison marker '{tokens[position + 1]}' not followed by adjective",
                position=position,
                word=f"ma+{tokens[position + 1]}+{adj_word}"
            ))
    
    def _validate_ma_number_interaction(self, position: int, tokens: List[str], 
                                      errors: List[SentenceValidationError]):
        """Validate ma + number particle interaction."""
        if position + 2 >= len(tokens):
            errors.append(SentenceValidationError(
                SentenceError.EMPHASIS_SCOPE_ERROR,
                f"Emphasis on number marker incomplete - missing target noun",
                position=position,
                word=f"ma+{tokens[position + 1]}"
            ))
            return
        
        # Check if there's a noun after the number marker
        noun_word = tokens[position + 2]
        noun_type = self.identify_word_type(noun_word)
        
        if noun_type != 'noun':
            errors.append(SentenceValidationError(
                SentenceError.EMPHASIS_SCOPE_ERROR,
                f"Emphasis on number marker '{tokens[position + 1]}' not followed by noun",
                position=position,
                word=f"ma+{tokens[position + 1]}+{noun_word}"
            ))
    
    def _validate_ma_derivational_interaction(self, position: int, tokens: List[str], 
                                            errors: List[SentenceValidationError]):
        """Validate ma + derivational particle interaction."""
        if position + 2 >= len(tokens):
            errors.append(SentenceValidationError(
                SentenceError.EMPHASIS_SCOPE_ERROR,
                f"Emphasis on derivational marker incomplete - missing target word",
                position=position,
                word=f"ma+{tokens[position + 1]}"
            ))
            return
        
        # Check if there's appropriate word after derivational marker
        target_word = tokens[position + 2]
        target_type = self.identify_word_type(target_word)
        derivational_particle = tokens[position + 1]
        
        expected_type = 'noun' if derivational_particle == 'se' else 'verb'
        
        if target_type != expected_type:
            errors.append(SentenceValidationError(
                SentenceError.EMPHASIS_SCOPE_ERROR,
                f"Emphasis on derivational marker '{derivational_particle}' not followed by {expected_type}",
                position=position,
                word=f"ma+{derivational_particle}+{target_word}"
            ))
    
    def _validate_ma_tense_interaction(self, position: int, tokens: List[str], 
                                     errors: List[SentenceValidationError]):
        """Validate ma + tense particle interaction."""
        if position + 2 >= len(tokens):
            errors.append(SentenceValidationError(
                SentenceError.EMPHASIS_SCOPE_ERROR,
                f"Emphasis on tense marker incomplete - missing target verb",
                position=position,
                word=f"ma+{tokens[position + 1]}"
            ))
            return
        
        # Check if there's a verb after the tense marker
        verb_word = tokens[position + 2]
        verb_type = self.identify_word_type(verb_word)
        
        if verb_type != 'verb':
            errors.append(SentenceValidationError(
                SentenceError.EMPHASIS_SCOPE_ERROR,
                f"Emphasis on tense marker '{tokens[position + 1]}' not followed by verb",
                position=position,
                word=f"ma+{tokens[position + 1]}+{verb_word}"
            ))
    
    def _validate_emphasis_semantics(self, position: int, 
                                   tokens: List[str]) -> List[SentenceValidationError]:
        """Validate semantic appropriateness of emphasis usage."""
        errors = []
        
        # Find what ma is emphasizing
        target_word = None
        for i in range(position + 1, min(position + 4, len(tokens))):
            if i < len(tokens):
                word_type = self.identify_word_type(tokens[i])
                if word_type in self.emphasis_scope_rules['target_restrictions']['allowed_targets']:
                    target_word = tokens[i]
                    break
                elif word_type == 'slot_2_particle':
                    continue
                else:
                    break
        
        if not target_word:
            return errors  # Already handled elsewhere
        
        # Check for semantic appropriateness based on context
        # This is mostly informational - emphasis is generally flexible
        
        # Check for potential discourse function
        sentence_position = self._get_emphasis_sentence_position(position, tokens)
        if sentence_position:
            # Could add context-specific validation here
            pass
        
        return errors
    
    def _validate_emphasis_discourse_patterns(self, emphasis_particles: List[Tuple[str, int]], 
                                            tokens: List[str]) -> List[SentenceValidationError]:
        """Validate discourse-level emphasis patterns."""
        errors = []
        
        if len(emphasis_particles) < 2:
            return errors  # No discourse patterns to validate
        
        # Check for prohibited patterns
        for i in range(len(emphasis_particles)):
            for j in range(i + 1, len(emphasis_particles)):
                pos1 = emphasis_particles[i][1]
                pos2 = emphasis_particles[j][1]
                
                # Check for double emphasis (ma ma word)
                if pos2 - pos1 == 1:
                    errors.append(SentenceValidationError(
                        SentenceError.EMPHASIS_SCOPE_ERROR,
                        f"Double emphasis detected: 'ma ma' is prohibited. "
                        f"{self.emphasis_discourse_rules['emphasis_scope_conflicts']['logic']}",
                        position=pos1,
                        word="ma+ma"
                    ))
                
                # Check for emphasis on same target
                target1 = self._find_emphasis_target(pos1, tokens)
                target2 = self._find_emphasis_target(pos2, tokens)
                
                if target1 and target2 and target1 == target2:
                    errors.append(SentenceValidationError(
                        SentenceError.EMPHASIS_SCOPE_ERROR,
                        f"Multiple emphasis on same word '{target1}' creates redundancy",
                        position=pos2,
                        word=f"ma+{target1}"
                    ))
        
        return errors
    
    def _get_emphasis_sentence_position(self, position: int, tokens: List[str]) -> str:
        """Determine the position of emphasis within the sentence."""
        if position == 0:
            return 'initial'
        elif position == len(tokens) - 2:  # ma + target at end
            return 'final'
        else:
            return 'medial'
    
    def _find_emphasis_target(self, ma_position: int, tokens: List[str]) -> Optional[str]:
        """Find the target word that ma is emphasizing."""
        for i in range(ma_position + 1, min(ma_position + 4, len(tokens))):
            if i < len(tokens):
                word_type = self.identify_word_type(tokens[i])
                if word_type in self.emphasis_scope_rules['target_restrictions']['allowed_targets']:
                    return tokens[i]
                elif word_type == 'slot_2_particle':
                    continue
                else:
                    break
        return None
    
    def validate_politeness_particle_context(self, tokens: List[str]) -> List[SentenceValidationError]:
        """
        Validate politeness particle 'so' usage in social contexts.
        
        Checks:
        1. Social context appropriateness
        2. Politeness-evidentiality combinations
        3. Register consistency validation
        4. Discourse function validation
        5. Pragmatic appropriateness
        """
        errors = []
        
        # Find all politeness particles
        politeness_particles = [(token, i) for i, token in enumerate(tokens) if token == 'so']
        
        if not politeness_particles:
            return errors
        
        for particle, position in politeness_particles:
            # Validate social context appropriateness
            errors.extend(self._validate_politeness_social_context(position, tokens))
            
            # Validate politeness-evidentiality combinations
            errors.extend(self._validate_politeness_evidentiality_combinations(position, tokens))
            
            # Validate register consistency
            errors.extend(self._validate_politeness_register_consistency(position, tokens))
            
            # Validate discourse function
            errors.extend(self._validate_politeness_discourse_function(position, tokens))
            
            # Validate pragmatic appropriateness
            errors.extend(self._validate_politeness_pragmatic_context(position, tokens))
        
        return errors
    
    def _validate_politeness_social_context(self, position: int, 
                                          tokens: List[str]) -> List[SentenceValidationError]:
        """
        Validate social context appropriateness of 'so' particle.
        
        Social contexts where 'so' is appropriate:
        - Requests and commands (with imperative 'to')
        - Formal statements requiring deference
        - Cross-cultural communication contexts
        - Situations with power/status differences
        - Professional/institutional communication
        
        Inappropriate contexts:
        - Casual statements between equals
        - Emotional outbursts or exclamations
        - Urgent commands requiring immediate action
        - Intimate/personal communication
        """
        errors = []
        
        # Check for appropriate contexts
        appropriate_contexts = self._identify_politeness_appropriate_contexts(position, tokens)
        inappropriate_contexts = self._identify_politeness_inappropriate_contexts(position, tokens)
        
        # Validate context appropriateness
        if inappropriate_contexts:
            for context_type, reason in inappropriate_contexts:
                errors.append(SentenceValidationError(
                    SentenceError.POLITENESS_CONTEXT_MISMATCH,
                    f"Politeness particle 'so' inappropriate in {context_type} context: {reason}",
                    position,
                    'so'
                ))
        
        # Check for missing politeness in formal contexts
        formal_indicators = self._detect_formal_context_indicators(tokens)
        if formal_indicators and position == 0:
            # If formal indicators present but no politeness, suggest consideration
            pass  # This would be a suggestion rather than error
        
        return errors
    
    def _identify_politeness_appropriate_contexts(self, position: int, 
                                                tokens: List[str]) -> List[Tuple[str, str]]:
        """Identify contexts where politeness is appropriate."""
        appropriate = []
        
        # Check for imperative mood (commands/requests)
        if 'to' in tokens:
            appropriate.append(('imperative', 'Commands benefit from politeness marking'))
        
        # Check for obligative mood (should/must)
        if 'ru' in tokens:
            appropriate.append(('obligative', 'Obligations are more polite when marked'))
        
        # Check for questions
        if 'wa' in tokens:
            appropriate.append(('interrogative', 'Questions often benefit from politeness'))
        
        # Check for formal vocabulary patterns
        formal_words = self._detect_formal_vocabulary(tokens)
        if formal_words:
            appropriate.append(('formal_vocabulary', f'Formal terms present: {", ".join(formal_words)}'))
        
        # Check for institutional/professional contexts
        institutional_markers = self._detect_institutional_context(tokens)
        if institutional_markers:
            appropriate.append(('institutional', f'Professional context: {", ".join(institutional_markers)}'))
        
        return appropriate
    
    def _identify_politeness_inappropriate_contexts(self, position: int, 
                                                  tokens: List[str]) -> List[Tuple[str, str]]:
        """Identify contexts where politeness may be inappropriate."""
        inappropriate = []
        
        # Check for emotional/exclamatory contexts
        emotional_markers = self._detect_emotional_context(tokens)
        if emotional_markers:
            inappropriate.append(('emotional', f'Emotional context may not suit formal politeness: {", ".join(emotional_markers)}'))
        
        # Check for urgent/emergency contexts
        urgency_markers = self._detect_urgency_context(tokens)
        if urgency_markers:
            inappropriate.append(('urgent', f'Urgent context may require direct communication: {", ".join(urgency_markers)}'))
        
        # Check for intimate/personal contexts
        intimate_markers = self._detect_intimate_context(tokens)
        if intimate_markers:
            inappropriate.append(('intimate', f'Personal context may not require formal politeness: {", ".join(intimate_markers)}'))
        
        # Check for casual register markers
        casual_markers = self._detect_casual_register(tokens)
        if casual_markers:
            inappropriate.append(('casual', f'Casual register conflicts with formal politeness: {", ".join(casual_markers)}'))
        
        return inappropriate
    
    def _validate_politeness_evidentiality_combinations(self, position: int, 
                                                      tokens: List[str]) -> List[SentenceValidationError]:
        """
        Validate politeness-evidentiality particle combinations.
        
        Appropriate combinations:
        - so + hi (polite direct observation)
        - so + ro (polite inference)
        - so + nu (polite hearsay)
        - so + ti (polite reported speech)
        - so + mu (polite memory)
        - so + pe (polite presumption)
        
        Pragmatic considerations:
        - Direct evidence (hi) + politeness = formal observation
        - Inference (ro) + politeness = deferential conclusion
        - Hearsay (nu) + politeness = respectful reporting
        - Reported (ti) + politeness = formal quotation
        - Memory (mu) + politeness = respectful recollection
        - Presumption (pe) + politeness = tentative suggestion
        """
        errors = []
        
        # Find evidentiality particles in the sentence
        evidentiality_particles = []
        for i, token in enumerate(tokens):
            if token in ['hi', 'ro', 'nu', 'ti', 'mu', 'pe']:
                evidentiality_particles.append((token, i))
        
        if not evidentiality_particles:
            return errors
        
        # Validate each politeness-evidentiality combination
        for ev_particle, ev_position in evidentiality_particles:
            combination_validity = self._validate_so_evidentiality_combination(
                position, ev_position, ev_particle, tokens
            )
            
            if not combination_validity['valid']:
                errors.append(SentenceValidationError(
                    SentenceError.POLITENESS_EVIDENTIALITY_COMBINATION_ERROR,
                    combination_validity['message'],
                    position,
                    f'so + {ev_particle}'
                ))
            
            # Check pragmatic appropriateness
            pragmatic_issues = self._check_politeness_evidentiality_pragmatics(
                ev_particle, tokens
            )
            
            for issue in pragmatic_issues:
                errors.append(SentenceValidationError(
                    SentenceError.POLITENESS_PRAGMATIC_MISMATCH,
                    issue,
                    position,
                    f'so + {ev_particle}'
                ))
        
        return errors
    
    def _validate_so_evidentiality_combination(self, so_pos: int, ev_pos: int, 
                                             ev_particle: str, tokens: List[str]) -> Dict:
        """Validate specific so + evidentiality combinations."""
        
        # Check particle ordering (evidentiality should precede politeness)
        if ev_pos > so_pos:
            return {
                'valid': False,
                'message': f"Evidentiality particle '{ev_particle}' must precede politeness 'so'"
            }
        
        # Validate semantic compatibility
        compatibility_rules = {
            'hi': {  # direct evidence
                'compatible': True,
                'pragmatic_function': 'formal_observation',
                'usage': 'Polite statement of directly observed facts'
            },
            'ro': {  # inference
                'compatible': True,
                'pragmatic_function': 'deferential_conclusion',
                'usage': 'Polite presentation of inferred conclusions'
            },
            'nu': {  # hearsay
                'compatible': True,
                'pragmatic_function': 'respectful_reporting',
                'usage': 'Polite transmission of hearsay information'
            },
            'ti': {  # reported speech
                'compatible': True,
                'pragmatic_function': 'formal_quotation',
                'usage': 'Polite reporting of what someone said'
            },
            'mu': {  # memory
                'compatible': True,
                'pragmatic_function': 'respectful_recollection',
                'usage': 'Polite sharing of remembered information'
            },
            'pe': {  # presumption
                'compatible': True,
                'pragmatic_function': 'tentative_suggestion',
                'usage': 'Polite expression of assumptions or presumptions'
            }
        }
        
        rule = compatibility_rules.get(ev_particle, {'compatible': False})
        
        if not rule['compatible']:
            return {
                'valid': False,
                'message': f"Evidentiality particle '{ev_particle}' not compatible with politeness 'so'"
            }
        
        return {
            'valid': True,
            'pragmatic_function': rule['pragmatic_function'],
            'usage': rule['usage']
        }
    
    def _check_politeness_evidentiality_pragmatics(self, ev_particle: str, 
                                                  tokens: List[str]) -> List[str]:
        """Check pragmatic appropriateness of politeness-evidentiality combinations."""
        issues = []
        
        # Check for pragmatic mismatches
        if ev_particle == 'hi':  # direct evidence
            # Direct evidence + politeness should not be used for obvious facts
            obvious_facts = self._detect_obvious_facts(tokens)
            if obvious_facts:
                issues.append(f"Polite direct evidence inappropriate for obvious facts: {', '.join(obvious_facts)}")
        
        elif ev_particle == 'ro':  # inference
            # Inference + politeness should not be used for certain conclusions
            certain_inferences = self._detect_certain_inferences(tokens)
            if certain_inferences:
                issues.append(f"Polite inference may be unnecessary for certain conclusions: {', '.join(certain_inferences)}")
        
        elif ev_particle == 'nu':  # hearsay
            # Hearsay + politeness should be used carefully with sensitive information
            sensitive_content = self._detect_sensitive_hearsay(tokens)
            if sensitive_content:
                issues.append(f"Polite hearsay requires extra care with sensitive content: {', '.join(sensitive_content)}")
        
        elif ev_particle == 'pe':  # presumption
            # Presumption + politeness should not be used for strong assumptions
            strong_assumptions = self._detect_strong_assumptions(tokens)
            if strong_assumptions:
                issues.append(f"Polite presumption inappropriate for strong assumptions: {', '.join(strong_assumptions)}")
        
        return issues
    
    def _validate_politeness_register_consistency(self, position: int, 
                                                tokens: List[str]) -> List[SentenceValidationError]:
        """
        Validate register consistency with politeness particle.
        
        Register consistency rules:
        1. Formal register should be maintained throughout sentence
        2. Casual markers conflict with politeness
        3. Technical register is compatible with politeness
        4. Emotional register may conflict with politeness
        5. Institutional register requires politeness consistency
        """
        errors = []
        
        # Detect register markers throughout the sentence
        register_analysis = self._analyze_sentence_register(tokens)
        
        # Check for register conflicts
        conflicts = self._detect_register_conflicts(register_analysis)
        
        for conflict in conflicts:
            errors.append(SentenceValidationError(
                SentenceError.POLITENESS_REGISTER_INCONSISTENCY,
                f"Register inconsistency: {conflict['description']}",
                position,
                'so'
            ))
        
        # Check for missing register markers in formal contexts
        formal_requirements = self._check_formal_register_requirements(register_analysis, tokens)
        
        for requirement in formal_requirements:
            errors.append(SentenceValidationError(
                SentenceError.POLITENESS_REGISTER_INCOMPLETE,
                f"Formal register incomplete: {requirement}",
                position,
                'so'
            ))
        
        return errors
    
    def _analyze_sentence_register(self, tokens: List[str]) -> Dict:
        """Analyze the register level of the entire sentence."""
        register_markers = {
            'formal': [],
            'casual': [],
            'technical': [],
            'emotional': [],
            'institutional': []
        }
        
        # Detect formal markers
        formal_indicators = self._detect_formal_vocabulary(tokens)
        register_markers['formal'].extend(formal_indicators)
        
        # Detect casual markers
        casual_indicators = self._detect_casual_register(tokens)
        register_markers['casual'].extend(casual_indicators)
        
        # Detect technical markers
        technical_indicators = self._detect_technical_vocabulary(tokens)
        register_markers['technical'].extend(technical_indicators)
        
        # Detect emotional markers
        emotional_indicators = self._detect_emotional_context(tokens)
        register_markers['emotional'].extend(emotional_indicators)
        
        # Detect institutional markers
        institutional_indicators = self._detect_institutional_context(tokens)
        register_markers['institutional'].extend(institutional_indicators)
        
        # Determine primary register
        primary_register = self._determine_primary_register(register_markers)
        
        return {
            'markers': register_markers,
            'primary': primary_register,
            'conflicts': self._identify_register_conflicts(register_markers)
        }
    
    def _detect_register_conflicts(self, register_analysis: Dict) -> List[Dict]:
        """Detect conflicts between register markers."""
        conflicts = []
        markers = register_analysis['markers']
        
        # Formal vs Casual conflict
        if markers['formal'] and markers['casual']:
            conflicts.append({
                'type': 'formal_casual_conflict',
                'description': f"Formal markers ({', '.join(markers['formal'])}) conflict with casual markers ({', '.join(markers['casual'])})"
            })
        
        # Politeness vs Emotional conflict
        if markers['emotional']:
            conflicts.append({
                'type': 'politeness_emotional_conflict',
                'description': f"Politeness marker conflicts with emotional context ({', '.join(markers['emotional'])})"
            })
        
        # Institutional consistency
        if markers['institutional'] and markers['casual']:
            conflicts.append({
                'type': 'institutional_casual_conflict',
                'description': f"Institutional context ({', '.join(markers['institutional'])}) requires formal register, not casual ({', '.join(markers['casual'])})"
            })
        
        return conflicts
    
    def _validate_politeness_discourse_function(self, position: int, 
                                              tokens: List[str]) -> List[SentenceValidationError]:
        """
        Validate discourse function of politeness particle.
        
        Discourse functions of 'so':
        1. Mitigating face-threatening acts
        2. Showing deference to addressee
        3. Marking formal/institutional register
        4. Softening requests and commands
        5. Expressing cultural sensitivity
        """
        errors = []
        
        # Identify discourse context
        discourse_context = self._identify_discourse_context(tokens)
        
        # Validate politeness function in context
        function_validation = self._validate_politeness_discourse_function_match(
            discourse_context, tokens
        )
        
        if not function_validation['appropriate']:
            errors.append(SentenceValidationError(
                SentenceError.POLITENESS_DISCOURSE_MISMATCH,
                function_validation['message'],
                position,
                'so'
            ))
        
        # Check for missing politeness in contexts that require it
        required_politeness_contexts = self._identify_required_politeness_contexts(tokens)
        
        for context in required_politeness_contexts:
            # Check if politeness is in correct slot 0 position, not absolute position 0
            is_correct_position = self._is_politeness_in_correct_position(position, tokens)
            if not is_correct_position:
                errors.append(SentenceValidationError(
                    SentenceError.POLITENESS_MISSING_REQUIRED,
                    f"Politeness required in {context} context but not in correct slot 0 position",
                    position,
                    'so'
                ))
        
        return errors
    
    def _is_politeness_in_correct_position(self, so_position: int, tokens: List[str]) -> bool:
        """Check if politeness particle is in correct position within slot 0."""
        # Find all slot 0 particles and their positions
        slot_0_positions = []
        for i, token in enumerate(tokens):
            if token in self.slot_0_particles:
                slot_0_positions.append((token, i))
        
        # Check if 'so' is in the correct order relative to other slot 0 particles
        for particle, pos in slot_0_positions:
            if pos < so_position:
                # There's a slot 0 particle before 'so'
                so_order = self._get_particle_order_index('so', self.slot_0_order)
                other_order = self._get_particle_order_index(particle, self.slot_0_order)
                
                # If the other particle should come after 'so', then 'so' is in wrong position
                if other_order > so_order:
                    return False
            elif pos > so_position:
                # There's a slot 0 particle after 'so'
                so_order = self._get_particle_order_index('so', self.slot_0_order)
                other_order = self._get_particle_order_index(particle, self.slot_0_order)
                
                # If the other particle should come before 'so', then 'so' is in wrong position
                if other_order < so_order:
                    return False
        
        return True
    
    def _validate_politeness_pragmatic_context(self, position: int, 
                                             tokens: List[str]) -> List[SentenceValidationError]:
        """
        Validate pragmatic appropriateness of politeness particle.
        
        Pragmatic considerations:
        1. Power relationships (superior to subordinate)
        2. Social distance (strangers, formal relationships)
        3. Cultural context (cross-cultural communication)
        4. Situational formality (professional, institutional)
        5. Face-saving strategies (avoiding imposition)
        """
        errors = []
        
        # Analyze pragmatic context
        pragmatic_context = self._analyze_pragmatic_context(tokens)
        
        # Check pragmatic appropriateness
        appropriateness_issues = self._check_pragmatic_appropriateness(pragmatic_context, tokens)
        
        for issue in appropriateness_issues:
            errors.append(SentenceValidationError(
                SentenceError.POLITENESS_PRAGMATIC_INAPPROPRIATE,
                issue,
                position,
                'so'
            ))
        
        return errors
    
    # Helper methods for context detection
    
    def _detect_formal_vocabulary(self, tokens: List[str]) -> List[str]:
        """Detect formal vocabulary markers."""
        formal_words = []
        
        # Technical/professional terms
        technical_terms = {
            'phuthui', 'whethea', 'luthia',  # document, book, letter
            'weshia', 'siwhea', 'phenu',     # market, house, yard
            'thephoa', 'luthea', 'phethoa'   # person, friend, family
        }
        
        for token in tokens:
            if token in technical_terms:
                formal_words.append(token)
        
        return formal_words
    
    def _detect_casual_register(self, tokens: List[str]) -> List[str]:
        """Detect casual register markers."""
        casual_markers = []
        
        # Casual indicators (contractions, informal particles, etc.)
        # In Phi, casualness might be indicated by omitted particles
        
        # Check for missing formal particles that would normally be present
        if 'ta' not in tokens and any(verb in tokens for verb in ['phuwa', 'shola', 'phemo']):
            casual_markers.append('omitted_present_tense')
        
        return casual_markers
    
    def _detect_emotional_context(self, tokens: List[str]) -> List[str]:
        """Detect emotional context markers."""
        emotional_markers = []
        
        # Emotional vocabulary
        emotional_words = {
            'whomo',  # like/love
            'sheho',  # kill
            'phira',  # want
            'phemo'   # think (when used emotionally)
        }
        
        # Emphasis particles indicating emotional intensity
        if 'ma' in tokens:
            emotional_markers.append('emphasis_particle')
        
        for token in tokens:
            if token in emotional_words:
                emotional_markers.append(token)
        
        return emotional_markers
    
    def _detect_urgency_context(self, tokens: List[str]) -> List[str]:
        """Detect urgency context markers."""
        urgency_markers = []
        
        # Urgent temporal adverbs (these indicate urgency, not just imperative mood)
        urgent_adverbs = {
            'harote',  # immediately
            'hotame',  # instantly
            'sipane'   # now
        }
        
        for token in tokens:
            if token in urgent_adverbs:
                urgency_markers.append(token)
        
        # Note: Imperative mood ('to') alone does not indicate urgency
        # Politeness is specifically designed to soften imperatives
        
        return urgency_markers
    
    def _detect_intimate_context(self, tokens: List[str]) -> List[str]:
        """Detect intimate/personal context markers."""
        intimate_markers = []
        
        # Personal pronouns in intimate contexts
        if 'mia' in tokens and 'thi' in tokens:
            intimate_markers.append('personal_pronouns')
        
        # Family/relationship terms
        family_terms = {
            'luthea',   # friend
            'phethoa',  # family
            'phethui'   # family member
        }
        
        for token in tokens:
            if token in family_terms:
                intimate_markers.append(token)
        
        return intimate_markers
    
    def _detect_institutional_context(self, tokens: List[str]) -> List[str]:
        """Detect institutional/professional context markers."""
        institutional_markers = []
        
        # Professional/institutional vocabulary
        institutional_terms = {
            'weshia',   # market
            'phuthui',  # document
            'whethea'   # book
        }
        
        for token in tokens:
            if token in institutional_terms:
                institutional_markers.append(token)
        
        return institutional_markers
    
    def _detect_technical_vocabulary(self, tokens: List[str]) -> List[str]:
        """Detect technical vocabulary markers."""
        technical_terms = []
        
        # Technical/specialized terms
        tech_words = {
            'phuthui',  # document
            'luthia',   # letter
            'whethea'   # book
        }
        
        for token in tokens:
            if token in tech_words:
                technical_terms.append(token)
        
        return technical_terms
    
    def _detect_obvious_facts(self, tokens: List[str]) -> List[str]:
        """Detect statements of obvious facts."""
        obvious = []
        
        # Weather statements that might be obvious
        if 'phala' in tokens:  # rain
            obvious.append('weather_observation')
        
        return obvious
    
    def _detect_certain_inferences(self, tokens: List[str]) -> List[str]:
        """Detect inferences that are presented as certain."""
        certain = []
        
        # Strong certainty markers would go here
        # In Phi, this might be indicated by specific vocabulary
        
        return certain
    
    def _detect_sensitive_hearsay(self, tokens: List[str]) -> List[str]:
        """Detect potentially sensitive hearsay content."""
        sensitive = []
        
        # Personal information, gossip, etc.
        sensitive_topics = {
            'sheho',   # kill
            'thunu'    # ban
        }
        
        for token in tokens:
            if token in sensitive_topics:
                sensitive.append(token)
        
        return sensitive
    
    def _detect_strong_assumptions(self, tokens: List[str]) -> List[str]:
        """Detect strong assumptions that shouldn't use tentative presumption."""
        strong = []
        
        # Definitive statements that conflict with presumptive evidentiality
        if 'phera' in tokens and 'mipho' in tokens:  # "is blue" - definitive
            strong.append('definitive_statement')
        
        return strong
    
    def _determine_primary_register(self, register_markers: Dict) -> str:
        """Determine the primary register of the sentence."""
        marker_counts = {k: len(v) for k, v in register_markers.items()}
        
        if marker_counts['formal'] > 0:
            return 'formal'
        elif marker_counts['institutional'] > 0:
            return 'institutional'
        elif marker_counts['technical'] > 0:
            return 'technical'
        elif marker_counts['casual'] > 0:
            return 'casual'
        elif marker_counts['emotional'] > 0:
            return 'emotional'
        else:
            return 'neutral'
    
    def _identify_register_conflicts(self, register_markers: Dict) -> List[str]:
        """Identify conflicts between different register markers."""
        conflicts = []
        
        if register_markers['formal'] and register_markers['casual']:
            conflicts.append('formal_casual_conflict')
        
        if register_markers['institutional'] and register_markers['emotional']:
            conflicts.append('institutional_emotional_conflict')
        
        return conflicts
    
    def _check_formal_register_requirements(self, register_analysis: Dict, 
                                          tokens: List[str]) -> List[str]:
        """Check if formal register requirements are met."""
        requirements = []
        
        if register_analysis['primary'] == 'formal':
            # Check for consistent formal marking
            if 'ta' not in tokens and any(verb in tokens for verb in ['phuwa', 'shola', 'phemo']):
                requirements.append('missing_explicit_tense_marking')
        
        return requirements
    
    def _identify_discourse_context(self, tokens: List[str]) -> Dict:
        """Identify the discourse context of the sentence."""
        context = {
            'speech_act': 'statement',
            'formality': 'neutral',
            'social_function': 'informative'
        }
        
        # Identify speech act
        if 'wa' in tokens:
            context['speech_act'] = 'question'
        elif 'to' in tokens:
            context['speech_act'] = 'command'
        elif 'ru' in tokens:
            context['speech_act'] = 'obligation'
        
        # Identify formality level
        formal_markers = self._detect_formal_vocabulary(tokens)
        if formal_markers:
            context['formality'] = 'formal'
        
        casual_markers = self._detect_casual_register(tokens)
        if casual_markers:
            context['formality'] = 'casual'
        
        return context
    
    def _validate_politeness_discourse_function_match(self, discourse_context: Dict, 
                                                    tokens: List[str]) -> Dict:
        """Validate that politeness function matches discourse context."""
        
        # Commands and requests benefit from politeness
        if discourse_context['speech_act'] in ['command', 'obligation']:
            return {'appropriate': True, 'message': 'Politeness appropriate for commands/obligations'}
        
        # Questions can benefit from politeness
        if discourse_context['speech_act'] == 'question':
            return {'appropriate': True, 'message': 'Politeness appropriate for questions'}
        
        # Formal contexts require politeness
        if discourse_context['formality'] == 'formal':
            return {'appropriate': True, 'message': 'Politeness required in formal contexts'}
        
        # Casual contexts may not need politeness
        if discourse_context['formality'] == 'casual':
            return {
                'appropriate': False, 
                'message': 'Politeness may be inappropriate in casual contexts'
            }
        
        return {'appropriate': True, 'message': 'Politeness generally appropriate'}
    
    def _identify_required_politeness_contexts(self, tokens: List[str]) -> List[str]:
        """Identify contexts that require politeness marking."""
        required_contexts = []
        
        # Institutional contexts
        if self._detect_institutional_context(tokens):
            required_contexts.append('institutional')
        
        # Formal requests
        if 'to' in tokens and self._detect_formal_vocabulary(tokens):
            required_contexts.append('formal_request')
        
        return required_contexts
    
    def _analyze_pragmatic_context(self, tokens: List[str]) -> Dict:
        """Analyze the pragmatic context for politeness appropriateness."""
        context = {
            'power_relationship': 'equal',
            'social_distance': 'neutral',
            'cultural_sensitivity': 'standard',
            'face_threat': 'low'
        }
        
        # Analyze for power relationships
        if 'to' in tokens:  # Commands suggest power relationship
            context['power_relationship'] = 'superior_to_subordinate'
        
        # Analyze for social distance
        formal_markers = self._detect_formal_vocabulary(tokens)
        if formal_markers:
            context['social_distance'] = 'distant'
        
        intimate_markers = self._detect_intimate_context(tokens)
        if intimate_markers:
            context['social_distance'] = 'close'
        
        # Analyze for face threat
        if 'to' in tokens or 'ru' in tokens:
            context['face_threat'] = 'high'
        
        return context
    
    def _check_pragmatic_appropriateness(self, pragmatic_context: Dict, 
                                       tokens: List[str]) -> List[str]:
        """Check pragmatic appropriateness of politeness in context."""
        issues = []
        
        # High face threat situations require politeness
        if pragmatic_context['face_threat'] == 'high' and 'so' not in tokens:
            issues.append('High face-threat situation may require politeness marking')
        
        # Close social distance may not need formal politeness
        if pragmatic_context['social_distance'] == 'close':
            issues.append('Close social relationship may not require formal politeness')
        
        # Equal power relationships in casual contexts
        if (pragmatic_context['power_relationship'] == 'equal' and 
            pragmatic_context['social_distance'] == 'close'):
            issues.append('Equal, close relationship may not require politeness marking')
        
        return issues
    
    def _detect_formal_context_indicators(self, tokens: List[str]) -> List[str]:
        """Detect indicators that suggest a formal context."""
        formal_indicators = []
        
        # Combine various formal markers
        formal_indicators.extend(self._detect_formal_vocabulary(tokens))
        formal_indicators.extend(self._detect_institutional_context(tokens))
        formal_indicators.extend(self._detect_technical_vocabulary(tokens))
        
        # Check for explicit formal particles
        if 'te' in tokens:  # explicit verb marking
            formal_indicators.append('explicit_verb_marking')
        
        if 'si' in tokens or 'na' in tokens:  # explicit role marking
            formal_indicators.append('explicit_role_marking')
        
        return formal_indicators
    
    def validate_discourse_particle_sequences(self, tokens: List[str]) -> List[SentenceValidationError]:
        """
        Validate discourse particle sequences for topic chains, contrast scope,
        and topic-contrast interaction patterns.
        
        This method handles:
        1. Topic chains with 'ha' across multiple sentences/clauses
        2. Contrast scope with 'mi' at different discourse levels
        3. Topic-contrast interaction patterns
        4. Discourse coherence and logical flow
        """
        errors = []
        
        # Find all discourse particles and their positions
        discourse_particles = []
        for i, token in enumerate(tokens):
            if token in ['ha', 'mi']:
                discourse_particles.append((token, i))
        
        if not discourse_particles:
            return errors  # No discourse particles to validate
        
        # Validate topic chain coherence
        errors.extend(self._validate_topic_chain_coherence(discourse_particles, tokens))
        
        # Validate contrast scope and logic
        errors.extend(self._validate_contrast_scope_logic(discourse_particles, tokens))
        
        # Validate topic-contrast interactions
        errors.extend(self._validate_topic_contrast_interactions(discourse_particles, tokens))
        
        # Validate discourse sequence patterns
        errors.extend(self._validate_discourse_sequence_patterns(discourse_particles, tokens))
        
        return errors
    
    def _validate_topic_chain_coherence(self, discourse_particles: List[Tuple[str, int]], 
                                       tokens: List[str]) -> List[SentenceValidationError]:
        """Validate topic chain coherence and proper topic management."""
        errors = []
        
        # Find all topic markers
        topic_markers = [(particle, pos) for particle, pos in discourse_particles if particle == 'ha']
        
        if not topic_markers:
            return errors
        
        # Check for topic chain violations
        for i, (particle, position) in enumerate(topic_markers):
            # Validate topic introduction vs. topic shift
            topic_context = self._analyze_topic_context(position, tokens)
            
            if topic_context['type'] == 'invalid_topic_shift':
                errors.append(SentenceValidationError(
                    SentenceError.TOPIC_CHAIN_VIOLATION,
                    f"Invalid topic shift at position {position}: {topic_context['reason']}",
                    position,
                    'ha'
                ))
            
            # Check for topic resumption patterns
            if i > 0:  # Not the first topic marker
                prev_position = topic_markers[i-1][1]
                resumption_validity = self._check_topic_resumption_validity(
                    prev_position, position, tokens
                )
                
                if not resumption_validity['valid']:
                    errors.append(SentenceValidationError(
                        SentenceError.TOPIC_CHAIN_VIOLATION,
                        f"Invalid topic resumption: {resumption_validity['reason']}",
                        position,
                        'ha'
                    ))
            
            # Validate nested topic structures
            nesting_errors = self._validate_topic_nesting(position, tokens)
            errors.extend(nesting_errors)
        
        return errors
    
    def _validate_contrast_scope_logic(self, discourse_particles: List[Tuple[str, int]], 
                                      tokens: List[str]) -> List[SentenceValidationError]:
        """Validate contrast scope and logical relationships."""
        errors = []
        
        # Find all contrast markers
        contrast_markers = [(particle, pos) for particle, pos in discourse_particles if particle == 'mi']
        
        if not contrast_markers:
            return errors
        
        for particle, position in contrast_markers:
            # Analyze contrast scope
            scope_analysis = self._analyze_contrast_scope(position, tokens)
            
            if scope_analysis['scope_error']:
                errors.append(SentenceValidationError(
                    SentenceError.CONTRAST_SCOPE_ERROR,
                    f"Contrast scope error: {scope_analysis['error_message']}",
                    position,
                    'mi'
                ))
            
            # Check logical contrast relationships
            logical_validity = self._check_contrast_logical_validity(position, tokens)
            
            if not logical_validity['valid']:
                errors.append(SentenceValidationError(
                    SentenceError.CONTRAST_SCOPE_ERROR,
                    f"Illogical contrast relationship: {logical_validity['reason']}",
                    position,
                    'mi'
                ))
            
            # Validate contrast with evidentiality
            evidentiality_interaction = self._check_contrast_evidentiality_interaction(position, tokens)
            
            if evidentiality_interaction['conflict']:
                errors.append(SentenceValidationError(
                    SentenceError.DISCOURSE_SEQUENCE_ERROR,
                    f"Contrast-evidentiality conflict: {evidentiality_interaction['message']}",
                    position,
                    'mi'
                ))
        
        return errors
    
    def _validate_topic_contrast_interactions(self, discourse_particles: List[Tuple[str, int]], 
                                            tokens: List[str]) -> List[SentenceValidationError]:
        """Validate complex topic-contrast interaction patterns."""
        errors = []
        
        # Find ha-mi combinations
        ha_positions = [pos for particle, pos in discourse_particles if particle == 'ha']
        mi_positions = [pos for particle, pos in discourse_particles if particle == 'mi']
        
        # Check for ha-mi interaction patterns
        for ha_pos in ha_positions:
            for mi_pos in mi_positions:
                interaction_analysis = self._analyze_ha_mi_interaction(ha_pos, mi_pos, tokens)
                
                if interaction_analysis['error']:
                    errors.append(SentenceValidationError(
                        SentenceError.TOPIC_CONTRAST_INTERACTION_ERROR,
                        interaction_analysis['message'],
                        min(ha_pos, mi_pos),
                        f"ha-mi at {ha_pos}-{mi_pos}"
                    ))
        
        # Validate complex argumentative structures
        argumentative_errors = self._validate_argumentative_discourse_patterns(
            discourse_particles, tokens
        )
        errors.extend(argumentative_errors)
        
        return errors
    
    def _validate_discourse_sequence_patterns(self, discourse_particles: List[Tuple[str, int]], 
                                            tokens: List[str]) -> List[SentenceValidationError]:
        """Validate overall discourse sequence patterns and coherence."""
        errors = []
        
        # Check for discourse repair patterns
        repair_errors = self._validate_discourse_repair_patterns(discourse_particles, tokens)
        errors.extend(repair_errors)
        
        # Validate meta-discourse management
        meta_discourse_errors = self._validate_meta_discourse_patterns(discourse_particles, tokens)
        errors.extend(meta_discourse_errors)
        
        # Check for parallel topic development
        parallel_errors = self._validate_parallel_topic_development(discourse_particles, tokens)
        errors.extend(parallel_errors)
        
        return errors
    
    def _analyze_topic_context(self, position: int, tokens: List[str]) -> Dict:
        """Analyze the context of a topic marker to determine its function."""
        context = {
            'type': 'topic_introduction',
            'reason': '',
            'valid': True
        }
        
        # Check what follows the topic marker
        if position + 1 < len(tokens):
            following_word = tokens[position + 1]
            
            # Check for proper topic noun or noun phrase
            # Allow some particles like 'ma' (emphasis) or 'so' (politeness) after 'ha'
            allowed_after_ha = {'ma', 'so'}
            
            if following_word in self.all_particles and following_word not in allowed_after_ha:
                # Only flag as error if it's a problematic particle
                problematic_particles = {'mi', 'wa', 'li', 'ta', 'su'}
                if following_word in problematic_particles:
                    context['type'] = 'invalid_topic_shift'
                    context['reason'] = 'Topic marker followed by particle instead of topic noun'
                    context['valid'] = False
        
        # Check for topic shift vs. topic introduction
        # Look for previous topic markers in the discourse
        prev_ha_positions = [i for i, token in enumerate(tokens[:position]) if token == 'ha']
        
        if prev_ha_positions:
            # This is a topic shift, validate appropriateness
            last_ha_pos = prev_ha_positions[-1]
            distance = position - last_ha_pos
            
            # Only flag as error if extremely close (adjacent or one word apart)
            if distance <= 2:  # Very close for meaningful topic shift
                context['type'] = 'invalid_topic_shift'
                context['reason'] = 'Topic shift too close to previous topic marker'
                context['valid'] = False
        
        return context
    
    def _check_topic_resumption_validity(self, prev_position: int, current_position: int, 
                                       tokens: List[str]) -> Dict:
        """Check if topic resumption is valid."""
        validity = {
            'valid': True,
            'reason': ''
        }
        
        # Check for intervening contrast markers
        intervening_mi = any(tokens[i] == 'mi' for i in range(prev_position + 1, current_position))
        
        if intervening_mi:
            # Topic resumption after contrast is valid
            validity['valid'] = True
            validity['reason'] = 'Valid topic resumption after contrast'
        else:
            # Check distance and content
            distance = current_position - prev_position
            if distance < 5:  # Arbitrary threshold for meaningful topic development
                validity['valid'] = False
                validity['reason'] = 'Topic resumption too soon without sufficient development'
        
        return validity
    
    def _validate_topic_nesting(self, position: int, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate nested topic structures."""
        errors = []
        
        # Check for proper nesting depth (avoid too deep nesting)
        ha_count_before = tokens[:position].count('ha')
        
        if ha_count_before > 3:  # Arbitrary limit for readability
            errors.append(SentenceValidationError(
                SentenceError.TOPIC_CHAIN_VIOLATION,
                f"Topic nesting too deep (level {ha_count_before + 1}), may reduce clarity",
                position,
                'ha'
            ))
        
        return errors
    
    def _analyze_contrast_scope(self, position: int, tokens: List[str]) -> Dict:
        """Analyze the scope and appropriateness of a contrast marker."""
        analysis = {
            'scope_error': False,
            'error_message': '',
            'scope_type': 'sentence_level'
        }
        
        # Check what the contrast is operating on
        if position == 0:
            analysis['scope_error'] = True
            analysis['error_message'] = 'Contrast marker at sentence beginning with no prior context'
            return analysis
        
        # Analyze the content being contrasted
        preceding_content = tokens[:position]
        following_content = tokens[position + 1:]
        
        # Check for meaningful contrast - be more permissive
        if not preceding_content:
            analysis['scope_error'] = True
            analysis['error_message'] = 'Contrast marker without preceding content'
        elif len(following_content) == 0:
            analysis['scope_error'] = True
            analysis['error_message'] = 'Contrast marker without following content'
        
        # Don't require logical contrast elements for now - too strict
        # The presence of 'mi' itself indicates the speaker intends contrast
        
        return analysis
    
    def _check_contrast_logical_validity(self, position: int, tokens: List[str]) -> Dict:
        """Check if the contrast relationship is logically valid."""
        validity = {
            'valid': True,
            'reason': ''
        }
        
        # Analyze semantic content for logical opposition
        preceding_tokens = tokens[:position]
        following_tokens = tokens[position + 1:]
        
        # Be more permissive - only flag obvious logical errors
        # The speaker's use of 'mi' indicates they perceive a contrast
        
        # Only check for very basic content requirements
        if len(preceding_tokens) == 0:
            validity['valid'] = False
            validity['reason'] = 'No content before contrast marker'
        elif len(following_tokens) == 0:
            validity['valid'] = False
            validity['reason'] = 'No content after contrast marker'
        
        # Don't require semantic opposition detection - too restrictive
        # Real discourse often has subtle contrasts not captured by simple word pairs
        
        return validity
    
    def _check_contrast_evidentiality_interaction(self, position: int, tokens: List[str]) -> Dict:
        """Check for conflicts between contrast and evidentiality markers."""
        interaction = {
            'conflict': False,
            'message': ''
        }
        
        # Find evidentiality particles near the contrast
        evidentiality_particles = ['hi', 'ro', 'nu', 'ti', 'mu', 'pe']
        
        # Check for evidentiality before contrast
        for i in range(max(0, position - 3), position):
            if tokens[i] in evidentiality_particles:
                # Check if the evidentiality type conflicts with contrast logic
                ev_particle = tokens[i]
                conflict_check = self._check_evidentiality_contrast_compatibility(ev_particle, tokens)
                
                if conflict_check['conflict']:
                    interaction['conflict'] = True
                    interaction['message'] = conflict_check['message']
        
        return interaction
    
    def _analyze_ha_mi_interaction(self, ha_pos: int, mi_pos: int, tokens: List[str]) -> Dict:
        """Analyze the interaction between ha and mi particles."""
        analysis = {
            'error': False,
            'message': '',
            'pattern_type': 'unknown'
        }
        
        if ha_pos < mi_pos:
            # ha before mi: topic then contrast
            distance = mi_pos - ha_pos
            
            if distance == 1:  # Adjacent: "ha mi"
                analysis['pattern_type'] = 'topic_contrast_combination'
                # This is valid: "speaking of X, however..."
                analysis['error'] = False
            elif distance < 5:
                analysis['pattern_type'] = 'topic_then_contrast'
                # Check if there's sufficient content between them
                intervening_content = tokens[ha_pos + 1:mi_pos]
                if len(intervening_content) < 2:
                    analysis['error'] = True
                    analysis['message'] = 'Insufficient content between topic and contrast markers'
            else:
                analysis['pattern_type'] = 'distant_topic_contrast'
                # Distant topic and contrast - generally acceptable
        
        elif mi_pos < ha_pos:
            # mi before ha: contrast then topic
            analysis['pattern_type'] = 'contrast_then_topic'
            # This can be valid in discourse repair or topic shift after contrast
            
            distance = ha_pos - mi_pos
            if distance < 3:
                analysis['error'] = True
                analysis['message'] = 'Topic marker too close after contrast without development'
        
        return analysis
    
    def _validate_argumentative_discourse_patterns(self, discourse_particles: List[Tuple[str, int]], 
                                                 tokens: List[str]) -> List[SentenceValidationError]:
        """Validate complex argumentative discourse structures."""
        errors = []
        
        # Check for proper argumentative flow
        ha_positions = [pos for particle, pos in discourse_particles if particle == 'ha']
        mi_positions = [pos for particle, pos in discourse_particles if particle == 'mi']
        
        # Validate argumentative sequences
        if len(ha_positions) > 1 and len(mi_positions) > 0:
            # Complex argumentative structure detected
            structure_validity = self._check_argumentative_structure_validity(
                ha_positions, mi_positions, tokens
            )
            
            if not structure_validity['valid']:
                errors.append(SentenceValidationError(
                    SentenceError.DISCOURSE_SEQUENCE_ERROR,
                    f"Invalid argumentative structure: {structure_validity['reason']}",
                    structure_validity['position'],
                    'discourse_structure'
                ))
        
        return errors
    
    def _validate_discourse_repair_patterns(self, discourse_particles: List[Tuple[str, int]], 
                                          tokens: List[str]) -> List[SentenceValidationError]:
        """Validate discourse repair and clarification patterns."""
        errors = []
        
        # Look for repair patterns: "ha mi" (topic clarification)
        for i in range(len(discourse_particles) - 1):
            current_particle, current_pos = discourse_particles[i]
            next_particle, next_pos = discourse_particles[i + 1]
            
            if current_particle == 'ha' and next_particle == 'mi' and next_pos - current_pos <= 2:
                # Potential repair pattern
                repair_validity = self._check_discourse_repair_validity(current_pos, next_pos, tokens)
                
                if not repair_validity['valid']:
                    errors.append(SentenceValidationError(
                        SentenceError.DISCOURSE_SEQUENCE_ERROR,
                        f"Invalid discourse repair pattern: {repair_validity['reason']}",
                        current_pos,
                        'ha-mi'
                    ))
        
        return errors
    
    def _validate_meta_discourse_patterns(self, discourse_particles: List[Tuple[str, int]], 
                                        tokens: List[str]) -> List[SentenceValidationError]:
        """Validate meta-discourse management patterns."""
        errors = []
        
        # Check for meta-discourse vocabulary
        meta_discourse_words = {'thiwhea', 'lawhui', 'phola'}  # discussion, time, action
        
        has_meta_discourse = any(word in tokens for word in meta_discourse_words)
        
        if has_meta_discourse and len(discourse_particles) < 2:
            errors.append(SentenceValidationError(
                SentenceError.DISCOURSE_SEQUENCE_ERROR,
                "Meta-discourse content should use explicit discourse structuring",
                0,
                'meta_discourse'
            ))
        
        return errors
    
    def _validate_parallel_topic_development(self, discourse_particles: List[Tuple[str, int]], 
                                           tokens: List[str]) -> List[SentenceValidationError]:
        """Validate parallel topic development patterns."""
        errors = []
        
        # Find multiple topic markers for parallel development
        ha_positions = [pos for particle, pos in discourse_particles if particle == 'ha']
        
        if len(ha_positions) >= 3:  # Potential parallel structure
            parallel_validity = self._check_parallel_topic_validity(ha_positions, tokens)
            
            if not parallel_validity['valid']:
                errors.append(SentenceValidationError(
                    SentenceError.TOPIC_CHAIN_VIOLATION,
                    f"Invalid parallel topic structure: {parallel_validity['reason']}",
                    parallel_validity['position'],
                    'parallel_topics'
                ))
        
        return errors
    
    # Helper methods for discourse analysis
    
    def _check_contrastive_elements(self, preceding: List[str], following: List[str]) -> Dict:
        """Check for contrastive elements in the content."""
        validity = {'valid': True, 'reason': ''}
        
        # Simple heuristic: look for opposing concepts
        # This could be expanded with semantic analysis
        
        if not preceding or not following:
            validity['valid'] = False
            validity['reason'] = 'Missing content for contrast'
        
        return validity
    
    def _detect_semantic_opposition(self, preceding: List[str], following: List[str]) -> bool:
        """Detect semantic opposition between content segments."""
        # Simple implementation - could be expanded
        
        # Look for explicit opposition markers
        opposition_pairs = {
            ('teshe', 'huphea'),  # good vs. problem
            ('tophe', 'pisha'),   # large vs. small
            ('waphe', 'thepo'),   # warm vs. cold
        }
        
        for word1 in preceding:
            for word2 in following:
                if (word1, word2) in opposition_pairs or (word2, word1) in opposition_pairs:
                    return True
        
        return False
    
    def _check_evidentiality_contrast_compatibility(self, ev_particle: str, tokens: List[str]) -> Dict:
        """Check compatibility between evidentiality and contrast."""
        compatibility = {'conflict': False, 'message': ''}
        
        # Some evidentiality types may conflict with certain contrasts
        if ev_particle == 'hi' and 'me' in tokens:  # direct evidence + negation
            compatibility['conflict'] = True
            compatibility['message'] = 'Direct evidence conflicts with negated contrast'
        
        return compatibility
    
    def _check_argumentative_structure_validity(self, ha_positions: List[int], 
                                              mi_positions: List[int], tokens: List[str]) -> Dict:
        """Check validity of complex argumentative structures."""
        validity = {'valid': True, 'reason': '', 'position': 0}
        
        # Check for proper argumentative flow
        all_positions = sorted(ha_positions + mi_positions)
        
        # Simple check: ensure reasonable spacing
        for i in range(len(all_positions) - 1):
            distance = all_positions[i + 1] - all_positions[i]
            if distance < 3:  # Too close
                validity['valid'] = False
                validity['reason'] = 'Discourse markers too close together'
                validity['position'] = all_positions[i]
                break
        
        return validity
    
    def _check_discourse_repair_validity(self, ha_pos: int, mi_pos: int, tokens: List[str]) -> Dict:
        """Check validity of discourse repair patterns."""
        validity = {'valid': True, 'reason': ''}
        
        # Check if there's appropriate content for repair
        if mi_pos - ha_pos == 1:  # Adjacent ha mi
            # This should be followed by clarification
            if mi_pos + 1 >= len(tokens):
                validity['valid'] = False
                validity['reason'] = 'Discourse repair pattern incomplete'
        
        return validity
    
    def _check_parallel_topic_validity(self, ha_positions: List[int], tokens: List[str]) -> Dict:
        """Check validity of parallel topic structures."""
        validity = {'valid': True, 'reason': '', 'position': 0}
        
        # Check for consistent spacing and structure
        if len(ha_positions) >= 3:
            # Look for regular patterns
            distances = [ha_positions[i + 1] - ha_positions[i] for i in range(len(ha_positions) - 1)]
            
            # Check if distances are reasonably consistent (parallel structure)
            avg_distance = sum(distances) / len(distances)
            for i, distance in enumerate(distances):
                if abs(distance - avg_distance) > avg_distance * 0.5:  # 50% variance threshold
                    validity['valid'] = False
                    validity['reason'] = 'Inconsistent parallel topic structure'
                    validity['position'] = ha_positions[i]
                    break
        
        return validity


def main():
    """Command-line interface for sentence validation."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Validate Phi sentences")
    parser.add_argument("sentence", nargs="?", help="Sentence to validate")
    parser.add_argument("--interactive", "-i", action="store_true", 
                       help="Interactive mode")
    parser.add_argument("--file", "-f", help="File with sentences to validate")
    
    args = parser.parse_args()
    
    validator = PhiSentenceValidator()
    
    if args.interactive:
        print("Phi Sentence Validator - Interactive Mode")
        print("Enter sentences to validate (empty line to quit):")
        print()
        
        while True:
            try:
                sentence = input("phi> ").strip()
                if not sentence:
                    break
                
                result = validator.validate_sentence(sentence)
                print(validator.generate_sentence_report(result))
                print("-" * 50)
                
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
    
    elif args.file:
        try:
            with open(args.file, 'r') as f:
                for line_num, line in enumerate(f, 1):
                    sentence = line.strip()
                    if not sentence or sentence.startswith('#'):
                        continue
                    
                    print(f"Line {line_num}: {sentence}")
                    result = validator.validate_sentence(sentence)
                    print(validator.generate_sentence_report(result))
                    print("=" * 60)
        
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found")
            return 1
    
    elif args.sentence:
        result = validator.validate_sentence(args.sentence)
        print(validator.generate_sentence_report(result))
    
    else:
        parser.print_help()
    
    return 0


if __name__ == "__main__":
    exit(main()) 