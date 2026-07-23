# Deferred questions and parked work

This ledger contains the questions and work that survived maintainer review on 2026-07-14. Each entry records where the matter stands and what would bring it back into active work. It is a memory aid, not a source of language law. [`canon.md`](../canon.md) and the [status roadmap](roadmap.md) stay authoritative until a new decision changes them.

## Design and language questions

### Spoken source material and code-switching

Status: Open design question.

Canon keeps foreign wording and source-script names, exact values, identifiers, and other unassimilated artifacts outside Phi syntax. The rule preserves source fidelity and lets every writing mode carry the same Phi passage. A page can set the source beside the Phi; live conversation has no equally obvious margin.

The open question is whether every foreign expression must stay outside a complete Phi clause or whether a clearly bounded source expression may participate in an otherwise Phi utterance without becoming Phi vocabulary. An unadapted name or title is one test. Measurements, identifiers, and foreign quotations provide others. Phi's grammar and particle system are complete, so the answer belongs in existing grammar and discourse practice rather than another external frame. The canonical rule continues to govern until this question receives a ruling.

### Sexual and reproductive anatomy

Status: Queued as a separate scenario-led vocabulary effort.

Phi needs ordinary, respectful language for sexual and reproductive anatomy. Consent and self-description come first. Daily care, reproduction, and injury supply the other tests, none of which should require a person to make a clinical claim before naming part of their body.

The effort will inventory existing body, birth, consent, and Medical vocabulary, then decide which distinctions belong in base vocabulary, an optional module, a registered compound, or separately preserved source terminology. Anatomy cannot be assigned to gender by default, and one common body cannot become the standard against which others are treated as deviations.

## Parked corpus and tooling work

### Legacy vocabulary prose audit

Status: Complete.

The workflow gives every new or revised entry a separate Humanizer pass and checks it against the [Phi voice guide](../documents/reference/voice_for_models.md). All 1,275 canonical entries now follow the target contract: definitions live in `description`, physical pronunciation in `articulatory_notes`, and usage in structured `examples`. Content entries also carry accurate semantic-domain rationales. Search terms, usage notes, sound symbolism, and direct pillar connections remain optional.

Articulatory notes follow the word through the mouth and describe breath, contact, release, stress, and hiatus accurately. Sound symbolism has a narrower optional role: it may preserve a genuine Phi-specific association, but it cannot turn a syllable into a hidden morpheme or treat a phoneme's meaning as universal.

The completed lexicon audit worked in `vocabulary/`, the canonical source, and regenerated every dependent reference. [`documents/validation/vocabulary_prose_coverage.json`](../documents/validation/vocabulary_prose_coverage.json) records 1,275 target entries with no legacy, partial, or dual remainder. The contextual retrofit checked active Phi against that finished vocabulary and is also complete: the literary shelf, the drafted book, all seven manual parts, the primer, all nine pamphlets, and the current documents are current, with the evaluation corpus the final batch. A passage reopens only for a real semantic, factual, voice, or corpus problem.

### Lexical relations between content words

Status: Parked until curated navigation would justify maintaining the field.

Revised definitions already cite the nearest Phi neighbour when the distinction helps a speaker. `thua` (fair) is located against `kolo` (equal), for example. This practice should continue as semantic neighbourhoods are revised, without making every entry recite a family tree. Search terms help English lookup and semantic domains collect broad areas, but neither records a direct relationship between two Phi words.

A future schema revision may add an optional `lexical_relations` array. Each item would name a canonical word and its controlled relationship, with a brief note where the boundary needs explanation. A link might record a contrast or place one word beneath a broader term. Validation can confirm that the target exists and apply reciprocal rules only where the relationship requires them.

This would be a curated lexical graph, not a substitute for vector search. Embeddings could later infer looser similarities from definitions and examples; curated links would preserve distinctions that the lexicon states outright. Revisit the field when the lexicon explorer needs related-word navigation or the project chooses to maintain an explicit lexical graph. The active prose migration does not depend on that decision.

### Tengwar renderer verification

Status: Parked until Tengwar work resumes or the mode approaches publication-ready status.

The renderer covers the full Phi inventory and builds every example in the Tengwar pamphlet. The gap is visual reference evidence for tehta placement. `h` has manual offsets but lacks independent confirmation; `p`, `k`, `w`, and internal `r` still rely on default bounding-box placement without preserved comparisons.

A verification pass will compare representative vowel placements against authoritative Tengwar Telcontar renders. Any justified offsets belong in `tengwar/glyphs.json`, accompanied by enough durable evidence to explain them. Temporary reference images belong under `build/` rather than among the project documents.

## Community direction

### Solarpunk community engagement

Status: Open strategic question.

Phi is not an auxiliary-language project. Solarpunk communities are the first audience Phi intends to approach, and the [Solarpunk Manifesto translation](../texts/solarpunk_manifesto.md) gives that relationship its first complete text. The [established modules](../documents/modules/README.md) cover ecology and governance directly. Work, household life, access, and shared systems carry the discussion into material practice and infrastructure.

The manner of approach is still open: which artifact should introduce Phi, what it asks of readers, how the project welcomes criticism, and what a healthy result would look like. [Book chapter 12](../book/12_a_language_for_the_commons.md) examines why solarpunk comes first, but the relationship extends beyond the book. Engagement begins when the maintainer is ready to offer Phi outside its own repository. A community will decide for itself whether any part of the language is useful.
