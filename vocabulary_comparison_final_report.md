# Phi Vocabulary Comparison Report

## Executive Summary

This report compares the existing JSON vocabulary files in `/vocabulary/` with the core vocabulary list in `PHI_CORE_VOCABULARY_ALIGNED.md`.

### Key Findings:
- **Core vocabulary target**: 871 words
- **Existing JSON files**: 190 files
- **Exact matches**: 73 words (8.4% coverage)
- **Unmatched existing words**: 16 words
- **Missing core words**: 798 words (91.6% of core vocabulary)

## Exact Matches (73 words)

These existing words exactly match core vocabulary entries and should be retained:

### A-E
- acceptance → shelao
- ancestor → thalume
- appreciation → phalua
- balance → malomi
- celebration → welia
- ceremony → thorea
- child → lopia
- clarity → lia
- community → wenu
- compassion → lothea
- connect → lorea
- connection → lorami
- cooperation → molawi
- courage → thomari
- create → kealo
- descendant → lumira
- difference → melino
- draw → liero
- elder → wheo
- empathy → meloa
- exchange → nowela

### F-L
- faith → pheo
- flow → selu
- freedom → shaloa
- gathering → tholu
- generosity → phaloa
- good → weloa
- gratitude → nalio
- guest → phemi
- harmony → lei
- heal → theala
- hear → hea
- helper → wesoa
- heritage → thanoa
- honesty → solani
- hope → sola
- host → hoa
- humility → lumea
- idea → lau
- joy → siora
- justice → shilei
- kindness → nea
- language → phealu

### M-S
- meaning → reo
- mediator → thereo
- member → wepa
- message → shilu
- neighbor → theko
- offer → phola
- parent → phao
- participant → paka
- partner → weo
- peace → shea
- question → phia
- respect → nawea
- ritual → thela
- service → heloa
- share → phowe
- sharing → shewe
- speak → mio
- steward → theluo
- stewardship → thelua
- story → thoma
- student → shone

### T-Y
- teacher → shoka
- thought → miu
- tradition → therema
- trust → theomi
- truth → theloa
- welcome → homi
- wisdom → noki
- write → themi
- youth → mea

## Unmatched Existing Words (16 words)

These words don't match any core vocabulary entry and should be reviewed for removal:

1. address → korani
2. bond → nolami
3. care → theama
4. caretaker → phalomi
5. clan → thalomi
6. compose → thomalo
7. consensus → wenoa
8. demonstrate → welira
9. excellence → phelio
10. express → mishoa
11. grace → miloa
12. loyalty → sheloni
13. narrate → thomala
14. request → nola
15. speech → themia
16. suggest → sela

## Major Gaps in Core Vocabulary

The following critical core vocabulary categories are missing significant coverage:

### Basic Pronouns & Determiners (0% coverage)
Missing: I, you, he/she/it, we, they, this, that, who, what, where, when, how, not, all, many, some, few, other

### Numbers (0% coverage)
Missing: one through twenty, hundred, thousand, etc.

### Body Parts (0% coverage)
Missing: head, eye, ear, nose, mouth, hand, foot, heart, etc.

### Nature & Environment (0% coverage)
Missing: tree, water, sun, moon, star, earth, sky, rain, wind, fire, etc.

### Basic Verbs (Limited coverage)
Have only: create, connect, draw, heal, hear, offer, share, speak, write
Missing: be, have, do, make, go, come, see, know, think, feel, eat, drink, sleep, live, etc.

### Basic Qualities (Limited coverage)
Have only: good
Missing: big, small, long, short, hot, cold, new, old, etc.

### Time & Space (0% coverage)
Missing: now, then, before, after, today, yesterday, tomorrow, up, down, left, right, etc.

## Recommendations

1. **Immediate Priority**: Create JSON files for the most basic core vocabulary:
   - Personal pronouns (I, you, we, they)
   - Basic verbs (be, have, do, go, come, see)
   - Basic qualities (big, small, hot, cold)
   - Numbers 1-10

2. **Secondary Priority**: Fill in major category gaps:
   - Body parts
   - Nature words
   - Time and space terms
   - Colors

3. **Review Existing Words**: 
   - Keep the 73 exact matches
   - Consider removing or repurposing the 16 unmatched words
   - Review the 101 partial matches to see if any should be adjusted

4. **Coverage Goal**: Work towards at least 50% coverage of the core vocabulary (435 words) as an initial milestone.

## Next Steps

1. Create a systematic plan to generate the missing 798 core vocabulary words
2. Ensure each new word follows the established phonological rules and philosophical principles
3. Maintain consistency with the existing vocabulary structure and JSON schema
4. Consider grouping word creation by semantic categories for efficiency