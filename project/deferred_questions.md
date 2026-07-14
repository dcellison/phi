# Deferred questions and parked work

This ledger contains the questions and work that survived maintainer review on 2026-07-14. Each entry records where the matter stands and what would bring it back into active work. It is a memory aid, not a source of language law. [`canon.md`](../canon.md) and the [status roadmap](roadmap.md) stay authoritative until a new decision changes them.

## Design and language questions

### Native glyph mode

Status: Parked for further exploration.

Phi intends to acquire one native script. That script is the mode already reserved in canon as the glyph mode, not another mode beyond it; Romanization and Tengwar are the other two peers. No design has been chosen.

Possible lineages include the [Mayan-inspired word-block exploration](../writing_systems/mayan_glyph_mode.md) and featural approaches suggested by Tengwar and Hangul. A breath stroke, open-ended glyphs, and word-blocks are seeds for drawing rather than a specification. Design resumes when the maintainer chooses to pick up those experiments. A mature proposal will need to preserve the same Phi information in Romanization, Tengwar, and the glyph mode.

### Spoken source material and code-switching

Status: Open design question.

Canon keeps foreign wording and source-script names, exact values, identifiers, and other unassimilated artifacts outside Phi syntax. The rule preserves source fidelity and lets every writing mode carry the same Phi passage. A page can set the source beside the Phi; live conversation has no equally obvious margin.

The open question is whether every foreign expression must stay outside a complete Phi clause or whether a clearly bounded source expression may participate in an otherwise Phi utterance without becoming Phi vocabulary. An unadapted name or title is one test. Measurements, identifiers, and foreign quotations provide others. Phi's grammar and particle system are complete, so the answer belongs in existing grammar and discourse practice rather than another external frame. The canonical rule continues to govern until this question receives a ruling.

## Parked corpus and tooling work

### Legacy vocabulary prose audit

Status: Parked for a dedicated vocabulary pass.

The existing workflow gives every new or revised entry a separate Humanizer pass and checks it against the [Phi voice guide](../documents/reference/voice_for_models.md). Older canonical JSON entries are uneven. Descriptions, grammatical notes, pillar rationales, and semantic-domain rationales need the same examination; concept labels, ordinary English examples, and other schema values that contain prose belong in the pass as well.

Sound symbolism needs particular care. The field should follow the word through the mouth. It begins with breath and obstruction, then notices what the lips and tongue touch. Vowel depth, openness, stress, and hiatus shape the contour that reaches the ear. Poetic attention can sharpen that description, but syllables do not carry hidden dictionary meanings or require a grand story.

The audit works in `vocabulary/`, the canonical source, and generated lexicon references follow through regeneration. It may rewrite English prose while leaving Phi forms and exact glosses fixed. Each batch ends with reference generation and full validation.

### Tengwar renderer verification

Status: Parked until Tengwar work resumes or the mode approaches publication-ready status.

The renderer covers the full Phi inventory and builds every example in the Tengwar pamphlet. The gap is visual reference evidence for tehta placement. `h` has manual offsets but lacks independent confirmation; `p`, `k`, `w`, and internal `r` still rely on default bounding-box placement without preserved comparisons.

A verification pass will compare representative vowel placements against authoritative Tengwar Telcontar renders. Any justified offsets belong in `writing_systems/tengwar_glyphs.json`, accompanied by enough durable evidence to explain them. Temporary reference images belong under `build/` rather than among the project documents.

## Community direction

### Solarpunk community engagement

Status: Open strategic question.

Phi is not an auxiliary-language project. Solarpunk communities are the first audience Phi intends to approach, and the [Solarpunk Manifesto translation](../texts/solarpunk_manifesto.md) gives that relationship its first complete text. The [established modules](../documents/modules/README.md) cover ecology and governance directly. Work, household life, access, and shared systems carry the discussion into material practice and infrastructure.

The manner of approach is still open: which artifact should introduce Phi, what it asks of readers, how the project welcomes criticism, and what a healthy result would look like. [Book chapter 12](../book/treatment.md) will examine why solarpunk comes first, but the relationship extends beyond the book. Engagement begins when the maintainer is ready to offer Phi outside its own repository. A community will decide for itself whether any part of the language is useful.
