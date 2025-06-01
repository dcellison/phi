#!/usr/bin/env python3
"""
Phase 2 Analysis: Strategic 'ph' Replacement Planning

Analyzes current 'ph' words to identify the best candidates for replacement
with other fricatives to achieve better balance while maintaining semantic coherence.
"""

import os
import re
from collections import defaultdict, Counter
from pathlib import Path


class Phase2Analyzer:
    """Analyzes 'ph' words for strategic replacement opportunities."""
    
    def __init__(self, pos_dir="pos"):
        self.pos_dir = Path(pos_dir)
        self.fricatives = ['ph', 'wh', 'th', 'sh']
        self.pos_data = {}
        self.ph_words = defaultdict(list)
        self.replacement_targets = {}
        
    def load_pos_files(self):
        """Load all POS files and extract 'ph' words."""
        print("PHASE 2 ANALYSIS: Strategic 'ph' Replacement Planning")
        print("=" * 60)
        print(f"Loading POS files from {self.pos_dir}/...")
        
        for pos_file in self.pos_dir.glob("*.md"):
            pos_name = pos_file.stem
            words = self._extract_ph_words_from_file(pos_file, pos_name)
            if words:
                self.pos_data[pos_name] = words
                self.ph_words[pos_name] = words
                print(f"  {pos_name}: {len(words)} 'ph' words")
        
        total_ph_words = sum(len(words) for words in self.ph_words.values())
        print(f"\nTotal 'ph' words found: {total_ph_words}")
        
    def _extract_ph_words_from_file(self, file_path, pos_name):
        """Extract 'ph' words with their meanings from a POS file."""
        ph_words = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Find table rows with phi words containing 'ph'
            pattern = r'\|\s*([a-z]*ph[a-z]*)\s*\|\s*([^|]+)\s*\|'
            matches = re.findall(pattern, content)
            
            for word, meaning in matches:
                word = word.strip()
                meaning = meaning.strip()
                if (word not in ['phi', 'word', 'english', 'translation'] and
                    len(word) > 1 and
                    word.isalpha() and
                    'ph' in word):
                    ph_words.append({
                        'word': word,
                        'meaning': meaning,
                        'pos': pos_name,
                        'pattern': self._analyze_word_pattern(word, pos_name)
                    })
                    
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            
        return ph_words
    
    def _analyze_word_pattern(self, word, pos_name):
        """Analyze the phonotactic pattern of a word."""
        if pos_name == 'adjectives':
            # Pattern: [C][V][F][V] - 'ph' should be in position 2-3
            if len(word) >= 4 and word[2:4] == 'ph':
                return 'medial_ph'
            elif word.startswith('ph'):
                return 'initial_ph_error'  # Shouldn't happen in adjectives
            else:
                return 'unknown_ph_position'
        elif pos_name == 'verbs':
            # Pattern: [F][V][C][V] - 'ph' should be in position 0-1
            if word.startswith('ph'):
                return 'initial_ph'
            else:
                return 'non_initial_ph_error'  # Shouldn't happen in verbs
        elif pos_name == 'nouns':
            # Pattern: [C/F][V/P][F][P] - 'ph' can be initial or medial
            if word.startswith('ph'):
                return 'initial_ph'
            elif 'ph' in word[2:]:
                return 'medial_ph'
            else:
                return 'unknown_ph_position'
        else:
            return 'other_pattern'
    
    def analyze_replacement_candidates(self):
        """Analyze which 'ph' words are best candidates for replacement."""
        print("\n" + "="*60)
        print("REPLACEMENT CANDIDATE ANALYSIS")
        print("="*60)
        
        # Current fricative distribution (from implementation results)
        current_distribution = {
            'ph': 361,
            'wh': 197,  # After Phase 1
            'th': 289,
            'sh': 202
        }
        
        total_fricatives = sum(current_distribution.values())
        ideal_per_fricative = total_fricatives / 4
        
        print(f"Current distribution:")
        for fricative in self.fricatives:
            count = current_distribution[fricative]
            deviation = count - ideal_per_fricative
            print(f"  {fricative}: {count} ({deviation:+.1f} from ideal {ideal_per_fricative:.1f})")
        
        # Calculate replacement targets
        ph_excess = current_distribution['ph'] - ideal_per_fricative
        sh_deficit = ideal_per_fricative - current_distribution['sh']
        th_excess = current_distribution['th'] - ideal_per_fricative
        
        print(f"\nReplacement targets:")
        print(f"  'ph' excess: {ph_excess:.1f} instances")
        print(f"  'sh' deficit: {sh_deficit:.1f} instances")
        print(f"  'th' excess: {th_excess:.1f} instances")
        
        # Recommend replacement strategy
        ph_to_sh = min(ph_excess, sh_deficit)
        ph_to_th_reduction = min(ph_excess - ph_to_sh, th_excess * 0.3)  # Reduce th excess by 30%
        
        print(f"\nRecommended replacements:")
        print(f"  Replace {ph_to_sh:.0f} 'ph' words with 'sh'")
        print(f"  Replace {ph_to_th_reduction:.0f} 'ph' words with 'th' (to reduce th excess)")
        print(f"  Total 'ph' replacements needed: {ph_to_sh + ph_to_th_reduction:.0f}")
        
        return {
            'ph_to_sh': int(ph_to_sh),
            'ph_to_th': int(ph_to_th_reduction),
            'total_replacements': int(ph_to_sh + ph_to_th_reduction)
        }
    
    def categorize_replacement_candidates(self, targets):
        """Categorize 'ph' words by replacement suitability."""
        print(f"\n" + "="*60)
        print("REPLACEMENT CANDIDATE CATEGORIZATION")
        print("="*60)
        
        # Priority categories for replacement
        categories = {
            'high_priority': [],      # Easy to replace, common patterns
            'medium_priority': [],    # Moderate replacement difficulty
            'low_priority': [],       # Difficult to replace, unique meanings
            'preserve': []            # Should not be replaced
        }
        
        # Words to preserve (core concepts, unique meanings)
        preserve_words = {
            'phemi', 'pheno', 'phewa', 'phemo', 'phire',  # Core communication/mental verbs
            'phahi', 'phera', 'phoni',  # Core existence verbs
            'mipha', 'sepha', 'teshe',  # Core evaluative adjectives
        }
        
        for pos_name, words in self.ph_words.items():
            print(f"\n{pos_name.upper()} ({len(words)} 'ph' words):")
            
            for word_data in words:
                word = word_data['word']
                meaning = word_data['meaning']
                
                if word in preserve_words:
                    categories['preserve'].append(word_data)
                    priority = "PRESERVE"
                elif self._is_high_priority_replacement(word_data):
                    categories['high_priority'].append(word_data)
                    priority = "HIGH"
                elif self._is_medium_priority_replacement(word_data):
                    categories['medium_priority'].append(word_data)
                    priority = "MEDIUM"
                else:
                    categories['low_priority'].append(word_data)
                    priority = "LOW"
                
                print(f"  {word:<12} ({meaning:<20}) - {priority}")
        
        # Summary
        print(f"\n" + "-"*60)
        print("REPLACEMENT PRIORITY SUMMARY:")
        print("-"*60)
        for category, words in categories.items():
            print(f"{category.replace('_', ' ').title()}: {len(words)} words")
        
        return categories
    
    def _is_high_priority_replacement(self, word_data):
        """Determine if a word is high priority for replacement."""
        word = word_data['word']
        meaning = word_data['meaning']
        pos = word_data['pos']
        
        # High priority: physical properties, simple actions, common adjectives
        high_priority_meanings = [
            'fragrant', 'rough', 'smooth', 'soft', 'light', 'heavy',
            'carry', 'push', 'pull', 'throw', 'put', 'set',
            'air out', 'bring', 'start', 'try', 'wait',
            'allow', 'hold', 'let', 'offer', 'share', 'take'
        ]
        
        return any(keyword in meaning.lower() for keyword in high_priority_meanings)
    
    def _is_medium_priority_replacement(self, word_data):
        """Determine if a word is medium priority for replacement."""
        word = word_data['word']
        meaning = word_data['meaning']
        pos = word_data['pos']
        
        # Medium priority: specific actions, descriptive adjectives
        medium_priority_meanings = [
            'answer', 'report', 'compose', 'decide', 'forget', 'like',
            'appear', 'fall', 'leave', 'walk', 'exit', 'become',
            'build', 'create', 'destroy', 'buy', 'return', 'send',
            'hear', 'see', 'taste', 'watch', 'do', 'fail'
        ]
        
        return any(keyword in meaning.lower() for keyword in medium_priority_meanings)
    
    def suggest_specific_replacements(self, categories, targets):
        """Suggest specific word replacements."""
        print(f"\n" + "="*60)
        print("SPECIFIC REPLACEMENT SUGGESTIONS")
        print("="*60)
        
        replacements_needed = targets['total_replacements']
        sh_replacements_needed = targets['ph_to_sh']
        
        print(f"Need to replace {replacements_needed} 'ph' words total")
        print(f"Priority: {sh_replacements_needed} to 'sh', remainder to 'th'")
        
        suggested_replacements = []
        
        # Start with high priority candidates
        candidates = categories['high_priority'] + categories['medium_priority']
        
        print(f"\nSUGGESTED REPLACEMENTS:")
        print("-" * 40)
        
        sh_count = 0
        th_count = 0
        
        for i, word_data in enumerate(candidates[:replacements_needed]):
            word = word_data['word']
            meaning = word_data['meaning']
            pos = word_data['pos']
            
            # Determine replacement fricative
            if sh_count < sh_replacements_needed:
                new_fricative = 'sh'
                sh_count += 1
            else:
                new_fricative = 'th'
                th_count += 1
            
            # Generate new word
            new_word = word.replace('ph', new_fricative)
            
            suggested_replacements.append({
                'original': word,
                'new': new_word,
                'meaning': meaning,
                'pos': pos,
                'fricative': new_fricative
            })
            
            print(f"{i+1:2d}. {word:<12} → {new_word:<12} ({meaning}) [{pos}]")
        
        print(f"\nReplacement summary:")
        print(f"  'ph' → 'sh': {sh_count} words")
        print(f"  'ph' → 'th': {th_count} words")
        print(f"  Total: {len(suggested_replacements)} words")
        
        return suggested_replacements
    
    def run_phase2_analysis(self):
        """Run complete Phase 2 analysis."""
        self.load_pos_files()
        targets = self.analyze_replacement_candidates()
        categories = self.categorize_replacement_candidates(targets)
        replacements = self.suggest_specific_replacements(categories, targets)
        
        return {
            'targets': targets,
            'categories': categories,
            'suggested_replacements': replacements
        }


def main():
    """Main function to run Phase 2 analysis."""
    analyzer = Phase2Analyzer()
    results = analyzer.run_phase2_analysis()
    
    print(f"\n" + "="*60)
    print("PHASE 2 ANALYSIS COMPLETE")
    print("="*60)
    print("Ready to proceed with strategic 'ph' word replacements!")


if __name__ == "__main__":
    main() 