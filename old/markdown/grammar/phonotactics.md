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