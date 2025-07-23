#!/usr/bin/env python3
"""Remove a word from the available words list after it's been used."""

import sys

def remove_word(word_to_remove, filename="available_two_syllable_words.txt"):
    """Remove a specific word from the available words file."""
    
    # Read all lines
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    # Find and remove the word
    removed = False
    new_lines = []
    for line in lines:
        if line.strip() == word_to_remove:
            removed = True
            continue  # Skip this line
        new_lines.append(line)
    
    if not removed:
        print(f"Warning: '{word_to_remove}' not found in {filename}")
        return False
    
    # Update the count in the header
    if "# Total:" in new_lines[1]:
        # Extract current count
        parts = new_lines[1].split("Total: ")
        if len(parts) > 1:
            count_part = parts[1].split(" words")[0]
            current_count = int(count_part.replace(",", ""))
            new_count = current_count - 1
            new_lines[1] = f"# Total: {new_count:,} words\n"
    
    # Write back
    with open(filename, 'w') as f:
        f.writelines(new_lines)
    
    print(f"Removed '{word_to_remove}' from {filename}")
    print(f"New total: {new_count:,} words")
    return True

def main():
    if len(sys.argv) != 2:
        print("Usage: python update_available_words.py <word>")
        sys.exit(1)
    
    word = sys.argv[1]
    remove_word(word)

if __name__ == "__main__":
    main()