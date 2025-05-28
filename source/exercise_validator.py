#!/usr/bin/env python3
"""
Comprehensive Phi Sentence Validator Exercise Framework

Tests the validator with a wide range of sentences from simple to complex,
organized by linguistic features and complexity levels.
"""

import sys
from pathlib import Path
from typing import List, Dict, Tuple
import json

# Add current directory to path
sys.path.append(str(Path(__file__).parent))

# Use direct import to avoid hanging
from phi_validation.core import PhiSentenceValidator

class SentenceExerciser:
    """Exercise the Phi sentence validator with comprehensive test cases."""
    
    def __init__(self):
        """Initialize the exerciser with validator and test sentences."""
        self.validator = PhiSentenceValidator()
        self.test_categories = self._build_test_categories()
        self.results = {}
    
    def _build_test_categories(self) -> Dict[str, List[Tuple[str, str, bool]]]:
        """Build comprehensive test categories with expected results."""
        return {
            # Basic sentence structures with varied vocabulary
            "basic_sentences": [
                ("mia ta thihi", "I present be", True),
                ("thi ta whemo", "you present think", True),
                ("sha ta whuni", "they present have", True),
                ("he thephoa ta phoni", "human person present live", True),
                ("pi whithea ta whawi", "animate dove present fly", True),
                ("ne lowhai ta riphe phera", "inanimate answer present important is", True),
                ("mia li whera", "I past learn", True),
                ("thi su whesa", "you future create", True),
            ],
            
            # Rich vocabulary showcase
            "vocabulary_showcase": [
                ("he thephoa ta whemo", "human person present think", True),
                ("pi mathai ta whuwe", "animate cat present sleep", True),
                ("ne whethea misha ta phera", "inanimate book beautiful present is", True),
                ("mia na ne raoshea ta whona", "I object inanimate sun present look", True),
                ("thi na ne riwhea ta shusa", "you object inanimate wind present hear", True),
                ("sha na ne waphe ta phewa", "they object inanimate warm present feel", True),
                ("he nowhea ta sheme", "human teacher present teach", True),
                ("pi saphoa ta whale", "animate snake present flow", True),
            ],
            
            # Natural world and environment
            "natural_world": [
                ("ne riwhea ta whuru", "inanimate wind present blow", True),
                ("pi lophea ta whari", "animate bird present sing", True),
                ("ne raoshea ta shine", "inanimate sun present seem", True),
                ("ne lashea ta whale", "inanimate rain present flow", True),
                ("pi whithea na ne loshea ta sharo", "animate dove object inanimate ocean present go", True),
                ("ne liphai ta pholi", "inanimate tree present grow", True),
                ("pi mathai na pi whithea ta shosa", "animate cat object animate dove present watch", True),
                ("ne shuwhia ta miwhi phera", "inanimate sand present fresh is", True),
            ],
            
            # Human activities and relationships
            "human_activities": [
                ("he thephoa na ne hiwhea ta shuni", "human person object inanimate house present build", True),
                ("he nowhea na he phiphea ta sheme", "human teacher object human child present teach", True),
                ("he luthea na ne noshea ta shuwo", "human friend object inanimate food present offer", True),
                ("he hishui na he phiphea ta phepa", "human parent object human child present heal", True),
                ("he thephoa na ne whethea ta shiho", "human person object inanimate book present buy", True),
                ("he hathai na ne thaphao ta whari", "human musician object inanimate song present sing", True),
                ("he luphea na ne nuthea ta whesa", "human artist object inanimate sculpture present create", True),
                ("he thephoa na he luthea ta whoso", "human person object human friend present marry", True),
            ],
            
            # Complex particle sequences
            "complex_particles": [
                ("hi so he thephoa ta whemo", "evidence politeness human person present think", True),
                ("ro ma ne lowhai ta riphe phera", "inference emphasis inanimate answer present important is", True),
                ("nu so sha na ne lophui li whesa", "hearsay politeness they object inanimate art past create", True),
                ("hi ma mia na ne mipho lowhai ta whona", "evidence emphasis I object inanimate blue answer present look", True),
                ("wa so he thephoa na ne phuphai ta whuni", "question politeness human person object inanimate medicine present have", True),
                ("mu ma thi na ne nushui li whera", "memory emphasis you object inanimate language past learn", True),
            ],
            
            # Word order variations with proper particle ordering
            "word_order_varied": [
                ("mia na ne whethea ta whupi", "I object inanimate book present read-silently", True),
                ("he thephoa na ne noshea ta theso", "human person object inanimate food present cook", True),
                ("thi na ne phuphai ta whuni", "you object inanimate medicine present have", True),
                ("sha na ne luthia ta shele", "they object inanimate letter present send", True),
                ("he phiphea na ne mophui ta whuwa", "human child object inanimate ball present throw", True),
                ("pi mathai na ne liwhai ta shire", "animate cat object inanimate drink present want", True),
                ("he thephoa na ne tuphai ta shiho", "human person object inanimate cup present buy", True),
            ],
            
            # Temporal and aspectual constructions
            "temporal_constructions": [
                ("mia na ne nushui li we whera", "I object inanimate language past perfective learn", True),
                ("thi na ne lophui ta la whesa", "you object inanimate art present progressive create", True),
                ("sha na ne phuphai su ni whuni", "they object inanimate medicine future perfect have", True),
                ("he thephoa na ne hiwhea li pu shuni", "human person object inanimate house past cessative build", True),
                ("pi lophea ta ri whari", "animate bird present imperfective sing", True),
                ("ne raoshea su po shine", "inanimate sun future inchoative seem", True),
                ("he nowhea ta wi sheme", "human teacher present iterative teach", True),
                ("mia na ne raoshea li wu whona", "I object inanimate sun past experiential look", True),
            ],
            
            # Modal constructions with logical contexts
            "modal_constructions": [
                ("he phiphea ru whera", "human child must learn", True),
                ("thi na ne lowhai to whesa", "you object inanimate answer imperative create", True),
                ("sha na ne phuphai we te whuni", "they object inanimate medicine want to have", True),
                ("he thephoa ru phepa", "human person must heal", True),
                ("wetu ne lashea ta whale thi su phite", "if inanimate rain present flow you future stay", True),
                ("he nowhea na he phiphea ru sheme", "human teacher object human child must teach", True),
                ("mia na ne noshea ru whuni", "I object inanimate food must have", True),
            ],
            
            # Evidentiality with appropriate contexts
            "evidentiality_contexts": [
                ("hi ne riwhea ta whuru", "direct-evidence inanimate wind present blow", True),
                ("ro he thephoa ta phoni", "inference human person present live", True),
                ("nu he thephoa na ne lophui li whesa", "hearsay human person object inanimate art past create", True),
                ("ti he nowhea li shuso mia ta whera", "reported human teacher past say I present learn", True),
                ("mu mia na ne raoshea li whona", "memory I object inanimate sun past look", True),
                ("pe ne lashea su whale", "presumption inanimate rain future flow", True),
                ("hi ro ne lowhai ta riphe", "direct inference inanimate answer present important", False),  # conflict
            ],
            
            # Derivational constructions with appropriate words
            "derivational_constructions": [
                ("mia ta se lathia", "I present use-as-axe", True),
                ("ra whesa ta misha phera", "creating present beautiful is", True),
                ("thi ta se tuphai", "you present use-as-cup", True),
                ("ra whari ta hesha phera", "singing present delicious is", True),
                ("he thephoa ta se hashia", "human person present use-as-hammer", True),
                ("ra whemo ta riphe phera", "thinking present important is", True),
                ("mia ta se ra whesa", "I present use-as creating", False),  # double derivation
            ],
            
            # Emphasis with varied targets
            "emphasis_constructions": [
                ("ma mia ta whemo", "emphasis I present think", True),
                ("he thephoa ma ta phoni", "human person emphasis present live", True),
                ("mia na ne lophui ta ma whesa", "I object inanimate art present emphasis create", True),
                ("ma he thephoa na ne phuphai ta whuni", "emphasis human person object inanimate medicine present have", True),
                ("ma mipho lowhai ta riphe phera", "emphasis blue answer present important is", True),
                ("ma ma mia ta whemo", "double emphasis I present think", False),  # double emphasis
                ("ma", "emphasis alone", False),  # no target
            ],
            
            # Politeness in appropriate contexts
            "politeness_contexts": [
                ("so mia ta thihi", "politeness I present be", True),
                ("so thi na ne lowhai to whesa", "politeness you object inanimate answer imperative create", True),
                ("so ru whera", "politeness must learn", True),
                ("hi so he thephoa ta phoni", "evidence politeness human person present live", True),
                ("wa so he thephoa na ne phuphai ta whuni", "question politeness human person object inanimate medicine present have", True),
                ("so hi mia ta whemo", "politeness evidence I present think", False),  # wrong order
            ],
            
            # Discourse structures with logical flow
            "discourse_structures": [
                ("ha mia ta whemo", "topic I present think", True),
                ("mia ta whera mi thi ta sheme", "I present learn contrast you present teach", True),
                ("ha he thephoa ta phoni", "topic human person present live", True),
                ("ha ne lowhai ta riphe phera mi sha ta miphe phera", "topic inanimate answer present important is contrast they present empty are", True),
                ("mi mia ta whemo", "contrast I present think", False),  # contrast without context
                ("ha mi mia ta whemo", "topic contrast I present think", True),
            ],
            
            # Interrogative structures with logical questions
            "interrogative_structures": [
                ("wa he thephoa ta phoni", "question human person present live", True),
                ("hamite mia ta whera", "how I present learn", True),
                ("wamine he thephoa na ne phuphai ta whuni", "why human person object inanimate medicine present have", True),
                ("timane ne lashea ta whale", "when inanimate rain present flow", True),
                ("wulime he nowhea ta phoni", "where human teacher present live", True),
                ("wa hamite mia ta whera", "question how I present learn", False),  # wa + wh conflict
                ("wa he thephoa ru whera", "question human person must learn", True),  # rhetorical
            ],
            
            # Narrative sequences with logical temporal relationships
            "narrative_sequences": [
                ("mia li whera matu thi li sheme", "I past learn after you past teach", True),
                ("he thephoa su whesa pimo thi ta whuni", "human person future create before you present have", True),
                ("wetu ne lashea ta whale thi su phite", "if inanimate rain present flow you future stay", True),
                ("he thephoa lu ta whemo riphe phera", "person who present think important is", True),
                ("mia li whera pimo thi ta sheme", "I past learn before you present teach", False),  # temporal logic error
                ("he thephoa su whesa matu thi li whuni", "human person future create after you past have", False),  # temporal logic error
            ],
            
            # Complex multi-feature sentences
            "complex_sentences": [
                ("hi so ma he thephoa ta we whera", "evidence politeness emphasis human person present perfective learn", True),
                ("wa so ma mia na ne lophui li we whesa", "question politeness emphasis I object inanimate art past perfective create", True),
                ("nu ha so he nowhea na ne nushui ta sheme", "hearsay topic politeness human teacher object inanimate language present teach", True),
                ("ro ma mia na ne lathia ta shero", "inference emphasis I object inanimate axe present carry", True),
                ("wa hi so ma he thephoa ta ru whera", "question evidence politeness emphasis human person present must learn", True),
            ],
            
            # Semantic role validation
            "semantic_roles": [
                ("he thephoa ta whemo", "human person present think", True),
                ("pi mathai ta whuwe", "animate cat present sleep", True),
                ("ne lowhai ta riphe phera", "inanimate answer present important is", True),
                ("he thephoa ne whethea na ta whesa", "human person inanimate book object present create", True),
                ("pi lophea ne liwhai na ta shire", "animate bird inanimate drink object present want", True),
                ("ne lowhai he thephoa na ta whemo", "inanimate answer human person object present think", False),  # animacy mismatch
                ("pi mathai ta shuni", "animate cat present build", False),  # verb requires human subject
            ],
            
            # Error cases for validation
            "error_cases": [
                ("invalidword ta whemo", "unknown word", False),
                ("mia ta ta whemo", "double tense", False),
                ("mia whemo ta thihi", "verb not at end", False),
                ("ta whemo mia", "wrong word order", False),
                ("mia li su whemo", "conflicting tenses", False),
                ("hi nu mia ta whemo", "conflicting evidentiality", False),
                ("ma wa mia ta whemo", "emphasis on question particle", False),
                ("so hi mia ta whemo", "wrong particle order", False),
            ],
            
            # Edge cases and boundary conditions
            "edge_cases": [
                ("", "empty sentence", False),
                ("whemo", "single verb (imperative)", True),
                ("ta", "single particle", False),
                ("mia mia ta whemo", "repeated pronoun", True),  # might be valid for emphasis
                ("he he thephoa ta whemo", "repeated animacy", False),
                ("ma ma ma mia ta whemo", "triple emphasis", False),
                ("so so mia ta whemo", "double politeness", False),
                ("ne lowhai", "noun phrase only", False),  # incomplete sentence
                ("ta thihi", "present be", True),  # valid existential
            ],
            
            # Colors and descriptions
            "descriptive_language": [
                ("ne mipho lowhai ta misha phera", "inanimate blue answer present beautiful is", True),
                ("ne hashe liphai ta tophe phera", "inanimate green tree present large is", True),
                ("he thephoa ne laphe roshai na ta whona", "human person inanimate red flower object present look", True),
                ("ne sathia mothao ta shine", "inanimate white cloud present seem", True),
                ("pi mathai ne waphe na ta phewa", "animate cat inanimate warm object present feel", True),
                ("ne tupha whethea ta hesha", "inanimate purple book present delicious", False),  # semantic mismatch
            ],
            
            # Professional and social contexts
            "professional_contexts": [
                ("he nowhea na he phiphea ta sheme", "human teacher object human child present teach", True),
                ("he luphea na ne nuthea ta whesa", "human artist object inanimate sculpture present create", True),
                ("he hathai na ne thaphao ta whari", "human musician object inanimate song present sing", True),
                ("he thephoa na ne wushia ta whuri", "human person object inanimate market present work", True),
                ("he raushai na he lushai ta phasu", "human leader object human group present lead", True),
                ("he thephoa na ne phuthui ta shota", "human person object inanimate document present document", True),
            ]
        }
    
    def run_category(self, category: str, verbose: bool = True) -> Dict:
        """Run tests for a specific category."""
        if category not in self.test_categories:
            print(f"❌ Unknown category: {category}")
            return {}
        
        tests = self.test_categories[category]
        results = {
            'total': len(tests),
            'correct': 0,
            'incorrect': 0,
            'details': []
        }
        
        if verbose:
            print(f"\n🧪 Testing Category: {category.upper()}")
            print("=" * 60)
        
        for sentence, description, expected_valid in tests:
            result = self.validator.validate_sentence(sentence)
            actual_valid = result['is_valid']
            correct = (actual_valid == expected_valid)
            
            if correct:
                results['correct'] += 1
                status = "✅"
            else:
                results['incorrect'] += 1
                status = "❌"
            
            test_detail = {
                'sentence': sentence,
                'description': description,
                'expected': expected_valid,
                'actual': actual_valid,
                'correct': correct,
                'errors': [{'type': e.error_type.value, 'message': e.message} for e in result['errors']]
            }
            results['details'].append(test_detail)
            
            if verbose:
                print(f"{status} '{sentence}'")
                print(f"   Description: {description}")
                print(f"   Expected: {'VALID' if expected_valid else 'INVALID'}, "
                      f"Got: {'VALID' if actual_valid else 'INVALID'}")
                
                if not correct:
                    print(f"   ⚠️  MISMATCH!")
                
                if result['errors'] and verbose:
                    print(f"   Errors: {len(result['errors'])}")
                    for error in result['errors'][:2]:  # Show first 2 errors
                        print(f"     - {error.error_type.value}: {error.message}")
                    if len(result['errors']) > 2:
                        print(f"     - ... and {len(result['errors']) - 2} more")
                
                print()
        
        if verbose:
            accuracy = (results['correct'] / results['total']) * 100
            print(f"Category Results: {results['correct']}/{results['total']} correct ({accuracy:.1f}%)")
        
        return results
    
    def run_all_categories(self, verbose: bool = True) -> Dict:
        """Run tests for all categories."""
        print("🎯 COMPREHENSIVE PHI SENTENCE VALIDATOR EXERCISE")
        print("=" * 60)
        
        all_results = {}
        total_tests = 0
        total_correct = 0
        
        for category in self.test_categories.keys():
            category_results = self.run_category(category, verbose)
            all_results[category] = category_results
            total_tests += category_results['total']
            total_correct += category_results['correct']
        
        # Overall summary
        overall_accuracy = (total_correct / total_tests) * 100
        print("\n" + "=" * 60)
        print("📊 OVERALL RESULTS")
        print("=" * 60)
        print(f"Total tests: {total_tests}")
        print(f"Correct predictions: {total_correct}")
        print(f"Incorrect predictions: {total_tests - total_correct}")
        print(f"Overall accuracy: {overall_accuracy:.1f}%")
        
        # Category breakdown
        print(f"\n📋 CATEGORY BREAKDOWN:")
        for category, results in all_results.items():
            accuracy = (results['correct'] / results['total']) * 100
            print(f"  {category:20} {results['correct']:3}/{results['total']:3} ({accuracy:5.1f}%)")
        
        return {
            'categories': all_results,
            'summary': {
                'total_tests': total_tests,
                'total_correct': total_correct,
                'overall_accuracy': overall_accuracy
            }
        }
    
    def run_interactive_mode(self):
        """Run interactive testing mode."""
        print("🎮 INTERACTIVE PHI SENTENCE VALIDATOR")
        print("=" * 50)
        print("Enter Phi sentences to validate (empty line to quit)")
        print("Commands:")
        print("  !categories - list available test categories")
        print("  !run <category> - run a specific test category")
        print("  !run all - run all test categories")
        print("  !help - show this help")
        print()
        
        while True:
            try:
                user_input = input("phi> ").strip()
                
                if not user_input:
                    print("Goodbye!")
                    break
                
                if user_input.startswith('!'):
                    self._handle_command(user_input)
                else:
                    # Validate user sentence
                    result = self.validator.validate_sentence(user_input)
                    
                    print(f"Sentence: '{user_input}'")
                    print(f"Valid: {'✅ YES' if result['is_valid'] else '❌ NO'}")
                    
                    if result['errors']:
                        print(f"Errors ({len(result['errors'])}):")
                        for error in result['errors']:
                            print(f"  - {error.error_type.value}: {error.message}")
                    else:
                        print("No errors detected!")
                    
                    print()
            
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")
    
    def _handle_command(self, command: str):
        """Handle interactive commands."""
        parts = command[1:].split()
        cmd = parts[0] if parts else ""
        
        if cmd == "categories":
            print("Available test categories:")
            for i, category in enumerate(self.test_categories.keys(), 1):
                count = len(self.test_categories[category])
                print(f"  {i:2}. {category:20} ({count} tests)")
            print()
        
        elif cmd == "run":
            if len(parts) < 2:
                print("Usage: !run <category> or !run all")
                return
            
            target = parts[1]
            if target == "all":
                self.run_all_categories(verbose=True)
            elif target in self.test_categories:
                self.run_category(target, verbose=True)
            else:
                print(f"Unknown category: {target}")
                print("Use !categories to see available categories")
        
        elif cmd == "help":
            print("Commands:")
            print("  !categories - list available test categories")
            print("  !run <category> - run a specific test category")
            print("  !run all - run all test categories")
            print("  !help - show this help")
            print()
        
        else:
            print(f"Unknown command: {command}")
            print("Use !help for available commands")
    
    def save_results(self, results: Dict, filename: str = "validation_results.json"):
        """Save test results to JSON file."""
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"Results saved to {filename}")


