# Content vocabulary decisions

This is the readable view of `project/content_vocabulary_decisions.json`. It records every candidate carried forward from the content-vocabulary migration and retrospective audit, including decisions to compose, defer, or keep exact source terminology. The broader coverage ledger retains settled comparisons from each batch. Regenerate this view with `python3 scripts/content_vocabulary_decisions.py --write`; CI checks that the register, the ledger, and the vocabulary remain in step.

The register is a memory aid, not proof that Phi has no other gaps. An unnoticed concept cannot appear in any inventory. From this repair onward, every potential coinage noticed during a content batch receives an ID here; it stays until it has an explicit decision, and an open or accepted candidate keeps its batch open.

## Decision statuses

| Status | Meaning |
|---|---|
| Open | The lexical question still needs a decision. |
| Accepted, not implemented | The decision is made, but its vocabulary or documentation has not landed. |
| Implemented | The accepted word or registered compound exists and is checked. |
| Compositional | Phi deliberately uses existing words or grammar for the concept. |
| Deferred | The question has a named trigger for returning to it. |
| Source-bound | Exact identity or authority stays with outside source terminology while Phi describes the surrounding relations. |
| Declined | Phi deliberately does not add the proposed distinction. |

## Batch state

| Batch | Prose migration | Lexical decisions | Candidate count |
|---|---|---|---:|
| [Core material qualities](#core-material-qualities) | complete | closed | 6 |
| [Environmental and spatial qualities](#environmental-and-spatial-qualities) | complete | closed | 1 |
| [Size, extent, and distance](#size-extent-and-distance) | complete | closed | 4 |
| [Pace, motion, and equilibrium](#pace-motion-and-equilibrium) | complete | closed | 0 |
| [Color](#color) | complete | closed | 0 |
| [Strength, deformation, and recovery](#strength-deformation-and-recovery) | complete | closed | 0 |
| [Sensory and perceptual qualities](#sensory-and-perceptual-qualities) | complete | closed | 2 |
| [Aesthetic and formal qualities](#aesthetic-and-formal-qualities) | complete | open | 5 |
| [Awareness and epistemic qualities](#awareness-and-epistemic-qualities) | complete | closed | 0 |
| [Ethics, care, and candour](#ethics-care-and-candour) | complete | closed | 2 |
| [Core emotion inventory](#core-emotion-inventory) | complete | open | 1 |
| [Affective response, anticipation, and resolve](#affective-response-anticipation-and-resolve) | complete | open | 2 |
| [Social relation, standing, and personal boundaries](#social-relation-standing-and-personal-boundaries) | complete | closed | 0 |
| [Life, age, and bodily condition](#life-age-and-bodily-condition) | complete | closed | 0 |
| [Cultivation, abundance, and wildness](#cultivation-abundance-and-wildness) | complete | open | 3 |
| [Structure, identity, and fit](#structure-identity-and-fit) | complete | closed | 0 |
| [Imagination, unfamiliarity, wonder, and reverence](#imagination-unfamiliarity-wonder-and-reverence) | complete | closed | 0 |
| [Practical readiness, care, and effort](#practical-readiness-care-and-effort) | complete | closed | 0 |
| [Access, perception, and independent participation](#access-perception-and-independent-participation) | complete | closed | 1 |
| [System fit, equivalence, and dependable performance](#system-fit-equivalence-and-dependable-performance) | complete | closed | 1 |
| [Work timing, status, capability, and answerability](#work-timing-status-capability-and-answerability) | complete | closed | 1 |
| [Medical course, transmission, and treatment response](#medical-course-transmission-and-treatment-response) | complete | closed | 1 |
| [Core speech and conversation](#core-speech-and-conversation) | complete | open | 1 |
| [Knowledge, understanding, belief, and memory](#knowledge-understanding-belief-and-memory) | complete | open | 2 |
| [Attention, observation, reflection, and imagination](#attention-observation-reflection-and-imagination) | complete | closed | 2 |
| [Desire, intention, choice, and commitment](#desire-intention-choice-and-commitment) | complete | closed | 0 |
| [Agreement, consent, refusal, and pressure](#agreement-consent-refusal-and-pressure) | complete | closed | 1 |
| [Participation, cooperation, contribution, and mutual aid](#participation-cooperation-contribution-and-mutual-aid) | complete | closed | 0 |
| [Giving, receiving, keeping, and circulation](#giving-receiving-keeping-and-circulation) | complete | open | 1 |
| [Basic motion, endpoints, and staying](#basic-motion-endpoints-and-staying) | complete | closed | 0 |
| [Manner, trajectory, and extended movement](#manner-trajectory-and-extended-movement) | complete | closed | 0 |
| [Posture, rest, waiting, and residence](#posture-rest-waiting-and-residence) | complete | closed | 0 |
| [Breath, intake, and expulsion](#breath-intake-and-expulsion) | complete | closed | 3 |
| [Contact, force, and placement](#contact-force-and-placement) | complete | open | 3 |
| [Material change, making, and joining](#material-change-making-and-joining) | complete | closed | 3 |
| [Change, continuity, repair, and renewal](#change-continuity-repair-and-renewal) | complete | closed | 2 |
| [Life, growth, cultivation, and flourishing](#life-growth-cultivation-and-flourishing) | complete | closed | 4 |
| [Care, affection, regard, and relational repair](#care-affection-regard-and-relational-repair) | complete | closed | 0 |
| [Learning, practice, guidance, and sustained effort](#learning-practice-guidance-and-sustained-effort) | complete | closed | 2 |
| [Measurement, comparison, meaning, and record](#measurement-comparison-meaning-and-record) | complete | open | 2 |
| [Ritual, play, and expressive response](#ritual-play-and-expressive-response) | complete | open | 3 |
| [Relation, boundaries, and remaining practical acts](#relation-boundaries-and-remaining-practical-acts) | complete | open | 1 |
| [Personhood, generations, kinship, and social belonging](#personhood-generations-kinship-and-social-belonging) | complete | open | 1 |
| [Body, anatomy, and bodily condition](#body-anatomy-and-bodily-condition) | complete | closed | 10 |
| [Recovered cross-inventory prompts](#recovered-cross-inventory-prompts) | not-started | open | 29 |

## Core material qualities

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-MAT-01` | hollow interior structure | Compositional | base expression | `whemoa muwi`. An empty interior says what is hollow without treating every empty vessel or room as a material structure. |
| `CV-MAT-02` | absorption of liquid or other material | Implemented | base | Words: `wosanu`. The verb puts the receiving body in subject position and distinguishes material taken within from liquid merely present on a surface or moving through. |
| `CV-MAT-03` | porous interior structure | Deferred | base or a material-focused module | When connected material practice repeatedly needs porosity itself rather than permeability to a named substance. Many small empty interiors can describe the visible arrangement, while a dedicated quality may become useful in soil, textile, building, or filter work. |
| `CV-MAT-04` | dense packing or scientific density | Deferred | base, Systems, Ecological, or exact source material | When connected material or scientific writing repeatedly needs one stable relation that existing thickness, concentration, packing, and source measurements cannot express cleanly. Everyday uses divide among thick body, rich concentration, and many things in little space; scientific density adds a defined magnitude and method. |
| `CV-MAT-05` | permeability to a named substance | Compositional | base clause, with exact technical criteria in source material | `phialu thue muralo po roke`. Permeability depends on what passes, under which conditions, so the ordinary clause names the substance, material, and possible passage. |
| `CV-MAT-06` | waterproofness | Compositional | base clause, with exact ratings in source material | `phialu muo muralo po ma koema`. A clause saying that water cannot enter or pass through leaves the claimed substance and practical condition visible. |

## Environmental and spatial qualities

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-MEAS-01` | temperature, humidity, and illumination as measured parameters | Deferred | Systems or Ecological, with exact values in source material | When a connected technical scenario repeatedly names the measured parameter apart from its value and instrument. Everyday quality words already cover hot, wet, and bright; technical work may still need neutral parameter nouns. |

## Size, extent, and distance

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-MEAS-02` | area as a neutral magnitude | Compositional | base expression | `leko ponalu`, `lokue ponalu`. The measured kind can name the relevant surface or place before `ponalu` supplies its size, while exact values stay in source material. |
| `CV-MEAS-03` | volume as occupied spatial magnitude | Compositional | base expression | `ponalu`, `tholu ponalu`. Overall size already handles ordinary occupied extent, and the size of a space can be named directly without confusing it with a container's technical capacity. |
| `CV-MEAS-04` | weight as a neutral physical magnitude | Implemented | base | Words: `pamolu`. The noun lets speakers compare or measure physical weight before judging an object heavy or light and without borrowing burden or technical load. |
| `CV-MEAS-05` | mass as a scientific magnitude distinct from weight | Deferred | Systems or exact source material | When connected scientific or engineering writing repeatedly needs to discuss mass apart from weight and exact source notation. Ordinary handling now has neutral weight, while scientific mass requires a stable technical distinction, method, and source value. |

## Pace, motion, and equilibrium

No lexical question from this batch remains outside an explicit coverage decision.

## Color

No lexical question from this batch remains outside an explicit coverage decision.

## Strength, deformation, and recovery

No lexical question from this batch remains outside an explicit coverage decision.

## Sensory and perceptual qualities

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-TASTE-01` | scientific basic-taste categories | Deferred | culinary or Medical use, with exact taxonomies source-bound | When connected culinary or medical writing repeatedly needs a stable taste distinction beyond source description. Ordinary flavours can use source nouns and response clauses without pretending that one scientific inventory is universal. |
| `CV-SENS-01` | itch, numbness, tingling, and dizziness | Implemented | base | Words: `sikoru`, `numaro`, `tiphori`, `wiloru`. A person can name four familiar sensations before anyone adds a broader bodily condition or clinical conclusion. |

## Aesthetic and formal qualities

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-AEST-01` | decorate or add applied ornament | Implemented | base | Words: `weshapi`. The verb names the addition of visible ornament and keeps design as a separate act. |
| `CV-AEST-02` | symmetry and asymmetry | Deferred | base, Work, or exact technical description | When a connected design, craft, or technical scenario repeats the relation often enough that comparison clauses become cumbersome. Ordinary clauses can compare corresponding parts, but design or technical work may need symmetry as a recurring property. |
| `CV-AEST-03` | style and characteristic aesthetic form | Open | base, Work, or art vocabulary | Does Phi want a general word for style, or should each aesthetic tradition be described by the forms that make it recognisable? Art, design, pattern, shape, and beauty do not quite name the recognisable manner shared across several works. |
| `CV-SHAPE-01` | straight as an ordinary shape quality | Implemented | base | Words: `tekari`. The adjective separates an uncurved course or extended form from a direct route or steady movement. |
| `CV-SHAPE-02` | round as an ordinary shape quality | Compositional | base expression | `sorui kire`. The existing circle noun already describes a circular form through the ordinary noun-describes rule, and active text has used the expression naturally. |

## Awareness and epistemic qualities

No lexical question from this batch remains outside an explicit coverage decision.

## Ethics, care, and candour

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-ETH-01` | cruel conduct and cruelty | Implemented | base | Words: `lerasu`. The adjective judges knowingly or callously caused avoidable suffering without declaring a permanent kind of person. |
| `CV-CONFLICT-01` | generic conflict and direct roots for violence, fighting, attack, defence, hunting, and killing | Declined | no lexical placement | Do not coin these roots in base vocabulary or a module. Describe mechanisms and effects with established Phi words, and preserve exact violent terminology beside Phi when faithful source wording is required. Phi refuses to make violent acts and roles ordinary vocabulary while retaining direct ways to name danger, harm, injury, coercion, protection, testimony, responsibility, redress, and repair. |

## Core emotion inventory

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-AFFECT-02` | guilt, anxiety, disgust, excitement, relief, frustration, and boredom | Open | base or later affective vocabulary | For each state, what felt structure matters in Phi, and does a root or an established composition express it more honestly? The core lesson is not the whole affective lexicon, and several layered states may deserve direct words or settled compositions. |

## Affective response, anticipation, and resolve

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-AFFECT-01` | sustained interest or engagement | Implemented | base | Words: `mewali`. The adjective keeps interest apart from curiosity and directed attention. |
| `CV-AFFECT-02` | guilt, anxiety, disgust, excitement, relief, frustration, and boredom | Open | base or later affective vocabulary | See the complete decision under [Core emotion inventory](#core-emotion-inventory). |

## Social relation, standing, and personal boundaries

No lexical question from this batch remains outside an explicit coverage decision.

## Life, age, and bodily condition

No lexical question from this batch remains outside an explicit coverage decision.

## Cultivation, abundance, and wildness

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-CLEAN-01` | dirty, contaminated, spoiled, and rotten | Open | base, Household, Ecological, or Medical | Which everyday conditions need direct words, while exact contamination and sanitation thresholds remain source-bound? Ordinary cleanliness, visible dirt, spoilage, contamination, and decay make different claims and should not be collapsed into one moral adjective. |
| `CV-FOOD-01` | rice and tea | Open | base or Household | Does Phi want stable general words for the foods and drinks, with exact varieties left to source names? These culturally widespread staples may deserve ordinary roots, though neither is a semantic universal Phi must copy from English. |
| `CV-FOOD-02` | nut | Compositional | base compound | `kerou lureko`. The registered compound names a fruit by its hard stone-like shell and is already used in an active text. |

## Structure, identity, and fit

No lexical question from this batch remains outside an explicit coverage decision.

## Imagination, unfamiliarity, wonder, and reverence

No lexical question from this batch remains outside an explicit coverage decision.

## Practical readiness, care, and effort

No lexical question from this batch remains outside an explicit coverage decision.

## Access, perception, and independent participation

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-ACCESS-01` | legal or certified accessibility | Source-bound | Accessibility plus exact source material | Keep the standard, measurement, decision, and legal category in their exact source form; use Phi for the access conditions and effects around them. Phi can describe the practical access relation but cannot silently inherit a jurisdiction's legal test. |

## System fit, equivalence, and dependable performance

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-SYS-01` | standards conformance, protocol support, and certified performance | Source-bound | Systems plus exact source material | Preserve the exact standard, protocol, version, result, or certificate and describe its practical system relation in Phi. A practical Phi quality cannot replace the version, test method, evidence, or issuing authority. |

## Work timing, status, capability, and answerability

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-WORK-01` | occupation titles, credentials, licences, and legal liability | Source-bound | Work or Commons plus exact source material | Keep the exact title, credential, issuer, scope, validity, or legal rule beside the Phi account of work, qualification, authority, or answerability. These categories draw their force from a named institution or legal order. |

## Medical course, transmission, and treatment response

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-MED-01` | indicated care and exact contraindication classes | Source-bound | Medical plus exact source material | Keep the exact recommendation or classification with its source and criteria; use Phi to state expected benefit, alternatives, reasons, and the person's decision. A general inverse of contraindicated would hide the source, strength, and grounds of a clinical recommendation. |

## Core speech and conversation

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-MEET-01` | meet as a verb | Open | base | Does the event noun already work naturally as a verb-like predicate through existing grammar, or does meeting another person deserve a direct verb? Phi has `lona` (meeting), arrival, presence, and togetherness, but the survey left the ordinary encounter verb undecided. |

## Knowledge, understanding, belief, and memory

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-COG-01` | amnesia, dementia, impairment, and exact cognitive assessment | Source-bound | Medical plus exact source material | Preserve the diagnosis, test, classification, and source; use Phi to describe the person's reported experience and observed abilities without replacing those records. Ordinary memory and understanding words cannot carry a diagnosis or test result by themselves. |
| `CV-LOSE-01` | lose and misplace a thing | Open | base | Should Phi coin one neutral verb for losing possession or location, and does deliberate abandonment need a different clause? Forgetting, releasing, lacking, and failing to find something do not by themselves report that a previously held thing is now missing. |

## Attention, observation, reflection, and imagination

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-MEDIT-01` | named meditation traditions, methods, and lineages | Source-bound | base practice vocabulary plus exact source names | Retain the tradition, method, teacher, or lineage name in its source form and use Phi to describe the practice being undertaken. One broad Phi meditation verb does not erase the histories and methods of named traditions. |
| `CV-AFFECT-01` | sustained interest or engagement | Implemented | base | See the complete decision under [Affective response, anticipation, and resolve](#affective-response-anticipation-and-resolve). |

## Desire, intention, choice, and commitment

No lexical question from this batch remains outside an explicit coverage decision.

## Agreement, consent, refusal, and pressure

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-RETRACT-01` | neutral retraction of a claim or proposal | Implemented | base | Words: `nosheku`. Retraction changes the speaker's present commitment while leaving the earlier words in the record. |

## Participation, cooperation, contribution, and mutual aid

No lexical question from this batch remains outside an explicit coverage decision.

## Giving, receiving, keeping, and circulation

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-LOSE-01` | lose and misplace a thing | Open | base | See the complete decision under [Knowledge, understanding, belief, and memory](#knowledge-understanding-belief-and-memory). |

## Basic motion, endpoints, and staying

No lexical question from this batch remains outside an explicit coverage decision.

## Manner, trajectory, and extended movement

No lexical question from this batch remains outside an explicit coverage decision.

## Posture, rest, waiting, and residence

No lexical question from this batch remains outside an explicit coverage decision.

## Breath, intake, and expulsion

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-NAUSEA-01` | nausea | Implemented | base | Words: `muthari`. The noun names a felt possibility of vomiting rather than sickness as a whole or the event of vomiting. |
| `CV-BREATH-01` | sneezing, hiccups, and belching | Implemented | base | Words: `nishoku`, `ketumi`, `rumeka`. Three ordinary verbs distinguish a sneeze's nasal burst, a hiccup's caught breath, and gas released in a belch. |
| `CV-INTAKE-01` | lick and suck | Implemented | base | Words: `lisaku`, `pumari`. One verb follows the tongue across a surface; the other follows inward pressure made by the mouth. |

## Contact, force, and placement

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-HIT-01` | brief physical impact | Implemented | base | Words: `patore`. The verb reports impact before the sentence decides intent, injury, or damage. |
| `CV-HIT-02` | peace-linguistic scope and retention of patore | Open | base or retired vocabulary | Do the nonviolent impact uses justify a general root with that broader reach, or should patore be narrowed or retired? The current root supports accidental impact, tool contact, and applause, but its unmarked scope also permits deliberate interpersonal hitting. |
| `CV-AIM-01` | physical alignment towards a selected point or object | Open | Work or a transparent construction | Does craft or measurement need a distinct physical-alignment relation, or do direction, orientation, and purpose already cover the legitimate uses? Direction and intention approach this relation without importing the combat-shaped English extensions of aim and target. |

## Material change, making, and joining

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-PUNCTURE-01` | puncture or make an opening with a point | Implemented | base | Words: `tisharu`. The verb separates a point-made hole from edge-driven cutting, digging, and sewing. |
| `CV-DISSOLVE-01` | dissolve through a medium | Implemented | base | Words: `wilanu`. The verb names dispersion through a medium without treating dissolution as mixing, melting, or disappearance. |
| `CV-TEXT-01` | English-shaped material metaphors in active texts | Deferred | text review rather than new vocabulary by default | When the planned active-text vocabulary review reaches each cited passage. Breaking into talk, digging into books, heavy trouble, and similar phrases need judgement as Phi images rather than silent definition changes. |

## Change, continuity, repair, and renewal

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-DISSOLVE-01` | dissolve through a medium | Implemented | base | See the complete decision under [Material change, making, and joining](#material-change-making-and-joining). |
| `CV-SWELL-01` | swell and shrink | Implemented | base | Words: `murase`, `kesiri`. Two deliberately distant forms cover opposite changes in bodily or material extent, with cause and diagnosis left to the surrounding account. |

## Life, growth, cultivation, and flourishing

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-WITHER-01` | wither or wilt | Implemented | base | Words: `kureno`. The verb names visible loss of turgor before dryness or death has necessarily occurred. |
| `CV-REPRO-01` | biological reproduction and deliberate breeding | Deferred | base, Ecological, or a reproductive-health vocabulary set | When ecological, husbandry, reproductive-health, or kinship scenarios need these relations in connected use. Fertility names capacity and birth names an event; reproduction and selective breeding introduce other relations. |
| `CV-CULT-01` | pollination, pruning, weeding, and fertilising | Deferred | Ecological, Household, or Work | When a garden, farm, orchard, or ecological-care scenario uses the acts often enough to decide their learning value. Existing verbs can describe what moves, is cut, is removed, or is supplied, while repeated specialist use may favour direct words. |
| `CV-SWELL-01` | swell and shrink | Implemented | base | See the complete decision under [Change, continuity, repair, and renewal](#change-continuity-repair-and-renewal). |

## Care, affection, regard, and relational repair

No lexical question from this batch remains outside an explicit coverage decision.

## Learning, practice, guidance, and sustained effort

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-TRY-01` | try or attempt an action | Implemented | base | Words: `mesatu`. The verb reports an action undertaken without claiming completion, persistence, or success. |
| `CV-EDU-01` | courses, curricula, schools, grades, and educational standing | Deferred | a possible Learning and Knowledge Practice module plus exact source material | When the Learning and Knowledge Practice profile receives connected scenarios or the book needs recurring institutional education vocabulary. A lesson composes readily, while institutional categories depend on their programme and issuer. |

## Measurement, comparison, meaning, and record

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-SEARCH-01` | search or seek | Implemented | base | Words: `sheraki`. The verb names sustained action towards finding something without claiming that the search succeeds. |
| `CV-WRITE-01` | page, ink, letter, and message | Open | base or a writing-practice vocabulary set | Which concepts deserve roots in a language with journal and literary practices, and which stay transparent parts, materials, or acts? Phi has writing, reading, books, telling, records, and messengers, but these ordinary objects were never decided. |

## Ritual, play, and expressive response

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-HIT-01` | brief physical impact | Implemented | base | See the complete decision under [Contact, force, and placement](#contact-force-and-placement). |
| `CV-HIT-02` | peace-linguistic scope and retention of patore | Open | base or retired vocabulary | See the complete decision under [Contact, force, and placement](#contact-force-and-placement). |
| `CV-APPLAUSE-01` | applause | Compositional | base expression | `manuwe patore`, `woraka`, `pharuki`, `nomela`. Repeated hand impacts name the physical act; appreciation, celebration, or encouragement states what the act is doing in that gathering. |

## Relation, boundaries, and remaining practical acts

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-COVER-01` | cover and uncover | Open | base or Household | Does one neutral cover verb earn a base root, with uncover as removal or reversal, or are the purposes different enough to keep explicit? Closing, hiding, protecting, wrapping, and placing something over a surface describe nearby acts but may not cover the ordinary physical relation cleanly. |

## Personhood, generations, kinship, and social belonging

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-ANIMAL-01` | bee, wolf, deer, bear, frog, spider, cow, and goat | Open | base or Ecological | Which animals does Phi want as direct roots now, independent of whether a particular source text has forced the issue? The animal inventory is broad but sparse for fables, husbandry, pollination, and ordinary ecological writing. |

## Body, anatomy, and bodily condition

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-BODY-01` | joint, elbow, wrist, ankle, hip, toe, eyelid, and nostril | Implemented | base roots and registered compounds | Words: `kiparu`, `lushe`. Compounds: `paloi thumai`, `mirae hisae`, `nophae phae`, `pelio kesho kiparu`, `manuwe kiparu`, `paloi kiparu`. A general body-joint noun supports the smaller landmarks, while hip keeps a direct regional word and the transparent subdivisions remain visible. |
| `CV-BODY-02` | brain | Implemented | base | Words: `meraku`. The organ now has its own noun without turning head, mind, memory, and thought into synonyms. |
| `CV-BODY-03` | throat | Implemented | base | Words: `shapelu`. The ordinary internal region is now distinct from the external neck and from exact clinical structures. |
| `CV-BODY-04` | lip, jaw, cheek, and forehead | Implemented | base | Words: `phimei`, `kathoru`, `meshoi`, `komeri`. Four common landmarks now support speech, eating, expression, touch, pain, and care without fresh descriptive puzzles. |
| `CV-BODY-05` | waist, pelvis, and buttocks | Implemented | base | Words: `norapi`, `kanomi`, `peshuma`. The lower torso now has ordinary regional nouns for clothing, posture, gait, pain, and non-contact care. |
| `CV-BODY-06` | saliva, urine, and faeces | Implemented | base | Words: `suhari`, `tomewu`, `mokathi`. Daily care, sanitation, childhood, and illness can now name these substances without euphemism or a medical module. |
| `CV-BODY-07` | mucus, body fat, and flesh | Implemented | base | Words: `nuwesu`, `lomeki`, `mashuri`. Mucus and fat keep their precise substance nouns. Flesh gathers the body's soft material into an ordinary whole without becoming one tissue or a food category. |
| `CV-BODY-08` | sexual and reproductive anatomy | Deferred | base and Medical, decided by ordinary autonomy and care needs | When a dedicated scenario set tests self-description, consent, sexual health, reproduction, pain, and care across varied bodies. This field must name bodies without treating one anatomy as the default or requiring a diagnosis before a body part can be spoken. |
| `CV-BODY-09` | named bones, vessels, nerves, glands, and exact anatomical classifications | Deferred | Medical plus exact biomedical source material | When a care, study, or public-health scenario repeatedly needs one structure beyond ordinary body-region language. Base vocabulary need not reproduce an atlas, but recurring care or study may reveal specialist words worth learning. |
| `CV-SENS-01` | itch, numbness, tingling, and dizziness | Implemented | base | See the complete decision under [Sensory and perceptual qualities](#sensory-and-perceptual-qualities). |

## Recovered cross-inventory prompts

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-MAT-02` | absorption of liquid or other material | Implemented | base | See the complete decision under [Core material qualities](#core-material-qualities). |
| `CV-MAT-05` | permeability to a named substance | Compositional | base clause, with exact technical criteria in source material | See the complete decision under [Core material qualities](#core-material-qualities). |
| `CV-MAT-06` | waterproofness | Compositional | base clause, with exact ratings in source material | See the complete decision under [Core material qualities](#core-material-qualities). |
| `CV-MEAS-02` | area as a neutral magnitude | Compositional | base expression | See the complete decision under [Size, extent, and distance](#size-extent-and-distance). |
| `CV-MEAS-03` | volume as occupied spatial magnitude | Compositional | base expression | See the complete decision under [Size, extent, and distance](#size-extent-and-distance). |
| `CV-MEAS-04` | weight as a neutral physical magnitude | Implemented | base | See the complete decision under [Size, extent, and distance](#size-extent-and-distance). |
| `CV-MEAS-05` | mass as a scientific magnitude distinct from weight | Deferred | Systems or exact source material | See the complete decision under [Size, extent, and distance](#size-extent-and-distance). |
| `CV-SENS-01` | itch, numbness, tingling, and dizziness | Implemented | base | See the complete decision under [Sensory and perceptual qualities](#sensory-and-perceptual-qualities). |
| `CV-AEST-03` | style and characteristic aesthetic form | Open | base, Work, or art vocabulary | See the complete decision under [Aesthetic and formal qualities](#aesthetic-and-formal-qualities). |
| `CV-SHAPE-01` | straight as an ordinary shape quality | Implemented | base | See the complete decision under [Aesthetic and formal qualities](#aesthetic-and-formal-qualities). |
| `CV-SHAPE-02` | round as an ordinary shape quality | Compositional | base expression | See the complete decision under [Aesthetic and formal qualities](#aesthetic-and-formal-qualities). |
| `CV-CONFLICT-01` | generic conflict and direct roots for violence, fighting, attack, defence, hunting, and killing | Declined | no lexical placement | See the complete decision under [Ethics, care, and candour](#ethics-care-and-candour). |
| `CV-AFFECT-02` | guilt, anxiety, disgust, excitement, relief, frustration, and boredom | Open | base or later affective vocabulary | See the complete decision under [Core emotion inventory](#core-emotion-inventory). |
| `CV-CLEAN-01` | dirty, contaminated, spoiled, and rotten | Open | base, Household, Ecological, or Medical | See the complete decision under [Cultivation, abundance, and wildness](#cultivation-abundance-and-wildness). |
| `CV-LOSE-01` | lose and misplace a thing | Open | base | See the complete decision under [Knowledge, understanding, belief, and memory](#knowledge-understanding-belief-and-memory). |
| `CV-INTAKE-01` | lick and suck | Implemented | base | See the complete decision under [Breath, intake, and expulsion](#breath-intake-and-expulsion). |
| `CV-AIM-01` | physical alignment towards a selected point or object | Open | Work or a transparent construction | See the complete decision under [Contact, force, and placement](#contact-force-and-placement). |
| `CV-SWELL-01` | swell and shrink | Implemented | base | See the complete decision under [Change, continuity, repair, and renewal](#change-continuity-repair-and-renewal). |
| `CV-COVER-01` | cover and uncover | Open | base or Household | See the complete decision under [Relation, boundaries, and remaining practical acts](#relation-boundaries-and-remaining-practical-acts). |
| `CV-BODY-07` | mucus, body fat, and flesh | Implemented | base | See the complete decision under [Body, anatomy, and bodily condition](#body-anatomy-and-bodily-condition). |
| `CV-ANIMAL-01` | bee, wolf, deer, bear, frog, spider, cow, and goat | Open | base or Ecological | See the complete decision under [Personhood, generations, kinship, and social belonging](#personhood-generations-kinship-and-social-belonging). |
| `CV-WRITE-01` | page, ink, letter, and message | Open | base or a writing-practice vocabulary set | See the complete decision under [Measurement, comparison, meaning, and record](#measurement-comparison-meaning-and-record). |
| `CV-FOOD-01` | rice and tea | Open | base or Household | See the complete decision under [Cultivation, abundance, and wildness](#cultivation-abundance-and-wildness). |
| `CV-FOOD-02` | nut | Compositional | base compound | See the complete decision under [Cultivation, abundance, and wildness](#cultivation-abundance-and-wildness). |
| `CV-MEET-01` | meet as a verb | Open | base | See the complete decision under [Core speech and conversation](#core-speech-and-conversation). |
| `CV-PHIL-01` | emergence, correlation, inference strength, and further responsibility distinctions | Deferred | Philosophical Reasoning, Systems, or shared base | When new philosophical arguments or systems explanations need one of the distinctions repeatedly and the existing relations become clumsy or ambiguous. The first philosophical pass named these as later questions rather than completed omissions. |
| `CV-SYSTEMS-02` | feedforward and later systems relations | Deferred | Systems and Shared Infrastructure | When an original system explanation needs anticipatory control often enough that ordinary input, model, and control clauses obscure the relation. The first Systems pass retained feedback and control but left feedforward and other less common relations for connected technical use. |
| `CV-ECON-01` | money, prices, wages, debt, profit, taxation, budgets, and contracts | Deferred | a possible Economic Systems and Provisioning module | When an economic profile receives scenarios that can keep accounting, exchange, obligation, extraction, livelihood, and source-defined legal relations apart. Governance and Work deliberately left wider political economy outside their first passes rather than declaring it unnecessary. |
| `CV-MED-SENSITIVE-01` | mental health, reproductive health, sexuality, gender, abuse, and coercive care | Deferred | base, Medical, or another sensitive domain profile | When separate scenarios are ready for each area, with autonomy, varied lived experience, refusal, power, and exact source terminology kept visible. The first Medical pass reserved these areas because they need language for self-description, consent, harm, care, and source-defined classifications without treating any one experience as the norm. |

## Prompt sources

These inventories were used only to recover questions that an earlier batch might have overlooked. They do not define Phi's semantic structure and do not turn the register into an English relex checklist.

- [Concepticon: Dunn 2012 207-item list](https://concepticon.clld.org/contributions/Dunn-2012-207): Used as a cross-linguistic prompt for common concepts, not as a list Phi must lexicalise.
- [SIL Comparative Lists of Semantic Domains, version 4](https://semdom.org/): Used to widen the audit beyond the headings that the earlier migration happened to choose.
