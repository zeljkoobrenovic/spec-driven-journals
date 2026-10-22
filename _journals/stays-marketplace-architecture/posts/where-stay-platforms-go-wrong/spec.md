---
status: accepted
revised: 2026-10-22
---

# Spec: Overbooked: Sixteen Ways Stay Platforms Go Wrong

## Intent

Give the book its shared vocabulary of failure. The page names the sixteen failure patterns that recur in accommodation (OTA-style) and hosted-stays marketplaces, so every chapter can open with a "failure patterns this chapter addresses" callout that links back here, and so design reviews can say "this is Connectivity Roulette" and move straight to the mechanism and the owner. For each pattern the reader gets a quote, the warning signs, the mechanism, the cost (with dated public examples where the research briefs have them, and a labeled fictional Corvane incident), which marketplace type it hits hardest and why, and the chapters that address it. After reading, an architect can recognize the patterns in their own platform, ask for the first number that reveals each one, and trace a symptom back to the upstream pattern that causes it.

Productscape domains covered: none as a product brick; the page is a preface that cuts across every domain of both models (TAM and HSM) by naming how they fail.

## Audience

Chief and enterprise architects, principal engineers and engineering leaders of OTAs, hosted-stays and vacation-rental marketplaces, channel managers and PMS vendors. They have lived through some of these incidents; they need names, mechanisms and a map to the chapters, not definitions of APIs or caches.

## Success criteria

- [x] Uses the sixteen exact pattern names, warning signs and "hits hardest" values from the style guide, in the style guide's order, in one summary table that also gives a first indicator per pattern.
- [x] Every pattern has a composite role quote, warning signs, mechanism, cost, a fictional Corvane illustration consistent with the ledger, a "Hits hardest" line with the reason, and a "Where this book helps" list with valid permalinks.
- [x] Public examples are dated and sourced (EU and US regulation with dates of application, company filings, developer documentation, security research), and the one inference about a real company (Vrbo's re-platforming) is labeled.
- [x] Includes a diagram of where patterns strike along the guest's journey and a diagram of the chains between patterns, with captions that state the point.
- [x] Ends with a chapter-by-pattern matrix built from the chapters' opening callouts, and hands off to [[meet-corvane]].
- [x] Length 6,000–8,500 words including tables, before Sources and Evidence (about 8,000).

## Non-goals

- Remedies in depth: each "Where this book helps" line points to the chapter that designs the fix.
- The book's argument and routing — [[introduction]]; Corvane's full landscape and cast — [[meet-corvane]].
- Regulation in depth — [[stays-regulation]] and [[taxes-on-stays]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The matrix was built from all 51 chapters' opening callouts on 2026-10-21; if a chapter's callout changes, its row here must change with it.
- The Gimmonix "about 40% not accurately mapped" figure is a vendor claim without a stated method; keep it labeled or replace it if a better source appears.
- The CNMC fine is sourced from press reports; replace with the CNMC decision text if fetched.

## Decision log

- **2026-10-21** — Modeled on LISTED's `where-listing-systems-go-wrong` (quote, signs, mechanism, cost, illustration, chapter links) but shortened each pattern to about 300 words to fit sixteen patterns into the 8,500-word cap; dropped LISTED's separate "first indicators" table and folded the indicator into the summary table.
- **2026-10-21** — Added a "Hits hardest" line per pattern, because the book's comparison of hotels and homes is its organizing idea; the line explains why, not only which.
- **2026-10-21** — Built the matrix from the "FAILURE PATTERNS THIS CHAPTER ADDRESSES" callouts of the written chapters (● only, no secondary marks), rather than judging relevance by hand, so the matrix stays mechanically checkable.
- **2026-10-21** — Grouped the patterns into four families (supply and inventory, marketplace rules, money trust and law, resilience and control) while keeping the style guide's order, and named four chains, with The Hotel-Shaped Home as the root of the shape chain.

## Sources

- **Internal**
  - `_research/style-guide.md` — the pattern names, warning signs and "hits hardest" values.
  - `_research/scenario-ledger.md` — Corvane incidents and numbers.
  - Research briefs: availability-pricing, booking-com, airbnb, expedia-agoda-tripcom, supply-connectivity, booking-reservations, payments-finance-tax, trust-safety-regulation, platform-data-ml, host-partner-guest-service.
  - Every chapter's opening callout, for the matrix.
- **External**
  - Google Hotel Center price accuracy policy; Expedia Rapid shopping documentation; Booking.com connectivity documentation (rate plans, overbookings, reservations).
  - Regulation (EU) 2024/1028, Regulation (EU) 2019/1150, Directive (EU) 2021/514, Directive (EU) 2025/516; the EU CPC accommodation actions; the FTC fees rule; NYC Local Law 18; Spain's Supreme Court ruling of 21 May 2026.
  - Airbnb, Booking Holdings and Expedia Group filings; Airbnb Engineering (2016); Booking.com KDD 2019 paper; Expedia Group Technology (2026); Sophos and ESET security research.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: verified pattern names, hits-hardest values and the 51-chapter matrix against every chapter callout; trimmed framing prose; American spelling; timetoread. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 2 mermaid diagrams to illustrations and added 1 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 7,901 → 7,857 prose words; no heading or structural changes; removed the cost-categories reading note and two repeated clauses, tightened four sentences; spec unchanged. *(AI-mediated session)*
