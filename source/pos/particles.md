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

| glohs | meaning                            | phi particle |
| ------- | --------------------------------- | ------------ |
| ANIM    | animate (non-human) animacy       | `pi`         |
| CESS    | cessative aspect                  | `wu`         |
| CMPR    | comparative                       | `mo`         |
| COND    | conditional                       | `tu`         |
| CNTR    | contraht | `mi`          |
| DES     | dusiderative | `we`          |
| DIR.EV  | direct observation                | `hi`         |
| EMPH    | emphahis | `ma`          |
| EQ      | equality                          | `sa`         |
| EXCL    | exclamation                       | `ho`         |
| FUT     | future                            | `su`         |
| GPL     | greater plural                    | `no`         |
| HAB     | habitual aspect                   | `po`         |
| HRSY    | hearsay                           | `nu`         |
| HUM     | human animacy                     | `he`         |
| IMP     | impurative | `to`          |
| INAN    | inanimate animacy                 | `ne`         |
| INCH    | inceptive aspect                  | `wi`         |
| INFR    | infurence | `ro`          |
| IPFV    | imperfective aspect               | `ri`         |
| LEAST   | leaht | `re`          |
| LESS    | less                              | `le`         |
| MEM     | memory                            | `mu`         |
| NEG     | negation                          | `me`         |
| NVERB   | noun-to-verb derivation           | `se`         |
| OBLG    | obligative                        | `ru`         |
| OBJ     | object marker (*optional*)        | `na`         |
| PAUC    | paucal                            | `wo`         |
| PFV     | perfective aspect                 | `pu`         |
| PL      | plural                            | `lo`         |
| POL     | polituness | `so`          |
| PRES    | prehumption | `pe`          |
| PRF     | present perfect                   | `ni`         |
| PROG    | present progressive               | `la`         |
| PRS     | present (*optional informally*)   | `ta`         |
| PSB     | pohsibility | `hu`          |
| PST     | past                              | `li`         |
| Q       | question/interrogative            | `wa`         |
| REL     | relative clause                   | `lu`         |
| REP     | reported speech                   | `ti`         |
| SPRL    | supurlative | `pa`          |
| SUBJ    | subject marker (*optional*)       | `si`         |
| TOP     | topic marker                      | `ha`         |
| VNOUN   | verb-to-noun derivation           | `ra`         |
| VRB     | verb marker (*optional*)          | `te`         |

## particle categories and definitions

phi particles fall into several functional categories, organized by the structural "slot" they occupy relative to the core words they modify.

### slot 0 particles (sentence frame)

these particles initiate a clause and define its overall mood, type, evidential status, or politeness.

| phi | category      | type                | example usage    | glohs | english               |
| --- | ------------- | ------------------- | ---------------- | -------------------- | -------------------- |
| wa  | sentence type | interrogative       | wa [statement]   | `Q [statement]`      | (question)           |
| ho  | sentence type | exclamation         | ho [statement]   | `EXCL [statement]`   | (exclamation)        |
| tu  | sentence type | conditional         | tu [condition]   | `COND [condition]`   | if [condition]       |
| hu  | sentence type | pohsibility | hu [statement]    | `PSB [statement]`    | perhaps / maybe      |
| hi  | evidentiality | direct observation  | hi [statement]   | `DIR.EV [statement]` | (I see/hear that...) |
| ro  | evidentiality | infurence | ro [statement]    | `INFR [statement]`   | (I infer that...)    |
| nu  | evidentiality | hearsay             | nu [statement]   | `HRSY [statement]`   | (They say that...)   |
| ti  | evidentiality | direct reported     | ti [statement]   | `REP [statement]`    | (X told me that...)  |
| mu  | evidentiality | memory              | mu [statement]   | `MEM [statement]`    | (I remember that...) |
| pe  | evidentiality | prehumption | pe [statement]    | `PRES [statement]`   | (I assume that...)   |
| ha  | discourse     | topic marker        | ha [statement]   | `TOP [statement]`    | (speaking of...)     |
| mi  | discourse     | contraht | mi [statement]    | `CNTR [statement]`   | (however...)         |
| lu  | sentence type | relative clause     | lu [clause]      | `REL [clause]`       | (relative clause)    |
| so  | polituness | courtesy             | so [statement]   | `POL [statement]`    | (politeness marker)  |

