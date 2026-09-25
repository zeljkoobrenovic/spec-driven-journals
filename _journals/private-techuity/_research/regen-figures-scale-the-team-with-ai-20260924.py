#!/usr/bin/env python3
"""Regenerate or edit the figures of 23-scale-the-team-with-ai after the in-depth review of 24 Sept 2026.

SAI-003: Figure 1 padlock label "No tool touches this" -> "Unchanged by faster coding alone" (lettering edit).
SAI-006: Figure 2 bar "Fresh samples, same checks" -> "Every item, same checks" (lettering edit).
SAI-004/005: Figure 3 gate ladder redrawn (gate day 120, quality and lead time, three non-overlapping bands).
SAI-002/004: TL;DR overview redrawn (seven queue days, two build days, one release day; gate day 120).

Usage: --generate <id...> writes candidates to /tmp/scale-ai-<id>.jpeg; --accept <id...> installs a candidate,
archives the old image under _research/discarded-*-variants/ and updates the prompt archives.
"""
from __future__ import annotations
import argparse, base64, hashlib, importlib.util, json, os, shutil, sys, time, urllib.error, urllib.parse, urllib.request
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
POST = '23-scale-the-team-with-ai'
IMG = J / 'posts' / POST / 'assets/images' / POST
ILL_ARCHIVE = J / '_research/article-illustration-prompts-20260913.json'
SUM_ARCHIVE = J / '_research/summary-visual-prompts-20260913.json'

BASE = ("Create one finished explanatory illustration for Owned, a practical book for product and engineering leaders. Landscape 16:9. Editorial ink-and-color diagram on a warm ivory background (#faf8f2), navy linework, muted teal for resources and useful progress, warm ochre for conditions and uncertainty. Use concrete objects and clean flat drawing with very light texture, generous space and a clear reading order. All labels must be large, high-contrast, correctly spelled and legible at article width and on a narrow phone screen. Use only the short labels requested below and no other text. Convey meaning through layout and objects; no dense paragraphs, no figure number, no decorative headline, no watermark, no logos, no photorealism, no 3D gradients. Do not invent financial values, dates, research findings or institutional policies.\n\n")

FIG3_SCENE = ("A decision ladder read from top to bottom, drawn as a vertical flow of simple flat panels joined by short navy arrows with one triangular arrowhead each. At the top, one ochre gate shaped like a simple archway with the label exactly 'Gate: day 120'. Directly under it, one navy diamond labelled exactly 'Quality and lead time hold?'. From the diamond one arrow goes left to a small ochre panel labelled exactly 'No: tool withdrawn', and one arrow goes down, labelled exactly 'Yes', into a vertical stack of three rungs, each a horizontal panel with a label on the left and a result on the right. Top rung, teal: left 'Gain of 20% or more', right 'Continue, extend seats'. Middle rung, ochre: left 'Gain above 0%, below 20%', right 'One 60-day extension, no new seats'. Bottom rung, light grey: left 'Gain of 0% or less', right 'Withdraw, record lessons'. The three rungs are stacked with a small gap between them and no arrows between the rungs; only the 'Yes' arrow enters the stack from above. To the right of the ladder, separate from every arrow, exactly ONE small navy card with a padlock reading exactly 'Second team: unchanged'; draw this card once only, never repeat it. Each rung contains only its two pieces of lettering and nothing else. No icons, charts, coins, chairs, calendars, hands or currency signs anywhere in the picture. No other labels, no people, no percentages other than the three written above.")

SUMMARY_PROMPT = ("Create one finished summary illustration explaining the whole post in Owned, a book for product and engineering leaders working with investors. Landscape 16:9. Calm editorial concept map with concrete drawn objects, navy ink, warm ivory background, muted teal and ochre. Use generous empty space, a clear reading order from left to right and large high-contrast labels legible at article width; every label is lettered in large plain capitals and nothing overlaps a label. Left: a single row of exactly ten equal square tiles standing on a bare floor, carrying the numerals 1 to 10, one numeral per tile, in order from left to right and nothing else; above the row hang exactly three signs joined to the tiles by plain brackets, in this order: QUEUE bracketing tiles 1 to 7, BUILD bracketing tiles 8 and 9, RELEASE bracketing only tile 10; a small robot hand holding a pencil touches only tiles 8 and 9. The three signs and the ten numerals are the only lettering in the left part of the picture. Centre: one clipboard standing upright labeled COMPLETED WORK with plain ticked ruled lines, and beside it, smaller and set aside, a plain counter dial labeled ACTIVITY. Centre-right: one open envelope on a desk and exactly three trays in one row labeled CONDITION, VOTE and BENCHMARK, with the note sliding into the BENCHMARK tray. Right: a simple closed wooden gate with a hanging sign labeled DAY 120, and behind the gate a pinned card labeled SECOND TEAM: CONDITIONS UNCHANGED. Use only the labels explicitly requested; no decorative title, paragraph text, figure number, watermark, photorealism or 3D gradients. Do not invent numbers, dates, research findings or financial claims.")