def main():
    """Main function for command-line usage."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Exercise Phi sentence validator")
    parser.add_argument("--category", "-c", help="Run specific category")
    parser.add_argument("--all", "-a", action="store_true", help="Run all categories")
    parser.add_argument("--interactive", "-i", action="store_true", help="Interactive mode")
    parser.add_argument("--quiet", "-q", action="store_true", help="Quiet mode (less verbose)")
    parser.add_argument("--save", "-s", help="Save results to file")
    
    args = parser.parse_args()
    
    exerciser = SentenceExerciser()
    
    if args.interactive:
        exerciser.run_interactive_mode()
    elif args.all:
        results = exerciser.run_all_categories(verbose=not args.quiet)
        if args.save:
            exerciser.save_results(results, args.save)
    elif args.category:
        results = exerciser.run_category(args.category, verbose=not args.quiet)
        if args.save:
            exerciser.save_results({args.category: results}, args.save)
    else:
        # Default: show available categories and run interactive mode
        print("🎯 PHI SENTENCE VALIDATOR EXERCISER")
        print("=" * 40)
        print("Available options:")
        print("  --all (-a)           Run all test categories")
        print("  --category (-c) CAT  Run specific category")
        print("  --interactive (-i)   Interactive mode")
        print("  --quiet (-q)         Less verbose output")
        print("  --save (-s) FILE     Save results to file")
        print()
        print("Available categories:")
        for category in exerciser.test_categories.keys():
            count = len(exerciser.test_categories[category])
            print(f"  {category:20} ({count} tests)")
        print()
        print("Starting interactive mode...")
        exerciser.run_interactive_mode()


if __name__ == "__main__":
    main() 