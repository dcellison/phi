# Phi Solo Listening Audit

This protocol turns lexical-density concerns into reproducible maintainer observations. It does not substitute for other listeners and cannot establish universal ease. Its first purpose is to prevent intuition or spelling distance from triggering broad renames.

## Two complementary audits

The existing `documents/minimal_pairs_baseline.txt` records grandfathered character edit-distance-one pairs among content words. `scripts/audit_phonetic_neighbors.py` adds phoneme-unit edit distance, feature-weighted substitutions, function-word priority, and corpus attestations. Neither score predicts confusion by itself.

Productive proper-name forms are an open class and do not enter either lexical baseline. `ne` marks their grammatical role, while shared or similar personal names are handled through ordinary clarification. A bearer may still use this audit when choosing among acceptable forms, but an automated neighbor score cannot invalidate their name.

Generate the current ranked baseline:

```bash
python3 scripts/audit_phonetic_neighbors.py --output documents/phonetic_neighbors_baseline.txt
```

Check a proposed coin against the phonetic inventory as well as the validator's spelling check:

```bash
python3 scripts/validate_examples.py neighbors candidate
python3 scripts/audit_phonetic_neighbors.py --candidate candidate
```

Generate a reproducible set of ABX recording prompts:

```bash
python3 scripts/audit_phonetic_neighbors.py --kind function --prompts 40 --seed 202601
```

## Recording protocol

1. Record each prompt's A, B, and X items as separate files without looking at a previous take.
2. Use careful reference speech in one session and comfortable conversational speech in another.
3. Repeat on at least three nonconsecutive days and include one quiet and one moderate-background-noise condition.
4. Randomize playback names so the written word is not visible during identification.
5. Record the response, condition, confidence, and whether replay was needed.
6. Keep raw recordings private by default. Publish only deliberately selected examples with explicit consent from every recorded speaker.

## Observation table

| Date | Pair | Register | Condition | Trials | Errors | Replays | Notes |
|---|---|---|---|---:|---:|---:|---|

## Rename gate

A similarity score never renames a word. For a discretionary or collision-driven rename during solo development, record a candidate only when the same confusion recurs across three sessions, the pair is structurally or corpus-prominent, and the problem remains after careful-production review. Prefer changing the less established and less attested member. A separately accepted structural migration, such as D013's universal three-syllable ceiling, may authorize replacement for its recorded reason without manufacturing confusion evidence. Every replacement still must pass ordinary validation, character-neighbor checks, this phonetic audit, corpus-wide replacement, retirement of the old form, and a migration note.

Without independent listeners, even a repeated maintainer confusion remains limited evidence. Nonurgent renames should wait. The first outside feedback should prioritize function words, frequent content words, valid productive names, retired-form rejection, and high-degree neighborhoods.

## Claims this protocol does not license

This audit cannot show that Phi is easy, that an accent is acceptable to every listener, that a pair is safe in spontaneous conversation, or that a vocabulary-wide threshold predicts comprehension. Those questions stay in the development log's external-evidence backlog.
