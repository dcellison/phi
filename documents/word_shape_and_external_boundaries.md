# Word Shape and External Boundary Decisions

## Summary

Phi no longer needs four-syllable words or guest/exact boundary frames. The language has enough usable word space in one-, two-, and three-syllable forms, and vocabulary modules now provide a cleaner way to expand domain coverage without giving Phi an unlimited escape hatch.

The combined direction is simple: Phi should have a firmer edge. It can expand through curated vocabulary, transparent compounds, modules, and productive Phi-shaped names, but it does not need to absorb every outside string as if the string had become Phi.

## Decision 1: No Four-Syllable Phi Words

Every canonical Phi lexicon entry is limited to one, two, or three syllables. Module words receive no exception. Productive name-forms after `ne` are limited to two or three syllables. Multiword expressions may be longer in total, but every Phi token within them obeys the same lexical ceiling.

All existing four-syllable entries will be removed from current Phi rather than retained as aliases. The migration is divided into reviewable stages so each replacement can preserve meaning, sound symbolism, lexical relationships, and listening contrast. Staging controls implementation risk; it does not weaken the destination or indefinitely grandfather any form.

The capacity argument supports the rule. With the current phonotactic constraints, Phi has 376,740 legal three-syllable forms. After applying the practical close-neighbor gate for content coinage, plus exact duplicate blocking across the lexicon, about 355,428 three-syllable forms remain available. That excludes the remaining two-syllable space, which should stay premium territory for grammar, very basic vocabulary, and compact high-frequency forms.

The stronger reason is cognitive and aesthetic. Three syllables are enough for ordinary content words while keeping Phi compact, speakable, and easy to scan by ear. Four-syllable roots make the lexicon feel less disciplined, especially when compounds and modules can already carry heavier semantic work.

The productive-name charter follows the same ceiling. A bearer-approved Phi-form adaptation may have two or three syllables; a longer or otherwise non-Phi preferred name remains outside the Phi passage rather than receiving an exception.

## Decision 2: Remove Guest and Exact Frames

The external boundary pairs `hasha ... hasho` and `patha ... patho` are removed from Phi.

The exact frame is the clearest mismatch. `patha ... patho` preserves source material by suspending Phi interpretation, which means the payload is not really Phi. That becomes especially visible in alternate scripts. Tengwar can render the boundary words, but the payload may remain Latin text, mathematical notation, source-script names, URLs, legal identifiers, or punctuation-rich fragments. The result is not script parity; it is a mode break.

The guest frame is less severe but still awkward. It creates a third category of material: not core vocabulary, not a productive name, not a transparent compound, not a module term, and not fully external. It also adds validator rules, listening-audit burden, punctuation constraints, and teaching complexity for a feature whose main job can now be handled by clearer mechanisms.

Vocabulary modules change the tradeoff. Instead of saying that Phi can carry anything if properly framed, the cleaner model is:

- Core Phi says what it has been designed to say.
- Optional modules expand what Phi can say in a curated domain.
- Transparent compounds handle occasional composition.
- Productive `ne` names handle accepted Phi-shaped names.
- Source-exact, foreign, quoted, technical, legal, mathematical, or otherwise unassimilated material remains outside Phi and is handled by the surrounding medium.

This is not a loss of precision. It is a change in where precision lives. A medical dosage, legal clause, species name, URL, historical term, or source quotation can still be preserved in the document, interface, citation, or conversation. Phi can point to it, describe it, contextualize it, or translate its role, but it should not pretend that the source payload has become part of Phi.

## Replacement Behavior

For names, prefer `ne` plus a productive Phi-shaped onym when the bearer or naming community accepts the form. If the preferred form is not Phi-shaped, keep the source name outside the Phi run and use ordinary surrounding-language or typographic convention.

For technical terms, first ask whether an existing word, transparent compound, or module term expresses the needed role. If the concept recurs often enough and matters to Phi's purposes, add or extend a vocabulary module. If the source form itself matters, preserve it outside Phi.

For source-form exact values, identifiers, formulas, source quotations, legal wording, medical records, and source-script material, preserve the exact artifact in the surrounding medium rather than inside a Phi frame. An integer from 0 through 242 may also be rendered as an internal Phi numeral when that representation is adequate, but the source form remains outside whenever its notation, unit, identity, or fidelity matters. A Phi sentence may refer to and analyze the separately presented artifact.

For alternate scripts such as Tengwar, this avoids mixed-mode failure. A Phi passage in Tengwar remains Phi. Non-Phi source material appears as non-Phi source material, not as an opaque object smuggled through Phi boundary words.

## Implementation Implications

Remove `hasha`, `hasho`, `patha`, and `patho` from the lexicon and grammar references. Keep them on the retired-form denylist so neither the lexicon nor productive-name mechanism can reassign them.

Retire the external-register validator path, including guest payload validation, exact payload masking, closer escaping, and external-frame tests.

Update the manual, quick reference, module documents, examples, and development protocol wherever they instruct speakers to use guest or exact frames.

Revise the name-form documentation so it no longer presents guest or exact frames as the fallback for long, multi-token, or source-exact names.

Keep `shola ... sholo` conceptually separate. It quotes Phi speech as Phi speech; it is not an external-material container.

Add a word-shape gate to the coinage workflow: every lexicon proposal must fit the one-, two-, or three-syllable system, with three syllables as the normal maximum for content vocabulary. During the staged purge, only entries recorded in the finite migration ledger may remain longer; the final stage removes that temporary allowance.

## Procedural Check

Before coining a word, find a form of no more than three syllables that preserves the needed contrast. Use the normal close-neighbor gate, and try a transparent multiword expression or clearer semantic carve when one short root would hide too much. A longer lexical root is not an available fallback.

Before preserving outside material, ask: does Phi need to express the concept, or does the source form itself need to remain intact? If Phi needs the concept, use vocabulary. If the source form needs to remain intact, keep it outside Phi and let Phi refer to it honestly.

The check is not "can Phi contain this somehow?" The check is "should this become Phi, or should Phi acknowledge that it is looking at something external?" That distinction is the point of the change.
