#!/usr/bin/env python3
"""Calculate the total number of possible Phi words given phonological rules."""

# Phi phonological inventory
CONSONANTS = ['h', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w']
FRICATIVE_DIGRAPHS = ['ph', 'th', 'sh', 'wh']
ALL_CONSONANTS = CONSONANTS + FRICATIVE_DIGRAPHS
VOWELS = ['a', 'e', 'i', 'o', 'u']

def calculate_two_syllable_words():
    """Calculate all possible two-syllable Phi words."""
    
    # Pattern 1: CV.CV
    cv_cv_count = len(ALL_CONSONANTS) * len(VOWELS) * len(ALL_CONSONANTS) * len(VOWELS)
    
    # Pattern 2: CV.V (vowel hiatus)
    cv_v_count = len(ALL_CONSONANTS) * len(VOWELS) * len(VOWELS)
    
    total = cv_cv_count + cv_v_count
    
    print("Two-Syllable Phi Words Calculation:")
    print("=" * 50)
    print(f"Consonants (including digraphs): {len(ALL_CONSONANTS)}")
    print(f"  Regular consonants: {CONSONANTS}")
    print(f"  Fricative digraphs: {FRICATIVE_DIGRAPHS}")
    print(f"Vowels: {len(VOWELS)} ({VOWELS})")
    print()
    print("Pattern CV.CV:")
    print(f"  {len(ALL_CONSONANTS)} × {len(VOWELS)} × {len(ALL_CONSONANTS)} × {len(VOWELS)} = {cv_cv_count:,}")
    print()
    print("Pattern CV.V:")
    print(f"  {len(ALL_CONSONANTS)} × {len(VOWELS)} × {len(VOWELS)} = {cv_v_count:,}")
    print()
    print(f"TOTAL possible two-syllable words: {total:,}")
    
    return total

def calculate_three_syllable_words():
    """Calculate all possible three-syllable Phi words."""
    
    # Pattern 1: CV.CV.CV
    cv_cv_cv = len(ALL_CONSONANTS) * len(VOWELS) * len(ALL_CONSONANTS) * len(VOWELS) * len(ALL_CONSONANTS) * len(VOWELS)
    
    # Pattern 2: CV.CV.V
    cv_cv_v = len(ALL_CONSONANTS) * len(VOWELS) * len(ALL_CONSONANTS) * len(VOWELS) * len(VOWELS)
    
    # Pattern 3: CV.V.CV
    cv_v_cv = len(ALL_CONSONANTS) * len(VOWELS) * len(VOWELS) * len(ALL_CONSONANTS) * len(VOWELS)
    
    total = cv_cv_cv + cv_cv_v + cv_v_cv
    
    print("\nThree-Syllable Phi Words Calculation:")
    print("=" * 50)
    print("Pattern CV.CV.CV:")
    print(f"  {len(ALL_CONSONANTS)} × {len(VOWELS)} × {len(ALL_CONSONANTS)} × {len(VOWELS)} × {len(ALL_CONSONANTS)} × {len(VOWELS)} = {cv_cv_cv:,}")
    print()
    print("Pattern CV.CV.V:")
    print(f"  {len(ALL_CONSONANTS)} × {len(VOWELS)} × {len(ALL_CONSONANTS)} × {len(VOWELS)} × {len(VOWELS)} = {cv_cv_v:,}")
    print()
    print("Pattern CV.V.CV:")
    print(f"  {len(ALL_CONSONANTS)} × {len(VOWELS)} × {len(VOWELS)} × {len(ALL_CONSONANTS)} × {len(VOWELS)} = {cv_v_cv:,}")
    print()
    print(f"TOTAL possible three-syllable words: {total:,}")
    
    return total

def main():
    two_syl = calculate_two_syllable_words()
    three_syl = calculate_three_syllable_words()
    
    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    print(f"Total possible two-syllable words: {two_syl:,}")
    print(f"Total possible three-syllable words: {three_syl:,}")
    print(f"Combined total: {two_syl + three_syl:,}")
    
    # Current usage
    print("\nCurrent Usage:")
    print(f"We have created approximately 546 words so far")
    print(f"That's {(546/two_syl)*100:.2f}% of possible two-syllable words")
    print(f"And {(546/(two_syl + three_syl))*100:.2f}% of possible two and three-syllable words combined")

if __name__ == "__main__":
    main()