---
name: wiki-lint
description: >
  Run the wiki linter and fix all errors it reports. Use when the user says "lint the
  wiki", "check for errors", "validate the notes", or before any commit. Also activates
  automatically if wiki-ingest or wiki-maintain reports lint failures.
---

# Wiki Lint Skill

You are the **Wiki Lint Agent** for the CoreBrain LLM Wiki Vault. Your job is to
ensure every Wiki note is valid, properly formatted, and correctly cited.

## Trigger Conditions

Activate this skill when the user:
- Says "lint the wiki", "check for errors", "validate notes"
- Is about to commit changes to version control
- Has just run `wiki-ingest` or `wiki-maintain` and lint reported errors
- Asks you to "fix broken citations" or "fix frontmatter"

## Mandatory Workflow

### Step 1 — Run the Linter

```bash
python scripts/wiki_tool.py lint
```

Read the full output carefully. Categorise all findings:
- **Errors** (must fix before committing)
- **Warnings** (should fix, document if deferred)

### Step 2 — Fix Errors Systematically

For each reported error, apply the appropriate fix:

#### Missing or Malformed Frontmatter
Open the file and add a valid YAML frontmatter block at the top using `_templates/wiki-note.md`
as your reference. Ensure the `---` delimiters are on their own lines.

#### Missing Required Fields
Add the missing field(s) to the frontmatter. Required fields are:
`title`, `tags`, `created_date`, `updated_date`, `sources`

#### Empty Tags Array
Add at least one lowercase tag that accurately describes the note's topic.

#### Broken Source Citations
The `sources` entry does not point to a real file. Fix by:
1. Checking if the source file exists in `Raw/Sources/` (possibly renamed or moved)
2. Correcting the path in the `sources` array
3. If the source genuinely does not exist, flag this to the user — do NOT delete the note;
   mark it with a `⚠️ source-missing` tag and log the issue

#### Malformed [[Core: ...]] References
Replace any incorrectly formatted cross-vault references with the canonical format:
`[[Core: Title Case Name]]` — capital C, space after colon, Title Case concept name.

#### [[Core: ...]] References Not in Catalog
The referenced concept note does not exist yet. Options:
1. Create the concept note (using `_templates/wiki-note.md`), then re-run `build`
2. Remove the reference if the concept is genuinely out of scope

### Step 3 — Rebuild Catalog After Fixes

If any new files were created or titles changed:

```bash
python scripts/wiki_tool.py build
```

### Step 4 — Re-Lint to Confirm Clean

```bash
python scripts/wiki_tool.py lint
```

**Do not proceed to commit until lint reports 0 errors.**

### Step 5 — Log the Lint Run

```bash
python scripts/wiki_tool.py log \
  --action "Lint: Completed" \
  --details "Fixed N error(s). Warnings: M. All files pass."
```

### Step 6 — Report to User

- Total errors found and fixed
- Any warnings that were deferred (and why)
- Confirmation that lint is now clean
- Whether any source files were found missing (requiring user action)
