#!/usr/bin/env python3
"""Validate that all agent and skill paths in .github/plugin.json exist."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    manifest = repo_root / ".github" / "plugin.json"
    marketplace = repo_root / ".github" / "plugin" / "marketplace.json"

    if not manifest.exists():
        print(f"ERROR: Manifest not found at {manifest}")
        return 1

    try:
        data = json.loads(manifest.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"ERROR: Invalid JSON in {manifest}: {exc}")
        return 1

    failures: list[str] = []

    # Check marketplace.json exists and is valid
    if not marketplace.exists():
        failures.append(f"Missing marketplace metadata: {marketplace.relative_to(repo_root)}")
    else:
        try:
            json.loads(marketplace.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            failures.append(f"Invalid JSON in {marketplace.relative_to(repo_root)}: {exc}")

    for rel in data.get("agents", []):
        path = manifest.parent / rel
        if not path.exists():
            failures.append(f"Missing agent file: {rel}")

    for rel in data.get("skills", []):
        skill_dir = manifest.parent / rel
        skill_md = skill_dir / "SKILL.md"
        if not skill_dir.exists():
            failures.append(f"Missing skill directory: {rel}")
        elif not skill_md.exists():
            failures.append(f"Missing SKILL.md in: {rel}")

    if failures:
        print("Plugin validation failed:")
        for item in failures:
            print(f"- {item}")
        return 1

    agent_count = len(data.get("agents", []))
    skill_count = len(data.get("skills", []))
    print(f"Plugin validation passed: {agent_count} agents, {skill_count} skills, marketplace metadata OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
