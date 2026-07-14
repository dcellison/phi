# The Phi Development Protocol

## Overview
Phi is a philosophical constructed language for practising mindful and compassionate speech, reflective writing, and discussion. It is not intended as a universal auxiliary language. Its phonology, grammar, lexicon, and teaching practices invite attention to the present utterance, evidential care, and cooperative communication; these are design intentions to test in use, not guarantees about what the language does to a speaker.

This protocol binds the maintainer and anyone contributing to the language: coining words, extending grammar, or writing its documents. The authority order for every claim is `/canon.md`. While Phi has one maintainer, significant choices are recorded in `project/development_log.md`; a public RFC process is deferred until recurring users make one useful.

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
- [ ] **Hiatus disyllable ((C)V.V)**: The relator shape — prepositions (mua, thue, wei), core pronouns (mia, thia, shia), clause-relators (lao, pheo, phoe, shai), and scale units (shao, phoi, lau, rei)
- [ ] **Plain disyllable (CV.CV)**: The frame shape — complementizers (openers -a, closers -o), frame conjunctions, classifiers, the vocative, and the -so pronoun pair (miso, wiso)
- [ ] **Multi-syllable**: Required for content words; quantifiers, discourse markers (fricative-initial — the breath before reframing), and interrogatives are content-shaped (2-3 syllables)

### Sound and articulation review
- [ ] **Complete spoken path**: `articulatory_notes` follows the word from its opening airflow through contact and release, vowel shape, stress, and any hiatus
- [ ] **Physical accuracy**: The note describes sounds the word contains and keeps semantic interpretation out of the mechanics
- [ ] **Ease and distinction**: The whole form remains comfortable enough for its intended frequency and distinct from crowded neighbours
- [ ] **Optional sound symbolism**: Record a phonesthetic association only when it feels genuine in Phi, and state it as an interpretation rather than a universal sound law or hidden morphology
- [ ] **Word length**: Every lexical word has at most three syllables. Two syllables remain premium space for the everyday and high-frequency; three syllables are the normal content-word range. Semantic weight never licenses a fourth syllable.

## Philosophical Consistency

### Mindful speech and tempo

Phi draws openly on Buddhist mindfulness and Right Speech. Mindfulness concerns attention to the present act of speaking and listening; Right Speech gives that attention an ethical direction through truthfulness, kindness, benefit, and nonviolence. Peace linguistics extends the practice by asking how an utterance affects relationship, agency, and power.

"Unhurried" describes freedom from needless haste, not a required speaking speed. A speaker may use a slower pace to learn pronunciation or make room for reflection, but fluent Phi may be quick when urgency or ordinary conversation calls for it. Review whether the design keeps these practices available and audible rather than treating elapsed time as proof of them.

### Five Pillars Integration
A new word records a pillar only when its connection is direct and specific. A word may have no pillar field. When a connection does fit, test it against the relevant question:
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
- [ ] **Keep source artifacts outside Phi syntax**: Preserve foreign wording, source-form exact records and values, scripts, units, formulas, and identifiers in the surrounding medium while Phi points to, translates, or analyzes them; an integer from 0 through 242 may also be rendered internally when adequate
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
- Choose a legal, speakable form whose rhythm and phonetic character suit its intended use
- Ensure phonological rules are met
- **Run the collision check**: `python3 scripts/validate_examples.py neighbors <candidate>`
  - REJECT any candidate at edit distance 1 from an existing word of the same part-of-speech class (content vs. the same function class)
  - The designed opener/closer paradigms are the sole same-class exception: each grammatical clause pair shares its first syllable and contrasts final `a` with `o`. Evaluate a new pair as one proposal, require that neither form has any additional distance-1 neighbor in its class, and prioritize the contrast in listening review
  - Cross-class distance-1 neighbors are allowed only when position disambiguates (particle vs. content word); note a useful warning in `usage_notes`
  - For natural opposites (left/right, give/take), prefer maximal phonetic dissimilarity, never a minimal pair
  - Prefer three syllables unless the concept truly belongs to the daily round: the two-syllable space is the most collision-congested (approximately 5,200 legal forms, heavily grandfathered), while three syllables offer approximately 377,000 legal forms and remain the absolute lexical maximum

### Step 3: Hiatus Check
- Map all syllable breaks (use dots: CV.V.CV)
- Verify no VVV sequences
- Confirm pronunciation maintains pure vowels

### Step 4: Prose and Relational Alignment
- Write an accurate `articulatory_notes` account of the complete word
- Decide whether an honest `sound_symbolism` association exists; omit the field when it does not
- Record only direct pillar connections, with a rationale specific to this word
- Add `usage_notes` only when the entry needs guidance beyond its definition and examples
- **Identify semantic family**: What roots does this share? What words does it illuminate?
- **Check transmutation quality**: Does this enable reframing concepts, not just renaming?

### Step 5: Compositional Testing
- Can this word combine with others meaningfully?
- Does it maintain Phi's aesthetic when spoken?
- Does it remain distinct in careful and conversational speech?
- Does it improve the intended expressions without creating a broader ambiguity?

### Step 6: Canonical Entry and Teaching
- Fill the target vocabulary fields with substantive content and serialize them in canonical schema order
- Give every content word accurate `semantic_domains` assignments and add validated `modules` membership when it belongs to optional domain vocabulary
- Store at least one natural Phi and English example pair that passes `python3 scripts/validate_examples.py`
- Refresh `documents/validation/vocabulary_prose_coverage.json` with `python3 scripts/vocabulary_prose_coverage.py`
- Regenerate the Part VII alphabetical, domain, module, and part-of-speech references
- Add or update a speaker-facing module chapter when the word belongs to an established vocabulary module

