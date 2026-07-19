---
title: "MADR"
tags:
  - "concept"
  - "madr"
  - "template"
  - "documentation"
created_date: "2026-07-19"
updated_date: "2026-07-19"
sources:
  - "Raw/Sources/The Markdown ADR (MADR) Template Explained and Distilled.md"
  - "Raw/Sources/MADR Template.md"
  - "Raw/Sources/MADR Template minimal.md"
  - "Raw/Sources/ADR Templates.md"
related:
  - "[[Architectural Decision Record]]"
  - "[[Architectural Decision]]"
summary: "Markdown Architectural Decision Records (MADRs) standardize ADR documenting in Markdown, providing both full and minimal templates optimized for version control and machine readability."
---

# MADR (Markdown Architectural Decision Record)

> **Summary**: Markdown Architectural Decision Records (MADRs) standardize ADR documenting in Markdown, providing both full and minimal templates optimized for version control and machine readability.

## Core Concept

**MADR** (Markdown Architectural Decision Record) is an open-source specification and template designed to make documenting architectural decisions as lean and structured as possible. By using Markdown, MADRs integrate seamlessly into version control (git), code review processes, and standard development IDEs. 

Crucially, the MADR template is designed to be **machine-readable** and **parseable**, allowing development teams to build automated tooling to lint records, generate decision logs, or export indexes (e.g., using toolings like `adr-log` or custom scripts).

---

## MADR Template Structures

The MADR project defines two primary formats for recording decisions:

### 1. Minimal Template
Ideal for simple, low-risk, or rapid-turnaround decisions. It contains only the essential fields:

```markdown
# {Short Title Representative of Problem and Solution}

## Context and Problem Statement
{Describe the context, problem statement, and core question in 2-3 sentences.}

## Considered Options
* {Title of Option 1}
* {Title of Option 2}
* ...

## Decision Outcome
Chosen option: "{Title of Option 1}", because {justification}.

### Consequences
* Good, because {positive consequence}
* Bad, because {negative consequence}
```

### 2. Full Template
Used for complex or high-risk architectural decisions. It adds optional metadata and detailed trade-off matrices:

- **Optional Frontmatter**: Metadata tags such as `status`, `date`, `decision-makers`, `consulted`, and `informed`.
- **Decision Drivers**: Explicit bulleted list of forces, requirements, and constraints guiding the choice.
- **Pros and Cons of the Options**: Dedicated sub-sections for each considered option, documenting:
  - Description/details
  - Good consequences (pros)
  - Bad consequences (cons)
- **Confirmation**: Explains how implementation compliance will be verified (e.g., ArchUnit tests, code reviews, manual audits).

---

## Key Points

- **Markdown Native**: Perfect for local-first documentation, code repository integration, and pull-request-based reviews.
- **Machine Readable**: Structured Markdown headers allow tools to automatically build a catalog and parse statuses.
- **Pragmatic Flexibility**: Teams can start with the minimal template and scale up to the full template only as technical complexity requires.
- **Compliance Validation**: The "Confirmation" block in the full template ensures decisions are not just captured but programmatically or procedurally enforced.

## Related Concepts

- [[Architectural Decision Record]]
- [[Architectural Decision]]
- [[ADR Adoption and Practices]]

## Source References

- [The Markdown ADR (MADR) Template Explained and Distilled](../Raw/Sources/The%20Markdown%20ADR%20(MADR)%20Template%20Explained%20and%20Distilled.md)
- [MADR Template](../Raw/Sources/MADR%20Template.md)
- [MADR Template minimal](../Raw/Sources/MADR%20Template%20minimal.md)
- [ADR Templates](../Raw/Sources/ADR%20Templates.md)

## Changelog

| Date | Change |
|---|---|
| 2026-07-19 | Initial creation |

---

*This note was generated from the `_templates/wiki-note.md` template.*
*Run `python scripts/wiki_tool.py lint` before committing.*
