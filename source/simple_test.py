#!/usr/bin/env python3
import sys
sys.path.append('phi_validation')
from phi_validation.core import PhiSentenceValidator

validator = PhiSentenceValidator()

# Test very simple sentences first
simple_tests = [
    'si mia ta shola.',  # I walk
    'si mia li shola.',  # I walked
    'si thi ta shola.',  # you walk
    'shola.',  # bare verb
]

for sentence in simple_tests:
    print(f'Testing: {sentence}')
    result = validator.validate_sentence(sentence)
    if result['is_valid']:
        print('  ✅ VALID')
    else:
        print('  ❌ INVALID')
        for error in result['actual_errors'][:3]:  # Show first 3 errors
            print(f'    - {error.message}')
    print() 