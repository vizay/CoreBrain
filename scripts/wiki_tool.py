#!/usr/bin/env python3
"""
wiki_tool.py — Deterministic engine for the CoreBrain LLM Wiki Vault.

Commands:
  build           Scan Wiki/ and regenerate Wiki/catalog.jsonl
  lint            Validate all Wiki/ .md files (frontmatter, tags, sources, Core refs)
  search-catalog  Search catalog.jsonl with --query
  log             Append a timestamped entry to Wiki/log.md
  refresh-hub     Download the latest catalog from the Hub (Spokes only)
  search-hub      Search the Hub's catalog.jsonl (Spokes only)
  upgrade-tooling Download the latest scripts and skills from the Hub (Spokes only)

Usage:
  python scripts/wiki_tool.py build
  python scripts/wiki_tool.py lint
  python scripts/wiki_tool.py search-catalog --query "transformer"
  python scripts/wiki_tool.py log --action "Ingested GPT-4 paper" --details "Added 3 wiki notes"
  python scripts/wiki_tool.py refresh-hub
  python scripts/wiki_tool.py search-hub --query "api"
  python scripts/wiki_tool.py upgrade-tooling

Dependencies: Python 3.10+ standard library only (os, json, argparse, re, pathlib, datetime, urllib, zipfile, tempfile).
"""

import os
import json
import argparse
import re
import sys
from pathlib import Path
from datetime import datetime, timezone
import urllib.request
import zipfile
import tempfile
import shutil

# ---------------------------------------------------------------------------
# Path anchors — all paths are relative to the vault root (parent of scripts/)
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
VAULT_ROOT = SCRIPT_DIR.parent
WIKI_DIR = VAULT_ROOT / "Wiki"
RAW_SOURCES_DIR = VAULT_ROOT / "Raw" / "Sources"
CATALOG_FILE = WIKI_DIR / "catalog.jsonl"
LOG_FILE = WIKI_DIR / "log.md"

# ---------------------------------------------------------------------------
# YAML frontmatter helpers
# ---------------------------------------------------------------------------
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
# Matches any [[Core: ...]] variant (forbidden in this vault — see AGENTS.md Rule 5)
CORE_REF_FORBIDDEN_RE = re.compile(r"\[\[Core:[^\]]+\]\]", re.IGNORECASE)
# Matches standard [[Concept Name]] wiki links
WIKI_LINK_RE = re.compile(r"\[\[([^\]|#]+?)(?:[|#][^\]]*)?\]\]")


def _parse_frontmatter(text: str) -> dict | None:
    """Return a dict of frontmatter key-value pairs, or None if absent/malformed."""
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None
    raw = match.group(1)
    result: dict = {}
    # Minimal YAML parser: handles scalars, quoted strings, and inline lists.
    current_key = None
    list_mode = False
    for line in raw.splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        # List item
        stripped_line = line.lstrip()
        if stripped_line.startswith("- "):
            item = stripped_line[2:].split("#")[0].strip().strip('"').strip("'")
            if current_key is not None:
                if not isinstance(result.get(current_key), list):
                    result[current_key] = []
                result[current_key].append(item)
            continue
        # Key: value
        if ":" in line:
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.split("#")[0].strip().strip('"').strip("'")
            current_key = key
            if value == "":
                result[key] = []
                list_mode = True
            else:
                result[key] = value
                list_mode = False
    return result


def _extract_summary(text: str, max_chars: int = 200) -> str:
    """Return a short summary: prefer the `summary` frontmatter field, else first prose line."""
    fm = _parse_frontmatter(text)
    if fm and fm.get("summary"):
        return fm["summary"][:max_chars]
    # Strip frontmatter block
    stripped = FRONTMATTER_RE.sub("", text, count=1).strip()
    for line in stripped.splitlines():
        line = line.strip()
        # Skip headings, blank lines, HTML comments
        if line and not line.startswith("#") and not line.startswith("<!--") and not line.startswith(">"):
            return line[:max_chars]
    return ""


