#!/usr/bin/env python3
"""Relabel one lettered string on a Gemini article figure of 18a-learn-through-investors-network.

In-depth review round 1, 23 September 2026 (INVNET-004): the third scene of
Figure 3 (`bring-the-question-home.jpeg`) read "Our records vary", which
misattributes the uneven stock records to Northline itself; the article says
the records of Northline's customers vary. The scene is relettered
"Customers’ records vary". Uses the same image-edit prompt and Gemini call as
the explainer-comics skill's `--retext`; the replaced image is archived under
`_research/discarded-illustration-variants/`.

Usage: python3 retext-figure-investor-learning-20260923.py bring-the-question-home "OLD WORDS" "NEW WORDS"
"""
from __future__ import annotations
import hashlib, importlib.util, os, sys
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[3]
J = ROOT / '_journals/private-techuity'
SCRIPT = ROOT / '.claude/skills/explainer-comics/scripts/generate_comic_pages.py'
sys.path.insert(0, str(SCRIPT.parent))
spec = importlib.util.spec_from_file_location('generate_comic_pages', SCRIPT)
pages = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pages)

MODEL = 'gemini-3-pro-image-preview'
POST = J / 'posts/18a-learn-through-investors-network'
IMAGES = POST / 'assets/images/18a-learn-through-investors-network'


def main() -> int:
    figure, old, new = sys.argv[1:4]
    key = os.environ.get('GEMINI_API_KEY', '').strip()
    assert key, 'Set GEMINI_API_KEY.'
    asset = IMAGES / f'{figure}.jpeg'
    prompt = (
        'Edit the attached illustration. Change ONLY one piece of lettering: replace the exact words '
        f'"{old}" with the exact words "{new}", in the same place, same lettering style, colour and size, '
        'on two lines if needed. Keep every other pixel of the illustration as it is: the same four scenes, '
        'people, faces, colours, dividers, arrows, headings and all other text. Add nothing else.'
    )
    previous = asset.read_bytes()
    data, mime = pages.call_image(key, MODEL, prompt, '16:9', previous)
    data, _, _ = pages.panels.normalize_image_bytes_for_target(data, mime, asset)
    backups = J / '_research/discarded-illustration-variants'
    backups.mkdir(exist_ok=True)
    (backups / f'18a-learn-through-investors-network-{figure}-{hashlib.sha256(previous).hexdigest()[:12]}.jpeg').write_bytes(previous)
    asset.write_bytes(data)
    print('retexted', asset.relative_to(ROOT), hashlib.sha256(data).hexdigest(), len(data), 'bytes')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
