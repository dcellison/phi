# The digraph merger audit

Completed 26 July 2026, backing the canon ruling that no two Phi words may differ only by `wh` against `w`.

## The question

Phi's four digraphs each have a plain consonant a letter away: `ph` beside `p`, `th` beside `t`, `sh` beside `s`, `wh` beside `w`. A learner who fails the digraph produces the plain consonant, so any pair of words separated only by that difference is a pair the learner cannot keep apart. The maintainer raised the case of `whenola` against `wenola` and asked whether the language should tolerate it.

## Method

Every one of the 1,287 lexicon entries was read, and each word holding a digraph was rewritten with the plain consonant in its place, one occurrence at a time and all at once, in any position rather than only at the word's opening. Each rewritten form was looked up in the live lexicon. Corpus counts come from every validated Phi line in `texts/`, `manual/`, `pamphlets/`, `primer/`, `book/`, and `documents/`.

## Result

| Digraph | Words holding it | Live collisions |
|---|---|---|
| `ph` beside `p` | 143 | 8 |
| `th` beside `t` | 175 | 10 |
| `sh` beside `s` | 137 | 11 |
| `wh` beside `w` | 43 | 1 |

The distribution is the finding. Three digraphs carry twenty-nine collisions between them and nobody has ever complained; `wh` carries one, and it was the one the maintainer noticed. The reason is that the four contrasts are not equal. `/ɸ/` against `/p/` and `/θ/` against `/t/` each separate a fricative from a stop, which is about as robust as a consonant contrast gets. `/ʃ/` against `/s/` separates two sibilants at different places of articulation, distinguished in nearly every language that has both. `/ʍ/` against `/w/` separates a voiceless approximant from its voiced twin, and the majority of English speakers have merged the two outright. The wine-whine merger is the majority pronunciation across most of the English-speaking world, and the distinction survives mainly in Scotland, Ireland, and parts of the American South. For a merged speaker `wha` and `wa` are not a hard contrast. They are the same sound.

So the `wh` line is different in kind, not in degree. A pair separated by `/ʍ/` against `/w/` is one word with two spellings for most of the people who will ever read Phi, while the other twenty-nine pairs are ordinary neighbours that reward attention.

## The single `wh` collision

`whenola` (wander, verb) against `wenola` (collaborate, verb). Neither appeared in any validated corpus line. `wenola` carries a solarpunk pillar, sits in a family with `molawi` (cooperate) and `wephari` (coordinate), and is cited across the manual's exchange chapter, the Work, Craft, and Repair module guide, and two evaluation documents; `whenola` appeared only in generated reference files and two cross-referencing entries. `whenola` was therefore the cheaper side to move, and it became `nurima`, whose nasal, tap, and second nasal pass the voice along without a closure, which is what its retired form's sound note had claimed for the old shape. The vacated form joined `documents/validation/retired_forms.txt`, and the resolved line left `documents/validation/minimal_pairs_baseline.txt`.

## The pairs left standing

The `ph` beside `p` collisions.

| Digraph word | Gloss | Class | Corpus | Plain word | Gloss | Class | Corpus |
|---|---|---|---|---|---|---|---|
| `pha` | INT.COMP | complementizer | 12 | `pa` | INCH | particle | 37 |
| `phao` | parent | noun | 40 | `pao` | goodbye | interjection | 5 |
| `pheloma` | serve | verb | 3 | `peloma` | harmful | adjective | 17 |
| `phelui` | word | noun | 17 | `pelui` | cold | adjective | 13 |
| `philu` | candle | noun | 1 | `pilu` | take | verb | 39 |
| `phina` | FEW | quantifier | 18 | `pina` | sew | verb | 3 |
| `pho` | INT.COMP.CLOSE | complementizer | 12 | `po` | POT | particle | 197 |
| `phuro` | renew | verb | 0 | `puro` | strength | noun | 0 |

The `th` beside `t` collisions.

