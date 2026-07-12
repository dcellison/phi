# Module overlap assessment

**Status:** First implementation complete. The 61 high-confidence words now carry 83 additional module classifications; the second-pass and base-vocabulary decisions remain open.

A speaker who selects Medical and Bodily Care in the lexicon explorer now sees forty-five words. The list includes the thirty roots coined for care and shared entries such as `hisophi` contaminant, `nomiki` concentration, `perawi` expose, and `mothami` baseline. That is the practical result of this review: words that belong to care are now taught there even when another profile first gave them a lexical home.

## What membership means

A `modules` value is a learning and discovery classification. Grammar and lexical meaning stay the same, and the label carries no authority of its own. Adding a second module says that a learner who chooses either field has a good reason to encounter the word. It does not say that either field owns the word.

Cross-use alone is too weak. Every domain draws on general reasoning and ordinary physical vocabulary. If every useful word received every plausible label, the module selector would become a second version of "any module" and stop helping anyone choose what to study.

## Decision rule

The assessment uses four tests:

1. **Lexical center:** The existing definition directly names a relation inside the second module's charter. A downstream consequence or occasional setting is not enough.
2. **Counterfactual coinage:** If the home module did not exist, the second module would probably need to coin essentially the same distinction rather than rely on a casual borrowing.
3. **Repeated need:** The word supports sustained discussion in the second field, not one scenario or one edge case.
4. **Boundary stability:** The extra label does not stretch the definition, import a professional standard, or imply that one domain settles another domain's questions.

A high-confidence recommendation passes all four. A second-pass candidate passes the first test but remains uncertain on independent need or module size. A base-vocabulary candidate appears too broad, ordinary, or important to safety and agency for any optional module to be its only route.

## Corpus snapshot

The lexicon contains 227 module-classified entries and 310 memberships. The profiles originally coined 22 Philosophical Reasoning roots, 25 Systems and Shared Infrastructure roots, and 30 roots in each of the other six modules. Sixty-one words now belong to more than one learning path; the other 166 retain one classification. Of the 227 words, 102 are cited in at least one profile document outside their original profile. Most of those citations still mark dependencies rather than shared lexical homes.

| Disposition | Words | Meaning |
|---|---:|---|
| High-confidence shared membership | 61 | Implemented with 83 additional classifications. |
| Second-pass candidate | 29 | The overlap is real, but its classification still needs a closer boundary decision. |
| Base-vocabulary review | 11 | Decide whether the module field should disappear instead of multiplying. |
| Retain one module | 126 | Cross-use does not move the word's lexical center. |
| **Total** | **227** | Every current module entry has a disposition. |

The largest corridors are Ecological and Systems with twelve high-confidence assignments, Accessibility and Commons with eleven, Systems and Work with ten, and Ecological and Medical with nine. A contaminant belongs in ecological and medical study; an interface belongs in systems and access. The counts catch that kind of overlap, not mere thematic kinship.

## Implemented shared membership

### From Philosophical Reasoning

| Words | Also classified in | Reason |
|---|---|---|
| `soneho` tradeoff | Commons and Collective Governance; Ecological Systems and Material Life | Allocation decisions and ecological choices often compare valued gains with named burdens. The definition belongs to both deliberative settings without deciding which loss is acceptable. |
| `manawi` compromise | Commons and Collective Governance | A negotiated settlement among different aims is a recurring governance relation, not merely a tool for discussing one. |

### From Systems and Shared Infrastructure

