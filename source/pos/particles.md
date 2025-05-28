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

| gloss | meaning                            | phi particle |
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

| phi | category      | type                | example usage    | gloss | english               |
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
| phi     | nuthui whuwa              |
| gloss | pebble throw               |

| type    | sentence (polite request)                             |
| ------- | ----------------------------------------------------- |
| english | please throw the pebble / would you throw the pebble? |
| phi     | so nuthui whuwa                                       |
| gloss | POL pebble throw                                       |

| type    | sentence (direct statement)   |
| ------- | ----------------------------- |
| english | i think the sky is blue  	  |
| phi     | mia phemo whethui phera mipho |
| gloss | 1sg think sky be blue          |

| type    | sentence (polite/deferential statement)                           |
| ------- | ----------------------------------------------------------------- |
| english | if i may say, i think the sky is blue / i believe the sky is blue |
| phi     | so mia phemo whethui phera mipho                                  |
| gloss | POL 1sg think sky be blue                                          |

##### evidentiality examples (`hi`, `ro`, `nu`, `ti`, `mu`, `pe`)

these particles indicate the source of the speaker's knowledge and typically appear early in the clause, following sentence type markers but preceding politeness.

| type    | sentence (i see it) |
| ------- | ------------------- |
| english | it's raining        |
| phi     | hi phera phala      |
| gloss | DIR.EV be rain       |

| type    | sentence (inferred) |
| ------- | ------------------- |
| english | it must be raining  |
| phi     | ro phera phala      |
| gloss | INFR be rain         |

| type    | sentence (hearsay)    |
| ------- | ----------------------|
| english | they say it's raining |
| phi     | nu phera phala        |
| gloss | HRSY be rain           |

| type    | sentence (reported)           |
| ------- | ------------------------------|
| english | she told me it's raining      |
| phi     | ti phera phala                |
| gloss | REP be rain                    |

| type    | sentence (memory)               |
| ------- | --------------------------------|
| english | i remember it was raining       |
| phi     | mu li phera phala               |
| gloss | MEM PST be rain                  |

| type    | sentence (presumption)          |
| ------- | --------------------------------|
| english | i assume it's raining           |
| phi     | pe phera phala                  |
| gloss | PRES be rain                     |

##### discourse marker examples (`ha`, `mi`)

these particles structure discourse and show relationships between topics and contrasting ideas.

| type    | sentence (topic introduction)         |
| ------- | --------------------------------------|
| english | speaking of trees, i saw a tall one   |
| phi     | ha liphai, mia li phose phi tophe     |
| gloss | TOP tree, 1sg PST see one tall        |

| type    | sentence (topic shift)                |
| ------- | --------------------------------------|
| english | as for the weather, it's beautiful    |
| phi     | ha whethui, phera mipha               |
| gloss | TOP weather, be beautiful              |

| type    | sentence (contrast)                   |
| ------- | --------------------------------------|
| english | i think it's blue. however, you disagree |
| phi     | mia mipho phemo. mi thi me phemo      |
| gloss | 1sg blue think. CNTR 2sg NEG think     |

| type    | sentence (contrast)                      |
| ------- | ----------------------------------------|
| english | the day was warm. in contrast, the night was cold |
| phi     | thashoa li waphe phera. mi thumea li thepo phera |
| gloss | day PST warm be. CNTR night PST cold be  |

### slot 1 particles (verb phrase)

these particles precede the verb complex and indicate tense, aspect, mood, or negation.