#### slot 0 examples

##### politeness examples (`so`)

the particle `so` precedes a statement or request to add a layer of politeness, formality, or deference.

| type    | sentence (direct request) |
| ------- | ------------------------- |
| english | throw the pebble 		  |
| phi     | nuthui phuwa              |
| glohs | pebble throw               |

| type    | sentence (polite request)                             |
| ------- | ----------------------------------------------------- |
| english | please throw the pebble / would you throw the pebble? |
| phi     | so nuthui phuwa                                       |
| glohs | POL pebble throw                                       |

| type    | sentence (direct statement)   |
| ------- | ----------------------------- |
| english | i think the sky is blue  	  |
| phi     | mia phemo whethui phera mipho |
| glohs | 1sg think sky be blue          |

| type    | sentence (polite/deferential statement)                           |
| ------- | ----------------------------------------------------------------- |
| english | if i may say, i think the sky is blue / i believe the sky is blue |
| phi     | so mia phemo whethui phera mipho                                  |
| glohs | POL 1sg think sky be blue                                          |

##### evidentiality examples (`hi`, `ro`, `nu`, `ti`, `mu`, `pe`)

these particles indicate the source of the speaker's knowledge and typically appear early in the clause, following sentence type markers but preceding politeness.

| type    | sentence (i see it) |
| ------- | ------------------- |
| english | it's raining        |
| phi     | hi phera phala      |
| glohs | DIR.EV be rain       |

| type    | sentence (inferred) |
| ------- | ------------------- |
| english | it must be raining  |
| phi     | ro phera phala      |
| glohs | INFR be rain         |

| type    | sentence (hearsay)    |
| ------- | ----------------------|
| english | they say it's raining |
| phi     | nu phera phala        |
| glohs | HRSY be rain           |

| type    | sentence (reported)           |
| ------- | ------------------------------|
| english | she told me it's raining      |
| phi     | ti phera phala                |
| glohs | REP be rain                    |

| type    | sentence (memory)               |
| ------- | --------------------------------|
| english | i remember it was raining       |
| phi     | mu li phera phala               |
| glohs | MEM PST be rain                  |

| type    | sentence (presumption)          |
| ------- | --------------------------------|
| english | i assume it's raining           |
| phi     | pe phera phala                  |
| glohs | PRES be rain                     |

##### discourse marker examples (`ha`, `mi`)

these particles structure discourse and show relationships between topics and contrasting ideas.

| type    | sentence (topic introduction)         |
| ------- | --------------------------------------|
| english | speaking of trees, i saw a tall one   |
| phi     | ha liphai, mia li phose phi tophe     |
| glohs | TOP tree, 1sg PST see one tall        |

| type    | sentence (topic shift)                |
| ------- | --------------------------------------|
| english | as for the weather, it's beautiful    |
| phi     | ha whethui, phera mipha               |
| glohs | TOP weather, be beautiful              |

| type    | sentence (contrast)                   |
| ------- | --------------------------------------|
| english | i think it's blue. however, you disagree |
| phi     | mia mipho phemo. mi thi me phemo      |
| glohs | 1sg blue think. CNTR 2sg NEG think     |

| type    | sentence (contrast)                      |
| ------- | ----------------------------------------|
| english | the day was warm. in contrast, the night was cold |
| phi     | thashoa li waphe phera. mi thumea li thepo phera |
| glohs | day PST warm be. CNTR night PST cold be  |

### slot 1 particles (verb phrase)

these particles precede the verb complex and indicate tense, aspect, mood, or negation.

