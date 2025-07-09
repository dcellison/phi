#!/usr/bin/env python3
"""
Manage the phi word pool - remove words as they get assigned meanings.
"""

import json
from datetime import datetime
import sys

def load_pool():
    """Load the current word pool."""
    try:
        with open('phi_word_pool.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ phi_word_pool.json not found. Run create_word_pool.py first.")
        return None

def save_pool(pool_data):
    """Save the updated word pool."""
    with open('phi_word_pool.json', 'w', encoding='utf-8') as f:
        json.dump(pool_data, f, indent=2, ensure_ascii=False)

def remove_word(word, meaning, category):
    """Remove a word from the pool and log the assignment."""
    pool_data = load_pool()
    if not pool_data:
        return False
    
    # Find and remove the word
    word_found = False
    for pattern, words in pool_data['available_words'].items():
        if word in words:
            words.remove(word)
            word_found = True
            
            # Log the assignment
            assignment = {
                'word': word,
                'pattern': pattern,
                'meaning': meaning,
                'category': category,
                'assigned_date': datetime.now().isoformat()
            }
            pool_data['assignment_log'].append(assignment)
            
            # Update metadata
            pool_data['metadata']['total_words'] -= 1
            pool_data['metadata']['pattern_counts'][pattern] -= 1
            
            print(f"✅ Removed '{word}' ({pattern}) → '{meaning}' ({category})")
            break
    
    if not word_found:
        print(f"❌ Word '{word}' not found in pool")
        return False
    
    save_pool(pool_data)
    return True

def add_word_back(word):
    """Add a word back to the pool (if assignment was cancelled)."""
    pool_data = load_pool()
    if not pool_data:
        return False
    
    # Check if word was previously assigned
    assignment_found = None
    for i, assignment in enumerate(pool_data['assignment_log']):
        if assignment['word'] == word:
            assignment_found = i
            break
    
    if assignment_found is None:
        print(f"❌ No assignment record found for '{word}'")
        return False
    
    # Get the pattern and add back to pool
    assignment = pool_data['assignment_log'][assignment_found]
    pattern = assignment['pattern']
    
    pool_data['available_words'][pattern].append(word)
    pool_data['available_words'][pattern].sort()
    
    # Remove from assignment log
    del pool_data['assignment_log'][assignment_found]
    
    # Update metadata
    pool_data['metadata']['total_words'] += 1
    pool_data['metadata']['pattern_counts'][pattern] += 1
    
    print(f"✅ Added '{word}' back to {pattern} pool")
    
    save_pool(pool_data)
    return True

def show_pool_status():
    """Display current pool status."""
    pool_data = load_pool()
    if not pool_data:
        return
    
    print("📊 PHI WORD POOL STATUS")
    print("=" * 40)
    
    total_available = pool_data['metadata']['total_words']
    total_assigned = len(pool_data['assignment_log'])
    
    print(f"Available words: {total_available}")
    print(f"Assigned words:  {total_assigned}")
    print(f"Total created:   {total_available + total_assigned}")
    
    print("\nPattern distribution:")
    for pattern, count in pool_data['metadata']['pattern_counts'].items():
        percentage = (count / total_available * 100) if total_available > 0 else 0
        print(f"  {pattern}: {count:3d} words ({percentage:4.1f}%)")
    
    if total_assigned > 0:
        print(f"\nRecent assignments:")
        recent = pool_data['assignment_log'][-5:]  # Last 5
        for assignment in recent:
            date = assignment['assigned_date'][:10]  # Just date part
            print(f"  {assignment['word']} → {assignment['meaning']} ({date})")

def get_available_words(pattern=None, limit=10):
    """Get available words from the pool."""
    pool_data = load_pool()
    if not pool_data:
        return []
    
    if pattern:
        words = pool_data['available_words'].get(pattern, [])
        print(f"Available {pattern} words ({len(words)} total):")
        for word in words[:limit]:
            print(f"  {word}")
        if len(words) > limit:
            print(f"  ... and {len(words) - limit} more")
    else:
        print("Available words by pattern:")
        for pat, words in pool_data['available_words'].items():
            print(f"  {pat}: {len(words)} words")

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python manage_word_pool.py status")
        print("  python manage_word_pool.py remove <word> <meaning> <category>")
        print("  python manage_word_pool.py add_back <word>")
        print("  python manage_word_pool.py list [pattern] [limit]")
        return
    
    command = sys.argv[1]
    
    if command == "status":
        show_pool_status()
    elif command == "remove" and len(sys.argv) >= 5:
        word = sys.argv[2]
        meaning = sys.argv[3]
        category = sys.argv[4]
        remove_word(word, meaning, category)
    elif command == "add_back" and len(sys.argv) >= 3:
        word = sys.argv[2]
        add_word_back(word)
    elif command == "list":
        pattern = sys.argv[2] if len(sys.argv) > 2 else None
        limit = int(sys.argv[3]) if len(sys.argv) > 3 else 10
        get_available_words(pattern, limit)
    else:
        print("❌ Invalid command or missing arguments")

if __name__ == "__main__":
    main() 