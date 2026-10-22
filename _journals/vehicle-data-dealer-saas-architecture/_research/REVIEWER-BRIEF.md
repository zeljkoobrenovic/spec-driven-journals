# Reviewer Brief — editorial pass

You are the senior editor for **Architecting a Vehicle Data and Dealer SaaS Platform** (ROOT = `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/vehicle-data-dealer-saas-architecture/`).

The priority is **quality**. Pages were written in parallel by different writers. Your job is to make your assigned pages correct, consistent with the rest of the book and compliant with the house style. Use surgical edits: do not change a page's argument.

## Read first

1. `ROOT/_research/style-guide.md`: format, the "Across Markets" rule, failure-pattern names, evidence discipline (including labeled assumptions), mermaid rules and valid permalinks.
2. `ROOT/_research/consistency-issues.md` (if present): every numbered item. Fix the items that touch your pages. Canonical decisions recorded there win.
3. `ROOT/_research/scenario-ledger.md`: the canonical Axleby facts, including every "Additions by chapter" line and every `[editor]` line.
   - `[editor]` lines win over chapter lines.
   - Where two chapter lines conflict and no editor line exists, prefer the chapter that *owns* the topic per PLAN.md, and record your resolution in your review log.
4. `ROOT/PLAN.md`: the contracts and the reading order.

## For each assigned page, check and fix

1. **Format.**
   - Front matter is complete: title, date, author, excerpt, permalink and timetoread. Timetoread is about 230 words per minute of prose; correct it if it is far off.
   - The callouts appear in order with exact labels: IN THIS CHAPTER, YOU WILL / WHY THE BUSINESS CARES / WHY ARCHITECTS SHOULD CARE / KEY POINTS (exactly 3) / FAILURE PATTERNS THIS CHAPTER ADDRESSES. The last links `where-vehicle-platforms-go-wrong.html` and lists 2–3 patterns with exact names.
   - A `<br>` follows the callouts.
   - Parts II–VII chapters have the section "Across Markets: What Changes by Country", with a table.
   - The page has failure handling, a Chief Architect's view, Questions to ask, and Sources and Evidence.
   - The page closes with a hand-off to the **next page in config.yaml order**. The last chapter of a part hands off to the next part's intro.
2. **Length.** Measure with `awk '/^## Sources and Evidence/{exit} {print}' index.md | wc -w`. Over **8,500**: trim to **≤ 8,000** (cut repetition between sections, restated callouts, over-long scene-setting, duplicate tables; keep evidence, the Axleby worked example and the market comparison). Record before/after counts.
3. **Axleby consistency.** Every figure, date, name, system and decision must agree with the ledger and with the owning chapter. Grep your pages for the recurring examples and the named systems (Connect XML, JSON API v1/v2, Turnstile, Anchor, AVK, Specbook, Tracewell, Pulse, Vantage, Lotwise Classic, Lotwise Dossier, Relay, Switchboard, Meterline, Charter, Axleby ID, Gatekeeper, Tradefloor, Odolo, DriveDesk, Kilometra) and check them.
4. **Evidence discipline.**
   - Company facts carry a dated source; old evidence (more than 3 years) is flagged as possibly superseded.
   - Inferences about real companies are labeled; nothing presents undocumented internals as fact.
   - Illustrative volumes, latencies and costs that are not ledger facts are labeled as assumptions.
   - Volatile facts say "as of 2026".
   - Incidents are never attributed to a real register or real vendor.
   - Spot-check 2–4 of the most load-bearing external claims per page with WebFetch where reachable; hedge any claim you cannot verify.
5. **Cross-links.** Only valid permalinks; no unresolved `[[…]]`; no XJ links outside the allowed sibling list; convert hard-coded `*.html` links to this book's pages into `[[permalink]]`.
6. **Mermaid.** `---begin mermaid---` / `---end mermaid---` fences and quoted labels. Each diagram is followed by a `**Figure N:**` caption; figures are numbered consecutively.
7. **Prose quality.** Remove the style guide's buzzwords and fix repetition; define acronyms on first use; American spelling; Axleby never uses real product names.

## Process

- Edit only your assigned pages and their `spec.md`. If you find a problem on another page, record it in your review log instead of editing it. Exception: you may append `[editor-review]` lines to the ledger (one small append edit; re-read the tail first).
- For each page you edit, append to its `spec.md` Changelog: `- **2026-10-22** — Editorial review pass: <one-line summary>. *(AI-mediated session)*`
- At the end, run the build: `cd /Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals && python3 _wiring/build.py 2>&1 | grep -iE "error|Traceback" | head`. A transient OSError from a parallel build can be ignored if a rerun passes.
- Then run the render check: `python3.11 ROOT/_research/tools/render_check.py <permalinks...>`. Every page must print `OK`. Fix anything that fails.
- Write your review log to `ROOT/_research/review-<your-scope>.md`: per page, what you changed (one line each), word counts before and after, and any remaining issue for the author.

## Report back

Under 200 words: pages reviewed, the most significant fixes, word counts before and after, the render-check result, and open issues for other parts or for the author.
