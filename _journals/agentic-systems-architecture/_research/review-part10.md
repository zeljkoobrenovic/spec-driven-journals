# Review — Part X (Evolution): chapters 38–40

Reviewer pass, 2026-10-28. Part intro (`part-10-intro`) not touched (being written by another agent).

## Timeline reconciliation (Alias Drift and Closewise migration)

**Alias Drift** — 33 (read only), 38 and the ledger agree: the alias moved over the weekend before Mon 2 Aug 2027 (WD1 of the July close); rejections ~11% vs 4%; Joost raised it Wed 4 Aug; Thu 5 Aug (WD4) Mei Lin's team traced it by replaying Monday's rejected inputs and running the suite on alias vs previous exact version (89.4% vs 96.1%) and pinned the previous version; alias ban and served-version recording September 2027. 39 only refers to the size of the jump (4% → 11%), which is consistent.
- 33 says the controller cost was "roughly 90 extra rejected entries … (the arithmetic is in [[versioning-agent-systems]])", but 38 had no such arithmetic. **Added to 38** using ledger figures: 1,498 proposals on the drifted model, 165 rejected, about 105 more than a 4% rate would give. **Cross-part issue (editor):** 33 should say "roughly 105", not "roughly 90" (90 matches the old ~325/day figure; the `[editor]` ruling is 380/day). Exact text in 33: "roughly 90 extra rejected entries to redo by hand in the busiest week of their month (the arithmetic is in [[versioning-agent-systems]])".
- 33 also says the rate "began to rise" on Monday and "By Thursday it was 11%", while its own table and the ledger say ~11% from day 1. Minor; for the editor.

**Closewise migration** — checked every date against the 2027/2028 calendar: September close WD1 Fri 1 Oct; October close Mon 1 – Fri 5 Nov (shadow); canary start Wed 17 Nov = WD13 (outside the seven-working-day rule); November close Wed 1 – Tue 7 Dec; rollback 7 Dec 16:40; `cw-2027.12.1` gated Fri 10 Dec; canary resumed Wed 15 Dec (WD11); full rollout Mon 17 Jan 2028 (WD11, after the December close on 3–7 Jan); holdback through the January close, before the 31 March 2028 floor. Numbers (1,936 shadow, 94.1%, 52/44/18, 196 vs 188, 5.1% vs 4.3%, 5 entries €183,400, 3 × 1,094 = 3,282 trials, 96.3% vs 96.0%) match the ledger and chapter 32. 38's migration calendar (November 2027, seven agents, eleven model ids, seven-working-day rule) matches. No changes to dates were needed.

## Ruling 23 (manifest labels)

