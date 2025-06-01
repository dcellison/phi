# Phi Validation Test Suite

## Overview

This comprehensive test suite validates all modules of the Phi sentence validation system. It provides thorough coverage of validation logic, edge cases, and integration testing.

## Test Structure

### Individual Module Tests

The test suite includes dedicated test classes for each validation module:

1. **TestLexiconValidator** - Word existence and type identification
2. **TestParticleValidator** - Particle ordering and scope validation
3. **TestWordOrderValidator** - SOV structure validation
4. **TestTemporalValidator** - Tense, aspect, and temporal logic
5. **TestSemanticRoleValidator** - Animacy, classifiers, and verb arguments
6. **TestModalityValidator** - Modal logic and constructions
7. **TestEvidentialityValidator** - Evidentiality particles and combinations
8. **TestDerivationalValidator** - se/ra constructions
9. **TestEmphasisValidator** - ma particle scope validation
10. **TestPolitenessValidator** - so particle context validation
11. **TestDiscourseValidator** - ha/mi discourse sequences
12. **TestInterrogativeValidator** - Question structure validation
13. **TestNarrativeValidator** - Temporal sequences and relative clauses

### Integration Tests

- **TestPhiSentenceValidatorIntegration** - End-to-end sentence validation
- **TestErrorHandling** - Edge cases and error handling

## Running the Tests

### Run All Tests
```bash
python3 test_phi_validation.py
```

### Run Specific Test Classes
```bash
python3 -m unittest test_phi_validation.TestLexiconValidator
python3 -m unittest test_phi_validation.TestParticleValidator
# etc.
```

### Run Individual Tests
```bash
python3 -m unittest test_phi_validation.TestLexiconValidator.test_valid_words
```

## Test Coverage

The test suite covers:

### ✅ Core Functionality (68 tests total)
- **Lexicon validation**: Word existence, type identification
- **Particle validation**: Ordering, scope, interactions
- **Word order**: SOV compliance, verb positioning
- **Temporal logic**: Tense/aspect compatibility, temporal sequences
- **Semantic roles**: Animacy agreement, classifier compatibility
- **Modal logic**: Obligative, conditional, desiderative constructions
- **Evidentiality**: Particle combinations, tense interactions, nesting
- **Derivational**: se/ra constructions, scope, semantics
- **Emphasis**: ma particle scope and interactions
- **Politeness**: so particle context and appropriateness
- **Discourse**: ha/mi sequences and topic-contrast interactions
- **Interrogative**: Question structures and tense appropriateness
- **Narrative**: Temporal sequences and relative clause consistency

### ✅ Integration Testing
- Simple valid sentences
- Complex multi-particle sentences
- Error detection and reporting
- Edge cases and error handling

### ✅ Error Handling
- Empty sentences
- Unknown words
- Invalid constructions
- Whitespace and punctuation handling
- Case insensitivity

## Test Results

**Current Status: 100% Success Rate**
- Tests run: 68
- Failures: 0
- Errors: 0
- Success rate: 100.0%

## Example Test Cases

### Valid Sentences
```python
'mia ta thilu'                    # I present be
'hi so he thephoa ta shola'       # direct-evidence politeness human person present walk
'wa mia ta shola'                 # question I present walk
'ma mia ta thilu'                 # emphasis I present be
```

### Invalid Constructions
```python
'so hi mia ta shola'              # wrong particle order
'ma ma mia ta shola'              # double emphasis
'wa hamite mia ta shola'          # wa + wh-word conflict
```

## Test Architecture

### Modular Design
Each validation module has its own test class with:
- Setup methods for test fixtures
- Individual tests for specific functionality
- Error case validation
- Edge case handling

### Comprehensive Coverage
Tests validate:
- **Positive cases**: Valid constructions work correctly
- **Negative cases**: Invalid constructions are properly detected
- **Edge cases**: Boundary conditions and unusual inputs
- **Integration**: Modules work together correctly

### Realistic Test Data
All test cases use:
- Real Phi vocabulary from the lexicon
- Authentic grammatical constructions
- Proper particle ordering
- Valid phonotactic patterns

## Adding New Tests

### For New Modules
1. Create a new test class inheriting from `unittest.TestCase`
2. Add setup method with test fixtures
3. Write individual test methods for each feature
4. Add the class to the test suite in `run_test_suite()`

### For New Features
1. Add test methods to existing relevant test class
2. Follow naming convention: `test_feature_description`
3. Include both positive and negative test cases
4. Document expected behavior in docstrings

## Debugging Failed Tests

### View Detailed Output
```bash
python3 test_phi_validation.py -v
```

### Run Single Failing Test
```bash
python3 -m unittest test_phi_validation.TestClassName.test_method_name -v
```

### Debug Validation Results
```python
from phi_validation.core import PhiSentenceValidator
validator = PhiSentenceValidator()
result = validator.validate_sentence('your test sentence')
print(f"Valid: {result['is_valid']}")
for error in result['errors']:
    print(f"  {error.error_type.value}: {error.message}")
```

## Continuous Integration

The test suite is designed for:
- **Automated testing**: Can be run in CI/CD pipelines
- **Regression detection**: Catches breaking changes
- **Quality assurance**: Ensures validation accuracy
- **Documentation**: Tests serve as usage examples

## Performance

- **Fast execution**: ~0.1 seconds for full suite
- **Efficient loading**: Lexicon loaded once per test class
- **Minimal overhead**: Focused on validation logic testing
- **Scalable**: Easy to add new tests without performance impact

## Contributing

When contributing to the validation modules:
1. **Write tests first**: Add tests for new functionality
2. **Maintain coverage**: Ensure new features are tested
3. **Update documentation**: Keep test documentation current
4. **Run full suite**: Verify all tests pass before submitting

## Validation Philosophy

The test suite embodies the validation system's philosophy:
- **Comprehensive**: Cover all aspects of Phi grammar
- **Accurate**: Reflect true Phi linguistic rules
- **Maintainable**: Clear, well-documented test code
- **Reliable**: Consistent, reproducible results