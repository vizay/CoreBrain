---
title: "LLM Wiki"
tags:
  - "llm-wiki"
  - "knowledge-management"
  - "agentic-ai"
created_date: "2026-07-19"
updated_date: "2026-07-19"
sources:
  - "Raw/Sources/Why LLM Wiki 🧠 Future Of Knowledge For Agentic AI & Humans.md"
  - "Raw/Sources/llm-wiki.md"
  - "Raw/Sources/How To Build LLM Wiki In Obsidian 🧠 A Memory Layer For Any Agentic AI.md"
  - "Raw/Sources/vibe-codingwanderloots-llm-wiki-core-setup-v1.0.0.md at main.md"
related:
  - "[[Knowledge Graph]]"
  - "[[RAG]]"
  - "[[Graph RAG]]"
  - "[[Raw-Wiki-Schema-Architecture]]"
  - "[[Hub-Spoke-Architecture]]"
summary: "A persistent, compounding knowledge base written and maintained by LLMs that sits between raw source documents and AI tools, replacing per-query RAG retrieval with a pre-compiled, interlinked wiki of structured markdown notes."
---

# LLM Wiki

> **Summary**: A persistent, compounding knowledge base written and maintained by LLMs that sits between raw source documents and AI tools, replacing per-query RAG retrieval with a pre-compiled, interlinked wiki of structured markdown notes.

## Core Concept

Instead of retrieving from raw documents at query time (standard RAG), the LLM incrementally builds and maintains a persistent wiki — a structured, interlinked collection of markdown files that sits between the user and their raw sources. When a new source is added, the LLM reads it, extracts key information, and integrates it into the existing wiki — updating entity pages, revising summaries, noting contradictions, and strengthening the evolving synthesis. The knowledge is compiled once and kept current, not re-derived on every query.

The wiki is a **persistent, compounding artifact**: cross-references are already there, contradictions have already been flagged, and the synthesis already reflects everything that has been read. It grows richer with every source added and every question asked.

The concept was popularised by Andrej Karpathy's GitHub gist and is grounded in years of prior knowledge-graph research.

## Key Points

- The LLM writes and maintains the wiki; the human curates sources and asks questions.
- Unlike RAG, knowledge is compiled once — not re-derived on every query.
- The wiki is just a git repo of markdown files: version history, branching, and collaboration come for free.
- A [[Schema]] (AGENTS.md or CLAUDE.md) acts as the contract between the human and the agent, defining conventions and workflows.
- The human's job: curate sources, direct analysis, ask good questions. The LLM's job: summarizing, cross-referencing, filing, bookkeeping.
- Good answers to queries can be filed back into the wiki as new pages, compounding exploration.
- Obsidian is a natural IDE for this system: the LLM is the programmer, the wiki is the codebase.

## Related Concepts

- [[Knowledge Graph]]
- [[RAG]]
- [[Graph RAG]]
- [[Raw-Wiki-Schema-Architecture]]
- [[Hub-Spoke-Architecture]]

## Source References

- [Why LLM Wiki 🧠 Future Of Knowledge For Agentic AI & Humans](../Raw/Sources/Why%20LLM%20Wiki%20🧠%20Future%20Of%20Knowledge%20For%20Agentic%20AI%20&%20Humans.md)
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
