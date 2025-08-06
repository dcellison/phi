#!/usr/bin/env python3
import os
import subprocess
from pathlib import Path

# Get all JSON files from discipline to zero alphabetically
vocabulary_dir = Path("vocabulary/content")
all_files = sorted([f for f in vocabulary_dir.glob("*.json")])

# Find the index of discipline.json
start_idx = None
for i, f in enumerate(all_files):
    if f.name == "discipline.json":
        start_idx = i
        break

if start_idx is None:
    print("Could not find discipline.json")
    exit(1)

# Process all files from discipline onwards
files_to_process = all_files[start_idx:]
print(f"Processing {len(files_to_process)} files from discipline.json to {files_to_process[-1].name}")

success_count = 0
error_count = 0

for filepath in files_to_process:
    try:
        result = subprocess.run(
            ["python3", "format_json.py", str(filepath)],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print(f"✓ {filepath.name}")
            success_count += 1
        else:
            print(f"✗ {filepath.name}: {result.stderr}")
            error_count += 1
    except Exception as e:
        print(f"✗ {filepath.name}: {e}")
        error_count += 1

print(f"\nCompleted: {success_count} successful, {error_count} errors")