# The texts

This shelf holds translations, original Phi work, and one refusal. A translation stays answerable to the source's claims and distinctions. In an original, Phi comes first and the English follows instead of governing it. The Ring Verse keeps Tolkien's wording outside Phi and answers it openly. Each work names its relationship to a source before the first line.

The two directions are written at different times. First, the translator carries the source into Phi and settles every Phi sentence. Then the source is put away. The English in parentheses begins from Phi alone and preserves what Phi marks without copying its word order. If the Phi changes, that English is discarded and made again. The adjacent source line keeps the author's choices visible, but it has no hand in the English reading.

[How a Phi translation is made](../documents/reference/translation_process.md) gives the full procedure. The [certification ledger](../documents/evaluation/translation_process_status.md) names every translation document and shows which ones have completed it. CI checks the ledger against the shelf. Adding a translation or changing a certified layer therefore requires an explicit status update.

Short works each have one Markdown file. An author collection gets its own directory and catalogue, so separate source works can stay together without pretending to be chapters. A book also gets a directory, where its chapter sequence and shared source witness stay together. The `sources/` directory holds source witnesses for the ungrouped works.

## Short works

| Work | Method | Coverage | Text |
|---|---|---|---|
| The Practice of Love | Translation | All ten verses in Fausböll's English. | [Read](metta_sutta.md) |
| A Solarpunk Manifesto | Translation | Five opening paragraphs and all 22 propositions. | [Read](solarpunk_manifesto.md) |
| When Care Becomes Coercion | Original | A sustained dialogue that ends with a bounded agreement and an unresolved general question. | [Read](care_and_coercion.md) |
| The Thing Holds Its Mending | Original | An essay on a rebuilt wall that narrows its own claim under objection and leaves the chooser of criteria open. | [Read](the_mended_wall.md) |
| When a Report Is Enough | Original | An essay on a dusk warning that justifies one chosen inspection and leaves the next walk unassigned. | [Read](the_report_at_dusk.md) |
| Worth Does Not Require a Valuer | Original | An essay on a fallen branch where a failed grammatical proof leaves a smaller claim about worth and a reason to attend. | [Read](the_worth_of_a_fallen_branch.md) |
| The North Wind and the Sun | Translation | The complete fable, followed by its translation limits. | [Read](north_wind_and_sun.md) |
| Article 1 of the Universal Declaration of Human Rights | Translation | Both sentences, with rights, reason, conscience, and obligation kept distinct. | [Read](human_rights_article_one.md) |
| The Babel Text | Translation | Genesis 11:1-9 in Phi translation. | [Read](babel_text.md) |
| The Ring Verse, Refused | Refusal | The familiar four lines answered without claiming to translate them. | [Read](ring_verse_refusal.md) |
| Schleicher's Fable | Translation | The complete fable beside a controlled English source. | [Read](schleicher_fable.md) |
| Selections from The Little Prince | Translation | Three passages from Katherine Woods: the sheep, the secret, and responsibility for the tamed animal. | [Read](little_prince_excerpts.md) |
| The Velveteen Rabbit | Translation | The complete story, followed by its translation limits. | [Read](velveteen_rabbit.md) |
| Selections from the Tao Te Ching | Translation | Legge's chapters 8, 11, 17, 63, and 76 in full Phi translation. | [Read](tao_te_ching.md) |
| The Heart Sutra | Translation | Müller's smaller Heart Sutra in full Phi translation. | [Read](heart_sutra.md) |

## Author collections

| Collection | Coverage | Text |
|---|---|---|
| Kahlil Gibran | Four complete teachings begin a translation of *The Prophet*. | [Open the collection](gibran/) |

## Book-length work

| Work | Method | Coverage | Text |
|---|---|---|---|
| News from Nowhere | Book in progress | The first six chapters of a planned 32. | [Open the book](news_from_nowhere/) |

## Maintaining the shelf

The machine-readable [catalogue](catalogue.json) owns the website order, method labels, display titles, and summaries. Every short work, author collection, and book directory appears there once. A collection has its own member catalogue. The site build stops when a catalogue and its shelf disagree.