# ---------------------------------------------------------------------------
# Command: build
# ---------------------------------------------------------------------------
def cmd_build(args) -> int:
    """Scan Wiki/ and regenerate catalog.jsonl."""
    WIKI_DIR.mkdir(parents=True, exist_ok=True)
    entries = []
    md_files = sorted(WIKI_DIR.rglob("*.md"))
    for path in md_files:
        # Skip the log file itself
        if path.name == "log.md":
            continue
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        fm = _parse_frontmatter(text)
        title = (fm or {}).get("title") or path.stem.replace("-", " ").replace("_", " ").title()
        summary = _extract_summary(text)
        rel_path = path.relative_to(VAULT_ROOT).as_posix()
        tags = (fm or {}).get("tags", [])
        if isinstance(tags, str):
            tags = [tags]
        entry = {
            "path": rel_path,
            "title": title,
            "summary": summary,
            "tags": tags,
            "sources": (fm or {}).get("sources", []),
            "updated_date": (fm or {}).get("updated_date", ""),
        }
        entries.append(entry)

    # Write catalog
    with CATALOG_FILE.open("w", encoding="utf-8") as f:
        for entry in entries:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    print(f"[build] Catalogued {len(entries)} notes -> {CATALOG_FILE.relative_to(VAULT_ROOT)}")

    return 0