| phi | category          | type                | example usage | gloss | english                       |
| --- | ----------------- | ------------------- | ------------- | --------------- | ---------------------------- |
| li  | tense/aspect      | simple past         | li whuwa      | `PST throw`     | did throw                    |
| ta  | tense/aspect      | simple present      | ta whuwa      | `PRS throw`     | do throw                     |
| su  | tense/aspect      | simple future       | su whuwa      | `FUT throw`     | will throw                   |
| we  | tense/aspect      | dusiderative | we whuwa       | `DES throw`     | wants to throw               |
| to  | tense/aspect      | impurative | to whuwa       | `IMP throw`     | (command to) throw           |
| ru  | tense/aspect      | obligative          | ru whuwa      | `OBLG throw`    | should throw                 |
| la  | tense/aspect      | present progressive | la whuwa      | `PROG throw`    | throwing                     |
| ni  | tense/aspect      | present perfect     | ni whuwa      | `PRF throw`     | has thrown                   |
| po  | tense/aspect      | habitual            | po whuwa      | `HAB throw`     | usually throws               |
| pu  | tense/aspect      | perfective          | pu whuwa      | `PFV throw`     | did throw (completed)        |
| ri  | tense/aspect      | imperfective        | ri whuwa      | `IPFV throw`    | was throwing / used to throw |
| wi  | tense/aspect      | inceptive           | wi whuwa      | `INCH throw`    | starts throwing              |
| wu  | tense/aspect      | cessative           | wu whuwa      | `CESS throw`    | stops throwing               |
| me  | negation          | negative            | me phemo      | `NEG think`     | (not) think                  |

#### slot 1 examples

##### basic tense/aspect examples (`li`, `ta`, `su`, `we`, `la`, `ni`)

these examples illustrate the basic use of each tense/aspect particle with a simple verb.

| type    | sentence            |
| ------- | ------------------- |
| english | i threw (did throw) |
| phi     | mia li whuwa        |
| gloss | 1sg PST throw        |

| type    | sentence            |
| ------- | ------------------- |
| english | i throw (do throw)  |
| phi     | mia ta whuwa        |
| gloss | 1sg PRS throw        |

| type    | sentence            |
| ------- | ------------------- |
| english | i will throw        |
| phi     | mia su whuwa        |
| gloss | 1sg FUT throw        |

| type    | sentence            |
| ------- | ------------------- |
| english | i want to throw     |
| phi     | mia we whuwa        |
| gloss | 1sg DES throw        |

| type    | sentence            |
| ------- | ------------------- |
| english | throw! (command)    |
| phi     | to whuwa            |
| gloss | IMP throw            |

| type    | sentence            |
| ------- | ------------------- |
| english | i am throwing       |
| phi     | mia la whuwa        |
| gloss | 1sg PROG throw       |

| type    | sentence            |
| ------- | ------------------- |
| english | i have thrown       |
| phi     | mia ni whuwa        |
| gloss | 1sg PRF throw        |

##### other aspect examples (`po`, `pu`, `ri`, `wi`, `wu`)

these examples show other aspectual nuances.

| type    | sentence                       |
| ------- | ------------------------------ |
| english | i usually throw                |
| phi     | mia po whuwa                   |
| gloss | 1sg HAB throw                   |

| type    | sentence                       |
| ------- | -------------------            |
| english | i threw (completed)            |
| phi     | mia li pu whuwa                |
| gloss | 1sg PST PFV throw               |

| type    | sentence                       |
| ------- | ------------------------------ |
| english | i used to throw / was throwing |
| phi     | mia li ri whuwa                |
| gloss | 1sg PST IPFV throw              |

| type    | sentence                       |
| ------- | ------------------------------ |
| english | i start throwing               |
| phi     | mia wi whuwa                   |
| gloss | 1sg INCH throw                  |

| type    | sentence                       |
| ------- | ------------------------------ |
| english | i stop throwing                |
| phi     | mia wu whuwa                   |
| gloss | 1sg CESS throw                  |

##### negation examples (`me`)

these examples show how the negation particle `me` combines with various tense and aspect particles.

| type    | sentence                       |
| ------- | ------------------------------ |
| english | i don't throw                  |
| phi     | mia me whuwa                   |
| gloss | 1sg NEG throw                   |

| type    | sentence                       |
| ------- | ------------------------------ |
| english | i didn't throw                 |
| phi     | mia li me whuwa                |
| gloss | 1sg PST NEG throw               |

