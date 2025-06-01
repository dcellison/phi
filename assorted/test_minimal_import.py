#!/usr/bin/env python3
"""
Minimal import test to isolate the hanging issue.
"""

import signal

def timeout_handler(signum, frame):
    print("❌ Import timed out!")
    exit(1)

signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(10)

print("Testing imports step by step...")

print("1. Importing errors...")
from phi_validation.errors import SentenceError, SentenceValidationError
print("✅ errors OK")

print("2. Importing lexicon...")
from phi_validation.lexicon import LexiconValidator
print("✅ lexicon OK")

print("3. Importing particles...")
from phi_validation.particles import ParticleValidator
print("✅ particles OK")

print("4. Importing word_order...")
from phi_validation.word_order import WordOrderValidator
print("✅ word_order OK")

print("5. Importing temporal...")
from phi_validation.temporal import TemporalValidator
print("✅ temporal OK")

print("6. Importing semantic_roles...")
from phi_validation.semantic_roles import SemanticRoleValidator
print("✅ semantic_roles OK")

print("7. Importing modality...")
from phi_validation.modality import ModalityValidator
print("✅ modality OK")

print("8. Importing evidentiality...")
from phi_validation.evidentiality import EvidentialityValidator
print("✅ evidentiality OK")

print("9. Importing derivational...")
from phi_validation.derivational import DerivationalValidator
print("✅ derivational OK")

print("10. Importing emphasis...")
from phi_validation.emphasis import EmphasisValidator
print("✅ emphasis OK")

print("11. Importing politeness...")
from phi_validation.politeness import PolitenessValidator
print("✅ politeness OK")

print("12. Importing discourse...")
from phi_validation.discourse import DiscourseValidator
print("✅ discourse OK")

print("13. Importing interrogative...")
from phi_validation.interrogative import InterrogativeValidator
print("✅ interrogative OK")

print("14. Importing narrative...")
from phi_validation.narrative import NarrativeValidator
print("✅ narrative OK")

print("15. All imports successful!")
signal.alarm(0)  # Cancel alarm 