#!/usr/bin/env python3

import re
import os
from collections import defaultdict

def is_valid_phi_word(word):
    """Check if a word follows phi phonotactic patterns"""
    if not word or len(word) < 2:
        return False
    
    # Filter out obvious non-phi words
    if any(char in word for char in [' ', '.', '(', ')', '[', ']', '/', '\\', ',']):
        return False
    
    if word.isupper():  # All caps abbreviations
        return False
    
    # Filter out English words and examples
    english_words = {
        'english', 'form', 'function', 'example', 'translation', 'object', 
        'subject', 'both', 'either', 'neither', 'tree', 'flower', 'ball', 
        'cup', 'bag', 'basket', 'bread', 'butter', 'not', 'only', 'but', 
        'also', 'and', 'or', 'nor', 'the', 'a', 'an', 'is', 'are', 'was',
        'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does',
        'did', 'will', 'would', 'could', 'should', 'may', 'might', 'can',
        'must', 'shall', 'formation'
    }
    
    if word.lower() in english_words:
        return False
    
    # Check for basic phi phonotactics (simplified)
    consonants = set('hlmnprstw')
    fricatives = {'ph', 'wh', 'th', 'sh'}
    vowels = set('iueoa')
    
    # Must contain only valid phi characters
    valid_chars = consonants | vowels | {'h'}  # h can be standalone or in fricatives
    if not all(c in valid_chars for c in word):
        return False
    
    # Must contain at least one vowel
    if not any(c in vowels for c in word):
        return False
    
    # Must not be too long (phi words are typically 2-8 characters)
    if len(word) > 8:
        return False
    
    return True

def extract_pos_data():
    """Extract all valid phi words from POS files with their parts of speech"""
    pos_data = {}
    pos_files = {
        'pos/nouns.md': 'noun',
        'pos/verbs.md': 'verb', 
        'pos/adjectives.md': 'adjective',
        'pos/adverbs.md': 'adverb',
        'pos/particles.md': 'particle',
        'pos/determiners.md': 'determiner',
        'pos/pronouns.md': 'pronoun',
        'pos/prepositions.md': 'preposition',
        'pos/conjunctions.md': 'conjunction',
        'pos/interjections.md': 'interjection',
        'pos/classifiers.md': 'classifier',
        'pos/numbers.md': 'number'
    }
    
    for pos_file, pos_type in pos_files.items():
        if os.path.exists(pos_file):
            with open(pos_file, 'r') as f:
                content = f.read()
            
            lines = content.split('\n')
            in_phi_table = False
            
            for line in lines:
                # Check if we're entering a phi word table
                if '| phi word | english translation |' in line:
                    in_phi_table = True
                    continue
                
                # Check if we're leaving the table (empty line or new section)
                if in_phi_table and (not line.strip() or line.startswith('#') or (line.startswith('|') and '---' in line)):
                    if not line.strip() or line.startswith('#'):
                        in_phi_table = False
                    continue
                
                # Extract entries within phi word tables
                if in_phi_table and line.startswith('| '):
                    parts = [p.strip() for p in line.split('|')]
                    if len(parts) >= 3:
                        phi_word = parts[1].strip()
                        english_meaning = parts[2].strip()
                        
                        if phi_word and english_meaning:
                            pos_data[phi_word] = {
                                'pos': pos_type,
                                'meaning': english_meaning
                            }
    
    return pos_data

def generate_phi_to_english_section(pos_data):
    """Generate the phi → english lookup section"""
    lines = []
    lines.append("## 1. phi → english lookup (alphabetical by phi)")
    lines.append("")
    
    # Group by first letter
    by_letter = defaultdict(list)
    for word in sorted(pos_data.keys()):
        first_letter = word[0]
        by_letter[first_letter].append(word)
    
    for letter in sorted(by_letter.keys()):
        lines.append(f"### {letter}")
        lines.append("")
        lines.append("| phi word | part of speech | english meaning |")
        lines.append("| -------- | -------------- | --------------- |")
        
        for word in by_letter[letter]:
            data = pos_data[word]
            lines.append(f"| {word} | {data['pos']} | {data['meaning']} |")
        
        lines.append("")
    
    return lines

