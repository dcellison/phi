# The Phi voice, for models

This document teaches a language model to write Phi documentation in the project's established voice. It is self-contained: everything needed is embedded here, because the model reading it may have no access to this repository, its history, or its tools. Read the whole document before generating anything.

The voice is one third of a trust system. This document carries the taste. The validator (`python3 scripts/validate_examples.py`, run standalone, zero errors and zero warnings) machine-checks the correctness of every Phi example, gloss, and lexicon entry. The maintainer's review is the final gate, and nothing in this document overrides it. For decisions about the language itself, the authority order is `/canon.md`; this document governs prose, not grammar.

Humanizer belongs inside the writing method, not at the edge of it. Write the complete and accurate text first, then apply the installed skill as a separate revision to everything the model generated. No prose category is exempt: a lexicon entry gets the same second look as a chapter or report, and so do table cells and boilerplate.

The skill's generic advice about neutral reference prose does not create an exception here. Phi reference writing keeps its definitions tight, but the sentences still need a person in them.

A model that follows this document should expect to land most of the voice and to be corrected on the remainder. That is the intended outcome, not a failure. What this document prevents is the expensive kind of miss: a whole body of work delivered in the wrong register.

## The stance

Write as one careful writer talking to one intelligent learner. The reader is smart, busy, and slightly skeptical; they did not come to be sold on Phi, and they did not come to be protected from it. They came to learn it. The philosophy is never a sales pitch and never a preamble; it is a consequence the reader is allowed to discover after the concrete thing that earns it.

## The two ways generation goes wrong

Models drift toward one of two failed registers, and knowing your own likely drift is the most useful thing this document can tell you.

The first pole is the brochure: inflated significance, promotional adjectives, every feature "vibrant" or "profound," every section ending in uplift. Style guides warn about this one, and most models now partially avoid it.

The second pole is the contract, and it is the one that actually damaged this project. A model being careful, especially in sensitive domains like medicine, coercion, or exploitation, defines every word by an exhaustive list of what it is not, restates every boundary five times as a disclaimer, and drills the reader with imperatives about what to state and preserve. The result reads like liability language. It happened here at measurable scale: chapters carrying up to 49 negative litanies each, a third of new dictionary entries ending in disclaimer lists, and instruction sentences beginning "State the source, criteria, scope, date, validity..." The information was correct. The voice was wrong, and all of it was rewritten.

The rule that replaces both poles: state a boundary once, where it teaches, and trust the reader. Here is the same semantic content both ways.

Contract register, as originally generated:

> Assignment is not a request, allocation, delegation, authorization, accepted obligation, competence, or consent.

The established voice, as merged:

> Assignment names an expected performer; acceptance stays the performer's own act.

Nothing was lost. The seven denials collapsed into the one distinction that carries them all, stated positively, in half the words. Every boundary in Phi's documentation can be taught this way, and the sensitive domains deserve it most: the medical module's sharpest lines ("Triage orders care under scarcity; it never ranks human worth") protect more by saying it once, plainly, than any disclaimer stack does.

## The register map

The voice is one voice in three registers, plus a class of text you must never touch. Identify which register an artifact belongs to before writing a word of it.

**Teaching prose** (manual chapters, pamphlets, primer): opens on something concrete the reader can check, a scene, a contrast, a problem. Philosophy arrives afterward as payoff. Sections end on a turn: a consequence, an image, a Phi line. Never a summary, never generic uplift.

**Reference prose** (tables, lexicon entries, grammar notes, quick references): stays close to the thing it defines. It is compact without sounding poured from a template. One earned distinction per slot. Humanizer is mandatory here too. Personality comes through exact word choice and a rhythm that does not repeat from entry to entry. The best detail could belong only to this definition.

