#!/usr/bin/env python3
"""
Phi Lexicon Word Removal Utility

Removes a word from both the phi_words.json file and the corresponding 
Markdown file in the source/pos/ directory.

Usage: python3 remove_word.py <word1> [word2] [word3] ...
       python3 remove_word.py --help
"""

import json
import sys
import re
import os
from pathlib import Path

def show_help():
    """Display help information."""
    print(__doc__)
    print("Examples:")
    print("  python3 remove_word.py pathea")
    print("  python3 remove_word.py pathea ronshea thashui")
    print("  python3 remove_word.py --help")

def load_json_data(json_path):
    """Load the phi_words.json file."""
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {json_path} not found")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in {json_path}: {e}")
        sys.exit(1)

def save_json_data(json_path, data):
    """Save the updated JSON data."""
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def remove_from_markdown(md_path, word, translation):
    """Remove a word entry from the markdown file."""
    if not os.path.exists(md_path):
        print(f"Warning: {md_path} not found")
        return False
    
    # Read file preserving original line endings
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Store original line ending style
    if '\r\n' in content:
        line_ending = '\r\n'
    elif '\r' in content:
        line_ending = '\r'
    else:
        line_ending = '\n'
    
    # Split into lines
    lines = content.splitlines()
    
    # Pattern to match the word entry in the table
    # More flexible pattern that handles extra whitespace
    escaped_word = re.escape(word)
    escaped_translation = re.escape(translation)
    pattern = rf'^\|\s*{escaped_word}\s*\|\s*{escaped_translation}\s*\|'
    
    new_lines = []
    removed = False
    
    for line in lines:
        if re.match(pattern, line):
            removed = True
            print(f"  Removed from {md_path}: {line.strip()}")
        else:
            new_lines.append(line)
    
    if removed:
        # Preserve original line endings and file structure
        new_content = line_ending.join(new_lines)
        if content.endswith(('\n', '\r\n', '\r')):
            new_content += line_ending
            
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    else:
        print(f"  Warning: Entry for '{word}' ({translation}) not found in {md_path}")
        return False

def remove_words(words_to_remove):
    """Remove multiple words from the lexicon."""
    # Get the script directory and construct paths
    script_dir = Path(__file__).parent
    json_path = script_dir / 'phi_words.json'
    pos_dir = script_dir.parent / 'source' / 'pos'
    
    # Load JSON data
    data = load_json_data(json_path)
    
    removed_words = []
    not_found_words = []
    
    for word in words_to_remove:
        if word in data:
            word_info = data[word]
            pos = word_info.get('pos', 'unknown')
            source_file = word_info.get('source_file', f'{pos}.md')
            translation = word_info.get('translation', 'unknown')
            
            print(f"\nRemoving '{word}' ({translation}) from {pos}:")
            
            # Remove from JSON
            del data[word]
            print(f"  Removed from phi_words.json")
            
            # Remove from markdown file
            md_path = pos_dir / source_file
            remove_from_markdown(md_path, word, translation)
            
            removed_words.append(word)
        else:
            not_found_words.append(word)
            print(f"\nWord '{word}' not found in lexicon")
    
    # Save updated JSON if any words were removed
    if removed_words:
        save_json_data(json_path, data)
        print(f"\nSuccessfully removed {len(removed_words)} word(s) from lexicon:")
        for word in removed_words:
            print(f"  - {word}")
    
    if not_found_words:
        print(f"\nWords not found: {', '.join(not_found_words)}")
    
    # Final counts
    print(f"\nTotal words remaining in lexicon: {len(data)}")

def main():
    # Handle help flag
    if len(sys.argv) == 2 and sys.argv[1] in ['--help', '-h', 'help']:
        show_help()
        sys.exit(0)
    
    if len(sys.argv) < 2:
        print("Usage: python3 remove_word.py <word1> [word2] [word3] ...")
        print("       python3 remove_word.py --help")
        print("Example: python3 remove_word.py pathea ronshea")
        sys.exit(1)
    
    words_to_remove = sys.argv[1:]
    
    # Confirm removal
    print(f"About to remove {len(words_to_remove)} word(s): {', '.join(words_to_remove)}")
    confirm = input("Continue? (y/N): ").strip().lower()
    
    if confirm != 'y':
        print("Removal cancelled")
        sys.exit(0)
    
    remove_words(words_to_remove)

if __name__ == "__main__":
    main() 