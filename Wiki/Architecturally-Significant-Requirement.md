---
title: "Architecturally Significant Requirement"
tags:
  - "concept"
  - "architecture"
  - "requirements"
created_date: "2026-07-19"
updated_date: "2026-07-19"
sources:
  - "Raw/Sources/Architecturally significant requirements.md"
related:
  - "[[Architectural-Decision]]"
summary: "An Architecturally Significant Requirement (ASR) is a requirement that has a measurable effect on a computer system's architecture, encompassing both functional and non-functional attributes."
---

# Architecturally Significant Requirement

> **Summary**: An Architecturally Significant Requirement (ASR) is a requirement that has a measurable effect on a computer system's architecture, encompassing both functional and non-functional attributes.

## Core Concept

An **Architecturally Significant Requirement (ASR)** is any requirement (functional or non-functional) that shapes a software system's architecture in a measurably identifiable way. 

Historically, software engineering discussions centered around **Non-Functional Requirements (NFRs)** or **Quality Attributes** as the sole drivers of system architecture. However, empirical studies show that:
1. Not all non-functional requirements affect the architecture (some are trivial or localized to individual components).
2. Many functional requirements have massive structural impacts on system design (e.g. data synchronization, offline capabilities, or multi-tenant separation).

Therefore, identifying which requirements are *architecturally significant* is a critical prerequisite for software architecture design.

## Characteristics of ASRs

ASRs can be identified and categorized by their unique descriptive characteristics, indicators, and heuristics:

### Descriptive Characteristics
ASRs are notoriously difficult to work with because they tend to be:
- Hard to define and articulate.
- Expressed vaguely in initial requests.
- Hidden inside other functional requirements.
- Subjective, variable, situational, and initially neglected.

### Key Indicators
A requirement is likely an ASR if it:
- Targets trade-off points (e.g., latency vs. consistency).
- Is highly strict, constraining, or non-negotiable.
- Breaks existing structural assumptions.
- Is associated with high business value or technical risk.
- Represents a concern of a particularly influential stakeholder.
- Has a "first-of-a-kind" (FOAK) character (cannot be addressed by existing components).
- Deviates from QoS/SLA characteristics already supported by the evolving architecture.
- Has caused budget overruns or customer dissatisfaction on past projects.

### Heuristics
When a requirement specifies a system's quality attributes, refers to its core structural features, imposes constraints, or defines the target environment/run-time platforms, it is highly likely to be an ASR.

## Elicitation and Management

Like all quality attributes, ASRs should be specified **SMART** (Specific, Measurable, Achievable, Relevant, Time-bound).
- **Quality Attribute Scenarios**: A structured way to make ASRs specific and measurable (defining source of stimulus, stimulus, environment, artifact, response, and response measure).
- **Quality Attribute Workshops (QAW)**: Structured facilitation methods developed by the Software Engineering Institute (SEI) to elicit and prioritize ASRs.
- **Lightweight Frameworks**: Using quality attribute utility trees tailored for specific application genres keeps architecture analysis lightweight and flexible.

## Impact and Technical Debt

ASRs directly drive and justify **Architectural Decisions (ADs)**. If ASRs are neglected or not properly satisfied:
- They lead to the accumulation of **Technical Debt**, which is costly and hard to resolve later.
- They complicate regulatory and compliance process audits (e.g., if security/compliance requirements were not satisfied by design).

## Related Concepts

- [[Architectural-Decision]]
- [[Architectural-Decision-Record]]
- [[AD-Definition-of-Ready]]

## Source References

- [Architecturally significant requirements](../Raw/Sources/Architecturally%20significant%20requirements.md)

## Changelog

| Date | Change |
|---|---|
| 2026-07-19 | Initial creation from Wikipedia source |

---

*This note was generated from the `_templates/wiki-note.md` template.*
*Run `python scripts/wiki_tool.py lint` before committing.*
