# 2. Three-Slot Particle System

Phi's grammar is expressed through a three-slot particle system: `Slot 0` → `Slot 1` → `Slot 2`. This system provides a clear and logical structure for modifying the meaning of sentences, verbs, and individual words.

## 2.1. Slot 0: Sentence Frame Particles
These appear at the very beginning of a sentence (after the vocative `ko`, if present) and shape its entire context.

**Question (`wa`):**
```
wa thi lothea kela
Q 2SG love understand
(Do you understand love?)
```

**Imperative (`no`):**
```
no minu shele
IMP family help
(Help the family.)
```

**Conditional (`lu` and `lu whe`):**
Phi distinguishes between real and unreal conditions.
- **Realis Conditional (`lu`):** Used for real or likely possibilities ("if").
  ```
  lu mia shele...
  COND 1SG help...
  (If I help...)
  ```
- **Irrealis Conditional (`lu whe`):** Used for unreal, hypothetical, or counterfactual situations ("if only...", "if it were that..."). It combines `lu` with the irrealis particle `whe`.
  ```
  lu whe mia to shele...
  COND IRR 1SG PST help...
  (If I had helped [but I didn't]...)
  ```

**Optative (`su`):**
Frames a sentence as a hope, wish, or prayer.
```
su weola wela sio
OPT community good be
(May the community be well / I hope for the community to be well.)
```

**Politeness (`pi`):**
```
pi no minu shele
POL IMP family help
(Please help the family.)
```

## 2.2. Slot 1: Verb Phrase Particles
These particles modify verbs and are placed immediately before the verb they affect. They are organized by their function.

### 2.2.1. Tense
- `to` (PST): `mia to kela` (I understood)
- `so` (FUT): `mia so kela` (I will understand)
- Present: unmarked default

### 2.2.2. Aspect
- `ki` (PFV): `mia to ki kela` (I have understood)
- `si` (IPFV): `mia si kela` (I am understanding)
- `pa` (INCH): `mia pa kela` (I begin to understand)
- `te` (CESS): `mia te kela` (I stop understanding)

### 2.2.3. Voice
- `se` (PASS): `thola se pholea` (The story is created.)

### 2.2.4. Modality
- `po` (POSS): `sha po thola` (The other can speak)
- `na` (NEC): `mia na sio` (I must exist)
- `ka` (CAUS): `mia pilo ka nima` (I make the child sleep)

### 2.2.5. Negation
- `ma` (NEG): `sha ma kela` (The other does not understand)

### 2.2.6. Particle Stacking
Slot 1 particles can be combined in a specific order: `Tense` > `Aspect` > `Voice` > `Modality`.
```
pi thi so pa po kela
POL 2SG FUT INCH POSS understand
(Politely, you will be able to begin to understand.)
```

### 2.2.7. The Causative Construction
The causative particle `ka` is a special modal used to indicate that the subject (the Agent) causes the object (the Patient) to perform an action. This changes the sentence structure slightly.

- **With an intransitive verb:** The agent is added as the new subject, and the original subject becomes the object (the patient).
  - **Base:** `pilo nima.` (The child sleeps.)
  - **Causative:** `mia pilo ka nima.` (I make the child sleep.)

- **With a transitive verb:** The agent is added as the new subject, and the original subject becomes the primary object (the patient).
  - **Base:** `thi thola kela.` (You understand the story.)
  - **Causative:** `mia thi thola ka kela.` (I make you understand the story.)

### 2.2.8. The Passive Voice
The voice particle `se` is used to form the passive voice. This construction promotes the object of an active sentence to the subject position and typically omits the original agent (the doer of the action). It is used to shift focus to the recipient of the action.

- **Structure:** `[Patient] se [Verb]`
- **Active:** `mia thola pholea` (I create the story.)
- **Passive:** `thola se pholea` (The story is created.)

## 2.3. Slot 2: Word-Level Particles
These precede and modify individual words:

**Number:**
- `lo` (PL): `lo whelea` (friends)

**Focus:**
- `she` (FOC): `mia she lothea kela` (I understand *love*)

**Comparison:**
- `mo` (COMP): Forms the comparative.
- `mo she` (SUPER): Forms the superlative.
- In a comparative sentence, the standard of comparison is marked with the postposition `thele` (than).
  ```
  noshale shiro thele mo wela sio
  garden forest than COMP good/beautiful be
  (The garden is more beautiful than the forest.)
  ```
- The equative ("as...as") is formed with the postposition `phea`.
  ```
  noshale shiro phea wela sio
  garden forest as good/beautiful be
  (The garden is as beautiful as the forest.)
  ```

**Deixis:**
- `pha` (PROX): `pha whelea` (this friend)
- `tha` (DIST): `that whelea` (that friend)

**Honorifics:**
Phi uses Slot 2 particles before a name or title to express social context and respect. This system is based on relationship, not hierarchy.
- `sa` (HON.RESPECT): Marks respect for a mentor or elder. `sa Thala`
- `ni` (HON.INTIM): Marks intimacy with a close friend or family. `ni Hino`
- `le` (HON.ROLE): Marks respect for a community role. `le Mako` 