#!/usr/bin/env python3
"""
Particle Validation Module

Handles particle ordering, scope validation, and particle-specific
grammatical rules for Phi sentences.
"""

from typing import List, Dict, Set, Optional
from .errors import SentenceError, SentenceValidationError
from .clause_parser import get_clause_parser


class ParticleValidator:
    """Validates particle ordering and scope in Phi sentences."""
    
    def __init__(self):
        """Initialize particle validation rules."""
        # Lexicon validator for word type identification
        self.lexicon_validator = None  # Will be set by core
        
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
        
        # Legacy particle categories for compatibility
        self.tense_particles = {'li', 'ta', 'su'}
        self.aspect_particles = {'we', 'la', 'ni', 'po', 'pu', 'ri', 'wi', 'wu'}
        self.mood_particles = {'to', 'ru', 'me'}
    
    def set_lexicon_validator(self, lexicon_validator):
        """Set the lexicon validator for word type identification."""
        self.lexicon_validator = lexicon_validator
    
    def validate_particles(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate all particle-related rules."""
        errors = []
        
        # 1. Validate particle ordering
        errors.extend(self.validate_particle_order(tokens))
        
        # 2. Validate particle scope
        errors.extend(self.validate_particle_scope(tokens))
        
        # 3. Validate no duplicate particles
        errors.extend(self.validate_no_duplicates(tokens))
        
        return errors
    
    def validate_particle_order(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate that particles appear in correct order within their slots."""
        errors = []
        
        # Check slot 0 ordering
        slot_0_particles = [(i, token) for i, token in enumerate(tokens) 
                           if token in self.slot_0_particles]
        errors.extend(self._validate_slot_order(slot_0_particles, self.slot_0_order, "Slot 0"))
        
        # Check slot 1 ordering
        slot_1_particles = [(i, token) for i, token in enumerate(tokens) 
                           if token in self.slot_1_particles]
        errors.extend(self._validate_slot_order(slot_1_particles, self.slot_1_order, "Slot 1"))
        
        # Check slot 2 ordering (group by target words)
        errors.extend(self._validate_slot_2_order(tokens))
        
        return errors
    
    def _validate_slot_order(self, particles: List[tuple], order_groups: List[List[str]], 
                           slot_name: str) -> List[SentenceValidationError]:
        """Validate ordering within a specific slot."""
        errors = []
        
        if len(particles) < 2:
            return errors  # No ordering issues with 0 or 1 particles
        
        # Check that particles appear in correct group order
        for i in range(len(particles) - 1):
            current_pos, current_particle = particles[i]
            next_pos, next_particle = particles[i + 1]
            
            current_group = self._get_particle_order_index(current_particle, order_groups)
            next_group = self._get_particle_order_index(next_particle, order_groups)
            
            if current_group > next_group:
                errors.append(SentenceValidationError(
                    SentenceError.PARTICLE_ORDER,
                    f"{slot_name} particle order violation: '{current_particle}' "
                    f"should come after '{next_particle}'",
                    position=current_pos,
                    word=current_particle
                ))
        
        return errors
    
    def _get_particle_order_index(self, particle: str, order_groups: List[List[str]]) -> int:
        """Get the ordering index of a particle within its slot."""
        for i, group in enumerate(order_groups):
            if particle in group:
                return i
        return len(order_groups)  # Unknown particles go last
    
    def _validate_slot_2_order(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate slot 2 particle ordering within groups that modify the same target word."""
        errors = []
        
        # Group consecutive slot 2 particles with their target words
        particle_groups = []
        i = 0
        while i < len(tokens):
            if tokens[i] in self.slot_2_particles:
                # Special handling for emphasis particle 'ma'
                if tokens[i] == 'ma':
                    # Check if 'ma' is followed by other slot 2 particles
                    if i + 1 < len(tokens) and tokens[i + 1] in self.slot_2_particles:
                        # 'ma' emphasizes the following phrase, treat as separate group
                        particle_groups.append({
                            'particles': [(i, tokens[i])],
                            'target_word': f"phrase_starting_with_{tokens[i + 1]}",
                            'target_pos': i + 1,
                            'is_emphasis': True
                        })
                        i += 1
                        continue
                    else:
                        # 'ma' followed by content word, normal processing
                        pass
                
                # Start of a particle group (normal processing)
                group_start = i
                group_particles = []
                
                # Collect consecutive slot 2 particles (excluding emphasis that modifies phrases)
                while i < len(tokens) and tokens[i] in self.slot_2_particles:
                    # Skip 'ma' if it's emphasizing a phrase (already handled above)
                    if tokens[i] == 'ma' and i > group_start:
                        break
                    group_particles.append((i, tokens[i]))
                    i += 1
                
                # Find the target word (should be immediately after the particles)
                target_word = None
                target_pos = None
                if i < len(tokens):
                    target_word = tokens[i]
                    target_pos = i
                
                if group_particles:  # Only add if we have particles
                    particle_groups.append({
                        'particles': group_particles,
                        'target_word': target_word,
                        'target_pos': target_pos,
                        'is_emphasis': False
                    })
            else:
                i += 1
        
        # Validate ordering within each group (skip emphasis groups)
        for group in particle_groups:
            if len(group['particles']) > 1 and not group.get('is_emphasis', False):
                errors.extend(self._validate_slot_order(
                    group['particles'], 
                    self.slot_2_order, 
                    f"Slot 2 (targeting '{group['target_word']}')"
                ))
        
        return errors
    
    def validate_particle_scope(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate that particles are properly positioned relative to their targets."""
        errors = []
        
        for i, token in enumerate(tokens):
            if token in self.slot_1_particles:
                # Slot 1 particles should precede a verb (including derived verbs and adjective predicates)
                verb_found = False
                for j in range(i + 1, len(tokens)):
                    next_token = tokens[j]
                    next_word_type = self._identify_word_type(next_token)
                    
                    # Check for regular verbs
                    if next_word_type == 'verb':
                        verb_found = True
                        break
                    
                    # Check for derivational constructions that create verbs
                    elif next_token == 'se' and j + 1 < len(tokens):
                        # se + noun = derived verb
                        following_token = tokens[j + 1]
                        following_word_type = self._identify_word_type(following_token)
                        if following_word_type == 'noun':
                            verb_found = True
                            break
                    
                    # Check for adjective + copula constructions
                    elif next_word_type == 'adjective' and j + 1 < len(tokens):
                        # adjective + phera = adjective predicate
                        following_token = tokens[j + 1]
                        if following_token == 'phera':  # copula verb
                            verb_found = True
                            break
                    
                    # Hit a non-verb content word (but not derivational particles or adjectives)
                    elif next_word_type and not next_word_type.endswith('_particle') and next_token not in ['se', 'ra'] and next_word_type != 'adjective':
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
                    next_word_type = self._identify_word_type(tokens[i + 1])
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
    
    def _identify_word_type(self, word: str) -> Optional[str]:
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
        if self.lexicon_validator:
            return self.lexicon_validator.identify_word_type(word)
        
        return None
    
    def is_particle(self, word: str) -> bool:
        """Check if a word is a particle."""
        return word in self.all_particles
    
    def get_particle_slot(self, particle: str) -> int:
        """Get the slot number (0, 1, or 2) for a particle."""
        if particle in self.slot_0_particles:
            return 0
        elif particle in self.slot_1_particles:
            return 1
        elif particle in self.slot_2_particles:
            return 2
        else:
            return -1  # Unknown particle
    
    def get_particle_category(self, particle: str) -> str:
        """Get the functional category of a particle."""
        if particle in self.tense_particles:
            return "tense"
        elif particle in self.aspect_particles:
            return "aspect"
        elif particle in self.mood_particles:
            return "mood"
        else:
            return "other"
    
    def validate_no_duplicates(self, tokens: List[str]) -> List[SentenceValidationError]:
        """Validate that particles are not duplicated inappropriately within each clause."""
        errors = []
        
        # Split sentence into clauses using shared clause parser
        clauses = get_clause_parser(self.lexicon_validator).split_into_clauses(tokens)
        
        # Validate each clause separately for particle duplicates
        for clause_tokens, clause_start_idx in clauses:
            if clause_tokens:  # Skip empty clauses
                clause_errors = self._validate_clause_no_duplicates(clause_tokens, clause_start_idx)
                errors.extend(clause_errors)
        
        return errors
    
    def _validate_clause_no_duplicates(self, tokens: List[str], start_idx: int) -> List[SentenceValidationError]:
        """Validate that particles are not duplicated within a single clause."""
        errors = []
        
        # Track particles we've seen by slot type within this clause
        seen_slot_0_particles = {}  # Sentence-level particles (should not repeat)
        seen_slot_1_particles = {}  # Verb-level particles (should not repeat)
        seen_slot_2_with_targets = []  # Slot 2 particles with their targets
        
        i = 0
        while i < len(tokens):
            token = tokens[i]
            
            if token in self.all_particles:
                if token in self.slot_0_particles:
                    # Slot 0 particles should not be duplicated within a clause
                    if token in seen_slot_0_particles:
                        prev_pos = seen_slot_0_particles[token]
                        errors.append(SentenceValidationError(
                            SentenceError.PARTICLE_ORDER,
                            f"Duplicate slot 0 particle '{token}' found at positions {start_idx + prev_pos} and {start_idx + i}. "
                            f"Sentence-level particles should not be repeated within a clause",
                            position=start_idx + i,
                            word=token
                        ))
                    else:
                        seen_slot_0_particles[token] = i
                
                elif token in self.slot_1_particles:
                    # Slot 1 particles should not be duplicated within a clause
                    if token in seen_slot_1_particles:
                        prev_pos = seen_slot_1_particles[token]
                        errors.append(SentenceValidationError(
                            SentenceError.PARTICLE_ORDER,
                            f"Duplicate slot 1 particle '{token}' found at positions {start_idx + prev_pos} and {start_idx + i}. "
                            f"Verb-level particles should not be repeated within a clause",
                            position=start_idx + i,
                            word=token
                        ))
                    else:
                        seen_slot_1_particles[token] = i
                
                elif token in self.slot_2_particles:
                    # Slot 2 particles can be repeated if they modify different targets
                    # Find the target word for this particle
                    target_word = None
                    target_pos = None
                    
                    # Look ahead to find the target (skip other slot 2 particles)
                    j = i + 1
                    while j < len(tokens) and tokens[j] in self.slot_2_particles:
                        j += 1
                    
                    if j < len(tokens):
                        target_word = tokens[j]
                        target_pos = j
                    
                    # Check if this particle+target combination already exists within this clause
                    for prev_particle, prev_target, prev_pos in seen_slot_2_with_targets:
                        if prev_particle == token and prev_target == target_word:
                            errors.append(SentenceValidationError(
                                SentenceError.PARTICLE_ORDER,
                                f"Duplicate slot 2 particle '{token}' modifying same target '{target_word}' "
                                f"found at positions {start_idx + prev_pos} and {start_idx + i}",
                                position=start_idx + i,
                                word=token
                            ))
                            break
                    
                    seen_slot_2_with_targets.append((token, target_word, i))
            
            i += 1
        
        return errors 