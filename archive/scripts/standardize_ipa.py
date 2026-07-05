#!/usr/bin/env python3
"""
Standardize IPA notation in vocabulary JSON files.

Applies:
1. Precise vowel diacritics: a→ä, e→e̞, o→o̞
2. Dental consonant marks: t→t̪, n→n̪
3. Penultimate stress marking
"""

import json
import re
from pathlib import Path
import sys


def apply_diacritics(ipa: str) -> str:
    """Apply precise IPA diacritics for vowels and dental consonants."""
    # Remove existing stress marks first
    ipa = ipa.replace('ˈ', '').replace('ˌ', '')

    # Apply vowel diacritics (only within IPA, not affecting dots)
    # Order matters: do replacements carefully to avoid double-replacing
    ipa = ipa.replace('a', 'ä')
    ipa = ipa.replace('e', 'e̞')
    ipa = ipa.replace('o', 'o̞')

    # Apply dental marks for t and n
    # Be careful not to affect θ (th sound)
    # t̪ and n̪ - dental diacritic
    result = []
    i = 0
    while i < len(ipa):
        char = ipa[i]
        if char == 't' and (i + 1 >= len(ipa) or ipa[i + 1] != '̪'):
            result.append('t̪')
        elif char == 'n' and (i + 1 >= len(ipa) or ipa[i + 1] != '̪'):
            result.append('n̪')
        else:
            result.append(char)
        i += 1

    return ''.join(result)


def add_stress_mark(ipa: str, syllable_count: int) -> str:
    """Add penultimate stress mark to IPA transcription."""
    if syllable_count <= 0:
        return ipa

    # Single syllable: stress on only syllable
    if syllable_count == 1:
        # Add stress at start, after the opening /
        if ipa.startswith('/'):
            return '/ˈ' + ipa[1:]
        return 'ˈ' + ipa

    # Multi-syllable: stress on penultimate (second-to-last)
    # Split by dots to find syllable boundaries
    # IPA format: /syl.la.ble/

    # Remove slashes for processing
    inner = ipa.strip('/')
    parts = inner.split('.')

    if len(parts) < 2:
        # No dots found, can't determine syllables
        return ipa

    # Insert stress mark before penultimate syllable
    penultimate_idx = len(parts) - 2
    parts[penultimate_idx] = 'ˈ' + parts[penultimate_idx]

    return '/' + '.'.join(parts) + '/'


def process_ipa(ipa: str, syllables: list) -> str:
    """Process IPA: apply diacritics and stress marking."""
    # Apply diacritics first
    ipa = apply_diacritics(ipa)

    # Add stress mark based on syllable count
    syllable_count = len(syllables) if syllables else 0
    ipa = add_stress_mark(ipa, syllable_count)

    return ipa


def process_file(file_path: Path, dry_run: bool = False) -> tuple[bool, str]:
    """Process a single JSON file. Returns (success, message)."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if 'ipa' not in data:
            return True, f"Skipped (no IPA field): {file_path.name}"

        old_ipa = data['ipa']
        syllables = data.get('syllables', [])

        new_ipa = process_ipa(old_ipa, syllables)

        if old_ipa == new_ipa:
            return True, f"Unchanged: {file_path.name}"

        if dry_run:
            return True, f"Would change: {file_path.name}: {old_ipa} → {new_ipa}"

        data['ipa'] = new_ipa

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write('\n')

        return True, f"Updated: {file_path.name}: {old_ipa} → {new_ipa}"

    except Exception as e:
        return False, f"Error processing {file_path.name}: {e}"


def process_directory(directory: Path, dry_run: bool = False) -> tuple[int, int]:
    """Process all JSON files in a directory. Returns (success_count, total_count)."""
    json_files = list(directory.glob("*.json"))
    if not json_files:
        print(f"  No JSON files in {directory}")
        return 0, 0

    success_count = 0
    updated_count = 0

    for file_path in sorted(json_files):
        success, message = process_file(file_path, dry_run)
        if success:
            success_count += 1
            if "Updated" in message or "Would change" in message:
                updated_count += 1
                print(f"  {message}")
        else:
            print(f"  {message}")

    return success_count, len(json_files)


def main():
    dry_run = '--dry-run' in sys.argv

    if dry_run:
        print("DRY RUN - no files will be modified\n")

    vocab_root = Path(__file__).parent.parent / "vocabulary"

    if not vocab_root.is_dir():
        print(f"Error: vocabulary directory not found at {vocab_root}")
        sys.exit(1)

    directories = [
        vocab_root / "content",
        vocab_root / "function" / "pronoun",
        vocab_root / "function" / "preposition",
        vocab_root / "function" / "particle",
        vocab_root / "function" / "interrogative",
        vocab_root / "function" / "conjunction",
        vocab_root / "function" / "classifier",
        vocab_root / "function" / "numeral",
        vocab_root / "interjection",
    ]

    total_success = 0
    total_files = 0

    for directory in directories:
        if directory.is_dir():
            print(f"\nProcessing {directory.relative_to(vocab_root)}...")
            success, total = process_directory(directory, dry_run)
            total_success += success
            total_files += total

    print(f"\n{'Would update' if dry_run else 'Processed'} {total_success}/{total_files} files successfully")


if __name__ == "__main__":
    main()
