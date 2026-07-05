# Phi: Language Archaeology, Design Review, and Improvement Plan

*Prepared 2026-07-03. Read-only analysis of the repository at `/Users/daniel/work/phi` (632 commits, 2021-04-03 → 2026-02-10). Claims are labeled as evidence (verified in files/git) or inference (reconstruction from that evidence).*

---

## 1. Executive Assessment

**Thesis.** Phi is a philosophically-driven engineered language whose *system design* is unusually coherent and whose *documentation corpus* is unusually incoherent. The phonology (2021) and the modifier-first grammar (Sep 2025) are stable, internally consistent, and genuinely load-bearing: all 789 vocabulary entries pass every phonotactic rule with zero violations, and the grammar's core claim — every modifier precedes what it modifies — survives scrutiny across particles, prepositions, possessors, relative clauses, and numerals. The problem is that the language was rebuilt in rapid layers (Jul 2025 lexicon rebuild, Sep 2025 modifier-first/ternary pivot, Jan 2026 vocabulary blitz, Feb 2026 clause grammar), and each layer's documentation was only partially migrated. The result: the repo currently contains at least four vocabulary strata that contradict each other, and the reference grammar teaches with words the lexicon no longer contains or has reassigned.

**Strongest at:** being a philosophical notation and an engineered semantic system. The pillar rationales are bespoke (1,791 unique rationale strings, zero copy-paste), the complementizer opener/closer design solves a real SOV parsing problem elegantly, and the ternary numeral system is a complete, internally consistent implementation of its stated values.

**Most vulnerable to:** canon drift. The single most urgent instance: `AUDIT_LOG.md` (committed Feb 10, 2026) records vocabulary fixes to the manual (`kofe`→`naphe`, `nima`→`nulae`, `nolea`→`theo`, `suno`→`sorae`) that **were never merged**. Verified directly: the branch `audit/documentation-examples` no longer exists locally or on origin, `nolea` persists in all five ch15 files, and `kofe` persists in seven manual files. The repo's own record of its cleanup is now itself misinformation.

**Top 5 recommendations:**