| type    | sentence                       |
| ------- | ------------------------------ |
| english | i won't throw                  |
| phi     | mia su me whuwa                |
| gloss | 1sg FUT NEG throw               |

| type    | sentence                       |
| ------- | ------------------------------ |
| english | i don't want to throw          |
| phi     | mia we me whuwa                |
| gloss | 1sg DES NEG throw               |

| type    | sentence                       |
| ------- | ------------------------------ |
| english | i am not throwing              |
| phi     | mia la me whuwa                |
| gloss | 1sg PROG NEG throw              |

##### combined tense/pos examples

tense/aspect particles precede other particles associated with the verb phrase, including the optional verb marker `te` and the base verb form (like `phera` for 'to be'). the gloss row shows the breakdown by particle.

| phi       | english | gloss | type                                |
| --------- | ------- | ----------- | ---------------------------------- |
| phera     | is      | be          | singular present                   |
| li phera  | was     | PST be      | simple past singular               |
| li te phera | was   | PST VRB be  | simple past singular (verb marked) |
| lo phera  | are     | PL be       | plural present                     |
| li lo phera | were  | PST PL be   | simple past plural                 |

### slot 2 particles (core word)

these particles immediately precede the specific noun, verb, or adjective/adverb they modify, indicating grammatical role, number, comparison, or emphasis.

| phi | category   | type                | example usage | gloss | english                 |
| --- | ---------- | ------------------- | ------------- | -------------- | ---------------------- |
| si  | pos marker | subject             | si mia        | `SUBJ 1sg`     | (subject marker) me    |
| na  | pos marker | object              | na nuthui     | `OBJ pebble`   | (object marker) pebble |
| te  | pos marker | verb                | te whuwa      | `VRB throw`    | (verb marker) throw    |
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
| gloss | sky be CMPR blue CMPR ocean                 |

| type    | sentence                                 |
| ------- | ---------------------------------------- |
| english | this blanket is the softest in the house |
| phi     | thi phelui phera pa pisha na lo phelui   |
| gloss | this blanket be SPRL soft OBJ PL blanket  |

| type    | sentence                                     |
| ------- | -------------------------------------------- |
| english | my house is as large as your house           |
| phi     | na mia siwhea phera sa tophe sa na thi siwhea |
| gloss | OBJ 1sg house be EQ large EQ OBJ 2sg house    |

| type    | sentence                                     |
| ------- | -------------------------------------------- |
| english | yesterday was less warm than today           |
| phi     | li phoshea phera le waphe le ta mathea       |
| gloss | PST yesterday be LESS warm LESS PRS today     |

| type    | sentence                                    |
| ------- | ------------------------------------------- |
| english | winter is the least colorful season of all  |
| phi     | methui phera re tephe re lo tawhai          |
| gloss | winter be LEAST colorful LEAST PL season     |

##### emphasis examples (`ma`)

the particle `ma` provides emphasis to the single word immediately following it, allowing focus to be placed on different parts of a sentence. `ma` emphasizes the single word immediately following it.

| type    | sentence  (neutral)                          |
| ------- | -------------------------------------------- |
| english | i throw the pebble at the tree every morning |
| phi     | mia ta whuwa nuthui na liphai lo thowai      |
| gloss | 1sg PRS throw pebble OBJ tree PL morning      |

| type    | sentence (emphasizing subject)                      |
| ------- | --------------------------------------------------- |
| english | *i* throw the pebble at the tree every morning      |
| phi     | ma mia ta whuwa nuthui na liphai lo thowai          |
| gloss | EMPH 1sg PRS throw pebble OBJ tree PL morning        |

| type    | sentence (emphasizing verb)                          |
| ------- | ---------------------------------------------------- |
| english | i *throw* the pebble at the tree every morning       |
| phi     | mia ta ma whuwa nuthui na liphai lo thowai           |
| gloss | 1sg PRS EMPH throw pebble OBJ tree PL morning         |

