#!/usr/bin/env python3
"""Regenerate three figures of 26-manage-technical-debt after the in-depth review of 24 September 2026 (round 3).

- MTD-025: Figure 1's top label "Reviewed monthly" conflicts with the quarterly register review -> "Measured monthly, reviewed quarterly" (lettering edit on the existing image).
- MTD-013: Figure 3 made proximity decisive ("Close dates first") and showed money as the only benefit -> redraw with the qualified rule and coin/shield/hourglass per card.
- MTD-013: the TL;DR overview's "CLOSE DATES FIRST" -> "DEADLINE RISK AGAINST HARM NOW" (lettering edit).

Same driver pattern as regen-figures-manage-technical-debt-round2-20260924.py; lettering edits attach the existing image.
`generate <id>` writes a candidate to /tmp; `accept <id> "<note>"` installs it, archives the previous image and updates the archive entry.
"""
from __future__ import annotations
import base64, hashlib, importlib.util, json, os, sys, urllib.request, urllib.parse
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[3]
J = ROOT / '_journals/private-techuity'
R2 = Path(__file__).with_name('regen-figures-manage-technical-debt-round2-20260924.py')
spec = importlib.util.spec_from_file_location('r2', R2)
r2 = importlib.util.module_from_spec(spec); sys.modules['r2'] = r2; spec.loader.exec_module(r2)
helper, STYLE, MODEL, KEY, POST = r2.helper, r2.STYLE, r2.MODEL, r2.KEY, r2.POST


def edit_prompt(old: str, new: str) -> str:
    return ("Edit the attached illustration. Change ONLY one piece of lettering: replace the exact words "
            f'"{old}" with the exact words "{new}", in the same place, same lettering style and color, on as many '
            "lines as the new words need so that they stay clear of every other element, shrinking the lettering a little "
            "if needed. Keep every other pixel of the picture as it is: the same shapes, columns, icons, colors and all "
            "other text. Add nothing else.")


FIGURES = {
    'carrying-cost-three-columns': dict(r2.FIGURES['carrying-cost-three-columns'], mode='edit',
        prompt=edit_prompt('Reviewed monthly', 'Measured monthly, reviewed quarterly'),
        archived_prompt=r2.FIGURES['carrying-cost-three-columns']['prompt'].replace(
            'one small navy label: Reviewed monthly.', 'one small navy label: Measured monthly, reviewed quarterly.').replace(
            'nothing else: Reviewed monthly;', 'nothing else: Measured monthly, reviewed quarterly;'),
        alt='An open ledger page labelled Measured monthly, reviewed quarterly across its top, ruled into three columns headed Cost carried, Risk carried and Speed lost; under the first heading a line reads euros per month and under the other two a line reads own units; the columns hold simple objects: coins and a clock, a cracked shield and a torn calendar, and an arrow slowed by a wall.',
        caption='Technical debt is a carrying cost measured every month and reviewed every quarter, in three columns: what it costs to keep, in euros per month, what risk it carries and what it slows, each in its own units. A count of issues or a percentage of the code belongs in none of them.',
        candidate=Path('/tmp/mtd-r3-figure1.jpeg'),
        expect=['Measured monthly, reviewed quarterly', 'Cost carried', 'euros per month', 'Risk carried', 'own units', 'Speed lost', 'own units']),
    'sequencing-rule': dict(
        archive=J / '_research/article-illustration-prompts-20260913.json',
        discard=J / '_research/discarded-illustration-variants',
        asset=POST / 'assets/images/26-manage-technical-debt/sequencing-rule.jpeg',
        mode='generate',
        prompt=STYLE + (
            'A single queue of five simple record cards laid left to right on the ivory background, with a large navy '
            'arrow beneath the whole row pointing right and labeled Order of work. The first two cards each carry a '
            'small ochre calendar icon with a ring binding and, beside it, a small cracked navy shield, and nothing else; '
            'they are grouped under one large navy bracket above them labeled Deadline risk weighed against harm now. '
            'The remaining three cards are grouped under a second navy bracket above them labeled Then by cost, risk '
            'and delay removed per effort. Each of these three cards shows two things side by side: on its left a tight '
            'group of three small icons, a stack of teal coins, a small navy shield and a small ochre hourglass; on its '
            'right a small row of navy wrench icons. Third card: a medium stack of coins and ONE wrench. Fourth card: a '
            'tall stack of coins and THREE wrenches. Fifth card: a short stack of coins and THREE wrenches. In the bottom '
            'right corner a small two-line legend: Coins, shield, hourglass: cost, risk and delay removed / Wrenches: '
            'effort. Cards are plain, with no writing on them.\n\n'
            'TEXT: draw exactly these labels, each once, and nothing else: Deadline risk weighed against harm now; Then '
            'by cost, risk and delay removed per effort; Order of work; Coins, shield, hourglass: cost, risk and delay '
            'removed; Wrenches: effort. No numbers, no dates, no title, no currency signs. Any other text is a defect.'),
        alt='Five record cards in a row: the first two each carry a calendar and a small cracked shield under a bracket labelled Deadline risk weighed against harm now; the next three each carry a coin stack, a shield and an hourglass for what the work removes beside a small wrench count for the effort, under a bracket labelled Then by cost, risk and delay removed per effort; below runs an arrow labelled Order of work.',
        caption='The sequencing rule written into the register: an item whose external date leaves little more time than the work needs, plus a margin for overrun, is weighed first, by what missing the date would cost against the harm undated items do now; items brought forward go in date order. The rest follow in order of the cost, risk and delay each tranche of effort would remove, read across all three columns. A distant date with little work behind it can wait.',
        candidate=Path('/tmp/mtd-r3-figure3.jpeg'),
        expect=['Deadline risk weighed against harm now', 'Then by cost, risk and delay removed per effort', 'Order of work', 'Coins, shield, hourglass: cost, risk and delay removed', 'Wrenches: effort', 'calendar + shield on cards 1-2', 'coins + shield + hourglass on cards 3-5', 'wrenches 1/3/3']),
    'summary-at-a-glance': dict(r2.FIGURES['summary-at-a-glance'], mode='edit',
        prompt=edit_prompt('CLOSE DATES FIRST', 'DEADLINE RISK AGAINST HARM NOW'),
        archived_prompt=r2.FIGURES['summary-at-a-glance']['prompt'].replace(
            'labelled CLOSE DATES FIRST.', 'labelled DEADLINE RISK AGAINST HARM NOW.').replace(
            'TRANCHE 2, CLOSE DATES FIRST.', 'TRANCHE 2, DEADLINE RISK AGAINST HARM NOW.'),
        alt='A technical-debt register with three columns, cost carried, risk carried and speed lost, feeding a rewrite path whose benefit arrives only at the end and a tranche path with gates that release the next stage, with a calendar and clock labelled deadline risk against harm now for the items whose dates are weighed first.',
        caption='Put each item on three columns, then fund the fix in tranches released by measured gates; an item with an outside date is weighed first, against the harm undated items do now.',
        candidate=Path('/tmp/mtd-r3-summary.jpeg'),
        expect=['REGISTER', 'COST CARRIED', 'RISK CARRIED', 'SPEED LOST', 'REWRITE', 'BENEFIT AT THE END', 'TRANCHE 1', 'GATE', 'TRANCHE 2', 'DEADLINE RISK AGAINST HARM NOW']),
}
for f in FIGURES.values():
    f.setdefault('archived_prompt', f['prompt'])
