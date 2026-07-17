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
| `CV-WEATHER-01` | hail, drizzle, rainstorm, snowstorm, and thunderstorm | Compositional | base expressions | `kerithe pheralu`, `moli pheralu`, `pheralu kurisha`, `phirenu kurisha`, `horuma kurisha`. Familiar weather subtypes remain transparent combinations of material, intensity, and event. Their exact thresholds and named warning categories come from the weather source in use. |
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
| `CV-PHIL-01` | emergence, correlation, inference strength, and further responsibility distinctions | Deferred | Philosophical Reasoning, Systems, or shared base | When new philosophical arguments or systems explanations need one of the distinctions repeatedly and the existing relations become clumsy or ambiguous. The first philosophical pass named these as later questions rather than completed omissions. |
| `CV-SYSTEMS-02` | feedforward and later systems relations | Deferred | Systems and Shared Infrastructure | When an original system explanation needs anticipatory control often enough that ordinary input, model, and control clauses obscure the relation. The first Systems pass retained feedback and control but left feedforward and other less common relations for connected technical use. |
| `CV-ECON-01` | money, prices, wages, debt, profit, taxation, budgets, and contracts | Deferred | a possible Economic Systems and Provisioning module | When an economic profile receives scenarios that can keep accounting, exchange, obligation, extraction, livelihood, and source-defined legal relations apart. Governance and Work deliberately left wider political economy outside their first passes rather than declaring it unnecessary. |
| `CV-MED-SENSITIVE-01` | mental health, reproductive health, sexuality, gender, abuse, and coercive care | Deferred | base, Medical, or another sensitive domain profile | When separate scenarios are ready for each area, with autonomy, varied lived experience, refusal, power, and exact source terminology kept visible. The first Medical pass reserved these areas because they need language for self-description, consent, harm, care, and source-defined classifications without treating any one experience as the norm. |

## Prompt sources

These inventories were used only to recover questions that an earlier batch might have overlooked. They do not define Phi's semantic structure and do not turn the register into an English relex checklist.

- [Concepticon: Dunn 2012 207-item list](https://concepticon.clld.org/contributions/Dunn-2012-207): Used as a cross-linguistic prompt for common concepts, not as a list Phi must lexicalise.
- [SIL Comparative Lists of Semantic Domains, version 4](https://semdom.org/): Used to widen the audit beyond the headings that the earlier migration happened to choose.
