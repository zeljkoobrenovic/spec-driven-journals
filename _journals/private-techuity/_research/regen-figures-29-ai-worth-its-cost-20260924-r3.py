#!/usr/bin/env python3
"""Round-3 figure driver for 29-ai-worth-its-cost (in-depth review, 24 September 2026).

AIC-008: Figure 2 lettering: "€540 a month" -> "€540 per customer a month"; the revenue
card's period gains "projected, September estimated"; the contribution card gains the
period and "projected". Gemini lettering edit on the existing image, as in round 2.

Usage: --generate fig2 writes /tmp/aic-figures/three-numbers-never-added.jpeg;
--accept fig2 installs it, archives the old image under
_research/discarded-illustration-variants/ and updates the prompt archive.
"""
from __future__ import annotations
import argparse, base64, hashlib, importlib.util, json, os, sys, time, urllib.error, urllib.parse, urllib.request
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
POST = '29-ai-worth-its-cost'
IMG = J / 'posts' / POST / 'assets/images' / POST
ARCHIVE_JSON = J / '_research/article-illustration-prompts-20260913.json'
CAND = Path('/tmp/aic-figures')
RENDERER = 'render-figures-29-ai-worth-its-cost-20260924.py'

EDIT_PROMPT = ("Edit the attached illustration. Change ONLY three pieces of lettering, one on each card, and add nothing else. "
               "On the left-hand card, replace the large line \"€540 a month\" with \"€540 per customer a month\", same large bold lettering, "
               "on two lines if needed, keeping the small lines \"planner time freed, before the fee\" below it. "
               "On the middle card, replace the small line \"April to September 2027\" with the two small lines \"April to September 2027\" and "
               "\"projected, September estimated\", one under the other. "
               "On the right-hand card, replace the two small lines \"after supplier cost, before payroll\" with the three small lines "
               "\"April to September 2027, projected\", \"after supplier cost,\" and \"before payroll\", one under the other, in the same "
               "lettering style, size and color, shifting the drawings on the cards up slightly if the extra lines need room so that no lettering "
               "touches or overlaps any other element. Keep every other pixel of the picture as it is: the same three cards, the crossed-out plus "
               "signs, the clock, documents, price tag, card, coins, cash box, colors, the card headings Customer value, Revenue, Contribution and "
               "the large amounts €57,000 and about €26,900.")

TARGETS = {
    'fig1': dict(key='usage-construction-rates-bridge', mode='render',
                 alt="A bridge chart from April's €1,400 of model charges to August's €5,824, drawn to one scale. Usage adds €2,644, construction adds €3,236, and the vendor's rate cut removes €1,456, so the bill peaks above the August total before the price cut brings it down."),
    'fig2': dict(key='three-numbers-never-added', mode='edit', prompt=EDIT_PROMPT,
                 alt="Three cards separated by crossed-out plus signs. Customer value: €540 per customer a month, planner time freed, before the €300 fee. Revenue: €57,000, April to September 2027, projected, September estimated. Contribution: about €26,900, April to September 2027, projected, after supplier cost, before payroll.",
                 expect=['Customer value', '€540 per customer a month', 'planner time freed, before the fee', 'Revenue', '€57,000', 'April to September 2027', 'projected, September estimated', 'Contribution', 'about €26,900', 'April to September 2027, projected', 'after supplier cost,', 'before payroll']),
    'fig3': dict(key='commitment-floor-against-demand-range', mode='render',
                 alt="A vertical scale of monthly model charges in euros at list price, drawn to one scale. A shaded band marks the 2028 demand range from €3,300 low to €7,600 high with €5,200 expected. Option C's committed floor of €2,400 lies below the band; Option B's floor of €3,900 lies inside it, just above the low end. A €2,000 stress case sits below both."),
}


def candidate(tid: str) -> Path:
    return CAND / f"{TARGETS[tid]['key']}.jpeg"


def asset(tid: str) -> Path:
    return IMG / f"{TARGETS[tid]['key']}.jpeg"


def call_image(prompt: str, key: str, image: bytes | None):
    parts = [{'text': prompt}]
    if image:
        parts.append({'inline_data': {'mime_type': 'image/jpeg', 'data': base64.b64encode(image).decode()}})
    payload = {'contents': [{'role': 'user', 'parts': parts}],
               'generationConfig': {'responseModalities': ['IMAGE'], 'imageConfig': {'aspectRatio': '16:9'}}}
    url = ('https://generativelanguage.googleapis.com/v1beta/models/' + urllib.parse.quote(MODEL, safe='') + ':generateContent')
    for attempt in range(4):
        req = urllib.request.Request(url, data=json.dumps(payload).encode(), method='POST',
                                     headers={'Content-Type': 'application/json', 'x-goog-api-key': key})
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                return helper.extract_image_bytes(json.loads(r.read().decode()))
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode('utf-8', 'replace')
            if exc.code not in (429, 500, 502, 503, 504) or attempt == 3:
                raise RuntimeError(f'Gemini error {exc.code}: {detail[:500]}')
        except (urllib.error.URLError, TimeoutError):
            if attempt == 3:
                raise
        time.sleep(5 * 2 ** attempt)
    raise RuntimeError('exhausted retries')


