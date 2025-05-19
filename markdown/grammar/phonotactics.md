# phonotactics

> phonotactics is the branch of linguistics that deals with the rules governing the allowed combinations of phonemes (basic units of sound) in a language. it defines the permissible arrangements of sounds within words, including constraints on which sounds can appear at the beginning, middle, or end of a syllable, and the sequences of sounds that are acceptable. phonotactic rules vary across languages and are essential for understanding the phonological structure and sound patterns of a language.

## groups

the following groups are used to fill in the form at the [awkwords](http://akana.conlang.org/tools/awkwords/) website in  order to generate sample words for a phi lexicon.

| group | pattern               |
| ----- | --------------------- |
| C     | `h/l/m/n/p/r/s/t/w`   |
| F     | `ph/wh/th/sh`         |
| V     | `i/u/e/o/a`           |
| P     | `[VV]^ii^uu^ee^oo^aa` |

## explanation of groups

**consonants (C):**
- single consonants: h, l, m, n, p, r, s, t, w

**fricative digraphs (F):**
- two-letter combinations: ph, wh, th, sh

**vowels (V):**
- single vowels: i, u, e, o, a

**vowel pairs (P):**
- any two vowels together, EXCEPT:
  - ii (no double i)
  - uu (no double u)
  - ee (no double e)
  - oo (no double o)
  - aa (no double a)

so valid vowel pairs would be combinations like:
- ia, io, iu, ie
- ua, ue, ui, uo
- ea, ei, eu, eo
- oa, oi, ou
- ae, ai, au, ao

## syllable structures

`(C)CV` or `V`

a syllable in phi is either `(C)CV` or `V`. if a syllable starts with two consonants, the pair will be a fricative digraph. a syllable always ends with a vowel. because there are no diphthongs in phi but there exist separately pronounced vowel pairs, `V` syllables are sometimes produced from the resulting vowel hiatus. this is the only alternative to the main syllable structure, and it only occurs directly after `(C)CV`. as well, there should be no duplicate syllables in the same word.

## word patterns

### long nouns

`[C/F][V/P][F][V/P]`

this pattern tends to produce soft words of two to four syllables. words can have a possible two fricatives, giving nouns an airy feel.

examples:

```
phoshiu ruwhai wowha poeshue nieshu mopho miupho woitho phawhu whuothu tuatheo
```

### short nouns

these patterns produce words of two syllables. they are also used for more common and specific nouns, such as colours. each of these nouns must use a fricative in one of the two positions.

`[C/F][V][C/F][V]`

examples:

```
miphi thathe phelu phowi nuse mawa nola phaphe whitho tuwhi phale whushu lipho
```

### verbs

`[C][V/P][C][V]`

this pattern produces words of two or three syllables. these words have no fricatives, reflecting that verbs are more utilitarian in phi.

examples:

```
miusu watu maoto heana loha naunu wemu moiha raro nima sana newi mala moewu
```