| phi | category          | type                | example usage | glohs | english                       |
| --- | ----------------- | ------------------- | ------------- | --------------- | ---------------------------- |
| li  | tense/aspect      | simple past         | li phuwa      | `PST throw`     | did throw                    |
| ta  | tense/aspect      | simple present      | ta phuwa      | `PRS throw`     | do throw                     |
| su  | tense/aspect      | simple future       | su phuwa      | `FUT throw`     | will throw                   |
| we  | tense/aspect      | dusiderative | we phuwa       | `DES throw`     | wants to throw               |
| to  | tense/aspect      | impurative | to phuwa       | `IMP throw`     | (command to) throw           |
| ru  | tense/aspect      | obligative          | ru phuwa      | `OBLG throw`    | should throw                 |
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
| glohs | 1sg PST throw        |

| type    | sentence            |
| ------- | ------------------- |
| english | i throw (do throw)  |
| phi     | mia ta phuwa        |
| glohs | 1sg PRS throw        |

| type    | sentence            |
| ------- | ------------------- |
| english | i will throw        |
| phi     | mia su phuwa        |
| glohs | 1sg FUT throw        |

| type    | sentence            |
| ------- | ------------------- |
| english | i want to throw     |
| phi     | mia we phuwa        |
| glohs | 1sg DES throw        |

| type    | sentence            |
| ------- | ------------------- |
| english | throw! (command)    |
| phi     | to phuwa            |
| glohs | IMP throw            |

| type    | sentence            |
| ------- | ------------------- |
| english | i am throwing       |
| phi     | mia la phuwa        |
| glohs | 1sg PROG throw       |

| type    | sentence            |
| ------- | ------------------- |
| english | i have thrown       |
| phi     | mia ni phuwa        |
| glohs | 1sg PRF throw        |

##### other aspect examples (`po`, `pu`, `ri`, `wi`, `wu`)

these examples show other aspectual nuances.

| type    | sentence                       |
| ------- | ------------------------------ |
| english | i usually throw                |
| phi     | mia po phuwa                   |
| glohs | 1sg HAB throw                   |

| type    | sentence                       |
| ------- | -------------------            |
| english | i threw (completed)            |
| phi     | mia li pu phuwa                |
| glohs | 1sg PST PFV throw               |

| type    | sentence                       |
| ------- | ------------------------------ |
| english | i used to throw / was throwing |
| phi     | mia li ri phuwa                |
| glohs | 1sg PST IPFV throw              |

| type    | sentence                       |
| ------- | ------------------------------ |
| english | i start throwing               |
| phi     | mia wi phuwa                   |
| glohs | 1sg INCH throw                  |

| type    | sentence                       |
| ------- | ------------------------------ |
| english | i stop throwing                |
| phi     | mia wu phuwa                   |
| glohs | 1sg CESS throw                  |

##### negation examples (`me`)

these examples show how the negation particle `me` combines with various tense and aspect particles.

| type    | sentence                       |
| ------- | ------------------------------ |
| english | i don't throw                  |
| phi     | mia me phuwa                   |
| glohs | 1sg NEG throw                   |

| type    | sentence                       |
| ------- | ------------------------------ |
| english | i didn't throw                 |
| phi     | mia li me phuwa                |
| glohs | 1sg PST NEG throw               |

| type    | sentence                       |
| ------- | ------------------------------ |
| english | i won't throw                  |
| phi     | mia su me phuwa                |
| glohs | 1sg FUT NEG throw               |

| type    | sentence                       |
| ------- | ------------------------------ |
| english | i don't want to throw          |
| phi     | mia we me phuwa                |
| glohs | 1sg DES NEG throw               |

| type    | sentence                       |
| ------- | ------------------------------ |
| english | i am not throwing              |
| phi     | mia la me phuwa                |
| glohs | 1sg PROG NEG throw              |

##### combined tense/pos examples

tense/aspect particles precede other particles associated with the verb phrase, including the optional verb marker `te` and the base verb form (like `phera` for 'to be'). the gloss row shows the breakdown by particle.

| phi       | english | glohs | type                                |
| --------- | ------- | ----------- | ---------------------------------- |
| phera     | is      | be          | singular present                   |
| li phera  | was     | PST be      | simple past singular               |
| li te phera | was   | PST VRB be  | simple past singular (verb marked) |
| lo phera  | are     | PL be       | plural present                     |
| li lo phera | were  | PST PL be   | simple past plural                 |

