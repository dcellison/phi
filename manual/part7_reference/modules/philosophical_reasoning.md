# Philosophical Reasoning

The Philosophical Reasoning module gives Phi speakers a precise optional vocabulary for constructing arguments, examining support, defining concepts, identifying logical relations, holding uncertainty, and discussing difficult choices. These words use ordinary Phi grammar. A speaker who has not learned them can still ask for a core paraphrase, and learning this module does not confer authority, expertise, or correctness.

The complete machine-generated list is also available under [Philosophical Reasoning in the module lexicon](../lexicon/by_module.md#philosophical-reasoning). The JSON entries in `vocabulary/content/` remain authoritative for each word's form and full definition.

## Core vocabulary used by the module

The module does not replace Phi's existing language of thought and dialogue. It adds narrower distinctions around these familiar resources.

| Area | Core Phi resources |
|---|---|
| Thought and stance | `remo` think, `nohero` believe, `sano` know, `shelomui` understand, `hiru` intuit, `kanelu` err |
| Truth and accuracy | `shewo` true, `theloa` truth, `telua` accurate, `phelira` mistaken |
| Meaning and explanation | `reo` meaning, `relo` symbol, `shelo` signify, `lilea` clarify, `solae` explain, `thelima` describe |
| Sources and modality | `hi` direct evidence, `ke` inference, `ti` report, `ho` assumption, `po` possibility, `na` necessity, `ma` negation |
| Dialogue and repair | `shareo` discuss, `nawo` agree, `naweri` refuse, `thekao` acknowledge, `shorela` rephrase, `shekoi` specify, `shelao` summarize |
| Values and choice | `sone` value, `rolia` worth, `noetha` essential, `kanu` choose, `kelomi` accept, `numike` negotiate, `seru` commit, `thonai` responsible |

## Module vocabulary

| Phi | Part of speech | Working sense | Essential contrast |
|---|---|---|---|
| `sherewa` | verb | claim; present a proposition for assessment | A claim is public; `nohero` is belief. |
| `mothare` | noun | premise; a starting claim in an argument | A premise is a role and need not be true or evidential. |
| `remoluma` | noun | conclusion; the claim reached by reasoning | A conclusion is not merely `lumae`, the final point in time or sequence. |
| `theremola` | noun | argument; premises organized to support a conclusion | An argument is not a quarrel or a dialogue. |
| `whakeru` | verb | object; raise a specific problem for response | An objection is not necessarily refusal, disagreement, or refutation. |
| `thesori` | noun | evidence; material offered for or against a claim | Evidence is not an evidential particle and is not automatically reliable. |
| `remotha` | noun | reason; a justificatory ground | A reason is distinct from cause, purpose, motivation, and evidence. |
| `kethira` | verb | infer; reach a conclusion from premises | The act of inference is distinct from inferential evidential `ke`. |
| `natheri` | verb | entail; imply by necessity | Entailment is stronger than support, sequence, or causal consequence. |
| `kithela` | adjective | valid; having premises that entail the conclusion | Validity does not establish that the premises are true. |
| `phiraketu` | verb | contradict; be unable to be true together under the same conditions | Contradiction is stronger than difference, contrast, or disagreement. |
| `letharo` | adjective | consistent; able to be true together | Consistency does not establish truth or sameness. |
| `phisuwa` | noun | example; a particular illustrating case | The noun names the case; `phisu` announces one in discourse. |
| `phiwhekira` | noun | counterexample; a case defeating a general claim | A surprising or irrelevant case is not necessarily a counterexample. |
| `whekatelu` | verb | refute; show that a claim or inference fails | Refutation requires more than objection or disagreement. |
| `kirothe` | verb | define; state meaning or conditions of application | Definition is narrower than description or clarification. |
| `kiremoa` | noun | criterion; a standard used in judgment or classification | A criterion is not merely a measurement or method. |
| `remolea` | noun | concept; an organized idea | A concept is distinct from its word, symbol, definition, and examples. |
| `wharemoi` | verb | doubt; remain unsettled about a proposition | Doubt is not denial or refutation. |
| `norethi` | adjective | confident; hold a strong but revisable stance | Confidence is not knowledge, truth, boldness, or authority. |
| `soneholu` | noun | tradeoff; a valued gain joined to a valued loss | A tradeoff is more than having several options. |
| `malonawi` | verb | compromise; agree through mutual concession | Compromise is not automatically fair, free, wise, or required. |

Verbs in this table receive their event or result nouns through Phi's ordinary event-noun rule: `sherewa` can name a claim, `kethira` an inference, `whakeru` an objection, `whekatelu` a refutation, `kirothe` a definition, `wharemoi` doubt, and `malonawi` a compromise. The adjectives `kithela`, `letharo`, and `norethi` likewise name validity, consistency, and confidence through the quality-noun rule; their entries remain verb-only or adjective-only as required by the lexicon schema.

## Claims, premises, and conclusions

`sherewa` names the act of putting a proposition forward. A speaker may claim something they believe, claim it only provisionally, or state it for examination without endorsing it. `mothare` and `remoluma` name roles inside a `theremola`: premises are offered as support, and the conclusion is what the argument reaches.

```
mia mena ha ruela welao nai meno sherewa.
1SG DECL.COMP PROX path good be DECL.COMP.CLOSE claim.
(I claim that this path is good.)
```

```
lo mothare ha remoluma panoru.
PL premise PROX conclusion support.
(The premises support this conclusion.)
```

```
ha theremola kithela nai.
PROX argument valid be.
(This argument is valid.)
```

An objection identifies a difficulty without pretending that the difficulty has already defeated the claim.

```
mia mena ha mothare shewo ma nai meno whakeru.
1SG DECL.COMP PROX premise true NEG be DECL.COMP.CLOSE object.
(I object that this premise is not true.)
```

## Evidence, reasons, and inference

`thesori` names material offered for assessment. The particles `hi`, `ke`, `ti`, and `ho` still mark how the speaker claims to have access to a verb's content; they do not certify the quality of the evidence. `remotha` names a consideration offered as justification, while `kethira` names the reasoning step from premises to a conclusion.

```
ha thesori ha sherewa panoru.
PROX evidence PROX claim support.
(This evidence supports this claim.)
```

```
mia lue lo mothare ha remoluma kethira.
1SG ABL PL premise PROX conclusion infer.
(I infer this conclusion from the premises.)
```

`natheri` is deliberately stronger than support. It says that the first proposition cannot be true under the stated interpretation while the second is false.

```
ha mothare ha remoluma natheri.
PROX premise PROX conclusion entail.
(This premise entails this conclusion.)
```

## Validity, contradiction, and refutation

A `kithela theremola` is structurally valid even when one of its premises is false. Claims are `letharo` when they can be true together and `phiraketu` when they cannot both be true under the same interpretation and relevant conditions.

```
ha sherewa ra sherewa phiraketu.
PROX claim DIST claim contradict.
(This claim contradicts that claim.)
```

```
lo sherewa letharo nai.
PL claim consistent be.
(The claims are consistent.)
```

A `phiwhekira` is a case within a general claim's scope that does not have the property assigned to every such case. It can therefore `whekatelu` the general claim as stated.

```
ha phiwhekira ra sherewa whekatelu.
PROX counterexample DIST claim refute.
(This counterexample refutes that claim.)
```

## Concepts, definitions, and criteria

`remolea` separates an organized idea from the `phelui` that names it, the `relo` that symbolizes it, the `reo` it carries, and any one `phisuwa` used to illustrate it. `kirothe` proposes a boundary or account of application; `kiremoa` names a standard used when applying that boundary.

```
mia shea kirothe.
1SG peace define.
(I define peace.)
```

```
ha phisuwa kirothe lilea.
PROX example define clarify.
(This example clarifies the definition.)
```

```
ha remolea ruka nai.
PROX concept complex be.
(This concept is complex.)
```

Necessary and sufficient conditions do not require two more roots. Direction makes the distinction: if category membership entails (`natheri`) the criterion, the criterion is necessary; if satisfying the criterion entails category membership, it is sufficient. When both directions hold, the criterion serves as both.

## Doubt and confidence

`wharemoi` lets a speaker remain unsettled without denying a claim. `norethi` reports the strength of a stance while leaving truth, knowledge, and authority as separate questions.

```
mia mena ha remoluma kithela nai meno wharemoi.
1SG DECL.COMP PROX conclusion valid be DECL.COMP.CLOSE doubt.
(I doubt that this conclusion is valid.)
```

```
mia norethi nai.
1SG confident be.
(I am confident.)
```

Principled suspension can remain compositional: `mena ... meno nohero ma kanu` says that the speaker does not choose the framed belief. This is more explicit than treating every uncertainty as a special lexical state.

## Tradeoffs and compromise

`soneholu` keeps a valued gain and a valued loss in the same concept. It should be followed by enough explanation to show which outcomes matter and who bears each burden. `malonawi` names agreement reached through concession, but the word does not bless the settlement as fair or voluntary.

```
ha kanu soneholu phelu.
PROX choose tradeoff hold.
(This choice has a tradeoff.)
```

```
mia nua thia to malonawi.
1SG COM 2SG PST compromise.
(I compromised with you.)
```

## Useful transparent compositions

Some useful philosophical expressions remain clearer as combinations because their parts expose the intended analysis.

| Phi expression | Practical meaning | Why it remains compositional |
|---|---|---|
| `sherewa remotha` | reason for a claim | Keeps the justificatory relation explicit. |
| `sone noa` | priority; value-position | Allows priorities to be compared without treating one ranking as universal. |
| `remo noa` | standpoint or perspective; thought-position | Keeps a perspective connected to a situated act of thinking. |
| `kithela theremola` | valid argument | Uses the ordinary modifier-first relation. |
| `noetha kiremoa` | essential criterion | Names importance without silently claiming logical sufficiency. |
| `mena ... meno nohero ma kanu` | suspend judgment; decline to choose the framed belief | States exactly what the speaker is withholding. |

## Source philosophical vocabulary

Tradition-specific terms, formal notation, exact quotations, and concepts whose source form matters remain outside the Phi passage in the surrounding medium. A module word may help explain the source concept, but it should not be presented as an exhaustive translation unless the relevant distinctions genuinely match. A pronunciation aid remains an outside conversational convention rather than a temporary class of Phi word.
