---
title: "Dynamic Source Processing"
tags:
  - architecture
  - llm-wiki
  - process
created_date: "2026-07-20"
updated_date: "2026-07-20"
sources:
  - "Raw/Sources/Dynamic Reference-Based Source Tracking.md"
summary: "An architectural process in the CoreBrain that tracks unprocessed raw sources dynamically through citation references, preserving file immutability and supporting binary formats."
---

# Dynamic Source Processing

> **Summary**: An architectural process in the CoreBrain that tracks unprocessed raw sources dynamically through citation references, preserving file immutability and supporting binary formats.

## Core Concept

Dynamic Source Processing replaces the legacy method of writing a `processed: true` flag inside raw source files. Instead, the processing state of a file in `Raw/Sources/` is evaluated dynamically by checking if its path or filename is cited within the `sources` array of any compiled note in the `Wiki/` folder.

## Key Advantages

1. **Strict Immutability**: By never writing metadata into the source file, this approach fully upholds the rule that raw sources (the ground truth) must remain completely untouched.
2. **Binary File Support**: Because the tracking is reference-based, it natively supports tracking binary files like PDFs, ePUBs, and DOCX files, which cannot contain standard YAML frontmatter.
3. **Simplicity**: The system relies on a simple set difference mechanism via the `wiki_tool.py list-unprocessed` command. It lists files in `Raw/Sources/` that do not appear in any `Wiki/` note's `sources` array.

## Workflow

When an agent invokes the `wiki-ingest` skill, it runs the `list-unprocessed` command to discover pending files. The agent then reads the files, extracts concepts, creates new Wiki notes citing those files, and runs the build command. The raw files immediately vanish from the `list-unprocessed` output without ever being physically modified.
