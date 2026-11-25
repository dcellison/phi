# Deferred questions and parked work

This ledger contains only questions and work that remain deliberately open or parked after maintainer review. Each entry records where the matter stands and what would bring it back into active work. Completed work belongs in the [status roadmap](roadmap.md) or [development log](development_log.md), not here. This file is a memory aid, not a source of language law; [`canon.md`](../canon.md) remains authoritative until a new decision changes it.

## Design and language questions

### Spoken source material and code-switching

Status: Open design question.

Canon keeps foreign wording and source-script names, exact values, identifiers, and other unassimilated artifacts outside Phi syntax. The rule preserves source fidelity and lets every writing mode carry the same Phi passage. A page can set the source beside the Phi; live conversation has no equally obvious margin.

The open question is whether every foreign expression must stay outside a complete Phi clause or whether a clearly bounded source expression may participate in an otherwise Phi utterance without becoming Phi vocabulary. An unadapted name or title is one test. Measurements, identifiers, and foreign quotations provide others. Phi's grammar and particle system are complete, so the answer belongs in existing grammar and discourse practice rather than another external frame. The canonical rule continues to govern until this question receives a ruling.

### Sexual and reproductive anatomy

Status: Queued as a separate scenario-led vocabulary effort.

Phi needs ordinary, respectful language for sexual and reproductive anatomy. Consent and self-description come first. Daily care, reproduction, and injury supply the other tests, none of which should require a person to make a clinical claim before naming part of their body.

The effort will inventory existing body, birth, consent, and Medical vocabulary, then decide which distinctions belong in base vocabulary, an optional module, a registered compound, or separately preserved source terminology. Anatomy cannot be assigned to gender by default, and one common body cannot become the standard against which others are treated as deviations.

### Optional subject and verb particles

Status: Open design question, raised by the maintainer on 2026-11-24 after the object particle was proposed. Measured, not ruled.

Phi's 2021 design had optional markers for subject, object, and verb (`si`, `na`, `te`, forms that now do other work). D134 restores an optional object marker as `ku`. The question is whether a subject particle and a verb particle should join it.

The addendum to `archive/seams_study.md` holds the measurement. On the ambiguous sentences of the texts shelf, `ku` can settle 72 percent; a subject particle or a verb particle adds about three points each; `ku` with `mua` or `sui` before a bare time phrase reaches 89 percent, and all four devices 95 percent. A subject particle would show where a main clause begins after a dependent clause and let a lone phrase be asserted as subject. A verb particle would separate manner from object where no Slot 1 particle stands and show where a relative clause ends; it would amount to an optional present-tense particle beside `to` and `so`.

What brings this back: the maintainer's ruling, or evidence from the phrase-reading ledger once `ku` is in use.

### Adjacent repeated words

Status: Open design question, raised by the maintainer on 2026-11-24 and deliberately left for a later discussion.

The maintainer never intended a Phi word to stand directly beside itself and finds the repetition ugly. Canon carries only the narrow case: a subject pronoun is not said a second time to mark its own possession (not `mia mia melu`). Nothing else forbids the pattern, the validators accept it, and it entered the corpus without his knowledge.

It arises in four ways. A pronoun subject meets the same pronoun as possessor or object (`shia shia rokai`, `mia mia riola`, `thia thia naseru`); *The Velveteen Rabbit* holds most of these, with others in *News from Nowhere* and *On Giving*. A name meets itself the same way (`ne tupiwa tupiwa`). Kinship stacks a term on itself, as in `phao phao phao` for a great-grandparent in *News from Nowhere*. The grammar itself produces the last kind: nested relatives open with `whu whu`, a headless relative sets a noun beside the same form used as its verb (`whu naphe naphe howela`), both taught in the Relative Clauses pamphlet, and two declarative frames opening together give `tha tha`, which a parser regression test pins.

Since this entry was written, D128 has licensed `miso` and `wiso` as possessors, so the pronoun kind has its replacement (`shia miso rokai`); the existing lines change as their texts are certified. A ruling still has to say whether the bar covers every adjacent repetition or only some of these kinds, and what replaces each one: a restructured clause, a new kinship word, a rule for nested frames. Several affected lines stand in certified translations, so each repair there needs fresh source-blind derivation, and a validator check should follow the ruling, not precede it.

