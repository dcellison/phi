---
tags:
  - pos
  - outlier
---
# numbers

> numbers are a feature of nouns, pronouns, adjectives and verb agreement that expresses count distinctions. used alone numbers are nouns. if we use them to describe nouns, as in one apple, two apples, three apples, etc., then the numbers are adjectives.

## phi usage

The phi number system prioritizes regularity and predictability. It is built upon base words for digits 0-9, and specific words for powers of ten (ten, hundred, thousand, etc.).

### construction

Numbers are constructed by stating the digit followed by its magnitude, proceeding from the highest magnitude to the lowest.
- **basic structure:** `digit magnitude digit magnitude ... digit`
- **no special words:** there are no unique words for numbers 11-19 or for multiples of ten. these are formed regularly:
    - 18 is `phi toa who` (one ten eight)
    - 40 is `pho toa sha` (four ten zero)
    - 42 is `pho toa whu` (four ten two)

### implicit zero rule

To reduce verbosity without sacrificing regularity, components representing zero (`sha <magnitude>`) are generally omitted.
- the component `sha <magnitude>` is **only stated** if *all* lower magnitude components would also be zero.
- **examples:**
    - 2023: `whu lae whu toa the` (two thousand two ten three). the "zero hundred" (`sha nui`) is omitted.
    - 2003: `whu lae the` (two thousand three). the "zero hundred" (`sha nui`) and "zero ten" (`sha toa`) are omitted.
    - 2000: `whu lae` (two thousand). implies `sha nui sha toa sha`.
    - 101: `phi nui phi` (one hundred one). the "zero ten" (`sha toa`) is omitted.
    - 100: `phi nui` (one hundred). implies `sha toa sha`.
    - 40: `pho toa sha` (four ten zero). the `sha` for the ones place must be stated.

### ordinal numbers

phi does not use distinct ordinal words like "first", "second", "third". instead, it uses a descriptive phrase structure, conceptually similar to "number one", "number two", etc. the exact particle or structure for this has yet to be defined but might involve the word for number.

### characteristics summary

- digits 0-9 are single syllable, following a `[F][V]` pattern.
- magnitude words are two syllables following a `[C][P]` pattern.
- consistent `digit + magnitude` structure.
- implicit zero rule for conciseness.
- no irregular forms ("teens", "twenty", etc.).
- descriptive ordinal formation.

## definition

### digits

| phi | english | number |
| --- | ------- | ------ |
| sha | zero    | 0      |
| phi | one     | 1      |
| whu | two     | 2      |
| the | three   | 3      |
| pho | four    | 4      |
| wha | five    | 5      |
| thi | six     | 6      |
| shu | seven   | 7      |
| who | eight   | 8      |
| pha | nine    | 9      |

### orders of magnitude

| phi | english     | number                                                | power |
| --- | ----------- | ----------------------------------------------------- | ----- |
| toa | ten         | 10                                                    | 10^1  |
| nui | hundred     | 100                                                   | 10^2  |
| lae | thousand    | 1,000                                                 | 10^3  |
| mio | million     | 1,000,000                                             | 10^6  |
| woi | billion     | 1,000,000,000                                         | 10^9  |
| heu | trillion    | 1,000,000,000,000                                     | 10^12 |
| sae | quadrillion | 1,000,000,000,000,000                                 | 10^15 |
| ruo | quintillion | 1,000,000,000,000,000,000                             | 10^18 |
| pei | sextillion  | 1,000,000,000,000,000,000,000                         | 10^21 |
| wea | septillion  | 1,000,000,000,000,000,000,000,000                     | 10^24 |
| poa | octillion   | 1,000,000,000,000,000,000,000,000,000                 | 10^27 |
| hua | nonillion   | 1,000,000,000,000,000,000,000,000,000,000             | 10^30 |
| tio | decillion   | 1,000,000,000,000,000,000,000,000,000,000,000         | 10^33 |
| nia | undecillion | 1,000,000,000,000,000,000,000,000,000,000,000,000     | 10^36 |
| rei | duodecillion| 1,000,000,000,000,000,000,000,000,000,000,000,000,000 | 10^39 |

## examples

below are some examples that demonstrate how numbers would be said and written in phi. phi uses implicit zero (omitting zero magnitudes unless needed) to improve conciseness.

### 18

| phi         | literal       | english  |
| ----------- | ------------- | -------- |
| phi toa who | one ten eight | eighteen |

### 42

| phi         | literal      | english   |
| ----------- | ------------ | --------- |
| pho toa whu | four ten two | forty-two |

### 2023

| phi                 | literal                    | english             |
| ------------------- | -------------------------- | ------------------- |
| whu lae whu toa the | two thousand two ten three | twenty twenty-three |

### 1024 - a kilobyte

| phi                 | literal                   | english                  |
| ------------------- | ------------------------- | ------------------------ |
| phi lae whu toa pho | one thousand two ten four | one thousand twenty-four |

### 1,073,741,824 - a gibibyte

| phi                                                                | literal                                                                          | english                                                                                      |
| ------------------------------------------------------------------ | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| phi woi thi toa the mio thi nui pho toa phi lae wha nui mi toa pho | one billion seven ten three million seven hundred four ten one thousand eight hundred two ten four | one billion seventy-three million seven hundred forty-one thousand eight hundred twenty-four |
