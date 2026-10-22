# Review log — Part IX (21 Oct 2026)

Scope: part-9-intro, 43–47. All pages were already under 8,500 words (counted up to Sources and Evidence), so nothing was trimmed. Format, callouts, hand-offs (43→44→45→46→47→part-10), mermaid and cross-links all passed. Render check: 6/6 OK, 0 failed mermaid, 0 unresolved links.

## Cross-book figure check (against the ledger and the owning chapters)
These all match: map v1 16/6/26 (48) → v2 23/6/20 (49); €145M and its ten-line split; Keystone Exit Plan (5.6M, 31,400 = five classes, 20 Dec 2027, Portugal 240k/21k/219k in 9 batches, last cohort Sept 2029, point of no return 90 days, CTO+CFO); Org Design v1 (19 Oct, 1 Jan 2028, 190 teams / 1,750 engineers, rows sum correctly, 210 moved, 14 new); the audit numbers; governance classes; the five fitness functions with their owners and baselines (1.8/5 per 10k, €3.20/€5.17, 0.65%); stressor workshop (23 people, 31 listed, 9 traced, Algarve 96/71/138); Frontdoor pilot and v2 numbers; Porto €304; 23 AI uses, 8 with no owner; Gauge = metric layer, Plumbline = reconciliation; place registry vs Waypoint (two components); the cross-type routing rule (Lisbon/Porto/Seville, ≤40 rooms).

## Changes per page
- **part-9-intro** (1,129 → 1,129): no change needed. It is above the 500–800 target, but every part intro in the book is 1,030–1,190 words, so it was left consistent with them.
- **43-converging-two-marketplaces** (7,374 → 7,396): the 14 Dec 2027 review is now "first annual review with the board" (ch. 47 said board, ch. 43 said forum); "Watchpost" removed in 3 places (not in the ledger or in travel-fraud) and replaced by booking risk score models on Warden; Gauge and Plumbline named in the register.
- **44-organizing-stays-engineering** (8,161 → 8,165): Watchpost replaced with booking risk score models; SLO spelled out on first use.
- **45-modernizing-a-live-marketplace** (7,142 → 7,144): "Since February" changed to "Since the spring" for the checkout attempt contract. It was adopted in Feb 2027 but rolled out in March and April.
- **46-ai-in-travel-stays** (7,419 → 7,419): removed a stray blank line.
- **47-evolving-the-platform** (7,014 → 7,035): the status of the "AI agents" stressor was "Candidate". It is now "Integrated for Roomstead", because Frontdoor v2 went live on 15 Nov 2027, before the workshop. The Fathom bootstrap is now described as the 2027 shadow run from a snapshot; the real balance migration is April 2028.
- Ledger: added one `[editor-review]` line covering the 14 Dec board review and the Watchpost removal.

## External spot checks (WebFetch)
- Verified: the Expedia Q1 2024 Vrbo quote and the lowered guidance; Booking 10-K FY2025 (4.4M properties, 3.9M homes, 36% alternative-accommodation nights, the "AI agents may further evolve…" quote); Airbnb Q2 2026 letter (50+ languages, nearly 45% resolved without a human, thousands of boutique hotels, hotel nights growing ~3× as fast, single-digit share).
- Not reachable: the Expedia Group Tech "operating model for agentic AI" post (403). Its quotes in ch. 46 are unverified in this pass.

## Open issues for other parts / the author
- **ch. 03 stays-capability-map** (Part I): at the time of this review it still did not present 16/6/26 as **v1 (March 2027)** or point to v2 in ch. 43 (consistency item 9).
- **Watchpost**: no longer in travel-fraud. Grep the whole book for any leftover mentions.
- **ch. 46**: the Expedia Romie claim is sourced only to a low-confidence secondary report, which the chapter already flags as low confidence.
