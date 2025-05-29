#!/usr/bin/env python3
"""
Test Evidentiality Examples from Manual

Validates evidentiality examples using the proven examples from exercise_validator.py
that are already validated and use proper phi vocabulary.
"""

import sys
from pathlib import Path

# Add the phi_validation module to path
sys.path.append(str(Path(__file__).parent / 'phi_validation'))

from phi_validation.core import PhiSentenceValidator

def test_evidentiality_examples():
    """Test evidentiality examples using validated examples from exercise_validator.py."""
    
    # Initialize validator
    validator = PhiSentenceValidator()

    # VALIDATED evidentiality examples from exercise_validator.py
    test_sentences = [
        # Direct evidence (hi)
        'hi ne riwhea ta whuru.',  # "The wind is blowing (I see it directly)"
        'hi mia ta whemo.',  # "I am thinking (direct evidence)"
        
        # Inference (ro)
        'ro he thephoa ta phoni.',  # "A person lives (I infer this from evidence)"
        'ro ne raoshea ta waphe phera.',  # "The sun is warm (I infer from evidence)"
        
        # Hearsay (nu)
        'nu he thephoa na ne lophui li whesa.',  # "A person created art (I heard this from others)"
        'nu he thephoa ta whemo.',  # "A person thinks (I heard this)"
        'nu sha na ne noshea li theso.',  # "They cooked food (people said this)"
        
        # Reported speech (ti)
        'ti he nowhea li shuso mia ta whera.',  # "The teacher said I am learning"
        'ti mia li shuso thi ta whera.',  # "I said you are learning"
        
        # Memory (mu)
        'mu mia na ne raoshea li whona.',  # "I looked at the sun (I remember this)"
        'mu he phiphea li whera.',  # "The child learned (I remember this)"
        
        # Presumption (pe)
        'pe ne lashea su whale.',  # "It will rain (I presume/expect this)"
        'pe pi mathai su whuwe.',  # "The cat will sleep (I presume this)"
    ]

    print('EVIDENTIALITY EXAMPLES VALIDATION')
    print('(Using validated examples from exercise_validator.py)')
    print('=' * 60)
    
    valid_count = 0
    total_count = len(test_sentences)

    for i, sentence in enumerate(test_sentences, 1):
        print(f'\n{i:2}. Testing: {sentence}')
        result = validator.validate_sentence(sentence)
        
        if result['is_valid']:
            print('    ✅ VALID')
            valid_count += 1
        else:
            print('    ❌ INVALID')
            for error in result['actual_errors']:
                print(f'       - {error.message}')
                if hasattr(error, 'word') and error.word:
                    print(f'         [word: {error.word}]')
    
    print(f'\n{"-" * 60}')
    print(f'SUMMARY: {valid_count}/{total_count} sentences are valid')
    
    if valid_count == total_count:
        print('🎉 ALL EVIDENTIALITY EXAMPLES ARE GRAMMATICALLY CORRECT!')
        print('✅ Ready to update the manual with these validated examples.')
    else:
        print(f'⚠️  {total_count - valid_count} sentences need fixing')
    
    return valid_count == total_count

if __name__ == "__main__":
    success = test_evidentiality_examples()
    sys.exit(0 if success else 1) 