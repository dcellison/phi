# The word proposal form

A specification for a browser form that lets someone outside the project propose a Phi word and delivers that proposal to the maintainer for review. The form is not built, and the delivery path is not chosen. This document records what the form would do, which parts of the word creation protocol a machine can carry, which parts it cannot, and what each available delivery path costs.

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

## Validation does not depend on delivery

Everything above runs in the browser with no account, no server, and no third party. A person can take a candidate all the way to a finished, validated entry while completely anonymous, and the page can show them the assembled JSON at the end of it.

Only the last hop needs a channel. This separation is what makes the delivery question a free choice rather than an architectural one: the form can be built once, and the button at the end can be repointed later without touching any of the checking.

## Delivery paths

The maintainer's constraint is that requiring a GitHub account must not be the only way in. That rules out any single-path design built on the file editor, and leaves the paths below. More than one can ship at the same time, and the first three can ship together with no infrastructure at all.

| Path | Proposer needs | Project takes on | What arrives |
|---|---|---|---|
| A. Prefilled file URL | A GitHub account | Nothing | A pull request, opened by the proposer from their own fork |
| B. GitHub issue form | A GitHub account | One workflow | An issue, converted to a pull request by an action |
| C. Form to email | An email address | One third-party form endpoint | An email holding the JSON, converted locally |
| D. Copy box | Nothing | Nothing | Whatever the proposer sends, by whatever route they choose |
| E. Serverless function | Nothing | A worker, a bot token, a workflow | An issue, converted to a pull request on a label |

**A, the prefilled file URL.** The page assembles the JSON and links to `github.com/dcellison/phi/new/main?filename=<path>&value=<urlencoded>`. A visitor without write access is offered a fork, and GitHub opens the pull request. A complete entry runs about 2 KB encoded, well inside any URL limit. This costs nothing to build or run and cannot break, so it is worth keeping as one button regardless of what else ships. For a proposer who already has an account it remains the best path.

**B, the GitHub issue form.** A YAML issue template renders structured fields, and an action converts a filled issue into a branch. Still needs an account, but it reaches people who will not open a file editor, which is a much larger group than the account requirement alone suggests.

**C, form to email.** The page posts to a form-to-email service of the Formspree or Web3Forms kind, where the form identifier is public and no secret enters the repository. The maintainer receives the JSON by mail, and a small local script turns it into a branch, a commit, and a pull request through `gh` in one command. Check current free-tier submission limits before choosing a provider, since those move. At the volume this will realistically see, thirty seconds of the maintainer's own machine is a fair trade for owning no infrastructure.

**D, the copy box.** The finished JSON in a selectable block, with an address or a link beside it. This is the fallback that cannot fail, and it should exist whatever else is built, because it means the channel degrades instead of breaking when a third party changes its terms.

**E, the serverless function.** A Cloudflare Worker or equivalent, fronted by a bot-detection widget such as Turnstile, takes the POST and opens a GitHub issue under a bot identity with the JSON in the body. An action then converts that issue into a pull request when the maintainer applies a label. Two properties make the issue route better than having the worker open a pull request directly. The token needs `issues: write` rather than `contents: write`, so an abused endpoint produces noise that can be deleted in bulk instead of branches. And a pull request exists only for proposals the maintainer has already decided to take seriously, which keeps the pull request list meaningful.

A reasonable order is to ship A, C, and D together, which requires no hosting and no secret, and to add E only if proposal volume justifies it. Under that plan the upgrade repoints one button and changes nothing else.

## Where a proposal lands

This depends on the delivery path, and the difference is not cosmetic.

Two CI steps check that derived artifacts are in sync: the phonetic neighbor baseline is regenerated and diffed, and the generated Part VII reference is regenerated and compared. A file added under `vocabulary/content/` without running `generate_reference.py` and `audit_phonetic_neighbors.py` produces a pull request that fails CI for reasons unrelated to the quality of the word. That would turn the strongest feature of the whole arrangement, a build that goes green or red before the maintainer looks, into noise.

Under paths A, C, and D, the proposer or the local script cannot regenerate those artifacts, so proposals go to a `proposals/` directory as a single JSON file. The lexicon stays the maintainer's space, a proposal never touches a derived artifact, and the file can carry fields that have no place in the lexicon schema. The envelope puts the candidate entry under one key and the proposal metadata under another. Promotion is then a maintainer action: move the entry into `vocabulary/content/`, run the regeneration commands, delete the staged file, and record the decision.

