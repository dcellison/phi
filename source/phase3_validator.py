#!/usr/bin/env python3
"""
Phase 3 Conversion Validator

Validates the suggested 'ph' → 'wh' and 'th' → 'wh' conversions to ensure no conflicts
with existing words and maintains phonotactic patterns.
"""

import sys
from pathlib import Path

# Add the current directory to path to import phi_validator
sys.path.append(str(Path(__file__).parent))

from phi_validator import PhiValidator, ValidationResult


class Phase3Validator:
    """Validates Phase 3 conversion suggestions."""
    
    def __init__(self):
        self.validator = PhiValidator()
        
        # Phase 3 conversion suggestions from analysis
        self.ph_to_wh_conversions = [
            {'original': 'liphia', 'new': 'liwhia', 'meaning': 'belief', 'pos': 'noun'},
            {'original': 'phemo', 'new': 'whemo', 'meaning': 'think', 'pos': 'verb'},
            {'original': 'phire', 'new': 'whire', 'meaning': 'want', 'pos': 'verb'},
            {'original': 'phema', 'new': 'whema', 'meaning': 'come', 'pos': 'verb'},
            {'original': 'phite', 'new': 'white', 'meaning': 'stay', 'pos': 'verb'},
            {'original': 'phiwo', 'new': 'whiwo', 'meaning': 'befriend', 'pos': 'verb'},
            {'original': 'photo', 'new': 'whoto', 'meaning': 'need', 'pos': 'verb'},
            {'original': 'phopu', 'new': 'whopu', 'meaning': 'play ball', 'pos': 'verb'},
            {'original': 'pheme', 'new': 'wheme', 'meaning': 'teach', 'pos': 'verb'},
            {'original': 'phuri', 'new': 'whuri', 'meaning': 'work', 'pos': 'verb'},
            {'original': 'wuphi', 'new': 'wuwhi', 'meaning': 'amber', 'pos': 'adjective'},
            {'original': 'pephe', 'new': 'pewhe', 'meaning': 'indigo', 'pos': 'adjective'},
            {'original': 'lopha', 'new': 'lowha', 'meaning': 'bent/curved', 'pos': 'adjective'},
            {'original': 'mipha', 'new': 'miwha', 'meaning': 'beautiful', 'pos': 'adjective'},
            {'original': 'tepha', 'new': 'tewha', 'meaning': 'intelligent', 'pos': 'adjective'},
            {'original': 'phelu', 'new': 'whelu', 'meaning': 'read aloud', 'pos': 'verb'},
            {'original': 'phawi', 'new': 'whawi', 'meaning': 'fly', 'pos': 'verb'},
            {'original': 'phuwe', 'new': 'whuwe', 'meaning': 'sleep', 'pos': 'verb'},
            {'original': 'phari', 'new': 'whari', 'meaning': 'sing', 'pos': 'verb'},
            {'original': 'phoa', 'new': 'whoa', 'meaning': 'beside', 'pos': 'preposition'},
            {'original': 'phoe', 'new': 'whoe', 'meaning': 'ago', 'pos': 'preposition'},
            {'original': 'phea', 'new': 'whea', 'meaning': 'besides', 'pos': 'preposition'},
            {'original': 'phio', 'new': 'whio', 'meaning': 'unlike', 'pos': 'preposition'},
            {'original': 'taphe', 'new': 'tawhe', 'meaning': 'surprised', 'pos': 'adjective'},
            {'original': 'phithui', 'new': 'whithui', 'meaning': 'lagoon', 'pos': 'noun'},
            {'original': 'phethoa', 'new': 'whethoa', 'meaning': 'vegetable', 'pos': 'noun'},
            {'original': 'phiphui', 'new': 'whiwhui', 'meaning': 'bee', 'pos': 'noun'},
            {'original': 'shephoa', 'new': 'shewhoa', 'meaning': 'sheep/goat', 'pos': 'noun'},
            {'original': 'thiphai', 'new': 'thiwhai', 'meaning': 'heart', 'pos': 'noun'},
            {'original': 'niphea', 'new': 'niwhea', 'meaning': 'needle', 'pos': 'noun'},
            {'original': 'phethie', 'new': 'whethie', 'meaning': 'room (enclosed)', 'pos': 'noun'},
            {'original': 'mipheo', 'new': 'miwheo', 'meaning': 'beauty', 'pos': 'noun'},
            {'original': 'shuphoa', 'new': 'shuwhoa', 'meaning': 'purpose/goal', 'pos': 'noun'},
            {'original': 'wuphia', 'new': 'wuwhia', 'meaning': 'amber', 'pos': 'noun'},
            {'original': 'nuphea', 'new': 'nuwhea', 'meaning': 'timber', 'pos': 'noun'},
            {'original': 'phahi', 'new': 'whahi', 'meaning': 'become', 'pos': 'verb'},
            {'original': 'phaiphea', 'new': 'whaiwhea', 'meaning': 'butterfly', 'pos': 'noun'},
            {'original': 'liphoa', 'new': 'liwhoa', 'meaning': 'fly', 'pos': 'noun'},
            {'original': 'nophai', 'new': 'nowhai', 'meaning': 'bread', 'pos': 'noun'},
            {'original': 'saiphoa', 'new': 'saiwhoa', 'meaning': 'meat', 'pos': 'noun'},
            {'original': 'phithoa', 'new': 'whithoa', 'meaning': 'death', 'pos': 'noun'},
            {'original': 'mophea', 'new': 'mowhea', 'meaning': 'heat', 'pos': 'noun'},
            {'original': 'thiphao', 'new': 'thiwhao', 'meaning': 'dance', 'pos': 'noun'},
            {'original': 'phemi', 'new': 'whemi', 'meaning': 'speak', 'pos': 'verb'},
            {'original': 'phumo', 'new': 'whumo', 'meaning': 'translate', 'pos': 'verb'},
        ]
        
        self.th_to_wh_conversions = [
            {'original': 'thisa', 'new': 'whisa', 'meaning': 'ask', 'pos': 'verb'},
            {'original': 'thomo', 'new': 'whomo', 'meaning': 'like', 'pos': 'verb'},
            {'original': 'thuni', 'new': 'whuni', 'meaning': 'have/possess', 'pos': 'verb'},
            {'original': 'thuno', 'new': 'whuno', 'meaning': 'break', 'pos': 'verb'},
            {'original': 'thusa', 'new': 'whusa', 'meaning': 'close', 'pos': 'verb'},
            {'original': 'thepa', 'new': 'whepa', 'meaning': 'fix/repair', 'pos': 'verb'},
            {'original': 'thuro', 'new': 'whuro', 'meaning': 'hide', 'pos': 'verb'},
            {'original': 'thora', 'new': 'whora', 'meaning': 'open', 'pos': 'verb'},
            {'original': 'thiwo', 'new': 'whiwo', 'meaning': 'give', 'pos': 'verb'},
            {'original': 'thonu', 'new': 'whonu', 'meaning': 'lose', 'pos': 'verb'},
            {'original': 'theta', 'new': 'wheta', 'meaning': 'continue', 'pos': 'verb'},
            {'original': 'thawu', 'new': 'whawu', 'meaning': 'do', 'pos': 'verb'},
            {'original': 'thuli', 'new': 'whuli', 'meaning': 'finish/complete', 'pos': 'verb'},
            {'original': 'rothe', 'new': 'rowhe', 'meaning': 'like (similar)', 'pos': 'adjective'},
            {'original': 'thupi', 'new': 'whupi', 'meaning': 'read silently', 'pos': 'verb'},
            {'original': 'thepi', 'new': 'whepi', 'meaning': 'jump', 'pos': 'verb'},
            {'original': 'thumi', 'new': 'whumi', 'meaning': 'run', 'pos': 'verb'},
        ]
    
    def validate_all_conversions(self):
        """Validate all Phase 3 conversion suggestions."""
        print("PHASE 3 CONVERSION VALIDATION")
        print("=" * 50)
        
        all_conversions = self.ph_to_wh_conversions + self.th_to_wh_conversions
        
        valid_conversions = []
        conflicts = []
        pattern_errors = []
        
        print(f"Validating {len(all_conversions)} conversion suggestions...")
        print()
        
        for conversion in all_conversions:
            original = conversion['original']
            new_word = conversion['new']
            meaning = conversion['meaning']
            pos = conversion['pos']
            
            # Validate the new word
            result = self.validator.validate_word(new_word, pos, meaning)
            
            if result["overall_status"] == ValidationResult.VALID:
                valid_conversions.append(conversion)
                print(f"✅ {original} → {new_word} ({meaning}) - VALID")
            elif result["overall_status"] == ValidationResult.CONFLICT:
                conflicts.append({
                    'conversion': conversion,
                    'conflicts': result["lexical_errors"]
                })
                print(f"❌ {original} → {new_word} ({meaning}) - CONFLICT")
                for error in result["lexical_errors"]:
                    print(f"   → {error.message}")
            else:
                pattern_errors.append({
                    'conversion': conversion,
                    'errors': result["phonotactic_errors"]
                })
                print(f"❌ {original} → {new_word} ({meaning}) - PATTERN ERROR")
                for error in result["phonotactic_errors"]:
                    print(f"   → {error.message}")
        
        print(f"\nVALIDATION SUMMARY:")
        print(f"Valid conversions: {len(valid_conversions)}")
        print(f"Conflicts: {len(conflicts)}")
        print(f"Pattern errors: {len(pattern_errors)}")
        
        return {
            'valid': valid_conversions,
            'conflicts': conflicts,
            'pattern_errors': pattern_errors
        }
    
    def resolve_conflicts(self, conflicts):
        """Suggest alternative conversions for conflicted words."""
        print(f"\nCONFLICT RESOLUTION")
        print("=" * 50)
        
        resolved_conversions = []
        unresolvable = []
        
        for conflict_data in conflicts:
            conversion = conflict_data['conversion']
            original = conversion['original']
            meaning = conversion['meaning']
            pos = conversion['pos']
            
            print(f"\nResolving conflict for: {original} ({meaning})")
            
            # For ph words, try sh as alternative to wh
            # For th words, try sh as alternative to wh
            if 'ph' in original:
                alt_word = original.replace('ph', 'sh')
                alt_fricative = 'sh'
            elif 'th' in original:
                alt_word = original.replace('th', 'sh')
                alt_fricative = 'sh'
            else:
                print(f"  ⚠️  Unknown fricative pattern in {original}")
                unresolvable.append(conversion)
                continue
            
            # Validate alternative
            result = self.validator.validate_word(alt_word, pos, meaning)
            
            if result["overall_status"] == ValidationResult.VALID:
                resolved_conversion = {
                    'original': original,
                    'new': alt_word,
                    'meaning': meaning,
                    'pos': pos,
                    'fricative': alt_fricative
                }
                resolved_conversions.append(resolved_conversion)
                print(f"  ✅ Alternative: {original} → {alt_word} (using {alt_fricative})")
            else:
                print(f"  ❌ {alt_word} also conflicts")
                unresolvable.append(conversion)
        
        print(f"\nResolution summary:")
        print(f"  Resolved with alternatives: {len(resolved_conversions)}")
        print(f"  Unresolvable conflicts: {len(unresolvable)}")
        
        return resolved_conversions, unresolvable
    
    def finalize_conversion_list(self):
        """Create the final validated conversion list."""
        print(f"\nFINALIZING PHASE 3 CONVERSION LIST")
        print("=" * 50)
        
        validation_results = self.validate_all_conversions()
        resolved_conversions, unresolvable = self.resolve_conflicts(validation_results['conflicts'])
        
        # Combine valid conversions with resolved conflicts
        final_conversions = validation_results['valid'] + resolved_conversions
        
        # Sort by conversion type and original word
        final_conversions.sort(key=lambda x: (x.get('fricative', 'wh'), x['original']))
        
        print(f"\nFINAL PHASE 3 CONVERSION LIST ({len(final_conversions)} words):")
        print("-" * 50)
        
        # Group by target fricative
        by_target = {'wh': [], 'sh': []}
        for conversion in final_conversions:
            target = conversion.get('fricative', 'wh')
            by_target[target].append(conversion)
        
        for target_fricative, conversions in by_target.items():
            if not conversions:
                continue
                
            print(f"\nConversions to '{target_fricative}' ({len(conversions)} words):")
            for conversion in conversions:
                source_fricative = 'ph' if 'ph' in conversion['original'] else 'th'
                print(f"  {conversion['original']:<12} → {conversion['new']:<12} "
                      f"({conversion['meaning']}) [{conversion['pos']}] "
                      f"[{source_fricative}→{target_fricative}]")
        
        # Calculate fricative distribution impact
        wh_additions = len(by_target['wh'])
        sh_additions = len(by_target['sh'])
        ph_reductions = len([c for c in final_conversions if 'ph' in c['original']])
        th_reductions = len([c for c in final_conversions if 'th' in c['original']])
        
        print(f"\nFRICATIVE DISTRIBUTION IMPACT:")
        print(f"  ph reductions: -{ph_reductions} words")
        print(f"  th reductions: -{th_reductions} words")
        print(f"  wh additions: +{wh_additions} words")
        print(f"  sh additions: +{sh_additions} words")
        print(f"  Total conversions: {len(final_conversions)} words")
        
        # Show unresolvable conflicts
        if unresolvable:
            print(f"\nUNRESOLVABLE CONFLICTS ({len(unresolvable)} words):")
            for conversion in unresolvable:
                print(f"  {conversion['original']} ({conversion['meaning']}) - "
                      f"no valid alternative found")
        
        return final_conversions, unresolvable


def main():
    """Main function to run Phase 3 validation."""
    validator = Phase3Validator()
    final_conversions, unresolvable = validator.finalize_conversion_list()
    
    print(f"\n" + "="*50)
    print("PHASE 3 VALIDATION COMPLETE")
    print("="*50)
    print(f"Ready to implement {len(final_conversions)} validated conversions!")
    
    if unresolvable:
        print(f"Note: {len(unresolvable)} conversions could not be resolved due to conflicts.")


if __name__ == "__main__":
    main() 