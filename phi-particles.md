---
tags:
  - pos
  - outlier
---
# particles

> particles are small, invariable words that do not fit neatly into the standard categories of nouns, verbs, adjectives, etc. they are used to express grammatical relationships, modify meanings, or convey nuances in a sentence. particles often accompany verbs to form phrasal verbs, indicating a special meaning different from the original verb alone. their meaning and function can vary significantly across different languages.

## introduction

particles are a cornerstone of phi grammar. because verbs do not conjugate, particles are essential for indicating grammatical information such as tense, mood, aspect, number, comparison, politeness, and emphasis. they can also optionally mark the grammatical role (subject, object, verb) of core words, enhancing clarity, particularly in more formal registers.

## core principle: precedence

in phi, particles strictly precede the word, phrase, or clause they modify or are associated with. for example, the particle `na` marks the following noun phrase as the object (`na nuthui` - 'the pebble' as object), and the particle `wa` turns the following statement into a question (`wa phera phala` - 'is it raining?'). this consistent pre-positioning is a defining feature of phi syntax.

the scope of a particle determines how much of the following sentence it affects. sentence frame particles (slot 0) typically apply to the entire clause. verb phrase particles (slot 1) modify the verb complex (tense, aspect, negation). core word particles (slot 2) generally modify only the immediately following word; the emphasis particle `ma` specifically targets only the single word after it.

## gloss abbreviations

interlinear glossing provides a morpheme-by-morpheme breakdown of linguistic examples, aligning the original text with its grammatical analysis and translation. this table lists the abbreviations used for grammatical categories in the glosses throughout this document. in a gloss, lowercase words indicates lexical items.

| gloss   | meaning                           | phi particle |
| ------- | --------------------------------- | ------------ |
| ANIM    | animate (non-human) animacy       | `pi`         |
| CESS    | cessative aspect                  | `wu`         |
| CMPR    | comparative                       | `mo`         |
| COND    | conditional                       | `tu`         |
| DES     | desiderative                      | `we`         |
| DIR.EV  | direct observation                | `hi`         |
| EMPH    | emphasis                          | `ma`         |
| EQ      | equality                          | `sa`         |
| EXCL    | exclamation                       | `ho`         |
| FUT     | future                            | `su`         |
| HAB     | habitual aspect                   | `po`         |
| HRSY    | hearsay                           | `nu`         |
| HUM     | human animacy                     | `he`         |
| IMP     | imperative                        | `to`         |
| INAN    | inanimate animacy                 | `ne`         |
| INCH    | inceptive aspect                  | `wi`         |
| INFR    | inference                         | `ro`         |
| IPFV    | imperfective aspect               | `ri`         |
| LEAST   | least                             | `re`         |
| LESS    | less                              | `le`         |
| NEG     | negation                          | `me`         |
| NVERB   | noun-to-verb derivation           | `se`         |
| OBLG    | obligative                        | `ru`         |
| OBJ     | object marker (*optional*)        | `na`         |
| PFV     | perfective aspect                 | `pu`         |
| PL      | plural                            | `lo`         |
| POL     | politeness                        | `so`         |
| PRF     | present perfect                   | `ni`         |
| PROG    | present progressive               | `la`         |
| PRS     | present (*optional informally*)   | `ta`         |
| PSB     | possibility                       | `hu`         |
| PST     | past                              | `li`         |
| Q       | question/interrogative            | `wa`         |
| SPRL    | superlative                       | `pa`         |
| SUBJ    | subject marker (*optional*)       | `si`         |
| VNOUN   | verb-to-noun derivation           | `ra`         |
| VRB     | verb marker (*optional*)          | `te`         |

## particle categories and definitions

phi particles fall into several functional categories, organized by the structural "slot" they occupy relative to the core words they modify.

### slot 0 particles (sentence frame)

these particles initiate a clause and define its overall mood, type, evidential status, or politeness.

