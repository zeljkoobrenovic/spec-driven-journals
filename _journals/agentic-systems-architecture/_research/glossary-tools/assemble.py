"""Assemble posts/glossary/index.md from head.md, terms.py and tail.md.

Rows are sorted alphabetically (ignoring a leading "The " and punctuation),
grouped by first letter, each group a | Term | Definition | Chapter | table,
with a letter jump list at the top. Run: python3 assemble.py
"""
import collections, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
from terms import T  # noqa: E402

def key(term):
    t = re.sub(r"^The ", "", term)
    t = re.sub(r"[^0-9A-Za-z ]", "", t).lower()
    return t

def display(term):
    # "Agent Committee, The" -> "The Agent Committee"
    m = re.match(r"^(.*), The(.*)$", term)
    return f"The {m.group(1)}{m.group(2)}" if m else term

LABEL = {"F": " *(failure pattern)*", "O": " *(Ostrell, fictional)*", "E": "", "A": "", "T": ""}

rows = sorted(T, key=lambda r: key(r[0]))
groups = collections.OrderedDict()
for r in rows:
    letter = key(r[0])[0].upper()
    groups.setdefault(letter, []).append(r)

out = []
jump = " · ".join(f"[{L}](#g-{L.lower()})" for L in groups)
out.append(f"**Jump to:** {jump}\n")
for L, rs in groups.items():
    out.append(f"## <a id=\"g-{L.lower()}\"></a>{L}\n")
    out.append("| Term | Definition | Chapter |")
    out.append("| --- | --- | --- |")
    for term, definition, owner, see, kind in rs:
        name = display(term).replace(" (failure pattern)", "")
        cell = f"[[{owner}]]"
        if see:
            cell += "<br>See also " + ", ".join(f"[[{s}]]" for s in see)
        definition = definition.replace("|", "\\|")
        out.append(f"| **{name}**{LABEL[kind]} | {definition} | {cell} |")
    out.append("")

body = "\n".join(out)
head = (HERE / "head.md").read_text().replace("__COUNT__", str(len(rows)))
tail = (HERE / "tail.md").read_text()
dest = ROOT / "posts/glossary/index.md"
dest.parent.mkdir(exist_ok=True)
dest.write_text(head.rstrip() + "\n\n" + body + "\n" + tail)
counts = collections.Counter(r[4] for r in rows)
print(f"{len(rows)} rows -> {dest}  {dict(counts)}")
