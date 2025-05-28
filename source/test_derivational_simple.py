#!/usr/bin/env python3
"""
Simple Derivational Validation Test

Test the core derivational validation fixes with only real words.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from phi_validation.core import PhiSentenceValidator


def test_core_derivational_fixes():
    """Test the core derivational validation fixes."""
    print("Testing Core Derivational Validation Fixes")
    print("=" * 50)
    
    validator = PhiSentenceValidator()
    
    # Test cases with only real words from the lexicon
    test_cases = [
        # The core problem case (should now work)
        ("ra shotu phera ritune tushe", "Complex: loving is very good", True),
        ("ra shotu phera tushe", "Complex: loving is good", True),
        ("ra shotu phera", "Basic: loving is", True),
        
        # Basic derivational constructions
        ("ra whumi phera", "Running is", True),
        ("mia ra whumi phera", "My running is", True),
        
        # Modifiers after verbs (should be allowed)
        ("mia phera tushe", "I am good", True),
        ("mia sholu ritune", "I walk very", True),
        ("thi thilu peshe", "You are small", True),
        
        # se constructions with real words
        ("mia se lathia", "I axe (use axe)", True),
        ("se lathia ta whuru", "Axing stops", True),
    ]
    
    print(f"\n🧪 Testing {len(test_cases)} cases with real words:")
    print("-" * 40)
    
    passed = 0
    failed = 0
    
    for sentence, description, should_be_valid in test_cases:
        print(f"\nTest: {sentence}")
        print(f"Expected: {description}")
        
        result = validator.validate_sentence(sentence)
        is_valid = result['is_valid']
        
        if is_valid == should_be_valid:
            print(f"✅ PASSED: {'VALID' if is_valid else 'INVALID'}")
            passed += 1
        else:
            print(f"❌ FAILED: Expected {'VALID' if should_be_valid else 'INVALID'}, got {'VALID' if is_valid else 'INVALID'}")
            failed += 1
            
            # Show errors for debugging
            if result['errors']:
                print("   Errors:")
                for error in result['errors']:
                    print(f"     • {error.error_type.value}: {error.message}")
            
            if result['warnings']:
                print("   Warnings:")
                for warning in result['warnings']:
                    print(f"     ⚠️ {warning.error_type.value}: {warning.message}")
    
    print("\n" + "=" * 50)
    print(f"📊 Results: {passed}/{len(test_cases)} passed")
    
    return failed == 0


def test_specific_fix():
    """Test the specific case that motivated this fix."""
    print("\n" + "=" * 50)
    print("🎯 Testing Specific Problematic Case")
    print("=" * 50)
    
    validator = PhiSentenceValidator()
    
    sentence = "ra shotu phera ritune tushe"
    print(f"Sentence: {sentence}")
    print(f"Structure: [ra shotu] [phera] [ritune] [tushe]")
    print(f"Semantics: [loving] [is] [very] [good]")
    
    result = validator.validate_sentence(sentence)
    
    print(f"\nResult: {'✅ VALID' if result['is_valid'] else '❌ INVALID'}")
    
    # Count different types of issues
    actual_errors = len(result['actual_errors'])
    warnings = len(result['warnings'])
    
    print(f"Actual errors: {actual_errors}")
    print(f"Warnings: {warnings}")
    
    if actual_errors == 0:
        print("🎉 SUCCESS: The problematic case now validates correctly!")
        if warnings > 0:
            print(f"Note: {warnings} warnings present, but these don't affect validity.")
        return True
    else:
        print("❌ Still has errors:")
        for error in result['actual_errors']:
            print(f"  • {error.error_type.value}: {error.message}")
        return False


def main():
    """Run the simplified derivational validation tests."""
    print("Enhanced Derivational Validation: Simple Test")
    print("=" * 60)
    
    # Test 1: Core derivational fixes with real words
    core_passed = test_core_derivational_fixes()
    
    # Test 2: Specific problematic case
    specific_passed = test_specific_fix()
    
    # Overall result
    print("\n" + "=" * 60)
    print("🏁 Final Assessment")
    print("=" * 60)
    
    if core_passed and specific_passed:
        print("🎉 SUCCESS: Enhanced derivational validation is working!")
        print("✅ The core derivational issues have been resolved.")
        print("✅ Complex derivational constructions now validate correctly.")
        print("✅ Post-verbal modifiers are properly supported.")
        print("\n🔧 Key Fixes Applied:")
        print("  • Word type normalization (verbs vs verb)")
        print("  • Enhanced SOV validation with derivational awareness")
        print("  • Semantic unit recognition for ra+verb and se+noun")
        print("  • Support for post-verbal modifiers (adjectives, adverbs)")
        return True
    else:
        print("⚠️ PARTIAL SUCCESS: Some issues remain.")
        if specific_passed:
            print("✅ The main problematic case is fixed.")
        if not core_passed:
            print("❌ Some edge cases still need work.")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 