#!/usr/bin/env python3
"""
Phi Word Lookup Utility

This script extracts all phi words from the POS documentation files and provides
lookup functionality to validate word existence, determine POS category, and 
retrieve English translations.

Usage:
    python phi_word_lookup.py word1 word2 word3
    python phi_word_lookup.py --extract  # Extract all words to JSON
    python phi_word_lookup.py --validate "mia whethea shose"  # Validate sentence
"""

import os
import re
import json
import argparse
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional

class PhiWordDatabase:
    def __init__(self, pos_directory: str = "../source/pos"):
        self.pos_directory = Path(pos_directory)
        self.word_db: Dict[str, Dict[str, str]] = {}
        self.pos_files = {
            'nouns.md': 'noun',
            'verbs.md': 'verb', 
            'adjectives.md': 'adjective',
            'adverbs.md': 'adverb',
            'particles.md': 'particle',
            'pronouns.md': 'pronoun',
            'prepositions.md': 'preposition',
            'determiners.md': 'determiner',
            'conjunctions.md': 'conjunction',
            'classifiers.md': 'classifier',
            'interjections.md': 'interjection',
            'numbers.md': 'number'
        }
        
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
            'noun': ['CFVFP', 'FVFP', 'FPFP', 'CFPFP'],  # Various noun patterns
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
            self.save_database()
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

def main():
    parser = argparse.ArgumentParser(description='Phi Word Lookup Utility')
    parser.add_argument('words', nargs='*', help='Words to look up')
    parser.add_argument('--extract', action='store_true', 
                        help='Extract all words from POS files')
    parser.add_argument('--validate', type=str, 
                        help='Validate all words in a sentence')
    parser.add_argument('--stats', action='store_true',
                        help='Show database statistics')
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
    parser.add_argument('--db-file', type=str, default='phi_words.json',
                        help='Database file path (default: phi_words.json)')
    
    args = parser.parse_args()
    
    # Initialize database
    db = PhiWordDatabase(args.pos_dir)
    
    # Try to load existing database, otherwise build new one
    if not db.load_database(args.db_file):
        print("Building new database from POS files...")
        db.build_database()
        db.save_database(args.db_file)
    
    # Handle different operations
    if args.extract:
        print("Re-extracting words from POS files...")
        db.build_database()
        db.save_database(args.db_file)
        
    elif args.validate:
        db.validate_sentence(args.validate)
        
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