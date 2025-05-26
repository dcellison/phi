---
tags:
  - validation
  - examples
  - usage
  - python
---
# phi validation tool usage examples

> practical examples demonstrating the Python algorithmic validation system
> for ensuring 100% compliance with phi's phonotactic patterns and lexical rules.

## installation and setup

**requirements**: Python 3.7+ with standard library only

**setup**:
```bash
cd source/
chmod +x phi_validator.py
```

**directory structure**:
```
source/
├── phi_validator.py          # main validation script
├── pos/                      # lexicon files
│   ├── verbs.md
│   ├── adjectives.md
│   ├── nouns.md
│   └── ... (other POS files)
└── validation-examples.md    # this file
```

---

## basic usage examples

### example 1: validate a new verb

**command**:
```bash
python phi_validator.py validate "phawi" verb "to fly"
```

**expected output**:
```
WORD VALIDATION REPORT
======================
Word: phawi
Intended POS: verb
Proposed meaning: to fly

OVERALL STATUS: VALID

PHONOTACTIC VALIDATION:
  ✓ All phonotactic patterns valid

LEXICAL VALIDATION:
  ✓ No lexical conflicts detected

✅ APPROVED: Word ready for lexicon integration
```

**pattern breakdown**:
- `ph` (fricative) + `a` (vowel) + `w` (consonant) + `i` (vowel)
- follows [F][V][C][V] verb pattern perfectly
- no conflicts with existing lexicon

### example 2: detect pattern violation

**command**:
```bash
python phi_validator.py validate "palawi" verb "to sing"
```

**expected output**:
```
WORD VALIDATION REPORT
======================
Word: palawi
Intended POS: verb
Proposed meaning: to sing

OVERALL STATUS: INVALID

PHONOTACTIC VALIDATION:
  [INVALID] Verb must start with fricative digraph, got: pa

LEXICAL VALIDATION:
  ✓ No lexical conflicts detected

❌ REJECTED: Fix errors before resubmission
```

**issue**: verbs must start with fricative digraph (ph, wh, th, sh), not consonant

### example 3: detect lexical conflict

**command**:
```bash
python phi_validator.py validate "phela" verb "to suggest"
```

**expected output**:
```
WORD VALIDATION REPORT
======================
Word: phela
Intended POS: verb
Proposed meaning: to suggest

OVERALL STATUS: CONFLICT

PHONOTACTIC VALIDATION:
  ✓ All phonotactic patterns valid

LEXICAL VALIDATION:
  [CONFLICT] Word 'phela' already defined in verb: die

❌ REJECTED: Fix errors before resubmission
```

**issue**: `phela` already exists meaning "die"

### example 4: validate complex noun

**command**:
```bash
python phi_validator.py validate "phuithui" noun "mud"
```

**expected output**:
```
WORD VALIDATION REPORT
======================
Word: phuithui
Intended POS: noun
Proposed meaning: mud

OVERALL STATUS: VALID

PHONOTACTIC VALIDATION:
  ✓ All phonotactic patterns valid

LEXICAL VALIDATION:
  ✓ No lexical conflicts detected

✅ APPROVED: Word ready for lexicon integration
```

**pattern breakdown**:
- `ph` (fricative) + `ui` (vowel pair) + `th` (fricative) + `ui` (vowel pair)
- follows [C/F][V/P][F][P] noun pattern correctly

---

## batch validation examples

### example 5: batch validation file

**create `new_words.txt`**:
```
# Format: word,pos,meaning
phawi,verb,to fly
hasui,adjective,purple
tephao,noun,mountain
napine,adverb,quickly
whuao,preposition,behind
```

**command**:
```bash
python phi_validator.py batch new_words.txt
```

**expected output**:
```
Line 2: hasui - INVALID
  Adjective must have exactly 4 components, got 3
Line 3: tephao - INVALID  
  Fourth component must be vowel pair, got: o
Line 4: napine - CONFLICT
  Word 'napine' already defined in adverb: quickly
```

**analysis**:
- `phawi`: ✅ valid verb
- `hasui`: ❌ adjective needs [C][V][F][V] pattern, got [C][V][C][V] 
- `tephao`: ❌ noun needs vowel pair at end, `o` is single vowel
- `napine`: ❌ already exists in lexicon
- `whuao`: ✅ valid preposition [F][P] pattern

---

## lexicon integrity checking

### example 6: check entire lexicon

**command**:
```bash
python phi_validator.py check-lexicon
```

**expected output**:
```
LEXICON INTEGRITY REPORT
========================
Total words: 1075
Pattern violations: 0
Homonym conflicts: 0

✅ Lexicon integrity maintained
```

### example 7: detect integrity issues

