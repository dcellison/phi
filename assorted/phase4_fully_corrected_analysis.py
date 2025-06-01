#!/usr/bin/env python3
"""
Phase 4 Fully Corrected Analysis: Complete Phonological Unit Accounting

Properly accounts for BOTH fricative digraphs AND vowel pairs as single units.
This gives the true phonological distribution in phi.
"""

import os
import re
from collections import defaultdict, Counter
from pathlib import Path


class Phase4FullyCorrectedAnalyzer:
    """Fully corrected analyzer accounting for all phonological units."""
    
    def __init__(self, pos_dir="pos"):
        self.pos_dir = Path(pos_dir)
        self.consonants = ['h', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w']
        self.vowels = ['i', 'u', 'e', 'o', 'a']
        self.fricatives = ['ph', 'wh', 'th', 'sh']
        
        # All possible vowel pairs (any combination except identical pairs)
        self.vowel_pairs = []
        for v1 in self.vowels:
            for v2 in self.vowels:
                if v1 != v2:  # No identical pairs like 'ii', 'uu'
                    self.vowel_pairs.append(v1 + v2)
        
    def load_all_words(self):
        """Load all words from POS files."""
        print("PHASE 4 FULLY CORRECTED ANALYSIS: Complete Phonological Units")
        print("=" * 75)
        print("Accounting for fricative digraphs AND vowel pairs as single units")
        print()
        
        all_words = []
        
        for pos_file in self.pos_dir.glob("*.md"):
            pos_name = pos_file.stem
            words = self._extract_words_from_file(pos_file, pos_name)
            all_words.extend(words)
        
        print(f"Total words loaded: {len(all_words)}")
        return all_words
    
    def analyze_corrected_phonological_distribution(self, words):
        """Analyze phonological distribution with proper unit accounting."""
        print(f"\n" + "="*75)
        print("CORRECTED PHONOLOGICAL DISTRIBUTION ANALYSIS")
        print("="*75)
        
        # Counters for different phonological units
        standalone_consonants = Counter()
        fricative_digraphs = Counter()
        standalone_vowels = Counter()
        vowel_pairs = Counter()
        
        total_consonant_units = 0
        total_vowel_units = 0
        
        for word_data in words:
            word = word_data['word']
            
            # Parse word into phonological units
            i = 0
            while i < len(word):
                # Check for fricative digraphs first
                if i < len(word) - 1 and word[i:i+2] in self.fricatives:
                    fricative_digraphs[word[i:i+2]] += 1
                    total_consonant_units += 1
                    i += 2
                # Check for vowel pairs
                elif i < len(word) - 1 and word[i:i+2] in self.vowel_pairs:
                    vowel_pairs[word[i:i+2]] += 1
                    total_vowel_units += 1
                    i += 2
                # Check for standalone consonants
                elif word[i] in self.consonants:
                    standalone_consonants[word[i]] += 1
                    total_consonant_units += 1
                    i += 1
                # Check for standalone vowels
                elif word[i] in self.vowels:
                    standalone_vowels[word[i]] += 1
                    total_vowel_units += 1
                    i += 1
                else:
                    i += 1  # Skip unknown characters
        
        print(f"CONSONANT UNITS:")
        print(f"Standalone consonants: {sum(standalone_consonants.values())}")
        print(f"Fricative digraphs: {sum(fricative_digraphs.values())}")
        print(f"Total consonant units: {total_consonant_units}")
        print()
        
        print(f"VOWEL UNITS:")
        print(f"Standalone vowels: {sum(standalone_vowels.values())}")
        print(f"Vowel pairs: {sum(vowel_pairs.values())}")
        print(f"Total vowel units: {total_vowel_units}")
        print()
        
        # Analyze fricative digraph distribution (we know this is balanced)
        if sum(fricative_digraphs.values()) > 0:
            ideal_per_fricative = sum(fricative_digraphs.values()) / len(self.fricatives)
            print(f"FRICATIVE DIGRAPH DISTRIBUTION:")
            print(f"Ideal per fricative: {ideal_per_fricative:.1f} (25%)")
            
            for fricative in self.fricatives:
                count = fricative_digraphs[fricative]
                percentage = (count / sum(fricative_digraphs.values())) * 100
                deviation = count - ideal_per_fricative
                deviation_pct = (deviation / ideal_per_fricative) * 100
                status = "✅" if abs(deviation_pct) <= 10 else "⚠️"
                print(f"  {fricative}: {count:3d} ({percentage:4.1f}%) "
                      f"[{deviation:+5.1f}] ({deviation_pct:+4.1f}%) {status}")
        
        # Analyze standalone consonant distribution
        if sum(standalone_consonants.values()) > 0:
            ideal_per_consonant = sum(standalone_consonants.values()) / len(self.consonants)
            print(f"\nSTANDALONE CONSONANT DISTRIBUTION:")
            print(f"Ideal per consonant: {ideal_per_consonant:.1f} ({100/len(self.consonants):.1f}%)")
            
            consonant_imbalances = []
            for consonant in self.consonants:
                count = standalone_consonants[consonant]
                percentage = (count / sum(standalone_consonants.values())) * 100
                deviation = count - ideal_per_consonant
                deviation_pct = (deviation / ideal_per_consonant) * 100
                
                if abs(deviation_pct) > 20:
                    status = "❌"
                    consonant_imbalances.append((consonant, deviation))
                elif abs(deviation_pct) > 10:
                    status = "⚠️"
                else:
                    status = "✅"
                
                print(f"  {consonant}: {count:3d} ({percentage:4.1f}%) "
                      f"[{deviation:+5.1f}] ({deviation_pct:+4.1f}%) {status}")
        
        # Analyze standalone vowel distribution
        if sum(standalone_vowels.values()) > 0:
            ideal_per_vowel = sum(standalone_vowels.values()) / len(self.vowels)
            print(f"\nSTANDALONE VOWEL DISTRIBUTION:")
            print(f"Ideal per vowel: {ideal_per_vowel:.1f} ({100/len(self.vowels):.1f}%)")
            
            vowel_imbalances = []
            for vowel in self.vowels:
                count = standalone_vowels[vowel]
                percentage = (count / sum(standalone_vowels.values())) * 100
                deviation = count - ideal_per_vowel
                deviation_pct = (deviation / ideal_per_vowel) * 100
                
                if abs(deviation_pct) > 20:
                    status = "❌"
                    vowel_imbalances.append((vowel, deviation))
                elif abs(deviation_pct) > 10:
                    status = "⚠️"
                else:
                    status = "✅"
                
                print(f"  {vowel}: {count:3d} ({percentage:4.1f}%) "
                      f"[{deviation:+5.1f}] ({deviation_pct:+4.1f}%) {status}")
        
        # Analyze vowel pair distribution
        if sum(vowel_pairs.values()) > 0:
            print(f"\nVOWEL PAIR DISTRIBUTION:")
            print(f"Total vowel pairs: {sum(vowel_pairs.values())}")
            print(f"Unique vowel pair types used: {len([vp for vp in vowel_pairs if vowel_pairs[vp] > 0])}")
            
            # Show most common vowel pairs
            most_common_pairs = vowel_pairs.most_common(10)
            print(f"Most common vowel pairs:")
            for pair, count in most_common_pairs:
                percentage = (count / sum(vowel_pairs.values())) * 100
                print(f"  {pair}: {count:3d} ({percentage:4.1f}%)")
        
        # Calculate vowel unit balance (standalone + pairs)
        print(f"\nOVERALL VOWEL UNIT ANALYSIS:")
        print(f"Standalone vowels: {sum(standalone_vowels.values())} units")
        print(f"Vowel pairs: {sum(vowel_pairs.values())} units")
        print(f"Total vowel units: {total_vowel_units}")
        
        standalone_pct = (sum(standalone_vowels.values()) / total_vowel_units) * 100
        pairs_pct = (sum(vowel_pairs.values()) / total_vowel_units) * 100
        
        print(f"Standalone vowels: {standalone_pct:.1f}% of vowel units")
        print(f"Vowel pairs: {pairs_pct:.1f}% of vowel units")
        
        return {
            'standalone_consonants': dict(standalone_consonants),
            'fricative_digraphs': dict(fricative_digraphs),
            'standalone_vowels': dict(standalone_vowels),
            'vowel_pairs': dict(vowel_pairs),
            'totals': {
                'consonant_units': total_consonant_units,
                'vowel_units': total_vowel_units,
                'standalone_vowels': sum(standalone_vowels.values()),
                'vowel_pairs': sum(vowel_pairs.values())
            }
        }
    
    def calculate_fully_corrected_targets(self, phonological_data):
        """Calculate optimization targets with full phonological unit accounting."""
        print(f"\n" + "="*75)
        print("FULLY CORRECTED OPTIMIZATION TARGETS")
        print("="*75)
        
        totals = phonological_data['totals']
        standalone_vowels = phonological_data['standalone_vowels']
        standalone_consonants = phonological_data['standalone_consonants']
        
        print("VOWEL OPTIMIZATION ANALYSIS:")
        print("(Now properly accounting for vowel pairs)")
        
        # Recalculate vowel balance with proper unit accounting
        total_vowel_units = totals['vowel_units']
        standalone_vowel_total = totals['standalone_vowels']
        vowel_pair_total = totals['vowel_pairs']
        
        print(f"Total vowel units: {total_vowel_units}")
        print(f"  Standalone vowels: {standalone_vowel_total} ({standalone_vowel_total/total_vowel_units*100:.1f}%)")
        print(f"  Vowel pairs: {vowel_pair_total} ({vowel_pair_total/total_vowel_units*100:.1f}%)")
        
        # Analyze standalone vowel balance
        if standalone_vowel_total > 0:
            ideal_per_standalone_vowel = standalone_vowel_total / len(self.vowels)
            print(f"\nStandalone vowel balance:")
            print(f"Ideal per vowel: {ideal_per_standalone_vowel:.1f}")
            
            vowel_adjustments = {}
            significant_vowel_imbalances = []
            
            for vowel in self.vowels:
                count = standalone_vowels.get(vowel, 0)
                deviation = count - ideal_per_standalone_vowel
                deviation_pct = (deviation / ideal_per_standalone_vowel) * 100 if ideal_per_standalone_vowel > 0 else 0
                vowel_adjustments[vowel] = -deviation
                
                if abs(deviation_pct) > 15:
                    significant_vowel_imbalances.append((vowel, deviation, deviation_pct))
                
                direction = "add" if -deviation > 0 else "reduce"
                print(f"  {vowel}: {count:3d} -> {direction} {abs(deviation):.1f} ({deviation_pct:+4.1f}%)")
        
        print(f"\nCONSONANT OPTIMIZATION ANALYSIS:")
        print("(Standalone consonants only - fricatives are balanced)")
        
        # Analyze standalone consonant balance
        total_consonant_units = totals['consonant_units']
        standalone_consonant_total = sum(standalone_consonants.values())
        fricative_total = total_consonant_units - standalone_consonant_total
        
        print(f"Total consonant units: {total_consonant_units}")
        print(f"  Standalone consonants: {standalone_consonant_total} ({standalone_consonant_total/total_consonant_units*100:.1f}%)")
        print(f"  Fricative digraphs: {fricative_total} ({fricative_total/total_consonant_units*100:.1f}%)")
        
        if standalone_consonant_total > 0:
            ideal_per_standalone_consonant = standalone_consonant_total / len(self.consonants)
            print(f"\nStandalone consonant balance:")
            print(f"Ideal per consonant: {ideal_per_standalone_consonant:.1f}")
            
            consonant_adjustments = {}
            significant_consonant_imbalances = []
            
            for consonant in self.consonants:
                count = standalone_consonants.get(consonant, 0)
                deviation = count - ideal_per_standalone_consonant
                deviation_pct = (deviation / ideal_per_standalone_consonant) * 100 if ideal_per_standalone_consonant > 0 else 0
                consonant_adjustments[consonant] = -deviation
                
                if abs(deviation_pct) > 15:
                    significant_consonant_imbalances.append((consonant, deviation, deviation_pct))
                
                direction = "add" if -deviation > 0 else "reduce"
                print(f"  {consonant}: {count:3d} -> {direction} {abs(deviation):.1f} ({deviation_pct:+4.1f}%)")
        
        # Determine optimization priorities
        print(f"\nOPTIMIZATION PRIORITIES:")
        
        if significant_vowel_imbalances:
            print("VOWEL OPTIMIZATION NEEDED:")
            for vowel, deviation, pct in significant_vowel_imbalances:
                direction = "reduce" if deviation > 0 else "increase"
                print(f"  {vowel}: {direction} by {abs(deviation):.0f} instances ({pct:+.1f}%)")
        else:
            print("✅ Vowel distribution is reasonably balanced")
        
        if significant_consonant_imbalances:
            print("CONSONANT OPTIMIZATION NEEDED:")
            for consonant, deviation, pct in significant_consonant_imbalances:
                direction = "reduce" if deviation > 0 else "increase"
                print(f"  {consonant}: {direction} by {abs(deviation):.0f} instances ({pct:+.1f}%)")
        else:
            print("✅ Consonant distribution is reasonably balanced")
        
        return {
            'vowel_adjustments': vowel_adjustments if 'vowel_adjustments' in locals() else {},
            'consonant_adjustments': consonant_adjustments if 'consonant_adjustments' in locals() else {},
            'significant_vowel_imbalances': significant_vowel_imbalances if 'significant_vowel_imbalances' in locals() else [],
            'significant_consonant_imbalances': significant_consonant_imbalances if 'significant_consonant_imbalances' in locals() else []
        }
    
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
                        'pos': pos_name
                    })
        
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
        
        return words
    
    def run_fully_corrected_analysis(self):
        """Run complete fully corrected analysis."""
        words = self.load_all_words()
        phonological_data = self.analyze_corrected_phonological_distribution(words)
        targets = self.calculate_fully_corrected_targets(phonological_data)
        
        print(f"\n" + "="*75)
        print("FULLY CORRECTED PHASE 4 ANALYSIS COMPLETE")
        print("="*75)
        
        print("Key insights:")
        print("1. Fricative digraphs are balanced (from Phase 3)")
        print("2. Vowel pairs provide additional vowel unit complexity")
        print("3. True imbalances are in standalone vowel/consonant distribution")
        print("4. Optimization should focus on standalone units only")
        
        return {
            'phonological_data': phonological_data,
            'targets': targets
        }


def main():
    """Main function to run fully corrected analysis."""
    analyzer = Phase4FullyCorrectedAnalyzer()
    results = analyzer.run_fully_corrected_analysis()


if __name__ == "__main__":
    main() 