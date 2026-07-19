---
title: "Software Architecture"
tags:
  - "concept"
  - "architecture"
  - "system-design"
created_date: "2026-07-19"
updated_date: "2026-07-19"
sources:
  - "Raw/Sources/Software architecture.md"
related:
  - "[[Architectural-Decision]]"
  - "[[Architecturally-Significant-Requirement]]"
  - "[[Architectural-Decision-Record]]"
summary: "Software Architecture is the set of structures needed to reason about a software system, comprising software elements, relations among them, and properties of both."
---

# Software Architecture

> **Summary**: Software Architecture is the set of structures needed to reason about a software system, comprising software elements, relations among them, and properties of both.

## Core Concept

**Software Architecture** is the discipline of creating and maintaining the structures of a software system. It functions as the blueprint for the system, analogous to the architecture of a building, and helps project management extrapolate necessary development tasks. 

Unlike application design, which focuses on functional processes and data supporting specific services (the *what*), software architecture design focuses on the infrastructure and structural decisions that allow that functionality to execute while satisfying **non-functional requirements (NFRs)** or **quality attributes** (the *how*).

### Two Fundamental Laws of Software Architecture

1. **Everything is a trade-off**: There is rarely a single optimal solution; every decision introduces trade-offs (e.g. performance vs. security, agility vs. stability).
2. **"Why" is more important than "how"**: Documenting the rationale and context behind a choice is far more valuable to a system's evolution than the implementation details of the choice itself.

---

## Core Architecture Activities

Software architecture design is an iterative lifecycle comprising four core activities:

1. **Architectural Analysis**: Understanding the environment and identifying **[[Architecturally-Significant-Requirement|Architecturally Significant Requirements (ASRs)]]** (both functional constraints and QoS/SLA characteristics defined under standards like **ISO/IEC 25010**).
2. **Architectural Synthesis (Design)**: The process of creating and refining the architecture based on ASRs, trade-offs, and evaluation results.
3. **Architecture Evaluation**: Assessing how well the design satisfies requirements, using techniques like the **Architecture Tradeoff Analysis Method (ATAM)** or TARA.
4. **Architecture Evolution**: Maintaining and adapting an existing architecture to meet changes in requirements and environment over the system's life.

### Supporting Activities
- **Knowledge Management & Communication**: Finding, sharing, and retaining architectural knowledge (which is often tacit). Gaps in design reasoning lead to incorrect architectures.
- **Design Reasoning & Decision Making**: Evaluating solution options and tradeoffs to make **[[Architectural-Decision|Architectural Decisions (ADs)]]**.
- **Documentation**: Describing the system through multiple viewpoints, commonly organized using Kruchten's **4+1 architectural view model** (static/logical, dynamic/process, deployment/physical, scenarios).

---

## Patterns and Styles

- **Architectural Pattern**: A proven, reusable solution to a recurring system-level problem, addressing overall structure and quality attributes (e.g., Circuit Breaker).
- **Architectural Style**: A coarse-grained structural organization that defines component and connector types, interactions, and constraints (e.g., Layered Architecture, Microservices, Event-Driven Architecture).

---

## Crucial Architectural Phenomena

### Software Architecture Erosion
Erosion refers to the widening gap between the *intended* architecture and the *implemented* architecture over time.
- **Causes**: Architectural violations, accumulation of technical debt, and knowledge vaporization.
- **Consequences**: Decreased performance, degraded quality, and massive maintenance cost increases. A prime example is the early Mozilla browser, which Netscape had to spend two years completely redeveloping due to poor design and erosion.
- **Measures**: Prevented via code reviews, automated conformance checks, and static analysis; remedied via refactoring and redesign.

### Software Architecture Recovery
The process of reverse-engineering a software system's architecture from its implementation and outdated documentation. Typically relies on static program analysis tools (software intelligence) to regain lost design contexts.

### Brooks' Conceptual Integrity
Introduced by Fred Brooks in *The Mythical Man-Month*, this represents the idea that an architecture must reflect a unified vision of what a system should do and how it should do it. The architect acts as the "keeper of the vision," ensuring additions align with this vision.

### Conway's Law
Melvin Conway's observation (1967) that organizations are constrained to produce system designs that are copies of the communication structures of these organizations.

### Fitness Functions
Automated, continuous design checks used to verify that architectural characteristics (such as scalability or security) do not degrade as the codebase evolves.

## Related Concepts

- [[Architectural-Decision]]
- [[Architecturally-Significant-Requirement]]
- [[Architectural-Decision-Record]]
- [[Hub-Spoke-Architecture]]
- [[Raw-Wiki-Schema-Architecture]]

## Source References

- [Software architecture](../Raw/Sources/Software%20architecture.md)

## Changelog

| Date | Change |
|---|---|
| 2026-07-19 | Initial creation from Wikipedia source |

---

*This note was generated from the `_templates/wiki-note.md` template.*
*Run `python scripts/wiki_tool.py lint` before committing.*