| type    | sentence (emphasizing object)                        |
| ------- | ---------------------------------------------------- |
| english | i throw the *pebble* at the tree every morning       |
| phi     | mia ta whuwa ma nuthui na liphai lo thowai           |
| gloss | 1sg PRS throw EMPH pebble OBJ tree PL morning         |

##### animacy examples (`he`, `pi`, `ne`)

these optional particles specify the animacy class of a noun.

| type    | sentence                              |
| ------- | ------------------------------------- |
| english | the person walks to the market daily  |
| phi     | he thephoa po phola na weshia lo thashoa |
| gloss | HUM person HAB walk OBJ market PL day  |

| type    | sentence                                  |
| ------- | ----------------------------------------- |
| english | the dog chased the cat around the house   |
| phi     | pi whiloa li shune na pi mathai shui na siwhea |
| gloss | ANIM dog PST chase OBJ ANIM cat around OBJ house  |

| type    | sentence                                  |
| ------- | ----------------------------------------- |
| english | the pebble rolled down the hill quickly   |
| phi     | ne nuthui li whowe thia na phiwhai ma tapine |
| gloss | INAN pebble PST move down OBJ hill EMPH fast  |

| type    | sentence                                       |
| ------- | ---------------------------------------------- |
| english | the *dogs* barked at the children all morning  |
| phi     | pi ma lo whiloa li phemi na lo phiphea lo thowai |
| gloss | ANIM EMPH PL dog PST bark OBJ PL child PL morning  |

| type    | sentence                                |
| ------- | --------------------------------------- |
| english | the blue-eyed persons gathered outside  |
| phi     | lo he thephoa na mo mipho whiphoa li shome walime |
| gloss | PL HUM person OBJ CMPR blue eye PST gather outside  |

| type    | sentence                                |
| ------- | --------------------------------------- |
| english | these inanimate objects are not mine    |
| phi     | lo ne nuthui me phera na mia            |
| gloss | PL INAN pebble NEG be OBJ 1sg            |

##### number examples (`wo`, `lo`, `no`)

these particles distinguish different quantities to provide precise number marking.

| type    | sentence                                  |
| ------- | ----------------------------------------- |
| english | i threw a few pebbles                     |
| phi     | mia li whuwa wo nuthui                    |
| gloss | 1sg PST throw PAUC pebble                  |

| type    | sentence                                  |
| ------- | ----------------------------------------- |
| english | i threw pebbles                           |
| phi     | mia li whuwa lo nuthui                    |
| gloss | 1sg PST throw PL pebble                    |

| type    | sentence                                  |
| ------- | ----------------------------------------- |
| english | i threw many pebbles                      |
| phi     | mia li whuwa no nuthui                    |
| gloss | 1sg PST throw GPL pebble                   |

| type    | sentence                                     |
| ------- | -------------------------------------------- |
| english | the few trees in the yard are very tall     |
| phi     | wo liphai na phenu phera ritune tophe        |
| gloss | PAUC tree OBJ yard be very tall              |

| type    | sentence                                     |
| ------- | -------------------------------------------- |
| english | many birds fly over the mountains daily     |
| phi     | no whiloa po phira shui na lo phiwhai lo thashoa |
| gloss | GPL bird HAB fly over OBJ PL mountain PL day  |

## particle order rules

when multiple particles are used, they follow a strict order based on their scope and category to ensure clarity. particles occupy defined "slots" relative to the core words (nouns, verbs, adjectives) they modify.

**core principle:** particles precede the element they modify.

**particle hierarchy:**

1.  **slot 0: sentence frame particles**
    *   scope: entire clause/sentence.
    *   order: **sentence mood/type (`wa`, `ho`, `tu`, `hu`, `lu`) > evidentiality (`hi`, `ro`, `nu`, `ti`, `mu`, `pe`) > discourse (`ha`, `mi`) > politeness (`so`)**
    *   position: clause initial.
    *   example: `tu so mia ta whuwa` (if politely I do throw...)
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
    *   example: `li pu me whuwa` (did not throw (completed action))
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
            *   example: `te ma whuwa` ((verb) *throw*)
            *   additional example: `te ma phuri` (VRB EMPH work) - "*work* (verb)"
        *   **before adjectives/adverbs:** `comparison (mo/pa/sa/le/re)` > `emphasis (ma)` > adjective/adverb
            *   example: `pa ma pisha` (most *soft*)
            *   additional example: `mo ma tapine` (CMPR EMPH fast) - "*faster*"