## Parked corpus and tooling work

### Teaching pages that do not yet know `ku`

Status: Parked with the rest of the teaching pass, by the maintainer's instruction of 2026-11-24 that the structural questions come first.

D134 added a thirty-ninth particle. Canon, the references, and the manual teach it. These pages still say thirty-eight or give a particle inventory without it: `short_road.md` (the section heading "Thirty-eight particles keep their places", which `scripts/build_site.py` also pins), `primer/30_this_one_only_this_one.md` and `primer/README.md`, the Three Slots pamphlet (`00_title.md`, the Slot 2 pages, and `12_appendix.md`), `pamphlets/README.md`, and `pamphlets/catalogue.json`. The primer teaches no lesson on `ku`, and the Pronouns and Relative Clauses pamphlets do not mention it.

### Teaching pages that do not yet know `hia`

Status: Parked with the rest of the teaching pass, by the maintainer's instruction of 2026-11-24 that the structural questions come first.

D135 added a fourth core pronoun and stated that an unsaid subject is the subject of the sentence before. Canon, the entry, and the manual's pronoun chapter teach both. The Pronouns and Topic-Drop pamphlet still teaches three pronouns (`00_title.md`, `01_three_words_one_shape.md`, `07_the_dropped_subject.md`, the exercises, and the appendix), and the primer and the Short Road do not mention `hia`.

### Text lines awaiting the reference sweep

Status: Parked by the maintainer's instruction of 2026-11-24 that the language is settled first and the texts are swept once afterwards.

D128 and D135 settle how Phi keeps third persons apart: `miso` for the subject's own, an unsaid subject for the same one continuing, `hia` for the other of two, and a name for anything else. The texts were written before those rulings. Nothing in them was changed. The study in `archive/reference_study.md` holds the measurements.

- Two `shia` in one clause, 38 clauses, 25 of them in `velveteen_rabbit`: 29 are the same person twice and take `miso` (`shia shia nophae hisae`, `shia muo shia pelio`); three are two different persons (`shia shia to ru kema lothea`, `shia wei shia shonui to whishela` in `news_from_nowhere/chapter_06`, `shia nua shia muo shelira to wapi`) and may take `hia`; five set a singular against a plural and stand.
- `velveteen_rabbit` 224, `shia roa shia to pa rato. shia to pa rotiku.`, where the source-blind English has the wrong rabbit whirl and dance. The source's "whirl round" is the wild rabbit turning on itself.
- Two improvised forms in `velveteen_rabbit`: `ha shia` for "this one" (218) and `phirae shia` for "the other".
- Names said where the source has only a pronoun: 75 in `velveteen_rabbit` by a word match on the source line. Some can become `hia`, `miso`, or an unsaid subject; each needs reading in place, and a text is free to keep its names.

`velveteen_rabbit` is certified, so a changed unit there needs fresh source-blind derivation under D102. What brings this back: the maintainer's word that the language-level items of the November 2026 assessment are settled.

### Text lines awaiting the roles sweep

Status: Parked by the maintainer's instruction of 2026-11-24 that the language is settled first and the texts are swept once afterwards.

D136 rules that a lone bare phrase before a verb is its subject and that an object standing alone takes `ku`, and it gives every verb entry a valency. The texts were written before both. Nothing in them was changed. The study is `archive/roles_study.md`. Unit numbers count the aligned blocks of each file in order.

- A lone object with its subject unsaid, which now takes `ku`: `news_from_nowhere/chapter_02` 9 (`wethalu lomare`); `chapter_05` 107 (`serao miona ma thumela`) and 117 (`wisola lokue thela thiranu`). These three came from reading 214 clauses once; the sweep should read the role column of the phrase-reading ledger again, file by file.
- A lone object after `nela`, `thona`, or `sola`, where `ku` stays optional and each line needs judging for whether a reader could take the phrase for a new subject: `news_from_nowhere/chapter_04` 99 (`sola mioru nai menoa nila`); `chapter_06` 62 (`nela sheloi thena po phelu`) and 63 (`nela sio mia shia to thinu`); `solarpunk_manifesto` 13; `the_report_at_dusk` 10 (`nela repha po nilaki`).
- `velveteen_rabbit` 215, `shia tha lo phirae tupiwa so ma nila tho to soliru`. The Phi is right under the rule (the other rabbits are the subject). Its derived English, "it would not see the other rabbits", is the misreading the rule answers and needs fresh source-blind derivation under D102.
- An intransitive verb given a bare object against its own entry: `news_from_nowhere/chapter_03` 67 (`hasi`, which takes `wei`), 206 (`lonae`, which takes `wei`), and 233 (`roke`, which takes `ka`); `chapter_05` 80 (`lonae`).
- `news_from_nowhere/chapter_06` 106 has a `tha` frame before `peshu`, which its entry calls intransitive while allowing reported content. The entry and the line should be read together.

