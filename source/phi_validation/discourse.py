#!/usr/bin/env python3
"""
Discourse Validation Module

Validates discourse particle sequences, topic chains, contrast scope,
and topic-contrast interaction patterns in Phi.
"""

from typing import List, Tuple, Dict, Optional
from .errors import SentenceError, SentenceValidationError


class DiscourseValidator:
    """Validates discourse structure and particle sequences."""
    
    def __init__(self):
        """Initialize discourse validation rules."""
        pass
    
    def validate_discourse_sequences(self, tokens: List[str]) -> List[SentenceValidationError]:
        """
        Validate discourse particle sequences for topic chains, contrast scope,
        and topic-contrast interaction patterns.
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
        
        return errors
    
    def _validate_discourse_sequence_patterns(self, discourse_particles: List[Tuple[str, int]], 
                                            tokens: List[str]) -> List[SentenceValidationError]:
        """Validate overall discourse sequence patterns and coherence."""
        errors = []
        
        # Check for discourse repair patterns
        repair_errors = self._validate_discourse_repair_patterns(discourse_particles, tokens)
        errors.extend(repair_errors)
        
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
            
            # Define all particles for checking
            all_particles = {
                'wa', 'ho', 'tu', 'hu', 'hi', 'ro', 'nu', 'ti', 'mu', 'pe',
                'ha', 'mi', 'lu', 'so', 'li', 'ta', 'su', 'we', 'la', 'ni',
                'po', 'pu', 'ri', 'wi', 'wu', 'to', 'ru', 'me', 'si', 'na',
                'te', 'se', 'ra', 'he', 'pi', 'ne', 'pa', 'mo', 'sa', 'le',
                're', 'wo', 'lo', 'no', 'ma'
            }
            
            if following_word in all_particles and following_word not in allowed_after_ha:
                # Only flag as error if it's a problematic particle
                problematic_particles = {'wa', 'li', 'ta', 'su'}  # removed 'mi' as it's valid in ha-mi combinations
                if following_word in problematic_particles:
                    context['type'] = 'invalid_topic_shift'
                    context['reason'] = 'Topic marker followed by particle instead of topic noun'
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
        
        # Only check for very basic content requirements
        if len(preceding_tokens) == 0:
            validity['valid'] = False
            validity['reason'] = 'No content before contrast marker'
        elif len(following_tokens) == 0:
            validity['valid'] = False
            validity['reason'] = 'No content after contrast marker'
        
        return validity
    
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