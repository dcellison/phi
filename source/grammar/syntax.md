---
tags:
  - grammar
  - standard
---
# syntax

> syntax refers to the rules governing how words and phrases are arranged to form sentences in a language. it defines the structural relationships between different elements, determining word order, agreement patterns, and hierarchical organization of phrases and clauses.

## introduction to phi syntax

phi syntax is characterized by consistency, regularity, and transparency. it follows 
a subject-object-verb (SOV) word order as its default structure, with modifiers typically 
preceding the words they modify. this head-final approach to both modification and 
complementation creates a syntax that is both predictable and flexible.

particles play a crucial role in phi syntax, serving to mark grammatical functions, 
tense, aspect, mood, and other features. this approach allows the core words (nouns, 
verbs, adjectives, etc.) to remain invariant while the particles carry grammatical 
information, similar to analytical languages like Japanese.

phi syntax is designed to minimize ambiguity by using explicit markers when needed, 
while still allowing for economy of expression when context makes relationships clear. 
this balance creates a syntax that is both precise and natural-feeling.

## basic sentence structure

the fundamental word order in phi is Subject-Object-Verb (SOV):

| phi                    | literal translation | english              |
| ---------------------- | ------------------- | -------------------- |
| thephoa nuthui phamo   | person pebble like  | the person likes the pebble |
| mia phimea phimu       | I tool use          | I use a tool         |
| thaphe lothia phuwe    | woman bed sleep     | the woman sleeps in the bed |

while the basic structure is SOV, phi allows for considerable variation based on:
1. Particle usage to clarify relationships
2. Topicalization for emphasis
3. Question formation
4. Complex sentence construction

## noun phrases

noun phrases in phi typically follow a head-final structure, with modifiers 
preceding the noun they modify:

### basic noun phrase structure

```
(determiner) (number) (classifier) (adjective) noun
```

examples of noun phrase construction:

| phi                   | composition                       | english translation     |
| --------------------- | --------------------------------- | ----------------------- |
| nuthui                | pebble                            | (a) pebble              |
| thueta nuthui         | that + pebble                     | that pebble             |
| phi teo nuthui        | one + CL.round + pebble           | one pebble              |
| pisha nuthui          | soft + pebble                     | soft pebble             |
| thueta phi teo pisha nuthui | that + one + CL.round + soft + pebble | that one soft pebble |

### possessive constructions

possession is expressed using the preposition `thue` ("of"):

| phi                   | literal translation   | english translation     |
| --------------------- | --------------------- | ----------------------- |
| nuthui thue thephoa   | pebble of person      | the person's pebble     |
| siwhea thue mia       | house of me           | my house                |
| thaphia thue thi      | hand of you           | your hand               |

### relative clauses

phi uses the particle `lu` placed at the beginning of the clause to 
distinguish relative clauses from simple sentences. this follows phi's pattern of using 
particles to mark grammatical functions and adheres to the [C][V] phonotactic pattern
for particles:

| phi                       | literal translation      | english translation       |
| ------------------------- | ------------------------ | ------------------------- |
| lu mia nuthui phemo       | REL I pebble think       | the pebble (that I) think about |
| lu mia thephoa phose      | REL I person see         | the person (whom) I see   |
| lu thephoa li phola       | REL person PST walk      | the person who walked     |

without the relative marker, "mia thephoa phose" would simply mean "I see the person" 
as a complete sentence. the relative particle clarifies that the clause is modifying
a noun.

examples in context:

| phi                            | literal translation            | english translation     |
| ------------------------------ | ------------------------------ | ----------------------- |
| lu mia thephoa phose hashe.    | REL I person see tall          | The person whom I see is tall. |
| mia lu thephoa phose phamo.    | I REL person see like          | I like the person whom I see. |
| lu thaphe raphe li phola       | REL woman path PST walk        | the woman who walked the path |

## verb phrases

verb phrases in phi contain the object and verb. the verb itself does not conjugate 
for tense, aspect, or agreement - these are expressed through particles.

### tense and aspect

tense and aspect particles precede the verb:

| phi             | composition         | english translation     |
| --------------- | ------------------- | ----------------------- |
| phola           | walk                | walk(s)                 |
| li phola        | PST + walk          | walked                  |
| su phola        | FUT + walk          | will walk               |
| la phola        | PROG + walk         | (is) walking            |
| li la phola     | PST + PROG + walk   | was walking             |
| ni phola        | PRF + walk          | has walked              |
| po phola        | HAB + walk          | usually walks           |

### negation

negation is expressed with the particle `me` placed before the verb:

| phi             | composition         | english translation     |
| --------------- | ------------------- | ----------------------- |
| me phola        | NEG + walk          | (does) not walk         |
| li me phola     | PST + NEG + walk    | did not walk            |
| su me phola     | FUT + NEG + walk    | will not walk           |

### complements

verb complements follow the object and precede the main verb:

| phi                     | literal translation    | english translation     |
| ----------------------- | ---------------------- | ----------------------- |
| mia nuthui raphe phera phemo | I pebble grey be think | I think the pebble is grey |
| mia phema phire        | I come want            | I want to come        |
| he mia li phola phare  | he I PST walk report   | He reported that I walked |

## questions

