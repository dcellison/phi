#!/usr/bin/env python3
"""
Phi Word Lookup Utility

This script extracts all phi words from the POS documentation files and provides
comprehensive validation functionality including:
- Lexicon accuracy (all phi words from official lexicon)
- SOV compliance (all sentences follow Subject-Object-Verb order)
- Glossing format (proper three-line structure: phi/gloss/english)
- Phonotactic compliance (all words follow correct POS patterns)
- Particle usage (correct grammatical particles where needed)

All data is read directly from source files for maximum reliability.

Usage:
    python phi_word_lookup.py word1 word2 word3
    python phi_word_lookup.py --extract  # Extract all words from POS files
    python phi_word_lookup.py --validate "mia whethea shose"  # Validate sentence
    python phi_word_lookup.py --validate-file "path/to/file.md"  # Validate file
    python phi_word_lookup.py --comprehensive-validate-file "path/to/file.md"  # Full validation
"""

import os
import re
import json
import argparse
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Set

class PhiLanguageValidator:
    """Comprehensive phi language validator for all grammatical requirements."""
    
    def __init__(self):
        # SOV validation patterns
        self.phi_particles = {
            'si', 'na', 'te', 'lo', 'tu', 'pu', 'wa',  # Essential core
            'li', 'ta', 'su', 'ni', 'ri', 'lu',        # Tense/aspect/mood
            'ra', 'se', 'we', 'wo', 'hi', 'ro',        # Modality
            'ha', 'mi', 'ma', 'nu', 'ho', 'po',        # Discourse management
            'pa', 'mo', 'sa', 'me', 'to'               # Comparison/quantification
        }
        
        self.phi_pronouns = {'mia', 'thi', 'sha', 'lua', 'nua'}
        
        # Clause boundary conjunctions for parsing - actual phi words
        self.clause_boundary_conjunctions = {
            'nene',  # and (coordination)
            'wiho',  # or (coordination)
            'tupo',  # but (coordination)
            'wane',  # when (temporal)
            'matu',  # after (temporal)
            'pimo',  # before (temporal)
            'lina',  # while (temporal)
            'wetu',  # if (logical)
            'renu',  # because (logical)
            'lipi',  # although (logical)
            'tela',  # that (logical)
            'woma',  # as (comparison)
            'rami'   # than (comparison)
        }
        
        # Expected POS patterns
        self.pos_patterns = {
            'noun': ['CVFP', 'CPFP', 'FVFP', 'FPFP'],
            'verb': ['FVCV'],
            'adjective': ['CVFV'],
            'adverb': ['CVCVCV'],
            'preposition': ['FP'],
            'determiner': ['FPCV'],
            'classifier': ['CP'],
            'conjunction': ['CVCV'],
            'interjection': ['CVCP'],
            'number': ['FV', 'FVFV'],
            'particle': ['CV'],
            'pronoun': ['CP', 'FV']
        }
        
        # Word database reference for type identification
        self.word_db = None
        
    def set_word_database(self, word_db):
        """Set reference to word database for type identification."""
        self.word_db = word_db
        
    def identify_word_type(self, word: str) -> Optional[str]:
        """Identify the part of speech of a word using the word database."""
        if self.word_db:
            word_info = self.word_db.get(word.lower())
            if word_info:
                return word_info['pos']
        
        # Fallback identification for common particles and pronouns
        if word in self.phi_particles:
            return 'particle'
        elif word in self.phi_pronouns:
            return 'pronoun'
        
        return None
        
    def split_into_clauses(self, tokens: List[str]) -> List[Tuple[List[str], int]]:
        """Split tokens into clauses at clause boundary conjunctions."""
        clauses = []
        current_clause = []
        current_start_idx = 0
        
        i = 0
        while i < len(tokens):
            token = tokens[i]
            
            if token in self.clause_boundary_conjunctions:
                # End current clause (before conjunction)
                if current_clause:
                    clauses.append((current_clause, current_start_idx))
                
                # Start new clause (after conjunction)
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
    
    def validate_sov_compliance(self, phi_line: str, gloss_line: str) -> Tuple[bool, str]:
        """Validate that a phi sentence follows SOV (Subject-Object-Verb) order."""
        phi_words = phi_line.strip().split()
        gloss_words = gloss_line.strip().split()
        
        if len(phi_words) != len(gloss_words):
            return False, f"Mismatched word count: {len(phi_words)} phi words vs {len(gloss_words)} gloss words"
        
        # Skip if not a complete sentence (just phrases)
        if len(phi_words) < 2:
            return True, "Phrase only, SOV not applicable"
        
        # Use sophisticated clause parsing
        clauses = self.split_into_clauses(phi_words)
        
        # Validate SOV order within each clause
        all_valid = True
        all_issues = []
        
        for clause_idx, (clause_phi, start_idx) in enumerate(clauses):
            if len(clause_phi) < 2:  # Skip single-word clauses
                continue
                
            # Get corresponding gloss words for this clause
            clause_gloss = gloss_words[start_idx:start_idx + len(clause_phi)]
            
            clause_valid, clause_issues = self._validate_clause_sov_advanced(clause_phi, clause_gloss)
            if not clause_valid:
                all_valid = False
                all_issues.append(f"Clause {clause_idx + 1}: {clause_issues}")
        
        if all_valid:
            return True, "SOV order correct in all clauses"
        else:
            return False, f"SOV violations: {'; '.join(all_issues)}"
    
    def _validate_clause_sov_advanced(self, phi_words: List[str], gloss_words: List[str]) -> Tuple[bool, str]:
        """Advanced SOV validation using proper grammatical role identification."""
        if len(phi_words) != len(gloss_words):
            return False, "Word count mismatch in clause"
        
        # Check for topic structures that don't follow SOV order
        if 'ha' in phi_words or 'TOP' in gloss_words:
            return True, "Topic structure - SOV order not enforced"
        
        # Check for focus structures that may have different word order
        if 'nu' in phi_words or 'FOC' in gloss_words:
            return True, "Focus structure - SOV order not enforced"
        
        # Check for conditional structures that may have different word order
        if 'lu' in phi_words or any(gloss == 'if' for gloss in gloss_words):
            return True, "Conditional structure - SOV order not enforced"
        
        # Build grammatical structure with proper role identification
        content_items = []  # List of (word, role) tuples in original order
        
        for i, (phi_word, gloss) in enumerate(zip(phi_words, gloss_words)):
            word_type = self.identify_word_type(phi_word)
            role = self._identify_grammatical_role(phi_word, gloss, word_type, phi_words, gloss_words, i)
            
            if role != 'particle':  # Only track content words for SOV order
                content_items.append((phi_word, role))
        
        if len(content_items) < 2:
            return True, "Not enough content words for SOV analysis"
        
        # Extract just the roles in the order they appear
        content_roles = [role for word, role in content_items]
        content_words = [word for word, role in content_items]
        
        # Check for verb to determine if this needs SOV validation
        if 'verb' not in content_roles:
            return True, "No verb found, SOV not applicable to noun/adjective phrases"
        
        # Find positions of S, O, V in the content word sequence
        subject_pos = content_roles.index('subject') if 'subject' in content_roles else -1
        object_pos = content_roles.index('object') if 'object' in content_roles else -1
        verb_pos = content_roles.index('verb') if 'verb' in content_roles else -1
        
        sov_issues = []
        
        # Check SOV constraints using content word positions
        if subject_pos != -1 and verb_pos != -1 and subject_pos > verb_pos:
            sov_issues.append(f"Subject after verb (content pos {subject_pos} > {verb_pos})")
        
        if object_pos != -1 and verb_pos != -1 and object_pos > verb_pos:
            sov_issues.append(f"Object after verb (content pos {object_pos} > {verb_pos})")
        
        if subject_pos != -1 and object_pos != -1 and subject_pos > object_pos:
            sov_issues.append(f"Subject after object (content pos {subject_pos} > {object_pos})")
        
        if sov_issues:
            return False, '; '.join(sov_issues)
        else:
            return True, "SOV order correct"
    
    def _identify_grammatical_role(self, phi_word: str, gloss: str, word_type: str, 
                                   phi_words: List[str], gloss_words: List[str], position: int) -> str:
        """Identify the grammatical role of a word in context."""
        # Handle particles first
        if phi_word in self.phi_particles:
            return 'particle'
        
        # Check for explicit role marking by examining surrounding particles
        # Look for SBJ, OBJ, VRB markers that precede this word
        if position > 0:
            prev_gloss = gloss_words[position - 1]
            if prev_gloss == 'SBJ':
                return 'subject'
            elif prev_gloss == 'OBJ':
                return 'object'  
            elif prev_gloss == 'VRB':
                return 'verb'
        
        # Check for explicit role marking in gloss
        if gloss in ['1SG', '2SG', '3SG'] or phi_word in self.phi_pronouns:
            # If not explicitly marked by particles, first pronoun is typically subject
            return 'subject'
        
        # Identify verbs by word type or actual phi words
        if word_type == 'verb' or phi_word in {
            'thewo',  # prepare
            'whemo',  # think
            'shose',  # see
            'whera',  # learn
            'whiwo',  # give
            'phera',  # be
            'thero',  # go
            'wusu',   # stay
            'phemi',  # run
            'thanu',  # complete
            'phusu',  # cook
            'whuru',  # eat
            'thalu',  # drink
            'phema',  # sleep
            'whute'   # wake
        }:
            return 'verb'
        
        # Identify objects - nouns by word type or actual phi words
        if word_type == 'noun' or phi_word in {
            'noshea',   # food
            'whuthea',  # water
            'liphai',   # tree
            'hiwhea',   # house
            'thephoa',  # person
            'whethea',  # book
            'phuithea', # tool
            'whothea'   # stone/material
        }:
            # If not explicitly marked, assume object for nouns
            return 'object'
        
        # Other word types
        if word_type == 'adjective':
            return 'adjective'
        elif word_type == 'adverb':
            return 'adverb'
        elif word_type == 'determiner':
            return 'determiner'
        
        # Default to content word if unknown
        return 'content'
    
    def validate_glossing_format(self, code_block: str) -> Tuple[bool, List[str]]:
        """Validate that a code block follows proper three-line glossing format."""
        lines = [line.strip() for line in code_block.strip().split('\n') if line.strip()]
        issues = []
        
        # Handle 4-line blocks with compositional analysis
        if len(lines) == 4 and lines[3].startswith('(composition:'):
            # Validate as 3-line block, ignoring the compositional analysis line
            lines = lines[:3]
        elif len(lines) == 4 and lines[0].startswith('written:'):
            # Handle orthographic analysis format: written:/pattern:/gloss:/english:
            # Extract the actual content by removing prefixes
            phi_line = lines[0].replace('written:', '').strip()
            gloss_line = lines[2].replace('gloss:', '').strip()
            english_line = lines[3].replace('english:', '').strip()
            # Capitalize first letter of extracted English line
            if english_line and english_line[0].islower():
                english_line = english_line[0].upper() + english_line[1:]
            lines = [phi_line, gloss_line, english_line]
        elif len(lines) >= 4 and ('english irregular:' in lines[0] or 'sentence:' in lines[0]):
            # Skip validation for educational demonstration blocks
            return True, []
        elif len(lines) != 3:
            issues.append(f"Expected 3 lines, found {len(lines)}")
            return False, issues
        
        phi_line, gloss_line, english_line = lines
        
        # Check if this is a word list or demonstration (not a grammatical sentence)
        is_word_list = (
            ',' in english_line or  # English translations separated by commas
            english_line.count(' ') >= 2 and all(word[0].isupper() for word in english_line.split() if word) or  # Multiple capitalized words
            gloss_line.startswith('/') and gloss_line.endswith('/')  # IPA transcription instead of glosses
        )
        
        if is_word_list:
            # For word lists, just validate basic format, skip SOV
            if not re.match(r'^[a-z\s\.]+$', phi_line):
                issues.append("Phi line contains invalid characters (only lowercase letters, spaces, periods allowed)")
            if not english_line[0].isupper():
                issues.append("English line should start with capital letter")
            return len(issues) == 0, issues
        
        # Validate phi line (first line)
        if not re.match(r'^[a-z\s\.]+$', phi_line):
            issues.append("Phi line contains invalid characters (only lowercase letters, spaces, periods allowed)")
        
        if ',' in phi_line:
            issues.append("Phi line contains comma (only periods and spaces allowed)")
        
        # Validate gloss line (second line) 
        phi_words = phi_line.split()
        gloss_words = gloss_line.split()
        
        if len(phi_words) != len(gloss_words):
            issues.append(f"Word count mismatch: {len(phi_words)} phi words vs {len(gloss_words)} gloss words")
        
        # Check for proper linguistic abbreviations - ONLY official phi glosses
        valid_glosses = {
            # Official phi particle glosses from particles.md
            'ABIL', 'AFF', 'ATT', 'CMPR', 'CNT', 'COND', 'DIR', 'DU', 'EMPH', 
            'EQL', 'EVEN', 'FOC', 'FUT', 'HEDGE', 'HORT', 'IMP', 'INFER', 'IPFV', 
            'LIM', 'NEC', 'NEG', 'OBJ', 'PASS', 'PAUC', 'PFV', 'PL', 'POS', 
            'PRH', 'PRS', 'PST', 'Q', 'SBJ', 'SHIFT', 'SPRL', 'TOP', 'VRB',
            # Standard pronoun glosses
            '1SG', '2SG', '3SG'
        }
        
        # Valid classifier abbreviations (CL.* format)
        valid_classifier_glosses = {
            # Shape and physical properties
            'CL.long', 'CL.flat', 'CL.round', 'CL.rectangular', 'CL.container', 'CL.flexible',
            # Animacy
            'CL.human', 'CL.animal', 'CL.plant', 'CL.inanimate',
            # Functional categories  
            'CL.building', 'CL.vehicle', 'CL.tool', 'CL.clothing', 'CL.document', 'CL.food',
            # Spatial and temporal
            'CL.place', 'CL.time', 'CL.event',
            # Quantitative groupings
            'CL.group', 'CL.mass', 'CL.pair'
        }
        
        for gloss in gloss_words:
            # Official glosses are uppercase abbreviations
            if gloss.isupper() and gloss not in valid_glosses:
                issues.append(f"Invalid gloss abbreviation: {gloss} (not in official phi gloss list)")
            # Classifier glosses follow CL.* pattern
            elif gloss.startswith('CL.') and gloss not in valid_classifier_glosses:
                issues.append(f"Invalid classifier gloss: {gloss} (not in official phi classifier list)")
            # Everything else should be lowercase content words (English translations)
        
        # Validate English line (third line)
        if english_line.startswith('"') or english_line.endswith('"'):
            issues.append("English line should not have quotes")
        
        if not english_line[0].isupper():
            issues.append("English line should start with capital letter")
        
        # Check SOV compliance (only for grammatical sentences, not word lists)
        sov_valid, sov_message = self.validate_sov_compliance(phi_line, gloss_line)
        if not sov_valid:
            issues.append(f"SOV violation: {sov_message}")
        
        return len(issues) == 0, issues
    
    def extract_code_blocks(self, content: str) -> List[Tuple[str, int]]:
        """Extract all code blocks from markdown content with their line numbers."""
        code_blocks = []
        lines = content.split('\n')
        
        i = 0
        while i < len(lines):
            if lines[i].strip() == '```':
                # Found start of code block
                start_line = i + 1
                block_lines = []
                i += 1
                
                # Collect lines until closing ```
                while i < len(lines) and lines[i].strip() != '```':
                    block_lines.append(lines[i])
                    i += 1
                
                if i < len(lines):  # Found closing ```
                    code_blocks.append(('\n'.join(block_lines), start_line))
                
            i += 1
        
        return code_blocks
    
    def validate_phonotactic_compliance(self, word: str, expected_pos: str) -> Tuple[bool, str]:
        """Validate that a word follows the correct phonotactic pattern for its POS."""
        pattern = self._analyze_phonotactic_pattern(word)
        expected_patterns = self.pos_patterns.get(expected_pos, [])
        
        if pattern in expected_patterns:
            return True, f"Valid {expected_pos} pattern: {pattern}"
        else:
            return False, f"Invalid pattern {pattern} for {expected_pos}. Expected: {', '.join(expected_patterns)}"
    
    def _analyze_phonotactic_pattern(self, word: str) -> str:
        """Analyze a phi word and return its phonotactic pattern."""
        pattern = ""
        i = 0
        
        while i < len(word):
            # Check for digraphs first
            if i < len(word) - 1:
                digraph = word[i:i+2]
                if digraph in ['ph', 'wh', 'th', 'sh']:
                    pattern += 'F'  # Fricative digraph
                    i += 2
                    continue
            
            # Check for vowel pairs
            if i < len(word) - 1:
                char1, char2 = word[i], word[i+1]
                if (char1 in 'aeiou' and char2 in 'aeiou' and 
                    char1 != char2):  # Different vowels
                    pattern += 'P'  # Vowel pair
                    i += 2
                    continue
            
            # Single character
            char = word[i]
            if char in 'aeiou':
                pattern += 'V'  # Vowel
            elif char in 'hlmnprstw':
                pattern += 'C'  # Consonant
            
            i += 1
            
        return pattern

