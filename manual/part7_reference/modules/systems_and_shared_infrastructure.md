# Systems and Shared Infrastructure

The Systems and Shared Infrastructure module gives Phi speakers optional vocabulary for explaining how components interact, how material, energy, and information move, how a system changes, and how technical work identifies limits, faults, hazards, and requirements. The words use ordinary Phi grammar. A speaker who has not learned them can still ask for a core paraphrase, and learning this module does not confer technical authority, expertise, ownership, or permission to act.

The complete machine-generated list is also available under [Systems and Shared Infrastructure in the module lexicon](../lexicon/by_module.md#systems-and-shared-infrastructure). The JSON entries in `vocabulary/content/` remain authoritative for each word's form and full definition.

## Core vocabulary used by the module

The module does not replace Phi's existing language of devices, movement, repair, measurement, or shared care. It adds narrower relations around these familiar resources.

| Area | Core Phi resources |
|---|---|
| Things and processes | `keli` device, `tenoa` tool, `teru` process, `norae` method, `norelu` form, `ruka` complex, `whoa` whole |
| Boundaries and relations | `norui` boundary, `shuna` edge, `pharune` include, `lorea` connect, `phaliso` network, `ruela` path, `shoeka` route |
| Movement and recurrence | `selu` flow, `roke` move, `kolua` carry, `sepho` send, `nuri` cycle, `turema` return |
| Upkeep and renewal | `thiranu` maintain, `shiroka` repair, `talome` restore, `thenoki` sustain, `sunoe` regenerate, `shorupo` protect |
| Limits and evidence | `phelona` require, `henoi` enough, `sharoi` exceed, `thenoi` fall short, `masue` measure, `siru` marker, `kiremoa` criterion, `hi` direct evidence, `ke` inference |
| Shared life | `laenu` commons, `sila` community, `phowe` share, `panoru` support, `theluo` steward, `thonai` responsible |

## Module vocabulary

| Phi | Part of speech | Working sense | Essential contrast |
|---|---|---|---|
| `terulora` | noun | system; bounded whole of interacting components | A system is not merely a collection, network, process, device, or harmonious whole. |
| `monakeli` | noun | component; functionally identified part | A component is not every piece, ingredient, member, or nearby object. |
| `norawiso` | noun | interface; defined means or place of interaction | An interface is more specific than a boundary or connection and is not only a screen. |
| `kelithora` | verb | function; perform a system role or operation | Functioning does not establish purpose, efficiency, reliability, safety, or success. |
| `nomirela` | noun | state; selected system conditions at a time | A state is an analytical description, not a permanent essence or every fact about a thing. |
| `phelorani` | verb | depend; require another element for function or state | Dependency is not logical entailment, cause, ownership, control, or personal inferiority. |
| `koemari` | noun | input; matter, energy, information, or influence entering a system | Not every arrival, cause, resource, instruction, or contribution is an input. |
| `thirulo` | noun | output; matter, energy, information, or effect leaving a system | An output is not automatically useful, intended, harmless, or evidence of good performance. |
| `selokaru` | verb | transfer; move something from a source to a recipient | Transfer is more specific than movement or flow and does not prove successful receipt or conservation. |
| `kiroweli` | noun | signal; detectable variation carrying information | A signal is not automatically a command, message, measurement, cause, or reliable evidence. |
| `ketorami` | verb | control; adjust a technical process toward a selected state | Technical control is not authority, command, coercion, ownership, or control of people. |
| `turekali` | noun | feedback; returned effect that alters an ongoing process | Feedback is more than return, recurrence, circular shape, response, or commentary. |
| `henoraki` | noun | capacity; conditioned limit of holding, processing, or delivery | Capacity is not current contents, output, human ability, permission, or guaranteed performance. |
| `talukori` | noun | load; technical demand placed on a system | Load does not unmarkedly mean labor, distress, obligation, cargo, or a burden placed on a person. |
| `pheluremi` | verb | store; retain for later retrieval or release | Storage does not establish preservation, security, ownership, capacity, or recoverability. |
| `poruseli` | adjective | efficient; high useful output relative to selected input | Efficiency is not speed, productivity, sustainability, fairness, safety, sufficiency, or goodness. |
| `masukiro` | verb | calibrate; relate an instrument to a stated reference | Calibration is not measurement, inspection, universal accuracy, or proof that a method is suitable. |
| `keliphira` | noun | fault; abnormal technical condition | A fault is not blame, moral wrongdoing, legal liability, breakage, or necessarily failure. |
| `thonureki` | verb | fail; not perform a stated required function | Failure need not involve physical breakage and does not identify its cause or responsible person. |
| `seluwhera` | noun | outage; bounded period of unavailable infrastructure service | An outage is not necessarily total system destruction, an unplanned event, or equally harmful to everyone. |
| `wesopanu` | adjective | redundant; having independent alternative means for a function | Technical redundancy is not needless repetition, identical duplication, or guaranteed reliability. |
| `nilakiro` | verb | inspect; systematically examine condition against criteria | Inspection is not repair, calibration, certification, approval, or a guarantee of safety. |
| `kolutheri` | adjective | reliable; consistently performing a required function under conditions | Reliability is not certainty, accuracy, safety, redundancy, or a person's trustworthiness. |
| `pelomaru` | noun | hazard; potential source or condition of harm | A hazard is not actual harm, present danger, blame, prohibition, or a complete risk assessment. |
| `kirosholu` | noun | specification; explicit set of technical requirements | A specification is not a standard, law, design, method, authority, compliance result, or permission for use. |

The verbs in this table receive their event or result nouns through Phi's ordinary event-noun rule: `kelithora` can name a function, `phelorani` a dependency, `selokaru` a transfer, `ketorami` control, `pheluremi` storage, `masukiro` calibration, `thonureki` failure, and `nilakiro` inspection. The adjectives `poruseli`, `wesopanu`, and `kolutheri` likewise name efficiency, redundancy, and reliability through the quality-noun rule; their entries remain adjective-only as required by the lexicon schema.

## Systems, components, functions, and states

`terulora` names an organized whole selected for analysis. Its `norui` boundary determines which `monakeli` components and relations are inside the account. A different question may draw a different boundary or treat one component as a system of its own. Calling something a system therefore begins an explanation; it does not finish one.

```
ha terulora lo monakeli lorea.
PROX system PL component connect.
(This system connects the components.)
```

```
ha monakeli mua ha terulora nai.
PROX component LOC PROX system be.
(This component is in this system.)
```

`kelithora` states that a component or system performs a characteristic or required operation. `nomirela` gathers the conditions selected to describe it at a time. The function, state variables, time, and evidence remain separate information.

```
ha monakeli kelithora.
PROX component function.
(This component functions.)
```

```
ha terulora nomirela mureo nai.
PROX system state stable be.
(This system's state is stable.)
```

`phelorani` makes a requirement relation explicit without turning it into cause, entailment, or authority.

```
ha terulora ra monakeli phelorani.
PROX system DIST component depend.
(This system depends on that component.)
```

## Inputs, outputs, and transfers

`koemari` and `thirulo` are always relative to a selected boundary. The same water, energy, material, or information can be one system's output and another system's input. Their forms are deliberately dissimilar so the directional opposition remains easy to hear.

```
ha phialu ha terulora koemari nai.
PROX water PROX system input be.
(The water is an input to this system.)
```

```
ha kenua ha terulora thirulo nai.
PROX energy PROX system output be.
(The energy is this system's output.)
```

`selokaru` identifies movement from a source toward a recipient. Flow, carrying, sending, and transfer can describe different aspects of the same event, but none automatically establishes that the complete amount arrived or remained unchanged.

```
ha monakeli wea ra monakeli phialu selokaru.
PROX component TOWARD DIST component water transfer.
(This component transfers water toward that component.)
```

## Signals, control, and feedback

A `kiroweli` is a detectable variation interpreted as information. Its source, medium, recipient, and meaning may all matter. A signal can indicate a `nomirela` state without being a command or proof that the state interpretation is correct.

```
ha kiroweli ha terulora nomirela shelo.
PROX signal PROX system state signify.
(This signal indicates the system's state.)
```

`ketorami` is restricted to technical control of a process or variable. It does not make control of people sound like neutral engineering. `turekali` requires a returned effect: something about a later output or state alters an input, control, or continuing process. A circular diagram or chain of connections alone is not feedback.

```
ha monakeli phialu selu ketorami.
PROX component water flow control.
(This component controls the water flow.)
```

```
ha turekali ha ketorami helui.
PROX feedback PROX control change.
(This feedback changes the control.)
```

## Capacity, load, storage, and efficiency

`henoraki` states how much or how quickly a system can hold, process, transmit, or provide under stated conditions. `talukori` states the demand placed on that function. The affected function, duration, and exact units must be supplied when they change the claim.

Source record outside Phi: `20 kWh`

```
ha siranomi ha terulora henoraki thelima.
PROX record PROX system capacity describe.
(This record describes this system's capacity.)
```

```
ha talukori ha henoraki sharoi.
PROX load PROX capacity exceed.
(This load exceeds the capacity.)
```

`pheluremi` retains something for later retrieval or release. It does not say that the store has enough capacity, prevents loss, preserves the contents, or belongs to anyone in particular.

```
ha terulora kenua pheluremi.
PROX system energy store.
(This system stores energy.)
```

`poruseli` compares selected useful output with selected input, loss, resource, or cost. Every efficiency claim therefore has a boundary and a value choice. A process can be efficient while harmful, inaccessible, insufficient, or unjust.

```
ha terulora poruseli nai.
PROX system efficient be.
(This system is efficient.)
```

## Faults, failures, and outages

A `keliphira` is an abnormal condition that may contribute to a failure. `thonureki` says that a required function was not performed. The fault, observed signs, failure, cause, responsibility, repair, and future safety are separate claims.

```
ha monakeli keliphira phelu.
PROX component fault hold.
(This component has a fault.)
```

```
ha monakeli to thonureki.
PROX component PST fail.
(This component failed.)
```

A `seluwhera` concerns the unavailable service experienced over a period. One component may fail without an outage, and an outage may occur without component failure. Planned work, missing input, unsafe conditions, or an external interruption can also make a service unavailable.

```
ha seluwhera mosha teku nai.
PROX outage period short be.
(The outage period is short.)
```

## Calibration, inspection, and specifications

`masukiro` compares a device with a reference and may establish, check, or adjust their relation. `nilakiro` examines condition against criteria. A person may calibrate without performing a complete inspection or inspect without calibrating anything.

```
mia ha keli masukiro.
1SG PROX device calibrate.
(I calibrate this device.)
```

```
mia ha terulora nilakiro.
1SG PROX system inspect.
(I inspect this system.)
```

`kirosholu` names a set of technical requirements. The module word identifies the role; the actual values, units, wording, identifier, source, and version remain in source material outside the Phi passage. Satisfying a specification does not prove that its requirements are wise, legitimate, sufficient, current, accessible, or safe.

```
ha kirosholu ha henoraki thelima.
PROX specification PROX capacity describe.
(This specification describes the capacity.)
```

## Hazards, redundancy, and reliability

`pelomaru` names a possible source or condition of harm. Exposure, likelihood, severity, affected people, and response remain separate. `wesopanu` says that independent alternatives are intended to preserve a function; shared causes can still defeat them. `kolutheri` reports consistent performance only for the function, conditions, duration, and evidence stated.

```
ha phialu selu pelomaru nai.
PROX water flow hazard be.
(This water flow is a hazard.)
```

```
ha terulora wesopanu nai.
PROX system redundant be.
(This system is redundant.)
```

```
ha terulora kolutheri nai.
PROX system reliable be.
(This system is reliable.)
```

These three assessments answer different questions. A redundant system can remain unreliable, a reliable system can contain a hazard, and reducing one hazard does not establish overall safety.

## Useful transparent compositions

Some systems expressions remain clearer as combinations because their parts expose the intended analysis.

| Phi expression | Practical meaning | Why it remains compositional |
|---|---|---|
| `terulora norui` | system boundary | Keeps the selected system and its analytical limit visible. |
| `monakeli terulora` | subsystem; component system | Shows the change of scale directly. |
| `sila panoru terulora` | shared infrastructure; community-support system | Names who is supported and preserves the possibility that the system fails, excludes, burdens, or lacks legitimate governance. |
| `panoru kelithora` | infrastructure service; support function | Identifies the provided function without assuming ownership, authority, entitlement, adequacy, or access. |
| `selu shoeka` | flow pathway | Keeps pathway connected to actual motion and an explicit route. |
| `masue maewo` | measurement threshold | Reuses the existing transition point while requiring the measured quantity and consequence to be stated. |
| `kirosholu norui` | specification tolerance or permitted boundary | Keeps the allowed range tied to a stated specification. |
| `thiranu mosha` | maintenance interval | Names upkeep and its period without hiding either. |
| `kelithora nomirela` | service or function state | Leaves availability, degradation, interruption, and approval as separate possible states. |
| `thonureki norelu` | failure mode | Names the form of failure without claiming its cause. |
| `kirosholu heno` | satisfy a specification | States that requirements are met without implying certification, legitimacy, or safety. |

## Source technical information

Measurements, units, formulas, identifiers, standards, exact specifications, source instructions, and versioned technical terminology remain outside the Phi passage in the surrounding medium. The module supplies relations around source material; it does not translate or normalize the artifact.

Use an existing word, transparent expression, module term, or fully admitted new word when Phi needs the concept. A pronunciation aid remains an outside conversational convention and does not acquire the definition of a module word merely because speakers use it repeatedly.

State the analysis in Phi where useful: which system and boundary are meant, what enters and leaves, which components and dependencies matter, how a state was observed, what exact condition applies, which hazard is proposed, and who may act. Exact preservation does not prove correct interpretation, technical competence, safety, accessibility, ownership, responsibility, or authority.
