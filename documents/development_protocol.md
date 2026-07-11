# The Phi Development Protocol

## Overview
Phi is a philosophical constructed language for reflective writing and discussion. It is not intended as a universal auxiliary language. Its phonology, grammar, lexicon, and teaching practices invite deliberate, cooperative communication; these are design intentions to test in use, not guarantees about what the language does to a speaker.

This protocol binds the maintainer and anyone contributing to the language: coining words, extending grammar, or writing its documents. The authority order for every claim is `/canon.md`. While Phi has one maintainer, significant choices are recorded in `documents/development_log.md`; a public RFC process is deferred until recurring users make one useful.

## The Organizing Principle: Modifier-First

Phi is organized by one modifier-first principle that reaches across traditional grammatical categories:

**Every element that modifies, specifies, or relates another element comes BEFORE what it affects.**

This "announce then deliver" principle creates transparent communication where all grammatical relationships are declared before their content. It applies universally to:
- Verbs after objects (SOV word order)
- Particles before words
- Adjectives before nouns
- Possessors before possessed
- Prepositions before objects
- Quantifiers before nouns
- Dependent clauses before main clauses

**This is syntax used as philosophical practice.** Every sentence can rehearse announcing a relation or intention before its content, but grammar alone does not guarantee reflection or peaceful conduct.

## Core Constraints Checklist

### Phonological Requirements
- [ ] **Uses only permitted sounds**: C={h,k,l,m,n,p,r,s,t,w}, F={ph,th,sh,wh}, V={a,e,i,o,u}
- [ ] **The fricative digraphs (F) are**: ph=/φ/, th=/θ/, sh=/ʃ/, wh=/ʍ/
- [ ] **Follows (C)CV structure**: Single consonants OR fricative digraphs only
- [ ] **Maintains vowel hiatus**: Each vowel = separate syllable (no diphthongs)
- [ ] **Vowel hiatus transcription**: Always show syllable breaks with dots: au=/a.u/, not /au/
- [ ] **Respects three-vowel constraint**: Never VVV+ sequences
- [ ] **No duplicate syllables in lexicon words**: Every proposed word satisfies the rule; source material outside Phi is not a lexical exception
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
- [ ] **Word length**: Every lexical word has at most three syllables. Two syllables remain premium space for the everyday and high-frequency; three syllables are the normal content-word range. Semantic weight never licenses a fourth syllable.

## Philosophical Consistency

### Five Pillars Integration
Each new word must explicitly connect to at least one pillar:
- [ ] **Solarpunk**: Sustainability, regeneration, positive futures
- [ ] **Buddhist concepts**: Mindfulness, impermanence, non-violence
- [ ] **Art Nouveau**: Organic forms, natural beauty, flowing patterns
- [ ] **Peace Linguistics**: Non-aggressive communication, collaboration
- [ ] **Pre-industrial wisdom**: Cyclical thinking, embodied knowledge

### Semantic Principles
- [ ] **Keep the core value-explicit**: Record what a choice favors, what it makes difficult, and whose needs it may fail to serve
- [ ] **Analyze violence and domination without normalizing them**: Prefer Phi descriptions when they expose a mechanism; preserve source testimony separately when faithful wording is required
- [ ] **Prefer holistic concepts**: Combine rather than separate (e.g., womu = house+belonging, the dwelling-heart)
- [ ] **Use compositional strategies**: Build complex ideas from simple roots
- [ ] **Enable transmutation**: Concepts should reframe, not just translate (rebuild ideas from ground up using Phi concepts)
- [ ] **Review refusals case by case**: A refusal must not obstruct care, self-identification, consent, safety, testimony, or philosophical critique
- [ ] **Keep source artifacts outside Phi syntax**: Preserve foreign wording, exact records, scripts, values, formulas, and identifiers in the surrounding medium while Phi points to, translates, or analyzes them
- [ ] **Create semantic families**: Build interconnected word networks where shared roots illuminate meanings (mycelial approach)

## Word Creation Protocol

This protocol creates lexical words. It does not apply to a productive proper-name form licensed by `ne`; use the separate name-form checklist below so a personal designation never acquires an invented dictionary meaning merely by being chosen.

The protocol is a quality checklist, not a burden-of-proof process. Phi is a personal constructed language, and a word may be coined because its concept is useful, valued, beautiful, or worth making easy to express. Composition remains an option when its parts illuminate the idea, while module vocabulary lets specialized speakers gain precision without obliging general learners to study every term.

### Step 1: Conceptual Analysis
- What experience, relation, object, quality, or practice does this represent?
- Can it be expressed by existing words, and would a transparent compound make the idea clearer than a new root?
- Would coinage make an important or recurring concept easier, more precise, more beautiful, or more natural to discuss?
- Does the concept belong in the general teaching path, one or more optional vocabulary modules, a transparent expression, or a separate source-material explanation?
- What is the intended semantic scope, and which neighboring concepts must the definition distinguish?
- Which values does the choice express, and what legitimate use or interpretation might it burden?

