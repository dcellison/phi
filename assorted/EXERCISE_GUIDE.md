# Phi Sentence Validator Exercise Guide

## Overview

The `exercise_validator.py` script provides a comprehensive framework for testing the Phi sentence validator with sentences ranging from simple to complex. It includes **150+ test sentences** organized into **14 categories** covering all aspects of Phi grammar.

## Quick Start

### 1. Interactive Mode (Recommended for Exploration)
```bash
python3 exercise_validator.py --interactive
```
- Test your own sentences interactively
- Run specific test categories on demand
- Get immediate feedback with detailed error explanations

### 2. Run All Tests
```bash
python3 exercise_validator.py --all
```
- Runs all 150+ test sentences across 14 categories
- Shows comprehensive accuracy statistics
- Identifies any validation issues

### 3. Run Specific Categories
```bash
python3 exercise_validator.py --category basic_sentences
python3 exercise_validator.py --category complex_particles
python3 exercise_validator.py --category error_cases
```

## Test Categories

### 📚 **Basic Categories (Simple → Complex)**

1. **`basic_sentences`** (7 tests)
   - Simple subject-verb constructions
   - Basic tense usage
   - Fundamental sentence patterns

2. **`particle_combinations`** (8 tests)
   - Single particle usage
   - Basic particle-word combinations
   - Common grammatical particles

3. **`complex_particles`** (6 tests)
   - Multiple particle sequences
   - Advanced particle interactions
   - Sophisticated grammatical constructions

### 🏗️ **Structural Categories**

4. **`word_order`** (5 tests)
   - SOV structure variations
   - Object marking with `na`
   - Complex argument structures

5. **`temporal_constructions`** (8 tests)
   - Tense-aspect combinations
   - Temporal particle sequences
   - Time-related grammatical patterns

6. **`modal_constructions`** (6 tests)
   - Obligative (`ru`) constructions
   - Imperative (`to`) usage
   - Conditional structures
   - Modal-tense interactions

### 🎯 **Advanced Linguistic Features**

7. **`evidentiality`** (8 tests)
   - All 6 evidentiality particles
   - Evidentiality combinations
   - Reported speech nesting

8. **`derivational`** (6 tests)
   - `se` (noun→verb) constructions
   - `ra` (verb→noun) constructions
   - Derivational scope and conflicts

9. **`emphasis`** (7 tests)
   - `ma` particle scope
   - Emphasis targeting
   - Multiple emphasis patterns

10. **`politeness`** (6 tests)
    - `so` particle contexts
    - Politeness appropriateness
    - Particle ordering with politeness

### 💬 **Discourse and Communication**

11. **`discourse`** (6 tests)
    - Topic marking (`ha`)
    - Contrast marking (`mi`)
    - Topic-contrast interactions

12. **`interrogatives`** (7 tests)
    - Yes/no questions (`wa`)
    - Wh-questions (`hamite`, `wamine`, etc.)
    - Question-particle conflicts

13. **`narrative`** (6 tests)
    - Temporal sequences
    - Relative clauses
    - Narrative coherence

### 🌟 **Complex and Edge Cases**

14. **`complex_sentences`** (5 tests)
    - Multi-feature sentences
    - Advanced particle combinations
    - Real-world complexity

15. **`error_cases`** (8 tests)
    - Known invalid constructions
    - Common grammatical errors
    - Validation accuracy testing

16. **`edge_cases`** (7 tests)
    - Boundary conditions
    - Unusual but potentially valid constructions
    - System robustness testing

## Usage Examples

### Interactive Session
```bash
$ python3 exercise_validator.py --interactive

🎮 INTERACTIVE PHI SENTENCE VALIDATOR
==================================================
Enter Phi sentences to validate (empty line to quit)
Commands:
  !categories - list available test categories
  !run <category> - run a specific test category
  !run all - run all test categories
  !help - show this help

phi> mia ta thilu
Sentence: 'mia ta thilu'
Valid: ✅ YES
No errors detected!

phi> ma ma mia ta thilu
Sentence: 'ma ma mia ta thilu'
Valid: ❌ NO
Errors (2):
  - emphasis_scope_error: Emphasis particle 'ma' cannot target particle 'ma'
  - emphasis_scope_error: Double emphasis detected: 'ma ma' is prohibited

phi> !run basic_sentences
[Runs basic sentence tests...]

phi> !categories
Available test categories:
   1. basic_sentences      (7 tests)
   2. particle_combinations (8 tests)
   [... etc ...]
```

