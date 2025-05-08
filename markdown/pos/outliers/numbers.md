---
tags:
  - pos
  - outlier
---
# numbers

> numbers are a feature of nouns, pronouns, adjectives and verb agreement that expresses count distinctions. used alone numbers are nouns. if we use them to describe nouns, as in one apple, two apples, three apples, etc., then the numbers are adjectives.

## phi usage

the phi number system prioritizes regularity and predictability over shortcuts found in many natural languages. it is built upon base words for digits 0-9 and specific words for powers of ten (ten, hundred, thousand, etc.).

### construction

numbers are constructed by stating the digit followed by its magnitude, proceeding from the highest magnitude to the lowest.
- **basic structure:** `digit magnitude digit magnitude ... digit`
- **no special words:** there are no unique words for numbers 11-19 (like "eleven" or "thirteen") or for multiples of ten (like "twenty" or "fifty"). these are formed regularly:
    - 18 is `lu toa wo` (one ten eight)
    - 40 is `pe toa no` (four ten zero)
    - 42 is `pe toa mi` (four ten two)

### implicit zero rule

to reduce verbosity without sacrificing regularity, components representing zero (`no <magnitude>`) are generally omitted.
- the component `no <magnitude>` is **only stated** if *all* lower magnitude components would also be zero.
- **examples:**
    - 2023: `mi lae mi toa ha` (two thousand two ten three). the "zero hundred" (`no nui`) is omitted because lower magnitudes (ten, one) are non-zero.
    - 2003: `mi lae ha` (two thousand three). the "zero hundred" (`no nui`) and "zero ten" (`no toa`) are omitted.
    - 2000: `mi lae` (two thousand). implies `no nui no toa no`.
    - 101: `lu nui lu` (one hundred one). the "zero ten" (`no toa`) is omitted.
    - 100: `lu nui` (one hundred). implies `no toa no`.
    - 40: `pe toa no` (four ten zero). the `no` for the ones place must be stated because there are no lower magnitudes to omit.

### ordinal numbers

phi does not use distinct ordinal words like "first", "second", "third". instead, it uses a descriptive phrase structure, conceptually similar to "number one", "number two", etc. the exact particle or structure for this is yet to be defined but might involve the word for number (`rewu`).

### characteristics summary

- digits 1-9 are single syllable (cv).
- magnitude words are two syllables (cv.v pattern).
- consistent `digit + magnitude` structure.
- implicit zero rule for conciseness.
- no irregular forms ("teens", "twenty", etc.).
- descriptive ordinal formation.

## definition

### digits

| phi | english | number |
| --- | ------- | ------ |
| no  | zero    | 0      |
| lu  | one     | 1      |
| mi  | two     | 2      |
| ha  | three   | 3      |
| pe  | four    | 4      |
| ra  | five    | 5      |
| se  | six     | 6      |
| ti  | seven   | 7      |
| wo  | eight   | 8      |
| mu  | nine    | 9      |

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

| phi       | literal       | english  |
| --------- | ------------- | -------- |
| lu toa wo | one ten eight | eighteen |

### 42

| phi       | literal      | english   |
| --------- | ------------ | --------- |
| pe toa mi | four ten two | forty-two |

### 2023

| phi              | literal                    | english             |
| ---------------- | -------------------------- | ------------------- |
| mi lae mi toa ha | two thousand two ten three | twenty twenty-three |

### 1024 - a kilobyte

| phi              | literal                   | english                  |
| ---------------- | ------------------------- | ------------------------ |
| lu lae mi toa pe | one thousand two ten four | one thousand twenty-four |

### 1,073,741,824 - a gibibyte

| phi                                                   | literal                                                                          | english                                                                                      |
| ----------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| lu woi ti toa ha mio ti nui pe toa lu lae wo nui mi toa pe | one billion seven ten three million seven hundred four ten one thousand eight hundred two ten four | one billion seventy-three million seven hundred forty-one thousand eight hundred twenty-four |
