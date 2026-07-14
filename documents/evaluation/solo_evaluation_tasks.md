# Solo Evaluation Tasks

These tasks let one maintainer gather disciplined observations without disguising self-review as learner research. They are reusable later with informal learners, but no score from the maintainer alone licenses a general learnability claim.

## 1. Structural regression

Run the standalone validator plus the productive-name unit tests. Then read every example added since the previous release and verify its free translation against the lexicon gloss line. Machine agreement establishes internal consistency only.

## 2. Expression and source-layer choice

Create twenty-four prompts divided evenly among canonical vocabulary, transparent composition, module vocabulary, productive Phi-form names, explicit translation, and separately presented source material. Shuffle them and classify them immediately or later without consulting the key, recording any prompt for which two choices remain defensible. Ambiguity in the task may reveal a documentation problem rather than a wrong answer.

Required prompt domains are personal names, place names, tradition-specific philosophy, source quotation, historical harmful terminology, exact time, medical quantity, scientific notation, URL or identifier, community practice, and a recurring semantic gap.

For the name prompts, include:

- Valid onyms with two, three, and four syllables
- A five-syllable proposal that the charter rejects
- A retired content form used as a name without its former meaning
- A current function word that cannot also be a name
- A former form absent from the current lexicon that follows the ordinary onym charter
- A multi-token source name
- A non-Latin source form
- Two people who share one onym
- A source name whose preferred adaptation is unknown

Repeat one chosen onym at least ten times in a short narrative and record its burden while keeping the source name separately available.

## 3. Function-word boundary recognition

Use `scripts/audit_phonetic_neighbors.py` to generate fixed-seed ABX prompts for dense function-word pairs. Follow `documents/evaluation/listening_audit.md`. Keep results separated by careful and conversational production.

## 4. Source-separation and rendering safety

Build the site with surrounding source examples containing mixed case, non-Latin script, punctuation, a URL, mathematical notation, and HTML-looking text. Confirm that none appears inside a Phi code block, that the Markdown renderer escapes it safely, and that Tengwar rendering is attempted only for complete Phi lines.

## 5. Open-reference philosophical paraphrase

Choose one unread Phi-only prompt whose answer key you have not seen. Paraphrase it immediately or later, consulting the grammar and lexicon if useful but keeping the proposition key closed until the interpretation is complete. Record the conditions of the reading, including references used, and distinguish vocabulary-learning friction from possible ambiguity in the language.

## 6. Argument transformation

For each corpus dialogue, change one premise while preserving the conclusion, then preserve the premises while changing the conclusion. Use the result as writing practice and as one source of ideas for clearer phrasing, teaching, compounds, or vocabulary; it is not an admission gate.

## 7. Conversation repair

Read both roles of one dialogue aloud without rehearsal. At each artificial misunderstanding, use only the conventions in `documents/grammar/philosophical_conversation.md`: pardon, clarify, non-knowledge, error, rephrase, understanding without agreement, turn handoff, wait, agreement, or refusal. Record which repair required English.

## Result record

| Date | Release | Task | Material | Result | Failure or ambiguity | Proposed follow-up |
|---|---|---|---|---|---|---|
| 2026-07-10 | 2026.1 candidate | structural regression | new external and philosophy documents | 937 entries; 0 errors; 0 warnings; 15 focused tests passed | no structural failure found | maintainer semantic review |
| 2026-07-10 | 2026.2 candidate | structural regression | productive name forms | 937 entries; 0 errors; 0 warnings; 12 name-form tests passed | no structural failure found | run repeated-name narrative task |
| 2026-07-10 | post-2026.2 main | argument transformation | Rain and the River; Grain for Hunger and Seed; Definition Under Pressure | six Phi-only prompts and a separate proposition key authored and structurally validated | no human interpretation recorded; the intended learner has not viewed the key | use any prompt immediately with the key closed and record whether references were used |
| pending | post-2026.2 main | open-reference paraphrase | philosophical transformation prompt packet | available immediately | no Phi-only paraphrase has been recorded | interpret one unread prompt without viewing the key, using the lexicon and grammar as needed |
| pending | post-frame-removal main | function-word boundary recognition | recorded ABX prompts | no recordings yet | maintainer audio unavailable in repository work | record in a separate session |

## External evidence boundary

If another person later uses these tasks, record their language background, consent, task conditions, and qualitative comments, but do not publish raw voice by default. Aggregate several participants before reporting percentages, and describe exactly what was measured rather than saying that Phi as a whole is easy or effective.
