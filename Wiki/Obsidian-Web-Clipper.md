---
title: "Obsidian Web Clipper"
tags:
  - tool
  - obsidian
  - capture
created_date: "2026-07-20"
updated_date: "2026-07-20"
sources:
  - "Raw/Sources/Obsidian Web Clipper.md"
  - "Raw/Sources/Clip web pages.md"
summary: "An official, open-source browser extension that captures web pages, articles, and highlights directly into an Obsidian vault as durable Markdown files."
---

# Obsidian Web Clipper

> **Summary**: An official, open-source browser extension that captures web pages, articles, and highlights directly into an Obsidian vault as durable Markdown files.

## Core Concept

The Obsidian Web Clipper is a browser extension that allows users to quickly extract web page content, metadata, and highlights, and save them locally to their Obsidian vault. By using customizable templates, variables, and filters, it serves as a powerful ingestion tool for personal knowledge bases and LLM Wikis.

## Key Features

- **Local Storage**: Clipped content is saved directly to the local vault, maintaining privacy and ensuring data is available offline.
- **Markdown Export**: Captures pages into durable Markdown files without vendor lock-in.
- **Templates**: Users can create specific templates (e.g., for recipes, academic papers, or articles) and even set rules to auto-apply templates based on the website domain.
- **Highlights**: Allows users to highlight text, images, and blocks on a webpage, which remain visible upon revisiting the page, and clip these highlights directly to Obsidian.
- **Content Extraction**: Intelligently extracts the main article content by default but can also extract raw meta tags, Schema.org variables, and element selectors.

## Interfaces & Usage

The extension can be triggered via the browser toolbar icon, hotkeys, or context menu. The interface features four main sections:
1. **Header**: Switch templates, turn on highlighting, read mode, and settings.
2. **Properties**: View and modify the extracted YAML properties.
3. **Note Content**: Preview the extracted Markdown body.
4. **Footer**: Select the target vault and folder, and click "Add to Obsidian".

Images are not downloaded by default (they are linked via URL) to save space, but can be downloaded locally from within Obsidian using a command.
