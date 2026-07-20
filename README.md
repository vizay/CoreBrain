<div align="center">
  <h1>🧠 CoreBrain</h1>
  <p><b>A Persistent, Compounding Memory Layer and LLM Wiki for Agentic AI</b></p>
</div>

---

## 📖 What is CoreBrain?

**CoreBrain** is a structured, distributed, agent-friendly knowledge base designed to serve as a persistent memory layer for Agentic AI development. When working with AI coding assistants (like Antigravity, Cursor, or Devin), context windows often get bloated, and AI agents frequently forget overarching architectural decisions, syntax preferences, or global project rules.

CoreBrain solves this by implementing an **LLM Wiki**: a knowledge management system where raw, immutable source materials are synthesized into dense, interconnected markdown notes by the AI itself. This enables your AI agents to query, learn, and abide by a unified set of rules and architectural decisions across any number of projects.

### 💖 Acknowledgements
A massive and appreciative thank you to the YouTuber and creator **[Wanderloots](https://www.youtube.com/@Wanderloots)**. His videos and pioneering concepts on "vibe-coding" and the LLM Wiki were the direct inspiration and foundational blueprint for this entire project. 

---

## 🏗️ Architecture & Design Overview

CoreBrain operates on a **Hub-and-Spoke Architecture**, supported by deterministic tooling:

- **The Hub (CoreBrain)**: This repository. It stores universal, project-agnostic knowledge (e.g., standard frameworks like FastAPI, global coding standards, and Architectural Decision Records). The Hub compiles its knowledge into a static JSON catalog that can be served over the web.
- **The Spokes (Local Vaults)**: Individual application repositories. Each Spoke contains a lightweight initialized version of the wiki (bootstrapped from the Hub). It holds *local*, project-specific knowledge but maintains a read-only dependency on the Hub's universal catalog. This read-only connection acts as a firewall, ensuring that local project nuances or accidental AI edits cannot pollute your global source of truth.
- **Deterministic Tooling**: To prevent AI hallucination and enforce strict structure, CoreBrain relies on standard Python (`wiki_tool.py`) for all mission-critical operations like building the knowledge catalog, linting rules, and searching. It never trusts the AI to manually manage state.

This design ensures that when you update a global rule in your CoreBrain, all of your individual agentic projects (Spokes) can instantly reference the updated knowledge securely.

---

## 📋 Requirements

Before setting up CoreBrain, ensure you have the following installed:

- **Obsidian**: The primary visual interface for reading, organizing, and navigating your markdown knowledge graph.
- **Python 3.8+**: Required for the `wiki_tool.py` deterministic engine. (No external dependencies; it uses only the standard library).
- **Git**: Required for version control, pre-commit hooks, and syncing Spoke repositories with Hub updates.
- **An Agentic AI Environment**: An AI assistant capable of running terminal commands and reading/writing files (e.g., Antigravity, Cursor, Devin).
- **Obsidian Web Clipper** *(Highly Recommended)*: A browser extension used to seamlessly clip documentation and articles into raw markdown format.

---

## 🚀 Getting Started

### 1. Initializing the Obsidian Vault
Since CoreBrain is built on markdown, it is best viewed through Obsidian.
1. Clone or download this repository to your local machine.
2. Open **Obsidian**.
3. Select **"Open folder as vault"** and point it to the root directory of your cloned repository.

### 2. Setting up the CoreBrain (The Hub)
1. Tell your Agentic AI: *"Please run the `/wiki-maintain` skill to rebuild the catalog and ensure there are no errors, then commit the results."* The AI will use the deterministic `wiki_tool.py` to safely prepare the repository.
2. Push your CoreBrain repository to GitHub.
3. Enable **GitHub Pages** on your repository (choose "GitHub Actions" as the source).
4. The included `.github/workflows/deploy-site.yml` will automatically trigger, build your CoreBrain, seamlessly inject the correct public URL, and publish your Hub.

### 3. Setting up a Spoke (Your App's Local Brain)
When starting a new software project (a Spoke), you can initialize its local brain to connect to your deployed Hub:
1. Open your new project repository in your Agentic AI environment.
2. Instruct the AI: *"Please initialize a CoreBrain Spoke by reading this bootstrap file: `https://[YOUR-GITHUB-USERNAME].github.io/CoreBrain/bootstrap.md`"* 
3. The AI will automatically download the initialization script, set up the local wiki structure, install git hooks, and download your Hub's global knowledge cache.
4. **Open Obsidian**, select **"Open folder as vault"**, and point it to your Spoke repository so you can view your local knowledge graph and add new source material to your local brain!

---

## 🎮 Usage Guide

### Using the Hub
The Hub is where you store universal knowledge (e.g., how to use a specific Python framework, global system design rules).
1. **Add Raw Material**: Save documentation, PDFs, or use the Obsidian Web Clipper to drop markdown files into `Raw/Sources/`.
2. **Ingest**: Tell your AI assistant to run the `/wiki-ingest` skill. The agent will read the raw sources, synthesize concepts, and generate well-formatted `Wiki/` notes.
3. **Commit & Deploy**: The AI will automatically run the `lint` tool to ensure everything is structured properly, log the action, and push the changes. Pushing to `main` will automatically update your live static Hub site.

### Using a Spoke
The Spoke is the local brain attached to a specific coding project.
- **Query Global Knowledge**: When developing, if your AI needs to remember global rules, it can run `python scripts/wiki_tool.py search-hub` to search your Hub's cached knowledge without needing to leave the project.
- **Store Local Knowledge**: If your project has specific architectures (like database schemas or local API routing), drop sources into the local `Raw/Sources/` and run local `/wiki-ingest`. 
- **Local Rules**: Add project-specific rules for the AI into `Schema/LOCAL-AGENTS.md`.
- **Upgrade Tooling**: If the Hub updates its base tools, tell your Spoke agent to run `python scripts/wiki_tool.py upgrade-tooling` to securely fetch the newest scripts without overwriting local knowledge.

---

## 🔬 Deep Dive: Under the Hood

CoreBrain is built entirely on standard Markdown, YAML frontmatter, and a single lightweight Python script. No heavy databases or complex vector stores are required.

### The Three-Layer Structure
1. **`Raw/`**: Contains the raw, unprocessed source files (PDFs, Web Clippings). **Rule 1: Raw Sources are strictly immutable.**
2. **`Wiki/`**: The synthesized knowledge. These are highly structured markdown files created by the AI, complete with `sources` arrays referencing the raw files.
3. **`Schema/`**: The rules engine. This folder contains `AGENTS.md` (the non-negotiable rules the AI must follow) and the agent skills (`.agents/skills/`) that teach the AI how to maintain the wiki.

### Dynamic Source Tracking
CoreBrain uses a dynamic, reference-based tracking system for ingestions. Instead of writing a `processed: true` flag inside a file, `wiki_tool.py` natively tracks whether a raw source is "processed" by checking if its filename or path is cited in the frontmatter of any compiled Wiki note. This allows seamless tracking of binary files (like PDFs) while strictly upholding file immutability.

### Deterministic Tooling (`wiki_tool.py`)
Because AI agents can sometimes be unpredictable, CoreBrain relies on standard Python to enforce structure:
- **`build`**: Compiles the `Wiki/` directory into a lightweight `catalog.jsonl` for fast semantic search.
- **`search-catalog`**: Allows the AI to query the knowledge base securely before reading broad context (Rule 3: Query First).
- **`lint`**: A strict pre-commit gate that ensures the AI hasn't hallucinated links, forgotten frontmatter, or modified raw sources.

### Read-Only Firewalling
A critical design feature of CoreBrain is the "air gap" between the Hub and the Spokes. When a Spoke queries the Hub (`search-hub`), it parses the downloaded JSON catalog from the Hub's static site deployment. It does not have write access to the Hub repository. This ensures that a rogue agent working on a specific web application doesn't accidentally hallucinate or modify global architectural guidelines.

### Hosting the static wiki content from the Hub
While the default setup relies on **GitHub Pages** (via the included `.github/workflows/deploy-site.yml`) to serve this static catalog, the architecture is entirely agnostic. You can serve the Hub's `site/` directory from AWS S3, Vercel, Netlify, or any traditional web server. If you choose to host it elsewhere, you simply need to adjust or replace the GitHub Action with your preferred deployment method.

---

## 🤝 Contributing
Contributions are welcome! Please ensure any changes to `wiki_tool.py` pass linting and respect the immutability of the `Raw/` directory.

## 📜 License
[MIT License](LICENSE)