**Boilerplate** (navigation pointers, regeneration notes, the module-mechanics paragraph that recurs across module guides): deliberately uniform. Humanize boilerplate when it is first written or deliberately revised, then preserve the approved sentence wherever it recurs. A policy sentence that appears in six files should be the same sentence six times; that uniformity is honest, like a license line.

**Untouchable text**: existing validated Phi example blocks (the fenced four-line blocks of Phi sentence, gloss line, parenthetical English, and source line), gloss lines anywhere, source quotations, and the protected formatting conventions listed under mechanics below. Humanizer does not turn a reuse task into a rewrite. When a task creates a new block, its ordinary English receives the pass before validation, while its Phi and exact gloss stay governed by the lexicon. Existing blocks are never edited for style, and several of them contain em dashes that are part of the convention, not a defect.

## The rules

These are the manual's own rules, each stated with its reason. The exemplar chapters for the target voice are `manual/part6_mastery/ch22_transmutation/`, `manual/part6_mastery/ch23_living_in_phi/`, and `manual/appendices/appendix_b_natural_languages.md`.

**1. Concrete first, philosophy earned.** Every section opens with something checkable: an example, a contrast, a problem, a scene. A module chapter about work opens on a mended chair coming back from the workshop, not on a scope declaration. Philosophy is the payoff of the concrete thing, never the preamble, and never a closing recap of principles already stated.

**2. One explanation, one home.** Each core principle is explained thoroughly exactly once in the corpus. Everywhere else it is used, not re-explained. If your text cannot proceed without restating a principle, point to where it lives.

**3. Plain copulas, plain verbs.** "Is," "has," "does." Not "serves as," "stands as," "functions as," "represents." A sentence avoiding "is" is usually avoiding a commitment.

**4. No inflation.** Banned outright, verbatim: testament, pivotal, crucial, vital, profound, vibrant, rich (figurative), stunning, groundbreaking, perfectly embodies, crystal clear, seamless, load-bearing, meaning-bearing. If a feature matters, show the sentence where it matters and let the reader supply the adjective.

**5. Kill the -ing tail.** A comma followed by a present participle restating the sentence ("...reflecting the language's commitment to mindfulness") adds fake depth. Either the point deserves its own sentence with a subject and a claim, or it does not deserve to exist.

**6. Vary the rhythm.** Short sentences land. Long ones unfold a thought that genuinely has stages. Three consecutive sentences with the same shape means one of them gets rebuilt.

**7. Lists are for enumerable things.** Particle inventories and tables of forms, yes. Ideas, arguments, and feelings are prose. Never the bold-header-colon list; that is an outline wearing a paragraph's clothes.

**8. Honesty is the register.** Where the language costs something, memory load, missing vocabulary, hard sounds, say so plainly and say what the cost buys. Credibility on the philosophy rests entirely on honesty about the trade-offs. No generic uplift endings.

**9. Examples do the work.** Every example is glossed, validated against the lexicon, and chosen to advance the argument rather than decorate it. The manual should feel like it belongs to a language that has literature, because it does.

**10. Ration the word "announce."** It is the language's central metaphor and it wears smooth with repetition. It may work where the modifier-first principle is being taught; it should be rare everywhere else. Using the principle beats naming it.

**11. Formatting.** Sentence case in headings. Straight quotes. Bold for Phi words being defined, italics for emphasis at most once or twice a section, no emoji.

**12. Endings.** The last paragraph of a file is not a summary. It is the one thing the reader should walk away holding, stated once, cleanly, and then the door.

**13. Now, not history.** Teaching prose states how the language is, never how it came to be: no retired forms, no past corrections, no decision dates, no audits, no project chronology, no draft narration. A learner reading "this was renamed in July" is being told about the project instead of the language. History lives in `/canon.md` and `/archive/` only. The one carve: a transmuted text's own gap log stays, because it is method, not chronology.

## The lexicon register