**example sentence demonstrating order:**

| type    | sentence                                                                   |
| ------- | -------------------------------------------------------------------------- |
| english | perhaps the polite person emphatically won't *throw* the *large* pebbles   |
| phi     | hu so thephoa su me ma whuwa ma tophe lo nuthui                            |
| gloss | PSB POL person FUT NEG EMPH throw EMPH large PL pebble                      |

*   breakdown:
    *   `hu so` (slot 0: perhaps polite)
    *   `thephoa` (subject noun)
    *   `su me` (slot 1: will not)
    *   `ma whuwa` (slot 2: *throw*)
    *   `ma tophe` (slot 2: *large*)
    *   `lo nuthui` (slot 2: plural pebble - object noun phrase)

## usage notes

*   **optional pos markers:** the subject (`si`), object (`na`), and verb (`te`) markers are optional. they are typically used for disambiguation (e.g., if a noun and verb share the same form) or in formal contexts to ensure maximum clarity.
    *   example: `phuri` could mean "to work" or "work/job" - `te phuri` (VRB work) clarifies it's a verb, while `si thuwhia` (SUBJ work) or `na thuwhia` (OBJ work) clarifies it's a noun

*   **optional animacy markers:** the animacy markers (`he`, `pi`, `ne`) are also optional. they can be used to clarify the nature of a noun, especially if ambiguous, or omitted if the context or lexical meaning makes the animacy clear. they generally do not apply to pronouns (e.g., `mia`, `thi`, `sha`).

*   **optional present tense (`ta`):** similarly, the simple present tense particle `ta` is formally required but often omitted in informal speech and writing when the present tense is implied by context (i.e., the absence of other tense/aspect markers). e.g., formal: `mia ta whuwa nuthui` (1sg PRS throw pebble), informal: `mia whuwa nuthui` (1sg throw pebble).

*   **questions (`wa`):** phi uses a hybrid question system. yes/no questions start with `wa`, followed by the declarative sentence structure (e.g., `wa phera phala?` - "is it raining?" vs. `phera phala` - "it is raining"). wh-questions use interrogative words and can be combined with other particles except `wa` (e.g., `hamite thi phola?` - "how do you walk?", `so wulime thi ta shola?` - "politely, where do you go?", vs. `wa thi phola?` - "do you walk?"). The `wa` particle cannot be combined with wh-questions as they represent different question systems.

*   **plurals (`wo`, `lo`, `no`):** phi uses a three-way number distinction to provide precise quantity marking. `wo` indicates a few items (paucal, 2-5), `lo` indicates an unspecified plural quantity, and `no` indicates many items (6+). these particles precede the noun they quantify. if combined with other slot 2 particles, number particles come after optional `si`/`na` and after `ma` (`na ma wo nuthui` - "the few *pebbles*").

*   examples:
    *   `wo nuthui` - "a few pebbles"
    *   `lo nuthui` - "pebbles" (general plural)
    *   `no nuthui` - "many pebbles"

*   **negation scope (`me`):** the placement of the negation particle determines its scope.
    *   verb phrase negation: `mia li me whuwa` (1sg PST NEG throw) - "I did not throw" (negates the action)
    *   constituent negation: `me lo nuthui` (NEG PL pebble) - "not pebbles" (negates just the noun)
    *   total vs. partial negation: to express "none" use `me` with the appropriate noun (`me thephoa` - "no person"); to express "not all" use `me lo` with the noun (`me lo thephoa` - "not all people")
    *   double negation: two negation particles cancel each other out, creating a positive assertion: `me me whuwa` (NEG NEG throw) - "not not throw" = "do throw"; typically, this is used for emphasis: `mia me me phemo` (1sg NEG NEG think) - "I definitely think so" / "I don't not think so"

