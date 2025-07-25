import json
import os
from pathlib import Path
import re

# Read the core vocabulary list
core_vocab_path = Path('/Users/daniel/phi/vocabulary/PHI_CORE_VOCABULARY_ALIGNED.md')
with open(core_vocab_path, 'r') as f:
    content = f.read()

# Extract all numbered items from the core vocabulary
core_words = set()

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

# Separate exact matches from partial matches
exact_matches = []
partial_matches = []
unmatched = []

for filename, vocab_data in existing_vocab.items():
    gloss = vocab_data['gloss']
    # Check if gloss exactly matches any core word
    if gloss in core_words:
        exact_matches.append((filename, gloss, vocab_data['word']))
    else:
        # Check if it's a partial match
        partial_match = False
        for core_word in core_words:
            if core_word in gloss or gloss in core_word:
                partial_matches.append((filename, gloss, vocab_data['word'], core_word))
                partial_match = True
                break
        if not partial_match:
            unmatched.append((filename, gloss, vocab_data['word']))

# Find missing core words
existing_glosses = {v['gloss'] for v in existing_vocab.values()}
missing_core_words = sorted(core_words - existing_glosses)

# Generate detailed report
print("# Phi Vocabulary Comparison Report\n")
print(f"## Summary")
print(f"- Core vocabulary words: {len(core_words)}")
print(f"- Existing JSON files: {len(existing_vocab)}")
print(f"- Exact matches: {len(exact_matches)}")
print(f"- Partial matches: {len(partial_matches)}")
print(f"- Unmatched existing words: {len(unmatched)}")
print(f"- Missing core words: {len(missing_core_words)}")
print(f"- Exact match coverage: {len(exact_matches)/len(core_words)*100:.1f}% of core vocabulary\n")

print(f"## Exact Matches ({len(exact_matches)})\n")
print("These existing words exactly match core vocabulary entries:\n")
print("| File | Gloss | Phi Word |")
print("|------|-------|----------|")
for item in sorted(exact_matches):
    print(f"| {item[0]}.json | {item[1]} | {item[2]} |")

print(f"\n## Partial Matches ({len(partial_matches)})\n")
print("These existing words partially match core vocabulary entries:\n")
print("| File | Gloss | Phi Word | Matches Core Word |")
print("|------|-------|----------|-------------------|")
for item in sorted(partial_matches):
    print(f"| {item[0]}.json | {item[1]} | {item[2]} | {item[3]} |")

print(f"\n## Unmatched Existing Words ({len(unmatched)})\n")
print("These existing words don't match any core vocabulary entry:\n")
print("| File | Gloss | Phi Word |")
print("|------|-------|----------|")
for item in sorted(unmatched):
    print(f"| {item[0]}.json | {item[1]} | {item[2]} |")

print(f"\n## Missing Core Words ({len(missing_core_words)})\n")
print("These core vocabulary words have no corresponding JSON file:\n")

# Group by first letter for easier reading
by_letter = {}
for word in missing_core_words:
    first_letter = word[0].upper() if word else '?'
    if first_letter not in by_letter:
        by_letter[first_letter] = []
    by_letter[first_letter].append(word)

for letter in sorted(by_letter.keys()):
    print(f"\n### {letter}")
    words_in_letter = sorted(by_letter[letter])
    # Format in columns for readability
    for i in range(0, len(words_in_letter), 4):
        row = words_in_letter[i:i+4]
        print("- " + ", ".join(f"`{w}`" for w in row))

# Action items
print("\n## Recommendations\n")
print("1. **Exact Matches**: These words can be kept as-is since they align with the core vocabulary.")
print("2. **Partial Matches**: Review these to determine if they should be:")
print("   - Renamed to match the core word exactly")
print("   - Kept as variations/derivatives of the core word")
print("   - Removed if they don't serve a unique purpose")
print("3. **Unmatched Words**: Consider whether these should be:")
print("   - Removed to focus on the core vocabulary")
print("   - Kept as extensions beyond the core")
print("4. **Missing Core Words**: These need to be created to complete the core vocabulary.")