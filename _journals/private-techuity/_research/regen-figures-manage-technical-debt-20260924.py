#!/usr/bin/env python3
"""Regenerate two figures of 26-manage-technical-debt after the in-depth review of 24 September 2026 (round 1).

- MTD-006: Figure 2 showed €340,000 and €58,000 as simple price tags. New tags separate staff time from
  additional cash (€300,000 time + €40,000 cash; €50,000 time + €8,000 cash) and add tranche 2's tag
  (€70,000 time + €10,000 cash) so the two-stage programme is visible.
- MTD-017: Figure 3 ranked undated items "by carrying cost" with coin piles only. New bracket
  "Then by cost removed per effort"; each undated card shows a coin stack (cost removed) beside a
  wrench count (effort), with a legend, so a large expensive repair can rank below a small cheap one.

Drives the illustrator helper directly (same pattern as regen-figures-toys-r-us-20260923.py).
`generate <id>` writes a candidate to /tmp; `accept <id> "<note>"` installs it, archives the previous
image under _research/discarded-illustration-variants/ and updates the prompt archive entry.
"""
from __future__ import annotations
import hashlib, importlib.util, json, os, sys, urllib.request, urllib.parse
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[3]
J = ROOT / '_journals/private-techuity'
HELPER = ROOT / '.claude/skills/article-illustrator/scripts/generate_illustrations_nanobanana.py'
sys.path.insert(0, str(HELPER.parent))
spec = importlib.util.spec_from_file_location('owned_illustration_helpers', HELPER)
helper = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = helper
spec.loader.exec_module(helper)

MODEL = 'gemini-3-pro-image-preview'
KEY = '26-manage-technical-debt'
POST = J / 'posts/26-manage-technical-debt'
ARCHIVE = J / '_research/article-illustration-prompts-20260913.json'
DISCARD = J / '_research/discarded-illustration-variants'

STYLE = ('Create one finished explanatory illustration for Owned, a practical book for product and '
         'engineering leaders. Landscape 16:9. Editorial ink-and-color diagram on a warm ivory background '
         '(#faf8f2), navy linework, muted teal for resources and useful progress, warm ochre for conditions '
         'and uncertainty. Use concrete objects and clean flat drawing with very light texture, generous space '
         'and a clear reading order. All labels must be large, high-contrast, correctly spelled and legible at '
         'article width and on a narrow phone screen. Use only the short labels requested below and no other '
         'text. Convey meaning through layout and objects; no dense paragraphs, no figure number, no decorative '
         'headline, no watermark, no logos, no photorealism, no 3D gradients. Do not invent financial values, '
         'dates, research findings or institutional policies.\n\n')