| Words | Also classified in | Reason |
|---|---|---|
| `terura` system, `pherami` depend, `koewi` input, `thirulo` output, `sekaru` transfer, `turelo` feedback | Ecological Systems and Material Life | The same systems vocabulary can trace what enters a watershed, what leaves it, what depends on that flow, and what changes after the flow returns. Each definition applies unchanged. |
| `monaki` component | Ecological Systems and Material Life; Work, Craft, and Repair | Functional parts recur in ecological analysis and in repair work. Calling something a component makes the same system-relative claim in all three modules. |
| `nowiso` interface, `wepanu` redundant | Accessibility and Participation | An access path meets the user at an interface, and redundancy can keep its function available when one path fails. Neither word promises that the path is usable. |
| `masuro` calibrate, `kiphira` fault, `thonuki` fail, `nilaki` inspect, `kisholu` specification | Work, Craft, and Repair | Repair and testing need these distinctions even outside infrastructure-scale systems. Their meanings do not change when the work happens at a bench. |
| `koluri` reliable | Accessibility and Participation; Work, Craft, and Repair | A device that works only on the test bench is not yet reliable. Reliability asks whether its named function continues under stated conditions for a stated duration. |
| `pemaru` hazard | Ecological Systems and Material Life; Medical and Bodily Care; Work, Craft, and Repair | A potential source of harm is a distinct object in environmental exposure, bodily care, and practical work. Hazard names the source before anyone makes the larger risk judgment. |

### From Ecological Systems and Material Life

| Words | Also classified in | Reason |
|---|---|---|
| `hisophi` contaminant, `pekira` toxic, `nomiki` concentration, `perawi` expose | Medical and Bodily Care; Work, Craft, and Repair | A clinic and a workshop may both need to say what is present, how much there is, whether it can harm a body, and who encountered it. The four words draw the same distinctions in either place. |
| `phisuri` sample | Medical and Bodily Care | A selected portion or observation and the limits of its representativeness are ordinary clinical and laboratory concerns. |
| `mothami` baseline, `herani` trend, `somethi` monitor | Medical and Bodily Care; Systems and Shared Infrastructure | A temperature chart and a service log each need a chosen reference, a pattern across observations, and a way to watch change over time. Cause is a separate finding. |
| `reteru` model | Systems and Shared Infrastructure | A purpose-bounded representation of a system belongs naturally in Systems. That module would need the word even without the ecological profile. |
| `whemori` waste, `tukelu` recycle | Household and Daily Life; Work, Craft, and Repair | A kitchen and a workshop both decide what becomes waste and what can be transformed for another use. `tukelu` keeps recycling separate from simple reuse. |
| `lurepa` nutrient | Household and Daily Life; Medical and Bodily Care | Food preparation and bodily care both need this function-relative biological category. It is narrower than food and less exact than a named chemical. |

### From Commons and Collective Governance

| Words | Also classified in | Reason |
|---|---|---|
| `shanewi` notify, `norathu` procedure, `shalori` represent, `tukiro` review, `whetuma` appeal | Accessibility and Participation | Someone cannot take part in a review they were never notified about, and an appeal can fail when the procedure excludes their representative. These words belong in access study without promising successful participation. |
| `loatho` delegate, `sithora` role | Work, Craft, and Repair | A cooperative may delegate a task to someone working in a role, yet the role and the person are not interchangeable. Authority and competence need their own words. |

### From Work, Craft, and Repair

| Words | Also classified in | Reason |
|---|---|---|
| `riporu` task, `rimawu` drudgery, `muphera` stock, `sitawi` inventory | Household and Daily Life | A household has tasks, stock, inventory, and sometimes drudgery. These words make domestic labor visible without assigning it to anyone. |
| `ritako` workload | Accessibility and Participation; Household and Daily Life | Workload names the accumulated weight of work in participation and domestic life. Overload begins when current capacity is exceeded. |
| `noporu` design | Accessibility and Participation; Systems and Shared Infrastructure | Access and technical function are shaped before an artifact is made. Design names the intended form and relations before anyone knows whether the result will work or be accessible. |
| `somaki` test | Accessibility and Participation; Medical and Bodily Care; Systems and Shared Infrastructure | A defined procedure under stated conditions is independently needed in access evaluation, clinical work, and system analysis. Each field decides what the result supports. |
| `luseri` provenance | Ecological Systems and Material Life | Material source and history matter to ecological extraction, reuse, contamination, and attribution without proving ownership or ethical approval. |
| `kisome` assess, `sethoni` handoff | Medical and Bodily Care | A care team assesses evidence for a purpose and hands work or information to the next participant. Diagnosis and acceptance have to be said separately. |
| `thimora` schedule, `lumethi` deadline | Accessibility and Participation | A participation process can exclude someone through its schedule or deadline even when the stated procedure is open. Both words leave room to ask who set the time and who agreed. |
| `pilora` exploit | Commons and Collective Governance | Disproportionate benefit under real power asymmetry belongs to collective and institutional analysis as fully as it belongs to labor criticism. |

