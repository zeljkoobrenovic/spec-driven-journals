"""For each owned term, print the first lines in the owning chapter that bold it (or mention it)."""
import re, sys, pathlib
root = pathlib.Path(__file__).resolve().parents[2]
rows = [l.rstrip("\n").split("\t") for l in open(root/"_research/glossary-tools/owns.tsv")]
only = sys.argv[1:]  # optional folder prefixes
for folder, perm, term in rows:
    if only and not any(folder.startswith(o) for o in only):
        continue
    base = re.sub(r"\s*\(.*?\)", "", term).strip()
    variants = [base] + base.split(" vs ")
    text = (root/"posts"/folder/"index.md").read_text()
    lines = text.split("\n")
    hits = []
    for v in variants:
        pat = re.compile(r"\*\*[^*]{0,40}" + re.escape(v).replace("\\ ", "[ -]") + r"[^*]{0,40}\*\*", re.I)
        for i, l in enumerate(lines):
            if pat.search(l) and i not in hits and not re.search(r"\bowns?\b|^> ", l):
                hits.append(i)
    print(f"=== {term}  [{perm}]")
    for i in hits[:2]:
        l = lines[i]
        m = re.search(re.escape(base).replace("\\ ", "[ -]"), l, re.I)
        s = max(0, (m.start() if m else 0) - 150)
        print("   ", l[s:s+420])
    if not hits:
        print("    (no bold hit)")
