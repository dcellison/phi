# Phi

**kia** — hello. Phi is a constructed language built for mindful communication: one grammatical rule, no irregular anything, sounds you cannot say fast, and a shelf of literature already written in it — including the Ring Verse, which the language refused to translate.

**If you are new, do not start here.** Start with **[kia.md](kia.md)** — five minutes, and it will tell you whether Phi is for you. Or start with the language alive: everything below is rendered to **[dcellison.github.io/phi](https://dcellison.github.io/phi/)** on every merge. This page is the map of the repository for whoever comes back.

## The five doors

| | | |
|---|---|---|
| **The invitation** | [kia.md](kia.md) | Five minutes of contact with the language. The front door. |
| **The primer** | [primer/](primer/) | Learn Phi by reading it: a prelude, twenty-four graded chapters about one household, and a capstone. No prior knowledge assumed. |
| **The manual** | [manual/](manual/) | The complete reference: phonology, the particle system, ternary numerals, social registers, transmutation. For verification and depth. |
| **The texts** | [texts on the site](https://dcellison.github.io/phi/texts/) | Phi's literature: eight transmutations, from the Metta Sutta to the whole of *The Velveteen Rabbit* — and the Ring Verse, refused, with the refusal shown line by line. |
| **The pamphlets** | [pamphlets on the site](https://dcellison.github.io/phi/pamphlets/) | Deep-dive companions to the manual: relative clauses and embedded speech, explained patiently, with exercises and answer keys. |

Four shelves, four jobs: `documents/` is what the language **is** (the specification), the manual is how it is **explained**, the primer is how it is **learned**, and the pamphlets are how it is **practiced**.

## The language itself

| | |
|---|---|
| [vocabulary/](vocabulary/) | The lexicon — one JSON file per word, the single source of truth for every form, meaning, and design rationale. About nine hundred words. |
| [documents/](documents/) | Grammar references, the compound registry, the phonology rules, the schema. |
| [pamphlets/](pamphlets/) | The sources for the texts shelf (eight transmutations, the Metta Sutta through *The Velveteen Rabbit*, plus the Ring Verse refusal) and the two study pamphlets. |
| [canon.md](canon.md) | The authority order when documents disagree, and every settled design decision. |
| [web/](web/) | The lexicon explorer — a static, searchable view over the vocabulary. Build and serve locally with `python3 scripts/build_explorer.py && python3 -m http.server -d web`. |

## Working on the repository

Everything is validated by machine, and the validation gates every pull request:

```bash
python3 scripts/validate_examples.py
```

This checks the lexicon against the schema and the sound rules, forbids new minimal pairs, and verifies that every Phi sentence quoted anywhere — manual, primer, pamphlets, the invitation — uses real words. If you change the vocabulary, regenerate the derived reference with `python3 scripts/generate_reference.py`. Design decisions live in [canon.md](canon.md); the working protocol for creating words lives in [documents/development_protocol.md](documents/development_protocol.md); the longer-term intentions live in [publishing.md](publishing.md).

## Licensing

Three answers for three things. **The language itself is free** — Phi's words, sounds, and grammar may be used, spoken, written, and built on by anyone, forever, no permission needed. **The code** (scripts/, web/) is Apache 2.0. **The content** — the lexicon, manual, primer, pamphlets, and documents — is [CC BY-NC-SA 4.0](LICENSES/CC-BY-NC-SA-4.0.txt): share and adapt with attribution, noncommercially, keeping derivatives open; commercial use needs separate permission. Details in [LICENSE](LICENSE).

---

*lo mia po nuawe thuroa.* — We can grow together.
