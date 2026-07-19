---
title: "ADR - Template Engine Strategy"
tags:
  - "concept"
  - "adr"
  - "templates"
  - "standardization"
created_date: "2026-07-19"
updated_date: "2026-07-19"
sources:
  - "Raw/Sources/ADR - Template Engine Strategy for LLM Wikis.md"
related:
  - "[[Architectural-Decision-Record]]"
  - "[[Raw-Wiki-Schema-Architecture]]"
summary: "This Architectural Decision Record establishes the use of standard file templates (_templates/) as the formatting blueprint for LLM agent operations."
---

# ADR - Template Engine Strategy

> **Summary**: This Architectural Decision Record establishes the use of standard file templates (`_templates/`) as the formatting blueprint for LLM agent operations.

## Context and Problem Statement
Left to their own devices, Large Language Models format markdown outputs arbitrarily. While they can generate excellent summaries, they often introduce inconsistencies in heading hierarchies, metadata tagging, or formatting across different chat sessions. For an LLM Wiki to act as a structured database (queried by programmatic tools), every node in the wiki must retain an identical, parseable structure—specifically frontmatter, core concepts, key points, related links, and a changelog. How do we ensure agents consistently output identically structured markdown documents across all invocations?

## Considered Options
1. **Prompt Engineering**: Provide the desired markdown structure as an explicit string within the system prompt or agent skill description.
2. **Template Engine Strategy**: Maintain a physical `_templates/` directory containing blueprint files (e.g., `wiki-note.md`) with explicit `{{PLACEHOLDERS}}` that agents read and fill.
3. **Post-processing Linter Auto-fix**: Allow the LLM to generate arbitrary text and use a script to try and regex-format it into the correct shape.

## Decision Outcome
Chosen option: **Template Engine Strategy**, because storing templates as physical files is superior to prompt-based structures. Agent skills (like `wiki-ingest`) are instructed to explicitly read `_templates/wiki-note.md` and use it as an immutable blueprint.

### Consequences
* **Good, because** it decouples the formatting logic from the prompt logic. Changing the structure of all future wiki notes only requires editing one markdown file, rather than updating multiple agent skill prompts.
* **Good, because** having explicit placeholders (`{{TITLE}}`, `{{TAG_1}}`) visually communicates the schema requirements to the LLM better than prose descriptions.
* **Bad, because** it requires the agent to spend slightly more time/tokens during its initial planning phase to use its file-reading tool to fetch the actual rules file.

## Related Concepts
- [[Architectural-Decision-Record]]
- [[Raw-Wiki-Schema-Architecture]]

## Source References
- [ADR - Template Engine Strategy for LLM Wikis](../Raw/Sources/ADR%20-%20Template%20Engine%20Strategy%20for%20LLM%20Wikis.md)

## Changelog
| Date | Change |
|---|---|
| 2026-07-19 | Initial Ingestion |

---
*This note was generated from the `_templates/wiki-note.md` template.*
*Run `python scripts/wiki_tool.py lint` before committing.*
