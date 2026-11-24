# Working instructions for Claude (and other AI tools)

You are working on Phi, a constructed language and Daniel Ellison's long-term project. The development rules are project documentation, not tool configuration — read and follow them exactly:

@project/development_protocol.md

For the exact continuation state after pull request #418, including utility commands and the active vocabulary workflow, read:

@project/handoff/README.md

Authority order when documents disagree: `canon.md`. Settled decisions there are never reopened silently.

## Repository working rules

- All work happens on branches, opened as pull requests; the owner reviews and merges every PR himself. Never commit to main.
- Run `python3 scripts/validate_examples.py` and `python3 scripts/validate_sentences.py` as separate commands before any commit that touches vocabulary or documentation. Keep their exit codes visible; zero errors is the bar.
- After vocabulary changes, regenerate derived artifacts: `python3 scripts/generate_reference.py` and `python3 scripts/build_site.py`.
- After any change that touches Phi examples or citations anywhere in the corpus, regenerate the neighbor baseline with `python3 scripts/audit_phonetic_neighbors.py --output documents/validation/phonetic_neighbors_baseline.txt` and commit the file when it changes. Continuous integration diffs this baseline, and its attestation counts move whenever cited examples change, even when no word form does.
- The same changes can move the sentence-order ledger. Regenerate it with `python3 scripts/audit_sentence_order.py --output documents/validation/sentence_order_baseline.txt` and read every added line before committing: each is a sentence that parses but may have a manner word outside the Slot 1 block or an object before a prepositional phrase. Repair the ones that do; commit the ledger with the ones whose order is right.
- The same changes move the phrase-reading ledger, which records for each file how many sentences divide into phrases in more than one way, how many clauses leave a role open, and how often `shia` is contested. Regenerate it with `python3 scripts/audit_phrase_readings.py --output documents/validation/phrase_readings_baseline.txt` and commit it. The figures are measurements, not faults: a higher number in a row is something to notice, not something that blocks a commit.
- No AI attribution anywhere: no "Generated with" footers in PRs, no Co-Authored-By trailers in commits. Contributors are not singled out.
- Self-generated filenames are lowercase snake_case; `README.md`, `CLAUDE.md`, and license files are the only exceptions.
- Markdown paragraphs are single lines — never hard-wrap prose; renderers break on it.
- Every directory outside `archive/` holds only current, in-use material. When work completes, archive its records in the same PR, with a catalogue row in `archive/README.md`.
- Work only within this repository's directories.
