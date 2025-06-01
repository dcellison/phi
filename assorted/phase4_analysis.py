#!/usr/bin/env python3
"""
Phase 4 Analysis: Vowel and Standalone Consonant Optimization

Analyzes vowel distribution imbalances and standalone consonant issues
to plan systematic optimization while preserving fricative balance.
"""

import os
import re
from collections import defaultdict, Counter
from pathlib import Path


class Phase4Analyzer:
    """Analyzes vowel and standalone consonant optimization opportunities."""
    
    def __init__(self, pos_dir="pos"):
        self.pos_dir = Path(pos_dir)
        self.consonants = ['h', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w']
        self.vowels = ['i', 'u', 'e', 'o', 'a']
        self.fricatives = ['ph', 'wh', 'th', 'sh']
        
    def load_current_state(self):
        """Load current phonological state from corrected analysis."""
        print("PHASE 4 ANALYSIS: Vowel and Standalone Consonant Optimization")
        print("=" * 70)
        
        # Current imbalances from corrected analysis
        self.vowel_distribution = {
            'a': 804,  # 26.3% (should be 20%) - overused +31.3%
            'e': 696,  # 22.7% (should be 20%) - slightly overused +13.7%
            'i': 671,  # 21.9% (should be 20%) - slightly overused +9.6%
            'o': 501,  # 16.4% (should be 20%) - underused -18.2%
            'u': 389   # 12.7% (should be 20%) - severely underused -36.5%
        }
        
        self.standalone_consonant_distribution = {
            'h': 75,   # 4.7% (should be 11.1%) - severely underused -57.5%
            'l': 205,  # 12.9% (should be 11.1%) - slightly overused +16.1%
            'm': 166,  # 10.4% (should be 11.1%) - balanced -6.0%
            'n': 184,  # 11.6% (should be 11.1%) - balanced +4.2%
            'p': 175,  # 11.0% (should be 11.1%) - balanced -0.9%
            'r': 139,  # 8.7% (should be 11.1%) - underused -21.3%
            's': 260,  # 16.4% (should be 11.1%) - overused +47.3%
            't': 275,  # 17.3% (should be 11.1%) - overused +55.8%
            'w': 110   # 6.9% (should be 11.1%) - underused -37.7%
        }
        
        total_vowels = sum(self.vowel_distribution.values())
        total_standalone_consonants = sum(self.standalone_consonant_distribution.values())
        
        ideal_per_vowel = total_vowels / len(self.vowels)
        ideal_per_consonant = total_standalone_consonants / len(self.consonants)
        
        print(f"Current vowel distribution:")
        print(f"Total vowels: {total_vowels}")
        print(f"Ideal per vowel: {ideal_per_vowel:.1f} (20%)")
        print()
        
        for vowel in self.vowels:
            count = self.vowel_distribution[vowel]
            percentage = (count / total_vowels) * 100
            deviation = count - ideal_per_vowel
            deviation_pct = (deviation / ideal_per_vowel) * 100
            status = "✅" if abs(deviation_pct) <= 15 else "⚠️" if abs(deviation_pct) <= 25 else "❌"
            print(f"  {vowel}: {count:3d} ({percentage:4.1f}%) "
                  f"[{deviation:+5.1f}] ({deviation_pct:+4.1f}%) {status}")
        
        print(f"\nCurrent standalone consonant distribution:")
        print(f"Total standalone consonants: {total_standalone_consonants}")
        print(f"Ideal per consonant: {ideal_per_consonant:.1f} (11.1%)")
        print()
        
        for consonant in self.consonants:
            count = self.standalone_consonant_distribution[consonant]
            percentage = (count / total_standalone_consonants) * 100
            deviation = count - ideal_per_consonant
            deviation_pct = (deviation / ideal_per_consonant) * 100
            status = "✅" if abs(deviation_pct) <= 15 else "⚠️" if abs(deviation_pct) <= 25 else "❌"
            print(f"  {consonant}: {count:3d} ({percentage:4.1f}%) "
                  f"[{deviation:+5.1f}] ({deviation_pct:+4.1f}%) {status}")
        
        return total_vowels, total_standalone_consonants, ideal_per_vowel, ideal_per_consonant
    
    def calculate_phase4_targets(self, total_vowels, total_consonants, ideal_per_vowel, ideal_per_consonant):
        """Calculate specific targets for Phase 4 optimization."""
        print(f"\n" + "="*70)
        print("PHASE 4 TARGET CALCULATIONS")
        print("="*70)
        
        # Calculate vowel adjustments needed
        vowel_adjustments = {}
        for vowel in self.vowels:
            current = self.vowel_distribution[vowel]
            deviation = current - ideal_per_vowel
            vowel_adjustments[vowel] = -deviation  # Negative deviation means we need to add
        
        print("Vowel adjustments needed:")
        for vowel in self.vowels:
            adj = vowel_adjustments[vowel]
            direction = "add" if adj > 0 else "reduce"
            print(f"  {vowel}: {direction} {abs(adj):.1f} instances")
        
        # Calculate consonant adjustments needed
        consonant_adjustments = {}
        for consonant in self.consonants:
            current = self.standalone_consonant_distribution[consonant]
            deviation = current - ideal_per_consonant
            consonant_adjustments[consonant] = -deviation
        
        print(f"\nStandalone consonant adjustments needed:")
        for consonant in self.consonants:
            adj = consonant_adjustments[consonant]
            direction = "add" if adj > 0 else "reduce"
            print(f"  {consonant}: {direction} {abs(adj):.1f} instances")
        
        # Phase 4 strategy priorities
        print(f"\nPhase 4 Strategy Priorities:")
        
        # Vowel priorities
        a_excess = -vowel_adjustments['a']  # How much 'a' we need to reduce
        u_deficit = vowel_adjustments['u']   # How much 'u' we need to add
        o_deficit = vowel_adjustments['o']   # How much 'o' we need to add
        
        print(f"  VOWEL OPTIMIZATION:")
        print(f"    Primary: Reduce 'a' usage by {a_excess:.0f} instances")
        print(f"    Primary: Increase 'u' usage by {u_deficit:.0f} instances")
        print(f"    Secondary: Increase 'o' usage by {o_deficit:.0f} instances")
        
        # Consonant priorities
        s_excess = -consonant_adjustments['s']
        t_excess = -consonant_adjustments['t']
        h_deficit = consonant_adjustments['h']
        w_deficit = consonant_adjustments['w']
        r_deficit = consonant_adjustments['r']
        
        print(f"  CONSONANT OPTIMIZATION:")
        print(f"    Primary: Reduce 's' usage by {s_excess:.0f} instances")
        print(f"    Primary: Reduce 't' usage by {t_excess:.0f} instances")
        print(f"    Primary: Increase 'h' usage by {h_deficit:.0f} instances")
        print(f"    Secondary: Increase 'w' usage by {w_deficit:.0f} instances")
        print(f"    Secondary: Increase 'r' usage by {r_deficit:.0f} instances")
        
        return {
            'vowel_adjustments': vowel_adjustments,
            'consonant_adjustments': consonant_adjustments,
            'a_excess': a_excess,
            'u_deficit': u_deficit,
            'o_deficit': o_deficit,
            's_excess': s_excess,
            't_excess': t_excess,
            'h_deficit': h_deficit,
            'w_deficit': w_deficit,
            'r_deficit': r_deficit
        }
    
    def run_phase4_analysis(self):
        """Run complete Phase 4 analysis."""
        total_vowels, total_consonants, ideal_per_vowel, ideal_per_consonant = self.load_current_state()
        targets = self.calculate_phase4_targets(total_vowels, total_consonants, ideal_per_vowel, ideal_per_consonant)
        
        print(f"\n" + "="*70)
        print("PHASE 4 OPTIMIZATION STRATEGY")
        print("="*70)
        
        print("Recommended approach:")
        print("1. VOWEL OPTIMIZATION: Focus on a→u conversions (highest impact)")
        print("2. CONSONANT OPTIMIZATION: Focus on s→h and t→h conversions")
        print("3. VALIDATION: Ensure all changes maintain phonotactic patterns")
        print("4. IMPLEMENTATION: Apply changes systematically by POS")
        
        return {
            'current_state': {
                'vowels': self.vowel_distribution,
                'consonants': self.standalone_consonant_distribution
            },
            'targets': targets
        }


def main():
    """Main function to run Phase 4 analysis."""
    analyzer = Phase4Analyzer()
    results = analyzer.run_phase4_analysis()
    
    print(f"\n" + "="*70)
    print("PHASE 4 ANALYSIS COMPLETE")
    print("="*70)
    print("Ready to proceed with vowel and consonant optimization!")


if __name__ == "__main__":
    main() 