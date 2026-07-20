---
title: "ADR - Agent Pointer Routing via .agents directory"
description: "Architectural Decision Record regarding the use of pointer files to route agent configuration from local environments to centralized schemas."
tags:
  - "clippings"
---

# ADR - Agent Pointer Routing via .agents directory

## Context and Problem Statement
In a multi-vault LLM Wiki architecture, the "Schema" layer defines the core contract for how agents must behave (e.g., rules against hallucinating links, required metadata formats). The universal rules are located centrally at `Schema/AGENTS.md`. However, LLM agent environments generally only look for custom rules in a local, root-level Workspace Customizations directory (specifically `.agents/AGENTS.md`). If we duplicate the rules from `Schema/AGENTS.md` into every spoke vault's `.agents/` folder, they will inevitably drift out of sync. How do we ensure local agents automatically execute the centralized schema rules without duplicating them?

## Considered Options
* **Duplicate files (Sync Script)**: Maintain a script that continuously copies `Schema/AGENTS.md` into `.agents/AGENTS.md` across all vaults.
* **Symlinks**: Use OS-level symlinks to map `.agents/AGENTS.md` to `Schema/AGENTS.md`.
* **Agent Pointer Routing**: Create a permanent, minimal `.agents/AGENTS.md` file whose sole content is an explicit instruction telling the agent to "Always read and strictly adhere to the rules defined in `Schema/AGENTS.md` before taking any action".

## Decision Outcome
Chosen option: **Agent Pointer Routing**. We use a minimal `.agents/AGENTS.md` file as a functional pointer. Because agent systems natively ingest `.agents/AGENTS.md` upon initialization, the LLM reads the instruction and immediately dynamically references the centralized `Schema/` layer before executing tasks. 

### Consequences
* **Good, because** it perfectly preserves the Single Source of Truth for rules in `Schema/AGENTS.md`.
* **Good, because** pointer files are plain markdown text, completely OS-agnostic (unlike symlinks which fail on Windows vs Unix), and require no background sync scripts.
* **Bad, because** it requires the agent to spend slightly more time/tokens during its initial planning phase to use its file-reading tool to fetch the actual rules file.