| phi | category      | type                | example usage    | gloss                | english              |
| --- | ------------- | ------------------- | ---------------- | -------------------- | -------------------- |
| wa  | sentence type | interrogative       | wa [statement]   | `Q [statement]`      | (question)           |
| ho  | sentence type | exclamation         | ho [statement]   | `EXCL [statement]`   | (exclamation)        |
| tu  | sentence type | conditional         | tu [condition]   | `COND [condition]`   | if [condition]       |
| hu  | sentence type | possibility         | hu [statement]   | `PSB [statement]`    | perhaps / maybe      |
| hi  | evidentiality | direct observation  | hi [statement]   | `DIR.EV [statement]` | (I see/hear that...) |
| ro  | evidentiality | inference           | ro [statement]   | `INFR [statement]`   | (I infer that...)    |
| nu  | evidentiality | hearsay             | nu [statement]   | `HRSY [statement]`   | (They say that...)   |
| so  | politeness    | courtesy            | so [statement]   | `POL [statement]`    | (politeness marker)  |

#### slot 0 examples

##### politeness examples (`so`)

the particle `so` precedes a statement or request to add a layer of politeness, formality, or deference.

| type    | sentence (direct request) |
| ------- | ------------------------- |
| english | throw the pebble 		  |
| phi     | nuthui phuwa              |
| gloss   | pebble throw              |

| type    | sentence (polite request)                             |
| ------- | ----------------------------------------------------- |
| english | please throw the pebble / would you throw the pebble? |
| phi     | so nuthui phuwa                                       |
| gloss   | POL pebble throw                                      |

| type    | sentence (direct statement)   |
| ------- | ----------------------------- |
| english | i think the sky is blue  	  |
| phi     | mia phemo whethui phera mipho |
| gloss   | 1sg think sky be blue         |

| type    | sentence (polite/deferential statement)                           |
| ------- | ----------------------------------------------------------------- |
| english | if i may say, i think the sky is blue / i believe the sky is blue |
| phi     | so mia phemo whethui phera mipho                                  |
| gloss   | POL 1sg think sky be blue                                         |

##### evidentiality examples (`hi`, `ro`, `nu`)

these particles indicate the source of the speaker's knowledge and typically appear early in the clause, following sentence type markers but preceding politeness.

| type    | sentence (i see it) |
| ------- | ------------------- |
| english | it's raining        |
| phi     | hi phera phala      |
| gloss   | DIR.EV be rain      |

| type    | sentence (inferred) |
| ------- | ------------------- |
| english | it must be raining  |
| phi     | ro phera phala      |
| gloss   | INFR be rain        |

| type    | sentence (hearsay)    |
| ------- | ----------------------|
| english | they say it's raining |
| phi     | nu phera phala        |
| gloss   | HRSY be rain          |

### slot 1 particles (verb phrase)

these particles precede the verb complex and indicate tense, aspect, mood, or negation.

| phi | category          | type                | example usage | gloss           | english                      |
| --- | ----------------- | ------------------- | ------------- | --------------- | ---------------------------- |
| li  | tense/aspect      | simple past         | li phuwa      | `PST throw`     | did throw                    |
| ta  | tense/aspect      | simple present      | ta phuwa      | `PRS throw`     | do throw                     |
| su  | tense/aspect      | simple future       | su phuwa      | `FUT throw`     | will throw                   |
| we  | tense/aspect/mood | desiderative        | we phuwa      | `DES throw`     | wants to throw               |
| to  | tense/aspect/mood | imperative          | to phuwa      | `IMP throw`     | (command to) throw           |
| ru  | tense/aspect/mood | obligative          | ru phuwa      | `OBLG throw`    | should throw                 |
| la  | tense/aspect      | present progressive | la phuwa      | `PROG throw`    | throwing                     |
| ni  | tense/aspect      | present perfect     | ni phuwa      | `PRF throw`     | has thrown                   |
| po  | tense/aspect      | habitual            | po phuwa      | `HAB throw`     | usually throws               |
| pu  | tense/aspect      | perfective          | pu phuwa      | `PFV throw`     | did throw (completed)        |
| ri  | tense/aspect      | imperfective        | ri phuwa      | `IPFV throw`    | was throwing / used to throw |
| wi  | tense/aspect      | inceptive           | wi phuwa      | `INCH throw`    | starts throwing              |
| wu  | tense/aspect      | cessative           | wu phuwa      | `CESS throw`    | stops throwing               |
| me  | negation          | negative            | me phemo      | `NEG think`     | (not) think                  |

#### slot 1 examples

##### basic tense/aspect examples (`li`, `ta`, `su`, `we`, `la`, `ni`)

these examples illustrate the basic use of each tense/aspect particle with a simple verb.

| type    | sentence            |
| ------- | ------------------- |
| english | i threw (did throw) |
| phi     | mia li phuwa        |
| gloss   | 1sg PST throw       |

