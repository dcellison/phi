# Language, values, and voice

This file collects the constraints a replacement model is most likely to violate while doing otherwise competent work. It does not replace [`canon.md`](../../canon.md) or the full [`voice guide`](../../documents/reference/voice_for_models.md).

## Governing description

Preserve this description. Daniel singled it out as an accurate statement of the language:

> Phi is a philosophical constructed language for practising mindful and compassionate speech. It asks speakers to attend to the present utterance: what they know, what they intend, and how their words may enter a relationship. Its unhurried quality is freedom from needless haste, not a prescribed speaking speed.

Phi draws openly on Buddhist mindfulness and Right Speech. Peace linguistics extends that attention to relationship, power, agency, repair, and nonviolence. None of this claims that grammar makes a speaker kind, peaceful, mindful, rational, or sustainable. Phi offers places where a speaker can practise; the speaker still chooses what to do there.

Do not dilute this into "a slow language" to avoid mentioning Buddhist roots. Fluent Phi may be quick. Learning may be slow. An emergency may require speed. The relevant question is whether needless haste displaced attention, not how many seconds the sentence took.

## Authority order

When sources disagree:

1. `vocabulary/` owns lexical form, gloss, IPA, syllables, class, and meaning.
2. Canonical grammar references own particles, complementizers, numerals, and other closed grammar inventories.
3. `manual/` teaches the language and must agree with the first two levels.
4. `texts/` and then `pamphlets/` must agree with the higher levels.
5. The language guide and design rationale explain why.
6. `archive/` records history and has no current authority.

`canon.md` records settled cross-cutting decisions and tells lower documents what to repair. The project protocol governs how changes are made. The roadmap governs what work is active. A generated reference never outranks the JSON that generated it.

## One grammar and one organizing principle

Every element that modifies, specifies, or relates another element comes before what it affects. This gives Phi strict SOV order, modifier-before-noun order, possessor before possession, prepositions before their objects, particles before their heads, and dependent material before the clause it frames.

The grammar and particle system are complete. Do not add a particle, module-specific syntax, parser mode, adverb class, or irregular construction to solve a vocabulary problem. A genuine grammatical failure would be a separate language-design decision, not an incidental part of a module or prose batch.

Main-clause past and future meaning requires the appropriate tense particle. An unmarked verb is present. Embedded clauses carry their own tense. Slot 1 order is tense, aspect, voice, evidentiality, modality, negation, with at most one item per rank except the ruled `se ka` voice pair.

Inside Phi, the period is the only visible punctuation and every letter is lowercase. Questions, quotations, address, clause boundaries, and names are spoken through words rather than silent marks. Pauses cannot change the grammar.

## One word, one lexical class

Phi rejected noun-to-verb and adjective-to-verb conversion. The validator enforces one scalar `pos` per entry.

- Every verb licenses an event noun with no change of form. `thalo` is walk as an act and a walk as its event.
- Every adjective licenses a quality noun with no change of form. `mioru` is beautiful and beauty through grammar.
- A noun before another noun describes it through ordinary modifier-first syntax without becoming an adjective entry.
- A quality enters a state with `kelu`; causation uses voice on an appropriate verb.
- Manner is a descriptor immediately before the verb inside the Slot 1 block. Phi has no adverb class.
- A temporary role can use a relative clause ending in `miona` rather than a permanent person noun.

Do not add an extra `pos`, describe a noun as a verb, or present a rule-derived noun as a second dictionary class.

## Word shape

Lexical words have at most three syllables without exception, including module words. Open syllables, full vowel hiatus, no VVV sequence, consonant or approved digraph onset, final vowel, and no duplicated syllable are enforced.

Content words use two or three syllables. Two-syllable space is crowded and belongs mainly to frequent daily concepts. Three syllables are normal and provide ample room. Four syllables do not signal semantic breadth and cannot enter vocabulary.

Careful IPA keeps penultimate stress, separate adjacent vowels, dental `t` and `n`, the four fricative digraphs `/ɸ θ ʃ ʍ/`, and a tap or trill for `r`. Conversational variants are accepted when contrasts and syllable count remain recoverable. Accent and tempo are not moral registers.

## Productive names

`ne` announces the next Phi token as a proper designation. It may name a person, animal, place, community, institution, work, event, or artifact. The particle marks designation rather than personhood.