# ---------------------------------------------------------------------------
# Command: lint
# ---------------------------------------------------------------------------
def cmd_lint(args) -> int:
    """Validate all Wiki/ .md files."""
    errors: list[str] = []
    warnings: list[str] = []
    md_files = sorted(WIKI_DIR.rglob("*.md"))

    # Load catalog titles and stems for [[Concept]] link validation
    catalog_titles: set[str] = set()
    catalog_stems: set[str] = set()
    if CATALOG_FILE.exists():
        with CATALOG_FILE.open(encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        entry = json.loads(line)
                        if entry.get("title"):
                            catalog_titles.add(entry["title"])
                        if entry.get("path"):
                            catalog_stems.add(Path(entry["path"]).stem)
                    except json.JSONDecodeError:
                        pass

    catalog_exists = CATALOG_FILE.exists()

    # Collect all raw source filenames for citation validation
    raw_source_files: set[str] = set()
    if RAW_SOURCES_DIR.exists():
        for p in RAW_SOURCES_DIR.rglob("*"):
            if p.is_file():
                # Store both relative posix path and filename stem
                raw_source_files.add(p.relative_to(VAULT_ROOT).as_posix())
                raw_source_files.add(p.name)

    for path in md_files:
        if path.name == "log.md":
            continue
        rel = path.relative_to(VAULT_ROOT).as_posix()
        text = path.read_text(encoding="utf-8-sig", errors="replace")

        # ── 1. Frontmatter must exist ──────────────────────────────────────
        fm = _parse_frontmatter(text)
        if fm is None:
            errors.append(f"{rel}: Missing or malformed YAML frontmatter.")
            continue  # Can't check further without frontmatter

        # ── 2. Required fields ─────────────────────────────────────────────
        for field in ("title", "tags", "created_date", "updated_date", "sources"):
            if field not in fm:
                errors.append(f"{rel}: Frontmatter missing required field `{field}`.")

        # ── 3. Tags must be non-empty lowercase list ────────────────────────
        tags = fm.get("tags", [])
        if isinstance(tags, str):
            tags = [tags]
        if not tags:
            errors.append(f"{rel}: `tags` array is empty.")
        else:
            for tag in tags:
                if tag != tag.lower():
                    warnings.append(f"{rel}: Tag `{tag}` should be lowercase.")

        # ── 4. Sources must resolve to real Raw/Sources/ files ─────────────
        sources = fm.get("sources", [])
        if isinstance(sources, str):
            sources = [sources]
        if not sources:
            errors.append(f"{rel}: `sources` array is empty (AGENTS.md Rule 2).")
        else:
            for src in sources:
                # Accept absolute vault-relative paths or bare filenames
                src_path = VAULT_ROOT / src if not Path(src).is_absolute() else Path(src)
                if not src_path.exists():
                    # Try matching by filename only
                    if Path(src).name not in raw_source_files and src not in raw_source_files:
                        errors.append(f"{rel}: Source `{src}` not found in Raw/Sources/.")

        # ── 5. Standard [[Concept]] link validation ────────────────────────
        # 5a. Flag any forbidden [[Core: ...]] references (AGENTS.md Rule 5)
        for forbidden in CORE_REF_FORBIDDEN_RE.finditer(text):
            errors.append(
                f"{rel}: Forbidden link `{forbidden.group()}` — "
                "do not use the Core: prefix inside this vault (AGENTS.md Rule 5). "
                "Use [[Concept Name]] instead."
            )

        # 5b. Warn when a [[Concept]] link doesn't resolve to a known catalog title
        if not catalog_exists:
            # We don't want to flood warnings if there's no catalog yet.
            if rel == md_files[-1].relative_to(VAULT_ROOT).as_posix():
                warnings.append("Cannot validate [[Concept]] links fully because catalog.jsonl is missing. Run `build` first.")
        else:
            for link_match in WIKI_LINK_RE.finditer(text):
                concept = link_match.group(1).strip()
                # Skip empty, relative path links, and external URLs
                if not concept or concept.startswith("http") or "/" in concept or concept.startswith("."):
                    continue
                
                # Check match against title, filename stem, or normalized version
                normalized_concept = concept.replace("-", " ").replace("_", " ").strip().lower()
                
                match_found = False
                if concept in catalog_titles or concept in catalog_stems:
                    match_found = True
                else:
                    for title in catalog_titles:
                        if title.replace("-", " ").replace("_", " ").strip().lower() == normalized_concept:
                            match_found = True
                            break
                    if not match_found:
                        for stem in catalog_stems:
                            if stem.replace("-", " ").replace("_", " ").strip().lower() == normalized_concept:
                                match_found = True
                                break
                                
                if not match_found:
                    warnings.append(
                        f"{rel}: [[{concept}]] not found in catalog. "
                        "Create the note first, then run `build`."
                    )

    # ── Report ─────────────────────────────────────────────────────────────
    total = len([p for p in md_files if p.name != "log.md"])
    if errors:
        print(f"[lint] FAIL {len(errors)} error(s), {len(warnings)} warning(s) across {total} file(s).\n")
        for e in errors:
            print(f"  ERROR   {e}")
        for w in warnings:
            print(f"  WARNING {w}")
        return 1
    elif warnings:
        print(f"[lint] WARN 0 errors, {len(warnings)} warning(s) across {total} file(s).\n")
        for w in warnings:
            print(f"  WARNING {w}")
        return 0
    else:
        print(f"[lint] OK All {total} file(s) passed with 0 errors, 0 warnings.")
        return 0


# ---------------------------------------------------------------------------
# Command: search-catalog
# ---------------------------------------------------------------------------
def cmd_search_catalog(args) -> int:
    """Search catalog.jsonl for --query and print matching paths."""
    if not CATALOG_FILE.exists():
        print("[search-catalog] catalog.jsonl not found. Run `build` first.", file=sys.stderr)
        return 1

    query = args.query.lower()
    tokens = query.split()
    results = []

    with CATALOG_FILE.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue
            haystack = " ".join([
                entry.get("title", ""),
                entry.get("summary", ""),
                " ".join(entry.get("tags", [])),
            ]).lower()
            score = sum(1 for token in tokens if token in haystack)
            if score > 0:
                results.append((score, entry))

    results.sort(key=lambda x: x[0], reverse=True)

    if not results:
        print(f"[search-catalog] No results for query: '{args.query}'")
        return 0

    print(f"[search-catalog] {len(results)} result(s) for '{args.query}':\n")
    for rank, (score, entry) in enumerate(results, 1):
        print(f"  [{rank}] {entry.get('title', '(no title)')}")
        print(f"       Path    : {entry.get('path', '')}")
        print(f"       Summary : {entry.get('summary', '')[:120]}")
        print(f"       Tags    : {', '.join(entry.get('tags', []))}")
        print()
    return 0


# ---------------------------------------------------------------------------
# Command: list-unprocessed
# ---------------------------------------------------------------------------
def cmd_list_unprocessed(args) -> int:
    """List files in Raw/Sources that are not cited in any Wiki note."""
    if not RAW_SOURCES_DIR.exists():
        return 0

    cited = set()
    for p in WIKI_DIR.rglob("*.md"):
        text = p.read_text(encoding="utf-8-sig", errors="replace")
        fm = _parse_frontmatter(text)
        if fm and "sources" in fm:
            sources = fm["sources"]
            if isinstance(sources, str):
                sources = [sources]
            for s in sources:
                cited.add(s)
                cited.add(Path(s).name)

    unprocessed = set()
    for p in RAW_SOURCES_DIR.rglob("*"):
        if p.is_file():
            rel_path = p.relative_to(VAULT_ROOT).as_posix()
            basename = p.name
            if rel_path not in cited and basename not in cited:
                unprocessed.add(rel_path)

    for uncited in sorted(unprocessed):
        print(uncited)
    return 0


# ---------------------------------------------------------------------------
# Command: log
# ---------------------------------------------------------------------------
def cmd_log(args) -> int:
    """Append a timestamped entry to Wiki/log.md."""
    WIKI_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    action = args.action
    details = args.details or ""

    header_needed = not LOG_FILE.exists()
    with LOG_FILE.open("a", encoding="utf-8") as f:
        if header_needed:
            f.write("# Wiki Activity Log\n\n")
            f.write("Chronological record of all agent actions in this vault.\n\n")
            f.write("---\n\n")
        f.write(f"## {timestamp} — {action}\n\n")
        if details:
            f.write(f"{details}\n\n")
        f.write("---\n\n")

    print(f"[log] Entry appended to {LOG_FILE.relative_to(VAULT_ROOT)}: {action}")
    return 0


# ---------------------------------------------------------------------------
# Command: build-site
# ---------------------------------------------------------------------------
def _slugify(text: str) -> str:
    return text.replace(" ", "-").replace("_", "-").lower()

def _simple_md_to_html(md_text: str, catalog_titles: set) -> str:
    import html
    # Very basic Markdown to HTML
    lines = md_text.splitlines()
    html_lines = []
    in_list = False
    
    for line in lines:
        line_stripped = line.strip()
        if not line_stripped:
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append("<br>")
            continue
            
        # Headings
        if line_stripped.startswith("### "):
            html_lines.append(f"<h3>{html.escape(line_stripped[4:])}</h3>")
        elif line_stripped.startswith("## "):
            html_lines.append(f"<h2>{html.escape(line_stripped[3:])}</h2>")
        elif line_stripped.startswith("# "):
            html_lines.append(f"<h1>{html.escape(line_stripped[2:])}</h1>")
        elif line_stripped.startswith("- "):
            if not in_list:
                html_lines.append("<ul>")
                in_list = True
            html_lines.append(f"<li>{html.escape(line_stripped[2:])}</li>")
        elif line_stripped.startswith("> "):
            html_lines.append(f"<blockquote>{html.escape(line_stripped[2:])}</blockquote>")
        else:
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append(f"<p>{html.escape(line_stripped)}</p>")
            
    if in_list:
        html_lines.append("</ul>")

    html_text = "\n".join(html_lines)
    
    # Process wiki links [[Concept]]
    def link_repl(match):
        concept = match.group(1).strip()
        slug = _slugify(concept)
        return f'<a href="{html.escape(slug)}.html">{html.escape(concept)}</a>'
        
    html_text = re.sub(r"\[\[([^\]|#]+?)(?:[|#][^\]]*)?\]\]", link_repl, html_text)
    
    # Process standard links [Text](url)
    html_text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda m: f'<a href="{html.escape(m.group(2))}">{html.escape(m.group(1))}</a>', html_text)
    
    return html_text