Vocabulary entries are reference entries with their own discipline. The schema sets the work each field must do; it cannot write the sentence for you. The completed entry gets a Humanizer pass everywhere it carries prose. That includes the concept label, description, sound symbolism, and grammatical notes. Pillar and tag rationales get the same treatment, as does ordinary English example text. The rules above apply, plus the following per field.

**description**: the word's actual range of use in two to four sentences. What it covers, one earned distinction from its nearest neighbor, and concrete situations over abstract scope-lists. A neighbor word is cited with its exact gloss, in the form 'word' (gloss). The failed pattern to avoid: a definitional range list followed by a tail of five to nine denials ("It does not establish ownership, entitlement, abundance, renewability, harmless use..."). Fold the denials into the one distinction that teaches, and let the rest go.

**sound_symbolism**: describes only sounds the word actually contains, named accurately. The job is to show how this word's real phonemes carry its meaning, in two or three sentences. If the sounds are honestly unremarkable, say less rather than inventing.

**grammatical_notes**: working reference. At least one worked example in valid grammar, related words named, genuine contrasts drawn. Not commentary, not philosophy.

**pillars**: a word carries exactly the pillars that genuinely fit it, whether that is one or five. There is no target number. Each rationale must pass the paste test below.

**Never in an entry**: "beautifully," "perfectly embodies," "reminds us," rhetorical questions, or philosophy that repeats what the project's protocol documents already say. An entry's philosophy lives in its specifics.

**The paste test**: every sentence you write for an entry should become false if pasted into a different entry. "This word supports mindful communication" pastes anywhere and is therefore worthless. "The thumb is exactly what the compound says; a coined label would hide the transparency" is true of one word in the language.

## Anti-patterns you count, not sense

You cannot check yourself against "don't be severe" or "be warm." You can check counts. Before delivering, count these in your own output; the thresholds are hard.

| Pattern | What it looks like | Threshold |
|---|---|---|
| Negative litany | "X is not A, B, C, D, or E" | at most one per two hundred words, and never two in adjacent sentences |
| Disclaimer tail | a definition ending in a list of denials | zero; fold into one distinction |
| Compliance imperative | "State the...", "Name the...", "Preserve the..." aimed at the reader | zero in teaching prose; in reference prose, rewrite as what the word invites or leaves open |
| Enumerative chain | comma lists past four items in running prose | rewrite or table |
| Em or en dash | any, in new prose | zero, no exceptions; commas, colons, periods, parentheses do the work |
| Curly quotes | any | zero; straight quotes only |
| Inflation vocabulary | the banned list under rule 4 | zero |
| -ing tail | comma plus participle restating the sentence | zero |
| Copula avoidance | "serves as," "functions as," "stands as" | zero |
| Rule of three | three parallel items where two or four would be honest | flag every triple; keep only those whose three items are each specific and load different content |
| Inline-header list | bolded label, colon, sentence | zero; prose or a real table |
| Aphorism formula | "X is the Y of Z," "the language of," "the currency of" | at most one per document, and only if it is specific enough to fail the paste test |
| Signposting | "Let's look at," "here's what you need to know" | zero |
| Staccato drama | runs of clipped fragments for manufactured weight | one short sentence lands; a run is engineered |
| Generic conclusion | upbeat summary endings | zero; end on a turn or just end |

Two notes on false positives. First, a single "X, not Y" contrast is ordinary English and often the exact teaching move this voice wants; the litany threshold is about stacked denials, not about contrast itself. Second, tables of enumerable facts are welcome in reference registers; the enumerative-chain rule is about prose pretending not to be a list.

## Corpus-level tells: the stamping problem

A model generating several artifacts in one sitting will stamp: the same opener shape, the same closer flourish, the same pet phrase migrating between files. Each file passes review alone. The collection confesses.

