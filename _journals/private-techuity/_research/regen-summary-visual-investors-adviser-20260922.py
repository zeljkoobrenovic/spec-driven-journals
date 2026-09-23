#!/usr/bin/env python3
"""Regenerate the TL;DR overview figure of 21-investors-adviser (legacy keys).

The prompt archive keys this post as `15-technology-principal` and its assets live
under `18-investors-adviser/`, so `generate_summary_visuals.py --post <slug>` cannot
select it. This drives the illustrator helper directly for this one figure.

Review finding IA-011: the PURPOSE / AUTHORITY / CAPACITY tabs and other small labels
are unreadable at 360px. Enlarge the essential labels and drop decorative microtext.
"""
from __future__ import annotations
import base64, hashlib, importlib.util, json, os, sys, urllib.request, urllib.parse
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path('/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals')
J = ROOT / '_journals/private-techuity'
HELPER = ROOT / '.codex/skills/article-illustrator/scripts/generate_illustrations_nanobanana.py'

sys.path.insert(0, str(HELPER.parent))
spec = importlib.util.spec_from_file_location('owned_illustration_helpers', HELPER)
helper = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = helper
spec.loader.exec_module(helper)

MODEL = 'gemini-3-pro-image-preview'
ARCHIVE = J / '_research/summary-visual-prompts-20260913.json'
LEGACY_KEY = '15-technology-principal'
ASSET = J / 'posts/21-investors-adviser/assets/images/18-investors-adviser/summary-at-a-glance.jpeg'

BASE = ('Create one finished summary illustration explaining the whole post in Owned, a book for product and '
        'engineering leaders working with investors. Landscape 16:9. Calm editorial concept map with concrete '
        'drawn objects, navy ink, warm ivory background, muted teal and ochre. Use generous empty space, a clear '
        'reading order and large high-contrast labels. Use only the labels explicitly requested; no decorative '
        'title, paragraph text, figure number, watermark, photorealism or 3D gradients. Do not invent numbers, '
        'dates, research findings or financial claims. \n\n')

SCENE = (
    'Two workspaces separated by a clear but permeable boundary. Left, an adviser’s evidence notebook labeled '
    'ADVISER. Right, a company operating plan with accountable hands on the plan labeled COMPANY LEADER. '
    'Between them sits one large explicit agreement card divided into exactly THREE side-by-side sections, whose only '
    'headings are the single words PURPOSE, AUTHORITY and CAPACITY, each written ONCE. The card has no tab strip, no '
    'second row of headings and no title bar above those three words. '
    'Below, both contribute through dotted lines to a decision record and a maintained service labeled '
    'SUSTAINABLE RESULT. Do not draw the adviser as the leader\'s boss or imply a universal technology-principal role.\n\n'
    'TEXT SIZE IS CRITICAL: draw exactly these six labels — ADVISER, COMPANY LEADER, PURPOSE, AUTHORITY, CAPACITY '
    'and SUSTAINABLE RESULT — in VERY LARGE bold capitals that stay clearly readable when the whole picture is '
    'displayed only 360 pixels wide on a phone. Make the three agreement tabs big enough to carry their words at '
    'that size; widen the card as needed. Write NO other text anywhere: the notebook, the operating plan and the '
    'decision record carry plain unlettered ruled lines and simple icons only, with no headings, no captions, '
    'no small annotations and no scribbled words. In particular the company operating plan on the right must contain NO words at all: its charts, timeline and org symbols are drawn with plain unlabelled shapes, bars, dots and lines. Any text smaller than the six named labels is a defect. Count the words in the finished image: there must be exactly six labels and nothing else.'
)


def call_image(prompt: str, key: str):
    endpoint = ('https://generativelanguage.googleapis.com/v1beta/models/'
                + urllib.parse.quote(MODEL, safe='') + ':generateContent')
    payload = {'contents': [{'role': 'user', 'parts': [{'text': prompt}]}],
               'generationConfig': {'responseModalities': ['IMAGE'], 'imageConfig': {'aspectRatio': '16:9'}}}
    request = urllib.request.Request(
        endpoint, data=json.dumps(payload).encode(),
        headers={'Content-Type': 'application/json', 'x-goog-api-key': key}, method='POST')
    with urllib.request.urlopen(request, timeout=300) as response:
        return helper.extract_image_bytes(json.loads(response.read().decode()))


def main() -> int:
    key = os.environ.get('GEMINI_API_KEY') or os.environ.get('GOOGLE_API_KEY')
    assert key, 'Set GEMINI_API_KEY before generating artwork.'
    prompt = BASE + SCENE
    print('--- prompt ---\n' + prompt + '\n--------------', flush=True)

    data, mime = call_image(prompt, key)
    data, _, _ = helper.normalize_image_bytes_for_target(data, mime, ASSET)
    assert helper.detect_image_mime(data) == 'image/jpeg'

    previous = ASSET.read_bytes()
    backups = J / '_research/discarded-summary-variants'
    backups.mkdir(exist_ok=True)
    (backups / f'21-investors-adviser-summary-at-a-glance-{hashlib.sha256(previous).hexdigest()[:12]}.jpeg').write_bytes(previous)
    ASSET.write_bytes(data)
    digest = hashlib.sha256(data).hexdigest()
    print('written', ASSET, digest[:16])

    archive = json.loads(ARCHIVE.read_text())
    for fig in archive['figures']:
        if fig.get('post') == LEGACY_KEY and fig.get('id') == 'summary-at-a-glance':
            fig['previous_prompt'] = fig['prompt']
            fig['prompt'] = prompt
            fig['sha256'] = digest
            fig['visual_review'] = 'regenerated 2026-09-22 (IA-011): essential labels enlarged for phone width, decorative microtext removed'
            break
    ARCHIVE.write_text(json.dumps(archive, ensure_ascii=False, indent=2) + '\n')
    print('archive entry updated under legacy key', LEGACY_KEY)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
