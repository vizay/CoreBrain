---
title: "ADR - Agentic-First Bootstrapping"
tags:
  - architecture
  - spoke
  - bootstrapping
created_date: 2026-07-20
updated_date: 2026-07-20
sources:
  - "Raw/Sources/ADR - Agentic-First Bootstrapping for Spokes.md"
---

# ADR - Agentic-First Bootstrapping for Spokes

**Date:** 2026-07-20  
**Status:** Accepted

> **Summary**: This Architectural Decision Record establishes the mechanism for initializing and updating spoke vaults, shifting from developer-executed shell scripts to an Agentic-First Bootstrapping Protocol.

## Context and Problem Statement
When a developer creates a new project that needs to act as a spoke connected to the CoreBrain hub, the local environment must be initialized with the `Local-Vault-Starter-Kit` (containing `.agents/`, `Schema/`, `scripts/`, etc.). Traditionally, developers run setup scripts via `curl` or `wget`. However, relying on OS-dependent shell commands creates friction and breaks the paradigm of an AI-native workflow. How do we make the spoke initialization and tooling update process completely seamless, cross-platform, and native to the agentic ecosystem?

## Considered Options
1. **Traditional Shell Scripts**: Host `init.sh` and `init.ps1` on the CoreBrain hub and have the developer run them in their terminal. (Rejected)
2. **NPM / Pip Packages**: Distribute the starter kit as a global package (e.g., `npx create-corebrain-spoke`). (Rejected)
3. **Agentic-First Bootstrapping Protocol**: Host an LLM-readable Markdown protocol (`bootstrap.md`) on the CoreBrain static site. The developer simply prompts their AI assistant to read the URL, and the AI autonomously downloads, extracts, and configures the environment using a cross-platform Python script embedded in the instructions. (Chosen Option)

## Decision Outcome
Chosen option: **Agentic-First Bootstrapping Protocol**, because it treats the CoreBrain hub as an "Instruction Server" for the AI rather than just a data dump. It works uniformly across any OS or AI-supported IDE without requiring the developer to execute arbitrary code manually.

### Implementation Details

#### 1. Initialization (`bootstrap.md`)
During the `build-site` compilation, the CoreBrain hub dynamically generates a `bootstrap.md` file alongside a `spoke-starter.zip`. The developer prompts their local agent to read `https://vizay.github.io/CoreBrain/bootstrap.md`. The agent follows the instructions, executing a short Python snippet that:
- Downloads and extracts `spoke-starter.zip`.
- Initializes Git and configures a pre-commit hook to enforce `wiki_tool.py lint`.
- Bootstraps the local cache by running `python scripts/wiki_tool.py refresh-hub`.

#### 2. Local vs. Global Rules (`AGENTS.md`)
To ensure that all spokes continuously inherit operational improvements from the CoreBrain, the global `Schema/AGENTS.md` is strictly maintained by the hub and is overwritten during updates. Project-specific agent rules are relegated to `Schema/LOCAL-AGENTS.md`, which is explicitly preserved.

#### 3. Maintenance (`upgrade-tooling` & `update-spoke`)
- The `wiki_tool.py` script includes an `upgrade-tooling` command that re-downloads `spoke-starter.zip` and safely overwrites core scripts and global rules while preserving `LOCAL-AGENTS.md`.
- The `.agents/skills/update-spoke/SKILL.md` skill instructs the agent to run the upgrade, refresh the catalog cache, and proactively audit local wiki notes for any inconsistencies against updated universal concepts.

### Consequences
* **Good, because** setup is completely frictionless and OS-agnostic for developers using agentic IDEs.
* **Good, because** global rules can be pushed to an infinite number of spokes effortlessly.
* **Bad, because** it relies heavily on the AI agent correctly executing the Python snippet during initialization without hallucinations.

## Related Concepts
- [[Architectural-Decision-Record]]
- [[Hub-Spoke-Architecture]]
