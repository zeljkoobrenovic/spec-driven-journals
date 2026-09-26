#!/usr/bin/env python3
"""Relabel one lettered string on a legacy comic panel of 21-the-financing-slipped.

In-depth review round 2, 23 September 2026 (FIN-002): panel 6 showed an
unexplained "SUPPORT AGREEMENT" that has no role in the story. The document is
relabelled "CUSTOMER CONTRACT" (same length), one of the protected obligations
the chapter establishes. Uses the same image-edit prompt and Gemini call as the
explainer-comics skill's `--retext` (which only accepts `comic-page` blocks);
the replaced image is archived under `_research/discarded-comic-variants/`.

Usage: python3 retext-panel-financing-slipped-20260923.py 06-scene "OLD WORDS" "NEW WORDS"
"""
from __future__ import annotations
import hashlib, importlib.util, json, os, re, sys
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path('/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals')
J = ROOT / '_journals/private-techuity'
SCRIPT = ROOT / '.claude/skills/explainer-comics/scripts/generate_comic_pages.py'
sys.path.insert(0, str(SCRIPT.parent))
spec = importlib.util.spec_from_file_location('generate_comic_pages', SCRIPT)
pages = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pages)

MODEL = 'gemini-3-pro-image-preview'
POST = J / 'posts/21-the-financing-slipped'
COMICS = POST / 'comics.md'
PANEL_RE = re.compile(r'<!-- comic-panel\s+(\{.*?\})\s*-->', re.S)


def main() -> int:
    panel_id, old, new = sys.argv[1:4]
    key = os.environ.get('GEMINI_API_KEY', '').strip()
    assert key, 'Set GEMINI_API_KEY.'
    items = {json.loads(m)['id']: json.loads(m) for m in PANEL_RE.findall(COMICS.read_text())}
    item = items[panel_id]
    assert new in item['prompt'], 'put the new words into the panel prompt first'
    asset = POST / item['asset']
    prompt = (
        'Edit the attached comic panel. Change ONLY one piece of lettering: replace the exact words '
        f'"{old}" with the exact words "{new}", in the same place, same lettering style and size. '
        'Keep every other pixel of the panel as it is: the same drawings, people, faces, colors, border, '
        'speech bubble, labels and all other text. Add nothing else.'
    )
    data, mime = pages.call_image(key, MODEL, prompt, item.get('aspect_ratio', '16:9'), asset.read_bytes())
    data, _, _ = pages.panels.normalize_image_bytes_for_target(data, mime, asset)
    previous = asset.read_bytes()
    backups = J / '_research/discarded-comic-variants'
    backups.mkdir(exist_ok=True)
    (backups / f'21-the-financing-slipped-comic-{panel_id}-{hashlib.sha256(previous).hexdigest()[:12]}.jpeg').write_bytes(previous)
    asset.write_bytes(data)
    print('retexted', asset.relative_to(ROOT), hashlib.sha256(data).hexdigest())
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
