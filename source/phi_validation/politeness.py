#!/usr/bin/env python3
"""
Politeness Validation Module

Validates politeness particle (so) context and usage in Phi sentences.
Handles social context appropriateness, register consistency, and pragmatic validation.
"""

from typing import List, Dict, Tuple, Optional
from .errors import SentenceError, SentenceValidationError


class PolitenessValidator:
    """Validates politeness particle usage and context."""
    
    def __init__(self):
        """Initialize politeness validation rules."""
        # Lexicon validator for word type identification
        self.lexicon_validator = None  # Will be set by core
        
        # Slot 0 particles for position validation
        self.slot_0_particles = {
            'wa', 'ho', 'tu', 'hu',  # sentence type
            'hi', 'ro', 'nu', 'ti', 'mu', 'pe',  # evidentiality
            'ha', 'mi', 'lu',  # discourse and relative
            'so'  # politeness
        }
        
        # Slot 0 ordering for position validation
        self.slot_0_order = [
            ['wa', 'ho', 'tu', 'hu'],  # sentence type
            ['hi', 'ro', 'nu', 'ti', 'mu', 'pe'],  # evidentiality
            ['ha', 'mi', 'lu'],  # discourse and relative
            ['so']  # politeness
        ]
    
    def set_lexicon_validator(self, lexicon_validator):
        """Set the lexicon validator for word type identification."""
        self.lexicon_validator = lexicon_validator
    
    def validate_politeness_context(self, tokens: List[str]) -> List[SentenceValidationError]:
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
    
    def _get_particle_order_index(self, particle: str, order_groups: List[List[str]]) -> int:
        """Get the ordering index of a particle within its slot."""
        for i, group in enumerate(order_groups):
            if particle in group:
                return i
        return 999  # Unknown particle gets lowest priority
    
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
        
        # Only flag emphasis as emotional if combined with emotional vocabulary
        # Emphasis alone is not necessarily emotional - it can be contrastive or formal
        if 'ma' in tokens:
            # Check if emphasis is used with emotional words
            has_emotional_words = any(word in emotional_words for word in tokens)
            if has_emotional_words:
                emotional_markers.append('emphasis_with_emotional_content')
            # Otherwise, emphasis is considered neutral/formal and compatible with politeness
        
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