This is not hypothetical. In one generation batch here, the flourish "confers nothing: not X, not Y, not Z" appeared in the intro of all six module guides, identically shaped, and survived every per-file check. In the corrective rewrite, done with full knowledge of the first failure, the phrase family "each their own separate fact" and its variants appeared thirty-seven times across chapters and entries before a counting pass caught it. Different model, different tic, same mechanism: voice under generation drifts toward self-templates, and no amount of care during writing catches it. Only measurement afterward does.

The rules that follow from this:

A flourish used once is spent for the batch. If you write a striking closer or a pointed triple in one artifact, the next artifact may not reuse its shape.

When producing more than one artifact, scan the whole batch for repeated sentence shapes, repeated openers, repeated closers, and any phrase of three or more words appearing in more than one artifact. Vary or flatten what you find. The uniform-boilerplate exemption applies only to text that is boilerplate on the register map.

Do not let a table cell and its expanding prose paragraph share sentences verbatim. The cell compresses; the prose teaches; they should read as two acts, not one act twice.

## Hard mechanics

These are structural. Violating them damages the corpus in ways a style review may not catch until later, so treat every item as a gate.

- Markdown paragraphs are single lines. Never hard-wrap prose; the renderers break on it.
- Inside Phi text: periods are the only punctuation, and there are no capital letters anywhere, ever, including names and the starts of sentences.
- A Phi word cited in English prose stays lowercase even when it opens the sentence. Never capitalize it to satisfy English sentence case; recast the sentence if the lowercase opening bothers you. A capitalized citation also hides the word from the validator's checks, so this is a correctness rule wearing a style rule's clothes.
- Never invent Phi. Every Phi word you write must exist in the lexicon, and every gloss line must render each word by its exact lexicon gloss, with uppercase labels for function words. If you cannot check the lexicon, do not write new Phi sentences at all; reuse existing validated example blocks verbatim instead.
- If you can run the validator, run it standalone before delivering anything containing Phi: `python3 scripts/validate_examples.py`. Zero errors and zero warnings is the bar. Drafts can be linted early with `--paths <file>`.
- Protected conventions that look like style violations and are not: the vocabulary introduction form `**word** — gloss`, the example form `**Phi sentence.** — English.`, bibliography bullets of the form `- **Title** (context) — description`, and the fenced four-line example blocks. The em dash inside these conventions is part of the convention. Leave all of them exactly as found.
- American spelling: color, gray.
- Sentence case in headings; module names keep their established title case.
- No history in teaching prose (rule 13 above), which includes your own process: never narrate drafts, passes, or corrections inside a deliverable.

## Tuning forks

Three short passages in the established voice, quoted verbatim from the corpus, each with the one thing to hear in it.

From the manual's chapter on exchange, a section opener:

> The last of the words-of sections is about what changes hands. Phi conducts its whole economy with a handful of verbs, one gift, one trader, and a refusal that completes a family you have met twice already.

Concrete before abstract, the count made vivid, and the reader's own prior knowledge woven in as continuity. No throat-clearing.

From the manual's negation section (`manual/part4_grammar/ch15_voice_possibility/05_negation_ma.md`), a closing:

> That is the sound the particle was built to make: firm but not final, clear but not harsh. The lips close. Then they open.

A turn ending on the body. Two short sentences land because the long one before them did the work; this is what rule 6 and rule 12 look like together.

From the lexicon entry for `nitho` (north), the description's opening:

> The cardinal direction of the world's turning axis — the still point around which the sky wheels.

Reference register with an image that is also the definition. The em dash is quoted from an existing entry; new prose does the same work with a colon.

## Before and after: the gallery

Each pair is real: the left column shipped in the wrong register and was rewritten to the right column, which is now merged. The lesson follows each pair.

A dictionary entry's opening (rilowa, assign). Before:

> To designate a person, group, or role as the expected performer of a stated task under a stated source or process. Assignment reports the designation, not its legitimacy or effect. It does not establish authority, acceptance, obligation, competence, capacity, compensation, responsibility for the result, or freedom from refusal.

After:

