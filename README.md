# Phi

**kia** — hello.

Phi is a philosophical constructed language for practicing mindful and compassionate speech. It asks speakers to attend to the present utterance: what they know, what they intend, and how their words may enter a relationship. Its unhurried quality is freedom from needless haste, not a prescribed speaking speed.

The language has one modifier-first organizing principle, regular forms, a lexicon past a thousand words, a literature shelf of translations and original work, and a published book asking what such a language can honestly claim.

The reader-facing shelves are rebuilt at **[phi.syrinx.net](https://phi.syrinx.net/)** whenever `main` changes; the site opens at hello and offers its doors from there. The rest of this page maps the language sources and working records behind them.

## The shelf

| | | |
|---|---|---|
| **The walk** | [short_road.md](short_road.md) | Phi's main systems at walking pace: about twenty minutes, with working examples along the way. |
| **The primer** | [primer/](primer/) | Learn Phi by reading it: a prelude, thirty graded chapters about one household, and a capstone. No prior knowledge assumed. |
| **The book** | [book/](book/) | Narrative nonfiction for a general reader: why the language works this way, and what the sciences of language and mind let it claim. A cold open, fourteen chapters, a close, and a consolidated bibliography. |
| **The manual** | [manual/](manual/) | The complete reference: phonology, the particle system, ternary numerals, social practice, source-material boundaries, and translation. For verification and depth. |
| **The pamphlets** | [pamphlets/](pamphlets/) | Focused companions to the manual, with extended examples, exercises, and answers. They cover difficult grammar as well as numerals, naming, source material, and Tengwar. |
| **The texts** | [texts/](texts/) | Phi's literature: translations answer to their sources, with a visible [certification mark](documents/reference/translation_certification.md) after they complete the isolated process. Original works begin in Phi, and the Ring Verse receives a refusal rather than a softened rendering. *News from Nowhere* keeps its opening chapters together as one book. |
| **The lexicon** | [explorer on the site](https://phi.syrinx.net/explore.html) | Every word and registered compound, with meanings and relations close at hand. |

`vocabulary/` and `documents/` say what the language **is**, the manual explains it, the primer teaches it, and the book asks **why**. `texts/` is where Phi is **read**; the pamphlets are where it is **practiced**.

## The language itself

| | |
|---|---|
| [vocabulary/](vocabulary/) | The lexicon source: one JSON file per word, with its schema and semantic-domain catalogue beside it. More than one thousand entries. |
| [documents/](documents/) | Current language documentation, indexed and separated by purpose. |
| [documents/modules/](documents/modules/) | Eight established vocabulary modules: optional specialist words organized over the one shared grammar, never a separate one. |
| [project/](project/) | Operational records for language decisions, current plans, translation certification, publication, and releases. |
| [tengwar/](tengwar/) | The current Phi Tengwar specification, renderer outlines, and source font. Retired writing-system studies remain in [the archive](archive/writing_systems/). |
| [kia.md](kia.md) | The site's front page: the invitation and its seven doors, rendered to the index on every merge. |
| [canon.md](canon.md) | The authority order when documents disagree, together with Phi's settled language decisions. |
| [colophon.md](colophon.md) | How Phi is made: the designer, the instrument, and the rules between them. Signed at the end, in the old way. |
| [site/](site/) | Maintained website assets for the lexicon explorer and reading shelves. Build the deployable site with `python3 scripts/build_site.py`; generated output goes to ignored `build/site/`. |

## Working on the repository

Machine checks guard the parts of the repository they can establish, and CI runs them on every pull request. The core local checks are:

```bash
python3 -m pip install --requirement project/requirements.txt
python3 scripts/validate_examples.py
python3 scripts/validate_sentences.py
python3 scripts/test_sentence_validator.py
python3 scripts/translation_process_status.py --check
python3 scripts/source_reconstruction.py
```

Install the pinned dependency once for each Python environment. The lexical validator checks every entry against the [executable schema](vocabulary/schema.json) before applying Phi's sound, layout, and corpus rules. It also checks lexical use across active documents. The sentence parser is a separate gate for complete examples in the lexicon and maintained teaching corpus. For the Morris chapters, the source-reconstruction checker selects each chapter from the stored novel and requires the ordered citations to reproduce it exactly. Machines can reject a particle in the wrong place or find a missing source phrase; they cannot decide whether a translation has understood Morris. Literary translations therefore use the [isolated process](documents/reference/translation_process.md) and its generated [certification register](documents/evaluation/translation_process_status.md).

The [CI workflow](.github/workflows/validate.yml) contains the complete recipe. If you change the vocabulary, regenerate the derived reference with `python3 scripts/generate_reference.py`. Settled language decisions live in [canon.md](canon.md); the current sequence lives in the [near-term development plan](project/near_term_development_plan.md); broader work and evidence gates live in the [status roadmap](project/roadmap.md). The [development protocol](project/development_protocol.md) governs language work, while the [publishing strategy](project/publishing.md) holds the longer view.

## Licensing

Phi separates the language from the work that describes it. **The language itself is free.** Phi's words, sounds, and grammar may be used, spoken, written, and built on by anyone, forever, with no permission needed. **The code** in `scripts/`, `site/`, and `.github/` is Apache 2.0. **The original project content** uses [CC BY-NC-SA 4.0](LICENSES/CC-BY-NC-SA-4.0.txt): share and adapt it with attribution for noncommercial purposes, and keep derivatives under the same license. The Solarpunk Manifesto source and translation retain their CC BY-SA 4.0 license, while third-party fonts retain their own licenses. [LICENSE](LICENSE) has the complete boundaries.

---

*lo mia po nuawe thuroa.* — We can grow together.
