# Reviewer Brief — BOOKED editorial pass

You are the senior editor for **BOOKED: Architecting Travel Accommodation and Hosted Stays Marketplaces** (ROOT = `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/stays-marketplace-architecture/`).

The user's priority is **quality**. Pages were written in parallel by different writers. Your job is to make your assigned pages correct, consistent with the rest of the book and compliant with the house style. Use surgical edits: do not change a page's argument.

## Read first

1. `ROOT/_research/style-guide.md`: format, the "Hotels and Homes" rule, failure-pattern names, evidence discipline, mermaid rules and valid permalinks.
2. `ROOT/_research/consistency-issues.md`: every numbered item. Fix the items that touch your pages. Canonical decisions recorded there win.
3. `ROOT/_research/scenario-ledger.md`: the canonical Corvane facts, including every "Additions by chapter" line and every `[editor]` line.
   - `[editor]` lines win over chapter lines.
   - Where two chapter lines conflict and no editor line exists, prefer the chapter that *owns* the topic per PLAN.md, and record your resolution in your review log.
   - The December 2027 capability map v2 in `converging-two-marketplaces` supersedes earlier sharing statements. Earlier chapters may describe v1 (March 2027) as history.
4. `ROOT/PLAN.md`: the contracts and the reading order.

## For each assigned page, check and fix

1. **Format.**
   - Front matter is complete: title, date, author, excerpt, permalink and timetoread. Timetoread is about 230 words per minute of prose; correct it if it is far off.
   - The callouts appear in order with exact labels: IN THIS CHAPTER, YOU WILL / WHY THE BUSINESS CARES / WHY ARCHITECTS SHOULD CARE / KEY POINTS (exactly 3) / FAILURE PATTERNS THIS CHAPTER ADDRESSES. The last links `where-stay-platforms-go-wrong.html` and lists 2–3 patterns with exact names.
   - A `<br>` follows the callouts.
   - Parts II–VIII chapters have the section "Hotels and Homes: Where the Two Marketplaces Differ", with a table.
   - The page has a Chief Architect's view, Questions to ask, and Sources and Evidence.
   - The page closes with a hand-off to the **next page in config.yaml order**. The last chapter of a part hands off to the next part's intro.
2. **Length.** Measure the page with `awk '/^## Sources and Evidence/{exit} {print}' index.md | wc -w`.
   - If it is over **9,000**, trim it to **≤ 8,500**. Cut repetition between sections, restated callout content, over-long scene-setting and duplicate tables. Keep the evidence, the Corvane worked example and the hotels-vs-homes comparison.
   - Pages between 8,500 and 9,000 may be trimmed lightly.
   - Record before and after counts in your log.
3. **Corvane consistency.** Every figure, date, name, system and decision must agree with the ledger and with the owning chapter. Grep your pages for the recurring examples and the named platforms (Tally, Pricegrid, Almanac, Switchyard, Stayline, Fathom, Plumbline = reconciliation, Gauge = metric layer, Levy, Warden, Waypoint, place registry, Clause, Courier, Threadline, Harbor, Kiln, One Stay map v1/v2) and check them.
4. **Evidence discipline.**
   - Company facts carry a dated source.
   - Old evidence (more than 3 years) is flagged as possibly superseded.
   - Inferences about real companies are labeled.
   - Nothing presents undocumented internals as fact.
   - Volatile facts say "as of 2026".
   - Spot-check 2–4 of the most load-bearing external claims per page with WebFetch where reachable (the web-search quota is exhausted; fetch known URLs directly). Writers' "for a reviewer to check" notes are summarized in the consistency log; hedge any claim you cannot verify.
5. **Cross-links.**
   - Use only valid permalinks.
   - No `[[…]]` link may be left unresolved, and no XJ links outside the allowed sibling list.
   - Convert hard-coded `*.html` links to this book's pages into `[[permalink]]`.
6. **Mermaid.** Use the `---begin mermaid---` / `---end mermaid---` fences and quoted labels. Each diagram is followed by a `**Figure N:**` caption, and figures are numbered consecutively.
7. **Prose quality.**
   - Remove the style guide's buzzwords and fix repetition.
   - Define acronyms on first use and use American spelling.
   - Real companies must not be described with Corvane's names, and Corvane must not use real programme names.

## Process

- Edit only your assigned pages and their `spec.md`. If you find a problem on another page, record it in your review log instead of editing it.
  - Exception: you may append `[editor-review]` lines to the ledger to record a resolution. Make one small append edit, and re-read the file's tail first.
- For each page you edit, append to its `spec.md` Changelog: `- **2026-10-21** — Editorial review pass: <one-line summary>. *(AI-mediated session)*`
- At the end, run the build: `cd /Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals && python3 _wiring/build.py 2>&1 | grep -iE "error|Traceback" | head`. A transient OSError from a parallel build can be ignored if a rerun passes.
- Then run the render check: `python3.11 ROOT/_research/tools/render_check.py <permalinks...>`. Every page must print `OK`, with no failed mermaid, no unresolved links and no `XJ:` entries outside the allowed sibling links. The `bibliography` page may still be missing; links to it are fine. Fix anything that fails.
- Write your review log to `ROOT/_research/review-<your-scope>.md`: per page, what you changed (one line each), the word counts before and after, and any remaining issue for the author.

## Report back

Under 200 words: pages reviewed, the most significant fixes, word counts before and after, the render-check result, and open issues for other parts or for the author.