| type    | sentence            |
| ------- | ------------------- |
| english | i throw (do throw)  |
| phi     | mia ta phuwa        |
| gloss   | 1sg PRS throw       |

| type    | sentence            |
| ------- | ------------------- |
| english | i will throw        |
| phi     | mia su phuwa        |
| gloss   | 1sg FUT throw       |

| type    | sentence            |
| ------- | ------------------- |
| english | i want to throw     |
| phi     | mia we phuwa        |
| gloss   | 1sg DES throw       |

| type    | sentence            |
| ------- | ------------------- |
| english | throw! (command)    |
| phi     | to phuwa            |
| gloss   | IMP throw           |

| type    | sentence            |
| ------- | ------------------- |
| english | i am throwing       |
| phi     | mia la phuwa        |
| gloss   | 1sg PROG throw      |

| type    | sentence            |
| ------- | ------------------- |
| english | i have thrown       |
| phi     | mia ni phuwa        |
| gloss   | 1sg PRF throw       |

##### other aspect examples (`po`, `pu`, `ri`, `wi`, `wu`)

these examples show other aspectual nuances.

| type    | sentence                       |
| ------- | ------------------------------ |
| english | i usually throw                |
| phi     | mia po phuwa                   |
| gloss   | 1sg HAB throw                  |

| type    | sentence                       |
| ------- | -------------------            |
| english | i threw (completed)            |
| phi     | mia li pu phuwa                |
| gloss   | 1sg PST PFV throw              |

| type    | sentence                       |
| ------- | ------------------------------ |
| english | i used to throw / was throwing |
| phi     | mia li ri phuwa                |
| gloss   | 1sg PST IPFV throw             |

| type    | sentence                       |
| ------- | ------------------------------ |
| english | i start throwing               |
| phi     | mia wi phuwa                   |
| gloss   | 1sg INCH throw                 |

| type    | sentence                       |
| ------- | ------------------------------ |
| english | i stop throwing                |
| phi     | mia wu phuwa                   |
| gloss   | 1sg CESS throw                 |

##### negation examples (`me`)

these examples show how the negation particle `me` combines with various tense and aspect particles.

| type    | sentence                       |
| ------- | ------------------------------ |
| english | i don't throw                  |
| phi     | mia me phuwa                   |
| gloss   | 1sg NEG throw                  |

| type    | sentence                       |
| ------- | ------------------------------ |
| english | i didn't throw                 |
| phi     | mia li me phuwa                |
| gloss   | 1sg PST NEG throw              |

| type    | sentence                       |
| ------- | ------------------------------ |
| english | i won't throw                  |
| phi     | mia su me phuwa                |
| gloss   | 1sg FUT NEG throw              |

| type    | sentence                       |
| ------- | ------------------------------ |
| english | i don't want to throw          |
| phi     | mia we me phuwa                |
| gloss   | 1sg DES NEG throw              |

| type    | sentence                       |
| ------- | ------------------------------ |
| english | i am not throwing              |
| phi     | mia la me phuwa                |
| gloss   | 1sg PROG NEG throw             |

##### combined tense/pos examples

tense/aspect particles precede other particles associated with the verb phrase, including the optional verb marker `te` and the base verb form (like `phera` for 'to be'). the gloss row shows the breakdown by particle.

| phi       | english | gloss       | type                               |
| --------- | ------- | ----------- | ---------------------------------- |
| phera     | is      | be          | singular present                   |
| li phera  | was     | PST be      | simple past singular               |
| li te phera | was   | PST VRB be  | simple past singular (verb marked) |
| lo phera  | are     | PL be       | plural present                     |
| li lo phera | were  | PST PL be   | simple past plural                 |

### slot 2 particles (core word)

these particles immediately precede the specific noun, verb, or adjective/adverb they modify, indicating grammatical role, number, comparison, or emphasis.

