#!/usr/bin/env python3.11
"""Round-4 media driver for 30-ai-worth-its-cost (in-depth review, 24 September 2026).

AIC-018 (comic page 4, strip 3): the 2028 calendar block reads "2028: SEVEN LICENCES, €8,600"
and Ines's bubble carries the assistant's cost boundary ("300% on licences and upkeep, 220%
with rollout time"). Two sequential generator --retext passes drifted (a duplicate box, a pink
cast, changed punctuation), so this edit starts from the accepted round-3 page and makes both
changes in one pass. That pass also misspelt two words in strip 1 ("suppiler", "heid"), so
--composite page4 keeps strips 1 and 2 from the accepted round-3 page and takes only strip 3
(rows from the white gutter at y=1590 down) from the candidate; colours match within a few
levels across the join.

AIC-008 (comic page 7, strip 1): Sam's card "TWO FIGURES, TWO PERIODS" becomes two lines,
"FEATURE 90%: APR–SEP 2027" and "ASSISTANT 300%: 2027", and his bubble carries projection,
cost boundaries and the April-to-October deferral.

AIC-020 (Figure 3): rendered by render-figures-30-ai-worth-its-cost-20260924.py with dark
lettering for the Option B and stress-case labels (the amber lines stay).

Usage: --generate page4|page7|fig3 writes a candidate under /tmp/aic-r4/; --composite page4 (see above);
--accept page4|page7|fig3 installs it and archives the replaced image (comic pages under
_research/discarded-comic-variants/, Figure 3 under discarded-illustration-variants/ with
its prompt-archive entry updated). After accepting a comic page, run the comic generator
with --render so comics.md records the new sha256.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, os, subprocess, sys
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[3]
J = ROOT / '_journals/private-techuity'
POST = '30-ai-worth-its-cost'
IMG = J / 'posts' / POST / 'assets/images' / POST
COMICS = J / 'posts' / POST / 'comics.md'
GEN = ROOT / '.claude/skills/explainer-comics/scripts/generate_comic_pages.py'
ARCHIVE_JSON = J / '_research/article-illustration-prompts-20260913.json'
RENDERER = J / '_research/render-figures-30-ai-worth-its-cost-20260924.py'
CAND = Path('/tmp/aic-r4')
MODEL = 'gemini-3-pro-image-preview'

KEEP = ("Keep every other pixel of the page as it is: the same drawings, people, faces, skin tones, colors, "
        "background tint, strips, borders, speech bubbles, labels and all other text and punctuation. "
        "Do not add any new box, card, sign or copy of the new words anywhere else on the page.")

TARGETS = {
    'page4': dict(
        asset='comic-page-04-a-return-with-a-period.jpeg',
        base=J / '_research/discarded-comic-variants/30-ai-worth-its-cost-comic-page-04-a-return-with-a-period-06dc669aba1f.jpeg',
        composite_from_row=1590,
        prompt=("Edit the attached comic page. Change ONLY two pieces of lettering in the bottom strip. "
                "1) On the wall calendar, in the right-hand block, replace the heading \"2028: SAME €8,000 TOOL\" with "
                "\"2028: SEVEN LICENCES, €8,600\", same lettering style and size, on two lines if needed, inside that "
                "same block; keep the line \"DEFERS NOTHING BY ITSELF\" under it. "
                "2) In the speech bubble whose tail points to the older grey-haired woman at the left, replace the words "
                "\"The assistant's 2027 return: 300%, projected, on a hire deferred from April to October.\" with "
                "\"Deferred hire, April to October: 300% on licences and upkeep, 220% with rollout time.\", same lettering, "
                "resizing that bubble only as much as the words need. " + KEEP)),
    'page7': dict(
        asset='comic-page-07-three-questions-three-answers.jpeg',
        base=None,
        prompt=("Edit the attached comic page. Change ONLY two pieces of lettering in the top strip. "
                "1) On the smaller card held by the man in the amber cardigan, replace \"TWO FIGURES, TWO PERIODS\" with two "
                "lines, one under the other: \"FEATURE 90%: APR–SEP 2027\" and \"ASSISTANT 300%: 2027\", in the same bold "
                "lettering, widening that card only as much as the lines need; every character fully visible, not covered by his hands. "
                "2) In his speech bubble, replace \"Feature 90% before staff costs; assistant 300%, hire deferred, quality holding. "
                "Both projections.\" with \"Projected, quality holding. Feature before staff costs; assistant before rollout time, "
                "hire deferred April–October.\", same lettering, resizing that bubble only as much as the words need. " + KEEP)),
}


def load_generator():
    sys.path.insert(0, str(GEN.parent))
    spec = importlib.util.spec_from_file_location('comic_pages', GEN)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def candidate(tid: str) -> Path:
    return CAND / (TARGETS[tid]['asset'] if tid in TARGETS else 'commitment-floor-against-demand-range.jpeg')


def generate(tid: str) -> None:
    CAND.mkdir(parents=True, exist_ok=True)
    if tid == 'fig3':
        subprocess.run([sys.executable, str(RENDERER), '--out-dir', str(CAND)], check=True)
        return
    gen = load_generator()
    t = TARGETS[tid]
    asset = IMG / t['asset']
    base = (t['base'] or asset).read_bytes()
    key = os.environ.get('GEMINI_API_KEY', '').strip()
    assert key, 'GEMINI_API_KEY not set'
    data, mime = gen.call_image(key, MODEL, t['prompt'], '3:4', base)
    data, _, _ = gen.panels.normalize_image_bytes_for_target(data, mime, asset)
    candidate(tid).write_bytes(data)
    print('candidate', tid, candidate(tid), hashlib.sha256(data).hexdigest()[:12])


def composite(tid: str) -> None:
    from io import BytesIO
    from PIL import Image
    t = TARGETS[tid]
    base = Image.open(t['base']).convert('RGB')
    cand = Image.open(candidate(tid)).convert('RGB')
    assert base.size == cand.size
    cut = t['composite_from_row']
    base.paste(cand.crop((0, cut, cand.width, cand.height)), (0, cut))
    buf = BytesIO()
    base.save(buf, 'JPEG', quality=95)
    candidate(tid).write_bytes(buf.getvalue())
    print('composited', tid, 'rows >=', cut, hashlib.sha256(buf.getvalue()).hexdigest()[:12])


def accept(tid: str) -> None:
    cand = candidate(tid)
    assert cand.exists(), f'no candidate for {tid}'
    if tid == 'fig3':
        asset = IMG / 'commitment-floor-against-demand-range.jpeg'
        old, new = asset.read_bytes(), cand.read_bytes()
        old_sha, new_sha = hashlib.sha256(old).hexdigest(), hashlib.sha256(new).hexdigest()
        arch = J / '_research/discarded-illustration-variants' / f'{POST}-commitment-floor-against-demand-range-{old_sha[:12]}.jpeg'
        if not arch.exists():
            arch.write_bytes(old)
        asset.write_bytes(new)
        archive = json.loads(ARCHIVE_JSON.read_text())
        hits = [e for e in archive['figures'] if e.get('post') == POST and e.get('id') == 'commitment-floor-against-demand-range']
        assert len(hits) == 1
        e = hits[0]
        e['sha256'] = new_sha
        e['visual_review'] = ('2026-09-24 (in-depth review round 4): AIC-020: Option B and stress-case labels lettered in dark ink '
                              '(amber kept for the lines), floor labels enlarged to 40 px for narrow screens; inspected at native '
                              f'size and 358 px wide; previous image archived as {arch.name}')
        ARCHIVE_JSON.write_text(json.dumps(archive, ensure_ascii=False, indent=2) + '\n')
        print('accepted fig3', new_sha[:16], 'archived', arch.name)
        return
    gen = load_generator()
    asset = IMG / TARGETS[tid]['asset']
    gen.archive(asset, COMICS, None)
    asset.write_bytes(cand.read_bytes())
    print('accepted', tid, hashlib.sha256(asset.read_bytes()).hexdigest()[:16])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--generate', nargs='*', default=[])
    ap.add_argument('--composite', nargs='*', default=[])
    ap.add_argument('--accept', nargs='*', default=[])
    a = ap.parse_args()
    for tid in a.generate:
        generate(tid)
    for tid in a.composite:
        composite(tid)
    for tid in a.accept:
        accept(tid)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
