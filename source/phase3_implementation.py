#!/usr/bin/env python3
"""
Phase 3 Implementation: Final Fricative Balance Optimization

Implements the validated conversions from Phase 3 to achieve optimal fricative balance.
"""

import os
import re
from pathlib import Path


class Phase3Implementer:
    """Implements Phase 3 conversions in POS files."""
    
    def __init__(self, pos_dir="pos"):
        self.pos_dir = Path(pos_dir)
        
        # Final validated conversions from Phase 3 validator
        self.conversions = [
            # ph → wh conversions (40 words)
            {'original': 'liphia', 'new': 'liwhia', 'meaning': 'belief', 'pos': 'noun'},
            {'original': 'phemo', 'new': 'whemo', 'meaning': 'think', 'pos': 'verb'},
            {'original': 'phema', 'new': 'whema', 'meaning': 'come', 'pos': 'verb'},
            {'original': 'phiwo', 'new': 'whiwo', 'meaning': 'befriend', 'pos': 'verb'},
            {'original': 'photo', 'new': 'whoto', 'meaning': 'need', 'pos': 'verb'},
            {'original': 'phopu', 'new': 'whopu', 'meaning': 'play ball', 'pos': 'verb'},
            {'original': 'phuri', 'new': 'whuri', 'meaning': 'work', 'pos': 'verb'},
            {'original': 'wuphi', 'new': 'wuwhi', 'meaning': 'amber', 'pos': 'adjective'},
            {'original': 'pephe', 'new': 'pewhe', 'meaning': 'indigo', 'pos': 'adjective'},
            {'original': 'lopha', 'new': 'lowha', 'meaning': 'bent/curved', 'pos': 'adjective'},
            {'original': 'tepha', 'new': 'tewha', 'meaning': 'intelligent', 'pos': 'adjective'},
            {'original': 'phawi', 'new': 'whawi', 'meaning': 'fly', 'pos': 'verb'},
            {'original': 'phuwe', 'new': 'whuwe', 'meaning': 'sleep', 'pos': 'verb'},
            {'original': 'phari', 'new': 'whari', 'meaning': 'sing', 'pos': 'verb'},
            {'original': 'phoe', 'new': 'whoe', 'meaning': 'ago', 'pos': 'preposition'},
            {'original': 'phea', 'new': 'whea', 'meaning': 'besides', 'pos': 'preposition'},
            {'original': 'phithui', 'new': 'whithui', 'meaning': 'lagoon', 'pos': 'noun'},
            {'original': 'phiphui', 'new': 'whiwhui', 'meaning': 'bee', 'pos': 'noun'},
            {'original': 'shephoa', 'new': 'shewhoa', 'meaning': 'sheep/goat', 'pos': 'noun'},
            {'original': 'thiphai', 'new': 'thiwhai', 'meaning': 'heart', 'pos': 'noun'},
            {'original': 'niphea', 'new': 'niwhea', 'meaning': 'needle', 'pos': 'noun'},
            {'original': 'phethie', 'new': 'whethie', 'meaning': 'room (enclosed)', 'pos': 'noun'},
            {'original': 'mipheo', 'new': 'miwheo', 'meaning': 'beauty', 'pos': 'noun'},
            {'original': 'wuphia', 'new': 'wuwhia', 'meaning': 'amber', 'pos': 'noun'},
            {'original': 'nuphea', 'new': 'nuwhea', 'meaning': 'timber', 'pos': 'noun'},
            {'original': 'phahi', 'new': 'whahi', 'meaning': 'become', 'pos': 'verb'},
            {'original': 'phaiphea', 'new': 'whaiwhea', 'meaning': 'butterfly', 'pos': 'noun'},
            {'original': 'liphoa', 'new': 'liwhoa', 'meaning': 'fly', 'pos': 'noun'},
            {'original': 'nophai', 'new': 'nowhai', 'meaning': 'bread', 'pos': 'noun'},
            {'original': 'saiphoa', 'new': 'saiwhoa', 'meaning': 'meat', 'pos': 'noun'},
            {'original': 'thiphao', 'new': 'thiwhao', 'meaning': 'dance', 'pos': 'noun'},
            {'original': 'phemi', 'new': 'whemi', 'meaning': 'speak', 'pos': 'verb'},
            {'original': 'phumo', 'new': 'whumo', 'meaning': 'translate', 'pos': 'verb'},
            
            # th → wh conversions (16 words)
            {'original': 'thisa', 'new': 'whisa', 'meaning': 'ask', 'pos': 'verb'},
            {'original': 'thomo', 'new': 'whomo', 'meaning': 'like', 'pos': 'verb'},
            {'original': 'thuni', 'new': 'whuni', 'meaning': 'have/possess', 'pos': 'verb'},
            {'original': 'thuno', 'new': 'whuno', 'meaning': 'break', 'pos': 'verb'},
            {'original': 'thusa', 'new': 'whusa', 'meaning': 'close', 'pos': 'verb'},
            {'original': 'thepa', 'new': 'whepa', 'meaning': 'fix/repair', 'pos': 'verb'},
            {'original': 'thuro', 'new': 'whuro', 'meaning': 'hide', 'pos': 'verb'},
            {'original': 'thora', 'new': 'whora', 'meaning': 'open', 'pos': 'verb'},
            {'original': 'thiwo', 'new': 'whiwo', 'meaning': 'give', 'pos': 'verb'},
            {'original': 'thonu', 'new': 'whonu', 'meaning': 'lose', 'pos': 'verb'},
            {'original': 'thawu', 'new': 'whawu', 'meaning': 'do', 'pos': 'verb'},
            {'original': 'thuli', 'new': 'whuli', 'meaning': 'finish/complete', 'pos': 'verb'},
            {'original': 'rothe', 'new': 'rowhe', 'meaning': 'like (similar)', 'pos': 'adjective'},
            {'original': 'thupi', 'new': 'whupi', 'meaning': 'read silently', 'pos': 'verb'},
            {'original': 'thepi', 'new': 'whepi', 'meaning': 'jump', 'pos': 'verb'},
            {'original': 'thumi', 'new': 'whumi', 'meaning': 'run', 'pos': 'verb'},
            
            # ph → sh conversions (7 words)
            {'original': 'phire', 'new': 'shire', 'meaning': 'want', 'pos': 'verb'},
            {'original': 'pheme', 'new': 'sheme', 'meaning': 'teach', 'pos': 'verb'},
            {'original': 'mipha', 'new': 'misha', 'meaning': 'beautiful', 'pos': 'adjective'},
            {'original': 'taphe', 'new': 'tashe', 'meaning': 'surprised', 'pos': 'adjective'},
            {'original': 'shuphoa', 'new': 'shushoa', 'meaning': 'purpose/goal', 'pos': 'noun'},
            {'original': 'phithoa', 'new': 'shithoa', 'meaning': 'death', 'pos': 'noun'},
            {'original': 'mophea', 'new': 'moshea', 'meaning': 'heat', 'pos': 'noun'},
        ]
        
        # Group conversions by POS for efficient processing
        self.conversions_by_pos = {}
        for conversion in self.conversions:
            pos = conversion['pos']
            if pos not in self.conversions_by_pos:
                self.conversions_by_pos[pos] = []
            self.conversions_by_pos[pos].append(conversion)
    
    def implement_conversions(self):
        """Implement all conversions across POS files."""
        print("PHASE 3 IMPLEMENTATION: Final Fricative Balance Optimization")
        print("=" * 60)
        
        total_implemented = 0
        
        for pos, conversions in self.conversions_by_pos.items():
            pos_file = self.pos_dir / f"{pos}s.md"  # Add 's' for plural
            if not pos_file.exists():
                pos_file = self.pos_dir / f"{pos}.md"  # Try singular
            
            if not pos_file.exists():
                print(f"⚠️  POS file not found for {pos}")
                continue
            
            implemented_count = self._implement_pos_conversions(pos_file, conversions)
            total_implemented += implemented_count
            
            print(f"✅ {pos}: {implemented_count}/{len(conversions)} conversions implemented")
        
        print(f"\n📊 IMPLEMENTATION SUMMARY:")
        print(f"Total conversions implemented: {total_implemented}/{len(self.conversions)}")
        
        return total_implemented
    
    def _implement_pos_conversions(self, pos_file, conversions):
        """Implement conversions for a specific POS file."""
        try:
            with open(pos_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            implemented_count = 0
            
            for conversion in conversions:
                original_word = conversion['original']
                new_word = conversion['new']
                meaning = conversion['meaning']
                
                # Create pattern to match the table row
                # Look for: | original_word | meaning |
                pattern = rf'\|\s*{re.escape(original_word)}\s*\|\s*{re.escape(meaning)}\s*\|'
                replacement = f'| {new_word} | {meaning} |'
                
                if re.search(pattern, content):
                    content = re.sub(pattern, replacement, content)
                    implemented_count += 1
                    print(f"  {original_word} → {new_word}")
                else:
                    print(f"  ⚠️  Pattern not found: {original_word} ({meaning})")
            
            # Write back to file if changes were made
            if content != original_content:
                with open(pos_file, 'w', encoding='utf-8') as f:
                    f.write(content)
            
            return implemented_count
            
        except Exception as e:
            print(f"❌ Error processing {pos_file}: {e}")
            return 0
    
    def calculate_final_distribution(self):
        """Calculate the final fricative distribution after Phase 3."""
        print(f"\n" + "="*60)
        print("FINAL FRICATIVE DISTRIBUTION CALCULATION")
        print("="*60)
        
        # Starting distribution (from Phase 2)
        current_distribution = {
            'ph': 305,  # 29.3%
            'wh': 198,  # 19.0%
            'th': 294,  # 28.3%
            'sh': 243   # 23.4%
        }
        
        # Calculate changes from Phase 3 conversions
        ph_reductions = len([c for c in self.conversions if 'ph' in c['original']])
        th_reductions = len([c for c in self.conversions if 'th' in c['original']])
        wh_additions = len([c for c in self.conversions if c['new'].startswith('wh') or 'wh' in c['new']])
        sh_additions = len([c for c in self.conversions if c['new'].startswith('sh') or 'sh' in c['new']])
        
        # Apply changes
        final_distribution = {
            'ph': current_distribution['ph'] - ph_reductions,
            'wh': current_distribution['wh'] + wh_additions,
            'th': current_distribution['th'] - th_reductions,
            'sh': current_distribution['sh'] + sh_additions
        }
        
        total_fricatives = sum(final_distribution.values())
        ideal_per_fricative = total_fricatives / 4
        
        print(f"Phase 3 conversion impact:")
        print(f"  ph: -{ph_reductions} words")
        print(f"  th: -{th_reductions} words")
        print(f"  wh: +{wh_additions} words")
        print(f"  sh: +{sh_additions} words")
        print()
        
        print(f"Final distribution:")
        print(f"Total fricatives: {total_fricatives}")
        print(f"Ideal per fricative: {ideal_per_fricative:.1f} (25%)")
        print()
        
        for fricative in ['ph', 'wh', 'th', 'sh']:
            count = final_distribution[fricative]
            percentage = (count / total_fricatives) * 100
            deviation = count - ideal_per_fricative
            deviation_pct = (deviation / ideal_per_fricative) * 100
            
            # Status: ✅ if within ±5%, ⚠️ if within ±10%, ❌ if worse
            if abs(deviation_pct) <= 5:
                status = "✅ EXCELLENT"
            elif abs(deviation_pct) <= 10:
                status = "⚠️ GOOD"
            else:
                status = "❌ NEEDS WORK"
            
            print(f"  {fricative}: {count:3d} ({percentage:4.1f}%) "
                  f"[{deviation:+5.1f}] ({deviation_pct:+4.1f}%) {status}")
        
        # Calculate overall balance improvement
        phase2_deviations = [45.0, -62.0, 34.0, -17.0]  # From Phase 2 results
        final_deviations = [final_distribution[f] - ideal_per_fricative for f in ['ph', 'wh', 'th', 'sh']]
        
        phase2_avg_deviation = sum(abs(d) for d in phase2_deviations) / 4
        final_avg_deviation = sum(abs(d) for d in final_deviations) / 4
        
        improvement = ((phase2_avg_deviation - final_avg_deviation) / phase2_avg_deviation) * 100
        
        print(f"\nBalance improvement from Phase 2:")
        print(f"  Average deviation: {phase2_avg_deviation:.1f} → {final_avg_deviation:.1f}")
        print(f"  Improvement: {improvement:.1f}%")
        
        return final_distribution


def main():
    """Main function to run Phase 3 implementation."""
    implementer = Phase3Implementer()
    
    # Implement conversions
    total_implemented = implementer.implement_conversions()
    
    # Calculate final distribution
    final_distribution = implementer.calculate_final_distribution()
    
    print(f"\n" + "="*60)
    print("PHASE 3 IMPLEMENTATION COMPLETE")
    print("="*60)
    print("🎉 Final fricative balance optimization achieved!")
    print(f"📈 {total_implemented} conversions successfully implemented")


if __name__ == "__main__":
    main() 