| phi | category   | type                | example usage | gloss          | english                |
| --- | ---------- | ------------------- | ------------- | -------------- | ---------------------- |
| si  | pos marker | subject             | si mia        | `SUBJ 1sg`     | (subject marker) me    |
| na  | pos marker | object              | na nuthui     | `OBJ pebble`   | (object marker) pebble |
| te  | pos marker | verb                | te phuwa      | `VRB throw`    | (verb marker) throw    |
| se  | derivation | noun-to-verb        | se lothea     | `NVERB love`   | (use noun as verb)     |
| ra  | derivation | verb-to-noun        | ra shote      | `VNOUN love`   | (use verb as noun)     |
| he  | animacy    | human               | he thephoa    | `HUM person`   | (human) person         |
| pi  | animacy    | animate (non-human) | pi whiloa     | `ANIM dog`     | (animate) dog          |
| ne  | animacy    | inanimate           | ne nuthui     | `INAN pebble`  | (inanimate) pebble     |
| pa  | comparison | superlative         | pa mipho      | `SPRL blue`    | most blue              |
| mo  | comparison | comparative         | mo mipho      | `CMPR blue`    | more blue              |
| sa  | comparison | equality            | sa mipho      | `EQ blue`      | as blue                |
| le  | comparison | less (comparative)  | le mipho      | `LESS blue`    | less blue              |
| re  | comparison | least (superlative) | re mipho      | `LEAST blue`   | least blue             |
| lo  | number     | plural              | lo nuthui     | `PL pebble`    | (plural) pebble        |
| ma  | emphasis   | word emphasis       | ma [word]     | `EMPH [word]`  | (emphasis marker)      |

#### slot 2 examples

##### comparison examples (`mo`, `pa`, `sa`, `le`, `re`)

these examples show how comparison particles combine with adjectives and the negation particle `me` to form comparative, superlative, equality, "less than", and "least" constructions.

| type    | sentence                                   |
| ------- | ------------------------------------------ |
| english | the sky is bluer than the ocean            |
| phi     | whethui phera mo mipho mo loshea           |
| gloss   | sky be CMPR blue CMPR ocean                |

| type    | sentence                                 |
| ------- | ---------------------------------------- |
| english | this blanket is the softest in the house |
| phi     | thi phelui phera pa pisha na lo phelui   |
| gloss   | this blanket be SPRL soft OBJ PL blanket |

| type    | sentence                                     |
| ------- | -------------------------------------------- |
| english | my house is as large as your house           |
| phi     | na mia siwhea phera sa tophe sa na thi siwhea |
| gloss   | OBJ 1sg house be EQ large EQ OBJ 2sg house   |

| type    | sentence                                     |
| ------- | -------------------------------------------- |
| english | yesterday was less warm than today           |
| phi     | li phoshea phera le waphe le ta mathea       |
| gloss   | PST yesterday be LESS warm LESS PRS today    |

| type    | sentence                                    |
| ------- | ------------------------------------------- |
| english | winter is the least colorful season of all  |
| phi     | methui phera re tephe re lo tawhai          |
| gloss   | winter be LEAST colorful LEAST PL season    |

##### emphasis examples (`ma`)

the particle `ma` provides emphasis to the single word immediately following it, allowing focus to be placed on different parts of a sentence. `ma` emphasizes the single word immediately following it.

| type    | sentence  (neutral)                          |
| ------- | -------------------------------------------- |
| english | i throw the pebble at the tree every morning |
| phi     | mia ta phuwa nuthui na liphai lo thowai      |
| gloss   | 1sg PRS throw pebble OBJ tree PL morning     |

| type    | sentence (emphasizing subject)                      |
| ------- | --------------------------------------------------- |
| english | *i* throw the pebble at the tree every morning      |
| phi     | ma mia ta phuwa nuthui na liphai lo thowai          |
| gloss   | EMPH 1sg PRS throw pebble OBJ tree PL morning       |

| type    | sentence (emphasizing verb)                          |
| ------- | ---------------------------------------------------- |
| english | i *throw* the pebble at the tree every morning       |
| phi     | mia ta ma phuwa nuthui na liphai lo thowai           |
| gloss   | 1sg PRS EMPH throw pebble OBJ tree PL morning        |

| type    | sentence (emphasizing object)                        |
| ------- | ---------------------------------------------------- |
| english | i throw the *pebble* at the tree every morning       |
| phi     | mia ta phuwa ma nuthui na liphai lo thowai           |
| gloss   | 1sg PRS throw EMPH pebble OBJ tree PL morning        |

##### animacy examples (`he`, `pi`, `ne`)

these optional particles specify the animacy class of a noun.

| type    | sentence                              |
| ------- | ------------------------------------- |
| english | the person walks to the market daily  |
| phi     | he thephoa po phola na weshia lo thashoa |
| gloss   | HUM person HAB walk OBJ market PL day |

