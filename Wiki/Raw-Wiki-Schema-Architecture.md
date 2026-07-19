---
title: "Raw-Wiki-Schema Architecture"
tags:
  - "architecture"
  - "llm-wiki"
  - "system-design"
created_date: "2026-07-19"
updated_date: "2026-07-19"
sources:
  - "Raw/Sources/llm-wiki.md"
  - "Raw/Sources/How To Build LLM Wiki In Obsidian 🧠 A Memory Layer For Any Agentic AI.md"
  - "Raw/Sources/vibe-codingwanderloots-llm-wiki-core-setup-v1.0.0.md at main.md"
related:
  - "[[LLM Wiki]]"
  - "[[Hub-Spoke Architecture]]"
summary: "The three-layer structural foundation of an LLM Wiki: Raw (immutable source documents), Wiki (LLM-generated compiled knowledge notes), and Schema (the agent contract defining conventions, rules, and workflows)."
---

# Raw-Wiki-Schema Architecture

> **Summary**: The three-layer structural foundation of an LLM Wiki: Raw (immutable source documents), Wiki (LLM-generated compiled knowledge notes), and Schema (the agent contract defining conventions, rules, and workflows).

## Core Concept

Every LLM Wiki is built on three distinct layers, each with a clearly defined ownership and responsibility:

### Layer 1 — Raw
Captured source documents: articles, transcripts, papers, PDFs clipped directly into the vault (e.g. via Obsidian Web Clipper). **Raw sources are immutable** — the LLM reads from them but never modifies them. They are the source of truth. If a source needs updating, a new versioned file is added alongside the original.

### Layer 2 — Wiki
A directory of LLM-generated markdown files: summaries, entity pages, concept pages, comparisons, and syntheses. **The LLM owns this layer entirely.** It creates pages, updates them when new sources arrive, maintains cross-references, and keeps everything consistent. The human reads it; the LLM writes it.

### Layer 3 — Schema
A document (e.g. `AGENTS.md` or `CLAUDE.md`) that tells the LLM how the wiki is structured, what conventions to follow, and what workflows to execute when ingesting sources, answering questions, or maintaining the wiki. **This is the key configuration file** — it is what makes the LLM a disciplined wiki maintainer rather than a generic chatbot. The human and LLM co-evolve this over time.

The schema is the **contract between the human and the agent**. Changing naming conventions or templates in the schema propagates to all future agent operations automatically.

## Key Points

- Raw sources are immutable ground truth; the Wiki is the compiled, maintained knowledge layer.
- The LLM writes the Wiki; the human curates Raw sources and evolves the Schema.
- The Schema makes agent behaviour repeatable and consistent across sessions and tools.
- Deterministic Python tooling (`wiki_tool.py`) enforces schema rules programmatically.
- The three layers map directly to folder structure: `Raw/`, `Wiki/`, `Schema/`.

## Related Concepts

- [[LLM Wiki]]
- [[Hub-Spoke Architecture]]

## Source References

- [llm-wiki (Karpathy Gist)](../Raw/Sources/llm-wiki.md)
- [How To Build LLM Wiki In Obsidian](../Raw/Sources/How%20To%20Build%20LLM%20Wiki%20In%20Obsidian%20🧠%20A%20Memory%20Layer%20For%20Any%20Agentic%20AI.md)
- [vibe-coding LLM Wiki Core Setup v1.0.0](../Raw/Sources/vibe-codingwanderloots-llm-wiki-core-setup-v1.0.0.md%20at%20main.md)

## Changelog

| Date | Change |
|---|---|
| 2026-07-19 | Initial creation |

---

*This note was generated from the `_templates/wiki-note.md` template.*
*Run `python scripts/wiki_tool.py lint` before committing.*
