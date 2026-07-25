# The word proposal form

A specification for a browser form that lets someone outside the project propose a Phi word and delivers that proposal to the maintainer as a pull request. The form is not built. This document records what it would do, which parts of the word creation protocol a machine can carry, and which parts it cannot.

The lexicon grows slowly by policy, because the protocol asks for a compound before it allows a root. A proposal channel is unlikely to change that, and it is not meant to. The reason to build one is that every proposal, accepted or refused, records something a person wanted to say in Phi and could not. The project has no other instrument for that, and no speakers to supply it. Refused proposals carry the same information as accepted ones.

## Scope

The form accepts content words: nouns, verbs, and adjectives. It refuses everything else and says why.

Phi's grammar is closed. Particles, prepositions, conjunctions, complementizers, quantifiers, and the rest of the function inventory are settled, and modules may add vocabulary but never syntax. A form that quietly accepted a particle proposal would invite work that canon has already ruled out. The refusal belongs in the interface, at the point where a proposer chooses a part of speech, rather than in a rejection note weeks later.

Proper names are also out of scope. They follow the productive name form checklist and take no lexicon entry, so `scripts/test_name_forms.py` already covers them from the command line.

## What the proposer supplies, and what the form derives

Two fields are mechanically derivable from the spelling, and the form generates both rather than asking for them.

`ipa` and `syllables` follow from the written form with no exceptions. An algorithm that maps each onset to its phoneme, each vowel to its quality, splits the digraphs, and places stress on the penultimate syllable reproduces all 1,276 stored values exactly. Asking a proposer to write the IPA invites errors that look right, and the dental diacritics on `t` and `n` are the ones a newcomer will miss. The form shows both fields as read-only output, which also teaches the pronunciation while the person is still choosing the shape.

The filename is derived too. It comes from the gloss, lowercased, with spaces and parenthetical disambiguators turned into hyphens, so `right (normative)` becomes `right-normative.json` and `side effect` becomes `side-effect.json`.

Everything else is the proposer's work: `word`, `gloss`, `pos`, `description`, `articulatory_notes`, `examples`, `semantic_domains`, and the optional `search_terms`, `usage_notes`, `sound_symbolism`, `pillars`, and `modules`.

## Checks that run in the browser

The site already ships `lexicon.json` to the client for the explorer, so the whole lexicon with parts of speech is available in the page with no server and no new build step. Every check below runs while the proposer types, and each failure names the rule and the conflicting word.

Phonotactics first: onsets drawn from the ten consonants and four digraphs, vowels from the five, an onset on the first syllable, every syllable open, no sequence of three vowels, no repeated syllable that carries an onset, and a total of two or three syllables. One syllable is reserved for particles and base numerals, and four is above the lexical ceiling.

Then the collision check, which is the one that matters most. A candidate at edit distance 1 from an existing content word is rejected outright. A candidate at distance 1 from a function word is allowed only when position disambiguates, and the form requires `usage_notes` before it will accept one. This mirrors the ratchet in `documents/validation/minimal_pairs_baseline.txt`, which holds 760 grandfathered pairs and may only shrink, so a proposal that would add a new pair cannot be accepted at all.

Two smaller checks: the candidate must not already exist in the lexicon, and it must not appear in `documents/validation/retired_forms.txt`, whose eight short forms are barred from lexical reassignment.

The form also steers rather than only refusing. Because the two-syllable space is 61 percent closed by existing neighbors while the three-syllable space is 91 percent open, the interface should suggest three syllables by default and ask a proposer who wants two to say why the concept belongs to the daily round.

## Where a proposal lands

Proposals go to a `proposals/` directory as a single JSON file, not into `vocabulary/content/`.