def edit_prompt(old: str, new: str) -> str:
    return ("Edit the attached illustration. Change ONLY one piece of lettering: replace the exact words "
            f'"{old}" with the exact words "{new}", in the same place, same lettering style, size and color, '
            "on as many lines as the new words need so that they stay clear of every other element. Keep every other pixel of the picture as it is: the same shapes, tiles, brackets, icons, colors and all other text. Add nothing else.")

TARGETS = {
    'fig1': dict(asset=IMG / 'one-day-of-ten.jpeg', archive=ILL_ARCHIVE, key='one-day-of-ten', mode='edit',
                 prompt=edit_prompt('No tool touches this', 'Unchanged by faster coding alone'),
                 expect=['Ten working days', 'Specialist queue: 7 days', 'Unchanged by faster coding alone', 'Build and test: 2 days', 'A tool can move this day', 'Release: 1 day', 'Halving the build saves one day of ten']),
    'fig2': dict(asset=IMG / 'two-pilots-one-method.jpeg', archive=ILL_ARCHIVE, key='two-pilots-one-method', mode='edit',
                 prompt=edit_prompt('Fresh samples, same checks', 'Every item, same checks'),
                 expect=['Engineering pilot', '14 engineers, 90 days', 'Customer setup pilot', '3 specialists, 90 days', 'Baseline: the 3 months before', 'Every item, same checks', 'Reviewer records review time']),
    'fig3': dict(asset=IMG / 'gate-rules-quality-first.jpeg', archive=ILL_ARCHIVE, key='gate-rules-quality-first', mode='generate',
                 prompt=BASE + FIG3_SCENE,
                 expect=['Gate: day 120', 'Quality and lead time hold?', 'No: tool withdrawn', 'Yes', 'Gain of 20% or more', 'Continue, extend seats', 'Gain above 0%, below 20%', 'One 60-day extension, no new seats', 'Gain of 0% or less', 'Withdraw, record lessons', 'Second team: unchanged']),
    'summary': dict(asset=IMG / 'summary-at-a-glance.jpeg', archive=SUM_ARCHIVE, key='summary-at-a-glance', mode='generate',
                    prompt=SUMMARY_PROMPT,
                    expect=['QUEUE (tiles 1-7)', 'BUILD (tiles 8-9)', 'RELEASE (tile 10)', 'COMPLETED WORK', 'ACTIVITY', 'CONDITION', 'VOTE', 'BENCHMARK', 'DAY 120', 'SECOND TEAM: CONDITIONS UNCHANGED']),
}

def candidate(tid: str) -> Path:
    return Path(f'/tmp/scale-ai-{tid}.jpeg')

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
        except (urllib.error.URLError, TimeoutError) as exc:
            if attempt == 3:
                raise
        time.sleep(5 * 2 ** attempt)
    raise RuntimeError('exhausted retries')

def generate(tid: str) -> None:
    t = TARGETS[tid]
    key = os.environ.get('GEMINI_API_KEY') or os.environ.get('GOOGLE_API_KEY')
    assert key, 'GEMINI_API_KEY missing'
    image = t['asset'].read_bytes() if t['mode'] == 'edit' else None
    data, mime = call_image(t['prompt'], key, image)
    data, _, _ = helper.normalize_image_bytes_for_target(data, mime, t['asset'])
    assert helper.detect_image_mime(data) == 'image/jpeg'
    candidate(tid).write_bytes(data)
    print('candidate', tid, candidate(tid), hashlib.sha256(data).hexdigest()[:16])
    print('  verify lettering:', ' | '.join(t['expect']))

