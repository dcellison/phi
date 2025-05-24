---
tags:
  - verification
  - lexicon
  - quality-control
---
# vocabulary verification system

> this document establishes systematic procedures for verifying that all phi words 
> used in lessons, examples, and documentation are properly defined in the @pos 
> lexicon, maintaining phi's principle of systematic transparency.

## verification principles

### consistency requirements
- **defined vocabulary only**: all phi words must exist in @pos files
- **accurate definitions**: word usage must match @pos definitions
- **phonotactic compliance**: words must follow their part-of-speech patterns
- **no homonyms**: each phonological form has exactly one meaning

### verification scope
- lesson content and examples
- grammar documentation
- system prompts and guides
- expansion plans and proposals

## verification process

### step 1: extract phi vocabulary

systematically extract all phi words from target files:

#### extraction patterns
- words in gloss blocks: `phi_word` above `english_gloss`
- inline phi text: words in backticks `phi_word`
- example sentences: phi content in code blocks
- vocabulary lists: phi words in tables

#### extraction method
```bash
# search for phi words in gloss blocks
grep -A1 -B1 "^[a-z][a-z]*$" lessons/

# search for backticked phi words  
grep -o "`[a-z][a-z]*`" lessons/

# search for words in examples
grep -o "[a-z][a-z]*" lessons/intermediate/
```

### step 2: compile master lexicon

create comprehensive vocabulary from @pos files:

#### source files
- `pos/adjectives.md` - [C][V][F][V] pattern
- `pos/nouns.md` - [C/F][V/P][F][P] pattern  
- `pos/verbs.md` - [F][V][C][V] pattern
- `pos/adverbs.md` - [C][V][C][V][C][V] pattern
- `pos/prepositions.md` - [F][P] pattern
- `pos/determiners.md` - [F][P][C][V] pattern
- `pos/classifiers.md` - [C][P] pattern
- `pos/conjunctions.md` - [C][V][C][V] pattern
- `pos/interjections.md` - [C][V][C][P] pattern
- `pos/numbers.md` - digits [F][V], magnitudes [F][V][F][V]
- `pos/particles.md` - [C][V] pattern
- `pos/pronouns.md` - exceptions: mia, thi, sha

#### lexicon compilation
```bash
# extract defined words from each pos file
grep "^| [a-z]" pos/*.md | cut -d'|' -f2 | tr -d ' '
```

### step 3: cross-reference verification

compare extracted vocabulary against master lexicon:

#### undefined words check
- words in lessons not found in @pos
- potential typos or phonotactic violations
- words created without lexicon updates

#### definition accuracy check  
- verify word usage matches @pos definitions
- check semantic consistency across examples
- identify context mismatches

#### phonotactic compliance check
- verify words follow part-of-speech patterns
- identify pattern violations
- check systematic consistency

### step 4: conflict detection

identify lexical conflicts and inconsistencies:

#### homonym detection
- multiple definitions for same phonological form
- semantic conflicts within @pos files
- cross-category duplications

#### pattern violations
- words that don't follow phonotactic rules
- exceptional forms without justification
- systematic inconsistencies

## verification results format

### undefined words report
```
UNDEFINED WORDS DETECTED:
- pushe: used in lesson-07 line 52, not found in @pos
- miphe: conflicting definitions (empty/difficult)
- thamu: used in lesson-05, not found in @pos

RECOMMENDATIONS:
- replace pushe → pisha (defined in adjectives)
- resolve miphe conflict (choose one definition)
- add thamu to appropriate @pos file
```

### definition mismatches
```
DEFINITION MISMATCHES:
- hashe: used as "blue" in lesson-06, defined as "green" in @pos
- pisha: used as "hard" in lesson-05, defined as "soft" in @pos

CORRECTIONS NEEDED:
- update lesson-06: hashe → mipho (blue)
- update lesson-05: pisha → tisho (hard)
```

### phonotactic violations
```
PATTERN VIOLATIONS:
- thamus: used as adjective, doesn't follow [C][V][F][V] pattern
- phimel: used as noun, doesn't follow [C/F][V/P][F][P] pattern

ACTIONS REQUIRED:
- replace thamus with compliant adjective
- replace phimel with compliant noun
```

## systematic verification checklist

### pre-publication verification
- [ ] extract all phi words from new content
- [ ] verify against master lexicon
- [ ] check definition accuracy
- [ ] confirm phonotactic compliance
- [ ] resolve any conflicts

### lexicon update verification
- [ ] check new words follow patterns
- [ ] verify no homonym conflicts
- [ ] update master lexicon compilation
- [ ] validate across all documentation

### periodic full verification
- [ ] comprehensive vocabulary extraction
- [ ] complete lexicon cross-reference
- [ ] systematic conflict detection
- [ ] documentation synchronization

## automation recommendations

### verification script structure
```python
# pseudocode for automated verification
def verify_vocabulary():
    lesson_words = extract_phi_words("lessons/")
    pos_lexicon = compile_master_lexicon("pos/")
    
    undefined = find_undefined_words(lesson_words, pos_lexicon)
    conflicts = detect_conflicts(pos_lexicon)
    violations = check_phonotactics(lesson_words)
    
    generate_report(undefined, conflicts, violations)
```

### integration points
- pre-commit hooks for vocabulary verification
- automated lexicon synchronization
- continuous integration checks
- documentation build validation

## quality assurance standards

### acceptance criteria
- zero undefined words in published content
- zero homonym conflicts in @pos lexicon  
- 100% phonotactic compliance
- consistent definition usage

### review process
- vocabulary verification before content review
- lexicon expert approval for new words
- systematic consistency validation
- cross-reference accuracy confirmation

## maintenance procedures

### regular verification schedule
- **weekly**: new content vocabulary check
- **monthly**: comprehensive lesson verification  
- **quarterly**: full lexicon conflict audit
- **annually**: systematic pattern compliance review

### update synchronization
- coordinate @pos updates with lesson revisions
- maintain vocabulary change logs
- propagate corrections across all content
- verify systematic consistency maintenance

this verification system ensures phi maintains its foundational principle of 
systematic transparency through rigorous vocabulary consistency and lexical integrity. 