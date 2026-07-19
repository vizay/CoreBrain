---
title: "Knowledge Graph"
tags:
  - "knowledge-graph"
  - "graph-theory"
  - "knowledge-management"
created_date: "2026-07-19"
updated_date: "2026-07-19"
sources:
  - "Raw/Sources/Why LLM Wiki 🧠 Future Of Knowledge For Agentic AI & Humans.md"
  - "Raw/Sources/llm-wiki.md"
related:
  - "[[LLM Wiki]]"
  - "[[RAG]]"
  - "[[Graph RAG]]"
summary: "A structured map of knowledge composed of nodes (concepts, entities, events), edges (named relationships), and triples (subject-relationship-object), allowing knowledge to compound and interconnect over time."
---

# Knowledge Graph

> **Summary**: A structured map of knowledge composed of nodes (concepts, entities, events), edges (named relationships), and triples (subject-relationship-object), allowing knowledge to compound and interconnect over time.

## Core Concept

A knowledge graph is built from three atomic elements:

- **Node**: a thing — a person, idea, place, event, or concept.
- **Edge**: a named relationship between two nodes (e.g. "caused", "depends on", "leads to", "references").
- **Triple**: the atom of a knowledge graph — subject, relationship, object. Two things and one connector.

Knowledge graphs scale by iteration: each triple connects to others, forming a compounding map that grows with every addition. Notable real-world examples include Google's Knowledge Graph (powering the side panel in search results) and Wikipedia (where every hyperlinked term is a node).

In Obsidian, a knowledge graph emerges naturally from `[[wikilinks]]`: each linked concept becomes a node, and the link itself is the edge. The structure is not designed upfront — it is what happens when notes are taken specifically about the relationships between concepts.

## Key Points

- The graph compounds over time: new connections can link back to notes written years earlier.
- Knowledge graphs enable discovery of connections between seemingly unrelated concepts.
- They form the foundation for [[Graph RAG]], where AI traverses relationships rather than retrieving flat chunks.
- Google and Wikipedia are large-scale examples of knowledge graphs in practice.
- Obsidian's graph view visualises the shape of a personal knowledge graph — hubs, orphans, and clusters.

## Related Concepts

- [[LLM Wiki]]
- [[RAG]]
- [[Graph RAG]]

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
