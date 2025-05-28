#!/usr/bin/env python3
"""
Test script to demonstrate the Phi Word Replacer functionality.
"""

from phi_word_replacer import PhiWordReplacer

def test_thihi_replacement():
    """Test replacing 'thihi' with a new verb."""
    replacer = PhiWordReplacer()
    
    print("🔄 PHI WORD REPLACER DEMO")
    print("=" * 50)
    print("Testing replacement of 'thihi' (be) with a new verb...")
    print()
    
    # First, let's see what thihi looks like currently
    print("🔍 Finding current occurrences of 'thihi'...")
    occurrences = replacer.find_word_occurrences('thihi')
    
    if occurrences:
        print(f"📍 Found 'thihi' in {len(occurrences)} files:")
        for file_path, file_occurrences in list(occurrences.items())[:3]:
            print(f"  {file_path}: {len(file_occurrences)} occurrences")
            for line_num, line in file_occurrences[:2]:
                print(f"    Line {line_num}: {line[:70]}{'...' if len(line) > 70 else ''}")
            if len(file_occurrences) > 2:
                print(f"    ... and {len(file_occurrences) - 2} more")
    else:
        print("❌ No occurrences of 'thihi' found")
    
    print()
    print("💡 Suggesting alternatives for verb (pattern [F][V][C][V]):")
    suggestions = replacer.suggest_alternatives('verb')
    if suggestions:
        for i, suggestion in enumerate(suggestions, 1):
            print(f"  {i}. {suggestion}")
    else:
        print("  No suggestions generated")
    
    print()
    print("🧪 Testing validation of a potential replacement...")
    
    # Test validation with a good verb
    test_word = "phelu"  # fricative + vowel + consonant + vowel
    is_valid, errors = replacer.validate_replacement('thihi', test_word, 'verb')
    
    print(f"Testing '{test_word}' as replacement:")
    print(f"  Valid: {is_valid}")
    if errors:
        for error in errors:
            print(f"  {error}")
    
    print()
    print("📋 This tool can:")
    print("  ✅ Find all occurrences of a word across all Phi files")
    print("  ✅ Validate new words follow phonotactic patterns")
    print("  ✅ Check for conflicts with existing words")
    print("  ✅ Create automatic backups before changes")
    print("  ✅ Generate detailed reports of changes")
    print("  ✅ Suggest alternatives following Phi patterns")

if __name__ == "__main__":
    test_thihi_replacement() 