#!/usr/bin/env python3
"""
Validate Proposed New Words for Fricative Rebalancing

Tests the proposed new 'wh' adjectives and verbs from the rebalancing plan
to ensure they follow correct phonotactic patterns and don't create conflicts.
"""

import sys
from pathlib import Path

# Add the current directory to path to import phi_validator
sys.path.append(str(Path(__file__).parent))

from phi_validator import PhiValidator, ValidationResult


def test_proposed_adjectives():
    """Test proposed new 'wh' adjectives."""
    print("TESTING PROPOSED 'WH' ADJECTIVES")
    print("=" * 50)
    
    proposed_adjectives = [
        ("lawhe", "smooth"),
        ("miwhe", "soft"),
        ("nawhe", "warm"),
        ("pawhe", "cool"),
        ("rawhe", "thick"),
        ("sawhe", "thin"),
        ("tawhe", "wide"),
        ("wawhe", "narrow"),
        ("hiwhe", "tall"),
        ("liwhe", "short"),
        ("miwha", "bright"),
        ("niwha", "dark"),
        ("piwha", "loud"),
        ("riwha", "quiet"),
        ("siwha", "fast"),
        ("tiwha", "slow"),
        ("wiwha", "strong"),
        ("hiwha", "weak"),
        ("liwha", "heavy"),
        ("miwho", "light"),
        ("niwho", "dense"),
        ("piwho", "loose"),
        ("riwho", "tight"),
        ("siwho", "flexible"),
        ("tiwho", "rigid"),
        ("wiwho", "elastic"),
        ("hiwho", "brittle"),
        ("liwho", "durable"),
        ("miwhi", "fresh"),
        ("niwhi", "stale"),
        ("piwhi", "pure"),
        ("riwhi", "mixed"),
        ("siwhi", "clean")
    ]
    
    validator = PhiValidator()
    valid_count = 0
    invalid_count = 0
    
    for word, meaning in proposed_adjectives:
        result = validator.validate_word(word, 'adjective', meaning)
        is_valid = result["overall_status"] == ValidationResult.VALID
        
        if is_valid:
            print(f"✅ {word} ({meaning}) - VALID")
            valid_count += 1
        else:
            print(f"❌ {word} ({meaning}) - INVALID:")
            for error in result["phonotactic_errors"] + result["lexical_errors"]:
                print(f"   → {error.message}")
            invalid_count += 1
    
    print(f"\nADJECTIVE RESULTS: {valid_count} valid, {invalid_count} invalid")
    return valid_count, invalid_count


def test_proposed_verbs():
    """Test proposed new 'wh' verbs."""
    print("\nTESTING PROPOSED 'WH' VERBS")
    print("=" * 50)
    
    proposed_verbs = [
        ("whale", "flow"),
        ("whame", "bend"),
        ("whane", "twist"),
        ("whape", "fold"),
        ("whare", "stretch"),
        ("whase", "compress"),
        ("whate", "expand"),
        ("whawe", "contract"),
        ("whele", "slide"),
        ("wheme", "roll"),
        ("whene", "spin"),
        ("whepe", "rotate"),
        ("where", "pivot"),
        ("whese", "tilt"),
        ("whete", "balance"),
        ("whewe", "stabilize"),
        ("while", "vibrate"),
        ("whime", "oscillate"),
        ("whine", "resonate"),
        ("whipe", "echo"),
        ("whire", "reflect"),
        ("whise", "absorb"),
        ("white", "emit"),
        ("whiwe", "radiate"),
        ("whole", "focus"),
        ("whome", "blur"),
        ("whone", "clarify"),
        ("whope", "obscure"),
        ("whore", "reveal"),
        ("whose", "conceal"),
        ("whote", "expose")
    ]
    
    validator = PhiValidator()
    valid_count = 0
    invalid_count = 0
    
    for word, meaning in proposed_verbs:
        result = validator.validate_word(word, 'verb', meaning)
        is_valid = result["overall_status"] == ValidationResult.VALID
        
        if is_valid:
            print(f"✅ {word} ({meaning}) - VALID")
            valid_count += 1
        else:
            print(f"❌ {word} ({meaning}) - INVALID:")
            for error in result["phonotactic_errors"] + result["lexical_errors"]:
                print(f"   → {error.message}")
            invalid_count += 1
    
    print(f"\nVERB RESULTS: {valid_count} valid, {invalid_count} invalid")
    return valid_count, invalid_count


