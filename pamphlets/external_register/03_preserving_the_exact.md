# Part 3: Preserving the exact

`patha` suspends Phi's internal spelling and vocabulary checks. A single standalone `patho` ends the suspension.

```
mia patha https://example.org/spec?v=2 patho theo.
1SG EXT.EXACT [https://example.org/spec?v=2] EXT.EXACT.CLOSE read.
(I read https://example.org/spec?v=2.)

mia patha E = mc² patho theo.
1SG EXT.EXACT [E = mc²] EXT.EXACT.CLOSE read.
(I read "E = mc².")

phao patha 5 mg patho to haolu.
parent EXT.EXACT [5 mg] EXT.EXACT.CLOSE PST speak.
(The parent said "5 mg.")
```

Capital letters, punctuation, digits, mathematical signs, arbitrary scripts, and external sound values all belong to the payload. They do not weaken the lowercase and period-only rules on either side.

## Escaping the closer

Two plain occurrences of `patho patho` inside payload represent one literal occurrence in the external material. The next single `patho` closes:

```
mia patha literal patho patho token patho theo.
1SG EXT.EXACT [literal patho patho token] EXT.EXACT.CLOSE read.
(I read material containing the literal token "patho.")
```

Everything except the closer is opaque. A word that looks like `hasha` or `patha` inside exact payload does not open another frame. Exact frames therefore never acquire nested Phi structure.

## Safe rendering

Opaque does not mean trusted as markup. Generated Phi pages escape payload before displaying it:

```
mia patha <sample data-id="7"> patho theo.
1SG EXT.EXACT [<sample data-id="7">] EXT.EXACT.CLOSE read.
(I read the exact sample tag.)
```

The source characters remain visible, but they cannot become active HTML.
