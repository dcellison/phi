#!/usr/bin/env python3
"""
Corrected Semantic Validator for Phi
Catches both lexicon errors AND POS category violations.
"""

import re
from phi_lexicon_reader import PhiLexiconReader

class CorrectedPhiSemanticValidator:
    """Enhanced validator that catches lexicon + semantic errors."""
    
    def __init__(self, lexicon_reader):
        self.lexicon = lexicon_reader.lexicon
        self.reader = lexicon_reader
    
    def _clean_word(self, word: str) -> str:
        """Remove punctuation and clean word for validation."""
        # Remove common punctuation
        cleaned = re.sub(r'[.,!?;:\[\]]', '', word.strip().lower())
        return cleaned
    
    def validate_sentence(self, sentence: str) -> dict:
        """Comprehensive validation: lexicon + semantics."""
        words = sentence.strip().split()
        issues = []
        
        # Check each word pair for both lexicon and semantic issues
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            
            # Clean words for lexicon lookup
            clean_word1 = self._clean_word(word1)
            clean_word2 = self._clean_word(word2)
            
            # Skip empty words or English labels
            if not clean_word1 or not clean_word2:
                continue
            if clean_word1 in ['category', 'english'] or clean_word2 in ['category', 'english']:
                continue
            
            # First check lexicon existence
            info1 = self.lexicon.get(clean_word1.lower())
            info2 = self.lexicon.get(clean_word2.lower())
            
            if not info1:
                issues.append({
                    'type': 'lexicon_error',
                    'word': word1,
                    'problem': f"'{word1}' not found in lexicon",
                    'suggestion': "Check spelling or use existing word"
                })
                continue  # Can't do semantic analysis if word doesn't exist
                
            if not info2:
                issues.append({
                    'type': 'lexicon_error', 
                    'word': word2,
                    'problem': f"'{word2}' not found in lexicon",
                    'suggestion': "Check spelling or use existing word"
                })
                continue  # Can't do semantic analysis if word doesn't exist
            
            # Now check semantic appropriateness
            pos1, pos2 = info1['pos'], info2['pos']
            trans1, trans2 = info1['translation'], info2['translation']
            
            # Check for pronoun misused as determiner
            if (pos1 == 'pronoun' and pos2 == 'noun' and 
                self._looks_like_determiner_context(clean_word1, clean_word2, sentence, trans1)):
                issues.append({
                    'type': 'pronoun_as_determiner',
                    'words': [word1, word2],
                    'problem': f"'{word1}' is pronoun ('{trans1}') used where determiner expected",
                    'suggestion': f"Use determiner like 'phiato' (this) instead of pronoun '{word1}' ({trans1})"
                })
            
            # Check for non-adjective after comparison particles
            if (clean_word1 in ['mo', 'pa', 'sa', 'le', 're'] and pos2 != 'adjective'):
                issues.append({
                    'type': 'non_adjective_after_comparison',
                    'words': [word1, word2],
                    'problem': f"Comparison particle '{word1}' followed by {pos2} '{word2}' ({trans2})",
                    'suggestion': f"Use adjective after comparison particle '{word1}'"
                })
        
        return {
            'sentence': sentence,
            'valid': len(issues) == 0,
            'issues': issues
        }
    
    def _looks_like_determiner_context(self, word1: str, word2: str, sentence: str, translation: str) -> bool:
        """Detect if this looks like determiner + noun context."""
        # Strong indicators this should be a determiner
        indicators = [
            'you' in translation.lower(),  # "you" being used as "this" 
            word1 in ['thi', 'tha', 'tho'],  # Common pronoun/determiner confusions
            sentence.strip().startswith(word1 + ' ' + word2),  # Sentence-initial position
            any(det in sentence for det in ['this', 'that'])  # English gloss suggests determiner
        ]
        return any(indicators)
    
    def suggest_correction(self, word: str) -> list:
        """Suggest corrections for problematic words."""
        suggestions = []
        
        clean_word = self._clean_word(word)
        info = self.lexicon.get(clean_word.lower())
        if not info:
            # Word doesn't exist - can't suggest semantic correction
            return [f"'{word}' not in lexicon - check spelling"]
        
        # Check for common POS confusions
        if info['pos'] == 'pronoun' and 'you' in info['translation'].lower():
            # Pronoun "you" likely should be determiner "this"
            determiners = self.reader.get_words_by_pos('determiner')
            this_words = [w for w in determiners if 'this' in self.lexicon[w]['translation'].lower()]
            suggestions.extend([f"Use '{w}' (this) instead of '{word}' (you)" for w in this_words])
        
        return suggestions

def demo_enhanced_validation():
    """Demo showing how enhanced validator catches multiple error types."""
    print("🔧 LOADING ENHANCED VALIDATOR...")
    reader = PhiLexiconReader('pos/')
    lexicon = reader.read_lexicon()
    validator = CorrectedPhiSemanticValidator(reader)
    
    test_cases = [
        # Correct examples
        "phiato phuthui phera pa pisha",  # this blanket is most soft
        "mia li whuwa",                   # I threw
        
        # Error examples  
        "thi phelui phera pa pisha",      # ERROR: pronoun + non-existent word
        "thi nuthui",                     # ERROR: pronoun used as determiner
        "pa thephoa",                     # ERROR: comparison + noun (not adjective)
        "mo whuwa",                       # ERROR: comparison + verb (not adjective)
    ]
    
    print(f"\n🔍 ENHANCED SEMANTIC VALIDATION DEMO:")
    print("=" * 60)
    
    for case in test_cases:
        result = validator.validate_sentence(case)
        status = "✅ VALID" if result['valid'] else "❌ INVALID"
        print(f"\n{status}: {case}")
        
        for issue in result['issues']:
            print(f"  🚨 {issue['type'].upper()}: {issue['problem']}")
            print(f"     💡 {issue['suggestion']}")
    
    # Show the corrected version
    print(f"\n✅ CORRECTED EXAMPLES:")
    print("❌ Wrong: thi phelui phera pa pisha na lo phelui")
    print("✅ Right: phiato phuthui phera pa pisha na lo phuthui")
    print("          (this blanket is most soft OBJ PL blanket)")

if __name__ == "__main__":
    demo_enhanced_validation() 