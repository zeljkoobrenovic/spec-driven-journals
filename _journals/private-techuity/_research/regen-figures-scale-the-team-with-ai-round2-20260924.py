#!/usr/bin/env python3
"""Round 2 of the in-depth review of 23-scale-the-team-with-ai (24 Sept 2026).

SAI-003: Figure 1 padlock label "Unchanged by faster coding alone" -> "Held at 7 days for this calculation" (lettering edit).
SAI-005: Figure 3 middle rung result gains the extension's terminal outcome (lettering edit).
SAI-002: TL;DR overview redrawn so the brackets span queue 1-7, build 8-9, release 10 (tiles coloured to match Figure 1).

Reuses the round-1 script's helpers. Usage: --generate <ids> writes candidates to /tmp/scale-ai-r2-<id>.jpeg;
--accept <ids> installs, archives the old image and updates the prompt archives.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, sys
from pathlib import Path
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('r1', HERE / 'regen-figures-scale-the-team-with-ai-20260924.py')
r1 = importlib.util.module_from_spec(spec); sys.modules['r1'] = r1; spec.loader.exec_module(r1)

SUMMARY_PROMPT = ("Create one finished summary illustration explaining the whole post in Owned, a book for product and engineering leaders working with investors. Landscape 16:9. Calm editorial concept map with concrete drawn objects, navy ink, warm ivory background, muted teal and ochre. Use generous empty space, a clear reading order from left to right and large high-contrast labels legible at article width; every label is lettered in large plain capitals and nothing overlaps a label. Left: a single row of exactly ten equal square tiles standing on a bare floor, carrying the numerals 1 to 10, one numeral per tile, in order from left to right and nothing else. Tiles 1, 2, 3, 4, 5, 6 and 7 are filled warm ochre; tiles 8 and 9 are filled muted teal; tile 10 is filled pale teal. Above the row hang exactly three signs, each joined to the tiles by one plain square bracket whose two feet stand exactly on the outer edges of the tiles it covers: the QUEUE sign and bracket cover exactly the seven ochre tiles, from the left edge of tile 1 to the right edge of tile 7; the BUILD sign and bracket cover exactly the two teal tiles 8 and 9; the RELEASE sign and bracket cover only tile 10. Each sign is centred over its own bracket, and the bracket boundaries fall exactly where the tile colours change, never in the middle of a colour. A small robot hand holding a pencil touches only tiles 8 and 9. The three signs and the ten numerals are the only lettering in the left part of the picture. Centre: one clipboard standing upright labeled COMPLETED WORK with plain ticked ruled lines, and beside it, smaller and set aside, a plain counter dial labeled ACTIVITY. Centre-right: one open envelope on a desk and exactly three trays in one row labeled CONDITION, VOTE and BENCHMARK, with the note sliding into the BENCHMARK tray. Right: a simple closed wooden gate with a hanging sign labeled DAY 120, and behind the gate a pinned card labeled SECOND TEAM: CONDITIONS UNCHANGED. Use only the labels explicitly requested; no decorative title, paragraph text, figure number, watermark, photorealism or 3D gradients. Do not invent numbers, dates, research findings or financial claims.")

FIG1_NEW = 'Held at 7 days for this calculation'
FIG3_NEW = 'One 60-day extension, no new seats; then 20% or more continues, less withdraws'

r1.TARGETS = {
    'fig1': dict(asset=r1.IMG / 'one-day-of-ten.jpeg', archive=r1.ILL_ARCHIVE, key='one-day-of-ten', mode='edit',
                 prompt=r1.edit_prompt('Unchanged by faster coding alone', FIG1_NEW),
                 expect=['Ten working days', 'Specialist queue: 7 days', FIG1_NEW, 'Build and test: 2 days', 'A tool can move this day', 'Release: 1 day', 'Halving the build saves one day of ten']),
    'fig3': dict(asset=r1.IMG / 'gate-rules-quality-first.jpeg', archive=r1.ILL_ARCHIVE, key='gate-rules-quality-first', mode='edit',
                 prompt=r1.edit_prompt('One 60-day extension, no new seats', FIG3_NEW),
                 expect=['Gate: day 120', 'Quality and lead time hold?', 'No: tool withdrawn', 'Yes', 'Gain of 20% or more', 'Continue, extend seats', 'Gain above 0%, below 20%', FIG3_NEW, 'Gain of 0% or less', 'Withdraw, record lessons', 'Second team: unchanged']),
    'summary': dict(asset=r1.IMG / 'summary-at-a-glance.jpeg', archive=r1.SUM_ARCHIVE, key='summary-at-a-glance', mode='generate',
                    prompt=SUMMARY_PROMPT,
                    expect=['QUEUE over tiles 1-7 (ochre)', 'BUILD over 8-9 (teal)', 'RELEASE over 10', 'COMPLETED WORK', 'ACTIVITY', 'CONDITION', 'VOTE', 'BENCHMARK', 'DAY 120', 'SECOND TEAM: CONDITIONS UNCHANGED']),
}
PLANK_PROMPT = SUMMARY_PROMPT.replace("Above the row hang exactly three signs, each joined to the tiles by one plain square bracket whose two feet stand exactly on the outer edges of the tiles it covers: the QUEUE sign and bracket cover exactly the seven ochre tiles, from the left edge of tile 1 to the right edge of tile 7; the BUILD sign and bracket cover exactly the two teal tiles 8 and 9; the RELEASE sign and bracket cover only tile 10. Each sign is centred over its own bracket, and the bracket boundaries fall exactly where the tile colours change, never in the middle of a colour.",
    "Directly on top of the row lie exactly three flat wooden planks, each resting on the upper edges of its own tiles and exactly as wide as the tiles it rests on, with a small gap where the tile colours change: the QUEUE plank rests on the seven ochre tiles only, spanning from the left edge of tile 1 to the right edge of tile 7; the BUILD plank rests on the two teal tiles 8 and 9 only; the RELEASE plank rests on the pale tile 10 only. Each plank carries its one word centred. No brackets, no hanging signs, no posts.")
assert PLANK_PROMPT != SUMMARY_PROMPT
r1.TARGETS['summaryB'] = dict(r1.TARGETS['summary'], prompt=PLANK_PROMPT, expect=['QUEUE plank on tiles 1-7 (ochre)', 'BUILD plank on 8-9 (teal)', 'RELEASE plank on 10', 'COMPLETED WORK', 'ACTIVITY', 'CONDITION', 'VOTE', 'BENCHMARK', 'DAY 120', 'SECOND TEAM: CONDITIONS UNCHANGED'])
r1.TARGETS['summaryC'] = dict(r1.TARGETS['summary'])
GAP_PROMPT = SUMMARY_PROMPT.replace("Left: a single row of exactly ten equal square tiles standing on a bare floor, carrying the numerals 1 to 10, one numeral per tile, in order from left to right and nothing else. Tiles 1, 2, 3, 4, 5, 6 and 7 are filled warm ochre; tiles 8 and 9 are filled muted teal; tile 10 is filled pale teal. Above the row hang exactly three signs, each joined to the tiles by one plain square bracket whose two feet stand exactly on the outer edges of the tiles it covers: the QUEUE sign and bracket cover exactly the seven ochre tiles, from the left edge of tile 1 to the right edge of tile 7; the BUILD sign and bracket cover exactly the two teal tiles 8 and 9; the RELEASE sign and bracket cover only tile 10. Each sign is centred over its own bracket, and the bracket boundaries fall exactly where the tile colours change, never in the middle of a colour.",
    "Left: exactly ten equal square tiles standing on a bare floor in one line, carrying the numerals 1 to 10, one numeral per tile, in order from left to right and nothing else, arranged as three separate groups with a clear empty gap of one tile's width between the groups: the first group is the seven ochre tiles numbered 1, 2, 3, 4, 5, 6 and 7 standing edge to edge; then a gap; then the second group, two muted-teal tiles numbered 8 and 9 standing edge to edge; then a gap; then the third group, one pale-teal tile numbered 10 standing alone. Above each group hangs one sign, centred over that group and no wider than it: the sign QUEUE over the seven ochre tiles, the sign BUILD over the two teal tiles, the sign RELEASE over the single pale tile. No brackets, no lines joining signs to tiles, no second row of tiles.")
assert GAP_PROMPT != SUMMARY_PROMPT
r1.TARGETS['summaryD'] = dict(r1.TARGETS['summary'], prompt=GAP_PROMPT, expect=['QUEUE over seven ochre tiles 1-7', 'gap', 'BUILD over teal 8-9', 'gap', 'RELEASE over pale 10', 'COMPLETED WORK', 'ACTIVITY', 'CONDITION', 'VOTE', 'BENCHMARK', 'DAY 120', 'SECOND TEAM: CONDITIONS UNCHANGED'])
r1.TARGETS['summaryE'] = dict(r1.TARGETS['summaryD'])
r1.candidate = lambda tid: Path(f'/tmp/scale-ai-r2-{tid}.jpeg')

def accept(tid: str, note: str) -> None:
    t = r1.TARGETS[tid]
    cand = r1.candidate(tid); assert cand.exists(), f'no candidate for {tid}'
    new = cand.read_bytes(); old = t['asset'].read_bytes()
    old_sha = hashlib.sha256(old).hexdigest(); new_sha = hashlib.sha256(new).hexdigest()
    arch_dir = r1.J / '_research' / ('discarded-summary-variants' if tid.startswith('summary') else 'discarded-illustration-variants')
    arch = arch_dir / f"{r1.POST}-{t['key']}-{old_sha[:12]}.jpeg"
    if not arch.exists(): arch.write_bytes(old)
    t['asset'].write_bytes(new)
    archive = json.loads(t['archive'].read_text())
    hits = []
    for v in (archive.values() if isinstance(archive, dict) else [archive]):
        if isinstance(v, list):
            hits += [e for e in v if isinstance(e, dict) and e.get('post') == r1.POST and e.get('id') == t['key']]
    assert len(hits) == 1, f'archive entry not found for {tid}'
    e = hits[0]
    e['sha256'] = new_sha
    stamp = f"2026-09-24 (in-depth review, round 2): {note}; previous image archived as {arch.name}"
    e['visual_review' if 'visual_review' in e else 'revision'] = stamp
    if tid == 'fig1':
        e['prompt'] = e['prompt'].replace("'Unchanged by faster coding alone'", f"'{FIG1_NEW}'")
        e['alt'] = e['alt'].replace('with a padlock noting that this is unchanged by faster coding alone', 'with a padlock noting that it is held at 7 days for this calculation')
        e['caption'] = ("The forecast trace after the delegation, laid out day by day for a catalogue change. Morgan’s tools reach the two building days. The seven-day queue is the wait for one of the two people who can change the invoicing module safely; it is held at seven days here as an assumption of the calculation, not as a limit of the tool. The pilot’s lead-time measure tests whether it shortens, either because the specialists clear it faster or because a third person passes the same transfer test as the billing engineer. Halving the building stage would bring a change forward by one day in ten.")
        e['visual_goal'] = 'The forecast ten-day trace as ten tiles: seven days of specialist queue held fixed as an assumption, two days of building where a tool can move one day, one day of release.'
    if tid == 'fig3':
        e['prompt'] = e['prompt'].replace("right 'One 60-day extension, no new seats'", f"right '{FIG3_NEW}'")
        e['alt'] = 'Decision ladder. A gate labelled day 120 leads to the question quality and lead time hold? No leads to tool withdrawn. Yes leads to three rungs: gain of 20% or more, continue and extend seats; gain above 0%, below 20%, one 60-day extension with no new seats, then 20% or more continues and less withdraws; gain of 0% or less, withdraw and record lessons. A separate padlocked card reads second team: unchanged.'
        e['caption'] = ("The gate rules as a ladder, judged on day 120 so that every setup has had its thirty days and the last reconciliation exists. Quality and lead time are the first question and the prerequisite for every branch; a pilot whose evidence is missing is treated the same way as one that fails it. Only then is throughput judged, in three bands that do not overlap, with a single extension for the middle band that ends on day 210 in one of the same two outcomes: continue at 20% or more, withdraw at anything less. The card at the side is the point of the section: none of the branches approves, resizes or cancels the second team, which stays on its three conditions for the board.")
    if tid.startswith('summary'):
        e['prompt'] = t['prompt']
    t['archive'].write_text(json.dumps(archive, ensure_ascii=False, indent=2) + '\n')
    print('accepted', tid, '->', t['asset'], new_sha[:16], 'archived', arch.name)

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--generate', nargs='*', default=[])
    ap.add_argument('--accept', nargs='*', default=[])
    ap.add_argument('--note', default='regenerated after round 2 of the in-depth review')
    a = ap.parse_args()
    for tid in a.generate: r1.generate(tid)
    for tid in a.accept: accept(tid, a.note)
