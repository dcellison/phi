> **⚠️ ARCHIVED — NOT CURRENT CANON.** This document is preserved as
> historical record only. It describes a superseded stage of Phi's design
> and contradicts the current language in places. For current canon, see
> `/CANON.md` at the repository root.

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the **Phi Language Project** - a constructed language designed for peaceful, mindful communication. The project includes a comprehensive book manuscript and language documentation. Phi is built on principles of nonviolence, mindfulness, and ecological harmony, with a systematic sound-meaning correspondence and analytical grammar structure.

## Key Architecture & Design Principles

### 1. Book Writing Workflow
The book follows a strict **paragraph-by-paragraph collaborative workflow**:
1. **Outline Section**: Create detailed paragraph outlines
2. **Approve Outline**: Get user approval before writing prose
3. **Draft Paragraph**: Write individual paragraphs for approval
4. **Assemble Section**: Combine approved paragraphs into complete sections

### 2. Language Design Principles
- **Analytical Structure**: No inflection or derivation - meaning conveyed through word order, particles, and composition
- **Sound-Meaning Correspondence**: Every sound chosen for symbolic value
- **SOV Word Order**: Subject-Object-Verb for mindful, deliberate communication
- **Three-Slot Particle System**: Slot 0 (sentence frame), Slot 1 (verb phrase), Slot 2 (word-level)
- **Philosophical Foundation**: Built on Solarpunk values, Buddhist concepts, Art Nouveau aesthetics, Peace Linguistics, and pre-industrial wisdom

### 3. Phonological System
**Critical grammatical rules (non-negotiable):**
- **Particles**: Always `CV` or `FV` syllables (e.g., `wa`, `no`, `she`, `pi`) - always precede their target
- **Prepositions**: Always `CV.V` structure (e.g., `mua`, `wei`, `lao`) - come before noun phrases
- **Conjunctions**: Always `CV.CV` structure (e.g., `nela`, `thona`, `sola`)
- **Verbs**: Complex phonotactic patterns, often multi-syllabic
- **Magnitudes**: Exception class allowed to use `CV.V` structure

**Phonological Variety Guidelines for Content Words:**
- **Syllable Count**: Maintain approximately 3:1 ratio of two-syllable to three-syllable words
- **Sound Distribution**: Consciously rotate between:
  - Simple consonants (h, k, l, m, n, p, r, s, t, w)
  - Fricative digraphs (ph, th, sh, wh) - these create the "feel" of Phi
  - Vowel pairs/hiatus (e.g., ao, ea, oa, ie) - essential for Phi's character
- **Syllable Patterns**: Avoid defaulting to CV.CV structure. Liberal use of:
  - FV patterns (fricative + vowel)
  - CV.V patterns (vowel hiatus)
  - FV.CV, CV.FV combinations
  - Three-syllable words with varied patterns
- **Phonological Diversity**: Each new word should sound distinct from existing vocabulary

### 4. Compositional Vocabulary
- **Holistic Concepts**: Single words encompass interconnected meanings (e.g., `wela` = good/beautiful/harmonious)
- **Compositional Building**: Complex ideas built from simple core concepts (e.g., `nima thola` = "sleep-story" = dream)
- **Values-Based Design**: Vocabulary reflects peaceful, sustainable, mindful worldview

## File Structure

### Core Directories
- `book/` - Book manuscript organized by parts and chapters
  - `part1_soul/` - Philosophy and sound system
  - `part2_grammar/` - Grammar and syntax
- `documents/` - Reference materials and tutorials
  - `grammar/` - Technical grammar specification
  - `guides/` - Learning guides and tutorials
  - `tutorial/` - Lesson-by-lesson instruction
- `lexicon/` - JSON vocabulary files organized by semantic category
- `grammar/` - JSON files with particles, prepositions, conjunctions, etc.

### Key Files
- `BOOK_PROJECT_BRIEFING.md` - Project status and workflow
- `documents/language_guide.md` - Core philosophy and introduction
- `documents/phonology_rules.md` - Complete phonological system
- `documents/grammar/README.md` - Grammar documentation overview
- `schema.json` - JSON schema for lexicon entries

