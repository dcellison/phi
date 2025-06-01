#!/usr/bin/env python3
"""
Comprehensive Phonological Analysis for Phi

Analyzes various phonological distributions beyond fricatives to identify
potential imbalances in consonants, vowels, syllable patterns, and more.
"""

import os
import re
from collections import defaultdict, Counter
from pathlib import Path


class ComprehensivePhonologicalAnalyzer:
    """Analyzes multiple phonological distributions in phi."""
    
    def __init__(self, pos_dir="pos"):
        self.pos_dir = Path(pos_dir)
        self.consonants = ['h', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w']
        self.vowels = ['i', 'u', 'e', 'o', 'a']
        self.fricatives = ['ph', 'wh', 'th', 'sh']
        self.pos_data = {}
        
    def load_all_words(self):
        """Load all words from POS files."""
        print("COMPREHENSIVE PHONOLOGICAL ANALYSIS")
        print("=" * 60)
        print("Loading all words from POS files...")
        
        all_words = []
        pos_counts = {}
        
        for pos_file in self.pos_dir.glob("*.md"):
            pos_name = pos_file.stem
            words = self._extract_words_from_file(pos_file, pos_name)
            
            if words:
                all_words.extend(words)
                pos_counts[pos_name] = len(words)
                print(f"  {pos_name}: {len(words)} words")
        
        print(f"\nTotal words loaded: {len(all_words)}")
        print(f"POS categories: {len(pos_counts)}")
        
        return all_words, pos_counts
    
    def _extract_words_from_file(self, file_path, pos_name):
        """Extract all words from a POS file."""
        words = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find table rows with phi words
            pattern = r'\|\s*([a-z]+)\s*\|\s*([^|]+)\s*\|'
            matches = re.findall(pattern, content)
            
            for word, meaning in matches:
                word = word.strip()
                meaning = meaning.strip()
                if (word not in ['phi', 'word', 'english', 'translation'] and
                    len(word) > 1 and word.isalpha()):
                    words.append({
                        'word': word,
                        'meaning': meaning,
                        'pos': pos_name,
                        'length': len(word)
                    })
        
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
        
        return words
    
    def analyze_consonant_distribution(self, words):
        """Analyze distribution of individual consonants."""
        print(f"\n" + "="*60)
        print("CONSONANT DISTRIBUTION ANALYSIS")
        print("="*60)
        
        consonant_counts = Counter()
        total_consonants = 0
        
        for word_data in words:
            word = word_data['word']
            for char in word:
                if char in self.consonants:
                    consonant_counts[char] += 1
                    total_consonants += 1
        
        ideal_per_consonant = total_consonants / len(self.consonants)
        
        print(f"Total consonant instances: {total_consonants}")
        print(f"Ideal per consonant: {ideal_per_consonant:.1f} ({100/len(self.consonants):.1f}%)")
        print()
        
        deviations = []
        for consonant in sorted(self.consonants):
            count = consonant_counts[consonant]
            percentage = (count / total_consonants) * 100
            deviation = count - ideal_per_consonant
            deviation_pct = (deviation / ideal_per_consonant) * 100
            deviations.append(abs(deviation))
            
            status = "✅" if abs(deviation_pct) <= 15 else "⚠️" if abs(deviation_pct) <= 25 else "❌"
            print(f"  {consonant}: {count:3d} ({percentage:4.1f}%) "
                  f"[{deviation:+5.1f}] ({deviation_pct:+4.1f}%) {status}")
        
        avg_deviation = sum(deviations) / len(deviations)
        print(f"\nAverage deviation: {avg_deviation:.1f} instances")
        
        if avg_deviation > ideal_per_consonant * 0.2:
            print("⚠️  Consonant distribution shows significant imbalance")
        else:
            print("✅ Consonant distribution is reasonably balanced")
        
        return consonant_counts, avg_deviation
    
    def analyze_vowel_distribution(self, words):
        """Analyze distribution of individual vowels."""
        print(f"\n" + "="*60)
        print("VOWEL DISTRIBUTION ANALYSIS")
        print("="*60)
        
        vowel_counts = Counter()
        total_vowels = 0
        
        for word_data in words:
            word = word_data['word']
            for char in word:
                if char in self.vowels:
                    vowel_counts[char] += 1
                    total_vowels += 1
        
        ideal_per_vowel = total_vowels / len(self.vowels)
        
        print(f"Total vowel instances: {total_vowels}")
        print(f"Ideal per vowel: {ideal_per_vowel:.1f} ({100/len(self.vowels):.1f}%)")
        print()
        
        deviations = []
        for vowel in sorted(self.vowels):
            count = vowel_counts[vowel]
            percentage = (count / total_vowels) * 100
            deviation = count - ideal_per_vowel
            deviation_pct = (deviation / ideal_per_vowel) * 100
            deviations.append(abs(deviation))
            
            status = "✅" if abs(deviation_pct) <= 15 else "⚠️" if abs(deviation_pct) <= 25 else "❌"
            print(f"  {vowel}: {count:3d} ({percentage:4.1f}%) "
                  f"[{deviation:+5.1f}] ({deviation_pct:+4.1f}%) {status}")
        
        avg_deviation = sum(deviations) / len(deviations)
        print(f"\nAverage deviation: {avg_deviation:.1f} instances")
        
        if avg_deviation > ideal_per_vowel * 0.2:
            print("⚠️  Vowel distribution shows significant imbalance")
        else:
            print("✅ Vowel distribution is reasonably balanced")
        
        return vowel_counts, avg_deviation
    
    def analyze_word_length_distribution(self, words):
        """Analyze distribution of word lengths."""
        print(f"\n" + "="*60)
        print("WORD LENGTH DISTRIBUTION ANALYSIS")
        print("="*60)
        
        length_counts = Counter()
        for word_data in words:
            length_counts[word_data['length']] += 1
        
        total_words = len(words)
        
        print(f"Total words: {total_words}")
        print()
        
        for length in sorted(length_counts.keys()):
            count = length_counts[length]
            percentage = (count / total_words) * 100
            print(f"  {length} chars: {count:3d} words ({percentage:4.1f}%)")
        
        # Check for reasonable distribution (most words should be 4-7 characters)
        short_words = sum(length_counts[i] for i in range(1, 4))
        medium_words = sum(length_counts[i] for i in range(4, 8))
        long_words = sum(length_counts[i] for i in range(8, 15))
        
        print(f"\nLength categories:")
        print(f"  Short (1-3 chars): {short_words} ({short_words/total_words*100:.1f}%)")
        print(f"  Medium (4-7 chars): {medium_words} ({medium_words/total_words*100:.1f}%)")
        print(f"  Long (8+ chars): {long_words} ({long_words/total_words*100:.1f}%)")
        
        if medium_words / total_words < 0.6:
            print("⚠️  Word length distribution may be suboptimal")
        else:
            print("✅ Word length distribution appears reasonable")
        
        return length_counts
    
    def analyze_initial_consonant_distribution(self, words):
        """Analyze distribution of word-initial consonants."""
        print(f"\n" + "="*60)
        print("INITIAL CONSONANT DISTRIBUTION ANALYSIS")
        print("="*60)
        
        initial_counts = Counter()
        fricative_initial_counts = Counter()
        
        for word_data in words:
            word = word_data['word']
            
            # Check for fricative digraph first
            if len(word) >= 2 and word[:2] in self.fricatives:
                fricative_initial_counts[word[:2]] += 1
            elif word[0] in self.consonants:
                initial_counts[word[0]] += 1
        
        total_consonant_initial = sum(initial_counts.values())
        total_fricative_initial = sum(fricative_initial_counts.values())
        total_initial = total_consonant_initial + total_fricative_initial
        
        print(f"Words starting with consonants: {total_consonant_initial}")
        print(f"Words starting with fricatives: {total_fricative_initial}")
        print(f"Total: {total_initial}")
        print()
        
        print("Single consonant initials:")
        if total_consonant_initial > 0:
            ideal_per_consonant = total_consonant_initial / len(self.consonants)
            for consonant in sorted(self.consonants):
                count = initial_counts[consonant]
                percentage = (count / total_consonant_initial) * 100 if total_consonant_initial > 0 else 0
                deviation = count - ideal_per_consonant
                deviation_pct = (deviation / ideal_per_consonant) * 100 if ideal_per_consonant > 0 else 0
                
                status = "✅" if abs(deviation_pct) <= 20 else "⚠️" if abs(deviation_pct) <= 35 else "❌"
                print(f"  {consonant}: {count:3d} ({percentage:4.1f}%) "
                      f"[{deviation:+5.1f}] ({deviation_pct:+4.1f}%) {status}")
        
        print("\nFricative digraph initials:")
        if total_fricative_initial > 0:
            ideal_per_fricative = total_fricative_initial / len(self.fricatives)
            for fricative in self.fricatives:
                count = fricative_initial_counts[fricative]
                percentage = (count / total_fricative_initial) * 100 if total_fricative_initial > 0 else 0
                deviation = count - ideal_per_fricative
                deviation_pct = (deviation / ideal_per_fricative) * 100 if ideal_per_fricative > 0 else 0
                
                status = "✅" if abs(deviation_pct) <= 10 else "⚠️" if abs(deviation_pct) <= 20 else "❌"
                print(f"  {fricative}: {count:3d} ({percentage:4.1f}%) "
                      f"[{deviation:+5.1f}] ({deviation_pct:+4.1f}%) {status}")
        
        return initial_counts, fricative_initial_counts
    
    def analyze_syllable_patterns(self, words):
        """Analyze syllable structure patterns."""
        print(f"\n" + "="*60)
        print("SYLLABLE PATTERN ANALYSIS")
        print("="*60)
        
        syllable_counts = Counter()
        cv_patterns = Counter()
        
        for word_data in words:
            word = word_data['word']
            syllables = self._count_syllables(word)
            syllable_counts[syllables] += 1
            
            # Analyze CV pattern
            pattern = self._get_cv_pattern(word)
            cv_patterns[pattern] += 1
        
        total_words = len(words)
        
        print("Syllable count distribution:")
        for syllables in sorted(syllable_counts.keys()):
            count = syllable_counts[syllables]
            percentage = (count / total_words) * 100
            print(f"  {syllables} syllables: {count:3d} words ({percentage:4.1f}%)")
        
        print(f"\nMost common CV patterns:")
        for pattern, count in cv_patterns.most_common(10):
            percentage = (count / total_words) * 100
            print(f"  {pattern}: {count:3d} words ({percentage:4.1f}%)")
        
        return syllable_counts, cv_patterns
    
    def _count_syllables(self, word):
        """Count syllables in a word (approximation based on vowel groups)."""
        vowel_groups = 0
        prev_was_vowel = False
        
        i = 0
        while i < len(word):
            # Check for fricative digraphs first
            if i < len(word) - 1 and word[i:i+2] in self.fricatives:
                prev_was_vowel = False
                i += 2
            elif word[i] in self.vowels:
                if not prev_was_vowel:
                    vowel_groups += 1
                prev_was_vowel = True
                i += 1
            else:
                prev_was_vowel = False
                i += 1
        
        return max(1, vowel_groups)  # At least 1 syllable
    
    def _get_cv_pattern(self, word):
        """Get consonant-vowel pattern of a word."""
        pattern = ""
        i = 0
        
        while i < len(word):
            # Check for fricative digraphs first
            if i < len(word) - 1 and word[i:i+2] in self.fricatives:
                pattern += "F"  # Fricative
                i += 2
            elif word[i] in self.consonants:
                pattern += "C"
                i += 1
            elif word[i] in self.vowels:
                pattern += "V"
                i += 1
            else:
                i += 1
        
        return pattern
    
    def analyze_pos_phonological_patterns(self, words):
        """Analyze phonological patterns by part of speech."""
        print(f"\n" + "="*60)
        print("POS-SPECIFIC PHONOLOGICAL PATTERNS")
        print("="*60)
        
        pos_groups = defaultdict(list)
        for word_data in words:
            pos_groups[word_data['pos']].append(word_data)
        
        for pos, pos_words in pos_groups.items():
            if len(pos_words) < 10:  # Skip small categories
                continue
                
            print(f"\n{pos.upper()} ({len(pos_words)} words):")
            
            # Average word length
            avg_length = sum(w['length'] for w in pos_words) / len(pos_words)
            print(f"  Average length: {avg_length:.1f} characters")
            
            # Initial consonant/fricative distribution
            initial_consonants = 0
            initial_fricatives = 0
            
            for word_data in pos_words:
                word = word_data['word']
                if len(word) >= 2 and word[:2] in self.fricatives:
                    initial_fricatives += 1
                elif word[0] in self.consonants:
                    initial_consonants += 1
            
            total_analyzed = initial_consonants + initial_fricatives
            if total_analyzed > 0:
                consonant_pct = (initial_consonants / total_analyzed) * 100
                fricative_pct = (initial_fricatives / total_analyzed) * 100
                print(f"  Initial consonants: {consonant_pct:.1f}%")
                print(f"  Initial fricatives: {fricative_pct:.1f}%")
    
    def run_comprehensive_analysis(self):
        """Run complete phonological analysis."""
        words, pos_counts = self.load_all_words()
        
        # Run all analyses
        consonant_results = self.analyze_consonant_distribution(words)
        vowel_results = self.analyze_vowel_distribution(words)
        length_results = self.analyze_word_length_distribution(words)
        initial_results = self.analyze_initial_consonant_distribution(words)
        syllable_results = self.analyze_syllable_patterns(words)
        self.analyze_pos_phonological_patterns(words)
        
        # Summary of findings
        print(f"\n" + "="*60)
        print("COMPREHENSIVE ANALYSIS SUMMARY")
        print("="*60)
        
        issues_found = []
        
        if consonant_results[1] > 20:  # High average deviation
            issues_found.append("Consonant distribution imbalance")
        
        if vowel_results[1] > 15:  # High average deviation
            issues_found.append("Vowel distribution imbalance")
        
        if issues_found:
            print("Potential issues identified:")
            for issue in issues_found:
                print(f"  ⚠️  {issue}")
        else:
            print("✅ No major phonological imbalances detected!")
        
        print(f"\nOverall assessment: Phi shows {'good' if len(issues_found) <= 1 else 'moderate'} phonological balance")
        
        return {
            'consonants': consonant_results,
            'vowels': vowel_results,
            'lengths': length_results,
            'initials': initial_results,
            'syllables': syllable_results,
            'issues': issues_found
        }


def main():
    """Main function to run comprehensive phonological analysis."""
    analyzer = ComprehensivePhonologicalAnalyzer()
    results = analyzer.run_comprehensive_analysis()
    
    print(f"\n" + "="*60)
    print("COMPREHENSIVE PHONOLOGICAL ANALYSIS COMPLETE")
    print("="*60)


if __name__ == "__main__":
    main() 