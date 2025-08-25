#!/usr/bin/env python3
"""
Reformat JSON files to compact single-line style with arrays on single lines.
"""

import json
from pathlib import Path
import sys

def compact_json_format(obj, indent=0):
    """Format JSON with compact arrays on single lines."""
    if isinstance(obj, dict):
        if not obj:
            return "{}"
        
        items = []
        for key, value in obj.items():
            if isinstance(value, (list, tuple)) and all(isinstance(x, (str, int, float, bool, type(None))) for x in value):
                # Simple arrays on one line
                value_str = json.dumps(value, ensure_ascii=False)
            elif isinstance(value, dict):
                # Nested dicts need proper formatting
                value_str = compact_json_format(value, indent + 2)
            else:
                value_str = json.dumps(value, ensure_ascii=False)
            items.append(f'{" " * (indent + 2)}"{key}": {value_str}')
        
        return "{\n" + ",\n".join(items) + "\n" + " " * indent + "}"
    else:
        return json.dumps(obj, ensure_ascii=False)

def reformat_json_file(file_path):
    """Reformat a JSON file to use compact formatting."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Format with compact style
        formatted = compact_json_format(data)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(formatted)
        
        print(f"✓ Reformatted: {file_path.name}")
        return True
    except Exception as e:
        print(f"✗ Error reformatting {file_path.name}: {e}")
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python reformat_json_compact.py <directory>")
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
    for file_path in sorted(json_files):
        if reformat_json_file(file_path):
            success_count += 1
    
    print(f"\nReformatted {success_count}/{len(json_files)} files successfully")

if __name__ == "__main__":
    main()