def generate_english_to_phi_section(pos_data):
    """Generate the english → phi lookup section"""
    lines = []
    lines.append("## 2. english → phi lookup (alphabetical by english)")
    lines.append("")
    
    # Create english → phi mapping
    english_to_phi = {}
    for phi_word, data in pos_data.items():
        english_meaning = data['meaning']
        pos_type = data['pos']
        
        # Handle multiple meanings separated by /
        meanings = [m.strip() for m in english_meaning.split('/')]
        for meaning in meanings:
            if meaning not in english_to_phi:
                english_to_phi[meaning] = []
            english_to_phi[meaning].append((phi_word, pos_type))
    
    # Group by first letter
    by_letter = defaultdict(list)
    for meaning in sorted(english_to_phi.keys()):
        first_letter = meaning[0].lower()
        by_letter[first_letter].append(meaning)
    
    for letter in sorted(by_letter.keys()):
        lines.append(f"### {letter}")
        lines.append("")
        lines.append("| english | phi word | part of speech |")
        lines.append("| ------- | -------- | -------------- |")
        
        for meaning in by_letter[letter]:
            for phi_word, pos_type in english_to_phi[meaning]:
                lines.append(f"| {meaning} | {phi_word} | {pos_type} |")
        
        lines.append("")
    
    return lines

def generate_pattern_section():
    """Generate the pattern identification section"""
    return [
        "## 3. pattern identification quick guide",
        "",
        "### phonotactic patterns for instant word type recognition",
        "",
        "**pattern recognition cheat sheet**",
        "",
        "| pattern | part of speech | example | meaning |",
        "| ------- | -------------- | ------- | ------- |",
        "| [F][V][C][V] | verb | `phola` | walk |",
        "| [C][V][F][V] | adjective | `hashe` | green |",
        "| [C/F][V/P][F][P] | noun | `siwhea` | house |",
        "| [C][V][C][V][C][V] | adverb | `napine` | quickly |",
        "| [F][P] | preposition | `wheo` | at |",
        "| [C][V] | particle | `li` | past |",
        "| [F][P][C][V] | determiner | `phiato` | this |",
        "| [C][V][C][V] | conjunction | `nene` | and |",
        "",
        "**fricative digraphs**: ph, wh, th, sh",
        "**consonants**: h, l, m, n, p, r, s, t, w",
        "**vowels**: i, u, e, o, a",
        "**vowel pairs**: any two different vowels (ia, uo, ei, etc.)",
        "",
        "### usage tips",
        "",
        "1. **start with patterns**: identify word type by sound structure",
        "2. **cross-reference**: use both directions for complete understanding",
        "3. **semantic grouping**: related words often appear together",
        "4. **systematic learning**: master patterns before memorizing individual words",
        "5. **practice recognition**: regular pattern drills improve fluency",
        "",
    ]

def main():
    print("Extracting data from POS files...")
    pos_data = extract_pos_data()
    
    print(f"Found {len(pos_data)} valid phi words")
    
    # Generate the complete lookup file
    lines = []
    
    # Header
    lines.extend([
        "---",
        "tags:",
        "  - reference",
        "  - lookup", 
        "  - translation",
        "  - quick-reference",
        "---",
        "# phi quick lookup tools",
        "",
        "> bidirectional lookup tables for instant translation between phi and english.",
        f"> over {len(pos_data)} words organized alphabetically for fast reference and learning support.",
        "",
        "## usage guide",
        "",
        "**phi → english lookup**: find english meanings for phi words (section 1)",
        "**english → phi lookup**: find phi words for english concepts (section 2)",
        "**pattern identification**: use phonotactic patterns to identify word types instantly",
        "**cross-reference**: words appear in both directions for complete coverage",
        "",
        "---",
        ""
    ])
    
    # Phi to English section
    lines.extend(generate_phi_to_english_section(pos_data))
    
    # English to Phi section  
    lines.extend(generate_english_to_phi_section(pos_data))
    
    # Pattern section
    lines.extend(generate_pattern_section())
    
    # Footer
    lines.extend([
        f"**total searchable vocabulary**: {len(pos_data)}+ words with complete bidirectional coverage",
        "",
        "---",
        "*these lookup tools provide instant access to phi's systematic vocabulary, supporting both learning and practical communication needs across all proficiency levels.*"
    ])
    
    # Write the file
    with open('phi-lookup-tools.md', 'w') as f:
        f.write('\n'.join(lines))
    
    print(f"Successfully rebuilt phi-lookup-tools.md with {len(pos_data)} words")

if __name__ == "__main__":
    main() 