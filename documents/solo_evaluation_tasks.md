# Solo Evaluation Tasks

These tasks let one maintainer gather disciplined observations without disguising self-review as learner research. They are reusable later with informal learners, but no score from the maintainer alone licenses a general learnability claim.

## 1. Structural regression

Run the standalone validator and external-register unit tests. Then read every example added since the previous release and verify its free translation against the lexicon gloss line. Machine agreement establishes internal consistency only.

## 2. External-layer choice

Create twenty prompts divided evenly among core composition, registered compound, adapted guest, and exact external material. Shuffle them, wait at least one day, classify each without consulting the key, and record any prompt for which two layers remain defensible. Ambiguity in the task may reveal a documentation problem rather than a wrong answer.

Required prompt domains are personal names, place names, tradition-specific philosophy, source quotation, historical harmful terminology, exact time, medical quantity, scientific notation, URL or identifier, community practice, and a recurring semantic gap.

## 3. Boundary recognition

Use `scripts/audit_phonetic_neighbors.py` to generate fixed-seed ABX prompts for `hasha/hasho`, `patha/patho`, and other dense function-word pairs. Follow `documents/listening_audit.md`. Keep results separated by careful and conversational production.

## 4. Exact-payload safety

Build the site with payloads containing mixed case, non-Latin script, punctuation, a URL, mathematical notation, doubled `patho`, and HTML-looking text. Inspect generated source to confirm that payload is escaped, visually marked, excluded from the lexicon, and retained as source text in mixed Tengwar output.

## 5. Delayed philosophical paraphrase

Choose one section of `documents/philosophical_test_corpus.md`, hide its translation, and return after at least seven days. Paraphrase the Phi into plain English, then compare propositions, evidential status, modality, negation scope, participants, and discourse relations. Record lost and added distinctions separately.

## 6. Argument transformation

For each corpus dialogue, change one premise while preserving the conclusion, then preserve the premises while changing the conclusion. If the language makes those edits difficult to distinguish, add the failure to the capability matrix rather than immediately adding vocabulary.

## 7. Conversation repair

Read both roles of one dialogue aloud without rehearsal. At each artificial misunderstanding, use only the conventions in `documents/grammar/philosophical_conversation.md`: pardon, clarify, non-knowledge, error, rephrase, understanding without agreement, turn handoff, wait, agreement, or refusal. Record which repair required English.

## Result record

| Date | Release | Task | Material | Result | Failure or ambiguity | Proposed follow-up |
|---|---|---|---|---|---|---|
| 2026-07-10 | 2026.1 candidate | structural regression | new external and philosophy documents | 937 entries; 0 errors; 0 warnings; 15 focused tests passed | no structural failure found | maintainer semantic review |
| pending | 2026.1 candidate | delayed paraphrase | philosophical corpus | not yet eligible | seven-day delay not elapsed | perform later without viewing translations |
| pending | 2026.1 candidate | boundary recognition | recorded ABX prompts | no recordings yet | maintainer audio unavailable in repository work | record in a separate session |

## External evidence boundary

If another person later uses these tasks, record their language background, consent, task conditions, and qualitative comments, but do not publish raw voice by default. Aggregate several participants before reporting percentages, and describe exactly what was measured rather than saying that Phi as a whole is easy or effective.
