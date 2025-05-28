#!/usr/bin/env python3
"""
Direct validation test bypassing package import.
"""

import signal
import sys
from pathlib import Path

def timeout_handler(signum, frame):
    print("❌ Test timed out!")
    exit(1)

signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(15)

print("Testing direct validation...")

# Add path for phi_validator
sys.path.append(str(Path(__file__).parent.parent))

print("1. Importing PhiSentenceValidator directly...")
from phi_validation.core import PhiSentenceValidator
print("✅ Direct import OK")

print("2. Instantiating validator...")
validator = PhiSentenceValidator()
print("✅ Instantiation OK")

print("3. Testing validation...")
result = validator.validate_sentence("mia ta thilu")
print(f"✅ Validation OK - Valid: {result['is_valid']}")

print("4. Testing report generation...")
report = validator.generate_report(result)
print("✅ Report generation OK")

print("5. All tests successful!")
print(f"Sample result: {result['sentence']} -> {'VALID' if result['is_valid'] else 'INVALID'}")

signal.alarm(0)  # Cancel alarm 