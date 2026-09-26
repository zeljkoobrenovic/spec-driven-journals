#!/usr/bin/env python3
"""Round 4 of the in-depth review of 24-scale-the-team-with-ai (24 Sept 2026).

SAI-018: Figure 3's top rung said 'Continue, extend seats' and the extension rung promised continuation at 20%,
although a qualifying gain is only eligible to continue if the added review hours are funded. Both results are
re-lettered on the existing image (lettering edit, artwork kept).

Reuses the round-1 script's helpers. Usage: --generate fig3 writes /tmp/scale-ai-r4-fig3.jpeg;
--accept fig3 installs it, archives the old image and updates the prompt archive.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, sys
from pathlib import Path
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('r1', HERE / 'regen-figures-scale-the-team-with-ai-20260924.py')
r1 = importlib.util.module_from_spec(spec); sys.modules['r1'] = r1; spec.loader.exec_module(r1)

TOP_OLD = 'Continue, extend seats'
TOP_NEW = 'Eligible only if review hours funded; if not, withdraw'
MID_OLD = 'One 60-day extension, no new seats; then 20% or more continues, less withdraws'
MID_NEW = 'One 60-day extension, no new seats; then 20% or more as above, less withdraws'

PROMPT = ("Edit the attached illustration. Change ONLY two pieces of lettering, both in the right half of the rungs of the ladder. "
          f'First, in the top teal rung, replace the exact words "{TOP_OLD}" with the exact words "{TOP_NEW}". '
          f'Second, in the middle ochre rung, replace the exact words "{MID_OLD.replace("; ", "; ")}" with the exact words "{MID_NEW}". '
          "Use the same lettering style, size and color, on as many lines as the new words need, and keep every word inside its own rung, clear of the rung's edges and of the left-hand label. "
          "Keep every other pixel of the picture as it is: the gate, the diamond, the arrows, the 'No: tool withdrawn' panel, the 'Yes' label, the bottom rung, the padlocked card and all other text. Add nothing else: no icons, coins or currency signs.")

EXPECT = ['Gate: day 120', 'Quality and lead time hold?', 'No: tool withdrawn', 'Yes', 'Gain of 20% or more', TOP_NEW,
          'Gain above 0%, below 20%', MID_NEW, 'Gain of 0% or less', 'Withdraw, record lessons', 'Second team: unchanged']

r1.TARGETS = {'fig3': dict(asset=r1.IMG / 'gate-rules-quality-first.jpeg', archive=r1.ILL_ARCHIVE, key='gate-rules-quality-first',
                           mode='edit', prompt=PROMPT, expect=EXPECT)}
r1.candidate = lambda tid: Path(f'/tmp/scale-ai-r4-{tid}.jpeg')

ALT = ('Decision ladder. A gate labelled day 120 leads to the question quality and lead time hold? No leads to tool withdrawn. '
       'Yes leads to three rungs: gain of 20% or more, eligible only if review hours are funded, and withdrawn if not; '
       'gain above 0%, below 20%, one 60-day extension with no new seats, then 20% or more is treated as the top rung and less withdraws; '
       'gain of 0% or less, withdraw and record lessons. A separate padlocked card reads second team: unchanged.')
CAPTION = ('The gate rules as a ladder, judged on day 120 so that every setup has had its thirty days and the last reconciliation exists. '
           'Quality and lead time are the first question and the prerequisite for every branch; a pilot whose evidence is missing is treated the same way as one that fails it. '
           'Only then is throughput judged, in three bands that do not overlap. A gain of 20% or more makes the tool eligible, not certain, to continue: '
           'it continues, and seats may be extended, only if Ines funds the added review hours by naming the work they displace, and otherwise it is withdrawn. '
           'The middle band gets a single extension that ends on day 210, where 20% or more meets the same review test and anything less withdraws. '
           'The card at the side is the point of the section: none of the branches approves, resizes or cancels the second team, which stays on its three conditions for the board.')


def accept(note: str) -> None:
    t = r1.TARGETS['fig3']
    cand = r1.candidate('fig3'); assert cand.exists(), 'no candidate'
    new = cand.read_bytes(); old = t['asset'].read_bytes()
    old_sha = hashlib.sha256(old).hexdigest(); new_sha = hashlib.sha256(new).hexdigest()
    arch = r1.J / '_research' / 'discarded-illustration-variants' / f"{r1.POST}-{t['key']}-{old_sha[:12]}.jpeg"
    if not arch.exists(): arch.write_bytes(old)
    t['asset'].write_bytes(new)
    archive = json.loads(t['archive'].read_text())
    hits = []
    for v in (archive.values() if isinstance(archive, dict) else [archive]):
        if isinstance(v, list):
            hits += [e for e in v if isinstance(e, dict) and e.get('post') == r1.POST and e.get('id') == t['key']]
    assert len(hits) == 1, 'archive entry not found'
    e = hits[0]
    assert f"'{TOP_OLD}'" in e['prompt'], 'top-rung wording not found in archived prompt'
    e['prompt'] = e['prompt'].replace(f"'{TOP_OLD}'", f"'{TOP_NEW}'")
    e['prompt'] = e['prompt'].replace("then 20% or more continues, less withdraws", "then 20% or more as above, less withdraws")
    e['alt'] = ALT
    e['caption'] = CAPTION
    e['sha256'] = new_sha
    e['visual_review'] = (e.get('visual_review', '') + f" 2026-09-24 (in-depth review, round 4): {note}; previous image archived as {arch.name}").strip()
    t['archive'].write_text(json.dumps(archive, ensure_ascii=False, indent=2) + '\n')
    print('accepted fig3 ->', t['asset'], new_sha[:16], 'archived', arch.name)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--generate', action='store_true')
    ap.add_argument('--accept', action='store_true')
    ap.add_argument('--note', default='top and middle rung results re-lettered as conditional on funded review (SAI-018)')
    a = ap.parse_args()
    if a.generate: r1.generate('fig3')
    if a.accept: accept(a.note)
