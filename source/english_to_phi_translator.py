#!/usr/bin/env python3
"""
English to Phi Translator with Validation

Translates English sentences to Phi using:
- Semantic analysis of English input
- Phi vocabulary mapping
- SOV structure conversion
- Iterative validation and refinement
- Multiple translation options
"""

import sys
import re
from pathlib import Path
from typing import List, Dict, Tuple, Optional, Set
from dataclasses import dataclass
from enum import Enum

# Add the current directory to path to import phi_validator
sys.path.append(str(Path(__file__).parent))

from phi_sentence_validator import PhiSentenceValidator


class TranslationStrategy(Enum):
    """Different approaches to translation."""
    LITERAL = "literal"           # Word-for-word translation
    SEMANTIC = "semantic"         # Meaning-based translation
    CONTEXTUAL = "contextual"     # Context-aware translation
    POETIC = "poetic"            # Literary/artistic translation


@dataclass
class EnglishAnalysis:
    """Analysis of English sentence structure."""
    words: List[str]
    pos_tags: List[str]
    subject: Optional[str]
    verb: Optional[str]
    object: Optional[str]
    modifiers: List[str]
    tense: str
    question_type: Optional[str]
    is_negative: bool
    is_passive: bool
    subordinate_clauses: List[Dict]


@dataclass
class PhiTranslation:
    """A Phi translation with metadata."""
    phi_sentence: str
    confidence: float
    strategy: TranslationStrategy
    validation_errors: List[str]
    is_valid: bool
    alternatives: List[str]


