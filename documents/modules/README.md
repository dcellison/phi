# Phi Practice and Domain Profiles

This directory holds practice and domain profiles for Phi. A profile helps a speaker find existing resources, learn optional domain vocabulary, and use Phi within a bounded field or shared practice. It is not a language fork, a professional standard, a competence credential, or a claim of authority over the people who work in that field.

Profiles may begin as zero-new-root inventories and later receive a straightforward vocabulary pass. A vocabulary module exists so speakers who need a domain can discuss it meaningfully without obliging general Phi speakers to learn every specialized term.

## Invariants

Every profile follows these rules:

1. Phi has one grammar. A module adds no particles, syntax, inflection, parser mode, or incompatible construction.
2. Existing roots remain in the shared lexicon. When another profile needs one, the word may stay a listed dependency or gain another module classification if it belongs in both learning paths. Neither choice changes its definition or gives a profile exclusive ownership.
3. A root may appear in several profiles. `theama` belongs in care, household, access, and community discussion whenever it is useful; no profile gets to narrow its meaning by listing it.
4. Core resources needed for ordinary life, identity, consent, safety, testimony, or communication stay available outside every profile.
5. Foreign wording, source-script names, exact records, formulas, identifiers, and other unassimilated artifacts remain outside Phi passages. A domain profile may describe or translate source material without turning its tokens into Phi words.
6. A module is optional as a learning and use focus, not as a parsing rule. A speaker unfamiliar with a specialized term may ask for a core paraphrase, explanation, transparent expression, or separately presented source form as appropriate.

## Profile Statuses

| Status | Meaning |
|---|---|
| **Profile** | Existing roots, documented compounds, and source-material practice organized for a domain; no module-specific vocabulary yet. |
| **Vocabulary pass** | Active review of which domain concepts compose naturally and which deserve coinage. |
| **Established vocabulary module** | Module-oriented content words have complete canonical entries, a generated module index, and a speaker-facing guide. Module membership is a learning aid, not a second parser or grammar. |

Every module-oriented word follows the complete [word-creation protocol](../development_protocol.md#word-creation-protocol), including full schema fields, semantic scope and contrasts, phonology, collision checks, natural examples, and generated references. Corpus evidence may inspire or improve a word, but a personal language does not need an external burden of proof before its maintainer coins a useful or valued concept.

## Required Contents

Every new profile should contain:

1. A concise charter, scope, and explicit non-goals.
2. A grouped map of existing core dependencies.
3. Existing compositions and source-material guidance relevant to the domain.
4. A vocabulary decision table distinguishing existing words, transparent compounds, module coinages, and source material that should remain outside the Phi passage.
5. Natural validated examples showing the domain vocabulary in ordinary Phi grammar.
6. A speaker-facing chapter under `manual/part7_reference/modules/` once module vocabulary is established.

## Core and Module Placement

Core versus module placement is an organizational judgment about what a general learner is expected to study, not a difference in grammar or lexical legitimacy. Broad everyday concepts normally belong to the core teaching path; specialized terms may carry one or more validated `modules` classifications in their canonical JSON entries. A word may move into broader teaching later if use makes that natural.

The [Module overlap assessment](module_overlap_assessment.md) accounts for all 227 current module entries. Sixty-one words now have shared membership, 29 still need a closer boundary decision, and eleven may belong in base vocabulary instead.

## Active Profiles

| Profile | Status | Roots coined here | Current memberships | Shared-core addition | Purpose |
|---|---|---:|---:|---|---|
| [Household and Daily Life](household_and_daily_life.md) | **Established vocabulary module** | 30 | 38 | `mirewu` private | Domestic relations, storage, cleaning, cloth, meals, and food preparation. |
| [Medical and Bodily Care](medical_and_bodily_care.md) | **Established vocabulary module** | 30 | 45 | `lesawi` consent | Symptoms, findings, health conditions, clinical evaluation, intervention effects, illness course, transmission, and public health. |
| [Systems and Shared Infrastructure](systems_and_shared_infrastructure.md) | **Established vocabulary module** | 25 | 34 | None | System structure, inputs and outputs, control, feedback, technical state, upkeep, reliability, hazards, and specifications. |
| [Philosophical Reasoning](philosophical_reasoning.md) | **Established vocabulary module** | 22 | 22 | None | Argument structure, evidence, inference, validity, definition, epistemic stance, and competing values. |
| [Accessibility and Participation](accessibility_and_participation.md) | **Established vocabulary module** | 30 | 43 | `sowelu` disabled | Access relations, communication forms, timing, technical fit, support, exclusion, and advocacy. |
| [Commons and Collective Governance](commons_and_collective_governance.md) | **Established vocabulary module** | 30 | 40 | None | Membership, institutions, authority, collective procedure, allocation, accountability, records, review, and institutional harm. |
| [Ecological Systems and Material Life](ecological_systems_and_material_life.md) | **Established vocabulary module** | 30 | 40 | None | Ecological organization, land and water processes, weather and climate, pollution and exposure, material afterlives, and repeated ecological observation. |
| [Work, Craft, and Repair](work_craft_and_repair.md) | **Established vocabulary module** | 30 | 48 | None | Work units and status, coordination, skill and qualification, training and evaluation, labor conditions, design, and material traceability. |

## Proposed Profile Catalogue

This catalogue records the profile ideas currently in scope so they do not depend on conversation memory. No additional profile is currently proposed. A new candidate should be recorded here with its intended role, reason for a separate organization layer, cross-module boundaries, and a useful first development prompt before creation.

[Potential Profile Explorations](potential_profile_explorations.md) preserves scenario-first possibilities, conditional candidates, and contexts that should remain cross-profile. An exploration enters the active catalogue when the maintainer chooses to develop it and its intended boundaries are clear.

## Cross-Module and Scenario-Gated Areas

| Area | Current handling |
|---|---|
| Solarpunk | A cross-module integration context, not a fixed vocabulary profile or ideology. The old common hall scenario should test several profiles together. |
| Reproductive health, sexuality, gender, and identity | Scenario-gated areas that must not be silently absorbed into Medical and Bodily Care. They may later justify one or more profiles after respectful corpus work and boundary review. |
| Technical measurement and science | Shared exact-register and reasoning practice for now. A separate profile should be considered only if cross-domain scenarios show needs not handled by Systems and Shared Infrastructure. |

Philosophical Reasoning established the implementation pattern: canonical JSON entries with validated module membership, a generated by-module index, and a curated Part VII chapter. All eight active profiles now follow it. Medical places `lesawi` consent in shared core, Accessibility does the same with `sowelu` disabled, and Household adds `mirewu` private. Existing scenarios remain sources of ideas and examples rather than admission gates.