What brings this back: the maintainer's word that the language-level items of the November 2026 assessment are settled.

### Teaching pages that do not yet know the lone-phrase rule

Status: Parked with the rest of the teaching pass, by the maintainer's instruction of 2026-11-24.

Canon and the manual's page on building sentences teach the rule and the three kinds of verb. The primer, the Short Road, and the Three Slots, Relative Clauses, and Pronouns pamphlets do not. Where one of them shows `ku` before a lone phrase as a free choice, it now understates the rule.

### Text lines awaiting the ordinary-words sweep

Status: Parked by the maintainer's instruction of 2026-11-24 that the language is settled first and the texts are swept once afterwards.

D137 coins `tasa` (other), `sute` (happen), `pumi` (use), `seme` (easy), `teoki` (warn), and `soaru` (apologize). The texts were written before them and keep their earlier devices. Nothing in them was changed. Each list is a word match on the source line, so every unit needs reading against its source: many lines with "other" rightly keep `phirae` where the sense is different, and many with "use" are "used to", which is habit. Unit numbers count the aligned blocks of each file in order.

- `phirae` where the source says other, another, or else, some of which are now `tasa`: `babel_text` 7; `gibran/on_giving` 25; `gibran/on_work` 6, 17; `heart_sutra` 33; `metta_sutta` 9, 22, 23, 24; `news_from_nowhere/chapter_01` 21, 77; `chapter_02` 209; `chapter_03` 1, 44, 119, 120, 161, 175, 183; `chapter_04` 72; `chapter_05` 4, 22, 75, 144, 147, 152, 167, 213, 250, 258, 273; `chapter_06` 5, 20, 26, 72, 74, 98, 113; `solarpunk_manifesto` 32; `velveteen_rabbit` 12, 29, 46, 57, 215, 263, 327, 345, 409, 413, 420. One line already improvises `phirae shia` for "the other", which is now `hia`.
- `nai`, `kelu`, `phoa`, or `shua` where the source says happen, now `sute`: `news_from_nowhere/chapter_01` 2; `chapter_02` 119; `chapter_06` 14, 43; `solarpunk_manifesto` 38; `velveteen_rabbit` 63, 69, 70, 72, 85, 90, 160, 356.
- `kethua ma`, `reshi`, or another device where the source says easy or easily, now `seme`: `metta_sutta` 4; `news_from_nowhere/chapter_01` 77; `chapter_02` 103, 189; `chapter_05` 136, 164, 268; `chapter_06` 97; `tao_te_ching` 36, 38, 42, 43; `velveteen_rabbit` 72, 204.
- Use as a verb, to be read for `pumi`: `news_from_nowhere/chapter_01` 19; `chapter_02` 88; `chapter_03` 20, 156, 159, 169, 187; `chapter_05` 99, 135, 181, 189, 199, 232, 242, 272; `chapter_06` 72; `solarpunk_manifesto` 32, 33; `tao_te_ching` 16, 18, 20; `velveteen_rabbit` 352, 407.
- Warn and sorry: `news_from_nowhere/chapter_05` 76; `chapter_06` 74; `solarpunk_manifesto` 3.

Several of these texts are certified. A changed unit there needs fresh source-blind derivation under D102. The primer, the pamphlets, and the Short Road do not teach the six words. What brings this back: the maintainer's word that the language-level items of the November 2026 assessment are settled.