| type    | sentence                                  |
| ------- | ----------------------------------------- |
| english | the dog chased the cat around the house   |
| phi     | pi whiloa li shune na pi mathai shui na siwhea |
| gloss   | ANIM dog PST chase OBJ ANIM cat around OBJ house |

| type    | sentence                                  |
| ------- | ----------------------------------------- |
| english | the pebble rolled down the hill quickly   |
| phi     | ne nuthui li whowe thia na phiwhai ma tapine |
| gloss   | INAN pebble PST move down OBJ hill EMPH fast |

| type    | sentence                                       |
| ------- | ---------------------------------------------- |
| english | the *dogs* barked at the children all morning  |
| phi     | pi ma lo whiloa li phemi na lo phiphea lo thowai |
| gloss   | ANIM EMPH PL dog PST bark OBJ PL child PL morning |

| type    | sentence                                |
| ------- | --------------------------------------- |
| english | the blue-eyed persons gathered outside  |
| phi     | lo he thephoa na mo mipho whiphoa li shome walime |
| gloss   | PL HUM person OBJ CMPR blue eye PST gather outside |

| type    | sentence                                |
| ------- | --------------------------------------- |
| english | these inanimate objects are not mine    |
| phi     | lo ne nuthui me phera na mia            |
| gloss   | PL INAN pebble NEG be OBJ 1sg           |

## particle order rules

when multiple particles are used, they follow a strict order based on their scope and category to ensure clarity. particles occupy defined "slots" relative to the core words (nouns, verbs, adjectives) they modify.

**core principle:** particles precede the element they modify.

**particle hierarchy:**

1.  **slot 0: sentence frame particles**
    *   scope: entire clause/sentence.
    *   order: **sentence mood/type (`wa`, `ho`, `tu`, `hu`) > evidentiality (`hi`, `ro`, `nu`) > politeness (`so`)**
    *   position: clause initial.
    *   example: `tu so mia ta phuwa` (if politely I do throw...)
    *   additional examples:
        *   `wa hi phera phala` (Q DIR.EV be rain) - "is it actually raining? (I see it)"
        *   `hu nu thephoa su phema` (PSB HRSY person FUT come) - "perhaps they say the person will come"

2.  **slot 1: verb phrase grammatical particles**
    *   scope: core verb phrase.
    *   order: **tense (`li`, `ta`, `su`) > aspect (`we`, `la`, `ni`, `po`, `pu`, `ri`, `wi`, `wu`) > negation (`me`)**
    *   position: precedes the verb and any slot 2 verb particles.
    *   example: `li pu me phuwa` (did not throw (completed action))
    *   additional examples:
        *   `su la phuri` (FUT PROG work) - "will be working"
        *   `li ri me phera mipho` (PST IPFV NEG be blue) - "wasn't blue" / "used to not be blue"

3.  **slot 2: core word immediate particles**
    *   scope: the specific noun, verb, or adjective immediately following.
    *   position: directly precedes the core word, following any slot 0 or 1 particles.
    *   order within slot 2:
        *   **before nouns:** `pos marker (si/na)` > `animacy (he/pi/ne)` > `emphasis (ma)` > `plural (lo)` > noun
            *   example: `na ne ma lo nuthui` (the *pebbles* (object, inanimate))
            *   additional example: `si he lo ma raushai` (SUBJ HUM PL EMPH leader) - "the *leaders* (subject, human)"
        *   **before verbs:** `pos marker (te)` > `emphasis (ma)` > verb
            *   example: `te ma phuwa` ((verb) *throw*)
            *   additional example: `te ma phuri` (VRB EMPH work) - "*work* (verb)"
        *   **before adjectives/adverbs:** `comparison (mo/pa/sa/le/re)` > `emphasis (ma)` > adjective/adverb
            *   example: `pa ma pisha` (most *soft*)
            *   additional example: `mo ma tapine` (CMPR EMPH fast) - "*faster*"

**example sentence demonstrating order:**

| type    | sentence                                                                   |
| ------- | -------------------------------------------------------------------------- |
| english | perhaps the polite person emphatically won't *throw* the *large* pebbles   |
| phi     | hu so thephoa su me ma phuwa ma tophe lo nuthui                            |
| gloss   | PSB POL person FUT NEG EMPH throw EMPH large PL pebble                     |

