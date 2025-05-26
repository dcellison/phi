#!/usr/bin/env python3
"""
Phase 4 True Phonological Analysis

Treats ALL phonological units as completely independent:
- Fricative digraphs (ph, wh, th, sh) as single units
- Vowel pairs (ai, eu, etc.) as single units  
- Standalone consonants as separate units
- Standalone vowels as separate units

No cross-contamination between unit types in frequency analysis.
"""

import os
import re
from collections import defaultdict, Counter
from pathlib import Path


class Phase4TruePhonologicalAnalyzer:
    """True phonological analyzer with complete unit independence."""
    
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
        print("PHASE 4 TRUE PHONOLOGICAL ANALYSIS")
        print("=" * 75)
        print("Complete unit independence: no cross-contamination between unit types")
        print()
        
        all_words = []
        
        for pos_file in self.pos_dir.glob("*.md"):
            pos_name = pos_file.stem
            words = self._extract_words_from_file(pos_file, pos_name)
            all_words.extend(words)
        
        print(f"Total words loaded: {len(all_words)}")
        return all_words
    
    def analyze_true_phonological_distribution(self, words):
        """Analyze phonological distribution with complete unit independence."""
        print(f"\n" + "="*75)
        print("TRUE PHONOLOGICAL DISTRIBUTION ANALYSIS")
        print("="*75)
        print("Each unit type analyzed independently")
        print()
        
        # Counters for different phonological unit TYPES
        standalone_consonants = Counter()
        fricative_digraphs = Counter()
        standalone_vowels = Counter()
        vowel_pairs = Counter()
        
        for word_data in words:
            word = word_data['word']
            
            # Parse word into phonological units
            i = 0
            while i < len(word):
                # Check for fricative digraphs first (highest priority)
                if i < len(word) - 1 and word[i:i+2] in self.fricatives:
                    fricative_digraphs[word[i:i+2]] += 1
                    i += 2
                # Check for vowel pairs (second priority)
                elif i < len(word) - 1 and word[i:i+2] in self.vowel_pairs:
                    vowel_pairs[word[i:i+2]] += 1
                    i += 2
                # Check for standalone consonants (third priority)
                elif word[i] in self.consonants:
                    standalone_consonants[word[i]] += 1
                    i += 1
                # Check for standalone vowels (fourth priority)
                elif word[i] in self.vowels:
                    standalone_vowels[word[i]] += 1
                    i += 1
                else:
                    i += 1  # Skip unknown characters
        
        # Analyze each unit type INDEPENDENTLY
        results = {}
        
        # 1. FRICATIVE DIGRAPHS (independent analysis)
        print("1. FRICATIVE DIGRAPH DISTRIBUTION:")
        print("   (Analyzed independently - balanced from Phase 3)")
        fricative_total = sum(fricative_digraphs.values())
        if fricative_total > 0:
            ideal_per_fricative = fricative_total / len(self.fricatives)
            print(f"   Total fricative units: {fricative_total}")
            print(f"   Ideal per fricative: {ideal_per_fricative:.1f} (25%)")
            
            fricative_imbalances = []
            for fricative in self.fricatives:
                count = fricative_digraphs[fricative]
                percentage = (count / fricative_total) * 100
                deviation = count - ideal_per_fricative
                deviation_pct = (deviation / ideal_per_fricative) * 100
                
                if abs(deviation_pct) > 15:
                    status = "❌"
                    fricative_imbalances.append((fricative, deviation, deviation_pct))
                elif abs(deviation_pct) > 7:
                    status = "⚠️"
                else:
                    status = "✅"
                
                print(f"     {fricative}: {count:3d} ({percentage:4.1f}%) "
                      f"[{deviation:+5.1f}] ({deviation_pct:+4.1f}%) {status}")
            
            results['fricatives'] = {
                'total': fricative_total,
                'distribution': dict(fricative_digraphs),
                'imbalances': fricative_imbalances
            }
        
        # 2. STANDALONE CONSONANTS (independent analysis)
        print(f"\n2. STANDALONE CONSONANT DISTRIBUTION:")
        print("   (Analyzed independently - no fricative contamination)")
        consonant_total = sum(standalone_consonants.values())
        if consonant_total > 0:
            ideal_per_consonant = consonant_total / len(self.consonants)
            print(f"   Total standalone consonant units: {consonant_total}")
            print(f"   Ideal per consonant: {ideal_per_consonant:.1f} ({100/len(self.consonants):.1f}%)")
            
            consonant_imbalances = []
            for consonant in self.consonants:
                count = standalone_consonants[consonant]
                percentage = (count / consonant_total) * 100
                deviation = count - ideal_per_consonant
                deviation_pct = (deviation / ideal_per_consonant) * 100
                
                if abs(deviation_pct) > 20:
                    status = "❌"
                    consonant_imbalances.append((consonant, deviation, deviation_pct))
                elif abs(deviation_pct) > 10:
                    status = "⚠️"
                else:
                    status = "✅"
                
                print(f"     {consonant}: {count:3d} ({percentage:4.1f}%) "
                      f"[{deviation:+5.1f}] ({deviation_pct:+4.1f}%) {status}")
            
            results['standalone_consonants'] = {
                'total': consonant_total,
                'distribution': dict(standalone_consonants),
                'imbalances': consonant_imbalances
            }
        
        # 3. STANDALONE VOWELS (independent analysis)
        print(f"\n3. STANDALONE VOWEL DISTRIBUTION:")
        print("   (Analyzed independently - no vowel pair contamination)")
        vowel_total = sum(standalone_vowels.values())
        if vowel_total > 0:
            ideal_per_vowel = vowel_total / len(self.vowels)
            print(f"   Total standalone vowel units: {vowel_total}")
            print(f"   Ideal per vowel: {ideal_per_vowel:.1f} ({100/len(self.vowels):.1f}%)")
            
            vowel_imbalances = []
            for vowel in self.vowels:
                count = standalone_vowels[vowel]
                percentage = (count / vowel_total) * 100
                deviation = count - ideal_per_vowel
                deviation_pct = (deviation / ideal_per_vowel) * 100
                
                if abs(deviation_pct) > 20:
                    status = "❌"
                    vowel_imbalances.append((vowel, deviation, deviation_pct))
                elif abs(deviation_pct) > 10:
                    status = "⚠️"
                else:
                    status = "✅"
                
                print(f"     {vowel}: {count:3d} ({percentage:4.1f}%) "
                      f"[{deviation:+5.1f}] ({deviation_pct:+4.1f}%) {status}")
            
            results['standalone_vowels'] = {
                'total': vowel_total,
                'distribution': dict(standalone_vowels),
                'imbalances': vowel_imbalances
            }
        
        # 4. VOWEL PAIRS (independent analysis)
        print(f"\n4. VOWEL PAIR DISTRIBUTION:")
        print("   (Analyzed independently - descriptive only)")
        pair_total = sum(vowel_pairs.values())
        if pair_total > 0:
            print(f"   Total vowel pair units: {pair_total}")
            print(f"   Unique vowel pair types used: {len([vp for vp in vowel_pairs if vowel_pairs[vp] > 0])}")
            
            # Show most common vowel pairs (descriptive, not prescriptive)
            most_common_pairs = vowel_pairs.most_common(10)
            print(f"   Most common vowel pairs:")
            for pair, count in most_common_pairs:
                percentage = (count / pair_total) * 100
                print(f"     {pair}: {count:3d} ({percentage:4.1f}%)")
            
            results['vowel_pairs'] = {
                'total': pair_total,
                'distribution': dict(vowel_pairs),
                'most_common': most_common_pairs
            }
        
        return results
    
    def calculate_true_optimization_targets(self, phonological_results):
        """Calculate optimization targets with complete unit independence."""
        print(f"\n" + "="*75)
        print("TRUE OPTIMIZATION TARGETS")
        print("="*75)
        print("Each unit type optimized independently")
        print()
        
        optimization_needed = []
        
        # 1. Fricative digraphs (should be balanced from Phase 3)
        if 'fricatives' in phonological_results:
            fricative_imbalances = phonological_results['fricatives']['imbalances']
            if fricative_imbalances:
                print("1. FRICATIVE DIGRAPH OPTIMIZATION:")
                for fricative, deviation, pct in fricative_imbalances:
                    direction = "reduce" if deviation > 0 else "increase"
                    print(f"   {fricative}: {direction} by {abs(deviation):.0f} units ({pct:+.1f}%)")
                optimization_needed.append('fricatives')
            else:
                print("1. FRICATIVE DIGRAPHS: ✅ Balanced (no optimization needed)")
        
        # 2. Standalone consonants
        if 'standalone_consonants' in phonological_results:
            consonant_imbalances = phonological_results['standalone_consonants']['imbalances']
            if consonant_imbalances:
                print("\n2. STANDALONE CONSONANT OPTIMIZATION:")
                overused_consonants = []
                underused_consonants = []
                
                for consonant, deviation, pct in consonant_imbalances:
                    direction = "reduce" if deviation > 0 else "increase"
                    print(f"   {consonant}: {direction} by {abs(deviation):.0f} units ({pct:+.1f}%)")
                    
                    if deviation > 0:
                        overused_consonants.append((consonant, abs(deviation)))
                    else:
                        underused_consonants.append((consonant, abs(deviation)))
                
                # Suggest conversions within standalone consonants only
                if overused_consonants and underused_consonants:
                    print("   Suggested standalone consonant conversions:")
                    for (over_cons, over_amt), (under_cons, under_amt) in zip(overused_consonants, underused_consonants):
                        conversion_amt = min(over_amt, under_amt)
                        print(f"     {over_cons} → {under_cons}: {conversion_amt:.0f} conversions")
                
                optimization_needed.append('standalone_consonants')
            else:
                print("\n2. STANDALONE CONSONANTS: ✅ Balanced (no optimization needed)")
        
        # 3. Standalone vowels
        if 'standalone_vowels' in phonological_results:
            vowel_imbalances = phonological_results['standalone_vowels']['imbalances']
            if vowel_imbalances:
                print("\n3. STANDALONE VOWEL OPTIMIZATION:")
                overused_vowels = []
                underused_vowels = []
                
                for vowel, deviation, pct in vowel_imbalances:
                    direction = "reduce" if deviation > 0 else "increase"
                    print(f"   {vowel}: {direction} by {abs(deviation):.0f} units ({pct:+.1f}%)")
                    
                    if deviation > 0:
                        overused_vowels.append((vowel, abs(deviation)))
                    else:
                        underused_vowels.append((vowel, abs(deviation)))
                
                # Suggest conversions within standalone vowels only
                if overused_vowels and underused_vowels:
                    print("   Suggested standalone vowel conversions:")
                    for (over_vowel, over_amt), (under_vowel, under_amt) in zip(overused_vowels, underused_vowels):
                        conversion_amt = min(over_amt, under_amt)
                        print(f"     {over_vowel} → {under_vowel}: {conversion_amt:.0f} conversions")
                
                optimization_needed.append('standalone_vowels')
            else:
                print("\n3. STANDALONE VOWELS: ✅ Balanced (no optimization needed)")
        
        # 4. Vowel pairs (descriptive only - no optimization targets)
        print("\n4. VOWEL PAIRS: Descriptive analysis only (natural distribution)")
        
        return {
            'optimization_needed': optimization_needed,
            'fricative_targets': phonological_results.get('fricatives', {}).get('imbalances', []),
            'consonant_targets': phonological_results.get('standalone_consonants', {}).get('imbalances', []),
            'vowel_targets': phonological_results.get('standalone_vowels', {}).get('imbalances', [])
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
    
    def run_true_phonological_analysis(self):
        """Run complete true phonological analysis."""
        words = self.load_all_words()
        phonological_results = self.analyze_true_phonological_distribution(words)
        targets = self.calculate_true_optimization_targets(phonological_results)
        
        print(f"\n" + "="*75)
        print("TRUE PHONOLOGICAL ANALYSIS COMPLETE")
        print("="*75)
        
        print("Key principles applied:")
        print("1. Complete unit independence - no cross-contamination")
        print("2. Fricative digraphs analyzed separately from component letters")
        print("3. Vowel pairs analyzed separately from component letters")
        print("4. Standalone units analyzed in isolation")
        print("5. Optimization targets respect unit boundaries")
        
        if targets['optimization_needed']:
            print(f"\nOptimization needed for: {', '.join(targets['optimization_needed'])}")
        else:
            print("\n✅ All phonological unit types are balanced!")
        
        return {
            'phonological_results': phonological_results,
            'targets': targets
        }


def main():
    """Main function to run true phonological analysis."""
    analyzer = Phase4TruePhonologicalAnalyzer()
    results = analyzer.run_true_phonological_analysis()


if __name__ == "__main__":
    main() 