### From Accessibility and Participation

| Words | Also classified in | Reason |
|---|---|---|
| `murethi` impairment | Medical and Bodily Care | Bodily, sensory, or cognitive function can be a medical subject without making impairment a diagnosis or disability a disease. |
| `loshenu` clearance, `thosami` compatible | Systems and Shared Infrastructure | A doorway needs clearance; a tool and an interface need compatibility. Source documents keep the exact dimensions and standards. |
| `pushali` overload | Systems and Shared Infrastructure; Work, Craft, and Repair | The definition explicitly covers a person or system exceeding current capacity through input, tasks, or demand. It is distinct from ordinary load and workload. |
| `thunesi` asynchronous | Commons and Collective Governance; Work, Craft, and Repair | Contributions made at different times are a real participation pattern in collective procedure and organized work, not merely an accommodation technique. |
| `misharo` consult, `pharomu` exclude, `wheparu` discriminate, `shaweri` advocate | Commons and Collective Governance | Collective decisions need to distinguish consultation from advocacy and exclusion from discrimination. Commons practice would need all four words independently. |
| `sirelu` disclose | Commons and Collective Governance; Medical and Bodily Care | Information crosses chosen and institutional boundaries in public records, privacy, and care. Disclosure names the crossing; authorization and consent must be stated separately. |

### From Household and Daily Life

| Words | Also classified in | Reason |
|---|---|---|
| `womuri` household | Commons and Collective Governance | A household is a continuing social unit that may pool resources and make decisions about daily work. That makes it relevant to Commons without turning it into an institution. |

## Current module sizes

The implemented set creates 83 additional classifications across 61 words. The vocabulary still contains 227 specialized entries; the generated module views contain 310 memberships because shared words appear wherever speakers need to find them.

| Module | Roots coined here | Incoming classifications | Current memberships |
|---|---:|---:|---:|
| Philosophical Reasoning | 22 | 0 | 22 |
| Systems and Shared Infrastructure | 25 | 9 | 34 |
| Ecological Systems and Material Life | 30 | 10 | 40 |
| Commons and Collective Governance | 30 | 10 | 40 |
| Work, Craft, and Repair | 30 | 18 | 48 |
| Medical and Bodily Care | 30 | 15 | 45 |
| Accessibility and Participation | 30 | 13 | 43 |
| Household and Daily Life | 30 | 8 | 38 |

Work grows the most because it sits between technical systems, household labor, accessibility, material practice, medicine, and governance. That is a property of the domain, not a reason to force its count back toward thirty.

## Second-pass candidates

These 29 words have real cross-domain use, but a second classification may duplicate a dependency list rather than improve the learning path. They remain open because the expanded lists need to be read as learning paths, not merely counted.

