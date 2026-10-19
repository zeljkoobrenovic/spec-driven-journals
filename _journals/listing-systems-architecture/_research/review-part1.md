# Editorial review: Part I (2026-10-19)

Scope: part-1-intro, 01-marketplace-taxonomy, 02-liquidity-and-network-effects, 03-industry-evolution, 04-business-capabilities, 05-bounded-contexts, 06-vertical-requirements. Render check: all seven pages OK (no failed mermaid, no unresolved links, no XJ entries).

## part-1-intro (`part-1`)
- Rewrote the ch. 03 row in the chapter table from the written chapter (five waves; "or the owner may sell a brand").
- Rewrote the ch. 03 Veldmark bullet: history read as sediment, the 2012 Polish purchase, and the March 2027 decision record that any brand may be sold within five years.
- Spec: open question on ch. 03 marked resolved; changelog entry.
- Remaining: about 880 words, slightly over the 800 cap; left as is.

## 01-marketplace-taxonomy
- Safe Deal 2026 figures changed from 4.1M / €310M to 11.6M / ~€1.02B, with ~€75M revenue and a take rate of about 7% (consistency item 1). Spec caveat about not computing a take rate removed.
- DSA Art. 30 wording corrected to "collect … and make best efforts to assess whether it is reliable and complete", checked against the Official Journal text through the EU Publications Office. The unofficial-mirror source was replaced with the EUR-Lex ELI link. The Omnibus (2019/2161) "online marketplace" definition was verified the same way and its link replaced (item 4).
- "Serves four Tradeyard profiles" corrected to three: Safe Deal runs in goods NL, BE and PL.
- Essen Golf: 23 raw leads, plus 19 after merging repeat contacts (item 11).
- Vinted fee: the unverified "renamed in October 2026" claim softened to "now called the Vinted fee (formerly the Buyer Protection fee)".
- timetoread 29 → 33 min.
- Spot-checked: Vinted GMV and revenue, Vinted price list, the Facebook Marketplace quote, Rightmove ARPA £1,621 and 70% margin.

## 02-liquidity-and-network-effects
- Brown-out cost now matches the owning chapter (reliability-and-scale): about 3.4M failed search requests and about 9,800 fewer first contacts. Before, it said 2.3M failed searches and ~40,000 contacts.
- "April 2027, two months into Common Ground" → three months (the programme was approved in January).
- Spot-checked: the Hemnet 29 Sep 2026 free formats and Q2 −23.1%, Rightmove 89%/75%/85%, Rightmove's busiest minute, Facebook's 450M visitors a month.

## 03-industry-evolution
- Dated timeline checked against case pages 46–51. Dates and ownership agree: eCG deal 21 Jul 2020 / 25 Jun 2021; NOK 115 offer and May 2024 take-private; willhaben sale 2025; Spain to EQT completed 27 Feb 2026; Fotocasa and Habitaclia to Scout24; KKR/CPP 29 Apr 2025; Yad2 to Apax Dec 2025; mobile.de clearance 8 Oct 2026 naming Oak Germany Buyer GmbH; OLX dates; Domain Aug 2025; AutoScout24 to H&F 2020.
- Fixes: "seven countries" → eight (item 19). The 2004 eBay row now separates mobile.de (closed April 2004) from Marktplaats (November 2004) and cites "eBay SEC filings (2004)". OLX Autos' $1.6B is dated to the year to March 2022. Central Asian sites are "agrees to sell".
- AVIV: the CEO quote is now the exact "…to create a European real estate marketplace" with no "unified" (item 18). "Fully integrated platform" is explicitly attributed to the interviewer.
- The separability decision record is dated March 2027 (ledger) instead of "Ingrid's first month" (February).
- timetoread 34 → 37 min. About 8,800 prose words including tables, under the 9,000 trim threshold; not trimmed.
- Spot-checked: Seamans and Zhu's 20.7% and $5B, Rightmove 70% and £425.1m, Vinted, and the AVIV interview wording.

## 04-business-capabilities
- TOGAF definition paraphrased: the guide is behind a login and could not be re-read. The OMG value-stream sentence is now quoted as Wikipedia quotes the OMG BAWG overview (2012) (item 4). Spec open questions updated.
- Strategic Report 2025 dated 2026 and linked. Rightmove's "62% of agency ARPA growth from product" verified.
- Added a [[toolkit]] link (Tool 1) (item 7).

## 05-bounded-contexts
- Kleinanzeigen Debezium quote corrected to the source wording ("often occur at the infrastructure level rather than in the application code").
- Checked: the listing ID format matches ch. 33 and the toolkit; the Lyon prices €389k/€389k/€395k match ch. 15; the 19 contexts, 31 decisions, four ACLs and the 214-column `ads` table match the ledger. Vinted 2026 claims verified.

## 06-vertical-requirements
- Closing hand-off now names [[part-2]] (item 13), then listing-aggregate.
- Essen Golf raw vs deduplicated leads.
- EPBD recast: the transposition date (Art. 35) and the certificate template by 29 May 2026 (Art. 19) were verified on the Official Journal text, and the EUR-Lex link was added.
- Added a [[toolkit]] link (Tool 2).
- Spot-checked: Vinted's 500,000+ PUDO points and own carrier in five countries, ESCO v1.2.1 counts. Table 5 arithmetic re-computed (correct).

## Open issues for other parts or the author
- `bibliography` page missing: the build warns "missing post: posts/bibliography/index.md". config.yaml lists it, but the folder does not exist.
- Ledger line [listing-aggregate] still says the bike was reserved at 16:32. The editor line (14:02) wins. The [transactions-and-payments] ledger line also says "paid … and reserved 16:32". These two ledger lines conflict with the editor resolution and with ch. 33. The author should decide whether the 14:02 editor line or the payments chapter's 16:31/16:32 order timeline is canonical: the payments chapter's offer-accepted time cannot follow a 14:02 reservation.
- Rightmove RNS 2026 and Autotrader FY26 PDFs are cited across many chapters. The Rightmove figures were verified from a cached text extract; Autotrader figures (ARPR £2,995, Deal Builder 6,700 retailers / 137,000 reservations) were not re-verified in this pass.
- ch. 02 still cites the Hagiu and Rothman HBR article from a summary (paywalled).
