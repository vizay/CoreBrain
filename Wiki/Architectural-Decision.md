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
  - "Raw/Sources/Architectural decision.md"
related:
  - "[[Architectural-Decision-Record]]"
  - "[[AD-Definition-of-Ready]]"
  - "[[AD-Definition-of-Done]]"
  - "[[Architecturally-Significant-Requirement]]"
summary: "An Architectural Decision (AD) is a justified design choice addressing an architecturally significant requirement (ASR), managed through systematic lifecycle steps."
---

# Architectural Decision

> **Summary**: An Architectural Decision (AD) is a justified design choice addressing an architecturally significant requirement (ASR), managed through systematic lifecycle steps.

## Core Concept

An **Architectural Decision (AD)** is a software engineering design choice that is justified and addresses a functional or non-functional requirement having a measurable impact on a system's quality, architecture, cost, or risk. 

Not all design decisions are architectural. To determine whether a requirement or design issue warrants an explicit architectural decision, it must be evaluated as an **[[Architecturally-Significant-Requirement|Architecturally Significant Requirement (ASR)]]**. 

## History of the Concept

While design rationale was recognized in early software architecture definitions (e.g., Perry and Wolf in 1992), it was not formally studied until the mid-2000s (starting with the Groningen workshop on Architectural Knowledge Management in 2004). Key milestones include:
- The recognition of software architecture as a "set of design decisions" (Jansen and Bosch, 2005).
- The integration of rationale into standard architecture descriptions (such as the **ISO/IEC/IEEE 42010:2011** standard, which defines rationale entities and logs).
- Systematic mapping of knowledge-based architecting approaches to manage tech stack, middleware, and patterns.

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

## Decision Management Steps

An Architectural Decision moves through five distinct lifecycle steps:

1. **Decision Identification**: Articulating design problems (decisions required) and checking urgency/importance. Teams often maintain a *decision backlog* alongside the product backlog.
2. **Decision Making**: Evaluating alternatives and selecting an option. Dialogue mapping is commonly used to build shared understanding. The decision is made when it satisfies a **[[AD-Definition-of-Ready|Definition of Ready (DoR)]]**.
3. **Decision Documentation**: Recording the selected alternative and its rationale (e.g., in an **[[Architectural-Decision-Record|Architectural Decision Record (ADR)]]** or using **Y-Statements**).
4. **Decision Enactment (Enforcement)**: Communicating the choice to stakeholders. Enforced through architecturally evident coding styles and focused code reviews.
5. **Decision Sharing (Optional)**: Structured reuse of decision knowledge and patterns across future projects.

The decision is complete when it satisfies a **[[AD-Definition-of-Done|Definition of Done (DoD)]]**.

### The Y-Statement Template (Example)

Fairbanks' Architecture Haikus evolved into **Y-Statements**, a standardized shorthand for documenting rationale:

> *“In the context of the Web shop service, facing the need to keep user session data consistent and current across shop instances, we decided for the Database Session State Pattern (and against Client Session State or Server Session State) to achieve cloud elasticity, accepting that a session database needs to be designed, implemented, and replicated.”*

## Group Decision-Making Challenges

In practice, architectural design is a collaborative group process. Research shows several common pitfalls in group decision-making:
- **Unstructured Approaches**: Lack of structure restricts broad participation and causes delays or omissions.
- **Lack of Collaboration Tooling**: Few tools support collaborative trade-off evaluation.
- **Group Cognitive Biases**: Teams frequently suffer from **groupthink** (premature consensus) and **group polarization** (shifting to more extreme positions).

## Key Points

- An AD represents a justified, high-impact design choice; an ASR is the driver that triggers it.
- Non-architectural decisions (e.g., class renamings or minor refactoring) should not be recorded as ADRs to avoid logging fatigue.
- Architectural significance is qualitative and context-dependent, aimed at addressing the "worst first."
- Group decision-making without structure often leads to delays, omissions, and cognitive biases like groupthink.

## Related Concepts

- [[Architectural-Decision-Record]]
- [[AD-Definition-of-Ready]]
- [[AD-Definition-of-Done]]
- [[ADR-Adoption-and-Practices]]
- [[Architecturally-Significant-Requirement]]

## Source References

- [Architectural Decision Records (ADRs)](../Raw/Sources/Architectural%20Decision%20Records%20(ADRs).md)
- [Architectural Significance Criteria and Some Core Decisions Required](../Raw/Sources/Architectural%20Significance%20Criteria%20and%20Some%20Core%20Decisions%20Required.md)
- [Architectural decision](../Raw/Sources/Architectural%20decision.md)

## Changelog

| Date | Change |
|---|---|
| 2026-07-19 | Initial creation |
| 2026-07-19 | Ingested Wikipedia source (added history, management steps, Y-statement, and group decision challenges) |

---

*This note was generated from the `_templates/wiki-note.md` template.*
*Run `python scripts/wiki_tool.py lint` before committing.*
