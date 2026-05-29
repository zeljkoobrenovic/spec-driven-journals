#!/usr/bin/env python3
"""Extract illustration-placeholder JSON blocks from a journal post.

The script validates required fields and emits machine-readable records that a
future image-generation script can use to call Gemini and write images to the
expected per-post assets directory.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

START = "<!-- illustration-placeholder"
END = "-->"
REQUIRED = {
    "id",
    "status",
    "asset",
    "aspect_ratio",
    "placement",
    "visual_goal",
    "prompt",
    "alt",
    "caption",
}


def post_slug(path: Path) -> str:
    if path.name in {"index.md", "index.markdown"}:
        return path.parent.name
    return path.stem


def source_image_path(post_path: Path, asset: str) -> Path:
    slug = post_slug(post_path)
    expected_prefix = f"assets/images/{slug}/"
    if not asset.startswith(expected_prefix):
        raise ValueError(
            f"asset must start with {expected_prefix!r}; got {asset!r}"
        )
    if post_path.name in {"index.md", "index.markdown"}:
        return post_path.parent / "assets" / "images" / slug / Path(asset).name
    journal_dir = post_path.parents[2]
    return journal_dir / "assets" / "images" / slug / Path(asset).name


def replacement_text(item: dict, figure_number: int) -> str:
    return (
        f"![{item['alt']}]({item['asset']})\n"
        f"**Figure {figure_number}:** *{item['caption']}*"
    )


def extract(text: str) -> list[tuple[int, int, str]]:
    pattern = re.compile(
        re.escape(START) + r"\s*(\{.*?\})\s*" + re.escape(END),
        re.DOTALL,
    )
    return [(m.start(), m.end(), m.group(1)) for m in pattern.finditer(text)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("post", type=Path)
    parser.add_argument(
        "--start-figure",
        type=int,
        default=1,
        help="Figure number to use for the first placeholder replacement.",
    )
    args = parser.parse_args()

    post = args.post
    text = post.read_text(encoding="utf-8")
    records = []
    for index, (start, end, raw_json) in enumerate(extract(text), start=1):
        try:
            item = json.loads(raw_json)
        except json.JSONDecodeError as exc:
            print(f"Invalid JSON in placeholder {index}: {exc}", file=sys.stderr)
            return 2
        missing = sorted(REQUIRED - set(item))
        if missing:
            print(
                f"Placeholder {index} missing required fields: {', '.join(missing)}",
                file=sys.stderr,
            )
            return 2
        try:
            image_path = source_image_path(post, item["asset"])
        except ValueError as exc:
            print(f"Placeholder {index}: {exc}", file=sys.stderr)
            return 2
        figure_number = args.start_figure + index - 1
        records.append(
            {
                "placeholder_index": index,
                "start": start,
                "end": end,
                "post": str(post),
                "id": item["id"],
                "status": item["status"],
                "asset": item["asset"],
                "source_image_path": str(image_path),
                "aspect_ratio": item["aspect_ratio"],
                "placement": item["placement"],
                "visual_goal": item["visual_goal"],
                "prompt": item["prompt"],
                "alt": item["alt"],
                "caption": item["caption"],
                "replacement_markdown": replacement_text(item, figure_number),
            }
        )

    print(json.dumps(records, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