def cmd_build_site(args) -> int:
    """Compile Wiki/ into static HTML in site/."""
    SITE_DIR = VAULT_ROOT / "site"
    SITE_DIR.mkdir(parents=True, exist_ok=True)
    
    md_files = sorted(WIKI_DIR.rglob("*.md"))
    entries = []
    
    # Parse notes
    for path in md_files:
        if path.name == "log.md":
            continue
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        fm = _parse_frontmatter(text)
        title = (fm or {}).get("title") or path.stem.replace("-", " ").replace("_", " ").title()
        summary = _extract_summary(text)
        tags = (fm or {}).get("tags", [])
        if isinstance(tags, str): tags = [tags]
        
        slug = _slugify(title)
        
        entries.append({
            "title": title,
            "slug": slug,
            "summary": summary,
            "tags": tags,
            "content": text,
            "path": path.relative_to(VAULT_ROOT).as_posix()
        })
        
    catalog_titles = {e["title"] for e in entries}
    
    # Generate HTML pages
    css = """
    body { font-family: sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; line-height: 1.6; color: #333; }
    a { color: #0366d6; text-decoration: none; }
    a:hover { text-decoration: underline; }
    blockquote { border-left: 4px solid #dfe2e5; padding-left: 16px; color: #6a737d; }
    .nav { margin-bottom: 20px; padding-bottom: 10px; border-bottom: 1px solid #eaecef; }
    """
    
    for entry in entries:
        html_content = _simple_md_to_html(entry["content"], catalog_titles)
        page_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>{entry['title']} - CoreBrain</title>