def check_for_conflicts():
    """Check if any proposed words conflict with existing words."""
    print("\nCHECKING FOR LEXICAL CONFLICTS")
    print("=" * 50)
    
    all_proposed = [
        # Adjectives
        ("lawhe", "adjective", "smooth"),
        ("miwhe", "adjective", "soft"),
        ("nawhe", "adjective", "warm"),
        ("pawhe", "adjective", "cool"),
        ("rawhe", "adjective", "thick"),
        ("sawhe", "adjective", "thin"),
        ("tawhe", "adjective", "wide"),
        ("wawhe", "adjective", "narrow"),
        ("hiwhe", "adjective", "tall"),
        ("liwhe", "adjective", "short"),
        ("miwha", "adjective", "bright"),
        ("niwha", "adjective", "dark"),
        ("piwha", "adjective", "loud"),
        ("riwha", "adjective", "quiet"),
        ("siwha", "adjective", "fast"),
        ("tiwha", "adjective", "slow"),
        ("wiwha", "adjective", "strong"),
        ("hiwha", "adjective", "weak"),
        ("liwha", "adjective", "heavy"),
        ("miwho", "adjective", "light"),
        ("niwho", "adjective", "dense"),
        ("piwho", "adjective", "loose"),
        ("riwho", "adjective", "tight"),
        ("siwho", "adjective", "flexible"),
        ("tiwho", "adjective", "rigid"),
        ("wiwho", "adjective", "elastic"),
        ("hiwho", "adjective", "brittle"),
        ("liwho", "adjective", "durable"),
        ("miwhi", "adjective", "fresh"),
        ("niwhi", "adjective", "stale"),
        ("piwhi", "adjective", "pure"),
        ("riwhi", "adjective", "mixed"),
        ("siwhi", "adjective", "clean"),
        # Verbs
        ("whale", "verb", "flow"),
        ("whame", "verb", "bend"),
        ("whane", "verb", "twist"),
        ("whape", "verb", "fold"),
        ("whare", "verb", "stretch"),
        ("whase", "verb", "compress"),
        ("whate", "verb", "expand"),
        ("whawe", "verb", "contract"),
        ("whele", "verb", "slide"),
        ("wheme", "verb", "roll"),
        ("whene", "verb", "spin"),
        ("whepe", "verb", "rotate"),
        ("where", "verb", "pivot"),
        ("whese", "verb", "tilt"),
        ("whete", "verb", "balance"),
        ("whewe", "verb", "stabilize"),
        ("while", "verb", "vibrate"),
        ("whime", "verb", "oscillate"),
        ("whine", "verb", "resonate"),
        ("whipe", "verb", "echo"),
        ("whire", "verb", "reflect"),
        ("whise", "verb", "absorb"),
        ("white", "verb", "emit"),
        ("whiwe", "verb", "radiate"),
        ("whole", "verb", "focus"),
        ("whome", "verb", "blur"),
        ("whone", "verb", "clarify"),
        ("whope", "verb", "obscure"),
        ("whore", "verb", "reveal"),
        ("whose", "verb", "conceal"),
        ("whote", "verb", "expose")
    ]
    
    validator = PhiValidator()
    conflict_count = 0
    
    for word, pos, meaning in all_proposed:
        result = validator.validate_word(word, pos, meaning)
        
        # Check for conflicts
        conflicts = [e for e in result["lexical_errors"] 
                    if e.level == ValidationResult.CONFLICT]
        
        if conflicts:
            print(f"❌ {word} ({pos}) conflicts:")
            for conflict in conflicts:
                print(f"   → {conflict.message}")
            conflict_count += 1
    
    if conflict_count == 0:
        print("✅ NO CONFLICTS FOUND - All proposed words are unique!")
    
    return conflict_count


