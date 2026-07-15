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
| D003 | Superseded | Add `hasha … hasho` as the adapted guest frame. | D012 removes the mechanism because guest material was neither Phi vocabulary nor fully external and created avoidable grammar, tooling, teaching, and script-parity costs. |
| D004 | Superseded | Add `patha … patho` as the exact opaque frame. | D012 keeps exact material outside Phi instead of embedding material that alternate Phi scripts cannot necessarily represent. |
| D005 | Superseded | External frames are nominal atoms. | D012 removes external atoms from Phi syntax. Source artifacts now remain in the surrounding medium while Phi refers to or analyzes them. |
| D006 | Superseded | Core refusals do not prohibit marked report. | D012 preserves testimony, history, critique, identity, consent, safety, quotation, and precision outside the Phi passage; lexical admission remains a separate case-by-case decision. |
| D007 | Accepted | Describe design intentions as intentions. | Phi invites deliberate and cooperative practice but does not claim to make speakers peaceful, prove a cognitive effect, or be universally easy to learn. |
| D008 | Accepted | Treat modifier-first as the organizing principle. | The phrase remains the best mnemonic, but teaching must also name the particle system, frame rules, classifiers, conversions, and numeral system that learners actually encounter. |
| D009 | Accepted | Let `ne` license productive Phi-form names. | A chosen Phi-shaped onym of two, three, or four syllables may follow `ne` without becoming a lexicon entry. Names with five or more syllables, multiple tokens, non-Phi shapes, and source-script forms remain outside the Phi passage unless the bearer or naming community accepts a valid adaptation. |
| D010 | Accepted | Treat practice and domain modules as optional lexical layers under one grammar. | Eight active profiles organize shared resources without moving them from the lexicon. Module terms are ordinary canonical content entries with validated `modules` metadata. Philosophical Reasoning establishes the generated-index and Part VII teaching pattern with 22 words; Systems and Shared Infrastructure applies it with 25; the other six modules each apply it with 30. Medical adds `lesawi` consent to shared core, Accessibility adds `sowelu` disabled, and Household adds `mirewu` private because those ordinary relations should not depend on optional study. Profiles add no grammar or parser mode. |
| D011 | Accepted | Treat the word-creation protocol as a quality checklist rather than an external admission gate. | The maintainer may coin a word because its concept is useful, valued, beautiful, or worth making easy to express. Every entry still requires complete schema fields, semantic scope and contrasts, sound and collision checks, examples, and synchronized references. |
| D012 | Accepted | Remove guest and exact external frames. | Phi sentences contain Phi words and Phi-form names. Unassimilated source text, scripts, values, identifiers, formulas, and quotations remain outside the Phi passage in the surrounding medium. The four former boundary words are retired from lexical use; because they are absent from the current lexicon, they receive no special treatment under the productive-name charter. |
| D013 | Accepted | Limit every Phi lexicon word to at most three syllables. | New four-syllable lexical words are prohibited. The 112 inherited content forms are recorded in a finite migration ledger and replaced without aliases through staged base and module passes. Productive onyms are not lexicon words; their separate charter permits two, three, or four syllables. |
| D014 | Accepted | Use `sileta` for sun as a lexical sibling of `silero` (star). | The final `a.e` hiatus of `sorae` was uncomfortable for the maintainer in ordinary speech. The new form keeps sun distinct from the wider class of stars, shares the audible `si.le` opening with `silero`, and passes the phonology and collision checks. The former word is retired from vocabulary and unavailable for lexical reassignment. |
| D015 | Accepted | Separate lexical retirement from name eligibility. | A retired form may be borne as a proper name when it satisfies the onym charter; this use restores no gloss, grammar, or lexical status. A proposed name that matches the current lexicon is allowed only when that entry is a content word. |
| D016 | Accepted | Do not retire four-syllable forms individually. | The universal lexical ceiling already excludes every four-syllable form from vocabulary, so `documents/validation/retired_forms.txt` records only shorter forms that need lexical protection. Any otherwise valid four-syllable form is available as a productive onym without consulting the migration ledger. |
| D017 | Accepted | Separate articulatory fact from optional sound symbolism in lexicon prose. | New and fully revised entries require `description`, `articulatory_notes`, and structured `examples`. Search terms and usage notes are optional, sound symbolism records only a genuine Phi-specific interpretation, and pillar rationales appear only for direct connections. Transitional schema alternatives preserve current entries while a committed coverage report tracks their migration. |
| D018 | Accepted | Give hot its own base adjective, `sukaro`, and keep `sulae` for moderate warmth. | Cooking, weather, bodily sensation, and safety need a direct distinction between warm and strongly heated. The new form passes phonology and collision checks, stays clearly apart from `pelui` cold, and shares only an audible family opening with `sulae` warm and `suloru` fever. |
| D019 | Accepted | Let `wuero` cover adjectival far and distant, and retire `thaeru`. | The two adjectives had the same range, while only `wuero` appeared in the active corpus. One ordinary near/far pair keeps the base lexicon smaller: `noshi` and `wuero` describe proximity, while `pai` and `woe` introduce the point from which distance is judged. |
| D020 | Accepted | Add base roots for damage, wear, weakness, and rigidity. | Corpus use exposed four distinctions that neighbouring words could not carry cleanly. `pukeri` names adverse change short of complete breakage, `rohemi` names gradual change through use or exposure, `huwa` names limited force in context, and `tinako` names resistance to bending or adjustment. Each form passes the phonology and collision checks; the words stay in base vocabulary because the distinctions recur beyond any one module. |
| D021 | Accepted | Add base adjective `shumeko` for sticky contact. | Food, repair, and cleaning scenarios exposed a surface property that location, wetness, and completed connection did not carry. `shumeko` describes a material or surface that clings after contact and resists easy separation; its quality noun supplies stickiness or adhesion. The form passes phonology and both collision checks, and ordinary household use keeps it outside optional modules. |
| D022 | Accepted | Add base adjective `selawi` for slippery contact. | Floor, path, and tool scenarios exposed low resistance to sideways sliding that wetness, texture, movement, and danger could not carry. `selawi` describes the contact behaviour without fixing the two surfaces in advance; its quality noun supplies slipperiness or low traction. The form passes phonology and both collision checks, and everyday warnings keep it outside optional modules. |
| D023 | Accepted | Add base nouns `patoku` solid, `larewu` liquid, and `heshowa` gas. | Substance names and behaviour clauses could not classify unknown material or state a general phase change. The nouns describe ordinary material categories under the conditions at hand, while `mirela` retains the analytical state and `kaero` the stage of a process. All three forms pass phonology and both collision checks. Their everyday use in handling and safety keeps them outside optional modules. |
| D024 | Accepted | Add base nouns `ponalu` size, `waleru` spatial length, and `hirawo` distance. | Quality nouns derived from large, long, and far kept an unwanted judgement at one end of each scale. `ponalu` leaves the separate dimensions intact; `waleru` stops at space rather than duration; `hirawo` does not absorb route choice or travel time. Exact values remain source material. All three forms pass phonology and both collision checks, and their ordinary use keeps them outside optional modules. |
| D025 | Accepted | Use `mioru` for beautiful and for beauty through the quality-noun rule; retire `phelora`. | The separate adjective and noun duplicated a distinction Phi already handles by syntax, and the maintainer found `phelora` uncomfortable in ordinary speech. Reclassifying `mioru` as an adjective preserves its established noun use through the quality-noun rule while giving both senses one comfortable form. `mioru` already occupied this sound shape; the migration creates no new form and retains its grandfathered edit-distance neighbours `lioru` and `moru`. The active corpus is migrated without an alias, and `phelora` is unavailable for lexical reassignment while remaining eligible as an onym under D015. |
| D026 | Accepted | Distinguish the core feeling lesson from the wider affective lexicon. | The nineteen forms taught together establish Phi's noun and adjective feeling patterns. The seven neighbouring adjectives already in the lexicon remain ordinary vocabulary, and future coinage follows the usual coverage gate. The registered constructions for anger, hatred, contempt, envy, loneliness, and wonder keep their forms because their parts carry useful meaning in those particular cases. Complexity by itself creates no general rule. |

