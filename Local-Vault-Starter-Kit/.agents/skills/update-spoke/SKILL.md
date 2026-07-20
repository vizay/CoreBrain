---
name: update-spoke
description: "Sync the local spoke with the CoreBrain hub, upgrade core tooling, and verify local knowledge alignment."
---

# update-spoke

Use this skill when the user asks to update the spoke, sync with CoreBrain, or pull the latest global rules.

## Protocol

1. **Upgrade Core Tooling:**
   Run the upgrade command to ensure the local engine (`wiki_tool.py`) and global rules (`AGENTS.md`) are up-to-date with the hub. This command preserves local custom rules in `LOCAL-AGENTS.md`.
   ```bash
   python scripts/wiki_tool.py upgrade-tooling
   ```

2. **Refresh the Hub Catalog Cache:**
   Run the refresh command to fetch the latest CoreBrain catalog JSON.
   ```bash
   python scripts/wiki_tool.py refresh-hub
   ```

3. **Audit Local Core References:**
   Scan the local `Wiki/` directory for any `[[Core: Concept Name]]` wikilinks. 
   Cross-reference those links against the newly downloaded `Schema/hub-cache/catalog.json`.
   - If any `[[Core: Concept Name]]` links are broken (e.g., the concept was renamed or deprecated in the hub), you must update the local markdown files to point to the new correct concept or remove the link.
   - If the Hub summary for a concept has significantly changed, review the local notes relying on that concept to ensure they are still architecturally sound.

4. **Lint and Commit:**
   If you made any changes to the local Wiki during the audit, run `python scripts/wiki_tool.py lint` and commit the fixes.

5. **Report Status:**
   Inform the user that the Spoke tooling and catalog are now fully synchronized with the CoreBrain, and summarize any local changes you had to make to maintain alignment.