## Source Material Checklist

- [ ] The Phi passage contains only Phi vocabulary, grammatical Phi clauses, and valid Phi-form names
- [ ] Foreign wording, source-script names, source-form exact records, formulas, identifiers, and quotations remain visibly outside the Phi passage; internal Phi numerals do not replace a source artifact whose original form matters
- [ ] The source artifact retains its own spelling, script, punctuation, notation, version, and provenance where those properties matter
- [ ] The Phi account identifies what it is pointing to and does not claim that its analysis exhausts the source concept
- [ ] Separate presentation is described as a boundary of language, not approval, condemnation, stigma, or loss of precision
- [ ] A recurring concept proposed for Phi passes the complete word-creation protocol rather than entering through repeated unmarked use

## Productive name-form checklist

- [ ] The bearer or naming community accepts the form
- [ ] The form is one lowercase token with two, three, or four Phi syllables
- [ ] It begins with a permitted onset, keeps every syllable open, has no VVV sequence, and duplicates no syllable with an onset
- [ ] If it matches a current lexicon entry, that entry is a content word rather than a function or other non-content word
- [ ] It appears after `ne` in formal, neutral, portable, and machine-validated Phi
- [ ] It receives no lexicon file, gloss, part of speech, articulatory note, sound-symbolism rationale, pillar claim, or automatic core status
- [ ] A retired content form may be chosen as a name without regaining its former gloss or returning to the lexicon
- [ ] Any otherwise valid four-syllable form is accepted without consulting lexical retirement or migration history
- [ ] It is not rejected merely for lexical edit-distance proximity; real referential confusion is handled by clarification, as with shared human names
- [ ] A preferred name with five or more syllables, multiple tokens, a non-Phi shape, or dependence on another script remains outside the Phi passage unless the bearer or naming community accepts another valid onym
- [ ] Run `python3 scripts/validate_examples.py name <form>` before publishing the name; the command must accept its shape and confirm that it does not match a current function or other non-content word

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
- Does the articulatory note make the spoken form teachable and accurate?
- If sound symbolism is claimed, is it useful without being presented as universal?
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
- Present, attentive speech at the pace the occasion permits
- Truthful, compassionate, and nonviolent speech understood as a practice rather than a grammatical achievement
- Explicit reflection on word choice and evidential stance
- Communication approached as collaborative art
- Attention to ecological relationships and natural cycles
- Semantic families that expose interconnection
- Transmutation rather than automatic word substitution
- Faithful separate source presentation when Phi is not the right carrier

**The constraints are part of the teaching. Their difficulty must earn its place in use.**

## Technical Implementation Notes

### When Using JSON Schema
[`vocabulary/schema.json`](../vocabulary/schema.json) is the executable entry contract. Stable fields identify the `word`, `gloss`, `ipa`, `syllables`, one scalar `pos`, and `description`. The target prose contract adds required `articulatory_notes` and structured `examples`; optional `search_terms`, `usage_notes`, `sound_symbolism`, and `pillars` appear only when useful. Content entries also have a `semantic_domains` object and may list one or more `modules`.

During the lexicon prose migration, the schema accepts legacy `sound_symbolism` in place of `articulatory_notes` and legacy `grammatical_notes` in place of `examples`. The deprecated `concept` and `grammatical_notes` fields are not used for new or fully revised entries. The committed coverage report measures the remaining legacy, partial, dual, and target entries.

Particles alone have `slot`. A Slot 1 particle also has `slot1_rank`, whose value places it in the canonical sequence of tense, aspect, voice, evidentiality, modality, and negation. The validator reads that ordering from the entries themselves.

Install the pinned validation dependency with `python3 -m pip install --requirement project/requirements.txt`, then run the validator as a standalone command. JSON Schema checks the entry's structure before the custom Phi checks inspect phonology, canonical serialization, cross-entry relations, and cited examples.

### File Organization
- Content words → `/vocabulary/content/`
- Function words → `/vocabulary/function/`
- Interjection words → `/vocabulary/interjection/`
- Vocabulary schema and semantic domains → `/vocabulary/schema.json`, `/vocabulary/semantic_domains.md`
- Grammar documentation → `/documents/grammar/`
- Language and writing references → `/documents/reference/`
- Design rationale → `/documents/design/`
- Evaluation material → `/documents/evaluation/`
- Practice and domain profiles → `/documents/modules/`
- Validator evidence and ledgers → `/documents/validation/`
- Python scripts → `/scripts/`
- Manual content → `/manual/`
- Literary translations and transmutations → `/texts/`
- Focused deep-dives → `/pamphlets/`
- Project operations and release records → `/project/`
- Historical material → `/archive/` (never a reference for current canon)

### Reference Documentation
**Authority order when documents disagree: see `/canon.md`.**

Validate vocabulary and examples before committing with `python3 scripts/validate_examples.py`.

For detailed information, consult:
- **Sound system**: `documents/reference/phonology_rules.md`, `documents/reference/phonetics.md`
- **Complete grammar**: the manual, Parts IV-V (ch9-ch20); inventories in `documents/grammar/`
- **Particle inventory**: `documents/grammar/particle_reference.md`
- **Compound idioms**: `documents/reference/compounds.md`
- **Numeral system**: `documents/grammar/numeral_reference.md`
- **Language overview**: `documents/reference/language_guide.md`
- **Design rationale**: `documents/design/`

## Final Reminder
Phi is both a language and a proposed practice of conscious communication. Every design decision should support philosophical expression, compassion, ecological relationship, and honest disagreement while remaining open to correction by actual use. The language offers the practice; speakers do the work.
