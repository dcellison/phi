# Phi Language: Core Phonological Rules

This document outlines the complete and formal phonological system for the Phi language. It serves as the single source of truth for all sound-related and structural rules.

These word-form rules govern every Phi lexical token and productive name-form. Canonical lexicon words have at most three syllables, with no exception; productive names have two, three, or four. A legal four-syllable name needs no lexical-retirement or migration check because four-syllable forms cannot enter the vocabulary. Unassimilated source material remains outside Phi and is not governed by this document.

## 1. Core Phonetic Inventories

### 1.1. `C` (Single Consonants)
A closed set of **10** single characters.

- `h, k, l, m, n, p, r, s, t, w`

### 1.2. `F` (Fricative Digraphs)
A closed set of **4** two-character units that are phonologically distinct from `C`. These function as single consonantal onsets.

- `ph, th, sh, wh`

### 1.3. `V` (Single Vowels)
A closed set of **5** single characters.

- `a, e, i, o, u`

### 1.4. `P` (Vowel Pairs)
A Vowel Pair consists of two adjacent, distinct vowels. There are **20** possible combinations.

- **From `i`**: `ia, ie, io, iu`
- **From `u`**: `ua, ue, ui, uo`
- **From `e`**: `ea, ei, eu, eo`
- **From `o`**: `oa, oi, ou, oe`
- **From `a`**: `ae, ai, au, ao`

**Fundamental Property:** All Vowel Pairs are pronounced in hiatus, meaning each vowel forms a separate syllable. For example, `au` is pronounced /a.u/.

## 2. Syllable Structure

### 2.1. The Unified Syllable Onset Rule: `(C)CV`
This single rule defines **all** possible syllable onsets in the language.

- **Case 1: The onset is a Single Consonant `C`**
  - The optional `(C)` is **not used**.
  - The single consonant (e.g., `m`, `k`, `l`) fulfills the mandatory `C` slot.
  - *Example:* `ma`, `ke`, `la`. (Structure: `CV`)

- **Case 2: The onset is a Fricative Digraph `F`**
  - The optional `(C)` is **used** and represents the **first character** of the digraph (e.g., `p` in `ph`).
  - The mandatory `C` represents the **second character** of the digraph (e.g., `h` in `ph`).
  - This is the **only** time the optional `(C)` is ever used.
  - *Example:* `ha`, `ko`, `tho`. (Structure: `(C)CV`)

### 2.2. The Syllable Nucleus: `V` or `P`
The nucleus of a syllable (the part that follows the onset) can be either a Single Vowel (`V`) or a Vowel Pair (`P`).

- **Full Syllable Structure:** `(C)C` + (`V` or `P`)

### 2.3. Universal Syllable Constraints
- **Consonant Onset Rule:**
  - The **initial syllable** of any word must begin with a Consonant (`C`) or Fricative (`F`).
  - **Subsequent syllables** must also begin with a `C` or `F`, with one exception: a lone vowel (`V`) resulting from vowel hiatus (e.g., the `u` in `hauno` /ha.u.no/) does not require an onset.
- **Open Syllables Only:** Every syllable must end with a vowel.
- **No Consonant Clusters:** The only multi-letter onsets are Fricative Digraphs (`F`), which are treated as a single unit under the `(C)CV` rule.

## 3. Vowel System Constraints

### 3.1. The Vowel Hiatus Rule
As stated in 1.4, all Vowel Pairs (`P`) are pronounced in hiatus. This means there is a clear syllable break between the two vowels.

### 3.2. The Three-Vowel Constraint
- **Strictly Forbidden:** A sequence of three or more consecutive vowels is not permitted anywhere in any word.
- **Formal Definition:** The sequences `VP` (a Vowel followed by a Pair) and `PV` (a Pair followed by a Vowel) are forbidden.

| Allowed Structure | Example | Forbidden Structure | Example (Invalid) |
| :--- | :--- | :--- | :--- |
| `CP` | `nau` (/na.u/) | `CVP` | `maou` (`a` + `ou`) |
| `CVC` + `P` | `nelau` (/ne.la.u/) | `CPV` | `naui` (`au` + `i`) |


## 4. Word-Level Constraints

### 4.1. No Duplicate Syllables in Lexicon Words
A lexicon word cannot contain the same syllable twice. Source material outside Phi is not a Phi word and therefore creates no lexical exception.
- **Allowed:** `kala`
- **Forbidden:** `kaka` 

### 4.2. Structural Hierarchy
- **Single Syllable Forms (`CV` only):** Reserved for particles and base numerals (mu, ta, wi). Particles use CV structure exclusively (no fricative digraphs) for instant recognition and disambiguation.
- **Two-Syllable Forms (`CV.V` or `FV.V`):** Used for pronouns (mia, thia, shia), prepositions (mua, thue, wei), and scale units (shao, phoi)
- **Multi-Syllable Forms:** Used for content words (nouns, verbs, descriptors)

## 5. IPA Notation Standards

### 5.1. Standard Correspondences

**Consonants:**
- `h` = /h/, `k` = /k/, `l` = /l/, `m` = /m/, `n` = /n̪/ (dental)
- `p` = /p/, `r` = /r/, `s` = /s/, `t` = /t̪/ (dental), `w` = /w/

**Fricative Digraphs:**
- `ph` = /ɸ/, `th` = /θ/, `sh` = /ʃ/, `wh` = /ʍ/

**Vowels:**
- `a` = /ä/ (open central), `e` = /e̞/ (true-mid), `i` = /i/
- `o` = /o̞/ (true-mid), `u` = /u/

### 5.2. Syllable Boundaries
All vowel pairs show explicit syllable boundaries: `au` = /ä.u/, `oi` = /o̞.i/

### 5.3. Stress Rules
Phi uses **penultimate stress**: primary stress falls on the second-to-last syllable.

| Word | Syllables | Stress Position | IPA |
|------|-----------|-----------------|-----|
| `mia` | mi-a | first (penultimate) | /ˈmi.ä/ |
| `haolu` | ha-o-lu | second (penultimate) | /hä.ˈo̞.lu/ |
| `mioru` | mi-o-ru | second (penultimate) | /mi.ˈo̞.ru/ |
| `mu` | mu | only syllable | /ˈmu/ |

**Single-syllable words** receive stress on their only syllable.

---
**Related Documentation:**
- Grammar rules: See `reference_grammar.md`
- Language philosophy: See `language_guide.md`
