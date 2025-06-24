# Phi S-Expression Schema

This document outlines the LISP-like s-expression schema for representing the grammatical and semantic structure of the Phi language.

## Guiding Principles

1.  **Reflect SOV Order**: The core clause structure is `(Verb Subject Object)`.
2.  **Particles as Wrappers/Operators**: Particles generally wrap the s-expression of the element they modify.
3.  **Head-Final for Pre-Nominal Modifiers**: For noun phrases, modifiers precede the noun. In s-expressions, the noun is the head, and modifiers are attributes or preceding elements.
4.  **Lexical Items as Atoms**: Phi words are atomic symbols (e.g., `thewo`, `mia`).
5.  **Clarity and Readability**: S-expressions aim for clarity.
6.  **Consistency**: Similar grammatical structures have consistent representations.

## 1. Core Clause Structure (SOV)

A simple clause `Subject Object Verb` (e.g., `mia whethea shose` - I book see) maps to:
`(Verb Subject Object)`
Example: `(shose mia whethea)`

## 2. Particles

Particles typically act as operators.

### 2.1. Sentence/Clause Level Particles
(Tense, Aspect, Mood, Evidentiality, Negation, Question)
Format: `(Particle Clause_S_Expression)`
Examples:
*   `li mia whethea shose` (PST I book see): `(li (shose mia whethea))`
*   `su ra mia whethea shose` (FUT NEC I book see): `(su (ra (shose mia whethea)))`
*   `me mia whethea shose` (NEG I book see): `(me (shose mia whethea))`
*   `wa mia whethea shose` (Q I book see): `(wa (shose mia whethea))`
*   `hi mia whethea shose` (DIR.EVID I book see): `(hi (shose mia whethea))`

### 2.2. Noun-Modifying Particles
(Plural `lo`, Dual `tu`, Paucal `pu`)
Format: `(Particle Noun_Phrase_S_Expression)`
Examples:
*   `lo whethea` (PL book): `(lo whethea)`
*   `lo phiato whethea` (PL this book): `(lo (whethea :det phiato))`

### 2.3. Constituent-Marking Particles (Optional)
(`si` subject, `na` object, `te` verb)
Represented as optional keyword attributes on the relevant part of the main clause.
Example: `si mia na whethea te shose`
S-expr: `(shose mia whethea :s-marker si :o-marker na :v-marker te)`
If not present, these attributes are omitted.

### 2.4. Discourse/Pragmatic Particles
(`ha` topic, `mi` contrast, `ma` emphasis, `nu` focus, `ho` topic shift, `po` attention)

*   **`ma` (emphasis):**
    *   Clause emphasis: `(ma (shose mia whethea))`
    *   Constituent emphasis: `ma tushe noshea` (EMPH good food) -> `(noshea :adj ((ma tushe)))`
*   **`nu` (focus):** Attaches to the focused constituent.
    *   `nu mia whethea shose` (FOC I book see): `(shose (nu mia) whethea)`
    *   `mia nu whethea shose` (I FOC book see): `(shose mia (nu whethea))`
*   **`ha` (topic):** `mia ha whethea shose` (I TOP book see)
    S-expr: `(ha mia (shose mia whethea))` (the first `mia` is topic-marked; the second is its grammatical role)
*   **`ho` (topic shift), `po` (attention):** Wrap the clause they modify.
    *   `(ho (new_clause_s_expr))`
    *   `(po (clause_s_expr))`

## 3. Noun Phrases (NPs)

Phi NP structure: `(Opt. Particles) (Opt. Determiner) (Opt. Number) (Adj*) Noun (Opt. Post-Nominal-PPs*)`
S-expression format: `(Noun_Root :det Determiner :num Number_Atom_Or_List :adj (Adj1 Adj2 ...) :pp (PP_S_Expr1 ...))`
Number-marking particles like `lo` wrap the NP s-expression (see 2.2).

Examples:
*   `whethea` (book): `(whethea)`
*   `tushe whethea` (good book): `(whethea :adj (tushe))`
*   `phiato tushe whethea` (this good book): `(whethea :det phiato :adj (tushe))`
*   `shoata the tushe riphe whethea` (all three good important book):
    `(whethea :det shoata :num the :adj (tushe riphe))`

## 4. Numbers

*   Digits (e.g., `phi`) and Magnitudes (e.g., `phitha`) are atoms.
*   Combined numbers, e.g., `phi shupho whu phitha the` (123), are represented as a list in the `:num` attribute:
    `(Noun :num (phi shupho whu phitha the))`

