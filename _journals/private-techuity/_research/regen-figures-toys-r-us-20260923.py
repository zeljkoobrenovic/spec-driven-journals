#!/usr/bin/env python3
"""Regenerate two figures of 30-toys-r-us (archived under the legacy key 28-toys-r-us).

In-depth review 23 September 2026, round 1:
- TRU-007: the TL;DR overview labelled two different symbols STAKEHOLDER EFFECTS and used
  abstract labels. New labels: WHY CUSTOMERS BUY, CASH UNTIL IMPROVEMENTS PAY OFF,
  EFFECTS ON EMPLOYEES AND SUPPLIERS, WHAT THE EVIDENCE CANNOT TELL US.
- TRU-008: Figure 2's arrow ended at "Investment capacity" without a direction, the dashed
  links were unexplained and "Execution needs" was abstract. New result label LESS CASH
  AVAILABLE FOR INVESTMENT, arrow word CAN REDUCE, node COST OF CARRYING OUT IMPROVEMENTS,
  legend DASHED LINES: POSSIBLE REINFORCEMENT, NOT MEASURED.
Round 2 (TRU-008 follow-up): CAN REDUCE followed by LESS CASH AVAILABLE FOR INVESTMENT read as a
  double negative, so the arrow word is now CAN LEAD TO with the destination label unchanged.

The prompt archives key this post as `28-toys-r-us`, so the illustrator helper is driven
directly. `generate --only <id>` writes a candidate to /tmp; `accept <id> "<note>"` installs
it, archives the previous image under _research/discarded-*-variants/ and updates the archive.
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
LEGACY_KEY = '28-toys-r-us'
POST = J / 'posts/30-toys-r-us'

STYLE = ('Create one finished explanatory illustration for Owned, a practical book for product and '
         'engineering leaders. Landscape 16:9. Editorial ink-and-color diagram on a warm ivory background '
         '(#faf8f2), navy linework, muted teal for resources and useful progress, warm ochre for conditions '
         'and uncertainty. Use concrete objects and clean flat drawing with very light texture, generous space '
         'and a clear reading order. All labels must be large, high-contrast, correctly spelled and legible at '
         'article width and on a narrow phone screen. Use only the short labels requested below and no other '
         'text. Convey meaning through layout and objects; no dense paragraphs, no figure number, no decorative '
         'headline, no watermark, no logos, no photorealism, no 3D gradients. Do not invent financial values, '
         'dates, research findings or institutional policies.\n\n')

SUMMARY_BASE = ('Create one finished summary illustration explaining the whole post in Owned, a book for product '
                'and engineering leaders working with investors. Landscape 16:9. Calm editorial concept map with '
                'concrete drawn objects, navy ink, warm ivory background, muted teal and ochre. Use generous empty '
                'space, a clear left-to-right reading order and large high-contrast labels legible at article width '
                'and on a phone. Use only the labels explicitly requested; no decorative title, paragraph text, '
                'figure number, watermark, photorealism or 3D gradients. Do not invent numbers, dates, research '
                'findings or financial claims.\n\n')

FIGURES = {
    'summary-at-a-glance': {
        'archive': J / '_research/summary-visual-prompts-20260913.json',
        'discard_dir': J / '_research/discarded-summary-variants',
        'asset': POST / 'assets/images/28-toys-r-us/summary-at-a-glance.jpeg',
        'prompt': SUMMARY_BASE + (
            'A toy-retail transition is shown as an unfinished plank bridge carrying one toy parcel, occupying the '
            'left two thirds of the image. Two separate stone supports beneath it carry one label each: the left '
            'support WHY CUSTOMERS BUY, containing a tiny toy-order screen with three toy pictures; the right support '
            'CASH UNTIL IMPROVEMENTS PAY OFF, containing a blank monthly calendar. '
            'In the right third, two clearly separate rows. Top row: two neutral outline figures, an employee with a '
            'name badge and a supplier carrying parcels, under the single label EFFECTS ON EMPLOYEES AND SUPPLIERS. '
            'Bottom row: an open plain report with a large question mark beside it, under the single label '
            'WHAT THE EVIDENCE CANNOT TELL US. '
            'No smiles, celebration, success arrows, improved-service claims, stable-job claims, investor-value '
            'claims, green check marks, winners, numerical amounts, dates or additional text. This is a question '
            'about feasibility and consequences, not a successful rescue or a claim of one cause.\n\n'
            'TEXT: draw exactly these four labels, each exactly once and nothing else: WHY CUSTOMERS BUY, '
            'CASH UNTIL IMPROVEMENTS PAY OFF, EFFECTS ON EMPLOYEES AND SUPPLIERS, WHAT THE EVIDENCE CANNOT TELL US. '
            'The calendar, screen and report carry no words, letters or numbers. Any other text is a defect.'),
        'alt': 'An unfinished bridge carrying a toy parcel rests on two supports labelled “Why customers buy” and “Cash until improvements pay off”; at the right, an employee and a supplier are labelled “Effects on employees and suppliers”, and an open report with a question mark is labelled “What the evidence cannot tell us”.',
        'caption': 'A necessary product improvement still needs funding until its benefits arrive, and the evidence leaves some consequences unmeasured.',
        'candidate': Path('/tmp/toys-summary-candidate.jpeg'),
    },
    'interacting-business-and-financing-pressures': {
        'archive': J / '_research/article-illustration-prompts-20260913.json',
        'discard_dir': J / '_research/discarded-illustration-variants',
        'asset': POST / 'assets/images/28-toys-r-us/interacting-business-and-financing-pressures.jpeg',
        'prompt': STYLE + (
            'A simple pressure diagram for a retailer. Four ochre circles sit at the corners of the left two thirds, '
            'each with one icon and one label beneath or above it: top left COMPETITION (running figures and gears), '
            'top right DEBT SERVICE (a balance scale with a plain round weight, no currency sign), bottom left COST OF CARRYING OUT IMPROVEMENTS '
            '(a clock and a wrench), bottom right SUPPLIER TERMS (a handshake over a plain blank sheet of paper that carries no words). '
            'In the centre a larger ochre circle shows a small shop front with a padlock, labelled CASH PRESSURE. '
            'Each of the four corner circles has one solid navy arrow pointing into the central circle. '
            'From the central circle one large solid navy arrow points right, with the words CAN LEAD TO printed '
            'along the arrow, to a teal circle at the far right showing a small plant in a pot, labelled '
            'LESS CASH AVAILABLE FOR INVESTMENT. '
            'Thin dashed double-ended lines join neighbouring corner circles (left to right along the top, left to '
            'right along the bottom, top to bottom on each side). '
            'A small legend line in the bottom right corner reads DASHED LINES: POSSIBLE REINFORCEMENT, NOT MEASURED. '
            'No villains, logos, numbers, percentages, currency symbols or causal weights. The sheet of paper, the scale and the shop carry no words or letters.\n\n'
            'TEXT: draw exactly these labels and nothing else: COMPETITION, DEBT SERVICE, COST OF CARRYING OUT '
            'IMPROVEMENTS, SUPPLIER TERMS, CASH PRESSURE, CAN LEAD TO, LESS CASH AVAILABLE FOR INVESTMENT, '
            'DASHED LINES: POSSIBLE REINFORCEMENT, NOT MEASURED. Any other text is a defect.'),
        'alt': "Competition, the cost of carrying out improvements, debt service and supplier terms each press on the retailer's cash, which can lead to less cash available for investment; dashed links mark possible reinforcing effects, not measured ones.",
        'caption': 'Four pressures can reduce the cash available for investment; the dashed links are possible reinforcements, not measured causes.',
        'candidate': Path('/tmp/toys-figure2-candidate.jpeg'),
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
    fig['discard_dir'].mkdir(exist_ok=True)
    (fig['discard_dir'] / f"30-toys-r-us-{fid}-{hashlib.sha256(previous).hexdigest()[:12]}.jpeg").write_bytes(previous)
    fig['asset'].write_bytes(data)
    digest = hashlib.sha256(data).hexdigest()
    archive = json.loads(fig['archive'].read_text())
    for entry in archive['figures']:
        if entry.get('post') == LEGACY_KEY and entry.get('id') == fid:
            entry.setdefault('revisions', []).append({
                'date': '2026-09-23', 'reason': note,
                'previous_prompt': entry['prompt'], 'previous_sha256': entry.get('sha256')})
            entry['prompt'] = fig['prompt']
            entry['alt'] = fig['alt']
            entry['caption'] = fig['caption']
            entry['sha256'] = digest
            entry['visual_review'] = 'accepted 2026-09-23 after direct inspection: ' + note
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
