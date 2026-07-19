---
title: "ADR - Read-Only Firewalling"
tags:
  - "concept"
  - "adr"
  - "security"
  - "multi-vault"
created_date: "2026-07-19"
updated_date: "2026-07-19"
sources:
  - "Raw/Sources/ADR - Read-Only Firewalling for CoreBrain Hub.md"
related:
  - "[[Architectural-Decision-Record]]"
  - "[[Hub-Spoke-Architecture]]"
summary: "This Architectural Decision Record establishes the enforcement of read-only permissions for spoke vault agents interacting with the central CoreBrain hub."
---

# ADR - Read-Only Firewalling

> **Summary**: This Architectural Decision Record establishes the enforcement of read-only permissions for spoke vault agents interacting with the central CoreBrain hub.

## Context and Problem Statement
In a Hub-Spoke topology, project-specific "spoke" vaults link to universal concepts located in the centralized CoreBrain hub using `Core: Concept Name` wikilinks. Because LLM agents operate actively within these local spoke vaults to ingest data and manage knowledge, there is a risk that a project-focused agent might accidentally modify, overwrite, or delete universal foundational notes located in the CoreBrain hub. How do we ensure that the hub's universal knowledge is protected from local project pollution or unintended agent edits?

## Considered Options
1. **Trust the Agent**: Provide prompts instructing the agent not to modify files outside the local project directory.
2. **Implement Read-Only Firewalling**: Strictly limit the agent's file system permissions and cross-vault tooling to read-only access for the CoreBrain directory.
3. **Duplicate Hub Knowledge**: Copy all hub knowledge into the spoke locally so it doesn't matter if it gets modified (breaks the Single Source of Truth).

## Decision Outcome
Chosen option: **Implement Read-Only Firewalling**, because LLM prompts are not foolproof security mechanisms. The architecture relies on OS-level or IDE-level permission boundaries (the "firewall") that strictly forbid agents operating in a spoke vault from executing `write` or `delete` actions against the CoreBrain repository path.

### Consequences
* **Good, because** it perfectly protects the integrity and universality of the CoreBrain from being polluted by project-specific context.
* **Good, because** it forces a deliberate pull-request (PR) workflow; if an agent discovers that a hub concept genuinely needs updating, a human must approve the change or the agent must submit a PR specifically targeting the CoreBrain repository.
* **Bad, because** it prevents agents from dynamically auto-updating hub notes on the fly when interacting with a local project, slightly slowing down the evolution of universal concepts.

## Related Concepts
- [[Architectural-Decision-Record]]
- [[Hub-Spoke-Architecture]]

## Source References
- [ADR - Read-Only Firewalling for CoreBrain Hub](../Raw/Sources/ADR%20-%20Read-Only%20Firewalling%20for%20CoreBrain%20Hub.md)

## Changelog
| Date | Change |
|---|---|
| 2026-07-19 | Initial ingestion |

---
*This note was generated from the `_templates/wiki-note.md` template.*
*Run `python scripts/wiki_tool.py lint` before committing.*
