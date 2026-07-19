---
title: "ADR - Local Vault Starter Kit"
tags:
  - "concept"
  - "adr"
  - "spoke-vault"
  - "scaffolding"
created_date: "2026-07-19"
updated_date: "2026-07-19"
sources:
  - "Raw/Sources/ADR - Local Vault Starter Kit for Spoke Generation.md"
related:
  - "[[Architectural-Decision-Record]]"
  - "[[Hub-Spoke-Architecture]]"
summary: "This Architectural Decision Record establishes the use of a distributable scaffolding directory (Local-Vault-Starter-Kit) within the CoreBrain to spin up standardized, hub-compliant spoke vaults."
---

# ADR - Local Vault Starter Kit

> **Summary**: This Architectural Decision Record establishes the use of a distributable scaffolding directory (`Local-Vault-Starter-Kit`) within the CoreBrain to spin up standardized, hub-compliant spoke vaults.

## Context and Problem Statement
In a multi-vault Hub-Spoke topology, the CoreBrain serves as the centralized hub of universal knowledge. However, individual projects require their own localized "spoke" vaults. Setting up a new spoke vault correctly so that it mirrors the 3-layer architecture (Raw/Wiki/Schema), incorporates the deterministic Python tooling (`wiki_tool.py`), and correctly links back to the hub using `Core:` references is a manual, error-prone process. How do we ensure that new spoke vaults are standardized, rapidly deployable, and architecturally compliant?

## Considered Options
1. **Manual setup documentation**: Write a guide detailing how to create folders and copy scripts manually.
2. **Maintain a `Local-Vault-Starter-Kit` directory**: Store a complete scaffold of a minimal, valid spoke vault directly inside the CoreBrain repository.
3. **External templating repository**: Maintain a completely separate GitHub repository for the spoke template (e.g., `vizay/spoke-template`).

## Decision Outcome
Chosen option: **Maintain a `Local-Vault-Starter-Kit` directory** inside the CoreBrain repository. Keeping the starter kit directly embedded in the CoreBrain ensures that any updates to core scripts (e.g., `wiki_tool.py`), agent skills, or templating conventions (`_templates/`) can be synchronized to the starter kit within the exact same commit.

### Consequences
* **Good, because** new spoke vaults can be bootstrapped instantly by copying a single directory, ensuring 100% architectural compliance out of the box.
* **Good, because** it tightly couples the evolution of the hub's tooling with the template distributed to the spokes, preventing version drift.
* **Bad, because** maintaining the starter kit requires duplicate effort when modifying core scripts (they must be updated in both the CoreBrain root and the `Local-Vault-Starter-Kit/scripts/` directory).

## Related Concepts
- [[Architectural-Decision-Record]]
- [[Hub-Spoke-Architecture]]

## Source References
- [ADR - Local Vault Starter Kit for Spoke Generation](../Raw/Sources/ADR%20-%20Local%20Vault%20Starter%20Kit%20for%20Spoke%20Generation.md)

## Changelog
| Date | Change |
|---|---|
| 2026-07-19 | Initial ingestion |

---
*This note was generated from the `_templates/wiki-note.md` template.*
*Run `python scripts/wiki_tool.py lint` before committing.*
