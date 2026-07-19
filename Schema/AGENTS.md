# CoreBrain LLM Wiki — Agent Rules (AGENTS.md)

These rules are **non-negotiable** and apply to every agent interaction within this vault.
All agents, automated scripts, and human contributors must comply.

---

## Rule 1 — Raw Sources Are Immutable

> **Never modify, rename, delete, or overwrite any file inside `Raw/Sources/`.**

Files in `Raw/Sources/` are ground-truth artifacts. They represent the original,
unprocessed inputs to the knowledge pipeline. Any transformation, synthesis, or
summarization must produce output in `Wiki/` — the source file must remain untouched.

If a source needs to be updated, add a new versioned file alongside the original.

---

## Rule 2 — No Hallucinations

> **Do not create a new Wiki page without citing at least one file from `Raw/Sources/`.**

Every Wiki note must include a `sources` array in its YAML frontmatter listing the
relative path(s) of its backing raw source(s). A Wiki page with an empty `sources`
array is considered invalid and will be rejected by `wiki_tool.py lint`.

---

## Rule 3 — Query First

> **Always search `Wiki/catalog.jsonl` using the Python tools before reading broad context.**

Before answering any architectural or knowledge question, run:

```bash
python scripts/wiki_tool.py search-catalog --query "<your query>"
```

This prevents redundant reads, avoids context-window bloat, and ensures answers
are grounded in indexed, validated knowledge. Only fall back to broad file scanning
if `search-catalog` returns no results.

---

## Rule 4 — Lint Before Commit

> **Always run `python scripts/wiki_tool.py lint` before committing any changes.**

No Wiki changes may be committed to version control without a clean lint pass.
The lint command validates:

- YAML frontmatter exists and is well-formed on every `.md` file in `Wiki/`.
- All `tags` fields are non-empty arrays of lowercase strings.
- All entries in the `sources` array resolve to real files in `Raw/Sources/`.
- All `[[Core: Concept Name]]` cross-references appear in `Wiki/catalog.jsonl`.

Fix all lint errors before committing. Lint warnings do not block commits but must
be logged via `python scripts/wiki_tool.py log`.

---

## Rule 5 — Standard Linking (Core Vault)

> **Because you are operating within the Core Knowledge Vault, use standard native wiki links for all concepts.**

When referencing a concept, do **not** use prefixes like `Core:`. Use standard Title Case wiki links. External or uningested concepts are fine to link, but keep the formatting clean.

- ✅ `[[Retrieval-Augmented Generation]]`
- ✅ `[[Transformer Architecture]]`
- ❌ `[[Core: Retrieval-Augmented Generation]]`  ← DO NOT use the Core prefix in this vault.
- ❌ `[[transformer architecture]]`  ← wrong case

---

## Enforcement

| Check | Enforced By |
|---|---|
| Immutability of `Raw/Sources/` | `wiki_tool.py lint` (path check) |
| Sources array non-empty | `wiki_tool.py lint` (frontmatter check) |
| Catalog queried first | Agent self-discipline + skill prompt |
| Clean lint before commit | `wiki_tool.py lint` (pre-commit gate) |
| `[[Core: ...]]` format | `wiki_tool.py lint` (regex + catalog check) |