D138 coins `rese` (sort), `kothe` (problem), `hanelo` (avoid), `tetaru` (opposite), `hatura` (urgent), and `sekuna` (accuse), and records how ten other words are already said. The same parking applies and nothing in the texts was changed. Each list is again a word match on the source line, so every unit needs reading against its source. No source line says problem, urgent, blame, or accuse.

- Kind of or sort of, to be read for `rese`; several of these use `kire`, and a hedging "a kind of" rightly keeps `phea`: `news_from_nowhere/chapter_02` 163; `chapter_03` 157, 159, 162, 168, 195; `chapter_04` 83, 98; `chapter_05` 243, 257; `chapter_06` 4, 11, 51, 65; `velveteen_rabbit` 198, 284.
- Opposite or contrary, to be read for `tetaru`: `news_from_nowhere/chapter_01` 63; `chapter_03` 12; `chapter_04` 62; `tao_te_ching` 4.
- Avoid, now `hanelo`: `solarpunk_manifesto` 13.
- False, to be read for `phelira` before the noun; the Heart Sutra line is the relative-clause chain the assessment quoted: `heart_sutra` 30; `solarpunk_manifesto` 4.
- Early and late, to be read against `phoe theali thimu`, `pheo theali thimu`, `thorui`, and `lumae`: `news_from_nowhere/chapter_01` 35; `chapter_02` 16, 25, 62, 176, 181; `chapter_03` 83, 165; `chapter_04` 69, 97; `chapter_05` 132, 186, 187; `chapter_06` 46, 98; `tao_te_ching` 46; `velveteen_rabbit` 321.
- Expect and guess, to be read against `ho`, `remo` with `so`, `hasi`, and `hiru`: `news_from_nowhere/chapter_01` 6; `chapter_02` 33, 58; `chapter_04` 3, 82, 83, 106; `chapter_06` 4.
- Remind, similar, succeed, survive, and important, which the texts already render by the recorded devices and which need only a confirming read: `news_from_nowhere/chapter_03` 16, 102, 209; `chapter_06` 112; `tao_te_ching` 28, 29.

The primer, the pamphlets, and the Short Road do not teach these six words either.

D139 coins `mipi` (baby) and records how nine other words for people and places are already said. No source line says baby or infant, so the word leaves no text line behind. The texts already render the other nine by the recorded devices; a confirming read of `news_from_nowhere/chapter_04` 51 and `chapter_06` 7 (crowd) is all that is owed. The teaching documents do not teach `mipi`.

D140 coins `hopu` (hole), `riti` (line), `lakari` (map), `ripati` (ladder), and `mepe` (half). The same parking applies and nothing in the texts was changed. Each list is a word match on the source line. No source line says map, list, ladder, fence, or ore.

- Line or row, where three units stretch `sima` (thread) and are now `riti`: `news_from_nowhere/chapter_01` 53; `chapter_02` 123; `chapter_03` 137, 229.
- Half, to be read for `mepe`; half as a degree (half awake, a half smile) rightly keeps `la` or `kesho`: `gibran/on_work` 30; `news_from_nowhere/chapter_02` 5, 40, 48, 136; `velveteen_rabbit` 285.
- Steps let down into a boat, written `kalei thena`, to be read for `ripati`: `news_from_nowhere/chapter_02` 51.
- Burrow, which keeps `nowhu` (cave) and needs only a confirming read against `hopu`: `velveteen_rabbit` 122, 147.
- Corner and gate, which the texts already render by the recorded devices and which need only a confirming read: `gibran/on_work` 29; `news_from_nowhere/chapter_03` 37, 217; `chapter_04` 96; `velveteen_rabbit` 150, 329.

The teaching documents do not teach these five words.

### Text lines awaiting the small-words sweep

Status: Parked by the maintainer's instruction of 2026-11-24 that the language is settled first and the texts are swept once afterwards.

D130 and D131 settle how Phi says again, still, already, not yet, no longer, even, at once, and when. The texts were written before those rulings and keep their earlier devices. Nothing in them was changed. Unit numbers count the aligned blocks of each file in order.

