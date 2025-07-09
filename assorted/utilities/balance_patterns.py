#!/usr/bin/env python3
"""
Generate new phi words to balance the four phonotactic patterns.
Prioritizes CPFP, FPFP, and FVFP to achieve ~25% distribution.
"""

import json
import random
from collections import defaultdict, Counter
from itertools import product

def load_existing_words():
    """Load the existing validated phi words."""
    try:
        with open('validated_phi_words.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            return set(data['words'])
    except FileNotFoundError:
        print("❌ Run generate_noun_cache.py first to create validated_phi_words.json")
        return set()

def get_phonological_components():
    """Define all valid phi phonological components."""
    consonants = list('hlmnprstw')
    vowels = list('aeiou')
    fricatives = ['ph', 'wh', 'th', 'sh']
    
    # Generate all possible vowel pairs (two different vowels)
    vowel_pairs = []
    for v1 in vowels:
        for v2 in vowels:
            if v1 != v2:
                vowel_pairs.append(v1 + v2)
    
    return consonants, vowels, fricatives, vowel_pairs

def analyze_existing_usage(existing_words):
    """Analyze phonological usage in existing words."""
    consonant_usage = Counter()
    vowel_usage = Counter()
    fricative_usage = Counter()
    vowel_pair_usage = Counter()
    
    for word in existing_words:
        # Parse each word to extract components
        i = 0
        while i < len(word):
            # Check for fricative digraphs first
            if i < len(word) - 1:
                digraph = word[i:i+2]
                if digraph in ['ph', 'wh', 'th', 'sh']:
                    fricative_usage[digraph] += 1
                    i += 2
                    continue
            
            # Check for vowel pairs
            if i < len(word) - 1:
                char1, char2 = word[i], word[i+1]
                if char1 in 'aeiou' and char2 in 'aeiou' and char1 != char2:
                    vowel_pair_usage[char1 + char2] += 1
                    i += 2
                    continue
            
            # Single character
            char = word[i]
            if char in 'aeiou':
                vowel_usage[char] += 1
            elif char in 'hlmnprstw':
                consonant_usage[char] += 1
            
            i += 1
    
    return consonant_usage, vowel_usage, fricative_usage, vowel_pair_usage

def generate_pattern_words(pattern, consonants, vowels, fricatives, vowel_pairs, 
                          existing_words, target_count):
    """Generate words for a specific pattern."""
    generated = []
    attempts = 0
    max_attempts = target_count * 500  # Increased for large batches
    
    while len(generated) < target_count and attempts < max_attempts:
        attempts += 1
        
        if pattern == 'CPFP':
            # [C][P][F][P] - consonant + vowel-pair + fricative + vowel-pair
            c = random.choice(consonants)
            p1 = random.choice(vowel_pairs)
            f = random.choice(fricatives)
            p2 = random.choice(vowel_pairs)
            word = c + p1 + f + p2
            
        elif pattern == 'FPFP':
            # [F][P][F][P] - fricative + vowel-pair + fricative + vowel-pair
            f1 = random.choice(fricatives)
            p1 = random.choice(vowel_pairs)
            f2 = random.choice(fricatives)
            p2 = random.choice(vowel_pairs)
            word = f1 + p1 + f2 + p2
            
        elif pattern == 'FVFP':
            # [F][V][F][P] - fricative + vowel + fricative + vowel-pair
            f1 = random.choice(fricatives)
            v = random.choice(vowels)
            f2 = random.choice(fricatives)
            p = random.choice(vowel_pairs)
            word = f1 + v + f2 + p
            
        elif pattern == 'CVFP':
            # [C][V][F][P] - consonant + vowel + fricative + vowel-pair
            c = random.choice(consonants)
            v = random.choice(vowels)
            f = random.choice(fricatives)
            p = random.choice(vowel_pairs)
            word = c + v + f + p
        
        # Check if word already exists
        if word not in existing_words and word not in generated:
            generated.append(word)
    
    return generated

def main():
    print("🎯 Phi Word Pattern Balancer")
    print("=" * 50)
    
    # Load existing words
    existing_words = load_existing_words()
    if not existing_words:
        return
    
    print(f"📚 Loaded {len(existing_words)} existing validated words")
    
    # Get phonological components
    consonants, vowels, fricatives, vowel_pairs = get_phonological_components()
    
    # Analyze current usage
    c_usage, v_usage, f_usage, vp_usage = analyze_existing_usage(existing_words)
    
    # Calculate current distribution
    total_words = len(existing_words)
    target_per_pattern = 346  # True mathematical balance: 346 × 4 = 1,384 total
    
    # Count current patterns
    pattern_counts = {'CVFP': 346, 'CPFP': 31, 'FVFP': 78, 'FPFP': 34}
    
    print("\n📊 CURRENT DISTRIBUTION:")
    for pattern, count in pattern_counts.items():
        percentage = (count / total_words) * 100
        print(f"   {pattern}: {count:3d} words ({percentage:4.1f}%)")
    
    print(f"\n🎯 TARGET: {target_per_pattern} words per pattern (25% each = 1,384 total)")
    
    # Calculate how many words we need for each pattern
    words_needed = {}
    for pattern, current in pattern_counts.items():
        needed = max(0, target_per_pattern - current)
        words_needed[pattern] = needed
        if needed > 0:
            print(f"   Need {needed:3d} more {pattern} words")
    
    total_needed = sum(words_needed.values())
    print(f"\n📈 Total new words needed: {total_needed}")
    print(f"📊 Final vocabulary size: {total_words + total_needed}")
    
    print("\n🔧 GENERATING NEW WORDS FOR PERFECT BALANCE...")
    print("-" * 60)
    
    all_new_words = {}
    
    # Generate words for underrepresented patterns
    for pattern in ['CPFP', 'FPFP', 'FVFP', 'CVFP']:  # Check all patterns
        needed = words_needed[pattern]
        if needed > 0:
            print(f"🔄 Generating {needed} {pattern} words...")
            new_words = generate_pattern_words(
                pattern, consonants, vowels, fricatives, vowel_pairs,
                existing_words, needed
            )
            all_new_words[pattern] = new_words
            existing_words.update(new_words)  # Add to avoid duplicates
            print(f"   ✅ Generated {len(new_words)} words")
        else:
            print(f"✅ {pattern} already balanced ({pattern_counts[pattern]} words)")
            all_new_words[pattern] = []
    
    # Save results
    output = {
        'generation_summary': {
            'existing_word_count': len(load_existing_words()),
            'target_per_pattern': target_per_pattern,
            'words_needed': words_needed,
            'total_new_words': sum(len(words) for words in all_new_words.values())
        },
        'new_words_by_pattern': all_new_words
    }
    
    with open('pattern_balance_words.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    # Create simple text file
    with open('pattern_balance_words.txt', 'w', encoding='utf-8') as f:
        f.write("# New Phi Words for Pattern Balance\n\n")
        
        for pattern, words in all_new_words.items():
            if words:
                f.write(f"## {pattern} Pattern ({len(words)} words)\n")
                for word in sorted(words):
                    f.write(f"{word}\n")
                f.write("\n")
    
    print(f"\n✅ GENERATION COMPLETE!")
    print("📁 Files created:")
    print("   - pattern_balance_words.json (structured data)")
    print("   - pattern_balance_words.txt (organized by pattern)")
    
    print(f"\n📊 NEW WORDS GENERATED:")
    total_generated = 0
    for pattern, words in all_new_words.items():
        count = len(words)
        total_generated += count
        print(f"   {pattern}: {count:2d} words")
    
    print(f"\n🎯 PROJECTED BALANCE AFTER ADDITION:")
    new_total = 1384  # 346 × 4 patterns
    for pattern, current in pattern_counts.items():
        new_count = target_per_pattern  # All patterns will have exactly 346 words
        percentage = (new_count / new_total) * 100
        print(f"   {pattern}: {new_count:3d} words ({percentage:4.1f}%)")

if __name__ == "__main__":
    main() 