1. **Recover or redo the lost audit branch.** The fixes in AUDIT_LOG.md exist nowhere in git. Redo them on main (they're well-specified in the log itself).
2. **Declare canon explicitly and demote everything else.** Move `book/`, `documents/tutorial/`, `documents/guides/`, `manual/part4_foundations/`, and `TERNARY_NUMBER_SYSTEM.md` to `archive/`; update CLAUDE.md's own stale examples (`wela` = good+beautiful is no longer true — `wela` is now the interrogative complementizer).
3. **Settle three disputed grammar points** that different current docs answer differently: the aspect inventory (`ro` HAB and `tha` PFV appear in the manual/pamphlets but not PARTICLE_REFERENCE), the conditional (`lu` Slot 0 particle vs `thoe` conjunction), and numeral negation (`ne` vs `ma` in NUMERAL_REFERENCE.md).
4. **Fix the two hard lexical collisions** (`phoi` = both "nine-group" and the preposition "from"; the `wela`/`welo`/`welao`/`towe` family) and adopt a minimal-pair policy for new coinages — the `-elV-/-olV-` neighborhood already has 216 single-vowel-contrast pairs.
5. **Repair or retire the script suite and automate the audit checklist.** Only 2 of ~19 scripts work correctly today. A single "every example word exists in the lexicon with the glossed meaning" validator, run before commits, would have prevented most of the drift documented below.

---

## 2. Source Map

| Source | Status | Confidence & basis |
|---|---|---|
| `vocabulary/*.json` (789 entries) | **Current canon** | High — newest content (Feb 5), internally consistent, what AUDIT_LOG audits against |
| `documents/grammar/COMPLEMENTIZER_REFERENCE.md` | **Current canon** (3 stale example words: `suno`, `mue`, `thimu`) | High — matches pamphlets exactly, dated Feb 5 |
| `pamphlets/` (both) | **Current canon** with localized defects (§7) | High — most recent grammar writing, Feb 4–5 |
| `manual/part5_complex` (ch18–21) | **Current canon**, near-clean | High — AUDIT_LOG: "written more recently with verified vocabulary" |
| `manual/part4_grammar` (ch11–17) | **Current, defective** — old vocab persists; ch15 uses an alien lexicon; ch16 inverts `ki`/`si` | High — verified by grep |
| `documents/phonology_rules.md`, `phonetics.md` | **Current canon** | High — matches all 789 words; oldest stable layer (2021 origin) |
| `documents/MODIFIER_FIRST_PHILOSOPHY.md`, `grammar/01-principles.md` | **Current canon** (01 has one stale word: `hauno`) | High |
| `documents/grammar/02–06`, `PARTICLE_REFERENCE.md`, `NUMERAL_REFERENCE.md` | **Current structure, stale examples** — particle system is authoritative; example vocabulary predates Jan 2026 (`kofe`, `nima`, `wiru`, `kela` "understand", `toremoa` "story", `wela` "good") | High |
| `CLAUDE.md` | **Current but stale in places** — `wela` example, Slot 1 order omits Evidentiality | High |
| `AUDIT_LOG.md` | **Record of intent, not of state** — claimed fixes never landed | High — verified directly |
| `documents/TERNARY_NUMBER_SYSTEM.md` | **Superseded proposal** — old arithmetic verbs (`wela`, `phei`), old scale-unit semantics, `nai` glossed 1PL | High — NUMERAL_REFERENCE supersedes it |
| `documents/tutorial/`, `guides/`, `language_guide.md`, `transmutation_guide.md` | **Stale** — pre-audit vocabulary throughout; teach retired constructions (`sho` quotative, bare relatives); reference a `reference_grammar.md` that doesn't exist; use particles (`silo` DUR, `lila` PURP) absent from PARTICLE_REFERENCE | High |
| `manual/part4_foundations/` | **Dead skeleton** — 7 chapter dirs, zero files | High |
| `book/` | **Superseded manuscript** — replaced by `manual/`; predates evidentials/relative clauses | High (inference from structure, mtimes, and AUDIT_LOG scope; no doc explicitly deprecates it) |
| `archive/` | **Historical only** — but `archive/CLAUDE.md`, `GEMINI.md`, `conceptual-roots.md` ("single source of truth") read as authoritative and contradict canon | High |
| `lexicon.db`, `scripts/`, `dashboard/` | **Generated/tooling, drifted** — DB missing 22 entries; ~17 of 19 scripts broken or unreliable; dashboard code current but environment cold | High — scripts were run |

---

## 3. Current Phi Model

**Phonology.** 10 consonants /h k l m n̪ p r s t̪ w/, 4 fricative digraphs /ɸ θ ʃ ʍ/, 5 pure vowels. (C)CV open syllables only; the only "cluster" is a digraph. All vowel sequences are hiatus (each vowel a syllable); three-vowel sequences forbidden; no repeated syllable within a word; all words consonant-initial, vowel-final; penultimate stress. **This holds perfectly in practice**: zero violations in 789 words. (16 entries have `syllables` metadata arrays that wrongly group vowel pairs, but the words themselves are legal.)

**Syntax.** SOV, strictly analytic (no inflection or derivation), zero articles, topic-drop when the referent is established. The organizing principle is modifier-first rather than head-directionality: objects before verbs, adjectives/possessors/quantifiers/demonstratives/relative clauses before nouns, but *prepositions* (not postpositions) — the one place head-final languages would disagree, resolved by declaring "announce then deliver" the master rule.

**Particles.** Three slots, all CV, no digraphs (deliberate, to keep particles instantly recognizable — the w/wh collision was engineered out in Jan 2026, commit `f862c47`). Slot 0 sentence frame (`wa` Q, `no` IMP, `lu`/`lu he` COND, `su` OPT, `pi` POL); Slot 1 pre-verbal stack ordered Tense > Aspect > Voice > Evidentiality > Modality > Negation (`to/so`; `ki/si/pa/te`; `se`; `hi/ke/ti/ho`; `po/na/ka`; `ma`); Slot 2 word-level (`lo` PL, `nu` ORD, `ko` FOC, `mo` CMPR, `ha/ra` deixis, `ne` NAME, honorifics `sa/ni/le`). Evidentials are optional; direct experience is unmarked.

**Complementizers and clause boundaries.** The most distinctive recent design: multi-syllable opener/closer pairs — `mena…meno` (declarative), `wela…welo` (embedded yes/no question), `shola…sholo` (quotation), with closers **required** because SOV stacks the embedded verb against the main verb; the closer marks the boundary. Openers end in -a, closers in -o. Clauses nest with strict pairing.

**Relative clauses.** Pre-nominal with invariant relativizer: `[rena CLAUSE] NOUN`, gap strategy, no resumptive pronouns, no closer (the head noun itself bounds the clause), headless relatives allowed.

**Pronouns, deixis, honorifics, vocative.** `mia`/`thia`/`shia` (1/2/3SG, non-gendered; glosses render 3SG as "ko"), pluralized with `lo`; reflexive `miso`, reciprocal `wiso`; `ha`/`ra` demonstratives; `ne` proper-name marker; three honorifics encoding *relationship* (respect/intimacy/role) rather than rank; vocative `kona` is extra-clausal.

**Numerals and classifiers.** Ternary: `mu`/`ta`/`wi` (0/1/2) plus countable scale units `shao`/`phoi`/`lau`/`rei` (3/9/27/81). Precision degrades by design past ~27; bare scale units mean approximate quantities. Four nature classifiers (`himo` people, `lipha` living, `themo` objects, `nophe` abstract), optional but valorized. Arithmetic via five value-framed verbs (`sholei` gather = add, `phanoi` portion = divide…); magnitude comparison via judgment-neutral `theloi`/`phenoi`.

**Vocabulary.** 789 entries (659 content, 110 function, 20 interjection), 13 semantic domains. Strong coverage: nature, community, wisdom, cognition, emotion. Absent by design: weapons, war, commerce. Absent apparently by accident: "write," egocentric/cardinal spatial terms, "how many." Every content entry carries bespoke sound-symbolism and pillar rationales.

**Transmutation vs translation.** Doctrine that ideas are rebuilt from Phi concepts rather than mapped word-for-word; documented with a full case study, though that case study now uses retired vocabulary.

**Tooling and data model.** JSON-per-word with a formal schema (near-perfect conformance); SQLite index (`lexicon.db`, 767/789 rows — misses all interjections and drops `kolo` via a `gloss UNIQUE` constraint); a FastAPI/React dashboard that reads the JSON directly (code current, environment not set up); ~19 scripts of which only `check_duplicates.py` and `lexicon_tool_simple.py` currently work as intended.

---

## 4. Development Archaeology

632 commits, 2021-04-03 → 2026-02-10, in eight phases. (All hashes/dates verified from git; "reason" lines are inference unless quoted.)

**Phase 1 — "plath" origin (Apr–Jun 2021, ~284 commits).** Initial commit `a7f361f` as "plath"; renamed to Phi (golden-ratio framing) within the phase. Per-POS markdown, a LaTeX manual with **Tengwar fonts**. Critically, the phonology in `24e7b6a:grammar/phonotactics.md` is already the current one — C/F/V inventories, (C)CV, hiatus, no diphthongs. **The sound system is the language's oldest surviving layer, unchanged for five years.**

**Phase 2 — dormancy and the voiced-stop wobble (Jul–Oct 2022, 5 commits).** `c06c530` added voiced stops b/d; `0cd94f7` removed them 13 days later. *Inference:* reverted to preserve the soft aesthetic — the earliest evidence that "gentleness" functions as a hard design constraint.

**Phase 3 — Obsidian revival (Feb–Apr 2024 + Oct 2024, ~87 commits).** Editing moved into an Obsidian vault; `book/` first appears (`b306f57`). Opaque bulk commits ("Edit lots of files.").

**Phase 4 — AI-assisted rebuild and the validator detour (May–Jun 2025, ~60 commits).** `52800e2` adds +39k lines of machine-generated candidate word lists; `7ca42cd` adds an LLM system prompt (commit style flips to LLM-generated from here). A Python sentence-validator suite reaches "100% validation accuracy across all 365 test cases" (`a508acc`, May 29) — and is deleted within days (`00eb7d7`, Jun 1). *Inference:* validator-driven development produced drift and report sprawl; the project pivoted to docs-as-source-of-truth. This problem — tooling racing ahead of, then falling behind, the language — recurs in every later phase.

**Phase 5 — JSON lexicon foundation (Jul–Aug 2025, ~70 commits).** The great purge: `97c09f6` (Jul 13) touches 483 files, −191,902 lines, deletes all validator artifacts and LaTeX, and **creates CLAUDE.md**. `scripts/` (Jul 21), `vocabulary/` (Jul 23), `lexicon.db` (Jul 24), `archive/` (Jul 24), and the pillar-bearing JSON schema (Jul 16) all originate here. Standalone Five Pillars docs are deleted and folded into per-word `pillars` fields. *Inference:* the pivot from "documents about a language" to "a database of a language."

**Phase 6 — typological crisis → modifier-first + ternary (Sep 2–16, 2025, 8 commits).** The pivotal week: `ad98b31` (Sep 9) "BREAKING CHANGE: All prepositions are now postpositions" (head-final consistency); `ff96ff2` (Sep 15) **reverts to prepositions** and creates MODIFIER_FIRST_PHILOSOPHY.md; `427b3e8` (Sep 16) replaces decimal numerals (the archive shows the old system reached `rai` = duodecillion) with ternary `mu/ta/wi` + scale units; `221f425` replaces 29 improvised words. *Inference, well-supported:* the postposition experiment exposed a conflict between orthodox head-final typology and the desired announce-before-deliver semantics; modifier-first was invented in six days to resolve that conflict and was then promoted to the language's master principle. Then a 3.5-month gap.

**Phase 7 — stabilization and vocabulary blitz (Dec 28, 2025 – Jan 30, 2026, ~63 commits).** PARTICLE_REFERENCE and NUMERAL_REFERENCE created (`65729a3`); evidentials added (`a28d947`, Dec 30); **~450 words coined in two days** (Jan 7–8) across 13 domains, followed immediately by collision cleanup (`c64965e`, 12 collisions); function-word review (conditional `thoe`, quantifiers, habitual aspect, discourse markers — Jan 14–15); particles reclassified into particles vs complementizers vs vocative (`c460eec`); CV-only particles eliminate the w/wh ambiguity (`f862c47`); dashboard added (`0832b80`).

**Phase 8 — manual, complementizers, relative clauses (Feb 2–10, 2026, ~50 commits).** New 7-part `manual/` replaces `book/`; sound-symbolism audit revises 28 arbitrary words (`7c38d76`); complementizer closers introduced and made **required** (`f99452e`, `cc3d42c`); interrogative complementizer redesigned `wena` → `wela`/`welo` (`da4bb61`); topic-drop added (`5bc2531`); pamphlets written; MkDocs site added and killed same day; correlative conjunctions added and removed same day (`cb2e30c`/`73c0dbe`); final commit adds AUDIT_LOG.md — whose fixes never landed.

**Abandoned-direction ledger:** voiced stops (2022); Tengwar/LaTeX manual; the sentence-validator suite; postpositions (6 days); decimal numerals 3–9; schema image prompts; MkDocs site; correlative conjunctions. The old **root-based phonosemantics** (every syllable a meaning-bearing root, per `archive/conceptual-roots.md`) was explicitly loosened: `archive/recap.md` records that a rationale-auditing script "was based on a flawed, overly rigid assumption that every syllable in a word must be a root," and the resolution was to treat roots as "an inspiration, not a constraint."

---

## 5. Inferred Design Motivations

All inference, each anchored to repo evidence:

- **Modifier-first instead of standard typology.** Direct evidence of the reasoning process exists in git: the project *tried* orthodox head-final (postpositions, `ad98b31`) and reverted within six days (`ff96ff2`). The motivation was philosophical, not typological — "announce then deliver" requires relators to precede their objects, which head-final typology forbids. Rather than accept a "mixed" system, the owner reframed the axis itself. This is the repo's clearest case of philosophy overriding linguistic convention *knowingly*, with the tradeoff documented in MODIFIER_FIRST_PHILOSOPHY.md.
- **Analytic grammar.** Stated directly (language_guide.md §2.6): stable word forms, no conjugation memorization, transparency. It also makes the lexicon database a complete description of the language — every form in a text should be a dictionary key, which is precisely what makes automated example-validation feasible (and what makes the current stale examples so detectable).
- **CV particles vs multi-syllable content words.** Evidence: phonology_rules.md §4.2 plus commit `f862c47` (eliminating w/wh particle ambiguity by restricting particles to CV). Motivation: instant grammatical/lexical disambiguation by word shape — a listener can classify every word's role from its syllable count and onset type before knowing its meaning. This is a genuinely engineered feature, not just aesthetics.
- **Phonosemantic vocabulary.** Inherited from the 2021–2024 root system; consciously *softened* in 2025 (recap.md) from "every syllable is a root" to holistic sound-symbolism narratives. Motivation: learnability and poetic coherence without the combinatorial straitjacket rigid roots imposed.
- **Ternary/approximate numbers.** The archive's decimal system with words for *undecillion* was the direct foil: PSYCHOLOGICAL_VIOLENCE_OF_MEASUREMENT.md argues precision itself enables ranking, accumulation, and dehumanization; the ternary system makes imprecision structural rather than advisory ("the violence of precise measurement is not forbidden but structurally impossible"). The number system is the language's strongest example of constraint-as-teaching.
- **Complementizer closers.** Purely technical motivation, stated in COMPLEMENTIZER_REFERENCE.md: SOV puts the embedded verb adjacent to the main verb; without `meno`, two stacked verbs are unparsable. The -a/-o opener/closer vowel alternation is an elegant systematization. This is the repo's best case of a real engineering problem solved within the aesthetic.
- **Optional evidentiality.** Added Dec 2025 (`a28d947`, "epistemic transparency"). Motivation: peace-linguistics — marking inference/report/assumption prevents asserting hearsay as witnessed fact. Made optional rather than obligatory (unlike Quechua-style systems), keeping the mindfulness opt-in rather than burdensome.
- **Topic-drop.** Added Feb 2026 (`5bc2531`), rationalized as "not saying what is already understood." *Inference:* this is a concession to naturalness — forced subject repetition was making texts stilted — and it's notable as the one feature that trades explicitness *away*, against the grain of announce-everything.
- **Avoidance/reframing of violent, industrial, precise concepts.** Consistent from the earliest archive docs to current CLAUDE.md red flags. The mechanism is lexical absence plus reframing (transmutation), not grammatical prohibition — you can still discuss calamity (`phaloa`) and struggle (`wothe`); you cannot efficiently discuss prices.

---

## 6. Evaluation Through Four Lenses

**As a constructed language / artlang.** *Strengths:* a distinctive, defensible aesthetic identity (the hiatus-heavy, fricative-soft sound is recognizably "Phi" across five years of material); an organizing principle that is genuinely original as artlang design (modifier-first as philosophy is not a Lojban clone or a Toki Pona clone); an unusually complete paper trail of design reasoning. *Limits:* the small phoneme inventory plus (C)CV plus no-duplicate-syllable constraints put hard combinatorial ceilings on the lexicon, and the dense minimal-pair neighborhoods (216 single-vowel-contrast pairs among content words) are the visible cost. *Tradeoff:* accepted deliberately — the constraints ARE the teaching — but the collision rate is now an empirical, not aesthetic, problem (§7).

**As an engineered semantic system.** *Strengths:* the JSON schema with mandatory concept/sound-symbolism/pillars fields is a real ontology, and it is honestly filled in (all 1,791 pillar rationales unique); word-shape encodes word-class; the 13-domain tag system replaced a failed 4,153-tag free-for-all (phi_tags_analysis_report.md). *Limits:* semantic relations exist only as prose — there are no explicit links between `theo` (read) and the missing "write," no antonym/derivation graph, so the "mycelial semantic families" CLAUDE.md calls for are aspirational rather than data. *Tradeoff:* prose rationales are richer than graph edges but unqueryable; the gap analysis findings (no write, no left/right) went undetected precisely because coverage isn't computable.

**As philosophical notation.** *Strengths:* this is the lens under which Phi is most successful. The ternary numerals, judgment-neutral comparison verbs (`theloi`/`phenoi`), relationship-based honorifics, and evidentials each *implement* a stated ethical position rather than merely gesturing at it; PSYCHOLOGICAL_VIOLENCE_OF_MEASUREMENT.md and MODIFIER_FIRST_PHILOSOPHY.md are serious position papers. *Limits:* some claimed mechanisms are asserted rather than demonstrated — see §7 on processing claims. *Tradeoff:* when philosophy and function conflict (postpositions, correlatives, rigid roots), the repo shows philosophy winning quickly and function being re-derived afterward; this keeps the system pure but generates rework.

**As a possible practical language.** *Strengths:* the grammar is complete enough for real texts — embedded clauses, relatives, questions, conditionals, voice, evidentials, discourse markers all exist with worked examples; analytic morphology plus strict word-shape rules genuinely lower the memorization load. *Limits:* (a) vocabulary gaps block ordinary life: no "write," "buy/sell/trade/money," "left/right," "how many," "problem," "city," "road," "bed," "clothes" — some intentional (commerce), some plainly accidental (a language with "read," "scholar," and "student" but no "write"); (b) the minimal-pair density means listening comprehension will be hard in noise; (c) hiatus-rich, multi-syllable content words make utterances long — by design, but it caps practical throughput; (d) no speakers, no texts longer than example sentences, no test of the ternary system against a real recipe or schedule. *Tradeoff:* Phi's own docs (NUMERAL_SYSTEM_GAPS.md) already acknowledge the sharpest of these and propose philosophy-compatible resolutions; the practical lens is limited more by unfinished work than by unresolvable contradictions.

---

## 7. Weaknesses and Tensions

### 7.1 The lost audit branch (documentation states fixes that don't exist)

- **Failure mode:** AUDIT_LOG.md on main claims ch11/ch14/ch15/ch17/ch20 vocabulary fixes are complete; none are present.
- **Mechanism:** work done on branch `audit/documentation-examples` was never merged; the branch has since been deleted; only the log file was cherry-picked to main (commit `47fe0dc`).
- **Evidence:** `git branch -a` shows no audit branch; `nolea` present in all 5 ch15 files; `kofe` in 7 manual files; `suno` at ch20/02:18,60 — all verified by grep this session.
- **Why it matters:** anyone (human or LLM) reading AUDIT_LOG will believe the manual is clean and build on rot; the project's memory of its own state is corrupted.
- **Recommendation:** redo the fixes on main directly from the log's replacement table; add a completion check to the log only after grep confirms zero hits.
- **Priority: immediate.**

### 7.2 Reference grammar teaches with a retired lexicon

- **Failure mode:** PARTICLE_REFERENCE.md, grammar/01–06, CLAUDE.md, COMPLEMENTIZER_REFERENCE.md, language_guide.md, and transmutation_guide.md use words the lexicon lacks or has reassigned: `kofe`, `nima`, `hauno`, `suno`, and — worse — reassigned words now teaching wrong meanings: `kela` glossed "understand" (lexicon: rejoice), `wela` "good" (lexicon: INT.COMP), `wiru` "child" (basket), `toremoa` "story" (mountain), `shiro` "forest" (tree), `hurao` "family" (patient), `lopia` "beautiful" (child), `mue` "in" (out-of).
- **Mechanism:** the Jan 2026 vocabulary blitz recoined hundreds of words; the manual's newest chapters were written against the new lexicon but the older reference docs were never re-baselined.
- **Evidence:** AUDIT_LOG's own "known incorrect patterns" list; systematic cross-check of doc examples against vocabulary JSON; `wela` = good+beautiful still at CLAUDE.md:62.
- **Why it matters:** reassigned words are far more dangerous than missing ones — a learner can't detect that `kela` no longer means "understand"; and CLAUDE.md drives every future LLM-assisted session, so its stale example actively regenerates drift.
- **Recommendation:** one sweep across documents/grammar/ + CLAUDE.md replacing the known-bad set; then the automated example validator (7.8).
- **Priority: immediate** (CLAUDE.md and PARTICLE_REFERENCE first).

### 7.3 Manual ch15 uses an alien, phonology-violating lexicon; ch16 inverts aspect glosses

- **Failure mode:** ch15 examples contain `via`, `vena`, `fina`, `tia`, `koa`, `luna`, `mira` — /v/ and /f/ don't exist in Phi; ch16 glosses `ki` as progressive and `si` as perfective, the reverse of every other document.
- **Mechanism:** ch15 appears to have been drafted from a different (possibly earlier or hallucinated) vocabulary snapshot and never reconciled; ch16 is a simple but systematic swap.
- **Evidence:** `ch15_verbs_time/combining_tense_aspect.md:31-32` ("mia fina to ki kira"); `ch16_voice_possibility/01_the_passive_se.md:85-91` vs PARTICLE_REFERENCE.md:120–136. Ironically, ch15 files carry the *newest* mtimes (Feb 10).
- **Why it matters:** these are the tense/aspect teaching chapters — the highest-traffic grammar content — and they currently teach words that cannot exist in the language.
- **Recommendation:** rewrite ch15 examples from the current lexicon; swap ch16's `ki`/`si` glosses.
- **Priority: immediate.**

### 7.4 Unsettled aspect and conditional inventories (grammar canon fork)

- **Failure mode:** PARTICLE_REFERENCE lists aspects `ki/si/pa/te`; manual ch11 adds `ro` (HAB); ch15 has `si/ki/pa/ro` (drops `te`); pamphlets use `ro` and a `tha` (PFV) that exists nowhere else. Conditionals: `lu` (Slot 0, sentence-initial per reference) coexists with conjunction `thoe` ("if"), and pamphlets use `lu` clause-internally.
- **Mechanism:** `ro` (habitual) and `thoe` were added during the Jan 14–15 function-word review (commits `f293579`…`800ad27`) but PARTICLE_REFERENCE (created Dec 28) was never updated; `tha` appears to be an error or an undocumented experiment.
- **Evidence:** grep results across manual/pamphlets/references; both `ro` and `thoe` exist in vocabulary JSON.
- **Why it matters:** this is not stale wording but a genuine unresolved design decision — two current documents give different answers to "what are Phi's aspects" and "how do you say if."
- **Recommendation:** rule explicitly: is `ro` canonical (then add to PARTICLE_REFERENCE and CLAUDE.md's stacking order)? Is `te` retained? Is `tha` an error? Is `thoe` the subordinator form and `lu` the sentence-frame form, or is one deprecated?
- **Priority: near-term** (decision), immediate for documenting whichever answer.

### 7.5 Hard lexical collisions: `phoi` and the `wela` family

- **Failure mode:** `phoi` is simultaneously the numeral scale-unit "nine-group" and the preposition "from" — `phoi phoi miona` ("from nine people") is a legal, baffling string. `wela` (INT.COMP opener) sits one vowel from `welo` (its closer), `welao` (good), and `towe` (well), in a language whose docs spent years using `wela` as "good."
- **Mechanism:** the small phonotactic space plus independent coinage passes; the complementizer redesign (`da4bb61`) reused the exact string that had been the language's flagship content word.
- **Evidence:** `content/nine-group.json` vs `function/preposition/from.json`; `function/complementizer/interrogative.json`; AUDIT_LOG's `wela`→`towe`/`welao` note; `check_duplicates.py` exits 1 on `phoi`.
- **Why it matters:** `phoi` breaks the language's own core promise that word shape announces word class (CV.V is supposed to signal preposition/pronoun/scale-unit — here it signals two at once in overlapping syntactic positions). The `wela` family guarantees learner interference with five years of legacy material.
- **Recommendation:** recoin one of the `phoi` pair (the preposition is cheaper to change than the numeral system); consider whether reusing `wela` for a function word was worth the collision or whether the complementizer should be recoined while the corpus is still small.
- **Priority: immediate** for `phoi`; near-term decision for `wela`.

### 7.6 Minimal-pair saturation in the `-elV-/-olV-` neighborhood

- **Failure mode:** auditory confusion between common words: `kela/keli/kelo/kelu/kolo/kolu/kulo` (rejoice/device/frame/become/equal/steady/guide), `helu/melu/nelu/phelu` (smooth/friend/revere/hold), `heloa/keloa/meloa/sheloa/theloa/weloa`.
- **Mechanism:** 10+4 onsets × 5 vowels with CV syllables makes ~70 syllables; the Jan 2026 two-day coinage of ~450 words filled the euphonious neighborhoods first. 216 content-word pairs now differ by a single vowel (1,480 edit-distance-1 pairs overall).
- **Evidence:** edit-distance analysis across all 789 entries.
- **Why it matters:** it directly undercuts the "Accessibility by Design" claim (language_guide.md §2.3) and the archive's own CREATION_WORKFLOW rule of "discarding minimal pairs" — the old workflow had an anti-collision step the blitz evidently didn't enforce.
- **Recommendation:** adopt a quantitative collision policy for new words (e.g., reject coinages within edit distance 1 of an existing word in the same POS class); audit the worst clusters and recoin the rarest members.
- **Priority: near-term.**

### 7.7 Processing claims outrun psycholinguistic reality (poetic rationale vs evidence)

- **Failure mode:** MODIFIER_FIRST_PHILOSOPHY.md claims listeners "process linearly" with "no need to hold elements in memory." In fact SOV with pre-verbal embedded clauses is a center-embedding design: in `mia mena thia mena shia wepu meno phaelo meno shelomui`, the listener holds two open `mena` frames and receives all three verbs stacked at the end. The closer system *mitigates* this (that's why `meno` is required) but the memory load is real and the doc claims the opposite. Similarly, phonetics.md claims sounds "common across the world's languages," but /ʍ/, /θ/, and /ɸ/ are each cross-linguistically minority sounds.
- **Mechanism:** philosophy documents written as advocacy rather than analysis.
- **Evidence:** the nesting example is from COMPLEMENTIZER_REFERENCE.md:92 itself; consonant typology is standard reference knowledge.
- **Why it matters:** not because the design is wrong — pre-announced structure genuinely helps *prediction* — but because false claims invite justified external criticism and obscure the honest tradeoff the closers were built to manage. The repo already shows the owner engineering around the real problem while the philosophy doc denies it exists.
- **Recommendation:** reframe: "modifier-first trades verb-anticipation load for early structural certainty, and closers bound that load." Replace the "most world languages" claim with "articulable by most speakers with modest practice."
- **Priority: long-term** (documentation honesty, not system change).

### 7.8 Tooling drift: the validation suite can't validate

- **Failure mode:** `check_vocabulary.py`/`phicheck` report 0 words (expect list-format JSON; all files are dicts); `find_available_words.py` therefore reports all 5,250 two-syllable forms free (a collision-generation machine if trusted); `lexicon_tool.py` crashes on `find`; `audit_rationales.py` and `check_word_vocabulary.py` reference nonexistent paths; `lexicon.db` silently omits all 20 interjections and drops `kolo` via `gloss UNIQUE`.
- **Mechanism:** the JSON format changed (list→dict) and directory layout changed after the scripts were written; nothing runs them, so nothing noticed. This is the third iteration of the same pattern (2025 validator purge, dashboard cold).
- **Evidence:** scripts executed read-only this session with results as listed in Appendix.
- **Why it matters:** every drift issue in this report (7.1–7.6) is machine-detectable, and the machines are all broken. `find_available_words.py` specifically would *cause* new collisions.
- **Recommendation:** keep exactly two tools — `check_duplicates.py` (works) and one rebuilt validator that checks: every example token exists in vocabulary with the glossed meaning; phonotactics; syllable-array hiatus correctness; slot ordering. Delete or archive the rest. Fix the DB builder (scan interjections, drop `gloss UNIQUE`).
- **Priority: immediate** for retiring the misleading scripts; near-term for the rebuilt validator.

### 7.9 Duplicated and contradictory secondary docs

- **Failure mode:** `documents/NUMERAL_SYSTEM_GAPS.md` and `documents/grammar/NUMERAL_GAPS.md` are near-identical duplicates; NUMERAL_REFERENCE.md uses `ne` as negation in comparisons (canon: `ma`; `ne` = NAME) and glosses `toremoa` as "stone" and "story" in adjacent sections; 03-questions.md's final example places `po` after the verb, violating its own Slot 1 rule; PARTICLE_REFERENCE's template line puts Slot 1 before the subject while its own example puts it after; CLAUDE.md's stacking order omits Evidentiality; TERNARY_NUMBER_SYSTEM.md proposes arithmetic verbs (`wela`, `phei`, `wealo`, `shalo`) superseded by NUMERAL_REFERENCE's (`sholei`, `leiro`, `welura`, `phanoi`); `manual/README.md` says Part IV "Not started"; `manual/part4_foundations/` is an empty duplicate skeleton; pamphlet-only gaps (`hasa`, `nae`, `nue`, and six correlatives `lera/lero, sera/sero, mira/miro` that don't exist in the lexicon despite the correlative feature being removed in `73c0dbe`).
- **Mechanism:** proposal documents and reference documents share a directory and a register; superseded proposals were never moved to archive.
- **Why it matters:** each is small; jointly they make "what is canon?" unanswerable without archaeology of this kind.
- **Recommendation:** the consolidation pass in §8.
- **Priority: near-term.**

### 7.10 Useful friction vs accidental obstruction (the philosophy boundary)

- **Where friction works as designed:** ternary numerals, classifier mindfulness, multi-syllable operation verbs, required closers — each slows speech in a way traceable to a stated value, with the cost analyzed in the project's own gap documents.
- **Where obstruction looks accidental:** no "write" (while "read," "scholar," "student" exist); no "how many" interrogative; no egocentric spatial terms (`left/right`) — nothing in the five pillars opposes handedness; topic-drop (which *reduces* explicitness) sits unreconciled with announce-everything; and the commerce gap is doctrinally motivated but total — Phi currently cannot express *gift-economy* transactions ("give," "share" exist, but "exchange/owe/offer-in-return" don't), which the philosophy actively endorses.
- **Recommendation:** treat NUMERAL_SYSTEM_GAPS.md's method (philosophical-tension analysis per gap) as the template and run it for spatial, commerce/gift, and literacy domains.
- **Priority: near-term** for "write"/"how many"; long-term for domains.

---

## 8. Recommendations (Prioritized Roadmap)

**Immediate cleanup (days):**

1. Redo the lost AUDIT_LOG fixes on main; verify with grep; update the log.
2. Fix CLAUDE.md: replace the `wela` example (line 62), add Evidentiality to the Slot 1 stacking order, and state the canon hierarchy explicitly.
3. Sweep PARTICLE_REFERENCE.md, COMPLEMENTIZER_REFERENCE.md, NUMERAL_REFERENCE.md, and grammar/01–06 for the known-bad word set (`kofe`, `nima`, `suno`, `hauno`, `wiru`, `kela`-as-understand, `wela`-as-good, `toremoa`-as-story, `shiro`-as-forest, `hurao`-as-family, `mue`-as-in, `ne`-as-NEG).
4. Rewrite manual ch15 examples with real vocabulary; swap ch16's `ki`/`si` glosses; fix 03-questions.md's post-verbal `po` and 02-particles' "that melu" typo.
5. Recoin the preposition `phoi` ("from").
6. Delete or quarantine the scripts that produce false results (`check_vocabulary.py`, `find_available_words.py`, `lexicon_tool.py`, `audit_rationales.py`, `check_word_vocabulary.py`, `calculate_possible_words.py`).

**Documentation/canon consolidation (1–2 weeks):**

7. Move to `archive/`: `book/`, `documents/tutorial/`, `documents/guides/`, `manual/part4_foundations/`, `TERNARY_NUMBER_SYSTEM.md`, one of the two NUMERAL_GAPS files, and `language_guide.md`'s stale sections (or rewrite it against current vocabulary — it's the philosophical front door and deserves to be current).
8. Add a one-page `CANON.md` (or a section in CLAUDE.md): the authority order is vocabulary JSON → COMPLEMENTIZER/PARTICLE/NUMERAL references → manual → pamphlets, with everything in archive/ explicitly non-normative. Add a deprecation header to `archive/CLAUDE.md`, `archive/GEMINI.md`, and `archive/conceptual-roots.md` ("single source of truth" must not survive in a stale file).
9. Fix `manual/README.md` status table; delete the retired correlatives from complementizers pamphlet 01/09 and fix its `hasa`/`nae`/`nue`/`hea` errors.

**Validation/tooling fixes (2–4 weeks):**

10. Rebuild one validator that enforces the AUDIT_LOG checklist mechanically: every example token in documents/, manual/, pamphlets/ exists in vocabulary with the glossed meaning; phonotactic legality; `syllables`-array hiatus correctness (16 current violations); slot ordering. Wire it into a pre-commit hook or a single `make check`.
11. Fix the lexicon.db builder: scan `interjection/`, drop the `gloss UNIQUE` constraint (it silently ate `kolo`), reconcile `lexicon_tool.py` vs `lexicon_tool_simple.py` into one tool.
12. Decide the dashboard's fate: either commit a working setup (requirements + build instructions verified) or archive it.

**Grammar decisions needing explicit settlement:**

13. Aspect inventory: is `ro` (HAB) canonical? Is `te` (CESS) retained? Is `tha` an error? Document the answer in PARTICLE_REFERENCE and CLAUDE.md.
14. Conditionals: division of labor between `lu` (Slot 0) and `thoe` (subordinating conjunction) — or deprecate one.
15. Whether `wela`/`welo` keeps its string despite the legacy collision, and whether `silo` (DUR) and `lila` (PURP) from the transmutation guide are real particles.
16. Classifier harmony in mixed-category arithmetic, and numeral negation ("not three but four") — both already flagged in NUMERAL_SYSTEM_GAPS.md.

**Vocabulary development priorities:**

17. "write" (glaring against read/scholar/student), "how many" interrogative, egocentric and cardinal spatial terms, gift-exchange verbs; then Tier 1 of NUMERAL_SYSTEM_GAPS (time units beyond day/week/month, fractions-as-portions, body-based measures).
18. Adopt the anti-collision policy (edit-distance ≥2 within POS class for new coinages) and re-audit the `-elV-/-olV-` cluster.

**Research questions for later:**

19. Corpus test: transmute one complete real text (a recipe, a meeting plan, a short story) and log every gap and every collision encountered — the fastest way to find the next hundred problems.
20. Ternary usability study: can two people actually schedule a meeting or split a harvest in Phi numbers? Where does approximation genuinely suffice vs fail?
21. Honest psycholinguistic framing of modifier-first (see 7.7), possibly with a small self-experiment in parsing nested `mena` clauses aloud.

---

## 9. Follow-Up Questions Worth Asking

1. "Draft the exact edits to fix CLAUDE.md and PARTICLE_REFERENCE.md against the current lexicon" — the highest-leverage single change.
2. "Redo the lost AUDIT_LOG fixes across the manual and show me the diff."
3. "Write the CANON.md authority document and the deprecation headers for archive files."
4. "Design the unified validator script (spec + implementation) that enforces the audit checklist."
5. "Settle the aspect system: lay out the arguments for and against `ro`/`te`/`tha` and recommend one inventory."
6. "Propose replacement coinages for the preposition `phoi` and evaluate whether `wela`/`welo` should be recoined."
7. "Run the collision audit: list the worst minimal-pair clusters with frequency-of-use estimates and recoining candidates."
8. "Transmute [a specific real text] into Phi and report every gap, collision, and awkwardness encountered."
9. "Design the missing spatial and gift-exchange vocabulary following the Word Creation Protocol, with pillar rationales."
10. "Rewrite MODIFIER_FIRST_PHILOSOPHY.md's processing claims to be defensible, keeping the philosophical case intact."

---

## 10. Appendix

**Commands run (read-only):** `git log --date=short --pretty --reverse` (full history, 632 commits), `git show --stat` on ~20 transition commits, `git log --follow` on key files, `git branch -a`, `git log --all --since=2026-02-04`; JSON analysis via jq/python3 (counts, schema conformance, phonotactic validation, edit-distance matrix); `sqlite3 lexicon.db` row/field comparison; executed `check_duplicates.py` (exit 1, 4 findings), `check_vocabulary.py`/`phicheck` (0 words — broken), `find_available_words.py` (invalid output), `lexicon_tool.py` (crash), `lexicon_tool_simple.py` (works, stale), `calculate_possible_words.py` (stale constants); grep verification of AUDIT_LOG claims. One side effect: importing `dashboard/main.py` created a git-ignored `__pycache__/` in dashboard/.

**Key files read in full:** CLAUDE.md; documents/{language_guide, phonology_rules, phonetics, MODIFIER_FIRST_PHILOSOPHY, TERNARY_NUMBER_SYSTEM, PSYCHOLOGICAL_VIOLENCE_OF_MEASUREMENT, transmutation_guide, VOCABULARY_REPLACEMENTS, NUMERAL_SYSTEM_GAPS, schema.json}; documents/grammar/{01–06, PARTICLE_REFERENCE, COMPLEMENTIZER_REFERENCE, NUMERAL_REFERENCE, NUMERAL_GAPS}; AUDIT_LOG.md. Via delegated deep-reads: all of manual/part4_grammar and part5_complex, both pamphlets, tutorial/guides samples, archive/ (ROOT_PHILOSOPHY, sound-meaning, CREATION_WORKFLOW, recap, conceptual-roots, core-primes, comparison reports, old CLAUDE.md/GEMINI.md), book/ structure, all 19 scripts, dashboard source, and the full vocabulary JSON corpus (789 files).

**Notable contradictions found (summary):** AUDIT_LOG vs working tree (fixes absent); `wela` = good+beautiful (CLAUDE.md:62, language_guide, PARTICLE_REFERENCE) vs `wela` = INT.COMP (lexicon, COMPLEMENTIZER_REFERENCE); `toremoa` = story vs stone vs mountain across three docs; `kela` = understand vs rejoice; `nai` = copula vs 1PL gloss (05-complex-constructions:84, TERNARY doc); `ne` = NAME vs negation (NUMERAL_REFERENCE:427); aspect inventory ki/si/pa/te vs +ro vs tha; `ki`/`si` glosses inverted in manual ch16; conditional `lu` vs `thoe`; `po` post-verbal in 03-questions.md:66; PARTICLE_REFERENCE template vs example on Slot-1/subject order; "say" = `shemui` vs `haolu`; sun = `remo` vs `suno` vs `sorae`; ch15's /v/ and /f/ words vs the phoneme inventory; NUMERAL_GAPS duplicated in two directories; manual README "Part IV not started" vs seven written chapters.

**Process note:** everything in sections 4 and 5 labeled *inference* is reconstruction from commit sequences, not owner testimony — the strongest-evidenced inferences are the postposition reversal (six days, two commits, and a philosophy document born between them) and the root-system loosening (explicitly narrated in archive/recap.md).
