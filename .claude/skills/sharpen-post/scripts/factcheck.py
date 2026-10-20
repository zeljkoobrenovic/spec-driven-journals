#!/usr/bin/env python3
"""Check that a sharpening pass lost no facts: compare a post with a git revision.

Usage:
    python3 factcheck.py <file.md>              # compare with HEAD
    python3 factcheck.py <file.md> --base REF   # compare with another revision

Counts, in the old and new text: numbers and dates, number words ("three",
"dozen"), [[cross-links]], URLs, inference labels, quoted passages, callout
labels and figure captions. Prints every item whose count fell, flags any
number word that changed in a heading ("four stages" -> "five stages"), and
checks that figure captions still run 1, 2, 3... For a lost number word it
prints the old sentences that held it and the closest new sentence, so a
rewording can be told from a lost fact. When sections were moved, renamed or
deleted, it lists positional pointers ("the final section", "below") in this
post and in other posts of the journal that link to it, since those may now
point at the wrong place.
Exit status 1 when something was lost, so a removal is never silent: either
restore it or name it in the report as a deliberate cut.
"""

import difflib
import os
import re
import subprocess
import sys
from collections import Counter

CHECKS = {
    "number or date": re.compile(r"(?<![\w-])[€$£]?\d[\d,.]*\d%?|(?<![\w-])[€$£]?\d%?(?![\w])"),
    "cross-link": re.compile(r"\[\[[^\]]+\]\]"),
    "url": re.compile(r"\((https?://[^)\s]+)\)|<(https?://[^>\s]+)>"),
    "evidence label": re.compile(r"INFERENCE, NOT DOCUMENTED|[Mm]y reading"),
    "callout label": re.compile(r"^>\s*\*\*\[?([A-Z][A-Z ,'’-]{3,}[A-Z])", re.M),
    # Every quote is paired; only passages of 12+ characters are reported.
    "quoted passage": re.compile(r"\"([^\"\n]*)\"|“([^”\n]*)”"),
}
FIGURE = re.compile(r"^\*\*Figure (\d+):?\*\*", re.M)
NUMBER_WORDS = ("one two three four five six seven eight nine ten eleven twelve thirteen fourteen "
                "fifteen sixteen seventeen eighteen nineteen twenty thirty forty fifty sixty seventy "
                "eighty ninety hundred thousand million billion dozen half single double triple twice "
                "first second third fourth fifth sixth seventh eighth ninth tenth").split()
NUMBER_WORD = re.compile(r"\b(" + "|".join(NUMBER_WORDS) + r")\b", re.I)
# Too common in prose to count there; still compared inside headings.
PROSE_SKIP = {"one", "half", "single", "double", "first", "second"}
HEADING = re.compile(r"^#{1,6} .*$", re.M)
POSITIONAL = re.compile(r"\b(final|last|closing|next|previous|preceding|following|earlier|later|"
                        r"opening|first|second|third) (section|part)s?\b|\bnear the (end|start)\b|"
                        r"\b(see |as )?(above|below)\b", re.I)
SENTENCE = re.compile(r"(?<=[.!?])\s+(?=[A-Z*\[(“\"])")


def strip_front_matter(text):
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            return text[end + 4:]
    return text


def sentences(text):
    return [x.strip() for para in text.split("\n\n") for x in SENTENCE.split(" ".join(para.split())) if x.strip()]


def word_context(word, old, new):
    """Old sentences holding `word` that are gone, each with its closest new sentence."""
    pattern = re.compile(rf"\b{word}\b", re.I)
    old_s, new_s = sentences(HEADING.sub("", old)), sentences(HEADING.sub("", new))
    kept = set(new_s)
    for sent in old_s:
        if pattern.search(sent) and sent not in kept:
            m = pattern.search(sent)
            start = max(0, m.start() - 110)  # long sentences: show the text around the word
            print(f"    was: {sent[start:start + 220]}")
            near = difflib.get_close_matches(sent, new_s, n=1, cutoff=0.4)
            print(f"    now: {near[0][start:start + 220]}" if near else "    now: (no similar sentence)")


def permalink_of(text):
    m = re.search(r"^permalink:\s*(\S+)", text, re.M)
    return m.group(1) if m else None


