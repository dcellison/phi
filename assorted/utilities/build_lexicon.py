import os
import re
from collections import defaultdict

def find_markdown_files(root_dir):
    """Find all markdown files in the specified directory."""
    markdown_files = []
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.md'):
                markdown_files.append(os.path.join(root, file))
    return markdown_files

def parse_markdown_table(file_path):
    """Parse a markdown file and extract words from tables."""
    words = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Regex to find markdown table rows with two columns
            # | phi_word | english_translation |
            table_rows = re.findall(r'\|\s*([a-z]+)\s*\|\s*([a-z\s-]+)\s*\|', content)
            for row in table_rows:
                phi_word = row[0].strip()
                english_translation = row[1].strip()
                if phi_word and english_translation and phi_word != "phi word":
                    words.append((phi_word, english_translation, os.path.basename(file_path)))
    except Exception as e:
        print(f"Error reading or parsing {file_path}: {e}")
    return words

def build_lexicon():
    """Build a master lexicon from all noun markdown files and check for duplicates."""
    noun_dir = 'source/pos/noun'
    output_file = 'lexicon.md'
    
    md_files = find_markdown_files(noun_dir)
    all_words = []
    for file in md_files:
        all_words.extend(parse_markdown_table(file))
        
    # Sort words alphabetically by Phi word
    all_words.sort(key=lambda x: x[0])

    # Write to master lexicon file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Phi Master Lexicon\n\n")
        f.write("> A complete list of all nouns in the Phi language.\n\n")
        f.write("| Phi Word | English Translation |\n")
        f.write("| :------- | :------------------ |\n")
        for word in all_words:
            f.write(f"| {word[0]} | {word[1]} |\n")
            
    print(f"Master lexicon has been built at: {output_file}")
    print(f"Total words: {len(all_words)}")

    # Check for duplicates
    phi_word_sources = defaultdict(list)
    for phi_word, _, source_file in all_words:
        phi_word_sources[phi_word].append(source_file)
        
    duplicates = {word: files for word, files in phi_word_sources.items() if len(files) > 1}
    
    if duplicates:
        print("\n--- DUPLICATE CHECK ---")
        print("Warning: Duplicate Phi words found!")
        for word, files in duplicates.items():
            file_list = ", ".join(sorted(list(set(files))))
            print(f"- Word: '{word}' found in files: {file_list}")
        print("-----------------------")
    else:
        print("\n--- DUPLICATE CHECK ---")
        print("Success: No duplicate Phi words found.")
        print("-----------------------")

if __name__ == "__main__":
    build_lexicon() 