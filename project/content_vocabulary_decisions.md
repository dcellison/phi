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
| [Aesthetic and formal qualities](#aesthetic-and-formal-qualities) | complete | closed | 5 |
| [Awareness and epistemic qualities](#awareness-and-epistemic-qualities) | complete | closed | 0 |
| [Ethics, care, and candour](#ethics-care-and-candour) | complete | closed | 2 |
| [Core emotion inventory](#core-emotion-inventory) | complete | closed | 1 |
| [Affective response, anticipation, and resolve](#affective-response-anticipation-and-resolve) | complete | closed | 2 |
| [Social relation, standing, and personal boundaries](#social-relation-standing-and-personal-boundaries) | complete | closed | 0 |
| [Life, age, and bodily condition](#life-age-and-bodily-condition) | complete | closed | 0 |
| [Cultivation, abundance, and wildness](#cultivation-abundance-and-wildness) | complete | closed | 3 |
| [Structure, identity, and fit](#structure-identity-and-fit) | complete | closed | 0 |
| [Imagination, unfamiliarity, wonder, and reverence](#imagination-unfamiliarity-wonder-and-reverence) | complete | closed | 0 |
| [Practical readiness, care, and effort](#practical-readiness-care-and-effort) | complete | closed | 0 |
| [Access, perception, and independent participation](#access-perception-and-independent-participation) | complete | closed | 1 |
| [System fit, equivalence, and dependable performance](#system-fit-equivalence-and-dependable-performance) | complete | closed | 1 |
| [Work timing, status, capability, and answerability](#work-timing-status-capability-and-answerability) | complete | closed | 1 |
| [Medical course, transmission, and treatment response](#medical-course-transmission-and-treatment-response) | complete | closed | 1 |
| [Core speech and conversation](#core-speech-and-conversation) | complete | closed | 1 |
| [Knowledge, understanding, belief, and memory](#knowledge-understanding-belief-and-memory) | complete | closed | 2 |
| [Attention, observation, reflection, and imagination](#attention-observation-reflection-and-imagination) | complete | closed | 2 |
| [Desire, intention, choice, and commitment](#desire-intention-choice-and-commitment) | complete | closed | 0 |
| [Agreement, consent, refusal, and pressure](#agreement-consent-refusal-and-pressure) | complete | closed | 1 |
| [Participation, cooperation, contribution, and mutual aid](#participation-cooperation-contribution-and-mutual-aid) | complete | closed | 0 |
| [Giving, receiving, keeping, and circulation](#giving-receiving-keeping-and-circulation) | complete | closed | 1 |
| [Basic motion, endpoints, and staying](#basic-motion-endpoints-and-staying) | complete | closed | 0 |
| [Manner, trajectory, and extended movement](#manner-trajectory-and-extended-movement) | complete | closed | 0 |
| [Posture, rest, waiting, and residence](#posture-rest-waiting-and-residence) | complete | closed | 0 |
| [Breath, intake, and expulsion](#breath-intake-and-expulsion) | complete | closed | 3 |
| [Contact, force, and placement](#contact-force-and-placement) | complete | closed | 3 |
| [Material change, making, and joining](#material-change-making-and-joining) | complete | closed | 3 |
| [Change, continuity, repair, and renewal](#change-continuity-repair-and-renewal) | complete | closed | 2 |
| [Life, growth, cultivation, and flourishing](#life-growth-cultivation-and-flourishing) | complete | closed | 4 |
| [Care, affection, regard, and relational repair](#care-affection-regard-and-relational-repair) | complete | closed | 0 |
| [Learning, practice, guidance, and sustained effort](#learning-practice-guidance-and-sustained-effort) | complete | closed | 2 |
| [Measurement, comparison, meaning, and record](#measurement-comparison-meaning-and-record) | complete | closed | 2 |
| [Ritual, play, and expressive response](#ritual-play-and-expressive-response) | complete | closed | 3 |
| [Relation, boundaries, and remaining practical acts](#relation-boundaries-and-remaining-practical-acts) | complete | closed | 1 |
| [Personhood, generations, kinship, and social belonging](#personhood-generations-kinship-and-social-belonging) | complete | closed | 1 |
| [Body, anatomy, and bodily condition](#body-anatomy-and-bodily-condition) | complete | closed | 10 |
| [Time, sequence, natural stations, and recurrence](#time-sequence-natural-stations-and-recurrence) | complete | closed | 6 |
| [Landscape, waters, sky, and weather](#landscape-waters-sky-and-weather) | complete | closed | 9 |
| [Plants, animals, and the living world](#plants-animals-and-the-living-world) | complete | closed | 8 |
| [Materials, substances, fibres, and fire](#materials-substances-fibres-and-fire) | complete | closed | 9 |
| [Dwelling, vessels, food, clothing, and light](#dwelling-vessels-food-clothing-and-light) | complete | closed | 7 |
| [Tools, travel, and practical objects](#tools-travel-and-practical-objects) | complete | closed | 8 |
| [Space, orientation, boundaries, and physical form](#space-orientation-boundaries-and-physical-form) | complete | closed | 9 |
| [Language, story, art, and representation](#language-story-art-and-representation) | complete | closed | 9 |
| [Reason, belief, ritual, and value](#reason-belief-ritual-and-value) | complete | closed | 13 |
| [Roles, places, relations, and remaining concrete nouns](#roles-places-relations-and-remaining-concrete-nouns) | complete | closed | 23 |
| [Recovered cross-inventory prompts](#recovered-cross-inventory-prompts) | complete | closed | 29 |

## Core material qualities

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-MAT-01` | hollow interior structure | Compositional | base expression | `whemoa muwi`. An empty interior says what is hollow without treating every empty vessel or room as a material structure. |
| `CV-MAT-02` | absorption of liquid or other material | Implemented | base | Words: `wosanu`. The verb puts the receiving body in subject position and distinguishes material taken within from liquid merely present on a surface or moving through. |
| `CV-MAT-03` | porous interior structure | Deferred | base or a material-focused module | When connected material practice repeatedly needs porosity itself rather than permeability to a named substance. Many small empty interiors can describe the visible arrangement, while a dedicated quality may become useful in soil, textile, building, or filter work. |
| `CV-MAT-04` | dense packing or scientific density | Deferred | base, Systems, Ecological, or exact source material | When connected material or scientific writing repeatedly needs one stable relation that existing thickness, concentration, packing, and source measurements cannot express cleanly. Everyday uses divide among thick body, high concentration, and many things in little space; scientific density adds a defined magnitude and method. |
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
| `CV-AEST-03` | style and characteristic aesthetic form | Implemented | base | Words: `senalu`. The noun names a recognisable manner shared across works while keeping pattern, design, shape, and aesthetic judgement distinct. |
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
| `CV-AFFECT-02` | guilt, anxiety, disgust, excitement, relief, frustration, and boredom | Implemented | base | Words: `naremu`, `weshoru`, `kophinu`, `rashowe`, `meraho`, `pasharo`, `moshaki`. Seven direct forms expand ordinary self-report beyond the core lesson. Each entry keeps the feeling apart from the judgement, event, or bodily condition that may accompany it. |

## Affective response, anticipation, and resolve

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-AFFECT-01` | sustained interest or engagement | Implemented | base | Words: `mewali`. The adjective keeps interest apart from curiosity and directed attention. |
| `CV-AFFECT-02` | guilt, anxiety, disgust, excitement, relief, frustration, and boredom | Implemented | base | See the complete decision under [Core emotion inventory](#core-emotion-inventory). |

## Social relation, standing, and personal boundaries

No lexical question from this batch remains outside an explicit coverage decision.

## Life, age, and bodily condition

No lexical question from this batch remains outside an explicit coverage decision.

## Cultivation, abundance, and wildness

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-CLEAN-01` | dirty, contaminated, spoiled, and rotten | Implemented | base and established modules | Words: `hureki`, `hiso`, `hisophi`, `mukesi`, `morume`. Base `hureki` names physical dirt. Existing clean, contaminant, spoil, and decompose entries keep practical cleanliness, unexpected presence, lost fitness, and material breakdown separate; active or completed decomposition supplies ordinary rotting without a moralised rotten root. |
| `CV-FOOD-01` | rice and tea | Implemented | base | Words: `napari`, `hasumi`. The two nouns cover ordinary rice and tea, while exact cultivars, blends, and trade names remain with their sources. |
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
| `CV-MEET-01` | meet as a verb | Implemented | base | Words: `haromi`. Phi does not turn a thing noun into its deed. The new verb names an encounter by plan or chance, while `lona` remains the gathering or meeting event. |

## Knowledge, understanding, belief, and memory

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-COG-01` | amnesia, dementia, impairment, and exact cognitive assessment | Source-bound | Medical plus exact source material | Preserve the diagnosis, test, classification, and source; use Phi to describe the person's reported experience and observed abilities without replacing those records. Ordinary memory and understanding words cannot carry a diagnosis or test result by themselves. |
| `CV-LOSE-01` | lose and misplace a thing | Implemented | base | Words: `wesaki`. The verb reports an unintentionally missing possession or location. Deliberate release, abandonment, contest results, and wider bereavement keep their own accounts. |

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
| `CV-LOSE-01` | lose and misplace a thing | Implemented | base | See the complete decision under [Knowledge, understanding, belief, and memory](#knowledge-understanding-belief-and-memory). |

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
| `CV-HIT-01` | brief physical impact | Declined | retired vocabulary | Retire patore. Forceful contact uses kema palo, while pesa, pukeri, or kaworu states movement or consequence when the event establishes it. A general impact root gathers contact, displacement, damage, and bodily injury under an unmarked verb whose ordinary reach includes interpersonal blows. |
| `CV-HIT-02` | peace-linguistic scope and retention of patore | Compositional | base expressions and existing result words | `kema palo`, `pesa`, `pukeri`, `kaworu`. Forceful contact, displacement, material damage, and bodily injury remain separate claims, so ordinary Phi selects the distinction the event establishes. |
| `CV-AIM-01` | physical alignment towards a selected point or object | Compositional | base construction usable in Work | `wea sileta rato`. `wea` (TOWARD) names the selected reference and `rato` (turn) changes an object's facing. The construction covers physical alignment without importing the combat-shaped extensions of aim or target. |

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
| `CV-WRITE-01` | page, ink, letter, and message | Implemented | base roots and registered compounds | Words: `penuwa`, `milaro`. Compounds: `thekiro tinoa`, `thekiro kiroa`, `thekiro milaro`. Page and message receive direct nouns. Writing dye supplies ink, writing sign supplies a written character, and writing message supplies a letter without reproducing the English homonym. |

## Ritual, play, and expressive response

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-HIT-01` | brief physical impact | Declined | retired vocabulary | See the complete decision under [Contact, force, and placement](#contact-force-and-placement). |
| `CV-HIT-02` | peace-linguistic scope and retention of patore | Compositional | base expressions and existing result words | See the complete decision under [Contact, force, and placement](#contact-force-and-placement). |
| `CV-APPLAUSE-01` | applause | Compositional | base expression | `miona wi manuwe roe telui wiso palo`, `woraka`, `pharuki`, `nomela`. Hands touching each other in rhythm describe the gesture; appreciation, celebration, or encouragement states why the gathering responds. |

## Relation, boundaries, and remaining practical acts

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-COVER-01` | cover and uncover | Implemented | base | Words: `tawemi`, `phae`. The new verb names the physical overlying act. Existing `phae` (open) removes or moves a cover when view or access returns, while closing and hiding keep their own purposes. |

## Personhood, generations, kinship, and social belonging

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-ANIMAL-01` | bee, wolf, deer, bear, frog, spider, cow, and goat | Implemented | base | Words: `hemoko`, `lorahu`, `thenari`, `maruko`, `tuleno`, `nirowe`, `mukowa`, `karume`. All eight familiar animals receive direct roots for ordinary ecological description, household life, and stories. Exact species, breeds, and technical classifications remain source-specific where needed. |

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

## Time, sequence, natural stations, and recurrence

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-TIME-01` | today, yesterday, tomorrow, and every day | Compositional | base expressions | `ha philo`, `luera philo`, `wireo philo`, `theula philo`. The day stays audible while a demonstrative, temporal noun, or quantifier locates it. Four short expressions cover the ordinary daily references without a second set of roots. |
| `CV-TIME-02` | always, never, often, rarely, and sometimes | Compositional | base expressions | `theula thimu`, `mawha thimu`, `sheloi shemu`, `phina shemu`, `soli shemu`. Frequency remains a claim over time or moments, so the size of the claim stays in the utterance instead of hiding inside an adverb. |
| `CV-TIME-03` | relative proximity, earliness, lateness, and simultaneity | Compositional | base grammar and expressions, with optional module vocabulary for organised work | `noshi luera`, `noshi wireo`, `wuero luera`, `wuero wireo`, `phoe`, `pheo`, `nuawe`, `thunesi`. Near or far time, before or after a reference, and occurrence within one span state the useful relation. Work that is deliberately spread across different times may use module adjective `thunesi` (asynchronous). |
| `CV-TIME-04` | age, lifetime, birthdays, anniversaries, and larger spans | Compositional | base expressions | `mia wi phoi ta shao torua phelu`, `lioru mosha`, `thowia philo`, `torua nuri`, `thorea`. A person holds counted years; a life has a period; a birth has a day; and a returning observance can name its event, annual cycle, or ceremony. These relations remain clearer than one broad anniversary root. |
| `CV-TIME-05` | calendar, history, chronology, and timeline | Compositional | base expressions plus separately preserved source records | `thimu sirami`, `luera nophi`, `luera sirami`, `nu`, `phoe`, `pheo`. A time record, a story or record of the past, ordinal position, and before-after relations distinguish the artefact from the account it carries. A named external calendar or chronology keeps its own source form. |
| `CV-TIME-06` | exact clock readings, clock units, time zones, and named calendar identifiers | Source-bound | separate source material with a Phi account | The complete clock reading, time zone, named calendar date, and exact unit notation remain outside the Phi passage. A Phi account may identify the record, its purpose, and its relation to an event without replacing data needed for coordination, care, accessibility, testimony, or safety. Phi's natural stations and calendar spans support ordinary temporal speech, while an exact external value retains the notation and standard that make it usable. |

## Landscape, waters, sky, and weather

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-LAND-01` | soil, ground, dry land, coast, and beach | Compositional | base roots and expressions | `muila`, `kurathi muila`, `kerime`, `leru`. `muila` already covers earth as soil, ground, and land, while `kerime` covers the water's edge and coastal strip. Dryness and loose beach material remain visible when those details matter. |
| `CV-LAND-02` | desert, cliff, and volcano | Implemented | base | Words: `harisu`, `pareshi`, `thokaru`. Three common landforms need more than a temporary condition or a picturesque approximation. The new roots keep a desert distinct from drought, a cliff distinct from its edge, and a quiet volcano distinct from a burning mountain. |
| `CV-WATER-01` | tide | Implemented | base | Words: `lunisa`. A recurring coastal cycle affects travel and shoreline work. It also determines access, gathering, and safety often enough to deserve a direct noun. Its entry keeps waves and currents separate. |
| `CV-WATER-02` | current, glacier, waterfall, groundwater, and wetland | Compositional | base expressions with an ecological-module term where needed | `phialu selu`, `kerithe luphore`, `phialu lepa`, `muila phialu`, `wirua muila menuro`. Movement through water takes more than one form. Existing expressions distinguish current and waterfall, while frozen flow, subsurface water, and wet habitat keep their defining relation audible. A technical classification can remain in its source record beside the Phi account. |
| `CV-SKY-01` | planet | Implemented | base | Words: `nowari`. Sun, star, moon, and Earth left the ordinary celestial inventory without a word for the class Earth belongs to. `nowari` supplies that class while named planets keep their source identities. |
| `CV-SKY-02` | horizon, atmosphere, and humidity | Compositional | base roots and expressions | `waero norui`, `haowu`, `wirua haowu`. The visible sky can have an apparent boundary, ordinary atmosphere is air around a place or world, and humidity is moisture in that air. Exact scientific layers and measurements remain separately identified when needed. |
| `CV-WEATHER-01` | hail, sleet, drizzle, wet or melting snow, rainstorm, snowstorm, and thunderstorm | Compositional | base expressions | `kerithe pheralu`, `moli pheralu`, `wirua phirenu`, `phirenu larewu kelu`, `pheralu kurisha`, `phirenu kurisha`, `horuma kurisha`. Familiar weather subtypes remain transparent combinations of material, wetness, change, intensity, and event. `wirua phirenu` covers wet snow, and `phirenu larewu kelu` says that snow is becoming liquid, without pretending that every source draws the sleet and slush boundaries alike. Exact thresholds and named warning categories come from the weather source in use. |
| `CV-LAND-03` | narrow geological and coastal landform classes | Deferred | base, ecological module, or exact source term according to use | When an active navigation, geological, ecological, or literary scenario repeatedly loses a landform distinction that existing roots and spatial relations cannot carry naturally. Bay, gulf, strait, canyon, gorge, delta, dune, and similar classes differ in which shape, process, or local name matters. Existing land and water relations can carry ordinary description until one distinction repeatedly needs a root. |
| `CV-SKY-03` | specialist astronomical and meteorological classes | Deferred | future module vocabulary plus exact scientific source material | When an astronomy or meteorology scenario needs the same class repeatedly for explanation rather than only as a named source object. Specialist astronomy can describe comets, asteroids, and galaxies without moving them all into the base path. Atmospheric layers, precipitation classes, and named severe-weather systems can likewise remain exact in their source material. |

## Plants, animals, and the living world

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-LIFE-01` | a single organism or living thing across plants, animals, and fungi | Deferred | Ecological or shared base, according to connected use | When connected ecological or philosophical writing repeatedly needs a singular participant spanning plants, animals, fungi, and other living categories. `lioru` names life, `lima` states that something is alive, and the familiar living categories retain their own nouns. A generic countable organism term may still help when one participant must range across those categories. |
| `CV-PLANT-01` | shrub, stem, thorn, sap, and pollen | Implemented | base | Words: `wotami`, `pakewu`, `kewati`, `phunelo`, `nophali`. These terms recur wherever plants meet hands or bodies: gardens, paths, care, and ecological writing. They separate growth form from supporting axis, then give thorn, sap, and pollen direct names. |
| `CV-PLANT-02` | trunk, petal, mushroom, thicket, orchard, and crop | Compositional | base compounds | `shiro pakewu`, `peloru lirowa`, `tokemi lureko`, `wotami sholei`, `lureko shiro koshira`, `sorila phireo`. Each expression leaves the defining plant or fungus relation in view. The six compounds are short in speech, and their parts help a learner recover the meaning. |
| `CV-PLANT-03` | specialist plant and fungus structures, exact kinds, and contextual food or cultivation categories | Deferred | Ecological, Household, Work, Medical, or exact source material | When connected ecological, garden, food, craft, or care writing repeatedly needs one of these distinctions beyond a transparent description or exact source name. This group mixes technical structures and named kinds with categories drawn by cooking, cultivation, or a particular purpose. One decision for all of them would be tidy only on paper. |
| `CV-ANIMAL-02` | ordinary animal feet, outer covering, mouth structures, homes, companion relations, young, calls, and groups | Compositional | base compounds | `wuloe nolika paloi`, `kethua nolika paloi`, `kethua pelori phulae`, `nolika whila`, `keloe nolika`, `pelori womu`, `hemoko womu`, `limu nolika`, `nolika haoni`, `nolika sholei`. Animal, body part, material quality, or social relation stays audible in each expression. The same small set of words covers familiar feet, homes, groups, and companion relations without a second list of opaque roots. |
| `CV-ANIMAL-03` | specialist animal anatomy, life stages, sex and age classes, breeds, calls, and taxonomic ranks | Deferred | Ecological, Medical, a later animal-care vocabulary set, or exact source material | When connected ecological, care, husbandry, or literary writing repeatedly needs one of these distinctions and transparent description becomes cumbersome or ambiguous. The group spans body structures, life stages, husbandry classes, and formal taxa, each answering a different practical question. Existing body words cover ordinary description while biological or legal categories keep the records that define them. |
| `CV-REPRO-01` | biological reproduction and deliberate breeding | Deferred | base, Ecological, or a reproductive-health vocabulary set | See the complete decision under [Life, growth, cultivation, and flourishing](#life-growth-cultivation-and-flourishing). |
| `CV-CULT-01` | pollination, pruning, weeding, and fertilising | Deferred | Ecological, Household, or Work | See the complete decision under [Life, growth, cultivation, and flourishing](#life-growth-cultivation-and-flourishing). |

## Materials, substances, fibres, and fire

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-MAT-03` | porous interior structure | Deferred | base or a material-focused module | See the complete decision under [Core material qualities](#core-material-qualities). |
| `CV-MAT-04` | dense packing or scientific density | Deferred | base, Systems, Ecological, or exact source material | See the complete decision under [Core material qualities](#core-material-qualities). |
| `CV-MAT-05` | permeability to a named substance | Compositional | base clause, with exact technical criteria in source material | See the complete decision under [Core material qualities](#core-material-qualities). |
| `CV-MAT-06` | waterproofness | Compositional | base clause, with exact ratings in source material | See the complete decision under [Core material qualities](#core-material-qualities). |
| `CV-MAT-07` | plastic, rubber, steel, ceramic, and concrete | Implemented | base | Words: `polenu`, `luwaro`, `teshilo`, `mueta`, `kapenu`. These five broad materials recur in daily life and ecological discussion. Homes, streets, clothing, and repair work all need names for them. Direct nouns keep those sentences short; grade and composition enter only when they matter. |
| `CV-MAT-08` | brick, adhesive, fuel, card or cardboard, and alloy | Compositional | base and cross-module compounds | `mueri kerou`, `shumeko muralo`, `thero muralo`, `theru pelua`, `welotu keluo`. Each compound exposes the practical relation behind its category instead of adding five opaque roots. A formulation or grade can join the Phi expression when it matters. |
| `CV-MAT-09` | paint, varnish, mortar, cement, plaster, asphalt, coal, charcoal, and related material products | Deferred | Household, Work, Systems, Ecological, or shared base according to connected use | When a connected household, craft, construction, energy, or ecological scenario repeatedly needs one of these products beyond a transparent material description. Paint and coal happen to be materials, but that fact gives them little else in common. Their next connected scenarios can decide which distinctions stay transparent and which deserve direct words. |
| `CV-MAT-10` | additional ordinary metals, alloys, fibres, and natural or manufactured materials | Deferred | base or one or more material-using modules according to connected use | When connected use repeatedly needs the same material identity in Phi rather than only in an exact source record. Aluminium, brass, bronze, cork, and similar names may earn Phi forms through repeated ordinary use. The present batch does not turn a survey of available materials into another list a general speaker must memorise. |
| `CV-MAT-11` | exact chemical substances, polymer identities, alloy grades, product formulations, and trade names | Source-bound | exact source material with a Phi account | The exact identifier stays outside the Phi passage with the notation and version that make it usable. Formulas and grades retain their source forms. So do standards, formulations, and trade identities. A broad Phi noun can still support discussion of a material's handling and effects. It cannot do the technical identifier's job. |

## Dwelling, vessels, food, clothing, and light

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-DWELL-01` | ceiling, stairs, corridor, gate, fence, and chimney | Compositional | base compounds | `muwi toru`, `rihe ruela`, `muwi ruela`, `norui ponu`, `norui moru`, `thumiro ruela`. Six common building features are short relations among an interior, route, boundary, wall, door, roof, and smoke. The registered compounds fit many building traditions and spare six opaque roots. |
| `CV-DWELL-02` | installed cooking, cooling, washing, bathing, and sanitation appliances or fixtures | Deferred | Household, Systems, Built Environment, or exact source material according to use | When a household, infrastructure, access, repair, or inhabited-place scenario repeatedly needs one stable appliance or fixture distinction beyond its function and exact source identity. Broad function can already be described with a device, place, action, temperature, water path, or storage relation. Stove, oven, refrigerator, sink, bath, and similar categories divide differently across technologies and dwellings, so connected use should decide which distinctions deserve Phi forms. |
| `CV-DWELL-03` | additional portable, directional, or electrically powered light sources | Compositional | base words and descriptions with exact equipment records where needed | `luma`, `lumoi`, `philu`. `luma` names the general made light source, `lumoi` a portable protected lamp, and `philu` a wick-fed candle. Shape, beam, energy source, and controls can distinguish a torch, flashlight, or electric fitting without another general light noun. |
| `CV-DWELL-04` | additional utensils, vessels, furnishings, and functional garment types | Deferred | Household, base, or another practical module according to connected use | When connected daily-life, care, craft, or literary use repeatedly needs one practical object or garment type and the transparent description becomes cumbersome or ambiguous. The base layer and Household module already cover ordinary containers, seating, bedding, storage, cleaning, clothing, and tableware. Forks, specialised pans, cupboards, and narrower footwear can be described by function until one distinction repeatedly earns a direct word. |
| `CV-DWELL-05` | exact food, dish, garment, household-object, and product identities | Source-bound | exact source identity beside a Phi account | An original name, cultural designation, or model stays in its source form when identity depends on it. Recipes, labels, and safety instructions remain with that source while Phi describes the item's ordinary relations and effects. Phi can describe how an item is made and used, what it is made from, and how it relates to the scene. A familiar category may still receive a Phi root later; exact identity remains with the source that establishes it. |
| `CV-FOOD-01` | rice and tea | Implemented | base | See the complete decision under [Cultivation, abundance, and wildness](#cultivation-abundance-and-wildness). |
| `CV-FOOD-02` | nut | Compositional | base compound | See the complete decision under [Cultivation, abundance, and wildness](#cultivation-abundance-and-wildness). |

## Tools, travel, and practical objects

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-TOOL-01` | additional hand tools, fasteners, powered tools, protective equipment, and calibration equipment | Deferred | Household, Work, Systems, Accessibility, base, or exact source material according to connected use | When connected household, craft, access, repair, or technical work repeatedly needs one stable implement or equipment class beyond its function and exact source identity. The base inventory supplies a general tool and device beside several familiar hand implements. This deferred field includes further cutting and digging tools, fasteners, powered equipment, and protective or calibration gear. Those groups answer different practical questions, so one undifferentiated expansion would be larger than it is useful. |
| `CV-TOOL-02` | ordinary tool and device parts such as handle, blade, head, grip, and fastener | Compositional | base descriptions and Work or Systems compounds | `phelu monaki`, `kati monaki`, `palo monaki`, `lorea monaki`. A part can be named by the contact or material change it performs, while its shape, material, and place in the larger object remain open. Exact replacement parts and standardized fasteners retain the identity supplied by their technical source. |
| `CV-MESH-01` | screens, filters, grids, and exact mesh classes beyond an ordinary net | Deferred | Household, Ecological, Systems, Work, or exact source material according to function | When connected household, ecological, craft, or technical use repeatedly needs one mesh-based object apart from its material, openings, function, and source specification. Base `mera` covers flexible open mesh and its ordinary physical uses. A rigid screen, fluid filter, computational grid, and measured mesh grade have little in common beyond an English family resemblance. |
| `CV-SIGNAL-01` | chimes, alarms, and other audible alert devices | Compositional | base words with Systems vocabulary or exact source records where needed | `teli`, `teli kirowi`, `pukea kirowi`. `teli` names the resonant bell or chime, while `kirowi` names a detected signal and `pukea` can state danger. A technical alarm account can add the source and sound, then say who should notice it and how they interpret it. |
| `CV-TRAVEL-01` | road, trail, walkway, and other traversable ground | Implemented | base | Words: `ruela`. Base `ruela` now states its ordinary range plainly: worn footpath, trail, made walkway, and prepared road are all traversable lines. Surface, construction, condition, permitted users, and access can be described without a separate road root. |
| `CV-TRAVEL-02` | a general vehicle or transport device | Compositional | base expression | `phaero keli`. `phaero keli` identifies an object by its transport function without claiming a particular power source, wheel arrangement, ownership relation, or service. Direct boat and wagon nouns remain available when their form is already known. |
| `CV-TRAVEL-03` | cycles, powered road vehicles, public transport vehicles, aircraft, and other transport classes | Deferred | Systems, Accessibility, Built Environment, Ecological, base, or exact source material according to connected use | When a connected mobility, access, infrastructure, ecological, repair, or literary scenario repeatedly loses one transport distinction in transparent description. A bicycle and bus do not ask the same thing of a route, body, energy source, or shared service, and an aircraft differs again. Existing vocabulary can describe their movement, construction, carrying role, and source of energy until one class repeatedly needs a direct Phi word. |
| `CV-TRAVEL-04` | exact vehicle models, routes, services, navigation identifiers, and equipment specifications | Source-bound | exact source identity beside a Phi account | Preserve model and service names, route numbers, and navigation codes in their original source form. Schedules, dimensions, ratings, and safety specifications keep their source notation. Phi can describe the vehicle, route, present condition, access relation, and travel event around an exact identifier. The identifier itself remains in the map, timetable, ticket, or technical record that makes it usable. |

## Space, orientation, boundaries, and physical form

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-MEAS-02` | area as a neutral magnitude | Compositional | base expression | See the complete decision under [Size, extent, and distance](#size-extent-and-distance). |
| `CV-MEAS-03` | volume as occupied spatial magnitude | Compositional | base expression | See the complete decision under [Size, extent, and distance](#size-extent-and-distance). |
| `CV-SHAPE-01` | straight as an ordinary shape quality | Implemented | base | See the complete decision under [Aesthetic and formal qualities](#aesthetic-and-formal-qualities). |
| `CV-SHAPE-02` | round as an ordinary shape quality | Compositional | base expression | See the complete decision under [Aesthetic and formal qualities](#aesthetic-and-formal-qualities). |
| `CV-AIM-01` | physical alignment towards a selected point or object | Compositional | base construction usable in Work | See the complete decision under [Contact, force, and placement](#contact-force-and-placement). |
| `CV-SPACE-01` | east and west within the cardinal direction system | Compositional | registered base expressions | `sileta thorui`, `sileta lumae`. Base `nitho` and `ronua` name north and south. East and west stay tied to the daily solar course: the sun's beginning names east, and its end names west. The four directions remain ordinary, value-neutral nouns. |
| `CV-SPACE-02` | corners, bends, and intersections | Compositional | base descriptions | `wi shuna lorea`, `wi moru lorea`, `ruela rato`, `wi ruela lorea`. English corner covers several shapes. Two joined edges or walls make one kind, a path's turn makes another, and connected paths make a third. Keeping those structures visible is clearer than asking one root to hide all three. |
| `CV-GEOM-01` | geometric points, lines, angles, axes, polygons, and exact relations beyond ordinary shape | Deferred | base, Work, Systems, a future mathematics profile, or exact source material according to connected use | When connected mathematical, design, craft, engineering, or teaching work repeatedly needs stable geometric objects and relations inside Phi rather than in an accompanying diagram or source definition. Circle, straightness, edges, surfaces, dimensions, position, and spatial relators cover ordinary physical description. A technical geometry inventory would introduce defined objects and relations whose exact meanings should be chosen together rather than borrowed one English headword at a time. |
| `CV-SPACE-03` | exact coordinates, addresses, map references, parcel identifiers, and survey records | Source-bound | exact source identity beside a Phi account | Coordinates, addresses, grid references, parcel and site identifiers, survey marks, datum names, scales, and exact dimensions retain their original source form. Phi may describe their place, use, source, and uncertainty without recoding them. Phi can discuss an exact spatial record through its ordinary spatial vocabulary. The record keeps the notation and reference system that lets another person locate or verify it. |

## Language, story, art, and representation

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-AEST-03` | style and characteristic aesthetic form | Implemented | base | See the complete decision under [Aesthetic and formal qualities](#aesthetic-and-formal-qualities). |
| `CV-WRITE-01` | page, ink, letter, and message | Implemented | base roots and registered compounds | See the complete decision under [Measurement, comparison, meaning, and record](#measurement-comparison-meaning-and-record). |
| `CV-LANG-01` | language varieties, dialects, registers, accents, grammar, scripts, and bounded sentences | Compositional | base expressions and event nouns | `haluma kire`, `haluma senalu`, `haluma haoni welisha`, `haluma sena`, `thekiro sena`, `shemui`. A language form, style, or voice colour says which kind of variation matters. Language pattern supplies grammar, writing pattern supplies script, and the event noun of `shemui` supplies a bounded utterance or sentence. |
| `CV-LANG-02` | exact named languages, scripts, orthographies, linguistic classifications, and source wording | Source-bound | source identity beside a Phi account or an accepted Phi-form onym | Preserve exact language and script names, orthographies, linguistic classifications, and quoted source wording in their original source form. A bearer or relevant naming community may accept a Phi-form onym under the ordinary name charter. Phi can discuss how people use and transmit a language, including interpretation across languages or modes, without recoding the identity that another community supplies. An accepted Phi-form onym may name a language or script, but it does not replace the source name. |
| `CV-ART-01` | poems, paintings, drawings, sculptures, novels, genres, and performances | Compositional | base roots and event nouns | `melira`, `kire`, `nophi shelu`, `meliho`, `rotiku`, `wile`. Phi names a work through the act or form that made it. `melira` covers poem and song, `kire` supplies drawing or shaping as an event noun, and `nophi shelu` identifies a story book. Singing, dancing, and playing retain the specific performance instead of entering one general genre hierarchy. |
| `CV-ART-02` | artist, writer, reader, singer, dancer, composer, and performer roles | Compositional | base relative clauses beside existing role nouns | `rena shela kealo miona`, `rena thekiro miona`, `rena theo miona`, `rena meliho miona`, `rena rotiku miona`, `rena meliphe kealo miona`. Direct nouns already name musician, poet, and storyteller. Other roles use a relative clause whose verb states the person's actual work. This also lets a role belong to one occasion without turning it into a permanent class. |
| `CV-MUSIC-01` | a general musical instrument beyond drum, flute, bell, and instrument string | Compositional | base expression | `meliphe tenoa`. `meliphe tenoa` identifies an object by its musical work. Base nouns still name the drum, flute, bell, and tensioned string when those familiar forms matter. |
| `CV-MUSIC-02` | additional instrument families, musical notation, melody, harmony theory, metre, tuning, and technical performance vocabulary | Deferred | base, a future music vocabulary set, or exact source material according to connected use | When connected musical composition, teaching, instrument care, or performance repeatedly needs stable distinctions that the present sound, timing, relation, and source vocabulary cannot carry naturally. The current lexicon distinguishes sound from music, a song from singing, and rhythm from harmony. It also has a general play verb, direct nouns for drum and flute, and words for a bell and a tensioned string when those forms matter. Music teaching or sustained practice may still need narrower relations chosen together rather than a shelf of borrowed labels. |
| `CV-ART-03` | exact work titles, quotations, lyrics, scores, named styles, genre labels, and source identifiers | Source-bound | source material beside a Phi account or an accepted Phi-form onym | Preserve exact titles, quotations, lyrics, scores, named styles, genre labels, catalogue identifiers, and edition details in their source form. A work may also bear an accepted Phi-form onym under `ne`, without changing the preserved source material. Phi can name the kind of work, its maker, medium, form, and reception. Exact identity stays with the title, wording, notation, or catalogue record that establishes which work is meant. |

## Reason, belief, ritual, and value

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-PHIL-01` | emergence, correlation, inference strength, and further responsibility distinctions | Deferred | Philosophical Reasoning, Systems, or shared base | When new philosophical arguments or systems explanations need one of the distinctions repeatedly and the existing relations become clumsy or ambiguous. The first philosophical pass named these as later questions rather than completed omissions. |
| `CV-REASON-01` | motivation, explanatory cause, justification, and purpose | Compositional | base clauses and existing reasoning vocabulary | `remotha`, `porua`, `thueli`, `ka`. English why can ask what moved a person, what caused an event, what an action was for, or what justifies a claim. Phi keeps those relations separate so that one answer cannot quietly stand in for another. |
| `CV-EPIST-01` | proof and certainty in ordinary claims | Compositional | base reasoning words with Philosophical Reasoning where needed | `thesori`, `remotha`, `sano`, `norethi`, `whekate`. Ordinary proof is better stated through the evidence, reasons, inference, or refutation that settles a particular point. Knowledge and confidence then report different stances towards the result rather than becoming a portable certificate of certainty. |
| `CV-EPIST-02` | formal proofs, exact probability values, odds, and named logical or epistemic standards | Source-bound | exact source material beside a Phi account | Formal proofs keep their notation, axioms, and named logic in source form. Probability statements keep their value, odds, reference class, and method identifier. Phi states what is claimed, how the result was obtained, and how it enters the present decision. A formal result depends on its notation, axioms, method, reference class, and stated standard. Phi can discuss the argument and evidence without recoding the identity that makes the result reproducible. |
| `CV-CHANCE-01` | favourable and harmful luck, chance contribution, and coincidence | Compositional | base nouns, modifiers, and temporal clauses | `soleha`, `welao soleha`, `peloma soleha`, `senao shemu`. Base `soleha` identifies the unplanned part of an outcome, and a modifier states how it mattered. A coincidence can place events in the same moment or relation without adding a causal claim. |
| `CV-RITE-01` | separate Phi roots for funeral, wedding rite, baptism, initiation, and other prescribed rites | Declined | described ceremonies under the single base noun `thorea` | `thorea` remains Phi's only ceremony word. The occasion or relation can be described, as in `lumeo thorea`; prescribed rites receive no separate roots. A dedicated root would make one inherited division of ceremonial life look universal. Phi instead says what the ceremony marks and leaves its form with the participants and tradition. |
| `CV-RITE-02` | exact ceremony and ritual names, inherited formulas, calendars, offices, and lineage identities | Source-bound | source identity beside a Phi description | A rite or festival keeps its exact name and inherited formula in source form. Calendars, ritual offices, lineage names, and tradition-specific classifications do the same. Phi may describe the actions, participants, timing, meaning, and consent around them. The general words for ceremony, ritual, custom, tradition, and festival allow discussion without replacing the identities that particular communities maintain. |
| `CV-META-01` | named souls, spirits, magical beings, divine agents, doctrines, and metaphysical classifications | Source-bound | base metaphysical vocabulary with exact source identities | Named spirits, souls, deities, and magical beings remain in their source form. Doctrines, cosmologies, afterlife states, and tradition-specific metaphysical categories do the same. Phi states the speaker's stance, evidence, relation, and interpretation. Phi can affirm, question, deny, narrate, or compare a metaphysical account. Exact names and doctrinal distinctions remain with the people and sources that establish what those entities or categories are. |
| `CV-META-02` | fate, destiny, and providence as general claims | Compositional | base future, purpose, modality, luck, and claim vocabulary | `wireo porua`, `na`, `soleha`, `sherewa`. A speaker can claim that a future is necessary, that a life or event has a purpose, or that chance shaped an outcome. Keeping those claims separate avoids turning fate into an unexplained mixture of necessity, purpose, and luck. |
| `CV-VISION-01` | revelation, prophecy, omen, and other claimed signs of what is hidden or future | Compositional | base vision, claim, sign, future, and evidential vocabulary | `lunai`, `wireo sherewa`, `kiroa`, `ti`. A vision can be reported as a vision, a prophecy as a future claim, and an omen as a sign under a stated interpretation. The evidential keeps the claimed route visible, while exact inherited categories remain source material. |
| `CV-JUST-01` | exact laws, legal rights, offences, remedies, judgments, contracts, and institutional justice procedures | Source-bound | Commons vocabulary beside exact legal source material | Statutes, legal rights and offences, remedies, judgments, and contracts remain in their source form. Jurisdiction, filing status, deadline, and procedure name do the same. Phi discusses the source and interpretation, then the effect and consequences for the people involved. Phi can discuss fairness, authority, accountability, redress, review, jurisdiction, and normative rights. The legal wording and status that decide what a document or institution actually recognises must remain exact. |
| `CV-VALUE-01` | importance, priority, merit, deservingness, dignity, worth, preciousness, and treasure | Compositional | base value and worth vocabulary with Work priority where needed | `sone`, `rolia`, `thaemo`, `themoka`, `noetha`, `porethu`, `meropi`. Valuing is an act, worth is a claimed property, preciousness is a cherishing relation, treasure is its cherished referent, and priority orders attention under a purpose. Merit and deservingness can state the relevant conduct, contribution, need, criterion, or responsibility instead of ranking a whole person. |
| `CV-ECON-01` | money, prices, wages, debt, profit, taxation, budgets, and monetary accounting | Declined | no Phi lexical roots; exact source records remain available beside a Phi account | Phi has no monetary roots or internal monetary accounting. Exact economic records remain in their source form when people need to discuss them. The later canon decision places the clock, ruler, and price tag under the same refusal. Exchange, giving, receiving, sharing, obligation, extraction, and livelihood keep their own non-monetary relations. |

## Roles, places, relations, and remaining concrete nouns

| ID | Concept | Status | Placement | Decision or return condition |
|---|---|---|---|---|
| `CV-ADVENTURE-01` | trip, expedition, exploration, quest, and adventure | Compositional | base travel, observation, purpose, and adventure vocabulary | `laniru`, `rulami`, `whenola`, `somela`. `laniru` gathers extended travel into one event, `rulami` names a venture whose course is not fully known, and `whenola` foregrounds movement without a fixed route or destination. Observation, inquiry, a sought object, and any institutional purpose can be stated in their own clauses instead of being hidden inside one English travel label. |
| `CV-COUNSEL-01` | advice, counsel, and recommendation as communicative acts | Compositional | base guidance, listening, reason, and claim vocabulary | `menua`, `kulo`, `sheluo`, `remotha`. `menua` names the person consulted, while `kulo` states guidance and `sheluo` attentive listening. A recommendation can state the proposed action, its source, and its reasons directly. This keeps the role from acquiring a hidden verb and leaves the other person's decision audible. |
| `CV-RISK-01` | ordinary danger, hazard, exposure, possible harm, and practical safety | Compositional | base safety vocabulary with Medical and Systems relations where needed | `pukea`, `pemaru`, `perawi`, `peloma`, `shurano`, `po`. `pukea` names possible harm in the conditions being discussed, `pemaru` its potential source or condition, `perawi` relevant contact, `peloma` a harmful effect or tendency, and `shurano` a practical safety judgement. Evidence, affected people, and conditions can be added without treating one risk word as the whole account. |
| `CV-RISK-02` | exact risk scores, warning levels, hazard classes, exposure limits, and safety thresholds | Source-bound | exact technical or institutional source beside a Phi safety account | Exact risk matrices, scores, categories, warning levels, hazard symbols, exposure limits, thresholds, and issuing authorities retain their source form. Phi can describe their purpose, evidence, uncertainty, and practical consequences without recoding them. Phi can say what danger is being considered, who may be exposed, what evidence is available, and what protection is proposed. A rating or threshold remains useful only inside the method and authority that defined it. |
| `CV-ENERGY-01` | electricity, electric charge and current, and related electrical phenomena | Deferred | Systems, Household, Ecological, Work, or base vocabulary according to connected use | When the Systems module prose migration or a connected household, ecological, repair, or infrastructure passage needs to distinguish electrical phenomena, charge, current, or electrical supply from general energy inside Phi. Base `kenua` supplies ordinary energy, and registered `thero muralo` supplies fuel as material used for fire. Electricity is distinct enough that a lasting solution should not be improvised as 'lightning energy' or made to cover charge, current, and supply by accident. |
| `CV-ENERGY-02` | exact energy quantities, units, ratings, tariffs, products, grid identities, and equipment specifications | Source-bound | exact technical, billing, or equipment source beside a Phi account | Energy quantities and units, meter readings, equipment ratings, tariffs, named products, grid and provider identities, account identifiers, and specifications retain their source form. Phi can state who supplied the record and how it enters the present decision. Phi can discuss an energy source, transfer, use, interruption, consequence, and shared decision without translating the notation that makes a reading, rating, or account verifiable. |
| `CV-MED-02` | exact medicine identity, formulation, amount, route, timing, course, prescriber, and instructions | Source-bound | exact medical or product source beside a Phi care account | Medicine names, active ingredients, formulations, strengths, amounts, routes, timing, course, prescriber or issuer, warnings, and instructions retain their source form. Phi can discuss need, offer, use, effect, questions, and the person's decision around that record. Base `nepha` names medicine and Medical vocabulary can discuss dose, administration, treatment, benefit, adverse effect, consent, and refusal. None of those words can safely reconstruct the exact product and instructions a person received. |
| `CV-NET-01` | net, web, network, system, and ordinary connected structures | Compositional | base structural and relational vocabulary | `mera`, `niro`, `phaliso`, `terura`, `lorea`. `mera` names flexible open mesh, `niro` an interconnected strand structure, `phaliso` the relations among connected points or participants, and `terura` a bounded interacting whole selected for analysis. The English words overlap, but Phi can choose the structure actually meant. |
| `CV-NET-02` | exact network names, addresses, protocols, accounts, services, and identifiers | Source-bound | exact technical or service source beside a Phi network account | Network and service names, addresses, protocols, versions, account names, credentials, and identifiers retain their source form. Passwords and other secret credentials do not enter Phi examples merely to demonstrate the boundary. Phi can describe participants, connections, access, failure, repair, and governance around a network. The name or identifier that lets a device or person find the intended network remains in its own system. |
| `CV-RESOURCE-01` | resource, material, supply, stock, commons, asset, and waste classifications | Compositional | base resource vocabulary with established module terms | `panuri`, `muralo`, `sephori`, `muphera`, `laenu`, `whemori`, `rolia`. `panuri` treats something as available for a purpose, `muralo` names matter in use, `sephori` the act of supply, `muphera` an available stock, `laenu` a commons and its governance, and `whemori` a waste classification. Access, authority, ownership, condition, and worth remain separate claims. |
| `CV-SACRED-01` | temple, shrine, sacred grove, pilgrimage place, sanctuary, and other revered or protected places | Compositional | base place, sacredness, building, refuge, and ritual vocabulary | `thunepa`, `thoepa`, `thelui`, `lokue`, `thelumo`. `thunepa` covers a particular place regarded as sacred, `thoepa` the wider sacred quality, and `thelui` a place set apart for refuge or protection. Physical form, customary use, pilgrimage, ceremony, and protection can be stated when they matter instead of importing one tradition's place hierarchy into the base lexicon. |
| `CV-SACRED-02` | exact sacred-site names, traditional designations, religious place classes, access rules, sanctuary law, and asylum status | Source-bound | source tradition, community, institution, or law beside a Phi account | Site names, traditional and religious designations, lineage or community accounts, access rules, sanctuary provisions, asylum and refugee statuses, and issuing authorities retain their source form. A relevant community may also accept a Phi-form onym under the name charter. Phi can report who regards a place as sacred, how it is approached, and what refuge is promised. It does not replace a community's own name for the place or a legal source that establishes a status and its limits. |
| `CV-ROLE-01` | exact counselling, custodial, academic, religious, and traditional role titles | Source-bound | source institution, profession, lineage, or community beside an ordinary Phi role description | Professional titles, licences, appointments, ranks, credentials, affiliations, lineage roles, traditional honorifics, duties, and jurisdictions retain their source form. An accepted Phi-form onym may accompany a personal name but does not alter the role record. `menua`, `woru`, `phewo`, and `thonua` name broad roles without importing licence, rank, jurisdiction, lineage, or authority. Phi can describe the person's actual guidance, keeping, inquiry, or practice around the exact title. |
| `CV-SECRET-01` | passwords, access credentials, security classifications, sealed records, and legally protected information | Source-bound | the access, security, legal, or institutional source that gives the information effect | Classification labels, access rules, record identifiers, and legal protections retain their source form. Passwords, keys, tokens, and other secret credentials stay outside Phi prose and examples; Phi can discuss their holder, access boundary, loss, or disclosure without exposing their contents. `kupela` names deliberately withheld information, `mirewu` a chosen access limit, `kupe` concealment, and `sirelu` disclosure. None of them reproduces a credential or proves the legal and technical effect of a classification. |
| `CV-WEATHER-01` | hail, sleet, drizzle, wet or melting snow, rainstorm, snowstorm, and thunderstorm | Compositional | base expressions | See the complete decision under [Landscape, waters, sky, and weather](#landscape-waters-sky-and-weather). |
| `CV-THING-01` | thing, object, entity, matter, stuff, situation, topic, and other general referents | Compositional | base general-reference, material, event-noun, and discourse vocabulary | `thena`, `muralo`, `shareo`, `sherewa`, `sirami`. `thena` supplies broad reference when a kind is unknown or irrelevant, `muralo` asks what matter is in use, and ordinary event nouns name acts or situations. A discussion can name the actual claim, question, event, or record rather than asking one general root to copy every sense of English 'thing' and 'matter'. |
| `CV-VALUE-01` | importance, priority, merit, deservingness, dignity, worth, preciousness, and treasure | Compositional | base value and worth vocabulary with Work priority where needed | See the complete decision under [Reason, belief, ritual, and value](#reason-belief-ritual-and-value). |
| `CV-SETTLE-01` | hamlet, village, town, city, neighbourhood, and settlement | Compositional | base settlement, scale, place, home, and community vocabulary | `silawo`, `whalo silawo`, `sila`, `womu`, `lokue`. `silawo` names several homes or households gathered in one locality, and `whalo silawo` makes scale explicit when English would say town or city. `sila` centres the community, `womu` a home, and ordinary place relations can describe a neighbourhood. Phi keeps this human-scale view unless an exact civic classification is doing real work. |
| `CV-SETTLE-02` | exact settlement names, municipal status, jurisdiction, boundaries, population records, and civic identifiers | Source-bound | map, civic, legal, statistical, or community source beside a Phi place account | Place names, municipal categories, jurisdictional terms, boundaries, population records, addresses, service areas, and civic identifiers retain their source form. A place may also bear an accepted Phi-form onym under the name charter. Phi can describe a settlement's homes, people, scale, paths, services, and relationships. The source classification remains necessary when a boundary, legal power, address, service area, or official identity depends on it. |
| `CV-MESH-01` | screens, filters, grids, and exact mesh classes beyond an ordinary net | Deferred | Household, Ecological, Systems, Work, or exact source material according to function | See the complete decision under [Tools, travel, and practical objects](#tools-travel-and-practical-objects). |
| `CV-EDU-01` | courses, curricula, schools, grades, and educational standing | Deferred | a possible Learning and Knowledge Practice module plus exact source material | See the complete decision under [Learning, practice, guidance, and sustained effort](#learning-practice-guidance-and-sustained-effort). |
| `CV-MAT-08` | brick, adhesive, fuel, card or cardboard, and alloy | Compositional | base and cross-module compounds | See the complete decision under [Materials, substances, fibres, and fire](#materials-substances-fibres-and-fire). |
| `CV-MAT-09` | paint, varnish, mortar, cement, plaster, asphalt, coal, charcoal, and related material products | Deferred | Household, Work, Systems, Ecological, or shared base according to connected use | See the complete decision under [Materials, substances, fibres, and fire](#materials-substances-fibres-and-fire). |

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
| `CV-AEST-03` | style and characteristic aesthetic form | Implemented | base | See the complete decision under [Aesthetic and formal qualities](#aesthetic-and-formal-qualities). |
| `CV-SHAPE-01` | straight as an ordinary shape quality | Implemented | base | See the complete decision under [Aesthetic and formal qualities](#aesthetic-and-formal-qualities). |
| `CV-SHAPE-02` | round as an ordinary shape quality | Compositional | base expression | See the complete decision under [Aesthetic and formal qualities](#aesthetic-and-formal-qualities). |
| `CV-CONFLICT-01` | generic conflict and direct roots for violence, fighting, attack, defence, hunting, and killing | Declined | no lexical placement | See the complete decision under [Ethics, care, and candour](#ethics-care-and-candour). |
| `CV-AFFECT-02` | guilt, anxiety, disgust, excitement, relief, frustration, and boredom | Implemented | base | See the complete decision under [Core emotion inventory](#core-emotion-inventory). |
| `CV-CLEAN-01` | dirty, contaminated, spoiled, and rotten | Implemented | base and established modules | See the complete decision under [Cultivation, abundance, and wildness](#cultivation-abundance-and-wildness). |
| `CV-LOSE-01` | lose and misplace a thing | Implemented | base | See the complete decision under [Knowledge, understanding, belief, and memory](#knowledge-understanding-belief-and-memory). |
| `CV-INTAKE-01` | lick and suck | Implemented | base | See the complete decision under [Breath, intake, and expulsion](#breath-intake-and-expulsion). |
| `CV-AIM-01` | physical alignment towards a selected point or object | Compositional | base construction usable in Work | See the complete decision under [Contact, force, and placement](#contact-force-and-placement). |
| `CV-SWELL-01` | swell and shrink | Implemented | base | See the complete decision under [Change, continuity, repair, and renewal](#change-continuity-repair-and-renewal). |
| `CV-COVER-01` | cover and uncover | Implemented | base | See the complete decision under [Relation, boundaries, and remaining practical acts](#relation-boundaries-and-remaining-practical-acts). |
| `CV-BODY-07` | mucus, body fat, and flesh | Implemented | base | See the complete decision under [Body, anatomy, and bodily condition](#body-anatomy-and-bodily-condition). |
| `CV-ANIMAL-01` | bee, wolf, deer, bear, frog, spider, cow, and goat | Implemented | base | See the complete decision under [Personhood, generations, kinship, and social belonging](#personhood-generations-kinship-and-social-belonging). |
| `CV-WRITE-01` | page, ink, letter, and message | Implemented | base roots and registered compounds | See the complete decision under [Measurement, comparison, meaning, and record](#measurement-comparison-meaning-and-record). |
| `CV-FOOD-01` | rice and tea | Implemented | base | See the complete decision under [Cultivation, abundance, and wildness](#cultivation-abundance-and-wildness). |
| `CV-FOOD-02` | nut | Compositional | base compound | See the complete decision under [Cultivation, abundance, and wildness](#cultivation-abundance-and-wildness). |
| `CV-MEET-01` | meet as a verb | Implemented | base | See the complete decision under [Core speech and conversation](#core-speech-and-conversation). |
| `CV-PHIL-01` | emergence, correlation, inference strength, and further responsibility distinctions | Deferred | Philosophical Reasoning, Systems, or shared base | See the complete decision under [Reason, belief, ritual, and value](#reason-belief-ritual-and-value). |
| `CV-SYSTEMS-02` | feedforward and later systems relations | Deferred | Systems and Shared Infrastructure | When an original system explanation needs anticipatory control often enough that ordinary input, model, and control clauses obscure the relation. The first Systems pass retained feedback and control but left feedforward and other less common relations for connected technical use. |
| `CV-ECON-01` | money, prices, wages, debt, profit, taxation, budgets, and monetary accounting | Declined | no Phi lexical roots; exact source records remain available beside a Phi account | See the complete decision under [Reason, belief, ritual, and value](#reason-belief-ritual-and-value). |
| `CV-MED-SENSITIVE-01` | mental health, reproductive health, sexuality, gender, abuse, and coercive care | Deferred | base, Medical, or another sensitive domain profile | When separate scenarios are ready for each area, with autonomy, varied lived experience, refusal, power, and exact source terminology kept visible. The first Medical pass reserved these areas because they need language for self-description, consent, harm, care, and source-defined classifications without treating any one experience as the norm. |

## Prompt sources

These inventories were used only to recover questions that an earlier batch might have overlooked. They do not define Phi's semantic structure and do not turn the register into an English relex checklist.

- [Concepticon: Dunn 2012 207-item list](https://concepticon.clld.org/contributions/Dunn-2012-207): Used as a cross-linguistic prompt for common concepts, not as a list Phi must lexicalise.
- [SIL Comparative Lists of Semantic Domains, version 4](https://semdom.org/): Used to widen the audit beyond the headings that the earlier migration happened to choose.
