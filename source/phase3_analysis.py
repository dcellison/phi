#!/usr/bin/env python3
"""
Phase 3 Analysis: Final Fricative Balance Optimization

Analyzes the current fricative distribution after Phase 2 and identifies
the precise adjustments needed to achieve optimal balance (25% ± 5% each).
"""

import os
import re
from collections import defaultdict, Counter
from pathlib import Path


class Phase3Analyzer:
    """Analyzes current state and plans final balance optimization."""
    
    def __init__(self, pos_dir="pos"):
        self.pos_dir = Path(pos_dir)
        self.fricatives = ['ph', 'wh', 'th', 'sh']
        self.pos_data = {}
        self.current_distribution = {}
        
    def load_current_state(self):
        """Load current fricative distribution from Phase 2 results."""
        print("PHASE 3 ANALYSIS: Final Fricative Balance Optimization")
        print("=" * 60)
        
        # Current distribution from Phase 2 results
        self.current_distribution = {
            'ph': 305,  # 29.3%
            'wh': 198,  # 19.0%
            'th': 294,  # 28.3%
            'sh': 243   # 23.4%
        }
        
        total_fricatives = sum(self.current_distribution.values())
        ideal_per_fricative = total_fricatives / 4
        
        print(f"Current distribution (after Phase 2):")
        print(f"Total fricatives: {total_fricatives}")
        print(f"Ideal per fricative: {ideal_per_fricative:.1f} (25%)")
        print()
        
        for fricative in self.fricatives:
            count = self.current_distribution[fricative]
            percentage = (count / total_fricatives) * 100
            deviation = count - ideal_per_fricative
            status = "✅" if abs(deviation) <= ideal_per_fricative * 0.2 else "❌"
            print(f"  {fricative}: {count:3d} ({percentage:4.1f}%) "
                  f"[{deviation:+5.1f}] {status}")
        
        return total_fricatives, ideal_per_fricative
    
    def calculate_phase3_targets(self, total_fricatives, ideal_per_fricative):
        """Calculate specific targets for Phase 3 adjustments."""
        print(f"\n" + "="*60)
        print("PHASE 3 TARGET CALCULATIONS")
        print("="*60)
        
        # Calculate deviations and required adjustments
        adjustments = {}
        for fricative in self.fricatives:
            current = self.current_distribution[fricative]
            deviation = current - ideal_per_fricative
            adjustments[fricative] = -deviation  # Negative deviation means we need to add
        
        print("Required adjustments to reach perfect balance:")
        for fricative in self.fricatives:
            adj = adjustments[fricative]
            direction = "add" if adj > 0 else "remove"
            print(f"  {fricative}: {direction} {abs(adj):.1f} instances")
        
        # Phase 3 strategy: Focus on the largest imbalances
        ph_excess = -adjustments['ph']  # How much ph we need to remove
        wh_deficit = adjustments['wh']   # How much wh we need to add
        th_excess = -adjustments['th']   # How much th we need to remove
        sh_deficit = adjustments['sh']   # How much sh we need to add
        
        print(f"\nPhase 3 Strategy:")
        print(f"  Primary: Convert {ph_excess:.0f} 'ph' words to other fricatives")
        print(f"  Secondary: Convert {th_excess:.0f} 'th' words to 'wh'")
        print(f"  Goal: Add {wh_deficit:.0f} 'wh' and {sh_deficit:.0f} 'sh' instances")
        
        # Recommended conversion plan
        ph_to_wh = min(ph_excess, wh_deficit)
        ph_to_sh = min(ph_excess - ph_to_wh, sh_deficit)
        th_to_wh = min(th_excess, wh_deficit - ph_to_wh)
        
        conversion_plan = {
            'ph_to_wh': int(ph_to_wh),
            'ph_to_sh': int(ph_to_sh),
            'th_to_wh': int(th_to_wh),
            'total_conversions': int(ph_to_wh + ph_to_sh + th_to_wh)
        }
        
        print(f"\nRecommended conversions:")
        print(f"  ph → wh: {conversion_plan['ph_to_wh']} words")
        print(f"  ph → sh: {conversion_plan['ph_to_sh']} words")
        print(f"  th → wh: {conversion_plan['th_to_wh']} words")
        print(f"  Total: {conversion_plan['total_conversions']} words")
        
        return conversion_plan
    
    def load_pos_files_for_candidates(self):
        """Load POS files to identify conversion candidates."""
        print(f"\n" + "="*60)
        print("LOADING CONVERSION CANDIDATES")
        print("="*60)
        
        candidates = {
            'ph_words': defaultdict(list),
            'th_words': defaultdict(list)
        }
        
        for pos_file in self.pos_dir.glob("*.md"):
            pos_name = pos_file.stem
            ph_words, th_words = self._extract_fricative_words(pos_file, pos_name)
            
            if ph_words:
                candidates['ph_words'][pos_name] = ph_words
            if th_words:
                candidates['th_words'][pos_name] = th_words
            
            print(f"  {pos_name}: {len(ph_words)} 'ph' words, {len(th_words)} 'th' words")
        
        total_ph = sum(len(words) for words in candidates['ph_words'].values())
        total_th = sum(len(words) for words in candidates['th_words'].values())
        print(f"\nTotal candidates: {total_ph} 'ph' words, {total_th} 'th' words")
        
        return candidates
    
    def _extract_fricative_words(self, file_path, pos_name):
        """Extract 'ph' and 'th' words from a POS file."""
        ph_words = []
        th_words = []
        
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
                    
                    if 'ph' in word:
                        ph_words.append({
                            'word': word,
                            'meaning': meaning,
                            'pos': pos_name
                        })
                    elif 'th' in word:
                        th_words.append({
                            'word': word,
                            'meaning': meaning,
                            'pos': pos_name
                        })
        
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
        
        return ph_words, th_words
    
    def prioritize_conversion_candidates(self, candidates, conversion_plan):
        """Prioritize words for conversion based on semantic and phonetic factors."""
        print(f"\n" + "="*60)
        print("PRIORITIZING CONVERSION CANDIDATES")
        print("="*60)
        
        # Priority categories for different types of conversions
        priority_suggestions = {
            'ph_to_wh': [],
            'ph_to_sh': [],
            'th_to_wh': []
        }
        
        # Analyze 'ph' words for conversion
        print("\nAnalyzing 'ph' words for conversion:")
        ph_candidates = []
        for pos_name, words in candidates['ph_words'].items():
            for word_data in words:
                priority = self._assess_conversion_priority(word_data, 'ph')
                ph_candidates.append((priority, word_data))
        
        # Sort by priority (higher is better for conversion)
        ph_candidates.sort(key=lambda x: x[0], reverse=True)
        
        # Assign ph conversions
        ph_to_wh_needed = conversion_plan['ph_to_wh']
        ph_to_sh_needed = conversion_plan['ph_to_sh']
        
        for i, (priority, word_data) in enumerate(ph_candidates):
            if len(priority_suggestions['ph_to_wh']) < ph_to_wh_needed:
                priority_suggestions['ph_to_wh'].append(word_data)
            elif len(priority_suggestions['ph_to_sh']) < ph_to_sh_needed:
                priority_suggestions['ph_to_sh'].append(word_data)
            else:
                break
        
        # Analyze 'th' words for conversion to 'wh'
        print("\nAnalyzing 'th' words for conversion to 'wh':")
        th_candidates = []
        for pos_name, words in candidates['th_words'].items():
            for word_data in words:
                priority = self._assess_conversion_priority(word_data, 'th')
                th_candidates.append((priority, word_data))
        
        # Sort by priority
        th_candidates.sort(key=lambda x: x[0], reverse=True)
        
        # Assign th → wh conversions
        th_to_wh_needed = conversion_plan['th_to_wh']
        for i, (priority, word_data) in enumerate(th_candidates[:th_to_wh_needed]):
            priority_suggestions['th_to_wh'].append(word_data)
        
        return priority_suggestions
    
    def _assess_conversion_priority(self, word_data, current_fricative):
        """Assess priority for converting a word (higher = better candidate)."""
        word = word_data['word']
        meaning = word_data['meaning']
        pos = word_data['pos']
        
        priority = 0
        
        # Higher priority for common, simple concepts
        high_priority_meanings = [
            'carry', 'push', 'pull', 'throw', 'put', 'set', 'hold', 'take',
            'bring', 'send', 'give', 'get', 'make', 'do', 'go', 'come',
            'see', 'hear', 'say', 'tell', 'ask', 'answer', 'think', 'know',
            'like', 'want', 'need', 'have', 'be', 'become', 'stay', 'leave',
            'start', 'stop', 'finish', 'continue', 'try', 'help', 'work',
            'play', 'learn', 'teach', 'show', 'hide', 'find', 'lose',
            'open', 'close', 'break', 'fix', 'build', 'destroy', 'create'
        ]
        
        if any(keyword in meaning.lower() for keyword in high_priority_meanings):
            priority += 3
        
        # Medium priority for descriptive and action words
        medium_priority_meanings = [
            'walk', 'run', 'jump', 'climb', 'swim', 'fly', 'fall', 'rise',
            'turn', 'move', 'stand', 'sit', 'lie', 'sleep', 'wake', 'eat',
            'drink', 'cook', 'clean', 'wash', 'dry', 'cut', 'write', 'read',
            'draw', 'paint', 'sing', 'dance', 'laugh', 'cry', 'smile'
        ]
        
        if any(keyword in meaning.lower() for keyword in medium_priority_meanings):
            priority += 2
        
        # Avoid core conceptual words (lower priority)
        preserve_meanings = [
            'exist', 'live', 'die', 'born', 'love', 'hate', 'fear', 'hope',
            'believe', 'trust', 'remember', 'forget', 'understand', 'explain',
            'mean', 'feel', 'seem', 'appear', 'happen', 'become', 'remain'
        ]
        
        if any(keyword in meaning.lower() for keyword in preserve_meanings):
            priority -= 2
        
        # Prefer shorter words (easier to convert)
        if len(word) <= 5:
            priority += 1
        
        # Prefer verbs for conversion (more flexible semantically)
        if pos == 'verbs':
            priority += 1
        
        return priority
    
    def generate_conversion_suggestions(self, priority_suggestions):
        """Generate specific word conversion suggestions."""
        print(f"\n" + "="*60)
        print("PHASE 3 CONVERSION SUGGESTIONS")
        print("="*60)
        
        all_suggestions = []
        
        for conversion_type, word_list in priority_suggestions.items():
            if not word_list:
                continue
                
            source_fricative = conversion_type.split('_')[0]
            target_fricative = conversion_type.split('_')[2]
            
            print(f"\n{source_fricative.upper()} → {target_fricative.upper()} conversions ({len(word_list)} words):")
            print("-" * 40)
            
            for i, word_data in enumerate(word_list, 1):
                original = word_data['word']
                meaning = word_data['meaning']
                pos = word_data['pos']
                
                # Generate new word
                new_word = original.replace(source_fricative, target_fricative)
                
                suggestion = {
                    'original': original,
                    'new': new_word,
                    'meaning': meaning,
                    'pos': pos,
                    'conversion_type': conversion_type,
                    'source_fricative': source_fricative,
                    'target_fricative': target_fricative
                }
                
                all_suggestions.append(suggestion)
                
                print(f"{i:2d}. {original:<12} → {new_word:<12} ({meaning}) [{pos}]")
        
        print(f"\nTotal Phase 3 suggestions: {len(all_suggestions)} words")
        
        return all_suggestions
    
    def run_phase3_analysis(self):
        """Run complete Phase 3 analysis."""
        total_fricatives, ideal_per_fricative = self.load_current_state()
        conversion_plan = self.calculate_phase3_targets(total_fricatives, ideal_per_fricative)
        candidates = self.load_pos_files_for_candidates()
        priority_suggestions = self.prioritize_conversion_candidates(candidates, conversion_plan)
        suggestions = self.generate_conversion_suggestions(priority_suggestions)
        
        return {
            'current_distribution': self.current_distribution,
            'conversion_plan': conversion_plan,
            'suggestions': suggestions,
            'total_fricatives': total_fricatives,
            'ideal_per_fricative': ideal_per_fricative
        }


def main():
    """Main function to run Phase 3 analysis."""
    analyzer = Phase3Analyzer()
    results = analyzer.run_phase3_analysis()
    
    print(f"\n" + "="*60)
    print("PHASE 3 ANALYSIS COMPLETE")
    print("="*60)
    print("Ready to proceed with final balance optimization!")


if __name__ == "__main__":
    main() 