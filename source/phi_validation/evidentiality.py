#!/usr/bin/env python3
"""
Evidentiality Validation Module

Validates evidentiality particle usage, combinations, nesting patterns,
and tense interactions in Phi sentences.
"""

from typing import List, Dict, Tuple, Optional
from .errors import SentenceError, SentenceValidationError


class EvidentialityValidator:
    """Validates evidentiality particles and their interactions."""
    
    def __init__(self):
        """Initialize evidentiality validation rules."""
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
                ('hi', 'ro'),  # direct evidence can be followed by inference
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
        
        # Tense particles for validation
        self.tense_particles = {'li', 'ta', 'su'}
    
    def validate_evidentiality(self, tokens: List[str]) -> List[SentenceValidationError]:
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