## Book Development Status

**Current Status (per BOOK_PROJECT_BRIEFING.md):**
- **Part I: The Soul of the Language** - Complete
  - Chapter 1: An Invitation to a More Mindful World ✓
  - Chapter 2: The Five Pillars of Wisdom ✓
  - Chapter 3: Sound and Soul - A Guide to Pronunciation ✓
- **Part II: The Grammar of Being** - In Progress
  - Chapter 4: The Mindful Sentence - Starting with `01_The_Verb-Final_Worldview.md`

## Working with the Language

### Core Vocabulary Structure
Lexicon files are organized by semantic domains in `/lexicon/`:
- `verbs/` - Organized by semantic categories (motion, cognition, etc.)
- `colors.json`, `emotions.json`, `environment.json` - Thematic vocabulary
- `numerals.json`, `quantifiers.json` - Number system
- `social_units.json` - Community and relationship terms

### Grammar Files
Systematic grammatical elements in `/grammar/`:
- `particles.json` - Three-slot particle system
- `prepositions.json` - Spatial and temporal relations
- `conjunctions.json` - Coordination and subordination
- `pronouns.json` - Personal and demonstrative pronouns

### JSON Schema
All lexicon entries follow the schema defined in `schema.json`:
```json
{
  "word": "string",          // The Phi word
  "gloss": "string",         // 1-2 word English gloss or Leipzig abbreviation
  "ipa": "string",           // IPA transcription with stress marks and syllable breaks
  "syllables": ["array"],    // Word broken into CV syllables for validation
  "slot": integer/null,      // Particle slot position (null for content words)
  "pos": ["array"],          // Parts of speech (e.g., "noun", "verb", "particle")
  "concept": "string",       // Full concept name from unified concepts document
  "description": "string",   // Detailed meaning and nuance
  "rationale": "string",     // Phonetic construction reasoning
  "pillars": ["array"],      // Philosophical pillars (enum: solarpunk, buddhist, art-nouveau, peace-linguistics, pre-industrial)
  "tags": ["array"]          // Categorical tags (e.g., "Being & Becoming")
}
```
All fields except `slot` are required. The `slot` field is only used for grammatical particles.

### Lexicon Creation Guidelines (for 1000-word core vocabulary)
When creating new Phi words:
1. **Original Words Only**: Do not pull from previous versions of Phi - create completely fresh words
2. **Syllable Ratio**: Maintain a 3:1 ratio of two-syllable to three-syllable words
3. **Rhotic 'r' Usage**: Use sparingly, only for special flair - it's challenging for many speakers
4. **Pillar Flexibility**: Re-evaluate and assign pillars based on the word's actual philosophical connections
5. **Specific Tags**: Use multiple, specific tags that capture different dimensions of the concept (e.g., "Aesthetic Experience", "Visual Harmony", "Natural Forms")
6. **Parts of Speech**: List ALL possible parts of speech the word could serve in Phi's analytical structure

## Development Guidelines

### Language Consistency
- **Phonological Patterns**: Every word must follow established phonotactic rules for its part of speech
- **Particle Precedence**: Particles always precede their targets, never follow
- **Head-Final Structure**: Maintain consistent SOV/head-final word order
- **Compositional Logic**: Build complex concepts from simple, intuitive components

### Writing Standards
- **Literary Tone**: Book should be evocative and philosophical, not dry or technical
- **Paragraph-by-Paragraph**: Follow strict collaborative workflow for book writing
- **Values Integration**: Ensure all content reflects Phi's peaceful, mindful philosophy
- **Technical Accuracy**: All linguistic examples must follow established grammatical rules

## Notes for Development

This is a **documentation and manuscript project** - the codebase contains structured content files (JSON, Markdown) rather than executable code. Focus on:
- Maintaining consistency across language documentation
- Following the established book writing workflow
- Preserving the philosophical integrity of the language design
- Ensuring all examples follow phonological and grammatical rules