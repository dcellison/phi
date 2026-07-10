# Part 6: Voice, page, and writing modes

Core Phi keeps its punctuation in words and can be transcribed from careful speech without recovering silent commas or capitals. Exact payload has a different contract.

## The boundary invariant

`patha` and `patho` are spoken or rendered in every Phi mode. They always tell the listener or reader where source material begins and ends. The internal payload may remain Latin text, Chinese characters, digits, a formula, or another notation even when the surrounding Phi is written in Tengwar.

Guest payload uses Phi sounds, so it can be rendered fully in Roman or Tengwar mode:

```
ne hasha samira hasho so shua.
NAME EXT.GUEST [samira] EXT.GUEST.CLOSE FUT come.
(Samira will come.)
```

Exact payload stays in source form between rendered boundaries:

```
ne patha 李明 patho so shua.
NAME EXT.EXACT [李明] EXT.EXACT.CLOSE FUT come.
(Li Ming will come.)
```

## Speaking exact material

The writer's payload is authoritative. A speaker may reproduce its source pronunciation, spell it, or describe it by a convention already shared with the listener. If exact recovery matters, transmit the written payload as well.

This is not a failure of the spoken-punctuation design. The external boundary remains fully audible; Phi simply declines to claim that an arbitrary script, URL, or formula can be reconstructed letter for letter from an unspecified oral rendering.
