#!/usr/bin/env python3
"""
Reformat JSON files to compact single-line style for arrays.
"""

import json
from pathlib import Path
import sys

def reformat_json(file_path):
    """Reformat a JSON file to use compact formatting."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Write back with compact formatting
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"✓ Reformatted: {file_path.name}")
        return True
    except Exception as e:
        print(f"✗ Error reformatting {file_path.name}: {e}")
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python reformat_json.py <directory>")
        sys.exit(1)
    
    directory = Path(sys.argv[1])
    if not directory.is_dir():
        print(f"Error: {directory} is not a directory")
        sys.exit(1)
    
    json_files = list(directory.glob("*.json"))
    if not json_files:
        print(f"No JSON files found in {directory}")
        return
    
    print(f"Reformatting {len(json_files)} JSON files in {directory}...")
    
    success_count = 0
    for file_path in json_files:
        if reformat_json(file_path):
            success_count += 1
    
    print(f"\nReformatted {success_count}/{len(json_files)} files successfully")

if __name__ == "__main__":
    main()