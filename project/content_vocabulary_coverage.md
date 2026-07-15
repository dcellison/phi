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
| Test concepts without corpus pressure | **DONE** | Base `shumeko` resolves adhesion, base `selawi` resolves traction, base `patoku`, `larewu`, and `heshowa` resolve ordinary material phase, and base `ponalu`, `waleru`, and `hirawo` supply the three neutral spatial magnitudes. |
| Sensory and perceptual qualities | **DONE** | Fifteen inherited entries now use the target prose contract. `pothu` (stink) remains unchanged while its lexical framing is reviewed. |
| Aesthetic and formal qualities | **DONE** | Thirteen inherited base adjectives now use the target prose contract, with `mioru` as the already-migrated anchor. Applied ornament remains a review question rather than a hurried coinage. |
| Awareness and epistemic qualities | **DONE** | Fifteen inherited entries now use the target prose contract. The scan of confusion, uncertainty, distraction, non-knowledge, obviousness, and general cognitive ability found no missing base root. |
| Resume inherited content prose migration | **NEXT** | Continue after the awareness and epistemic qualities batch. Each semantic group passes through this coverage gate. |

## Batch overview

| Semantic batch | Migration | Coverage status | Open question |
|---|---|---|---|
| Core material qualities | [PR #346](https://github.com/dcellison/phi/pull/346) | **COVERED** | `shumeko` covers surface adhesion, `selawi` covers low traction, and the three base phase nouns classify ordinary material states. |
| Environmental and spatial qualities | [PR #347](https://github.com/dcellison/phi/pull/347) | **COVERED** | No obvious base vocabulary gap remains after the addition of `sukaro` (hot). |
| Size, extent, and distance | [PR #348](https://github.com/dcellison/phi/pull/348) and D024 | **COVERED** | `ponalu` supplies overall physical size, `waleru` spatial length, and `hirawo` separation between referents. |
| Pace, motion, and equilibrium | [PR #349](https://github.com/dcellison/phi/pull/349) | **COVERED** | Changes of rate remain ordinary constructions. |
| Color | [PR #350](https://github.com/dcellison/phi/pull/350) | **SETTLED** | Canon closes the system at seven adjective roots and an open construction built from a source noun and color. |
| Strength, deformation, and recovery | [PR #351](https://github.com/dcellison/phi/pull/351) and D020 | **COVERED** | Four base roots now close the damage, wear, weakness, and rigidity questions exposed by the retrospective. |
| Sensory and perceptual qualities | [PR #362](https://github.com/dcellison/phi/pull/362) | **REVIEW** | The channels and ordinary qualities are covered. `pothu` remains under review as the dedicated strongly unpleasant odour verb. |
| Aesthetic and formal qualities | [PR #364](https://github.com/dcellison/phi/pull/364) | **REVIEW** | The ordinary distinctions are covered. Phi can describe ornamented work but does not yet name an applied ornament or the act of decorating directly. |
| Awareness and epistemic qualities | [PR #365](https://github.com/dcellison/phi/pull/365) and [PR #366](https://github.com/dcellison/phi/pull/366) | **COVERED** | Direct words and established constructions keep consciousness, attention, truth, accuracy, error, uncertainty, insight, intuition, understanding, and judgement apart without a new base root. |

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
| Neutral measurement dimensions | `ponalu` (size), `waleru` (length), `hirawo` (distance), `raeli` (height), `lonai` (width), and `nusho` (depth) | **COVERED** | The [box, cloth, and road scenario](../documents/evaluation/content_vocabulary_scenario_tests.md#4-the-box-the-cloth-and-the-road-between-villages) establishes the three missing neutral nouns without importing units or extending spatial length into duration. |

The adjective system is complete for ordinary comparison, and the six nouns let a speaker name the magnitude under discussion without choosing an end of its scale. Exact values and units remain separate source material.

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

## Sensory and perceptual qualities

A bell can be heard without being listened to. A warm bowl can be touched, sensed, and felt in three different claims. This field keeps those distinctions intact and separates a sensory channel from the speaker's evaluation of what arrived through it. The difference matters most with smell, where an honest report of aversion can easily become a judgement about a place or person.

| Conceptual test | Current Phi coverage | Status | Finding |
|---|---|---|---|
| General perception without naming one channel | `morae` (sense), with `phaelo` (feel) and `sano` (know) as neighbours | **COVERED** | `morae` reports perceptual detection. `phaelo` gives the bodily or emotional experience, while `sano` makes the resulting knowledge claim. |
| Visual perception and close observation | `nila` (see) and `somela` (observe) | **COVERED** | Ordinary sight uses `nila`; sustained attention to details or patterns uses `somela`. Visual understanding does not need a second English-shaped sense of see. |
| Sound reaching perception and attention directed towards it | `hea` (hear) and `sheluo` (listen) | **COVERED** | Hearing reports reception. Listening adds chosen attention without promising agreement or comprehension. |
| Neutral sound and contextual noise | `shonuwa` (sound) and `kohura` (noise) | **COVERED** | Sound is the broad physical category. Noise is sound heard as irregular, indistinct, or interfering in a particular setting, not a claim that the source lacks pattern or worth. |
| High and low perceived sound intensity | `theisa` (loud), `maeli` (quiet), and quality nouns by rule | **COVERED** | Loudness does not imply aggression, and quietness does not imply calm or stillness. Degree and context locate intermediate volume. |
| Physical contact, tactile information, and felt experience | `palo` (touch), `palethu` (tactile), `phaelo` (feel), and the migrated texture words | **COVERED** | Contact, information available through contact, and the resulting sensation remain three separate facts. The accessibility module keeps `palethu` available where the channel itself matters. |
| Olfactory perception and a neutral odour | `whinu` (smell), including its event noun | **COVERED** | The verb names perception through smell, and the event noun names the odour. A source can possess or give that smell without a second emission verb. |
| Pleasant or source-specific scent | `kaelo whinu` (sweet scent), source nouns before `whinu`, and ordinary clauses about response | **COMPOSITIONAL** | Phi can identify what a scent resembles or how a person responds to it without turning pleasantness into an objective property of every nose. |
| Strongly unpleasant odour | `pothu` (stink), currently a dedicated intransitive verb | **REVIEW** | The distinction is useful for direct warnings and description, but the inherited entry treats aversion as a smell "gone wrong" and invites the contemptuous English use against people. Its one active literary use reports an underground railway carriage. The form and that use remain unchanged while Phi decides whether to redefine the verb contextually or replace it with a `whinu` construction. |
| Flavour perception and a named flavour | `thorima` (taste), its event noun, and source nouns used as descriptors | **COVERED** | `thorima` stays with bodily flavour rather than copying the English homonym for aesthetic judgement. A source such as `morisa` (salt) can describe the flavour directly. |
| Recurring taste qualities | `kaelo` (sweet), `tuko` (sour), `puko` (bitter), and `morisa thorima` (salt taste) | **COVERED** | Three adjectives cover established recurring qualities, while a transparent noun description supplies saltiness. The limited corpus extensions `kaelo whinu`, `kaelo haolu`, and `puko pelui` remain explicit comparisons rather than unrestricted emotional senses. |
| A scientific basic-taste inventory | Exact source taxonomy beside ordinary Phi taste descriptions | **DEFERRED** | Phi need not encode one scientific inventory in base roots. A culinary or medical text can describe a source-linked flavour, preserve an exact taxonomy outside Phi, or expose a recurring distinction later. |
| Visibility and sensory availability | `po nila` (can see), `hewasu` (audible), `palethu` (tactile), and `thewuni` (legible) | **COMPOSITIONAL** | Base grammar states whether someone can see under present conditions. Accessibility vocabulary names the narrower cases where sound, touch, or text must carry usable information for a participant. |

No new root follows from this pass. The useful distinctions already have direct words or ordinary constructions, with one deliberate exception: `pothu` stays in review because Phi needs candour about unpleasant odours without borrowing the contempt that English packs into "stink".

## Aesthetic and formal qualities

A plain bowl can be beautiful, and an elegant mechanism can still be difficult to use. This field keeps those judgements from collapsing into one word of praise. It distinguishes a speaker's response from the form being noticed, then separates qualities of light and composure from questions of exactness or integrity.

| Conceptual test | Current Phi coverage | Status | Finding |
|---|---|---|---|
| General aesthetic appreciation and wonder | `mioru` (beautiful), `kaeli` (like), `woraka` (appreciate), and `waora` (wondrous) | **COVERED** | Beauty is the speaker's aesthetic judgement, liking states preference, appreciation recognizes value, and wonder begins when experience exceeds expectation. None has to stand in for the others. |
| Refinement and flowing form | `phiro` (elegant) and `luwae` (graceful) | **COVERED** | Elegance attends to considered proportion and economy. Grace follows motion, gesture, or a line that seems ready to move. |
| Relation among parts | `koru` (harmonious), `weilo` (balanced), `lei` (harmonize), and `shemoli` (harmonize something) | **COVERED** | Harmony concerns how different parts fit; balance concerns equilibrium or workable proportion. The two verbs distinguish parts harmonizing from someone tuning one thing to another. |
| Character and spread of light | `pholuo` (luminous), `horae` (radiant), and `keru` (bright) | **COVERED** | Luminosity appears held in or steadily given by a source or surface. Radiance reaches outward, while brightness states intensity. |
| Absence of ornament and low complexity | `mueli` (plain), `siloma` (simple), and `ruka` (complex) | **COVERED** | Plainness says ornament is absent. Simplicity and complexity concern how many parts or relations must be followed, so either can occur in decorated or undecorated work. |
| Precision, accuracy, and fit | `kiro` (precise), `telua` (accurate), and `theali` (fitting) | **COVERED** | Precision narrows variation or scope, accuracy agrees with a reference or fact, and fittingness relates a thing to its present context or purpose. |
| Unmixed composition, cleanliness, and clarity | `shiloa` (pure), `hiso` (clean), and `nuwi` (clear) | **COVERED** | Purity concerns mixture in a stated respect. Cleanliness concerns unwanted material, while clarity concerns sight or understanding. `shiloa` does not grade a person's moral worth. |
| Depth and perceptible intensity | `simoe` (rich), `thurai` (vibrant), and `lorua` (abundant) | **COVERED** | Richness concerns concentration or depth within a quality. Vibrancy concerns force that can be perceived, and abundance concerns quantity available. |
| Calm made visible or audible | `thiro` (serene), `shena` (calm), and `noalu` (tranquil) | **COVERED** | Serenity is settled composure in manner or scene. Calm reports low present agitation, while tranquility has remained undisturbed. |
| Integrity and completion | `whoa` (whole) and `sholu` (complete) | **COVERED** | A whole thing holds together as one. A complete set or process has everything its stated requirement calls for. |
| Negative aesthetic response | `mioru ma nai` (is not beautiful), `ma kaeli` (do not like), degree, and the concrete feature being judged | **COMPOSITIONAL** | Phi can own the response and name what prompted it without treating ugliness as an objective property, especially of a person. Connected writing may reopen the question if strong aesthetic aversion repeatedly needs a direct adjective. |
| Applied ornament or decorating | `mueli ma nai` (is not plain), with `noporu` (design), `kire` (shape), `shela` (art), and making verbs | **REVIEW** | Current words can describe the resulting pattern or form, but none directly names an ornament added to a thing or the act of adding it. Art and craft writing should test whether that recurring distinction belongs in base vocabulary or an optional domain. |
| Symmetry and asymmetry | `kolo` (equal), `sena` (pattern), repeated spatial relations, and exact source description | **DEFERRED** | Ordinary description can compare corresponding parts. A dedicated term should wait for connected design or technical use that needs symmetry as one recurring property. |

The thirteen inherited base adjectives in this field now use the target prose contract. Their definitions remove several old shortcuts: purity is composition rather than moral essence, richness is not personal wealth, harmony permits disagreement, and serenity makes no promise about another person's state. No new root is coined in this pass. Applied ornament remains the one direct lexical question.

## Awareness and epistemic qualities

A person can be conscious without attending, aware without understanding, and confident while mistaken. This field keeps those differences visible. It also asks where Phi should use grammar or transparent composition instead of giving every English judgement about a mind its own root.

| Conceptual test | Current Phi coverage | Status | Finding |
|---|---|---|---|
| Conscious experience, directed awareness, and mindful attention | `waeli` (conscious), `selua` (aware), `thesua` (mindful), and `theonu` (attend) | **COVERED** | Consciousness is the presence of experience, awareness notices something particular, mindfulness deliberately attends to the present act, and attending directs focus. None implies the others automatically. |
| Truth, accuracy, and error | `shewo` (true), `telua` (accurate), `phelira` (mistaken), and `kanelu` (err) | **COVERED** | Truth concerns accord with reality, accuracy compares a representation with its reference, mistaken describes a present error, and err names the event of making one. Negated `shewo` supplies false where the context makes that contrast clear. |
| Clarity, clarification, and understanding | `nuwi` (clear), `lilea` (clarify), and `shelomu` (understand) | **COVERED** | Clarity is low obstruction in the material or meaning at hand, clarification changes how something can be followed, and understanding is the resulting cognitive relation. |
| Curiosity, receptivity, and practical opening | `kuelo` (curious), `loetha` (open, receptive), `thilou` (inquire), and `phae` (open) | **COVERED** | Curiosity supplies interest, receptivity allows consideration, inquiry asks, and opening creates access. None grants entitlement to another person's knowledge, attention, records, or body. |
| Insight, intuition, consideration, and wisdom | `seloi` (insightful), `sorai` (insight), `thuni` (intuitive), `hiru` (intuit), `phenui` (thoughtful), and `phue` (wise) | **COVERED** | Insight concerns depth, intuition concerns a non-analytical route, thoughtfulness includes effects on others, and wisdom concerns sound judgement informed by understanding and experience. None guarantees factual accuracy. |
| Foolish action without a permanent person class | `tawimo` (foolish), with the act and circumstances stated | **COVERED** | The adjective can assess an ill-judged choice or a person's conduct at one time. It does not establish a fixed class of foolish people. |
| Puzzlement or confusion | Registered `remo tiwa` (thought-tying), `nuwi` (clear), and `lilea` (clarify) | **COVERED** | The compound already names confusion as thoughts tangled in the present matter. It has carried the distinction repeatedly in *News from Nowhere* and points naturally towards clarification. |
| Non-knowledge, uncertainty, and suspended judgement | `ma sano` (not know), embedded questions, evidential `ho`, and Philosophical Reasoning `whamoi` (doubt) and `norethi` (confident) | **COMPOSITIONAL** | Base Phi can state exactly what is not known or remains in question. The optional module adds stance strength and doubt where sustained reasoning needs them, without forcing those roots into the base lexicon. |
| Attention that stops or turns elsewhere | Negative or cessative marking with `theonu`, followed by the new object of attention when it matters | **COMPOSITIONAL** | Distracted can hide several events: attention ceased, shifted, was interrupted, or never began. Phi can state the event and its cause rather than choosing one vague adjective in advance. |
| Ignorance or lack of awareness | `ma sano` (not know) and negated `selua` (aware) | **COMPOSITIONAL** | These forms identify the missing knowledge or awareness without making ignorance a permanent property of a person. A connected text can name the subject matter and the available access. |
| Recognition versus understanding | `miratu` (recognize) and `shelomu` (understand) | **COVERED** | Recognition connects a present perception with prior knowledge; understanding grasps meaning or relation. A person can do either without doing the other. |
| Obviousness or evident appearance | `nuwi` for a clear meaning or relation, `hi` and `ke` for direct and inferred sources, and `thesori` for evidence | **COMPOSITIONAL** | English obvious often hides whether something was directly seen, inferred, easy to follow, or merely expected by the speaker. Phi states the relevant basis and leaves room for another participant not to share it. |
| Correction and revision | `telua`, `phelira`, `kanelu`, `helui` (change), `lilea`, and established repair forms | **COVERED** | Phi can identify the error, revise the understanding or wording, and reassess accuracy as separate acts. Correction need not become punishment or erasure. |
| Belief supported by reasons or evidence versus intuition | `nohero` (believe), `remotha` (reason), `thesori` (evidence), the evidentials, and `thuni` | **COMPOSITIONAL** | Phi can state a belief, what supports it, how the speaker encountered that support, and whether the judgement arrived intuitively. Intuition is not smuggled in as justification. |
| General intelligence or smartness | `shonela` (learn), `shelomu`, `sano`, `seloi`, `phue`, pace words, and domain-specific skill or expertise | **COMPOSITIONAL** | One scalar label would collapse learning, memory, speed, insight, knowledge, judgement, and practiced skill into a ranking of people. The actual ability or act can be named instead. |

The fifteen inherited entries in this batch now use the target prose contract. No new root follows from the coverage pass. The most tempting apparent gaps already have a stable compound, a direct contrast, or a construction that says more precisely what happened. Connected use can reopen any of those decisions, but none is being kept off the page as an unexamined absence.

## Resolved review decisions

Corpus pressure and the sharper semantic map support four base roots. None carries a module field because each distinction belongs in ordinary material, household, ecological, and reflective speech.

| Concept | Decision | Boundary kept visible |
|---|---|---|
| General damage | `pukeri`, an intransitive verb whose event noun supplies damage | `pukate` is complete breakage; `kaworu` is bodily injury; technical faults and failures retain their own roots. |
| Gradual wear | `rohemi`, an intransitive process verb whose event noun supplies wear | Wear accumulates through use or exposure and may leave a thing useful; damage says its condition or function became worse. |
| Weak | `huwa`, a contextual adjective for relatively little force | `welua` remains susceptibility to damage, and uncertainty in evidence keeps its own vocabulary. |
| Rigid | `tinako`, an adjective for resistance to bending or adjustment | `kethua` concerns indentation, while `luwi` concerns change in shape or arrangement without damage. |

## Scenario decisions and queue

Four scenario decisions are complete:

| Concept | Decision | Boundary kept visible |
|---|---|---|
| Sticky or adhesive | Base adjective `shumeko`; its quality noun supplies stickiness or adhesion | `wirua` remains moisture, `lorea` remains the resulting connection, and relational `nolami` does not acquire the physical English homonym. |
| Slippery or low traction | Base adjective `selawi`; its quality noun supplies slipperiness or low traction | `helu` remains surface regularity, `wirua` remains moisture, `roke` remains actual movement, and `pukea` remains the practical judgement of danger. |
| Solid, liquid, and gas | Base nouns `patoku`, `larewu`, and `heshowa` | Substance words identify what the material is; `mirela` selects an analytical state; `kaero` names a stage in a process. Finer categories can enter through connected module use or exact source material. |
| Neutral spatial magnitudes | Base nouns `ponalu` size, `waleru` length, and `hirawo` distance | Large and small, long and short, and near and far remain contextual judgements; duration, route choice, travel time, capacity, exact dimensions, and source values keep their own expressions. |

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

The retrospective review queue is complete. The inherited content prose migration has now passed through sensory and perceptual qualities, aesthetic and formal qualities, and awareness and epistemic qualities. The next semantic neighbourhood begins after this batch with the same coverage gate in place; `pothu` and applied ornament remain recorded review questions rather than hidden gaps.
