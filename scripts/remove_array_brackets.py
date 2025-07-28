#!/usr/bin/env python3
"""Remove unnecessary array brackets from JSON files."""

import json
from pathlib import Path

lexicon_dir = Path(__file__).parent.parent / "lexicon"
json_files = list(lexicon_dir.glob("*.json"))

print(f"Found {len(json_files)} JSON files to process")

for file_path in json_files:
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    # If it's an array with one element, extract that element
    if isinstance(data, list) and len(data) == 1:
        data = data[0]
        
        # Write back as a single object
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Updated: {file_path.name}")
    else:
        print(f"Skipped: {file_path.name} (not a single-element array)")

print("\nDone!")