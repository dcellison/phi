#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Rationale Auditing Tool for the Phi Language Project (v2).

This tool audits the entire lexicon to ensure that the 'rationale' field for each
word is consistent with its component syllables as defined in the conceptual roots,
correctly handling both simple and composite roots.
"""

import json
import re
from pathlib import Path
import sys

# --- Configuration ---
PROJECT_ROOT = Path(__file__).parent.parent
VOCABULARY_DIR = PROJECT_ROOT / "vocabulary"
ROOTS_FILE = PROJECT_ROOT / "conceptual-roots.md"

def parse_roots():
    """Parses the conceptual-roots.md file and returns a set of all valid roots."""
    roots = set()
    try:
        with open(ROOTS_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.match(r"\|\s*`([a-zA-Z]+)`", line)
                if match:
                    root = match.group(1).strip()
                    if root:
                        roots.add(root)
    except IOError as e:
        print(f"Fatal Error: Could not read roots file at {ROOTS_FILE}", file=sys.stderr)
        print(f"Details: {e}", file=sys.stderr)
        sys.exit(1)
    return roots

def find_root_combinations(syllables, roots):
    """
    Recursively finds all valid ways a list of syllables can be covered by roots.
    Returns a list of lists, where each inner list is a valid root combination.
    """
    if not syllables:
        return [[]]  # Base case: successful parse of all syllables

    all_combinations = []
    # Try to match roots of increasing length at the start of the syllable list
    for i in range(1, len(syllables) + 1):
        prefix = "".join(syllables[:i])
        if prefix in roots:
            # If we found a valid root, recurse on the rest of the syllables
            remaining_syllables = syllables[i:]
            sub_combinations = find_root_combinations(remaining_syllables, roots)
            
            # For each successful sub-combination, prepend our current root
            for sub_combo in sub_combinations:
                all_combinations.append([prefix] + sub_combo)
    
    return all_combinations

def main():
    """Main function to run the audit."""
    print("Starting rationale audit...")

    roots = parse_roots()
    print(f"Successfully parsed {len(roots)} conceptual roots.")

    json_files = sorted(list(VOCABULARY_DIR.glob("*.json")))
    if not json_files:
        print("Error: No .json files found in the vocabulary directory.", file=sys.stderr)
        sys.exit(1)
    
    print(f"Found {len(json_files)} JSON files to audit.")

    results = {"ok": [], "mismatch": [], "unparseable": []}

    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                entry = json.load(f)[0]

                word = entry.get("word")
                syllables = entry.get("syllables", [])
                rationale = entry.get("rationale", "").lower()

                if not word or not syllables or not rationale:
                    results["mismatch"].append(f"{word} ({file_path.name}): Missing key fields.")
                    continue

                possible_root_sets = find_root_combinations(syllables, roots)

                if not possible_root_sets:
                    results["unparseable"].append(f"{word} ({file_path.name}): Syllables cannot be formed from any combination of known roots.")
                    continue

                is_consistent = False
                for root_set in possible_root_sets:
                    if all(f"'{root}'" in rationale for root in root_set):
                        is_consistent = True
                        break
                
                if is_consistent:
                    results["ok"].append(f"{word} ({file_path.name})")
                else:
                    # Provide a helpful message showing the expected combinations
                    expected = " or ".join([f"({', '.join(rs)})" for rs in possible_root_sets])
                    results["mismatch"].append(f"{word} ({file_path.name}): Rationale does not mention expected roots. Expected: {expected}")

        except (json.JSONDecodeError, IndexError) as e:
            results["mismatch"].append(f"FILE_ERROR ({file_path.name}): Could not parse. Details: {e}")

    # Generate Report
    print("\n--- Rationale Audit Report ---")

    if results["unparseable"]:
        print(f"\n[!] UNPARSEABLE ({len(results['unparseable'])}): Words whose syllables do not match any root combination.")
        for item in sorted(results["unparseable"]):
            print(f"  - {item}")

    if results["mismatch"]:
        print(f"\n[!] MISMATCH ({len(results['mismatch'])}): Rationales needing review or correction.")
        for item in sorted(results["mismatch"]):
            print(f"  - {item}")

    print(f"\n[*] OK ({len(results['ok'])}): Rationales are consistent with their roots.")
    
    print("\n--- Summary ---")
    print(f"Total Files Audited: {len(json_files)}")
    print(f"OK: {len(results['ok'])}")
    print(f"Mismatch: {len(results['mismatch'])}")
    print(f"Unparseable: {len(results['unparseable'])}")
    print("---------------")

    if not results["mismatch"] and not results["unparseable"]:
        print("\nAudit complete. All rationales are consistent!")
    else:
        print("\nAudit complete. Action is required for the files listed above.")

if __name__ == "__main__":
    main()
