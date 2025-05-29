#!/usr/bin/env python3
"""
Core Sentence Validation

Main orchestration class for Phi sentence validation.
Coordinates all validation modules and provides the primary interface.
"""

import sys
import re
from pathlib import Path
from typing import List, Dict, Tuple, Optional

# Add the parent directory to path to import phi_validator
sys.path.append(str(Path(__file__).parent.parent))

from phi_validator import PhiValidator

# Import error definitions
from .errors import SentenceError, SentenceValidationError

# Import validation modules
from .lexicon import LexiconValidator
from .particles import ParticleValidator
from .word_order import WordOrderValidator
from .temporal import TemporalValidator
from .semantic_roles import SemanticRoleValidator
from .modality import ModalityValidator
from .evidentiality import EvidentialityValidator
from .emphasis import EmphasisValidator
from .politeness import PolitenessValidator
from .discourse import DiscourseValidator
from .interrogative import InterrogativeValidator
from .narrative import NarrativeValidator
from .punctuation import PunctuationValidator


class PhiSentenceValidator:
    """
    Main sentence validator for Phi.
    
    Orchestrates all validation modules to provide comprehensive
    sentence-level grammatical analysis.
    """
    
    def __init__(self):
        """Initialize the validator and all sub-modules."""
        # Initialize the word-level validator
        self.word_validator = PhiValidator()
        
        # Initialize all validation modules
        self.lexicon_validator = LexiconValidator(self.word_validator)
        self.particle_validator = ParticleValidator()
        self.word_order_validator = WordOrderValidator()
        self.temporal_validator = TemporalValidator()
        self.semantic_role_validator = SemanticRoleValidator()
        self.modality_validator = ModalityValidator()
        self.evidentiality_validator = EvidentialityValidator()
        self.emphasis_validator = EmphasisValidator()
        self.politeness_validator = PolitenessValidator()
        self.discourse_validator = DiscourseValidator()
        self.interrogative_validator = InterrogativeValidator()
        self.narrative_validator = NarrativeValidator()
        self.punctuation_validator = PunctuationValidator()
        
        # Set up cross-module dependencies
        self.word_order_validator.set_lexicon_validator(self.lexicon_validator)
        self.particle_validator.set_lexicon_validator(self.lexicon_validator)
        self.temporal_validator.set_lexicon_validator(self.lexicon_validator)
        self.semantic_role_validator.set_lexicon_validator(self.lexicon_validator)
        self.modality_validator.set_lexicon_validator(self.lexicon_validator)
        self.emphasis_validator.set_lexicon_validator(self.lexicon_validator)
        self.narrative_validator.set_lexicon_validator(self.lexicon_validator)
        self.punctuation_validator.set_lexicon_validator(self.lexicon_validator)
        
    def tokenize_sentence(self, sentence: str) -> List[str]:
        """Tokenize a Phi sentence into words."""
        # Use the punctuation validator to clean the text properly
        cleaned = self.punctuation_validator.clean_text_for_tokenization(sentence)
        return cleaned.split()
    
    def validate_sentence(self, sentence: str) -> Dict:
        """
        Comprehensive validation of a Phi sentence.
        
        Returns a dictionary with:
        - sentence: original sentence
        - tokens: tokenized words
        - errors: list of validation errors
        - actual_errors: list of actual errors
        - warnings: list of warnings
        - is_valid: boolean indicating overall validity
        - error_summary: count of errors by type
        """
        # First, validate punctuation on the raw text
        all_errors = []
        all_errors.extend(self.punctuation_validator.validate_punctuation(sentence, []))
        
        # Then tokenize for grammar validation
        tokens = self.tokenize_sentence(sentence)
        
        if not tokens:
            empty_error = SentenceValidationError(
                SentenceError.INVALID_WORD,
                "Empty sentence"
            )
            return {
                "sentence": sentence,
                "tokens": tokens,
                "errors": [empty_error] + all_errors,
                "actual_errors": [empty_error] + all_errors,
                "warnings": [],
                "is_valid": False,
                "error_summary": {"Empty sentence": 1}
            }
        
        # Continue with grammar validation
        # 1. Lexicon validation (word existence and types)
        all_errors.extend(self.lexicon_validator.validate_words(tokens))
        
        # 2. Particle validation (ordering and scope)
        all_errors.extend(self.particle_validator.validate_particles(tokens))
        
        # 3. Word order validation (SOV structure)
        all_errors.extend(self.word_order_validator.validate_order(tokens))
        
        # 4. Temporal validation (tense, aspect, temporal logic)
        all_errors.extend(self.temporal_validator.validate_temporal_structure(tokens))
        
        # 5. Semantic role validation (animacy, classifiers, arguments)
        all_errors.extend(self.semantic_role_validator.validate_semantic_roles(tokens))
        
        # 6. Modality validation (modal logic, conditionals)
        all_errors.extend(self.modality_validator.validate_modal_logic(tokens))
        
        # 7. Evidentiality validation (evidential particles and combinations)
        all_errors.extend(self.evidentiality_validator.validate_evidentiality(tokens))
        
        # 8. Emphasis validation (ma particle scope)
        all_errors.extend(self.emphasis_validator.validate_emphasis_scope(tokens))
        
        # 9. Politeness validation (so particle context)
        all_errors.extend(self.politeness_validator.validate_politeness_context(tokens))
        
        # 10. Discourse validation (ha/mi sequences)
        all_errors.extend(self.discourse_validator.validate_discourse_sequences(tokens))
        
        # 11. Interrogative validation (question structures)
        all_errors.extend(self.interrogative_validator.validate_interrogatives(tokens))
        
        # 12. Narrative validation (relative clauses, sequences)
        all_errors.extend(self.narrative_validator.validate_narrative_structure(tokens))
        
        # Summarize errors by type
        error_summary = {}
        actual_errors = []
        warnings = []
        
        for error in all_errors:
            error_type = error.error_type.value
            error_summary[error_type] = error_summary.get(error_type, 0) + 1
            
            # Separate warnings from actual errors
            if error_type.endswith('_warning'):
                warnings.append(error)
            else:
                actual_errors.append(error)
        
        return {
            "sentence": sentence,
            "tokens": tokens,
            "errors": all_errors,
            "actual_errors": actual_errors,
            "warnings": warnings,
            "is_valid": len(actual_errors) == 0,  # Only actual errors affect validity
            "error_summary": error_summary
        }
    
    def generate_report(self, validation_result: Dict) -> str:
        """Generate a formatted sentence validation report."""
        sentence = validation_result["sentence"]
        tokens = validation_result["tokens"]
        errors = validation_result["errors"]
        actual_errors = validation_result["actual_errors"]
        warnings = validation_result["warnings"]
        is_valid = validation_result["is_valid"]
        
        report = f"""
PHI SENTENCE VALIDATION REPORT
==============================
Sentence: {sentence}
Tokens: {' | '.join(tokens)}

VALIDATION STATUS: {'✅ VALID' if is_valid else '❌ INVALID'}
"""
        
        if actual_errors:
            report += f"\nACTUAL ERRORS FOUND ({len(actual_errors)}):\n"
            for i, error in enumerate(actual_errors, 1):
                position_info = f" (position {error.position})" if error.position is not None else ""
                word_info = f" [word: {error.word}]" if error.word else ""
                report += f"  {i}. [{error.error_type.value.upper()}]{position_info} {error.message}{word_info}\n"
            
            # Error summary
            report += f"\nERROR SUMMARY:\n"
            for error_type, count in validation_result["error_summary"].items():
                report += f"  {error_type}: {count}\n"
        else:
            report += "\n✅ No actual errors found - sentence follows all Phi grammar rules!\n"
        
        if warnings:
            report += f"\nWARNINGS FOUND ({len(warnings)}):\n"
            for i, warning in enumerate(warnings, 1):
                position_info = f" (position {warning.position})" if warning.position is not None else ""
                word_info = f" [word: {warning.word}]" if warning.word else ""
                report += f"  {i}. [{warning.error_type.value.upper()}]{position_info} {warning.message}{word_info}\n"
            
            # Warning summary
            report += f"\nWARNING SUMMARY:\n"
            for error_type, count in validation_result["error_summary"].items():
                if error_type.endswith('_warning'):
                    report += f"  {error_type}: {count}\n"
        else:
            report += "\n✅ No warnings found - sentence follows all Phi grammar rules!\n"
        
        return report