> To designate someone as the expected performer of a task. The verb reports the designation and stops there: whether the assigner had standing, and whether the person accepts, are the next sentences, not this one. Refusal, 'naweri' (refuse), remains a full answer.

The eight-item denial tail became one boundary stated as what the word does, plus the one neighbor that completes the picture.

A reference table cell (riporu, task). Before:

> A task is not purposeful labor, a role, obligation, technical dependency, accepted assignment, or proof that the work is useful.

After:

> A task is one bounded piece of work; `riola` is the labor that fills it.

A contrast cell holds exactly one contrast, and the best contrast is usually a neighbor word, not a denial list.

A compliance imperative (deadlines and schedules). Before:

> State who set either one, what source artifact carries its exact value, what assumptions it uses, and whether affected people accepted it.

After:

> Both leave room to ask who set them and who agreed.

The instruction to the reader became a property of the words. The voice never drills; it shows what the vocabulary makes askable.

A chapter opening (the work module). Before:

> The Work, Craft, and Repair module gives Phi speakers optional vocabulary for organizing work, describing practical capacities, examining labor conditions, evaluating made or repaired things, and tracing materials through use.

After:

> A chair comes back from the workshop with one leg pale and new. Whoever sits in it tonight may want to know who cut that leg, whether the wood came from the elm the storm took, and when the chair can stand in the hall again.

Scope declarations tell; scenes teach. The scope information still appears, one sentence later, carried by the scene.

A boundary in a sensitive domain (triage). Before:

> Triage is not diagnosis, refusal of care, fairness, legitimate criteria, guaranteed benefit, exclusion authority, or ranking human worth.

After:

> Triage orders care under scarcity; it never ranks human worth.

Sensitive domains tempt the contract register hardest, and need it least. Keep the one boundary that protects, state it plainly, and it protects more.

A document ending (governance source material). Before:

> Exact preservation does not make a law applicable, an office authorized, a right recognized, a contract voluntary, a vote valid, a record authentic, a sanction legitimate, a government representative, or an institution just.

After:

> Preserving a source document exactly does not make its law applicable, its office authorized, or its institution just. What preservation buys is honesty: the history and the identity that a paraphrase would otherwise erase.

Even a warning can end on a turn. The nine-item litany kept its three strongest items and gained a reason to care.

## The protocol

Run this loop on everything you produce. It is not advice; deliverables arrive pre-audited or not at all.

1. Draft in the correct register from the register map.
2. Humanizer pass: take the complete draft through the installed skill's draft, audit, and final loop. Apply it to every generated prose field, even in reference and technical work. Meaning, schema, and protected elements stay put.
3. Mechanical pass: count every row of the anti-pattern table against the humanized draft. Scan for em dashes, curly quotes, and banned vocabulary explicitly.
4. Batch pass, when producing more than one artifact: scan across artifacts for repeated shapes and migrating phrases, and vary or flatten them.
5. Read the draft aloud, or as close as you can come, and apply the four verdicts. If it sounds like a brochure, cut the adjectives. If it sounds like a committee, cut the hedges. If it sounds like a sermon, move the philosophy after the example. If it sounds like a contract, state each boundary once and trust the reader.
6. Validate any Phi content, or if you cannot, confine yourself to existing validated blocks.
7. Deliver with a short note of what the audit found and changed. Claiming the audit ran without naming a single finding is the most common way to skip it.

## What this document cannot do

It cannot transfer judgment. Whether a particular triple is earned, whether a boundary is content or disclaimer, whether a turn has become a formula: these calls have residue that no rule captures, and the writer holding every rule in this document still develops blind spots toward their own output. The protocol's counting pass exists because of that, not despite it.

So the last rule is about posture. Hold the work lightly, expect the maintainer's corrections, and fold each one back into how you write the next file. The voice documented here was not designed in one sitting; it accreted through exactly that loop, one correction at a time. You are not being asked to imitate a document. You are being asked to join a practice.
