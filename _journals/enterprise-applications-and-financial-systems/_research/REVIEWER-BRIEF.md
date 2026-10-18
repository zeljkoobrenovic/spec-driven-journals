# Reviewer Brief — RECONCILED final editorial pass

You are the senior editor for **RECONCILED: Enterprise Architecture for Financial Systems** (ROOT = `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/enterprise-applications-and-financial-systems/`). The user's priority is **quality**. Chapters were written in parallel by different writers; your job is to make your assigned chapters correct, consistent with the rest of the book, and compliant with the house style — with **minimal, surgical edits**. Do not rewrite chapters, change their arguments, or shorten them wholesale.

## Read first

1. `ROOT/_research/style-guide.md` (format, failure-pattern names, evidence discipline, mermaid rules, valid permalinks — note Part V permalinks `part-5`, `case-uber-payments` are valid too).
2. `ROOT/_research/consistency-issues.md` — every numbered item; fix those that touch your chapters. Canonical decisions recorded there win.
3. `ROOT/_research/scenario-ledger.md` — canonical Northmere facts, including all "Additions by chapter" and every `[editor]` line (editor lines win over chapter lines).
4. `ROOT/PLAN.md` — chapter contracts.

## For each assigned chapter, check and fix

1. **Format.** Front matter complete (title, date, author, excerpt, permalink, timetoread — compute ~230 words/min of prose and correct if far off). Callouts in order with exact labels: IN THIS CHAPTER, YOU WILL / WHY FINANCE CARES / WHY ARCHITECTS SHOULD CARE / KEY POINTS (exactly 3) / FAILURE PATTERNS THIS CHAPTER ADDRESSES (link to `where-finance-architecture-goes-wrong.html`, 2–3 patterns, **exact names** from the style guide). `<br>` after the callouts. A Chief Architect's view section, a Questions to ask list, a Sources and Evidence section, a closing hand-off link to the next chapter in config order (fix hand-offs that point to the wrong next chapter).
2. **Northmere consistency.** Every figure, date, name, system and decision agrees with the ledger and with the chapters that own it. Typical traps: Lisbon dates (batch 1047 booked 14 Mar; bank credit 16 Mar; payout settled 26 Apr), €1.74 fee breakdown, the two different €420 chargebacks, Wayfare rail = merchant of record but agent (net €6.72 at ticket issue), OneStream renewal 31 Dec 2027, standard IDs STD-FIN-01..06, the Dec 2027 accounting-hub decision (Central Finance rejected), cast roles and pronouns. Where a chapter is set before a decision, presenting it as open is fine.
3. **Evidence discipline.** Vendor facts link to sources; unverified items listed in consistency-issues item 7 and in the chapter's own spec "Open questions" are hedged ("as of 2026", "reported", "to be confirmed"); no invented vendor internals; the fictional status of Northmere is stated once; recommendations are worded as judgement. Fix any URL flagged in consistency-issues item 18 for your chapters (replace with a canonical URL you can verify with WebFetch, or remove the link and keep the citation text).
4. **Cross-links.** Only valid permalinks; no `[[…]]` left unresolved; link targets make sense.
5. **Mermaid.** Fences `---begin mermaid---` / `---end mermaid---`; labels quoted; no unquoted parentheses/colons; each diagram followed by a `**Figure N:**` caption; figures numbered consecutively.
6. **Prose quality.** Remove buzzwords listed in the style guide; fix obvious repetition between adjacent sections; ensure first-use definitions of acronyms; American spelling. Keep edits small.

## Process

- Edit only your assigned files (plus their `spec.md`). If you find a problem in another part's chapter, record it in your report instead of editing it.
- For each chapter you edit, append to its `spec.md` Changelog: `- **2026-10-18** — Editorial review pass: <one-line summary>. *(AI-mediated session)*`
- At the end run `cd /Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals && python3 _wiring/build.py 2>&1 | grep -iE "error|Traceback" | head` (a transient ai-notes asset error from parallel builds can be ignored if a rerun passes) and then run the render check: `python3.11 /private/tmp/claude-501/-Users-zeljkoobrenovic-PycharmProjects-spec-driven-journals/d17de6c1-27df-4ac8-963a-4f42cb16c093/scratchpad/render_check.py <permalink> <permalink> ...` with your chapters' permalinks — every page must show `OK` (no failed mermaid, no unresolved links). Fix anything that fails.
- Write your review log to `ROOT/_research/review-<your-scope>.md`: per chapter, what you changed (one line each) and any remaining issue for the author.

## Report back

Under 200 words: chapters reviewed, the most significant fixes, render-check result, and open issues for other parts or the author.