*   breakdown:
    *   `hu so` (slot 0: perhaps polite)
    *   `thephoa` (subject noun)
    *   `su me` (slot 1: will not)
    *   `ma phuwa` (slot 2: *throw*)
    *   `ma tophe` (slot 2: *large*)
    *   `lo nuthui` (slot 2: plural pebble - object noun phrase)

## usage notes

*   **optional pos markers:** the subject (`si`), object (`na`), and verb (`te`) markers are optional. they are typically used for disambiguation (e.g., if a noun and verb share the same form) or in formal contexts to ensure maximum clarity.
    *   example: `phuri` could mean "to work" or "work/job" - `te phuri` (VRB work) clarifies it's a verb, while `si thuwhia` (SUBJ work) or `na thuwhia` (OBJ work) clarifies it's a noun

*   **optional animacy markers:** the animacy markers (`he`, `pi`, `ne`) are also optional. they can be used to clarify the nature of a noun, especially if ambiguous, or omitted if the context or lexical meaning makes the animacy clear. they generally do not apply to pronouns (e.g., `mia`, `thi`, `sha`).

*   **optional present tense (`ta`):** similarly, the simple present tense particle `ta` is formally required but often omitted in informal speech and writing when the present tense is implied by context (i.e., the absence of other tense/aspect markers). e.g., formal: `mia ta phuwa nuthui` (1sg PRS throw pebble), informal: `mia phuwa nuthui` (1sg throw pebble).

*   **questions (`wa`):** questions start with `wa`, followed by the declarative sentence structure. e.g., `wa phera phala?` (is it raining?) vs. `phera phala` (it is raining).

*   **plurals (`lo`):** `lo` precedes the noun it pluralizes (`lo nuthui` - pebbles). if combined with other slot 2 particles, `lo` comes after optional `si`/`na` and after `ma` (`na ma lo nuthui`).

*   **negation scope (`me`):** the placement of the negation particle determines its scope.
    *   verb phrase negation: `mia li me phuwa` (1sg PST NEG throw) - "I did not throw" (negates the action)
    *   constituent negation: `me lo nuthui` (NEG PL pebble) - "not pebbles" (negates just the noun)
    *   total vs. partial negation: to express "none" use `me` with the appropriate noun (`me thephoa` - "no person"); to express "not all" use `me lo` with the noun (`me lo thephoa` - "not all people")
    *   double negation: two negation particles cancel each other out, creating a positive assertion: `me me phuwa` (NEG NEG throw) - "not not throw" = "do throw"; typically, this is used for emphasis: `mia me me phemo` (1sg NEG NEG think) - "I definitely think so" / "I don't not think so"

*   **exclusive plurals:** to express "we/us (but not you)", use `lo mia me thi` (plural me not you). exclusion can target others: `lo mia me lo sha` (plural me not plural it -> us not them).
    *   example: `lo mia me thi su phuwa nuthui` (PL 1sg NEG 2sg FUT throw pebble) - "we (not you) will throw the pebble"
    *   example: `lo mia su thuli na lo thuwhia me lo thi` (PL 1sg FUT finish OBJ PL work NEG PL 2sg) - "we will finish the jobs without you all"

*   **derivational particles:** these particles allow words from one part of speech to be used temporarily as another part of speech, providing flexibility while maintaining phi's phonological distinctions between word classes.
    *   `se` - noun-to-verb derivation (NVERB): transforms a noun into a verb construct. example: `mia na thi se lothea` (1sg OBJ 2sg NVERB love) - "i love you" (using the noun "lothea" as a verb)
    *   `ra` - verb-to-noun derivation (VNOUN): transforms a verb into a noun construct. example: `ra shote phera ritune teshe` (VNOUN love be very good) - "loving is very good" (using the verb "shote" as a noun)
    *   these derivational particles follow the same precedence rules as other core word particles, appearing immediately before the word being transformed.
    *   this is particularly useful for:
        *   noun-to-verb: when a dedicated verb doesn't exist or for creative/metaphorical expressions
        *   verb-to-noun: for abstract concepts or gerund-like constructions
        *   note: these are distinct from the more permanent solutions created with full lexical entries and should be seen as flexible, contextual transformations

*   **future considerations:** ideas like multiple plurals (for "several" vs "many") remain under consideration and are not yet defined.

## future considerations

the following concepts represent potential extensions to the phi particle system. these are not currently implemented but represent areas for future growth that maintain phi's design principles.

### multiple plurals

phi could benefit from a more nuanced plural system distinguishing between different quantities:

