# Editorial review — Part IX (LEADERSHIP)

Reviewer pass, 22 October 2026. Prose words measured with `awk '/^## Sources and Evidence/{exit} {print}' index.md | sed 's/|/ /g' | wc -w`. No page exceeded 8,500, so nothing was trimmed. All seven pages: front matter complete, callouts in order with exact labels, 3 KEY POINTS, 2–3 exact failure-pattern names, `<br>`, valid `[[…]]` links only (one allowed LISTED sibling link in 44), mermaid fences and consecutive figure captions, hand-off to the next page in config order. Build clean; render check OK on all seven.

## part-9 (part-9-intro) — 1,283 → 1,283
- "programme" → "program" (American spelling). Facts checked against 44–49 (€7.8M build-data run rate, 58 records/19 invoices, 57 orphans).
- Open (author): the intro is longer than the 500–800 words the style guide suggests for part intros; left as is (no trim rule triggered).

## build-buy-or-partner (44) — 8,295 → 8,295
- Checked against the ledger: build-data €13.1M/28.5M (2026) → €7.8M/13.5M (Q4 2027), flat-fee break-even, EV Overvaluation €1.1M/610 cars, Merelstad €180, Tradefloor 11,500 hand-offs, identity inventory, Handback detection rates. All agree.
- Verified with WebFetch: Stripe meter configuration and 24-hour adjustment limit (docs.stripe.com).
- "programme" → "program". timetoread 35 min is right for the length.

## one-platform-from-many-products (45) — 7,456 → 7,491
- **Item 29:** v2 tier row now says E2 (not offered) carries no tier, and a sentence explains that the tier counts sum to 39 for this reason. Appended an `[editor-review]` ledger line saying the same.
- Corrected "Six of v1's eight red capabilities" → "Seven" (v1 red A8, B2, B5, B10, D1, F1, F4, F5; only F4 stays red, and F5 turned green).
- Sold-audit sentence aligned with `events-webhooks-and-sync` (one sold event, eight consumers, six mechanisms).
- "programme(s)" → "program(s)".
- Verified with WebFetch: Keyloop scale and $1.45bn sale price.

## organizing-engineering (46) — 7,592 → 7,594
- "sixty channel adapters" → "61 channel adapters" (ledger).
- Hedged "faster than any documented case" → "aims to move faster than that documented sequence".
- Team, head-count and hub totals check out (35 teams, 300 engineers; 115/85/55/25/20); DriveDesk Outage figures match `dms-integration`.

## modernizing-the-platform (47) — 7,604 → 7,604
- Sources and Evidence subheadings converted from italics to `###` (house format).
- Verified with WebFetch: GitHub's password-auth brownouts (30 Sept, 28 Oct 2020) and removal (13 Nov 2020).
- Connect XML traffic, segments, parallel-run figures and the wave plan agree with the ledger.

## ai-in-dealer-workflows (48) — 7,243 → 7,241
- **Item 30:** the sentence "This updates the timetable given in [[valuation-engine]], which was written before the Omnibus text was final" now says that the amended dates apply wherever the book discusses high-risk obligations, including Vantage. It no longer depends on how valuation-engine is worded.
- WebFetch check of Regulation (EU) 2026/1744: the act exists (OJ L 2026/1744, in force 27 July 2026) and amends Article 113 of the AI Act. The amended dates themselves could not be read within the fetch window, so they rest on the writer's fetch and the Gibson Dunn source.
- Pilot figures agree with the ledger.

## evolving-the-vehicle-platform (49) — 7,734 → 7,843
Written before 45–48 existed; aligned with them:
- **Separability:** the sentence "S8 and S16 were the only stressors nothing in One Dossier addressed" now refers to the *original plan*, and adds that this finding is why the December 2027 integration contract (45) requires separability.
- **Item 29 / kernel:** added one sentence mapping R1–R4 to the v2 tiers. A2, F4 and F5 are kernel; A6 provenance is shared platform; F1 and F2, the other kernel members, form R7.
- Year 3 now says v2 webhooks are live from Q3 2028 (item 20). The Connect XML zero-call target and F12 now mention the paid extensions that end by 30 June 2030 (47).
- The agent-tools option links to the November 2027 external-agent policy (48).
- The hand-off now ends at `[[part-10]]`; it previously ended at case-cox-automotive.
- timetoread 36 → 34 min. "programme" → "program".

## Open issues for other parts / the author
1. **valuation-engine (Part III), item 30:** line ~349 still gives the pre-Omnibus AI Act dates (2 Aug 2026 / 2 Aug 2027) and says the Omnibus was "still in negotiation in October 2026". It should use Regulation (EU) 2026/1744's dates (2 Dec 2027 for Annex III; 2 Aug 2028 for Art. 6(1)), as 48 does.
2. **"programme" vs "program"** is mixed across the book (about 26 pages use "programme", including the ledger's "One Dossier programme"). Part IX now uses "program". The final editor should normalize the rest of the book to American spelling.
3. Part IX intro is about 1,280 words, above the 500–800 guideline for part intros.
