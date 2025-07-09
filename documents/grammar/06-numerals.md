# 6. Numerals

This document covers the complete system for expressing numerical concepts in Phi.

## 6.1. Cardinal Numbers
Phi uses a regular, base-10 positional system. Numbers are constructed by stating the digit followed by its magnitude, from highest to lowest. The component for the ones place is a digit by itself.

- **18:** `shu toa pho` (one ten eight)
- **42:** `shi toa wha` (four ten two)
- **101:** `shu nui shu` (one hundred one)

### 6.1.1. Implicit Zero Rule
Components representing zero magnitude (e.g., `phi nui` for "zero hundred") are omitted for brevity, unless all lower magnitudes are also zero.

- **2023:** `wha lae wha toa tho` (two thousand two ten three). The `phi nui` is omitted.
- **2003:** `wha lae tho` (two thousand three). `phi nui` and `phi toa` are omitted.
- **2000:** `wha lae` (two thousand).
- **40:** `shi toa phi` (four ten zero). The final `phi` must be stated.

## 6.2. Ordinal Numbers
Ordinal numbers ("first", "second", etc.) are formed by adding the postposition `noa` to a cardinal number. The resulting phrase functions as an adjective and precedes the noun it modifies.

- **The third friend:** `tho noa whelea`
- **The 18th story:** `shu toa pho noa thola`

## 6.3. Advanced Numerical Concepts
Phi handles concepts like frequency and fractions compositionally, by combining numbers with specific classifier nouns.

### 6.3.1. Frequency
Frequency (e.g., "once," "twice") is expressed by using a cardinal number followed by the noun `sheko` (instance/occurrence).

- **Once:** `shu sheko`
- **Twice:** `wha sheko`
- **Ten times:** `shu toa sheko`

### 6.3.2. Fractions
Phi uses a hybrid system for fractions, with unique nouns for common denominators and a logical genitive structure for all others.

**Common Fractions:**
Common fractions are formed by using a cardinal number with a "fraction-base" noun (e.g., `hapo` for a half-part, `shipo` for a quarter-part).

- **A half (1/2):** `shu hapo`
- **A third (1/3):** `shu thopi`
- **Three quarters (3/4):** `tho lo shipo`
- **Five eighths (5/8):** `phe lo phoso`

**Uncommon Fractions:**
Less common fractions are expressed using a genitive (possessive) structure with the generic noun `thepo` (part). The structure is `[Denominator Phrase] [Numerator Phrase]`, which translates to "[Numerator Part(s)] of [the Denominator's Parts]."

- **A seventh (1/7):** `[she lo thepo] shu thepo` (Of the seven parts, one part)
- **Two sevenths (2/7):** `[she lo thepo] wha lo thepo` (Of the seven parts, the two parts)

## 6.4. Noun Classifiers (Optional)
To add a layer of mindfulness and specificity when counting, Phi uses an optional system of noun classifiers. While not grammatically mandatory, using a classifier is considered more precise and respectful. The classifier, a noun itself, is placed between the number and the noun being counted.

**Structure:** `[Number] [Classifier] [Noun]`

### 6.4.1. Core Classifiers
Phi uses a minimal set of four core classifiers for broad categories:

- **`himo`**: For people.
- **`lipha`**: For other living things (plants, animals).
- **`themo`**: For inanimate objects.
- **`nophe`**: For abstract concepts (ideas, stories).

### 6.4.2. Examples
- **Standard Counting:**
  ```
  tho lo whelea
  three PL friend
  (three friends)
  ```
- **Counting with a Classifier:**
  ```
  tho himo whelea
  three person-classifier friend
  (three (esteemed) friends)
  ```
- **Other Examples:**
  - `shi lipha shiro` (four life-classifier tree -> four trees)
  - `wha themo pota` (two thing-classifier table -> two tables)
  - `shu nophe thola` (one concept-classifier story -> one story)

---
**Complete particle inventory:** See `grammar/particles.json`
**Complete conjunction inventory:** See `grammar/conjunctions.json` 