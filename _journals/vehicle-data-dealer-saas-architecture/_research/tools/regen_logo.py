"""Regenerate one post's header logo with a brand-free prompt suffix.

Usage: python3 regen_logo.py <folder> [extra instruction ...]

Builds the same prompt as _wiring/generate_logos.py (title + excerpt + body
snippet), appends the book's brand rules plus any extra instruction, and
overwrites posts/<folder>/assets/images/<folder>/logo.jpeg. Front matter is
not touched (the logo: line already points at that file).
"""
import os
import pathlib
import sys

REPO = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO / "_wiring"))
import generate_logos as g  # noqa: E402
from build import parse_front_matter  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[2]

SUFFIX = (
    " Brand rules: draw no logos, brand marks or badges, and write no car-maker, model, vendor, portal or "
    "marketplace names anywhere; cars are generic unbranded vehicles; any VIN, plate or identifier shown is an "
    "obviously generic placeholder. Money, if shown, is in euros. Real company names may not appear."
)


def main(folder: str, extra: str) -> None:
    post = ROOT / "posts" / folder / "index.md"
    meta, body = parse_front_matter(post.read_text(encoding="utf-8"))
    prompt = g.build_prompt(meta.get("title", ""), meta.get("excerpt", ""), body) + SUFFIX
    if extra:
        prompt += " " + extra
    out = post.parent / "assets" / "images" / folder / "logo.jpeg"
    out.write_bytes(g.call_gemini_image(os.environ["GEMINI_API_KEY"], prompt))
    print(out)


if __name__ == "__main__":
    main(sys.argv[1], " ".join(sys.argv[2:]))
