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

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from phi_validator import PhiValidator

class PhiWordReplacer:
    """Systematic word replacement tool for Phi language files."""
    
    def __init__(self, backup_dir: str = "backups"):
        self.validator = PhiValidator()
        self.backup_dir = Path(backup_dir)
        self.backup_dir.mkdir(exist_ok=True)
        
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
        
        # Check if old word exists
        if not self._word_exists_in_lexicon(old_word):
            errors.append(f"Warning: '{old_word}' not found in lexicon")
        
        # Check if new word already exists
        if self._word_exists_in_lexicon(new_word):
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
    
    def _word_exists_in_lexicon(self, word: str) -> bool:
        """Check if a word exists in the current lexicon."""
        for pos_file in Path("pos").glob("*.md"):
            try:
                with open(pos_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Look for word in table format
                pattern = rf'\|\s*{re.escape(word)}\s*\|'
                if re.search(pattern, content):
                    return True
            except Exception:
                continue
        return False
    
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
                    # Backup specific files from current directory
                    for pattern in self.file_patterns:
                        for file_path in Path(".").glob(pattern):
                            if file_path.is_file() and not file_path.name.startswith('.'):
                                dest = backup_path / file_path.name
                                shutil.copy2(file_path, dest)
                else:
                    # Backup entire directory
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
                
            if target_dir.name == ".":
                # Search specific files in current directory
                search_files = []
                for pattern in self.file_patterns:
                    search_files.extend(Path(".").glob(pattern))
            else:
                # Search all files in directory
                search_files = []
                for pattern in self.file_patterns:
                    search_files.extend(target_dir.rglob(pattern))
        
            for file_path in search_files:
                if not file_path.is_file():
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
    
    def suggest_alternatives(self, pos: str, meaning: str = None) -> List[str]:
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
        
        if pos in patterns:
            pattern_info = patterns[pos]
            print(f"\n💡 Suggestions for {pos} (pattern: {pattern_info['pattern']}):")
            
            # Generate some example patterns
            fricatives = ['ph', 'wh', 'th', 'sh']
            consonants = ['h', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w']
            vowels = ['i', 'u', 'e', 'o', 'a']
            
            if pos == 'verb':
                for f in fricatives[:2]:
                    for v1 in vowels[:2]:
                        for c in consonants[:2]:
                            for v2 in vowels[:2]:
                                suggestion = f + v1 + c + v2
                                if not self._word_exists_in_lexicon(suggestion):
                                    suggestions.append(suggestion)
                                    if len(suggestions) >= 5:
                                        break
                            if len(suggestions) >= 5:
                                break
                        if len(suggestions) >= 5:
                            break
                    if len(suggestions) >= 5:
                        break
        
        return suggestions[:5]
    
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
    
    # Get user input
    old_word = input("Enter the word to replace: ").strip().lower()
    if not old_word:
        print("❌ No word provided")
        return
    
    new_word = input("Enter the new word: ").strip().lower()
    if not new_word:
        print("❌ No new word provided")
        return
    
    pos = input("Enter the part of speech (verb/noun/adjective/etc.): ").strip().lower()
    if not pos:
        print("❌ No part of speech provided")
        return
    
    # Show suggestions if requested
    show_suggestions = input("Show alternative suggestions? (y/n): ").strip().lower()
    if show_suggestions == 'y':
        suggestions = replacer.suggest_alternatives(pos)
        if suggestions:
            print(f"\n💡 Alternative suggestions for {pos}:")
            for i, suggestion in enumerate(suggestions, 1):
                print(f"  {i}. {suggestion}")
            print()
    
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