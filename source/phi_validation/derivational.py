#!/usr/bin/env python3
"""
Derivational Validation Module

Validates derivational particle usage including se and ra constructions,
semantic appropriateness, phonotactic consistency, and contextual usage.
"""

from typing import List, Dict, Tuple, Optional
from .errors import SentenceError, SentenceValidationError


class DerivationalValidator:
    """Validates derivational particles and their constructions."""
    
    def __init__(self):
        """Initialize derivational validation rules."""
        # Lexicon validator for word type identification
        self.lexicon_validator = None  # Will be set by core
        
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
    
    def set_lexicon_validator(self, lexicon_validator):
        """Set the lexicon validator for word type identification."""
        self.lexicon_validator = lexicon_validator
    
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
            word_type = self.lexicon_validator.identify_word_type(token) if self.lexicon_validator else None
            
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
                word_type = self.lexicon_validator.identify_word_type(tokens[i]) if self.lexicon_validator else None
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
                word_type = self.lexicon_validator.identify_word_type(tokens[i]) if self.lexicon_validator else None
                expected_type = self.derivational_particles[particle]['source_pos']
                if word_type == expected_type:
                    target_word = tokens[i]
                    target_position = i
                    break
        
        if not target_word:
            return errors  # No target to validate
        
        # Validate that the source word follows correct phonotactics
        # For derivational validation, we check phonotactics without meaning
        if hasattr(self.lexicon_validator, 'word_validator'):
            phonotactic_errors = self.lexicon_validator.word_validator.validate_phonotactics(target_word, expected_type)
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
                word_type = self.lexicon_validator.identify_word_type(tokens[i]) if self.lexicon_validator else None
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
            word_type = self.lexicon_validator.identify_word_type(tokens[i]) if self.lexicon_validator else None
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
            word_type = self.lexicon_validator.identify_word_type(tokens[i]) if self.lexicon_validator else None
            if word_type == 'verb':
                verb_found_after = True
                break
        
        return verb_found_after  # If verb comes after, this is likely noun position 