| Digraph word | Gloss | Class | Corpus | Plain word | Gloss | Class | Corpus |
|---|---|---|---|---|---|---|---|
| `tha` | DECL.COMP | complementizer | 195 | `ta` | one | numeral | 268 |
| `thei` | BETWEEN | preposition | 13 | `tei` | UNTIL | preposition | 10 |
| `theli` | EACH | quantifier | 1 | `teli` | bell | noun | 1 |
| `thelui` | sanctuary | noun | 0 | `telui` | rhythm | noun | 1 |
| `theo` | read | verb | 59 | `teo` | watch out | interjection | 3 |
| `theru` | thick | adjective | 11 | `teru` | process | verb | 1 |
| `tho` | DECL.COMP.CLOSE | complementizer | 195 | `to` | PST | particle | 1663 |
| `tholu` | space | noun | 25 | `tolu` | staff | noun | 1 |
| `thoru` | proud | adjective | 9 | `toru` | roof | noun | 4 |
| `thua` | fair | adjective | 5 | `tua` | no | interjection | 1 |

The `sh` beside `s` collisions.

| Digraph word | Gloss | Class | Corpus | Plain word | Gloss | Class | Corpus |
|---|---|---|---|---|---|---|---|
| `sha` | QUOT.COMP | complementizer | 191 | `sa` | HON.RESPECT | particle | 9 |
| `shai` | CONC | conjunction | 14 | `sai` | ouch | interjection | 1 |
| `sheloi` | MANY | quantifier | 67 | `seloi` | insightful | adjective | 0 |
| `shelu` | book | noun | 30 | `selu` | flow | verb | 7 |
| `shena` | calm | adjective | 9 | `sena` | pattern | noun | 2 |
| `sheru` | slow | adjective | 8 | `seru` | commit | verb | 2 |
| `shila` | winter | noun | 5 | `sila` | community | noun | 31 |
| `sho` | QUOT.COMP.CLOSE | complementizer | 191 | `so` | FUT | particle | 112 |
| `shorai` | commune | verb | 0 | `sorai` | insight | noun | 2 |
| `shorui` | weary | adjective | 3 | `sorui` | circle | noun | 10 |
| `shua` | come | verb | 112 | `sua` | who | interrogative | 12 |

## The three pairs worth the maintainer's attention

Three of the standing pairs deserve naming, because they sit in the same syntactic slot rather than merely in the same lexicon, and because the complementizer half of each arrived with the move to fricative monosyllables:

- `tho` (DECL.COMP.CLOSE) against `to` (PST), the most frequent particle in the corpus at 1,663 lines
- `sho` (QUOT.COMP.CLOSE) against `so` (FUT)
- `pho` (INT.COMP.CLOSE) against `po` (POT)

Each closer stands immediately before the main verb, which is exactly where those particles stand, so position does not separate them the way it separates most function words. The two often land side by side: the corpus holds 227 instances of `sho to`, 122 of `tho to`, 17 of `pho to`, and a handful of `tho po`, `tho so`, and `sho so`. What separates them is the onset alone.

Two of the three are fricative against stop, `/θ/` against `/t̪/` and `/ɸ/` against `/p/`, which is a much stronger cue than the voicing contrast this audit rules on. The third, `/ʃ/` against `/s/`, is sibilant against sibilant, and it is the weakest of the three only beside its neighbours rather than in absolute terms: sibilants are the loudest consonants Phi has, these two differ in place with a wide spectral separation, and no English dialect merges them. `sho to` is also the commonest of these sequences. The settled decision that minimal pairs are acceptable among function words, judged by ear and position, covers all three.

All three were kept. The maintainer judged the sibilant pair much easier to tell apart than the voicing pair this audit bars, and set a speaker's reported confusion as the only condition for reopening the question (D063).

## What the audit did not examine

Speakers who realize `/θ/` as `[t]`, `[f]`, or `[s]`, or `/ɸ/` as `[f]`, are a separate question from the one asked here: this audit measured each digraph against its own plain letter, not against every substitution a given accent might make.

That question is now closed, and the ruling is D064. Phi tells a speaker what a word should sound like and asks for care in the saying. It does not redesign its vocabulary to survive every substitution an accent makes. The `wh` bar is narrower than it looks: effort can close a difficult contrast, and closing it is the speaker's work, but nothing closes a contrast the speaker's phonology no longer holds. That is why `wh` against `w` is barred and `th` against `t` is not.

Hiberno-English, the case that prompted the ruling, shows how much room the language already leaves. Irish speakers who realize `th` as a stop commonly keep "thin" apart from "tin" by making the first dental and the second alveolar, and `documents/reference/phonetics.md` section 5.2 already lets Phi's dental `/t̪/` be alveolar `[t]`, since Phi holds no dental-alveolar contrast. The same strategy carries `theo` apart from `teo` in that accent, on place rather than manner.
