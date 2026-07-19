---
title: "AD Definition of Done"
tags:
  - "concept"
  - "agile"
  - "decision-making"
  - "done-criteria"
created_date: "2026-07-19"
updated_date: "2026-07-19"
sources:
  - "Raw/Sources/A Definition of Done for Architectural Decision Making.md"
related:
  - "[[Architectural Decision]]"
  - "[[Architectural Decision Record]]"
  - "[[AD Definition of Ready]]"
summary: "The Definition of Done (DoD) for Architectural Decisions uses the 5-criteria 'ecADR' mnemonic to establish the exit gates for a completed, valid architectural choice."
---

# AD Definition of Done (DoD)

> **Summary**: The Definition of Done (DoD) for Architectural Decisions uses the 5-criteria 'ecADR' mnemonic to establish the exit gates for a completed, valid architectural choice.

## Core Concept

While standard Agile Definitions of Done check whether a feature is "done-done" (tested, integrated, deployable), they do not measure the completion of architectural design tasks. Deciding when technical design work is "finished" can be ambiguous. The **AD Definition of Done** establishes formal exit criteria to ensure an architectural decision is robust, documented, agreed upon, and actionable before the team moves on.

---

## The ecADR Exit Criteria

Olaf Zimmermann proposes the **ecADR** mnemonic to define the done-done status of an Architectural Decision:

- **E — Evidence**: Gaining sufficient proof that the chosen design will work in practice. Evidence can be gathered by:
  - Building a prototype, proof-of-concept, or running an architectural spike.
  - Vetting the design via trusted industry benchmarks.
  - Vouching for the design through trusted experts who have deployed it in similar contexts.
- **C — Criteria**: Clearly identifying at least two distinct design alternatives and comparing them against the core decision drivers and stakeholder concerns.
- **A — Agreement**: Socializing the decision to achieve consensus or formal sign-off. The decision must be challenged and accepted by peers, mentors, or design boards before lock-in.
- **D — Documentation**: Documenting and publishing the decision rationale using a standardized, lean template (such as [[MADR]] or Y-statements) that is shared with all affected stakeholders.
- **R — Realization & review plan**: Scheduling the implementation of the decision, planning how compliance will be verified (testing the architecture), and establishing a timeline to review or potentially revise the decision in the future.

---

## Key Points

- Satisfying the `ecADR` exit criteria transforms an AD from a temporary intent into an official, active project contract.
- Teams should adapt the strictness of the "Agreement" gate depending on the organizational reach (e.g., decentralized team autonomy vs. formal architecture board sign-offs).
- A decision is never "done" without a plan to test its implementation (realization) and retrospectively review it (expiration/revision).

## Related Concepts

- [[Architectural Decision]]
- [[Architectural Decision Record]]
- [[AD Definition of Ready]]
- [[ADR Adoption and Practices]]

## Source References

- [A Definition of Done for Architectural Decision Making](../Raw/Sources/A%20Definition%20of%20Done%20for%20Architectural%20Decision%20Making.md)

## Changelog

| Date | Change |
|---|---|
| 2026-07-19 | Initial creation |

---

*This note was generated from the `_templates/wiki-note.md` template.*
*Run `python scripts/wiki_tool.py lint` before committing.*
