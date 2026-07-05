#!/usr/bin/env python3
"""
Phi Vocabulary Statistics
Shows statistics about the current vocabulary
"""

import json
from pathlib import Path
from collections import Counter, defaultdict

def analyze_vocabulary(words_dir: Path):
    """Analyze the Phi vocabulary and generate statistics."""
    stats = {
        'total_words': 0,
        'categories': defaultdict(int),
        'syllable_counts': Counter(),
        'pos_counts': Counter(),
        'pillar_counts': Counter(),
        'fricative_counts': Counter(),
        'vowel_hiatus_count': 0,
        'words_by_length': Counter(),
        'initial_sounds': Counter()
    }
    
    fricatives = {'ph', 'th', 'sh', 'wh'}
    
    for category_dir in words_dir.iterdir():
        if category_dir.is_dir() and not category_dir.name.startswith('.'):
            for json_file in category_dir.glob('*.json'):
                if json_file.name not in ['SUMMARY.md'] and not json_file.name.endswith('.md'):
                    try:
                        with open(json_file, 'r', encoding='utf-8') as f:
                            data = json.load(f)
                            if isinstance(data, list) and len(data) > 0:
                                word_data = data[0]
                                
                                # Count basic stats
                                stats['total_words'] += 1
                                stats['categories'][category_dir.name] += 1
                                
                                # Word info
                                word = word_data.get('word', '')
                                stats['words_by_length'][len(word)] += 1
                                
                                # Initial sound
                                if len(word) >= 2 and word[:2] in fricatives:
                                    stats['initial_sounds'][word[:2]] += 1
                                elif len(word) >= 1:
                                    stats['initial_sounds'][word[0]] += 1
                                
                                # Syllable count
                                syllables = word_data.get('syllables', [])
                                stats['syllable_counts'][len(syllables)] += 1
                                
                                # Parts of speech
                                for pos in word_data.get('pos', []):
                                    stats['pos_counts'][pos] += 1
                                
                                # Pillars
                                for pillar in word_data.get('pillars', []):
                                    stats['pillar_counts'][pillar] += 1
                                
                                # Fricatives
                                for fric in fricatives:
                                    if fric in word:
                                        stats['fricative_counts'][fric] += 1
                                
                                # Vowel hiatus (simplified check)
                                vowels = 'aeiou'
                                for i in range(len(word) - 1):
                                    if word[i] in vowels and word[i+1] in vowels:
                                        stats['vowel_hiatus_count'] += 1
                                        break
                                
                    except Exception as e:
                        print(f"Error reading {json_file}: {e}")
    
    return stats

def print_stats(stats):
    """Print formatted statistics."""
    print("\n🌟 PHI VOCABULARY STATISTICS 🌟\n")
    print("=" * 50)
    
    print(f"\n📊 TOTAL WORDS: {stats['total_words']}")
    
    print("\n📁 WORDS BY CATEGORY:")
    for category, count in sorted(stats['categories'].items()):
        percentage = (count / stats['total_words']) * 100
        print(f"   {category:<40} {count:>4} ({percentage:>5.1f}%)")
    
    print("\n🔤 SYLLABLE DISTRIBUTION:")
    total_syllables = sum(stats['syllable_counts'].values())
    for syll_count in sorted(stats['syllable_counts'].keys()):
        count = stats['syllable_counts'][syll_count]
        percentage = (count / total_syllables) * 100
        print(f"   {syll_count}-syllable words: {count:>4} ({percentage:>5.1f}%)")
    
    # Calculate 2:3 syllable ratio
    two_syll = stats['syllable_counts'].get(2, 0)
    three_syll = stats['syllable_counts'].get(3, 0)
    if three_syll > 0:
        ratio = two_syll / three_syll
        print(f"\n   2-syllable to 3-syllable ratio: {ratio:.2f}:1")
    
    print("\n🗣️ PARTS OF SPEECH:")
    for pos, count in sorted(stats['pos_counts'].items(), key=lambda x: -x[1])[:10]:
        print(f"   {pos:<15} {count:>4}")
    
    print("\n🎯 PHILOSOPHICAL PILLARS:")
    for pillar, count in sorted(stats['pillar_counts'].items(), key=lambda x: -x[1]):
        percentage = (count / stats['total_words']) * 100
        print(f"   {pillar:<20} {count:>4} ({percentage:>5.1f}%)")
    
    print("\n🔊 PHONOLOGICAL FEATURES:")
    print(f"   Words with fricative digraphs:")
    for fric, count in sorted(stats['fricative_counts'].items()):
        print(f"      {fric}: {count}")
    print(f"   Words with vowel hiatus: {stats['vowel_hiatus_count']}")
    
    print("\n🔤 INITIAL SOUNDS:")
    for sound, count in sorted(stats['initial_sounds'].items(), key=lambda x: -x[1])[:15]:
        percentage = (count / stats['total_words']) * 100
        print(f"   {sound:<5} {count:>4} ({percentage:>5.1f}%)")
    
    print("\n📏 WORD LENGTH DISTRIBUTION:")
    for length, count in sorted(stats['words_by_length'].items()):
        print(f"   {length} characters: {count}")
    
    print("\n" + "=" * 50)

def main():
    words_dir = Path(__file__).parent.parent / "words"
    
    if not words_dir.exists():
        print(f"❌ Words directory not found: {words_dir}")
        return
    
    stats = analyze_vocabulary(words_dir)
    print_stats(stats)

if __name__ == "__main__":
    main()