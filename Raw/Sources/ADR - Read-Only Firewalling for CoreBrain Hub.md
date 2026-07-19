---
title: "ADR - Read-Only Firewalling for CoreBrain Hub"
description: "Architectural Decision Record regarding the restriction of agent write access to the CoreBrain hub from spoke vaults."
tags:
  - "clippings"
processed: true
---

# ADR - Read-Only Firewalling for CoreBrain Hub

## Context and Problem Statement
In a Hub-Spoke topology, project-specific "spoke" vaults link to universal concepts located in the centralized CoreBrain hub using `Core: Concept Name` wikilinks. Because LLM agents operate actively within these local spoke vaults to ingest data and manage knowledge, there is a risk that a project-focused agent might accidentally modify, overwrite, or delete universal foundational notes located in the CoreBrain hub. How do we ensure that the hub's universal knowledge is protected from local project pollution or unintended agent edits?

## Considered Options
* **Trust the Agent**: Provide prompts instructing the agent not to modify files outside the local project directory.
* **Implement Read-Only Firewalling**: Strictly limit the agent's file system permissions and cross-vault tooling to read-only access for the CoreBrain directory.
* **Duplicate Hub Knowledge**: Copy all hub knowledge into the spoke locally so it doesn't matter if it gets modified (breaks the Single Source of Truth).

## Decision Outcome
Chosen option: **Implement Read-Only Firewalling**, because LLM prompts are not foolproof security mechanisms. The architecture relies on OS-level or IDE-level permission boundaries (the "firewall") that strictly forbid agents operating in a spoke vault from executing `write` or `delete` actions against the CoreBrain repository path.

### Consequences
* **Good, because** it perfectly protects the integrity and universality of the CoreBrain from being polluted by project-specific context.
* **Good, because** it forces a deliberate pull-request (PR) workflow; if an agent discovers that a hub concept genuinely needs updating, a human must approve the change or the agent must submit a PR specifically targeting the CoreBrain repository.
* **Bad, because** it prevents agents from dynamically auto-updating hub notes on the fly when interacting with a local project, slightly slowing down the evolution of universal concepts.
