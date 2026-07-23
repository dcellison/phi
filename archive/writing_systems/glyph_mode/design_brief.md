# Design brief

> **Archived:** This brief belonged to the native-glyph project retired on 23 July 2026. Its requirements and open questions are preserved as design history and do not describe planned Phi work.

## The job

The glyph mode will give Phi one native hand. It should be writable with an ordinary pen and satisfying with a broad quill, compact enough for running prose, and composed with some of the spatial presence of Maya glyph blocks. Its appearance may be new; the language inside it is not.

The working description is **featural alphasyllabary**. A reader sees a word block, follows its onset cells in a fixed order, and recovers every consonant and vowel. The system has no inherent vowel and omits no vowel. It therefore resembles a syllabary on the page while building its cells from smaller, reusable sound forms.

## Information model

```text
word block
  onset cell
    consonant core
    primary vowel
    optional hiatus vowel
  next onset cell
    consonant core
    primary vowel
    optional hiatus vowel
```

Every Phi word begins with a consonant. Every consonant is followed by a vowel, and no word permits three consecutive vowels. An onset cell can therefore hold `CV` or `CVV` without a carrier, a vowel suppressor, or an unwritten default. A word block must accommodate one through four onset cells because lexical words stop at three syllables while productive names may reach four.

The proposed block preserves spoken order. Every spoken word receives its own block, including function words and names, in the same sequence heard in speech. A block does not pull a particle away from that sequence or turn scope into an overhead arc. The period remains the only visible punctuation.

## Visual aim

The Maya influence belongs first to composition: roughly square groupings, a strong principal form with smaller companions, controlled asymmetry, and shapes that make use of the space between strokes. It does not require Maya logograms, calendar signs, deities, or copied ornamental details. Phi needs a related visual experience, not a costume made from another writing tradition.

Art Nouveau may inform the movement of the line through plantlike turns and changing tension, but semantic motifs do not belong inside the sound inventory. A glyph for `m` should remain `m` whether it appears in a word for soil, medicine, argument, or rain.

## Hand constraints

- The same skeleton must work with pencil, monoline pen, fountain pen, and broad quill.
- Stroke weight and nib angle may change the expression of a form but never its reading.
- Open counters and large internal spaces take priority over small enclosed details.
- A writer should not need color, shading, filled regions, or ruler-straight frames.
- Vowel forms must remain distinguishable when a block is written at ordinary note-taking size.
- A three-cell lexical word and a four-cell name must remain legible without expanding into a miniature illustration.
- The writing path should avoid needless retracing and should not require the writer to plan a sentence-wide enclosure before beginning the sentence.

These are design tests rather than a claim that the first sheet already passes them. Pen lifts, writing time, and minimum readable size will be measured only after a candidate hand exists.

## Featural possibilities

Consonant families may share gestures drawn from articulation. Stops can share closure, nasals can adapt that closure to an open channel, and related fricatives can use a common release or breath treatment. The resemblance must be obvious enough to help memory but substantial enough to survive hurried handwriting. A single tiny tick cannot carry the difference between two frequent sounds.

The five vowels need both shape and a habitual location. Position alone is compact but vulnerable to drift; shape alone can crowd the consonant. The studies therefore make the primary vowel a recognizable companion near the upper part of its consonant and repeat that shape below for a second vowel in hiatus.

The reserved breath stroke has no assigned function. It may become part of a consonant-family distinction, a visual path through a block, or nothing at all. It cannot mark two unrelated facts merely because the phrase sounds apt.

## Block questions

Two layout families are worth testing. A strict quadrat gives every word the same square advance and scales its cells to fit. An elastic block keeps cell size steadier and lets longer words grow modestly wider. The first gives a strong page texture; the second may be kinder to a quick hand. Both must keep one fixed internal reading order.

One-cell blocks should not tower over grammatical words merely because they have room. Four-cell blocks should not shrink their vowel forms past recognition. The useful answer may include a narrow range of approved proportions rather than one box imposed on every word.

## What is not being designed yet

The first stage does not design logograms, spelling alternatives, ligatures, or abbreviations. Numeral forms, font encoding, and keyboard input wait as well. Common words may acquire natural shorthand after a hand has been used enough to show where pressure actually falls. Designing those shortcuts before the ordinary script would make decoration responsible for evidence that only writing can supply.

## Review sequence

1. Choose the line qualities and block proportions worth taking to paper.
2. Establish unmistakable consonant and vowel forms in a complete inventory.
3. Write repeated word lists, names, particles, and short passages at several sizes.
4. Record collisions, awkward joins, excessive pen lifts, and forms that collapse under speed.
5. Revise the hand before specifying digital assembly or teaching it to a learner.

A proposal leaves the studio only when a person can write it without drawing each word as a picture and another reader can recover the Romanized Phi without help from the translation.
