#!/usr/bin/env python3
"""
Phase 2 Replacement Validator

Validates the suggested 'ph' → 'sh'/'th' replacements to ensure no conflicts
with existing words and refines the replacement list.
"""

import sys
from pathlib import Path

# Add the current directory to path to import phi_validator
sys.path.append(str(Path(__file__).parent))

from phi_validator import PhiValidator, ValidationResult


class Phase2Validator:
    """Validates Phase 2 replacement suggestions."""
    
    def __init__(self):
        self.validator = PhiValidator()
        
        # Suggested replacements from Phase 2 analysis
        self.suggested_replacements = [
            {'original': 'papho', 'new': 'pasho', 'meaning': 'fragrant', 'pos': 'adjective'},
            {'original': 'nipha', 'new': 'nisha', 'meaning': 'light (weight)', 'pos': 'adjective'},
            {'original': 'rupha', 'new': 'rusha', 'meaning': 'rough', 'pos': 'adjective'},
            {'original': 'phithai', 'new': 'shithai', 'meaning': 'sunlight', 'pos': 'noun'},
            {'original': 'laphui', 'new': 'lashui', 'meaning': 'mistake/error', 'pos': 'noun'},
            {'original': 'phishui', 'new': 'shishui', 'meaning': 'softness', 'pos': 'noun'},
            {'original': 'phero', 'new': 'shero', 'meaning': 'carry', 'pos': 'verb'},
            {'original': 'phuma', 'new': 'shuma', 'meaning': 'push', 'pos': 'verb'},
            {'original': 'phete', 'new': 'shete', 'meaning': 'put', 'pos': 'verb'},
            {'original': 'phesi', 'new': 'shesi', 'meaning': 'set', 'pos': 'verb'},
            {'original': 'phuwa', 'new': 'shuwa', 'meaning': 'throw', 'pos': 'verb'},
            {'original': 'phoru', 'new': 'shoru', 'meaning': 'set fire', 'pos': 'verb'},
            {'original': 'phimo', 'new': 'shimo', 'meaning': 'allow', 'pos': 'verb'},
            {'original': 'phasi', 'new': 'shasi', 'meaning': 'hold', 'pos': 'verb'},
            {'original': 'phimi', 'new': 'shimi', 'meaning': 'let', 'pos': 'verb'},
            {'original': 'phuwo', 'new': 'shuwo', 'meaning': 'offer', 'pos': 'verb'},
            {'original': 'phiwe', 'new': 'shiwe', 'meaning': 'pull', 'pos': 'verb'},
            {'original': 'phate', 'new': 'shate', 'meaning': 'share', 'pos': 'verb'},
            {'original': 'phita', 'new': 'shita', 'meaning': 'take', 'pos': 'verb'},
            {'original': 'phisa', 'new': 'shisa', 'meaning': 'air out', 'pos': 'verb'},
            {'original': 'phure', 'new': 'shure', 'meaning': 'bring', 'pos': 'verb'},
            {'original': 'pheta', 'new': 'sheta', 'meaning': 'start', 'pos': 'verb'},
            {'original': 'phena', 'new': 'shena', 'meaning': 'try', 'pos': 'verb'},
            {'original': 'pheso', 'new': 'sheso', 'meaning': 'wait', 'pos': 'verb'},
            {'original': 'phau', 'new': 'shau', 'meaning': 'through', 'pos': 'preposition'},
            {'original': 'tiphi', 'new': 'tishi', 'meaning': 'animal-like', 'pos': 'adjective'},
            {'original': 'nupha', 'new': 'nusha', 'meaning': 'reported/hearsay', 'pos': 'adjective'},
            {'original': 'sheophei', 'new': 'sheoshei', 'meaning': 'meadow', 'pos': 'noun'},
            {'original': 'phiphai', 'new': 'shishai', 'meaning': 'heart', 'pos': 'noun'},
            {'original': 'shophai', 'new': 'shoshai', 'meaning': 'door', 'pos': 'noun'},
            {'original': 'thaphui', 'new': 'thashui', 'meaning': 'doubt', 'pos': 'noun'},
            {'original': 'phithao', 'new': 'shithao', 'meaning': 'freedom', 'pos': 'noun'},
            {'original': 'lephui', 'new': 'leshui', 'meaning': 'wisdom', 'pos': 'noun'},
            {'original': 'phata', 'new': 'shata', 'meaning': 'answer/reply', 'pos': 'verb'},
            {'original': 'phare', 'new': 'share', 'meaning': 'report', 'pos': 'verb'},
            {'original': 'phewu', 'new': 'shewu', 'meaning': 'compose', 'pos': 'verb'},
            {'original': 'phiso', 'new': 'shiso', 'meaning': 'decide', 'pos': 'verb'},
            {'original': 'phime', 'new': 'shime', 'meaning': 'forget', 'pos': 'verb'},
            {'original': 'phomo', 'new': 'shomo', 'meaning': 'like', 'pos': 'verb'},
            {'original': 'pharu', 'new': 'sharu', 'meaning': 'appear', 'pos': 'verb'},
            {'original': 'phali', 'new': 'shali', 'meaning': 'fall', 'pos': 'verb'},
            {'original': 'phewi', 'new': 'shewi', 'meaning': 'leave', 'pos': 'verb'},
            {'original': 'phola', 'new': 'shola', 'meaning': 'walk', 'pos': 'verb'},
            {'original': 'phetu', 'new': 'shetu', 'meaning': 'exit', 'pos': 'verb'},
            {'original': 'phuni', 'new': 'shuni', 'meaning': 'build', 'pos': 'verb'},
            {'original': 'phesa', 'new': 'shesa', 'meaning': 'create', 'pos': 'verb'},
            {'original': 'phoro', 'new': 'shoro', 'meaning': 'destroy', 'pos': 'verb'},
            {'original': 'phiho', 'new': 'shiho', 'meaning': 'buy', 'pos': 'verb'},
            {'original': 'phume', 'new': 'shume', 'meaning': 'return', 'pos': 'verb'},
            {'original': 'phele', 'new': 'shele', 'meaning': 'send', 'pos': 'verb'},
            {'original': 'phusa', 'new': 'shusa', 'meaning': 'hear', 'pos': 'verb'},
            {'original': 'phose', 'new': 'shose', 'meaning': 'see', 'pos': 'verb'},
            {'original': 'phusi', 'new': 'shusi', 'meaning': 'taste', 'pos': 'verb'},
            {'original': 'phosa', 'new': 'shosa', 'meaning': 'watch', 'pos': 'verb'},
            {'original': 'phawu', 'new': 'shawu', 'meaning': 'do', 'pos': 'verb'},
            {'original': 'phota', 'new': 'shota', 'meaning': 'document', 'pos': 'verb'},
            {'original': 'phio', 'new': 'shio', 'meaning': 'unlike', 'pos': 'preposition'},
        ]
    
    def validate_replacements(self):
        """Validate all suggested replacements for conflicts."""
        print("PHASE 2 REPLACEMENT VALIDATION")
        print("=" * 50)
        
        valid_replacements = []
        conflicts = []
        pattern_errors = []
        
        for replacement in self.suggested_replacements:
            original = replacement['original']
            new_word = replacement['new']
            meaning = replacement['meaning']
            pos = replacement['pos']
            
            # Validate the new word
            result = self.validator.validate_word(new_word, pos, meaning)
            
            if result["overall_status"] == ValidationResult.VALID:
                valid_replacements.append(replacement)
                print(f"✅ {original} → {new_word} ({meaning}) - VALID")
            elif result["overall_status"] == ValidationResult.CONFLICT:
                conflicts.append({
                    'replacement': replacement,
                    'conflicts': result["lexical_errors"]
                })
                print(f"❌ {original} → {new_word} ({meaning}) - CONFLICT")
                for error in result["lexical_errors"]:
                    print(f"   → {error.message}")
            else:
                pattern_errors.append({
                    'replacement': replacement,
                    'errors': result["phonotactic_errors"]
                })
                print(f"❌ {original} → {new_word} ({meaning}) - PATTERN ERROR")
                for error in result["phonotactic_errors"]:
                    print(f"   → {error.message}")
        
        print(f"\nVALIDATION SUMMARY:")
        print(f"Valid replacements: {len(valid_replacements)}")
        print(f"Conflicts: {len(conflicts)}")
        print(f"Pattern errors: {len(pattern_errors)}")
        
        return {
            'valid': valid_replacements,
            'conflicts': conflicts,
            'pattern_errors': pattern_errors
        }
    
    def resolve_conflicts(self, conflicts):
        """Suggest alternative replacements for conflicted words."""
        print(f"\nCONFLICT RESOLUTION")
        print("=" * 50)
        
        resolved_replacements = []
        
        for conflict_data in conflicts:
            replacement = conflict_data['replacement']
            original = replacement['original']
            meaning = replacement['meaning']
            pos = replacement['pos']
            
            print(f"\nResolving conflict for: {original} ({meaning})")
            
            # Try alternative fricatives
            alternatives = ['th', 'wh']  # Try th and wh as alternatives to sh
            
            for alt_fricative in alternatives:
                alt_word = original.replace('ph', alt_fricative)
                
                # Validate alternative
                result = self.validator.validate_word(alt_word, pos, meaning)
                
                if result["overall_status"] == ValidationResult.VALID:
                    resolved_replacement = {
                        'original': original,
                        'new': alt_word,
                        'meaning': meaning,
                        'pos': pos,
                        'fricative': alt_fricative
                    }
                    resolved_replacements.append(resolved_replacement)
                    print(f"  ✅ Alternative: {original} → {alt_word} (using {alt_fricative})")
                    break
                else:
                    print(f"  ❌ {alt_word} also conflicts")
            else:
                print(f"  ⚠️  No valid alternative found for {original}")
        
        return resolved_replacements
    
    def finalize_replacement_list(self):
        """Create the final validated replacement list."""
        print(f"\nFINALIZING REPLACEMENT LIST")
        print("=" * 50)
        
        validation_results = self.validate_replacements()
        resolved_conflicts = self.resolve_conflicts(validation_results['conflicts'])
        
        # Combine valid replacements with resolved conflicts
        final_replacements = validation_results['valid'] + resolved_conflicts
        
        # Sort by POS for organized implementation
        final_replacements.sort(key=lambda x: (x['pos'], x['original']))
        
        print(f"\nFINAL REPLACEMENT LIST ({len(final_replacements)} words):")
        print("-" * 50)
        
        by_pos = {}
        for replacement in final_replacements:
            pos = replacement['pos']
            if pos not in by_pos:
                by_pos[pos] = []
            by_pos[pos].append(replacement)
        
        for pos, replacements in by_pos.items():
            print(f"\n{pos.upper()} ({len(replacements)} replacements):")
            for replacement in replacements:
                fricative = replacement.get('fricative', 'sh')
                print(f"  {replacement['original']:<12} → {replacement['new']:<12} "
                      f"({replacement['meaning']}) [{fricative}]")
        
        # Calculate fricative distribution impact
        sh_count = sum(1 for r in final_replacements if r.get('fricative', 'sh') == 'sh')
        th_count = sum(1 for r in final_replacements if r.get('fricative', 'sh') == 'th')
        wh_count = sum(1 for r in final_replacements if r.get('fricative', 'sh') == 'wh')
        
        print(f"\nFRICATIVE DISTRIBUTION IMPACT:")
        print(f"  ph → sh: {sh_count} words")
        print(f"  ph → th: {th_count} words") 
        print(f"  ph → wh: {wh_count} words")
        print(f"  Total ph reduction: {len(final_replacements)} words")
        
        return final_replacements


def main():
    """Main function to run Phase 2 validation."""
    validator = Phase2Validator()
    final_replacements = validator.finalize_replacement_list()
    
    print(f"\n" + "="*50)
    print("PHASE 2 VALIDATION COMPLETE")
    print("="*50)
    print(f"Ready to implement {len(final_replacements)} validated replacements!")


if __name__ == "__main__":
    main() 