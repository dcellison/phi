# Undefined Vocabulary Audit

## Executive Summary

A systematic audit of Phi documentation reveals approximately 77 undefined vocabulary items used throughout tutorials, examples, and grammatical descriptions. These fall into two categories:

1. **Improvised Phi words** (29 items): Words that appear to be Phi but were created without following the proper workflow
2. **English placeholders** (48 items): English words in square brackets awaiting Phi translations

This represents a critical gap in the language's development, as core concepts used to teach the language lack formal definitions.

## The Problem

### Improvised Phi Words
These 29 words appear throughout the documentation as if they were established Phi vocabulary, but they:
- Have no JSON definition files
- Were likely created on-the-fly by LLMs
- May not follow sound symbolism principles
- Lack proper philosophical alignment
- Have no verified etymological transparency

### English Placeholders
These 48 English words appear in square brackets within grammatical examples, indicating where Phi words are needed but don't exist. They appear in critical grammatical explanations, making it impossible to create proper Phi sentences for many basic concepts.

## Category 1: Improvised Phi Words (29 items)

These words appear in Phi examples but have no formal definitions:

### Basic Nouns (10)
1. **phino** - used as "book/text"
2. **noshale** - used as "garden" 
3. **whelea** - used as "friend"
4. **weola** - used as "community"
5. **thola** - used as "story"
6. **shiro** - used as "forest/tree"
7. **mathea** - used as "parent"
8. **liso** - used as "water"
9. **keto** - used as "stone"
10. **pota** - used as "table"

### Verbs (14)
11. **nima** - used as "sleep"
12. **nolea** - used as "read"
13. **shima** - also used as "read" (duplicate concept?)
14. **phela** - used as "grow"
15. **wepu** - used as "leave/depart"
16. **hishe** - used as "believe"
17. **nothe** - used as "decide"
18. **whao** - used as "gather"
19. **thekoa** - used as "build"
20. **tole** - used as "remember"
21. **pholea** - ✅ REPLACED with **kealo** (create)
22. **phera** - used as "rain" (verb)

### Adjectives/Descriptors (3)
23. **nosa** - used as "mindful"
24. **philo** - used as "calm"
25. **miro** - used as "beautiful"

### Abstract Concepts (4)
26. **shalai** - used as "purpose"
27. **sheala** - used as "joy"
28. **welale** - used as "beauty/harmony" (quality)
29. **soli** - used as "several" (quantifier)

### Issues with These Words

**Semantic Problems:**
- **whelea** (friend): Contains 'whe' suggesting wind/breath + 'lea' suggesting path, doesn't convey warmth/connection
- **phera** (rain): Starts with abstract fricative 'phe' but rain is physical
- **keto** (stone): Contains 'ke' (knowledge) + 'to' (past particle), unrelated to stone's nature
- **shima/nolea**: Two different words for "read" suggests lack of coordination

**Sound Symbolism Violations:**
- Physical objects starting with abstract fricatives (ph, th, sh, wh)
- Lack of systematic sound-meaning relationships
- No clear compositional transparency

## Category 2: English Placeholders (48 items)

These English words appear in square brackets in grammatical examples:

### Nature & Environment (11)
1. **forest** - natural area
2. **mountain** - elevation
3. **valley** - depression
4. **river** - water flow
5. **rain/rains** - precipitation
6. **storm** - weather event
7. **fire** - combustion
8. **seed** - plant beginning
9. **tree** - plant
10. **water** - liquid (also in List 1 as "liso")
11. **wood** - tree material

### Time & Seasons (9)
12. **dawn** - day beginning
13. **evening** - day end
14. **night** - darkness period
15. **time** - temporal concept
16. **season** - year division
17. **summer** - warm season
18. **winter** - cold season
19. **ceremony** - ritual event
20. **end** - termination

### Human Concepts (8)
21. **friend/friends** - companion (also in List 1 as "whelea")
22. **elders** - older people
23. **community** - group (also in List 1 as "weola")
24. **miona** - person (actually already exists!)
25. **gift** - given object
26. **home** - dwelling place
27. **house** - structure
28. **town** - settlement

### Objects & Tools (7)
29. **table** - furniture (also in List 1 as "pota")
30. **wall** - barrier
31. **surface** - top layer
32. **hammer** - tool
33. **tools** - implements
34. **object** - thing
35. **tall** - height quality

### Abstract Concepts (13)
36. **understanding** - comprehension
37. **philosophy** - wisdom system
38. **meditation** - practice
39. **realization** - awakening
40. **evidence** - proof
41. **conflict** - discord
42. **fear** - emotion
43. **hope** - emotion
44. **patience** - quality
45. **heart** - center/emotion
46. **good** - quality (already exists as "wela"!)
47. **into** - transformation (not a noun?)
48. **mia** - (pronoun "I", already exists!)

### Duplicates and Errors
- **miona** - already defined as "person"
- **mia** - already defined as "I" 
- **good** - already defined as "wela"
- **into** - preposition, not a noun
- **water** - appears as both "liso" (List 1) and placeholder
- **friend** - appears as both "whelea" (List 1) and placeholder
- **community** - appears as both "weola" (List 1) and placeholder
- **table** - appears as both "pota" (List 1) and placeholder

## Priorities for Resolution

### Tier 1: Most Critical (appear frequently in tutorials)
1. friend/whelea
2. community/weola  
3. water/liso
4. book/phino
5. garden/noshale
6. story/thola
7. sleep/nima
8. read/nolea/shima
9. mindful/nosa
10. create/kealo ✅

### Tier 2: Essential for Basic Communication
11. house/home
12. tree/forest/shiro
13. mountain
14. river
15. time
16. night/day/dawn/evening
17. give (shele exists)
18. take (pilu exists)
19. grow/phela
20. remember/tole

### Tier 3: Important Concepts
21. parent/mathea
22. stone/keto
23. rain/phera
24. purpose/shalai
25. joy/sheala
26. calm/philo
27. beautiful/miro
28. table/pota
29. wall
30. tools

## Recommended Actions

### Immediate Steps
1. **Audit existing words**: Verify which improvised words should be kept vs. replaced
2. **Create core vocabulary**: Use proper 9-pass workflow for Tier 1 words
3. **Establish naming principles**: Ensure systematic sound-meaning relationships

### Systematic Approach
1. **Group related concepts**: Create word families with shared roots
2. **Apply sound symbolism**: Ensure sounds match meanings
3. **Check for conflicts**: Avoid duplicate concepts and conflicting etymologies
4. **Maintain compositionality**: Build complex concepts from simple roots

### Quality Control
1. **Follow workflow**: Use documented 9-pass process for each word
2. **Document decisions**: Explain sound choices and philosophical alignments
3. **Test in context**: Ensure words work in existing examples
4. **Update documentation**: Replace all placeholders with final words

## Estimated Scope

- **Unique concepts needing words**: ~70
- **Time per word** (following proper workflow): ~30 minutes
- **Total time estimate**: ~35 hours of focused work
- **Documentation updates**: Additional 10-15 hours

## Conclusion

This audit reveals that Phi's documentation contains a significant amount of undefined vocabulary, undermining the language's claim to systematic development. The mix of improvised words and placeholders suggests rapid prototyping without proper linguistic consideration.

Resolving this requires:
1. Systematic word creation following established workflows
2. Careful attention to sound symbolism and philosophical alignment
3. Comprehensive documentation updates
4. Quality control to prevent future improvisation

This is not just a vocabulary gap—it's a foundational issue that affects the language's credibility and learnability.