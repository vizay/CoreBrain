---
title: "ADR - Project-Scoped Agent Skills"
tags:
  - "concept"
  - "adr"
  - "agentic-ai"
  - "workflows"
created_date: "2026-07-19"
updated_date: "2026-07-19"
sources:
  - "Raw/Sources/ADR - Project-Scoped Agent Skills and Rules.md"
related:
  - "[[Architectural-Decision-Record]]"
  - "[[Raw-Wiki-Schema-Architecture]]"
summary: "This Architectural Decision Record establishes the use of a dedicated .agents directory to store executable workflow skills and global agent rules within version control."
---

# ADR - Project-Scoped Agent Skills

> **Summary**: This Architectural Decision Record establishes the use of a dedicated `.agents/` directory to store executable workflow skills and global agent rules within version control.

## Context and Problem Statement
LLM agents interacting with the wiki require specific, repeatable instructions on how to perform routine operations (e.g., how to correctly ingest a Wikipedia clipping, how to resolve linting errors, or how to rebuild the catalog). If these instructions are maintained only in a chat UI's custom prompt configuration, they are not version-controlled, cannot be audited, and are not automatically deployed alongside the vault to new environments. How do we ensure agent behavior is deterministic, version-controlled, and instantly portable to any new machine or spoke vault?

## Considered Options
1. **Rely on UI-based custom prompts**: Paste workflows into the agent's system prompt or GUI settings.
2. **Store skills as normal Wiki notes**: Write prompt instructions as standard Markdown files inside `Wiki/`.
3. **Introduce a dedicated `.agents/` customization directory**: Store skills as `SKILL.md` files and rules as `AGENTS.md` in a directory specifically monitored by the agent.

## Decision Outcome
Chosen option: **Introduce a dedicated `.agents/` customization directory**, because it integrates seamlessly with native agent discovery mechanisms (Workspace Customizations Root). By storing workflow pipelines (like `wiki-ingest` and `wiki-lint`) as `SKILL.md` files in `.agents/skills/`, and overriding global behavior via `.agents/AGENTS.md`, the LLM inherently learns how to operate the repository the moment it opens it.

### Consequences
* **Good, because** agent behavior becomes co-located with the codebase, fully version-controlled, and auditable.
* **Good, because** new spoke vaults automatically inherit their agent execution pipelines by copying the `.agents/` directory from the starter kit.
* **Bad, because** maintaining complex multi-step prompt pipelines in markdown requires careful syntax formatting (YAML frontmatter) to be recognized properly by IDE interpreters.

## Related Concepts
- [[Architectural-Decision-Record]]
- [[Raw-Wiki-Schema-Architecture]]

## Source References
- [ADR - Project-Scoped Agent Skills and Rules](../Raw/Sources/ADR%20-%20Project-Scoped%20Agent%20Skills%20and%20Rules.md)

## Changelog
| Date | Change |
|---|---|
| 2026-07-19 | Initial ingestion |

---
*This note was generated from the `_templates/wiki-note.md` template.*
*Run `python scripts/wiki_tool.py lint` before committing.*
