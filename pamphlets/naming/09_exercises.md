# Part 9: Exercises

Answers follow at the end. Where an exercise asks for judgment, the key gives the reasoning, not just the mark: check your *why* against it.

## Part A: Word or someone

Translate each sentence; where a cast-word appears, say whether it is vocabulary or a person, and what decided it.

1. `keruko lopha mua womu nai.`
2. `ne moli wei mia loami to loa.`
3. `mia moli haolu.`
4. `ne keruko kau silawo to thalo.`
5. `thinoe mua muila nulae.`

## Part B: Build the address

Produce the Phi, aloud first.

6. Call your friend: no name needed.
7. Call sulae with the respect you owe a mentor.
8. Call moli with earned intimacy, the shorter way.
9. Introduce yourself with either a content-word name or a productive Phi-form name.
10. Ask a parent their child's name, politely.

## Part C: Choose the honorific

Say the address; if more than one is true, say which truth you would announce and why.

11. The teacher who has corrected your Phi for three years.
12. A healer you have never met, arriving to help.
13. Your oldest friend, weeping at your table.
14. A peer you respect and barely know.
15. The elder's elder, spoken of in a story.

## Part D: Repair

Each item is damaged. Fix it, or declare it sound.

16. `kona ne melu.`
17. `kona sa ne sulae.`
18. The gloss line `NAME seed smile.` under `ne thinoe seniku.`
19. Narration: *Sulae arrives with Siora.*
20. In a letter to a stranger: `siora kau silawo so shua.`

## Part E: Read the register

For each corpus line, say why `ne` is present or absent.

21. `ne sulae ha ma nai.`
22. `wa siora sulopa sola milura nuola.`
23. `ne siora pao.`
24. `mia ne sulae kua nai ma sano.`
25. `ne thinoe shola no wei muila thinoe loa. … sholo to haolu.`: account for both the announced `thinoe` and the bare one.

## Part F: Build a Phi-form name

Assemble a lowercase name of two, three, or four Phi syllables. Check its onset, open syllables, vowel sequence, and duplicate syllables; then run `python3 scripts/validate_examples.py name FORM` and say `mia nomei ne … nai.` It needs no dictionary meaning. The form should be yours or accepted by the person it represents, not assigned because someone else thinks its sound or meaning fits.

Then classify these candidates for direct use after `ne`:

26. `samira`
27. `sa`
28. `saweriko`
29. `sawerikona`
30. `mamama`
31. `amina`

---

## Answer key

**Part A.**

1. *The sturdy vessel is in the house.* Vocabulary: no announcement, and vessels are what sturdiness is for.
2. *moli gave me a gift.* A person: `ne` said so, and the gloss carries her as herself.
3. *I speak gently.* Vocabulary: manner, exactly as the sutta uses it.
4. *keruko walked to the village.* A person, announced; without `ne` the sentence would be about something sturdy walking, which is to say broken.
5. *The seed sleeps in the earth.* Vocabulary, and no ambiguity even in a household that loved a thinoe: careful text without `ne` has already told you no one is there.

**Part B.**

6. `kona melu.`
7. `kona ne sa sulae.`
8. `kona ni moli.` The honorific carries the announcement, and intimacy takes the shorter road.
9. `mia nomei ne … nai.` The blank may be a listed content word or a valid productive onym; only the former has a dictionary meaning.
10. `pi thia lopia nomei hina nai.` Politeness first of everything, the possessor chain before the name-word, `hina` standing where the answer will.

**Part C.**

11. `kona ne sa …` Respect earned and announced.
12. `kona ne le …` You know the role, not the person; announce the truth you have.
13. `kona ni …` `le` may also be true if the friend is a healer, but the night needs the friend, not the role; which truth you announce is itself information.
14. `kona ne …` Plain and correct. If it feels cold, the feeling is imported.
15. Plain `ne thinoe`, as the corpus story has it. The story reintroduces the referent clearly; `sa` would report a particular speaker's respect but is not required to make the memorial form grammatical.

**Part D.**

16. It depends on the intended atom. `kona melu.` calls someone by the role *friend*. `kona ne melu.` is correct if melu is actually the proper name being used.
17. `kona ne sa sulae.` Announce the name's coming, then the relationship, then the name.
18. `NAME thinoe smile.` Carried, not translated.
19. *sulae arrives with siora.* The names are Phi's; English is only hosting.
20. `ne siora kau silawo so shua.` Outside the family circle, the announcement is what makes the sentence portable; bare `siora` hands a stranger *joy* and a puzzle.

**Part E.**

21. Portable clarity or first mention: the referent is announced explicitly.
22. The household scene has already established siora; shared discourse licenses the omission.
23. The household chooses to reannounce at departure as part of its threshold style.
24. Neutral portable speech keeps `ne`; the reader cannot be assumed to share the local discourse state.
25. Outside the quotation, `ne thinoe` reintroduces a named person. Inside her own words, bare `thinoe` is *seed*, ordinary vocabulary. The contrast demonstrates the name marker without requiring a special grammar for memory or death.

**Part F.**

26. Valid: `sa.mi.ra`, three distinct open syllables.
27. Invalid as a productive onym: one syllable, and `sa` is a reserved honorific.
28. Valid: `sa.we.ri.ko`, four distinct open syllables. The lexical ceiling does not apply to a productive name.
29. Invalid as a productive onym: `sa.we.ri.ko.na` has five syllables.
30. Invalid as a productive onym: it duplicates `ma`.
31. Invalid as a Phi-form onym because it begins with a vowel. The source form may remain outside Phi, or its bearer may accept an adaptation such as `ne hamina`.