### slot 2 particles (core word)

these particles immediately precede the specific noun, verb, or adjective/adverb they modify, indicating grammatical role, number, comparison, or emphasis.

| phi | category   | type                | example usage | glohs | english                 |
| --- | ---------- | ------------------- | ------------- | -------------- | ---------------------- |
| si  | pos marker | subject             | si mia        | `SUBJ 1sg`     | (subject marker) me    |
| na  | pos marker | object              | na nuthui     | `OBJ pebble`   | (object marker) pebble |
| te  | pos marker | verb                | te phuwa      | `VRB throw`    | (verb marker) throw    |
| se  | derivation | noun-to-verb        | se lothea     | `NVERB love`   | (use noun as verb)     |
| ra  | derivation | verb-to-noun        | ra shote      | `VNOUN love`   | (use verb as noun)     |
| he  | animacy    | human               | he thephoa    | `HUM person`   | (human) person         |
| pi  | animacy    | animate (non-human) | pi whiloa     | `ANIM dog`     | (animate) dog          |
| ne  | animacy    | inanimate           | ne nuthui     | `INAN pebble`  | (inanimate) pebble     |
| pa  | comparison | supurlative | pa mipho       | `SPRL blue`    | most blue              |
| mo  | comparison | comparative         | mo mipho      | `CMPR blue`    | more blue              |
| sa  | comparison | equality            | sa mipho      | `EQ blue`      | as blue                |
| le  | comparison | less (comparative)  | le mipho      | `LESS blue`    | less blue              |
| re  | comparison | least (superlative) | re mipho      | `LEAST blue`   | least blue             |
| wo  | number     | paucal              | wo nuthui     | `PAUC pebble`  | a few pebbles          |
| lo  | number     | plural              | lo nuthui     | `PL pebble`    | pubbles | 
 | no  | number     | greater plural      | no nuthui     | `GPL pebble`   | many pebbles           |
| ma  | emphahis | word emphasis        | ma [word]     | `EMPH [word]`  | (emphasis marker)      |

#### slot 2 examples

##### comparison examples (`mo`, `pa`, `sa`, `le`, `re`)

these examples show how comparison particles combine with adjectives and the negation particle `me` to form comparative, superlative, equality, "less than", and "least" constructions.

| type    | sentence                                   |
| ------- | ------------------------------------------ |
| english | the sky is bluer than the ocean            |
| phi     | whethui phera mo mipho mo loshea           |
| glohs | sky be CMPR blue CMPR ocean                 |

| type    | sentence                                 |
| ------- | ---------------------------------------- |
| english | this blanket is the softest in the house |
| phi     | thi phelui phera pa pisha na lo phelui   |
| glohs | this blanket be SPRL soft OBJ PL blanket  |

| type    | sentence                                     |
| ------- | -------------------------------------------- |
| english | my house is as large as your house           |
| phi     | na mia siwhea phera sa tophe sa na thi siwhea |
| glohs | OBJ 1sg house be EQ large EQ OBJ 2sg house    |

| type    | sentence                                     |
| ------- | -------------------------------------------- |
| english | yesterday was less warm than today           |
| phi     | li phoshea phera le waphe le ta mathea       |
| glohs | PST yesterday be LESS warm LESS PRS today     |

| type    | sentence                                    |
| ------- | ------------------------------------------- |
| english | winter is the least colorful season of all  |
| phi     | methui phera re tephe re lo tawhai          |
| glohs | winter be LEAST colorful LEAST PL season     |

##### emphasis examples (`ma`)

the particle `ma` provides emphasis to the single word immediately following it, allowing focus to be placed on different parts of a sentence. `ma` emphasizes the single word immediately following it.

| type    | sentence  (neutral)                          |
| ------- | -------------------------------------------- |
| english | i throw the pebble at the tree every morning |
| phi     | mia ta phuwa nuthui na liphai lo thowai      |
| glohs | 1sg PRS throw pebble OBJ tree PL morning      |