<style>{css}</style>
</head>
<body>
<div class="nav"><a href="index.html">← Back to Index</a></div>
{html_content}
</body>
</html>"""
        (SITE_DIR / f"{entry['slug']}.html").write_text(page_html, encoding="utf-8")
        
    # Generate index.html
    index_links = []
    for entry in entries:
        index_links.append(f'<li><a href="{entry["slug"]}.html">{entry["title"]}</a> - {entry["summary"]}</li>')
    
    index_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>CoreBrain Index</title>
<style>{css}</style>
</head>
<body>
<h1>CoreBrain Knowledge Graph</h1>
<p>This is the compiled, read-only static site of the CoreBrain.</p>
<ul>
{"".join(index_links)}
</ul>
</body>
</html>"""
    (SITE_DIR / "index.html").write_text(index_html, encoding="utf-8")
    
    # Write catalog.json (for agents to consume)
    # Strip full content to keep catalog small
    catalog_entries = []
    for entry in entries:
        e = entry.copy()
        e.pop("content", None)
        catalog_entries.append(e)
        
    with (SITE_DIR / "catalog.json").open("w", encoding="utf-8") as f:
        json.dump(catalog_entries, f, ensure_ascii=False, indent=2)
        
    # --- Agentic First Bootstrapping Generation ---
    hub_url = args.url.rstrip('/')
    
    # 1. Package the Starter Kit into spoke-starter.zip
    import zipfile
    import os
    STARTER_KIT_DIR = VAULT_ROOT / "Local-Vault-Starter-Kit"
    ZIP_PATH = SITE_DIR / "spoke-starter.zip"
    if STARTER_KIT_DIR.exists():
        with zipfile.ZipFile(ZIP_PATH, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(STARTER_KIT_DIR):
                for file in files:
                    file_path = Path(root) / file
                    # Relative path inside the zip should not include "Local-Vault-Starter-Kit"
                    arcname = file_path.relative_to(STARTER_KIT_DIR)
                    zipf.write(file_path, arcname)
                    
    # 2. Generate bootstrap.md
    python_script = '''import urllib.request
import zipfile
import tempfile
import pathlib
import json
import os
import subprocess
import sys

if len(sys.argv) < 2:
    print("Usage: python init_spoke.py <HUB_BASE_URL>")
    sys.exit(1)

HUB_URL = sys.argv[1].rstrip("/")
ZIP_URL = f"{HUB_URL}/spoke-starter.zip"

print(f"Downloading spoke-starter.zip from {ZIP_URL}...")
req = urllib.request.Request(ZIP_URL, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    zip_data = response.read()

with tempfile.TemporaryDirectory() as tmpdir:
    zip_path = pathlib.Path(tmpdir) / "spoke-starter.zip"
    zip_path.write_bytes(zip_data)
    with zipfile.ZipFile(zip_path, 'r') as z:
        z.extractall(".")

print("Configuring Schema/hub-config.json...")
os.makedirs("Schema", exist_ok=True)
with open("Schema/hub-config.json", "w") as f:
    json.dump({{"hub_pages_url": HUB_URL}}, f, indent=2)

print("Ensuring git is initialized...")
if not os.path.exists(".git"):
    subprocess.run(["git", "init"])

print("Installing pre-commit hook...")
hook_dir = pathlib.Path(".git/hooks")
if hook_dir.exists():
    hook_path = hook_dir / "pre-commit"
    hook_content = """#!/bin/sh
python scripts/wiki_tool.py lint
if [ $? -ne 0 ]; then
  echo "Wiki lint failed. Fix errors before committing."
  exit 1
fi
"""
    hook_path.write_text(hook_content, encoding="utf-8")
    # Make executable on Unix
    if os.name == 'posix':
        os.chmod(hook_path, 0o755)

print("Hydrating knowledge from CoreBrain hub...")
subprocess.run([sys.executable, "scripts/wiki_tool.py", "refresh-hub"])

print("Spoke initialization complete!")
'''

    bootstrap_content = f"""# Spoke Initialization Protocol

You are an agentic AI initializing a CoreBrain Spoke in the user's repository. Follow these steps exactly:

1. Identify the base URL of this very `bootstrap.md` file you are currently reading. For example, if you read this from `https://example.com/bootstrap.md`, the base URL is `https://example.com`.

2. Save the following python script to a temporary file named `init_spoke.py` in the root of the project:
```python
{python_script}
```

3. Execute the script, passing the base URL as an argument:
```bash
python init_spoke.py <BASE_URL>
```

4. Delete `init_spoke.py` after it finishes successfully.

5. Inform the user that the Spoke is successfully initialized, the catalog has been downloaded, and you are ready to work.
"""
    (SITE_DIR / "bootstrap.md").write_text(bootstrap_content, encoding="utf-8")
        
    print(f"[build-site] Built static site with {len(entries)} notes -> {SITE_DIR.relative_to(VAULT_ROOT)}")
    print(f"[build-site] Generated spoke-starter.zip and bootstrap.md using HUB_URL={hub_url}")
    return 0



# ---------------------------------------------------------------------------
# Spoke Commands (refresh-hub, search-hub, upgrade-tooling)
# ---------------------------------------------------------------------------
def _get_hub_url() -> str:
    config_path = VAULT_ROOT / "Schema" / "hub-config.json"
    if not config_path.exists():
        print("Error: Schema/hub-config.json not found. This command is for Spokes only.", file=sys.stderr)
        sys.exit(1)
    with config_path.open() as f:
        data = json.load(f)
    return data.get("hub_pages_url", "").rstrip("/")

def cmd_refresh_hub(args) -> int:
    """Download the latest catalog from the Hub."""
    hub_url = _get_hub_url()
    catalog_url = f"{hub_url}/catalog.json"
    print(f"[refresh-hub] Fetching global catalog from {catalog_url}...")
    
    req = urllib.request.Request(catalog_url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode("utf-8"))
    except Exception as e:
        print(f"Failed to download catalog: {e}", file=sys.stderr)
        return 1
        
    WIKI_DIR.mkdir(parents=True, exist_ok=True)
    hub_catalog = WIKI_DIR / "hub_catalog.jsonl"
    with hub_catalog.open("w", encoding="utf-8") as f:
        for entry in data:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
            
    print(f"[refresh-hub] Successfully saved {len(data)} global notes to Wiki/hub_catalog.jsonl.")
    return 0

def cmd_search_hub(args) -> int:
    """Search the Hub's catalog.jsonl with --query."""
    hub_catalog = WIKI_DIR / "hub_catalog.jsonl"
    if not hub_catalog.exists():
        print("[search-hub] hub_catalog.jsonl not found. Run `refresh-hub` first.", file=sys.stderr)
        return 1

    query = args.query.lower()
    tokens = query.split()
    results = []

    with hub_catalog.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line: continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue
            haystack = " ".join([
                entry.get("title", ""),
                entry.get("summary", ""),
                " ".join(entry.get("tags", [])),
            ]).lower()
            score = sum(1 for token in tokens if token in haystack)
            if score > 0:
                results.append((score, entry))

    results.sort(key=lambda x: x[0], reverse=True)

    if not results:
        print(f"[search-hub] No results for query: '{args.query}'")
        return 0

    print(f"[search-hub] {len(results)} result(s) for '{args.query}':\n")
    for rank, (score, entry) in enumerate(results, 1):
        print(f"  [{rank}] {entry.get('title', '(no title)')}")
        print(f"       Summary : {entry.get('summary', '')[:120]}")
        print(f"       Tags    : {', '.join(entry.get('tags', []))}")
        print()
    return 0

def cmd_upgrade_tooling(args) -> int:
    """Download the latest scripts and skills from the Hub."""
    hub_url = _get_hub_url()
    zip_url = f"{hub_url}/spoke-starter.zip"
    print(f"[upgrade-tooling] Fetching spoke-starter.zip from {zip_url}...")
    
    req = urllib.request.Request(zip_url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            zip_data = response.read()
    except Exception as e:
        print(f"Failed to download toolkit: {e}", file=sys.stderr)
        return 1
        
    with tempfile.TemporaryDirectory() as tmpdir:
        zip_path = Path(tmpdir) / "spoke-starter.zip"
        zip_path.write_bytes(zip_data)
        
        extract_dir = Path(tmpdir) / "extracted"
        with zipfile.ZipFile(zip_path, 'r') as z:
            z.extractall(extract_dir)
            
        # 1. Overwrite scripts/wiki_tool.py
        src_script = extract_dir / "scripts" / "wiki_tool.py"
        dst_script = VAULT_ROOT / "scripts" / "wiki_tool.py"
        if src_script.exists():
            shutil.copy2(src_script, dst_script)
            print("[upgrade-tooling] Updated scripts/wiki_tool.py")
            
        # 2. Overwrite .agents/skills/
        src_skills = extract_dir / ".agents" / "skills"
        dst_skills = VAULT_ROOT / ".agents" / "skills"
        if src_skills.exists():
            dst_skills.mkdir(parents=True, exist_ok=True)
            # Copy all skills from src to dst, overwriting existing
            for item in src_skills.iterdir():
                if item.is_dir():
                    dst_item = dst_skills / item.name
                    if dst_item.exists():
                        shutil.rmtree(dst_item)
                    shutil.copytree(item, dst_item)
            print("[upgrade-tooling] Updated .agents/skills/")
            
    print("[upgrade-tooling] Upgrade complete!")
    return 0

# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------
def main() -> int:
    parser = argparse.ArgumentParser(
        prog="wiki_tool.py",
        description="Deterministic engine for the CoreBrain LLM Wiki Vault.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # build
    subparsers.add_parser("build", help="Scan Wiki/ and regenerate catalog.jsonl")

    # lint
    subparsers.add_parser("lint", help="Validate all Wiki/ .md files")

    # search-catalog
    sp_search = subparsers.add_parser("search-catalog", help="Search catalog.jsonl")
    sp_search.add_argument("--query", required=True, help="Search query string")

    # list-unprocessed
    subparsers.add_parser("list-unprocessed", help="List files in Raw/Sources that are not cited in any Wiki note")

    # log
    sp_log = subparsers.add_parser("log", help="Append an entry to Wiki/log.md")
    sp_log.add_argument("--action", required=True, help="Short action title")
    sp_log.add_argument("--details", default="", help="Additional details")

    # build-site
    sp_build_site = subparsers.add_parser("build-site", help="Compile Wiki/ into static HTML in site/")
    sp_build_site.add_argument("--url", required=True, help="The GitHub Pages URL where the hub is hosted")

    # refresh-hub
    subparsers.add_parser("refresh-hub", help="Download the latest catalog from the Hub (Spokes only)")

    # search-hub
    sp_search_hub = subparsers.add_parser("search-hub", help="Search the Hub's catalog.jsonl (Spokes only)")
    sp_search_hub.add_argument("--query", required=True, help="Search query string")

    # upgrade-tooling
    subparsers.add_parser("upgrade-tooling", help="Download the latest scripts and skills from the Hub (Spokes only)")

    args = parser.parse_args()

    dispatch = {
        "build": cmd_build,
        "lint": cmd_lint,
        "search-catalog": cmd_search_catalog,
        "list-unprocessed": cmd_list_unprocessed,
        "log": cmd_log,
        "build-site": cmd_build_site,
        "refresh-hub": cmd_refresh_hub,
        "search-hub": cmd_search_hub,
        "upgrade-tooling": cmd_upgrade_tooling,
    }
    return dispatch[args.command](args)


if __name__ == "__main__":
    sys.exit(main())

