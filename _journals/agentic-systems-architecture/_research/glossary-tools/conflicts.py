"""Find definitional sentences ('**term** is/means') for owned terms in chapters other than the owner."""
import re, pathlib
root = pathlib.Path(__file__).resolve().parents[2]
rows = [l.rstrip("\n").split("\t") for l in open(root/"_research/glossary-tools/owns.tsv")]
chap = {p.parent.name: p.read_text() for p in sorted((root/"posts").glob("[0-9][0-9]-*/index.md"))}
for folder, perm, term in rows:
    base = re.sub(r"\s*\(.*?\)", "", term).strip()
    pat = re.compile(r"\*\*" + re.escape(base) + r"(?: \([^)]*\))?\*\*(?: \([A-Za-z]+\))? (?:is|means|are)\b[^.]*\.", re.I)
    for name, text in chap.items():
        if name == folder: continue
        for m in pat.finditer(text):
            print(f"{term} [{perm}] in {name}: {m.group(0)[:300]}")
