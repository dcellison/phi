# Phi

**kia** — hello. Phi is a philosophical constructed language built around one modifier-first organizing principle, regular forms, and a practice of unhurried communication. Its shelf of literature includes a Ring Verse transmutation whose refusal remains visibly separate from Tolkien's source.

**If you are new, do not start here.** Start with **[kia.md](kia.md)** — five minutes, and it will tell you whether Phi is for you. Or start with the language alive: everything below is rendered to **[dcellison.github.io/phi](https://dcellison.github.io/phi/)** on every merge. This page is the map of the repository for whoever comes back.

## The six doors

| | | |
|---|---|---|
| **The invitation** | [kia.md](kia.md) | Five minutes of contact with the language. The front door. |
| **The short road** | [short_road.md](short_road.md) | The whole language at walking pace: twenty minutes, one working example per idea. The second door. |
| **The primer** | [primer/](primer/) | Learn Phi by reading it: a prelude, twenty-four graded chapters about one household, and a capstone. No prior knowledge assumed. |
| **The manual** | [manual/](manual/) | The complete reference: phonology, the particle system, ternary numerals, social practice, source-material boundaries, translation, and transmutation. For verification and depth. |
| **The texts** | [texts on the site](https://dcellison.github.io/phi/texts/) | Phi's literature: four close translations and eleven transmutations, with three works appearing in both forms, alongside the first chapters of *News from Nowhere* and the Ring Verse refusal. |
| **The pamphlets** | [pamphlets on the site](https://dcellison.github.io/phi/pamphlets/) | Deep-dive companions to the manual: relative clauses and embedded speech, explained patiently, with exercises and answer keys. |

Four shelves, four jobs: `documents/` is what the language **is** (the specification), the manual is how it is **explained**, the primer is how it is **learned**, and the pamphlets are how it is **practiced**.

## The language itself

| | |
|---|---|
| [vocabulary/](vocabulary/) | The lexicon — one JSON file per word, the single source of truth for every form, meaning, and design rationale. More than one thousand entries. |
| [documents/](documents/) | Current language references and development evidence, indexed by purpose. This includes the [language assessment](documents/language_assessment.md), [lexicon expansion survey](documents/lexicon_expansion_survey.md), [status roadmap](documents/roadmap.md), and solo-maintainer development log. |
| [documents/modules/](documents/modules/) | Experimental practice and domain profiles that organize shared core vocabulary and record gaps without creating separate grammars or lexicons. |
| [pamphlets/](pamphlets/) | The sources for the texts shelf (twelve works, the Metta Sutta through *News from Nowhere*, plus the Ring Verse refusal) and the study pamphlets. |
| [canon.md](canon.md) | The authority order when documents disagree, and every settled design decision. |
| [colophon.md](colophon.md) | How Phi is made: the designer, the instrument, and the rules between them. Signed at the end, in the old way. |
| [web/](web/) | The lexicon explorer — a static, searchable view over the vocabulary. Build and serve locally with `python3 scripts/build_explorer.py && python3 -m http.server -d web`. |

## Working on the repository

Everything is validated by machine, and the validation gates every pull request:

```bash
python3 scripts/validate_examples.py
```

This checks the lexicon against the schema and the sound rules, forbids new minimal pairs, and verifies that every Phi sentence quoted anywhere — manual, primer, pamphlets, the invitation — uses real words. If you change the vocabulary, regenerate the derived reference with `python3 scripts/generate_reference.py`. Design decisions live in [canon.md](canon.md); active work and evidence gates live in the [status roadmap](documents/roadmap.md); the working protocol for creating words lives in [documents/development_protocol.md](documents/development_protocol.md); the longer-term intentions live in [publishing.md](publishing.md).

## Licensing

Three answers for three things. **The language itself is free** — Phi's words, sounds, and grammar may be used, spoken, written, and built on by anyone, forever, no permission needed. **The code** (scripts/, web/) is Apache 2.0. **The content** — the lexicon, manual, primer, pamphlets, and documents — is [CC BY-NC-SA 4.0](LICENSES/CC-BY-NC-SA-4.0.txt): share and adapt with attribution, noncommercially, keeping derivatives open; commercial use needs separate permission. Details in [LICENSE](LICENSE).

---

*lo mia po nuawe thuroa.* — We can grow together.