def main():
    """Command-line interface for sentence validation."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Validate Phi sentences")
    parser.add_argument("sentence", nargs="?", help="Sentence to validate")
    parser.add_argument("--interactive", "-i", action="store_true", 
                       help="Interactive mode")
    parser.add_argument("--file", "-f", help="File with sentences to validate")
    
    args = parser.parse_args()
    
    validator = PhiSentenceValidator()
    
    if args.interactive:
        print("Phi Sentence Validator - Interactive Mode")
        print("Enter sentences to validate (empty line to quit):")
        print()
        
        while True:
            try:
                sentence = input("phi> ").strip()
                if not sentence:
                    break
                
                result = validator.validate_sentence(sentence)
                print(validator.generate_report(result))
                print("-" * 50)
                
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
    
    elif args.file:
        try:
            with open(args.file, 'r') as f:
                for line_num, line in enumerate(f, 1):
                    sentence = line.strip()
                    if not sentence or sentence.startswith('#'):
                        continue
                    
                    print(f"Line {line_num}: {sentence}")
                    result = validator.validate_sentence(sentence)
                    print(validator.generate_report(result))
                    print("=" * 60)
        
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found")
            return 1
    
    elif args.sentence:
        result = validator.validate_sentence(args.sentence)
        print(validator.generate_report(result))
    
    else:
        parser.print_help()
    
    return 0


if __name__ == "__main__":
    exit(main()) 