---
title: "ADR - Git Hygiene and Version Control"
tags:
  - "concept"
  - "adr"
  - "git"
  - "vcs"
created_date: "2026-07-19"
updated_date: "2026-07-19"
sources:
  - "Raw/Sources/ADR - Git Hygiene and Version Control for Local Vaults.md"
related:
  - "[[Architectural-Decision-Record]]"
  - "[[Hub-Spoke-Architecture]]"
summary: "This Architectural Decision Record establishes the rule for untracking IDE-specific UI caches and agent ephemeral log files to prevent Git repository pollution."
---

# ADR - Git Hygiene and Version Control

> **Summary**: This Architectural Decision Record establishes the rule for untracking IDE-specific UI caches and agent ephemeral log files to prevent Git repository pollution.

## Context and Problem Statement
Local markdown vaults are often managed using thick-client IDEs like Obsidian. These tools generate a high volume of IDE-specific UI cache files (e.g., `.obsidian/workspace.json`, `graph.json`) that change every time a user opens a file, resizes a panel, or views the graph. Furthermore, automated LLM agents create ephemeral execution logs and scratch files (e.g., `.agents/**/*.log`, `.agents/**/scratch/`). If these files are tracked in version control, they cause massive, meaningless Git history churn and frequent merge conflicts across different team members or spoke vaults. How do we cleanly version-control the knowledge graph without polluting the repository with UI state?

## Considered Options
1. **Track Everything**: Commit all files within the repository, accepting that history will be noisy.
2. **Exclude IDE folders entirely**: Add `.obsidian/` to `.gitignore`, losing out on syncing universal themes, plugins, and keybindings across the team.
3. **Granular `.gitignore` strategy**: Track universal IDE configurations (like plugins and snippets), but explicitly untrack local cache files and agent ephemeral logs.

## Decision Outcome
Chosen option: **Granular `.gitignore` strategy**. We maintain a specifically crafted `.gitignore` file that explicitly excludes `workspace.json`, `workspace-mobile.json`, `graph.json`, `.trash/`, and `.agents/**/*.log`. Universal configurations (like `appearance.json` or community plugins) remain tracked.

### Consequences
* **Good, because** it ensures the Git commit history only represents genuine changes to knowledge (Raw sources, Wiki nodes, Schema rules, or Scripts) and not transient UI clicks.
* **Good, because** it prevents merge conflicts when multiple agents or human users are interacting with different vaults simultaneously.
* **Bad, because** users must be vigilant; if a new IDE cache file is introduced in a software update, it must be manually added to the `.gitignore` or it will pollute the history.

## Related Concepts
- [[Architectural-Decision-Record]]
- [[Hub-Spoke-Architecture]]

## Source References
- [ADR - Git Hygiene and Version Control for Local Vaults](../Raw/Sources/ADR%20-%20Git%20Hygiene%20and%20Version%20Control%20for%20Local%20Vaults.md)

## Changelog
| Date | Change |
|---|---|
| 2026-07-19 | Initial Ingestion |

---
*This note was generated from the `_templates/wiki-note.md` template.*
*Run `python scripts/wiki_tool.py lint` before committing.*
