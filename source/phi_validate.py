#!/usr/bin/env python3
"""
Phi Comprehensive Validator - Standard Command-Line Tool
Easy-to-use interface for 4-layer phi validation on any text.
"""

import argparse
import sys
from pathlib import Path
from enhanced_particles_validator import EnhancedParticlesValidator

def validate_file(filepath: str, validator: EnhancedParticlesValidator) -> dict:
    """Validate a phi file using comprehensive 4-layer validation."""
    try:
        results = validator.validate_particles_file(filepath)
        return results
    except Exception as e:
        print(f"❌ Error validating file: {e}")
        return None

def validate_sentence(sentence: str, validator: EnhancedParticlesValidator) -> dict:
    """Validate a single phi sentence."""
    return validator.validate_complete(sentence)

def print_validation_summary(results: dict, verbose: bool = False):
    """Print a summary of validation results."""
    if not results:
        return
    
    total = results['total']
    valid_count = len(results['valid'])
    issue_count = len(results['issues'])
    
    print(f"\n📊 VALIDATION SUMMARY:")
    print(f"  Total sentences: {total}")
    print(f"  ✅ Valid: {valid_count} ({valid_count/total*100:.1f}%)")
    print(f"  ❌ Invalid: {issue_count} ({issue_count/total*100:.1f}%)")
    
    if issue_count > 0:
        # Count issues by layer
        layer_stats = {'lexicon': 0, 'phonotactics': 0, 'structure': 0, 'semantics': 0}
        for sentence, result in results['issues']:
            for layer, data in result['layers'].items():
                if not data['valid']:
                    layer_stats[layer] += 1
        
        print(f"\n📋 Issues by layer:")
        for layer, count in layer_stats.items():
            if count > 0:
                print(f"  {layer.upper()}: {count} sentences")
        
        if verbose:
            print(f"\n❌ INVALID SENTENCES:")
            for i, (sentence, result) in enumerate(results['issues'][:10], 1):
                issue_types = [layer for layer, data in result['layers'].items() if not data['valid']]
                print(f"  {i:2}. {sentence[:60]}...")
                print(f"      Issues: {', '.join(issue_types)}")
            
            if len(results['issues']) > 10:
                print(f"      ... and {len(results['issues'])-10} more")

def print_sentence_result(sentence: str, result: dict, verbose: bool = False):
    """Print results for a single sentence validation."""
    status = "✅ VALID" if result['overall_valid'] else "❌ INVALID"
    print(f"\n{status}: {sentence}")
    
    if verbose or not result['overall_valid']:
        print(f"\n📋 Validation layers:")
        for layer, data in result['layers'].items():
            status = "✅ PASS" if data['valid'] else "❌ FAIL"
            issue_count = len(data['issues'])
            print(f"  {status} {layer.upper()}: {issue_count} issues")
            
            if issue_count > 0 and verbose:
                for issue in data['issues'][:3]:  # Show first 3 issues
                    print(f"      🚨 {issue}")
                if issue_count > 3:
                    print(f"      ... and {issue_count-3} more")

def main():
    """Main command-line interface."""
    parser = argparse.ArgumentParser(
        description="Phi Comprehensive Validator - 4-layer validation for phi text",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  phi_validate.py pos/particles.md                    # Validate particles.md
  phi_validate.py --sentence "mia li whuwa"           # Validate single sentence  
  phi_validate.py pos/particles.md --verbose          # Detailed output
  phi_validate.py --sentence "thi phela" --verbose    # Detailed single sentence
        """
    )
    
    # Main arguments
    parser.add_argument('file', nargs='?', help='Phi file to validate')
    parser.add_argument('--sentence', '-s', help='Single phi sentence to validate')
    parser.add_argument('--verbose', '-v', action='store_true', help='Detailed output')
    parser.add_argument('--quiet', '-q', action='store_true', help='Minimal output')
    
    args = parser.parse_args()
    
    # Validate arguments
    if not args.file and not args.sentence:
        parser.error("Must specify either a file or --sentence")
    
    if args.file and args.sentence:
        parser.error("Cannot specify both file and --sentence")
    
    if args.file and not Path(args.file).exists():
        parser.error(f"File not found: {args.file}")
    
    # Initialize validator
    if not args.quiet:
        print("🔧 PHI COMPREHENSIVE VALIDATOR")
        print("=" * 50)
        print("4-layer validation: Lexicon → Phonotactics → Structure → Semantics")
        print()
    
    validator = EnhancedParticlesValidator()
    
    # Run validation
    if args.file:
        # File validation
        if not args.quiet:
            print(f"📖 Validating file: {args.file}")
        
        results = validate_file(args.file, validator)
        if results:
            print_validation_summary(results, args.verbose)
            
            # Exit code based on results
            if len(results['issues']) == 0:
                sys.exit(0)  # All valid
            else:
                sys.exit(1)  # Has issues
    
    else:
        # Single sentence validation
        if not args.quiet:
            print(f"📝 Validating sentence: {args.sentence}")
        
        result = validate_sentence(args.sentence, validator)
        print_sentence_result(args.sentence, result, args.verbose)
        
        # Exit code based on result
        sys.exit(0 if result['overall_valid'] else 1)

if __name__ == "__main__":
    main() 