#!/usr/bin/env python3.11
"""Round-5 media driver for 29-ai-worth-its-cost (in-depth review, 24 September 2026).

AIC-018 (comic page 4, strip 3): the 2028 calendar heading "2028: SEVEN LICENCES, €8,600" read as
if €8,600 were the licence cost alone; it becomes "2028: LICENCES + UPKEEP, €8,600" (seven licences
€4,200 plus €4,400 upkeep; the five-word label limit leaves "seven" to the caption and alt text).
Round 4 showed that whole-page Gemini edits drift elsewhere on the page, so --composite pastes only
the heading box of the right-hand calendar block (BOX) from the candidate onto the installed page.

Usage: --generate writes a candidate under /tmp/aic-r5/; --composite limits it to BOX;
--accept installs it and archives the replaced page under _research/discarded-comic-variants/.
Afterwards run the comic generator with --render so comics.md records the new sha256.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, os, sys
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[3]
J = ROOT / '_journals/private-techuity'
POST = '29-ai-worth-its-cost'
ASSET = J / 'posts' / POST / 'assets/images' / POST / 'comic-page-04-a-return-with-a-period.jpeg'
COMICS = J / 'posts' / POST / 'comics.md'
GEN = ROOT / '.claude/skills/explainer-comics/scripts/generate_comic_pages.py'
CAND = Path('/tmp/aic-r5') / ASSET.name
MODEL = 'gemini-3-pro-image-preview'
BOX = (905, 1745, 1318, 1852)  # left, top, right, bottom: heading area of the 2028 block, above its rule

PROMPT = ("Edit the attached comic page. Change ONLY one piece of lettering in the bottom strip. On the wall "
          "calendar, in the right-hand block, replace the two-line heading \"2028: SEVEN LICENCES, €8,600\" with "
          "the two lines \"2028: LICENCES +\" and \"UPKEEP, €8,600\", in the same lettering style, size and "
          "position, inside that same block and above its horizontal rule; keep the line \"DEFERS NOTHING BY "
          "ITSELF\" under the rule unchanged. Keep every other pixel of the page as it is: the same drawings, "
          "people, faces, colors, strips, borders, speech bubbles, labels and all other text and punctuation. "
          "Do not add any new box, card, sign or copy of the new words anywhere else on the page.")


def load_generator():
    sys.path.insert(0, str(GEN.parent))
    spec = importlib.util.spec_from_file_location('comic_pages', GEN)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def generate() -> None:
    gen = load_generator()
    key = os.environ.get('GEMINI_API_KEY', '').strip()
    assert key, 'GEMINI_API_KEY not set'
    CAND.parent.mkdir(parents=True, exist_ok=True)
    data, mime = gen.call_image(key, MODEL, PROMPT, '3:4', ASSET.read_bytes())
    data, _, _ = gen.panels.normalize_image_bytes_for_target(data, mime, ASSET)
    CAND.write_bytes(data)
    print('candidate', CAND, hashlib.sha256(data).hexdigest()[:12])


def composite() -> None:
    from io import BytesIO
    from PIL import Image
    base = Image.open(ASSET).convert('RGB')
    cand = Image.open(CAND).convert('RGB')
    assert base.size == cand.size
    base.paste(cand.crop(BOX), BOX[:2])
    buf = BytesIO()
    base.save(buf, 'JPEG', quality=95)
    CAND.write_bytes(buf.getvalue())
    print('composited box', BOX, hashlib.sha256(buf.getvalue()).hexdigest()[:12])


def accept() -> None:
    assert CAND.exists(), 'no candidate'
    load_generator().archive(ASSET, COMICS, None)
    ASSET.write_bytes(CAND.read_bytes())
    print('accepted', hashlib.sha256(ASSET.read_bytes()).hexdigest()[:16])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--generate', action='store_true')
    ap.add_argument('--composite', action='store_true')
    ap.add_argument('--accept', action='store_true')
    a = ap.parse_args()
    if a.generate:
        generate()
    if a.composite:
        composite()
    if a.accept:
        accept()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