def analyze_fricative_impact():
    """Analyze the fricative distribution impact of adding these words."""
    print("\nFRICATIVE DISTRIBUTION IMPACT ANALYSIS")
    print("=" * 50)
    
    # Current distribution (from deep analysis)
    current = {
        'ph': 361,
        'wh': 133,
        'th': 289,
        'sh': 202
    }
    
    # Proposed additions
    new_wh_adjectives = 33
    new_wh_verbs = 31
    total_new_wh = new_wh_adjectives + new_wh_verbs
    
    # Calculate new distribution
    new_distribution = current.copy()
    new_distribution['wh'] += total_new_wh
    
    total_fricatives = sum(new_distribution.values())
    ideal_per_fricative = total_fricatives / 4
    
    print(f"Current total fricatives: {sum(current.values())}")
    print(f"After adding {total_new_wh} 'wh' words: {total_fricatives}")
    print(f"New ideal per fricative: {ideal_per_fricative:.1f}")
    
    print("\nDistribution comparison:")
    print(f"{'Fricative':<10} {'Current':<8} {'New':<8} {'Ideal':<8} {'Deviation':<12}")
    print("-" * 50)
    
    for fricative in ['ph', 'wh', 'th', 'sh']:
        current_count = current[fricative]
        new_count = new_distribution[fricative]
        deviation = new_count - ideal_per_fricative
        deviation_pct = (deviation / ideal_per_fricative * 100) if ideal_per_fricative > 0 else 0
        
        print(f"{fricative:<10} {current_count:<8} {new_count:<8} {ideal_per_fricative:<8.1f} "
              f"{deviation:+5.1f} ({deviation_pct:+5.1f}%)")
    
    # Calculate balance improvement
    current_deviations = [abs(current[f] - sum(current.values())/4) for f in ['ph', 'wh', 'th', 'sh']]
    new_deviations = [abs(new_distribution[f] - ideal_per_fricative) for f in ['ph', 'wh', 'th', 'sh']]
    
    current_avg_deviation = sum(current_deviations) / 4
    new_avg_deviation = sum(new_deviations) / 4
    
    print(f"\nBalance improvement:")
    print(f"Current average deviation: {current_avg_deviation:.1f}")
    print(f"New average deviation: {new_avg_deviation:.1f}")
    print(f"Improvement: {current_avg_deviation - new_avg_deviation:+.1f}")
    
    if new_avg_deviation < current_avg_deviation:
        print("✅ SIGNIFICANT IMPROVEMENT in fricative balance!")
    else:
        print("❌ No improvement in balance")


def main():
    """Run all validation tests."""
    print("PHI LANGUAGE - NEW WORD VALIDATION")
    print("=" * 60)
    
    # Test adjectives
    adj_valid, adj_invalid = test_proposed_adjectives()
    
    # Test verbs
    verb_valid, verb_invalid = test_proposed_verbs()
    
    # Check conflicts
    conflict_count = check_for_conflicts()
    
    # Analyze impact
    analyze_fricative_impact()
    
    # Summary
    print("\n" + "=" * 60)
    print("VALIDATION SUMMARY")
    print("=" * 60)
    print(f"Adjectives: {adj_valid} valid, {adj_invalid} invalid")
    print(f"Verbs: {verb_valid} valid, {verb_invalid} invalid")
    print(f"Conflicts: {conflict_count}")
    
    total_valid = adj_valid + verb_valid
    total_invalid = adj_invalid + verb_invalid
    
    if total_invalid == 0 and conflict_count == 0:
        print(f"\n✅ ALL {total_valid} PROPOSED WORDS ARE VALID AND CONFLICT-FREE!")
        print("Ready for implementation!")
    else:
        print(f"\n⚠️  Issues found: {total_invalid} invalid words, {conflict_count} conflicts")
        print("Review and fix issues before implementation.")


if __name__ == "__main__":
    main() 