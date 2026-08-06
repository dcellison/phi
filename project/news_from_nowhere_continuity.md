# News from Nowhere source-to-Phi continuity

This is the maintained continuity record for translating William Morris's *News from Nowhere* into Phi. It is available during source-to-Phi work and cross-chapter review. It records choices that must survive beyond one chapter; chapter-local explanations belong in the chapter notes instead.

The language remains governed by [`canon.md`](../canon.md), the lexicon, and the grammar references. This record applies those authorities to one continuing work. The [development log](development_log.md) supplies the decisions cited below, especially D097 for names and continuing speech, D099 for `toreku`, and D100 for `lomathu`.

## Isolation boundary

This file contains source information: the work's title, source names, narrative relationships, and summaries of translation choices. It may be read while translating Morris into Phi and while comparing Phi across chapters.

It must not be shown to, consulted by, or summarized for a fresh Phi-to-English context. That context receives only the anonymous frozen-Phi reference and packets produced by `scripts/translation_layers.py`, as required by the [translation process](../documents/reference/translation_process.md). The prohibition also covers excerpts from this file copied into a prompt. A source-to-Phi worker may update this record before the Phi freeze; a source-blind reader may not inspect it at any stage.

Do not add source passages, aligned units, exact glosses, derived English, digests, certification evidence, or audit history here. Record a choice only when another chapter may need it.

## Working rules

- Use Phi's complete vocabulary, including optional modules, wherever the distinction fits the source. The novel is not restricted to the base learning path.
- Search the current lexicon and this record before composing around a recurring concept. A real lexical gap may justify ordinary vocabulary development; an exact source identity does not become a gap merely because it stays beside Phi.
- Preserve Morris's participant structure, claim strength, imagery, repetition, logical relations, evidence, modality, aspect, and tone in Phi before any English is derived.
- Keep source-form names, dates, units, technical labels, historical categories, and wordplay in the adjacent source material when canon places them outside Phi. Phi still carries every relation needed to understand why the item matters.
- Validate every complete Phi sentence. Then compare names, recurring descriptions, evidence, and speaker-turn boundaries with earlier chapters before freezing the chapter.

## Recurring people and onyms

Canon's **A translation names its people** ruling governs this table. Formal translated Phi repeats `ne` at every use of an onym. When Morris uses a role or epithet instead of a personal name, Phi translates that role or epithet rather than substituting the onym. A one-time person with no continuing relation needs no newly invented onym; D097's already settled forms remain controlling.

| Source designation | Settled Phi onym | Continuity rule |
|---|---|---|
| Guest; the source also adds William | `ne phemi` | The narrator chooses Guest for himself in chapter 3. William remains exact in Morris. Use the onym from that naming point onward when the source uses Guest as his name. Before that point, and when the source uses traveller, stranger, or guest as a description, preserve the relevant pronoun or description. |
| Dick | `ne kulo` | Use for the recurring guide when the source uses Dick. Source descriptions such as companion, guide, or driver remain descriptions. Outside `ne`, `kulo` retains its ordinary lexical use, guide. |
| Bob; Robert | `ne selomi` | Use for the recurring weaver when the source uses either form of his personal name. When the source says the weaver, use the role description `selomi miona` instead. |
| Boffin | `ne solai` | Use for the character's nickname. Do not replace it with the onym for his different source name. |
| Henry Johnson | `ne keruko` | Use for the same character's stated real name. `ne solai` and `ne keruko` therefore identify one bearer under two distinct source names. The source epithet dustman remains `muhena miona` or another propositionally exact description. |
| Annie | `ne luwae` | Use whenever the source uses Annie. Descriptions based on age, appearance, kinship, or role remain descriptions. |
| Jim | `ne woru` | Use whenever the source uses Jim. Outside `ne`, `woru` retains its lexical use, keeper. |

When a later chapter introduces another recurring person, settle one legal onym at the first point where recurrence is established, check that it follows the productive-name charter, and add it here in the same change. Do not reserve onyms in advance from knowledge of later chapters.

## Recurring places

No place onym is established in chapters 1 through 6. Exact English place names remain in Morris's adjacent wording. Phi refers to the place by the role, visible form, relation, or deixis that the sentence requires; none of the descriptions below silently becomes a proper name.