def accept(tid: str, note: str) -> None:
    t = TARGETS[tid]
    cand = candidate(tid)
    assert cand.exists(), f'no candidate for {tid}'
    new = cand.read_bytes()
    old = t['asset'].read_bytes()
    old_sha = hashlib.sha256(old).hexdigest()
    new_sha = hashlib.sha256(new).hexdigest()
    arch_dir = J / '_research' / ('discarded-summary-variants' if tid == 'summary' else 'discarded-illustration-variants')
    arch_dir.mkdir(exist_ok=True)
    arch = arch_dir / f"{POST}-{t['key']}-{old_sha[:12]}.jpeg"
    if not arch.exists():
        arch.write_bytes(old)
    t['asset'].write_bytes(new)
    # update the prompt archive entry
    archive = json.loads(t['archive'].read_text())
    entries = archive['figures'] if isinstance(archive, dict) and 'figures' in archive else archive
    hits = [e for e in (entries if isinstance(entries, list) else []) if e.get('post') == POST and e.get('id') == t['key']]
    if not hits and isinstance(archive, dict):
        for v in archive.values():
            if isinstance(v, list):
                hits = [e for e in v if isinstance(e, dict) and e.get('post') == POST and e.get('id') == t['key']]
                if hits:
                    break
    assert len(hits) == 1, f'archive entry not found for {tid}'
    e = hits[0]
    if t['mode'] == 'generate':
        e['prompt'] = t['prompt']
    e['sha256'] = new_sha
    stamp = f"2026-09-24 (in-depth review): {note}; previous image archived as {arch.name}"
    if 'visual_review' in e:
        e['visual_review'] = stamp
    else:
        e['revision'] = stamp
    if tid == 'fig1':
        e['alt'] = e['alt'].replace('with a padlock noting that no tool touches this', 'with a padlock noting that this is unchanged by faster coding alone')
        e['caption'] = ("The forecast trace after the delegation, laid out day by day for a catalogue change. Morgan’s tools reach the two building days. The seven-day queue is the wait for one of the two people who can change the invoicing module safely; faster coding alone does not move it, and it is held fixed here as an assumption. A tool relieves it only if it passes the same transfer test as the billing engineer, or if the pilot’s lead-time measure shows the specialists clearing it faster. Halving the building stage would bring a change forward by one day in ten.")
        e['prompt'] = e['prompt'].replace("'No tool touches this'", "'Unchanged by faster coding alone'")
    if tid == 'fig2':
        e['alt'] = e['alt'].replace('fresh samples, same checks', 'every item, same checks')
        e['prompt'] = e['prompt'].replace("'Fresh samples, same checks'", "'Every item, same checks'")
        e['visual_goal'] = e['visual_goal'].replace('fresh samples with the old checks', 'every item checked the old way')
        e['caption'] = ("Two pilots, one method. The engineering pilot and the customer-setup pilot differ in what can go wrong, a code defect found by a test or a wrong configuration found by a customer, and share the rules that make the result a measurement: a baseline from the same trace, every change and every setup checked the old way each month, and review time written down by the person who reads the generated work. The fourth rule, recording what else changed, is not drawn.")
    if tid == 'fig3':
        e['visual_goal'] = 'The gate as a ladder judged on day 120: quality and lead time as the prerequisite before any throughput band, three non-overlapping bands, and the second team’s decision outside all of it.'
        e['alt'] = 'Decision ladder. A gate labelled day 120 leads to the question quality and lead time hold? No leads to tool withdrawn. Yes leads to three rungs: gain of 20% or more, continue and extend seats; gain above 0%, below 20%, one 60-day extension with no new seats; gain of 0% or less, withdraw and record lessons. A separate padlocked card reads second team: unchanged.'
        e['caption'] = ("The gate rules as a ladder, judged on day 120 so that every setup has had its thirty days and the last reconciliation exists. Quality and lead time are the first question and the prerequisite for every branch; a pilot whose evidence is missing is treated the same way as one that fails it. Only then is throughput judged, in three bands that do not overlap, with a single extension for the middle band. The card at the side is the point of the section: none of the branches approves, resizes or cancels the second team, which stays on its three conditions for the board.")
    if tid == 'summary':
        e['alt'] = 'A tool touches only the build tiles of a ten-day trace of seven queue days, two build days and one release day; completed work is measured on a clipboard while an activity counter sits aside; an adviser’s note is sorted into condition, vote and benchmark; and a gate marked day 120 stands before the second team’s unchanged conditions.'
    t['archive'].write_text(json.dumps(archive, ensure_ascii=False, indent=2) + '\n')
    print('accepted', tid, '->', t['asset'], new_sha[:16], 'archived', arch.name)

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--generate', nargs='*', default=[])
    ap.add_argument('--accept', nargs='*', default=[])
    ap.add_argument('--note', default='regenerated after the in-depth review')
    a = ap.parse_args()
    for tid in a.generate:
        generate(tid)
    for tid in a.accept:
        accept(tid, a.note)
