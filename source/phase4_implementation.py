#!/usr/bin/env python3
"""
Phase 4 Implementation: True Phonological Optimization

Implements the true optimization targets from Phase 4 analysis:
1. Standalone vowel optimization: e → u (120 conversions)
2. Standalone consonant optimization: s → h (83 conversions), t → r (38 conversions)

Maintains complete phonotactic pattern compliance and unit independence.
"""

import os
import re
from collections import defaultdict, Counter
from pathlib import Path


class Phase4Implementation:
    """Implements Phase 4 optimization with true phonological targets."""
    
    def __init__(self, pos_dir="pos"):
        self.pos_dir = Path(pos_dir)
        self.consonants = ['h', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w']
        self.vowels = ['i', 'u', 'e', 'o', 'a']
        self.fricatives = ['ph', 'wh', 'th', 'sh']
        
        # Vowel pairs for proper parsing
        self.vowel_pairs = []
        for v1 in self.vowels:
            for v2 in self.vowels:
                if v1 != v2:
                    self.vowel_pairs.append(v1 + v2)
        
        # Optimization targets from true analysis
        self.targets = {
            'vowel_conversions': {
                'e_to_u': 120  # e → u conversions needed
            },
            'consonant_conversions': {
                's_to_h': 83,  # s → h conversions needed
                't_to_r': 38   # t → r conversions needed
            }
        }
        
    def find_optimization_candidates(self):
        """Find specific words suitable for Phase 4 optimization."""
        print("PHASE 4 IMPLEMENTATION: Finding Optimization Candidates")
        print("=" * 70)
        
        candidates = {
            'e_to_u': [],
            's_to_h': [],
            't_to_r': []
        }
        
        for pos_file in self.pos_dir.glob("*.md"):
            pos_name = pos_file.stem
            words = self._extract_words_from_file(pos_file, pos_name)
            
            for word_data in words:
                word = word_data['word']
                meaning = word_data['meaning']
                
                # Find e → u candidates (standalone e that can become u)
                if self._has_standalone_vowel(word, 'e'):
                    u_variant = self._convert_standalone_vowel(word, 'e', 'u')
                    if u_variant and self._is_phonotactically_valid(u_variant, pos_name):
                        priority = self._assess_vowel_conversion_priority(word, meaning, pos_name)
                        candidates['e_to_u'].append({
                            'original': word,
                            'new': u_variant,
                            'meaning': meaning,
                            'pos': pos_name,
                            'priority': priority
                        })
                
                # Find s → h candidates (standalone s that can become h)
                if self._has_standalone_consonant(word, 's'):
                    h_variant = self._convert_standalone_consonant(word, 's', 'h')
                    if h_variant and self._is_phonotactically_valid(h_variant, pos_name):
                        priority = self._assess_consonant_conversion_priority(word, meaning, pos_name)
                        candidates['s_to_h'].append({
                            'original': word,
                            'new': h_variant,
                            'meaning': meaning,
                            'pos': pos_name,
                            'priority': priority
                        })
                
                # Find t → r candidates (standalone t that can become r)
                if self._has_standalone_consonant(word, 't'):
                    r_variant = self._convert_standalone_consonant(word, 't', 'r')
                    if r_variant and self._is_phonotactically_valid(r_variant, pos_name):
                        priority = self._assess_consonant_conversion_priority(word, meaning, pos_name)
                        candidates['t_to_r'].append({
                            'original': word,
                            'new': r_variant,
                            'meaning': meaning,
                            'pos': pos_name,
                            'priority': priority
                        })
        
        # Sort candidates by priority and show top candidates
        for conversion_type, word_list in candidates.items():
            word_list.sort(key=lambda x: x['priority'], reverse=True)
            target_count = self.targets['vowel_conversions'].get(conversion_type, 
                          self.targets['consonant_conversions'].get(conversion_type, 0))
            
            print(f"\n{conversion_type.upper()} candidates (need {target_count} conversions):")
            print(f"Found {len(word_list)} total candidates")
            
            # Show top candidates up to target + 20% buffer
            show_count = min(len(word_list), int(target_count * 1.2))
            for i, candidate in enumerate(word_list[:show_count]):
                print(f"  {i+1:2d}. {candidate['original']} → {candidate['new']} "
                      f"({candidate['meaning']}) [{candidate['pos']}] "
                      f"(priority: {candidate['priority']})")
        
        return candidates
    
    def validate_conversions(self, candidates):
        """Validate conversions for conflicts and phonotactic compliance."""
        print(f"\n" + "=" * 70)
        print("PHASE 4 VALIDATION: Checking for Conflicts")
        print("=" * 70)
        
        validated_conversions = {}
        conflicts_found = []
        
        # Track all proposed new words to detect conflicts
        all_new_words = set()
        
        for conversion_type, word_list in candidates.items():
            target_count = self.targets['vowel_conversions'].get(conversion_type,
                          self.targets['consonant_conversions'].get(conversion_type, 0))
            
            validated_list = []
            
            for candidate in word_list[:target_count]:
                new_word = candidate['new']
                
                # Check for conflicts with existing words or other conversions
                if new_word in all_new_words:
                    conflicts_found.append(f"Duplicate: {new_word} from {conversion_type}")
                    continue
                
                # Check if new word already exists in phi
                if self._word_exists_in_phi(new_word):
                    conflicts_found.append(f"Exists: {new_word} already in phi")
                    continue
                
                # Validate phonotactic pattern
                if not self._is_phonotactically_valid(new_word, candidate['pos']):
                    conflicts_found.append(f"Invalid: {new_word} violates {candidate['pos']} pattern")
                    continue
                
                # If we get here, conversion is valid
                validated_list.append(candidate)
                all_new_words.add(new_word)
            
            validated_conversions[conversion_type] = validated_list
            
            print(f"{conversion_type.upper()}: {len(validated_list)}/{target_count} conversions validated")
        
        if conflicts_found:
            print(f"\nConflicts found ({len(conflicts_found)}):")
            for conflict in conflicts_found[:10]:  # Show first 10
                print(f"  ⚠️  {conflict}")
            if len(conflicts_found) > 10:
                print(f"  ... and {len(conflicts_found) - 10} more")
        else:
            print("\n✅ No conflicts found!")
        
        return validated_conversions, conflicts_found
    
    def apply_conversions(self, validated_conversions):
        """Apply validated conversions to POS files."""
        print(f"\n" + "=" * 70)
        print("PHASE 4 APPLICATION: Applying Conversions")
        print("=" * 70)
        
        total_conversions = 0
        conversion_log = []
        
        # Group conversions by POS file
        pos_conversions = defaultdict(list)
        
        for conversion_type, word_list in validated_conversions.items():
            for candidate in word_list:
                pos_conversions[candidate['pos']].append({
                    'type': conversion_type,
                    'original': candidate['original'],
                    'new': candidate['new'],
                    'meaning': candidate['meaning']
                })
        
        # Apply conversions to each POS file
        for pos_name, conversions in pos_conversions.items():
            pos_file = self.pos_dir / f"{pos_name}.md"
            
            if not pos_file.exists():
                print(f"⚠️  Warning: {pos_file} not found")
                continue
            
            # Read current content
            with open(pos_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Apply each conversion
            modified_content = content
            pos_conversion_count = 0
            
            for conversion in conversions:
                original = conversion['original']
                new_word = conversion['new']
                
                # Replace in table format: | original | meaning |
                pattern = rf'\|\s*{re.escape(original)}\s*\|\s*([^|]+)\s*\|'
                replacement = f'| {new_word} | \\1 |'
                
                new_content = re.sub(pattern, replacement, modified_content)
                
                if new_content != modified_content:
                    modified_content = new_content
                    pos_conversion_count += 1
                    total_conversions += 1
                    
                    conversion_log.append({
                        'pos': pos_name,
                        'type': conversion['type'],
                        'original': original,
                        'new': new_word,
                        'meaning': conversion['meaning']
                    })
                    
                    print(f"  {pos_name}: {original} → {new_word} ({conversion['type']})")
            
            # Write modified content back to file
            if pos_conversion_count > 0:
                with open(pos_file, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                print(f"✅ {pos_name}: {pos_conversion_count} conversions applied")
        
        print(f"\nTotal conversions applied: {total_conversions}")
        
        return conversion_log
    
    def _extract_words_from_file(self, file_path, pos_name):
        """Extract all words from a POS file."""
        words = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
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
    
    def _has_standalone_vowel(self, word, vowel):
        """Check if word has standalone vowel (not in vowel pair)."""
        i = 0
        while i < len(word):
            # Skip fricative digraphs
            if i < len(word) - 1 and word[i:i+2] in self.fricatives:
                i += 2
            # Skip vowel pairs
            elif i < len(word) - 1 and word[i:i+2] in self.vowel_pairs:
                i += 2
            # Check for standalone vowel
            elif word[i] == vowel:
                return True
            else:
                i += 1
        return False
    
    def _has_standalone_consonant(self, word, consonant):
        """Check if word has standalone consonant (not in fricative digraph)."""
        i = 0
        while i < len(word):
            # Skip fricative digraphs
            if i < len(word) - 1 and word[i:i+2] in self.fricatives:
                i += 2
            # Skip vowel pairs
            elif i < len(word) - 1 and word[i:i+2] in self.vowel_pairs:
                i += 2
            # Check for standalone consonant
            elif word[i] == consonant:
                return True
            else:
                i += 1
        return False
    
    def _convert_standalone_vowel(self, word, old_vowel, new_vowel):
        """Convert first standalone vowel occurrence."""
        i = 0
        while i < len(word):
            # Skip fricative digraphs
            if i < len(word) - 1 and word[i:i+2] in self.fricatives:
                i += 2
            # Skip vowel pairs
            elif i < len(word) - 1 and word[i:i+2] in self.vowel_pairs:
                i += 2
            # Convert standalone vowel
            elif word[i] == old_vowel:
                return word[:i] + new_vowel + word[i+1:]
            else:
                i += 1
        return None
    
    def _convert_standalone_consonant(self, word, old_consonant, new_consonant):
        """Convert first standalone consonant occurrence."""
        i = 0
        while i < len(word):
            # Skip fricative digraphs
            if i < len(word) - 1 and word[i:i+2] in self.fricatives:
                i += 2
            # Skip vowel pairs
            elif i < len(word) - 1 and word[i:i+2] in self.vowel_pairs:
                i += 2
            # Convert standalone consonant
            elif word[i] == old_consonant:
                return word[:i] + new_consonant + word[i+1:]
            else:
                i += 1
        return None
    
    def _is_phonotactically_valid(self, word, pos_name):
        """Check if word follows phi phonotactic patterns."""
        if len(word) < 2:
            return False
        
        # Basic pattern checks for major POS
        if pos_name == 'verbs':
            # Verbs: [F][V][C][V] - start with fricative
            return len(word) >= 4 and word[:2] in self.fricatives
        elif pos_name == 'adjectives':
            # Adjectives: [C][V][F][V] - start with consonant
            return (len(word) >= 4 and 
                    word[0] in self.consonants and 
                    word[1] in self.vowels)
        elif pos_name == 'nouns':
            # Nouns: [C/F][V/P][F][P] - complex pattern, basic check
            return len(word) >= 4
        else:
            # Other POS - basic validity
            return True
    
    def _word_exists_in_phi(self, word):
        """Check if word already exists in phi vocabulary."""
        for pos_file in self.pos_dir.glob("*.md"):
            try:
                with open(pos_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                pattern = rf'\|\s*{re.escape(word)}\s*\|'
                if re.search(pattern, content):
                    return True
            except Exception:
                continue
        return False
    
    def _assess_vowel_conversion_priority(self, word, meaning, pos_name):
        """Assess priority for vowel conversion."""
        priority = 0
        
        # Higher priority for words with multiple 'e' instances
        priority += word.count('e') * 2
        
        # Higher priority for common concepts
        common_words = ['water', 'fire', 'earth', 'air', 'tree', 'house', 'person', 'good', 'big']
        if any(concept in meaning.lower() for concept in common_words):
            priority += 3
        
        # Prefer longer words (more stable)
        if len(word) >= 6:
            priority += 2
        elif len(word) >= 5:
            priority += 1
        
        # Prefer certain POS
        if pos_name in ['nouns', 'adjectives']:
            priority += 1
        
        return priority
    
    def _assess_consonant_conversion_priority(self, word, meaning, pos_name):
        """Assess priority for consonant conversion."""
        priority = 0
        
        # Higher priority for words with multiple target consonants
        priority += word.count('s') * 2
        priority += word.count('t') * 2
        
        # Higher priority for common concepts
        common_words = ['water', 'fire', 'earth', 'air', 'tree', 'house', 'person', 'good', 'big']
        if any(concept in meaning.lower() for concept in common_words):
            priority += 3
        
        # Prefer longer words
        if len(word) >= 6:
            priority += 2
        elif len(word) >= 5:
            priority += 1
        
        # Prefer certain POS
        if pos_name in ['nouns', 'adjectives', 'adverbs']:
            priority += 1
        
        return priority
    
    def run_phase4_implementation(self):
        """Run complete Phase 4 implementation."""
        print("Starting Phase 4 Implementation...")
        print("Targets: e→u (120), s→h (83), t→r (38)")
        print()
        
        # Step 1: Find candidates
        candidates = self.find_optimization_candidates()
        
        # Step 2: Validate conversions
        validated_conversions, conflicts = self.validate_conversions(candidates)
        
        # Step 3: Apply conversions
        if any(validated_conversions.values()):
            conversion_log = self.apply_conversions(validated_conversions)
            
            print(f"\n" + "=" * 70)
            print("PHASE 4 IMPLEMENTATION COMPLETE")
            print("=" * 70)
            
            # Summary
            total_applied = len(conversion_log)
            print(f"Successfully applied {total_applied} conversions:")
            
            for conversion_type in ['e_to_u', 's_to_h', 't_to_r']:
                count = len(validated_conversions.get(conversion_type, []))
                target = self.targets['vowel_conversions'].get(conversion_type,
                        self.targets['consonant_conversions'].get(conversion_type, 0))
                percentage = (count / target * 100) if target > 0 else 0
                print(f"  {conversion_type}: {count}/{target} ({percentage:.1f}%)")
            
            return {
                'conversion_log': conversion_log,
                'validated_conversions': validated_conversions,
                'conflicts': conflicts
            }
        else:
            print("\n❌ No valid conversions found!")
            return None


def main():
    """Main function to run Phase 4 implementation."""
    implementer = Phase4Implementation()
    results = implementer.run_phase4_implementation()


if __name__ == "__main__":
    main() 