| Source place | Established Phi treatment | Continuity rule |
|---|---|---|
| The Thames | Use `luphore` with the deictic or spatial relation required by the scene. The current river is often `ha luphore`; the exact name remains with Morris. |
| Hammersmith | Use contextual place reference such as `ha lokue`, then name the relevant function directly. The guest-house may use registered `phemi womu`; its hall or gathering function may use `lona lokue` within a larger description. Hammersmith itself has no fixed Phi alias. |
| Barn Elms | Continue the established `ra welamu lokue`, that place of elms, once the source identity is available beside it. The phrase remains a description, not `ne` material. |
| Epping Forest | Introduce the relevant large forest with `shelira` and its relation, then use `ra shelira` while the referent remains established. Do not turn the description into a source-name substitute outside that context. |
| London | Describe the aspect asserted in the sentence: the great town, the great social place, the old centre, or another explicit relation. Earlier phrases such as `whalo silawo` and `whalo punoa lokue` are propositions, not interchangeable names. |
| Bloomsbury | The present route uses established distal place reference, `ra lokue`. Re-establish the destination when another place could compete for that reference; no Phi alias has been assigned. |

When exact naming is itself an event, Phi may state that someone gave or spoke a place's name without inserting the English token into Phi syntax. Consider a Phi place onym only if later connected prose demonstrates a recurring referential need that deixis and accurate description cannot meet. Record any accepted form here before reusing it.

## Recurring social concepts

| Source concept | Chosen Phi treatment | Boundary to preserve |
|---|---|---|
| The League and its sections | `shalimo` for the continuing alliance; `shalimo phanoi` for one section | The historical label *Anarchist* remains with Morris. State the section's objection to `karami`, authority, when that claim matters. Do not make alliance mean meeting or political doctrine. |
| Society, community, and gathering | `punoa` for a social order or society; `sila` for a community; `lona` for a meeting or gathering | Keep the scale and relation distinct. `lona lokue` is a place used for meetings, not a generic public institution. |
| Commons and authority | `laenu` for commons, `shereni` for entitlement, and `karami` for authority | Authority does not imply legitimacy, ownership, jurisdiction, consent, or beneficial rule. State whichever relation Morris actually gives. |
| Work | `riola` for labour or work, with the worker, object, manner, willingness, coercion, and result stated separately when relevant | Do not make easy work lesser work, reluctance a disease, or compulsory work voluntary. Chapter 6's `wesha` names avoidable reluctance within accepted or chosen work only when that narrower relation is actually claimed. |
| Exchange and markets | `wisola` for exchange; registered `wisola lokue` for market; `wisola rolutha` for an exchange-wagon; `wisola piru` for a trader in the act of exchange; `luera wisola terura` for the old exchange system | `wisola` does not by itself mean buying, selling, price, money, fairness, or profit. State giving, receiving, required return, metal tokens, or institutional relations separately. Preserve exact commercial labels with Morris where Phi has not accepted them. |
| Guest-house and hall | Registered `phemi womu` for a guest-house and `lona lokue` for a hall; compose `phemi lona lokue` when the guest hall's gathering function is the point | A dwelling, lodging relation, meeting-place, and institution are different claims. Do not let one convenient English word erase them. |
| School and education | `shonela sholei` for a learning group where that is the intended sense; `thumela terura` for a teaching system; ordinary clauses for learning, teaching, reading, practice, and coercive institutions | Morris's school polysemy and the exact language names remain in the source. Phi must not manufacture a homonym or let a neutral teaching phrase conceal coercion. |
| Gender, rank, and class labels | Use `miona` with the visible, relational, occupational, or reported classification that matters | Do not import unmarked gendered person classes or source ranks into Phi. If Morris's act of categorising is itself part of the claim, report that category as a source-held concept rather than silently deleting it. |
| Violence, coercion, and contempt | Use explicit relations such as `kawhera` coerce, `peloma` harmful, and `kaworu` injury, plus the physical acts and speaker judgements actually asserted | Do not coin a martial umbrella term, sanitize domination as guidance, or adopt a contemptuous judgement as the narrator's fact. Faithful translation may report cruelty without giving it Phi's approval. |

## Recurring material and built-world concepts