## Completed discretionary lexical migrations

| Decision | Former form | Current form | Result |
|---|---|---|---|
| D014 | `sorae` (sun) | `sileta` (sun) | The new root forms an audible family with `silero` (star); the former root is retired. |
| D025 | `phelora` (beautiful) and noun-class `mioru` (beauty) | adjective-class `mioru` (beautiful; beauty by rule) | One adjective now serves both grammatical uses; `phelora` is retired and the separate noun entry is removed. |

## Release milestones

### Phi 2026.1: external register and honest scope

This release contains the two external frames, validator and rendering support, revised scope claims, advanced teaching material, a philosophical capability baseline, an original test corpus, and solo speech-audit tools. It contains no broad lexical renaming campaign.

### Phi 2026.2: productive names and optional vocabulary modules

This release makes proper names productive under `ne` without adding a new particle or treating names as vocabulary. It also establishes eight optional lexical modules under one grammar, each with a complete vocabulary pass. New words require implementation quality, not external proof of necessity. A discretionary or collision-driven breaking rename requires recorded listening evidence and a migration table; a separately accepted structural migration may supply another recorded reason and still requires complete replacement and migration checks.

### Completed breaking migration: firmer word and source boundaries

The completed migration supersedes the Phi 2026.1 external frames, prohibits four-syllable vocabulary, and records replacements for all 112 inherited four-syllable content forms. Productive names remain a separate open class with a four-syllable maximum. Historical release manifests remain unchanged as records of what those releases contained.

## Requires external evidence

The following questions cannot be settled by maintainer intuition or machine validation: acquisition speed, accent tolerance, real listening-confusion rates, curriculum pacing, spontaneous conversation repair, cultural interpretation of Phi's values, and any effect on thought or conduct. Until other speakers provide evidence, documentation must label claims in these areas as hypotheses or maintainer observations.

## Deferred infrastructure

Public RFCs, community councils, formal multilingual studies, raw audio collection, and a fixed release cadence are deferred. Reconsider them only after Phi has recurring users, stable source-material practice, substantial original philosophical writing, and repeated questions that the solo workflow cannot answer well.
