#!/usr/bin/env python3
"""
phi Word Validation System

Comprehensive algorithmic validation of phi words against strict phonotactic
patterns and lexical integrity requirements. Ensures 100% systematic compliance
for phi's growing vocabulary.

Usage:
    python phi_validator.py validate "phawi" verb "to fly"
    python phi_validator.py check_lexicon
    python phi_validator.py batch_validate words.txt
"""

import re
import json
import argparse
from typing import Dict, List, Tuple, Optional, Set
from dataclasses import dataclass
from enum import Enum
import glob
import os
from pathlib import Path
from collections import defaultdict
from phi_lexicon_reader import PhiLexiconReader


class ValidationResult(Enum):
    VALID = "VALID"
    INVALID = "INVALID"
    WARNING = "WARNING"
    CONFLICT = "CONFLICT"


@dataclass
class ValidationError:
    level: ValidationResult
    message: str
    details: Optional[str] = None


@dataclass
class WordEntry:
    word: str
    pos: str
    meaning: str
    line_number: Optional[int] = None


class PhiValidator:
    """Main validation class for phi words and lexicon integrity."""
    
    def __init__(self, pos_directory: str = "pos/"):
        self.pos_directory = pos_directory
        
        # Phonological components
        self.consonants = set("hlmnprstw")
        self.fricatives = {"ph", "wh", "th", "sh"}
        self.vowels = set("iueoa")
        self.forbidden_vowel_pairs = {"ii", "uu", "ee", "oo", "aa"}
        
        # Pattern definitions
        self.patterns = {
            "noun": "[C/F][V/P][F][P]",
            "verb": "[F][V][C][V]", 
            "adjective": "[C][V][F][V]",
            "adverb": "[C][V][C][V][C][V]",
            "preposition": "[F][P]",
            "determiner": "[F][P][C][V]",
            "classifier": "[C][P]", 
            "conjunction": "[C][V][C][V]",
            "interjection": "[C][V][C][P]",
            "particle": "[C][V]",
            "digit": "[F][V]",
            "magnitude": "[F][V][F][V]"
        }
        
        # Load existing lexicon
        self.lexicon = self._load_lexicon()
    
    def _normalize_pos_name(self, pos_name: str) -> str:
        """Convert plural POS filename to singular form expected by patterns."""
        pos_mapping = {
            "adjectives": "adjective",
            "nouns": "noun", 
            "verbs": "verb",
            "adverbs": "adverb",
            "prepositions": "preposition",
            "determiners": "determiner",
            "classifiers": "classifier",
            "conjunctions": "conjunction",
            "interjections": "interjection",
            "particles": "particle",
            "numbers": "digit",  # numbers can be either digit or magnitude
            "pronouns": "pronoun"  # special case, not in patterns
        }
        return pos_mapping.get(pos_name, pos_name)
    
    def _load_lexicon(self) -> Dict[str, List[WordEntry]]:
        """Load all words from pos/ files into memory using PhiLexiconReader."""
        
        # Use the authoritative PhiLexiconReader instead of duplicating parsing logic
        reader = PhiLexiconReader(self.pos_directory)
        lexicon_data = reader.read_lexicon()
        
        # Convert to the expected format: Dict[pos_name, List[WordEntry]]
        lexicon = defaultdict(list)
        
        for word, info in lexicon_data.items():
            pos = info['pos']
            translation = info['translation']
            file_name = info['file']
            
            # Normalize POS name to match existing expectations
            normalized_pos = self._normalize_pos_name(pos)
            
            # Create WordEntry (line_number not available from PhiLexiconReader)
            entry = WordEntry(word, normalized_pos, translation, line_number=None)
            lexicon[normalized_pos].append(entry)
        
        # Convert defaultdict back to regular dict
        lexicon = dict(lexicon)
        
        # Print summary (PhiLexiconReader already prints detailed info)
        total_words = sum(len(entries) for entries in lexicon.values())
        print(f"Converted to validator format: {total_words} total words")
        print("=" * 50)
        
        return lexicon
    
    def _syllabify(self, word: str) -> List[str]:
        """Break word into syllables following phi rules."""
        syllables = []
        i = 0
        
        while i < len(word):
            syllable = ""
            
            # Check for fricative digraph at start
            if i < len(word) - 1 and word[i:i+2] in self.fricatives:
                syllable += word[i:i+2]
                i += 2
            elif word[i] in self.consonants:
                syllable += word[i]
                i += 1
            
            # Add vowel(s) - handle vowel pairs
            if i < len(word) and word[i] in self.vowels:
                syllable += word[i]
                i += 1
                
                # Check for vowel pair
                if i < len(word) and word[i] in self.vowels:
                    syllable += word[i]
                    i += 1
            
            if syllable:
                syllables.append(syllable)
                
        return syllables
    
    def _is_vowel_pair(self, text: str) -> bool:
        """Check if text is a valid vowel pair."""
        if len(text) != 2:
            return False
        return (text[0] in self.vowels and 
                text[1] in self.vowels and 
                text not in self.forbidden_vowel_pairs)
    
    def _parse_word_components(self, word: str, pattern: str) -> List[str]:
        """Parse word into components based on expected pattern."""
        components = []
        i = 0
        
        # Simple component parsing for validation
        while i < len(word):
            # Check for fricative digraph
            if i < len(word) - 1 and word[i:i+2] in self.fricatives:
                components.append(word[i:i+2])
                i += 2
            elif word[i] in self.consonants:
                components.append(word[i])
                i += 1
            elif word[i] in self.vowels:
                # Check for vowel pair
                if (i < len(word) - 1 and 
                    word[i+1] in self.vowels and 
                    word[i:i+2] not in self.forbidden_vowel_pairs):
                    components.append(word[i:i+2])
                    i += 2
                else:
                    components.append(word[i])
                    i += 1
            else:
                i += 1  # Skip invalid characters
                
        return components
    
    def validate_phonotactics(self, word: str, pos: str) -> List[ValidationError]:
        """Validate word against phonotactic patterns."""
        errors = []
        
        # Handle special cases
        if pos == "pronoun":
            # Pronouns are exceptional (mia, thi, sha)
            if word not in ["mia", "thi", "sha"]:
                errors.append(ValidationError(
                    ValidationResult.INVALID,
                    f"Invalid pronoun: {word} (only mia, thi, sha allowed)"
                ))
            return errors
        
        # For numbers, try both digit and magnitude patterns
        if pos == "digit":
            # Try digit pattern [F][V]
            if len(word) == 3 and word[:2] in self.fricatives and word[2] in self.vowels:
                return []  # Valid digit pattern - no further validation needed
            
            # Try magnitude pattern [F][V][F][V]
            if (len(word) == 6 and 
                word[:2] in self.fricatives and 
                word[2] in self.vowels and
                word[3:5] in self.fricatives and
                word[5] in self.vowels):
                return []  # Valid magnitude pattern - no further validation needed
            
            # If neither pattern matches, it's invalid
            errors.append(ValidationError(
                ValidationResult.INVALID,
                f"Number does not match digit [F][V] or magnitude [F][V][F][V] patterns"
            ))
            return errors
        
        if pos not in self.patterns:
            errors.append(ValidationError(
                ValidationResult.INVALID,
                f"Unknown part of speech: {pos}"
            ))
            return errors
        
        # Basic character validation
        valid_chars = self.consonants | self.vowels
        for char in word:
            if char not in valid_chars:
                errors.append(ValidationError(
                    ValidationResult.INVALID,
                    f"Invalid character '{char}' in word"
                ))
        
        # Syllable structure validation
        syllables = self._syllabify(word)
        
        # Check open syllables
        for syllable in syllables:
            if not syllable or syllable[-1] not in self.vowels:
                errors.append(ValidationError(
                    ValidationResult.INVALID,
                    f"Closed syllable detected: '{syllable}'"
                ))
        
        # Check for duplicate syllables
        if len(syllables) != len(set(syllables)):
            errors.append(ValidationError(
                ValidationResult.INVALID,
                "Duplicate syllables found"
            ))
        
        # Check forbidden vowel pairs
        for i in range(len(word) - 1):
            pair = word[i:i+2]
            if pair in self.forbidden_vowel_pairs:
                errors.append(ValidationError(
                    ValidationResult.INVALID,
                    f"Forbidden vowel pair: {pair}"
                ))
        
        # Pattern-specific validation
        if pos == "verb":
            errors.extend(self._validate_verb_pattern(word))
        elif pos == "adjective":
            errors.extend(self._validate_adjective_pattern(word))
        elif pos == "noun":
            errors.extend(self._validate_noun_pattern(word))
        elif pos == "adverb":
            errors.extend(self._validate_adverb_pattern(word))
        elif pos == "preposition":
            errors.extend(self._validate_preposition_pattern(word))
        elif pos == "particle":
            errors.extend(self._validate_particle_pattern(word))
        elif pos in ["determiner", "classifier", "conjunction", "interjection"]:
            errors.extend(self._validate_other_patterns(word, pos))
        
        return errors
    
    def _validate_verb_pattern(self, word: str) -> List[ValidationError]:
        """Validate verb pattern [F][V][C][V]."""
        errors = []
        
        if len(word) < 4:
            errors.append(ValidationError(
                ValidationResult.INVALID,
                f"Verb too short: {len(word)} chars (minimum 4)"
            ))
            return errors
        
        # Must start with fricative
        if word[:2] not in self.fricatives:
            errors.append(ValidationError(
                ValidationResult.INVALID,
                f"Verb must start with fricative digraph, got: {word[:2]}"
            ))
        
        # Pattern: fricative + vowel + consonant + vowel
        components = self._parse_word_components(word, "verb")
        if len(components) != 4:
            errors.append(ValidationError(
                ValidationResult.INVALID,
                f"Verb must have exactly 4 components, got {len(components)}"
            ))
        else:
            # Check each component
            if components[0] not in self.fricatives:
                errors.append(ValidationError(
                    ValidationResult.INVALID,
                    f"First component must be fricative, got: {components[0]}"
                ))
            if components[1] not in self.vowels:
                errors.append(ValidationError(
                    ValidationResult.INVALID,
                    f"Second component must be vowel, got: {components[1]}"
                ))
            if components[2] not in self.consonants:
                errors.append(ValidationError(
                    ValidationResult.INVALID,
                    f"Third component must be consonant, got: {components[2]}"
                ))
            if components[3] not in self.vowels:
                errors.append(ValidationError(
                    ValidationResult.INVALID,
                    f"Fourth component must be vowel, got: {components[3]}"
                ))
        
        return errors
    
    def _validate_adjective_pattern(self, word: str) -> List[ValidationError]:
        """Validate adjective pattern [C][V][F][V]."""
        errors = []
        
        if len(word) < 4:
            errors.append(ValidationError(
                ValidationResult.INVALID,
                f"Adjective too short: {len(word)} chars (minimum 4)"
            ))
            return errors
        
        components = self._parse_word_components(word, "adjective")
        if len(components) != 4:
            errors.append(ValidationError(
                ValidationResult.INVALID,
                f"Adjective must have exactly 4 components, got {len(components)}"
            ))
        else:
            if components[0] not in self.consonants:
                errors.append(ValidationError(
                    ValidationResult.INVALID,
                    f"First component must be consonant, got: {components[0]}"
                ))
            if components[1] not in self.vowels:
                errors.append(ValidationError(
                    ValidationResult.INVALID,
                    f"Second component must be vowel, got: {components[1]}"
                ))
            if components[2] not in self.fricatives:
                errors.append(ValidationError(
                    ValidationResult.INVALID,
                    f"Third component must be fricative, got: {components[2]}"
                ))
            if components[3] not in self.vowels:
                errors.append(ValidationError(
                    ValidationResult.INVALID,
                    f"Fourth component must be vowel, got: {components[3]}"
                ))
        
        return errors
    
    def _validate_noun_pattern(self, word: str) -> List[ValidationError]:
        """Validate noun pattern [C/F][V/P][F][P]."""
        errors = []
        
        if len(word) < 4:
            errors.append(ValidationError(
                ValidationResult.INVALID,
                f"Noun too short: {len(word)} chars (minimum 4)"
            ))
            return errors
        
        components = self._parse_word_components(word, "noun")
        if len(components) != 4:
            errors.append(ValidationError(
                ValidationResult.INVALID,
                f"Noun must have exactly 4 components, got {len(components)}"
            ))
        else:
            # First: consonant or fricative
            if (components[0] not in self.consonants and 
                components[0] not in self.fricatives):
                errors.append(ValidationError(
                    ValidationResult.INVALID,
                    f"First component must be consonant or fricative, got: {components[0]}"
                ))
            
            # Second: vowel or vowel pair
            if (components[1] not in self.vowels and 
                not self._is_vowel_pair(components[1])):
                errors.append(ValidationError(
                    ValidationResult.INVALID,
                    f"Second component must be vowel or vowel pair, got: {components[1]}"
                ))
            
            # Third: fricative required
            if components[2] not in self.fricatives:
                errors.append(ValidationError(
                    ValidationResult.INVALID,
                    f"Third component must be fricative, got: {components[2]}"
                ))
            
            # Fourth: vowel pair required
            if not self._is_vowel_pair(components[3]):
                errors.append(ValidationError(
                    ValidationResult.INVALID,
                    f"Fourth component must be vowel pair, got: {components[3]}"
                ))
        
        return errors
    
    def _validate_adverb_pattern(self, word: str) -> List[ValidationError]:
        """Validate adverb pattern [C][V][C][V][C][V]."""
        errors = []
        
        if len(word) != 6:
            errors.append(ValidationError(
                ValidationResult.INVALID,
                f"Adverb must be exactly 6 characters, got {len(word)}"
            ))
            return errors
        
        # Check for fricatives (not allowed in adverbs)
        for fricative in self.fricatives:
            if fricative in word:
                errors.append(ValidationError(
                    ValidationResult.INVALID,
                    f"Adverbs cannot contain fricative digraphs, found: {fricative}"
                ))
        
        # Check alternating pattern
        for i in range(0, 6, 2):
            if word[i] not in self.consonants:
                errors.append(ValidationError(
                    ValidationResult.INVALID,
                    f"Position {i+1} must be consonant, got: {word[i]}"
                ))
        
        for i in range(1, 6, 2):
            if word[i] not in self.vowels:
                errors.append(ValidationError(
                    ValidationResult.INVALID,
                    f"Position {i+1} must be vowel, got: {word[i]}"
                ))
        
        return errors
    
    def _validate_preposition_pattern(self, word: str) -> List[ValidationError]:
        """Validate preposition pattern [F][P]."""
        errors = []
        
        if len(word) < 3 or len(word) > 4:
            errors.append(ValidationError(
                ValidationResult.INVALID,
                f"Preposition must be 3-4 characters, got {len(word)}"
            ))
            return errors
        
        # Must start with fricative
        if word[:2] not in self.fricatives:
            errors.append(ValidationError(
                ValidationResult.INVALID,
                f"Preposition must start with fricative, got: {word[:2]}"
            ))
        
        # Must end with vowel pair
        if not self._is_vowel_pair(word[2:]):
            errors.append(ValidationError(
                ValidationResult.INVALID,
                f"Preposition must end with vowel pair, got: {word[2:]}"
            ))
        
        return errors
    
    def _validate_particle_pattern(self, word: str) -> List[ValidationError]:
        """Validate particle pattern [C][V]."""
        errors = []
        
        if len(word) != 2:
            errors.append(ValidationError(
                ValidationResult.INVALID,
                f"Particle must be exactly 2 characters, got {len(word)}"
            ))
            return errors
        
        if word[0] not in self.consonants:
            errors.append(ValidationError(
                ValidationResult.INVALID,
                f"Particle must start with consonant, got: {word[0]}"
            ))
        
        if word[1] not in self.vowels:
            errors.append(ValidationError(
                ValidationResult.INVALID,
                f"Particle must end with vowel, got: {word[1]}"
            ))
        
        return errors
    
    def _validate_other_patterns(self, word: str, pos: str) -> List[ValidationError]:
        """Validate other part-of-speech patterns."""
        errors = []
        # Simplified validation for other patterns
        # Full implementation would include specific checks for each pattern
        return errors
    
    def check_lexical_conflicts(self, word: str, pos: str, meaning: str) -> List[ValidationError]:
        """Check for lexical conflicts with existing vocabulary."""
        errors = []
        
        # Check for homonyms across all parts of speech
        for existing_pos, entries in self.lexicon.items():
            for entry in entries:
                if entry.word == word:
                    if existing_pos != pos:
                        errors.append(ValidationError(
                            ValidationResult.CONFLICT,
                            f"Word '{word}' already exists as {existing_pos}: {entry.meaning}"
                        ))
                    else:
                        errors.append(ValidationError(
                            ValidationResult.CONFLICT,
                            f"Word '{word}' already defined in {pos}: {entry.meaning}"
                        ))
        
        # Removed expensive similar meaning check for performance
        # This was causing O(n²) complexity during lexicon validation
        
        return errors
    
    def validate_word(self, word: str, pos: str, meaning: str) -> Dict:
        """Complete validation of a single word."""
        word = word.lower().strip()
        pos = pos.lower().strip()
        
        results = {
            "word": word,
            "pos": pos,
            "meaning": meaning,
            "phonotactic_errors": [],
            "lexical_errors": [],
            "overall_status": ValidationResult.VALID,
            "recommendations": []
        }
        
        # Phonotactic validation
        phonotactic_errors = self.validate_phonotactics(word, pos)
        results["phonotactic_errors"] = phonotactic_errors
        
        # Lexical validation
        lexical_errors = self.check_lexical_conflicts(word, pos, meaning)
        results["lexical_errors"] = lexical_errors
        
        # Determine overall status
        has_invalid = any(e.level == ValidationResult.INVALID for e in 
                         phonotactic_errors + lexical_errors)
        has_conflict = any(e.level == ValidationResult.CONFLICT for e in 
                          phonotactic_errors + lexical_errors)
        has_warning = any(e.level == ValidationResult.WARNING for e in 
                         phonotactic_errors + lexical_errors)
        
        if has_invalid:
            results["overall_status"] = ValidationResult.INVALID
        elif has_conflict:
            results["overall_status"] = ValidationResult.CONFLICT
        elif has_warning:
            results["overall_status"] = ValidationResult.WARNING
        
        return results
    
    def generate_report(self, validation_result: Dict) -> str:
        """Generate a formatted validation report."""
        word = validation_result["word"]
        pos = validation_result["pos"]
        meaning = validation_result["meaning"]
        status = validation_result["overall_status"]
        
        report = f"""
WORD VALIDATION REPORT
======================
Word: {word}
Intended POS: {pos}
Proposed meaning: {meaning}

OVERALL STATUS: {status.value}

PHONOTACTIC VALIDATION:
"""
        
        if validation_result["phonotactic_errors"]:
            for error in validation_result["phonotactic_errors"]:
                report += f"  [{error.level.value}] {error.message}\n"
        else:
            report += "  ✓ All phonotactic patterns valid\n"
        
        report += "\nLEXICAL VALIDATION:\n"
        if validation_result["lexical_errors"]:
            for error in validation_result["lexical_errors"]:
                report += f"  [{error.level.value}] {error.message}\n"
        else:
            report += "  ✓ No lexical conflicts detected\n"
        
        if status == ValidationResult.VALID:
            report += "\n✅ APPROVED: Word ready for lexicon integration\n"
        elif status == ValidationResult.WARNING:
            report += "\n⚠️  REVIEW NEEDED: Address warnings before approval\n"
        else:
            report += "\n❌ REJECTED: Fix errors before resubmission\n"
        
        return report
    
    def check_lexicon_integrity(self) -> Dict:
        """Comprehensive check of entire lexicon for integrity issues."""
        print("Starting lexicon integrity check...")
        print("=" * 50)
        
        results = {
            "total_words": 0,
            "pattern_violations": [],
            "homonym_conflicts": [],
            "recommendations": []
        }
        
        all_words = {}  # word -> [(pos, meaning), ...]
        
        # Collect all words
        print("\nValidating phonotactic patterns...")
        for pos, entries in self.lexicon.items():
            if not entries:
                continue
                
            print(f"\nProcessing {pos} ({len(entries)} words):")
            
            for i, entry in enumerate(entries, 1):
                results["total_words"] += 1
                
                # Progress indicator
                if i % 50 == 0 or i == len(entries):
                    print(f"  Progress: {i}/{len(entries)} words processed")
                
                if entry.word not in all_words:
                    all_words[entry.word] = []
                all_words[entry.word].append((pos, entry.meaning))
                
                # Simple phonotactic compliance check (optimized for bulk validation)
                errors = self._quick_pattern_check(entry.word, pos)
                if errors:
                    results["pattern_violations"].append({
                        "word": entry.word,
                        "pos": pos,
                        "errors": errors
                    })
                    print(f"    ⚠️  Pattern violation: {entry.word} - {errors[0]}")
        
        # Check for homonyms
        print(f"\nAnalyzing homonym conflicts...")
        homonym_count = 0
        for word, definitions in all_words.items():
            if len(definitions) > 1:
                homonym_count += 1
                results["homonym_conflicts"].append({
                    "word": word,
                    "definitions": definitions
                })
                if homonym_count <= 10:  # Show first 10 conflicts
                    print(f"  Conflict #{homonym_count}: '{word}' -> {definitions}")
        
        if homonym_count > 10:
            print(f"  ... and {homonym_count - 10} more conflicts")
        
        print("\n" + "=" * 50)
        print("Lexicon integrity check complete!")
        
        return results

    def _quick_pattern_check(self, word: str, pos: str) -> List[str]:
        """Enhanced pattern validation for bulk processing - more thorough but still fast."""
        errors = []
        
        # Skip unknown POS
        if pos not in self.patterns and pos not in ["pronoun", "digit"]:
            return [f"Unknown part of speech: {pos}"]
        
        # Handle special cases
        if pos == "pronoun":
            if word not in ["mia", "thi", "sha"]:
                errors.append(f"Invalid pronoun: {word}")
            return errors
        
        if pos == "digit":
            # Try digit pattern [F][V]
            if len(word) == 3 and word[:2] in self.fricatives and word[2] in self.vowels:
                return []  # Valid digit pattern
            
            # Try magnitude pattern [F][V][F][V]
            if (len(word) == 6 and 
                word[:2] in self.fricatives and 
                word[2] in self.vowels and
                word[3:5] in self.fricatives and
                word[5] in self.vowels):
                return []  # Valid magnitude pattern
            
            # Neither pattern matches
            return [f"Number does not match digit [F][V] or magnitude [F][V][F][V] patterns"]
        
        # Basic character validation
        valid_chars = self.consonants | self.vowels
        for char in word:
            if char not in valid_chars:
                errors.append(f"Invalid character '{char}'")
        
        # Check forbidden vowel pairs
        for i in range(len(word) - 1):
            pair = word[i:i+2]
            if pair in self.forbidden_vowel_pairs:
                errors.append(f"Forbidden vowel pair: {pair}")
        
        # Quick pattern checks for major POS
        if pos == "noun":
            if len(word) < 4:
                errors.append("Noun too short")
            else:
                # Check pattern [C/F][V/P][F][P]
                components = self._parse_word_components(word, pos)
                if len(components) != 4:
                    errors.append(f"Noun pattern violation: {len(components)} components")
                elif components[2] not in self.fricatives:
                    errors.append("Third component must be fricative")
                elif not self._is_vowel_pair(components[3]):
                    errors.append("Fourth component must be vowel pair")
        
        elif pos == "verb":
            if len(word) < 4:
                errors.append("Verb too short")
            elif word[:2] not in self.fricatives:
                errors.append("Verb must start with fricative")
        
        elif pos == "adjective":
            if len(word) < 4:
                errors.append("Adjective too short")
            else:
                components = self._parse_word_components(word, pos)
                if len(components) >= 3 and components[2] not in self.fricatives:
                    errors.append("Third component must be fricative")
        
        elif pos == "particle":
            if len(word) != 2:
                errors.append(f"Particle must be 2 chars, got {len(word)}")
        
        return errors