| phi | category | type          | example usage    | gloss           | english description         |
| --- | -------- | ------------- | ---------------- | --------------- | --------------------------- |
| lo  | number   | general plural| lo nuthui        | `PL pebble`     | pebbles (unspecified count) |
| wo  | number   | paucal        | wo nuthui        | `PAUC pebble`   | a few pebbles (2-5)         |
| mo  | number   | plural        | mo nuthui        | `PL pebble`     | several pebbles (6-20)      |
| no  | number   | greater plural| no nuthui        | `GPL pebble`    | many pebbles (21+)          |

this would create a four-way distinction in number:
- singular (unmarked): `nuthui` - "a pebble"
- paucal (few): `wo nuthui` - "a few pebbles"
- plural (several): `mo nuthui` - "several pebbles"
- greater plural (many): `no nuthui` - "many pebbles"

implementation notes:
- this would refine the current `lo` into more specific quantifiers
- interaction with other slot 2 particles would follow the same precedence rules
- this would give phi more expressive power for quantity distinctions common in some natural languages

example sentences:
- `mia wo nuthui li phuwa` - "i threw a few pebbles"
- `mia mo nuthui li phuwa` - "i threw several pebbles"
- `mia no nuthui li phuwa` - "i threw many pebbles"

### evidentiality expansion

phi's current evidentiality system (direct observation, inference, hearsay) could be expanded to include these additional distinctions:

| phi | category      | type                | example usage    | gloss                | english                   |
| --- | ------------- | ------------------- | ---------------- | -------------------- | ------------------------- |
| hi  | evidentiality | direct observation  | hi [statement]   | `DIR.EV [statement]` | (I see/hear that...)      |
| ro  | evidentiality | inference           | ro [statement]   | `INFR [statement]`   | (I infer that...)         |
| nu  | evidentiality | hearsay             | nu [statement]   | `HRSY [statement]`   | (They say that...)        |
| mu  | evidentiality | memory              | mu [statement]   | `MEM [statement]`    | (I remember that...)      |
| su  | evidentiality | second-hand         | su [statement]   | `2H [statement]`     | (I was told directly...)  |
| pu  | evidentiality | established fact    | pu [statement]   | `FACT [statement]`   | (It is known that...)     |

this would create a more nuanced system for source-of-knowledge marking.

### nominal classification

a lightweight classifier system could be introduced, using slot 2 particles to mark semantic categories:

| phi | category    | type                   | example usage | gloss            | english                    |
| --- | ----------- | ---------------------- | ------------- | ---------------- | -------------------------- |
| ha  | classifier  | humans                 | ha thephoa    | `CL:HUM person`  | person (human class)       |
| pa  | classifier  | tools/implements       | pa phimea     | `CL:TOOL tool`   | tool (implement class)     |
| ma  | classifier  | animals                | ma thiphea    | `CL:ANIM animal` | animal (animal class)      |
| ta  | classifier  | flat/flexible objects  | ta whephai    | `CL:FLAT paper`  | paper (flat class)         |
| sa  | classifier  | round objects          | sa mophui     | `CL:ROUND ball`  | ball (round class)         |
| wa  | classifier  | long objects           | wa rophai     | `CL:LONG rope`   | rope (long class)          |
| la  | classifier  | liquids                | la wheisha    | `CL:LIQ water`   | water (liquid class)       |

these would be optional and could enhance semantic precision, particularly for counting expressions and demonstratives.

### other potential extensions

other particle categories that could be considered:
- **mirativity markers**: indicating surprise or unexpectedness
- **valency-changing particles**: applicatives, causatives, etc.
- **register markers**: particles indicating formal, informal, poetic, or technical speech
- **discourse markers**: particles for topic, focus, or discourse structure

all extensions would adhere to phi's phonological and syntactic principles while enhancing expressive possibilities.

## available [C][V] combinations

the following consonant-vowel combinations are currently unused in the phi particle system and remain available for future particle assignments:

| combination | status  |
| ----------- | ------- |
| ha          | unused  |
| lu          | unused  |
| mi          | unused  |
| mu          | unused  |
| ni          | unused  |
| no          | unused  |
| pe          | unused  |
| ti          | unused  |
| wo          | unused  |

these combinations follow phi's particle pattern of a single consonant followed by a single vowel. when designing new particles, consideration should be given to phonological distinctiveness, mnemonic value, and systematic coherence with existing particles.
