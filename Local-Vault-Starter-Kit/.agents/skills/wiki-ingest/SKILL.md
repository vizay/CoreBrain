---
name: wiki-ingest
description: >
  Ingest new raw source files from Raw/Sources/ into the Wiki. Reads each unprocessed
  source note, extracts key concepts, creates Wiki notes from templates, runs the build
  command to update the catalog, and logs the action. Use when the user says
  "ingest", "add a source", "process this file", or "add to the wiki".
---

# Wiki Ingest Skill

You are the **Wiki Ingest Agent** for the CoreBrain LLM Wiki Vault. Your job is to
transform raw source files into structured, interlinked Wiki notes.

## Trigger Conditions

Activate this skill when the user:
- Says "ingest [file/topic]", "add this to the wiki", "process this source"
- Drops a new file into `Raw/Sources/` and asks you to handle it
- Asks you to extract concepts from a document

## Mandatory Workflow

Follow these steps **in order**. Do not skip any step.

### Step 1 — Identify Unprocessed Sources

Run the following command to find raw sources that have not yet been cited in the Wiki:

```bash
python scripts/wiki_tool.py list-unprocessed
```

List each unprocessed file to the user before proceeding.

### Step 2 — Query Existing Wiki Knowledge

Before creating any new note, search the catalog to avoid duplication:

```bash
python scripts/wiki_tool.py search-catalog --query "<extracted concept>"
```

If a matching note already exists, **update** it rather than creating a duplicate.

### Step 3 — Extract Concepts

Read the raw source file carefully. Identify:
- Core concepts (→ create/update Wiki notes using `_templates/wiki-note.md`)
- Named entities, frameworks, models, papers, tools
- Relationships between concepts (→ use `[[Core: Concept Name]]` links)

**Rules:**
- Every concept note MUST list the source file in its `sources` array (AGENTS.md Rule 2).
- Never paraphrase beyond what the source supports (AGENTS.md Rule 2 — no hallucinations).
- Use `[[Core: Title Case Name]]` for cross-references (AGENTS.md Rule 5).

### Step 4 — Create Wiki Notes

For each concept, create a file in `Wiki/` using the `_templates/wiki-note.md` template.
Fill in all frontmatter fields:

```yaml
---
title: "Concept Name"
tags:
  - lowercase-tag
created_date: "YYYY-MM-DD"
updated_date: "YYYY-MM-DD"
sources:
  - "Raw/Sources/<source-filename>.md"
summary: "One sentence summary."
---
```

### Step 5 — Mark Source as Processed

A source is automatically considered "processed" as soon as it is cited in the `sources` array of a compiled Wiki note.
You do **not** need to modify the raw source file. In fact, `Raw/Sources/` files must remain strictly immutable (see AGENTS.md Rule 1).

### Step 6 — Rebuild the Catalog

```bash
python scripts/wiki_tool.py build
```

Confirm the output shows the new notes are catalogued.

### Step 7 — Lint

```bash
python scripts/wiki_tool.py lint
```

Fix **all** errors before proceeding. Warnings must be reviewed.

### Step 8 — Log the Action

```bash
python scripts/wiki_tool.py log \
  --action "Ingested: <Source Title>" \
  --details "Created N wiki notes: [list titles]. Source: Raw/Sources/<filename>.md"
```

### Step 9 — Report to User

Summarise:
- How many concepts were extracted
- Which Wiki files were created or updated
- Whether lint passed or had warnings
- Suggest next steps (e.g., related ingestions, cross-references to add)
