#!/usr/bin/env python3
"""
Modality Validation Module

Validates modal logic including obligative, conditional, and desiderative
constructions in Phi sentences.
"""

from typing import List, Dict, Tuple, Optional
from .errors import SentenceError, SentenceValidationError


class ModalityValidator:
    """Validates modal logic and constructions."""
    
    def __init__(self):
        """Initialize modal validation rules."""
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
        
        # Lexicon validator for word type identification
        self.lexicon_validator = None  # Will be set by core
    
    def set_lexicon_validator(self, lexicon_validator):
        """Set the lexicon validator for word type identification."""
        self.lexicon_validator = lexicon_validator
    
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
                    next_word_type = self._identify_word_type(next_token)
                    
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
                    elif self._identify_word_type(tokens[j]) == 'verb':
                        # Reached verb without explicit tense (default present)
                        protasis_tense = 'ta'
                        break
                
                # Find tense in apodosis (main clause) - before wetu
                for j in range(i - 1, -1, -1):
                    if tokens[j] in self.conditional_rules['apodosis_tenses'] + ['li', 'ta']:
                        apodosis_tense = tokens[j]
                        break
                    elif self._identify_word_type(tokens[j]) == 'verb':
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
                        elif te_found and self._identify_word_type(tokens[j]) == 'verb':
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
    
    def _identify_word_type(self, word: str) -> Optional[str]:
        """Identify the part of speech of a word."""
        if self.lexicon_validator:
            return self.lexicon_validator.identify_word_type(word)
        return None 