A productive Phi-form onym:

- is one lowercase token;
- has two, three, or four legal Phi syllables;
- keeps open syllables and the VVV limit;
- does not duplicate a syllable that has an onset;
- has no lexicon entry, gloss, part of speech, pillar claim, or module membership;
- may match a current lexicon entry only when that entry is a content word;
- may use an otherwise legal retired form without restoring its old meaning;
- may always use an otherwise legal four-syllable form without consulting migration history;
- belongs to the bearer or relevant naming community, which decides whether an adapted form represents the name.

Formal, neutral, portable, and machine-validated Phi retains `ne` at every mention. Household or conversational speech may omit it after the referent is established and while reference remains clear. Keeping `ne` is always correct.

A preferred name that is multiword, source-script dependent, five or more syllables, or otherwise non-Phi stays outside the Phi passage unless its bearer accepts a Phi-form onym. Do not force adaptation for tool convenience.

## Source material

The guest and exact frames were removed. Do not restore them under another name.

Foreign wording, source-script names, exact values and records, identifiers, formulas, quotations, legal and medical text, citations, and other unassimilated artifacts remain beside or around Phi in the surrounding page, interface, or conversation. Phi may point to, describe, translate, analyse, or discuss them, but the source tokens occupy no Phi syntactic position under current canon.

This boundary preserves source identity and parity among Romanization, Tengwar, and the future glyph mode. It says nothing about approval, condemnation, stigma, or Phi's capacity to understand the material.

Live spoken source material and code-switching remain an open design question. The difficulty is that conversation has no obvious page margin. Until canon changes, retain the current boundary; a new frame requires an explicit language-design decision. Any solution must use the complete existing grammar and discourse practice rather than create a second parser.

`shola ... sholo` instead quotes grammatical Phi as Phi and therefore remains inside the language.

## Modules

Phi has one canonical lexicon and eight optional learning paths. A word with no `modules` field is base vocabulary. A word may list several modules. Every module word follows ordinary phonology, syntax, derivation rules, and schema.

A speaker who does not know a module term may ask for a base paraphrase, transparent expression, explanation, or separately presented source form. This right appears in the module teaching and should not disappear during revision.

Module placement does not make a word less real. It limits what a general learner is expected to memorize. Core concepts needed for ordinary life, identity, consent, safety, testimony, and communication remain available outside optional study.

## Peace linguistics

Phi's peace-linguistic boundary was sharpened after a vocabulary audit found combat metaphors and a recently introduced broad impact verb. Read [`documents/evaluation/peace_linguistics_vocabulary_audit.md`](../../documents/evaluation/peace_linguistics_vocabulary_audit.md) before touching this area.

Do not coin generic conflict or direct roots centred on violence, fighting, attack, defence, hunting, killing, weapons, enemies, or war. Do not normalize domination through rule, lordship, mastery, thrones, captivity, or master-and-servant metaphor. Do not use combat vocabulary as a casual metaphor for argument, debugging, design, medicine, or governance.

This refusal does not require silence. Phi keeps direct language for danger, harm, injury, coercion, protection, warning, testimony, responsibility, accountability, redress, repair, and refusal. Faithful source material may preserve violent wording outside Phi. A close translation can describe the mechanism explicitly. A transmutation may refuse its direction only after the source has been heard.

Phi has no general verb for "hit." `kema palo` reports forceful contact. Movement, damage, and bodily injury receive their own claims through `pesa`, `pukeri`, and `kaworu`. The retired `patore` cannot return to vocabulary, though a bearer may choose it as a valid onym.

## Measurement, time, exchange, and number

Read [`documents/design/psychological_violence_of_measurement.md`](../../documents/design/psychological_violence_of_measurement.md) before proposing a unit or translating an exact record.

Phi tells the day through eight natural stations of the sun. Hour, minute, second, and clock time are refused as unmarked core vocabulary. A required appointment time or safety record remains exact beside the Phi account.

Core Phi has no metre, mile, kilogram, litre, or other unit words, and none will be coined. Neutral nouns for size, length, distance, height, width, depth, and weight identify what is gauged. Comparison, embodied standards, travel time, and natural cycles describe ordinary scale. Exact scientific units and records stay in their source notation.

