# Content vocabulary coverage

This ledger checks whether Phi's completed semantic batches cover the concepts they set out to handle. It looks only at content vocabulary. The grammar and its closed function word systems have already been migrated and validated; a missing content distinction is not a reason to reopen particles, conjunctions, prepositions, or other function classes.

Completeness here does not mean reproducing an English dictionary. English can suggest a question, but it does not decide which distinctions Phi should lexicalize. A field is adequate when ordinary Phi can preserve its useful contrasts through an existing root, a natural construction, an established grammatical rule, or a deliberate decision to leave specialized precision to a module or separate source material.

The initial retrospective covers the six semantic batches completed in PRs #346 through #351. It records possible gaps without coining words. A `REVIEW` row sends a question to the maintainer before any root is coined.

## Status vocabulary

| Status | Meaning |
|---|---|
| **COVERED** | Existing vocabulary directly handles the ordinary distinction. |
| **COMPOSITIONAL** | Existing words or grammar express the distinction naturally enough that no dedicated root is presently needed. |
| **REVIEW** | Phi can work around the concept, but corpus pressure or a clean semantic distinction makes dedicated vocabulary worth considering. |
| **DEFERRED** | The concept belongs to a later semantic batch, an optional module, or a scenario that can establish whether it matters. |
| **SETTLED** | Canon deliberately closes the lexical question. |

