#!/usr/bin/env python3
"""Regenerate Figure 1 of 15-adopt-outcome-thinking after the in-depth review of 24 September 2026 (round 3).

- AOT-006: the shared measure (share of customers reaching a first real schedule within eight weeks) was absent from the
  customer pyramid, whose top carried only the median. New render: the top block carries the median and the share, the
  business block is labelled as a share, and the dotted-line sign says the two ends read the same dates.

Round-2 notes kept below for the record.

- AOT-006 / AOT-007 / AOT-013: Figure 1 claimed two shared measures and carried responsibility tags broader than
  the measures under them. New render: one dotted link (first real schedule within eight weeks), a responsibility
  tag under each pair of measures, the gross-margin note as a card outside the pyramid, and a card saying the
  business measures are a selection (renewal rate counts customers, NRR counts revenue).
- AOT-008: Figure 3 put every measure on one axis starting at setup go-live, with day 90 on the same axis.
  New render: one row per measure with its own trigger and window, and the day-90 review on a separate
  closing-based row.

Drives the illustrator helper directly (same pattern as regen-figures-manage-technical-debt-20260924.py).
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
KEY = '15-adopt-outcome-thinking'
POST = J / 'posts/15-adopt-outcome-thinking'
ARCHIVE = J / '_research/article-illustration-prompts-20260913.json'
DISCARD = J / '_research/discarded-illustration-variants'

STYLE = ('Create one finished explanatory illustration for Owned, a practical book for product and engineering '
         'leaders. Landscape 16:9. Editorial ink-and-color diagram on a warm ivory background (#faf8f2), navy '
         'linework, muted teal for the customer side and useful progress, warm ochre for the business side and '
         'conditions. Use concrete objects and clean flat drawing with very light texture, generous space and a '
         'clear reading order. All labels must be large, high-contrast, correctly spelled and legible at article '
         'width and on a narrow phone screen. Use only the short labels requested below, spelled exactly as '
         'written, and no other text. Convey meaning through layout and objects; no dense paragraphs, no figure '
         'number, no decorative headline, no watermark, no logos, no photorealism, no 3D gradients. Do not invent '
         'financial values, dates, research findings or institutional policies.\n\n')

FIGURES = {

    'two-pyramids-joined': {
        'asset': POST / 'assets/images/15-adopt-outcome-thinking/two-pyramids-joined.jpeg',
        'prompt': STYLE + (
            "Two flat block pyramids side by side, each exactly three rows high, drawn with thin navy outlines, every "
            "block lettered. LEFT, teal pyramid. Top row, one wide block, lettered exactly 'Customer outcome: median "
            "weeks to first real schedule; share within eight weeks'. Middle row, three equal blocks, lettered exactly 'Setup effort', 'Customer "
            "data readiness', 'Early use'. Bottom row, six small equal blocks, two beneath each middle block, lettered "
            "exactly, left to right: 'Staff hours per setup', 'Setups needing manual configuration', 'Data clean "
            "enough to load', 'Days until the customer returns its data', 'Scheduling real work in week one', 'Setup "
            "support requests in month one'. Directly beneath each PAIR of bottom blocks hangs one small teal "
            "responsibility tag, exactly as wide as that pair, so the left pyramid has three tags in a row, lettered "
            "exactly, left to right: 'Product accountable'; 'Shared: product, customer, customer success'; 'Shared: "
            "product, customer success, support'. RIGHT, ochre pyramid. Top row, one wide block, lettered exactly "
            "'Business outcome: net revenue retention'. Middle row, two equal blocks, lettered exactly 'Renewal', "
            "'Expansion'. Bottom row, four small equal blocks, two beneath each middle block, lettered exactly, left "
            "to right: 'Share reaching first schedule within eight weeks', 'Renewal rate at contract anniversary', 'All "
            "technicians scheduled by month three', 'Technicians or locations added within a year'. The block 'Share reaching "
            "first schedule within eight weeks' is tinted teal like the left pyramid; the other three are ochre. "
            "Directly beneath the right pyramid's bottom row hang three small ochre responsibility tags, lettered "
            "exactly, left to right: under the first block, 'Product accountable'; under the second block, 'Customer "
            "success and pricing accountable'; under the third and fourth blocks together, one tag exactly as wide as "
            "that pair, 'Sales and customer success accountable'. Exactly one dotted navy line in the whole picture: it "
            "runs from the left pyramid's top block to the teal block 'Share reaching first schedule within eight weeks' in the "
            "right pyramid, with a small navy sign on it lettered exactly 'The one shared measure: same dates; link under test'. "
            "Three free-standing cards with no connecting lines: in the top left corner of the picture, a small teal "
            "card lettered exactly 'Staff hours and month-one requests also feed gross margin, outside this pyramid'; "
            "in the top right corner, a small ochre card lettered exactly 'New customers signed feed annual recurring "
            "revenue (sales); not part of retention'; centred at the very bottom of the picture beneath the tags, a "
            "small ochre card lettered exactly 'Business measures are a selection: renewal rate counts customers, net "
            "revenue retention counts revenue'. No people, no other labels, no numbers other than the words eight, "
            "one, three and a year inside the labels.\n\n"
            "TEXT: draw exactly the block labels, the seven responsibility tags, the one sign and the three cards "
            "listed above, each once, and nothing else. Any other text is a defect."),
        'alt': 'Two block pyramids side by side, each with three levels: the outcome on top, the contributing factors beneath and their measures beneath those. The teal customer pyramid is topped by customer outcome, median weeks to first real schedule and the share within eight weeks; under it setup effort, customer data readiness and early use; under those staff hours per setup, setups needing manual configuration, data clean enough to load, days until the customer returns its data, scheduling real work in week one and setup support requests in month one. The ochre business pyramid is topped by business outcome, net revenue retention; under it renewal and expansion; under those the share reaching a first schedule within eight weeks, renewal rate at contract anniversary, all technicians scheduled by month three and technicians or locations added within a year. Under each pair of measures a tag names who is accountable: product for staff hours and manual configuration; product, the customer and customer success for the two data measures; product, customer success and support for week-one scheduling and month-one requests; product for the share within eight weeks; customer success and pricing for the renewal rate; sales and customer success for the two expansion measures. One dotted line from the customer outcome to the share reaching a first schedule within eight weeks is labelled the one shared measure, same dates, link under test. Three cards stand apart: staff hours and month-one requests also feed gross margin, outside this pyramid; new customers signed feed annual recurring revenue and are not part of retention; the measures are a selection, and renewal rate counts customers while net revenue retention counts revenue.',
        'caption': 'The two pyramids and the chain between them. Every branch has the same three levels: outcome, factor, measures. One measure sits in both pyramids: the share of customers reaching a first real schedule within eight weeks, read from the same dates as the customer outcome’s median, confirms the customer outcome and, if the hypothesis holds, feeds renewal. Staff hours per setup are not shared: they are the suspected main cause of the customer’s wait, which the pilot tests by lowering them, and they also feed gross margin, outside the retention pyramid, as new customers signed feed annual recurring revenue. The tag under each pair of measures says who is accountable for them; product influences the business measures through the shared one. The business measures are a selection of indicators the teams can act on: the renewal rate counts customers, while net revenue retention counts revenue.',
        'candidate': Path('/tmp/aot-figure1-r3-candidate.jpeg'),
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


def generate(fid: str, suffix: str = '') -> None:
    key = os.environ.get('GEMINI_API_KEY') or os.environ.get('GOOGLE_API_KEY')
    assert key, 'Set GEMINI_API_KEY before generating artwork.'
    fig = FIGURES[fid]
    data, mime = call_image(fig['prompt'], key)
    data, _, _ = helper.normalize_image_bytes_for_target(data, mime, fig['asset'])
    assert helper.detect_image_mime(data) == 'image/jpeg'
    target = fig['candidate'].with_name(fig['candidate'].stem + suffix + '.jpeg')
    target.write_bytes(data)
    print('candidate', target, hashlib.sha256(data).hexdigest()[:16])


def accept(fid: str, note: str, suffix: str = '') -> None:
    fig = FIGURES[fid]
    data = fig['candidate'].with_name(fig['candidate'].stem + suffix + '.jpeg').read_bytes()
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
            entry['visual_review'] = 'accepted 2026-09-24 (in-depth review round 3) after direct inspection: ' + note
            break
    else:
        raise SystemExit('archive entry not found')
    ARCHIVE.write_text(json.dumps(archive, ensure_ascii=False, indent=2) + '\n')
    print('installed', fig['asset'], digest[:16])


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'generate':
        generate(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else '')
    elif cmd == 'accept':
        accept(sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else '')
    else:
        raise SystemExit('usage: generate <id> [suffix] | accept <id> <note> [suffix]')