*   **exclusive plurals:** to express "we/us (but not you)", use `lo mia me thi` (plural me not you). exclusion can target others: `lo mia me lo sha` (plural me not plural it -> us not them).
    *   example: `lo mia me thi su whuwa nuthui` (PL 1sg NEG 2sg FUT throw pebble) - "we (not you) will throw the pebble"
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

## discourse particle sequences

discourse particles `ha` (topic marker) and `mi` (contrast marker) are essential for structuring complex arguments, extended narratives, and sophisticated communication. understanding their interaction patterns and scope rules enables effective multi-sentence discourse management.

### topic chains with `ha`

topic chains use `ha` to maintain thematic coherence across multiple sentences, creating explicit topic continuity that guides listener attention through complex discussions.

#### basic topic introduction and maintenance

| type    | discourse sequence |
| ------- | ------------------ |
| english | speaking of the weather, it's been quite unpredictable. the rain comes suddenly. then the sun appears. but the wind remains constant. |
| phi     | ha whethui, li phera ritune me phemo. lashea ta phema tapine. mi taoshea ta pharu. tupo riwhea ta thewa sa. |
| gloss   | TOP weather, PST be very NEG predictable. rain PRS come quickly. CNTR sun PRS appear. but wind PRS remain same. |

#### topic shift and subtopic development

| type    | discourse sequence |
| ------- | ------------------ |
| english | speaking of trees, the old oak is magnificent. as for its branches, they reach toward the sky. regarding its roots, they extend deep underground. |
| phi     | ha liphai, lotha whiophea phera mipha. ha na seiwhea, sha ta phiwe naho whethui. ha na haiwhia, sha ta phiwe thia na riphoa. |
| gloss   | TOP tree, old oak be beautiful. TOP OBJ branch, 3sg PRS reach toward sky. TOP OBJ root, 3sg PRS reach down OBJ ground. |

#### topic resumption after digression

| type    | discourse sequence |
| ------- | ------------------ |
| english | speaking of the market, it's very busy today. (digression about crowds) anyway, back to the market - the prices have increased significantly. |
| phi     | ha weshia, ta phera ritune thasha mathea. [...] ha mi weshia, lo phothui li phiro ritune tophe. |
| gloss   | TOP market, PRS be very busy today. [...] TOP CNTR market, PL price PST increase very much. |

#### nested topic structures

| type    | discourse sequence |
| ------- | ------------------ |
| english | speaking of education, universities are important. regarding universities, their libraries are essential. as for libraries, their digital resources are expanding rapidly. |
| phi     | ha muphui, lo thuwhui phera riphe. ha lo thuwhui, na lo whethea phera weshi. ha lo whethea, na lo pewhia phuroa ta phiro tapine ritune. |
| gloss   | TOP education, PL university be important. TOP PL university, OBJ PL library be necessary. TOP PL library, OBJ PL digital resource PRS increase quickly very. |

### contrast scope with `mi`

the contrast marker `mi` operates at different levels of discourse structure, from simple sentence-level contrasts to complex argumentative sequences spanning multiple paragraphs.

#### sentence-level contrast

| type    | discourse sequence |
| ------- | ------------------ |
| english | the morning was peaceful. however, the afternoon became chaotic. |
| phi     | thowai li phera tapha. mi phawhoa li phera tasha. |
| gloss   | morning PST be peaceful. CNTR afternoon PST be chaotic. |

#### paragraph-level contrast

| type    | discourse sequence |
| ------- | ------------------ |
| english | the northern regions experience mild summers with gentle breezes and moderate temperatures. in contrast, the southern areas face intense heat with scorching winds and extreme conditions. |
| phi     | lo huphe thauthea ta phewa supha tawhea nene luwhea riwhea nene waphe thephui. mi lo thia thauthea ta phewa notha tawhea nene rathu riwhea nene tasha thephui. |
| gloss   | PL north region PRS experience mild summer and gentle wind and warm temperature. CNTR PL south region PRS experience hot summer and bright wind and dangerous temperature. |

