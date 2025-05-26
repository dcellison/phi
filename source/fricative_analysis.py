#!/usr/bin/env python3
"""
Fricative Digraph Distribution Analysis for Phi Language

Analyzes the distribution of fricative digraphs (ph, wh, th, sh) across
different parts of speech in the phi language to ensure balanced
phonological inventory usage.
"""

import os
import re
from collections import defaultdict, Counter
from pathlib import Path


class FricativeAnalyzer:
    """Analyzes fricative digraph distribution in phi lexicon."""
    
    def __init__(self, pos_dir="pos"):
        self.pos_dir = Path(pos_dir)
        self.fricatives = ['ph', 'wh', 'th', 'sh']
        self.pos_data = {}
        self.fricative_counts = defaultdict(lambda: defaultdict(int))
        self.total_counts = defaultdict(int)
        
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
            # Pattern: | phi_word | english_translation |
            pattern = r'\|\s*([a-z]+)\s*\|[^|]+\|'
            matches = re.findall(pattern, content)
            
            for word in matches:
                # Filter out table headers and non-phi words
                if (word not in ['phi', 'word', 'english', 'translation'] and
                    len(word) > 1 and
                    word.isalpha()):
                    words.append(word)
                    
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            
        return words
    
    def analyze_fricatives(self):
        """Analyze fricative digraph distribution."""
        print("\nAnalyzing fricative digraph distribution...")
        
        for pos_name, words in self.pos_data.items():
            for word in words:
                fricatives_in_word = self._find_fricatives(word)
                
                for fricative in fricatives_in_word:
                    self.fricative_counts[pos_name][fricative] += 1
                    self.total_counts[fricative] += 1
                    
    def _find_fricatives(self, word):
        """Find all fricative digraphs in a word."""
        fricatives_found = []
        i = 0
        
        while i < len(word) - 1:
            digraph = word[i:i+2]
            if digraph in self.fricatives:
                fricatives_found.append(digraph)
                i += 2  # Skip next character since we found a digraph
            else:
                i += 1
                
        return fricatives_found
    
    def print_detailed_analysis(self):
        """Print detailed fricative distribution analysis."""
        print("\n" + "="*80)
        print("FRICATIVE DIGRAPH DISTRIBUTION ANALYSIS")
        print("="*80)
        
        # Overall distribution
        print("\nOVERALL FRICATIVE DISTRIBUTION:")
        print("-" * 40)
        total_fricatives = sum(self.total_counts.values())
        
        for fricative in self.fricatives:
            count = self.total_counts[fricative]
            percentage = (count / total_fricatives * 100) if total_fricatives > 0 else 0
            print(f"{fricative}: {count:4d} ({percentage:5.1f}%)")
            
        print(f"\nTotal fricative instances: {total_fricatives}")
        
        # Distribution by POS
        print("\nDISTRIBUTION BY PART OF SPEECH:")
        print("-" * 60)
        
        # Header
        print(f"{'POS':<15} {'Total':<8} {'ph':<6} {'wh':<6} {'th':<6} {'sh':<6}")
        print("-" * 60)
        
        for pos_name in sorted(self.pos_data.keys()):
            pos_total = sum(self.fricative_counts[pos_name].values())
            ph_count = self.fricative_counts[pos_name]['ph']
            wh_count = self.fricative_counts[pos_name]['wh']
            th_count = self.fricative_counts[pos_name]['th']
            sh_count = self.fricative_counts[pos_name]['sh']
            
            print(f"{pos_name:<15} {pos_total:<8} {ph_count:<6} {wh_count:<6} "
                  f"{th_count:<6} {sh_count:<6}")
        
        # Percentage distribution by POS
        print("\nPERCENTAGE DISTRIBUTION BY POS:")
        print("-" * 70)
        print(f"{'POS':<15} {'ph%':<8} {'wh%':<8} {'th%':<8} {'sh%':<8}")
        print("-" * 70)
        
        for pos_name in sorted(self.pos_data.keys()):
            pos_total = sum(self.fricative_counts[pos_name].values())
            if pos_total > 0:
                ph_pct = (self.fricative_counts[pos_name]['ph'] / pos_total * 100)
                wh_pct = (self.fricative_counts[pos_name]['wh'] / pos_total * 100)
                th_pct = (self.fricative_counts[pos_name]['th'] / pos_total * 100)
                sh_pct = (self.fricative_counts[pos_name]['sh'] / pos_total * 100)
                
                print(f"{pos_name:<15} {ph_pct:<8.1f} {wh_pct:<8.1f} "
                      f"{th_pct:<8.1f} {sh_pct:<8.1f}")
    
    def analyze_balance(self):
        """Analyze how balanced the fricative distribution is."""
        print("\nBALANCE ANALYSIS:")
        print("-" * 40)
        
        total_fricatives = sum(self.total_counts.values())
        ideal_count = total_fricatives / 4  # Perfect balance would be 25% each
        
        print(f"Ideal count per fricative (25% each): {ideal_count:.1f}")
        print("\nDeviation from ideal balance:")
        
        deviations = []
        for fricative in self.fricatives:
            count = self.total_counts[fricative]
            deviation = abs(count - ideal_count)
            deviation_pct = (deviation / ideal_count * 100) if ideal_count > 0 else 0
            deviations.append(deviation_pct)
            
            print(f"{fricative}: {deviation:+6.1f} ({deviation_pct:+5.1f}%)")
        
        avg_deviation = sum(deviations) / len(deviations)
        print(f"\nAverage deviation: {avg_deviation:.1f}%")
        
        if avg_deviation < 10:
            print("✅ Distribution is well-balanced!")
        elif avg_deviation < 20:
            print("⚠️  Distribution has moderate imbalance")
        else:
            print("❌ Distribution is significantly imbalanced")
    
    def suggest_improvements(self):
        """Suggest improvements for better balance."""
        print("\nSUGGESTIONS FOR IMPROVEMENT:")
        print("-" * 40)
        
        total_fricatives = sum(self.total_counts.values())
        ideal_count = total_fricatives / 4
        
        overused = []
        underused = []
        
        for fricative in self.fricatives:
            count = self.total_counts[fricative]
            if count > ideal_count * 1.1:  # More than 10% above ideal
                overused.append((fricative, count - ideal_count))
            elif count < ideal_count * 0.9:  # More than 10% below ideal
                underused.append((fricative, ideal_count - count))
        
        if overused:
            print("Overused fricatives:")
            for fricative, excess in overused:
                print(f"  {fricative}: {excess:.1f} instances above ideal")
        
        if underused:
            print("Underused fricatives:")
            for fricative, deficit in underused:
                print(f"  {fricative}: {deficit:.1f} instances below ideal")
        
        if not overused and not underused:
            print("✅ Distribution is already well-balanced!")
    
    def run_analysis(self):
        """Run complete fricative analysis."""
        self.load_pos_files()
        self.analyze_fricatives()
        self.print_detailed_analysis()
        self.analyze_balance()
        self.suggest_improvements()


def main():
    """Main function to run fricative analysis."""
    analyzer = FricativeAnalyzer()
    analyzer.run_analysis()


if __name__ == "__main__":
    main() 