Money, coin, price, pay, buy, sell, debt, wage, wealth, and poor are refused. Giving, receiving, sharing, and mutual exchange remain explicit acts. Exact economic records stay outside the Phi passage. `rolia` is inherent worth; `sone` is the act of valuing. Do not turn a person into a scarcity category.

Phi's internal numerals are finite ternary. Exact integers run from 0 through 242. Larger exact values, negatives, fractions, units, formulas, and technical notation remain source material. A number within the range may be rendered in Phi when that rendering is adequate, while the source form remains preserved when its notation or identity matters.

The documentation must not claim that people directly perceive three, nine, or twenty-seven as unanalysed wholes. Ternary is learnable, but rare, and its cost should be stated honestly.

## Other settled refusals and compositions

- The seven coined color adjectives are the whole palette. Gray, orange, pink, violet, and other negotiated hues compose from a referent plus `welisha`.
- Anger, hatred, contempt, envy, loneliness, and wonder keep their settled compositions where the parts matter. This does not forbid direct affect roots when they add a useful distinction.
- `thorea` is the only ceremony word. Specific rites are described rather than standardized as vocabulary.
- Death is `lumeo` and receives no softened substitute. Gentleness comes through grammar, grief, and care rather than euphemism.
- Art-form and genre roots are generally refused under "a work is its making." `melira` covers song and poem; `kire` covers shaping and drawing as an event noun; `shela` is art as the category. Further instruments may still be coined through the full protocol when actual musical life needs them.
- Universal gendered person classes and marriage as a universal institution are currently refused. Exact self-description and legal or cultural status may remain in source material. Consent, partnership, kinship, and bodily care remain speakable.
- Generic "bad" is refused. State whether something is harmful, broken, unwell, mistaken, cruel, unsuitable, or otherwise defective in the way that matters.
- East and west are the solar compounds `sileta thorui` and `sileta lumae`. North and south remain direct roots.

## Translation and transmutation

A translation preserves the source's propositions, relations, images, and difficult material as closely as Phi permits. A missing one-word equivalent calls for composition or explicit description, not a quieter rewrite. The source citation remains adjacent and exact.

A transmutation lets the source pass through Phi's five pillars and conceptual habits. That freedom does not permit lazy approximation. The Phi must agree with its exact gloss and back-translation, and the notes must identify deliberate changes and remaining losses.

The literary shelf prefers transmutation because it preserves Phi's own heart. Paired close translations demonstrate that the language can carry a source closely and make the divergence visible. Not every long work needs both. *News from Nowhere* remains a transmutation-only 32-chapter project unless Daniel changes the plan.

## The five pillars

The five named commitments are Solarpunk, secular Buddhist philosophy, Art Nouveau aesthetics, peace linguistics, and pre-industrial wisdom. They guide choices but do not require a `pillars` field on every word or an equal paragraph in every text.

A pillar rationale must be direct and specific. It should fail when pasted into another entry. Do not decorate neutral reference prose with general claims about mindfulness, harmony, sustainability, community, or beauty.

## Phi project voice

Before generating or revising any Phi project text:

1. Read `documents/reference/voice_for_models.md` in full.
2. Load Humanizer and read its `SKILL.md` in full.
3. Draft the complete, accurate text under canon, schema, source, and artifact requirements.
4. Apply Humanizer to the complete draft as a separate revision.
5. Audit the result against every applicable voice count and the batch-stamping rules.
6. Validate Phi, structure, sources, and generated files after prose revision.
7. Report one concrete pattern found and corrected.

The voice has three registers:

| Register | Practice |
|---|---|
| Teaching prose | Open on a scene, example, problem, or contrast. Let philosophy arrive after the concrete thing earns it. End on a turn, not a recap. |
| Reference prose | Stay close to the definition. Keep one useful distinction in each slot, exact language, and varied sentence shape. Human personality comes through specificity rather than chatter. |
| Boilerplate | Preserve approved shared furniture exactly across a series. Humanize it when first written, then stop varying policy sentences merely to sound original. |

Existing validated Phi blocks, gloss lines, source quotations, and protected formatting conventions are untouchable during a style pass. Humanizer may revise new English around them but cannot move lexical facts, grammar, or source wording.

## Voice prohibitions

New Phi-authored prose has no em or en dashes, curly quotes, generic uplift, brochure language, contract-style denial tails, fake depth added by comma-plus-participle, repeated rule-of-three cadence, or ornate substitutes for a plain `is`.