| Current module | Words | Possible additional modules | Reason to wait |
|---|---|---|---|
| Philosophical Reasoning | `whakeru` object | Commons and Collective Governance | Commons uses objections often. The open question is whether it should teach the reasoning term itself or list it as a dependency. |
| Systems and Shared Infrastructure | `kelitho` function | Work, Craft, and Repair | Testing and repair revolve around function. Its definition, however, is explicitly system-relative, so Systems may be the clearer teaching home. |
| Systems and Shared Infrastructure | `mirela` state | Ecological Systems and Material Life | Ecological state is useful. Keeping it as a dependency would make clear that the analysis comes from general systems work. |
| Systems and Shared Infrastructure | `poruli` efficient | Ecological Systems and Material Life; Work, Craft, and Repair | Both domains evaluate efficiency, yet the word hides a boundary and a value choice. That may warrant a deliberate Systems dependency rather than two new labels. |
| Systems and Shared Infrastructure | `phelure` store | Household and Daily Life | Households store things for later retrieval. Because the word is this broad, base review may make more sense than a second optional label. |
| Systems and Shared Infrastructure | `seluwhe` outage | Accessibility and Participation | A service outage can remove access. The event itself, however, is infrastructural rather than an access relation. |
| Ecological Systems and Material Life | `morume` decompose | Household and Daily Life | Composting brings decomposition into household practice, while `mukesi` spoil may already cover what the household module needs to teach. |
| Ecological Systems and Material Life | `pesenu` pollute | Medical and Bodily Care; Work, Craft, and Repair | Pollution reaches bodies and workplaces, but the word names an impaired environmental condition. The resulting exposure and harm already have their own terms. |
| Ecological Systems and Material Life | `phaluwe` flood | Accessibility and Participation; Systems and Shared Infrastructure | Floods shape access and infrastructure, though those modules usually discuss the resulting barrier, outage, or failure rather than the hydrological event itself. |
| Commons and Collective Governance | `helolu` redress, `kanuro` decision | Accessibility and Participation | Both matter to access disputes, but their definitions are governance relations used by the access profile. The unresolved question is whether that dependency is enough once Accessibility's 43 words are read together. |
| Commons and Collective Governance | `kanuwa` authorize, `lothoni` accountable, `naseru` obligation | Work, Craft, and Repair | Work institutions need all three. The question is whether these social and normative relations belong beside the work itself or stay in Commons. |
| Work, Craft, and Repair | `rilowa` assign | Commons and Collective Governance; Household and Daily Life | Assignment structures labor in both settings. A second pass should decide whether its expected-performer definition belongs there or stays a Work term applied there. |
| Work, Craft, and Repair | `sephori` supply, `katemu` offcut | Ecological Systems and Material Life | Material movement and remnants have ecological consequences, but neither word by itself makes an ecological claim. |
| Work, Craft, and Repair | `hasoru` pending | Medical and Bodily Care | Results and care decisions can be pending. This could be ordinary workflow vocabulary that Medicine borrows. |
| Work, Craft, and Repair | `someru` supervise, `sikanu` certify | Commons and Collective Governance | Both involve institutions and claimed responsibility. Their definitions point first to practical work and formal judgment of it. |
| Work, Craft, and Repair | `kirero` quality | Systems and Shared Infrastructure | Systems work evaluates criterion-relative quality, but the Systems profile already teaches sharper measures such as function and reliability. Quality may work better there as a dependency. |
| Accessibility and Participation | `hasenu` recess | Commons and Collective Governance | A recess is common in proceedings, but its access value lies in the bounded pause rather than governance status. |
| Accessibility and Participation | `phelotu` format, `sanowu` predictable | Systems and Shared Infrastructure | Technical systems have formats and predictable behavior. The current definitions keep both person- and communication-relative concerns close to Accessibility. |
| Accessibility and Participation | `samethu` equivalent | Philosophical Reasoning; Systems and Shared Infrastructure | Bounded equivalence belongs to comparison and technical fit, but its present examples and contrasts are strongly tied to alternate formats. |
| Accessibility and Participation | `thimelo` pace | Work, Craft, and Repair | Work has pace, yet the word was coined to keep participation and processing time visible rather than to measure productivity. |
| Accessibility and Participation | `wiresu` postpone | Commons and Collective Governance; Work, Craft, and Repair | Moving an activity or decision later is common in both fields. The classification question is whether timing makes it an access word shared outward or a general planning word. |
| Household and Daily Life | `mukesi` spoil | Ecological Systems and Material Life | Spoilage is a material change, but its definition is the household's practical loss of intended use rather than decomposition itself. |
| Household and Daily Life | `muneki` latrine | Medical and Bodily Care; Systems and Shared Infrastructure | Sanitation touches health and infrastructure, while the word itself names the everyday place or fixture rather than a treatment system or clinical relation. |

