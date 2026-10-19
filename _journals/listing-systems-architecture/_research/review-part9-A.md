# Review log — Part IX A (case-adevinta, case-olx, case-ebay-classifieds)

Editorial review pass, 19 Oct 2026. All three pages already met the format contract (callouts in order, exact failure-pattern names, Chief Architect's view, Questions to ask, Sources and Evidence, correct hand-offs: case-adevinta → case-olx → case-ebay-classifieds → case-aviv). `[[part-9]]` now resolves in-journal. Render check: all three OK (mermaid 3/3/4, no failures, no unresolved links, no XJ).

## Claims re-verified with WebFetch (19 Oct 2026)

- **Adevinta:** eCG completion release (25 Jun 2021, #1 in 16 countries, about 3bn visits, €1.6bn pro forma, €130–165m synergies, Shpock to Russmedia 2 Jun 2021, Denmark to Schibsted about €278m); Q1 2024 release (28 May 2024, "Platform convergence project progressing well and according to plan", +31% transactional); Strategic Report 2025 (decentralization quote verbatim, parallel running, Spain completed 27 Feb 2026 with about €1.1bn gain, €1,550m dividend + €470m capital return, branch of 3 Mar 2026 for Kleinanzeigen.de GmbH, headcount 4,439, €1,891m / €865m / €970m); Spain sale to EQT (21 Jul 2025, six brands); SCHIP post (6 Jun 2023, 4,000+ developers, about 5,000 apps); multi-cloud governance (17 Dec 2024, 732 AWS / 425 GCP, <150 in 2019; note the post's own chart caption gives lower GCP figures); Galo Navarro talk (1,500 engineers, about 20 marketplaces, 10 minutes, about 200 Spanish microservices); Kleinanzeigen help page (Adyen, up to 14 days).
- **OLX:** OLX FY26 release (29 Jun 2026; US$992m, +28%/+16%; seven markets; 71%; La Centrale closed 17 Nov 2025, +13% traffic, +30% leads, "ahead of plan"; Kiwi closed 1 Aug 2025; Fixly 29 Oct 2025; Uzbekistan and Kazakhstan signing only); Prosus FY26 media release (US$481m aEBITDA, 48%, +8pp; motors US$429m 59%, real estate US$185m 46%, jobs US$87m 43%); Naspers Avito disposal (14 Oct 2022, RUB 151bn, 99%); Fin24 OLX Autos (US$1.6bn, +158%, 175,000 cars, US$206m losses, exit-rationale quote); hybrid search post (35→70, retrained LTR, linear re-ranker, about 3% / about 5%, full rollout; via the blog's RSS feed); OfferUp–letgo (Mar 2020, 40%, run by OfferUp); Otodim (13 May 2026, beta, inventory quote, in-development features).
- **eBay Classifieds:** SEC 2004 Marktplaats (10 Nov 2004, about €225m, "separate business", 1m+ listings); SEC 2020 transaction release (US$9.2bn, US$2.5bn + about 540m shares, 44% / 33.3%, US$150–185m, "partner in key areas"); CMA decision (2 Mar 2021, published 8 Apr 2021, transitional-services sentence verbatim, "platforms, related tangible and intangible assets"); Worldline OPP release (29 Sep 2022, Marktplaats and eBay Kleinanzeigen named); t3n (20 Jul 2023, OPP as Kleinanzeigen's provider); Australia sale (25 Aug 2022, US$60m, transition quote); Kleinanzeigen rebrand (16 May 2023, old domain "several more years"); MoVe webhook README (all quoted sentences).
- Not re-fetchable (Medium returns 403): Marktplaats Elasticsearch post, Berlin Tech Blog Kafka (2019), Debezium migration (2025) and Android rebrand (2025) posts. The briefs mark them VERIFIED; left as is.

## case-adevinta

- Kleinanzeigen row of the transactional table: dated the provider history (OPP at the 2020 launch and still in July 2023; Adyen per the October 2026 help page; switch date not public) per consistency-issues item 2; added onlinemarketing.de 2020 and t3n 2023 sources.
- Marktplaats row and comparison table: OPP dated "as reported in 2022"; 2026 provider marked not verified.
- Timeline: Shpock buyer and date added (Russmedia Equity Partners, 2 Jun 2021), matching case-ebay-classifieds.
- Veldmark worked question: changed from a hypothetical 2029 Hearthly sale to the ledger's canonical stressor (investor's Nov 2027 question about a 2030 Hearthly sale; Ingrid's Dec 2027 estimate: 7 shared capabilities, 9–12 months of TSAs with the separability rules, 20+ without); cited tenancy model v1's exit-path rule; linked [[multi-country-platforms]] and [[long-term-evolution]]. Hearthly on Google Cloud qualified "through at least 2028".
- Expanded OCR and EU5 on first use; "catalogue" → "catalog" (3).

## case-olx

- Timeline 2014: noted that Schibsted's OLX Brazil stake passed to Adevinta in 2019 (agrees with Phase 2 and case-adevinta).
- Margin table note: added Prosus's "8pp expansion", implying about 40% aEBITDA margin in FY25.
- Pay&Ship row: noted that the 2023 post does not name the payment provider or licensed party.

## case-ebay-classifieds

- Payments layer: OPP at Kleinanzeigen dated to July 2023 (t3n); Adyen switch "some time after July 2023, not public"; Kleinanzeigen help page added to Sources.
- CMA paragraph: acceptance date 2 Jun 2021 and Shpock buyer added.
- Worked question: tied the dependency register to tenancy model v1's exit paths and the separability tabletops in [[long-term-evolution]].
- PaaS expanded in KEY POINTS; "licence" → "license" (2), "programme" → "program"; timetoread 34 → 36 (page grew; about 8,400 words before Sources incl. tables).

## Cross-case consistency (checked, consistent)

2021 sale terms (US$9.2bn / US$2.5bn cash + 540m shares; €130–165m vs US$150–185m stated as guidance vs estimate); completion 25 Jun 2021; Denmark €278m to Schibsted; Gumtree UK 1 Dec 2021; Kleinanzeigen rename 16 May 2023 and €15m cost; Marktplaats payments from 2017 via OPP, Gelijk Oversteken withdrawn Apr 2022; OLX Brasil 50/50 JV; Veldmark facts (Common Ground, OpenSearch/Elasticsearch decision, Keybridge, Safe Deal €75m on Adyen for Platforms, Polish dealer overlap, Tradeyard PT 1.1M live / 210k weekly) all match the ledger.

## Open issues for the author / other parts

- Lengths: prose before Sources is about 7,800 / 7,700 / 8,400 words including tables — above the 7,000 case target; no clear repetition found worth trimming.
- Kijiji €147m impairment (OnlineMarketplaces, 2024) and Gumtree South Africa to Impresa Capital (Jul 2022) are trade-press only; not re-verified.
- willhaben sale completion and the mobile.de dual track remain unconfirmed as of Oct 2026 (already flagged in case-adevinta).
- Other chapters' Kleinanzeigen/Marktplaats provider statements (ch. 01, 29, 41) looked consistent with item 2 in a grep; not reviewed in depth.
