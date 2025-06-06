#!/usr/bin/env python3
"""
Create a comprehensive pool of all 1,384 validated phi word forms.
This pool will be managed - words removed as they get assigned meanings.
"""

import json
from datetime import datetime

def main():
    print("🔄 Creating Comprehensive Phi Word Pool")
    print("=" * 50)
    
    # Load original validated words
    try:
        with open('validated_phi_words.json', 'r', encoding='utf-8') as f:
            original_data = json.load(f)
            original_words = set(original_data['words'])
        print(f"📚 Loaded {len(original_words)} original validated words")
    except FileNotFoundError:
        print("❌ validated_phi_words.json not found")
        return
    
    # Load new generated words
    try:
        with open('pattern_balance_words.json', 'r', encoding='utf-8') as f:
            balance_data = json.load(f)
            new_words_by_pattern = balance_data['new_words_by_pattern']
        
        # Collect all new words
        new_words = set()
        for pattern, words in new_words_by_pattern.items():
            new_words.update(words)
        
        print(f"🆕 Loaded {len(new_words)} newly generated words")
    except FileNotFoundError:
        print("❌ pattern_balance_words.json not found")
        return
    
    # Combine all words
    all_words = original_words.union(new_words)
    
    # Define pattern analysis function locally
    def analyze_word_pattern(word: str) -> tuple:
        pattern = ""
        i = 0
        
        while i < len(word):
            # Check for fricative digraphs first
            if i < len(word) - 1:
                digraph = word[i:i+2]
                if digraph in ['ph', 'wh', 'th', 'sh']:
                    pattern += 'F'
                    i += 2
                    continue
            
            # Check for vowel pairs
            if i < len(word) - 1:
                char1, char2 = word[i], word[i+1]
                if char1 in 'aeiou' and char2 in 'aeiou' and char1 != char2:
                    pattern += 'P'
                    i += 2
                    continue
            
            # Single character
            char = word[i]
            if char in 'aeiou':
                pattern += 'V'
            elif char in 'hlmnprstw':
                pattern += 'C'
            else:
                return pattern, [], False, []  # Invalid character
            
            i += 1
        
        is_valid = pattern in ['CVFP', 'CPFP', 'FVFP', 'FPFP'] and len(pattern) == 4
        return pattern, [], is_valid, []
    
    # Organize by pattern for the pool
    word_pool = {
        'CVFP': [],
        'CPFP': [],
        'FVFP': [],
        'FPFP': []
    }
    
    for word in sorted(all_words):
        pattern, _, is_valid, _ = analyze_word_pattern(word)
        if is_valid:
            word_pool[pattern].append(word)
    
    # Create the comprehensive pool file
    pool_data = {
        'metadata': {
            'created': datetime.now().isoformat(),
            'total_words': len(all_words),
            'purpose': 'Available phi word forms for lexicon assignment',
            'usage': 'Remove words from this pool as they get assigned meanings',
            'pattern_counts': {
                pattern: len(words) for pattern, words in word_pool.items()
            }
        },
        'available_words': word_pool,
        'assignment_log': []  # Track words as they get assigned
    }
    
    # Save the comprehensive pool
    with open('phi_word_pool.json', 'w', encoding='utf-8') as f:
        json.dump(pool_data, f, indent=2, ensure_ascii=False)
    
    # Create a simple flat list version too
    all_words_list = []
    for pattern, words in word_pool.items():
        all_words_list.extend(words)
    
    with open('phi_word_pool.txt', 'w', encoding='utf-8') as f:
        f.write("# Phi Word Pool - Available Forms\n")
        f.write(f"# Total: {len(all_words_list)} words\n")
        f.write(f"# Created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        for word in sorted(all_words_list):
            f.write(f"{word}\n")
    
    print(f"\n✅ COMPREHENSIVE WORD POOL CREATED!")
    print("📁 Files created:")
    print("   - phi_word_pool.json (manageable pool with metadata)")
    print("   - phi_word_pool.txt (simple list)")
    
    print(f"\n📊 POOL SUMMARY:")
    print(f"   Total available words: {len(all_words_list)}")
    for pattern, words in word_pool.items():
        count = len(words)
        percentage = (count / len(all_words_list)) * 100
        print(f"   {pattern}: {count:3d} words ({percentage:4.1f}%)")
    
    print(f"\n💡 NEXT STEPS:")
    print("   1. Use phi_word_pool.json as your master pool")
    print("   2. Remove words from pool as you assign meanings")
    print("   3. Track assignments in the assignment_log")

if __name__ == "__main__":
    main() 