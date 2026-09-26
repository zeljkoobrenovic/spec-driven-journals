#!/usr/bin/env python3
"""Regenerate two figures of 27-manage-technical-debt after the in-depth review of 24 September 2026 (round 2).

- MTD-023: Figure 1 carried one unqualified "per month" label over all three columns. New label
  "Reviewed monthly" across the top, "euros per month" only under Cost carried, "own units" under the others.
- MTD-013: the TL;DR overview said "DATED ITEMS FIRST"; the qualified rule is "CLOSE DATES FIRST".

Same driver pattern as regen-figures-manage-technical-debt-20260924.py (illustrator module, Gemini 16:9).
`generate <id>` writes a candidate to /tmp; `accept <id> "<note>"` installs it, archives the previous image and
updates the matching prompt archive entry.
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
KEY = '27-manage-technical-debt'
POST = J / 'posts/27-manage-technical-debt'

STYLE = ('Create one finished explanatory illustration for Owned, a practical book for product and '
         'engineering leaders. Landscape 16:9. Editorial ink-and-color diagram on a warm ivory background '
         '(#faf8f2), navy linework, muted teal for resources and useful progress, warm ochre for conditions '
         'and uncertainty. Use concrete objects and clean flat drawing with very light texture, generous space '
         'and a clear reading order. All labels must be large, high-contrast, correctly spelled and legible at '
         'article width and on a narrow phone screen. Use only the short labels requested below and no other '
         'text. Convey meaning through layout and objects; no dense paragraphs, no figure number, no decorative '
         'headline, no watermark, no logos, no photorealism, no 3D gradients. Do not invent financial values, '
         'dates, research findings or institutional policies.\n\n')

SUMMARY_STYLE = ('Create one finished summary illustration explaining the whole post in Owned, a book for product and '
         'engineering leaders working with investors. Landscape 16:9. Calm editorial concept map with concrete drawn '
         'objects, navy ink, warm ivory background, muted teal and ochre. Use generous empty space, a clear '
         'left-to-right reading order and large high-contrast labels legible on a phone. Use only the labels '
         'explicitly requested; no decorative title, paragraph text, figure number, watermark, photorealism or 3D '
         'gradients. Do not invent numbers, dates, research findings or financial claims. \n\n')

FIGURES = {
    'carrying-cost-three-columns': {
        'archive': J / '_research/article-illustration-prompts-20260913.json',
        'discard': J / '_research/discarded-illustration-variants',
        'asset': POST / 'assets/images/27-manage-technical-debt/carrying-cost-three-columns.jpeg',
        'prompt': STYLE + (
            'A single open ledger page drawn flat on the ivory background, ruled into three tall columns of equal '
            'width. Across the top edge of the page, above all three columns, one small navy label: Reviewed monthly. '
            'Column headings, large navy capitals, exactly these three and nothing else: Cost carried; Risk carried; '
            'Speed lost. Directly under the heading Cost carried a smaller navy line: euros per month. Directly under '
            'the heading Risk carried a smaller navy line: own units. Directly under the heading Speed lost a smaller '
            'navy line: own units. Under Cost carried draw a small stack of ochre coins beside a wall clock. Under Risk '
            'carried draw a cracked navy shield with a small warning triangle and a torn calendar page. Under Speed '
            'lost draw a teal arrow that runs into a low wall and slows, with a small hourglass. No other words, no '
            'numbers, no currency signs, no rows of figures, no title.\n\n'
            'TEXT: draw exactly these labels and nothing else: Reviewed monthly; Cost carried; Risk carried; Speed '
            'lost; euros per month; own units; own units. Any other text is a defect.'),
        'alt': 'An open ledger page labelled Reviewed monthly across its top, ruled into three columns headed Cost carried, Risk carried and Speed lost; under the first heading a line reads euros per month and under the other two a line reads own units; the columns hold simple objects: coins and a clock, a cracked shield and a torn calendar, and an arrow slowed by a wall.',
        'caption': 'Technical debt is a carrying cost read every month in three columns: what it costs to keep, in euros per month, what risk it carries and what it slows, each in its own units. A count of issues or a percentage of the codebase belongs in none of them.',
        'candidate': Path('/tmp/mtd-figure1-candidate.jpeg'),
    },
    'summary-at-a-glance': {
        'archive': J / '_research/summary-visual-prompts-20260913.json',
        'discard': J / '_research/discarded-summary-variants',
        'asset': POST / 'assets/images/27-manage-technical-debt/summary-at-a-glance.jpeg',
        'prompt': SUMMARY_STYLE + (
            'Three stations from left to right. (1) On the left, one large upright ledger sheet labelled REGISTER at '
            'its top. Under the heading the sheet is divided into exactly three columns headed, left to right, COST '
            'CARRIED, RISK CARRIED and SPEED LOST; under each heading sits one simple icon (a small plain stack of '
            'coins under COST CARRIED, a cracked shield under RISK CARRIED, an hourglass under SPEED LOST) and below '
            'the icons run five plain ruled rows with no words or numbers in them. (2) In the middle, one thin line '
            'leaves the register and splits into two paths, one above the other. The upper path is ONE long, flat, '
            'plain bar labelled REWRITE, with a single small flag standing only at its far right end, labelled BENEFIT '
            'AT THE END. The lower path is a short staircase of exactly two solid ascending steps: the first step '
            'labelled TRANCHE 1 with a small flag standing on it, then a small closed barrier gate labelled GATE, then '
            'the second, higher step labelled TRANCHE 2 with a small flag standing on it; after the second step a third '
            'step is drawn only as a dashed outline with no label. (3) On the right, one small wall calendar with one '
            'day circled and a small clock beside it, labelled CLOSE DATES FIRST. The bars, steps, flags, coins, '
            'shield, hourglass and calendar carry no words, letters or numbers. No dollar, euro or other currency sign '
            'anywhere.\n\n'
            'TEXT: draw exactly these labels and nothing else: REGISTER, COST CARRIED, RISK CARRIED, SPEED LOST, '
            'REWRITE, BENEFIT AT THE END, TRANCHE 1, GATE, TRANCHE 2, CLOSE DATES FIRST. Make every label large and '
            'bold; the three column headings and the two path labels are the biggest, the others at least half their '
            'height. Any other text is a defect.'),
        'alt': 'A technical-debt register with three columns, cost carried, risk carried and speed lost, feeding a rewrite path whose benefit arrives only at the end and a tranche path with gates that release the next stage, with items whose dates are close sequenced first.',
        'caption': 'Put each item on three columns, then fund the fix in tranches released by measured gates; a close date goes first.',
        'candidate': Path('/tmp/mtd-summary-candidate.jpeg'),
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
    fig['discard'].mkdir(exist_ok=True)
    (fig['discard'] / f"{KEY}-{fid}-{hashlib.sha256(previous).hexdigest()[:12]}.jpeg").write_bytes(previous)
    fig['asset'].write_bytes(data)
    digest = hashlib.sha256(data).hexdigest()
    archive = json.loads(fig['archive'].read_text())
    for entry in archive['figures']:
        if entry.get('post') == KEY and entry.get('id') == fid:
            entry.setdefault('revisions', []).append({
                'date': '2026-09-24', 'reason': note,
                'previous_prompt': entry['prompt'], 'previous_sha256': entry.get('sha256')})
            entry['prompt'] = fig['prompt']
            entry['alt'] = fig['alt']
            entry['caption'] = fig['caption']
            entry['sha256'] = digest
            entry['visual_review'] = 'accepted 2026-09-24 (round 2) after direct inspection: ' + note
            break
    else:
        raise SystemExit('archive entry not found')
    fig['archive'].write_text(json.dumps(archive, ensure_ascii=False, indent=2) + '\n')
    print('installed', fig['asset'], digest[:16])


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'generate':
        generate(sys.argv[2])
    elif cmd == 'accept':
        accept(sys.argv[2], sys.argv[3])
    else:
        raise SystemExit('usage: generate <id> | accept <id> <note>')
