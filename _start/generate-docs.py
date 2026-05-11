"""Generate ``docs/start/index.html`` from the template in
``_start/_templates/index.html`` and the config in
``_start/_config/apps.json``.

Usage:
    python3 _start/generate-docs.py

The template uses three ``${placeholder}`` substitutions:

- ``${domain_name}``        — taken from ``config.domainName`` (apps.json).
- ``${domain_description}`` — taken from ``config.domainDescription``.
- ``${apps}``               — the full apps.json content, embedded as JSON
                              so the page's inline JavaScript can read it.

Icon assets under ``_start/_templates/icons/`` are mirrored into
``docs/start/icons/`` so the template's ``icons/logo.png`` reference
resolves at runtime.

Standard-library only — matches the rest of the build tooling.
"""

from __future__ import annotations

import json
import shutil
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
START_DIR = REPO_ROOT / "_start"
TEMPLATE_FILE = START_DIR / "_templates" / "index.html"
TEMPLATE_ICONS_DIR = START_DIR / "_templates" / "icons"
CONFIG_FILE = START_DIR / "_config" / "apps.json"
OUT_DIR = REPO_ROOT / "docs" / "start"


def _copy_icons(src: Path, dst: Path) -> None:
    """Mirror ``src`` into ``dst`` if ``src`` exists. Files are overwritten
    so re-runs pick up template changes."""
    if not src.is_dir():
        return
    dst.mkdir(parents=True, exist_ok=True)
    for entry in src.iterdir():
        target = dst / entry.name
        if entry.is_dir():
            if target.exists():
                shutil.rmtree(target)
            shutil.copytree(entry, target)
        else:
            shutil.copy2(entry, target)


def main() -> int:
    if not TEMPLATE_FILE.is_file():
        raise SystemExit(f"error: missing template at {TEMPLATE_FILE}")
    if not CONFIG_FILE.is_file():
        raise SystemExit(f"error: missing config at {CONFIG_FILE}")

    template = TEMPLATE_FILE.read_text(encoding="utf-8")
    config_text = CONFIG_FILE.read_text(encoding="utf-8")
    config_data = json.loads(config_text)

    cfg = config_data.get("config") or {}
    domain_name = cfg.get("domainName", "")
    domain_description = cfg.get("domainDescription", "")

    # The whole apps.json is embedded verbatim — the template's inline JS does
    # `const apps = ${apps}.apps` and `const config = ${apps}.config`.
    apps_json = json.dumps(config_data, ensure_ascii=False)

    html = (
        template
        .replace("${domain_name}", domain_name)
        .replace("${domain_description}", domain_description)
        .replace("${apps}", apps_json)
    )

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "index.html").write_text(html, encoding="utf-8")
    _copy_icons(TEMPLATE_ICONS_DIR, OUT_DIR / "icons")

    rel_out = (OUT_DIR / "index.html").relative_to(REPO_ROOT)
    print(f"[built] _start -> {rel_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
