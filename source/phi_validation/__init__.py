"""
Phi Sentence Validation Package

A modular sentence validation system for the Phi constructed language.
Validates complete sentences for grammatical correctness, including:
- SOV word order compliance
- Particle placement and ordering
- Semantic coherence
- Discourse structure
- Pragmatic appropriateness

Usage:
    from phi_validation import PhiSentenceValidator
    
    validator = PhiSentenceValidator()
    result = validator.validate_sentence("mia ta thihi")
    print(validator.generate_report(result))
"""

from .core import PhiSentenceValidator

__version__ = "1.0.0"
__author__ = "Phi Language Development Team"

__all__ = [
    "PhiSentenceValidator"
] 