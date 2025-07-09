#!/usr/bin/env python3

import json
from datetime import datetime

def main():
    # Load the JSON file
    with open('phi_words.json', 'r') as f:
        data = json.load(f)
    
    # Create backup with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = f'phi_words_backup_{timestamp}.json'
    with open(backup_file, 'w') as f:
        json.dump(data, f, indent=2)
    print(f'Backup created: {backup_file}')
    
    # Update categories by removing 'essential ' prefix
    updated_count = 0
    for word, info in data.items():
        if isinstance(info, dict) and 'category' in info:
            old_category = info['category']
            if old_category.startswith('essential '):
                new_category = old_category[10:]  # Remove 'essential ' (10 chars)
                info['category'] = new_category
                updated_count += 1
                if updated_count <= 10:  # Show first 10 examples
                    print(f'Updated: "{old_category}" -> "{new_category}"')
                elif updated_count == 11:
                    print('... (showing first 10 examples)')
    
    # Save updated JSON
    with open('phi_words.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f'\nTotal categories updated: {updated_count}')

if __name__ == '__main__':
    main() 