#### argumentative contrast sequences

| type    | discourse sequence |
| ------- | ------------------ |
| english | supporters argue that technology improves education by providing access to information. however, critics contend that it creates distractions and reduces human interaction. furthermore, research suggests that balanced approaches work best. |
| phi     | lo raushai ta phemo pewhia ta thulo muphui thotu siphai phose. mi lo thetu ta phemo sha ta phesa thiphui nene thuru he thephoa thiphui. nene tashoa ta phemo sa phola ta phuri pa teshe. |
| gloss   | PL supporter PRS think technology PRS improve education provide information access. CNTR PL critic PRS think 3sg PRS create distraction and reduce HUM person interaction. and research PRS think balanced approach PRS work most good. |

#### contrast with evidentiality

| type    | discourse sequence |
| ------- | ------------------ |
| english | i see that the project is progressing well. however, i hear that there are significant challenges behind the scenes. |
| phi     | hi phuphui ta phola teshe. mi nu no huphea phera na me phemo thauthea. |
| gloss   | DIR.EV project PRS progress good. CNTR HRSY many problem be OBJ NEG see area. |

### topic-contrast interaction patterns

when `ha` and `mi` appear together, they create sophisticated discourse structures that manage both thematic development and argumentative contrast simultaneously.

#### contrast within topic maintenance

| type    | discourse sequence |
| ------- | ------------------ |
| english | speaking of the new policy, most employees support it. however, within that same topic, senior staff have expressed concerns. |
| phi     | ha papho tushui, lo phuri thephoa ta renu sha. ha mi thi tushui, lo phuwhia phuri ta phemi huphea. |
| gloss   | TOP new policy, PL work person PRS support 3sg. TOP CNTR this policy, PL senior work PRS express concern. |

#### topic shift with contrast

| type    | discourse sequence |
| ------- | ------------------ |
| english | speaking of urban planning, cities need green spaces. as for rural development, however, the priorities are completely different. |
| phi     | ha thuwhui phola, lo thuwhui ta photo hashe thauthea. ha mi rathea phola, tupo lo riphe phera ritune lepha. |
| gloss   | TOP city planning, PL city PRS need green area. TOP CNTR rural development, but PL priority be very different. |

#### complex argumentative structures

| type    | discourse sequence |
| ------- | ------------------ |
| english | regarding economic policy, traditional approaches emphasize stability. however, speaking of innovation, modern strategies prioritize growth. nevertheless, concerning sustainability, both approaches must consider environmental impact. |
| phi     | ha phuthia tushui, lotha phola ta ma thiphie. mi ha papho phola, papho phola ta ma phiro. tupo ha muwhui thewa, lo phola ru thira muwhui mothea. |
| gloss   | TOP economic policy, traditional approach PRS EMPH stability. CNTR TOP new approach, new approach PRS EMPH growth. but TOP environmental sustainability, PL approach should consider environmental impact. |

#### discourse repair and clarification

| type    | discourse sequence |
| ------- | ------------------ |
| english | speaking of the meeting, it went well. actually, let me clarify - regarding the first part, it was productive. however, concerning the second half, there were some issues. |
| phi     | ha thiphui, sha li phola teshe. ha mi thiphui, na phi wuthai, sha li phera phuri teshe. mi na whu wuthai, wo huphea li phera. |
| gloss   | TOP meeting, 3sg PST go good. TOP CNTR meeting, OBJ one part, 3sg PST be work good. CNTR OBJ two part, few problem PST be. |

### advanced discourse patterns

#### parallel topic development

