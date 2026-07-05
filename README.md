# Phi

**kia** — hello. Phi is a constructed language built for mindful communication: one grammatical rule, no irregular anything, sounds you cannot say fast, and a philosophy pronounced rather than printed.

**If you are new, do not start here.** Start with **[kia.md](kia.md)** — five minutes, and it will tell you whether Phi is for you. This page is the map of the repository for whoever comes back.

## The three books

| | | |
|---|---|---|
| **The invitation** | [kia.md](kia.md) | Five minutes of contact with the language. The front door. |
| **The primer** | [primer/](primer/) | Learn Phi by reading it: a prelude, twenty-four graded chapters about one household, and a capstone. No prior knowledge assumed. |
| **The manual** | [manual/](manual/) | The complete reference: phonology, the particle system, ternary numerals, social registers, transmutation. For verification and depth. |

## The language itself

| | |
|---|---|
| [vocabulary/](vocabulary/) | The lexicon — one JSON file per word, the single source of truth for every form, meaning, and design rationale. About nine hundred words. |
| [documents/](documents/) | Grammar references, the compound registry, the phonology rules, the schema. |
| [pamphlets/](pamphlets/) | The texts: the Metta Sutta (the first text ever written in Phi) and *The North Wind and the Sun*. |
| [CANON.md](CANON.md) | The authority order when documents disagree, and every settled design decision. |
| [web/](web/) | The lexicon explorer — a static, searchable view over the vocabulary. Build and serve locally with `python3 scripts/build_explorer.py && python3 -m http.server -d web`. |

## Working on the repository

Everything is validated by machine, and the validation gates every pull request:

```bash
python3 scripts/validate_examples.py
```

This checks the lexicon against the schema and the sound rules, forbids new minimal pairs, and verifies that every Phi sentence quoted anywhere — manual, primer, pamphlets, the invitation — uses real words. If you change the vocabulary, regenerate the derived reference with `python3 scripts/generate_reference.py`. Design decisions live in [CANON.md](CANON.md); the working protocol for creating words lives in [CLAUDE.md](CLAUDE.md); the longer-term intentions live in [PUBLISHING.md](PUBLISHING.md).

---

*lo mia po nuawe thuroa.* — We can grow together.
