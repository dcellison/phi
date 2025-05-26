#!/usr/bin/env python3
"""
New Words for Dylan Translation: "Blowin' in the Wind"

Creates ONLY the truly missing words needed for Dylan translation.
Most vocabulary already exists in Phi!
"""

import sys
from pathlib import Path

# Add the current directory to path to import phi_validator
sys.path.append(str(Path(__file__).parent))

from phi_validator import PhiValidator, ValidationResult


def create_dylan_vocabulary():
    """Create only the truly missing words needed for Dylan translation."""
    
    # Only words that don't exist in current Phi vocabulary
    proposed_words = [
        # NOUNS - Pattern: [C/F][V/P][F][P]
        ("whithea", "noun", "dove"),                   # wh + i + th + ea
        ("phothea", "noun", "cannonball"),             # ph + o + th + ea
        
        # VERBS - Pattern: [F][V][C][V]
        ("thunu", "verb", "ban/prohibit"),             # th + u + n + u
        ("whuru", "verb", "blow (wind)"),              # wh + u + r + u
        
        # ADVERBS - Pattern: [C][V][C][V][C][V]
        ("walito", "adverb", "forever/always"),        # w + a + l + i + t + o
    ]
    
    return proposed_words


def validate_new_words():
    """Validate all proposed new words."""
    print("VALIDATING MINIMAL NEW WORDS FOR DYLAN TRANSLATION")
    print("=" * 60)
    print("Note: Most vocabulary already exists in Phi!")
    print()
    
    validator = PhiValidator()
    proposed_words = create_dylan_vocabulary()
    
    valid_words = []
    invalid_words = []
    
    for word, pos, meaning in proposed_words:
        result = validator.validate_word(word, pos, meaning)
        is_valid = result["overall_status"] == ValidationResult.VALID
        
        if is_valid:
            print(f"✅ {word} ({pos}) - {meaning} - VALID")
            valid_words.append((word, pos, meaning))
        else:
            print(f"❌ {word} ({pos}) - {meaning} - INVALID:")
            for error in result["phonotactic_errors"] + result["lexical_errors"]:
                print(f"   → {error.message}")
            invalid_words.append((word, pos, meaning))
    
    print(f"\nVALIDATION SUMMARY:")
    print(f"Valid words: {len(valid_words)}")
    print(f"Invalid words: {len(invalid_words)}")
    
    if valid_words:
        print(f"\nVALID WORDS TO ADD:")
        for word, pos, meaning in valid_words:
            print(f"  {word} ({pos}): {meaning}")
    
    if invalid_words:
        print(f"\nINVALID WORDS NEEDING REVISION:")
        for word, pos, meaning in invalid_words:
            print(f"  {word} ({pos}): {meaning}")
    
    return valid_words, invalid_words


def generate_improved_translation():
    """Generate improved translation using existing + minimal new vocabulary."""
    print("\n" + "=" * 60)
    print("IMPROVED TRANSLATION USING EXISTING + MINIMAL NEW VOCABULARY")
    print("=" * 60)
    
    print("**riwhea wheo whuru** (Blowin' in the Wind)")
    print()
    
    print("**hamite naphai huphui li phola**")
    print("**pimo thi huphui thami**")
    print("How many roads must a man walk")
    print("Before you call him a man?")
    print()
    
    print("**hamite latheo sathi whithea li sharo**")
    print("**pimo shuwhia wheo phuwe**")
    print("How many seas must a white dove sail")
    print("Before sleeping in the sand?")
    print()
    
    print("**wha nene hamite thashoa phothea li phawi**")
    print("**pimo walito thunu**")
    print("Yes, and how many times must cannonballs fly")
    print("Before they're forever banned?")
    print()
    
    print("**lowhai mia miwhoa riwhea wheo whuru**")
    print("**lowhai riwhea wheo whuru**")
    print("The answer, my friend, is blowin' in the wind")
    print("The answer is blowin' in the wind")
    
    print("\n" + "=" * 60)
    print("VOCABULARY BREAKDOWN:")
    print("=" * 60)
    print("EXISTING WORDS USED:")
    print("  naphai (road/path), huphui (man), latheo (sea)")
    print("  sathi (white), shuwhia (sand), phuwe (sleep)")
    print("  phawi (fly), riwhea (wind), thami (call/name)")
    print("  sharo (go/sail), lowhai (answer), miwhoa (friend)")
    print("  hamite (how many), thashoa (times/day)")
    print()
    print("NEW WORDS CREATED:")
    print("  whithea (dove), phothea (cannonball)")
    print("  thunu (ban), whuru (blow), walito (forever)")


if __name__ == "__main__":
    valid_words, invalid_words = validate_new_words()
    
    if len(invalid_words) == 0:
        generate_improved_translation()
    else:
        print(f"\nPlease fix {len(invalid_words)} invalid words before generating translation.") 