---
title: "CoreBrain Architecture Overview"
tags:
  - "concept"
  - "architecture"
  - "llm-wiki"
  - "moc"
created_date: "2026-07-19"
updated_date: "2026-07-19"
sources:
  - "Raw/Sources/CoreBrain Architecture Master Document.md"
related:
  - "[[LLM-Wiki]]"
  - "[[Hub-Spoke-Architecture]]"
  - "[[Raw-Wiki-Schema-Architecture]]"
summary: "This document serves as the high-level Map of Content (MoC) and Whitepaper describing the system design, topology, and 7 design pillars of the CoreBrain vault."
---

# CoreBrain Architecture Overview

> **Summary**: This document serves as the high-level Map of Content (MoC) and Whitepaper describing the system design, topology, and 7 design pillars of the CoreBrain vault.

## Core Concept
The **CoreBrain** is a highly structured, centralized "LLM Wiki" designed to serve as an immutable, universally accessible knowledge hub for autonomous AI agents. Unlike standard chat interfaces where knowledge decays over time, the CoreBrain acts as a persistent, version-controlled **Map of Memory** where agents can read, index, and ingest conceptual knowledge programmatically.

## Architectural Foundations

The architecture combines three main conceptual designs:

1. **The LLM Wiki**: Employs a separation of concerns between mutable agent-owned notes (`Wiki/`) and immutable human-curated inputs (`Raw/`).
2. **Hub-Spoke Topology**: Establishes the central CoreBrain as the universal repository (Hub) and individual projects as isolated environments (Spokes) that reference the hub.
3. **Three-Layer Directory Structure**: Physically separates files into `Raw/` (immutability), `Wiki/` (graph), and `Schema/` (governance).

## The 7 Design Pillars (ADRs)
The operational safety, portability, and uniformity of the CoreBrain are enforced through 7 foundational Architectural Decision Records:

* **Pillar 1: Tooling & Automation** — Governed by [[ADR-Deterministic-Python-Tooling]] (`wiki_tool.py` CLI).
* **Pillar 2: Agent Customization** — Governed by [[ADR-Project-Scoped-Agent-Skills]] (`.agents/skills/`).
* **Pillar 3: Spoke Scaffolding** — Governed by [[ADR-Local-Vault-Starter-Kit]] (`Local-Vault-Starter-Kit/`).
* **Pillar 4: Security Boundary** — Governed by [[ADR-Read-Only-Firewalling]] (hub write protection).
* **Pillar 5: Standardization** — Governed by [[ADR-Template-Engine-Strategy]] (`_templates/wiki-note.md`).
* **Pillar 6: Version Control** — Governed by [[ADR-Git-Hygiene-and-Version-Control]] (`.gitignore` rules).
* **Pillar 7: Rule Enforcement** — Governed by [[ADR-Agent-Pointer-Routing]] (centralized schema redirection).

## Related Concepts
- [[LLM-Wiki]]
- [[Hub-Spoke-Architecture]]
- [[Raw-Wiki-Schema-Architecture]]

## Source References
- [CoreBrain Architecture Master Document](../Raw/Sources/CoreBrain%20Architecture%20Master%20Document.md)

## Changelog
| Date | Change |
|---|---|
| 2026-07-19 | Initial Ingestion |

---
*This note was generated from the `_templates/wiki-note.md` template.*
*Run `python scripts/wiki_tool.py lint` before committing.*
