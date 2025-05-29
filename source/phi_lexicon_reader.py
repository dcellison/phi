#!/usr/bin/env python3
"""
Phi Lexicon Reader - Authoritative Lexicon Parser
Reads all POS files and provides the definitive current lexicon state.
"""

import re
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional
from collections import defaultdict
import json
import itertools

class PhiLexiconReader:
    """Authoritative reader for the complete Phi lexicon."""
    
    def __init__(self, pos_directory: str = "pos"):
        self.pos_dir = Path(pos_directory)
        self.lexicon = {}  # word -> {'pos': str, 'translation': str, 'file': str}
        self.pos_counts = defaultdict(int)
        self.duplicates = defaultdict(list)  # word -> list of (pos, file) tuples
        self.errors = []
        
    def read_lexicon(self) -> Dict:
        """Read and parse all POS files to build complete lexicon."""
        print(f"📚 Reading Phi lexicon from {self.pos_dir}/")
        
        if not self.pos_dir.exists():
            self.errors.append(f"POS directory not found: {self.pos_dir}")
            return {}
        
        # Get all markdown files in pos directory
        pos_files = list(self.pos_dir.glob("*.md"))
        
        if not pos_files:
            self.errors.append(f"No .md files found in {self.pos_dir}")
            return {}
        
        print(f"Found {len(pos_files)} POS files to process")
        
        for pos_file in sorted(pos_files):
            self._process_pos_file(pos_file)
        
        self._analyze_duplicates()
        self._generate_summary()
        
        return self.lexicon
    
    def _process_pos_file(self, pos_file: Path) -> None:
        """Process a single POS file."""
        raw_pos_name = pos_file.stem  # filename without .md extension
        
        # Convert plural filenames to singular POS names for consistency
        pos_name_mapping = {
            'pronouns': 'pronoun',
            'nouns': 'noun',
            'verbs': 'verb', 
            'adjectives': 'adjective',
            'adverbs': 'adverb',
            'particles': 'particle',
            'prepositions': 'preposition',
            'determiners': 'determiner',
            'classifiers': 'classifier',
            'conjunctions': 'conjunction',
            'interjections': 'interjection',
            'numbers': 'number'
        }
        
        pos_name = pos_name_mapping.get(raw_pos_name, raw_pos_name)
        print(f"  Processing {pos_file.name}...")
        
        try:
            with open(pos_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            self.errors.append(f"Could not read {pos_file}: {e}")
            return
        
        # Find vocabulary tables by their headers first
        # Look for table headers with "phi word" and "english translation" (or similar)
        lines = content.split('\n')
        vocabulary_tables = []
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Check if this line looks like a table header
            if '|' in line and ('phi' in line.lower() or 'word' in line.lower()):
                # Check if next line is a separator (|---|---|)
                if i + 1 < len(lines) and '|' in lines[i + 1] and '-' in lines[i + 1]:
                    # Extract header columns
                    headers = [col.strip().lower() for col in line.split('|') if col.strip()]
                    
                    # Check if this is a vocabulary table (has phi/word and english/translation columns)
                    has_phi_column = any('phi' in h or 'word' in h or 'formation' in h for h in headers)
                    has_translation_column = any('english' in h or 'translation' in h for h in headers)
                    
                    # Must be 2-3 columns for vocabulary (phi word + translation + optional function)
                    # Exclude grammar example tables (4+ columns with 'gloss', 'type', etc.)
                    is_grammar_example = any(keyword in h for h in headers 
                                           for keyword in ['gloss', 'type', 'sentence', 'discourse'])
                    
                    if (has_phi_column and has_translation_column and 
                        len(headers) >= 2 and len(headers) <= 3 and 
                        not is_grammar_example):
                        
                        # This is a vocabulary table - collect all its rows
                        table_start = i + 2  # Skip header and separator
                        table_rows = []
                        
                        j = table_start
                        while j < len(lines):
                            row_line = lines[j].strip()
                            if not row_line or not row_line.startswith('|'):
                                break  # End of table
                            
                            # Extract row data
                            row_data = [col.strip() for col in row_line.split('|') if col.strip()]
                            if len(row_data) >= 2:  # Must have at least phi word and translation
                                table_rows.append((row_data[0], row_data[1]))
                            j += 1
                        
                        vocabulary_tables.extend(table_rows)
                        i = j  # Skip past this table
                        continue
            
            i += 1
        
        # Process the vocabulary table entries
        words_found = 0
        for phi_word, translation in vocabulary_tables:
            phi_word = phi_word.strip().lower()
            translation = translation.strip()
            
            # Skip header rows and empty entries
            if (phi_word in ['phi', 'word', 'term', 'lexeme'] or 
                translation.lower() in ['english', 'translation', 'meaning', 'gloss'] or
                not phi_word or not translation):
                continue
            
            # Check for duplicates
            if phi_word in self.lexicon:
                existing = self.lexicon[phi_word]
                # Only flag as duplicate if it's a different POS or different file
                if existing['pos'] != pos_name or existing['file'] != pos_file.name:
                    if phi_word not in self.duplicates:
                        self.duplicates[phi_word].append((existing['pos'], existing['file']))
                    self.duplicates[phi_word].append((pos_name, pos_file.name))
                # If it's the same word, same POS, same file - just ignore the duplicate entry
            else:
                self.lexicon[phi_word] = {
                    'pos': pos_name,
                    'translation': translation,
                    'file': pos_file.name
                }
                words_found += 1
        
        self.pos_counts[pos_name] = words_found
        print(f"    → {words_found} words loaded from {pos_name}")
    
    def _analyze_duplicates(self) -> None:
        """Analyze and report duplicate words across POS files."""
        if self.duplicates:
            print(f"\n⚠️  Found {len(self.duplicates)} duplicate words:")
            for word, occurrences in self.duplicates.items():
                print(f"  '{word}' appears in:")
                for pos, file in occurrences:
                    print(f"    - {pos} ({file})")
    
    def _generate_summary(self) -> None:
        """Generate summary statistics."""
        total_words = len(self.lexicon)
        print(f"\n📊 Lexicon Summary:")
        print(f"  Total unique words: {total_words}")
        print(f"  POS categories: {len(self.pos_counts)}")
        print(f"  Duplicate conflicts: {len(self.duplicates)}")
        
        print(f"\n📋 Words by POS:")
        for pos, count in sorted(self.pos_counts.items()):
            percentage = (count / total_words * 100) if total_words > 0 else 0
            print(f"  {pos:15} {count:4} words ({percentage:5.1f}%)")
    
    def word_exists(self, word: str) -> bool:
        """Check if a word exists in the lexicon."""
        return word.lower() in self.lexicon
    
    def get_word_info(self, word: str) -> Optional[Dict]:
        """Get information about a specific word."""
        return self.lexicon.get(word.lower())
    
    def get_words_by_pos(self, pos: str) -> List[str]:
        """Get all words for a specific part of speech."""
        return [word for word, info in self.lexicon.items() 
                if info['pos'] == pos.lower()]
    
    def search_words(self, pattern: str) -> List[Tuple[str, Dict]]:
        """Search for words matching a pattern."""
        import re
        regex = re.compile(pattern, re.IGNORECASE)
        return [(word, info) for word, info in self.lexicon.items() 
                if regex.search(word)]
    
    def find_conflicts(self) -> Dict[str, List[Tuple[str, str]]]:
        """Find words that appear in multiple POS categories."""
        return dict(self.duplicates)
    
    def validate_phonotactics(self, pos: str = None) -> Dict:
        """Validate phonotactic patterns for words."""
        # Phi phonotactic patterns
        patterns = {
            'verb': r'^(ph|wh|th|sh)[iueoa][hlmnprstw][iueoa]$',
            'noun': r'^[hlmnprstw]?[iueoa]{1,2}(ph|wh|th|sh)[iueoa]{1,2}$|^(ph|wh|th|sh)[iueoa]{1,2}(ph|wh|th|sh)[iueoa]{1,2}$',
            'adjective': r'^[hlmnprstw][iueoa](ph|wh|th|sh)[iueoa]$',
            'adverb': r'^[hlmnprstw][iueoa][hlmnprstw][iueoa][hlmnprstw][iueoa]$',
            'particle': r'^[hlmnprstw][iueoa]$',
            'preposition': r'^(ph|wh|th|sh)[iueoa]{2}$',
            'determiner': r'^(ph|wh|th|sh)[iueoa]{2}[hlmnprstw][iueoa]$',
            'classifier': r'^[hlmnprstw][iueoa]{2}$',
            'conjunction': r'^[hlmnprstw][iueoa][hlmnprstw][iueoa]$',
            'interjection': r'^[hlmnprstw][iueoa][hlmnprstw][iueoa]{2}$',
            'number': r'^(ph|wh|th|sh)[iueoa]$|^(ph|wh|th|sh)[iueoa](ph|wh|th|sh)[iueoa]$',
        }
        
        violations = defaultdict(list)
        
        target_pos = [pos.lower()] if pos else patterns.keys()
        
        for target in target_pos:
            if target not in patterns:
                continue
                
            pattern = patterns[target]
            regex = re.compile(pattern)
            
            words = self.get_words_by_pos(target)
            for word in words:
                if not regex.match(word):
                    violations[target].append(word)
        
        return dict(violations)
    
    def generate_unassigned_words(self, pos: str, limit: int = 50) -> List[str]:
        """Generate unassigned words that follow phonotactic patterns for a POS."""
        # Phi phonotactic generation patterns
        generation_patterns = {
            'verb': {
                'pattern': '[F][V][C][V]',
                'components': {
                    'F': ['ph', 'wh', 'th', 'sh'],
                    'V': ['i', 'u', 'e', 'o', 'a'],
                    'C': ['h', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w']
                }
            },
            'adjective': {
                'pattern': '[C][V][F][V]',
                'components': {
                    'C': ['h', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w'],
                    'V': ['i', 'u', 'e', 'o', 'a'],
                    'F': ['ph', 'wh', 'th', 'sh']
                }
            },
            'adverb': {
                'pattern': '[C][V][C][V][C][V]',
                'components': {
                    'C': ['h', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w'],
                    'V': ['i', 'u', 'e', 'o', 'a']
                }
            },
            'particle': {
                'pattern': '[C][V]',
                'components': {
                    'C': ['h', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w'],
                    'V': ['i', 'u', 'e', 'o', 'a']
                }
            },
            'preposition': {
                'pattern': '[F][P]',
                'components': {
                    'F': ['ph', 'wh', 'th', 'sh'],
                    'P': ['ia', 'ie', 'io', 'iu', 'ua', 'ue', 'ui', 'uo', 'ea', 'ei', 'eo', 'eu', 'oa', 'oe', 'oi', 'ou', 'ai', 'ae', 'ao', 'au']
                }
            },
            'determiner': {
                'pattern': '[F][P][C][V]',
                'components': {
                    'F': ['ph', 'wh', 'th', 'sh'],
                    'P': ['ia', 'ie', 'io', 'iu', 'ua', 'ue', 'ui', 'uo', 'ea', 'ei', 'eo', 'eu', 'oa', 'oe', 'oi', 'ou', 'ai', 'ae', 'ao', 'au'],
                    'C': ['h', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w'],
                    'V': ['i', 'u', 'e', 'o', 'a']
                }
            },
            'classifier': {
                'pattern': '[C][P]',
                'components': {
                    'C': ['h', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w'],
                    'P': ['ia', 'ie', 'io', 'iu', 'ua', 'ue', 'ui', 'uo', 'ea', 'ei', 'eo', 'eu', 'oa', 'oe', 'oi', 'ou', 'ai', 'ae', 'ao', 'au']
                }
            },
            'conjunction': {
                'pattern': '[C][V][C][V]',
                'components': {
                    'C': ['h', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w'],
                    'V': ['i', 'u', 'e', 'o', 'a']
                }
            },
            'interjection': {
                'pattern': '[C][V][C][P]',
                'components': {
                    'C': ['h', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w'],
                    'V': ['i', 'u', 'e', 'o', 'a'],
                    'P': ['ia', 'ie', 'io', 'iu', 'ua', 'ue', 'ui', 'uo', 'ea', 'ei', 'eo', 'eu', 'oa', 'oe', 'oi', 'ou', 'ai', 'ae', 'ao', 'au']
                }
            },
            'number': {
                'pattern': '[F][V]',
                'components': {
                    'F': ['ph', 'wh', 'th', 'sh'],
                    'V': ['i', 'u', 'e', 'o', 'a']
                }
            }
        }
        
        pos_lower = pos.lower()
        if pos_lower not in generation_patterns:
            return []
        
        pattern_info = generation_patterns[pos_lower]
        components = pattern_info['components']
        
        unassigned = []
        
        # Generate combinations based on pattern
        if pos_lower == 'verb':  # [F][V][C][V]
            for f in components['F']:
                for v1 in components['V']:
                    for c in components['C']:
                        for v2 in components['V']:
                            word = f + v1 + c + v2
                            if not self.word_exists(word):
                                unassigned.append(word)
                                if len(unassigned) >= limit:
                                    return unassigned
        
        elif pos_lower == 'adjective':  # [C][V][F][V]
            for c in components['C']:
                for v1 in components['V']:
                    for f in components['F']:
                        for v2 in components['V']:
                            word = c + v1 + f + v2
                            if not self.word_exists(word):
                                unassigned.append(word)
                                if len(unassigned) >= limit:
                                    return unassigned
        
        elif pos_lower == 'adverb':  # [C][V][C][V][C][V]
            for c1 in components['C']:
                for v1 in components['V']:
                    for c2 in components['C']:
                        for v2 in components['V']:
                            for c3 in components['C']:
                                for v3 in components['V']:
                                    word = c1 + v1 + c2 + v2 + c3 + v3
                                    if not self.word_exists(word):
                                        unassigned.append(word)
                                        if len(unassigned) >= limit:
                                            return unassigned
        
        elif pos_lower == 'particle':  # [C][V]
            for c in components['C']:
                for v in components['V']:
                    word = c + v
                    if not self.word_exists(word):
                        unassigned.append(word)
                        if len(unassigned) >= limit:
                            return unassigned
        
        elif pos_lower == 'preposition':  # [F][P]
            for f in components['F']:
                for p in components['P']:
                    word = f + p
                    if not self.word_exists(word):
                        unassigned.append(word)
                        if len(unassigned) >= limit:
                            return unassigned
        
        elif pos_lower == 'determiner':  # [F][P][C][V]
            for f in components['F']:
                for p in components['P']:
                    for c in components['C']:
                        for v in components['V']:
                            word = f + p + c + v
                            if not self.word_exists(word):
                                unassigned.append(word)
                                if len(unassigned) >= limit:
                                    return unassigned
        
        elif pos_lower == 'classifier':  # [C][P]
            for c in components['C']:
                for p in components['P']:
                    word = c + p
                    if not self.word_exists(word):
                        unassigned.append(word)
                        if len(unassigned) >= limit:
                            return unassigned
        
        elif pos_lower == 'conjunction':  # [C][V][C][V]
            for c1 in components['C']:
                for v1 in components['V']:
                    for c2 in components['C']:
                        for v2 in components['V']:
                            word = c1 + v1 + c2 + v2
                            if not self.word_exists(word):
                                unassigned.append(word)
                                if len(unassigned) >= limit:
                                    return unassigned
        
        elif pos_lower == 'interjection':  # [C][V][C][P]
            for c1 in components['C']:
                for v in components['V']:
                    for c2 in components['C']:
                        for p in components['P']:
                            word = c1 + v + c2 + p
                            if not self.word_exists(word):
                                unassigned.append(word)
                                if len(unassigned) >= limit:
                                    return unassigned
        
        elif pos_lower == 'number':  # [F][V]
            for f in components['F']:
                for v in components['V']:
                    word = f + v
                    if not self.word_exists(word):
                        unassigned.append(word)
                        if len(unassigned) >= limit:
                            return unassigned
        
        return unassigned
    
    def export_lexicon(self, format: str = 'json', filename: str = None) -> str:
        """Export lexicon in various formats."""
        if not filename:
            filename = f"phi_lexicon.{format}"
        
        if format == 'json':
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.lexicon, f, indent=2, ensure_ascii=False)
        
        elif format == 'csv':
            import csv
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['word', 'pos', 'translation', 'file'])
                for word, info in sorted(self.lexicon.items()):
                    writer.writerow([word, info['pos'], info['translation'], info['file']])
        
        elif format == 'md':
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("# Complete Phi Lexicon\n\n")
                f.write(f"Total words: {len(self.lexicon)}\n\n")
                
                for pos in sorted(self.pos_counts.keys()):
                    words = self.get_words_by_pos(pos)
                    f.write(f"## {pos.title()} ({len(words)} words)\n\n")
                    f.write("| Phi Word | Translation |\n")
                    f.write("|----------|-------------|\n")
                    for word in sorted(words):
                        info = self.lexicon[word]
                        f.write(f"| {word} | {info['translation']} |\n")
                    f.write("\n")
        
        print(f"✅ Lexicon exported to {filename}")
        return filename
    
    def interactive_lookup(self):
        """Interactive word lookup tool."""
        print("\n🔍 INTERACTIVE PHI LEXICON LOOKUP")
        print("=" * 50)
        print("Commands:")
        print("  <word>           - Look up a word")
        print("  pos:<pos>        - List all words for a POS")
        print("  search:<pattern> - Search with regex pattern")
        print("  unassigned:<pos> - Show unassigned words for POS")
        print("  stats            - Show lexicon statistics")
        print("  conflicts        - Show duplicate words")
        print("  validate:<pos>   - Validate phonotactics for POS")
        print("  export:<format>  - Export lexicon (json/csv/md)")
        print("  quit             - Exit")
        print()
        
        while True:
            try:
                query = input("lexicon> ").strip()
                
                if not query or query == 'quit':
                    break
                
                if query == 'stats':
                    self._generate_summary()
                
                elif query == 'conflicts':
                    conflicts = self.find_conflicts()
                    if conflicts:
                        print(f"Found {len(conflicts)} conflicts:")
                        for word, occurrences in conflicts.items():
                            print(f"  '{word}': {occurrences}")
                    else:
                        print("No conflicts found!")
                
                elif query.startswith('pos:'):
                    pos = query[4:].strip()
                    words = self.get_words_by_pos(pos)
                    if words:
                        print(f"{pos} words ({len(words)}):")
                        for word in sorted(words)[:20]:  # Show first 20
                            info = self.lexicon[word]
                            print(f"  {word} - {info['translation']}")
                        if len(words) > 20:
                            print(f"  ... and {len(words) - 20} more")
                    else:
                        print(f"No words found for POS: {pos}")
                
                elif query.startswith('unassigned:'):
                    pos = query[11:].strip()
                    unassigned = self.generate_unassigned_words(pos, limit=30)
                    if unassigned:
                        print(f"Unassigned {pos} words ({len(unassigned)} shown):")
                        for i, word in enumerate(unassigned, 1):
                            print(f"  {i:2}. {word}")
                    else:
                        print(f"No unassigned words found for POS: {pos} (or unsupported POS)")
                
                elif query.startswith('search:'):
                    pattern = query[7:].strip()
                    results = self.search_words(pattern)
                    if results:
                        print(f"Found {len(results)} matches:")
                        for word, info in results[:20]:
                            print(f"  {word} ({info['pos']}) - {info['translation']}")
                        if len(results) > 20:
                            print(f"  ... and {len(results) - 20} more")
                    else:
                        print(f"No matches for pattern: {pattern}")
                
                elif query.startswith('validate:'):
                    pos = query[9:].strip()
                    violations = self.validate_phonotactics(pos)
                    if violations:
                        for pos_name, words in violations.items():
                            if words:
                                print(f"{pos_name} violations ({len(words)}):")
                                for word in words[:10]:
                                    print(f"  {word}")
                                if len(words) > 10:
                                    print(f"  ... and {len(words) - 10} more")
                    else:
                        print(f"No phonotactic violations found for {pos}")
                
                elif query.startswith('export:'):
                    format = query[7:].strip()
                    if format in ['json', 'csv', 'md']:
                        self.export_lexicon(format)
                    else:
                        print("Supported formats: json, csv, md")
                
                else:
                    # Word lookup
                    word = query.lower()
                    info = self.get_word_info(word)
                    if info:
                        print(f"'{word}' found:")
                        print(f"  POS: {info['pos']}")
                        print(f"  Translation: {info['translation']}")
                        print(f"  File: {info['file']}")
                    else:
                        print(f"'{word}' not found in lexicon")
                
                print()
            
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")


def main():
    """Main function for command-line usage."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Phi Lexicon Reader")
    parser.add_argument("--pos-dir", "-p", default="pos", help="POS directory path")
    parser.add_argument("--word", "-w", help="Look up specific word")
    parser.add_argument("--pos", help="List words for specific POS")
    parser.add_argument("--unassigned", "-u", help="Show unassigned words for POS")
    parser.add_argument("--limit", "-l", type=int, default=50, help="Limit for unassigned words")
    parser.add_argument("--export", "-e", choices=['json', 'csv', 'md'], help="Export format")
    parser.add_argument("--validate", "-v", help="Validate phonotactics for POS")
    parser.add_argument("--interactive", "-i", action="store_true", help="Interactive mode")
    parser.add_argument("--conflicts", "-c", action="store_true", help="Show conflicts")
    
    args = parser.parse_args()
    
    reader = PhiLexiconReader(args.pos_dir)
    lexicon = reader.read_lexicon()
    
    if not lexicon:
        print("❌ Failed to read lexicon")
        return
    
    if args.word:
        info = reader.get_word_info(args.word)
        if info:
            print(f"'{args.word}' found:")
            print(f"  POS: {info['pos']}")
            print(f"  Translation: {info['translation']}")
            print(f"  File: {info['file']}")
        else:
            print(f"'{args.word}' not found in lexicon")
    
    elif args.pos:
        words = reader.get_words_by_pos(args.pos)
        if words:
            print(f"{args.pos} words ({len(words)}):")
            for word in sorted(words):
                info = lexicon[word]
                print(f"  {word} - {info['translation']}")
        else:
            print(f"No words found for POS: {args.pos}")
    
    elif args.unassigned:
        unassigned = reader.generate_unassigned_words(args.unassigned, args.limit)
        if unassigned:
            print(f"Unassigned {args.unassigned} words ({len(unassigned)} shown):")
            for i, word in enumerate(unassigned, 1):
                print(f"  {i:2}. {word}")
        else:
            print(f"No unassigned words found for POS: {args.unassigned}")
    
    elif args.export:
        reader.export_lexicon(args.export)
    
    elif args.validate:
        violations = reader.validate_phonotactics(args.validate)
        if violations:
            for pos, words in violations.items():
                if words:
                    print(f"{pos} violations ({len(words)}):")
                    for word in words:
                        print(f"  {word}")
        else:
            print(f"No phonotactic violations found for {args.validate}")
    
    elif args.conflicts:
        conflicts = reader.find_conflicts()
        if conflicts:
            print(f"Found {len(conflicts)} conflicts:")
            for word, occurrences in conflicts.items():
                print(f"  '{word}': {occurrences}")
        else:
            print("No conflicts found!")
    
    elif args.interactive:
        reader.interactive_lookup()
    
    else:
        # Default: show summary and start interactive mode
        print("\n🔍 Starting interactive lookup mode...")
        reader.interactive_lookup()


if __name__ == "__main__":
    main() 