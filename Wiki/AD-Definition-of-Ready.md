---
title: "AD Definition of Ready"
tags:
  - "concept"
  - "agile"
  - "decision-making"
  - "readiness"
created_date: "2026-07-19"
updated_date: "2026-07-19"
sources:
  - "Raw/Sources/A Definition of Ready for Architectural Decisions (ADs).md"
related:
  - "[[Architectural Decision]]"
  - "[[Architectural Decision Record]]"
  - "[[AD Definition of Done]]"
summary: "The Definition of Ready (DoR) for Architectural Decisions uses the 5-criteria 'START' backronym to determine when a design choice is mature enough to be officially made."
---

# AD Definition of Ready (DoR)

> **Summary**: The Definition of Ready (DoR) for Architectural Decisions uses the 5-criteria 'START' backronym to determine when a design choice is mature enough to be officially made.

## Core Concept

In Agile feature development, the *Definition of Ready (DoR)* ensures that user stories are mature enough to enter a sprint. Similarly, in software architecture, an **AD Definition of Ready** specifies the entry conditions for decision-making. Making a major architectural decision too early results in guessing; making it too late causes costly rework and project delays. The DoR helps identify when an architectural decision has reached its **Most Responsible Moment (MRM)** to be finalized.

---

## The START Criteria Mnemonic

The entry conditions for a ready AD are encapsulated in the **START** backronym:

- **S — Stakeholders are known**: The decision-makers, consulting subject-matter experts, and affected stakeholders are identified and engaged. (e.g., mapped via a RACI matrix).
- **T — Time (Most Responsible Moment) has come**: The decision is both important and urgent. The MRM has arrived; deciding now is highly useful, whereas waiting would block progress or defer critical architectural spikes.
- **A — Alternatives exist and are understood**: At least two viable design alternatives (options) have been identified, and their initial pros, cons, and trade-offs are documented.
- **R — Requirements/criteria are known**: The context, problem statement, and key decision drivers (functional and non-functional requirements, constraints) are clearly analyzed.
- **T — Template is chosen**: A standardized ADR template (e.g., [[MADR]]) has been chosen, validated, and initialized to document the decision lifecycle.

---

## Prioritizing Early Decisions (Big ADs)

Certain decisions are highly significant and must reach their Definition of Ready early in the project lifecycle. These "big" decisions include:

1. **High Architectural Significance**: Scoring highly on the [[Architectural Decision#Seven-Criteria-for-Architectural-Significance-The-ASR-Test|ASR Test]].
2. **High Cost/Impact**: Requiring significant financial investment (licensing, hosting) or staffing training.
3. **Long Execution Time**: Requiring proofs-of-concept, architectural spikes, or lengthy procurement phases.
4. **Many Outgoing Dependencies**: Strategic choices that trigger multiple downstream technical decisions.
5. **Conflict-Prone**: Decisions involving multiple stakeholders with competing goals that take a long time to align.
6. **High Abstraction Level**: Core framework choices (such as choosing an integration style or architectural pattern) that shape all subsequent designs.

## Related Concepts

- [[Architectural Decision]]
- [[Architectural Decision Record]]
- [[AD Definition of Done]]
- [[ADR Adoption and Practices]]

## Source References

- [A Definition of Ready for Architectural Decisions (ADs)](../Raw/Sources/A%20Definition%20of%20Ready%20for%20Architectural%20Decisions%20(ADs).md)

## Changelog

| Date | Change |
|---|---|
| 2026-07-19 | Initial creation |

---

*This note was generated from the `_templates/wiki-note.md` template.*
*Run `python scripts/wiki_tool.py lint` before committing.*