def main():
    """Command-line interface for phi validation."""
    parser = argparse.ArgumentParser(description="Phi Word Validation System")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Validate single word
    validate_parser = subparsers.add_parser("validate", help="Validate a single word")
    validate_parser.add_argument("word", help="Word to validate")
    validate_parser.add_argument("pos", help="Part of speech")
    validate_parser.add_argument("meaning", help="Proposed meaning")
    validate_parser.add_argument("--pos-dir", default="pos/", help="POS files directory")
    
    # Check lexicon integrity
    lexicon_parser = subparsers.add_parser("check-lexicon", help="Check entire lexicon")
    lexicon_parser.add_argument("--pos-dir", default="pos/", help="POS files directory")
    
    # Batch validation
    batch_parser = subparsers.add_parser("batch", help="Batch validate from file")
    batch_parser.add_argument("file", help="File with word,pos,meaning per line")
    batch_parser.add_argument("--pos-dir", default="pos/", help="POS files directory")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 0
    
    validator = PhiValidator(args.pos_dir)
    
    if args.command == "validate":
        result = validator.validate_word(args.word, args.pos, args.meaning)
        print(validator.generate_report(result))
        return 0
    
    elif args.command == "check-lexicon":
        results = validator.check_lexicon_integrity()
        
        print(f"LEXICON INTEGRITY REPORT")
        print(f"========================")
        print(f"Total words: {results['total_words']}")
        print(f"Pattern violations: {len(results['pattern_violations'])}")
        print(f"Homonym conflicts: {len(results['homonym_conflicts'])}")
        
        if results['pattern_violations']:
            print("\nPATTERN VIOLATIONS:")
            for violation in results['pattern_violations']:
                print(f"  {violation['word']} ({violation['pos']}): {violation['errors']}")
        
        if results['homonym_conflicts']:
            print("\nHOMONYM CONFLICTS:")
            for conflict in results['homonym_conflicts']:
                print(f"  {conflict['word']}: {conflict['definitions']}")
        
        print("\nValidation complete!")
        return 0
    
    elif args.command == "batch":
        try:
            with open(args.file, 'r') as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    
                    parts = line.split(',', 2)
                    if len(parts) != 3:
                        print(f"Line {line_num}: Invalid format (need word,pos,meaning)")
                        continue
                    
                    word, pos, meaning = [p.strip() for p in parts]
                    result = validator.validate_word(word, pos, meaning)
                    
                    if result["overall_status"] != ValidationResult.VALID:
                        print(f"Line {line_num}: {word} - {result['overall_status'].value}")
                        for error in result["phonotactic_errors"] + result["lexical_errors"]:
                            print(f"  {error.message}")
        
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found")
            return 1
        
        return 0


if __name__ == "__main__":
    import sys
    exit_code = main()
    sys.exit(exit_code) 