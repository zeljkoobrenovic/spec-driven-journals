# Reviewer Brief — part review and repair

You are reviewing and repairing one part of **Architecting Agentic Systems** after its chapters were written by parallel writers. ROOT = `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/agentic-systems-architecture/`.

## Read first

1. `ROOT/_research/style-guide.md` (format, evidence discipline, failure-pattern names, valid permalinks, banned words).
2. `ROOT/_research/consistency-issues.md` — **every numbered ruling**; they win over chapters.
3. `ROOT/_research/scenario-ledger.md` — including all "Additions by chapter" and `[editor]` lines.
4. Every chapter of your part **in full** (index.md and spec.md), plus the part intro if it exists. Skim the KEY POINTS of neighbouring parts' chapters so you can spot contradictions across parts.

## What to check and fix (edit the chapters directly; minimal, targeted edits)

1. **Consistency rulings applied.** In particular: turn vs exchange (19); Forge split (20); credit limits (21); RFC 8693 `sub`/`act` (22); manifest label `ad-2027.10.2` (23); Closewise close-week volume 380/day (`[editor]`); approval model (6); unknown-outcome state (5); exactly-once *effect* wording (4); authorization vs execution (15); harness meaning (1). Fix every deviation.
2. **Ostrell numbers and dates** agree with the ledger and with the other chapters of your part (amounts, dates, tier changes, team sizes, volumes). Where two chapters disagree and no ruling exists, choose the ledger's or the earlier-owned chapter's figure, fix the other, and log it.
3. **Ownership and repetition.** A term is defined in depth only in the chapter that owns it (PLAN "Owns"); elsewhere one clause and a `[[link]]`. Cut re-teaching and duplicated incident retellings (keep one or two sentences and link to the owner). This is also how you bring over-length chapters down.
4. **Length.** Prose and tables from front matter to "Sources and Evidence" must be ≤ 8,000 words (`python3 -c` count of words excluding table pipes, code fences and mermaid blocks is fine). Trim anything over; prefer cutting repetition and generic sentences.
5. **Evidence.** Every company/vendor claim carries a year; research findings say what was measured and a limitation; inferences and assumptions are labeled; interview material is labeled as a design example with path and step. **Spot-check citations**: for each chapter, WebFetch at least 4 sources, prioritizing the ones the writer flagged as from memory, secondary or unverified, and any claim about events after mid-2026 or naming model versions released after mid-2026. If a source does not support the claim, fix the claim or replace the source; if it cannot be verified, label the claim honestly ("reported by …; not verified against the primary text") or remove it. Never invent a replacement source.
6. **Format.** The callouts (exact labels), exactly three KEY POINTS, 2–3 failure patterns with exact names, "Across Domains: How the Stakes Change the Design" in Parts II–X, Questions to ask, closing hand-off to the next page in reading order (last chapter of a part hands to the next part's `[[part-N]]`), Sources and Evidence grouped per the style guide, closing fictional disclaimer. Banned words removed.
7. **Specs.** spec.md still matches the article (Success criteria, Non-goals). Set `revised: 2026-10-28` and add a Changelog line `- **2026-10-28** — Review pass: <what changed>. *(AI-mediated session)*` if you changed the article.

Do not edit chapters outside your part. Record cross-part problems (a contradiction with another part's chapter) in your log for the editor, with the exact text in both places.

## Verify

- `cd /Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals && python3 _wiring/build.py 2>&1 | grep -iE "agentic" | head` (transient errors from other journals' parallel builds can be ignored if a rerun passes).
- `python3.11 ROOT/_research/tools/render_check.py <permalinks of your part>` — no mermaid failures and no XJ entries other than not-yet-written `part-N`/reference pages.

## Deliverable

`ROOT/_research/review-part<N>.md`: per chapter, the issues found and the fixes made (with before/after for any changed number), sources spot-checked (URL → verdict), word counts before/after, and cross-part issues for the editor.

## Report back

Under 200 words: chapters reviewed, the most important fixes, citations that failed verification and what you did, and open cross-part issues.

## Privacy rule for web requests

Never put the user's email address or any personal identifier in HTTP headers, User-Agent strings, query strings or request bodies.
