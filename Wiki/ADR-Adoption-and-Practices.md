---
title: "ADR Adoption and Practices"
tags:
  - "concept"
  - "best-practices"
  - "adr"
  - "adoption"
created_date: "2026-07-19"
updated_date: "2026-07-19"
sources:
  - "Raw/Sources/AD Practices.md"
  - "Raw/Sources/How to create Architectural Decision Records (ADRs) — and how not to.md"
  - "Raw/Sources/How to review Architectural Decision Records (ADRs) — and how not to.md"
  - "Raw/Sources/An Adoption Model for Architectural Decision Making and Capturing.md"
  - "Raw/Sources/Decision-making ADRs weightings are a work-around.md"
related:
  - "[[Architectural Decision]]"
  - "[[Architectural Decision Record]]"
  - "[[MADR]]"
summary: "Compiles industry best practices for writing, reviewing, and adopting Architectural Decision Records, including key anti-patterns, criteria normalization, and the five-level AD adoption model."
---

# ADR Adoption and Practices

> **Summary**: Compiles industry best practices for writing, reviewing, and adopting Architectural Decision Records, including key anti-patterns, criteria normalization, and the five-level AD adoption model.

## ADR Creation Practices & Anti-patterns

Standard templates like [[MADR]] provide structure, but creating high-value ADR logs requires team discipline and design maturity.

### Good Practices
- **Select by Significance**: Only log decisions that address at least one [[Architectural Decision#Seven-Criteria-for-Architectural-Significance-The-ASR-Test|Architecturally Significant Requirement (ASR)]] to avoid logging fatigue.
- **Do Not Defer High-Impact Choices**: Hard-to-change options (e.g., programming language, database system) must not be kicked down the road in the name of sprint flexibility.
- **Prioritize Evolutionary Qualities**: Weight criteria toward observability, flexibility, and the ability to adapt rather than speculative long-term scale.
- **Split Wicked Decisions into Stages**: If a final long-term choice is unclear, structure the ADR to define a short-term compromise, a mid-term plan, and a long-term target.
- **State Your Confidence**: Be transparent about doubts or assumptions; a good ADR acts as a living document to be revised as technical spikes yield concrete data.

### Anti-Patterns to Avoid
- **Post-Hoc Alibi Logs**: Writing ADRs solely after-the-fact as a bureaucratic box-checking exercise, rather than using them to actively drive the design process.
- **Micro-Decision Overload**: Documenting minor implementation details (e.g., class names, folder structures) that do not impact quality or cost.
- **Vendor Propaganda**: Aligning justifications with vendor marketing or personal biases instead of concrete requirements and engineering trade-offs.

---

## Normalizing Decision Criteria (The Weighting Workaround)

When comparing options, teams often fall into the trap of using mathematical weightings on criteria to calculate a score. This introduces formula maintenance overhead and hides bias. 

Jacqui Read suggests **normalizing criteria down to the same level of abstraction** as the best solution:
- Avoid mixing high-level drivers (e.g., "compatibility") with low-level details (e.g., "API stability").
- Break high-level concerns down into 3-4 lower-level sub-criteria (e.g., breaking "maintainability" into API stability, release frequency, and developer familiarity).
- Comparing options across normalized, granular criteria provides better decision drivers without requiring complex weightings.

---

## ADR Review Guidelines

Decision records must be peer-reviewed to ensure alignment. Teams should use a standard checklist during sprint reviews or technical board sessions:
1. **Urgency**: Is this decision needed now, or should it be deferred?
2. **Completeness**: Are at least two options compared? Are negative consequences and trade-offs explicitly detailed?
3. **Traceability**: Are the decision drivers mapped directly back to system requirements?
4. **Actionability**: Is there a clear realization and review plan?
5. **Tone**: Is the justification objective, professional, and free of vendor bias?

---

## Architectural Decision Adoption Model (ADAM)

Zimmermann and Anvari define five progressive levels of organizational adoption for AD management:

```
Level 1: Undefined & Unconscious ➔ Decisions made intuitively; zero documentation or reviews.
Level 2: Ad-hoc & Unstructured  ➔ Single teams adopt basic logs, mostly after-the-fact.
Level 3: Encouraged & Supported  ➔ ASRs actively drive critical decisions; light tooling (MADR) adopted.
Level 4: Systematic & Diligent   ➔ JITA/JEA principles applied; mandatory reviews; issue-tracker integration.
Level 5: Optimized & Rigorous    ➔ Curated global ASR catalogs; cross-unit sharing; continuous optimization.
(Ambient & AI-Assisted)          ➔ Emerging Level 6: AI agents assist in capturing, linting, and querying.
```

## Related Concepts

- [[Architectural Decision]]
- [[Architectural Decision Record]]
- [[MADR]]
- [[AD Definition of Ready]]
- [[AD Definition of Done]]

## Source References

- [AD Practices](../Raw/Sources/AD%20Practices.md)
- [How to create Architectural Decision Records (ADRs) — and how not to](../Raw/Sources/How%20to%20create%20Architectural%20Decision%20Records%20(ADRs)%20—%20and%20how%20not%20to.md)
- [How to review Architectural Decision Records (ADRs) — and how not to](../Raw/Sources/How%20to%20review%20Architectural%20Decision%20Records%20(ADRs)%20—%20and%20how%20not%20to.md)
- [An Adoption Model for Architectural Decision Making and Capturing](../Raw/Sources/An%20Adoption%20Model%20for%20Architectural%20Decision%20Making%20and%20Capturing.md)
- [Decision-making ADRs: weightings are a work-around](../Raw/Sources/Decision-making%20ADRs%20weightings%20are%20a%20work-around.md)

## Changelog

| Date | Change |
|---|---|
| 2026-07-19 | Initial creation |

---

*This note was generated from the `_templates/wiki-note.md` template.*
*Run `python scripts/wiki_tool.py lint` before committing.*
