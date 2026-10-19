# Review log — Part VIII (editorial pass, 19 Oct 2026)

Scope: part-8-intro, 41-platform-consolidation, 42-organizing-marketplace-engineering, 43-modernization-and-migration, 44-ai-in-listing-systems, 45-long-term-evolution, plus the cross-page restoration of `[[long-term-evolution]]` links. Render check: all six pages OK (no failed mermaid, no unresolved links, no XJ entries).

## Book-wide change in this scope

- "programme(s)" changed to "program(s)", "licence" to "license", "catalogue" to "catalog", "grey zone" to "gray zone" in all six pages and their specs (American spelling per the style guide). **About 15 other pages still use "programme"** (it is also the ledger's spelling for "Common Ground programme"). Editor to decide book-wide.

## part-8-intro

- American spelling (3× program).
- Veldmark thread: "Ingrid Halvorsen's team decides:" reworded. Organization v1 was decided by the CTO and the consolidation review went to the board, so Ingrid now "shapes" the decisions.
- Format, chapter table, hand-off to [[platform-consolidation]], ledger dates: all correct.

## 41-platform-consolidation

- Vertical table and Sources: AVIV "rowing back from one platform" now says the 2025 phrase "fully integrated platform" came from the interviewer or press (consistency item 18), with a link to [[case-aviv]].
- timetoread 31 changed to 27 min (about 6,200 words of prose).
- American spelling (program ×5, licenses, catalog).
- Verified: Bundeskartellamt mobile.de/Carwow release (published 8 Oct 2026, both quotes correct) and Adevinta's €130–165M synergy target over three years. Synergy-ledger arithmetic matches the ledger (€9.6M; €4.1M deferred).
- Open for the toolkit reviewer: Tool 11 (consolidation card) uses a three-way per-layer decision (keep separate / shared service / full replatform), while ch. 41 has five integration options plus divest and a stage-0–4 sequence. Tool 11 also leaves out the synergy-ledger figures and the "second migration only within 3% of baseline" rule. The facts do not conflict, but the toolkit could adopt ch. 41's vocabulary (consistency item 24).

## 42-organizing-marketplace-engineering

- Hard-coded `long-term-evolution.html` link changed back to `[[long-term-evolution]]`. Added to the spec's Sources.
- leboncoin citation (an RSS feed URL) now says it is the September 2026 BotISS post, read from the feed summary. Open: replace it with the direct post URL if one can be found.
- American spelling (program ×4, catalog ×3). Added a blank line before figure captions.
- Ledger checks passed: engineering baseline, org v1 dates, 74 decision records, team counts.

## 43-modernization-and-migration

- American spelling. Added a blank line before figure captions.
- Verified: Vinted Vespa migration (6 clusters, May 2023 to April 2024, 2.5× latency, change-to-visible 300 s to 5 s). Yardstick inventory and waves match the ledger. Canary and ramp dates are internally consistent (all Fridays in 2028).
- Only two failure patterns (within the 2–3 allowed).

## 44-ai-in-listing-systems

- Hard-coded `long-term-evolution.html` link changed back to `[[long-term-evolution]]` (consistency item 10). Added to the spec's Sources.
- Sources reformatted to house style: `###` group headings and "— publisher, year. Note." entries.
- Poland and Portugal rollout now says "once Polish and Portuguese evaluation sets exist". It used to say "after the taxonomy harmonization", but ch. 39 has the taxonomy service live in `ty:pt` from 4 Oct 2027.
- "grey zone" changed to "gray zone".
- Verified: Digital Omnibus = Regulation (EU) 2026/1744, published in the OJ on 24 Jul 2026, with Annex III on 2 Dec 2027, Annex I on 2 Aug 2028 and marking grace to 2 Dec 2026. OLX Auto Description 98%/89% (28 Aug 2026). DSA Art. 20(6) wording.
- Note: the Llama Guard entry in Sources is not cited in the body. It is harmless but could be cited in the T&S section.

## 45-long-term-evolution (synthesis)

- Checked the Part I–VIII guarantee table, the four ideas, the stressor table, the residue counts and all twelve scorecard baselines against the ledger and the owning chapters' KEY POINTS. They match. Examples: Ranking policy +5.3% / −2.5% VAS, 41,000 lingering copies, 3.8%→0.3% carousel ghost clicks, unit costs, 23/41 unowned/unmonitored models. "Eight of ten stressors covered" recounted as correct. The S3 statement about not having a canonical goods entity matches [[entity-resolution]].
- Fixes:
  - "Six years of paid boosts" changed to "Five layers of paid boosts ... since 2016", per the ranking ledger line.
  - "Five weeks before the board meeting" changed to "four weeks". The question arrives about 16 Nov; the board meets 14 Dec.
  - Part IX bridge: "eBay Classifieds Group's shared platforms" changed to "national leaders, thin shared layer and sale", to match case-ebay-classifieds KEY POINTS. The other case descriptions match the case titles and KEY POINTS.
  - The Schibsted 2016 slide is marked "widely reported", and its Sources note now points to [[industry-evolution]]. [[case-adevinta]] does not contain that quote.
  - Added Adevinta Annual Report 2023 to Sources. It backs the "unified global platform" quote used in the pendulum section.
  - The Prosus/OLX Autos source is now described as the 2023 move to exit, with a link to [[case-olx]].
  - Sources reformatted to house style. American spelling (program ×7, license ×3).
  - timetoread 42 changed to 46 min.
- Length: about 7,000 words of prose excluding tables (10,700 with tables). That is under the 9,000-word prose trim threshold, so nothing was trimmed.
- Verified: the Productscape quotes match `productscape-digest.md`. The Auto Trader ArchUnit post (2026-06-18) is backed by brief-automotive as VERIFIED. Medium returned 403 to a re-fetch.

## Cross-page `[[long-term-evolution]]` restoration

- Fixed in scope: ch. 42 and ch. 44 (index and spec).
- **Not edited (per coordinator): ch. 39.** `39-multi-country-platforms/spec.md` line 56 still says "the long-term evolution chapter (not yet linked)". The ch. 39 reviewer is restoring it.
- **Out of scope, recorded for the owner:** `where-listing-systems-go-wrong/index.md` line 436 (and its whole chapter-by-pattern matrix, lines 385 onward) uses hard-coded `[NN Title](permalink.html)` links for every chapter, including `long-term-evolution.html`. They resolve correctly because they are relative in-journal links. Converting them to `[[…]]` would replace the "NN Title" labels with full titles in a dense matrix, so the owner may prefer to keep them.
- No other plain-text or `.html` references to long-term-evolution were found in posts/.

## Other observations

- The build warns `missing post: posts/bibliography/index.md` (another part's page, not yet written).
- Ledger line [transactions-and-payments] still says the bike was "reserved 16:32". The editor line says 14:02 (consistency item 9). The ch. 29 reviewer should check this.
