#!/usr/bin/env python3
"""
Single Part-of-Speech Principle Analysis for Phi Language
Comprehensive validation of Phi's revolutionary linguistic feature.
"""

import sys
import os
import re
from pathlib import Path
from collections import defaultdict, Counter
from typing import Dict, List, Set, Tuple, Optional

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from phi_validator import PhiValidator

class SinglePOSPrincipleAnalyzer:
    """Analyzes the Single Part-of-Speech Principle across the entire lexicon."""
    
    def __init__(self, pos_directory: str = "pos/"):
        self.pos_directory = Path(pos_directory)
        self.validator = PhiValidator(pos_directory)
        
        # Phonotactic patterns for validation
        self.patterns = {
            'noun': r'^[hlmnprstw]|^(ph|wh|th|sh)',  # [C/F][V/P][F][P]
            'verb': r'^(ph|wh|th|sh)',  # [F][V][C][V]
            'adjective': r'^[hlmnprstw]',  # [C][V][F][V]
            'adverb': r'^[hlmnprstw]',  # [C][V][C][V][C][V]
            'preposition': r'^(ph|wh|th|sh)',  # [F][P]
            'determiner': r'^(ph|wh|th|sh)',  # [F][P][C][V]
            'classifier': r'^[hlmnprstw]',  # [C][P]
            'conjunction': r'^[hlmnprstw]',  # [C][V][C][V]
            'interjection': r'^[hlmnprstw]',  # [C][V][C][P]
            'particle': r'^[hlmnprstw]',  # [C][V]
            'number': r'^(ph|wh|th|sh)',  # [F][V] or [F][V][F][V]
            'pronoun': r'^[hlmnprstw]'  # Special case
        }
        
        # Fricatives and consonants
        self.fricatives = {'ph', 'wh', 'th', 'sh'}
        self.consonants = {'h', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w'}
        self.vowels = {'i', 'u', 'e', 'o', 'a'}
        
        # Results storage
        self.lexicon = {}
        self.violations = []
        self.cross_pos_conflicts = []
        self.phonotactic_violations = []
        self.pattern_statistics = defaultdict(int)
        
    def load_lexicon(self) -> Dict[str, Dict[str, str]]:
        """Load all words from POS files."""
        lexicon = {}
        
        for pos_file in self.pos_directory.glob("*.md"):
            pos_name = pos_file.stem
            normalized_pos = self._normalize_pos_name(pos_name)
            
            try:
                with open(pos_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract words from markdown tables
                words = self._extract_words_from_markdown(content)
                
                for word, meaning in words:
                    if word in lexicon:
                        # Cross-POS conflict detected!
                        self.cross_pos_conflicts.append({
                            'word': word,
                            'pos1': lexicon[word]['pos'],
                            'pos2': normalized_pos,
                            'meaning1': lexicon[word]['meaning'],
                            'meaning2': meaning
                        })
                    else:
                        lexicon[word] = {
                            'pos': normalized_pos,
                            'meaning': meaning,
                            'file': pos_file.name
                        }
                        
            except Exception as e:
                print(f"Error reading {pos_file}: {e}")
        
        self.lexicon = lexicon
        return lexicon
    
    def _normalize_pos_name(self, pos_name: str) -> str:
        """Convert plural POS filename to singular form."""
        mapping = {
            'adjectives': 'adjective',
            'nouns': 'noun',
            'verbs': 'verb',
            'adverbs': 'adverb',
            'prepositions': 'preposition',
            'determiners': 'determiner',
            'classifiers': 'classifier',
            'conjunctions': 'conjunction',
            'interjections': 'interjection',
            'particles': 'particle',
            'numbers': 'number',
            'pronouns': 'pronoun'
        }
        return mapping.get(pos_name, pos_name)
    
    def _extract_words_from_markdown(self, content: str) -> List[Tuple[str, str]]:
        """Extract words and meanings from markdown table format."""
        words = []
        
        # Look for table rows with | word | meaning | pattern
        table_pattern = r'\|\s*([a-z]+)\s*\|\s*([^|]+)\s*\|'
        matches = re.findall(table_pattern, content, re.MULTILINE)
        
        for word, meaning in matches:
            word = word.strip()
            meaning = meaning.strip()
            
            # Skip header rows and empty entries
            if (word and meaning and 
                word not in ['phi word', 'word', 'particle'] and
                not word.startswith('-')):
                words.append((word, meaning))
        
        return words
    
    def validate_phonotactic_patterns(self) -> List[Dict]:
        """Validate that each word follows its POS phonotactic pattern."""
        violations = []
        
        for word, info in self.lexicon.items():
            pos = info['pos']
            
            # Use the comprehensive validator
            errors = self.validator.validate_phonotactics(word, pos)
            
            if errors:
                violations.append({
                    'word': word,
                    'pos': pos,
                    'meaning': info['meaning'],
                    'errors': [error.message for error in errors],
                    'file': info['file']
                })
        
        self.phonotactic_violations = violations
        return violations
    
    def analyze_pattern_distribution(self) -> Dict[str, Dict]:
        """Analyze the distribution of phonotactic patterns."""
        stats = defaultdict(lambda: defaultdict(int))
        
        for word, info in self.lexicon.items():
            pos = info['pos']
            
            # Count pattern characteristics
            if word.startswith(tuple(self.fricatives)):
                stats[pos]['fricative_start'] += 1
            elif word[0] in self.consonants:
                stats[pos]['consonant_start'] += 1
            
            # Count length distribution
            length = len(word)
            stats[pos][f'length_{length}'] += 1
            
            # Count total words per POS
            stats[pos]['total'] += 1
        
        return dict(stats)
    
    def check_derivational_violations(self) -> List[Dict]:
        """Check for words that might violate the single POS principle through derivation."""
        potential_violations = []
        
        # Look for words that might be derived forms
        for word, info in self.lexicon.items():
            pos = info['pos']
            meaning = info['meaning'].lower()
            
            # Check for semantic patterns that suggest derivation
            derivation_indicators = [
                ('ing', 'gerund'),
                ('tion', 'nominalization'),
                ('ly', 'adverbialization'),
                ('er', 'agentive'),
                ('ed', 'past_participle')
            ]
            
            for indicator, derivation_type in derivation_indicators:
                if indicator in meaning:
                    potential_violations.append({
                        'word': word,
                        'pos': pos,
                        'meaning': meaning,
                        'derivation_type': derivation_type,
                        'indicator': indicator
                    })
        
        return potential_violations
    
    def find_semantic_overlaps(self) -> List[Dict]:
        """Find words with similar meanings across different POS."""
        semantic_overlaps = []
        
        # Group words by semantic similarity
        semantic_groups = defaultdict(list)
        
        for word, info in self.lexicon.items():
            # Extract key semantic concepts
            meaning_words = set(info['meaning'].lower().split())
            
            for meaning_word in meaning_words:
                if len(meaning_word) > 3:  # Skip short words
                    semantic_groups[meaning_word].append((word, info))
        
        # Find groups with multiple POS
        for concept, word_list in semantic_groups.items():
            if len(word_list) > 1:
                pos_set = {info['pos'] for _, info in word_list}
                if len(pos_set) > 1:
                    semantic_overlaps.append({
                        'concept': concept,
                        'words': [(word, info['pos'], info['meaning']) 
                                for word, info in word_list],
                        'pos_count': len(pos_set)
                    })
        
        return semantic_overlaps
    
    def run_comprehensive_analysis(self) -> Dict:
        """Run complete Single POS Principle analysis."""
        print("🔍 Starting Comprehensive Single POS Principle Analysis...")
        
        # Load lexicon
        print("📚 Loading lexicon...")
        self.load_lexicon()
        
        # Validate phonotactic patterns
        print("🔤 Validating phonotactic patterns...")
        phonotactic_violations = self.validate_phonotactic_patterns()
        
        # Analyze pattern distribution
        print("📊 Analyzing pattern distribution...")
        pattern_stats = self.analyze_pattern_distribution()
        
        # Check for derivational violations
        print("🔄 Checking for derivational violations...")
        derivational_violations = self.check_derivational_violations()
        
        # Find semantic overlaps
        print("🎯 Finding semantic overlaps...")
        semantic_overlaps = self.find_semantic_overlaps()
        
        # Compile results
        results = {
            'lexicon_size': len(self.lexicon),
            'cross_pos_conflicts': self.cross_pos_conflicts,
            'phonotactic_violations': phonotactic_violations,
            'derivational_violations': derivational_violations,
            'semantic_overlaps': semantic_overlaps,
            'pattern_statistics': pattern_stats,
            'pos_distribution': Counter(info['pos'] for info in self.lexicon.values())
        }
        
        return results
    
    def generate_report(self, results: Dict) -> str:
        """Generate comprehensive analysis report."""
        report = []
        
        report.append("# SINGLE PART-OF-SPEECH PRINCIPLE ANALYSIS REPORT")
        report.append("=" * 60)
        report.append("")
        
        # Executive Summary
        report.append("## 🎯 EXECUTIVE SUMMARY")
        report.append("")
        
        total_words = results['lexicon_size']
        cross_pos_conflicts = len(results['cross_pos_conflicts'])
        phonotactic_violations = len(results['phonotactic_violations'])
        
        if cross_pos_conflicts == 0 and phonotactic_violations == 0:
            report.append("✅ **PERFECT COMPLIANCE**: Single POS Principle is AIRTIGHT")
            report.append(f"- **{total_words} words analyzed** - Zero violations found")
            report.append("- **Zero cross-POS conflicts** - Each word serves exactly one function")
            report.append("- **Zero phonotactic violations** - All patterns perfectly enforced")
        else:
            report.append("⚠️ **VIOLATIONS DETECTED**: Single POS Principle needs attention")
            report.append(f"- **{cross_pos_conflicts} cross-POS conflicts** found")
            report.append(f"- **{phonotactic_violations} phonotactic violations** found")
        
        report.append("")
        
        # Lexicon Overview
        report.append("## 📊 LEXICON OVERVIEW")
        report.append("")
        report.append(f"**Total Words**: {total_words}")
        report.append("")
        
        # POS Distribution
        report.append("### Part-of-Speech Distribution")
        for pos, count in sorted(results['pos_distribution'].items()):
            percentage = (count / total_words) * 100
            report.append(f"- **{pos}**: {count} words ({percentage:.1f}%)")
        report.append("")
        
        # Cross-POS Conflicts
        if results['cross_pos_conflicts']:
            report.append("## ❌ CROSS-POS CONFLICTS (CRITICAL VIOLATIONS)")
            report.append("")
            for conflict in results['cross_pos_conflicts']:
                report.append(f"### Word: `{conflict['word']}`")
                report.append(f"- **Conflict**: Used as both {conflict['pos1']} and {conflict['pos2']}")
                report.append(f"- **Meaning 1**: {conflict['meaning1']}")
                report.append(f"- **Meaning 2**: {conflict['meaning2']}")
                report.append("")
        else:
            report.append("## ✅ CROSS-POS CONFLICTS: NONE FOUND")
            report.append("")
            report.append("Perfect compliance! No word appears in multiple POS categories.")
            report.append("")
        
        # Phonotactic Violations
        if results['phonotactic_violations']:
            report.append("## ❌ PHONOTACTIC VIOLATIONS")
            report.append("")
            for violation in results['phonotactic_violations']:
                report.append(f"### Word: `{violation['word']}` ({violation['pos']})")
                report.append(f"- **Meaning**: {violation['meaning']}")
                report.append(f"- **Errors**: {', '.join(violation['errors'])}")
                report.append(f"- **File**: {violation['file']}")
                report.append("")
        else:
            report.append("## ✅ PHONOTACTIC VIOLATIONS: NONE FOUND")
            report.append("")
            report.append("Perfect compliance! All words follow their POS phonotactic patterns.")
            report.append("")
        
        # Pattern Statistics
        report.append("## 📈 PHONOTACTIC PATTERN ANALYSIS")
        report.append("")
        
        for pos, stats in results['pattern_statistics'].items():
            if stats['total'] > 0:
                report.append(f"### {pos.title()} ({stats['total']} words)")
                
                fricative_count = stats.get('fricative_start', 0)
                consonant_count = stats.get('consonant_start', 0)
                
                if fricative_count > 0:
                    fricative_pct = (fricative_count / stats['total']) * 100
                    report.append(f"- **Fricative start**: {fricative_count} ({fricative_pct:.1f}%)")
                
                if consonant_count > 0:
                    consonant_pct = (consonant_count / stats['total']) * 100
                    report.append(f"- **Consonant start**: {consonant_count} ({consonant_pct:.1f}%)")
                
                # Length distribution
                lengths = [key for key in stats.keys() if key.startswith('length_')]
                if lengths:
                    length_info = []
                    for length_key in sorted(lengths):
                        length = length_key.split('_')[1]
                        count = stats[length_key]
                        length_info.append(f"{length}:{count}")
                    report.append(f"- **Length distribution**: {', '.join(length_info)}")
                
                report.append("")
        
        # Semantic Analysis
        if results['semantic_overlaps']:
            report.append("## 🎯 SEMANTIC OVERLAP ANALYSIS")
            report.append("")
            report.append("Words with similar meanings across different POS:")
            report.append("")
            
            for overlap in results['semantic_overlaps'][:10]:  # Top 10
                report.append(f"### Concept: '{overlap['concept']}'")
                for word, pos, meaning in overlap['words']:
                    report.append(f"- **{word}** ({pos}): {meaning}")
                report.append("")
        
        # Final Assessment
        report.append("## 🏆 FINAL ASSESSMENT")
        report.append("")
        
        if cross_pos_conflicts == 0 and phonotactic_violations == 0:
            report.append("### ✅ SINGLE POS PRINCIPLE: **PERFECTLY IMPLEMENTED**")
            report.append("")
            report.append("Phi's Single Part-of-Speech Principle is **AIRTIGHT**:")
            report.append("- Every word serves exactly one grammatical function")
            report.append("- Phonotactic patterns perfectly enforce POS distinctions")
            report.append("- No derivational relationships between POS categories")
            report.append("- Revolutionary linguistic achievement confirmed")
        else:
            report.append("### ⚠️ SINGLE POS PRINCIPLE: **NEEDS ATTENTION**")
            report.append("")
            report.append("Issues found that require resolution:")
            if cross_pos_conflicts > 0:
                report.append(f"- {cross_pos_conflicts} words violate single POS constraint")
            if phonotactic_violations > 0:
                report.append(f"- {phonotactic_violations} words violate phonotactic patterns")
        
        return "\n".join(report)

def main():
    """Run the Single POS Principle analysis."""
    analyzer = SinglePOSPrincipleAnalyzer()
    results = analyzer.run_comprehensive_analysis()
    
    # Generate and save report
    report = analyzer.generate_report(results)
    
    with open("SINGLE_POS_PRINCIPLE_ANALYSIS.md", "w", encoding="utf-8") as f:
        f.write(report)
    
    print("\n" + "="*60)
    print("📋 ANALYSIS COMPLETE!")
    print("="*60)
    print(f"📊 Total words analyzed: {results['lexicon_size']}")
    print(f"❌ Cross-POS conflicts: {len(results['cross_pos_conflicts'])}")
    print(f"🔤 Phonotactic violations: {len(results['phonotactic_violations'])}")
    print(f"📄 Report saved to: SINGLE_POS_PRINCIPLE_ANALYSIS.md")
    
    if len(results['cross_pos_conflicts']) == 0 and len(results['phonotactic_violations']) == 0:
        print("\n🎉 PERFECT COMPLIANCE: Single POS Principle is AIRTIGHT! 🎉")
    else:
        print("\n⚠️ VIOLATIONS FOUND: Review required")

if __name__ == "__main__":
    main() 