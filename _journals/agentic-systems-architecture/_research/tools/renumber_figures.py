"""Renumber all **Figure N:** captions in an index.md in document order and
update in-text references ("Figure 3", "Figures 2 and 4", "Figures 2–3") to match.

Illustrations are generated with --start-figure 101 so their temporary numbers
never collide with the existing (mermaid) figures; this script then makes the
whole sequence consecutive. Only numbers that belonged to captions are remapped.

Usage: python3 renumber_figures.py <index.md> [<index.md> ...] [--check]
"""
import re
import sys

CAPTION = re.compile(r"^(\*\*Figure )(\d+)(:\*\*)", re.M)
REF = re.compile(r"\b(Figures?)(\s+)(\d+(?:\s*(?:,|and|&|–|-|to)\s*\d+)*)")
FENCE = re.compile(r"^(```|---begin mermaid---|---end mermaid---)", re.M)


def renumber(text: str) -> tuple[str, dict]:
    old_numbers = [int(m.group(2)) for m in CAPTION.finditer(text)]
    mapping, seen = {}, set()
    for new, old in enumerate(old_numbers, start=1):
        if old in seen:
            raise ValueError(f"duplicate caption number {old}")
        seen.add(old)
        mapping[old] = new
    counter = iter(range(1, len(old_numbers) + 1))
    text = CAPTION.sub(lambda m: f"{m.group(1)}{next(counter)}{m.group(3)}", text)

    def fix_ref(m):
        nums = re.sub(r"\d+", lambda n: str(mapping.get(int(n.group()), int(n.group()))), m.group(3))
        return f"{m.group(1)}{m.group(2)}{nums}"

    # Rewrite references outside caption lines, outside code/mermaid blocks.
    out, inside = [], False
    for line in text.split("\n"):
        if FENCE.match(line):
            inside = not inside if line.startswith("```") else line.startswith("---begin")
            out.append(line)
            continue
        if inside or CAPTION.match(line):
            out.append(line)
        else:
            out.append(REF.sub(fix_ref, line))
    return "\n".join(out), mapping


if __name__ == "__main__":
    check = "--check" in sys.argv
    for path in [a for a in sys.argv[1:] if a != "--check"]:
        src = open(path, encoding="utf-8").read()
        new, mapping = renumber(src)
        changed = {o: n for o, n in mapping.items() if o != n}
        print(f"{path}: {len(mapping)} figures, remapped {changed}")
        if not check and new != src:
            open(path, "w", encoding="utf-8").write(new)