class PhiWordDatabase:
    def __init__(self, pos_directory: str = "../source/pos"):
        self.pos_directory = Path(pos_directory)
        self.word_db: Dict[str, Dict[str, str]] = {}
        self.validator = PhiLanguageValidator()
        # Connect validator to word database for type identification
        self.validator.set_word_database(self.word_db)
        self.pos_files = self._discover_pos_files()
        
    def _discover_pos_files(self) -> Dict[str, str]:
        """Automatically discover all POS files in the directory structure."""
        pos_files = {}
        
        if not self.pos_directory.exists():
            print(f"Warning: POS directory {self.pos_directory} does not exist")
            return pos_files
        
        # Find all .md files recursively
        for md_file in self.pos_directory.rglob("*.md"):
            # Skip certain files
            if md_file.name.lower() in ['.ds_store', 'readme.md', 'index.md']:
                continue
                
            # Get relative path from pos_directory
            relative_path = md_file.relative_to(self.pos_directory)
            
            # Determine POS type from directory structure
            if len(relative_path.parts) > 1:
                # File is in a subdirectory - use directory name as POS type
                # e.g., nouns/objects.md -> POS = "noun"
                pos_type = relative_path.parts[0].rstrip('s')  # Remove plural 's'
                if pos_type == 'noun':  # Handle special case
                    pos_type = 'noun'
                elif pos_type in ['verb', 'adjective', 'adverb', 'particle', 
                                'pronoun', 'preposition', 'determiner', 
                                'conjunction', 'classifier', 'interjection']:
                    pos_type = pos_type
                else:
                    # Default to using directory name as-is
                    pos_type = relative_path.parts[0].rstrip('s')
            else:
                # File is in root POS directory - use filename as POS type
                # e.g., verbs.md -> POS = "verb"
                filename_without_ext = md_file.stem
                if filename_without_ext.endswith('s'):
                    pos_type = filename_without_ext.rstrip('s')
                else:
                    pos_type = filename_without_ext
            
            # Store the relative path as key and POS type as value
            pos_files[str(relative_path)] = pos_type
            
        return pos_files
    
    def show_discovered_files(self) -> None:
        """Display all discovered POS files for debugging."""
        print("Discovered POS files:")
        print("=" * 50)
        for filepath, pos_type in sorted(self.pos_files.items()):
            print(f"{filepath:30} -> {pos_type}")
        print(f"\nTotal: {len(self.pos_files)} files discovered")
    
    def _analyze_phonotactic_pattern(self, word: str) -> str:
        """Analyze a phi word and return its phonotactic pattern."""
        pattern = ""
        i = 0
        
        while i < len(word):
            # Check for digraphs first
            if i < len(word) - 1:
                digraph = word[i:i+2]
                if digraph in ['ph', 'wh', 'th', 'sh']:
                    pattern += 'F'  # Fricative digraph
                    i += 2
                    continue
            
            # Check for vowel pairs
            if i < len(word) - 1:
                char1, char2 = word[i], word[i+1]
                if (char1 in 'aeiou' and char2 in 'aeiou' and 
                    char1 != char2):  # Different vowels
                    pattern += 'P'  # Vowel pair
                    i += 2
                    continue
            
            # Single character
            char = word[i]
            if char in 'aeiou':
                pattern += 'V'  # Vowel
            elif char in 'hlmnprstw':
                pattern += 'C'  # Consonant
            
            i += 1
            
        return pattern
    
    def _count_syllables(self, word: str) -> int:
        """Count syllables in a phi word (each vowel = 1 syllable, including those in vowel pairs)."""
        syllables = 0
        i = 0
        
        while i < len(word):
            # Count each vowel individually, even in vowel pairs (hiatus)
            if word[i] in 'aeiou':
                syllables += 1
            
            i += 1
            
        return syllables
    
    def _find_digraphs(self, word: str) -> List[str]:
        """Find all digraphs in a phi word."""
        digraphs = []
        i = 0
        
        while i < len(word) - 1:
            digraph = word[i:i+2]
            if digraph in ['ph', 'wh', 'th', 'sh']:
                digraphs.append(digraph)
                i += 2
            else:
                i += 1
                
        return digraphs
    
    def _find_vowel_pairs(self, word: str) -> List[str]:
        """Find all vowel pairs in a phi word."""
        vowel_pairs = []
        i = 0
        
        while i < len(word) - 1:
            char1, char2 = word[i], word[i+1]
            if (char1 in 'aeiou' and char2 in 'aeiou' and 
                char1 != char2):  # Different vowels = vowel pair
                vowel_pairs.append(char1 + char2)
                i += 2
            else:
                i += 1
                
        return vowel_pairs
    
    def _extract_category_from_heading(self, lines: List[str], table_line: int) -> str:
        """Extract semantic category from the nearest heading above a table."""
        # Look backwards from the table to find the most recent heading
        for i in range(table_line - 1, -1, -1):
            line = lines[i].strip()
            
            # Look for markdown headings
            if line.startswith('###') or line.startswith('##'):
                # Clean up the heading
                heading = re.sub(r'^#+\s*', '', line)
                heading = re.sub(r'\s*\(\d+\s+\w+\).*$', '', heading)  # Remove "(12 nouns)" etc
                heading = re.sub(r'\s*\*.*\*\s*$', '', heading)  # Remove italic descriptions
                return heading.strip()
                
        return "uncategorized"
    
    def extract_words_from_file(self, filepath: Path, pos_category: str) -> Dict[str, Dict[str, str]]:
        """Extract phi words from a single POS markdown file."""
        words = {}
        
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                
            # Find tables with the specific header "| phi word | english translation |"
            # Split content into lines for processing
            lines = content.split('\n')
            
            i = 0
            while i < len(lines):
                line = lines[i].strip()
                
                # Look for the exact phi word table header
                if (line.startswith('| phi word |') and 'english translation' in line and line.endswith('|')):
                    # Extract category from heading above this table
                    category = self._extract_category_from_heading(lines, i)
                    
                    # Skip the header line and separator line (if it exists)
                    i += 1
                    if i < len(lines) and lines[i].strip().startswith('|') and '---' in lines[i]:
                        i += 1
                    
                    # Extract words from this table until we hit an empty line or new section
                    while i < len(lines):
                        line = lines[i].strip()
                        
                        # Stop if we hit an empty line, heading, or non-table line
                        if (not line or 
                            line.startswith('#') or 
                            not line.startswith('|') or
                            ('---' in line and line.startswith('|'))):
                            break
                            
                        # Extract phi word and translation from table row
                        # Pattern: | phi_word | english_translation |
                        match = re.match(r'\|\s*([a-z]{2,})\s*\|\s*([^|]+?)\s*\|', line)
                        if match:
                            phi_word = match.group(1).strip()
                            english_translation = match.group(2).strip()
                            
                            # Skip if not a valid phi word
                            if self._is_valid_phi_word(phi_word):
                                # Only add if we haven't seen this word in this file yet
                                if phi_word not in words:
                                    # Analyze the word structure
                                    pattern = self._analyze_phonotactic_pattern(phi_word)
                                    syllables = self._count_syllables(phi_word)
                                    digraphs = self._find_digraphs(phi_word)
                                    vowel_pairs = self._find_vowel_pairs(phi_word)
                                    
                                    words[phi_word] = {
                                        'pos': pos_category,
                                        'translation': english_translation,
                                        'source_file': filepath.name,
                                        'pattern': pattern,
                                        'syllables': syllables,
                                        'category': category,
                                        'digraphs': digraphs,
                                        'vowel_pairs': vowel_pairs
                                    }
                        
                        i += 1
                else:
                    i += 1
                
        except FileNotFoundError:
            print(f"Warning: File {filepath} not found")
        except Exception as e:
            print(f"Error processing {filepath}: {e}")
            
        return words
    
    def _is_valid_phi_word(self, word: str) -> bool:
        """Basic validation for phi words."""
        if not word or len(word) < 2:
            return False
            
        # Check if word contains only valid phi characters
        valid_chars = set('abcdefghijklmnopqrstuvwxyz')
        return all(char in valid_chars for char in word.lower())
    
    def build_database(self) -> None:
        """Extract all words from all POS files and build the database."""
        print("Building phi word database...")
        
        for filename, pos_category in self.pos_files.items():
            filepath = self.pos_directory / filename
            print(f"Processing {filename}...")
            
            file_words = self.extract_words_from_file(filepath, pos_category)
            
            # Add all words from this file to the database
            # Check for duplicates across different files only
            for word, info in file_words.items():
                if word in self.word_db:
                    if self.word_db[word]['source_file'] != filepath.name:
                        print(f"Warning: Duplicate word '{word}' found in {filename} "
                              f"(previously in {self.word_db[word]['source_file']})")
                    # Don't overwrite - keep the first occurrence
                else:
                    self.word_db[word] = info
                    
        print(f"Database built: {len(self.word_db)} words extracted")
        
        # Update validator with new database
        self.validator.set_word_database(self.word_db)
        
    def lookup_word(self, word: str) -> Optional[Dict[str, str]]:
        """Look up a single word in the database."""
        return self.word_db.get(word.lower())
    
    def validate_words(self, words: List[str]) -> List[Tuple[str, bool, Optional[Dict[str, str]]]]:
        """Validate a list of words and return results."""
        results = []
        for word in words:
            word_info = self.lookup_word(word)
            exists = word_info is not None
            results.append((word, exists, word_info))
        return results
    
    def validate_sentence(self, sentence: str) -> None:
        """Validate all words in a sentence."""
        # Split sentence into words (handle basic tokenization)
        words = re.findall(r'\b[a-zA-Z]+\b', sentence)
        
        print(f"Validating sentence: '{sentence}'")
        print("=" * 50)
        
        all_valid = True
        for word in words:
            word_info = self.lookup_word(word)
            if word_info:
                pattern_info = f"[{word_info['pattern']}]" if 'pattern' in word_info else ""
                print(f"✓ {word:12} [{word_info['pos']:12}] {word_info['translation']} {pattern_info}")
            else:
                print(f"✗ {word:12} [NOT FOUND]")
                all_valid = False
                
        print("=" * 50)
        if all_valid:
            print("✓ All words are valid phi words!")
        else:
            print("✗ Some words were not found in phi vocabulary")
    
    def save_database(self, filepath: str = "phi_words.json") -> None:
        """Save the word database to a JSON file."""
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(self.word_db, file, indent=2, ensure_ascii=False)
        print(f"Database saved to {filepath}")
    
    def load_database(self, filepath: str = "phi_words.json") -> bool:
        """Load the word database from a JSON file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                self.word_db = json.load(file)
            print(f"Database loaded from {filepath}: {len(self.word_db)} words")
            
            # Update validator with loaded database
            self.validator.set_word_database(self.word_db)
            return True
        except FileNotFoundError:
            print(f"Database file {filepath} not found")
            return False
        except Exception as e:
            print(f"Error loading database: {e}")
            return False
    
    def get_pos_stats(self) -> Dict[str, int]:
        """Get statistics about words by POS category."""
        stats = {}
        for word_info in self.word_db.values():
            pos = word_info['pos']
            stats[pos] = stats.get(pos, 0) + 1
        return stats
    
    def get_pattern_stats(self) -> Dict[str, int]:
        """Get statistics about phonotactic patterns."""
        stats = {}
        for word_info in self.word_db.values():
            if 'pattern' in word_info:
                pattern = word_info['pattern']
                stats[pattern] = stats.get(pattern, 0) + 1
        return stats
    
    def search_by_translation(self, search_term: str) -> List[Tuple[str, Dict[str, str]]]:
        """Search for phi words by English translation."""
        results = []
        search_lower = search_term.lower()
        
        for phi_word, info in self.word_db.items():
            if search_lower in info['translation'].lower():
                results.append((phi_word, info))
                
        return results
    
    def search_by_pattern(self, pattern: str) -> List[Tuple[str, Dict[str, str]]]:
        """Search for phi words by phonotactic pattern."""
        results = []
        
        for phi_word, info in self.word_db.items():
            if 'pattern' in info and info['pattern'] == pattern.upper():
                results.append((phi_word, info))
                
        return results
    
    def get_expected_pattern_for_pos(self, pos: str) -> str:
        """Get the expected phonotactic pattern for a given POS."""
        patterns = {
            'noun': ['CVFP', 'CPFP', 'FVFP', 'FPFP'],  # Corrected based on [C/F][V/P][F][P]
            'verb': ['FVCV'],  # digraph + vowel + consonant + vowel
            'adjective': ['CVFV'],  # consonant + vowel + digraph + vowel
            'adverb': ['CVCVCV'],  # three syllables, no digraphs
            'preposition': ['FP'],  # digraph + vowel pair
            'determiner': ['FPCV'],  # digraph + vowel pair + consonant + vowel
            'classifier': ['CP'],  # consonant + vowel pair
            'conjunction': ['CVCV'],  # consonant + vowel + consonant + vowel
            'interjection': ['CVCP'],  # consonant + vowel + consonant + vowel pair
            'number': ['FV', 'FVFV'],  # digit or magnitude patterns
            'particle': ['CV'],  # consonant + vowel
            'pronoun': ['CP', 'FV']  # special cases like mia, thi, sha
        }
        return patterns.get(pos, [])
    
    def validate_word_for_pos(self, word: str, pos: str) -> Tuple[bool, str]:
        """Validate that a word follows the correct pattern for its POS."""
        if not self._is_valid_phi_word(word):
            return False, "Contains invalid characters"
        
        pattern = self._analyze_phonotactic_pattern(word)
        expected_patterns = self.get_expected_pattern_for_pos(pos)
        
        if not expected_patterns:
            return False, f"Unknown POS: {pos}"
        
        if pattern in expected_patterns:
            return True, f"Valid {pos} pattern: {pattern}"
        else:
            return False, f"Invalid pattern {pattern} for {pos}. Expected: {', '.join(expected_patterns)}"
    
    def add_word_to_lexicon(self, phi_word: str, translation: str, pos: str, category: str = None) -> bool:
        """Add a new word to the phi lexicon."""
        # Validate the word
        is_valid, message = self.validate_word_for_pos(phi_word, pos)
        if not is_valid:
            print(f"Cannot add word '{phi_word}': {message}")
            return False
        
        # Check if word already exists
        if self.lookup_word(phi_word):
            print(f"Word '{phi_word}' already exists in the lexicon")
            return False
        
        # Determine target file
        filename = None
        for file, file_pos in self.pos_files.items():
            if file_pos == pos:
                filename = file
                break
        
        if not filename:
            print(f"Unknown POS: {pos}. Valid options: {', '.join(set(self.pos_files.values()))}")
            return False
        
        filepath = self.pos_directory / filename
        
        # If no category specified, try to infer or ask
        if not category:
            category = self._suggest_category_for_word(pos, translation)
            if not category:
                category = "miscellaneous"
        
        # Add word to file
        success = self._insert_word_into_file(filepath, phi_word, translation, category)
        
        if success:
            print(f"Successfully added '{phi_word}' ({translation}) as {pos} to {filename}")
            # Rebuild database to include new word
            self.build_database()
            return True
        else:
            print(f"Failed to add word to {filename}")
            return False
    
    def _suggest_category_for_word(self, pos: str, translation: str) -> str:
        """Suggest a semantic category based on translation keywords."""
        # Simple keyword-based categorization
        translation_lower = translation.lower()
        
        if pos == 'noun':
            if any(word in translation_lower for word in ['person', 'man', 'woman', 'child', 'people']):
                return 'essential people and relationships'
            elif any(word in translation_lower for word in ['house', 'building', 'place', 'room']):
                return 'essential places and landforms'
            elif any(word in translation_lower for word in ['water', 'fire', 'earth', 'air', 'weather']):
                return 'essential natural phenomena'
            elif any(word in translation_lower for word in ['book', 'tool', 'object', 'thing']):
                return 'essential objects and tools'
        elif pos == 'verb':
            if any(word in translation_lower for word in ['see', 'hear', 'feel', 'smell', 'taste']):
                return 'essential perception verbs'
            elif any(word in translation_lower for word in ['go', 'come', 'walk', 'run', 'move']):
                return 'essential motion verbs'
            elif any(word in translation_lower for word in ['make', 'create', 'build', 'change']):
                return 'essential creation and change verbs'
            elif any(word in translation_lower for word in ['think', 'know', 'learn', 'understand']):
                return 'essential social verbs'
        elif pos == 'adjective':
            if any(word in translation_lower for word in ['red', 'blue', 'green', 'yellow', 'black', 'white', 'color']):
                return 'essential colors'
            elif any(word in translation_lower for word in ['good', 'bad', 'beautiful', 'ugly']):
                return 'essential evaluative'
            elif any(word in translation_lower for word in ['big', 'small', 'large', 'tiny', 'size']):
                return 'essential size and dimension'
            elif any(word in translation_lower for word in ['happy', 'sad', 'angry', 'emotion']):
                return 'essential emotional and personality'
        
        return None
    
    def _insert_word_into_file(self, filepath: Path, phi_word: str, translation: str, category: str) -> bool:
        """Insert a new word into the appropriate markdown file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            
            # Find the best place to insert the word
            insert_line = self._find_insertion_point(lines, category)
            
            if insert_line is None:
                # Create new category section
                insert_line = self._create_new_category_section(lines, category)
            
            # Create the new word entry
            new_entry = f"| {phi_word} | {translation} |\n"
            
            # Insert the new entry
            lines.insert(insert_line, new_entry)
            
            # Write back to file
            with open(filepath, 'w', encoding='utf-8') as file:
                file.writelines(lines)
            
            return True
            
        except Exception as e:
            print(f"Error inserting word into {filepath}: {e}")
            return False
    
    def _find_insertion_point(self, lines: List[str], target_category: str) -> Optional[int]:
        """Find the best line to insert a new word in the given category."""
        category_start = None
        table_end = None
        
        for i, line in enumerate(lines):
            # Look for category heading
            if line.strip().startswith('#') and target_category.lower() in line.lower():
                category_start = i
                continue
            
            # If we found our category, look for the table
            if category_start is not None:
                # Look for table header
                if line.strip().startswith('| phi word |'):
                    # Find end of this table
                    j = i + 2  # Skip header and separator
                    while j < len(lines) and lines[j].strip().startswith('|') and '---' not in lines[j]:
                        j += 1
                    table_end = j
                    break
        
        return table_end
    
    def _create_new_category_section(self, lines: List[str], category: str) -> int:
        """Create a new category section and return insertion point."""
        # Find a good place to add the new section (before conclusion/end)
        insert_point = len(lines) - 1
        
        # Look for conclusion or similar ending sections
        for i in range(len(lines) - 1, -1, -1):
            if any(keyword in lines[i].lower() for keyword in ['conclusion', 'remaining', '##']):
                insert_point = i
                break
        
        # Add new category section
        new_section = [
            f"\n## {category}\n\n",
            "| phi word | english translation |\n",
            "| -------- | ------------------- |\n"
        ]
        
        for line in reversed(new_section):
            lines.insert(insert_point, line)
        
        return insert_point + len(new_section)

    def extract_non_lexicon_words_from_file(self, filepath: Path) -> List[Tuple[str, bool, Optional[Dict[str, str]]]]:
        """Extract phi words from a file, excluding official lexicon tables."""
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
        except FileNotFoundError:
            print(f"Warning: File {filepath} not found")
            return []
        except Exception as e:
            print(f"Error reading {filepath}: {e}")
            return []
        
        # Remove official lexicon tables
        cleaned_content = self._remove_lexicon_tables(content)
        
        # Extract potential phi words from remaining text
        potential_words = self._extract_potential_phi_words(cleaned_content)
        
        # Validate each word
        results = []
        for word in sorted(set(potential_words)):  # Remove duplicates and sort
            word_info = self.lookup_word(word)
            exists = word_info is not None
            results.append((word, exists, word_info))
        
        return results
    
    def _remove_lexicon_tables(self, content: str) -> str:
        """Remove tables with the official lexicon header from content."""
        lines = content.split('\n')
        cleaned_lines = []
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Check if this is an official lexicon table header
            if (line.startswith('| phi word |') and 'english translation' in line and line.endswith('|')):
                # Skip this line and the separator line if it exists
                i += 1
                if i < len(lines) and lines[i].strip().startswith('|') and '---' in lines[i]:
                    i += 1
                
                # Skip all table rows until we hit a non-table line
                while i < len(lines):
                    line = lines[i].strip()
                    if (not line or 
                        line.startswith('#') or 
                        not line.startswith('|') or
                        ('---' in line and line.startswith('|'))):
                        break
                    i += 1
                continue
            else:
                cleaned_lines.append(lines[i])
                i += 1
        
        return '\n'.join(cleaned_lines)
    
    def _extract_potential_phi_words(self, text: str) -> List[str]:
        """Extract potential phi words from text using targeted patterns."""
        potential_words = []
        
        # Pattern 1: Words in backticks (most reliable indicator of phi words)
        backtick_words = re.findall(r'`([a-z]{2,})`', text)
        potential_words.extend(backtick_words)
        
        # Pattern 2: Words followed by translation glosses in parentheses
        # e.g., "mipho (blue)" or "hashe (green)"
        gloss_pattern = r'([a-z]{2,})\s*\([^)]*\)'
        gloss_words = re.findall(gloss_pattern, text.lower())
        potential_words.extend(gloss_words)
        
        # Pattern 3: Words in "examples:" contexts
        examples_sections = re.findall(r'examples?[:\s]+([^.!?]*)', text.lower(), re.IGNORECASE)
        for section in examples_sections:
            # Extract phi-like words from examples sections
            example_words = re.findall(r'\b([a-z]{2,})\b', section)
            for word in example_words:
                if self._has_phi_characteristics(word):
                    potential_words.append(word)
        
        # Pattern 4: Words that strongly match phi phonotactic patterns
        # Only include if they have clear phi structure
        text_words = re.findall(r'\b([a-z]{2,})\b', text.lower())
        for word in text_words:
            if (self._has_strong_phi_pattern(word) and 
                not self._is_common_english_word(word)):
                potential_words.append(word)
        
        return potential_words
    
    def _has_phi_characteristics(self, word: str) -> bool:
        """Check if word has strong phi characteristics."""
        if len(word) < 2:
            return False
            
        # Must contain only valid phi characters
        if not all(c in 'aeiouhlmnprstwph' for c in word):
            return False
            
        # Must have at least one vowel
        if not any(c in 'aeiou' for c in word):
            return False
            
        # Exclude obvious English words
        if self._is_common_english_word(word):
            return False
            
        return True
    
    def _has_strong_phi_pattern(self, word: str) -> bool:
        """Check if word strongly matches expected phi phonotactic patterns."""
        if not self._has_phi_characteristics(word):
            return False
            
        pattern = self._analyze_phonotactic_pattern(word)
        
        # Expected phi patterns by POS
        phi_patterns = {
            'CVFV',    # adjective
            'FVCV',    # verb  
            'CVFP', 'CPFP', 'FVFP', 'FPFP',  # noun
            'CVCVCV',  # adverb
            'FP',      # preposition
            'FPCV',    # determiner
            'CP',      # classifier
            'CVCV',    # conjunction
            'CVCP',    # interjection
            'FV', 'FVFV',  # number
            'CV'       # particle
        }
        
        return pattern in phi_patterns
    
    def _is_common_english_word(self, word: str) -> bool:
        """Check if word is a common English word (expanded list)."""
        english_words = {
            # Common articles, prepositions, conjunctions
            'the', 'and', 'are', 'for', 'not', 'but', 'can', 'may', 'has', 'was',
            'were', 'been', 'have', 'will', 'with', 'from', 'they', 'them', 'this',
            'that', 'what', 'when', 'where', 'who', 'how', 'why', 'than', 'then',
            'each', 'some', 'more', 'most', 'many', 'much', 'such', 'very', 'well',
            'also', 'just', 'only', 'even', 'now', 'here', 'there', 'where',
            'first', 'last', 'next', 'new', 'old', 'good', 'great', 'small',
            'large', 'high', 'low', 'long', 'short', 'early', 'late', 'right',
            'left', 'few', 'several', 'both', 'either', 'neither', 'all', 'any',
            'other', 'another', 'same', 'different', 'own', 'way', 'part', 'use',
            'work', 'life', 'time', 'year', 'day', 'week', 'month', 'number',
            'people', 'person', 'man', 'woman', 'child', 'place', 'home', 'house',
            'room', 'world', 'country', 'state', 'city', 'town', 'name', 'word',
            'language', 'english', 'structure', 'pattern', 'example', 'system',
            # Additional documentation words
            'allows', 'appear', 'apparent', 'assessment', 'assessments', 
            'eliminates', 'emotional', 'emotions', 'essential', 'essentials',
            'helps', 'human', 'interpretation', 'into', 'items', 'its',
            'listeners', 'maintains', 'material', 'minimal', 'natural',
            'notes', 'nouns', 'oppositions', 'parts', 'patterns', 'per',
            'positions', 'properties', 'rather', 'remain', 'sensation',
            'separate', 'shape', 'shapes', 'show', 'shows', 'situation',
            'start', 'states', 'stone', 'taste', 'temporal', 'terms', 'their',
            'these', 'total', 'traits', 'tree', 'two', 'while', 'without',
            # Linguistic terminology
            'adjective', 'adjectives', 'noun', 'verb', 'verbs', 'particle',
            'particles', 'phonetic', 'phonetics', 'syntax', 'semantic',
            'morphology', 'grammar', 'grammatical', 'linguistic', 'linguistics',
            # Category and technical terms
            'basic', 'colors', 'consonant', 'digraph', 'domains', 'evaluative',
            'no', 'one', 'personality', 'qualities', 'sensation', 'shapes', 
            'sov', 'state', 'temporal', 'terms', 'vowel', 'fricative'
        }
        
        return word.lower() in english_words

    def validate_file_words(self, filepath: str) -> None:
        """Validate all non-lexicon phi words in a file and report results."""
        file_path = Path(filepath)
        
        print(f"Validating phi words in: {filepath}")
        print("=" * 60)
        print("(Excluding official lexicon tables)")
        print()
        
        results = self.extract_non_lexicon_words_from_file(file_path)
        
        if not results:
            print("No potential phi words found outside lexicon tables.")
            return
        
        valid_words = []
        invalid_words = []
        
        for word, exists, word_info in results:
            if exists:
                valid_words.append((word, word_info))
            else:
                invalid_words.append(word)
        
        # Report valid words
        if valid_words:
            print(f"✓ VALID WORDS ({len(valid_words)}):")
            print("-" * 40)
            for word, info in valid_words:
                pattern = info.get('pattern', '?')
                category = info.get('category', 'unknown')
                print(f"  {word:12} [{info['pos']:12}] {info['translation']} [{pattern}] ({category})")
            print()
        
        # Report invalid words
        if invalid_words:
            print(f"✗ INVALID WORDS ({len(invalid_words)}):")
            print("-" * 40)
            for word in invalid_words:
                print(f"  {word:12} [NOT FOUND IN LEXICON]")
            print()
        
        # Summary
        total = len(results)
        valid_count = len(valid_words)
        invalid_count = len(invalid_words)
        
        print("SUMMARY:")
        print("-" * 20)
        print(f"Total words found: {total}")
        print(f"Valid words: {valid_count}")
        print(f"Invalid words: {invalid_count}")
        
        if invalid_count == 0:
            print("✓ All phi words are valid!")
        else:
            print(f"✗ {invalid_count} invalid words need attention")

    def comprehensive_validate_file(self, filepath: str) -> None:
        """Perform comprehensive validation of a phi documentation file."""
        print(f"COMPREHENSIVE VALIDATION: {filepath}")
        print("=" * 80)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
        except FileNotFoundError:
            print(f"❌ File not found: {filepath}")
            return
        
        # 1. Lexicon Accuracy Check
        print("1. LEXICON ACCURACY")
        print("-" * 40)
        self.validate_file_words(filepath)
        
        # 2. SOV Compliance & Glossing Format Check
        print("\n2. SOV COMPLIANCE & GLOSSING FORMAT")
        print("-" * 40)
        code_blocks = self.validator.extract_code_blocks(content)
        
        # Initialize issue counters
        sov_issues = 0
        glossing_issues = 0
        
        if not code_blocks:
            print("✅ No code blocks found - SOV check not applicable")
        else:
            for i, (block, line_num) in enumerate(code_blocks):
                is_valid, issues = self.validator.validate_glossing_format(block)
                
                if is_valid:
                    print(f"✅ Code block {i+1} (line {line_num}): Valid format and SOV")
                else:
                    print(f"❌ Code block {i+1} (line {line_num}): Issues found:")
                    for issue in issues:
                        print(f"   - {issue}")
                        if "SOV" in issue:
                            sov_issues += 1
                        else:
                            glossing_issues += 1
            
            print(f"\nSOV Issues: {sov_issues}, Glossing Issues: {glossing_issues}")
        
        # 3. Phonotactic Compliance Check  
        print("\n3. PHONOTACTIC COMPLIANCE")
        print("-" * 40)
        
        # Extract phi words from lexicon tables
        phi_words_in_file = self._extract_lexicon_words(content)
        phonotactic_issues = 0
        
        for word, expected_pos in phi_words_in_file:
            is_valid, message = self.validator.validate_phonotactic_compliance(word, expected_pos)
            if not is_valid:
                print(f"❌ {word}: {message}")
                phonotactic_issues += 1
        
        if phonotactic_issues == 0:
            print(f"✅ All {len(phi_words_in_file)} lexicon words follow correct phonotactic patterns")
        else:
            print(f"❌ {phonotactic_issues}/{len(phi_words_in_file)} words have phonotactic issues")
        
        # 4. Overall Summary
        print("\n4. VALIDATION SUMMARY")
        print("-" * 40)
        
        total_issues = sov_issues + glossing_issues + phonotactic_issues
        if total_issues == 0:
            print("🎉 FILE FULLY VALIDATED - All checks passed!")
        else:
            print(f"⚠️  FILE NEEDS ATTENTION - {total_issues} total issues found")
            print("   Please fix issues before marking as 'validated'")
    
    def _extract_lexicon_words(self, content: str) -> List[Tuple[str, str]]:
        """Extract phi words from official lexicon tables in a file."""
        words = []
        lines = content.split('\n')
        current_pos = "unknown"
        
        # Get the filepath being processed (if available) from pos_files mapping
        # This is more reliable than trying to guess from content
        first_lines = '\n'.join(lines[:5]).lower()
        
        # Try exact filename matching first
        for filename, pos in self.pos_files.items():
            pos_name = filename.replace('.md', '')
            if first_lines.startswith(f'# {pos_name}'):
                current_pos = pos
                break
        
        # If no exact match, try partial matches for compound filenames
        if current_pos == "unknown":
            for filename, pos in self.pos_files.items():
                # Handle cases like "objects-overhaul.md" with header "# objects"
                if '/' in filename:  # It's in a subdirectory
                    base_name = filename.split('/')[-1].replace('.md', '')
                    # Try the base word (e.g., "objects" from "objects-overhaul")
                    base_word = base_name.split('-')[0]
                    if first_lines.startswith(f'# {base_word}'):
                        current_pos = pos
                        break
                else:
                    # Try the base word for root-level files too
                    base_name = filename.replace('.md', '')
                    base_word = base_name.split('-')[0]
                    if first_lines.startswith(f'# {base_word}'):
                        current_pos = pos
                        break
        
        # If still no match, try content-based detection with specific patterns
        if current_pos == "unknown":
            if 'gloss abbreviations' in content.lower() and '| gloss | meaning | phi particle |' in content:
                current_pos = 'particle'
            elif 'essential digits' in content.lower() and '| phi word | english translation | value |' in content:
                current_pos = 'number'
            elif 'categorize nouns' in content.lower() and 'CL.' in content:
                current_pos = 'classifier'
            else:
                # Fallback to general content matching
                for filename, pos in self.pos_files.items():
                    pos_name = filename.replace('.md', '')
                    if pos_name in content.lower():
                        current_pos = pos
                        break
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Look for official lexicon table headers
            if (line.startswith('| phi word |') and 'english translation' in line):
                # Skip header and separator
                i += 2
                
                # Extract words from table
                while i < len(lines):
                    line = lines[i].strip()
                    if not line.startswith('|') or '---' in line or not line:
                        break
                    
                    match = re.match(r'\|\s*([a-z]{2,})\s*\|\s*([^|]+?)\s*\|', line)
                    if match:
                        phi_word = match.group(1).strip()
                        words.append((phi_word, current_pos))
                    
                    i += 1
            else:
                i += 1
        
        return words

