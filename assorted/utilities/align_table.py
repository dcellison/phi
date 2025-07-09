#!/usr/bin/env python3
import re

def align_table_columns(filename):
    with open(filename, 'r') as f:
        content = f.read()
    
    lines = content.split('\n')
    output_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check if this is a table header line (flexible matching)
        if ('phi word' in line and 'concept description' in line and 
            'cultural meaning' in line and 'english translation' in line and '|' in line):
            # Found a table, process it
            table_lines = []
            table_lines.append(line)  # header
            i += 1
            
            # Get the separator line
            if i < len(lines) and '|' in lines[i] and '-' in lines[i]:
                table_lines.append(lines[i])
                i += 1
                
                # Collect all table rows
                while i < len(lines) and lines[i].strip().startswith('|') and lines[i].strip().endswith('|'):
                    table_lines.append(lines[i])
                    i += 1
                
                # Process this table
                aligned_table = align_single_table(table_lines)
                output_lines.extend(aligned_table)
            else:
                output_lines.append(line)
        else:
            output_lines.append(line)
            i += 1
    
    # Write back to file
    with open(filename, 'w') as f:
        f.write('\n'.join(output_lines))

def align_single_table(table_lines):
    # Parse all rows to find column contents
    all_rows = []
    
    for line in table_lines:
        if '|' in line:
            # Split by | and clean up
            parts = [part.strip() for part in line.split('|')]
            # Remove empty first/last elements from splitting
            if parts and parts[0] == '':
                parts = parts[1:]
            if parts and parts[-1] == '':
                parts = parts[:-1]
            all_rows.append(parts)
    
    if not all_rows:
        return table_lines
    
    # Find max width for each column
    num_cols = len(all_rows[0])
    col_widths = [0] * num_cols
    
    for row in all_rows:
        for i, cell in enumerate(row):
            if i < len(col_widths):
                col_widths[i] = max(col_widths[i], len(cell))
    
    # Add 2 extra characters to each column width
    col_widths = [w + 2 for w in col_widths]
    
    # Rebuild the table
    aligned_lines = []
    
    for row_idx, row in enumerate(all_rows):
        if row_idx == 1:  # separator line
            # Build separator line with proper dashes
            parts = []
            for i in range(num_cols):
                parts.append('-' * col_widths[i])
            aligned_lines.append('| ' + ' | '.join(parts) + ' |')
        else:
            # Build data line
            parts = []
            for i in range(num_cols):
                cell = row[i] if i < len(row) else ''
                parts.append(cell.ljust(col_widths[i]))
            aligned_lines.append('| ' + ' | '.join(parts) + ' |')
    
    return aligned_lines

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python align_table.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    align_table_columns(filename)
    print("Table alignment completed!")
