import os
import re
import random
import argparse
import sys
from collections import defaultdict

# --- Phonological Components ---
CONSONANTS = ['h', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w']
FRICATIVES = ['ph', 'wh', 'th', 'sh']
VOWELS = ['a', 'e', 'i', 'o', 'u']

def get_vowel_pairs():
    """Generates all possible unique vowel pairs."""
    return [v1 + v2 for v1 in VOWELS for v2 in VOWELS if v1 != v2]

VOWEL_PAIRS = get_vowel_pairs()
C_OR_F = CONSONANTS + FRICATIVES

# --- Core Functions ---

def is_valid_phi_noun(word):
    """Validates if a word follows the [C/F][V][F][P] pattern for Phi nouns."""
    if len(word) < 4:
        return False
    
    # Check if it matches the pattern [C/F][V][F][P]
    # Part 1: consonant or fricative
    if word.startswith(('ph', 'wh', 'th', 'sh')):
        part1_end = 2
    elif word[0] in CONSONANTS:
        part1_end = 1
    else:
        return False
    
    # Part 2: single vowel
    if part1_end >= len(word) or word[part1_end] not in VOWELS:
        return False
    part2_end = part1_end + 1
    
    # Part 3: fricative digraph
    if part2_end + 1 >= len(word):
        return False
    fricative = word[part2_end:part2_end + 2]
    if fricative not in FRICATIVES:
        return False
    part3_end = part2_end + 2
    
    # Part 4: vowel pair (remaining characters)
    if part3_end >= len(word):
        return False
    vowel_pair = word[part3_end:]
    if len(vowel_pair) != 2 or vowel_pair not in VOWEL_PAIRS:
        return False
    
    return True

def is_valid_phi_verb(word):
    """Validates if a word follows the [F][V][C][V] pattern for Phi verbs."""
    if len(word) != 4:
        return False
    
    # Part 1: fricative digraph (2 characters)
    fricative = word[0:2]
    if fricative not in FRICATIVES:
        return False
    
    # Part 2: single vowel (1 character)
    if word[2] not in VOWELS:
        return False
    
    # Part 3: consonant (1 character)
    if word[3] not in CONSONANTS:
        return False
    
    return True

def find_markdown_files(root_dir):
    """Finds all markdown files in the specified directory, walking subdirectories."""
    markdown_files = []
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.md'):
                markdown_files.append(os.path.join(root, file))
    return markdown_files

def get_existing_phi_words(root_dir, exclude_file):
    """Parses all markdown files in a directory to get a set of existing Phi words, excluding the target file."""
    existing_words = set()
    md_files = find_markdown_files(root_dir)
    for file_path in md_files:
        # Normalize paths for reliable comparison
        if os.path.abspath(file_path) == os.path.abspath(exclude_file):
            continue
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # More precise regex to capture only the first column of tables
                # This matches: | word | anything | but only captures the first word
                table_rows = re.findall(r'\|\s*([a-z]+)\s*\|\s*[^|]+\s*\|', content)
                for phi_word in table_rows:
                    clean_word = phi_word.strip()
                    # Only add if it's a valid Phi word (noun or verb) and not a header
                    if (clean_word != 'phi word' and 
                        (is_valid_phi_noun(clean_word) or is_valid_phi_verb(clean_word))):
                        existing_words.add(clean_word)
        except Exception as e:
            print(f"Warning: Could not read or parse {file_path}: {e}", file=sys.stderr)
    return existing_words

def generate_phi_noun():
    """Generates a single, phonotactically correct three-syllable Phi noun."""
    part1 = random.choice(C_OR_F)
    part2 = random.choice(VOWELS)
    part3 = random.choice(FRICATIVES)
    part4 = random.choice(VOWEL_PAIRS)
    return f"{part1}{part2}{part3}{part4}"

def generate_phi_verb():
    """Generates a single, phonotactically correct Phi verb following [F][V][C][V] pattern."""
    part1 = random.choice(FRICATIVES)  # Fricative digraph
    part2 = random.choice(VOWELS)      # Single vowel
    part3 = random.choice(CONSONANTS)  # Single consonant
    part4 = random.choice(VOWELS)      # Single vowel
    return f"{part1}{part2}{part3}{part4}"

def generate_unique_nouns_for_file(english_words, master_word_set):
    """
    Generates a unique Phi noun for each unique English word, checking against
    a master set that is updated in real-time.
    """
    new_lexicon = {}
    unique_english_words = sorted(list(set(english_words)))
    
    print(f"Generating {len(unique_english_words)} unique Phi words...", file=sys.stderr)
    print(f"Avoiding {len(master_word_set)} existing words", file=sys.stderr)

    for eng_word in unique_english_words:
        attempts = 0
        while True:
            candidate = generate_phi_noun()
            attempts += 1
            # Check against the master set that includes previously generated words
            if candidate not in master_word_set:
                new_lexicon[eng_word] = candidate
                # Add the new word to the master set to prevent future collisions
                master_word_set.add(candidate)
                print(f"Generated: {eng_word} -> {candidate} (after {attempts} attempts)", file=sys.stderr)
                break
            elif attempts > 1000:
                print(f"Error: Could not generate unique word for '{eng_word}' after 1000 attempts", file=sys.stderr)
                sys.exit(1)
    return new_lexicon

def generate_unique_verbs_for_file(english_words, master_word_set):
    """
    Generates a unique Phi verb for each unique English word, checking against
    a master set that is updated in real-time.
    """
    new_lexicon = {}
    unique_english_words = sorted(list(set(english_words)))
    
    print(f"Generating {len(unique_english_words)} unique Phi verbs...", file=sys.stderr)
    print(f"Avoiding {len(master_word_set)} existing words", file=sys.stderr)

    for eng_word in unique_english_words:
        attempts = 0
        while True:
            candidate = generate_phi_verb()
            attempts += 1
            # Check against the master set that includes previously generated words
            if candidate not in master_word_set:
                new_lexicon[eng_word] = candidate
                # Add the new word to the master set to prevent future collisions
                master_word_set.add(candidate)
                print(f"Generated: {eng_word} -> {candidate} (after {attempts} attempts)", file=sys.stderr)
                break
            elif attempts > 1000:
                print(f"Error: Could not generate unique word for '{eng_word}' after 1000 attempts", file=sys.stderr)
                sys.exit(1)
    return new_lexicon

def regenerate_file_content(file_path, lexicon):
    """Rebuilds the file content with newly generated words."""
    output_lines = []
    in_table = False
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            # Look for the specific table separator after the phi word/english translation header
            if '--------' in line and '-------' in line:
                in_table = True
                output_lines.append(line)
                continue
            
            if not in_table:
                output_lines.append(line)
                continue
            
            # Updated regex to handle English words with parentheses and special characters
            match = re.match(r'(\|\s*)([^|]*)(\s*\|\s*)([^|]+)(\s*\|)', line)
            if match:
                english_word = match.group(4).strip()
                if english_word in lexicon:
                    new_phi_word = lexicon[english_word]
                    # Format with fixed padding for alignment
                    output_lines.append(f"| {new_phi_word:<8} | {english_word:<19} |\n")
                else:
                    output_lines.append(line)
            else:
                 output_lines.append(line)
    
    return "".join(output_lines)

def main():
    parser = argparse.ArgumentParser(
        description="Regenerate a markdown file with guaranteed unique Phi words (nouns or verbs).",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('target_file', help="The path to the markdown file to regenerate.")
    parser.add_argument('--dir', default='../source/pos/noun', help="The root directory to scan for existing Phi files.")
    args = parser.parse_args()
    
    # Convert to absolute paths for reliable operation
    target_file = os.path.abspath(args.target_file)
    
    # Auto-detect if we're working with verbs or nouns based on path
    is_verb_file = '/verb/' in target_file or '/verb' in target_file
    
    if is_verb_file:
        # For verbs, only search in verb directories (verbs can't conflict with nouns due to different patterns)
        search_dir = os.path.abspath('../source/pos/verb')
        if os.path.exists(search_dir):
            master_word_set = get_existing_phi_words(search_dir, target_file)
        else:
            master_word_set = set()
    else:
        # For nouns, use the provided directory (default noun directory)
        search_dir = os.path.abspath(args.dir)
        if not os.path.exists(search_dir):
            print(f"Error: Search directory not found at {search_dir}", file=sys.stderr)
            sys.exit(1)
        master_word_set = get_existing_phi_words(search_dir, target_file)
    
    if not os.path.exists(target_file):
        print(f"Error: Target file not found at {target_file}", file=sys.stderr)
        sys.exit(1)

    # 2. Get English words from the target file
    english_words_to_translate = []
    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()
        # Updated regex to handle empty first columns and capture English words with parentheses, etc.
        table_rows = re.findall(r'\|\s*[^|]*\s*\|\s*([^|]+)\s*\|', content)
        for eng_word in table_rows:
            clean_eng_word = eng_word.strip()
            # Filter out headers, separators, and invalid entries
            if (clean_eng_word != 'english translation' and 
                not clean_eng_word.startswith('-') and 
                len(clean_eng_word) > 0 and
                clean_eng_word != '--------'):
                english_words_to_translate.append(clean_eng_word)

    # 3. Generate new unique mappings using appropriate function
    if is_verb_file:
        new_lexicon = generate_unique_verbs_for_file(english_words_to_translate, master_word_set)
    else:
        new_lexicon = generate_unique_nouns_for_file(english_words_to_translate, master_word_set)

    # 4. Regenerate and print the new file content to standard output
    new_content = regenerate_file_content(target_file, new_lexicon)
    print(new_content)

if __name__ == "__main__":
    main()