class EnglishToPhiTranslator:
    """Translates English sentences to grammatically correct Phi."""
    
    def __init__(self):
        self.validator = PhiSentenceValidator()
        self.vocabulary_map = self._load_vocabulary_mappings()
        self.grammar_patterns = self._load_grammar_patterns()
        self.max_iterations = 5
        
    def _load_vocabulary_mappings(self) -> Dict[str, Dict]:
        """Load English-to-Phi vocabulary mappings."""
        # This would ideally load from the actual Phi lexicon files
        # For now, we'll create a comprehensive mapping
        
        return {
            # Common verbs
            'walk': {'phi': 'shola', 'pos': 'verb', 'animacy_req': 'animate'},
            'run': {'phi': 'whumi', 'pos': 'verb', 'animacy_req': 'animate'},
            'like': {'phi': 'whomo', 'pos': 'verb', 'animacy_req': 'animate'},
            'love': {'phi': 'whomo', 'pos': 'verb', 'animacy_req': 'animate'},
            'sleep': {'phi': 'whuwe', 'pos': 'verb', 'animacy_req': 'animate'},
            'fly': {'phi': 'whawi', 'pos': 'verb', 'animacy_req': 'animate'},
            'sail': {'phi': 'sharo', 'pos': 'verb', 'animacy_req': 'animate'},
            'call': {'phi': 'shuna', 'pos': 'verb', 'animacy_req': 'human'},
            'ban': {'phi': 'thunu', 'pos': 'verb', 'animacy_req': 'human'},
            'blow': {'phi': 'whuru', 'pos': 'verb', 'context': 'wind'},
            'blowing': {'phi': 'whuru', 'pos': 'verb', 'context': 'wind'},  # progressive form
            'carry': {'phi': 'shero', 'pos': 'verb', 'animacy_req': 'animate'},
            'build': {'phi': 'shuni', 'pos': 'verb', 'animacy_req': 'human'},
            'be': {'phi': '', 'pos': 'auxiliary'},  # copula, often omitted in Phi
            'is': {'phi': '', 'pos': 'auxiliary'},  # copula, often omitted in Phi
            'are': {'phi': '', 'pos': 'auxiliary'},  # copula, often omitted in Phi
            'was': {'phi': '', 'pos': 'auxiliary'},  # copula, often omitted in Phi
            'were': {'phi': '', 'pos': 'auxiliary'},  # copula, often omitted in Phi
            
            # Common nouns
            'person': {'phi': 'thephoa', 'pos': 'noun', 'animacy': 'he'},
            'man': {'phi': 'thephoa', 'pos': 'noun', 'animacy': 'he'},
            'woman': {'phi': 'thephoa', 'pos': 'noun', 'animacy': 'he'},
            'friend': {'phi': 'luthea', 'pos': 'noun', 'animacy': 'he'},
            'road': {'phi': 'huphui', 'pos': 'noun', 'animacy': 'ne'},
            'roads': {'phi': 'huphui', 'pos': 'noun', 'animacy': 'ne'},  # plural
            'path': {'phi': 'huphui', 'pos': 'noun', 'animacy': 'ne'},
            'sea': {'phi': 'latheo', 'pos': 'noun', 'animacy': 'ne'},
            'seas': {'phi': 'latheo', 'pos': 'noun', 'animacy': 'ne'},  # plural
            'ocean': {'phi': 'latheo', 'pos': 'noun', 'animacy': 'ne'},
            'dove': {'phi': 'whithea', 'pos': 'noun', 'animacy': 'pi'},
            'bird': {'phi': 'lophea', 'pos': 'noun', 'animacy': 'pi'},
            'wind': {'phi': 'riwhea', 'pos': 'noun', 'animacy': 'ne'},
            'sand': {'phi': 'shuwhia', 'pos': 'noun', 'animacy': 'ne'},
            'cannonball': {'phi': 'phothea', 'pos': 'noun', 'animacy': 'ne'},
            'cannonballs': {'phi': 'phothea', 'pos': 'noun', 'animacy': 'ne'},  # plural
            'answer': {'phi': 'lowhai', 'pos': 'noun', 'animacy': 'ne'},
            'book': {'phi': 'whethea', 'pos': 'noun', 'animacy': 'ne', 'classifier': 'moi'},
            'books': {'phi': 'whethea', 'pos': 'noun', 'animacy': 'ne', 'classifier': 'moi'},  # plural
            'house': {'phi': 'hiwhea', 'pos': 'noun', 'animacy': 'ne'},
            
            # Articles and determiners
            'the': {'phi': '', 'pos': 'article'},  # often omitted in Phi
            'a': {'phi': '', 'pos': 'article'},   # often omitted in Phi
            'an': {'phi': '', 'pos': 'article'},  # often omitted in Phi
            
            # Pronouns
            'I': {'phi': 'mia', 'pos': 'pronoun'},
            'you': {'phi': 'thi', 'pos': 'pronoun'},
            'he': {'phi': 'sha', 'pos': 'pronoun'},
            'she': {'phi': 'sha', 'pos': 'pronoun'},
            'it': {'phi': 'sha', 'pos': 'pronoun'},
            'they': {'phi': 'sha', 'pos': 'pronoun'},
            'my': {'phi': 'mia', 'pos': 'pronoun'},
            
            # Question words
            'how': {'phi': 'hamito', 'pos': 'adverb'},
            'many': {'phi': 'hamite', 'pos': 'adverb', 'context': 'quantity'},
            'where': {'phi': 'hamire', 'pos': 'adverb'},
            'when': {'phi': 'hamile', 'pos': 'adverb'},
            'who': {'phi': 'hamise', 'pos': 'adverb'},
            'what': {'phi': 'hamise', 'pos': 'adverb'},
            
            # Prepositions
            'in': {'phi': 'phia', 'pos': 'preposition'},
            'on': {'phi': 'wheo', 'pos': 'preposition'},
            'at': {'phi': 'wheo', 'pos': 'preposition'},
            'from': {'phi': 'shio', 'pos': 'preposition'},
            'to': {'phi': 'phae', 'pos': 'preposition'},
            
            # Conjunctions
            'before': {'phi': 'pimo', 'pos': 'conjunction'},
            'after': {'phi': 'matu', 'pos': 'conjunction'},
            'since': {'phi': 'tura', 'pos': 'conjunction'},
            'if': {'phi': 'wetu', 'pos': 'conjunction'},
            'and': {'phi': 'nene', 'pos': 'conjunction'},
            
            # Adverbs
            'forever': {'phi': 'walito', 'pos': 'adverb'},
            'always': {'phi': 'walito', 'pos': 'adverb'},
            'now': {'phi': 'sipane', 'pos': 'adverb'},
            'soon': {'phi': 'somire', 'pos': 'adverb'},
            'recently': {'phi': 'pulime', 'pos': 'adverb'},
            
            # Adjectives
            'white': {'phi': 'sathi', 'pos': 'adjective'},
            'blue': {'phi': 'mipho', 'pos': 'adjective'},
            'green': {'phi': 'hashe', 'pos': 'adjective'},
            'beautiful': {'phi': 'mipha', 'pos': 'adjective'},
            'big': {'phi': 'lophu', 'pos': 'adjective'},
            'small': {'phi': 'niphe', 'pos': 'adjective'},
        }
    
    def _load_grammar_patterns(self) -> Dict:
        """Load English-to-Phi grammar transformation patterns."""
        return {
            'tense_mapping': {
                'past': 'li',
                'present': 'ta', 
                'future': 'su',
                'will': 'su',
                'would': 'su',
                'must': 'ru',
                'should': 'ru',
                'can': 'ta',  # ability in present
                'could': 'li'  # ability in past
            },
            
            'question_patterns': {
                'yes_no': {'marker': 'wa', 'structure': 'wa + SOV'},
                'wh_question': {'structure': 'WH + SOV'},
                'how_many': {'structure': 'hamite + noun + SOV'}
            },
            
            'clause_patterns': {
                'before_clause': {'conjunction': 'pimo', 'tense_logic': 'future_in_subordinate'},
                'after_clause': {'conjunction': 'matu', 'tense_logic': 'past_in_subordinate'},
                'if_clause': {'conjunction': 'wetu', 'tense_logic': 'present_or_future'}
            }
        }
    
    def translate(self, english_sentence: str, strategy: TranslationStrategy = TranslationStrategy.SEMANTIC) -> List[PhiTranslation]:
        """Translate English sentence to Phi with validation."""
        
        # 1. Analyze English sentence
        analysis = self._analyze_english(english_sentence)
        
        # 2. Generate initial translation(s)
        initial_translations = self._generate_initial_translations(analysis, strategy)
        
        # 3. Validate and refine translations
        validated_translations = []
        for translation in initial_translations:
            refined = self._validate_and_refine(translation, analysis)
            validated_translations.append(refined)
        
        # 4. Sort by confidence and validity
        validated_translations.sort(key=lambda t: (t.is_valid, t.confidence), reverse=True)
        
        return validated_translations
    
    def _analyze_english(self, sentence: str) -> EnglishAnalysis:
        """Analyze English sentence structure and meaning."""
        # Clean and tokenize
        original_words = sentence.replace('?', '').replace('.', '').replace(',', '').split()
        words = [word.lower() for word in original_words]
        
        # Detect question type
        question_type = None
        if sentence.strip().endswith('?'):
            if words[0] in ['how', 'what', 'where', 'when', 'who', 'why']:
                question_type = 'wh_question'
            elif words[0] in ['do', 'does', 'did', 'will', 'can', 'could', 'should', 'must']:
                question_type = 'yes_no'
            else:
                question_type = 'yes_no'  # assume yes/no if ends with ?
        
        # Detect tense and progressive aspect
        tense = 'present'
        is_progressive = False
        
        if any(word in words for word in ['will', 'shall']):
            tense = 'future'
        elif any(word in words for word in ['was', 'were', 'did', 'had']):
            tense = 'past'
        elif any(word in words for word in ['must', 'should']):
            tense = 'obligative'
        
        # Detect progressive aspect (is/was/will be + -ing)
        for i, word in enumerate(words):
            if word in ['is', 'are', 'was', 'were'] and i + 1 < len(words):
                next_word = words[i + 1]
                if next_word.endswith('ing'):
                    is_progressive = True
                    break
        
        # Better subject/verb/object detection
        subject = None
        verb = None
        obj = None
        main_verb = None
        
        # Handle "The X is Y-ing" pattern
        if 'is' in words or 'are' in words:
            is_index = words.index('is') if 'is' in words else words.index('are')
            
            # Subject is before 'is/are'
            for i in range(is_index - 1, -1, -1):
                if words[i] in self.vocabulary_map or words[i] == 'the':
                    if words[i] != 'the':
                        subject = words[i]
                    break
            
            # Look for -ing verb after 'is/are'
            for i in range(is_index + 1, len(words)):
                if words[i].endswith('ing'):
                    # Remove -ing to get base verb
                    base_verb = words[i][:-3]  # remove 'ing'
                    if base_verb in self.vocabulary_map:
                        main_verb = base_verb
                    elif base_verb + 'e' in self.vocabulary_map:  # handle "blowing" -> "blow"
                        main_verb = base_verb + 'e'
                    elif words[i][:-4] + 'w' in self.vocabulary_map:  # handle "blowing" -> "blow"
                        main_verb = words[i][:-4] + 'w'
                    break
        
        # Fallback: look for any verb in vocabulary
        if not main_verb:
            for i, word in enumerate(words):
                if word in self.vocabulary_map and self.vocabulary_map[word]['pos'] == 'verb':
                    main_verb = word
                    # Subject is typically before verb
                    if i > 0 and words[i-1] in self.vocabulary_map:
                        subject = words[i-1]
                    # Object is typically after verb
                    if i < len(words) - 1 and words[i+1] in self.vocabulary_map:
                        obj = words[i+1]
                    break
        
        # If no subject found yet, look for first noun
        if not subject:
            for word in words:
                if word in self.vocabulary_map and self.vocabulary_map[word]['pos'] == 'noun':
                    subject = word
                    break
        
        return EnglishAnalysis(
            words=words,
            pos_tags=[],  # Would be filled by proper NLP
            subject=subject,
            verb=main_verb,
            object=obj,
            modifiers=[],
            tense=tense,
            question_type=question_type,
            is_negative='not' in words or "n't" in sentence,
            is_passive=False,  # Would detect passive voice
            subordinate_clauses=[]
        )
    
    def _generate_initial_translations(self, analysis: EnglishAnalysis, strategy: TranslationStrategy) -> List[PhiTranslation]:
        """Generate initial Phi translation candidates."""
        translations = []
        
        # Generate primary translation
        phi_words = []
        confidence = 1.0
        
        # Handle questions
        if analysis.question_type == 'yes_no':
            phi_words.append('wa')
        
        # Handle wh-questions
        if analysis.question_type == 'wh_question':
            for word in analysis.words:
                if word in ['how', 'many']:
                    if 'how' in analysis.words and 'many' in analysis.words:
                        phi_words.append('hamite')  # how many
                        break
                elif word in self.vocabulary_map and self.vocabulary_map[word]['pos'] == 'adverb':
                    phi_words.append(self.vocabulary_map[word]['phi'])
                    break
        
        # Translate words in SOV order
        # Subject first
        if analysis.subject and analysis.subject in self.vocabulary_map:
            subject_info = self.vocabulary_map[analysis.subject]
            
            # Add animacy marker if needed
            if 'animacy' in subject_info:
                phi_words.append(subject_info['animacy'])
            
            phi_words.append(subject_info['phi'])
        
        # Handle prepositions and their objects
        preposition_phrases = []
        for i, word in enumerate(analysis.words):
            if word in self.vocabulary_map and self.vocabulary_map[word]['pos'] == 'preposition':
                prep_phi = self.vocabulary_map[word]['phi']
                # Look for noun after preposition
                if i + 1 < len(analysis.words):
                    next_word = analysis.words[i + 1]
                    if next_word in self.vocabulary_map and self.vocabulary_map[next_word]['pos'] == 'noun':
                        noun_info = self.vocabulary_map[next_word]
                        preposition_phrases.append((noun_info['phi'], prep_phi))
        
        # Add prepositional phrases
        for noun_phi, prep_phi in preposition_phrases:
            phi_words.append(noun_phi)
            phi_words.append(prep_phi)
        
        # Object with marker (if not already handled in prepositional phrases)
        if analysis.object and analysis.object in self.vocabulary_map:
            # Check if this object is already in a prepositional phrase
            obj_already_added = any(analysis.object in self.vocabulary_map and 
                                  self.vocabulary_map[analysis.object]['phi'] == noun_phi 
                                  for noun_phi, _ in preposition_phrases)
            
            if not obj_already_added:
                phi_words.append('na')  # object marker
                obj_info = self.vocabulary_map[analysis.object]
                
                # Add classifier if needed
                if 'classifier' in obj_info:
                    phi_words.append(obj_info['classifier'])
                
                phi_words.append(obj_info['phi'])
        
        # Tense/mood particles (should come before aspect)
        if analysis.tense in self.grammar_patterns['tense_mapping']:
            tense_particle = self.grammar_patterns['tense_mapping'][analysis.tense]
            if tense_particle not in phi_words:  # avoid duplicates
                phi_words.append(tense_particle)
        
        # Progressive aspect (comes after tense)
        is_progressive = any(word.endswith('ing') for word in analysis.words)
        if is_progressive:
            phi_words.append('la')  # progressive aspect
        
        # Verb last (SOV)
        if analysis.verb and analysis.verb in self.vocabulary_map:
            phi_words.append(self.vocabulary_map[analysis.verb]['phi'])
        
        # Handle remaining words (adjectives, adverbs not yet processed)
        for word in analysis.words:
            if (word in self.vocabulary_map and 
                word not in [analysis.subject, analysis.verb, analysis.object] and
                self.vocabulary_map[word]['pos'] in ['adjective', 'adverb'] and
                self.vocabulary_map[word]['phi'] not in phi_words):
                
                phi_words.append(self.vocabulary_map[word]['phi'])
        
        # Clean up empty words and duplicates while preserving order
        cleaned_phi_words = []
        seen = set()
        for word in phi_words:
            if word and word not in seen:
                cleaned_phi_words.append(word)
                seen.add(word)
        
        phi_sentence = ' '.join(cleaned_phi_words)
        
        translation = PhiTranslation(
            phi_sentence=phi_sentence,
            confidence=confidence,
            strategy=strategy,
            validation_errors=[],
            is_valid=False,
            alternatives=[]
        )
        
        translations.append(translation)
        return translations
    
    def _validate_and_refine(self, translation: PhiTranslation, analysis: EnglishAnalysis) -> PhiTranslation:
        """Validate translation and refine if needed."""
        
        for iteration in range(self.max_iterations):
            # Validate current translation
            validation_result = self.validator.validate_sentence(translation.phi_sentence)
            
            if validation_result['is_valid']:
                translation.is_valid = True
                translation.validation_errors = []
                break
            else:
                # Store errors
                translation.validation_errors = [
                    f"{error.error_type.value}: {error.message}" 
                    for error in validation_result['errors']
                ]
                
                # Try to fix errors
                fixed_sentence = self._fix_validation_errors(
                    translation.phi_sentence, 
                    validation_result['errors'],
                    analysis
                )
                
                if fixed_sentence != translation.phi_sentence:
                    translation.phi_sentence = fixed_sentence
                    translation.confidence *= 0.9  # Reduce confidence for each fix
                else:
                    # Can't fix further
                    break
        
        return translation
    
    def _fix_validation_errors(self, phi_sentence: str, errors: List, analysis: EnglishAnalysis) -> str:
        """Attempt to fix validation errors."""
        tokens = phi_sentence.split()
        
        for error in errors:
            error_type = error.error_type.value
            
            # Fix missing verb
            if error_type == 'missing_verb' and analysis.verb:
                if analysis.verb in self.vocabulary_map:
                    verb_phi = self.vocabulary_map[analysis.verb]['phi']
                    if verb_phi not in tokens:
                        tokens.append(verb_phi)
            
            # Fix word order (move verb to end)
            elif error_type == 'word_order':
                # Find verb and move to end
                for i, token in enumerate(tokens):
                    word_type = self.validator.identify_word_type(token)
                    if word_type == 'verb':
                        verb = tokens.pop(i)
                        tokens.append(verb)
                        break
            
            # Fix animacy mismatches
            elif error_type == 'animacy_mismatch':
                # This would require more sophisticated analysis
                pass
            
            # Fix tense inconsistencies
            elif error_type == 'tense_inconsistency':
                # Adjust tense based on context
                if analysis.question_type and analysis.tense == 'obligative':
                    # For rhetorical questions, ensure 'ru' is present
                    if 'ru' not in tokens:
                        # Insert before verb
                        for i, token in enumerate(tokens):
                            if self.validator.identify_word_type(token) == 'verb':
                                tokens.insert(i, 'ru')
                                break
        
        return ' '.join(tokens)
    
    def translate_interactive(self):
        """Interactive translation mode."""
        print("English to Phi Translator")
        print("=" * 40)
        print("Enter English sentences to translate to Phi.")
        print("Type 'quit' to exit.\n")
        
        while True:
            try:
                english = input("English> ").strip()
                if english.lower() in ['quit', 'exit', 'q']:
                    break
                
                if not english:
                    continue
                
                print(f"\nTranslating: '{english}'")
                print("-" * 40)
                
                translations = self.translate(english)
                
                for i, translation in enumerate(translations[:3], 1):
                    status = "✅ VALID" if translation.is_valid else "❌ INVALID"
                    print(f"\nTranslation {i}: {status}")
                    print(f"Phi: {translation.phi_sentence}")
                    print(f"Confidence: {translation.confidence:.2f}")
                    print(f"Strategy: {translation.strategy.value}")
                    
                    if translation.validation_errors:
                        print("Validation errors:")
                        for error in translation.validation_errors:
                            print(f"  - {error}")
                
                print("\n" + "=" * 40)
                
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break


def main():
    """Command-line interface for the translator."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Translate English to Phi")
    parser.add_argument("sentence", nargs="?", help="English sentence to translate")
    parser.add_argument("--interactive", "-i", action="store_true", 
                       help="Interactive mode")
    parser.add_argument("--strategy", choices=['literal', 'semantic', 'contextual', 'poetic'],
                       default='semantic', help="Translation strategy")
    
    args = parser.parse_args()
    
    translator = EnglishToPhiTranslator()
    
    if args.interactive:
        translator.translate_interactive()
    elif args.sentence:
        strategy = TranslationStrategy(args.strategy)
        translations = translator.translate(args.sentence, strategy)
        
        print(f"Translating: '{args.sentence}'")
        print("=" * 50)
        
        for i, translation in enumerate(translations, 1):
            status = "✅ VALID" if translation.is_valid else "❌ INVALID"
            print(f"\nTranslation {i}: {status}")
            print(f"Phi: {translation.phi_sentence}")
            print(f"Confidence: {translation.confidence:.2f}")
            
            if translation.validation_errors:
                print("Validation errors:")
                for error in translation.validation_errors:
                    print(f"  - {error}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main() 