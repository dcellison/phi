#!/usr/bin/env python3
import json
import sys
import os

def compact_json(obj, indent_level=0):
    """Custom JSON formatter that puts arrays on single lines"""
    indent = "  " * indent_level
    next_indent = "  " * (indent_level + 1)
    
    if isinstance(obj, dict):
        if not obj:
            return "{}"
        items = []
        for key, value in obj.items():
            formatted_value = compact_json(value, indent_level + 1)
            items.append(f'{next_indent}"{key}": {formatted_value}')
        return "{\n" + ",\n".join(items) + "\n" + indent + "}"
    
    elif isinstance(obj, list):
        if not obj:
            return "[]"
        # Format arrays on single lines
        formatted_items = [json.dumps(item, ensure_ascii=False) for item in obj]
        return "[" + ", ".join(formatted_items) + "]"
    
    else:
        # For strings, numbers, booleans, null
        return json.dumps(obj, ensure_ascii=False)

def format_json_file(filepath):
    """Format JSON file to have compact arrays"""
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        # Write back with custom formatting
        with open(filepath, 'w') as f:
            f.write(compact_json(data))
            f.write('\n')  # Add newline at end
        
        return True
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        if format_json_file(filepath):
            print(f"Formatted: {filepath}")
    else:
        print("Usage: python format_json.py <filepath>")