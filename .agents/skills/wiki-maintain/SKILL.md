---
name: wiki-maintain
description: >
  Perform routine maintenance on the wiki: rebuild the catalog, fix broken links,
  update stale notes, and ensure structural integrity. Use when the user says
  "maintain the wiki", "rebuild catalog", "update stale notes", "clean up the wiki",
  or on a scheduled cadence.
---

# Wiki Maintain Skill

You are the **Wiki Maintenance Agent** for the CoreBrain LLM Wiki Vault. Your job is
to keep the vault in a healthy, consistent, and up-to-date state.

## Trigger Conditions

Activate this skill when the user:
- Says "maintain the wiki", "run maintenance", "clean up the wiki"
- Says "rebuild catalog", "update the index", "refresh the wiki"
- Says "find stale notes", "update old entries", "fix broken links"
- Schedules a periodic maintenance run (e.g., weekly)

## Maintenance Checklist

Work through each section in order. Check off items as you complete them.

---

### 1. Rebuild the Catalog

Always start with a fresh catalog build:

```bash
python scripts/wiki_tool.py build
```

Verify the output count. Note any files that were skipped (e.g., no frontmatter).

---

### 2. Run a Full Lint Pass

```bash
python scripts/wiki_tool.py lint
```

Fix **all** errors before continuing. See the `wiki-lint` skill for detailed fix procedures.

---

### 3. Identify Stale Notes

A note is **stale** if:
- Its `updated_date` is more than 90 days old **and** it has no `sources` entries that
  have been updated since

For each stale note found:
1. Check if its raw source has been updated or supplemented
2. If yes, re-read the source and update the note's content and `updated_date`
3. If no update is needed, simply confirm and move on

---

### 4. Verify All [[Core: ...]] Cross-References Are Bidirectional

For every `[[Core: Concept A]]` reference in note B, check whether Concept A's note
also references B (where appropriate). Add missing back-references in the `related`
frontmatter array.

---

### 5. Detect Orphan Notes

An **orphan** is a Wiki note that is not referenced by any other note and has no
`[[Core: ...]]` links to it. List orphans for the user — they may need to be:
- Linked from other notes
- Deleted if irrelevant
- Promoted to a top-level index entry

Search for orphans by scanning all Wiki notes for references to each other.

---

### 6. Check Raw/Sources for Unprocessed Files

```bash
python scripts/wiki_tool.py list-unprocessed
```

List all unprocessed sources and inform the user. Suggest running `wiki-ingest`
for each one.

---

### 7. Update Wiki/log.md

Log the maintenance session:

```bash
python scripts/wiki_tool.py log \
  --action "Maintenance: Routine Pass" \
  --details "Rebuilt catalog. Lint: N errors fixed. Stale notes: M updated. Orphans: K found."
```

---

### 8. Final Lint Confirmation

```bash
python scripts/wiki_tool.py lint
```

Confirm 0 errors before finishing.

---

### 9. Report to User

Provide a maintenance summary:

| Check | Status |
|---|---|
| Catalog rebuilt | ✓ / N notes |
| Lint errors | 0 (or list) |
| Stale notes updated | N |
| Orphan notes | N (list) |
| Unprocessed sources | N (list) |
| Log entry written | ✓ |

Flag any items that require user decisions (e.g., whether to delete orphan notes,
whether to ingest unprocessed sources now).
