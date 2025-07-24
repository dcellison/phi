# The Book of Phi: Project Briefing & Status

This document summarizes the current status, workflow, and critical design decisions for the "Book of Phi" project. It is intended to bootstrap any new session and ensure continuity.

## 1. High-Level Goal

Our objective is to write a complete, book-length manuscript that is both a comprehensive guide to the Phi language and a deep exploration of its underlying philosophy. The book should be written with a literary, evocative, and expository tone, not as a dry technical manual.

## 2. Collaborative Workflow

We have established a strict, paragraph-by-paragraph collaborative workflow to ensure the necessary depth and quality of the text.

1.  **Outline Section:** For each new section of a chapter, a detailed, paragraph-by-paragraph outline will be proposed.
2.  **Approve Outline:** The user provides feedback and approval on the outline before any prose is written.
3.  **Draft Paragraph:** Each paragraph is drafted and presented individually for feedback and approval.
4.  **Assemble Section:** Only after all paragraphs for a section are approved will they be assembled into a single file.

## 3. Book Structure

The manuscript is organized into a nested directory structure:

`book/partX_name/XX_chapter_name/YY_section_name.md`

-   **Example:** `book/part1_soul/01_Introduction/01_The_Invisible_Architecture.md`

## 4. Current Status (as of session end on 2024-05-18)

-   **Part I: The Soul of the Language**
    -   **Chapter 1: An Invitation to a More Mindful World** - **Complete.** All sections have been written and approved to the new "book-length" standard.
    -   **Chapter 2: The Five Pillars of Wisdom** - **Complete.** All sections have been rewritten and approved to the new standard.
    -   **Chapter 3: Sound and Soul - A Guide to Pronunciation** - **Complete.** All sections have been written and approved.

-   **Part II: The Grammar of Being**
    -   **Chapter 4: The Mindful Sentence** - **In Progress.** We have just completed a major refactoring of the language's case and conjunction system. We are now ready to begin writing Chapter 4, starting with the first section, `01_The_Verb-Final_Worldview.md`.

## 5. Critical Grammatical & Phonotactic Rules

The following rules have been established after extensive refactoring and are non-negotiable for ensuring the language's consistency.

1.  **Particles:**
    -   **Structure:** Always a single `CV` or `FV` syllable (e.g., `wa`, `no`, `she`, `pi`).
    -   **Function:** Grammatical markers that always **precede** their target. They are not conjunctions or prepositions.

2.  **Prepositions (formerly Postpositions/Case Markers):**
    -   **Structure:** Always a two-syllable word with a **`CV.V` (Consonant-Vowel Pair)** structure (e.g., `mua`, `wei`, `lao`).
    -   **Function:** This unique phonetic signature makes them instantly recognizable. They are **not particles**. They always come **before** the noun phrase they modify (e.g., `mua hauno` - "in the house"). This makes the language's head-final grammar perfectly consistent.

3.  **Conjunctions:**
    -   **Structure:** Always a two-syllable word with a **`CV.CV`** structure (e.g., `nela`, `thona`, `sola`).
    -   **Function:** Their unique phonetic signature distinguishes them from particles and prepositions. They link two grammatically equal elements.

4.  **Magnitudes (The One Exception):**
    -   The number magnitudes (`toa`, `nui`, `lae`, etc.) are the **only** class of words, other than prepositions, that are allowed to use the `CV.V` structure. This is a known and accepted exception. 