**hypothetical output with problems**:
```
LEXICON INTEGRITY REPORT
========================
Total words: 1075
Pattern violations: 2
Homonym conflicts: 1

PATTERN VIOLATIONS:
  thamus (adjective): ['Adjective must have exactly 4 components, got 6']
  phimel (noun): ['Fourth component must be vowel pair, got: l']

HOMONYM CONFLICTS:
  mipho: [('adjective', 'blue'), ('noun', 'blueness')]
```

---

## advanced usage patterns

### example 8: systematic word creation workflow

**step 1**: determine requirements
```bash
# need verb for "to swim"
# verb pattern: [F][V][C][V]
```

**step 2**: construct systematically
```bash
# [F] = fricative → choose 'sh'
# [V] = vowel → choose 'u'  
# [C] = consonant → choose 'w'
# [V] = vowel → choose 'i'
# result: shuwi
```

**step 3**: validate
```bash
python phi_validator.py validate "shuwi" verb "to swim"
```

**step 4**: check result
```
✅ APPROVED: Word ready for lexicon integration
```

### example 9: pattern space analysis

**checking verb pattern saturation**:
```python
# Verb pattern [F][V][C][V] combinations:
# F = 4 fricatives (ph, wh, th, sh)
# V = 5 vowels (i, u, e, o, a)
# C = 9 consonants (h, l, m, n, p, r, s, t, w)  
# V = 5 vowels
# Total: 4 × 5 × 9 × 5 = 900 possible verbs

# Current verb count: 171 words
# Saturation: 171/900 = 19% (plenty of space remaining)
```

### example 10: debugging common errors

**forbidden vowel pairs**:
```bash
python phi_validator.py validate "phiithui" noun "water"
# ❌ Forbidden vowel pair: ii
```

**duplicate syllables**:
```bash
python phi_validator.py validate "phiaphi" noun "light"  
# ❌ Duplicate syllables found
```

**wrong pattern for part of speech**:
```bash
python phi_validator.py validate "sha" verb "to see"
# ❌ Verb too short: 3 chars (minimum 4)
```

---

## integration with development workflow

### pre-commit validation

**git hook example**:
```bash
#!/bin/bash
# .git/hooks/pre-commit

echo "Validating phi vocabulary..."
python source/phi_validator.py check-lexicon

if [ $? -ne 0 ]; then
    echo "❌ Validation failed - commit blocked"
    exit 1
fi

echo "✅ Validation passed"
```

### automated testing

**continuous integration**:
```yaml
# .github/workflows/phi-validation.yml
name: Phi Vocabulary Validation

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Validate lexicon integrity
      run: python source/phi_validator.py check-lexicon
```

### lesson content validation

**validate lessons before publication**:
```bash
# extract phi words from lesson files
grep -o "`[a-z][a-z]*`" lessons/*.md > lesson_words.txt

# batch validate against lexicon
python phi_validator.py batch lesson_words.txt
```

---

## troubleshooting guide

### common validation errors

**"Unknown part of speech"**:
- solution: use standard POS names (verb, noun, adjective, etc.)
- check spelling of part-of-speech argument

**"Invalid character in word"**:
- solution: only use phi phonemes (h,l,m,n,p,r,s,t,w + i,u,e,o,a)
- remove non-phi characters

**"Closed syllable detected"**:
- solution: ensure all syllables end with vowels
- phi has only open syllables

**"Pattern violations"**:
- solution: follow systematic patterns exactly
- use pattern formulas as construction templates

### performance optimization

**large lexicon handling**:
- tool loads entire lexicon into memory for fast validation
- typical 1,000+ word lexicon loads in <1 second
- batch validation processes 100+ words per second

**file structure requirements**:
- POS files must be in `pos/` directory
- files must follow `| word | meaning |` table format
- encoding must be UTF-8

---

## validation best practices

### systematic word creation

1. **pattern first**: start with correct phonotactic pattern
2. **components second**: select valid phonemes systematically  
3. **validate immediately**: check compliance before proceeding
4. **test contextually**: verify word works in sentences

### quality assurance

1. **pre-validation**: check patterns before semantic assignment
2. **batch processing**: validate multiple candidates simultaneously
3. **lexicon monitoring**: regular integrity checks
4. **documentation sync**: ensure all content uses validated vocabulary

### collaborative development

1. **shared validation**: all contributors use same tool
2. **version control**: track validation reports in git
3. **issue tracking**: document and resolve validation conflicts
4. **systematic reviews**: pattern compliance in code reviews

---

**systematic compliance**: this Python validation tool provides automated
verification of phi's strict phonotactic and lexical rules, ensuring 100%
systematic integrity as the language scales beyond 1,000+ words. 