phi uses a systematic hybrid approach to questions with two distinct patterns:

### yes/no questions

yes/no questions are formed by adding the question particle `wa` at the beginning of 
any declarative statement:

| phi                   | literal translation    | english translation     |
| --------------------- | ---------------------- | ----------------------- |
| thephoa phola         | person walk            | The person walks        |
| wa thephoa phola      | Q person walk          | Does the person walk?   |
| mia nuthui phamo      | I pebble like          | I like the pebble       |
| wa mia nuthui phamo   | Q I pebble like        | Do I like the pebble?   |

### wh-questions

wh-questions use interrogative words and can be combined with other particles except `wa`, in their normal syntactic position:

| phi                   | literal translation    | english translation     |
| --------------------- | ---------------------- | ----------------------- |
| hamite thi phola      | how you walk           | How do you walk?        |
| so wulime thi phola   | POL where you walk     | Where do you go? (polite) |
| hi timane thephoa phola | DIR.EV when person walk | When does the person walk? (I see) |
| ro whieso nuthui thi phamo | INFR which pebble you like | Which pebble do you like? (I infer) |

this systematic distinction keeps each question type clean and predictable, 
while allowing wh-questions to be modified by politeness, evidentiality, and other 
non-interrogative particles. the `wa` particle cannot be combined with wh-questions 
as they represent different question systems.

## complex sentences

complex sentences are formed using conjunctions to connect clauses:

### coordination

coordinating conjunctions connect elements of equal syntactic status:

| phi                           | literal translation       | english translation     |
| ----------------------------- | ------------------------- | ----------------------- |
| thephoa phola nene thaphe phuwe | person walk and woman sleep | The person walks and the woman sleeps |
| mia mipho phamo tupo tupha me phamo | I blue like but purple NEG like | I like blue but I don't like purple |

### subordination

subordinating conjunctions create dependent relationships between clauses:

| phi                           | literal translation       | english translation     |
| ----------------------------- | ------------------------- | ----------------------- |
| mia wheisha phera wetu phola  | I water be if walk        | I walk if there is water |
| thaphe waphi phera renu phuwe | woman tired be because sleep | The woman sleeps because she is tired |
| mia thi phema lina phola      | I you come until walk     | I walk until you come   |

## particle ordering

when multiple particles are used, they follow a strict order based on their scope and category:

1. **Sentence particles** (sentence mood/type > evidentiality > politeness)
   - Example: `tu so mia ta phuwa` (if politely I do throw)
   - Includes: `wa` (question), `lu` (relative), `tu` (conditional), `so` (politeness)

2. **Verb phrase particles** (tense > aspect > negation)
   - Example: `li ni me phuwa` (did not throw [completed action])
   - Includes: `li` (past), `su` (future), `la` (progressive), `ni` (perfective), `me` (negation)

3. **Core word particles** (pos marker > animacy > emphasis > plural)
   - Example: `si he ma lo raushai` (the *leaders* [subject, human, emphatic, plural])
   - Includes: `si` (subject), `na` (object), `he` (human), `ma` (emphasis), `lo` (plural)

## topicalization and emphasis

topics can be fronted for emphasis:

| phi                     | literal translation     | english translation     |
| ----------------------- | ----------------------- | ----------------------- |
| nuthui mia phamo       | pebble I like          | As for the pebble, I like it |
| ma nuthui mia phamo     | EMPH pebble I like      | It's the *pebble* that I like |
| nuthui na mia ma phamo  | pebble OBJ I EMPH like  | The pebble, I *really* like |

## syntactic differences from english

phi syntax differs from english in several key ways:

1. SOV word order rather than SVO: `mia nuthui phamo` (I pebble like) = "I like the pebble"
2. No copula required for adjectives: `nuthui pisha` (pebble soft) = "The pebble is soft"
3. No articles required: `thephoa` can mean "a person," "the person," or simply "person"
4. No verb conjugation for person/number: `phola` means "walk(s)" regardless of subject
5. Particles rather than word order changes for questions: `wa` + statement = question
6. No passive voice transformation: active voice is used throughout
7. No infinitive marker: verb phrases are simply juxtaposed

## example texts

the following examples demonstrate phi syntax in context:

### simple conversation

**mia:**  
mimia. hamite thi.  
hello how you  
"Hello! How are you?"  

**thi:**  
wanume. hamite thi.  
well how you  
"Well. How are you?"  

**mia:**  
mia ritune luphi.  
I very happy  
"I am very happy."  

**mia:**  
welime thi sharo phira.  
where you go want  
"Where do you want to go?"  

**thi:**  
mia siwhea na sharo phira.  
I house OBJ go want  
"I want to go home."  

**mia:**  
mia thi phiu sharo su.  
I you with go FUT  
"I will go with you."  

**thi:**  
teshe. lo mia sharo.  
good HORT we go  
"Good! Let's go!"

## syntax development notes

phi syntax is designed to be learnable and logical while still allowing for natural
expression. the syntax prioritizes regularity over idiomaticity, meaning that grammatical
patterns are consistent even when they might differ from common natural language patterns.

future development of phi syntax should maintain these principles of regularity,
clarity, and semantic transparency, while expanding to accommodate more complex
expressions and specialized domains as needed. 