## Base-vocabulary review

Multiple labels are the wrong answer when a word is too general or too important to hide behind every relevant optional filter. These eleven entries need a separate decision about removing their `modules` field entirely.

| Current module | Words | Why base placement deserves review |
|---|---|---|
| Philosophical Reasoning | `sherewa` claim, `thesori` evidence, `remotha` reason, `kirema` criterion | Phi is intended for philosophical discussion, and these four distinctions also organize ecological, medical, technical, and governance claims. Their present definitions are not tradition-specific. |
| Commons and Collective Governance | `sirami` record | A durable account is ordinary vocabulary for a clinic, a workbench, a household, or a person's own memory before an institution gives it status. |
| Commons and Collective Governance | `kawhera` coerce, `whepelo` retaliate | A speaker may need these words to discuss a coerced choice or retaliation after reporting harm, even outside formal governance study. The core invariant already protects vocabulary needed for safety. |
| Ecological Systems and Material Life | `muralo` material, `panuri` resource | Both are broad relational nouns used throughout work, households, infrastructure, and commons decisions. The question is whether their analytical precision is specialized enough to justify optional study. |
| Ecological Systems and Material Life | `howenu` weather | Weather shapes ordinary decisions about travel and shelter. Climate is the clearly specialized neighbor. |
| Work, Craft, and Repair | `winora` plan | A person can plan a meal, a journey, care, or collective action without entering the Work module. The current definition is not limited to organized work. |

Base promotion changes what a general learner is expected to know. It should not be bundled silently into the mechanical overlap patch.

## Why the other words stay single

The 126 retained entries are not isolated. They remain available to every speaker and may appear in every profile. Their one module label still names the best learning home.

| Home module | High-confidence shared | Second pass | Base review | Retain one module |
|---|---:|---:|---:|---:|
| Philosophical Reasoning | 2 | 1 | 4 | 15 |
| Systems and Shared Infrastructure | 16 | 5 | 0 | 4 |
| Ecological Systems and Material Life | 12 | 3 | 3 | 12 |
| Commons and Collective Governance | 7 | 5 | 3 | 15 |
| Work, Craft, and Repair | 13 | 7 | 1 | 9 |
| Medical and Bodily Care | 0 | 0 | 0 | 30 |
| Accessibility and Participation | 10 | 6 | 0 | 14 |
| Household and Daily Life | 1 | 2 | 0 | 27 |
| **Total** | **61** | **29** | **11** | **126** |

Medical contributes no words outward in the first recommendation because its coinages are deliberately scoped to bodily care and the course of illness. It still gains fifteen incoming classifications from measurement, access, systems, and work. Household keeps most of its concrete objects and domestic actions singly classified for the opposite reason: a bottle may be used in a clinic or workshop without becoming medical or craft vocabulary.

The complete retained set is below. Each word may be used anywhere; the table records only its best learning home.

