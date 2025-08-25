# Phi Language Development Instructions

## Overview
Phi is a constructed auxiliary language designed to promote mindful, peaceful communication through its phonological, grammatical, and philosophical structure. Every aspect—from individual sounds to sentence patterns—serves to slow speech, encourage reflection, and embody non-violence.

## Core Constraints Checklist

### Phonological Requirements
- [ ] **Uses only permitted sounds**: C={h,k,l,m,n,p,r,s,t,w}, F={ph,th,sh,wh}, V={a,e,i,o,u}
- [ ] **Follows (C)CV structure**: Single consonants OR fricative digraphs only
- [ ] **Maintains vowel hiatus**: Each vowel = separate syllable (no diphthongs)
- [ ] **Respects three-vowel constraint**: Never VVV+ sequences
- [ ] **No duplicate syllables**: Cannot repeat same CV unit within word
- [ ] **Begins with consonant**: All words start with C or F
- [ ] **Ends with vowel**: All syllables are open
- [ ] **Dental articulation**: /t/ and /n/ are dental, not alveolar

### Structural Hierarchy
- [ ] **Single syllable (CV/FV)**: Reserved for particles, pronouns, numerals
- [ ] **Multi-syllable**: Required for content words
- [ ] **Prepositions**: Must follow CV.V pattern (e.g., mua, thue)
- [ ] **Particles**: Simple CV structure for instant recognition

### Sound Symbolism Alignment
- [ ] **Fricatives (ph,th,sh,wh)**: Abstract, philosophical, or gentle concepts
- [ ] **Liquids (l,r,w)**: Flow, connection, continuity
- [ ] **Nasals (m,n)**: Grounding, stability, internality
- [ ] **Stops (p,t,k)**: Clear boundaries, definition (use sparingly)
- [ ] **Vowel progression**: Consider emotional arc (e.g., closed→open = restriction→freedom)

## Philosophical Consistency

### Five Pillars Integration
Each new word must explicitly connect to at least one pillar:
- [ ] **Solarpunk**: Sustainability, regeneration, positive futures
- [ ] **Buddhist concepts**: Mindfulness, impermanence, non-violence
- [ ] **Art Nouveau**: Organic forms, natural beauty, flowing patterns
- [ ] **Peace Linguistics**: Non-aggressive communication, collaboration
- [ ] **Pre-industrial wisdom**: Cyclical thinking, embodied knowledge

### Semantic Principles
- [ ] **Avoid violence**: No direct words for weapons, war, harm
- [ ] **Prefer holistic concepts**: Combine rather than separate (e.g., wela = good+beautiful)
- [ ] **Use compositional strategies**: Build complex ideas from simple roots
- [ ] **Enable transmutation**: Concepts should reframe, not just translate
- [ ] **Maintain value neutrality**: Let speakers map to their own cultural understanding

## Word Creation Protocol

### Step 1: Conceptual Analysis
- What core human value/experience does this represent?
- Can this be composed from existing words?
- How does this concept support peaceful/mindful communication?

### Step 2: Sound Selection
- Choose sounds that embody the concept's feeling
- Ensure phonological rules are met
- Test for inadvertent similarity to existing words

### Step 3: Hiatus Check
- Map all syllable breaks (use dots: CV.V.CV)
- Verify no VVV sequences
- Confirm pronunciation maintains pure vowels

### Step 4: Philosophical Alignment
- Write explicit connections to relevant pillars
- Craft sound_symbolism description
- Ensure grammatical_notes explain usage

### Step 5: Compositional Testing
- Can this word combine with others meaningfully?
- Does it maintain Phi's aesthetic when spoken?
- Does it slow speech appropriately for mindfulness?

## Grammar Extension Rules

### When Adding Particles
- [ ] Assign to correct slot (0, 1, or 2)
- [ ] Maintain CV structure for recognizability
- [ ] Ensure particle ordering remains logical
- [ ] Document interaction with existing particles

### When Creating Constructions
- [ ] Preserve strict SOV order
- [ ] Maintain head-final principle
- [ ] Support compositional transparency
- [ ] Enable mindful sentence building

## Quality Checks

### Pronunciation Test
- Read aloud with full hiatus
- Verify gentle, flowing quality
- Ensure sustainable vocal production
- Check for natural rhythm/musicality

### Philosophical Test
- Does this support peaceful communication?
- Does it encourage mindfulness?
- Does it reflect interconnection/interdependence?
- Does it resist hierarchical/violent framing?

### Learnability Test
- Is the sound-meaning connection intuitive?
- Can the concept be understood compositionally?
- Does it follow all established patterns?
- Will speakers find it beautiful to speak?

## Red Flags to Avoid
- ❌ Creating exceptions to phonological rules
- ❌ Adding irregular grammatical patterns
- ❌ Introducing culturally specific concepts
- ❌ Enabling easy expression of violence/hierarchy
- ❌ Prioritizing efficiency over mindfulness
- ❌ Breaking vowel hiatus for any reason
- ❌ Using consonant clusters beyond F digraphs
- ❌ Creating words that encourage rapid speech

## Core Philosophy Reminder
Every addition to Phi should make speakers:
- Speak more slowly and deliberately
- Think more carefully about word choice
- Feel the physical practice of peace in articulation
- Experience communication as collaborative art
- Connect with the natural world's patterns

**The constraints ARE the teaching. The difficulty IS the practice.**

## Technical Implementation Notes

### When Using JSON Schema
All vocabulary entries must include:
- `word`: The Phi word
- `gloss`: 1-2 word English equivalent
- `ipa`: Full IPA transcription with syllable breaks
- `syllables`: Array of CV units
- `pos`: Array of possible parts of speech
- `concept`: Full conceptual description
- `description`: Detailed semantic explanation
- `sound_symbolism`: How phonetics embody meaning
- `pillars`: Explicit connections to Five Pillars
- `tags`: Add tags after deep assessment

### File Organization
- Content words → `/vocabulary/content/`
- Function words → `/vocabulary/function/`
- Interjection words → `/vocabulary/interjection/`
- Grammar documentation → `/documents/grammar/`
- Python scripts → `/scripts/`
- Book content → `/book/`
- DO NOT access files from any other directory

## Final Reminder
Phi is not merely a language but a practice of conscious communication. Every design decision should support the transformation of speakers toward greater mindfulness, compassion, and connection with all beings. The language itself is the teaching.