FIGURES = {
    'rewrite-versus-tranches': {
        'asset': POST / 'assets/images/26-manage-technical-debt/rewrite-versus-tranches.jpeg',
        'prompt': STYLE + (
            'Two horizontal timelines stacked one above the other, each running left to right along a thin navy '
            'baseline with small tick marks. Upper timeline, label at its left in large navy: Rewrite. It is one long '
            'unbroken ochre bar reaching the far right, with a single teal flag at the very end labeled Benefit at '
            'month nine, and one ochre price tag hanging from the middle of the bar lettered on two lines: '
            '€300,000 staff time / + €40,000 cash. Lower timeline, label at its left in large navy: Tranches. It is '
            'two shorter teal bars in sequence. The first bar ends at a small navy gate drawn as two posts with a '
            'crossbar, labeled Gate, under a tick labeled Month three, with a teal flag above the gate labeled '
            'Benefit and a teal price tag hanging from the first bar lettered on two lines: €50,000 staff time / '
            '+ €8,000 cash. The second bar starts after that gate and ends at a second identical gate labeled Gate, '
            'under a tick labeled Month seven, with a second teal flag labeled Benefit and a second teal price tag '
            'hanging from the second bar lettered on two lines: €70,000 staff time / + €10,000 cash. The lower '
            'timeline ends at month seven, well short of the upper bar. Price tags are plain rectangles with a '
            'string, large lettering, nothing else drawn on them.\n\n'
            'TEXT: draw exactly these labels and nothing else: Rewrite; Tranches; Benefit at month nine; Gate; Gate; '
            'Month three; Month seven; Benefit; Benefit; €300,000 staff time + €40,000 cash; €50,000 staff time '
            '+ €8,000 cash; €70,000 staff time + €10,000 cash. No other words, no axis numbers, no title. Any other '
            'text is a defect.'),
        'alt': 'Two timelines: a rewrite drawn as one long bar with its only benefit at month nine and a price tag of 300,000 euro of staff time plus 40,000 euro of cash, against a tranche plan drawn as two shorter bars with gates and benefits at month three and month seven, tagged 50,000 euro of staff time plus 8,000 euro of cash for the first tranche and 70,000 euro of staff time plus 10,000 euro of cash for the second.',
        'caption': 'The rewrite carries its whole benefit to month nine: about €300,000 of staff time and €40,000 of additional cash before anything is in hand. The tranche plan puts a measured benefit in hand at month three for about €50,000 of time and €8,000 of cash, and again at month seven for about €70,000 of time and €10,000 of cash, and each gate decides whether the next tranche is funded.',
        'candidate': Path('/tmp/mtd-figure2-candidate.jpeg'),
    },
    'sequencing-rule': {
        'asset': POST / 'assets/images/26-manage-technical-debt/sequencing-rule.jpeg',
        'prompt': STYLE + (
            'A single queue of five simple record cards laid left to right on the ivory background, with a large navy '
            'arrow beneath the whole row pointing right and labeled Order of work. The first two cards each carry a '
            'small ochre calendar icon with a ring binding and nothing else, grouped under one large navy bracket '
            'above them labeled Close dates first. The remaining three cards are grouped under a second navy bracket '
            'above them labeled Then by cost removed per effort. Each of these three cards shows two things side by '
            'side: on its left a stack of teal coins, on its right a small row of navy wrench icons. Third card: a '
            'medium stack of coins and ONE wrench. Fourth card: a tall stack of coins and THREE wrenches. Fifth card: '
            'a short stack of coins and THREE wrenches. In the bottom right corner a small two-line legend: '
            'Coins: cost removed / Wrenches: effort. Cards are plain, with no writing on them.\n\n'
            'TEXT: draw exactly these labels, each once, and nothing else: Close dates first; Then by cost removed per '
            'effort; Order of work; Coins: cost removed; Wrenches: effort. No numbers, no dates, no title, no currency '
            'signs. Any other text is a defect.'),
        'alt': 'Five record cards in a row: the first two carry calendar icons under a bracket labeled Close dates first; the next three each carry a stack of coins for the cost removed beside a row of wrenches for the effort, under a bracket labeled Then by cost removed per effort, with a legend reading coins cost removed, wrenches effort, above an arrow labeled Order of work.',
        'caption': 'The sequencing rule written into the register: items with a close external date go first, in date order; the rest follow in order of the carrying cost each tranche of effort would remove, read across all three columns. A close date outranks a large number.',
        'candidate': Path('/tmp/mtd-figure3-candidate.jpeg'),
    },
}


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


def generate(fid: str) -> None:
    key = os.environ.get('GEMINI_API_KEY') or os.environ.get('GOOGLE_API_KEY')
    assert key, 'Set GEMINI_API_KEY before generating artwork.'
    fig = FIGURES[fid]
    data, mime = call_image(fig['prompt'], key)
    data, _, _ = helper.normalize_image_bytes_for_target(data, mime, fig['asset'])
    assert helper.detect_image_mime(data) == 'image/jpeg'
    fig['candidate'].write_bytes(data)
    print('candidate', fig['candidate'], hashlib.sha256(data).hexdigest()[:16])


def accept(fid: str, note: str) -> None:
    fig = FIGURES[fid]
    data = fig['candidate'].read_bytes()
    previous = fig['asset'].read_bytes()
    DISCARD.mkdir(exist_ok=True)
    (DISCARD / f"{KEY}-{fid}-{hashlib.sha256(previous).hexdigest()[:12]}.jpeg").write_bytes(previous)
    fig['asset'].write_bytes(data)
    digest = hashlib.sha256(data).hexdigest()
    archive = json.loads(ARCHIVE.read_text())
    for entry in archive['figures']:
        if entry.get('post') == KEY and entry.get('id') == fid:
            entry.setdefault('revisions', []).append({
                'date': '2026-09-24', 'reason': note,
                'previous_prompt': entry['prompt'], 'previous_sha256': entry.get('sha256')})
            entry['prompt'] = fig['prompt']
            entry['alt'] = fig['alt']
            entry['caption'] = fig['caption']
            entry['sha256'] = digest
            entry['visual_review'] = 'accepted 2026-09-24 after direct inspection: ' + note
            break
    else:
        raise SystemExit('archive entry not found')
    ARCHIVE.write_text(json.dumps(archive, ensure_ascii=False, indent=2) + '\n')
    print('installed', fig['asset'], digest[:16])


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'generate':
        generate(sys.argv[2])
    elif cmd == 'accept':
        accept(sys.argv[2], sys.argv[3])
    else:
        raise SystemExit('usage: generate <id> | accept <id> <note>')