| Home module | Retain one module | Why |
|---|---|---|
| Philosophical Reasoning | `kethira` infer, `kirothe` define, `kithela` valid, `letharo` consistent, `mothare` premise, `natheri` entail, `norethi` confident, `phiketu` contradict, `phisuwa` example, `phiwheki` counterexample, `remole` concept, `remuma` conclusion, `themore` argument, `whamoi` doubt, `whekate` refute | This set names the structure and evaluation of reasoning itself. Other profiles use it without needing a second teaching home. |
| Systems and Shared Infrastructure | `henora` capacity, `ketora` control, `kirowi` signal, `takori` load | Capacity, control, signal, and load are technical system relations. Other profiles have barrier, workload, or overload when those sharper relations are not intended. |
| Ecological Systems and Material Life | `kuramo` drought, `likori` species, `liloni` population, `litero` ecosystem, `liweso` ecological community, `luphano` watershed, `meluri` climate, `menuro` habitat, `munari` sediment, `philima` biodiversity, `wheraku` erode, `wiralu` runoff | Here the vocabulary describes ecological entities and processes, rather than a relation merely borrowed by ecological discussion. |
| Commons and Collective Governance | `helaki` amend, `karami` authority, `kasira` vote, `kirethu` legitimate, `makelu` abstain, `nashaku` enforce, `nasholu` rule, `naweso` consensus, `norulo` jurisdiction, `phanuli` allocate, `phenori` ownership, `punoki` institution, `repora` propose, `shereni` entitlement, `wemari` member | Each word locates action inside collective or institutional relations. Use in work or access does not move that center. |
| Work, Craft, and Repair | `kiranu` qualified, `noraku` blocked, `nukesa` expert, `pokera` competent, `rinoka` project, `thesani` skill, `thunaro` train, `wephari` coordinate, `wepuri` progress | This group describes practical capacity and the organization or status of work. |
| Medical and Bodily Care | `helanu` recover, `hisaro` clinical finding, `katheo` acute, `kaworu` injury, `kithawu` triage, `kithero` diagnose, `mikasu` dose, `mokanu` disease, `morashi` relapse, `nathoku` contraindicated, `nephoru` treat, `nurawi` chronic, `pelaku` severity, `peshiro` infection, `phamori` symptom, `porewi` side effect, `sewaro` transmit, `shorenu` immune, `shuneki` vaccinate, `sonari` isolate, `soranu` screen, `suloru` fever, `teshori` quarantine, `thekamu` intervene, `thephaku` inflammation, `welathi` contagious, `weshaku` outbreak, `whekaro` adverse effect, `whemaki` allergy, `wireki` prognosis | Each definition makes a specifically medical or bodily-care distinction. The module gains useful scientific and procedural words from elsewhere, but its own coinages keep their clear home. |
| Accessibility and Participation | `hewasu` audible, `hinawu` accommodate, `kelasu` usable, `kopharu` barrier, `lokane` accessible, `naphelu` assistive, `palethu` tactile, `ralemi` independent, `runaki` wayfind, `ruweli` access, `shoraku` interpret, `sitheku` transcribe, `thekasi` caption, `thewuni` legible | Access relations and communication forms are the point of this group. A system or institution may use the words, but access is what each definition asks the learner to notice. |
| Household and Daily Life | `kirato` lock, `kolupe` bucket, `komalu` pillow, `lirupa` bag, `lophani` bottle, `lupaki` fold, `molupa` box, `napako` bake, `norupe` spoon, `nurome` meal, `phareme` ingredient, `phelasi` shelf, `phemiru` visit, `pheomu` leftovers, `phurewa` sweep, `phurilo` broom, `sawathi` soap, `seluto` pour, `tapulo` jar, `tapuri` lid, `thekopa` recipe, `therapi` boil, `tholupi` room, `welotu` mix, `wethaki` towel, `wethamo` blanket, `wethate` laundry | A clinic or workshop may have a bottle or broom. The objects and daily actions do not become specialist vocabulary there. |

## Remaining review

The canonical entries, generated reference, module profiles, and Part VII index now distinguish roots coined for a profile from the larger set classified for its learning path. The explorer reads the same `modules` arrays and shows a shared word under every applicable filter.

1. [x] Apply the high-confidence classifications with exact membership counts.
2. [x] Regenerate the module reference and verify every shared word against the explorer's filter rule.
3. [x] Distinguish profile coinage from current membership in profiles and speaker guides.
4. [ ] Re-read the expanded module lists and decide the 29 second-pass candidates by what the learning paths now feel like, not by a target count.
5. [ ] Review the eleven base candidates separately because removing a module field changes the general learning path.

The first implementation stops at the 61 high-confidence words. The expanded lists give the next review something concrete to judge: whether each disputed word belongs in the learning path or should remain a dependency.
