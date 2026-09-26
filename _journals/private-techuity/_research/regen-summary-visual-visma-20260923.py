#!/usr/bin/env python3
"""Regenerate the TL;DR overview figure of 35-visma (archive key and asset folder `27-visma`).

In-depth review round 3, finding VISMA-011: the overview carried the specialist labels
RECONCILIATION (on the open book) and OPERATING DESIGN, plus small thread labels that a
reader of the summary alone could not follow and that were hard to read on a phone.
This version keeps the four main themes and replaces the book's label with plain words;
the small thread labels are dropped. Writes to a candidate path; `--accept "<note>"`
installs the candidate, archives the previous image under
`_research/discarded-summary-variants/` and updates the archive entry.
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
ARCHIVE_KEY = '27-visma'
ASSET = J / 'posts/35-visma/assets/images/27-visma/summary-at-a-glance.jpeg'
CANDIDATE = Path('/tmp/visma-summary-candidate.jpeg')

BASE = ('Create one finished summary illustration explaining the whole post in Owned, a book for product and '
        'engineering leaders working with investors. Landscape 16:9. Calm editorial concept map with concrete '
        'drawn objects, navy ink, warm ivory background, muted teal and ochre. Use generous empty space, a clear '
        'reading order and large high-contrast labels legible at article width and on a phone. Use only '
        'the labels explicitly requested; no decorative title, paragraph text, figure number, watermark, photorealism '
        'or 3D gradients. Do not invent numbers, dates, research findings or financial claims. \n\n')

SCENE = (
    'Two distinct software-product desks, one at the left and one at the right, each with a monitor showing a plain '
    'blank screen, connect through a modest shared-service hub drawn as a small box with two gears between them. '
    'The left desk is labelled LOCAL DECISIONS and the hub is labelled SHARED SUPPORT. Above the desks, two separate '
    'signed share certificates hang from a thin line and are labelled CHANGING OWNERSHIP. Below the desks lies one '
    'open book showing two ruled columns with no numbers, letters or ticks, labelled ONE YEAR, TWO PROFIT FIGURES. '
    'Three thin dotted threads run separately from the certificates, from the desks and from the hub to the book, '
    'with no arrowheads and no growth arrow: ownership changes, the way the work is organized and the way each figure '
    'is calculated must each be examined on its own. No invented acquisitions, company logos, earnings values, '
    'currency signs, uniform central control or claim that shared support caused the valuation.\n\n'
    'TEXT: draw exactly these four labels, each once and nothing else: LOCAL DECISIONS, SHARED SUPPORT, '
    'CHANGING OWNERSHIP, ONE YEAR, TWO PROFIT FIGURES. The screens, certificates and book carry no words, letters, '
    'numbers or currency symbols. Any other text is a defect.'
)

ALT = ('Two software-product desks labelled Local decisions joined by a shared-support hub, two share certificates '
       'above them labelled Changing ownership, and an open book below labelled One year, two profit figures, each '
       'connected by its own dotted thread.')


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
    (backups / f'35-visma-summary-at-a-glance-{hashlib.sha256(previous).hexdigest()[:12]}.jpeg').write_bytes(previous)
    ASSET.write_bytes(data)
    digest = hashlib.sha256(data).hexdigest()
    archive = json.loads(ARCHIVE.read_text())
    for fig in archive['figures']:
        if fig.get('post') == ARCHIVE_KEY and fig.get('id') == 'summary-at-a-glance':
            fig.setdefault('revisions', []).append({
                'date': '2026-09-23',
                'reason': note,
                'previous_prompt': fig['prompt'],
                'previous_sha256': fig['sha256'],
            })
            fig['prompt'] = BASE + SCENE
            fig['sha256'] = digest
            fig['alt'] = ALT
            fig['caption'] = ('Three things to examine separately: who owns the shares after each transaction, how '
                              'local decisions and shared support are organized, and how each of the year’s two '
                              'profit figures was calculated.')
            fig['visual_review'] = 'accepted 2026-09-23 after direct inspection: ' + note
            fig['current_asset'] = 'posts/35-visma/assets/images/27-visma/summary-at-a-glance.jpeg'
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
