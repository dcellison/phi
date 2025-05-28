#!/usr/bin/env python3
"""
Emphasis Validation Module

Validates emphasis particle (ma) scope and usage in Phi sentences.
Handles contrastive focus, target identification, and discourse patterns.
"""

from typing import List, Optional, Tuple
from .errors import SentenceError, SentenceValidationError


class EmphasisValidator:
    """Validates emphasis particle usage and scope."""
    
    def __init__(self):
        """Initialize emphasis validation rules."""
        # Lexicon validator for word type identification
        self.lexicon_validator = None  # Will be set by core
        
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
    
    def set_lexicon_validator(self, lexicon_validator):
        """Set the lexicon validator for word type identification."""
        self.lexicon_validator = lexicon_validator
    
    def validate_emphasis_scope(self, tokens: List[str]) -> List[SentenceValidationError]:
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
        
        # Get the immediate next word
        immediate_target = tokens[position + 1]
        immediate_target_type = self._identify_word_type(immediate_target)
        
        # Special handling for animacy particles - they're valid when followed by nouns
        if immediate_target in ['he', 'pi', 'ne']:
            if position + 2 < len(tokens):
                following_word = tokens[position + 2]
                following_type = self._identify_word_type(following_word)
                if following_type == 'noun':
                    # Valid: ma + animacy + noun (emphasizes the noun phrase)
                    return errors
                else:
                    errors.append(SentenceValidationError(
                        SentenceError.EMPHASIS_SCOPE_ERROR,
                        f"Emphasis on animacy marker '{immediate_target}' not followed by noun",
                        position=position,
                        word=f"ma+{immediate_target}"
                    ))
                    return errors
            else:
                errors.append(SentenceValidationError(
                    SentenceError.EMPHASIS_SCOPE_ERROR,
                    f"Emphasis on animacy marker '{immediate_target}' incomplete - missing target noun",
                    position=position,
                    word=f"ma+{immediate_target}"
                ))
                return errors
        
        # Special handling for POS markers (na, si) - they're valid when followed by noun phrases
        if immediate_target in ['na', 'si']:
            if position + 2 < len(tokens):
                # Check if followed by animacy + noun or just noun
                following_word = tokens[position + 2]
                following_type = self._identify_word_type(following_word)
                if following_type == 'noun':
                    # Valid: ma + na/si + noun (emphasizes the noun phrase)
                    return errors
                elif following_word in ['he', 'pi', 'ne'] and position + 3 < len(tokens):
                    # Check for ma + na/si + animacy + noun pattern
                    noun_word = tokens[position + 3]
                    noun_type = self._identify_word_type(noun_word)
                    if noun_type == 'noun':
                        # Valid: ma + na/si + animacy + noun (emphasizes the noun phrase)
                        return errors
                    else:
                        errors.append(SentenceValidationError(
                            SentenceError.EMPHASIS_SCOPE_ERROR,
                            f"Emphasis on POS marker '{immediate_target}' with animacy marker not followed by noun",
                            position=position,
                            word=f"ma+{immediate_target}"
                        ))
                        return errors
                else:
                    errors.append(SentenceValidationError(
                        SentenceError.EMPHASIS_SCOPE_ERROR,
                        f"Emphasis on POS marker '{immediate_target}' not followed by noun phrase",
                        position=position,
                        word=f"ma+{immediate_target}"
                    ))
                    return errors
            else:
                errors.append(SentenceValidationError(
                    SentenceError.EMPHASIS_SCOPE_ERROR,
                    f"Emphasis on POS marker '{immediate_target}' incomplete - missing target noun phrase",
                    position=position,
                    word=f"ma+{immediate_target}"
                ))
                return errors
        
        # Special handling for derivational particles
        if immediate_target in ['se', 'ra']:
            if position + 2 < len(tokens):
                following_word = tokens[position + 2]
                following_type = self._identify_word_type(following_word)
                expected_type = 'noun' if immediate_target == 'se' else 'verb'
                if following_type == expected_type:
                    # Valid derivational construction
                    return errors
                else:
                    errors.append(SentenceValidationError(
                        SentenceError.EMPHASIS_SCOPE_ERROR,
                        f"Emphasis on derivational particle '{immediate_target}' not followed by {expected_type}",
                        position=position,
                        word=f"ma+{immediate_target}"
                    ))
                    return errors
        
        # Special handling for tense particles - allow for temporal emphasis
        if immediate_target in ['ta', 'li', 'su']:
            # Valid: ma + tense for temporal contrast (NOW vs THEN vs WILL)
            return errors
        
        # Find the target word (skip intervening particles to find content word)
        target_position = None
        target_word = None
        target_type = None
        
        # Look for the first content word after ma
        for i in range(position + 1, len(tokens)):
            word_type = self._identify_word_type(tokens[i])
            
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
        target_type = self._identify_word_type(target_word)
        
        # Check if ma is directly targeting a tense particle
        if target_word == 'ta':
            # Allow emphasis on present tense for temporal contrast
            # This is valid for contrastive focus: "NOW they live" vs "THEN they lived"
            return errors
        elif target_word in ['li', 'su']:
            # Allow emphasis on past/future tense for temporal contrast
            return errors
        
        # Special handling for animacy particles - they're valid targets when followed by nouns
        if target_word in ['he', 'pi', 'ne']:
            # Check if animacy particle is followed by a noun
            if position + 2 < len(tokens):
                following_word = tokens[position + 2]
                following_type = self._identify_word_type(following_word)
                if following_type == 'noun':
                    # Valid: ma + animacy + noun (emphasizes the noun phrase)
                    return errors
                else:
                    errors.append(SentenceValidationError(
                        SentenceError.EMPHASIS_SCOPE_ERROR,
                        f"Emphasis on animacy marker '{target_word}' not followed by noun",
                        position=position,
                        word=f"ma+{target_word}"
                    ))
                    return errors
            else:
                errors.append(SentenceValidationError(
                    SentenceError.EMPHASIS_SCOPE_ERROR,
                    f"Emphasis on animacy marker '{target_word}' incomplete - missing target noun",
                    position=position,
                    word=f"ma+{target_word}"
                ))
                return errors
        
        # Special handling for POS markers (na, si) - they're valid targets when followed by noun phrases
        if target_word in ['na', 'si']:
            # Check if POS marker is followed by a noun phrase
            if position + 2 < len(tokens):
                following_word = tokens[position + 2]
                following_type = self._identify_word_type(following_word)
                if following_type == 'noun':
                    # Valid: ma + na/si + noun (emphasizes the noun phrase)
                    return errors
                elif following_word in ['he', 'pi', 'ne'] and position + 3 < len(tokens):
                    # Check for ma + na/si + animacy + noun pattern
                    noun_word = tokens[position + 3]
                    noun_type = self._identify_word_type(noun_word)
                    if noun_type == 'noun':
                        # Valid: ma + na/si + animacy + noun (emphasizes the noun phrase)
                        return errors
                    else:
                        errors.append(SentenceValidationError(
                            SentenceError.EMPHASIS_SCOPE_ERROR,
                            f"Emphasis on POS marker '{target_word}' with animacy marker not followed by noun",
                            position=position,
                            word=f"ma+{target_word}"
                        ))
                        return errors
                else:
                    errors.append(SentenceValidationError(
                        SentenceError.EMPHASIS_SCOPE_ERROR,
                        f"Emphasis on POS marker '{target_word}' not followed by noun phrase",
                        position=position,
                        word=f"ma+{target_word}"
                    ))
                    return errors
            else:
                errors.append(SentenceValidationError(
                    SentenceError.EMPHASIS_SCOPE_ERROR,
                    f"Emphasis on POS marker '{target_word}' incomplete - missing target noun phrase",
                    position=position,
                    word=f"ma+{target_word}"
                ))
                return errors
        
        # Special handling for other slot 2 particles that can be emphasized
        if target_word in ['se', 'ra']:
            # Derivational particles - check if followed by appropriate word
            if position + 2 < len(tokens):
                following_word = tokens[position + 2]
                following_type = self._identify_word_type(following_word)
                if (target_word == 'se' and following_type == 'noun') or (target_word == 'ra' and following_type == 'verb'):
                    # Valid derivational construction
                    return errors
                else:
                    errors.append(SentenceValidationError(
                        SentenceError.EMPHASIS_SCOPE_ERROR,
                        f"Emphasis on derivational particle '{target_word}' not followed by appropriate word",
                        position=position,
                        word=f"ma+{target_word}"
                    ))
                    return errors
        
        # Check for prohibited targets (other particles that shouldn't be emphasized)
        prohibited_particles = ['wa', 'ho', 'tu', 'hu', 'hi', 'ro', 'nu', 'ti', 'mu', 'pe', 'ha', 'mi', 'lu', 'so', 'we', 'la', 'ni', 'po', 'pu', 'ri', 'wi', 'wu', 'to', 'ru', 'me', 'si', 'na', 'te']
        if target_word in prohibited_particles:
            errors.append(SentenceValidationError(
                SentenceError.EMPHASIS_SCOPE_ERROR,
                f"Emphasis particle 'ma' cannot target particle '{target_word}'. "
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
                word_type = self._identify_word_type(tokens[i])
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
        
        return errors
    
    def _validate_emphasis_particle_interactions(self, position: int, 
                                               tokens: List[str]) -> List[SentenceValidationError]:
        """Validate emphasis particle interactions with other particles."""
        errors = []
        
        # Check what comes immediately after ma
        if position + 1 >= len(tokens):
            return errors  # Already handled in scope validation
        
        next_token = tokens[position + 1]
        next_word_type = self._identify_word_type(next_token)
        
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
        noun_type = self._identify_word_type(noun_word)
        
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
        adj_type = self._identify_word_type(adj_word)
        
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
        noun_type = self._identify_word_type(noun_word)
        
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
        target_type = self._identify_word_type(target_word)
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
        verb_type = self._identify_word_type(verb_word)
        
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
                word_type = self._identify_word_type(tokens[i])
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
                word_type = self._identify_word_type(tokens[i])
                if word_type in self.emphasis_scope_rules['target_restrictions']['allowed_targets']:
                    return tokens[i]
                elif word_type == 'slot_2_particle':
                    continue
                else:
                    break
        return None
    
    def _identify_word_type(self, word: str) -> Optional[str]:
        """Identify the part of speech of a word using the lexicon validator."""
        if self.lexicon_validator:
            return self.lexicon_validator.identify_word_type(word)
        return None 