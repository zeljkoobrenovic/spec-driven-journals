#!/usr/bin/env python3
"""Regenerate the TL;DR (summary) overview figure of an Owned chapter — 28 Sept 2026 summary rewrite.

The summaries were rewritten as fluent, conversational reads of the key points and one worked
example; their overview figures are redrawn with more detail, so a reader can grasp the chapter's
key concepts from the picture alone.

Each post's prompt lives in `_research/summary-rewrite-20260928/<post-folder>.json`:

    {"asset": "assets/images/<folder>/summary-at-a-glance.jpeg",   # relative to the post folder
     "scene": "...scene description and the exact TEXT list...",
     "alt": "...", "caption": "...", "aspect_ratio": "16:9"}

Usage:
    python3 regen-summary-visuals-20260928.py generate <post-folder> [--out <candidate.jpeg>]
    python3 regen-summary-visuals-20260928.py accept <post-folder> <candidate.jpeg> "<review note>"

`generate` writes a candidate (default: the session scratchpad or /tmp). `accept` installs it,
archives any previous image under `_research/discarded-summary-variants/` and updates (or appends)
the entry in `summary-visual-prompts-20260913.json` under a file lock, so parallel runs are safe.
"""
from __future__ import annotations

import fcntl
import hashlib
import importlib.util
import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[3]
J = ROOT / '_journals/private-techuity'
HELPER = ROOT / '.claude/skills/article-illustrator/scripts/generate_illustrations_nanobanana.py'
sys.path.insert(0, str(HELPER.parent))
_spec = importlib.util.spec_from_file_location('owned_illustration_helpers', HELPER)
helper = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = helper
_spec.loader.exec_module(helper)

MODEL = 'gemini-3-pro-image-preview'
ARCHIVE = J / '_research/summary-visual-prompts-20260913.json'
PROMPTS = J / '_research/summary-rewrite-20260928'
LOCK = J / '_research/.summary-visual-archive.lock'
DATE = '2026-09-28'

BASE = ('Create one finished summary illustration explaining the whole chapter in Owned, a book for product and '
        'engineering leaders working with investors. Calm, detailed editorial infographic with concrete drawn '
        'objects: navy ink line work, warm ivory background, muted teal and ochre used only in shapes, arrows and '
        'accents. The picture must let a reader grasp the chapter\'s key concepts on its own: show the structure '
        '(steps, contrasts, flows or options) clearly, with a strong left-to-right or top-to-bottom reading order '
        'and generous spacing between groups. All lettering is dark navy, bold, sans-serif, large and '
        'high-contrast, legible on a phone. Use only the labels explicitly requested, each exactly once and '
        'spelled exactly as given; no title, paragraph text, figure number, watermark, logos, photorealism or 3D '
        'gradients. Do not invent numbers, dates, names or claims beyond the requested labels.\n\n')


def load(post: str) -> dict:
    return json.loads((PROMPTS / f'{post}.json').read_text())


def call_image(prompt: str, aspect: str, key: str) -> tuple[bytes, str]:
    endpoint = ('https://generativelanguage.googleapis.com/v1beta/models/'
                + urllib.parse.quote(MODEL, safe='') + ':generateContent')
    payload = {'contents': [{'role': 'user', 'parts': [{'text': prompt}]}],
               'generationConfig': {'responseModalities': ['IMAGE'],
                                    'imageConfig': {'aspectRatio': aspect, 'imageSize': '2K'}}}
    request = urllib.request.Request(
        endpoint, data=json.dumps(payload).encode(),
        headers={'Content-Type': 'application/json', 'x-goog-api-key': key}, method='POST')
    with urllib.request.urlopen(request, timeout=300) as response:
        return helper.extract_image_bytes(json.loads(response.read().decode()))


def generate(post: str, out: Path) -> None:
    key = os.environ.get('GEMINI_API_KEY') or os.environ.get('GOOGLE_API_KEY')
    assert key, 'Set GEMINI_API_KEY before generating artwork.'
    cfg = load(post)
    asset = J / 'posts' / post / cfg['asset']
    data, mime = call_image(BASE + cfg['scene'], cfg.get('aspect_ratio', '16:9'), key)
    data, _, _ = helper.normalize_image_bytes_for_target(data, mime, asset)
    assert helper.detect_image_mime(data) == 'image/jpeg'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(data)
    print('candidate', out, hashlib.sha256(data).hexdigest()[:16])


def accept(post: str, candidate: Path, note: str) -> None:
    cfg = load(post)
    asset = J / 'posts' / post / cfg['asset']
    data = candidate.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    rel_asset = f'posts/{post}/{cfg["asset"]}'
    with open(LOCK, 'w') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        if asset.exists():
            previous = asset.read_bytes()
            backups = J / '_research/discarded-summary-variants'
            backups.mkdir(exist_ok=True)
            (backups / f'{post}-summary-{hashlib.sha256(previous).hexdigest()[:12]}.jpeg').write_bytes(previous)
        asset.parent.mkdir(parents=True, exist_ok=True)
        asset.write_bytes(data)
        archive = json.loads(ARCHIVE.read_text())
        tail = cfg['asset'].split('assets/images/', 1)[-1]
        entry = None
        for fig in archive['figures']:
            paths = [fig.get('current_asset', ''), fig.get('asset', '')]
            if fig.get('post') == post or any(p.endswith(tail) for p in paths if p):
                entry = fig
                break
        if entry is None:
            entry = {'post': post, 'figure': 1, 'id': 'summary-at-a-glance', 'status': 'generated',
                     'asset': cfg['asset'], 'aspect_ratio': cfg.get('aspect_ratio', '16:9'),
                     'placement': 'after the opening paragraph of the TL;DR modality'}
            archive['figures'].append(entry)
        elif 'prompt' in entry:
            entry.setdefault('revisions', []).append({
                'date': DATE, 'reason': 'summary rewrite: more detailed overview. ' + note,
                'previous_prompt': entry['prompt'], 'previous_sha256': entry.get('sha256')})
        entry.update({'prompt': BASE + cfg['scene'], 'sha256': digest, 'alt': cfg['alt'],
                      'caption': cfg['caption'], 'current_asset': rel_asset,
                      'visual_review': f'accepted {DATE} after direct inspection: {note}'})
        ARCHIVE.write_text(json.dumps(archive, ensure_ascii=False, indent=2) + '\n')
    print('installed', asset.relative_to(ROOT), digest[:16])


if __name__ == '__main__':
    cmd, post = sys.argv[1], sys.argv[2]
    if cmd == 'generate':
        default = Path(os.environ.get('TMPDIR', '/tmp')) / f'summary-candidate-{post}.jpeg'
        out = Path(sys.argv[sys.argv.index('--out') + 1]) if '--out' in sys.argv else default
        generate(post, out)
    elif cmd == 'accept':
        accept(post, Path(sys.argv[3]), sys.argv[4])
    else:
        raise SystemExit(__doc__)