The banned inflation list in the voice guide is literal. Phi prose never attaches the ordinary English verb meaning "to carry" as a hyphenated adjective suffix. Daniel rejected that entire construction and does not want variants reintroduced. Avoid the stock hyphenated adjective made from `future` and `facing` as well.

Reference entries must not be stamped from a template. Compare openers, closers, repeated trigrams, and pet verbs across the entire batch. A flourish is spent after one use. Approved boilerplate is the only honest exception.

State one boundary once. The earlier generated module prose accumulated long lists of what each word did not authorize or guarantee. Those lists were factually careful and humanly unreadable. The correct move is usually one positive definition and one nearby contrast.

The no-guarantee hedge has a ruled budget: at most one full-strength statement per chapter in teaching prose, placed where its temptation is strongest, and the cap is a ceiling rather than a quota. A kept boundary must teach its own chapter's subject; the general charter is stated once, in Part I, and a chapter whose subject does not raise the temptation carries none.

Imagery is welcome under one rule: hang it on design-intent verbs (built to, asks, offers, invites), never on effect verbs that credit grammar with changing the speaker. When an older draft holds a good image on a false verb, restore the image and retire the verb. The voice guide's gallery shows the move on the real Part I restoration.

## Book voice

The book is narrative nonfiction for an intelligent general reader. It is not the manual, a sales page, or a project diary. It may discuss project history because the treatment grants the book that register; teaching prose elsewhere still describes Phi as it is now.

Warmth matters. Daniel found the early chapters too cool and asked for a light touch drawn from Jerome K. Jerome's *Three Men in a Boat*. Use the type of humour sparingly:

- allow the narrator to be mildly implicated rather than floating above the scene;
- notice the practical absurdity in laboratory apparatus, institutional habits, or human confidence;
- let one dry sentence release tension after accurate exposition;
- prefer a concrete inconvenience to a crafted punchline;
- never turn a person, community, disability, sacred practice, source tradition, or act of harm into the joke.

Read adjacent chapters before drafting so the warmth and furniture continue. Do not paste the same humorous turn into each chapter. Scientific claims stay exact, qualifications stay near the claim, and humour cannot make a weak citation look stronger.

Two register rulings from 22 July 2026 bind the book beyond the humour note. Hedging is low: the honest number, stated once where the claim is made, is the hedge, and the prose then moves on with confidence rather than stacking qualifications. A boundary or refusal appears at most once in the whole book, as a sentence in the chapter where the reader actually brings the temptation, so search the other chapters before spending one, and never restate a hedge as a paragraph closer or a chapter-ending caution. Warmth is high: the book is openly aspirational and inspirational, with imagery hung on design-intent verbs such as built to, offers, asks, and invites, and aspiration reserved for what the practice opens rather than promises of what it causes. Daniel's own words set both: "Lower the importance of hedging. It is getting in the way of a good book," and "keep it very warm, aspirational, and inspirational."

## Spelling note

At the July 2026 model handoff, Daniel ruled that new prose uses American spelling for now, in the book as well as everywhere else, matching the voice guide's hard-mechanics line. His earlier Canadian preference for book chapters is superseded until he reopens it, and existing repository prose still contains both practices.

Do not resolve the residual mix through an unrequested repository-wide sweep; a dedicated spelling pass remains Daniel's to schedule. Write American in new prose, and preserve the surrounding file's established spelling during small revisions.

## Interaction with Daniel

Daniel often asks exploratory questions and explicitly distinguishes them from commands. Answer the question without editing when he says "just discuss," "take no action," or asks what you think. Once he gives a command such as "proceed," carry it through implementation, validation, commit, push, PR, and CI unless he sets a stopping point.

He prefers direct technical explanation and will challenge decisions that hide behind process. Do not invent an audience, approval gate, or evidence burden for his personal language. At the same time, preserve the roadmap's real evidence boundaries: one maintainer cannot generate learner, listener, cultural, or community evidence by writing more confidently.

When a correction reveals a systemic failure, repair the process as well as the immediate item. The decision register exists because possible coinages were once lost. The peace-linguistics audit exists because combat metaphors slipped into entries. The voice guide's batch count exists because individually plausible prose repeated itself across files. Use those instruments; they were paid for already.
