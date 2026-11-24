# The Phi sentence validator

`shia ho mua womu nai.` contains familiar words, follows Phi phonotactics, and ends in a verb. It is still ungrammatical: the complement `mua womu` has slipped behind Slot 1. The sentence parser reports `PHS102` at its first word. The repaired `shia mua womu ho nai.` puts the complement back before `ho nai`.

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
| Slot 2 | Wider scope comes first, a noun phrase uses one quantity strategy, `lo` cannot double, `mo ko` keeps its fixed order, and `lo ha` or `lo ra` is licensed only as a bare plural pronoun; `we` and `li` on a verb stand before the Slot 1 stack, never between it and the verb (`PHS106`) |
| Complements | `tha ... tho`, `pha ... pho`, and `sha ... sho` balance and nest; every embedded question takes `pha ... pho`; `wa` stays out of that frame; quotations close on one of the four canonical speech or hearing verbs |
| Dependent material | Relative, adverbial, purpose, and conditional material precedes what it modifies; a `lu` condition is a complete sentence before its consequence; `pheo` and `phoe` stand over a clause or a time phrase and over no other noun or bare `ha` or `ra` (`PHS062`); the preposition `tei` may open a clause before the main clause, and after a subject it takes a noun phrase only |
| Being and becoming | The predicative complement precedes the Slot 1 stack and `nai` or `kelu`; manner remains immediately before the final verb |
| Relations and number | Prepositions receive an object before the predicate stack, exact numerals descend through each scale once, and classifiers appear only where the numeral system licenses them |

Diagnostic codes begin with `PHS`. They are stable enough for regression tests and direct a reader to the first word at which the rejected structure becomes determinate.

`PHS062` reads a time phrase narrowly: a time noun at the head, with nothing before it except counts, quantifiers, adjectives, Slot 2 particles, or a relative clause. Inside a clause the check stops at the first time noun it reaches, so `phoe kelua nurome` (before the morning meal) passes as `phoe kelua`; that shape still needs a reader.

`PHS085` catches the clearest missing question frame: a top-level gap-word is followed by a visibly finite inner predicate and then a matrix predicate. The diagnostic points back to `pha ... pho` without pretending that every unmarked verb has a known valency.

## Order advisories

`shia siora to phaelo.` (they felt joy) and `shia pakiro to whano.` have the same shape: an adjective directly before the Slot 1 stack. In the first, the adjective is a quality noun and the verb's object. In the second it is a manner word, and canon puts manner inside the stack: `shia to pakiro whano.` Choosing between them takes verb valency, which the lexicon does not record, so the parser accepts both.

It also reports both. An advisory marks a sentence that parses and has a second reading under which canon's order is broken. Advisories carry `PHL` codes, print as `REVIEW` lines, and never change an exit code.

| Code | Shape | The order canon asks for, if the doubtful reading is the intended one |
|---|---|---|
| `PHL001` | An adjective stands directly before the Slot 1 stack of a verb other than `nai` or `kelu` | A manner or depictive word stands inside the stack, directly before the verb |
| `PHL002` | A noun or pronoun stands between a clause-initial `mia`, `thia`, or `shia` (or `lo` with one of them) and a phrase opened by a preposition, `pheo`, or `phoe` | A direct object follows its adjuncts: S PP O V |
| `PHL003` | A period stands before `sho` | The closer follows the last quoted word. This one has no second reading: every line is a fault awaiting repair |
| `PHL004` | A prepositional phrase opens a clause that then names a pronoun or a name, or a `pheo` or `phoe` time phrase opens a sentence and a noun phrase follows | An adjunct that is not a clause follows an explicit subject |
| `PHL005` | A `lu` condition and its consequence both carry `to`, and neither carries `ro` | `lu` states an open condition or a habit. One past occasion, the English "when", takes `pheo` for sequence or `whau` for overlap. The sentence stands when the speaker really does not know whether the condition held |

The checks stay quiet where the surface settles the reading. For `PHL001` that means a name atom, or an adjective marked as a noun phrase by a preposition, `lo`, a numeral, a quantifier, a classifier, or coordination with a noun. For `PHL002` it means a gapped relative clause, a compound subject, and a bare time phrase such as `nosa` or `wireo philo`, which is an adjunct like the phrase after it. The cost of the last exemption is that a time noun used as a real object before an adjunct passes unseen. `PHL004` stays quiet when no subject follows the opening phrase (`mua womu therilu.`, `no wei mia shua.`), and it does not see a fronted place phrase whose subject is an ordinary noun. Unframed speech and an untensed dependent clause leave no mark the parser can find; both need a reader.

```bash
python3 scripts/validate_sentences.py --sentence "shia pakiro to whano."
python3 scripts/validate_sentences.py --paths texts/example.md --lint
python3 scripts/audit_sentence_order.py --output documents/validation/sentence_order_baseline.txt
python3 scripts/audit_sentence_order.py --check
```

A literal `--sentence` always prints its advisories. Corpus runs print them with `--lint`.

`documents/validation/sentence_order_baseline.txt` is the review ledger. It lists every advisory in the lexicon and the active Markdown, keyed by code, flagged word, file, and sentence, with no line numbers, so unrelated edits leave it alone. CI regenerates it and fails on any difference. A new candidate therefore reaches review as one added line, and a repaired sentence as one removed line.

The ledger mixes two kinds of line: sentences whose order is right under the reading their author meant, and sentences that still need repair. Presence in the ledger means a sentence has been seen, not that it has been cleared. Lines from `texts/` wait for the two-phase translation process before any change.

## Limits

The parser knows grammar, not the English translation beside it. It cannot decide whether an evidential claim is warranted, whether an honorific tells the truth about a relationship, or whether a source sentence has been translated faithfully.

Some attachment remains ambiguous on the Phi surface. A clause-initial pronoun can head a possessive phrase when later structure forces that reading, while event nouns and quality nouns retain their verb or adjective spelling. Embedded questions no longer add another uncertain boundary: `pha` opens the complete question and `pho` returns the listener to the surrounding clause. The parser accepts any legal surface parse instead of inventing semantic valency. It can enforce `misa` against a visible preposition, complement frame, or Slot 1 stack, but a bare noun chain may admit more than one legal subject-object reading. A sentence whose intended object order depends only on the English translation still needs a human reading; the order advisories above collect the two commonest cases for that reading. The machine catches determinate modifier-first failures and leaves genuine lexical ambiguity visible.

## Corpus adoption

CI parses every structured lexicon example, the maintained teaching corpus, and the grammar regression suite. Literary texts and older evaluation material predate this parser, so the broader `--docs` scan remains an audit and migration tool until each remaining corpus area has been reviewed against the new tree. A clean default run means every dictionary sentence and every recognized example in canon, the references, manual, pamphlets, primer, book, Kia, and the Short Road parses. It does not yet say the same about every literary or evaluation line.

Each reviewed corpus area can move under the mandatory command after its rejected sentences have been separated into text defects and parser defects. The text changes only after the parser defects are repaired. That order matters: an old sentence does not become grammatical merely because satisfying a mistaken diagnostic would be convenient.
