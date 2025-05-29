#!/usr/bin/env python3
"""
Comprehensive Particles Validation - Standard Workflow
Validates all Phi words in particles.md using 4-layer validation:
- Layer 1: Lexicon existence (phi_lexicon_reader.py)
- Layer 2: Phonotactic patterns (phi_validator.py)  
- Layer 3: Sentence structure (clause_parser.py)
- Layer 4: Semantic appropriateness (corrected_semantic_validator.py)
"""

import re
from enhanced_particles_validator import EnhancedParticlesValidator

def main():
    """Run comprehensive 4-layer validation on particles.md as standard workflow."""
    print("🔧 PHI PARTICLES COMPREHENSIVE VALIDATION")
    print("=" * 60)
    print("Standard 4-layer validation workflow:")
    print("  Layer 1: Lexicon existence checking")
    print("  Layer 2: Phonotactic pattern validation")
    print("  Layer 3: Sentence structure parsing")
    print("  Layer 4: Semantic appropriateness checking")
    print()
    
    # Initialize the comprehensive validator
    validator = EnhancedParticlesValidator()
    
    # Run full validation on particles.md
    results = validator.validate_particles_file('pos/particles.md')
    
    if results:
        # Additional analysis
        total = results['total']
        valid_count = len(results['valid'])
        issue_count = len(results['issues'])
        
        print(f"\n🎯 DETAILED ANALYSIS:")
        print(f"  📊 Overall success rate: {valid_count/total*100:.1f}%")
        
        # Show breakdown by validation layer
        layer_stats = {'lexicon': 0, 'phonotactics': 0, 'structure': 0, 'semantics': 0}
        for sentence, result in results['issues']:
            for layer, data in result['layers'].items():
                if not data['valid']:
                    layer_stats[layer] += 1
        
        print(f"\n📋 Issues by validation layer:")
        for layer, count in layer_stats.items():
            if count > 0:
                percentage = count/issue_count*100 if issue_count > 0 else 0
                print(f"  {layer.upper():<12}: {count:3} sentences ({percentage:5.1f}% of issues)")
        
        # Show some examples of valid sentences
        if results['valid']:
            print(f"\n✅ EXAMPLES OF VALID SENTENCES:")
            for i, sentence in enumerate(results['valid'][:5], 1):
                print(f"  {i}. {sentence}")
            if len(results['valid']) > 5:
                print(f"     ... and {len(results['valid'])-5} more valid sentences")
        
        # Show some examples of problematic sentences
        if results['issues']:
            print(f"\n❌ EXAMPLES OF PROBLEMATIC SENTENCES:")
            for i, (sentence, result) in enumerate(results['issues'][:3], 1):
                print(f"  {i}. {sentence[:50]}...")
                issue_types = [layer for layer, data in result['layers'].items() if not data['valid']]
                print(f"     Issues: {', '.join(issue_types)}")
            if len(results['issues']) > 3:
                print(f"     ... and {len(results['issues'])-3} more problematic sentences")
        
        print(f"\n📈 RECOMMENDATIONS:")
        if layer_stats['lexicon'] > 0:
            print(f"  🔤 Lexicon: Fix {layer_stats['lexicon']} invalid words")
        if layer_stats['semantics'] > 0:
            print(f"  🧠 Semantics: Address {layer_stats['semantics']} POS/context misuse issues")
        if layer_stats['phonotactics'] > 0:
            print(f"  🔤 Phonotactics: Review {layer_stats['phonotactics']} pattern violations")
        if layer_stats['structure'] > 0:
            print(f"  🏗️  Structure: Fix {layer_stats['structure']} sentence structure issues")
        
        if valid_count == total:
            print(f"  🎉 Perfect! All sentences pass comprehensive validation!")
        elif valid_count/total >= 0.9:
            print(f"  🌟 Excellent! Over 90% validation success rate.")
        elif valid_count/total >= 0.8:
            print(f"  👍 Good! Over 80% validation success rate.")
        else:
            print(f"  📝 Needs work. Focus on the most common issue types above.")

if __name__ == "__main__":
    main() 