This matters more than it looks. Two CI steps check that derived artifacts are in sync: the phonetic neighbor baseline is regenerated and diffed, and the generated Part VII reference is regenerated and compared. A proposer who adds a file under `vocabulary/content/` without running `generate_reference.py` and `audit_phonetic_neighbors.py` produces a pull request that fails CI for reasons unrelated to the quality of the word. That turns the strongest feature of the whole arrangement, a build that goes green or red before the maintainer looks, into noise.

A staging directory avoids it. The lexicon stays the maintainer's space, a proposal never touches a derived artifact, and the proposal file can carry fields that have no place in the lexicon schema. The envelope puts the candidate entry under one key and the proposal metadata under another.

Promotion is then a maintainer action: move the entry into `vocabulary/content/`, run the regeneration commands, delete the staged file, and record the decision. Nothing stays in `proposals/` after a decision, which satisfies the rule that every directory outside `archive/` holds current material.

## Delivery to GitHub

The site is static and has no server, so the form assembles the JSON and hands off through a prefilled file URL of the form `github.com/dcellison/phi/new/main?filename=proposals/<name>.json&value=<urlencoded>`. A visitor without write access is offered a fork, and GitHub opens the pull request. A complete entry runs about 2 KB encoded, well inside any URL limit.

This requires a GitHub account, which is a real filter on who can propose. Whether that filter is welcome is a maintainer decision. The alternative is a GitHub issue form plus an action that converts a filled issue into a branch, which reaches people who will not use a file editor and costs a workflow to maintain.

## What continuous integration settles

A proposal pull request needs its own workflow, triggered on changes under `proposals/`, running a `scripts/validate_proposal.py` that applies the lexicon checks to a staged file. The existing `validate.yml` runs the full corpus and would not see the file.

Green means the form is phonologically legal, collision free, schema complete, and that every cited example passes the validator, including the gloss line lint that renders each word by its exact lexicon gloss. That last check is a quiet test of competence. Writing an example that passes it requires knowing the grammar, not just the dictionary.

Red means the maintainer never has to open it.

## What no machine settles

Whether the concept deserves a root at all. This is the first step of the word creation protocol, it is pure judgment, and it is the step a stranger will skip, because coining is enjoyable and composing is work. The protocol's answer is usually a compound, and 112 of the register's decisions record exactly that outcome.

So the form carries one field the schema does not have, and it is required: which existing words the proposer tried to compose this from, and why the composition failed. The reasoning is already demanded by the protocol, the decision register already has a `compositional` status waiting for the answer, and requiring it in the form deters the proposals that would otherwise arrive in volume. When the honest answer is that a compound works, the field has written the rejection note.

Four other things stay human. Whether the word fits Phi's worldview and its peace linguistics boundaries. Whether it belongs to base vocabulary or to one or more modules. Whether the semantic family placement illuminates anything. And whether `articulatory_notes` is accurate rather than plausible, since nothing mechanical can tell the difference between a true account of the airflow and a fluent invention.

Expect to edit rather than only to judge. A proposal will arrive well formed and its prose will still need bringing to the register, because the voice is documented but not enforceable by test.

## Changes this would require elsewhere

`project/development_protocol.md` currently defers a public RFC process until recurring users make one useful. A proposal form is a light RFC process, so that sentence needs rewriting in the same change rather than being left to contradict the site.

The decision register gains a source. A refused proposal is still a noticed question, and the rule that no noticed gap disappears into conversation applies to a stranger's proposal exactly as it applies to one of the maintainer's own. Each refusal wants an identifier and a status.

## Non-goals

The form does not accept grammar proposals, does not vote, does not queue, and does not tell a proposer that a submission will be accepted. It produces one reviewable pull request per proposal and nothing else.

## Open questions for the maintainer

Whether requiring a GitHub account is the right filter or too high a bar.

Whether `proposals/` should hold refused proposals until their decision identifiers are recorded, or whether refusal closes the pull request and the register carries the whole memory.

Whether the form should offer a compound builder beside the coinage fields, so that the composition it asks about can be attempted in the same place rather than somewhere else.
