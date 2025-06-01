#!/usr/bin/env python3
"""
Phase 4 Candidate Finder

Identifies specific words that can be optimized for vowel and consonant balance
while maintaining phonotactic patterns and semantic integrity.
"""

import os
import re
from collections import defaultdict, Counter
from pathlib import Path


class Phase4CandidateFinder:
    """Finds specific optimization candidates for Phase 4."""
    
    def __init__(self, pos_dir="pos"):
        self.pos_dir = Path(pos_dir)
        self.consonants = ['h', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w']
        self.vowels = ['i', 'u', 'e', 'o', 'a']
        self.fricatives = ['ph', 'wh', 'th', 'sh']
        
    def find_vowel_optimization_candidates(self):
        """Find words suitable for vowel optimization (a→u, a→o)."""
        print("PHASE 4 CANDIDATE FINDER: Vowel Optimization")
        print("=" * 60)
        
        candidates = {
            'a_to_u': [],
            'a_to_o': [],
            'e_to_u': [],
            'e_to_o': []
        }
        
        for pos_file in self.pos_dir.glob("*.md"):
            pos_name = pos_file.stem
            words = self._extract_words_from_file(pos_file, pos_name)
            
            for word_data in words:
                word = word_data['word']
                meaning = word_data['meaning']
                
                # Look for words with 'a' that could become 'u' or 'o'
                if 'a' in word and len(word) >= 4:
                    # Try a→u conversion
                    u_variant = word.replace('a', 'u', 1)  # Replace first 'a'
                    if self._is_phonotactically_valid(u_variant, pos_name):
                        candidates['a_to_u'].append({
                            'original': word,
                            'new': u_variant,
                            'meaning': meaning,
                            'pos': pos_name,
                            'priority': self._assess_vowel_priority(word, meaning, pos_name)
                        })
                    
                    # Try a→o conversion
                    o_variant = word.replace('a', 'o', 1)  # Replace first 'a'
                    if self._is_phonotactically_valid(o_variant, pos_name):
                        candidates['a_to_o'].append({
                            'original': word,
                            'new': o_variant,
                            'meaning': meaning,
                            'pos': pos_name,
                            'priority': self._assess_vowel_priority(word, meaning, pos_name)
                        })
                
                # Look for words with 'e' that could become 'u' or 'o'
                if 'e' in word and len(word) >= 4:
                    # Try e→u conversion
                    u_variant = word.replace('e', 'u', 1)
                    if self._is_phonotactically_valid(u_variant, pos_name):
                        candidates['e_to_u'].append({
                            'original': word,
                            'new': u_variant,
                            'meaning': meaning,
                            'pos': pos_name,
                            'priority': self._assess_vowel_priority(word, meaning, pos_name)
                        })
                    
                    # Try e→o conversion
                    o_variant = word.replace('e', 'o', 1)
                    if self._is_phonotactically_valid(o_variant, pos_name):
                        candidates['e_to_o'].append({
                            'original': word,
                            'new': o_variant,
                            'meaning': meaning,
                            'pos': pos_name,
                            'priority': self._assess_vowel_priority(word, meaning, pos_name)
                        })
        
        # Sort by priority and show top candidates
        for conversion_type, word_list in candidates.items():
            word_list.sort(key=lambda x: x['priority'], reverse=True)
            print(f"\n{conversion_type.upper()} candidates ({len(word_list)} total):")
            for i, candidate in enumerate(word_list[:10]):  # Show top 10
                print(f"  {i+1:2d}. {candidate['original']} → {candidate['new']} "
                      f"({candidate['meaning']}) [{candidate['pos']}] "
                      f"(priority: {candidate['priority']})")
        
        return candidates
    
    def find_consonant_optimization_candidates(self):
        """Find words suitable for consonant optimization (s→h, t→h, etc.)."""
        print(f"\n" + "=" * 60)
        print("PHASE 4 CANDIDATE FINDER: Consonant Optimization")
        print("=" * 60)
        
        candidates = {
            's_to_h': [],
            't_to_h': [],
            's_to_w': [],
            't_to_r': [],
            'l_to_h': []
        }
        
        for pos_file in self.pos_dir.glob("*.md"):
            pos_name = pos_file.stem
            words = self._extract_words_from_file(pos_file, pos_name)
            
            for word_data in words:
                word = word_data['word']
                meaning = word_data['meaning']
                
                # Only consider standalone consonants (not in fricative digraphs)
                standalone_consonants = self._get_standalone_consonants(word)
                
                # Look for 's' that could become 'h'
                if 's' in standalone_consonants and len(word) >= 4:
                    h_variant = self._replace_standalone_consonant(word, 's', 'h')
                    if h_variant and self._is_phonotactically_valid(h_variant, pos_name):
                        candidates['s_to_h'].append({
                            'original': word,
                            'new': h_variant,
                            'meaning': meaning,
                            'pos': pos_name,
                            'priority': self._assess_consonant_priority(word, meaning, pos_name)
                        })
                
                # Look for 't' that could become 'h'
                if 't' in standalone_consonants and len(word) >= 4:
                    h_variant = self._replace_standalone_consonant(word, 't', 'h')
                    if h_variant and self._is_phonotactically_valid(h_variant, pos_name):
                        candidates['t_to_h'].append({
                            'original': word,
                            'new': h_variant,
                            'meaning': meaning,
                            'pos': pos_name,
                            'priority': self._assess_consonant_priority(word, meaning, pos_name)
                        })
                
                # Look for 's' that could become 'w'
                if 's' in standalone_consonants and len(word) >= 4:
                    w_variant = self._replace_standalone_consonant(word, 's', 'w')
                    if w_variant and self._is_phonotactically_valid(w_variant, pos_name):
                        candidates['s_to_w'].append({
                            'original': word,
                            'new': w_variant,
                            'meaning': meaning,
                            'pos': pos_name,
                            'priority': self._assess_consonant_priority(word, meaning, pos_name)
                        })
                
                # Look for 't' that could become 'r'
                if 't' in standalone_consonants and len(word) >= 4:
                    r_variant = self._replace_standalone_consonant(word, 't', 'r')
                    if r_variant and self._is_phonotactically_valid(r_variant, pos_name):
                        candidates['t_to_r'].append({
                            'original': word,
                            'new': r_variant,
                            'meaning': meaning,
                            'pos': pos_name,
                            'priority': self._assess_consonant_priority(word, meaning, pos_name)
                        })
                
                # Look for 'l' that could become 'h' (l is slightly overused)
                if 'l' in standalone_consonants and len(word) >= 4:
                    h_variant = self._replace_standalone_consonant(word, 'l', 'h')
                    if h_variant and self._is_phonotactically_valid(h_variant, pos_name):
                        candidates['l_to_h'].append({
                            'original': word,
                            'new': h_variant,
                            'meaning': meaning,
                            'pos': pos_name,
                            'priority': self._assess_consonant_priority(word, meaning, pos_name)
                        })
        
        # Sort by priority and show top candidates
        for conversion_type, word_list in candidates.items():
            word_list.sort(key=lambda x: x['priority'], reverse=True)
            print(f"\n{conversion_type.upper()} candidates ({len(word_list)} total):")
            for i, candidate in enumerate(word_list[:8]):  # Show top 8
                print(f"  {i+1:2d}. {candidate['original']} → {candidate['new']} "
                      f"({candidate['meaning']}) [{candidate['pos']}] "
                      f"(priority: {candidate['priority']})")
        
        return candidates
    
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
    
    def _get_standalone_consonants(self, word):
        """Get standalone consonants (not in fricative digraphs)."""
        standalone = []
        i = 0
        while i < len(word):
            if i < len(word) - 1 and word[i:i+2] in self.fricatives:
                i += 2  # Skip fricative digraph
            elif word[i] in self.consonants:
                standalone.append(word[i])
                i += 1
            else:
                i += 1
        return standalone
    
    def _replace_standalone_consonant(self, word, old_consonant, new_consonant):
        """Replace first occurrence of standalone consonant."""
        i = 0
        while i < len(word):
            if i < len(word) - 1 and word[i:i+2] in self.fricatives:
                i += 2  # Skip fricative digraph
            elif word[i] == old_consonant:
                # Replace this consonant
                return word[:i] + new_consonant + word[i+1:]
            else:
                i += 1
        return None
    
    def _is_phonotactically_valid(self, word, pos_name):
        """Basic check if word follows phi phonotactic patterns."""
        # This is a simplified check - in practice, we'd use the full validator
        if len(word) < 2:
            return False
        
        # Check for basic pattern compliance
        if pos_name == 'verbs':
            # Verbs should start with fricative: [F][V][C][V]
            return len(word) >= 4 and word[:2] in self.fricatives
        elif pos_name == 'adjectives':
            # Adjectives: [C][V][F][V]
            return (len(word) >= 4 and 
                    word[0] in self.consonants and 
                    word[1] in self.vowels)
        elif pos_name == 'nouns':
            # Nouns: [C/F][V/P][F][P] - more complex, simplified check
            return len(word) >= 4
        else:
            # Other POS - basic check
            return True
    
    def _assess_vowel_priority(self, word, meaning, pos_name):
        """Assess priority for vowel optimization."""
        priority = 0
        
        # Higher priority for words with multiple target vowels
        priority += word.count('a') * 3  # 'a' is most overused
        priority += word.count('e') * 1  # 'e' is slightly overused
        
        # Higher priority for common words
        common_meanings = [
            'water', 'fire', 'earth', 'air', 'sun', 'moon', 'star',
            'tree', 'flower', 'animal', 'person', 'house', 'food',
            'good', 'bad', 'big', 'small', 'hot', 'cold', 'new', 'old',
            'go', 'come', 'see', 'hear', 'say', 'do', 'make', 'have'
        ]
        
        if any(keyword in meaning.lower() for keyword in common_meanings):
            priority += 2
        
        # Prefer longer words (more stable)
        if len(word) >= 6:
            priority += 2
        elif len(word) >= 5:
            priority += 1
        
        # Prefer certain POS
        if pos_name in ['nouns', 'adjectives']:
            priority += 1
        
        return priority
    
    def _assess_consonant_priority(self, word, meaning, pos_name):
        """Assess priority for consonant optimization."""
        priority = 0
        
        # Higher priority for words with multiple target consonants
        standalone = self._get_standalone_consonants(word)
        priority += standalone.count('s') * 3  # 's' is most overused
        priority += standalone.count('t') * 3  # 't' is most overused
        priority += standalone.count('l') * 1  # 'l' is slightly overused
        
        # Higher priority for common words
        common_meanings = [
            'water', 'fire', 'earth', 'air', 'sun', 'moon', 'star',
            'tree', 'flower', 'animal', 'person', 'house', 'food',
            'good', 'bad', 'big', 'small', 'hot', 'cold', 'new', 'old',
            'go', 'come', 'see', 'hear', 'say', 'do', 'make', 'have'
        ]
        
        if any(keyword in meaning.lower() for keyword in common_meanings):
            priority += 2
        
        # Prefer longer words
        if len(word) >= 6:
            priority += 2
        elif len(word) >= 5:
            priority += 1
        
        # Prefer certain POS
        if pos_name in ['nouns', 'adjectives', 'adverbs']:
            priority += 1
        
        return priority
    
    def run_candidate_search(self):
        """Run complete candidate search."""
        vowel_candidates = self.find_vowel_optimization_candidates()
        consonant_candidates = self.find_consonant_optimization_candidates()
        
        print(f"\n" + "=" * 60)
        print("PHASE 4 CANDIDATE SEARCH COMPLETE")
        print("=" * 60)
        
        total_vowel = sum(len(candidates) for candidates in vowel_candidates.values())
        total_consonant = sum(len(candidates) for candidates in consonant_candidates.values())
        
        print(f"Found {total_vowel} vowel optimization candidates")
        print(f"Found {total_consonant} consonant optimization candidates")
        print("Ready for validation and implementation!")
        
        return {
            'vowel_candidates': vowel_candidates,
            'consonant_candidates': consonant_candidates
        }


def main():
    """Main function to run Phase 4 candidate search."""
    finder = Phase4CandidateFinder()
    results = finder.run_candidate_search()


if __name__ == "__main__":
    main() 