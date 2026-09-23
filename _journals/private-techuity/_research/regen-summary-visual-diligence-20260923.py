#!/usr/bin/env python3
"""Regenerate the TL;DR overview figure of 23-diligence-corrects-the-plan (legacy keys).

The prompt archive keys this post as `16-diligence-and-thesis` and its assets live under
`21-diligence-corrects-the-plan/`, so `generate_summary_visuals.py --post <slug>` cannot
select it. This drives the illustrator helper directly for this one figure.

In-depth review round 2, finding DCP-002: the funded-action checklist carried unexplained
management jargon (EXECUTION, RESOURCE ALLOCATION, MILESTONE TRACKING), a "$" coin and
stray microtext. Replace them with plain labels and no currency symbol.
Writes to a candidate path; `--accept` installs the candidate and updates the archive.
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
LEGACY_KEY = '16-diligence-and-thesis'
ASSET = J / 'posts/23-diligence-corrects-the-plan/assets/images/21-diligence-corrects-the-plan/summary-at-a-glance.jpeg'
CANDIDATE = Path('/tmp/diligence-summary-candidate.jpeg')

BASE = ('Create one finished summary illustration explaining the whole post in Owned, a book for product and '
        'engineering leaders working with investors. Landscape 16:9. Calm editorial concept map with concrete '
        'drawn objects, navy ink, warm ivory background, muted teal and ochre. Use generous empty space, a clear '
        'left-to-right reading order and large high-contrast labels. Use only the labels explicitly requested; no '
        'decorative title, paragraph text, figure number, watermark, photorealism or 3D gradients. Do not invent '
        'numbers, dates, research findings or financial claims. \n\n')

SCENE = (
    'Four stations from left to right joined by one thin connecting line. '
    '(1) A stack of plain document pages labelled THESIS. '
    '(2) A large magnifying glass over plain unlettered papers and small unlabelled chart shapes, labelled EVIDENCE. '
    '(3) An open notebook labelled RECORDED RESPONSE; its right page shows three empty tick boxes, one under the other, '
    'with the words PROCEED, CHANGE and DECLINE, none of them ticked; its left page has plain ruled lines only. '
    '(4) A clipboard labelled FUNDED ACTION with two tabs at its top labelled ACCOUNTABLE LEADER (a simple person icon) '
    'and BUDGET (a plain stack of coins with no currency symbol); below them a short checklist of exactly three lines '
    'reading DO THE WORK, ASSIGN PEOPLE AND MONEY and CHECK PROGRESS. '
    'One small ochre sticky note labelled LIMITS is attached at station 2 and travels with the work: an identical '
    'LIMITS note is clipped to the notebook and to the clipboard. '
    'No approval stamp, no certificate, no dollar, euro or other currency sign anywhere.\n\n'
    'TEXT: draw exactly these labels and nothing else — THESIS, EVIDENCE, RECORDED RESPONSE, FUNDED ACTION, LIMITS '
    '(three times), PROCEED, CHANGE, DECLINE, ACCOUNTABLE LEADER, BUDGET, DO THE WORK, ASSIGN PEOPLE AND MONEY, '
    'CHECK PROGRESS. Make every label large and bold enough to read on a phone: the notebook choices, the two clipboard tabs and the three checklist lines must each be at least HALF the height of the station headings, so draw the notebook and the clipboard large (together they may fill half the width) and keep the thesis pages and magnifying glass compact. Papers, charts and ruled lines carry '
    'no words, letters or numbers. Any other text is a defect.'
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
    (backups / f'23-diligence-corrects-the-plan-summary-at-a-glance-{hashlib.sha256(previous).hexdigest()[:12]}.jpeg').write_bytes(previous)
    ASSET.write_bytes(data)
    digest = hashlib.sha256(data).hexdigest()
    archive = json.loads(ARCHIVE.read_text())
    for fig in archive['figures']:
        if fig.get('post') == LEGACY_KEY and fig.get('id') == 'summary-at-a-glance':
            fig['previous_prompt'] = fig['prompt']
            fig['prompt'] = BASE + SCENE
            fig['sha256'] = digest
            fig['visual_review'] = note
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
