import json
import os
from pathlib import Path

# Read the core vocabulary list
core_vocab_path = Path('/Users/daniel/phi/vocabulary/PHI_CORE_VOCABULARY_ALIGNED.md')
with open(core_vocab_path, 'r') as f:
    content = f.read()

# Extract all numbered items from the core vocabulary
core_words = set()
import re

# Match lines like "123. word" or "123. word (description)"
pattern = r'^\d+\.\s+([^\(\n]+?)(?:\s*\(|$)'
for line in content.split('\n'):
    match = re.match(pattern, line.strip())
    if match:
        word = match.group(1).strip().lower()
        # Handle entries with slashes (alternatives)
        if '/' in word:
            for w in word.split('/'):
                core_words.add(w.strip())
        else:
            core_words.add(word)

print(f"Total core words extracted: {len(core_words)}")

# Read all JSON files in vocabulary directory
vocab_dir = Path('/Users/daniel/phi/vocabulary')
json_files = list(vocab_dir.glob('*.json'))

# Dictionary to store existing vocabulary
existing_vocab = {}
for json_file in json_files:
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
            # Handle array format
            if isinstance(data, list) and len(data) > 0:
                entry = data[0]  # Take first entry if multiple
                if isinstance(entry, dict) and 'gloss' in entry:
                    gloss = entry['gloss'].lower()
                    existing_vocab[json_file.stem] = {
                        'gloss': gloss,
                        'word': entry.get('word', ''),
                        'data': entry
                    }
            # Handle single dict format
            elif isinstance(data, dict) and 'gloss' in data:
                gloss = data['gloss'].lower()
                existing_vocab[json_file.stem] = {
                    'gloss': gloss,
                    'word': data.get('word', ''),
                    'data': data
                }
    except Exception as e:
        print(f"Error reading {json_file}: {e}")

print(f"\nTotal existing vocabulary files: {len(existing_vocab)}")

# Compare existing vocabulary with core list
matched = []
unmatched = []

for filename, vocab_data in existing_vocab.items():
    gloss = vocab_data['gloss']
    # Check if gloss matches any core word
    if gloss in core_words:
        matched.append((filename, gloss, vocab_data['word']))
    else:
        # Check if it's a partial match (e.g., "speak" matches "speaker")
        partial_match = False
        for core_word in core_words:
            if core_word in gloss or gloss in core_word:
                matched.append((filename, gloss, vocab_data['word'], f"partial: {core_word}"))
                partial_match = True
                break
        if not partial_match:
            unmatched.append((filename, gloss, vocab_data['word']))

# Find missing core words
existing_glosses = {v['gloss'] for v in existing_vocab.values()}
missing_core_words = sorted(core_words - existing_glosses)

# Generate report
print("\n" + "="*80)
print("VOCABULARY COMPARISON REPORT")
print("="*80)

print(f"\n1. MATCHED WORDS ({len(matched)}):")
print("-" * 40)
for item in sorted(matched):
    if len(item) == 3:
        print(f"{item[0]}.json: '{item[1]}' -> {item[2]}")
    else:
        print(f"{item[0]}.json: '{item[1]}' -> {item[2]} ({item[3]})")

print(f"\n2. UNMATCHED EXISTING WORDS ({len(unmatched)}):")
print("-" * 40)
for item in sorted(unmatched):
    print(f"{item[0]}.json: '{item[1]}' -> {item[2]}")

print(f"\n3. MISSING CORE WORDS ({len(missing_core_words)}):")
print("-" * 40)
# Group by first letter for easier reading
by_letter = {}
for word in missing_core_words:
    first_letter = word[0] if word else '?'
    if first_letter not in by_letter:
        by_letter[first_letter] = []
    by_letter[first_letter].append(word)

for letter in sorted(by_letter.keys()):
    print(f"\n{letter.upper()}:")
    for word in sorted(by_letter[letter]):
        print(f"  - {word}")

# Summary
print("\n" + "="*80)
print("SUMMARY:")
print(f"- Core vocabulary words: {len(core_words)}")
print(f"- Existing JSON files: {len(existing_vocab)}")
print(f"- Matched words: {len(matched)}")
print(f"- Unmatched existing words: {len(unmatched)}")
print(f"- Missing core words: {len(missing_core_words)}")
print(f"- Coverage: {len(matched)/len(core_words)*100:.1f}% of core vocabulary")