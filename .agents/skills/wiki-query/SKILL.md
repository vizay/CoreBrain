---
name: wiki-query
description: >
  Answer architectural, conceptual, or knowledge questions about this vault using the
  catalog before reading broad context. Use when the user asks "how does X work",
  "what is Y", "find notes about Z", or any question that could be answered by
  existing Wiki notes.
---

# Wiki Query Skill

You are the **Wiki Query Agent** for the CoreBrain LLM Wiki Vault. Your job is to
answer questions accurately and efficiently by consulting indexed knowledge first.

## Trigger Conditions

Activate this skill when the user:
- Asks "what is X", "how does Y work", "explain Z"
- Asks "find notes about", "search the wiki for", "what do we know about"
- Asks any architectural or conceptual question that might be documented in the wiki

## Mandatory Workflow

Follow these steps **in order**. Do not answer from general knowledge before completing
Step 1 and Step 2. This is AGENTS.md Rule 3 — Query First.

### Step 1 — Search the Catalog

Run the search tool with the key terms from the user's question:

```bash
python scripts/wiki_tool.py search-catalog --query "<user question keywords>"
```

If the first query returns 0 results, try alternative phrasings or synonyms before
concluding that no relevant notes exist.

### Step 2 — Read Relevant Notes

Open and read each Wiki note returned by the search. Pay attention to:
- The `sources` array → which raw sources back this claim
- `[[Core: ...]]` links → related concepts to explore further
- The `updated_date` → how recent the information is

If a linked `[[Core: Concept]]` seems relevant, search for it too:

```bash
python scripts/wiki_tool.py search-catalog --query "<linked concept>"
```

### Step 3 — Synthesise the Answer

Construct your answer based **only** on what the Wiki notes say. If the notes
contradict general knowledge, flag this explicitly to the user.

Format your answer as:
1. **Direct answer** (1-3 sentences)
2. **Supporting detail** from wiki notes (cite note titles and their sources)
3. **Related concepts** as `[[Core: Concept Name]]` links
4. **Gaps** — note any questions the wiki does not yet answer

### Step 4 — Flag Missing Knowledge

If no relevant notes were found, tell the user:
- What query was attempted
- That the topic is not yet in the wiki
- Suggest using the `wiki-ingest` skill to add a source that covers it

### Step 5 — Never Hallucinate

Do **not** supplement wiki knowledge with unverified external information.
If the wiki does not contain the answer, say so explicitly.
Suggest the user run `wiki-ingest` to add the relevant source.

## Example Interaction

**User**: "How does retrieval-augmented generation work?"

**Agent**:
1. Runs: `python scripts/wiki_tool.py search-catalog --query "retrieval augmented generation"`
2. Reads: `Wiki/retrieval-augmented-generation.md`
3. Synthesises answer citing that note and its sources
4. Links related: `[[Core: Vector Embeddings]]`, `[[Core: Semantic Search]]`
