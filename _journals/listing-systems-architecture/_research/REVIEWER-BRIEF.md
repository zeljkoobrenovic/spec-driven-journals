# Reviewer Brief — LISTED editorial pass

You are the senior editor for **LISTED: Architecting Large-Scale Classifieds and Marketplace Platforms** (ROOT = `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/listing-systems-architecture/`). The user's priority is **quality**. Pages were written in parallel by different writers; your job is to make your assigned pages correct, consistent with the rest of the book, and compliant with the house style — with **minimal, surgical edits**. Do not rewrite pages, change their arguments, or shorten them wholesale.

## Read first

1. `ROOT/_research/style-guide.md` (format, failure-pattern names, evidence discipline, mermaid rules, valid permalinks).
2. `ROOT/_research/consistency-issues.md` — every numbered item; fix those that touch your pages. Canonical decisions recorded there win.
3. `ROOT/_research/scenario-ledger.md` — canonical Veldmark facts, including all "Additions by chapter" and every `[editor]` line (editor lines win over chapter lines; where two chapter lines conflict and no editor line exists, prefer the chapter that *owns* the topic per PLAN and record your resolution in your review log).
4. `ROOT/PLAN.md` — contracts and reading order.

## For each assigned page, check and fix

1. **Format.** Front matter complete (title, date, author, excerpt, permalink, timetoread — ~230 words/min of prose; correct if far off). Callouts in order with exact labels: IN THIS CHAPTER, YOU WILL / WHY THE BUSINESS CARES / WHY ARCHITECTS SHOULD CARE / KEY POINTS (exactly 3) / FAILURE PATTERNS THIS CHAPTER ADDRESSES (link `where-listing-systems-go-wrong.html`, 2–3 patterns, **exact names**). `<br>` after the callouts. A Chief Architect's view, Questions to ask, Sources and Evidence, and a closing hand-off to the **next page in config.yaml order** (fix wrong hand-offs; the last chapter of a part hands off to the next part's intro).
2. **Veldmark consistency.** Every figure, date, name, system and decision agrees with the ledger and with the owning chapter. Grep for the recurring examples (Rotterdam bike, Essen Golf, Lyon apartment, Barcelona ring, Sunday brown-out, Safe Deal, Ruhrblick) in your pages and check them against the ledger.
3. **Evidence discipline.** Company facts carry a dated source; old evidence (>3 years) is flagged as possibly superseded; inferences about real companies are labeled; nothing presents undocumented internals as fact; "as of 2026" on volatile facts. Where a writer flagged an unverified legal text (see consistency-issues item 4), verify it via the EU Publications Office route in WRITER-BRIEF.md or hedge it. Spot-check 3–5 of the most load-bearing external claims per page with WebFetch.
4. **Cross-links.** Only valid permalinks; restore links writers removed because a page did not yet exist (`[[toolkit]]`, `[[glossary]]`, `[[long-term-evolution]]`, `[[part-N]]`, `[[introduction]]`); convert hard-coded `*.html` links to this book's pages back to `[[permalink]]`; no `[[…]]` left unresolved; links make sense.
5. **Mermaid.** `---begin mermaid---` / `---end mermaid---` fences; quoted labels; each diagram followed by a `**Figure N:**` caption; figures numbered consecutively.
6. **Prose quality.** Remove style-guide buzzwords; fix obvious repetition between adjacent sections; first-use definitions of acronyms; American spelling. Pages far over length (>9,000 words of prose) may be trimmed of clear repetition only.

## Process

- Edit only your assigned pages (plus their `spec.md`). If you find a problem in another page, record it in your review log instead of editing it.
- For each page you edit, append to its `spec.md` Changelog: `- **2026-10-19** — Editorial review pass: <one-line summary>. *(AI-mediated session)*`
- At the end run `cd /Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals && python3 _wiring/build.py 2>&1 | grep -iE "error|Traceback" | head` (a transient error from another journal's parallel build can be ignored if a rerun passes), then `python3.11 /private/tmp/claude-501/-Users-zeljkoobrenovic-PycharmProjects-spec-driven-journals/fae6a289-cfa0-449a-8385-7b4381f86340/scratchpad/render_check.py <permalinks...>` — every page must print `OK` (no failed mermaid, no unresolved links, no `XJ:` entries). Fix anything that fails.
- Write your review log to `ROOT/_research/review-<your-scope>.md`: per page, what you changed (one line each) and any remaining issue for the author.

## Report back

Under 200 words: pages reviewed, the most significant fixes, render-check result, and open issues for other parts or the author.
