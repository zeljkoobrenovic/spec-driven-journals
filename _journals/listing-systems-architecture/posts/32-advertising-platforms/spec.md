---
status: accepted
revised: 2026-10-21
---

# Spec: Selling Attention: Display, Native and Retail-Media Advertising

## Intent

Show architects how a listing marketplace runs advertising beside its listings without letting advertising erode matches or breach privacy law. The chapter must split "advertising" into three businesses with different stacks (display and native through an ad server and header bidding; sponsored listings inside search and ranking; retail media built on first-party audiences), and argue for one shared policy layer over them: labels, ad load, consent, data-use exclusions and contact-based guardrails. It owns the terms ad stack, first-party audience and sponsored listing.

## Audience

Chief architects, heads of ad tech and data, product leaders and monetization leaders at marketplace groups who own or depend on an advertising unit; data-protection leads who must approve audience products.

## Success criteria

- [x] Reader can name the components of a marketplace ad stack and who should own each (Figure 1 and component table).
- [x] Reader can explain the header-bidding timeout trade-off with Prebid's documented behavior and set page-speed rules for ad slots (Figure 2).
- [x] Reader can explain why sponsored-listing decisions belong inside ranking, and the regulatory floor for paid ranking (Figure 3; Omnibus Annex I 11a, P2B Art. 5, DSA Art. 26).
- [x] Reader can design a first-party audience service with consent checks, exclusions (DSA Art. 26(3), 28(2)), minimum sizes and controlled activation.
- [x] Reader can state the consent architecture consequences of TCF v2.3, Google's certified-CMP requirement and the EDPB's consent-or-pay opinion.
- [x] The Veldmark example uses the ledger's €100M Veldmark Ads figure and works three decisions with numbers.
- [x] Trade-off and vertical-difference tables are present; every company claim carries a dated source.

## Non-goals

- How paid and organic candidates are blended and evaluated in ranking ([[ranking]]).
- Product catalog, pricing and entitlements for visibility products ([[products-and-entitlements]]).
- Revenue model comparison and KPIs ([[monetization-models]]).
- Tracking plans and consent on behavioral events in general ([[data-platform]]); Core Web Vitals and SEO ([[web-and-seo-architecture]]).
- Full regulatory analysis ([[marketplace-regulation]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- eBay's Promoted Listings pricing modes (cost per sale, cost per click) were not verified this session and are not described; add if verified.
- The European Commission's adtech proceedings against Google were not verified (web search quota exhausted); only the April 2025 US ruling is cited.
- Google Ad Manager terminology (line items, key-values with Prebid) is described generically; verify against current Google documentation before print.

## Decision log

- **2026-10-19** — Split advertising into three businesses rather than describing one "ad stack", because their decision points (ad server, ranking, audience service) and owners differ, and the conflicts between them are the chapter's real subject.
- **2026-10-19** — Invented a Veldmark Ads revenue split (programmatic €41M, direct and native €26M, sponsored listings €19M, retail media €14M; inventory Tradeyard €58M, Motorvane €24M, Hearthly €18M) summing to the ledger's €100M, and recorded it in the ledger.
- **2026-10-19** — Measured ad decisions against contacts in the worked example, tying the chapter to the book's liquidity thesis instead of to ad-industry metrics alone.
- **2026-10-19** — Kept consent mechanics here and linked to [[data-platform]] for ePrivacy basics, to avoid repeating chapter 36.

## Sources

- **Internal**
  - [[ranking]] — Top-listing relevance floor; paid-organic blending.
  - [[monetization-models]], [[products-and-entitlements]], [[data-platform]], [[messaging-and-leads]], [[experimentation]].
  - `_research/brief-monetization-economics.md` (Part 7), `brief-adevinta.md`, `brief-trust-safety-regulation.md`; `scenario-ledger.md`.
- **External**
  - Adevinta Annual Report 2023 (2024); eBay, CarGurus 10-Ks for FY2025 (2026); Autotrader FY26 and Rightmove FY2025 results (2026); OLX Tech Blog on hybrid search (2025).
  - DSA Arts. 26 and 28; Directive (EU) 2019/2161; Regulation (EU) 2019/1150; EDPB Opinion 08/2024 (2024).
  - IAB Europe TCF; Google Ad Manager CMP requirement; Prebid documentation; IAB Tech Lab ads.txt; MRC viewability guideline (2015); Google Privacy Sandbox update (2025); US DOJ press release (2025).

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: Hand-off restored to [[part-7]], VLOP statement sourced to the Commission's list (updated 15 Oct 2026), Omnibus and P2B citations verified and relinked to EUR-Lex. *(AI-mediated session)*
- **2026-10-19** — Added 3 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 4 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 5,566 → 5,615 prose words; lead now places the chapter as Part VI's last revenue line and names what Part VII reuses; the two vocabulary distinctions moved ahead of the terms table; five first sentences rewritten to state their point; no headings renamed, no sections moved. *(AI-mediated session)*
- **2026-10-20** — Replaced 3 mermaid diagram(s) with generated illustrations (figure numbers and captions unchanged; sources archived in `_research/mermaid-figures.json`); known differences from the source: Figure 1: kept attempt 3: extra arrow 'Ad policy service' to 'Consent management platform' carrying 'ad load, exclusions, labels' (the arrow to 'Ad slots' has no label); 'floors, caps, labels' printed twice; arrows both ways between 'Search results' and 'Sponsored listing auction'; extra arrow 'Campaign and budget service' to 'Ad server'; 'impressions, viewability' arrow from 'Ad slots' merged with the 'creative' line. *(AI-mediated session)*
- **2026-10-21** — Renamed failure patterns to match [[where-listing-systems-go-wrong]]: Seeing Double, Search as System of Record, Multiplier Creep, Fast Mail for Fraudsters, The Copy-Paste Country, Deal-Shaped Architecture, The Forced Fit, Billing by Guesswork, Set-and-Forget AI. *(AI-mediated session)*
