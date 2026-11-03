"""List owned terms per chapter from PLAN.md: folder, permalink, term."""
import re, sys, pathlib
root = pathlib.Path(__file__).resolve().parents[2]
plan = (root / "PLAN.md").read_text()
for m in re.finditer(r"\*\*(\d\d-[a-z0-9-]+) → `([a-z0-9-]+)`\*\*.*?Owns: (.*?)\. (?:Sources|Briefs)", plan):
    folder, perm, owns = m.groups()
    for t in re.split(r",\s*(?![^()]*\))", owns):
        print(f"{folder}\t{perm}\t{t.strip()}")
