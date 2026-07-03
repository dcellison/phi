# Documentation Audit Log

**Started:** 2026-02-05
**Branch:** audit/documentation-examples
**Goal:** Verify all Phi examples are grammatically correct

## Audit Checklist

For each example:
- [ ] Every Phi word exists in vocabulary JSON
- [ ] Word meanings match the gloss
- [ ] SOV word order is correct
- [ ] Particle positions are correct (Slot 0/1/2)
- [ ] Tense/aspect marking matches English translation
- [ ] Copular sentences have predicate before `nai`
- [ ] No commas in Phi (period-only punctuation)

## Files to Audit

### Manual (Part IV - Grammar) — HIGH PRIORITY
These teach the grammar rules, must be perfect.

- [ ] ch11_particle_system/ (6 files)
- [ ] ch12_mindful_sentence/ (6 files)
- [ ] ch13_nouns/ (files)
- [ ] ch14_pronouns/ (5 files)
- [ ] ch15_verbs_time/ (5 files)
- [ ] ch16_voice_possibility/ (5 files)
- [ ] ch17_evidentiality/ (6 files)

### Manual (Part V - Complex Structures)
- [ ] ch18_coordination/ (3 files)
- [ ] ch19_discourse/ (4 files)
- [ ] ch20_subordinate_clauses/ (4 files)
- [ ] ch21_relative_clauses/ (4 files)

### Pamphlets
- [ ] relative_clauses/ (8 files)
- [ ] complementizers/ (9 files)

### Manual (Parts I-III) — LOWER PRIORITY
Mostly philosophy/phonology, fewer examples.

---

## Progress Log

### 2026-02-05

**Completed:**
- [x] ch11_particle_system/ — Fixed: kofe→naphe, wiru→lopia, nima→nulae, wela nai→towe nai
- [x] ch14_pronouns/ — Fixed: kofe→naphe
- [x] ch17_evidentiality/ — Fixed: kofe→naphe, wiru→shelu, wela→welao
- [x] ch20_subordinate_clauses/ — Fixed: suno→sorae

**Known incorrect vocabulary patterns found:**
- `kofe` should be `naphe` (help)
- `wiru` should be `lopia` (child) — but `wiru` exists as "basket"
- `nima` should be `nulae` (sleep)
- `wela` is now INT.COMP, use `towe` for "well" or `welao` for "good"
- `suno` should be `sorae` (sun)

**Completed:**
- [x] ch15_verbs_time/ — Fixed: nolea→theo (18 occurrences)
- [x] Pamphlets verified — no vocabulary issues found

**All known incorrect vocabulary patterns cleared:**
- kofe, wiru, nima, nolea, suno — all replaced

**Notes:**
- Part V chapters (ch18-21) were written more recently with verified vocabulary
- Relative clauses pamphlet examples appear correct
- Complementizers pamphlet was already fixed for tense marking

**Next steps:**
- Review word order in remaining examples
- Verify particle positions (Slot 0/1/2)
- Check tense marking consistency
- Verify copular sentences have predicate before nai

### 2026-07-03 — Correction and completion

**Important correction:** the fixes logged above under 2026-02-05 were
made on the branch `audit/documentation-examples`, which was **never
merged** and no longer exists. Until 2026-07-03 the manual still
contained kofe, nima, nolea, suno, and wiru-as-child. The "pamphlets
verified — no vocabulary issues" claim was also incorrect (hasa, nae,
nue, shema, pelae, and six nonexistent correlatives were present).

All fixes were redone on branch `consistency/canon-repair`, verified
mechanically this time:

- Every item in the 2026-02-05 list re-applied (kofe→naphe, wiru→lopia,
  nima→nulae, nolea→theo, suno→sorae, wela→towe/welao)
- ch15 rebuilt (had phonology-violating words: via, vena, fina)
- ch16 ki/si gloss inversion and Slot 1 ordering corrected
- Reference docs re-baselined; pamphlet errors fixed
- Checklist automated: `scripts/validate_examples.py` now verifies
  word existence, phonotactics, syllable arrays, and duplicates.
  Documentation validates with zero errors as of this entry.