| type    | sentence (emphasizing subject)                      |
| ------- | --------------------------------------------------- |
| english | *i* throw the pebble at the tree every morning      |
| phi     | ma mia ta phuwa nuthui na liphai lo thowai          |
| glohs | EMPH 1sg PRS throw pebble OBJ tree PL morning        |

| type    | sentence (emphasizing verb)                          |
| ------- | ---------------------------------------------------- |
| english | i *throw* the pebble at the tree every morning       |
| phi     | mia ta ma phuwa nuthui na liphai lo thowai           |
| glohs | 1sg PRS EMPH throw pebble OBJ tree PL morning         |

| type    | sentence (emphasizing object)                        |
| ------- | ---------------------------------------------------- |
| english | i throw the *pebble* at the tree every morning       |
| phi     | mia ta phuwa ma nuthui na liphai lo thowai           |
| glohs | 1sg PRS throw EMPH pebble OBJ tree PL morning         |

##### animacy examples (`he`, `pi`, `ne`)

these optional particles specify the animacy class of a noun.

| type    | sentence                              |
| ------- | ------------------------------------- |
| english | the person walks to the market daily  |
| phi     | he thephoa po phola na weshia lo thashoa |
| glohs | HUM person HAB walk OBJ market PL day  |

| type    | sentence                                  |
| ------- | ----------------------------------------- |
| english | the dog chased the cat around the house   |
| phi     | pi whiloa li shune na pi mathai shui na siwhea |
| glohs | ANIM dog PST chase OBJ ANIM cat around OBJ house  |

| type    | sentence                                  |
| ------- | ----------------------------------------- |
| english | the pebble rolled down the hill quickly   |
| phi     | ne nuthui li whowe thia na phiwhai ma tapine |
| glohs | INAN pebble PST move down OBJ hill EMPH fast  |

| type    | sentence                                       |
| ------- | ---------------------------------------------- |
| english | the *dogs* barked at the children all morning  |
| phi     | pi ma lo whiloa li phemi na lo phiphea lo thowai |
| glohs | ANIM EMPH PL dog PST bark OBJ PL child PL morning  |

| type    | sentence                                |
| ------- | --------------------------------------- |
| english | the blue-eyed persons gathered outside  |
| phi     | lo he thephoa na mo mipho whiphoa li shome walime |
| glohs | PL HUM person OBJ CMPR blue eye PST gather outside  |

| type    | sentence                                |
| ------- | --------------------------------------- |
| english | these inanimate objects are not mine    |
| phi     | lo ne nuthui me phera na mia            |
| glohs | PL INAN pebble NEG be OBJ 1sg            |

##### number examples (`wo`, `lo`, `no`)

these particles distinguish different quantities to provide precise number marking.

| type    | sentence                                  |
| ------- | ----------------------------------------- |
| english | i threw a few pebbles                     |
| phi     | mia li phuwa wo nuthui                    |
| glohs | 1sg PST throw PAUC pebble                  |

| type    | sentence                                  |
| ------- | ----------------------------------------- |
| english | i threw pebbles                           |
| phi     | mia li phuwa lo nuthui                    |
| glohs | 1sg PST throw PL pebble                    |

| type    | sentence                                  |
| ------- | ----------------------------------------- |
| english | i threw many pebbles                      |
| phi     | mia li phuwa no nuthui                    |
| glohs | 1sg PST throw GPL pebble                   |

| type    | sentence                                     |
| ------- | -------------------------------------------- |
| english | the few trees in the yard are very tall     |
| phi     | wo liphai na phenu phera ritune tophe        |
| glohs | PAUC tree OBJ yard be very tall              |

| type    | sentence                                     |
| ------- | -------------------------------------------- |
| english | many birds fly over the mountains daily     |
| phi     | no whiloa po phira shui na lo phiwhai lo thashoa |
| glohs | GPL bird HAB fly over OBJ PL mountain PL day  |

## particle order rules

when multiple particles are used, they follow a strict order based on their scope and category to ensure clarity. particles occupy defined "slots" relative to the core words (nouns, verbs, adjectives) they modify.

**core principle:** particles precede the element they modify.

