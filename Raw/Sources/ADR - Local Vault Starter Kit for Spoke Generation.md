---
title: "ADR - Local Vault Starter Kit for Spoke Generation"
description: "Architectural Decision Record regarding the use of a distributable starter kit for spawning new project spoke vaults."
tags:
  - "clippings"
processed: true
---

# ADR - Local Vault Starter Kit for Spoke Generation

## Context and Problem Statement
In a multi-vault Hub-Spoke topology, the CoreBrain serves as the centralized hub of universal knowledge. However, individual projects require their own localized "spoke" vaults. Setting up a new spoke vault correctly so that it mirrors the 3-layer architecture (Raw/Wiki/Schema), incorporates the deterministic Python tooling (`wiki_tool.py`), and correctly links back to the hub using `Core:` references is a manual, error-prone process. How do we ensure that new spoke vaults are standardized, rapidly deployable, and architecturally compliant?

## Considered Options
* **Manual setup documentation**: Write a guide detailing how to create folders and copy scripts manually.
* **Maintain a `Local-Vault-Starter-Kit` directory**: Store a complete scaffold of a minimal, valid spoke vault directly inside the CoreBrain repository.
* **External templating repository**: Maintain a completely separate GitHub repository for the spoke template (e.g., `vizay/spoke-template`).

## Decision Outcome
Chosen option: **Maintain a `Local-Vault-Starter-Kit` directory** inside the CoreBrain repository. Keeping the starter kit directly embedded in the CoreBrain ensures that any updates to core scripts (e.g., `wiki_tool.py`), agent skills, or templating conventions (`_templates/`) can be synchronized to the starter kit within the exact same commit. 

### Consequences
* **Good, because** new spoke vaults can be bootstrapped instantly by copying a single directory, ensuring 100% architectural compliance out of the box.
* **Good, because** it tightly couples the evolution of the hub's tooling with the template distributed to the spokes, preventing version drift.
* **Bad, because** maintaining the starter kit requires duplicate effort when modifying core scripts (they must be updated in both the CoreBrain root and the `Local-Vault-Starter-Kit/scripts/` directory).
