---
title: "ADR - Read-Only Firewalling"
tags:
  - "concept"
  - "adr"
  - "security"
  - "multi-vault"
created_date: "2026-07-19"
updated_date: "2026-07-19"
sources:
  - "Raw/Sources/ADR - Read-Only Firewalling for CoreBrain Hub.md"
related:
  - "[[Architectural-Decision-Record]]"
  - "[[Hub-Spoke-Architecture]]"
summary: "This Architectural Decision Record establishes the enforcement of read-only permissions for spoke vault agents interacting with the central CoreBrain hub."
---

# ADR - Read-Only Firewalling

> **Summary**: This Architectural Decision Record establishes the enforcement of read-only permissions for spoke vault agents interacting with the central CoreBrain hub.

## Context and Problem Statement
In a Hub-Spoke topology, project-specific "spoke" vaults link to universal concepts located in the centralized CoreBrain hub. Because LLM agents operate actively within these local spoke vaults to ingest data and manage knowledge, there is a risk that a project-focused agent might accidentally modify, overwrite, or delete universal foundational notes located in the CoreBrain hub. How do we ensure that the hub's universal knowledge is protected from local project pollution or unintended agent edits while remaining easily accessible to spokes?

## Considered Options
1. **Trust the Agent**: Provide prompts instructing the agent not to modify files outside the local project directory. (Rejected)
2. **OS-Level Permissions / IDE Sandboxing**: Strictly limit the agent's file system permissions and cross-vault tooling to read-only access for the CoreBrain directory using file attributes or agent config. (Rejected)
3. **Static Site Distribution via GitHub Pages**: Remove the markdown source files from the spoke's local environment entirely. The hub builds its markdown into static HTML and `catalog.json` payloads hosted on GitHub Pages. Spokes download the cached JSON and query the site via HTTPS. (Chosen Option)

## Decision Outcome
Chosen option: **Static Site Distribution via GitHub Pages**, because it establishes a structural and physical firewall rather than relying on constraints or permissions. By forcing the spoke agents to read the hub through a static site deployed over HTTPS, it becomes physically impossible for a spoke agent to push write actions back to the hub.

### Implementation Details
* The CoreBrain hub runs a `build-site` step via GitHub Actions to compile all `Wiki/*.md` files into a static site hosted on `https://vizay.github.io/CoreBrain`.
* Spoke agents run `python scripts/wiki_tool.py refresh-hub` to download a lightweight `catalog.json` locally.
* Spoke agents use `search-hub` to query the cache and then use HTTP web-fetching tools (`read_url_content`) to read the core concepts over the internet.

### Consequences
* **Good, because** it perfectly protects the integrity and universality of the CoreBrain from being polluted by project-specific context.
* **Good, because** the firewall is structurally inherent in the transport layer (HTTP vs File System) rather than a constraint that has to be enforced.
* **Bad, because** spokes are decoupled from real-time hub updates and must run a `refresh-hub` sync step to get the latest catalogue of CoreBrain concepts.

## Related Concepts
- [[Architectural-Decision-Record]]
- [[Hub-Spoke-Architecture]]

## Source References
- [ADR - Read-Only Firewalling for CoreBrain Hub](../Raw/Sources/ADR%20-%20Read-Only%20Firewalling%20for%20CoreBrain%20Hub.md)

## Changelog
| Date | Change |
|---|---|
| 2026-07-19 | Initial ingestion |

---
*This note was generated from the `_templates/wiki-note.md` template.*
*Run `python scripts/wiki_tool.py lint` before committing.*
