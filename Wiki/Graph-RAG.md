---
title: "Graph RAG"
tags:
  - "graph-rag"
  - "retrieval-augmented-generation"
  - "knowledge-graph"
  - "agentic-ai"
created_date: "2026-07-19"
updated_date: "2026-07-19"
sources:
  - "Raw/Sources/Why LLM Wiki 🧠 Future Of Knowledge For Agentic AI & Humans.md"
  - "Raw/Sources/llm-wiki.md"
related:
  - "[[RAG]]"
  - "[[Knowledge Graph]]"
  - "[[LLM Wiki]]"
summary: "Graph RAG is an advanced retrieval approach that traverses the relationship structure between documents and concepts rather than retrieving flat vector chunks, significantly outperforming standard RAG on large, complex, interconnected datasets."
---

# Graph RAG

> **Summary**: Graph RAG is an advanced retrieval approach that traverses the relationship structure between documents and concepts rather than retrieving flat vector chunks, significantly outperforming standard RAG on large, complex, interconnected datasets.

## Core Concept

Where standard [[RAG]] retrieves isolated chunks of text similar to a query, Graph RAG follows the edges of a [[Knowledge Graph]] — traversing relationships between sources, concepts, and entities to find answers that live *between* documents rather than within them.

On larger, complex datasets, Graph RAG significantly outperforms standard RAG. Rather than burning through tokens retrieving thousands of chunks, the AI can follow the relationship between sources much more effectively.

An [[LLM Wiki]] is a practical, personal implementation of the Graph RAG principle: the wiki's cross-references and interlinked pages form the graph that the LLM traverses when answering questions, rather than doing vector retrieval over raw documents.

## Key Points

- Graph RAG traverses relationships between documents; standard RAG retrieves flat chunks.
- Significantly outperforms RAG on complex, high-volume information spanning many sources.
- Token-efficient: follows relationships instead of retrieving thousands of chunks.
- The [[LLM Wiki]] is a pragmatic personal implementation of this principle using plain markdown and wikilinks.
- Requires a structured knowledge graph to exist as a prerequisite.

## Related Concepts

- [[RAG]]
- [[Knowledge Graph]]
- [[LLM Wiki]]

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