## 5. Pronouns

Represented as atoms: `mia`, `thi`, `sha`, `lua`, `nua`.
These fill Subject or Object slots or are complements of prepositions.
Pluralized pronouns: `(lo mia)` (we).

## 6. Adjectives

Represented as atoms. In NPs, they appear in a list under the `:adj` attribute.
If modified by an adverb (e.g., `ritune tushe` - very good):
`(Noun :adj ((ritune tushe)))`

## 7. Adverbs

*   **Modifying a Verb:** Adverbs serially wrap the clause/verb phrase.
    `Adv1 Adv2 (Verb Subject Object)` -> `(Adv1 (Adv2 (Verb Subject Object)))`
    Example: `mia ritune wanume napine whera` (I very well quickly learn)
    S-expr: `(ritune (wanume (napine (whera mia))))`
*   **Modifying an Adjective:** `(Adv Adj)` e.g., `(ritune tushe)`.
*   **Modifying another Adverb:** `(Adv1 Adv2)` e.g., `(ritune wanume)`.

## 8. Prepositional Phrases

All `[F][P]` relational words are prepositions and precede their complement.
Format: `(Preposition Complement_NP_S_Expression)`
Examples:
*   `wheo liphai` (at tree): `(wheo liphai)`
*   `phia hiwhea` (in house): `(phia hiwhea)`

Used as an argument/adjunct to a verb:
*   `mophui phia hiwhea phera` (ball in house be): `(phera mophui (phia hiwhea))`

Used as a post-nominal modifier within an NP:
*   `whethea thia phuawhai` (book behind stone): `(whethea :pp (thia phuawhai))`

Possession with `thue` (of):
*   `whethea thue mia` (book of I -> my book) as a phrase: `(thue whethea mia)`
*   If object: `(shose thi (thue whethea mia))` (You see my book)

## 9. Conjunctions

Format: `(Conjunction Arg1_S_Expr Arg2_S_Expr ...)`

*   **Coordinating** (`nene` and, `wiho` or, `tupo` but):
    *   Objects: `(thewo mia (nene noshea wheishea))` (I prepare food and water)
    *   Clauses: `(nene (sharo mia) (phite thi))` (I go and you stay)
*   **Subordinating** (`wane` when, `matu` after, `wetu` if, `renu` because, `tela` that):
    *   `(wane (sharo mia) (thewo sha))` (When I go, s/he prepares)
    *   `(whemo mia (tela (whera sha)))` (I think that s/he learns)
*   **Correlative** (`toha...sipa` both...and):
    *   `toha X sipa Y` -> `(both-and X Y)` (uses a compound operator name)
    *   `toha noshea sipa wheishea riphe`: `(riphe (both-and noshea wheishea))`

## 10. Interjections

Format: `(Interjection Clause_S_Expression)` or `(Interjection)` if standalone.
Examples:
*   `mimia me mipho phera`: `(mimia (me (phera <Subject> mipho)))`
*   `wowou`: `(wowou)`

## Summary of S-expression Functional Heads (Operators)

This is not exhaustive but covers primary types:
*   Verbs (e.g., `shose`, `whera`)
*   Particles (e.g., `li`, `su`, `ra`, `me`, `wa`, `lo`, `ma`, `nu`, `hi`, `po`, `ho`)
*   Conjunctions (e.g., `nene`, `wiho`, `wane`, `wetu`, `tela`, `both-and`)
*   Prepositions (e.g., `phia`, `thue`, `wheo`)
*   Adverbs (when modifying clauses or other adverbs/adjectives directly, e.g. `ritune`, `napine`)
*   Interjections (e.g., `mimia`, `wowou`)

## Summary of Attributes (Keywords for NPs)

*   `:det` (Determiner)
*   `:num` (Number - value is an atom or a list of number atoms)
*   `:adj` (Adjective(s) - value is a list of adjective atoms or modified adjective s-expressions)
*   `:pp` (Post-nominal Prepositional Phrase(s) - value is a list of PP s-expressions)
*   Optional markers (on verb clause): `:s-marker`, `:o-marker`, `:v-marker`

## Future Considerations

*   Refining representation for complex adverbial interactions.
*   Detailed mapping rules for less common particle combinations.
*   Handling of anaphora and discourse-level phenomena (likely a layer above this sentence-level schema). 