- 38: Answerdesk diff `2027.09.7 → 2027.10.1` → **`ad-2027.09.7 → ad-2027.10.2`** (matches 34). Closewise manifest `2027.09.3` → **`cw-2027.09.3`**.
- 39: `2027.09.3`, `2027.10.2`, `2027.12.1` → **`cw-2027.09.3`, `cw-2027.10.2`, `cw-2027.12.1`** (the unprefixed `2027.10.2` collided with Answerdesk's `ad-2027.10.2`).
- Ledger: the staged-rollout line uses unprefixed labels; appended a clarifying `[staged-rollout-and-rollback]` line (append only).
- Cross-part (editor): `22-side-effects-and-external-actions` line 279 has `"credit_policy", "version": "2027.10.2"` (a policy version, not a manifest — probably fine, but could be confused with the manifest label); `28` has `bulkhead/answerdesk@2027.08.3` (policy, fine).

## Per chapter

### 38 — versioning-agent-systems
Fixes:
- Labels per ruling 23 (above).
- `eval_binding … suite-v9` → `suite-v1` (ledger: suite v1 April 2027, v2 October 2027; a September manifest was gated on v1).
- Added Alias Drift cost arithmetic (1,498 / 165 / ~105).
- OpenAI quote "Move prompts into app code" is not on the page → replaced with the page's wording "move reusable prompt content into your application code".
- Tidemark "provenance, confidence and expiry" → "trust level" (ledger: schema v3 replaced model confidence with trust levels).
Checked, no change: approval/policy-version interplay (ruling 6, in-flight runs keep their policy), Answerdesk A2 limits (€9,000 / 120 a day), 31-hour Tracker Update, alias ban September 2027.
Sources spot-checked:
- platform.claude.com model-deprecations → **supported** (60 days' notice; "likely to be less reliable"; partner platforms own schedules; API version 2026-10-21 removes temperature/top_p/top_k with a 400; notice-to-retirement 60–62 days for 2026 entries).
- developers.openai.com deprecations → **partly**: 2026-06-03 notice, 2026-11-30 shutdowns and notice periods supported; quote wrong → fixed.
- modelcontextprotocol.io versioning + 2026-07-28 changelog → **supported** (date semantics; sessions and initialize handshake removed; four revisions 2025-03-26, 2025-06-18, 2025-11-25, 2026-07-28).
- arxiv 2408.04667 (Atil et al.) → **supported** ("up to 15%" over 10 runs).
- Thinking Machines nondeterminism → **supported** (1,000 completions, 80 unique; batch-invariant identical; slowdown).
Words: ~7,190 → 7,237 (≤ 8,000).

### 39 — staged-rollout-and-rollback
Fixes:
- Labels per ruling 23 (above).
- Anthropic 2026-04-23 postmortem: the quoted phrase was not exact → now quotes "made it past multiple human and automated code reviews, as well as unit tests, end-to-end tests, automated verification, and dogfooding"; caching change described accurately ("after an idle session, dropped prior reasoning on every turn").
Checked, no change: 380/day (`[editor]`), seven-working-day rule, profile B 5% canary at A2 in both arms, version vs tier separation, rollback asymmetry, forward fixes executed by deterministic code (ruling 14), SoD on reversals.
Sources spot-checked:
- anthropic.com/engineering/april-23-postmortem → **supported after fix** (dates, commitments "soak periods, a broader eval suite, and gradual rollouts", per-model evals for every system prompt change).
- CrowdStrike preliminary PIR → **supported** (04:09 / 05:27 UTC; "is not code or a kernel driver"; Content Validator bug; "starting with a canary deployment").
- Argo Rollouts analysis docs → **supported** (abort, weight to zero; inconclusive pauses for manual resume/abort).
- Hilton, Google Cloud blog (24 March 2017) → **supported** (all quotes).
Words: ~6,980 → 6,994.

### 40 — owning-agentic-systems
Fixes:
- "an external effect is still at-least-once" → "a call to an external system is still executed at least once and made exactly-once in effect only by keys and receipts" (ruling 4).
- OpenAI quote corrected as in 38.
- METR March 2026 note: "recent values shift by 1.5–2×" overstated → now "move one recent model's 50% horizon by about 1.5× and its 80% horizon by about 2×" (the note gives the spread for Opus 4.6).
Checked, no change: Close-Day Queue numbers and times, roadmap items 1–9 and registry counts (11 entries, 21 action classes), billing-specialist retirement dates, €5,000 delegation, team 14 → 19, kill switch holds not drops (ruling 10), A1 cap on external commitments.
Sources spot-checked:
- anthropic.com/research/measuring-agent-autonomy → **supported** (18 Feb 2026; "deployment overhang").
- METR 2026-03-20 note → **partly** → fixed.
- Microsoft CAF AI CoE → **supported** (both quotes; updated 2026-10-15).
- Regulation (EU) 2026/1744 → primary fetched only as Cellar metadata (amends 2024/1689, in force 27 July 2026); the 2 December 2027 Annex III date is **consistent with multiple secondary summaries** (law-firm and compliance notes); kept, primary link retained.
- OpenAI deprecations (Assistants API 2026-08-26) → **supported**.
Render check: `[[part-11]]` unresolved — the part-11 intro is not written yet (expected).
Words: ~7,070 → 7,101.

## Format and specs
All three: callouts with exact labels, three KEY POINTS, 2–3 failure patterns with exact names, Across Domains section, Questions to ask, hand-off (38 → 39 → 40 → `[[part-11]]`), grouped Sources, fictional disclaimer; no banned words. Specs still match; changelog lines added (revised already 2026-10-28).

## Verify
- Build: `[built] agentic-systems-architecture` (warnings only for not-yet-written pages).
- render_check: 38 and 39 OK; 40 only `[[part-11]]` unresolved; no mermaid failures.

## Cross-part issues for the editor
1. 33: "roughly 90 extra rejected entries" → ~105 (see above); "By Thursday it was 11%" vs ~11% from day 1.
2. 34 line ~245 area: "Toolyard enforced the €250 limit and one credit per ticket" — ruling 21 wording is "one credit per technician visit; at most one active credit proposal per ticket".
3. Ledger inconsistency outside Part X: Fixture Purge response line ([partial-failure-and-compensation]) says the reviewer flagged it Thu 22 July 2027, while the canonical [domain-coding-agents] line says Fri 16 July.
