---
title: "RAG"
tags:
  - "rag"
  - "retrieval-augmented-generation"
  - "agentic-ai"
  - "llm"
created_date: "2026-07-19"
updated_date: "2026-07-19"
sources:
  - "Raw/Sources/Why LLM Wiki 🧠 Future Of Knowledge For Agentic AI & Humans.md"
  - "Raw/Sources/llm-wiki.md"
related:
  - "[[Graph RAG]]"
  - "[[LLM Wiki]]"
  - "[[Knowledge Graph]]"
summary: "Retrieval-Augmented Generation (RAG) is the standard approach where an LLM converts documents into vector embeddings, retrieves the most similar chunks at query time, and generates an answer — rediscovering knowledge from scratch on every question."
---

# RAG

> **Summary**: Retrieval-Augmented Generation (RAG) is the standard approach where an LLM converts documents into vector embeddings, retrieves the most similar chunks at query time, and generates an answer — rediscovering knowledge from scratch on every question.

## Core Concept

RAG works by converting source documents into numerical embeddings (vectors), then at query time finding the chunks most similar to the question and feeding them to the LLM to generate a response. Tools like NotebookLM, ChatGPT file uploads, and most document-AI systems use this pattern.

**The limitation**: the LLM rediscovers knowledge from scratch on every query. There is no accumulation. For simple "what is X" questions this works well. But when the answer lives *between* documents — in the connections and relationships — RAG struggles. It cannot follow the relationship between sources the way a reference librarian knows which books led to which, which chapters are related, which ideas depend on one another.

The [[LLM Wiki]] pattern addresses this limitation by pre-compiling knowledge into a persistent, interlinked structure rather than re-deriving it at query time.

## Key Points

- RAG converts documents to vectors and retrieves relevant chunks at query time.
- Knowledge is never accumulated — it is re-derived from scratch on every question.
- Works well for simple, single-document questions.
- Degrades for complex questions requiring synthesis across many sources.
- Does not preserve relationships between documents.
- The alternative is [[Graph RAG]] (for complex datasets) or the [[LLM Wiki]] pattern (for persistent, curated knowledge bases).

## Related Concepts

- [[Graph RAG]]
- [[LLM Wiki]]
- [[Knowledge Graph]]

## Source References

- [Why LLM Wiki 🧠 Future Of Knowledge For Agentic AI & Humans](../Raw/Sources/Why%20LLM%20Wiki%20🧠%20Future%20Of%20Knowledge%20For%20Agentic%20AI%20&%20Humans.md)
- [llm-wiki (Karpathy Gist)](../Raw/Sources/llm-wiki.md)

## Changelog

| Date | Change |
|---|---|
| 2026-07-19 | Initial creation |

---

*This note was generated from the `_templates/wiki-note.md` template.*
*Run `python scripts/wiki_tool.py lint` before committing.*
