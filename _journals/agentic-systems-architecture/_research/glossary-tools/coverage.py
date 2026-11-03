"""Check every owned term in owns.tsv has a glossary row (by normalized prefix match)."""
import re, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from terms import T
names = [re.sub(r"[^a-z0-9 ^@]", "", t[0].lower()) for t in T]
alias = {"runtime (agent)": "agent runtime", "resume vs replay": "resume", "budget (step/cost/time)": "budget",
         "mcp (book use)": "mcp", "system of record (agent context)": "system of record",
         "policy enforcement point (brief; deep in 30)": "policy enforcement point",
         "evidence log (brief; deep in 30)": "evidence log", "version pinning (brief; deep in 38)": "version pinning",
         "agent registry (lifecycle)": "agent registry"}
miss = 0
for line in open(HERE / "owns.tsv"):
    folder, perm, term = line.rstrip("\n").split("\t")
    t = alias.get(term.lower(), term.lower())
    t = re.sub(r"[^a-z0-9 ^@]", "", re.sub(r"\s*\((agent|agent run|agent action|run|a2a|agentic)\)", "", t))
    if not any(n.startswith(t) for n in names):
        print("MISSING", term, perm); miss += 1
print("missing:", miss)