assert 'CLOSE DATES FIRST' not in FIGURES['summary-at-a-glance']['archived_prompt']
assert 'Reviewed monthly' not in FIGURES['carrying-cost-three-columns']['archived_prompt']


def call_image(prompt: str, key: str, image: bytes | None):
    parts = [{'text': prompt}]
    if image:
        parts.append({'inline_data': {'mime_type': 'image/jpeg', 'data': base64.b64encode(image).decode()}})
    endpoint = ('https://generativelanguage.googleapis.com/v1beta/models/' + urllib.parse.quote(MODEL, safe='') + ':generateContent')
    payload = {'contents': [{'role': 'user', 'parts': parts}],
               'generationConfig': {'responseModalities': ['IMAGE'], 'imageConfig': {'aspectRatio': '16:9'}}}
    request = urllib.request.Request(endpoint, data=json.dumps(payload).encode(),
                                     headers={'Content-Type': 'application/json', 'x-goog-api-key': key}, method='POST')
    with urllib.request.urlopen(request, timeout=300) as response:
        return helper.extract_image_bytes(json.loads(response.read().decode()))


def generate(fid: str) -> None:
    key = os.environ.get('GEMINI_API_KEY') or os.environ.get('GOOGLE_API_KEY')
    assert key, 'Set GEMINI_API_KEY before generating artwork.'
    fig = FIGURES[fid]
    image = fig['asset'].read_bytes() if fig['mode'] == 'edit' else None
    data, mime = call_image(fig['prompt'], key, image)
    data, _, _ = helper.normalize_image_bytes_for_target(data, mime, fig['asset'])
    assert helper.detect_image_mime(data) == 'image/jpeg'
    fig['candidate'].write_bytes(data)
    print('candidate', fid, fig['candidate'], hashlib.sha256(data).hexdigest()[:16])
    print('  verify lettering:', ' | '.join(fig['expect']))


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
            entry['prompt'] = fig['archived_prompt']
            entry['alt'] = fig['alt']
            entry['caption'] = fig['caption']
            entry['sha256'] = digest
            entry['visual_review'] = 'accepted 2026-09-24 (round 3) after direct inspection: ' + note
            break
    else:
        raise SystemExit('archive entry not found')
    fig['archive'].write_text(json.dumps(archive, ensure_ascii=False, indent=2) + '\n')
    print('installed', fig['asset'], digest[:16])


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'generate':
        for fid in sys.argv[2:]:
            generate(fid)
    elif cmd == 'accept':
        accept(sys.argv[2], sys.argv[3])
    else:
        raise SystemExit('usage: generate <id>... | accept <id> <note>')