| type    | discourse sequence |
| ------- | ------------------ |
| english | speaking of technology in education, it offers many benefits. speaking of technology in healthcare, it also provides significant advantages. however, speaking of technology in privacy, it raises serious concerns. |
| phi     | ha pewhia na muphui, sha ta thotu no teshe. ha pewhia na showhia, sha ta thotu riphe teshe. mi ha pewhia na nithoa, sha ta phesa tasha huphea. |
| gloss   | TOP technology OBJ education, 3sg PRS provide many good. TOP technology OBJ healthcare, 3sg PRS provide important good. CNTR TOP technology OBJ privacy, 3sg PRS create serious concern. |

#### contrastive topic chains

| type    | discourse sequence |
| ------- | ------------------ |
| english | speaking of morning routines, i prefer exercise first. however, regarding evening routines, i prioritize relaxation. in contrast, concerning weekend routines, i focus on social activities. |
| phi     | ha thowai phola, mia ta phire phuri phi. mi ha phawhoa phola, mia ta riphe shesa. mi ha rewhoa phola, mia ta ma he thephoa thiphui. |
| gloss   | TOP morning routine, 1sg PRS prefer work first. CNTR TOP evening routine, 1sg PRS prioritize rest. CNTR TOP weekend routine, 1sg PRS EMPH HUM person interaction. |

#### meta-discourse management

| type    | discourse sequence |
| ------- | ------------------ |
| english | speaking of our discussion, we've covered the main points. however, regarding time constraints, we should focus on conclusions. therefore, concerning next steps, let's establish clear actions. |
| phi     | ha lo mia thiwhea, lo mia li phose na riphe niphia. mi ha lawhui huphea, lo mia ru ma rushai phemo. huwa ha su phola, lo mia ru phesa teshe phawu. |
| gloss   | TOP PL 1sg discussion, PL 1sg PST see OBJ important point. CNTR TOP time problem, PL 1sg should EMPH conclusion think. so TOP future action, PL 1sg should create good action. |

### discourse particle scope rules

1. **topic scope (`ha`)**: extends until a new topic is introduced or the discourse unit ends
2. **contrast scope (`mi`)**: applies to the immediately following clause or sentence
3. **interaction scope**: when both particles appear, `ha` establishes the thematic frame while `mi` provides the contrastive relationship within that frame
4. **reset conditions**: new `ha` markers reset topic scope; new `mi` markers reset contrast scope
5. **embedding**: topic-contrast patterns can be embedded within larger discourse structures

these patterns enable phi speakers to construct sophisticated arguments, maintain thematic coherence across extended discourse, and explicitly signal the logical relationships between ideas in complex communication.

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

## phi particle vocabulary

this section provides a comprehensive list of all phi particles with their basic english translations, organized alphabetically for quick reference.

| phi word | english translation |
| -------- | ------------------- |
| ha | topic marker |
| he | human animacy marker |
| hi | direct evidence marker |
| ho | exclamation marker |
| hu | possibility marker |
| la | progressive aspect |
| le | less (comparative) |
| li | past tense |
| lo | plural |
| lu | relative clause marker |
| ma | emphasis marker |
| me | negation |
| mi | contrast marker |
| mo | comparative |
| mu | memory evidentiality |
| na | object marker |
| ne | inanimate animacy marker |
| ni | present perfect |
| no | greater plural |
| nu | hearsay evidentiality |
| pa | superlative |
| pe | presumption evidentiality |
| pi | animate animacy marker |
| po | habitual aspect |
| pu | perfective aspect |
| ra | verb-to-noun derivation |
| re | least (superlative) |
| ri | imperfective aspect |
| ro | inference evidentiality |
| ru | obligative |
| sa | equality |
| se | noun-to-verb derivation |
| si | subject marker |
| so | politeness marker |
| su | future tense |
| ta | present tense |
| te | verb marker |
| ti | reported speech evidentiality |
| to | imperative |
| tu | conditional |
| wa | question marker |
| we | desiderative |
| wi | inceptive aspect |
| wo | paucal |
| wu | cessative aspect |

---

*for detailed usage examples and grammatical explanations of each particle, see the comprehensive sections above.*

