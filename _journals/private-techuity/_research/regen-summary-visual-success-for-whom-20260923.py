#!/usr/bin/env python3
"""Regenerate the TL;DR overview figure of 38-success-for-whom (legacy keys).

The prompt archive keys this post as `24-durable-value` and its assets live under
`30-success-for-whom/`, so `generate_summary_visuals.py --post <slug>` cannot select it.
This drives the illustrator helper directly for this one figure.

In-depth review round 2, finding SFW-13: the timeline's last station read AFTER OWNERSHIP,
although ownership continues under the next owner; the investor wallet also showed
dollar-sign coins against the journal's euro-only style, and COMPANY ECONOMICS is plainer
as COMPANY INCOME AND COSTS. Writes to a candidate path; `--accept "<note>"` installs the
candidate, archives the previous image and updates the archive entry.
"""
from __future__ import annotations
import hashlib, importlib.util, json, os, sys, urllib.request, urllib.parse
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
LEGACY_KEY = '24-durable-value'
ASSET = J / 'posts/38-success-for-whom/assets/images/30-success-for-whom/summary-at-a-glance.jpeg'
CANDIDATE = Path('/tmp/success-for-whom-summary-candidate.jpeg')

BASE = ('Create one finished summary illustration explaining the whole post in Owned, a book for product and '
        'engineering leaders working with investors. Landscape 16:9. Calm editorial concept map with concrete '
        'drawn objects, navy ink, warm ivory background, muted teal and ochre. Use generous empty space, a clear '
        'left-to-right reading order and large high-contrast labels legible at article width and on a phone. Use only '
        'the labels explicitly requested; no decorative title, paragraph text, figure number, watermark, photorealism '
        'or 3D gradients. Do not invent numbers, dates, research findings or financial claims. \n\n')

SCENE = (
    'In the centre, a simple company building with an open arched doorway, the building labelled COMPANY and the '
    'doorway labelled OWNERSHIP-CHANGE DOORWAY below it. A single thin path runs out of the doorway to the right and '
    'continues past the building edge. Around the building, five equal round inspection windows, each with one object '
    'and one label beneath it: top left, a plain closed wallet with two plain round coins beside it, labelled '
    'INVESTOR RESULT; top right, an open ledger book with ruled lines only and a pen, labelled COMPANY INCOME AND COSTS; '
    'bottom left, a wrench, a gear and a screwdriver, labelled OPERATING CAPABILITY; bottom right, two standing '
    'people, one with a briefcase and one with a shopping bag, labelled PEOPLE AFFECTED; far right, at the end of the '
    'path, a wall calendar with blank ruled cells and a small forward arrow on it, labelled AFTER THE OWNERSHIP CHANGE. '
    'Thin connector lines join each window to the building. No combined score, trophy, green check marks, currency '
    'signs or invented evidence. Equal window sizes indicate separate questions, not equal numerical weighting.\n\n'
    'TEXT: draw exactly these seven labels, each once and nothing else: COMPANY, OWNERSHIP-CHANGE DOORWAY, '
    'INVESTOR RESULT, COMPANY INCOME AND COSTS, OPERATING CAPABILITY, PEOPLE AFFECTED, AFTER THE OWNERSHIP CHANGE. '
    'The coins, ledger, calendar and people carry no words, letters, numbers or currency symbols: no dollar sign, no '
    'euro sign, no pound sign anywhere. Any other text is a defect.'
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


def generate() -> None:
    key = os.environ.get('GEMINI_API_KEY') or os.environ.get('GOOGLE_API_KEY')
    assert key, 'Set GEMINI_API_KEY before generating artwork.'
    data, mime = call_image(BASE + SCENE, key)
    data, _, _ = helper.normalize_image_bytes_for_target(data, mime, ASSET)
    assert helper.detect_image_mime(data) == 'image/jpeg'
    CANDIDATE.write_bytes(data)
    print('candidate', CANDIDATE, hashlib.sha256(data).hexdigest()[:16])


def accept(note: str) -> None:
    data = CANDIDATE.read_bytes()
    previous = ASSET.read_bytes()
    backups = J / '_research/discarded-summary-variants'
    backups.mkdir(exist_ok=True)
    (backups / f'38-success-for-whom-summary-at-a-glance-{hashlib.sha256(previous).hexdigest()[:12]}.jpeg').write_bytes(previous)
    ASSET.write_bytes(data)
    digest = hashlib.sha256(data).hexdigest()
    archive = json.loads(ARCHIVE.read_text())
    for fig in archive['figures']:
        if fig.get('post') == LEGACY_KEY and fig.get('id') == 'summary-at-a-glance':
            fig.setdefault('revisions', []).append({
                'date': '2026-09-23',
                'reason': note,
                'previous_prompt': fig['prompt'],
                'previous_sha256': fig['sha256'],
            })
            fig['prompt'] = BASE + SCENE
            fig['sha256'] = digest
            fig['alt'] = ('Five circles around a company building with an open doorway: investor result, company income '
                          'and costs, operating capability, people affected and, along an arrow to a calendar, after the '
                          'ownership change.')
            fig['visual_review'] = 'accepted 2026-09-23 after direct inspection: ' + note
            fig['current_asset'] = 'posts/38-success-for-whom/assets/images/30-success-for-whom/summary-at-a-glance.jpeg'
            break
    else:
        raise SystemExit('archive entry not found')
    ARCHIVE.write_text(json.dumps(archive, ensure_ascii=False, indent=2) + '\n')
    print('installed', ASSET, digest[:16])


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--accept':
        accept(sys.argv[2])
    else:
        generate()
