# Phi Language Development TODO

## COMPLETED: Fix Postposition References in Documentation

### Background
Previously, Phi experimented with postpositions for typological consistency with SOV order, but ultimately returned to prepositions for philosophical and practical reasons. However, some outdated postposition references remained in the codebase.

### Completed Changes
- [x] Convert all vocabulary/function/preposition/\*.json files to use "preposition" terminology
- [x] Update all POS tags to "preposition" 
- [x] Fix all example sentences to use preposition patterns
- [x] Update grammar documentation to reflect preposition usage
- [x] Update book chapters discussing prepositions
- [x] Rework ordinal system: `nu` as particle, `noa` as position noun
- [x] Check all other function words for consistent terminology

### Impact
All documentation now consistently reflects that Phi uses prepositions, maintaining clarity for learners.

## Critical: Ternary Number System Conversion

### Phase 1: Core Implementation
- [ ] Create new base ternary number words:
  - [ ] `mu` (0) - void, emptiness
  - [ ] `ta` (1) - singularity, focus
  - [ ] `wi` (2) - pairing, relationship
  
- [ ] Create ternary position/scale classifiers:
  - [ ] `sha` - "three-group" (3¹ = 3)
  - [ ] `pho` - "nine-group" (3² = 9)
  - [ ] `lau` - "twenty-seven-group" (3³ = 27)
  - [ ] `rei` - "eighty-one-group" (3⁴ = 81)

### Phase 2: Remove Obsolete System
- [ ] Delete base-10 number words (three through nine):
  - [ ] Remove vocabulary/content/three.json
  - [ ] Remove vocabulary/content/four.json
  - [ ] Remove vocabulary/content/five.json
  - [ ] Remove vocabulary/content/six.json
  - [ ] Remove vocabulary/content/seven.json
  - [ ] Remove vocabulary/content/eight.json
  - [ ] Remove vocabulary/content/nine.json
  
- [ ] Update existing number words:
  - [ ] Convert zero.json to `mu`
  - [ ] Convert one.json to `ta`
  - [ ] Convert two.json to `wi`

### Phase 3: Documentation Updates
- [ ] Update documents/grammar/06-numerals.md for ternary system
- [ ] Update book/part2_grammar sections on numerals
- [ ] Update all example sentences using numbers
- [ ] Create new guide for ternary counting mindfulness

## Critical: Missing Core Vocabulary

### Classifier Words (Documented but Never Created!)
These are referenced throughout the documentation but don't exist:
- [ ] `himo` - classifier for people
- [ ] `lipha` - classifier for living things  
- [ ] `themo` - classifier for inanimate objects
- [ ] `nophe` - classifier for abstract concepts

### Essential Verbs (Perception & Cognition)
Continuing from completed words (know, think, feel):
- [ ] want
- [ ] need
- [ ] like
- [ ] love (verb)

### Other Missing Core Vocabulary
Check MINIMAL_VIABLE_VOCABULARY.md for other critical gaps:
- [ ] Basic time words (day, night, etc.)
- [ ] Common foods/objects
- [ ] Essential descriptors

## Philosophical Documentation

### Completed
- [x] TERNARY_NUMBER_SYSTEM.md - Full conceptual framework
- [x] PSYCHOLOGICAL_VIOLENCE_OF_MEASUREMENT.md - Philosophical rationale
- [x] Integration with Five Pillars documented

### Needed
- [ ] Practical guide for approximate expression
- [ ] Cultural practices around ternary counting
- [ ] Examples of resistance to quantification

## Technical Implementation

### Lexicon Management
- [ ] Run full sync after adding new words
- [ ] Validate all phonological constraints
- [ ] Check for word conflicts

### Testing
- [ ] Create example texts using ternary numbers
- [ ] Validate all grammar examples still work
- [ ] Test classifier + number combinations

## Notes

**Why Ternary?** 
The shift from base-10 to ternary is fundamental to Phi's philosophy. It makes precise counting difficult beyond human-scale quantities (27), encouraging approximation and reducing the psychological violence of precise measurement. This aligns with Buddhist non-attachment, indigenous "one-two-many" counting, and solarpunk resistance to growth-for-growth's-sake.

**Classifier Gap:**
The classifier system is extensively documented in the book and grammar but the actual words were never created. This is a critical gap that makes many example sentences invalid.

**Integration:**
The ternary position markers (sha, pho, lau, rei) work alongside nature classifiers (himo, lipha, themo, nophe) to create two types of mindful counting:
- Nature classifiers: conscious of WHAT you're counting
- Scale classifiers: conscious of HOW MUCH you're counting

---
*Last updated: 2025-09-09*
*Priority: Implement ternary numbers and missing classifiers before adding new vocabulary*
