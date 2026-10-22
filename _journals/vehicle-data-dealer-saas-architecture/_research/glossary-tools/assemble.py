import re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from rows import S, AX, REG

OUT = sys.argv[1]

def links(chs):
    return ", ".join(f"[[{c}]]" for c in chs)

def plain(s):
    return s.replace("*", "").strip()

index = []  # (label, anchor)
body = []
nrows = 0

def table(anchor, rows):
    global nrows
    out = ["| Term | Definition | Chapter |", "| --- | --- | --- |"]
    for term, d, chs, aliases in rows:
        out.append(f"| **{term}** | {d} | {links(chs)} |")
        index.append((term, anchor))
        for a in aliases:
            index.append((a, anchor))
        nrows += 1
    return out

for anchor, title, intro, rows in S:
    body += [f"## <a id=\"{anchor}\"></a>{title}", "", intro, ""] + table(anchor, rows) + [""]

# register terms
anchor, title, intro, rows = REG
body += [f"## <a id=\"{anchor}\"></a>{title}", "", intro, "",
         "| Term | Market | English | Meaning | Chapter |", "| --- | --- | --- | --- | --- |"]
for term, mk, en, meaning, chs in rows:
    body.append(f"| **{term}** | {mk} | {en} | {meaning} | {links(chs)} |")
    index.append((term, anchor))
    nrows += 1
body.append("")

anchor, title, intro, rows = AX
body += [f"## <a id=\"{anchor}\"></a>{title}", "", intro, ""] + table(anchor, rows) + [""]

# alphabetical index
def key(label):
    p = plain(label)
    p = re.sub(r"^(The|the)\s+", "", p)
    p = p.lstrip("§€ ")
    return p.lower()

seen = set()
groups = {}
for label, anc in sorted(index, key=lambda x: key(x[0])):
    if (plain(label).lower(), anc) in seen:
        continue
    seen.add((plain(label).lower(), anc))
    k = key(label)
    letter = k[0].upper() if k[0].isalpha() else "0–9"
    groups.setdefault(letter, []).append(f"[{label}](#{anc})")

order = ["0–9"] + [chr(c) for c in range(65, 91)]
idx = ["## <a id=\"g-index\"></a>Alphabetical Index", ""]
for L in order:
    if L in groups:
        idx.append(f"- **{L}** — " + " · ".join(groups[L]))
idx.append("")

head = open(os.path.join(os.path.dirname(__file__), "head.md")).read()
tail = open(os.path.join(os.path.dirname(__file__), "tail.md")).read()
text = head + "\n".join(body) + "\n".join(idx) + "\n" + tail
words = len(re.sub(r"\[\[[^\]]+\]\]|\(#g-[a-z]+\)", "", text).split())
text = text.replace("__TTR__", str(round(words / 200)))
text = text.replace("__NROWS__", str(nrows))
open(OUT, "w").write(text)
print("rows", nrows, "index entries", sum(len(v) for v in groups.values()), "words", words)