| Source concept | Chosen Phi treatment | Boundary to preserve |
|---|---|---|
| Railway and station | `nurako` for railway and `nurako lokue` for its station or place | Use the direct Systems word now that it exists. Exact railway names and source-era technical distinctions remain with Morris. |
| Architectural arch | Work `toreku`, with material as an ordinary modifier such as `kerou toreku` | `loriphi` is an optical rainbow. It may enter architecture only in an explicit comparison, never as the noun arch. D099 governs this repair. |
| Brick | Registered `mueri kerou`, clay-stone | The compound identifies the material object. Colour, firing, arrangement, and condition remain separate claims. |
| Bronze and other exact materials | Registered `welotu keluo`, mixed metal, when the mixture is what Phi can establish; visible weight, colour, thread, or surface may be stated separately | Morris retains exact material identities such as bronze, lead, plaster, and named techniques. Do not invent composition or properties that the source does not supply. |
| Wagon and source-specific vehicles | `rolutha` for the ordinary wagon or carriage-level vehicle; state shafts, weight, use, animal relation, and motion separately | Wherry, carriage type, and regional vehicle names remain exact with Morris unless Phi has the needed accepted distinction. |
| Manure | Ecological `lomathu` for animal dung collected or kept for soil use | Medical `mokathi` is faeces and must not stand in for manure. D100 governs the distinction. |
| Species, historical styles, and named artefacts | Use an existing exact Phi root when one exists; otherwise describe only the material, form, behaviour, or relation the proposition needs | The adjacent source preserves the exact identity. Do not guess a species, material, date, style, or artefact from a broad description. |
| Exact quantities and measurements | Render an exact integer in Phi when it is within the numeral range and adequate to the claim; keep dates, clock readings, units, out-of-range values, and source-significant notation outside Phi | Do not replace a source measurement with a false exact Phi equivalent. A qualitative relation may accompany the preserved source value when that relation is part of the source. |

## Narrator and evidence

- Chapter 1 begins as a report about a friend. Use an explicit speech or declarative matrix where Morris states that the friend speaks; use reportative `ti` where the narration itself presents an event as secondhand. The final passage deliberately hands the account to the first person.
- From chapter 2 onward, `mia` is Guest's narrative voice. Use `lo mia` only where the narrator belongs to the plural participant group. Do not let a source plural silently become Guide plus Guest, or a source singular become the group.
- Main narrated past events carry `to` on their own predicates. Relative, complement, and other embedded clauses carry tense according to their own temporal relation; narrative context never supplies missing tense for a past clause.
- Evidentials state the source being claimed, not the truth of the proposition. Use `hi` for explicitly claimed direct witness, `ke` for an inference from evidence, `ti` for information received from another source, and `ho` for an assumption or supposition. An unmarked clause remains a plain assertion. Do not mark every first-person event `hi` merely because Guest narrates it.
- Keep perception, inference, memory, and thought distinct. `nila` states seeing, `halemu` remembering, and `remo` thinking; an evidential may refine a proposition but does not replace the event that Morris gives.
- Preserve epistemic distance inside dialogue. The mock medical history in chapter 6 uses report, assumption, inference, treatment, contagion, and isolation vocabulary without converting the speakers' satire into medical fact.
- When the source's gender, rank, occupation, object label, or proper name is not encoded in Phi, do not smuggle it into another Phi constituent. The source line preserves that identity; Phi must still keep the participants and relations distinguishable enough for the scene.

## Quotation and continuing speech

The [complementizer reference](../documents/grammar/complementizer_reference.md) governs `sha ... sho`. It frames grammatical Phi words, not Morris's English. The frame must reach a licensed speech or speech-reception predicate, with the predicate's tense after `sho`.

- One uninterrupted speaker turn receives one `sha ... sho` frame. The framed opening assertion establishes the speaker and reaches its matrix predicate; later assertions in the same uninterrupted turn are bare continuations rather than newly attributed quotations. A single aligned unit may hold several Phi sentences inside its one frame when the source partition keeps them together, but a frame is never left syntactically open for a later unit to close.
- A change of speaker or an actual narrative interruption ends the continuing turn. A citation boundary, source paragraph break, or additional sentence by the same uninterrupted speaker does not by itself require another frame.
- Direct address stays inside the spoken material and uses `kona`, followed by `ne` when the addressee is named.
- Exact spoken wording uses `sha ... sho`; reported content uses `tha ... tho`; an embedded question uses `pha ... pho`. Direct thought is not quotation merely because English prints it between quotation marks. Use a thought predicate with the appropriate declarative or interrogative content unless the character actually speaks the words.
- Preserve the source's speech act. Questions remain questions, requests remain requests, and a forceful voice is expressed through the relevant speech event or manner rather than by multiplying quotation frames.