Work package states in the next table use the [roadmap status vocabulary](roadmap.md#status-vocabulary).

## Current position

| Work package | Status | Result or next action |
|---|---|---|
| Retrospective audit of completed content batches | **DONE** | All six concept maps and their findings appear below. |
| Review concepts with direct corpus pressure | **DONE** | Base `pukeri` damage, `rohemi` wear down, `huwa` weak, and `tinako` rigid now carry the four accepted distinctions. |
| Test concepts without corpus pressure | **NEXT** | Base `shumeko` resolves adhesion, base `selawi` resolves traction, and base `patoku`, `larewu`, and `heshowa` resolve ordinary material phase; neutral measurement still needs a practical test. |
| Resume inherited content prose migration | **READY** | Continue after the review queue and apply the coverage gate to every new semantic batch. |

## Batch overview

| Semantic batch | Migration | Coverage status | Open question |
|---|---|---|---|
| Core material qualities | [PR #346](https://github.com/dcellison/phi/pull/346) | **COVERED** | `shumeko` covers surface adhesion, `selawi` covers low traction, and the three base phase nouns classify ordinary material states. |
| Environmental and spatial qualities | [PR #347](https://github.com/dcellison/phi/pull/347) | **COVERED** | No obvious base vocabulary gap remains after the addition of `sukaro` (hot). |
| Size, extent, and distance | [PR #348](https://github.com/dcellison/phi/pull/348) | **REVIEW** | Neutral nouns for overall size, length, and distance may still be useful. |
| Pace, motion, and equilibrium | [PR #349](https://github.com/dcellison/phi/pull/349) | **COVERED** | Changes of rate remain ordinary constructions. |
| Color | [PR #350](https://github.com/dcellison/phi/pull/350) | **SETTLED** | Canon closes the system at seven adjective roots and an open construction built from a source noun and color. |
| Strength, deformation, and recovery | [PR #351](https://github.com/dcellison/phi/pull/351) and D020 | **COVERED** | Four base roots now close the damage, wear, weakness, and rigidity questions exposed by the retrospective. |

## Audit method

1. Define the field through physical or communicative tests rather than through a list of English synonyms.
2. Inventory existing roots, quality and event nouns, and registered compounds. Check available constructions, module vocabulary, and relevant corpus uses too.
3. Check opposing values, intermediate conditions, changes of state, and resulting states where the field actually distinguishes them.
4. Mark a concept `REVIEW` only when its meaning remains distinct after composition or when Phi texts repeatedly work around it.
5. Keep exact standards, measurements, taxonomies, and source identities outside Phi when their original form matters.
6. Record the decision before a semantic batch closes, even when the decision is to leave the concept compositional.

## Core material qualities

This field asks how an object responds to force, contact, contents, and light. The migrated batch covers six paired everyday scales cleanly. The remaining questions concern kinds of contact and matter that those scales never claimed to describe.

| Conceptual test | Current Phi coverage | Status | Finding |
|---|---|---|---|
| Force needed to lift or support | `tumoa` (heavy), `phelo` (light) | **COVERED** | Context supplies the comparison, so Phi does not need a fixed weight boundary. |
| Response to ordinary pressure | `kethua` (hard), `wuloe` (soft) | **COVERED** | Hardness concerns resistance to indentation; softness concerns yielding contact. |
| Surface regularity | `keloa` (rough), `helu` (smooth) | **COVERED** | These words report bumps, ridges, and continuity rather than beauty or loudness. |
| Readiness to cut or pierce | `tiso` (sharp), `shoru` (dull) | **COVERED** | The pair works for edges and for established cognitive extensions. |
| Substance across a cross-section | `theru` (thick), `lemi` (thin) | **COVERED** | Width and depth remain separate dimensions. |
| Contents relative to a boundary or capacity | `pheno` (full), `whemoa` (empty) | **COVERED** | Completeness, sufficiency, zero, and absence remain distinct. |
| Visibility through matter | `nuwi` (clear), illumination words, and ordinary negation | **COMPOSITIONAL** | A separate transparent or opaque pair would duplicate coverage unless practical use exposes a narrower distinction. |
| Adhesion to another surface | `shumeko` (sticky), with `lorea` (connect) for the resulting relation | **COVERED** | The adjective names a material or surface that clings after contact and resists easy separation. Its quality noun supplies stickiness or adhesion. |
| Low traction or easy sliding | `selawi` (slippery) | **COVERED** | The adjective describes contact that permits easy sideways sliding during ordinary use. A floor is understood against foot contact, and a tool against the hand. |
| General material phase | `patoku` (solid), `larewu` (liquid), and `heshowa` (gas) | **COVERED** | The three nouns classify material under the conditions at hand. They leave substance identity, mechanical qualities, and finer specialist phases to their own words or exact source material. |
| Interior structure | `whemoa` (empty) covers an unfilled bounded place | **DEFERRED** | Hollow, porous, and dense concern structure rather than the six migrated scales. They belong in a later shape or material structure audit. |

The batch is complete. `shumeko` covers adhesion, `selawi` covers slipperiness or low traction, and the phase nouns distinguish ordinary solids, liquids, and gases. Finer classifications remain available through connected specialist use.

## Environmental and spatial qualities

This field now has a four-step thermal scale and paired coverage for moisture, illumination, and depth. The addition of `sukaro` (hot) repaired the one conspicuous hole in an otherwise coherent group.

| Conceptual test | Current Phi coverage | Status | Finding |
|---|---|---|---|
| Temperature felt in ordinary life | `sukaro` (hot), `sulae` (warm), `neri` (cool), `pelui` (cold) | **COVERED** | The four roots preserve intense and moderate ranges without pretending that everyone experiences one fixed threshold. |
| Moisture in air, surfaces, or material | `wirua` (wet), `kurathi` (dry) | **COVERED** | `wirua` already reaches dampness, soaking, wet weather, and moisture-laden air; degree and context supply amount. |
| Amount of light | `keru` (bright), `nuelo` (dark) | **COVERED** | `pholuo` (luminous), `horae` (radiant), and `shomelu` (shadow) add source and pattern where needed. |
| Distance below a surface | `nulo` (deep), `saphei` (shallow), `nusho` (depth) | **COVERED** | Depth remains distinct from thickness and vertical height. |
| Changes involving these qualities | `kelu` (become), the causative, and specific verbs such as `therapi` (boil) | **COMPOSITIONAL** | Phi can state becoming hot, cooling, drying, wetting, freezing into ice, or boiling without storing a separate verb for every transition. |
| Exact temperature, humidity, or illumination as a measured parameter | System state, source measurements, and contextual quality statements | **DEFERRED** | Neutral measurement nouns may help technical work later, but their absence does not leave ordinary environmental speech without hot, wet, or bright. |

No further base root is an obvious omission in this batch. Technical measurement language can return through Systems or Ecological use rather than enlarging the daily scale in advance.

## Size, extent, and distance

Phi divides spatial judgement by the dimension a speaker is actually considering. One general opposition between large and small does not have to do every job.

| Conceptual test | Current Phi coverage | Status | Finding |
|---|---|---|---|
| Overall scale or amount | `whalo` (large), `thiku` (small) | **COVERED** | The comparison remains contextual and can apply beyond physical objects. |
| End-to-end extent or duration | `laeno` (long), `teku` (short) | **COVERED** | One pair handles paths and periods without confusing length with height. |
| Side-to-side extent | `losha` (wide), `hieru` (narrow), `lonai` (width) | **COVERED** | The dimension has adjectives and a neutral measurement noun. |
| Vertical extent or position | `raelu` (tall), `mulu` (low), `raeli` (height) | **COVERED** | Phi does not need separate roots for tall extent and high position; `raelu` carries both. |
| Inward or downward extent | `nulo` (deep), `saphei` (shallow), `nusho` (depth) | **COVERED** | The environmental batch completes this spatial axis. |
| Proximity | `noshi` (near), `wuero` (far), with established near and far prepositions | **COVERED** | Adjectives describe the quality, while grammar introduces an explicit reference object. |
| Intermediate or equal extent | Context, comparison, degree, and `kolo` (equal) | **COMPOSITIONAL** | A compulsory medium-sized root would add an English label where an unmarked contextual middle often does the work. |
| Neutral measurement dimensions | `raeli` (height), `lonai` (width), and `nusho` (depth) exist; quality nouns supply longness, largeness, nearness, and farness | **REVIEW** | Phi has no unambiguous neutral nouns for overall size, length, or distance. A measurement scenario should test whether the adjective quality nouns are read naturally as dimensions or only as marked qualities. |

The adjective system is complete for ordinary comparison. The remaining question is narrower: whether measurement and craft need neutral dimension nouns parallel to height, width, and depth.

## Pace, motion, and equilibrium

This group separates rate from movement, then keeps variation and disturbance apart. Proportion and agitation have their own words. Several English words that look like missing opposites turn out to be plain changes or negations once those axes are kept apart.

| Conceptual test | Current Phi coverage | Status | Finding |
|---|---|---|---|
| High or low rate | `reshi` (fast), `sheru` (slow), `thimelo` (pace) | **COVERED** | Speed says nothing by itself about care, attention, or steadiness. |
| Movement and its absence | `roke` (move), `moesha` (still), `therilu` (rest) | **COVERED** | Stillness concerns motion; rest concerns an activity or body's pause. |
| Variation through time | `kolu` (steady), `helui` (change), `telui` (rhythm), `sena` (pattern) | **COVERED** | A steady course may be fast or slow, and a repeated rhythm need not be motionless. |
| Survival of disturbance | `mureo` (stable), `thuroi` (resilient) | **COVERED** | Stability retains a state; resilience recovers after disruption. |
| Equilibrium or workable proportion | `weilo` (balanced), `malomi` (balance) | **COVERED** | Physical equilibrium and competing needs share the word without becoming moral approval. |
| Agitation | `shena` (calm), `wipha` (restless), `noalu` (tranquil) | **COVERED** | Calm and restlessness can occur without a change in visible motion. |
| Acceleration and deceleration | `reshi kelu` (become fast), `sheru kelu` (become slow) | **COMPOSITIONAL** | The transparent state change says what happened without requiring two dedicated verbs in base vocabulary. |
| Sudden or gradual change | `tiroe` (instant), rate words, periods, and change clauses | **COMPOSITIONAL** | A scenario can state how long the transition took and how quickly it proceeded. No current text shows pressure for dedicated roots. |

No obvious everyday gap remains here. Future prose can reopen a distinction if the composition becomes clumsy, but the present system covers the field without equating mindful speech with slowness.

## Color

Color is the one retrospective field whose boundary is already settled in canon. Seven adjective roots cover the recurring perceptual categories, and an open noun construction names other hues from a source that carries them.

| Conceptual test | Current Phi coverage | Status | Finding |
|---|---|---|---|
| Core hue adjectives | `nuko` (black), `whilo` (white), `rulo` (red), `liro` (green), `soriu` (yellow), `shilu` (blue), `mureli` (brown) | **SETTLED** | Canon permits no eighth color adjective root. |
| Color as a property | `welisha` (color) | **COVERED** | A source noun before `welisha` names a hue without pretending that every community divides the spectrum alike. |
| Recurring additional hues | `kerou welisha` (gray), `thero welisha` (orange), `horathe welisha` (pink), `norawhi welisha` (violet or purple) | **SETTLED** | These registered compounds preserve their stone, fire, dawn, and dusk sources. |
| Bright and dark shades | `keru` (bright), `nuelo` (dark), followed by a hue | **COMPOSITIONAL** | Illumination modifies color without adding another root. |
| Exact color standards or source-specific names | Separate source material plus a Phi description | **COMPOSITIONAL** | Exact identity remains outside Phi when a standard, pigment, product, or tradition-specific label matters. |

This audit records the closure rather than reopening it. A future text may add another registered compound built from a source and `welisha`, but it will not add an eighth adjective root.

## Strength, deformation, and recovery

The migrated words now separate force from construction and susceptibility to damage from the ability to change shape. Recovery has its own test. That sharper map also exposes several places where older texts borrowed a neighbour because the intended word was absent.

| Conceptual test | Current Phi coverage | Status | Finding |
|---|---|---|---|
| Force exerted or withstood | `kema` (strong) | **COVERED** | The word reaches bodies, materials, resolve, and sensory intensity while remaining distinct from sturdy construction. |
| Construction under expected use | `keruko` (sturdy), `pheru` (endure) | **COVERED** | Sturdiness concerns how something is built; endurance can state that it continues through time or difficulty. |
| Susceptibility to comparatively small force | `welua` (fragile) | **COVERED** | Fragility does not mean general weakness or softness. |
| Bending or adaptation without damage | `luwi` (flexible) | **COVERED** | The same root can describe material and a plan that changes without losing purpose. |
| Recovery after disruption | `thuroi` (resilient), `shiroka` (repair), `talome` (restore), `helanu` (recover) | **COVERED** | The adjective covers capacity; the verbs distinguish technical repair, restoration, and medical recovery. |
| Lack of force or capacity | `huwa` (weak), contrasted with `kema` (strong) | **COVERED** | Weakness now names relatively little capacity to exert or withstand the force relevant to a situation. `welua` remains fragility rather than doing two jobs. |
| Resistance to bending or rearrangement | `tinako` (rigid), contrasted with `luwi` (flexible) and `kethua` (hard) | **COVERED** | Rigidity concerns resistance to bending or adjustment; hardness remains resistance to indentation. The adjective also extends to plans and procedures with little room to adjust. |
| General damage and damaged condition | `pukeri` (damage), with `pukate` (break), `kaworu` (injury), `kiphira` (fault), and `thonuki` (fail) retaining narrower work | **COVERED** | The intransitive root names adverse change in condition or function without requiring complete breakage. Its event noun supplies damage, and the causative can name what caused it. |
| Gradual wear through use or time | `rohemi` (wear down) | **COVERED** | Wear now names change accumulated through use or exposure without deciding that the result is harmful or unusable. Its event noun supplies wear. |
| Brittle response | `kethua` (hard) together with `welua` (fragile) | **COMPOSITIONAL** | Glass gives the model: it resists indentation and still cracks under a small impact. |
| Elastic response | `luwi` (flexible) together with `thuroi` (resilient) | **COMPOSITIONAL** | One word supplies shape change without damage and the other supplies return toward a workable state. |
| Toughness or durability | `kema` (strong), `keruko` (sturdy), `luwi` (flexible), and `pheru` (endure), selected by the actual test | **COMPOSITIONAL** | English gathers several material behaviours under these labels. The intended test determines which Phi word fits. |
| Deformation as an event | `helui` (change), `kire` (shape), `norelu` (form), and state vocabulary | **COMPOSITIONAL** | Technical discussion can state the changed shape and conditions. A dedicated term belongs in Systems or Work only if connected use needs it. |

The four direct review items now have base roots. Their definitions keep the axes separate: a thing may be damaged without breaking, worn without being harmed, weak without being fragile, or rigid without being hard. The remaining questions below still need connected use before Phi decides whether they deserve roots.

## Resolved review decisions

Corpus pressure and the sharper semantic map support four base roots. None carries a module field because each distinction belongs in ordinary material, household, ecological, and reflective speech.

| Concept | Decision | Boundary kept visible |
|---|---|---|
| General damage | `pukeri`, an intransitive verb whose event noun supplies damage | `pukate` is complete breakage; `kaworu` is bodily injury; technical faults and failures retain their own roots. |
| Gradual wear | `rohemi`, an intransitive process verb whose event noun supplies wear | Wear accumulates through use or exposure and may leave a thing useful; damage says its condition or function became worse. |
| Weak | `huwa`, a contextual adjective for relatively little force | `welua` remains susceptibility to damage, and uncertainty in evidence keeps its own vocabulary. |
| Rigid | `tinako`, an adjective for resistance to bending or adjustment | `kethua` concerns indentation, while `luwi` concerns change in shape or arrangement without damage. |

## Scenario decisions and queue

Three scenario decisions are complete:

| Concept | Decision | Boundary kept visible |
|---|---|---|
| Sticky or adhesive | Base adjective `shumeko`; its quality noun supplies stickiness or adhesion | `wirua` remains moisture, `lorea` remains the resulting connection, and relational `nolami` does not acquire the physical English homonym. |
| Slippery or low traction | Base adjective `selawi`; its quality noun supplies slipperiness or low traction | `helu` remains surface regularity, `wirua` remains moisture, `roke` remains actual movement, and `pukea` remains the practical judgement of danger. |
| Solid, liquid, and gas | Base nouns `patoku`, `larewu`, and `heshowa` | Substance words identify what the material is; `mirela` selects an analytical state; `kaero` names a stage in a process. Finer categories can enter through connected module use or exact source material. |

One question remains without comparable corpus pressure. A short practical scenario comes before any decision to coin.

| Review item | Evidence | Likely placement if coined | Decision needed |
|---|---|---|---|
| Neutral size, length, and distance nouns | Height, width, and depth have nouns; the other dimensions rely on adjective quality nouns and context. | Base vocabulary | Test measurement, route, and craft sentences for ambiguity before adding parallel roots. |

Hollow, porous, and dense remain deferred to a later shape and material structure field. They are recorded here so that absence is not mistaken for a completed decision.

## Coverage gate for future batches

Every future content batch follows this sequence before its migration PR closes:

1. Add the batch to this ledger with its intended semantic axes.
2. Inventory existing roots, grammatical derivations, and registered compounds. Check module coverage and active corpus paraphrases too.
3. Test opposites, intermediate conditions, changes, and resulting states only where the field itself makes those distinctions useful.
4. Classify every plausible gap as covered, compositional, review, deferred, or settled.
5. Bring review items to the maintainer before coining. A missing English headword alone never satisfies this step.
6. Implement accepted roots in their own bounded vocabulary work. Each addition needs complete schema fields and the required prose passes. Run collision checks before coinage; examples and generated references follow, and the validator closes the implementation.
7. Record deliberate non-coinage just as clearly as coinage, then mark the batch closed for coverage.

The gate applies only to content vocabulary. Phi's closed grammar remains closed unless connected use reveals an actual grammatical failure, which is a separate language-design question rather than a vocabulary-coverage result.

## Resume point

The retrospective mapping and its four direct lexical decisions are complete. Base `shumeko` closes adhesion, base `selawi` closes traction, and base `patoku`, `larewu`, and `heshowa` close material phase. Neutral measurement is the last open scenario; once its decision is recorded, the inherited content prose migration resumes after the strength and recovery batch with this gate in place.