### Batch Testing
```bash
# Run all tests with detailed output
python3 exercise_validator.py --all

# Run specific category quietly
python3 exercise_validator.py --category evidentiality --quiet

# Save results to file
python3 exercise_validator.py --all --save results.json
```

## Understanding Results

### Test Output Format
```
✅ 'mia ta thilu'
   Description: I present be
   Expected: VALID, Got: VALID

❌ 'ma ma mia ta thilu'
   Description: double emphasis I present walk
   Expected: INVALID, Got: INVALID
   Errors: 2
     - emphasis_scope_error: Emphasis particle 'ma' cannot target particle 'ma'
     - emphasis_scope_error: Double emphasis detected: 'ma ma' is prohibited
```

### Accuracy Statistics
```
📊 OVERALL RESULTS
============================================================
Total tests: 150
Correct predictions: 145
Incorrect predictions: 5
Overall accuracy: 96.7%

📋 CATEGORY BREAKDOWN:
  basic_sentences       7/  7 (100.0%)
  particle_combinations 8/  8 (100.0%)
  complex_particles     6/  6 (100.0%)
  [... etc ...]
```

## Test Categories in Detail

### Simple to Complex Progression

**Level 1: Basic Sentences**
```
mia ta thilu          # I present be
thi ta shola          # you present walk
sha ta whumi          # they present run
```

**Level 2: Single Particles**
```
so mia ta thilu       # politeness I present be
hi mia ta shola       # direct-evidence I present walk
ma mia ta thilu       # emphasis I present be
```

**Level 3: Multiple Particles**
```
hi so he thephoa ta shola    # evidence politeness human person present walk
so ma he thephoa ta shola    # politeness emphasis human person present walk
```

**Level 4: Complex Constructions**
```
hi so ma he thephoa ta we shola    # evidence politeness emphasis human person present perfective walk
nu so ha he thephoa mi ta shola ta thilu    # hearsay politeness topic human person contrast present walk present be
```

### Error Detection Testing
```
invalidword ta shola     # Unknown word
mia ta ta shola         # Double tense
hi nu mia ta shola      # Conflicting evidentiality
ma ma mia ta thilu      # Double emphasis
```

## Advanced Features

### Custom Test Categories
You can easily add your own test categories by modifying the `_build_test_categories()` method:

```python
"my_custom_tests": [
    ("sentence", "description", expected_valid),
    # Add your test sentences here
]
```

### Result Analysis
The framework provides detailed JSON output for programmatic analysis:

```python
{
  "categories": {
    "basic_sentences": {
      "total": 7,
      "correct": 7,
      "incorrect": 0,
      "details": [...]
    }
  },
  "summary": {
    "total_tests": 150,
    "total_correct": 145,
    "overall_accuracy": 96.7
  }
}
```

### Integration with Development
- **Regression testing**: Run after validator changes
- **Feature validation**: Test new grammatical rules
- **Performance benchmarking**: Measure validation speed
- **Error analysis**: Identify validation gaps

## Best Practices

### For Learning Phi Grammar
1. Start with `basic_sentences` to understand fundamentals
2. Progress through `particle_combinations` for common patterns
3. Explore `complex_particles` for advanced usage
4. Test your own sentences interactively

### For Validator Development
1. Run `error_cases` to ensure proper error detection
2. Use `edge_cases` to test robustness
3. Add new test categories for new features
4. Save results for comparison across versions

### For Linguistic Analysis
1. Focus on specific categories (e.g., `evidentiality`, `discourse`)
2. Analyze error patterns in complex sentences
3. Use quiet mode for batch processing
4. Export results for statistical analysis

## Troubleshooting

### Common Issues
- **Import errors**: Ensure you're in the `source/` directory
- **Hanging**: Use direct imports, avoid package-level imports
- **Unknown words**: Check if test sentences use valid Phi vocabulary

### Performance Tips
- Use `--quiet` for faster batch processing
- Run specific categories instead of all tests for focused testing
- Save results to avoid re-running expensive tests

## Conclusion

The exercise framework provides a comprehensive way to:
- **Validate** the sentence validator's accuracy
- **Explore** Phi grammar systematically
- **Test** new sentences interactively
- **Analyze** validation patterns and errors

With 150+ carefully crafted test sentences covering all aspects of Phi grammar, this framework ensures thorough validation of the sentence validator while providing an excellent tool for exploring the Phi language! 