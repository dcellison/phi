#!/usr/bin/env python3
"""
Deep Fricative Distribution Analysis for Phi Language

Investigates WHY certain fricatives are over/underused in specific parts of speech
by analyzing positional patterns, phonotactic constraints, and usage distribution.
"""

import os
import re
from collections import defaultdict, Counter
from pathlib import Path


class DeepFricativeAnalyzer:
    """Deep analysis of fricative distribution patterns in phi lexicon."""
    
    def __init__(self, pos_dir="pos"):
        self.pos_dir = Path(pos_dir)
        self.fricatives = ['ph', 'wh', 'th', 'sh']
        self.pos_data = {}
        self.fricative_counts = defaultdict(lambda: defaultdict(int))
        self.positional_counts = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
        self.word_patterns = defaultdict(list)
        
        # Phonotactic patterns for each POS
        self.pos_patterns = {
            'verbs': '[F][V][C][V]',
            'adjectives': '[C][V][F][V]', 
            'nouns': '[C/F][V/P][F][P]',
            'adverbs': '[C][V][C][V][C][V]',
            'prepositions': '[F][P]',
            'determiners': '[F][P][C][V]',
            'classifiers': '[C][P]',
            'conjunctions': '[C][V][C][V]',
            'interjections': '[C][V][C][P]',
            'numbers': '[F][V] or [F][V][F][V]',
            'particles': '[C][V]',
            'pronouns': 'various'
        }
        
    def load_pos_files(self):
        """Load all POS files and extract words."""
        print(f"Loading POS files from {self.pos_dir}/...")
        
        for pos_file in self.pos_dir.glob("*.md"):
            pos_name = pos_file.stem
            words = self._extract_words_from_file(pos_file)
            if words:
                self.pos_data[pos_name] = words
                print(f"  {pos_name}: {len(words)} words")
        
        print(f"\nTotal POS categories: {len(self.pos_data)}")
        total_words = sum(len(words) for words in self.pos_data.values())
        print(f"Total words: {total_words}")
        
    def _extract_words_from_file(self, file_path):
        """Extract phi words from a POS markdown file."""
        words = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Find table rows with phi words
            pattern = r'\|\s*([a-z]+)\s*\|[^|]+\|'
            matches = re.findall(pattern, content)
            
            for word in matches:
                if (word not in ['phi', 'word', 'english', 'translation'] and
                    len(word) > 1 and
                    word.isalpha()):
                    words.append(word)
                    
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            
        return words
    
    def analyze_fricative_positions(self):
        """Analyze fricative usage by position within words."""
        print("\nAnalyzing fricative positions...")
        
        for pos_name, words in self.pos_data.items():
            for word in words:
                fricatives_with_positions = self._find_fricatives_with_positions(word)
                
                for fricative, position in fricatives_with_positions:
                    self.fricative_counts[pos_name][fricative] += 1
                    self.positional_counts[pos_name][position][fricative] += 1
                    
                # Store word patterns for analysis
                self.word_patterns[pos_name].append({
                    'word': word,
                    'length': len(word),
                    'fricatives': fricatives_with_positions
                })
    
    def _find_fricatives_with_positions(self, word):
        """Find all fricative digraphs with their positions in a word."""
        fricatives_found = []
        i = 0
        
        while i < len(word) - 1:
            digraph = word[i:i+2]
            if digraph in self.fricatives:
                # Determine position type
                if i == 0:
                    position = 'initial'
                elif i >= len(word) - 2:
                    position = 'final'
                else:
                    position = 'medial'
                    
                fricatives_found.append((digraph, position))
                i += 2  # Skip next character since we found a digraph
            else:
                i += 1
                
        return fricatives_found
    
    def analyze_pos_constraints(self):
        """Analyze how phonotactic patterns constrain fricative usage."""
        print("\n" + "="*80)
        print("PHONOTACTIC CONSTRAINT ANALYSIS")
        print("="*80)
        
        for pos_name in sorted(self.pos_data.keys()):
            if pos_name in self.pos_patterns:
                pattern = self.pos_patterns[pos_name]
                words = self.pos_data[pos_name]
                
                print(f"\n{pos_name.upper()} - Pattern: {pattern}")
                print("-" * 60)
                
                # Analyze fricative positions for this POS
                position_totals = defaultdict(int)
                for position in ['initial', 'medial', 'final']:
                    for fricative in self.fricatives:
                        count = self.positional_counts[pos_name][position][fricative]
                        position_totals[position] += count
                
                # Show position distribution
                print("Position distribution:")
                for position in ['initial', 'medial', 'final']:
                    total = position_totals[position]
                    if total > 0:
                        print(f"  {position}: {total} fricatives")
                        for fricative in self.fricatives:
                            count = self.positional_counts[pos_name][position][fricative]
                            if count > 0:
                                pct = (count / total * 100)
                                print(f"    {fricative}: {count:3d} ({pct:5.1f}%)")
                
                # Analyze why certain fricatives dominate
                self._analyze_pos_bias(pos_name, pattern)
    
    def _analyze_pos_bias(self, pos_name, pattern):
        """Analyze why certain fricatives are biased in this POS."""
        fricative_totals = defaultdict(int)
        for fricative in self.fricatives:
            fricative_totals[fricative] = self.fricative_counts[pos_name][fricative]
        
        total_fricatives = sum(fricative_totals.values())
        if total_fricatives == 0:
            return
            
        print("\nFricative bias analysis:")
        
        # Calculate expected vs actual distribution
        expected_per_fricative = total_fricatives / 4
        
        biases = []
        for fricative in self.fricatives:
            actual = fricative_totals[fricative]
            bias = actual - expected_per_fricative
            bias_pct = (bias / expected_per_fricative * 100) if expected_per_fricative > 0 else 0
            biases.append((fricative, actual, bias, bias_pct))
        
        # Sort by bias magnitude
        biases.sort(key=lambda x: abs(x[2]), reverse=True)
        
        for fricative, actual, bias, bias_pct in biases:
            status = "OVERUSED" if bias > 0 else "UNDERUSED" if bias < 0 else "BALANCED"
            print(f"  {fricative}: {actual:3d} ({bias:+5.1f}, {bias_pct:+5.1f}%) - {status}")
        
        # Suggest reasons based on pattern
        self._suggest_bias_reasons(pos_name, pattern, biases)
    
    def _suggest_bias_reasons(self, pos_name, pattern, biases):
        """Suggest reasons for fricative bias in this POS."""
        print("\nPossible reasons for bias:")
        
        # Get most biased fricatives
        overused = [f for f, _, bias, _ in biases if bias > 0]
        underused = [f for f, _, bias, _ in biases if bias < 0]
        
        if pos_name == 'verbs':
            print("  - Verbs start with fricatives [F][V][C][V]")
            if 'ph' in overused:
                print("    → 'ph' may be preferred for verb-initial position")
            if 'wh' in underused:
                print("    → 'wh' may be avoided in verb-initial position")
                
        elif pos_name == 'adjectives':
            print("  - Adjectives have fricatives in medial position [C][V][F][V]")
            if 'ph' in overused:
                print("    → 'ph' may be preferred in medial position")
            if 'wh' in underused:
                print("    → 'wh' may be avoided in medial position (0% usage!)")
                
        elif pos_name == 'nouns':
            print("  - Nouns can have fricatives in multiple positions [C/F][V/P][F][P]")
            print("    → More balanced distribution expected")
            
        elif pos_name == 'prepositions':
            print("  - Prepositions start with fricatives [F][P]")
            print("    → Should have even distribution across all fricatives")
            
        # Check for phonological preferences
        if 'wh' in underused:
            print(f"  - 'wh' is significantly underused in {pos_name}")
            print("    → May indicate phonological avoidance or aesthetic preference")
            
        if 'ph' in overused:
            print(f"  - 'ph' is significantly overused in {pos_name}")
            print("    → May indicate unconscious bias toward 'ph' sounds")
    
    def analyze_fricative_gaps(self):
        """Identify specific gaps in fricative usage."""
        print("\n" + "="*80)
        print("FRICATIVE USAGE GAPS ANALYSIS")
        print("="*80)
        
        for pos_name in sorted(self.pos_data.keys()):
            fricative_totals = defaultdict(int)
            for fricative in self.fricatives:
                fricative_totals[fricative] = self.fricative_counts[pos_name][fricative]
            
            total_fricatives = sum(fricative_totals.values())
            if total_fricatives == 0:
                continue
                
            print(f"\n{pos_name.upper()}:")
            
            # Find zero-usage fricatives
            zero_usage = [f for f in self.fricatives if fricative_totals[f] == 0]
            if zero_usage:
                print(f"  ❌ ZERO usage: {', '.join(zero_usage)}")
            
            # Find severely underused fricatives (< 10% when should be 25%)
            severely_underused = []
            for fricative in self.fricatives:
                actual_pct = (fricative_totals[fricative] / total_fricatives * 100)
                if actual_pct < 10 and fricative_totals[fricative] > 0:
                    severely_underused.append((fricative, actual_pct))
            
            if severely_underused:
                print("  ⚠️  Severely underused:")
                for fricative, pct in severely_underused:
                    print(f"     {fricative}: {pct:.1f}% (should be ~25%)")
            
            # Find overused fricatives (> 40% when should be 25%)
            overused = []
            for fricative in self.fricatives:
                actual_pct = (fricative_totals[fricative] / total_fricatives * 100)
                if actual_pct > 40:
                    overused.append((fricative, actual_pct))
            
            if overused:
                print("  🔥 Overused:")
                for fricative, pct in overused:
                    print(f"     {fricative}: {pct:.1f}% (should be ~25%)")
    
    def suggest_rebalancing_strategies(self):
        """Suggest specific strategies for rebalancing fricative usage."""
        print("\n" + "="*80)
        print("REBALANCING STRATEGIES")
        print("="*80)
        
        # Overall strategy
        total_fricatives = sum(self.fricative_counts[pos][f] 
                             for pos in self.pos_data.keys() 
                             for f in self.fricatives)
        ideal_per_fricative = total_fricatives / 4
        
        print(f"\nCurrent total fricatives: {total_fricatives}")
        print(f"Ideal per fricative: {ideal_per_fricative:.1f}")
        
        # Calculate current imbalances
        current_totals = defaultdict(int)
        for pos in self.pos_data.keys():
            for fricative in self.fricatives:
                current_totals[fricative] += self.fricative_counts[pos][fricative]
        
        print("\nCurrent vs ideal distribution:")
        for fricative in self.fricatives:
            current = current_totals[fricative]
            difference = current - ideal_per_fricative
            print(f"  {fricative}: {current:3d} (ideal: {ideal_per_fricative:.1f}, "
                  f"difference: {difference:+5.1f})")
        
        print("\nSTRATEGIC RECOMMENDATIONS:")
        print("-" * 40)
        
        # Specific recommendations by POS
        if current_totals['wh'] < ideal_per_fricative * 0.8:
            print("1. INCREASE 'wh' usage:")
            print("   - Create more 'wh' words in underrepresented POS")
            print("   - Consider 'wh' for new verbs, adjectives, and nouns")
            
        if current_totals['ph'] > ideal_per_fricative * 1.2:
            print("2. REDUCE 'ph' bias:")
            print("   - Avoid defaulting to 'ph' for new words")
            print("   - Consider replacing some 'ph' words with other fricatives")
            
        if self.fricative_counts['adjectives']['wh'] == 0:
            print("3. CRITICAL: Add 'wh' adjectives:")
            print("   - Adjectives have ZERO 'wh' usage")
            print("   - Create adjectives with 'wh' in medial position")
            
        print("4. FUTURE EXPANSION GUIDELINES:")
        print("   - Prioritize underused fricatives for new words")
        print("   - Monitor fricative distribution in each new word batch")
        print("   - Aim for 25% distribution across all fricatives")
    
    def run_deep_analysis(self):
        """Run complete deep fricative analysis."""
        self.load_pos_files()
        self.analyze_fricative_positions()
        self.analyze_pos_constraints()
        self.analyze_fricative_gaps()
        self.suggest_rebalancing_strategies()


def main():
    """Main function to run deep fricative analysis."""
    analyzer = DeepFricativeAnalyzer()
    analyzer.run_deep_analysis()


if __name__ == "__main__":
    main() 