---
title: "Dynamic Reference-Based Source Tracking"
author: "Antigravity Agent"
url: "internal://brain-architecture"
source_type: "documentation"
ingested_date: "2026-07-20"
tags:
  - source
  - architecture
notes: "Documentation for the transition to dynamic source processing."
---

# Dynamic Reference-Based Source Tracking

> **Source file in `Raw/Sources/`. Do NOT edit once ingested. See AGENTS.md Rule 1.**

## Metadata

| Field | Value |
|---|---|
| Author / Origin | Antigravity Agent |
| URL / Reference | internal://brain-architecture |
| Ingested | 2026-07-20 |

## Raw Content

<!-- Paste or transcribe the raw source content below. Do not summarize or paraphrase. -->

The transition to a dynamic reference-based tracking system for raw sources is complete. The system now strictly upholds Rule 1 (Raw Sources Are Immutable) and fully supports binary formats like PDFs.

## What Was Changed

### 1. `list-unprocessed` Command
A new command was added to `wiki_tool.py` (in both the main CoreBrain repository and the `Local-Vault-Starter-Kit`). 
This command intelligently scans all raw sources and compares their filenames and full relative paths against the `sources:` frontmatter array of every compiled Wiki note.

### 2. Rule 1 Immutability Clarification
`AGENTS.md` was updated to explicitly state that processing state is tracked dynamically via citations in Wiki notes, prohibiting agents from writing `processed: true` to source files.

### 3. Skill & Template Simplification
The `wiki-ingest` skill was streamlined:
- In Step 1, the agent runs `python scripts/wiki_tool.py list-unprocessed` instead of scanning files manually.
- In Step 5, the agent skips modifying the source file entirely.
- The `processed: false` flag and the "Processed" metadata table row were removed from `_templates/source-note.md`.

### 4. Codebase Cleanup
A script was run to strip the `processed: true` line from all existing files in `Raw/Sources/`, leaving them as pure, immutable source material.

---

*This note was generated from the `_templates/source-note.md` template.*
*To synthesize concepts from this source, use the `wiki-ingest` skill.*
