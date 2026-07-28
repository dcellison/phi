# The Phi sentence validator

`shia ho womu nai.` contains familiar words, follows Phi phonotactics, and ends in a verb. It is still ungrammatical: the complement `womu` has slipped behind Slot 1. The sentence parser reports `PHS102` at that word. The repaired `shia womu ho nai.` puts the complement back before `ho nai`.

## Two validators

Phi keeps lexical integrity and sentence structure in separate programs.

| Program | Owns |
|---|---|
| `scripts/validate_examples.py` | JSON Schema, word forms, IPA, glosses, citations, names, documentation vocabulary, generated references, and repository integrity |
| `scripts/validate_sentences.py` | Complete utterance structure, grammatical frames, predicate shape, modifier-first order, and the three particle slots |

Neither program calls the other. A word-level check cannot quietly become a sentence parser, and a syntax change cannot disturb coining or citation work.

## What a parse contains

The parser tokenizes the whole utterance before judging any local sequence. Its root node spans the entire input, with nested nodes for the structures found inside it.

| Layer | Nodes |
|---|---|
| Utterance | sequences, conditions, clauses, coordination |
| Embedded structure | complement frames, relatives, adverbial frames |
| Standalone forms | vocatives, interjections, licensed fragments |

A result is valid only when the tree accounts for the entire input.

The tree matters when a short form is ambiguous. A verb can be an event noun, and an adjective can be a quality noun, without receiving a second lexicon class. The parser tries the grammatical readings available on the surface and accepts the sentence if at least one complete canonical parse exists.

## Commands

```bash
python3 scripts/validate_sentences.py
python3 scripts/test_sentence_validator.py
python3 scripts/validate_sentences.py --sentence "thepalu thiku to nai." --show-tree
python3 scripts/validate_sentences.py --sentence "henoi." --fragment
python3 scripts/validate_sentences.py --paths primer/26_making_it_happen.md
python3 scripts/validate_sentences.py --docs
```

The default command parses every structured sentence under `vocabulary/` and every recognized complete example in canon, the grammar references, the manual, pamphlets, primer, book, Kia, and the Short Road. `--paths` checks selected active Markdown beside the lexicon, `--lexicon-only` narrows the run to structured dictionary examples, and `--docs` scans every recognized complete example in the active repository. A literal `--sentence` is treated as a complete assertion unless `--fragment` licenses a standalone response or noun phrase. The scanner never enters `archive/`.

## Enforced structure

| Area | Parser gate |
|---|---|
| Surface | Lowercase Phi words, single spaces, periods only, and a final period |
| Lexicon and names | Every token is current vocabulary or a legal name atom in the position licensed by `ne` or an honorific |
| Sentence frame | Slot 0 opens the sentence; only `pi wa` and `pi no` combine; a discourse marker follows the frame and precedes the clause; a coordinator stands between equal constituents |
| Questions | `wa` asks about the whole proposition and stays out of a content question; each content-question clause has one gap-word; `misa` follows an explicit subject and precedes the remaining clause material |
| Predicate | A complete assertion ends in a lexical verb; interjections, vocatives, and recognized nominal fragments have their own trees |
| Slot 1 | Tense, aspect, voice, evidentiality, modality, and negation keep their fixed order and one-per-rank limit, with `se ka` as the single paired voice |
| Slot 2 | Wider scope comes first, a noun phrase uses one quantity strategy, `lo` cannot double, `mo ko` keeps its fixed order, and `lo ha` or `lo ra` is licensed only as a bare plural pronoun |
| Complements | `tha ... tho`, `pha ... pho`, and `sha ... sho` balance and nest; every embedded question takes `pha ... pho`; `wa` stays out of that frame; quotations close on one of the four canonical speech or hearing verbs |
| Dependent material | Relative, adverbial, purpose, and conditional material precedes what it modifies; a `lu` condition is a complete sentence before its consequence |
| Being and becoming | The predicative complement precedes the Slot 1 stack and `nai` or `kelu`; manner remains immediately before the final verb |
| Relations and number | Prepositions receive an object before the predicate stack, exact numerals descend through each scale once, and classifiers appear only where the numeral system licenses them |

Diagnostic codes begin with `PHS`. They are stable enough for regression tests and direct a reader to the first word at which the rejected structure becomes determinate.

`PHS085` catches the clearest missing question frame: a top-level gap-word is followed by a visibly finite inner predicate and then a matrix predicate. The diagnostic points back to `pha ... pho` without pretending that every unmarked verb has a known valency.

## Limits

The parser knows grammar, not the English translation beside it. It cannot decide whether an evidential claim is warranted, whether an honorific tells the truth about a relationship, or whether a source sentence has been translated faithfully.

Some attachment remains ambiguous on the Phi surface. A clause-initial pronoun can head a possessive phrase when later structure forces that reading, while event nouns and quality nouns retain their verb or adjective spelling. Embedded questions no longer add another uncertain boundary: `pha` opens the complete question and `pho` returns the listener to the surrounding clause. The parser accepts any legal surface parse instead of inventing semantic valency. It can enforce `misa` against a visible preposition, complement frame, or Slot 1 stack, but a bare noun chain may admit more than one legal subject-object reading. A sentence whose intended object order depends only on the English translation still needs a human reading. The machine catches determinate modifier-first failures and leaves genuine lexical ambiguity visible.

## Corpus adoption

CI parses every structured lexicon example, the maintained teaching corpus, and the grammar regression suite. Literary texts and older evaluation material predate this parser, so the broader `--docs` scan remains an audit and migration tool until each remaining corpus area has been reviewed against the new tree. A clean default run means every dictionary sentence and every recognized example in canon, the references, manual, pamphlets, primer, book, Kia, and the Short Road parses. It does not yet say the same about every literary or evaluation line.

Each reviewed corpus area can move under the mandatory command after its rejected sentences have been separated into text defects and parser defects. The text changes only after the parser defects are repaired. That order matters: an old sentence does not become grammatical merely because satisfying a mistaken diagnostic would be convenient.
