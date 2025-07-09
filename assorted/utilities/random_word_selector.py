#!/usr/bin/env python3
"""
Randomly select words from the phi word pool by pattern.
Avoids alphabetical bias for true phonological diversity.
"""

import json
import random
import sys

def load_pool():
    """Load the current word pool."""
    try:
        with open('phi_word_pool.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ phi_word_pool.json not found. Run create_word_pool.py first.")
        return None

def random_select(pattern, count):
    """Randomly select words from a specific pattern."""
    pool_data = load_pool()
    if not pool_data:
        return []
    
    available_words = pool_data['available_words'].get(pattern, [])
    
    if len(available_words) < count:
        print(f"⚠️  Only {len(available_words)} {pattern} words available, requested {count}")
        count = len(available_words)
    
    selected = random.sample(available_words, count)
    return sorted(selected)  # Sort for consistent display

def balanced_selection(total_words):
    """Select words evenly across all four patterns."""
    words_per_pattern = total_words // 4
    remainder = total_words % 4
    
    selections = {}
    
    for i, pattern in enumerate(['CVFP', 'CPFP', 'FVFP', 'FPFP']):
        # Distribute remainder across first few patterns
        count = words_per_pattern + (1 if i < remainder else 0)
        selections[pattern] = random_select(pattern, count)
    
    return selections

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python random_word_selector.py <pattern> <count>")
        print("  python random_word_selector.py balanced <total_count>")
        print("  python random_word_selector.py mixed <count_per_pattern>")
        print()
        print("Examples:")
        print("  python random_word_selector.py CVFP 5")
        print("  python random_word_selector.py balanced 12")
        print("  python random_word_selector.py mixed 3")
        return
    
    command = sys.argv[1]
    
    if command in ['CVFP', 'CPFP', 'FVFP', 'FPFP']:
        if len(sys.argv) < 3:
            print("❌ Please specify count")
            return
        
        pattern = command
        count = int(sys.argv[2])
        selected = random_select(pattern, count)
        
        print(f"🎲 Random {pattern} words ({count} selected):")
        for word in selected:
            print(f"  {word}")
    
    elif command == "balanced":
        if len(sys.argv) < 3:
            print("❌ Please specify total count")
            return
        
        total = int(sys.argv[2])
        selections = balanced_selection(total)
        
        print(f"🎲 Balanced selection ({total} words total):")
        for pattern, words in selections.items():
            print(f"  {pattern} ({len(words)}): {', '.join(words)}")
    
    elif command == "mixed":
        if len(sys.argv) < 3:
            print("❌ Please specify count per pattern")
            return
        
        count_each = int(sys.argv[2])
        
        print(f"🎲 Mixed selection ({count_each} from each pattern):")
        for pattern in ['CVFP', 'CPFP', 'FVFP', 'FPFP']:
            selected = random_select(pattern, count_each)
            print(f"  {pattern}: {', '.join(selected)}")
    
    else:
        print(f"❌ Unknown command: {command}")

if __name__ == "__main__":
    main() 