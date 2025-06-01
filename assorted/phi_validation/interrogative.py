#!/usr/bin/env python3
"""
Interrogative Validation Module

Validates question structures and interrogative constructions in Phi sentences.
Handles yes/no questions, wh-questions, rhetorical questions, and tense appropriateness.
"""

from typing import List, Dict, Tuple, Optional
from .errors import SentenceError, SentenceValidationError


class InterrogativeValidator:
    """Validates interrogative constructions and question structures."""
    
    def __init__(self):
        """Initialize interrogative validation rules."""
        # Lexicon validator for word type identification
        self.lexicon_validator = None  # Will be set by core
        
        # Tense particles for tense detection
        self.tense_particles = {'li', 'ta', 'su'}  # past, present, future
        
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
                        'preferred_tenses': ['li', 'ta', 'su'],  # manner questions work with all tenses
                        'logic': 'Manner questions can ask about past methods, current processes, or future plans'
                    },
                    'wamine': {  # why
                        'preferred_tenses': ['li', 'ta', 'su'],  # reason questions work with all tenses
                        'logic': 'Reason questions can ask about past events, current states, or future intentions'
                    },
                    'timane': {  # when
                        'preferred_tenses': ['li', 'su', 'ta'],  # past events, future plans, or habitual
                        'logic': 'Time questions can ask about past events, future plans, or habitual occurrences'
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
    
    def set_lexicon_validator(self, lexicon_validator):
        """Set the lexicon validator for word type identification."""
        self.lexicon_validator = lexicon_validator
    
    def validate_interrogatives(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate interrogative constructions and question-answer tense matching."""
        errors = []
        
        # 1. Validate duplicate interrogative words
        errors.extend(self._validate_duplicate_interrogatives(tokens))
        
        # 2. Validate yes/no questions
        errors.extend(self._validate_yes_no_questions(tokens))
        
        # 3. Validate wh-questions
        errors.extend(self._validate_wh_questions(tokens))
        
        # 4. Validate rhetorical questions
        errors.extend(self._validate_rhetorical_questions(tokens))
        
        # 5. Validate question context appropriateness
        errors.extend(self._validate_question_context(tokens))
        
        return errors
    
    def _validate_duplicate_interrogatives(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate that interrogative words are not duplicated."""
        errors = []
        
        # Track interrogative words we've seen
        seen_interrogatives = {}
        wh_markers = self.interrogative_rules['wh_questions']['markers']
        
        for i, token in enumerate(tokens):
            if token in wh_markers:
                if token in seen_interrogatives:
                    # Found duplicate interrogative word
                    prev_position = seen_interrogatives[token]
                    errors.append(SentenceValidationError(
                        SentenceError.QUESTION_CONTEXT_MISMATCH,
                        f"Duplicate interrogative word '{token}' found at positions {prev_position} and {i}. "
                        f"Interrogative words should not be repeated within the same question.",
                        position=i,
                        word=token
                    ))
                else:
                    seen_interrogatives[token] = i
        
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
    
    def _identify_word_type(self, word: str) -> Optional[str]:
        """Identify the part of speech of a word using the lexicon validator."""
        if self.lexicon_validator:
            return self.lexicon_validator.identify_word_type(word)
        return None 