D097 established the one-frame convention across chapters 1 through 6. Later chapter work must compare each long turn with the preceding and following narrative material before deciding where the frame ends.

## Rejected renderings likely to recur

| Pressure | Do not repeat | Current resolution |
|---|---|---|
| A source personal name looks pronounceable enough to insert | Put an unaccepted source token directly into Phi or improvise a new adaptation at each mention | Use the settled onym table for recurring people. Keep the exact source name in Morris's line. |
| A familiar place recurs | Treat a convenient description as though it were a fixed proper name | Keep the source name outside Phi and use accurate deixis or relation. Establish a place onym only through an explicit later decision. |
| English supplies a useful pun or homonym | Make one Phi form carry both English senses | Translate the two propositions separately. The poor/poorly and school passages keep their English wordplay in Morris. |
| A source idiom contains a physical metaphor | Translate the metaphor's literal action even when the source asserts a discourse act | Translate the asserted act. Conversational entry uses `koema`-shaped entry, not `pukate` breakage. |
| A stone span resembles a rainbow | Use `loriphi` as arch | Use `toreku`; reserve `loriphi` for a rainbow or an explicit comparison. |
| Dung is intended for soil | Use bodily `mokathi` | Use Ecological `lomathu`. Keep `mokathi` within bodily-care reference. |
| A market scene resembles commerce familiar to Guest | Let `wisola` imply price, purchase, sale, profit, or fairness | State exchange and each material or institutional relation the source supplies. Keep source-era labels beside Phi. |
| A violent, coercive, contemptuous, or gendered source label lacks a direct root | Omit the relation, soften it into a benevolent term, or coin a broad disfavoured category | State the observable act, harm, coercion, injury, role, or reported judgement. Preserve the exact label in the source. |
| A source name, date, material, species, or technical category lacks a Phi root | Choose a near word and let the source line repair the mismatch | Keep the exact identity outside Phi and describe only the distinctions Phi actually states. Coin only when connected Phi use demonstrates a genuine lexical need. |

## Open continuity questions

- Later recurring people have no reserved onyms. Settle each form from the person's source relation when their translated appearance establishes recurrence, then add it to this record.
- No place onym has yet proved necessary. Reconsider only if repeated contextual descriptions become ambiguous or prevent Phi from carrying a source relation; repetition alone is not enough.
- Later chapters may place sustained pressure on economic, legal, political, historical, or craft distinctions that the first six chapters could leave source-bound. Search all modules and compounds first, then distinguish a genuine Phi concept from an exact source category before proposing vocabulary.
- A future narrator, document, song, inscription, or story inside the novel may introduce a new evidence or quotation layer. Decide whose claim and whose exact words each clause carries before extending the current narrative convention.
- Add a brief checkpoint entry below after every three new chapters or a natural narrative boundary. Record only cross-chapter findings and settled repairs; keep unit-level work in its ordinary audit material.

## Checkpoints

### Chapters 1-6

- D097 aligned settled person names and continuing-speech frames across all six chapters. Seven onym forms now cover six named people because Boffin and Henry Johnson remain distinct names for one bearer.
- No Phi place onym is active. Repeated places use source identity beside contextual Phi descriptions, with `ra welamu lokue` for Barn Elms the clearest reused descriptive referent.
- The cross-chapter vocabulary remains compatible with one grammar and the full canonical lexicon. Optional module terms are used where their distinctions matter.
- D099 replaced the architectural rainbow workaround with `toreku`; D100 separated soil-use `lomathu` from bodily `mokathi`. Both decisions apply prospectively.
- No unresolved contradiction among the first six chapters is known at this checkpoint. Later chapters must extend this record when they establish a new recurring choice rather than relying on memory.
