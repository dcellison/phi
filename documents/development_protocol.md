# The Phi Development Protocol

## Overview
Phi is a constructed auxiliary language designed to promote mindful, peaceful communication through its phonological, grammatical, and philosophical structure. Every aspect—from individual sounds to sentence patterns—serves to slow speech, encourage reflection, and embody non-violence.

This protocol binds anyone developing the language — coining words, extending grammar, or writing its documents. The authority order for every claim is `/canon.md`.

## The Organizing Principle: Modifier-First

Phi is governed by a single, exceptionless principle that supersedes traditional grammatical categories:

**Every element that modifies, specifies, or relates another element comes BEFORE what it affects.**

This "announce then deliver" principle creates transparent communication where all grammatical relationships are declared before their content. It applies universally to:
- Verbs after objects (SOV word order)
- Particles before words
- Adjectives before nouns
- Possessors before possessed
- Prepositions before objects
- Quantifiers before nouns
- Dependent clauses before main clauses

**This is not just syntax—it's embodied philosophy.** Every sentence becomes practice in announcing intent before action, fostering conscious communication.

## Core Constraints Checklist

### Phonological Requirements
- [ ] **Uses only permitted sounds**: C={h,k,l,m,n,p,r,s,t,w}, F={ph,th,sh,wh}, V={a,e,i,o,u}
- [ ] **The fricative digraphs (F) are**: ph=/φ/, th=/θ/, sh=/ʃ/, wh=/ʍ/
- [ ] **Follows (C)CV structure**: Single consonants OR fricative digraphs only
- [ ] **Maintains vowel hiatus**: Each vowel = separate syllable (no diphthongs)
- [ ] **Vowel hiatus transcription**: Always show syllable breaks with dots: au=/a.u/, not /au/
- [ ] **Respects three-vowel constraint**: Never VVV+ sequences
- [ ] **No duplicate syllables**: Cannot repeat same CV unit within word
- [ ] **Begins with consonant**: All words start with C or F
- [ ] **Ends with vowel**: All syllables are open
- [ ] **Dental articulation**: /t/ and /n/ are dental, not alveolar

### Structural Hierarchy
The full function-word shape charter is a canon ruling (see `/canon.md`); the checklist summarizes it.
- [ ] **Single syllable (CV)**: Reserved for particles and base numerals (mu, ta, wi); particles never take fricative digraphs
- [ ] **Hiatus disyllable ((C)V.V)**: The relator shape — prepositions (mua, thue, wei), core pronouns (mia, thia, shia), clause-relators (lao, pheo, phoe, shai), and scale units (shao, phoi)
- [ ] **Plain disyllable (CV.CV)**: The frame shape — complementizers (openers -a, closers -o), frame conjunctions, classifiers, the vocative, and the -so pronoun pair (miso, wiso)
- [ ] **Multi-syllable**: Required for content words; quantifiers, discourse markers (fricative-initial — the breath before reframing), and interrogatives are content-shaped (2-3 syllables)

