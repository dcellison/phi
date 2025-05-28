#!/usr/bin/env python3
"""
Phi Word Replacer - Systematic Word Replacement Tool
Replaces Phi words across all files while maintaining phonotactic integrity.
"""

import sys
import os
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional
import shutil
from datetime import datetime
import random

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from phi_validator import PhiValidator
from phi_lexicon_reader import PhiLexiconReader

class PhiWordReplacer:
    """Systematic word replacement tool for Phi language files."""
    
    def __init__(self, backup_dir: str = "backups"):
        self.validator = PhiValidator()
        self.lexicon_reader = PhiLexiconReader()
        self.lexicon = {}
        self.backup_dir = Path(backup_dir)
        self.backup_dir.mkdir(exist_ok=True)
        
        # Load authoritative lexicon
        print("📚 Loading authoritative lexicon...")
        self.lexicon = self.lexicon_reader.read_lexicon()
        
        # Files to search and replace in
        self.target_directories = [
            Path("pos"),
            Path("grammar"),
            Path("lessons"),
            Path("phi_validation"),
            Path(".")  # Current directory for other files
        ]
        
        # File patterns to include
        self.file_patterns = ["*.md", "*.py", "*.txt"]
        
        # Track changes made
        self.changes_made = []
        self.files_modified = set()
        
    def validate_replacement(self, old_word: str, new_word: str, pos: str) -> Tuple[bool, List[str]]:
        """Validate that the new word follows Phi phonotactic rules."""
        errors = []
        
        # Check if old word exists using authoritative lexicon
        if not self.lexicon_reader.word_exists(old_word):
            errors.append(f"Warning: '{old_word}' not found in lexicon")
        
        # Check if new word already exists using authoritative lexicon
        if self.lexicon_reader.word_exists(new_word):
            errors.append(f"Error: '{new_word}' already exists in lexicon")
        
        # Validate phonotactics of new word
        phonotactic_errors = self.validator.validate_phonotactics(new_word, pos)
        if phonotactic_errors:
            for error in phonotactic_errors:
                errors.append(f"Phonotactic error: {error.message}")
        
        # Check length constraints
        if len(new_word) < 2:
            errors.append("Error: New word must be at least 2 characters")
        
        # Check character validity
        valid_chars = set("hlmnprstw") | set("iueoa")
        for char in new_word:
            if char not in valid_chars:
                errors.append(f"Error: Invalid character '{char}' in new word")
        
        return len([e for e in errors if e.startswith("Error:")]) == 0, errors
    
    def create_backup(self) -> str:
        """Create a timestamped backup of all relevant files."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = self.backup_dir / f"phi_backup_{timestamp}"
        backup_path.mkdir(exist_ok=True)
        
        print(f"Creating backup in {backup_path}...")
        
        # Backup all target directories
        for target_dir in self.target_directories:
            if target_dir.exists():
                if target_dir.name == ".":
                    # Backup specific files from current directory, excluding backups
                    for pattern in self.file_patterns:
                        for file_path in Path(".").glob(pattern):
                            if (file_path.is_file() and 
                                not file_path.name.startswith('.') and
                                not str(file_path).startswith('backups/')):
                                dest = backup_path / file_path.name
                                shutil.copy2(file_path, dest)
                else:
                    # Backup entire directory, but skip backups directory
                    if target_dir.name == "backups":
                        continue
                    dest = backup_path / target_dir.name
                    if target_dir.is_dir():
                        shutil.copytree(target_dir, dest, dirs_exist_ok=True)
        
        print(f"✅ Backup created: {backup_path}")
        return str(backup_path)
    
    def find_word_occurrences(self, word: str) -> Dict[str, List[Tuple[int, str]]]:
        """Find all occurrences of a word across all files."""
        occurrences = {}
        
        # Search in all target files
        for target_dir in self.target_directories:
            if not target_dir.exists():
                continue
                
            # Skip backups directory entirely
            if target_dir.name == "backups":
                continue
                
            if target_dir.name == ".":
                # Search specific files in current directory
                search_files = []
                for pattern in self.file_patterns:
                    for file_path in Path(".").glob(pattern):
                        # Exclude files in backups directory
                        if not str(file_path).startswith('backups/'):
                            search_files.append(file_path)
            else:
                # Search all files in directory
                search_files = []
                for pattern in self.file_patterns:
                    search_files.extend(target_dir.rglob(pattern))
        
            for file_path in search_files:
                if not file_path.is_file():
                    continue
                    
                # Double-check to exclude backup files
                if str(file_path).startswith('backups/'):
                    continue
                    
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                    
                    file_occurrences = []
                    for line_num, line in enumerate(lines, 1):
                        # Look for word boundaries to avoid partial matches
                        pattern = rf'\b{re.escape(word)}\b'
                        if re.search(pattern, line, re.IGNORECASE):
                            file_occurrences.append((line_num, line.strip()))
                    
                    if file_occurrences:
                        occurrences[str(file_path)] = file_occurrences
                        
                except Exception as e:
                    print(f"Warning: Could not read {file_path}: {e}")
        
        return occurrences
    
    def replace_word_in_file(self, file_path: Path, old_word: str, new_word: str) -> int:
        """Replace all occurrences of old_word with new_word in a file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Use word boundaries to avoid partial replacements
            pattern = rf'\b{re.escape(old_word)}\b'
            new_content, count = re.subn(pattern, new_word, content, flags=re.IGNORECASE)
            
            if count > 0:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                self.files_modified.add(str(file_path))
                self.changes_made.append({
                    'file': str(file_path),
                    'old_word': old_word,
                    'new_word': new_word,
                    'count': count
                })
            
            return count
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return 0
    
    def replace_word(self, old_word: str, new_word: str, pos: str, 
                    dry_run: bool = True, create_backup: bool = True) -> Dict:
        """Replace a word throughout all Phi files."""
        
        print(f"🔄 {'DRY RUN: ' if dry_run else ''}Replacing '{old_word}' with '{new_word}' ({pos})")
        
        # Validate replacement
        is_valid, errors = self.validate_replacement(old_word, new_word, pos)
        
        if not is_valid:
            print("❌ Validation failed:")
            for error in errors:
                print(f"  {error}")
            return {
                'success': False,
                'errors': errors,
                'files_modified': [],
                'total_replacements': 0
            }
        
        if errors:  # Warnings
            print("⚠️ Warnings:")
            for error in errors:
                print(f"  {error}")
        
        # Find all occurrences
        print(f"\n🔍 Finding occurrences of '{old_word}'...")
        occurrences = self.find_word_occurrences(old_word)
        
        if not occurrences:
            print(f"❌ No occurrences of '{old_word}' found")
            return {
                'success': False,
                'errors': [f"No occurrences of '{old_word}' found"],
                'files_modified': [],
                'total_replacements': 0
            }
        
        print(f"📍 Found '{old_word}' in {len(occurrences)} files:")
        total_occurrences = 0
        for file_path, file_occurrences in occurrences.items():
            print(f"  {file_path}: {len(file_occurrences)} occurrences")
            total_occurrences += len(file_occurrences)
            
            # Show first few occurrences
            for line_num, line in file_occurrences[:3]:
                print(f"    Line {line_num}: {line[:80]}{'...' if len(line) > 80 else ''}")
            if len(file_occurrences) > 3:
                print(f"    ... and {len(file_occurrences) - 3} more")
        
        print(f"\n📊 Total occurrences: {total_occurrences}")
        
        if dry_run:
            print("\n🔍 DRY RUN - No changes made")
            return {
                'success': True,
                'dry_run': True,
                'files_found': list(occurrences.keys()),
                'total_occurrences': total_occurrences,
                'files_modified': [],
                'total_replacements': 0
            }
        
        # Create backup if requested
        backup_path = None
        if create_backup:
            backup_path = self.create_backup()
        
        # Perform replacements
        print(f"\n🔄 Performing replacements...")
        total_replacements = 0
        
        for file_path_str in occurrences.keys():
            file_path = Path(file_path_str)
            count = self.replace_word_in_file(file_path, old_word, new_word)
            total_replacements += count
            if count > 0:
                print(f"  ✅ {file_path}: {count} replacements")
        
        print(f"\n🎉 Replacement complete!")
        print(f"  Files modified: {len(self.files_modified)}")
        print(f"  Total replacements: {total_replacements}")
        if backup_path:
            print(f"  Backup created: {backup_path}")
        
        return {
            'success': True,
            'dry_run': False,
            'backup_path': backup_path,
            'files_modified': list(self.files_modified),
            'total_replacements': total_replacements,
            'changes_made': self.changes_made
        }
    
    def suggest_alternatives(self, pos: str, meaning: str = None, count: int = 8) -> List[str]:
        """Suggest alternative words that follow phonotactic patterns."""
        suggestions = []
        
        # Get phonotactic pattern for POS
        patterns = {
            'verb': {'start': 'fricative', 'pattern': '[F][V][C][V]'},
            'noun': {'start': 'consonant_or_fricative', 'pattern': '[C/F][V/P][F][P]'},
            'adjective': {'start': 'consonant', 'pattern': '[C][V][F][V]'},
            'adverb': {'start': 'consonant', 'pattern': '[C][V][C][V][C][V]'},
            'particle': {'start': 'consonant', 'pattern': '[C][V]'},
            'preposition': {'start': 'fricative', 'pattern': '[F][P]'},
            'determiner': {'start': 'fricative', 'pattern': '[F][P][C][V]'},
            'classifier': {'start': 'consonant', 'pattern': '[C][P]'},
            'conjunction': {'start': 'consonant', 'pattern': '[C][V][C][V]'},
            'interjection': {'start': 'consonant', 'pattern': '[C][V][C][P]'},
            'number': {'start': 'fricative', 'pattern': '[F][V] or [F][V][F][V]'},
        }
        
        if pos not in patterns:
            return suggestions
            
        pattern_info = patterns[pos]
        
        # Define phoneme sets
        fricatives = ['ph', 'wh', 'th', 'sh']
        consonants = ['h', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w']
        vowels = ['i', 'u', 'e', 'o', 'a']
        vowel_pairs = ['ai', 'au', 'ei', 'eu', 'io', 'iu', 'oa', 'oe', 'ua', 'ue']
        
        # Generate candidates based on POS pattern
        candidates = []
        
        if pos == 'verb':  # [F][V][C][V]
            for f in fricatives:
                for v1 in vowels:
                    for c in consonants:
                        for v2 in vowels:
                            candidate = f + v1 + c + v2
                            if not self.lexicon_reader.word_exists(candidate):
                                candidates.append(candidate)
        
        elif pos == 'adjective':  # [C][V][F][V]
            for c in consonants:
                for v1 in vowels:
                    for f in fricatives:
                        for v2 in vowels:
                            candidate = c + v1 + f + v2
                            if not self.lexicon_reader.word_exists(candidate):
                                candidates.append(candidate)
        
        elif pos == 'noun':  # [C/F][V/P][F][P]
            # Consonant start variants
            for c in consonants:
                for v in vowels + vowel_pairs:
                    for f in fricatives:
                        for p in vowel_pairs:
                            candidate = c + v + f + p
                            if not self.lexicon_reader.word_exists(candidate):
                                candidates.append(candidate)
            # Fricative start variants
            for f1 in fricatives:
                for v in vowels + vowel_pairs:
                    for f2 in fricatives:
                        for p in vowel_pairs:
                            candidate = f1 + v + f2 + p
                            if not self.lexicon_reader.word_exists(candidate):
                                candidates.append(candidate)
        
        elif pos == 'particle':  # [C][V]
            for c in consonants:
                for v in vowels:
                    candidate = c + v
                    if not self.lexicon_reader.word_exists(candidate):
                        candidates.append(candidate)
        
        elif pos == 'preposition':  # [F][P]
            for f in fricatives:
                for p in vowel_pairs:
                    candidate = f + p
                    if not self.lexicon_reader.word_exists(candidate):
                        candidates.append(candidate)
        
        elif pos == 'adverb':  # [C][V][C][V][C][V]
            for c1 in consonants[:3]:  # Limit to avoid too many combinations
                for v1 in vowels[:3]:
                    for c2 in consonants[:3]:
                        for v2 in vowels[:3]:
                            for c3 in consonants[:3]:
                                for v3 in vowels[:3]:
                                    candidate = c1 + v1 + c2 + v2 + c3 + v3
                                    if not self.lexicon_reader.word_exists(candidate):
                                        candidates.append(candidate)
        
        # Sample diverse suggestions from candidates
        if candidates:
            # Shuffle to get random distribution
            random.shuffle(candidates)
            
            # Try to get diverse suggestions by sampling from different parts
            if len(candidates) > count * 3:
                # Sample from different sections to ensure diversity
                section_size = len(candidates) // count
                for i in range(count):
                    start_idx = i * section_size
                    end_idx = min(start_idx + section_size, len(candidates))
                    if start_idx < len(candidates):
                        section_candidates = candidates[start_idx:end_idx]
                        if section_candidates:
                            suggestions.append(random.choice(section_candidates))
            else:
                # Just take the first available candidates
                suggestions = candidates[:count]
        
        return suggestions[:count]
    
    def generate_report(self, result: Dict) -> str:
        """Generate a detailed report of the replacement operation."""
        report = []
        report.append("# PHI WORD REPLACEMENT REPORT")
        report.append("=" * 50)
        report.append("")
        
        if result.get('dry_run'):
            report.append("## 🔍 DRY RUN ANALYSIS")
        else:
            report.append("## ✅ REPLACEMENT COMPLETED")
        
        report.append("")
        report.append(f"**Operation**: {'Analysis' if result.get('dry_run') else 'Replacement'}")
        report.append(f"**Timestamp**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")
        
        if result.get('success'):
            if result.get('dry_run'):
                report.append(f"**Files Found**: {len(result.get('files_found', []))}")
                report.append(f"**Total Occurrences**: {result.get('total_occurrences', 0)}")
            else:
                report.append(f"**Files Modified**: {len(result.get('files_modified', []))}")
                report.append(f"**Total Replacements**: {result.get('total_replacements', 0)}")
                if result.get('backup_path'):
                    report.append(f"**Backup Created**: {result.get('backup_path')}")
        else:
            report.append("**Status**: FAILED")
            for error in result.get('errors', []):
                report.append(f"- {error}")
        
        return "\n".join(report)

def main():
    """Interactive word replacement tool."""
    replacer = PhiWordReplacer()
    
    print("🔄 PHI WORD REPLACER")
    print("=" * 50)
    print("Replace words systematically across all Phi files")
    print()
    
    # Get old word and POS first
    old_word = input("Enter the word to replace: ").strip().lower()
    if not old_word:
        print("❌ No word provided")
        return
    
    pos = input("Enter the part of speech (verb/noun/adjective/etc.): ").strip().lower()
    if not pos:
        print("❌ No part of speech provided")
        return
    
    # Show current usage of the word
    print(f"\n🔍 Finding current occurrences of '{old_word}'...")
    occurrences = replacer.find_word_occurrences(old_word)
    
    if occurrences:
        print(f"📍 Found '{old_word}' in {len(occurrences)} files:")
        total_occurrences = sum(len(file_occurrences) for file_occurrences in occurrences.values())
        print(f"📊 Total occurrences: {total_occurrences}")
        
        # Show a few examples
        shown_files = 0
        for file_path, file_occurrences in occurrences.items():
            if shown_files >= 3:
                remaining_files = len(occurrences) - shown_files
                if remaining_files > 0:
                    print(f"  ... and {remaining_files} more files")
                break
            print(f"  {file_path}: {len(file_occurrences)} occurrences")
            for line_num, line in file_occurrences[:1]:  # Show just one example per file
                print(f"    Line {line_num}: {line[:70]}{'...' if len(line) > 70 else ''}")
            shown_files += 1
    else:
        print(f"❌ No occurrences of '{old_word}' found")
        return
    
    # Show suggestions
    print(f"\n💡 Suggestions for {pos} replacements:")
    patterns = {
        'verb': '[F][V][C][V]',
        'noun': '[C/F][V/P][F][P]',
        'adjective': '[C][V][F][V]',
        'adverb': '[C][V][C][V][C][V]',
        'particle': '[C][V]',
        'preposition': '[F][P]',
        'determiner': '[F][P][C][V]',
        'classifier': '[C][P]',
        'conjunction': '[C][V][C][V]',
        'interjection': '[C][V][C][P]',
        'number': '[F][V] or [F][V][F][V]',
    }
    
    if pos in patterns:
        print(f"Pattern: {patterns[pos]}")
        suggestions = replacer.suggest_alternatives(pos)
        if suggestions:
            for i, suggestion in enumerate(suggestions, 1):
                print(f"  {i}. {suggestion}")
        else:
            print("  No available suggestions found")
    else:
        print(f"  Unknown POS '{pos}' - no pattern available")
    
    print()
    
    # Now ask for the new word
    new_word = input("Enter the new word (or choose from suggestions above): ").strip().lower()
    if not new_word:
        print("❌ No new word provided")
        return
    
    # Dry run first
    print("\n🔍 Running analysis (dry run)...")
    dry_result = replacer.replace_word(old_word, new_word, pos, dry_run=True)
    
    if not dry_result['success']:
        print("❌ Analysis failed. Aborting.")
        return
    
    # Ask for confirmation
    print(f"\n📋 Analysis Summary:")
    print(f"  Files found: {len(dry_result.get('files_found', []))}")
    print(f"  Total occurrences: {dry_result.get('total_occurrences', 0)}")
    
    confirm = input("\nProceed with replacement? (y/n): ").strip().lower()
    if confirm != 'y':
        print("❌ Operation cancelled")
        return
    
    # Perform actual replacement
    print("\n🔄 Performing replacement...")
    result = replacer.replace_word(old_word, new_word, pos, dry_run=False, create_backup=True)
    
    # Generate report
    report = replacer.generate_report(result)
    
    # Save report
    report_file = f"word_replacement_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\n📄 Report saved: {report_file}")

if __name__ == "__main__":
    main() 