def pointers(path, permalink):
    """Lines with positional pointers in this post and in sibling posts that link to it."""
    posts_dir = os.path.dirname(os.path.dirname(os.path.abspath(path)))
    hits = []
    for root, _, files in os.walk(posts_dir):
        for name in files:
            if not name.endswith(".md") or name == "spec.md":
                continue
            f = os.path.join(root, name)
            own = os.path.samefile(f, path)
            for n, line in enumerate(open(f, encoding="utf-8"), 1):
                if line.startswith("#") or not POSITIONAL.search(line):
                    continue
                if own or (permalink and (f"[[{permalink}]]" in line or f"{permalink}.html" in line)):
                    hits.append(f"{os.path.relpath(f)}:{n}: {line.strip()[:200]}")
    return hits


def tokens(kind, text):
    out = []
    for m in CHECKS[kind].finditer(text):
        groups = [g for g in m.groups() if g] if m.groups() else []
        token = groups[0] if groups else m.group(0)
        if kind == "quoted passage" and len(token) < 12:
            continue
        out.append(token.rstrip(".,") if kind == "number or date" else token)
    return Counter(out)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    path = sys.argv[1]
    base = sys.argv[sys.argv.index("--base") + 1] if "--base" in sys.argv else "HEAD"
    try:
        old = subprocess.run(["git", "show", f"{base}:./{path}"], capture_output=True,
                             text=True, check=True).stdout
    except subprocess.CalledProcessError:
        old = subprocess.run(["git", "show", f"{base}:{path}"], capture_output=True,
                             text=True, check=True).stdout
    new = open(path, encoding="utf-8").read()
    permalink = permalink_of(new)
    old, new = strip_front_matter(old), strip_front_matter(new)

    lost = 0
    for kind in CHECKS:
        before, after = tokens(kind, old), tokens(kind, new)
        for token, n in sorted(before.items()):
            if after[token] < n:
                lost += 1
                print(f"LOST {kind}: {token!r} ({n} -> {after[token]})")

    # Number words in prose: a fall in count is reported like a lost number.
    def prose_words(text):
        body = HEADING.sub("", text)
        return Counter(w.lower() for w in NUMBER_WORD.findall(body) if w.lower() not in PROSE_SKIP)
    before, after = prose_words(old), prose_words(new)
    for word, n in sorted(before.items()):
        if after[word] < n:
            lost += 1
            print(f"LOST number word: {word!r} ({n} -> {after[word]})")
            word_context(word, old, new)

    # Number words in headings: any change is flagged, because a heading that
    # says "four" where the section lists five is a factual claim.
    def heading_words(text):
        return Counter(w.lower() for h in HEADING.findall(text) for w in NUMBER_WORD.findall(h))
    hb, ha = heading_words(old), heading_words(new)
    for word in sorted(set(hb) | set(ha)):
        if hb[word] != ha[word]:
            lost += 1
            print(f"CHANGED heading number word: {word!r} ({hb[word]} -> {ha[word]}); confirm the section still says so")

    figures = [int(n) for n in FIGURE.findall(new)]
    if figures != list(range(1, len(figures) + 1)):
        lost += 1
        print(f"FIGURES out of sequence: {figures}")
    old_figures = len(FIGURE.findall(old))
    if len(figures) != old_figures:
        print(f"NOTE figures {old_figures} -> {len(figures)}; check every 'Figure N' reference")

    # Moved, renamed or deleted sections can strand pointers by position.
    old_h, new_h = HEADING.findall(old), HEADING.findall(new)
    if old_h != new_h:
        hits = pointers(path, permalink)
        for hit in hits:
            print(f"POINTER {hit}")
        if hits:
            lost += 1
            print("POINTER: the outline changed; confirm each pointer above still names the right place, or report it.")

    if lost:
        print(f"{lost} item(s) lost or changed compared with {base}: restore each, or name it in the report as a deliberate cut or a checked correction.")
        sys.exit(1)
    print(f"OK: no numbers, dates, links, URLs, labels, quotes or figures lost compared with {base}.")


if __name__ == "__main__":
    main()