- `we` where the source says again or once more, now `ture`: `news_from_nowhere/chapter_01` 63, 72, 73; `chapter_02` 43, 46, 54, 92, 140; `chapter_03` 42, 122, 136, 142, 143, 223; `chapter_05` 229; `chapter_06` 120. Five more units leave again unsaid.
- `we` where the source says even, now `we ko`: `gibran/on_children` 11; `news_from_nowhere/chapter_01` 64; `chapter_02` 26, 40, 101; `chapter_05` 30, 146; `chapter_06` 43, 118; `velveteen_rabbit` 40, 170, 258.
- Still, yet, already, and no longer by other means (`si` alone, `nosa`, `mawha thimu`, present `te`, or nothing): `gibran/on_children` 6; `news_from_nowhere/chapter_01` 27, 32; `chapter_02` 17, 62, 145, 155, 207; `chapter_03` 195; `chapter_04` 7, 29, 47; `chapter_05` 232; `chapter_06` 9, 24, 82, 109; `schleicher_fable` 3; `solarpunk_manifesto` 16, 33; `velveteen_rabbit` 88, 161, 259, 315, 337, 378, 422. Some of these already say the right thing (`to te` in *The Velveteen Rabbit* 161 and 337); each needs reading against its source.
- `nosa` or `reshi` where the source says at once, now `pheo mu thimu`: `news_from_nowhere/chapter_02` 57, 226, 231; `chapter_03` 9, 84; `chapter_04` 1, 6; `chapter_05` 27; `velveteen_rabbit` 313.
- A past `lu` sentence where the source says when: the review ledger lists these under `PHL005`.
- Until with a clause that was dropped: `news_from_nowhere/chapter_01` 68 and `velveteen_rabbit` 225. The noun forms elsewhere (`tei thia luwi`) remain grammatical.

Three of these texts are certified. A changed unit there needs fresh source-blind derivation under D102, and the sweep is the place for it. What brings this back: the maintainer's word that the language-level items of the November 2026 assessment are settled.

### Lexical relations between content words

Status: Parked until curated navigation would justify maintaining the field.

Revised definitions already cite the nearest Phi neighbour when the distinction helps a speaker. `thua` (fair) is located against `kolo` (equal), for example. This practice should continue as semantic neighbourhoods are revised, without making every entry recite a family tree. Search terms help English lookup and semantic domains collect broad areas, but neither records a direct relationship between two Phi words.

A future schema revision may add an optional `lexical_relations` array. Each item would name a canonical word and its controlled relationship, with a brief note where the boundary needs explanation. A link might record a contrast or place one word beneath a broader term. Validation can confirm that the target exists and apply reciprocal rules only where the relationship requires them.

This would be a curated lexical graph, not a substitute for vector search. Embeddings could later infer looser similarities from definitions and examples; curated links would preserve distinctions that the lexicon states outright. Revisit the field when the lexicon explorer needs related-word navigation or the project chooses to maintain an explicit lexical graph. The current schema and completed prose migration do not depend on that decision.

### Tengwar renderer verification

Status: Parked until the maintainer reopens Tengwar glyph tuning.

The renderer covers the full Phi inventory and builds every example in the Tengwar pamphlet. The gap is visual reference evidence for tehta placement. `h` has manual offsets but lacks independent confirmation; `p`, `k`, `w`, and internal `r` still rely on default bounding-box placement without preserved comparisons.

A verification pass will compare representative vowel placements against authoritative Tengwar Telcontar renders. Any justified offsets belong in `tengwar/glyphs.json`, accompanied by enough durable evidence to explain them. Temporary reference images belong under `build/` rather than among the project documents.

## Community direction

### Solarpunk community engagement

Status: Open strategic question.

Phi is not an auxiliary-language project. Solarpunk communities are the first audience Phi intends to approach, and the [Solarpunk Manifesto translation](../texts/solarpunk_manifesto.md) gives that relationship its first complete text. The [established modules](../documents/modules/README.md) cover ecology and governance directly. Work, household life, access, and shared systems carry the discussion into material practice and infrastructure.

The manner of approach is still open: which artifact should introduce Phi, what it asks of readers, how the project welcomes criticism, and what a healthy result would look like. [Book chapter 12](../book/12_a_language_for_the_commons.md) examines why solarpunk comes first, but the relationship extends beyond the book. Engagement begins when the maintainer is ready to offer Phi outside its own repository. A community will decide for itself whether any part of the language is useful.
