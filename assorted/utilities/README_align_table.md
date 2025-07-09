# Table Alignment Script

## Purpose
Aligns Markdown table columns in Phi vocabulary files for consistent, professional formatting.

## Usage
```bash
python3 utilities/align_table.py <filename>
```

## What it does
1. Finds all Markdown tables with the standard Phi vocabulary format:
   - `| phi word | concept description | cultural meaning | english translation |`
2. Calculates the longest string in each column
3. Sets column width to longest string + 2 characters
4. Left-aligns all text within columns
5. Updates separator lines with proper dashes

## Example
**Before:**
```
| phi word | concept description | cultural meaning | english translation |
| -------- | ------------------- | ---------------- | ------------------- |
|          | person | individual | human |
```

**After:**
```
| phi word   | concept description   | cultural meaning   | english translation   |
| ---------- | --------------------- | ------------------ | --------------------- |
|            | person                | individual         | human                 |
```

## Files it works with
- All Phi vocabulary files in `source/pos/noun/` directory
- Any Markdown file with the standard 4-column table format

## Notes
- Script modifies files in-place (overwrites original)
- Always backup files before running if unsure
- Handles multiple tables within the same file
- Preserves all non-table content unchanged
