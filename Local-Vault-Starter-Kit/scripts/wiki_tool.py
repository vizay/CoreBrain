#!/usr/bin/env python3
"""
wiki_tool.py — Deterministic engine for the CoreBrain LLM Wiki Vault.

Commands:
  build           Scan Wiki/ and regenerate Wiki/catalog.jsonl
  lint            Validate all Wiki/ .md files (frontmatter, tags, sources, Core refs)
  search-catalog  Search catalog.jsonl with --query
  log             Append a timestamped entry to Wiki/log.md

Usage:
  python scripts/wiki_tool.py build
  python scripts/wiki_tool.py lint
  python scripts/wiki_tool.py search-catalog --query "transformer"
  python scripts/wiki_tool.py log --action "Ingested GPT-4 paper" --details "Added 3 wiki notes"

Dependencies: Python 3.8+ standard library only (os, json, argparse, re, pathlib, datetime).
"""

import os
import json
import argparse
import re
import sys
from pathlib import Path
from datetime import datetime, timezone

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
        if line.startswith("  - ") or line.startswith("- "):
            item = line.strip().lstrip("- ").strip().strip('"').strip("'")
            if current_key is not None:
                if not isinstance(result.get(current_key), list):
                    result[current_key] = []
                result[current_key].append(item)
            continue
        # Key: value
        if ":" in line:
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            current_key = key
            list_mode = value == ""
            if not list_mode:
                result[key] = value
            else:
                result[key] = []
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
    skipped = []
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
    if skipped:
        for s in skipped:
            print(f"  [skip] {s}")
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
        if catalog_titles or catalog_stems:
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
# Command: refresh-hub
# ---------------------------------------------------------------------------
def cmd_refresh_hub(args) -> int:
    """Download catalog.json from the CoreBrain static site into the local hub cache."""
    import urllib.request
    import urllib.error
    
    HUB_CONFIG_FILE = VAULT_ROOT / "Schema" / "hub-config.json"
    HUB_CACHE_DIR = VAULT_ROOT / "Schema" / "hub-cache"
    
    if not HUB_CONFIG_FILE.exists():
        print(f"[refresh-hub] Error: {HUB_CONFIG_FILE.relative_to(VAULT_ROOT)} not found.", file=sys.stderr)
        return 1
        
    try:
        config = json.loads(HUB_CONFIG_FILE.read_text(encoding="utf-8"))
        hub_url = config.get("hub_pages_url")
        if not hub_url:
            print("[refresh-hub] Error: 'hub_pages_url' missing in hub-config.json.", file=sys.stderr)
            return 1
    except Exception as e:
        print(f"[refresh-hub] Error reading hub-config.json: {e}", file=sys.stderr)
        return 1

    catalog_url = hub_url.rstrip("/") + "/catalog.json"
    print(f"[refresh-hub] Fetching from {catalog_url} ...")
    
    try:
        req = urllib.request.Request(catalog_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
    except Exception as e:
        print(f"[refresh-hub] Failed to download catalog: {e}", file=sys.stderr)
        return 1
        
    HUB_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_file = HUB_CACHE_DIR / "catalog.json"
    
    with cache_file.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print(f"[refresh-hub] Successfully cached {len(data)} CoreBrain notes to {cache_file.relative_to(VAULT_ROOT)}")
    return 0

# ---------------------------------------------------------------------------
# Command: search-hub
# ---------------------------------------------------------------------------
def cmd_search_hub(args) -> int:
    """Search the cached CoreBrain catalog for --query."""
    CACHE_FILE = VAULT_ROOT / "Schema" / "hub-cache" / "catalog.json"
    
    if not CACHE_FILE.exists():
        print("[search-hub] Hub cache not found. Run `refresh-hub` first.", file=sys.stderr)
        return 1
        
    query = args.query.lower()
    tokens = query.split()
    results = []

    try:
        with CACHE_FILE.open(encoding="utf-8") as f:
            catalog = json.load(f)
    except Exception as e:
        print(f"[search-hub] Error reading cache: {e}", file=sys.stderr)
        return 1

    for entry in catalog:
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

    HUB_CONFIG_FILE = VAULT_ROOT / "Schema" / "hub-config.json"
    print(f"[search-hub] {len(results)} result(s) for '{args.query}':\n")
    for rank, (score, entry) in enumerate(results, 1):
        print(f"  [{rank}] Core: {entry.get('title', '(no title)')}")
        print(f"       Summary : {entry.get('summary', '')[:120]}")
        print(f"       Tags    : {', '.join(entry.get('tags', []))}")
        print(f"       URL     : {json.loads(HUB_CONFIG_FILE.read_text(encoding='utf-8')).get('hub_pages_url', '').rstrip('/')}/{entry.get('slug', '')}.html" if HUB_CONFIG_FILE.exists() else "")
        print()
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

    # log
    sp_log = subparsers.add_parser("log", help="Append an entry to Wiki/log.md")
    sp_log.add_argument("--action", required=True, help="Short action title")
    sp_log.add_argument("--details", default="", help="Additional details")

    # refresh-hub
    subparsers.add_parser("refresh-hub", help="Download the latest CoreBrain catalog")

    # search-hub
    sp_search_hub = subparsers.add_parser("search-hub", help="Search the cached CoreBrain catalog")
    sp_search_hub.add_argument("--query", required=True, help="Search query string")

    args = parser.parse_args()

    dispatch = {
        "build": cmd_build,
        "lint": cmd_lint,
        "search-catalog": cmd_search_catalog,
        "log": cmd_log,
        "refresh-hub": cmd_refresh_hub,
        "search-hub": cmd_search_hub,
    }
    return dispatch[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
