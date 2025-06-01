# semantics

> semantics refers to the study of meaning in language, encompassing how words, phrases, and sentences convey meaning, how meanings are composed systematically from component parts, and how meaning relates to truth conditions, reference, and conceptual representation across different linguistic and cultural contexts.

## introduction to phi semantics

phi implements a **systematic compositional transparency principle** that transforms traditional semantic challenges into explicit grammatical solutions. unlike natural languages where meaning often depends on contextual inference, idiomatic complexity, or covert semantic operations, phi employs principled explicit encoding mechanisms that make meaning construction transparent and systematically predictable.

this systematic approach represents a fundamental departure from conventional semantic organization, where phi achieves conceptual clarity through grammatical explicitness rather than inferential dependency, creating a semantic system optimized for logical precision and cross-linguistic accessibility.

## systematic semantic architecture

### lexical meaning transparency
phi's phonotactically distinct word classes ensure that the basic semantic domain of a word (e.g., entity, process, property, relation) is evident from its form, providing an initial layer of semantic clarity before specific lexical meaning is accessed.

### particle-based compositional system
phi uses systematic particles to explicitly mark semantic relationships, ensuring compositional transparency:

- **temporal relations**: `li` (past), `ta` (present), `su` (future) particles explicitly define the temporal frame of events and states.
- **aspectual distinctions**: `ni` (perfective) and `ri` (imperfective) particles clearly delineate the internal temporal structure of situations.
- **modal meanings**: particles like `ra` (necessity), `se` (possibility), `we` (ability), `wo` (prohibition), and `lu` (conditional) explicitly encode modal concepts.
- **spatial relations**: prepositions (e.g., `phia` - in, `wheo` - at, `shio` - from) systematically define locative and directional relationships.
- **logical connections**: conjunctions (e.g., `nene` - and, `woma` - or, `matu` - after) explicitly mark the logical relationships between clauses and phrases.
- **quantificational scope**: particles and determiners (e.g., `shoata` - all, `sheapa` - some, `lo` - plural) clearly define the scope and quantity of nominal referents.

### syntactic-semantic interface
phi's SOV (subject-object-verb) word order and phonotactic cues for grammatical categories create a predictable framework for semantic interpretation. the consistent placement of arguments before the verb, combined with explicit particle marking, clarifies semantic roles (agent, patient, theme, etc.) and predicate-argument structures.

## semantic relationship encoding
phi addresses core lexical semantic relationships through its design:

- **synonymy**: achieved through distinct lexical items that share core conceptual features, with subtle differences often tied to specific phonotactic nuances within a word class if desired, or through pragmatic context.
- **antonymy**: expressed by separate lexical items with opposing core meanings (e.g., `tophe` - big, `sesu` - small [hypothetical]).
- **hyponymy/hypernymy**: managed through lexical specificity; a general term (hypernym) and more specific terms (hyponyms) are distinct nouns.
- **meronymy**: part-whole relationships are expressed through possessive constructions or specific relational nouns if needed.

## truth-conditional semantics in phi
the explicitness of phi's grammatical and particle system leads to relatively straightforward truth-conditional analysis. the meaning of a sentence can be systematically derived from the meanings of its words and the semantic functions of the particles and grammatical structures involved.

- **declarative sentences**: their truth depends on whether the state of affairs described by the predicate holds true for the specified arguments in the given temporal and modal context.
- **negation**: the particle `me` reverses the truth value of the proposition it modifies.
- **quantification**: determiners and number marking clearly specify the domain over which a predication must hold true.

## ambiguity resolution
phi's design principles aim to minimize semantic ambiguity:

- **lexical ambiguity**: reduced because each word has a unique phonotactic template tied to a specific grammatical (and thus broad semantic) category. while homophony between different parts of speech is impossible, homophony within a part of speech is possible but minimized.
- **structural (syntactic) ambiguity**: mitigated by strict SOV word order and the explicit marking of semantic roles and relationships through particles. scope ambiguities are generally resolved by particle placement.
- **scope ambiguity**: typically resolved by the fixed positions of quantifiers, modals, and negation particles relative to the elements they modify.

## usage examples

### basic semantic composition
```
mia li na whethea phose
i past OBJ book see
"i saw the book"
(composition: past(see(i, book)))
```

### modal and temporal interaction
```
sha su ra whethea phina
it/he/she future NEC book find
"s/he will have to find the book"
(composition: future(must(find(s/he, book))))
```

### quantification and negation
```
lo thephoa me na whethea phose
PL person NEG OBJ book see
"people do not see the book" / "no people see the book"
(composition: not(see(people, book)) or for-all(x) if person(x) then not(see(x,book)))
```

### complex semantic relationships (hypothetical)
```
wetu mia whera matu mia thophu
if i learn after i understand
"if i learn, then i understand" (lit: if i learn, after i understand)
```

## conclusion

phi semantics is characterized by its directness and transparency, achieved through a unique synergy of phonotactically distinct word classes and an explicit particle system. this design ensures that the meaning of complex expressions is systematically derivable from the meanings of individual words and the clear semantic functions of grammatical markers. by minimizing reliance on contextual inference for core semantic relations, phi offers a robust framework for precise conceptual representation and logical consistency.