---
title: "ADR - Agent Pointer Routing"
tags:
  - "concept"
  - "adr"
  - "routing"
  - "configuration"
created_date: "2026-07-19"
updated_date: "2026-07-19"
sources:
  - "Raw/Sources/ADR - Agent Pointer Routing via .agents directory.md"
related:
  - "[[Architectural-Decision-Record]]"
  - "[[Raw-Wiki-Schema-Architecture]]"
  - "[[ADR-Project-Scoped-Agent-Skills]]"
summary: "This Architectural Decision Record establishes the use of pointer files (.agents/AGENTS.md) to redirect agent attention to centralized repository rules."
---

# ADR - Agent Pointer Routing

> **Summary**: This Architectural Decision Record establishes the use of pointer files (`.agents/AGENTS.md`) to redirect agent attention to centralized repository rules.

## Context and Problem Statement
In a multi-vault LLM Wiki architecture, the "Schema" layer defines the core contract for how agents must behave (e.g., rules against hallucinating links, required metadata formats). The universal rules are located centrally at `Schema/AGENTS.md`. However, LLM agent environments generally only look for custom rules in a local, root-level Workspace Customizations directory (specifically `.agents/AGENTS.md`). If we duplicate the rules from `Schema/AGENTS.md` into every spoke vault's `.agents/` folder, they will inevitably drift out of sync. How do we ensure local agents automatically execute the centralized schema rules without duplicating them?

## Considered Options
1. **Duplicate files (Sync Script)**: Maintain a script that continuously copies `Schema/AGENTS.md` into `.agents/AGENTS.md` across all vaults.
2. **Symlinks**: Use OS-level symlinks to map `.agents/AGENTS.md` to `Schema/AGENTS.md`.
3. **Agent Pointer Routing**: Create a permanent, minimal `.agents/AGENTS.md` file whose sole content is an explicit instruction telling the agent to "Always read and strictly adhere to the rules defined in `Schema/AGENTS.md` before taking any action".

## Decision Outcome
Chosen option: **Agent Pointer Routing**. We use a minimal `.agents/AGENTS.md` file as a functional pointer. Because agent systems natively ingest `.agents/AGENTS.md` upon initialization, the LLM reads the instruction and immediately dynamically references the centralized `Schema/` layer before executing tasks.

### Consequences
* **Good, because** it perfectly preserves the Single Source of Truth for rules in `Schema/AGENTS.md`.
* **Good, because** pointer files are plain markdown text, completely OS-agnostic (unlike symlinks which fail on Windows vs Unix), and require no background sync scripts.
* **Bad, because** it requires the agent to spend slightly more time/tokens during its initial planning phase to use its file-reading tool to fetch the actual rules file.

## Related Concepts
- [[Architectural-Decision-Record]]
- [[Raw-Wiki-Schema-Architecture]]
- [[ADR-Project-Scoped-Agent-Skills]]

## Source References
- [ADR - Agent Pointer Routing via .agents directory](../Raw/Sources/ADR%20-%20Agent%20Pointer%20Routing%20via%20.agents%20directory.md)

## Changelog
| Date | Change |
|---|---|
| 2026-07-19 | Initial Ingestion |

---
*This note was generated from the `_templates/wiki-note.md` template.*
*Run `python scripts/wiki_tool.py lint` before committing.*
