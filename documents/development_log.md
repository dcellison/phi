# Phi Development Log

This is the lightweight decision record for Phi while it has one maintainer. It is not an RFC system. A decision enters canon only after its status becomes accepted and its vocabulary, grammar references, teaching material, validator, and generated artifacts agree.

Implementation status, dependencies, optional evaluation work, and the next development packages are tracked in the [status roadmap](roadmap.md). This log records decisions; the roadmap records execution.

## Statuses

- **Proposed**: worth investigating, with no authority over current Phi.
- **Experimental**: specified closely enough to use in test material, but not yet canon.
- **Accepted**: implemented and recorded in canon.
- **Superseded**: replaced by a later decision, with migration recorded where needed.
- **Rejected**: considered and declined, with the reason retained.

## Current decisions

| ID | Status | Decision | Evidence and consequence |
|---|---|---|---|
| D001 | Accepted | Phi is philosophy-first, not an auxiliary language. | Development prioritizes sustained philosophical expression and discussion. Everyday community use remains a proving context rather than a promise of general completeness. |
| D002 | Accepted | Use a solo-maintainer workflow. | Significant decisions are recorded here. Formal RFCs, voting, and governance machinery remain deferred until recurring users make them useful. |
| D003 | Accepted | Add `hasha … hasho` as the adapted guest frame. | It carries Phi-pronounceable external names and terms without granting them lexicon membership. Every occurrence remains marked. |
| D004 | Accepted | Add `patha … patho` as the exact opaque frame. | It preserves spelling, scripts, notation, measurements, identifiers, quotations, and faithful reports that core Phi cannot or should not reconstruct. |
| D005 | Accepted | External frames are nominal atoms. | Phi particles stay outside; `ne` precedes the whole atom; source grammar does not enter Phi. Guest frames cannot nest, and exact payload is opaque except for its escaped closer. |
| D006 | Accepted | Core refusals do not prohibit marked report. | Exact external material may carry a refused concept for testimony, history, critique, identity, consent, safety, quotation, or precision. Core admission remains a separate case-by-case decision. |
| D007 | Accepted | Describe design intentions as intentions. | Phi invites deliberate and cooperative practice but does not claim to make speakers peaceful, prove a cognitive effect, or be universally easy to learn. |
| D008 | Accepted | Treat modifier-first as the organizing principle. | The phrase remains the best mnemonic, but teaching must also name the particle system, frame rules, classifiers, conversions, and numeral system that learners actually encounter. |
| D009 | Accepted | Let `ne` license productive Phi-form names. | A chosen two-, three-, or four-syllable Phi-shaped onym may follow `ne` without becoming a lexicon entry. This gives names an open class while retaining guest frames for five-or-more-syllable, multi-token, or otherwise non-onym adaptations and exact frames for source-faithful forms. |
| D010 | Accepted | Treat practice and domain modules as optional lexical layers under one grammar. | Eight active profiles organize shared resources without moving them from the lexicon. Module terms are ordinary canonical content entries with validated `modules` metadata; Philosophical Reasoning establishes the generated-index and Part VII teaching pattern with 22 words, Systems and Shared Infrastructure applies it with 25, Ecological Systems and Material Life applies it with 30, and Commons and Collective Governance applies it with 30. Profiles add no grammar or parser mode. |
| D011 | Accepted | Treat the word-creation protocol as a quality checklist rather than an external admission gate. | The maintainer may coin a word because its concept is useful, valued, beautiful, or worth making easy to express. Every entry still requires complete schema fields, semantic scope and contrasts, sound and collision checks, examples, and synchronized references. |

## Release milestones

### Phi 2026.1: external register and honest scope

This release contains the two external frames, validator and rendering support, revised scope claims, advanced teaching material, a philosophical capability baseline, an original test corpus, and solo speech-audit tools. It contains no broad lexical renaming campaign.

### Phi 2026.2: productive names and optional vocabulary modules

This release makes proper names productive under `ne` without adding a new particle or treating names as vocabulary. It also establishes optional lexical modules under one grammar and gives Philosophical Reasoning, Systems and Shared Infrastructure, Ecological Systems and Material Life, and Commons and Collective Governance complete vocabulary passes. New words require implementation quality, not external proof of necessity. Any breaking lexical rename still requires recorded listening evidence and a migration table.

## Requires external evidence

The following questions cannot be settled by maintainer intuition or machine validation: acquisition speed, accent tolerance, real listening-confusion rates, curriculum pacing, spontaneous conversation repair, cultural interpretation of Phi's values, and any effect on thought or conduct. Until other speakers provide evidence, documentation must label claims in these areas as hypotheses or maintainer observations.

## Deferred infrastructure

Public RFCs, community councils, formal multilingual studies, raw audio collection, fixed release cadence, and automatic promotion of frequent guest forms are deferred. Reconsider them only after Phi has recurring users, a stable external register, substantial original philosophical writing, and repeated questions that the solo workflow cannot answer well.
