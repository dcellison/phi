# Phi

**kia** — hello.

Phi is a philosophical constructed language for practising mindful and compassionate speech. It asks speakers to attend to the present utterance: what they know, what they intend, and how their words may enter a relationship. Its unhurried quality is freedom from needless haste, not a prescribed speaking speed.

The language has one modifier-first organising principle, regular forms, and a shelf of literature that includes a Ring Verse transmutation whose refusal remains visibly separate from Tolkien's source.

**If you are new, do not start here.** Start with **[kia.md](kia.md)** — five minutes, and it will tell you whether Phi is for you. Or start with the language alive: everything below is rendered to **[dcellison.github.io/phi](https://dcellison.github.io/phi/)** on every merge. This page is the map of the repository for whoever comes back.

## The six doors

| | | |
|---|---|---|
| **The invitation** | [kia.md](kia.md) | Five minutes of contact with the language. The front door. |
| **The short road** | [short_road.md](short_road.md) | The whole language at walking pace: twenty minutes, one working example per idea. The second door. |
| **The primer** | [primer/](primer/) | Learn Phi by reading it: a prelude, twenty-four graded chapters about one household, and a capstone. No prior knowledge assumed. |
| **The manual** | [manual/](manual/) | The complete reference: phonology, the particle system, ternary numerals, social practice, source-material boundaries, translation, and transmutation. For verification and depth. |
| **The texts** | [texts on the site](https://dcellison.github.io/phi/texts/) | Phi's literature has nine close translations and eleven transmutations. Seven works have both; the Ring Verse is a refusal, and *News from Nowhere* keeps its opening chapters together as one book. |
| **The pamphlets** | [pamphlets on the site](https://dcellison.github.io/phi/pamphlets/) | Deep-dive companions to the manual: relative clauses and embedded speech, explained patiently, with exercises and answer keys. |

Five shelves divide the work. `documents/` says what the language **is**, the manual explains it, and the primer teaches it. `texts/` is where Phi is **read**; the pamphlets are where it is **practiced**.

## The language itself

| | |
|---|---|
| [vocabulary/](vocabulary/) | The lexicon: one JSON file per word, with its schema and semantic-domain catalogue beside it. More than one thousand entries. |
| [documents/](documents/) | Current language documentation, indexed and separated by purpose. |
| [documents/modules/](documents/modules/) | Experimental practice and domain profiles that organize shared core vocabulary and record gaps without creating separate grammars or lexicons. |
| [project/](project/) | Operational records: the development protocol, decision log, status roadmap, publication strategy, and release manifests. |
| [texts/](texts/) | The literary shelf: twelve short works and *News from Nowhere*, whose 32 chapters have their own book directory. The source witnesses live there too. |
| [pamphlets/](pamphlets/) | Focused teaching companions with extended explanation, exercises, and answer keys. |
| [canon.md](canon.md) | The authority order when documents disagree, and every settled design decision. |
| [colophon.md](colophon.md) | How Phi is made: the designer, the instrument, and the rules between them. Signed at the end, in the old way. |
| [site/](site/) | Maintained website assets for the lexicon explorer and reading shelves. Build the deployable site with `python3 scripts/build_site.py`; generated output goes to ignored `build/site/`. |

## Working on the repository

Everything is validated by machine, and the validation gates every pull request:

```bash
python3 scripts/validate_examples.py
```

This checks the lexicon against its [schema](vocabulary/schema.json) and the sound rules, forbids new minimal pairs, and verifies that every Phi sentence quoted in the manual, primer, texts, pamphlets, or invitation uses real words. If you change the vocabulary, regenerate the derived reference with `python3 scripts/generate_reference.py`. Design decisions live in [canon.md](canon.md); active work and evidence gates live in the [status roadmap](project/roadmap.md); the working protocol for creating words lives in [project/development_protocol.md](project/development_protocol.md); the longer-term intentions live in [the publishing strategy](project/publishing.md).

## Licensing

Three answers for three things. **The language itself is free.** Phi's words, sounds, and grammar may be used, spoken, written, and built on by anyone, forever, with no permission needed. **The code** in `scripts/`, `site/`, and `.github/` is Apache 2.0. **The content** in the lexicon, manual, primer, texts, pamphlets, documents, and project records uses [CC BY-NC-SA 4.0](LICENSES/CC-BY-NC-SA-4.0.txt): share and adapt it with attribution for noncommercial purposes, and keep derivatives under the same license. The Solarpunk Manifesto source and translation retain the source's CC BY-SA 4.0 license. [LICENSE](LICENSE) has the details.

---

*lo mia po nuawe thuroa.* — We can grow together.
