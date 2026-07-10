# Phi Practice and Domain Profiles

This directory holds practice and domain profiles for Phi. A profile helps a speaker find existing resources, learn optional domain vocabulary, and use Phi within a bounded field or shared practice. It is not a language fork, a professional standard, a competence credential, or a claim of authority over the people who work in that field.

Profiles may begin as zero-new-root inventories and later receive a straightforward vocabulary pass. A vocabulary module exists so speakers who need a domain can discuss it meaningfully without obliging general Phi speakers to learn every specialized term.

## Invariants

Every profile follows these rules:

1. Phi has one grammar. A module adds no particles, syntax, inflection, parser mode, or incompatible construction.
2. Existing roots remain in the shared lexicon. A profile lists them as dependencies; it does not move their JSON entries or claim exclusive ownership. Module words also remain ordinary canonical entries but are optional as a learning focus.
3. A root may appear in several profiles. `theama` belongs in care, household, access, and community discussion whenever it is useful; no profile gets to narrow its meaning by listing it.
4. Core resources needed for ordinary life, identity, consent, safety, testimony, or communication stay available outside every profile.
5. Guest and exact material remain governed by `hasha ... hasho` and `patha ... patho`. A domain profile does not turn an outside term into an unmarked Phi word.
6. A module is optional as a learning and use focus, not as a parsing rule. A speaker unfamiliar with a specialized term may ask for a core paraphrase, explanation, guest adaptation, or exact source form as appropriate.

## Profile Statuses

| Status | Meaning |
|---|---|
| **Profile** | Existing roots, documented compounds, and external-register practice organized for a domain; no module-specific vocabulary yet. |
| **Vocabulary pass** | Active review of which domain concepts compose naturally and which deserve coinage. |
| **Established vocabulary module** | Module-oriented content words have complete canonical entries, a generated module index, and a speaker-facing guide. Module membership is a learning aid, not a second parser or grammar. |

Every module-oriented word follows the complete [word-creation protocol](../development_protocol.md#word-creation-protocol), including full schema fields, semantic scope and contrasts, phonology, collision checks, natural examples, and generated references. Corpus evidence may inspire or improve a word, but a personal language does not need an external burden of proof before its maintainer coins a useful or valued concept.

## Required Contents

Every new profile should contain:

1. A concise charter, scope, and explicit non-goals.
2. A grouped map of existing core dependencies.
3. Existing compositions and external-register guidance relevant to the domain.
4. A vocabulary decision table distinguishing existing words, transparent compounds, module coinages, and material that should remain external.
5. Natural validated examples showing the domain vocabulary in ordinary Phi grammar.
6. A speaker-facing chapter under `manual/part7_reference/modules/` once module vocabulary is established.

## Core and Module Placement

Core versus module placement is an organizational judgment about what a general learner is expected to study, not a difference in grammar or lexical legitimacy. Broad everyday concepts normally belong to the core teaching path; specialized terms may carry one or more validated `modules` classifications in their canonical JSON entries. A word may move into broader teaching later if use makes that natural.

## Active Profiles

| Profile | Status | New roots | Purpose |
|---|---|---:|---|
| [Household and Daily Life](household_and_daily_life.md) | **Profile** | 0 | Test the module format against a dense, low-stakes existing vocabulary field. |
| [Medical and Bodily Care](medical_and_bodily_care.md) | **Profile** | 0 | Organize bodily self-report, care, consent, safety, evidence, and exact health information without medicalizing accessibility. |
| [Systems and Shared Infrastructure](systems_and_shared_infrastructure.md) | **Profile** | 0 | Organize devices, processes, flows, maintenance, shared resources, reasoning, and exact technical information. |
| [Philosophical Reasoning](philosophical_reasoning.md) | **Established vocabulary module** | 22 | Add optional terminology for argument structure, evidence, inference, validity, definition, epistemic stance, and competing values. |
| [Accessibility and Participation](accessibility_and_participation.md) | **Cross-domain profile** | 0 | Organize environmental and procedural access, communication practices, timing, autonomy, support, and participation without medicalizing disability. |
| [Commons and Collective Governance](commons_and_collective_governance.md) | **Profile** | 0 | Organize shared resources, deliberation, allocation, collective choices, responsibility, accountability, records, and review without presuming authority. |
| [Ecological Systems and Material Life](ecological_systems_and_material_life.md) | **Profile** | 0 | Organize land, water, weather, living beings, materials, flows, ecological evidence, limits, protection, restoration, and regeneration without treating values or exact science as conclusions. |
| [Work, Craft, and Repair](work_craft_and_repair.md) | **Profile** | 0 | Organize labor, making, tools, materials, practical learning, work-sharing, maintenance, repair, safety, checking, and exact work information without romanticizing labor or presuming authority. |

## Proposed Profile Catalogue

This catalogue records the profile ideas currently in scope so they do not depend on conversation memory. No additional profile is currently proposed. A new candidate should be recorded here with its intended role, reason for a separate organization layer, cross-module boundaries, and a useful first development prompt before creation.

[Potential Profile Explorations](potential_profile_explorations.md) preserves scenario-first possibilities, conditional candidates, and contexts that should remain cross-profile. An exploration enters the active catalogue when the maintainer chooses to develop it and its intended boundaries are clear.

## Cross-Module and Scenario-Gated Areas

| Area | Current handling |
|---|---|
| Solarpunk | A cross-module integration context, not a fixed vocabulary profile or ideology. The old common hall scenario should test several profiles together. |
| Reproductive health, sexuality, gender, and identity | Scenario-gated areas that must not be silently absorbed into Medical and Bodily Care. They may later justify one or more profiles after respectful corpus work and boundary review. |
| Technical measurement and science | Shared exact-register and reasoning practice for now. A separate profile should be considered only if cross-domain scenarios show needs not handled by Systems and Shared Infrastructure. |

Philosophical Reasoning is the first profile to complete a vocabulary pass and therefore establishes the implementation pattern: canonical JSON entries with validated module membership, a generated by-module index, and a curated Part VII chapter. The other active profiles may follow the same pattern when their vocabulary passes begin; their existing scenarios remain useful sources of ideas and examples rather than admission gates.
