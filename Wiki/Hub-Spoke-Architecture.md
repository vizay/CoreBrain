---
title: "Hub-Spoke Architecture"
tags:
  - "architecture"
  - "llm-wiki"
  - "system-design"
  - "multi-vault"
created_date: "2026-07-19"
updated_date: "2026-07-19"
sources:
  - "Raw/Sources/Why LLM Wiki 🧠 Future Of Knowledge For Agentic AI & Humans.md"
  - "Raw/Sources/How To Build LLM Wiki In Obsidian 🧠 A Memory Layer For Any Agentic AI.md"
related:
  - "[[LLM Wiki]]"
  - "[[Raw-Wiki-Schema-Architecture]]"
summary: "A multi-vault LLM Wiki topology where a central CoreBrain hub holds universal, project-agnostic knowledge, and individual project-specific spoke vaults reference hub concepts via Core-prefixed wikilinks while maintaining their own local wiki."
---

# Hub-Spoke Architecture

> **Summary**: A multi-vault LLM Wiki topology where a central CoreBrain hub holds universal, project-agnostic knowledge, and individual project-specific spoke vaults reference hub concepts via `Core: Concept Name` wikilinks while maintaining their own local wiki.

## Core Concept

A single LLM Wiki vault can serve one domain well, but knowledge systems that span multiple projects or teams benefit from a hub-spoke topology:

**The Hub (CoreBrain)** is a shared, universal knowledge vault. It contains foundational concepts — frameworks, tools, patterns, research, and any knowledge that is reusable across all projects. It is maintained by agents and humans collaboratively and is the source of truth for cross-cutting concerns.

**Spoke Vaults** are project-specific local wikis. Each spoke is an independent LLM Wiki deployed into a specific project repository or working context. It maintains its own `Raw/`, `Wiki/`, and `Schema/` layers for project-specific knowledge, but can reference universal concepts from the CoreBrain hub using the `` `Core: Concept Name` `` link format.

This separation keeps local project context isolated and focused, while allowing the hub to grow independently as a compounding universal knowledge base.

The author (Wanderloots) describes a similar personal separation: "I like to keep a separate human vault that's only based on my own thinking, and then I have an LLM vault that I use for my AI generation." The hub-spoke pattern extends this into a team or multi-project setting.

## Key Points

- The CoreBrain is the hub: universal, project-agnostic, shared across all spokes.
- Spoke vaults are project-local: focused, isolated, deployed alongside specific codebases or workstreams.
- `Core: Concept Name` is the linking convention from a spoke to a hub concept (double-bracket wikilink with Core: prefix).
- Standard double-bracketed links (without a prefix) reference local spoke concepts.
- Agents in spoke vaults should be firewalled from other vaults (Obsidian safe system).
- The `Local-Vault-Starter-Kit` in CoreBrain provides the template for deploying a new spoke.

## Related Concepts

- [[LLM Wiki]]
- [[Raw-Wiki-Schema-Architecture]]

## Source References

- [Why LLM Wiki 🧠 Future Of Knowledge For Agentic AI & Humans](../Raw/Sources/Why%20LLM%20Wiki%20🧠%20Future%20Of%20Knowledge%20For%20Agentic%20AI%20&%20Humans.md)
- [How To Build LLM Wiki In Obsidian](../Raw/Sources/How%20To%20Build%20LLM%20Wiki%20In%20Obsidian%20🧠%20A%20Memory%20Layer%20For%20Any%20Agentic%20AI.md)

## Changelog

| Date | Change |
|---|---|
| 2026-07-19 | Initial creation |

---

*This note was generated from the `_templates/wiki-note.md` template.*
*Run `python scripts/wiki_tool.py lint` before committing.*
