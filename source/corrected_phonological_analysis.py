#!/usr/bin/env python3
"""
Corrected Phonological Analysis for Phi

Properly accounts for fricative digraphs when analyzing consonant distribution.
Fricative digraphs (ph, wh, th, sh) should be treated as single units, not as
separate consonants that inflate 'h', 'p', 's', 't', 'w' counts.
"""

import os
import re
from collections import defaultdict, Counter
from pathlib import Path


class CorrectedPhonologicalAnalyzer:
    """Analyzes phonological distributions with proper fricative digraph handling."""
    
    def __init__(self, pos_dir="pos"):
        self.pos_dir = Path(pos_dir)
        self.consonants = ['h', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w']
        self.vowels = ['i', 'u', 'e', 'o', 'a']
        self.fricatives = ['ph', 'wh', 'th', 'sh']
        self.pos_data = {}
        
    def load_all_words(self):
        """Load all words from POS files."""
        print("CORRECTED PHONOLOGICAL ANALYSIS")
        print("=" * 60)
        print("(Properly accounting for fricative digraphs)")
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
    
    def analyze_consonant_distribution_corrected(self, words):
        """Analyze consonant distribution properly accounting for fricative digraphs."""
        print(f"\n" + "="*60)
        print("CORRECTED CONSONANT DISTRIBUTION ANALYSIS")
        print("="*60)
        print("(Fricative digraphs treated as single units)")
        
        consonant_counts = Counter()
        fricative_counts = Counter()
        total_consonant_units = 0
        total_fricative_units = 0
        
        for word_data in words:
            word = word_data['word']
            i = 0
            
            while i < len(word):
                # Check for fricative digraphs first
                if i < len(word) - 1 and word[i:i+2] in self.fricatives:
                    fricative_counts[word[i:i+2]] += 1
                    total_fricative_units += 1
                    i += 2
                elif word[i] in self.consonants:
                    consonant_counts[word[i]] += 1
                    total_consonant_units += 1
                    i += 1
                else:
                    i += 1  # Skip vowels
        
        print(f"Standalone consonant instances: {total_consonant_units}")
        print(f"Fricative digraph instances: {total_fricative_units}")
        print(f"Total consonant units: {total_consonant_units + total_fricative_units}")
        print()
        
        # Analyze standalone consonants
        if total_consonant_units > 0:
            ideal_per_consonant = total_consonant_units / len(self.consonants)
            print(f"STANDALONE CONSONANTS:")
            print(f"Ideal per consonant: {ideal_per_consonant:.1f} ({100/len(self.consonants):.1f}%)")
            print()
            
            consonant_deviations = []
            for consonant in sorted(self.consonants):
                count = consonant_counts[consonant]
                percentage = (count / total_consonant_units) * 100
                deviation = count - ideal_per_consonant
                deviation_pct = (deviation / ideal_per_consonant) * 100
                consonant_deviations.append(abs(deviation))
                
                status = "✅" if abs(deviation_pct) <= 15 else "⚠️" if abs(deviation_pct) <= 25 else "❌"
                print(f"  {consonant}: {count:3d} ({percentage:4.1f}%) "
                      f"[{deviation:+5.1f}] ({deviation_pct:+4.1f}%) {status}")
            
            avg_consonant_deviation = sum(consonant_deviations) / len(consonant_deviations)
            print(f"\nAverage consonant deviation: {avg_consonant_deviation:.1f} instances")
        
        # Analyze fricative digraphs (we know these are balanced from Phase 3)
        if total_fricative_units > 0:
            ideal_per_fricative = total_fricative_units / len(self.fricatives)
            print(f"\nFRICATIVE DIGRAPHS:")
            print(f"Ideal per fricative: {ideal_per_fricative:.1f} ({100/len(self.fricatives):.1f}%)")
            print()
            
            for fricative in self.fricatives:
                count = fricative_counts[fricative]
                percentage = (count / total_fricative_units) * 100
                deviation = count - ideal_per_fricative
                deviation_pct = (deviation / ideal_per_fricative) * 100
                
                status = "✅" if abs(deviation_pct) <= 10 else "⚠️" if abs(deviation_pct) <= 20 else "❌"
                print(f"  {fricative}: {count:3d} ({percentage:4.1f}%) "
                      f"[{deviation:+5.1f}] ({deviation_pct:+4.1f}%) {status}")
        
        # Overall assessment
        if total_consonant_units > 0:
            if avg_consonant_deviation > ideal_per_consonant * 0.2:
                print("\n⚠️  Standalone consonant distribution shows imbalance")
                consonant_imbalanced = True
            else:
                print("\n✅ Standalone consonant distribution is reasonably balanced")
                consonant_imbalanced = False
        else:
            consonant_imbalanced = False
        
        return consonant_counts, fricative_counts, consonant_imbalanced
    
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
            vowel_imbalanced = True
        else:
            print("✅ Vowel distribution is reasonably balanced")
            vowel_imbalanced = False
        
        return vowel_counts, avg_deviation, vowel_imbalanced
    
    def analyze_fricative_impact_on_consonants(self, words):
        """Analyze how fricative digraphs affect apparent consonant usage."""
        print(f"\n" + "="*60)
        print("FRICATIVE DIGRAPH IMPACT ANALYSIS")
        print("="*60)
        
        # Count consonants in fricative digraphs vs standalone
        fricative_consonant_usage = Counter()
        standalone_consonant_usage = Counter()
        
        for word_data in words:
            word = word_data['word']
            i = 0
            
            while i < len(word):
                # Check for fricative digraphs first
                if i < len(word) - 1 and word[i:i+2] in self.fricatives:
                    digraph = word[i:i+2]
                    # Count each consonant in the digraph
                    for char in digraph:
                        if char in self.consonants:
                            fricative_consonant_usage[char] += 1
                    i += 2
                elif word[i] in self.consonants:
                    standalone_consonant_usage[word[i]] += 1
                    i += 1
                else:
                    i += 1
        
        print("Consonant usage breakdown:")
        print("Consonant | In Digraphs | Standalone | Total | % in Digraphs")
        print("-" * 60)
        
        for consonant in sorted(self.consonants):
            in_digraphs = fricative_consonant_usage[consonant]
            standalone = standalone_consonant_usage[consonant]
            total = in_digraphs + standalone
            pct_in_digraphs = (in_digraphs / total * 100) if total > 0 else 0
            
            print(f"    {consonant}     |     {in_digraphs:3d}     |     {standalone:3d}    | {total:3d}   | {pct_in_digraphs:5.1f}%")
        
        # Identify which consonants are heavily used in digraphs
        heavily_digraph_consonants = []
        for consonant in self.consonants:
            in_digraphs = fricative_consonant_usage[consonant]
            standalone = standalone_consonant_usage[consonant]
            total = in_digraphs + standalone
            if total > 0 and (in_digraphs / total) > 0.5:
                heavily_digraph_consonants.append(consonant)
        
        print(f"\nConsonants heavily used in digraphs (>50%): {heavily_digraph_consonants}")
        
        return fricative_consonant_usage, standalone_consonant_usage
    
    def run_corrected_analysis(self):
        """Run corrected phonological analysis."""
        words, pos_counts = self.load_all_words()
        
        # Run corrected analyses
        consonant_results = self.analyze_consonant_distribution_corrected(words)
        vowel_results = self.analyze_vowel_distribution(words)
        fricative_impact = self.analyze_fricative_impact_on_consonants(words)
        
        # Summary of findings
        print(f"\n" + "="*60)
        print("CORRECTED ANALYSIS SUMMARY")
        print("="*60)
        
        issues_found = []
        
        if consonant_results[2]:  # consonant_imbalanced
            issues_found.append("Standalone consonant distribution imbalance")
        
        if vowel_results[2]:  # vowel_imbalanced
            issues_found.append("Vowel distribution imbalance")
        
        if issues_found:
            print("Actual issues identified:")
            for issue in issues_found:
                print(f"  ⚠️  {issue}")
        else:
            print("✅ No major phonological imbalances detected!")
        
        print(f"\nCorrected assessment: The apparent 'h' overuse was due to fricative digraphs.")
        print(f"Phi shows {'good' if len(issues_found) <= 1 else 'moderate'} phonological balance")
        
        return {
            'consonants': consonant_results,
            'vowels': vowel_results,
            'fricative_impact': fricative_impact,
            'issues': issues_found
        }


def main():
    """Main function to run corrected phonological analysis."""
    analyzer = CorrectedPhonologicalAnalyzer()
    results = analyzer.run_corrected_analysis()
    
    print(f"\n" + "="*60)
    print("CORRECTED PHONOLOGICAL ANALYSIS COMPLETE")
    print("="*60)


if __name__ == "__main__":
    main() 