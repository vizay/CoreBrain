---
title: "ADR - Template Engine Strategy for LLM Wikis"
description: "Architectural Decision Record regarding the use of standardized templates as an immutable blueprint for agent-generated wiki nodes."
tags:
  - "clippings"
---

# ADR - Template Engine Strategy for LLM Wikis

## Context and Problem Statement
Left to their own devices, Large Language Models format markdown outputs arbitrarily. While they can generate excellent summaries, they often introduce inconsistencies in heading hierarchies, metadata tagging, or formatting across different chat sessions. For an LLM Wiki to act as a structured database (queried by programmatic tools), every node in the wiki must retain an identical, parseable structure—specifically frontmatter, core concepts, key points, related links, and a changelog. How do we ensure agents consistently output identically structured markdown documents across all invocations?

## Considered Options
* **Prompt Engineering**: Provide the desired markdown structure as an explicit string within the system prompt or agent skill description.
* **Template Engine Strategy**: Maintain a physical `_templates/` directory containing blueprint files (e.g., `wiki-note.md`) with explicit `{{PLACEHOLDERS}}` that agents read and fill.
* **Post-processing Linter Auto-fix**: Allow the LLM to generate arbitrary text and use a script to try and regex-format it into the correct shape.

## Decision Outcome
Chosen option: **Template Engine Strategy**, because storing templates as physical files is superior to prompt-based structures. Agent skills (like `wiki-ingest`) are instructed to explicitly read `_templates/wiki-note.md` and use it as an immutable blueprint.

### Consequences
* **Good, because** it decouples the formatting logic from the prompt logic. Changing the structure of all future wiki notes only requires editing one markdown file, rather than updating multiple agent skill prompts.
* **Good, because** having explicit placeholders (`{{TITLE}}`, `{{TAG_1}}`) visually communicates the schema requirements to the LLM better than prose descriptions.
* **Bad, because** it requires the agent to spend context-window tokens reading the template file during the generation step.
