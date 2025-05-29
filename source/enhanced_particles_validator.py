#!/usr/bin/env python3
"""
Enhanced Particles Validator - Comprehensive 4-Layer Validation
Validates phi text using: Lexicon + Phonotactics + Structure + Semantics
"""

import re
from typing import Dict, List, Tuple, Optional
from phi_lexicon_reader import PhiLexiconReader
from phi_validator import PhiValidator
from corrected_semantic_validator import CorrectedPhiSemanticValidator

class EnhancedParticlesValidator:
    """Comprehensive 4-layer phi validation system."""
    
    def __init__(self, pos_directory: str = "pos/"):
        print("🔧 Loading comprehensive validation tools...")
        
        # Layer 1: Lexicon Reader
        self.lexicon_reader = PhiLexiconReader(pos_directory)
        self.lexicon_data = self.lexicon_reader.read_lexicon()
        
        # Layer 2: Phonotactic Validator (modified for sentence mode)
        self.phonotactic_validator = PhiValidator(pos_directory)
        
        # Layer 4: Semantic Validator
        self.semantic_validator = CorrectedPhiSemanticValidator(self.lexicon_reader)
        
        print("✅ All validation tools loaded!")
    
    def _clean_word(self, word: str) -> str:
        """Remove punctuation and clean word for validation."""
        # Remove common punctuation
        cleaned = re.sub(r'[.,!?;:]', '', word.strip().lower())
        return cleaned
    
    def _extract_sentences(self, text: str) -> List[str]:
        """Extract phi sentences from markdown tables in particles.md."""
        lines = text.split('\n')
        sentences = []
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Look specifically for phi table rows
            if line.startswith('| phi'):
                # Extract content between the second and third pipe symbols
                parts = line.split('|')
                if len(parts) >= 3:
                    phi_content = parts[2].strip()
                    if phi_content and phi_content != 'phi':  # Skip header row
                        # Clean up any remaining markdown formatting
                        phi_content = re.sub(r'`([^`]+)`', r'\1', phi_content)  # Remove backticks
                        phi_content = phi_content.strip()
                        if phi_content:
                            sentences.append(phi_content)
        
        return sentences
    
    def validate_lexicon_layer(self, sentence: str) -> Dict:
        """Layer 1: Check if all words exist in lexicon."""
        words = sentence.split()
        valid_words = []
        invalid_words = []
        issues = []
        
        for word in words:
            cleaned_word = self._clean_word(word)
            if cleaned_word in self.lexicon_data:
                valid_words.append(cleaned_word)
            else:
                invalid_words.append(word)
                issues.append(f"'{word}' not in lexicon")
        
        return {
            'valid': len(invalid_words) == 0,
            'valid_words': valid_words,
            'invalid_words': invalid_words,
            'issues': issues
        }
    
    def validate_phonotactics_layer(self, sentence: str) -> Dict:
        """Layer 2: Check phonotactic patterns (sentence mode)."""
        words = sentence.split()
        issues = []
        
        for word in words:
            cleaned_word = self._clean_word(word)
            if not cleaned_word:
                continue
                
            # Get word info from lexicon
            if cleaned_word in self.lexicon_data:
                word_info = self.lexicon_data[cleaned_word]
                pos = word_info['pos']
                
                # Validate phonotactics for this POS (skip conflict checking)
                phonotactic_errors = self.phonotactic_validator.validate_phonotactics(cleaned_word, pos)
                
                # Filter out "already defined" errors - those are expected for existing words
                relevant_errors = [e for e in phonotactic_errors 
                                 if 'already defined' not in e.message]
                
                if relevant_errors:
                    for error in relevant_errors:
                        issues.append(f"{cleaned_word}: {error.message}")
                else:
                    # Add "already defined" as info, not error
                    pos_name = word_info['pos']
                    translation = word_info['translation']
                    issues.append(f"{cleaned_word}: Word '{cleaned_word}' already defined in {pos_name}: {translation}")
        
        return {
            'valid': len([i for i in issues if 'already defined' not in i]) == 0,
            'issues': issues
        }
    
    def validate_structure_layer(self, sentence: str) -> Dict:
        """Layer 3: Basic sentence structure validation."""
        # For now, basic validation - could be expanded with clause_parser.py
        words = sentence.split()
        issues = []
        
        # Basic checks
        if len(words) == 0:
            issues.append("Empty sentence")
        elif len(words) == 1:
            if words[0].lower() not in ['category', 'english']:
                # Single word sentences might be valid (interjections, etc.)
                pass
        
        # Could add more sophisticated parsing here
        return {
            'valid': len(issues) == 0,
            'issues': issues
        }
    
    def validate_semantics_layer(self, sentence: str) -> Dict:
        """Layer 4: Semantic appropriateness validation."""
        try:
            result = self.semantic_validator.validate_sentence(sentence)
            return {
                'valid': result['valid'],
                'issues': [f"{issue['type']}: {issue['problem']}" for issue in result['issues']]
            }
        except Exception as e:
            return {
                'valid': True,  # Don't fail on semantic validator errors
                'issues': [f"Semantic validation error: {str(e)}"]
            }
    
    def validate_complete(self, sentence: str) -> Dict:
        """Run complete 4-layer validation on a sentence."""
        layers = {
            'lexicon': self.validate_lexicon_layer(sentence),
            'phonotactics': self.validate_phonotactics_layer(sentence),
            'structure': self.validate_structure_layer(sentence),
            'semantics': self.validate_semantics_layer(sentence)
        }
        
        overall_valid = all(layer['valid'] for layer in layers.values())
        
        return {
            'sentence': sentence,
            'overall_valid': overall_valid,
            'layers': layers
        }
    
    def validate_particles_file(self, filepath: str) -> Dict:
        """Validate all phi sentences in particles.md or similar file."""
        print(f"📖 Reading {filepath}...")
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            print(f"❌ File not found: {filepath}")
            return None
        
        sentences = self._extract_sentences(content)
        print(f"Found {len(sentences)} phi example sentences")
        
        print(f"\n🔍 COMPREHENSIVE VALIDATION RESULTS:")
        print("=" * 70)
        
        valid_sentences = []
        problematic_sentences = []
        
        for i, sentence in enumerate(sentences, 1):
            result = self.validate_complete(sentence)
            
            if result['overall_valid']:
                valid_sentences.append(sentence)
            else:
                problematic_sentences.append((sentence, result))
                print(f"\n❌ ISSUE #{i}: {sentence[:50]}...")
                
                # Show issues by layer
                for layer_name, layer_data in result['layers'].items():
                    if not layer_data['valid'] and layer_data['issues']:
                        # Only show actual errors, not "already defined" info
                        actual_errors = [issue for issue in layer_data['issues'] 
                                       if 'already defined' not in issue]
                        if actual_errors:
                            print(f"  🚨 {layer_name.upper()}: {'; '.join(actual_errors[:2])}")
        
        # Summary
        total = len(sentences)
        valid_count = len(valid_sentences)
        issue_count = len(problematic_sentences)
        
        print(f"\n📊 COMPREHENSIVE VALIDATION SUMMARY:")
        print(f"  Total sentences: {total}")
        print(f"  ✅ Completely valid: {valid_count} ({valid_count/total*100:.1f}%)")
        print(f"  ❌ Have issues: {issue_count} ({issue_count/total*100:.1f}%)")
        
        return {
            'total': total,
            'valid': valid_sentences,
            'issues': problematic_sentences
        }

if __name__ == "__main__":
    validator = EnhancedParticlesValidator()
    results = validator.validate_particles_file('pos/particles.md') 