### Sound Symbolism Alignment
- [ ] **Fricatives (ph,th,sh,wh)**: Abstract, philosophical, or gentle concepts
- [ ] **Liquids (l,r,w)**: Flow, connection, continuity
- [ ] **Nasals (m,n)**: Grounding, stability, internality
- [ ] **Stops (p,t,k)**: Clear boundaries, definition (use sparingly)
- [ ] **Vowel progression**: Consider emotional arc (e.g., closed→open = restriction→freedom)
- [ ] **Word length**: Length is part of the symbolism. Two syllables suit the everyday and near-at-hand (the household's words: womu, melu, nila); three syllables are the lexicon's broad middle; four syllables are for what is vast, slow, gentle, or worth lingering on (toremoa, thaeluro, shelomui, loamira). Phi spends breath where breath is deserved — never shorten a word at the cost of its meaning's weight

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
- [ ] **Prefer holistic concepts**: Combine rather than separate (e.g., womu = house+belonging, the dwelling-heart)
- [ ] **Use compositional strategies**: Build complex ideas from simple roots
- [ ] **Enable transmutation**: Concepts should reframe, not just translate (rebuild ideas from ground up using Phi concepts)
- [ ] **Maintain value neutrality**: Let speakers map to their own cultural understanding
- [ ] **Create semantic families**: Build interconnected word networks where shared roots illuminate meanings (mycelial approach)

## Word Creation Protocol

### Step 1: Conceptual Analysis
- What core human value/experience does this represent?
- Can this be composed from existing words?
- How does this concept support peaceful/mindful communication?

### Step 2: Sound Selection
- Choose sounds that embody the concept's feeling
- Ensure phonological rules are met
- **Run the collision check**: `python3 scripts/validate_examples.py neighbors <candidate>`
  - REJECT any candidate at edit distance 1 from an existing word of the same part-of-speech class (content vs. the same function class)
  - Cross-class distance-1 neighbors are allowed only when position disambiguates (particle vs. content word) — note them in `grammatical_notes`
  - For natural opposites (left/right, give/take), prefer maximal phonetic dissimilarity, never a minimal pair
  - Prefer three or more syllables unless the concept truly belongs to the daily round: the two-syllable space is the most collision-congested (≈5,200 legal forms, heavily grandfathered), while three syllables offer ≈377,000 and four are effectively inexhaustible

### Step 3: Hiatus Check
- Map all syllable breaks (use dots: CV.V.CV)
- Verify no VVV sequences
- Confirm pronunciation maintains pure vowels

### Step 4: Philosophical and Relational Alignment
- Write explicit connections to relevant pillars
- Craft sound_symbolism description
- Ensure grammatical_notes explain usage
- **Identify semantic family**: What roots does this share? What words does it illuminate?
- **Check transmutation quality**: Does this enable reframing concepts, not just renaming?

### Step 5: Compositional Testing
- Can this word combine with others meaningfully?
- Does it maintain Phi's aesthetic when spoken?
- Does it slow speech appropriately for mindfulness?

## Grammar Extension Rules

### When Adding Particles
- [ ] Assign to correct slot (0, 1, or 2)
- [ ] Maintain CV structure for recognizability
- [ ] Respect **Slot 1 stacking order**: Tense > Aspect > Voice > Evidentiality > Modality > Negation
- [ ] Ensure particle ordering remains logical
- [ ] Document interaction with existing particles
- [ ] **See `documents/grammar/particle_reference.md` for complete particle inventory**

### When Creating Constructions
- [ ] Preserve strict SOV order (modifier-first principle)
- [ ] Maintain head-final principle
- [ ] Support compositional transparency
- [ ] Enable mindful sentence building
- [ ] Document how causative `ka` changes structure (agent→subject, subject→object)
- [ ] Document how passive `se` promotes object to subject
- [ ] Verify discourse adverbs position: after Slot 0, before subject

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
- ❌ Creating words that don't fit into semantic families
- ❌ Enabling word-for-word translation rather than transmutation
- ❌ Creating particles that violate slot positioning rules

## Core Philosophy Reminder
Every addition to Phi should make speakers:
- Speak more slowly and deliberately
- Think more carefully about word choice
- Feel the physical practice of peace in articulation (embodied/somatic practice)
- Experience communication as collaborative art
- Connect with the natural world's patterns
- Transform through repetition of gentle, mindful sounds
- Discover semantic families that teach through interconnection
- Practice "transmutation" rather than mere translation

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
- Manual content → `/manual/`
- Focused deep-dives → `/pamphlets/`
- Historical material → `/archive/` (never a reference for current canon)

### Reference Documentation
**Authority order when documents disagree: see `/canon.md`.**
Validate vocabulary and examples before committing:
`python3 scripts/validate_examples.py`

For detailed information, consult:
- **Sound system**: `documents/phonology_rules.md`, `documents/phonetics.md`
- **Complete grammar**: the manual, Parts IV-V (ch9-ch20); inventories in `documents/grammar/`
- **Particle inventory**: `documents/grammar/particle_reference.md`
- **Compound idioms**: `documents/compounds.md`
- **Numeral system**: `documents/grammar/numeral_reference.md`
- **Philosophy**: `documents/language_guide.md`

## Final Reminder
Phi is not merely a language but a practice of conscious communication. Every design decision should support the transformation of speakers toward greater mindfulness, compassion, and connection with all beings. The language itself is the teaching.