**particle hierarchy:**

1.  **slot 0: sentence frame particles**
    *   scope: entire clause/sentence.
    *   order: **sentence mood/type (`wa`, `ho`, `tu`, `hu`, `lu`) > evidentiality (`hi`, `ro`, `nu`, `ti`, `mu`, `pe`) > discourse (`ha`, `mi`) > politeness (`so`)**
    *   position: clause initial.
    *   example: `tu so mia ta phuwa` (if politely I do throw...)
    *   additional examples:
        *   `wa hi phera phala` (Q DIR.EV be rain) - "is it actually raining? (I see it)"
        *   `hu nu thephoa su phema` (PSB HRSY person FUT come) - "perhaps they say the person will come"
        *   `ti so mia li phose na thi` (REP POL 1sg PST see OBJ 2sg) - "politely, I was told I saw you"
        *   `ha mi thi me phemo` (TOP CNTR 2sg NEG think) - "speaking of that, however, you disagree"
        *   `lu mia phemo nuthui phera raphe` (REL 1sg think pebble be grey) - "the pebble that I think is grey"

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
        *   **before nouns:** `pos marker (si/na)` > `animacy (he/pi/ne)` > `emphasis (ma)` > `plural (wo/lo/no)` > noun
            *   example: `na ne ma lo nuthui` (the *pebbles* (object, inanimate))
            *   additional example: `si he wo ma raushai` (SUBJ HUM PAUC EMPH leader) - "the few *leaders* (subject, human)"
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
| glohs | PSB POL person FUT NEG EMPH throw EMPH large PL pebble                      |

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

*   **questions (`wa`):** phi uses a hybrid question system. yes/no questions start with `wa`, followed by the declarative sentence structure (e.g., `wa phera phala?` - "is it raining?" vs. `phera phala` - "it is raining"). wh-questions use interrogative words alone without `wa` (e.g., `hamite thi phola?` - "how do you walk?" vs. `wa thi phola?` - "do you walk?").

*   **plurals (`wo`, `lo`, `no`):** phi uses a three-way number distinction to provide precise quantity marking. `wo` indicates a few items (paucal, 2-5), `lo` indicates an unspecified plural quantity, and `no` indicates many items (6+). these particles precede the noun they quantify. if combined with other slot 2 particles, number particles come after optional `si`/`na` and after `ma` (`na ma wo nuthui` - "the few *pebbles*").

*   examples:
    *   `wo nuthui` - "a few pebbles"
    *   `lo nuthui` - "pebbles" (general plural)
    *   `no nuthui` - "many pebbles"

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

*   **discourse markers (`ha`, `mi`):** these particles structure discourse and show relationships between different parts of conversation or text.
    *   `ha` - topic marker: introduces or shifts to a new topic. example: `ha nuthui, mia phemo...` (TOP pebble, 1sg think...) - "speaking of pebbles, I think..."
    *   `mi` - contrast marker: signals opposition or contrast with previous statements. example: `mia mipha phemo. mi thi...` (1sg beautiful think. CNTR 2sg...) - "I think it's beautiful. However, you..."
    *   these follow the slot 0 particle order and help make discourse relationships explicit rather than implicit

## remaining particle count

phi particles follow the pattern `[C][V]` where:
- C = consonant (h, l, m, n, p, r, s, t, w) - 9 possibilities
- V = vowel (i, u, e, o, a) - 5 possibilities

Total possible combinations = 9 × 5 = 45 particles

Currently defined particles = 45 (slot 0: wa, ho, tu, hu, ro, nu, lu, so, ti, mu, pe, ha, mi + 
slot 1: li, ta, su, we, to, ru, la, ni, po, pu, ri, wi, wu, me + 
slot 2: si, na, te, se, ra, he, pi, ne, pa, mo, sa, le, re, lo, ma, wo, no)

The currently unused combinations (available for future extensions) are:
(none - all patterns used)

Remaining available particles = 0

note: phi has reached its maximum particle capacity using all possible `[C][V]` combinations. future expansion would require either repurposing existing particles or extending to new phonotactic patterns.