def generate(tid: str) -> None:
    t = TARGETS[tid]
    assert t['mode'] == 'edit', f'{tid} is rendered by {RENDERER}, not generated'
    key = os.environ.get('GEMINI_API_KEY') or os.environ.get('GOOGLE_API_KEY')
    assert key, 'GEMINI_API_KEY missing'
    data, mime = call_image(t['prompt'], key, asset(tid).read_bytes())
    data, _, _ = helper.normalize_image_bytes_for_target(data, mime, asset(tid))
    assert helper.detect_image_mime(data) == 'image/jpeg'
    CAND.mkdir(exist_ok=True)
    candidate(tid).write_bytes(data)
    print('candidate', tid, candidate(tid), hashlib.sha256(data).hexdigest()[:16])
    print('  verify lettering:', ' | '.join(t['expect']))


def accept(tid: str, note: str) -> None:
    t = TARGETS[tid]
    cand = candidate(tid)
    assert cand.exists(), f'no candidate for {tid}'
    new, old = cand.read_bytes(), asset(tid).read_bytes()
    old_sha, new_sha = hashlib.sha256(old).hexdigest(), hashlib.sha256(new).hexdigest()
    arch_dir = J / '_research/discarded-illustration-variants'
    arch_dir.mkdir(exist_ok=True)
    arch = arch_dir / f"{POST}-{t['key']}-{old_sha[:12]}.jpeg"
    if not arch.exists():
        arch.write_bytes(old)
    asset(tid).write_bytes(new)
    archive = json.loads(ARCHIVE_JSON.read_text())
    hits = [e for e in archive['figures'] if e.get('post') == POST and e.get('id') == t['key']]
    assert len(hits) == 1
    e = hits[0]
    e['sha256'] = new_sha
    e['alt'] = t['alt']
    if t['mode'] == 'render':
        e['status'] = 'rendered'
        e['renderer'] = f'_research/{RENDERER} (authored SVG rasterized with Playwright; numeric coordinates, one scale)'
        e['prompt'] = f'Not a Gemini prompt: rendered from numeric coordinates by _research/{RENDERER}.'
    else:
        e['prompt'] = e['prompt'].replace("'€540 a month'", "'€540 per customer a month'").replace("'April to September 2027'", "'April to September 2027' and 'projected, September estimated'").replace("'after supplier cost, before payroll'", "'April to September 2027, projected', 'after supplier cost,' and 'before payroll'")
        e['prompt'] = e['prompt'].replace("Customer value, €540 a month, planner time freed, before the fee, Revenue, €57,000, April to September 2027, Contribution, about €26,900, after supplier cost, before payroll.", "Customer value, €540 per customer a month, planner time freed, before the fee, Revenue, €57,000, April to September 2027, projected, September estimated, Contribution, about €26,900, April to September 2027, projected, after supplier cost, before payroll.")
        e['edit_prompt'] = t['prompt']
    stamp = e.get('visual_review', '') + f" / 2026-09-24 (in-depth review round 3): {note}; previous image archived as {arch.name}"
    e['visual_review'] = stamp
    if t['key'] == 'three-numbers-never-added':
        e['visual_goal'] = 'Customer value (time freed, before the fee), revenue and contribution before payroll (supplier costs in the months they concern) are three different answers to what the feature is worth, belonging to different owners, and must never be summed.'
        e['caption'] = "Three answers to what the sorting feature is worth, and none of them adds to the others. Customer value is the estimated worth of the planner time one customer frees each month, before the fee, and is not money Larkspur receives; revenue is Larkspur's money before costs; contribution is what remains after the supplier running cost for the stated period, each month's bills counted in that month, before the salaries already in payroll. The two period figures are projections because September is estimated at August's level."
    if t['key'] == 'commitment-floor-against-demand-range':
        e['visual_goal'] = "A committed spend is a floor under next year's cost. Option C's €2,400 floor sits below the low end of the derived demand range (€3,300 to €7,600 a month at list price); Option B's €3,900 floor sits inside it, 600 above the low end and 1,300 below the expected case, which is why C saves at every point in the range and B costs more when demand disappoints. Drawn to one scale."
    ARCHIVE_JSON.write_text(json.dumps(archive, ensure_ascii=False, indent=2) + '\n')
    print('accepted', tid, '->', asset(tid), new_sha[:16], 'archived', arch.name)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--generate', nargs='*', default=[])
    ap.add_argument('--accept', nargs='*', default=[])
    ap.add_argument('--note', default='revised after the in-depth review')
    a = ap.parse_args()
    for tid in a.generate:
        generate(tid)
    for tid in a.accept:
        accept(tid, a.note)
