#!/usr/bin/env python3
"""
Clause Parsing Utilities

Shared utilities for parsing sentence clauses, handling clause boundaries,
and conditional sentence structures in Phi.
"""

from typing import List, Tuple, Optional


class ClauseParser:
    """Utility class for parsing sentence clauses and boundaries."""
    
    def __init__(self, lexicon_validator=None):
        """Initialize clause parsing rules."""
        self.lexicon_validator = lexicon_validator
        
        # Clause boundary conjunctions
        self.clause_boundary_conjunctions = {
            'wetu',  # if
            'matu',  # after
            'pimo',  # before
            'wane',  # when
            'lina',  # while
            'runa',  # until
            'mi'     # contrast (creates discourse boundary)
        }
        
        # Reported speech verbs that introduce separate clauses
        self.reported_speech_verbs = {
            'shuso',  # say
            'shuna',  # call (can introduce reported speech)
        }
    
    def split_into_clauses(self, tokens: List[str]) -> List[Tuple[List[str], int]]:
        """Split tokens into clauses at clause boundary conjunctions and reported speech verbs."""
        clauses = []
        current_clause = []
        current_start_idx = 0
        
        i = 0
        while i < len(tokens):
            token = tokens[i]
            
            # Special handling for ha-mi combinations
            if token == 'ha' and i + 1 < len(tokens) and tokens[i + 1] == 'mi':
                # ha mi should be treated as a single discourse unit, not split
                current_clause.append(token)  # Add ha
                current_clause.append(tokens[i + 1])  # Add mi
                i += 2  # Skip both ha and mi
                continue
            elif token in self.clause_boundary_conjunctions:
                # End current clause (before conjunction)
                if current_clause:
                    clauses.append((current_clause, current_start_idx))
                
                # Handle conditional sentences specially
                if token == 'wetu':
                    # Parse wetu conditional: wetu [if-clause] [then-clause]
                    if_clause, then_clause, next_i = self.parse_conditional_clauses(tokens, i + 1)
                    
                    if if_clause:
                        clauses.append((if_clause, i + 1))
                    if then_clause:
                        clauses.append((then_clause, i + 1 + len(if_clause)))
                    
                    i = next_i
                    current_clause = []
                    current_start_idx = i
                else:
                    # Start new clause (after conjunction)
                    current_clause = []
                    current_start_idx = i + 1
                    i += 1
            elif token in self.reported_speech_verbs:
                # Handle reported speech: [main clause with speech verb] [reported clause]
                current_clause.append(token)  # Include the speech verb in the main clause
                
                # End the main clause here
                clauses.append((current_clause, current_start_idx))
                
                # Start new clause for reported speech content
                current_clause = []
                current_start_idx = i + 1
                i += 1
            else:
                current_clause.append(token)
                i += 1
        
        # Add final clause
        if current_clause:
            clauses.append((current_clause, current_start_idx))
        
        return clauses
    
    def parse_conditional_clauses(self, tokens: List[str], start_idx: int) -> Tuple[List[str], List[str], int]:
        """Parse wetu conditional into if-clause and then-clause."""
        if_clause = []
        then_clause = []
        
        # Find the boundary between if-clause and then-clause
        # Look for the start of the then-clause (typically a pronoun or new subject)
        boundary_idx = None
        
        # Strategy: find the first verb, then look for the next subject (pronoun/noun)
        first_verb_idx = None
        
        for i in range(start_idx, len(tokens)):
            token = tokens[i]
            word_type = self.identify_word_type(token)
            
            # Find first verb
            if word_type == 'verb' and first_verb_idx is None:
                first_verb_idx = i
                continue
            
            # After finding first verb, look for then-clause subject
            if first_verb_idx is not None:
                # Look for pronouns or animacy markers that start new clause
                if (token in ['mia', 'thi', 'sha'] or  # pronouns
                    token in ['he', 'pi', 'ne']):  # animacy markers (start of noun phrase)
                    boundary_idx = i
                    break
        
        # If no clear boundary found, use a fallback strategy
        if boundary_idx is None:
            # Look for the pattern: [verb] [pronoun/animacy] as clause boundary
            for i in range(start_idx + 1, len(tokens) - 1):
                prev_token = tokens[i - 1]
                curr_token = tokens[i]
                
                # If previous token could be end of verb phrase and current starts new subject
                if (curr_token in ['mia', 'thi', 'sha', 'he', 'pi', 'ne']):
                    boundary_idx = i
                    break
        
        # Final fallback: split roughly in the middle
        if boundary_idx is None:
            remaining_tokens = tokens[start_idx:]
            boundary_idx = start_idx + len(remaining_tokens) // 2
        
        # Split into clauses
        if_clause = tokens[start_idx:boundary_idx]
        then_clause = tokens[boundary_idx:] if boundary_idx < len(tokens) else []
        
        return if_clause, then_clause, len(tokens)
    
    def identify_word_type(self, word: str) -> Optional[str]:
        """Identify the part of speech of a word using the lexicon validator."""
        if self.lexicon_validator:
            return self.lexicon_validator.identify_word_type(word)
        
        # Fallback to simplified identification if no lexicon validator available
        # This is only for basic clause boundary detection
        if word in ['mia', 'thi', 'sha']:
            return 'pronoun'
        elif word in ['he', 'pi', 'ne']:
            return 'particle'  # animacy particles
        elif word in ['li', 'ta', 'su']:
            return 'particle'  # tense particles
        elif word in ['na', 'si', 'te']:
            return 'particle'  # role particles
        
        return None


# Global instance for shared use
def get_clause_parser(lexicon_validator=None):
    """Get a ClauseParser instance with optional lexicon validator."""
    return ClauseParser(lexicon_validator)