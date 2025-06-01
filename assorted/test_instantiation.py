#!/usr/bin/env python3
"""
Test class instantiation to isolate the hanging issue.
"""

import signal
import sys
from pathlib import Path

def timeout_handler(signum, frame):
    print("❌ Instantiation timed out!")
    exit(1)

signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(15)

print("Testing class instantiation step by step...")

# Add path for phi_validator
sys.path.append(str(Path(__file__).parent.parent))

print("1. Importing phi_validator...")
from phi_validator import PhiValidator
print("✅ phi_validator import OK")

print("2. Instantiating PhiValidator...")
word_validator = PhiValidator()
print("✅ PhiValidator instantiation OK")

print("3. Importing validation modules...")
from phi_validation.errors import SentenceError, SentenceValidationError
from phi_validation.lexicon import LexiconValidator
from phi_validation.particles import ParticleValidator
from phi_validation.word_order import WordOrderValidator
from phi_validation.temporal import TemporalValidator
from phi_validation.semantic_roles import SemanticRoleValidator
from phi_validation.modality import ModalityValidator
from phi_validation.evidentiality import EvidentialityValidator
from phi_validation.derivational import DerivationalValidator
from phi_validation.emphasis import EmphasisValidator
from phi_validation.politeness import PolitenessValidator
from phi_validation.discourse import DiscourseValidator
from phi_validation.interrogative import InterrogativeValidator
from phi_validation.narrative import NarrativeValidator
print("✅ All imports OK")

print("4. Instantiating LexiconValidator...")
lexicon_validator = LexiconValidator(word_validator)
print("✅ LexiconValidator instantiation OK")

print("5. Instantiating ParticleValidator...")
particle_validator = ParticleValidator()
print("✅ ParticleValidator instantiation OK")

print("6. Instantiating WordOrderValidator...")
word_order_validator = WordOrderValidator()
print("✅ WordOrderValidator instantiation OK")

print("7. Instantiating TemporalValidator...")
temporal_validator = TemporalValidator()
print("✅ TemporalValidator instantiation OK")

print("8. Instantiating SemanticRoleValidator...")
semantic_role_validator = SemanticRoleValidator()
print("✅ SemanticRoleValidator instantiation OK")

print("9. Instantiating ModalityValidator...")
modality_validator = ModalityValidator()
print("✅ ModalityValidator instantiation OK")

print("10. Instantiating EvidentialityValidator...")
evidentiality_validator = EvidentialityValidator()
print("✅ EvidentialityValidator instantiation OK")

print("11. Instantiating DerivationalValidator...")
derivational_validator = DerivationalValidator()
print("✅ DerivationalValidator instantiation OK")

print("12. Instantiating EmphasisValidator...")
emphasis_validator = EmphasisValidator()
print("✅ EmphasisValidator instantiation OK")

print("13. Instantiating PolitenessValidator...")
politeness_validator = PolitenessValidator()
print("✅ PolitenessValidator instantiation OK")

print("14. Instantiating DiscourseValidator...")
discourse_validator = DiscourseValidator()
print("✅ DiscourseValidator instantiation OK")

print("15. Instantiating InterrogativeValidator...")
interrogative_validator = InterrogativeValidator()
print("✅ InterrogativeValidator instantiation OK")

print("16. Instantiating NarrativeValidator...")
narrative_validator = NarrativeValidator()
print("✅ NarrativeValidator instantiation OK")

print("17. All instantiations successful!")
signal.alarm(0)  # Cancel alarm 