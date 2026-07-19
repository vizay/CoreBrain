---
title: "ADR - Deterministic Python Tooling for Wiki Maintenance"
description: "Architectural Decision Record regarding the use of deterministic Python tooling to maintain the LLM Wiki schema."
tags:
  - "clippings"
processed: true
---

# ADR - Deterministic Python Tooling for Wiki Maintenance

## Context and Problem Statement
LLMs are highly capable of synthesizing and linking knowledge, but they are inherently probabilistic. When operating an LLM Wiki, there is a constant risk that an agent might hallucinate broken links, miss required metadata fields in frontmatter, or fail to maintain a strict index of all created concepts. How do we ensure the Wiki remains structurally sound, consistent, and programmatically accessible without restricting the LLM's generative freedom?

## Considered Options
* **Rely on LLM-native checks**: Prompting the agent to verify its own work and double-check links.
* **Introduce a deterministic Python CLI**: Using a hard-coded script (`wiki_tool.py`) to handle indexing, linting, and logging.
* **Rely on human-in-the-loop manual validation**: Having the human review every metadata tag and link before committing.

## Decision Outcome
Chosen option: **Introduce a deterministic Python CLI (`wiki_tool.py`)**, because it provides hard programmatic constraints that perfectly balance the LLM's probabilistic nature. The tool will enforce schema rules programmatically via a `lint` command, generate the `catalog.jsonl` index via a `build` command, and enforce an immutable log via a `log` command.

### Consequences
* **Good, because** it guarantees the integrity of the knowledge graph (zero broken links and zero malformed frontmatter).
* **Good, because** the generated `catalog.jsonl` provides an instantly searchable, fast-retrieval index for agents to query before they read broader context.
* **Bad, because** it introduces an external Python dependency and requires maintaining script logic alongside the Markdown vault.
