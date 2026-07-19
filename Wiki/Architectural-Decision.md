---
title: "Architectural Decision"
tags:
  - "concept"
  - "architecture"
  - "decision-making"
created_date: "2026-07-19"
updated_date: "2026-07-19"
sources:
  - "Raw/Sources/Architectural Decision Records (ADRs).md"
  - "Raw/Sources/Architectural Significance Criteria and Some Core Decisions Required.md"
related:
  - "[[Architectural Decision Record]]"
  - "[[AD Definition of Ready]]"
  - "[[AD Definition of Done]]"
summary: "An Architectural Decision (AD) is a justified design choice addressing an architecturally significant requirement (ASR), evaluated against seven core significance criteria."
---

# Architectural Decision

> **Summary**: An Architectural Decision (AD) is a justified design choice addressing an architecturally significant requirement (ASR), evaluated against seven core significance criteria.

## Core Concept

An **Architectural Decision (AD)** is a software engineering design choice that is justified and addresses a functional or non-functional requirement having a measurable impact on a system's quality, architecture, cost, or risk. 

Not all design decisions are architectural. To determine whether a requirement or design issue warrants an explicit architectural decision, it must be evaluated as an **Architecturally Significant Requirement (ASR)**. The distinction is typically evaluated via a qualitative, multi-criteria assessment rather than a simple quantitative scale.

## Seven Criteria for Architectural Significance (The ASR Test)

Olaf Zimmermann proposes a "5+2" model of criteria to assess whether a requirement or technical issue has architectural significance:

### Core Criteria (Objective)
1. **Value and Risk**: High business value or technical risk implication. Preventing violation of compliance/regulations, or protecting against high-impact failures.
2. **Key Concern**: Touches upon a major stakeholder's top priority or concern (e.g., security, compliance, core business capabilities).
3. **New Quality of Service (QoS)**: An unusual QoS requirement that is at least one order of magnitude more advanced than previous systems (e.g., scaling to 10x traffic, reducing latency by 90%).
4. **External Dependency**: High reliance on uncontrollable, unpredictable, or unreliable external dependencies (compile-time, run-time, logical, or organizational).
5. **Cross-Cutting Impact**: System-wide impact affecting multiple layers, components, or cross-cutting technical concerns.

### Context-Specific Heuristics
6. **First-of-a-Kind (FOAK)**: Involves high novelty for the development team (technologies, architectures, or patterns never built by the team before).
7. **Past Trouble/Problem**: Addresses a problem area or technical component that caused severe trouble, technical debt, or failures in the past.

---

## Key Points

- An AD represents a justified, high-impact design choice; an ASR is the driver that triggers it.
- Non-architectural decisions (e.g., class renamings or minor refactoring) should not be recorded as ADRs to avoid logging fatigue.
- Architectural significance is qualitative and context-dependent, aimed at addressing the "worst first."
- Core decisions (such as architecture style, tech stack, and integration mechanisms) have early Most Responsible Moments (MRMs) and should be addressed promptly.

## Related Concepts

- [[Architectural Decision Record]]
- [[AD Definition of Ready]]
- [[AD Definition of Done]]
- [[ADR Adoption and Practices]]

## Source References

- [Architectural Decision Records (ADRs)](../Raw/Sources/Architectural%20Decision%20Records%20(ADRs).md)
- [Architectural Significance Criteria and Some Core Decisions Required](../Raw/Sources/Architectural%20Significance%20Criteria%20and%20Some%20Core%20Decisions%20Required.md)

## Changelog

| Date | Change |
|---|---|
| 2026-07-19 | Initial creation |

---

*This note was generated from the `_templates/wiki-note.md` template.*
*Run `python scripts/wiki_tool.py lint` before committing.*