def main():
    parser = argparse.ArgumentParser(description='Phi Word Lookup Utility')
    parser.add_argument('words', nargs='*', help='Words to look up')
    parser.add_argument('--extract', action='store_true', 
                        help='Extract all words from POS files')
    parser.add_argument('--validate', type=str, 
                        help='Validate all words in a sentence')
    parser.add_argument('--validate-file', type=str,
                        help='Validate phi words in a file (excluding lexicon tables)')
    parser.add_argument('--comprehensive-validate-file', type=str,
                        help='Perform comprehensive validation of a phi documentation file')
    parser.add_argument('--stats', action='store_true',
                        help='Show database statistics')
    parser.add_argument('--show-files', action='store_true',
                        help='Show all discovered POS files')
    parser.add_argument('--patterns', action='store_true',
                        help='Show phonotactic pattern statistics')
    parser.add_argument('--search', type=str,
                        help='Search for words by English translation')
    parser.add_argument('--pattern', type=str,
                        help='Search for words by phonotactic pattern (e.g., FVCV)')
    parser.add_argument('--add-word', nargs=3, metavar=('PHI_WORD', 'TRANSLATION', 'POS'),
                        help='Add new word to lexicon: phi_word translation pos')
    parser.add_argument('--category', type=str,
                        help='Semantic category for new word (used with --add-word)')
    parser.add_argument('--pos-dir', type=str, default='../source/pos',
                        help='Path to POS directory (default: ../source/pos)')
    
    args = parser.parse_args()
    
    # Initialize database
    db = PhiWordDatabase(args.pos_dir)
    
    # Always build database from source files (no caching)
    print("Building database from source files...")
    db.build_database()
    
    # Handle different operations
    if args.extract:
        print("Re-extracting words from POS files...")
        db.build_database()
        
    elif args.validate:
        db.validate_sentence(args.validate)
        
    elif args.validate_file:
        db.validate_file_words(args.validate_file)
        
    elif args.comprehensive_validate_file:
        db.comprehensive_validate_file(args.comprehensive_validate_file)
        
    elif args.stats:
        stats = db.get_pos_stats()
        print("\nPhi Word Database Statistics:")
        print("=" * 30)
        total = 0
        for pos, count in sorted(stats.items()):
            print(f"{pos:12}: {count:4} words")
            total += count
        print("-" * 30)
        print(f"{'TOTAL':12}: {total:4} words")
        
        if args.show_files:
            db.show_discovered_files()
        
    elif args.patterns:
        stats = db.get_pattern_stats()
        print("\nPhonOtactic Pattern Statistics:")
        print("=" * 40)
        for pattern, count in sorted(stats.items(), key=lambda x: x[1], reverse=True):
            print(f"{pattern:8}: {count:4} words")
            
    elif args.pattern:
        results = db.search_by_pattern(args.pattern)
        if results:
            print(f"\nFound {len(results)} words with pattern '{args.pattern.upper()}':")
            print("=" * 50)
            for phi_word, info in results:
                category = info.get('category', 'unknown')
                print(f"{phi_word:12} [{info['pos']:12}] {info['translation']} ({category})")
        else:
            print(f"No words found with pattern '{args.pattern.upper()}'")
        
    elif args.search:
        results = db.search_by_translation(args.search)
        if results:
            print(f"\nFound {len(results)} words containing '{args.search}':")
            print("=" * 50)
            for phi_word, info in results:
                pattern_info = f"[{info.get('pattern', '?')}]" if 'pattern' in info else ""
                category = info.get('category', 'unknown')
                print(f"{phi_word:12} [{info['pos']:12}] {info['translation']} {pattern_info} ({category})")
        else:
            print(f"No words found containing '{args.search}'")
            
    elif args.add_word:
        phi_word, translation, pos = args.add_word
        category = args.category
        db.add_word_to_lexicon(phi_word, translation, pos, category)
        
    elif args.words:
        # Look up individual words
        print("Word Lookup Results:")
        print("=" * 70)
        for word in args.words:
            word_info = db.lookup_word(word)
            if word_info:
                pattern = word_info.get('pattern', '?')
                syllables = word_info.get('syllables', '?')
                category = word_info.get('category', 'unknown')
                digraphs = ', '.join(word_info.get('digraphs', [])) or 'none'
                vowel_pairs = ', '.join(word_info.get('vowel_pairs', [])) or 'none'
                
                print(f"✓ {word:12} [{word_info['pos']:12}] {word_info['translation']}")
                print(f"  Pattern: {pattern} | Syllables: {syllables} | Digraphs: {digraphs} | Vowel Pairs: {vowel_pairs}")
                print(f"  Category: {category}")
                print()
            else:
                print(f"✗ {word:12} [NOT FOUND]")
                print()
                
    else:
        # Interactive mode
        print("Phi Word Lookup Utility - Interactive Mode")
        print("Type words to look up, 'quit' to exit")
        print("Prefix with 's:' to search translations (e.g., 's:water')")
        print("Prefix with 'p:' to search patterns (e.g., 'p:FVCV')")
        print("=" * 70)
        
        while True:
            try:
                user_input = input("\nLookup: ").strip()
                if user_input.lower() in ['quit', 'exit', 'q']:
                    break
                    
                if user_input.startswith('s:'):
                    # Search mode
                    search_term = user_input[2:].strip()
                    results = db.search_by_translation(search_term)
                    if results:
                        print(f"Found {len(results)} matches:")
                        for phi_word, info in results[:10]:  # Limit to 10 results
                            pattern = info.get('pattern', '?')
                            category = info.get('category', 'unknown')
                            print(f"  {phi_word:12} [{info['pos']:12}] {info['translation']} [{pattern}] ({category})")
                        if len(results) > 10:
                            print(f"  ... and {len(results) - 10} more")
                    else:
                        print(f"No words found containing '{search_term}'")
                        
                elif user_input.startswith('p:'):
                    # Pattern search mode
                    pattern = user_input[2:].strip()
                    results = db.search_by_pattern(pattern)
                    if results:
                        print(f"Found {len(results)} words with pattern '{pattern.upper()}':")
                        for phi_word, info in results[:10]:  # Limit to 10 results
                            category = info.get('category', 'unknown')
                            print(f"  {phi_word:12} [{info['pos']:12}] {info['translation']} ({category})")
                        if len(results) > 10:
                            print(f"  ... and {len(results) - 10} more")
                    else:
                        print(f"No words found with pattern '{pattern.upper()}'")
                        
                else:
                    # Regular lookup
                    words = user_input.split()
                    for word in words:
                        word_info = db.lookup_word(word)
                        if word_info:
                            pattern = word_info.get('pattern', '?')
                            syllables = word_info.get('syllables', '?')
                            category = word_info.get('category', 'unknown')
                            digraphs = ', '.join(word_info.get('digraphs', [])) or 'none'
                            vowel_pairs = ', '.join(word_info.get('vowel_pairs', [])) or 'none'
                            print(f"✓ {word:12} [{word_info['pos']:12}] {word_info['translation']} [{pattern}] ({category})")
                            print(f"  Digraphs: {digraphs} | Vowel Pairs: {vowel_pairs}")
                        else:
                            print(f"✗ {word:12} [NOT FOUND]")
                            
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break

if __name__ == "__main__":
    main() 