### Step 2: Sound Selection
- Choose sounds that embody the concept's feeling
- Ensure phonological rules are met
- **Run the collision check**: `python3 scripts/validate_examples.py neighbors <candidate>`
  - REJECT any candidate at edit distance 1 from an existing word of the same part-of-speech class (content vs. the same function class)
  - The designed opener/closer paradigms are the sole same-class exception: each grammatical clause pair shares its first syllable and contrasts final `a` with `o`. Evaluate a new pair as one proposal, require that neither form has any additional distance-1 neighbor in its class, and prioritize the contrast in listening review
  - Cross-class distance-1 neighbors are allowed only when position disambiguates (particle vs. content word) — note them in `grammatical_notes`
  - For natural opposites (left/right, give/take), prefer maximal phonetic dissimilarity, never a minimal pair
  - Prefer three syllables unless the concept truly belongs to the daily round: the two-syllable space is the most collision-congested (approximately 5,200 legal forms, heavily grandfathered), while three syllables offer approximately 377,000 legal forms and remain the absolute lexical maximum

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
- Does it remain distinct in careful and conversational speech?
- Does it improve the intended expressions without creating a broader ambiguity?

### Step 6: Canonical Entry and Teaching
- Fill every required vocabulary field with substantive content and serialize it in canonical schema order
- Give every content word accurate semantic-domain tags and add validated `modules` membership when it belongs to optional domain vocabulary
- Include grammatical examples that pass `python3 scripts/validate_examples.py`
- Regenerate the Part VII alphabetical, domain, module, and part-of-speech references
- Add or update a speaker-facing module chapter when the word belongs to an established vocabulary module

## Source Material Checklist

- [ ] The Phi passage contains only Phi vocabulary, grammatical Phi clauses, and valid Phi-form names
- [ ] Foreign wording, source-script names, exact records, formulas, identifiers, and quotations remain visibly outside the Phi passage
- [ ] The source artifact retains its own spelling, script, punctuation, notation, version, and provenance where those properties matter
- [ ] The Phi account identifies what it is pointing to and does not claim that its analysis exhausts the source concept
- [ ] Separate presentation is described as a boundary of language, not approval, condemnation, stigma, or loss of precision
- [ ] A recurring concept proposed for Phi passes the complete word-creation protocol rather than entering through repeated unmarked use

## Productive Name-Form Checklist

- [ ] The bearer or naming community accepts the form
- [ ] The form is one lowercase token with two or three Phi syllables
- [ ] It begins with a permitted onset, keeps every syllable open, has no VVV sequence, and duplicates no onset-bearing syllable
- [ ] It is not a function word, interjection, complementizer, or other grammatical boundary
- [ ] It appears after `ne` in formal, neutral, portable, and machine-validated Phi
- [ ] It receives no lexicon file, gloss, part of speech, sound-symbolism rationale, pillar claim, or automatic core status
- [ ] It is not rejected merely for lexical edit-distance proximity; real referential confusion is handled by clarification, as with shared human names
- [ ] A longer, multi-token, non-Phi-shaped, or source-script preferred name remains outside the Phi passage unless the bearer or naming community accepts another valid onym
- [ ] Run `python3 scripts/validate_examples.py name <form>` before publishing the name; the command must accept its shape and confirm that it is neither a reserved non-content form nor a retired form

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
- Does this support cooperative communication in the motivating scenario?
- Does it invite reflection without claiming to cause it?
- Does it reflect interconnection/interdependence?
- Does it resist hierarchical/violent framing?
- Can it report or criticize a disfavored framing faithfully when needed?

### Learnability Test
- Is the sound-meaning association teachable without presenting symbolism as universal?
- Can the concept be understood compositionally?
- Does it follow all established patterns?
- Is it distinguishable from nearby high-frequency words in recorded self-review?
- Which learnability questions still require evidence from other speakers?

## Red Flags to Avoid
- Creating silent exceptions to core phonological rules
- Adding irregular grammar without a demonstrated discourse need
- Presenting a culturally situated choice as neutral or universal
- Making care, identity, consent, safety, testimony, or critique impossible in order to preserve an aesthetic refusal
- Treating efficiency or slowness as an unconditional virtue
- Breaking core vowel hiatus or adding consonant clusters beyond the four digraphs
- Creating words without testing composition and semantic-family relationships first
- Presenting a word-for-word substitution as Phi where transmutation, explicit translation, or separate source presentation would be more honest
- Creating particles that violate slot positioning rules

## Core Philosophy Reminder
Every addition to Phi should make the following practices available without claiming that grammar compels them:
- Careful, deliberate speech
- Explicit reflection on word choice and evidential stance
- Communication approached as collaborative art
- Attention to ecological relationships and natural cycles
- Semantic families that expose interconnection
- Transmutation rather than automatic word substitution
- Faithful separate source presentation when Phi is not the right carrier

**The constraints are part of the teaching. Their difficulty must earn its place in use.**

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

Validate vocabulary and examples before committing with `python3 scripts/validate_examples.py`.

For detailed information, consult:
- **Sound system**: `documents/phonology_rules.md`, `documents/phonetics.md`
- **Complete grammar**: the manual, Parts IV-V (ch9-ch20); inventories in `documents/grammar/`
- **Particle inventory**: `documents/grammar/particle_reference.md`
- **Compound idioms**: `documents/compounds.md`
- **Numeral system**: `documents/grammar/numeral_reference.md`
- **Philosophy**: `documents/language_guide.md`

## Final Reminder
Phi is both a language and a proposed practice of conscious communication. Every design decision should support philosophical expression, compassion, ecological relationship, and honest disagreement while remaining open to correction by actual use. The language offers the practice; speakers do the work.
