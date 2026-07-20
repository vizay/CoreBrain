---
title: "CoreBrain Architecture Master Document"
description: "The top-level Map of Content (MoC) and Whitepaper detailing the design, topology, and 7 pillars of the CoreBrain LLM Wiki."
tags:
  - "clippings"
---

# CoreBrain Architecture Master Document

## Executive Summary
The **CoreBrain** is a highly structured, centralized "LLM Wiki" designed to serve as an immutable, universally accessible knowledge hub for autonomous AI agents. Unlike standard chat interfaces where knowledge decays over time, the CoreBrain acts as a persistent, version-controlled **Map of Memory** where agents can read, index, and ingest conceptual knowledge programmatically.

## The Core Philosophy
The system is built entirely around the concept of the **LLM Wiki**. The core philosophy states that:
1. **Raw Sources are Immutable**: Humans clip and save source documents (PDFs, articles, transcripts). Agents never modify them.
2. **The Wiki is Agent-Owned**: Agents synthesize, summarize, and cross-reference the raw sources into a graph of Markdown files.
3. **The Schema is the Contract**: A set of rules and tooling defines exactly how the agent must format, validate, and maintain the knowledge graph.

## The Topology
To prevent project-specific knowledge from polluting universal concepts, the architecture employs a **Hub-Spoke Topology**:
* **The Hub (CoreBrain)**: Holds universal, project-agnostic knowledge (e.g., definitions of software architecture, scientific concepts, standard operating procedures).
* **The Spokes (Local Vaults)**: Individual, project-specific repositories where agents actually perform daily work. Spokes link back to the hub using `Core:` wikilinks to retrieve universal knowledge without duplicating it.

## The Directory Structure
The repository strictly adheres to a **Three-Layer Architecture**:
1. `Raw/`: The source of truth containing immutable human-curated clippings.
2. `Wiki/`: The compiled, LLM-generated knowledge graph.
3. `Schema/`: The global rules and structural contracts.

## The 7 Pillars of CoreBrain Design
To ensure agents operate safely and deterministically within this environment, the CoreBrain relies on 7 key Architectural Decision Records (ADRs):

1. **Tooling & Automation**: Because LLMs are probabilistic, the architecture uses a deterministic Python script (`wiki_tool.py`) to build the search catalog and lint markdown schema.
2. **Agent Customization**: Agent workflow instructions (skills) and rules are kept in a version-controlled `.agents/` directory rather than ephemeral UI prompts.
3. **Spoke Scaffolding**: To ensure all newly deployed project spokes are compliant with the hub's structure, the CoreBrain houses a distributable `Local-Vault-Starter-Kit`.
4. **Security Boundary**: Agents operating within local spoke vaults are restricted by OS-level **Read-Only Firewalling** when querying the CoreBrain hub, ensuring universal knowledge cannot be accidentally deleted or overwritten by a rogue project agent.
5. **Standardization**: A **Template Engine Strategy** (`_templates/`) forces agents to generate all wiki notes using explicit file blueprints containing `{{PLACEHOLDERS}}`, eliminating unpredictable formatting.
6. **Version Control**: A granular **Git Hygiene** `.gitignore` strategy explicitly tracks the knowledge graph while excluding all IDE-specific UI caches (e.g., `workspace.json`) and ephemeral agent scratchpads.
7. **Rule Enforcement**: **Agent Pointer Routing** utilizes a minimal `.agents/AGENTS.md` pointer file within local directories to route the agent's attention directly to the central `Schema/AGENTS.md`, ensuring total compliance across environments without duplicating the rulebook.