Under paths B and E, the action creating the pull request runs inside the repository and can regenerate both artifacts itself. That allows the entry to go straight into `vocabulary/content/` with everything in sync, so CI reports on the word's merits alone and no staging directory is needed. The proposal metadata then belongs in the pull request body rather than in a file.

Whichever applies, nothing stays in `proposals/` after a decision, which satisfies the rule that every directory outside `archive/` holds current material.

## What continuous integration settles

If proposals land in `proposals/`, they need their own workflow, triggered on changes to that directory, running a `scripts/validate_proposal.py` that applies the lexicon checks to a staged file. The existing `validate.yml` runs the full corpus and would not see it. If proposals land in `vocabulary/content/` by way of an action, `validate.yml` already covers them and no new workflow is required.

Green means the form is phonologically legal, collision free, schema complete, and that every cited example passes the validator, including the gloss line lint that renders each word by its exact lexicon gloss. That last check is a quiet test of competence. Writing an example that passes it requires knowing the grammar, not just the dictionary.

Red means the maintainer never has to open it.

## What no machine settles

Whether the concept deserves a root at all. This is the first step of the word creation protocol, it is pure judgment, and it is the step a stranger will skip, because coining is enjoyable and composing is work. The protocol's answer is usually a compound, and 112 of the register's decisions record exactly that outcome.

So the form carries one field the schema does not have, and it is required: which existing words the proposer tried to compose this from, and why the composition failed. The reasoning is already demanded by the protocol, the decision register already has a `compositional` status waiting for the answer, and requiring it in the form deters the proposals that would otherwise arrive in volume. When the honest answer is that a compound works, the field has written the rejection note.

Four other things stay human. Whether the word fits Phi's worldview and its peace linguistics boundaries. Whether it belongs to base vocabulary or to one or more modules. Whether the semantic family placement illuminates anything. And whether `articulatory_notes` is accurate rather than plausible, since nothing mechanical can tell the difference between a true account of the airflow and a fluent invention.

Expect to edit rather than only to judge. A proposal will arrive well formed and its prose will still need bringing to the register, because the voice is documented but not enforceable by test.

## What the project spends

Three costs are worth choosing knowingly rather than discovering later.

The site currently makes no third-party calls. The only external links in the built pages point at github.com, so the whole thing runs on GitHub and nothing else. Paths C and E spend that property, and D and A do not.

Anonymity costs the follow-up. A GitHub account gives a persistent identity and a place to ask whether the proposer tried composing the idea first. An anonymous submission arrives as a blob with no way back, and an optional contact field recovers most of that. Whether a proposer is credited anywhere is a separate decision, and the repository rules currently say contributors are not singled out.

Spam scales with attention rather than with time. At no speakers the volume will be near zero, so the cheap paths are correct until the day they are not, and the staged order above exists so that day costs one button.

## Changes this would require elsewhere

`project/development_protocol.md` currently defers a public RFC process until recurring users make one useful. A proposal form is a light RFC process, so that sentence needs rewriting in the same change rather than being left to contradict the site.

The decision register gains a source. A refused proposal is still a noticed question, and the rule that no noticed gap disappears into conversation applies to a stranger's proposal exactly as it applies to one of the maintainer's own. Each refusal wants an identifier and a status.

## Non-goals

The form takes coinage proposals for content words and nothing else, and grammar proposals stop at the part-of-speech field. It holds no vote and keeps no queue, and it tells a proposer nothing about the likely outcome. One reviewable proposal arrives at a time.

## Open questions for the maintainer

Which delivery paths ship, and in what order.

Whether the no-third-party-calls property of the site is worth keeping, which decides between the email and serverless routes on one side and the copy box on the other.

Whether the form collects a contact address, and whether a proposer is named anywhere if a word is accepted.

Whether `proposals/` should hold refused proposals until their decision identifiers are recorded, or whether refusal closes the pull request and the register carries the whole memory.

Whether the form should offer a compound builder beside the coinage fields, so that the composition it asks about can be attempted in the same place rather than somewhere else.
