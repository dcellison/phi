# Phi

**kia** — hello.

Phi is a philosophical constructed language for practicing mindful and compassionate speech. It asks speakers to attend to the present utterance: what they know, what they intend, and how their words may enter a relationship. Its unhurried quality is freedom from needless haste, not a prescribed speaking speed.

The language has one modifier-first organizing principle, regular forms, a lexicon past a thousand words, a literature shelf of translations, transmutations, and original work, and a published book asking what such a language can honestly claim.

Everything below is rendered to **[dcellison.github.io/phi](https://dcellison.github.io/phi/)** on every merge; the site opens at hello and offers its doors from there. This page is the map of the repository.

## The shelf

| | | |
|---|---|---|
| **The walk** | [short_road.md](short_road.md) | The whole language at walking pace: twenty minutes, one working example per idea. |
| **The primer** | [primer/](primer/) | Learn Phi by reading it: a prelude, twenty-four graded chapters about one household, and a capstone. No prior knowledge assumed. |
| **The book** | [book/](book/) | Narrative nonfiction for a general reader: why the language works this way, and what the sciences of language and mind let it claim. A cold open, fourteen chapters, a close, and a consolidated bibliography. |
| **The manual** | [manual/](manual/) | The complete reference: phonology, the particle system, ternary numerals, social practice, source-material boundaries, translation, and transmutation. For verification and depth. |
| **The pamphlets** | [pamphlets/](pamphlets/) | Deep-dive companions to the manual: relative clauses and embedded speech, explained patiently, with exercises and answer keys. |
| **The texts** | [texts/](texts/) | Phi's literature: nine close translations, eleven transmutations, and one original work. Seven of the source works have both versions. The Ring Verse is a refusal, and *News from Nowhere* keeps its opening chapters together as one book. |
| **The lexicon** | [explorer on the site](https://dcellison.github.io/phi/explore.html) | Every word and registered compound, with meanings and relations close at hand. |

`documents/` says what the language **is**, the manual explains it, the primer teaches it, and the book asks **why**. `texts/` is where Phi is **read**; the pamphlets are where it is **practiced**.

## The language itself

| | |
|---|---|
| [vocabulary/](vocabulary/) | The lexicon source: one JSON file per word, with its schema and semantic-domain catalogue beside it. More than one thousand entries. |
| [documents/](documents/) | Current language documentation, indexed and separated by purpose. |
| [documents/modules/](documents/modules/) | Eight established vocabulary modules: optional specialist words organized over the one shared grammar, never a separate one. |
| [project/](project/) | Operational records: the development protocol, decision log, status roadmap, publication strategy, and release manifests. |
| [tengwar/](tengwar/) | The current Phi Tengwar specification, renderer outlines, and source font. Retired writing-system studies remain in [the archive](archive/writing_systems/). |
| [kia.md](kia.md) | The site's front page: the invitation and its seven doors, rendered to the index on every merge. |
| [canon.md](canon.md) | The authority order when documents disagree, and every settled design decision. |
| [colophon.md](colophon.md) | How Phi is made: the designer, the instrument, and the rules between them. Signed at the end, in the old way. |
| [site/](site/) | Maintained website assets for the lexicon explorer and reading shelves. Build the deployable site with `python3 scripts/build_site.py`; generated output goes to ignored `build/site/`. |

## Working on the repository

Everything is validated by machine, and the validation gates every pull request:

```bash
python3 -m pip install --requirement project/requirements.txt
python3 scripts/validate_examples.py
```

Install the pinned dependency once for each Python environment. The validator then checks every lexicon entry against the [executable schema](vocabulary/schema.json) before applying Phi's sound, layout, and corpus rules. It also forbids new minimal pairs and verifies every Phi sentence quoted anywhere in the documentation, from the front page and the walk through the primer, manual, pamphlets, texts, and book. If you change the vocabulary, regenerate the derived reference with `python3 scripts/generate_reference.py`. Design decisions live in [canon.md](canon.md); active work and evidence gates live in the [status roadmap](project/roadmap.md); the working protocol for creating words lives in [project/development_protocol.md](project/development_protocol.md); the longer-term intentions live in [the publishing strategy](project/publishing.md).

## Licensing

Three answers for three things. **The language itself is free.** Phi's words, sounds, and grammar may be used, spoken, written, and built on by anyone, forever, with no permission needed. **The code** in `scripts/`, `site/`, and `.github/` is Apache 2.0. **The content** in the lexicon, manual, primer, book, texts, pamphlets, documents, and project records uses [CC BY-NC-SA 4.0](LICENSES/CC-BY-NC-SA-4.0.txt): share and adapt it with attribution for noncommercial purposes, and keep derivatives under the same license. The Solarpunk Manifesto source and translation retain the source's CC BY-SA 4.0 license. [LICENSE](LICENSE) has the details.

---

*lo mia po nuawe thuroa.* — We can grow together.
