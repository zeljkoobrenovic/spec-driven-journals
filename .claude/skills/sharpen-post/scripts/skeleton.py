#!/usr/bin/env python3
"""Print a post's skeleton: headings, plus the first sentence of every paragraph.

Usage:
    python3 skeleton.py <file.md>             # headings + first sentences
    python3 skeleton.py <file.md> --headings  # headings only
    python3 skeleton.py <file.md> --stats     # word, paragraph and heading counts

Front matter, fenced blocks (``` and ---begin x--- / ---end x---), tables, images,
HTML-only lines and <br> are skipped. Blockquotes and list items are shown with a
marker so the reader can see them, but they are not treated as prose paragraphs.
"""

import re
import sys

SENTENCE_END = re.compile(r"(?<=[.!?])[\"')\]*_]*\s+(?=[A-Z\[*\"'(`0-9])")


def body_lines(text):
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                lines = lines[i + 1:]
                break
    out, fence = [], None
    for line in lines:
        s = line.strip()
        if fence:
            if s == fence or (fence == "```" and s.startswith("```")):
                fence = None
            continue
        if s.startswith("```"):
            fence = "```"
            continue
        m = re.match(r"^---begin ([\w-]+)---$", s)
        if m:
            fence = f"---end {m.group(1)}---"
            continue
        out.append(line)
    return out


def blocks(lines):
    """Group lines into blocks separated by blank lines or <br>."""
    block = []
    for line in lines:
        s = line.strip()
        if not s or s.lower() in ("<br>", "<br/>", "<br />"):
            if block:
                yield block
                block = []
            continue
        if s.startswith("#"):
            if block:
                yield block
                block = []
            yield [line]
            continue
        block.append(line)
    if block:
        yield block


def first_sentence(text):
    text = re.sub(r"\s+", " ", text).strip()
    parts = SENTENCE_END.split(text, maxsplit=1)
    return parts[0]


def classify(block):
    first = block[0].strip()
    if first.startswith("#"):
        return "heading"
    if first.startswith("|"):
        return "table"
    if first.startswith(">"):
        return "quote"
    if re.match(r"^([-*+]|\d+[.)])\s", first):
        return "list"
    if first.startswith("!["):
        return "image"
    if first.startswith("<") and not re.search(r"[A-Za-z]{3,}\s+[A-Za-z]{3,}", re.sub(r"<[^>]+>", "", first)):
        return "html"
    if re.match(r"^\*\*Figure\s+\d+", first):
        return "caption"
    return "para"


def words(text):
    return len(re.findall(r"[A-Za-z0-9€$£%'’-]+", text))


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    path, mode = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else "")
    lines = body_lines(open(path, encoding="utf-8").read())
    all_blocks = list(blocks(lines))

    if mode == "--stats":
        paras = [b for b in all_blocks if classify(b) == "para"]
        heads = [b for b in all_blocks if classify(b) == "heading"]
        prose = sum(words(" ".join(b)) for b in all_blocks if classify(b) in ("para", "list", "quote"))
        print(f"headings={len(heads)} paragraphs={len(paras)} prose_words={prose}")
        return

    n = 0
    for b in all_blocks:
        kind = classify(b)
        if kind == "heading":
            level = len(b[0].strip()) - len(b[0].strip().lstrip("#"))
            print(("" if level <= 2 else "  " * (level - 2)) + b[0].strip())
        elif mode == "--headings":
            continue
        elif kind == "para":
            n += 1
            print(f"    P{n}: {first_sentence(' '.join(b))}")
        elif kind in ("list", "quote"):
            print(f"    [{kind}] {first_sentence(re.sub(r'^[>*+-]+|^\d+[.)]', '', b[0].strip()).strip())[:120]}")
        elif kind == "caption":
            print(f"    [figure] {first_sentence(' '.join(b))[:120]}")


if __name__ == "__main__":
    main()
