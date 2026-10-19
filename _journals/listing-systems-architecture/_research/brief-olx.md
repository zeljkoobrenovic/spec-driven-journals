# Research brief: OLX Group (Prosus): history, footprint, economics and engineering

Prepared 19 October 2026 for chapter writers of *Architecting Listing Systems: Engineering Large-Scale Classifieds and Marketplace Platforms*. OLX is documented here as a case study. It is unusually useful for the book for three reasons:

1. It is one of the few classifieds groups that has gone through **every major portfolio move**: global roll-up, regional mergers, a failed vertical-integration bet (OLX Autos), forced exit (Russia), carve-outs into joint ventures (US, MENA/South Asia, Brazil) and a final retreat to a compact European core.
2. Its parent, Prosus, **reports OLX's revenue and profit separately**, so the economics of a focused classifieds business can be read from primary filings.
3. Its engineering blog (tech.olx.com, a Medium publication) has published concrete search, ranking, recommendation, trust-and-safety and infrastructure write-ups from **2018 to August 2026**. That makes it possible to trace how one company's listing stack evolved.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: I fetched the page during this research session (19 October 2026) and it supports the claim. Paraphrases stay close to the source. Quoted text is quoted. Publication dates are given for all technical evidence.
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (press, trade press, analyst note, encyclopedia), not primary documentation.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. **Every architectural inference about OLX's proprietary internals is tagged this way.** Do not print it as fact.

**How the engineering-blog evidence was obtained.** tech.olx.com returns HTTP 403 to automated fetches.
- The ten most recent posts (June 2025 to August 2026) were read in full from the publication's own RSS feed (`https://tech.olx.com/feed`).
- Older posts were read from Internet Archive copies of the original tech.olx.com URLs. For those, the cited URL is the original tech.olx.com URL. The publication date comes from the page's own `datePublished` metadata.
- Two linked posts could not be retrieved. Both are listed under Open questions:
  - "The evolution of image model serving at OLX"
  - "Replicating MySQL tables on S3 as Parquet (DanaDB)"

**Research limitation.** The session's shared web-search quota ran out partway through. After that point, only known URLs were fetched directly; no new searches were made. The following topics could not be researched and are flagged as gaps rather than filled with guesses:
- Experimentation platform naming
- Event-tracking pipeline naming
- "OLX Magic"
- OLX Europe's internal platform names
- Detailed Kafka, Kubernetes or observability write-ups

**Evidence age matters.** OLX's engineering posts span **eight years and three different OLX organizations**:
- Pre-2020 global OLX, including India, Indonesia, Pakistan, South Africa and LatAm
- OLX Autos, 2019–2023
- Today's OLX Europe plus South Africa

Several posts describe markets OLX no longer owns. Each system description below says which era it comes from, and whether it is likely to have been replaced.

**Volatility flags.** ⚠ marks facts likely to change within about 12 months: ownership, deal closings, product names, AI metrics, guidance.

---

## PART 1: Corporate history

### 1.1 Timeline

| Date | Event | Evidence |
| --- | --- | --- |
| 2006 | OLX founded by **Fabrice Grinda and Alec Oxenford** as a Craigslist alternative outside the US. Name said to derive from "OnLine eXchange". Same year, acquires Mundoanuncio.com (Hispanic classifieds). | [WIDELY REPORTED: https://en.wikipedia.org/wiki/OLX, 2026] |
| 2007 | Avito founded in Moscow by Swedish entrepreneurs Jonas Nordlander and Filip Engelbert. Avito merges into the group story later. | [WIDELY REPORTED: https://en.wikipedia.org/wiki/Avito.ru, 2026] |
| 2010 | **Naspers acquires a majority stake** in OLX. | [WIDELY REPORTED: https://en.wikipedia.org/wiki/OLX, 2026] |
| 2013 | Avito merges with Slando.ru and OLX.ru "to become the Russian market leader for classified ads". | [WIDELY REPORTED: https://en.wikipedia.org/wiki/Avito.ru, 2026] |
| 2013 | Naspers buys a 51% stake in dubizzle (UAE) for $120m. | [WIDELY REPORTED: search summary of Arabian Business/Wamda coverage, 2018–2020; not fetched] |
| 2014 | Naspers raises its OLX stake to **95%**. Mass rebranding of acquired local brands to OLX: Romania, Bulgaria, Kazakhstan, Belarus, Hungary and Poland in April 2014 (Poland's Tablica.pl became OLX.pl); Tokobagus (Indonesia) in March; Slando.ua (Ukraine) joins in September. November 2014: Naspers–Schibsted joint venture to co-own **OLX Brazil**. | [WIDELY REPORTED: https://en.wikipedia.org/wiki/OLX, 2026]. The Tablica.pl detail is [ASSUMPTION/JUDGEMENT]. |
| 2016 | Naspers consolidates its classifieds operations under **OLX Group**, Amsterdam-headquartered, Dutch-domiciled. | [WIDELY REPORTED: https://en.wikipedia.org/wiki/OLX, 2026] |
| Feb–Sep 2018 | Exits from Nigeria (Feb) and Venezuela (Sep). | [WIDELY REPORTED: https://en.wikipedia.org/wiki/OLX, 2026] |
| Apr 2018 | Group buys the remaining 49% of dubizzle for $190m. | [WIDELY REPORTED: search summary of Wamda/Arabian Business coverage; not fetched] |
| Jan 2019 | Naspers takes **full control of Avito**, paying $1.16bn for 29.1%. | [WIDELY REPORTED: https://en.wikipedia.org/wiki/Avito.ru, 2026] |
| Apr 2019 | Jiji acquires OLX's businesses in Kenya, Ghana, Uganda, Tanzania and Nigeria. Carousell acquires OLX Philippines, and OLX takes a 10% stake in Carousell. | [WIDELY REPORTED: https://en.wikipedia.org/wiki/OLX, 2026] |
| 2019 | OLX takes a **controlling stake in Frontier Car Group** (car-buying "instant offer" business) through a ~$400m investment, valuing FCG at ~$700m. OLX had been a smaller strategic investor in 2018. This becomes **OLX Autos**. | [VERIFIED: https://techcrunch.com/2021/03/29/prosus-classifieds-group-olx-shuts-down-berlins-frontier-car-group-to-focus-olx-autos-on-latam-and-asia/, published 2021-03-29] |
| 25 Oct 2019 | OLX acquires **Inmokey**, real-estate agency software from Mar del Plata, Argentina, with 1,500+ agents (Argentina, Ecuador, Peru). It is an early example of OLX buying **pro-tools SaaS** for real estate. | [VERIFIED: https://www.olxgroup.com/news/olx-group-acquires-inmokey-a-solid-commitment-towards-user-oriented-technology/, published 2019-10-25] |
| 24–25 Mar 2020 | **OfferUp and letgo combine their US businesses.** OfferUp operates the combined business from Bellevue, WA, under Nick Huzar. OLX Group owns **40%** and leads a $120m round. "letgo's business outside of North America will remain separately owned and operated" by OLX. | [VERIFIED: https://www.olxgroup.com/news/offerup-and-letgo-combine-us-marketplaces-to-deliver-a-better-buying-and-selling-experience-for-more-than-20-million-monthly-users/, published 2020-03-25]. Closing reported as 21 Sep 2020 [WIDELY REPORTED: search summary of a deal database; not fetched]. |
| 2 Jun 2020 | **EMPG + OLX MENA/South Asia merger.** OLX contributes dubizzle plus OLX Egypt, Lebanon, Pakistan and several GCC countries to Emerging Markets Property Group (Bayut, Zameen, Bproperty, Mubawab, Kaidee). The Dubai-based company is valued at ~$1bn, with a $150m round. **OLX holds 39%**, the largest single shareholder. The combined company later trades as Dubizzle Group. | [VERIFIED: https://www.wamda.com/index.php/en/2020/06/empg-reveals-details-merger-olx, published 2020-06-02]. Dubizzle Group naming is [WIDELY REPORTED]. |
| 30 Oct 2020 | **OLX Brazil**, a 50/50 JV of Adevinta and Prosus, completes the acquisition of 100% of **Grupo ZAP** (ZAP, Viva Real) for ~R$2.9bn. The combined business has ~1,600 staff (~400 tech), ~14m real-estate ads and ~70m monthly visits. | [VERIFIED: https://www.olxgroup.com/news/olx-brazil-completes-the-acquisition-of-100-of-grupo-zap/, published 2020-11-19] |
| 7 Dec 2020 | OLX completes acquisition of **Kiwi Finance**, the largest credit broker in Romania. | [VERIFIED: https://www.olxgroup.com/news/olx-group-successfully-acquires-kiwi-finance-the-largest-credit-broker-in-romania/, published 2020-12-07] |
| 25 Feb 2021 | OLX acquires **Obido** (Poland), a new-build ("primary market") developer-to-buyer platform with AI-supported matching. The brand is retained. | [VERIFIED: https://www.olxgroup.com/news/olx-group-acquires-obido-an-innovative-real-estate-platform-for-the-primary-market/, published 2021-02-25] |
| 29 Mar 2021 | OLX closes FCG's Berlin entity. ~100 roles and core product development move to India. OLX Autos focuses on **Latin America and Asia** (Argentina, Chile, Colombia, Ecuador, India, Indonesia, Mexico, Peru) plus CarFirst (Pakistan), Cars45 (Nigeria) and webuyanycar.com (US). | [VERIFIED: TechCrunch, published 2021-03-29, as above] |
| 2021 | Romain Voog becomes CEO. | [WIDELY REPORTED: https://en.wikipedia.org/wiki/OLX, 2026] |
| 14 Oct 2022 | **Avito sold** to Kismet Capital Group subsidiaries for **RUB 151bn**. Prosus held an effective 99%. Closing was expected October 2022. Avito's NAV at 31 Mar 2022 was US$1,379.9m and attributable profit US$160.3m. | [VERIFIED: https://www.naspers.com/news-insights/regulatory-updates/2022/disposal-of-avito-group, published 2022-10-14] |
| 14 Oct 2022 (cont.) | The price is ~US$2.46bn, against a pre-invasion valuation estimate of ~$6bn. | [VERIFIED: https://www.euronews.com/next/2022/10/14/ukraine-crisis-prosus-avito, published 2022-10-14] |
| Jan 2023 | Plan to cut ~15% of the global workforce (~1,500 roles). | [VERIFIED: https://techcrunch.com/2023/06/20/olx-group-layoffs, published 2023-06-20] |
| 2 Mar 2023 | Prosus announces it will **exit OLX Autos**. It cites "higher cost of capital, high inflation and a reversal of pandemic trends" and a "significant and persistent slowdown" in used cars. OLX Autos revenue was $1.6bn in FY22 (+158%), just over half of classifieds revenue, with ~175k cars transacted. H1 FY23 trading losses widened to $206m. AutoTrader (South Africa) is not part of OLX Autos. | [VERIFIED: https://www.news24.com/fin24/companies/prosus-looks-to-ditch-olx-autos-business-as-second-hand-car-market-slows-20230302, published 2023-03-02] |
| 20 Jun 2023 | ~**800 roles** cut. OLX Autos stops new purchasing in Argentina, Mexico and Colombia. Chile, LatAm financing, and classifieds plus Autos transaction businesses in India, Indonesia and Turkey are pursued as individual sales. | [VERIFIED: https://techcrunch.com/2023/06/20/olx-group-layoffs, published 2023-06-20] |
| Aug 2023 | **OLX India sold to CarTrade** (₹535.54 crore). The **Indonesian business sold to Astra International.** | [WIDELY REPORTED: https://en.wikipedia.org/wiki/OLX, 2026] |
| FY24–FY25 | OLX Chile, Colombia and Mexico disposals appear in the Prosus FY25 list of disposals. All OLX Autos operations are "disposed of, classified as held for sale or closed by 31 March 2025". FY25 discontinued-operations loss was US$128m, including US$84m impairment on the US operation held for sale. | [VERIFIED: Prosus FY25 results booklet, copy at https://www.lobbyregister.bundestag.de/media/57/dc/638531/prosus-financial-results-fy25-booklet.pdf, published 2025-06] |
| Apr 2024 | **Christian Gisy** named OLX Group CEO. | [WIDELY REPORTED: https://en.wikipedia.org/wiki/OLX, 2026]. Gisy's CEO role is confirmed in 2025–26 releases [VERIFIED: https://www.olxgroup.com/?p=4285, published 2025-11-24] |
| 1 Aug 2025 | Sale of **Kiwi Finance** (Romania) closed. | [VERIFIED: https://www.olxgroup.com/?p=5024, published 2026-06-29] |
| Aug 2025 | Final OLX Autos operation sold. | [WIDELY REPORTED: https://www.onlinemarketplaces.com/articles/olx-revenue-climbs-to-992m-as-prosus-folds-classifieds-into-europe/, 2026] |
| 4 / 21 Aug 2025 | Agreement to sell **OLX Uzbekistan** (100%) to a JV led by TBC Bank Group (50% + 1 share) with Titan Investments. OLX UZ had 5.4m MAU, 2.2m active listings and was the 6th most-visited site in Uzbekistan. Rationale: "sharpen our focus on core product categories and geographies" (Gisy). | [VERIFIED: https://www.olxgroup.com/news/olx-group-to-sell-olx-uzbekistan-to-a-joint-venture-led-by-tbc-bank-group/, published 2025-08-21]. The FY26 release dates the agreement 4 Aug 2025. |
| 26 Sep 2025 | OLX agrees to buy **La Centrale** (France, motors) from Providence Equity for **€1.1bn** cash. This is OLX's first move into Western Europe. | [WIDELY REPORTED: search summary of Prosus SENS / BusinessDay coverage, 2025-09-26; not fetched]. Price and closing confirmed below. |
| 21–23 Oct 2025 | Agreement to sell **OLX Kazakhstan** to VEON's Beeline Kazakhstan for **$75m**, expected to close Q1 2026. | [VERIFIED: https://www.onlinemarketplaces.com/?p=104706, published 2025-10-23]. ⚠ Closing not verified. |
| 29 Oct 2025 | Agreement to sell **Fixly** (Poland, services marketplace). | [VERIFIED: https://www.olxgroup.com/?p=5024, published 2026-06-29]. ⚠ Buyer and closing not verified. |
| 17 Nov 2025 | **La Centrale acquisition closed.** | [VERIFIED: https://www.olxgroup.com/?p=4285, published 2025-11-24] |
| 13 May 2026 | **Otodim** launched (beta) in Ukraine: a dedicated real-estate search platform drawing on OLX Ukraine inventory. | [VERIFIED: https://www.olxgroup.com/news/olx-group-launches-otodim-platform-in-ukraine-deepening-commitment-to-the-countrys-real-estate-market/, published 2026-05-13] |

### 1.2 What the brief asked about, and what the evidence actually says

- **"Merger with Avito/Letgo/dubizzle/Property24/Storia/Otodom/Otomoto/Imovirtual/Standvirtual."** These were never one merger. They were assembled across roughly 2010–2016 through acquisitions and rebrandings under Naspers' classifieds division, then consolidated under the OLX Group legal and operating umbrella in 2016. The vertical brands (Otodom, Otomoto, Storia, Autovit, Imovirtual, Standvirtual) kept their own consumer brands. [WIDELY REPORTED: https://en.wikipedia.org/wiki/OLX, 2026; ASSUMPTION/JUDGEMENT on the exact acquisition dates of each vertical brand, which were not verified in this session]
- **letgo** was a Naspers/OLX-funded app. It was combined with OfferUp in the US in 2020. The non-US letgo business (notably Turkey) stayed with OLX. Turkey was among the countries named for sale in 2023. [VERIFIED: OfferUp release 2020-03-25; TechCrunch 2023-06-20]
- **Property24** (South Africa) remains a Prosus classifieds asset and appears in Prosus's real-estate disclosures. [VERIFIED: https://www.onlinemarketplaces.com/articles/prosus-hy-2026-real-estate-revenues-up-26-as-olx-sees-healthy-growth/, published 2025-11-24]. Whether it is operated by OLX Group or reported alongside it is not clear from the sources I fetched. Prosus' FY25 segment table shows a separate "OLX South Africa" line (revenue US$52m in FY25). [VERIFIED: Prosus FY25 booklet]
- **Russia.** OLX/Prosus fully exited Russia with the Avito sale in October 2022. [VERIFIED: Naspers, 2022-10-14]

### 1.3 The portfolio arc in one sentence

From ~45 markets in 2018 ("a network of leading classifieds platforms in 45 markets, encompassing such brands as OLX, Avito, Letgo, and Dubizzle") [VERIFIED: https://tech.olx.com/understanding-language-through-search-78ea37be7ac8, published 2018-11-05] to **seven markets** in FY26: Bulgaria, France, Poland, Portugal, Romania, South Africa and Ukraine. [VERIFIED: https://www.olxgroup.com/?p=5024, published 2026-06-29]

[ASSUMPTION/JUDGEMENT] For the book, OLX is the clearest public example of a classifieds group concluding that (a) **local leadership in a few markets beats global breadth**, and (b) **inventory-owning transaction models (instant car buying) do not combine well with high-margin listing businesses** once capital gets expensive.

---

## PART 2: Current footprint (as of October 2026) ⚠

### 2.1 Markets and brands

| Market | Brands (consumer-facing) | Notes | Evidence |
| --- | --- | --- | --- |
| Poland | OLX.pl (general, jobs), **Otomoto** (motors), **Otodom** (real estate), Obido (new-build) | Largest European market. Otomoto is the first AutoIQ and AutoGPT market. OLX Poznań office hosts engineering. | [VERIFIED: AutoGPT release 2026-04-02; Obido release 2021-02-25; tech.olx.com Masterclass post 2026-02-25] |
| Romania | OLX.ro, **Autovit.ro**, **Storia.ro** | Kiwi Finance sold Aug 2025 | [VERIFIED: onlinemarketplaces HY26 article 2025-11-24; FY26 release] |
| Portugal | OLX.pt, **Standvirtual**, **Imovirtual** | First CompassGPT market (Imovirtual) | [VERIFIED: CLAIM AI release 2026-06-29] |
| Bulgaria | OLX.bg | | [VERIFIED: FY26 release] |
| Ukraine | OLX.ua, **Otodim** (beta, May 2026) | 150+ employees. Active users at 92% of 2021 level in 2025. | [VERIFIED: Otodim release 2026-05-13] |
| France | **La Centrale** (motors) | Acquired Nov 2025. +13% traffic and +30% leads YoY reported in FY26. | [VERIFIED: FY26 release 2026-06-29] |
| South Africa | Property24, AutoTrader (SA), OLX South Africa line in Prosus accounts | Whether all three are under OLX Group management is not verified | [VERIFIED: FY26 release lists South Africa; Prosus FY25 booklet; fin24 2023-03-02 for AutoTrader] |

**No longer OLX markets (verify before using older engineering posts as "current"):**
- Kazakhstan: sale agreed Oct 2025 ⚠
- Uzbekistan: sale agreed Aug 2025 ⚠
- India and Indonesia: sold 2023
- Pakistan, Egypt, Lebanon, GCC: contributed to EMPG/Dubizzle Group in 2020, where OLX holds a minority stake
- US: OfferUp, 40% stake
- Brazil: OLX Brasil, a 50% JV with Adevinta
- LatAm Autos: closed or sold
- Russia: Avito sold in 2022

The brief's mention of Kazakhstan and Uzbekistan as part of the 2026 footprint is therefore **out of date**. [VERIFIED: FY26 release]

### 2.2 Scale indicators (company-reported)

| Metric | Value | Period | Evidence |
| --- | --- | --- | --- |
| Daily active listings | ~64m | FY25 | [VERIFIED: https://www.olxgroup.com/news/olx-group-reports-strong-fy-2025-results-with-18-revenue-growth-and-61-profit-uplift-year-on-year/, published 2025-06-23] |
| Monthly app users | 29m | FY25 | [VERIFIED: same] |
| "Nearly 60 million daily listings" | ~60m | H1 FY26 and FY26 (after the Central Asia exits) | [VERIFIED: https://www.olxgroup.com/?p=4285, 2025-11-24; https://www.olxgroup.com/?p=5024, 2026-06-29] |
| Monthly app users / active listings (engineering blog) | 45m app users, 73m+ active listings | Mid-2025 | [VERIFIED: https://tech.olx.com/scaling-recommendations-service-at-olx-db4548813e3a, RSS pubDate 2025-07-08] |
| Brands / markets | "nine brands in nine markets" | FY25 | [VERIFIED: FY25 release 2025-06-23] |

[ASSUMPTION/JUDGEMENT] The gap between "29m monthly app users" (FY25 corporate) and "45m app users" (engineering blog, mid-2025) is probably a difference of definition (unique vs. per-brand counts, or including Central Asia). Writers should cite one figure with its source and period, not mix them.

### 2.3 Verticals and strategic focus

- OLX is "focusing its efforts on high-growth categories such as motors, real estate and jobs." [VERIFIED: Prosus FY25 booklet]
- **Motors.** "Enhanced monetisation efforts and innovative products like dealer tools, as well as trust-building initiatives such as providing vehicle history transparency and dealer ratings." [VERIFIED: same]
- **Real estate.** Growth was "propelled by product enhancements, including the rollout of a unified platform, fully reimagined app and tools optimised for agents." [VERIFIED: same]
- **Jobs.** "AI-enabled products such as candidate-employer matching", with an ambition in "blue- and grey-collar job markets across Poland, Romania and Ukraine." [VERIFIED: same]
- **Car parts** is called out as a growth area in Central and Eastern Europe, with "compatibility features". [VERIFIED: same]
- **Delivery de-prioritised.** "The second half of the year saw a shift in strategy, marked by the **de-prioritisation of pay-and-ship in Europe**." [VERIFIED: same]. See Part 3.8.
- In FY26, motors, real estate and jobs reached **71% of revenue**. [VERIFIED: FY26 release 2026-06-29]

---

## PART 3: Financials as reported by Prosus and OLX ⚠

### 3.1 Headline numbers

| Period | Revenue | Growth | Profit measure | Margin | Evidence |
| --- | --- | --- | --- | --- | --- |
| FY24 (to 31 Mar 2024) | n/a in the sources fetched; FY25 growth implies ~US$660m | — | aEBIT margin 25% | 25% | [VERIFIED: Prosus FY25 booklet] |
| **FY25** (to 31 Mar 2025) | **US$777m** | +18% (18% local currency) | aEBIT **US$270m**, +63% (+61% LC) | **35%** aEBIT | [VERIFIED: Prosus FY25 booklet; OLX FY25 release 2025-06-23] |
| H1 FY26 (to 30 Sep 2025) | **US$473m** (from US$389m) | +22% (+17% LC ex-M&A) | adj. EBITDA US$231m (+52%); aEBIT US$205m (+59%) | **49%** adj. EBITDA | [VERIFIED: https://www.olxgroup.com/?p=4285, published 2025-11-24] |
| **FY26** (to 31 Mar 2026) | **US$992m** (from US$777m) | +28% (+16% LC ex-M&A) | adj. EBITDA +53% (+38% LC); margin +8pp | ~48% adj. EBITDA | [VERIFIED: https://www.olxgroup.com/?p=5024, published 2026-06-29] |
| FY26 (trade press) | — | — | adj. EBITDA **US$481m** (from US$314m); aEBIT **US$427m** | 48% | [VERIFIED: https://www.onlinemarketplaces.com/articles/olx-revenue-climbs-to-992m-as-prosus-folds-classifieds-into-europe/, published 2026-06-29] |
| FY26 (analyst) | — | "16% in local currency" | adj. EBITDA margin "improving 800bps to 48%" | 48% | [VERIFIED: Old Mutual "Aperture" note on Prosus FY26, https://www.oldmutual.co.za/om-docs/blt9aa45c31c7ec5847/Aperture_Prosus_FY_2026_Results.pdf, 2026-07] |

**Vertical growth:**

| Vertical | FY25 | H1 FY26 | FY26 |
| --- | --- | --- | --- |
| Motors | +24% LC | +27% | **+42%** (La Centrale-assisted) |
| Real estate | +23% LC | +26% | +26% |
| Jobs | n/a | +12% | +14% |

[VERIFIED: Prosus FY25 booklet; https://www.olxgroup.com/?p=4285; https://www.olxgroup.com/?p=5024]

### 3.2 Segment detail (Prosus FY25)

The FY25 constant-currency reconciliation tables split Classifieds into lines. [VERIFIED: Prosus FY25 booklet, segmental tables]

| Line | FY24 revenue | FY25 revenue | FY24 trading profit | FY25 trading profit |
| --- | --- | --- | --- | --- |
| OLX Europe | US$610m | **US$725m** | US$176m | **US$260m** |
| OLX South Africa | US$46m | US$52m | US$27m | US$30m |

- OLX Europe revenue grew +19% in local currency.
- OLX Europe trading profit grew +47% to +48%.
- [ASSUMPTION/JUDGEMENT] OLX Europe's FY25 trading margin was therefore ~36%. In H1 FY26 the adjusted-EBITDA margin reached 49%, after Central Asia (lower-ARPU) was removed and price increases landed. This is a textbook case of a "**focus and monetize**" phase in classifieds.

### 3.3 Reporting changes and pitfalls

- From FY26, OLX "is now shown as a single line within Prosus's European operations." Earlier disclosures split out country figures such as OLX Brazil and OLX Poland. [VERIFIED: onlinemarketplaces, 2026-06-29]
- **OLX Brasil is a 50% JV with Adevinta**, not an OLX Group subsidiary. Prosus lists it as "OLX Brazil (50%)". [VERIFIED: OLX Brazil/ZAP release 2020-11-19; onlinemarketplaces HY26 article 2025-11-24]
- Trade-press claims that OLX Brasil is "included within the European presentation" are confused. Writers should not repeat them. [ASSUMPTION/JUDGEMENT: equity-accounted JVs are not consolidated into segment revenue]
- **Metric names change between periods.** FY25 uses aEBIT ("trading profit"). H1 FY26 and FY26 lead with adjusted EBITDA. Do not compare a 35% aEBIT margin with a 49% EBITDA margin as if they were the same measure. [ASSUMPTION/JUDGEMENT]
- **Guidance.** Management stated an "ambition... to sustain strong revenue growth at over 20% while enhancing the profit margin to near 50%". [VERIFIED: Prosus FY25 booklet] ⚠
- **Prosus context.** FY26 ecosystem revenue was ~US$9.7bn, with organic growth of 12% "through strong growth in iFood in Latin America and OLX in Europe". [VERIFIED: Old Mutual note, 2026-07]

### 3.4 OLX Autos economics, for contrast

- FY22: OLX Autos revenue $1.6bn, +158%, "just over half of the classifieds business's revenue".
- H1 FY23: trading losses $206m. [VERIFIED: fin24 2023-03-02]
- H1 FY22: OLX Autos grew revenue 84% to $1bn but "had not yet reached profitability". [VERIFIED: TechCrunch 2023-06-20]
- [ASSUMPTION/JUDGEMENT] The lesson for the book: **revenue from transacting inventory is not comparable to listing revenue.** OLX Autos briefly doubled reported revenue while destroying margin. When it was removed, reported revenue fell and profitability rose sharply.

---

## PART 4: Engineering. What OLX has published

### 4.0 Engineering-evidence map (by era)

| Era | Org context | Posts used in this brief | Still current? |
| --- | --- | --- | --- |
| 2018–2019 | Global OLX (SA, India, Pakistan, Indonesia, LatAm) | Query2vec synonyms (SA); LTR intro; Step Functions ML pipeline | **Mostly historical.** Markets divested except SA. |
| 2020–2021 | OLX Europe + OLX Autos + Asia | Duplicate detection; fraud rings; Dali image service; Jobs recommender; Autosuggest; Data Science overview; Cassandra chat; JFR on K8s (Autos); Item2Vec; XAI | **Mixed.** Europe items likely evolved. Autos and India items are historical. |
| 2022–2024 | OLX Europe | Solr LTR (Jun 2022); delivery time ML (May 2023); GenAI job-role extraction (Jan 2024); Pact (Jun 2024) | **Likely partly current**, extended |
| 2025–2026 | OLX Europe | LambdaMART/XGBoost (Feb 2025); Hydra/LTR monorepo (Jun 2025); GST experimentation (Aug 2025); recommendations service at scale (Jul 2025); hybrid search (Sep 2025); embedding evaluation (Oct 2025); frontend single-repo multi-brand (Feb 2026); Work Organization Framework at OLX Motors (Mar 2026); Web Locks (Jul 2026); causal inference on boosts (Aug 2026); agent-context experiment (Aug 2026) | **Current** |

### 4.1 Platform and architecture: monolith, microservices, languages

**What is published:**

- **Go and PHP coexist; the PHP side is legacy.** An August 2026 post on coding agents describes a realistic change touching "around 18–20 files across three codebases". The specialists set up for that experiment include "backend-service-a.md # specialist for the first Go service", "backend-service-b.md # specialist for the second Go service" and "backend-service-c.md # specialist for the PHP service". The codebases "have years of history and firm architectural conventions", documented in per-repo `AGENTS.md` files. [VERIFIED: https://tech.olx.com/does-it-matter-how-you-feed-an-agent-its-context-ee1519586520, RSS pubDate 2026-08-21]
- **Microservices with contract testing.** OLX adopted **Pact** consumer-driven contract testing for REST interactions "as part of a technical journey using a microservices-based architecture". It uses a standardized pipeline, mock providers and a Pact **broker**, and aims to "expand and explore asynchronous interactions". [VERIFIED: https://tech.olx.com/journey-to-contract-testing-through-pact-04a39a3fcc22, published 2024-06-24]
- **Service-estate hygiene at OLX Motors (2024–25).** A March 2026 post lists outcomes of the "Work Organization Framework" (WOF) for Product, Data, Marketing and Tech initiatives. [VERIFIED: https://tech.olx.com/empowering-innovation-through-structure-93c15614f6d3, RSS pubDate 2026-03-18]
  - Pipeline times cut by up to 44%, "saving teams 94 hours per week".
  - A unified Notification Center replaced varied deployment notifications "across 60+ services". It sends consistent updates to **Slack, New Relic, OpsLevel and Sentry**.
  - 45+ components migrated to **AWS Secrets Manager**.
  - "Full EU backup compliance for all Tier 1 and 2 databases".
  - **User identification standardized across 71 services, "with 73% now using modern UUIDs instead of legacy user IDs"**.
  - Tailwind v4 rolled out. Automated accessibility testing cut main listing page violations from 120 to 43.
- **Frontend: one repo, many brands.** A February 2026 Poznań masterclass talk: "One-product, three brands — Our strategy for serving different countries from a single repo… how we efficiently manage multiple websites from a single repository, balancing localisation, configuration, and design to cater to the unique needs of our international brands." [VERIFIED: https://tech.olx.com/olx-masterclass-frontend-2026-068299a2df50, RSS pubDate 2026-02-25]
- **Frontend stack.** React and Next.js. [VERIFIED: https://tech.olx.com/handling-concurrency-on-the-web-with-web-locks-api-163b7e07eddd, RSS pubDate 2026-07-14]
- **Unified real-estate platform.** Prosus FY25 credits real-estate growth partly to "the rollout of a unified platform". [VERIFIED: Prosus FY25 booklet; OLX FY25 release 2025-06-23]

**Not verified in this session:**
- A named "OLX Europe shared platform" programme
- The specific Otodom/Storia/Imovirtual and Otomoto/Autovit/Standvirtual consolidation mechanics
- The PHP→Go migration timeline
- Job-ad evidence (seen only in search-result snippets, not fetched) states that a Motors team works on "a legacy in PHP to a microservices architecture on Golang, Kafka and GraphQL" and runs "entirely on Amazon Web Services". Treat as [WIDELY REPORTED / ASSUMPTION]. Re-verify from a live posting before printing.

**Reference-architecture inference** [ASSUMPTION/JUDGEMENT]. The combined evidence is consistent with a common classifieds pattern:
- **One codebase per vertical, serving several country brands.** Otomoto, Autovit and Standvirtual on one motors stack; Otodom, Storia and Imovirtual on one real-estate stack. Brand, locale and taxonomy are configuration.
- The "three brands" in the 2026 frontend talk and the "unified platform" in real estate both point this way.
- **A legacy PHP core is being strangled by Go services.** Kafka is the event backbone and GraphQL is the client-facing aggregation layer.
- **Identity was historically per-platform.** That is why user IDs had to be standardized to UUIDs across 71 services.

Writers should present this as an inference, not as OLX's documented architecture.

### 4.2 Cloud, Kubernetes and observability

- **AWS-first.** "It's not a secret that OLX works heavily on top of AWS, thus Sagemaker is currently the first stop when problems arise." [VERIFIED: https://tech.olx.com/building-an-aws-serverless-ml-pipeline-with-step-functions-b39feed12bab, published 2019-04-15]
- The 2018 CTO talk (Olaf Zschiedrich, GOTO Berlin 2018) covered "designing a data lake/reservoir architecture on AWS", "collecting and storing billions of events and records per day" and SageMaker/TensorFlow. [VERIFIED: https://gotopia.tech/sessions/652/from-big-data-mess-to-data-as-an-innovation-enabler, 2018]
  - "Reservoir" appears there as a generic term. **No evidence was found that OLX's data lake is named "Reservoir".**
- **Kubernetes on AWS at scale (2020).** OLX's image-processing services "run in Kubernetes on AWS". At peak (~30,000 req/s on the busiest cluster), the earlier thumbor-based processor needed "~6000 pods". [VERIFIED: https://tech.olx.com/presenting-dali-an-image-processor-service-514e6be00de8, published 2020-02-25]
- **Kubernetes at OLX Autos (2021).** "We run a lot of JVM workloads in our Kubernetes cluster… Java or Kotlin". New Relic was the primary APM, and Java Flight Recorder was adopted for in-cluster profiling. [VERIFIED: https://tech.olx.com/jvm-profiling-in-kubernetes-with-java-flight-recorder-b39a6181a99c, published 2021-04-15]. **Historical.** OLX Autos is closed.
- **Observability tooling (current).**
  - New Relic: event-loop diagnostics on the recommendations service. [VERIFIED: recommendations post, 2025-07-08]
  - Sentry and OpsLevel (service catalog), as deployment notification targets. [VERIFIED: WOF post, 2026-03-18]
- **Kubernetes scheduling.** The recommendations service deploys with "topology spread constraints and node selectors". [VERIFIED: recommendations post, 2025-07-08]
- **Load shedding at the edge.** A two-part 2021 post, "Load shedding with NGINX using adaptive concurrency control", exists on tech.olx.com (sitemap, 2021-02-25). It **could not be retrieved**. Cite only its existence.

### 4.3 Search: retrieval, ranking, autosuggest

This is OLX's best-documented area and maps directly onto the book's search chapters.

**Engine: Apache Solr (BM25 + Solr LTR plugin).**

- 2022: "We're exploiting the capabilities of our search engine **Solr**, namely **Solr LTR plugin**."
  - Features live in the ads collection. Some are computed at query time (text similarity), others "refreshed periodically (e.g. CTR)".
  - The model is a **LambdaMART** (XGBoost) converted to a Solr MART model.
  - [VERIFIED: https://tech.olx.com/learning-to-rank-sorting-search-results-b21a8bd48808, published 2022-06-22]
- 2025: "Our existing search architecture already included keyword matching, implemented in **SOLR using BM25 scoring**." [VERIFIED: https://tech.olx.com/hybrid-search-where-keywords-meet-vectors-enabling-classifieds-discovery-b7c383fe4fc4, RSS pubDate 2025-09-09]
- Autosuggest (2020, global markets) also ran on a Solr `SuggestComponent`, using infix, blended-infix and fuzzy lookups. [VERIFIED: https://tech.olx.com/autosuggest-retrieval-ranking-part-2-14a8f50fef34, published 2020-12-22]
- No evidence was found of an Elasticsearch/OpenSearch migration in Europe. A job posting mentions both engines as acceptable experience. [WIDELY REPORTED: search snippet of an OLX Lever job posting, 2025–26; not fetched]

**Ranking evolution (a clean four-stage story):**

| Stage | When | What | Evidence |
| --- | --- | --- | --- |
| 0. Sort by date/price only | Before ~2021 (Europe) | "Less than a year ago it wasn't possible to sort search results by any criteria other than ad age or price." | [VERIFIED: LTR post 2022-06-22] |
| 1. Hand-tuned formula | ~2021 | "Recommended" sort. Text similarity + ad statistics (CTR) + temporal features, "hand-crafted into a simple formula". Making CTR available to ranking "was no joke". | [VERIFIED: same] |
| 1b. (Global, 2019) logistic regression | 2019 | Coefficients "plugged into the ranking function of the existing search engine" to avoid new serving infrastructure; +10% on the key search metric. "Search generates about 80% of total conversions." | [VERIFIED: https://tech.olx.com/ranking-ads-with-machine-learning-ee03d7734bf4, published 2019-05-14] |
| 2. LambdaMART in Solr | 2022 | Labels: purchase **or messages/calls to sellers** ("because transactions aren't always confirmed"). Offline NDCG. Results: +12% conversions on page 1, +5% purchases, +4% unique buyers, and **unique contacted sellers up**. Offline NDCG correlated with online A/B results. | [VERIFIED: LTR post 2022-06-22] |
| 3. Two LTR variants | by 2025 | **"Vanilla LTR"** trained on seller-contact "successful events". **"VAS LTR"** balances "maximizing relevance for users and ensuring visibility for Value Added Services (VAS), ads that have paid for additional exposure". | [VERIFIED: hybrid search post 2025-09-09] |
| 4. Hybrid retrieval | 2025 | BM25 top-1,000 plus a fixed allocation of vector results (35, then 70), re-ranked by an LTR model retrained with query–ad vector similarity as a feature | [VERIFIED: same] |

**LTR as a platform.** LTR is the default "Recommended Ads" sort "on our OLX websites in several countries". It is being tested in Motors and Real Estate. Projects spread across teams and repositories caused "duplicated efforts", so OLX "**centralize[d] all LTR projects within a single repository**" with Facebook's **Hydra** for hierarchical configuration (brand-level configs such as `brand: olx`, `brand: real_estate`). [VERIFIED: https://tech.olx.com/unlocking-flexibility-in-configuration-the-power-of-hydra-3f9e69263bb4, RSS pubDate 2025-06-02]

**Hybrid search details (Sep 2025).** [VERIFIED: hybrid search post 2025-09-09]
- **Problem.** Keyword matching produced "low recall or even zero results pages (ZRPs)". A growing "extension chain" of fallback steps (location expansion, etc.) became "increasingly complex and difficult to improve upon".
- **Embedding models.**
  - Candidates were **mCLIP** (text encoder only, titles, 77-token limit) and **multilingual-e5-small** (titles + descriptions, 512 tokens).
  - Multilingual support was "non-negotiable". A single model across markets was a goal.
  - Initially used "out of the box with no additional fine-tuning".
  - Image embeddings were tried and "quickly dropped after an unsuccessful experiment".
- **Thresholds failed.** Similarity scores "did not consistently separate relevant from non-relevant ads". OLX used a **fixed-size allocation** instead of a threshold.
- **Ranker blindness.** The existing LTR, trained only on keyword-retrieved results, "consistently assigned lower relevance scores to vector search results". This was "particularly problematic for VAS ads retrieved via semantic search". OLX retrained with the similarity feature.
- **Cold-start workaround.** No interaction data existed for vector results in the main flow. OLX shipped a temporary **linear re-ranker** built on the old **Edismax** BM25-weighted function plus recency, which was boosted to protect VAS ads that get "recency resets upon service purchases". The aim of the A/B test was to "do no harm" and collect training data.
- **Rollout path.**
  1. Vector search as a step in the extension chain, in a **smaller market**: >100% increase in seller-contact events per user.
  2. Main-flow A/B/C test failed to converge because of a web tracking bug.
  3. Re-run on apps: ~3% more users with a successful event.
  4. Re-run on mWeb: ~5% more users with a successful event and higher ad CTR.
  5. Full rollout in that market. Next: largest markets, fine-tuning, better blending.

**Embedding model governance (Oct 2025).** [VERIFIED: https://tech.olx.com/importance-of-offline-evaluation-to-guide-model-choice-1c2be1c4599a, RSS pubDate 2025-10-07]
- Model choice was filtered from the MTEB leaderboard by memory and latency constraints, text-only and multilingual: "Portuguese, Polish, Russian, Bulgarian, Ukrainian, and Kazakh".
- The offline dataset was built from consecutive interactions, weighting favorites and chat replies above clicks and recent above old, in BEIR format. **multilingual-e5-small** won in all languages.
- Fine-tuned with Sentence Transformers (MultipleNegativesRankingLoss). Low-resource languages (Uzbek, Kazakh) benefited most.
- **Similarity is not relevance.** The A/B test lost to the incumbent because "location" and "price" were missing. OLX added a re-rank layer (weighted location distance + similarity, grid-searched).
- An in-house **Item2Vec** model had previously been "used by other teams across OLX, such as the search team".

**Older global-era search work (historical; markets divested).**
- **Query2vec synonym expansion (South Africa, 2018).** Skip-gram over in-session query chains. Null searches cut by **27%**. An early version returned "shoes" for "clothes", which led to a stronger evaluation process. [VERIFIED: https://tech.olx.com/understanding-language-through-search-78ea37be7ac8, published 2018-11-05]
- **Autosuggest corpus from user queries (2020).** Results by market:

  | Market | Null searches | Autosuggest adoption | Search conversion |
  | --- | --- | --- | --- |
  | India | −2% | n/a | n/a |
  | Indonesia | −5.1% | +31% | +1.2% |
  | Pakistan | −20% | n/a | +4.1% |
  | South Africa | −5% | n/a | +2.4% |
  | LatAm | n/a | +15.7% | n/a |

  [VERIFIED: autosuggest post 2020-12-22]
- **Search2vec, query categorization and spell checking (Europe, 2020).** OLX.pl had "19 million active listings". [VERIFIED: https://tech.olx.com/data-science-at-olx-7c7406d1713f, published 2020-11-10]

**Jobs search enrichment with GenAI (Jan 2024).** [VERIFIED: https://tech.olx.com/extracting-job-roles-in-job-ads-a-journey-with-generative-ai-e8b8cf399659, published 2024-01-18]
- Job roles were "buried within the titles and descriptions". OLX used **Prosus AI Assistant** (API from July 2023; Prosus has "a special agreement with OpenAI"; "zero-day data retention policy") to build a normalized job-role taxonomy from top searched keywords and extracted roles (Polish market POC).
- **Pipeline.** "A new service subscribed to ad events utilized Prosus AI Assistant to extract job taxonomy information and sent job roles to the **Kinesis** platform used by our Search team." Extracted roles were added to the search index.
- **Volumes.** ~2,000 new or updated ads per day, giving ~4,000 API requests per day.
- **Cost reality check.** "Approximately 15K per month" (currency unstated). This prompted evaluation of self-hosted models.
- **Impact so far.** Retrieval-only. Fewer extensions and fewer keyword searches per user when results were under 50.

### 4.4 Recommendations

| System | When | Design | Results | Evidence |
| --- | --- | --- | --- | --- |
| Jobs recommender (OLX.pl) | 2020 | ALS (Implicit library, chosen over LightFM). **Airflow** orchestrates **AWS Batch** Docker jobs, predictions go to **S3**, **Presto** SQL filters users and active ads. Separate delivery pipeline sends email/push via an internal campaign tool, with a 3-day frequency cap. | ~5% more job applicants, ~2.5% more applications | [VERIFIED: https://tech.olx.com/intro-to-our-jobs-recommender-service-4317b55fc075, published 2020-10-28] |
| Item2Vec (OLX Europe) | 2021 | Content-aware encoder ("proposed by Avito and used currently in OLX") trained on in-session co-views, solving cold start. Ensemble with item-item CF performs best. | 10–20% uplift in clicks and contacts from recommendation sections (item page, home feed). Embeddings reused for monetization and ranking. | [VERIFIED: https://tech.olx.com/item2vec-neural-item-embeddings-to-enhance-recommendations-1fd948a6f293, published 2021-10-26] |
| Recommendations service | 2025 | Owned by the data team (moved from "a shared backend service"). **Python/FastAPI**, reading **ScyllaDB** (primary; shard-aware driver), **DynamoDB** (via aioboto3) and internal HTTP services. | Tens of thousands of req/s, **p99 < 10 ms**. See optimizations below. | [VERIFIED: https://tech.olx.com/scaling-recommendations-service-at-olx-db4548813e3a, RSS pubDate 2025-07-08] |
| Open-source embeddings for similar items | 2025 | multilingual-e5-small, fine-tuned, with a location re-rank | Offline recall gains. Online needed business features. | [VERIFIED: offline-evaluation post 2025-10-07] |

**Recommendations service optimizations (2025):**
- Async I/O: −40% latency, +50% throughput.
- Batching ScyllaDB fan-out reads: p99 −50%.
- Dropping Pydantic for slotted dataclasses: >30% lower latency.
- Python GC tuning (gen0 700→7000; gen1/2 10→20): −20% overall; homepage p99 52→12 ms.

**Explainability.** Dimensionality-reduction XAI was used to understand the deep-learning recommender and the factors users weigh. [VERIFIED: https://tech.olx.com/explainable-ai-at-olx-understanding-models-by-understanding-data-c8905ee688ae, published 2021-11-08]

[ASSUMPTION/JUDGEMENT] The 2025 move of serving into a data-team-owned Python service is a notable architectural choice. The author concedes "it's worth questioning whether switching to a different language might be more efficient". It is a good worked example of the **ownership vs. runtime-efficiency trade-off** for ML serving.

### 4.5 Experimentation and measurement

- **Group sequential testing.** OLX "migrated from fixed horizon experiments to GST to achieve faster insights, lower costs, and greater efficiency".
  - Methods: O'Brien-Fleming-type efficacy boundaries and Pampallona–Tsiatis efficacy plus futility boundaries.
  - The post quantifies peeking: 30 daily looks gave a **27.9%** false-positive rate at α=5%.
  - Maximum sample-size inflation reaches ~1.25 at 20 stages. Expected sample size is ~78.8% of fixed-horizon under H1 for a 5-stage design.
  - Traffic-forecast sensitivity is noted.
  - [VERIFIED: https://tech.olx.com/speed-with-rigor-testing-smarter-with-group-sequential-design-af962363ce90, RSS pubDate 2025-08-05]
- **Offline–online correlation as a gate.** The 2022 LTR post shows offline NDCG correlating with online A/B outcomes and uses this to pre-select candidates. [VERIFIED: LTR post 2022-06-22]
- **Causal inference for monetization products (Aug 2026).**
  - Higher-tier packages (more "boosts" per 30 days) appeared to perform *worse* than cheaper ones. The cause was **selection bias**: professional sellers self-select packages.
  - OLX applied **propensity-score matching** on car attributes (year, mileage, gearbox, fuel, make/model, price). Pre-matching overall SMD was 0.326.
  - Validated against a randomized experiment that granted an extra boost.
  - The post notes such experiments are costly because "every additional boost granted during an experiment represents premium visibility that was not purchased by the seller".
  - Conclusion: "Experiments establish causal benchmarks, while observational methods extend those insights."
  - [VERIFIED: https://tech.olx.com/correlation-lied-to-us-rethinking-product-impact-with-causal-inference-5ba47181f7c5, RSS pubDate 2026-08-04]
- **Experimentation platform name.** Not verified. The brief's "Laboratory?" could not be confirmed. A search for a candidate internal name returned nothing. Treat any platform name as unknown.

### 4.6 Trust and safety, fraud, moderation

- **Moderation architecture (2020).** Listings pass through an **automatic moderation system** of many ML components that accepts, rejects or escalates to a **moderation panel** for human moderators. [VERIFIED: https://tech.olx.com/a-two-step-framework-for-duplicate-detection-fbbe4c905480, published 2020-01-16]
  - Models: NSFW, forbidden items (e.g., weapons), duplicate detection, chat moderation and fraud detection. [VERIFIED: https://tech.olx.com/data-science-at-olx-7c7406d1713f, published 2020-11-10]
  - "More than half of the models we use in production are in the trust and safety and search and recommendations areas".
  - "More than 40 machine learning services" in production in 2020. [VERIFIED: same]
- **Duplicate detection** uses a **two-step framework**: cheap heuristic candidate generation, then an ML classifier on candidate pairs. Duplicates matter for spam and for fraud (copied listings used to collect deposits). [VERIFIED: duplicate-detection post 2020-01-16]
- **Fraud rings (2020).** Supervised models struggle because fraud patterns are scarce and shifting. OLX proposed **outlier detection** plus **graph linking** of accounts via shared attributes (phone, email, message text) to isolate rings. It describes rings creating pools of dormant fake accounts. [VERIFIED: https://tech.olx.com/detecting-fraud-rings-with-unsupervised-learning-554bedf29dbf, published 2020-06-24]
- **Chat image fraud with GenAI (2026).**
  - "Chat Images GenAI" detects and blocks suspicious images and **QR codes** sent in chat in real time.
  - Fraudulent images are "around 30% of all fraud cases on the platform in Poland". QR-code detection has 80% precision.
  - Live in Poland, Portugal, Bulgaria, Romania "and other countries".
  - OLX states its systems "moderate chat messages in real time, identify suspicious ads, and detect deceptive activity before it reaches users".
  - [VERIFIED: https://www.olxgroup.com/?p=4590, published 2026-01-28] ⚠
- **Ukraine fraud claims** (90% fewer fraud cases over three years; blocking of phishing-link messages before delivery) come from a press-office-sourced news report. [WIDELY REPORTED: Interfax-Ukraine search snippet, 2025-01; not fetched]
- **Direction of travel** (job ad): build a "Risk Engine", anomaly detection and real-time ML decisioning, moving from reactive to proactive. [WIDELY REPORTED: search snippet of an OLX Trust & Safety PM posting, 2025–26; not fetched]

### 4.7 Images and media

- **Media pipeline (2020).** CDN in front. "Around 80% of our traffic is cached and served by our CDN provider". The remaining 20% is "millions of requests a day", ~30,000 req/s at peak on the busiest cluster. Behind the CDN: a public API and an **on-demand image processor** that resizes, rotates, watermarks, re-encodes and compresses. [VERIFIED: Dali post 2020-02-25]
- **Thumbor → Dali (Rust).**
  - OLX replaced thumbor with **Dali**, a Rust service (Actix-Web). It first used OpenCV, then switched to **libvips** because OpenCV's watermarks did not match thumbor's.
  - It handled ~2× thumbor's load per instance.
  - Autoscaling on CPU was hard. The team overcommitted with a 60% average-CPU threshold, knowingly underutilizing.
  - [VERIFIED: same]
  - Dali was later open-sourced on GitHub. [ASSUMPTION/JUDGEMENT: not verified this session]
  - ⚠ The 2020 description may be superseded. No later post was found.
- **Image quality models for sellers.** Count, blur and darkness checks, plus title and description length, feed "actionable recommendations". The "infrastructure for serving deep learning models" post was not retrieved. [VERIFIED: DS overview 2020-11-10]
- **AI-generated listing videos.** A Feb 2026 OLX news item exists: "From static to dynamic: how OLX is revolutionizing ad presentation with AI-powered videos". Title only, from the olxgroup.com news sitemap; content not fetched. AutoIQ can "turn videos or ads into listings or short-form content". [VERIFIED: CLAIM AI release 2026-06-29]

### 4.8 Messaging, delivery and payments

- **Chat storage on Cassandra (2021).**
  - "At OLX chat we need to save the user chats for a long time… millions of messages per day… users can log in from multiple frontend clients."
  - Cassandra has served archival since **2017**, after "migrating from a legacy system using SQL". Partitioned by user id.
  - Messages are mutable (state changes), which drove a compaction-strategy change to **LCS** for read-heavy tables (`chats`, `threads`) after read amplification caused CPU and memory pressure.
  - [VERIFIED: https://tech.olx.com/cassandra-compaction-trade-offs-848ba51c64c0, published 2021-03-17]
  - ⚠ The author and context point to the OLX India-era chat team. Whether Europe's chat runs on the same stack today is **not verified**.
- **Pay&Ship (escrow-style delivery).** "The seller sends the item through a delivery service, and OLX holds the money of the transaction and transfers it to the seller when the package is delivered." [VERIFIED: https://tech.olx.com/machine-learning-for-delivery-time-estimation-1-591c8df849a0, published 2023-05-19]
  - Delivery-time ML found average seller handover ~1 day and carrier ~2 days. Two **CatBoost quantile-regression** models (α=0.05 and 0.95) produce a displayed range.
  - Productionized with **MLflow**, an internal deployment tool called **FrejaML**, **Airflow**, and AWS batch prediction. [VERIFIED: same]
  - **Status: de-prioritized.** Prosus FY25: "de-prioritisation of pay-and-ship in Europe" in H2 FY25. [VERIFIED: Prosus FY25 booklet] ⚠ The delivery-estimation system may be retired or reduced. Writers should present Pay&Ship as a **historical experiment in adding transactions to classifieds**, not as a current growth pillar.
- **"Safe Deal" / "OLX Pay".** Not verified in this session. Do not name these products without a source.
- **Fintech.** Kiwi Finance (Romanian credit broker) was bought in 2020 and sold in 2025. This marks a retreat from embedded finance in favour of core listings. [VERIFIED: Kiwi release 2020-12-07; FY26 release 2026-06-29]

### 4.9 Data platform

**Verified fragments:**

| Component | Use | Evidence |
| --- | --- | --- |
| AWS data lake (S3) | ML pipelines | 2018 talk; 2019 Step Functions post |
| Airflow | Orchestration | jobs recommender 2020; delivery ML 2023 |
| AWS Batch | Batch training and prediction | jobs 2020 |
| Presto | SQL | jobs 2020 |
| AWS Glue | ETL | 2019 |
| SageMaker | Training / batch transform | 2019 |
| Step Functions, CloudWatch Events, Lambda | Triggering | 2019 |
| MLflow | Tracking / registry | 2023 |
| FrejaML | Internal model deployment | 2023 |
| Kinesis | Search-team ingestion of enriched ad events | 2024 |
| ScyllaDB and DynamoDB | Online feature / recommendation stores | 2025 |

- **Event tracking at scale.** "Billions of events and records per day". [VERIFIED: GOTO 2018]
- **Not verified in this session:**
  - Kafka as the backbone (seen only in job-ad snippets: Kafka, Redshift, Trino, Spark, Airflow, a lakehouse with **Apache Iceberg** and a "Medallion architecture")
  - Data-mesh claims
  - Any platform named "Reservoir"
  - The "DanaDB" MySQL→S3 Parquet replication tool (post exists, link found, content not retrievable)
- [ASSUMPTION/JUDGEMENT] The trajectory, from SageMaker/Glue/Step Functions (2019) to Airflow/MLflow (2020–23) to Iceberg/Trino lakehouse (job ads, 2025–26), matches the industry's broad move from managed-service glue to open table formats. Treat the 2019 Step Functions design as **likely superseded**.

### 4.10 Pro tools and SaaS for professional sellers

- **Motors: AutoIQ** (dealer-facing AI agent, Otomoto Poland, all customers, early 2026). It works as a "24/7 analyst for dealers":
  - Faster listing creation
  - A single lead dashboard
  - Follow-up and pricing recommendations
  - AI-written descriptions in the dealer's tone
  - Video-to-listing

  Dealers publish listings up to 36% faster. Dealer responsiveness is up 12%. Weekly engagement is 21%. [VERIFIED: https://www.olxgroup.com/news/olx-launches-agentic-ai-products-to-transform-property-search-and-car-sales-at-claim-ai-in-lisbon/, dated 2026-02-25 in body; sitemap 2026-06-29] ⚠
- **Price evaluation for Otomoto sellers** (2020): an ML model suggests the optimal price range. [VERIFIED: DS overview 2020-11-10]
- **Real estate.**
  - "Tools optimised for agents" are part of the FY25 real-estate story. [VERIFIED: Prosus FY25 booklet]
  - Historical acquisitions of agent software: Inmokey (LatAm, 2019) and Obido (Poland new-build, 2021). [VERIFIED: releases above]
  - "StoriaCRM" and an Imovirtual CRM product were **not verified**.
- **Services: Fixly** (Poland) was divested (agreement 29 Oct 2025). [VERIFIED: FY26 release] Fixly was a services marketplace, not dealer SaaS.
- **Monetization products.** Packages with N "boosts" per 30 days, and "Value Added Services" that buy exposure and recency resets. These interact directly with ranking: the VAS LTR objective, and the protected recency in the linear re-ranker. [VERIFIED: causal-inference post 2026-08-04; hybrid search post 2025-09-09]

### 4.11 Generative AI and agents ⚠

| Item | What | Evidence |
| --- | --- | --- |
| Investment | >US$200m in AI since 2018. US$17m+ in FY25, US$20m planned for FY26 (H1 statement), US$30m actual FY26. ~150 people working in AI. | [VERIFIED: FY25 release 2025-06-23; H1 release 2025-11-24; https://www.olxgroup.com/ai-at-olx/ (fetched 2026-10-19, date unknown); FY26 release 2026-06-29] |
| Use-case counts | 55 (FY25), "over 60… including 10 generative AI" (H1 FY26), "more than 85… and 12 generative AI solutions" (FY26), "75 active AI use cases… 10 agentic" (Apr 2026 release) | [VERIFIED: releases as dated]. Counts are company-defined and inconsistent across documents. Cite with date. |
| GenAI ad posting | Auto-filled attributes and descriptions. Posting time −35% to −55%. Ad quality up to +37%. | [VERIFIED: H1 FY26 release 2025-11-24; ai-at-olx page] |
| Auto Description | Draft listing from a photo plus basic details. Seller reviews. ~2m keystrokes saved per month. Human evaluation: 98% style/relevance, 89% faithfulness. | [VERIFIED: https://www.olxgroup.com/news/how-olx-uses-ai-to-reduce-repetitive-work/, published 2026-08-28] |
| Jobs Matchmaking | LLM + OCR **CV parsing**, an **AI Navigator** using a jobs taxonomy, and **AI Sourcing** that shows matching candidates from the existing pool, with consent-based CV sharing. Hiring 16% faster. FY26: AI matchmaking is 59% of engagement actions; 63% of employers engage within 5 minutes of a match. | [VERIFIED: https://www.olxgroup.com/news/smarter-matches-faster-hires-thats-the-power-of-olx-ai/, published 2026-01-27; FY26 release] |
| CompassGPT | Conversational property search **inside ChatGPT** (Apps → Imovirtual, @imovirtual). Shortlists with trade-offs, resale and appreciation signals. Built with OpenAI. | [VERIFIED: CLAIM AI release, 2026-02-25/06-29] |
| AutoGPT | Conversational car search **inside ChatGPT**. Live on Otomoto. La Centrale, Autovit and Standvirtual scheduled. Built with OpenAI. Buyers find a suitable vehicle "at least 20% faster" than with filters. "More than 2,600 AI agents". | [VERIFIED: https://www.olxgroup.com/news/olx-launches-autogpt-agentic-ai-assistant-transforming-automotive-search-across-europe/, published 2026-04-02] |
| Internal agents | "Agentic Workforce" programme: close to 3,000 employee-built agents (data, legal, support). Sales2Text call transcription and scoring. | [VERIFIED: how-olx-uses-ai post 2026-08-28] |
| Engineering agents | "**Forge**, our internal AI-augmented delivery program… engineers orchestrate while narrow, specialized agents handle the mechanical work", with a lint gate as a hard merge condition. Token quota is "our biggest constraint". | [VERIFIED: agent-context post 2026-08-21] |
| Prosus AI Assistant | Prosus-provided LLM assistant and API (from July 2023), used for job-role extraction | [VERIFIED: job-roles post 2024-01-18] |
| Responsible AI | OLX states EU AI Act alignment, opt-outs, disclosure of AI content, no AI price-setting without consent, no automated decisions materially affecting people (including recruitment/HR), and model documentation. | [VERIFIED: https://www.olxgroup.com/ai-at-olx/, date unknown] |
| "OLX Magic" (Prosus, 2024) | A secondary LLMOps case-study summary of a 2024 Prosus talk describes it as follows:<br>- **What it is.** A consumer e-commerce agent built on the same agentic stack as Prosus's internal assistant (Tokan), live in **Poland**, "still in development".<br>- **Tools.** Text and visual catalog search, plus web search.<br>- **Agent design.** Memory, planning and e-commerce guardrails.<br>- **Features.** Dynamic filter suggestions, natural-language filters, contextual highlights and Smart Compare.<br>- **Lessons.** A blank ChatGPT-style chat UI failed, so the team moved back to the familiar search bar, results grid and filters with AI built in. The assistant is "only as good as your search", which led the team to rebuild search with embeddings from titles, images and descriptions.<br>- **Gaps.** No metrics were disclosed. Recent OLX releases (2025–26) do not use the name, so its current status is unknown. | [WIDELY REPORTED: https://zenml.io/llmops-database/agent-based-ai-assistants-for-enterprise-and-e-commerce-applications, 2024 talk; original talk https://www.youtube.com/watch?v=mVo_l9m9R1s not fetched] ⚠ |

[ASSUMPTION/JUDGEMENT] The **architecturally significant move** in 2026 is distribution, not models. CompassGPT and AutoGPT run as apps *inside ChatGPT*, with OLX supplying proprietary inventory and transaction data. That reverses the classic classifieds assumption that discovery happens on the marketplace's own surfaces. It also makes listing data quality, structured attributes and API-grade inventory access the new competitive surface.

---

## PART 5: Organization and ways of working

- **Squads and chapters (OLX Autos, 2021):** squads own end-to-end journeys; chapters such as Android, backend and QA are led by chapter leads who line-manage; yearly strategic, quarterly squad and two-week sprint planning. [VERIFIED: https://tech.olx.com/scaling-agile-olx-2b2dd7b9def4, published 2021-09-23] Historical.
- **WOF at OLX Motors (2024–2026).** "By 2024, at OLX Motors, we had a classic case of 'too much of everything, not enough of anything.'" OLX introduced a cross-functional initiative framework covering governance, champions and drivers, and outcome tracking. It completed 29 initiatives. [VERIFIED: WOF post 2026-03-18]
- **Data team owning a production service.** Recommendations serving moved out of a shared backend team "to gain greater autonomy and flexibility". [VERIFIED: recommendations post 2025-07-08]
- **Engineering hubs.** Poznań (masterclasses) and Portugal (many 2025–26 authors and roles). [VERIFIED: Masterclass post 2026-02-25]. Lisbon hosted CLAIM AI 2026. [VERIFIED: CLAIM AI release]. Portugal as an engineering hub is otherwise [ASSUMPTION/JUDGEMENT].
- **"Personalized ranking" team** inside search (2020). [VERIFIED: DS overview 2020-11-10]

---

## PART 6: Reference-architecture inference (clearly labeled)

[ASSUMPTION/JUDGEMENT throughout. This section synthesizes the verified fragments into a plausible current OLX Europe listing stack, for use as a teaching model. Writers must not present it as OLX's documented architecture.]

```
Sellers (C2C + pro) ──> Posting flows (GenAI attribute fill, Auto Description, AutoIQ for dealers)
                          │
                          ▼
                   Listing service(s) [Go microservices; legacy PHP core]
                          │  ad events (Kafka? / Kinesis for search ingestion — verified 2024)
          ┌───────────────┼──────────────────────┬─────────────────────────┐
          ▼               ▼                      ▼                         ▼
   Moderation pipeline   Search indexing        Feature/embedding         Data lake / lakehouse
   (auto ML: NSFW,       (Solr collection:      pipelines (Airflow;        (S3; Iceberg/Trino per job
   forbidden, dupes,     BM25 fields +          e5-small embeddings;       ads; billions of events/day)
   fraud graph) → human  CTR features +         Item2Vec)
   panel                 vectors)
                          │
                          ▼
   Query → Solr: BM25 top-N + fixed-quota vector top-K → LTR rerank (XGBoost LambdaMART via Solr LTR;
           Vanilla vs VAS objectives) → page; extension chain fallback for ZRPs
   Recommendations: FastAPI service over ScyllaDB + DynamoDB; CF + Item2Vec ensemble; home feed, item page
   Chat: real-time moderation incl. GenAI image/QR fraud; (Cassandra-backed in the 2021 India-era design)
   Media: CDN (≈80% hit) → image API → on-demand processor (Rust/libvips "Dali", 2020) on K8s/AWS
   Experimentation: GST boundaries; offline–online correlation gates; causal methods for monetization
   Off-platform discovery: ChatGPT apps (CompassGPT, AutoGPT) over OLX inventory + transaction data
```

Points of genuine uncertainty in this picture:
- Whether Kafka or Kinesis is the primary event bus. Possibly both, by team.
- Whether all verticals share one Solr estate.
- Whether Dali survives.
- How brand-per-country configuration is implemented server-side.

---

## PART 7: Key lessons for the book

1. **Ranking is a two-sided-marketplace objective, not a relevance metric.** OLX labels "success" as seller contact (messages or calls), because transactions are not observable. It checks that ranking does not concentrate demand on a few sellers: unique contacted sellers *rose* after LTR. [VERIFIED: LTR post 2022-06-22; hybrid search post 2025-09-09]
2. **Paid visibility must be encoded in the ranker, explicitly.** OLX runs separate "Vanilla" and "VAS" LTR objectives. Any retrieval change, such as vector search, can silently bury paid ads if the ranker never saw such candidates. [VERIFIED: hybrid search post 2025-09-09]
3. **Hybrid search is an evolution of a working lexical stack, not a replacement.** Keep BM25 for exact intent and traceability. Add a fixed quota of vector candidates, because similarity thresholds did not separate relevant from irrelevant. Retrain the ranker with a similarity feature. Bootstrap training data with a deliberately "do no harm" experiment. [VERIFIED: hybrid search post 2025-09-09]
4. **Prove new retrieval in the fallback path first.** Slotting vector search into the zero-results "extension chain", in a smaller market, isolated its value (>100% more contact events per user) before touching the main flow. [VERIFIED: same]
5. **Embedding similarity is not relevance in local classifieds.** Location and price must be re-introduced after retrieval. Offline recall gains lost online until a location-aware re-rank was added. [VERIFIED: offline-evaluation post 2025-10-07]
6. **Offline evaluation earns its keep only if it is calibrated against online results.** OLX publishes an explicit NDCG-vs-A/B correlation and uses it to pre-select models. It also uses group sequential testing to stop experiments early without inflating false positives (27.9% with naive daily peeking). [VERIFIED: LTR post 2022-06-22; GST post 2025-08-05]
7. **Measuring monetization products needs causal methods.** Sellers self-select into boost packages, so naive comparisons can show premium packages "underperforming". Propensity matching, validated by a small randomized experiment, recovered the true incremental effect. [VERIFIED: causal-inference post 2026-08-04]
8. **Multi-brand, multi-country verticals favor one codebase with configuration over forks.** Examples: one frontend repo serving three brands; a centralized LTR repo with Hydra brand configs; a "unified platform" in real estate. [VERIFIED: Masterclass 2026-02-25; Hydra post 2025-06-02; Prosus FY25 booklet] The single-codebase reading of the real-estate platform is [ASSUMPTION/JUDGEMENT].
9. **Identity and service-estate hygiene is a precondition for consolidation.** OLX Motors had to standardize user identification across 71 services, centralize secrets and unify deploy notifications before cross-brand work scaled. [VERIFIED: WOF post 2026-03-18]
10. **Moderation is a pipeline of specialized models plus a human panel, and fraud has moved into chat.** Duplicate detection is two-stage (candidates, then classifier). Fraud rings need graph and outlier methods. By 2026, GenAI screens chat images and QR codes in real time. [VERIFIED: duplicate 2020-01-16; fraud rings 2020-06-24; olxgroup.com 2026-01-28]
11. **Media is a CDN problem first and a compute problem second.** With ~80% CDN hit rate, the residual 20% still needed thousands of pods. Rewriting the processor (thumbor → Rust/libvips) roughly halved per-request cost. Autoscaling on CPU stayed imperfect. [VERIFIED: Dali post 2020-02-25]
12. **Transactional add-ons are optional; core listing monetization is not.** OLX Autos (inventory-owning) doubled revenue and destroyed margin. Pay&Ship was de-prioritized in Europe. Kiwi Finance and Fixly were sold. Margins went from 25% aEBIT (FY24) to ~48–49% adjusted EBITDA (FY26) on a focused motors, real-estate and jobs core. [VERIFIED: fin24 2023-03-02; Prosus FY25 booklet; OLX FY26 release 2026-06-29]
13. **ML serving ownership vs. runtime efficiency is a real trade-off.** A data-team-owned Python/FastAPI recommendations service reached p99 under 10 ms only after async I/O, batching, removing validation overhead and GC tuning. The team openly questions the language choice. [VERIFIED: recommendations post 2025-07-08]
14. **GenAI's first durable wins are on the supply side.** Structured attributes and descriptions at posting time (−35–55% posting time), taxonomy normalization for search (job roles), and seller and dealer copilots. External-API cost was large enough (~15K/month for one pipeline) to trigger build-vs-buy reviews. [VERIFIED: H1 FY26 release 2025-11-24; job-roles post 2024-01-18; Auto Description post 2026-08-28]
15. **Discovery is leaving the marketplace's own surfaces.** OLX now ships property and car search as ChatGPT apps built with OpenAI. Inventory quality and structured, API-grade listing data become the moat. [VERIFIED: CLAIM AI release; AutoGPT release 2026-04-02] The "moat" interpretation is [ASSUMPTION/JUDGEMENT].

---

## PART 8: Open questions / not publicly documented

- **OLX Europe platform consolidation mechanics.** Not documented in what I could fetch:
  - Which brands share a codebase (Otodom/Storia/Imovirtual; Otomoto/Autovit/Standvirtual/La Centrale)
  - When the "unified platform" rolled out
  - Whether La Centrale will be migrated onto the motors platform
- **Languages and migration.** The PHP→Go migration's scope, timeline and remaining legacy share. Only indirect evidence exists (Go and PHP services in the 2026 agent post; job-ad snippets).
- **Event backbone.** Kafka (job ads) vs. Kinesis (verified for search ingestion, 2024). Schema governance and event naming are unknown. A tracking system name (e.g., "Ninja") is unverified.
- **Experimentation platform.** Name, architecture, assignment service and metric store are unknown. Only methods (GST, causal inference) are documented.
- **Data platform.** "Reservoir" as a proper name is unverified. The Iceberg/Trino lakehouse is seen only in job-ad snippets. The DanaDB (MySQL→S3 Parquet) post exists but could not be retrieved.
- **Search infrastructure.** Solr version, SolrCloud topology, how vectors are stored and served (in Solr dense-vector fields or a separate ANN store), and indexing latency. None are stated.
- **Chat and messaging in Europe today.** The Cassandra post is from the 2021 India-era chat team. The current European chat stack is undocumented.
- **Image processing today.** Whether Dali (2020) is still in service.
- **Payments.** "Safe Deal", "OLX Pay" and Pay&Ship status after the FY25 de-prioritization. Is it still live in any market?
- **"OLX Magic."** Only a secondary summary of a 2024 Prosus talk was found. Current status and any metrics are unknown.
- **Pro SaaS.** Dealer CRM and agent CRM products beyond AutoIQ are unverified ("StoriaCRM" and Imovirtual CRM claims).
- **Pending deal closings** ⚠ Kazakhstan (expected Q1 2026), Uzbekistan and Fixly. Buyer identity for Fixly is unverified.
- **Load shedding.** The 2021 NGINX adaptive-concurrency posts exist but could not be retrieved.
- **South Africa.** Whether Property24 and AutoTrader SA are operated by OLX Group or sit elsewhere in Prosus.

---

## PART 9: Source list

**Primary: OLX Group and Prosus/Naspers**

| # | Title | Publisher | Date | URL |
| --- | --- | --- | --- | --- |
| 1 | OLX Group FY26 results ("continues strong performance as motors, real estate and jobs drive growth") | OLX Group | 2026-06-29 | https://www.olxgroup.com/?p=5024 |
| 2 | OLX Group H1 FY26 results | OLX Group | 2025-11-24 | https://www.olxgroup.com/?p=4285 |
| 3 | OLX Group reports strong FY 2025 results with 18% revenue growth and 61% profit uplift | OLX Group | 2025-06-23 | https://www.olxgroup.com/news/olx-group-reports-strong-fy-2025-results-with-18-revenue-growth-and-61-profit-uplift-year-on-year/ |
| 4 | Prosus financial results FY25 booklet (copy hosted on the Bundestag lobby register) | Prosus | 2025-06 | https://www.lobbyregister.bundestag.de/media/57/dc/638531/prosus-financial-results-fy25-booklet.pdf |
| 5 | Disposal of Avito Group (SENS) | Naspers | 2022-10-14 | https://www.naspers.com/news-insights/regulatory-updates/2022/disposal-of-avito-group |
| 6 | OfferUp and letgo combine US marketplaces | OLX Group | 2020-03-25 | https://www.olxgroup.com/news/offerup-and-letgo-combine-us-marketplaces-to-deliver-a-better-buying-and-selling-experience-for-more-than-20-million-monthly-users/ |
| 7 | OLX Group to sell OLX Uzbekistan to a JV led by TBC Bank Group | OLX Group | 2025-08-21 | https://www.olxgroup.com/news/olx-group-to-sell-olx-uzbekistan-to-a-joint-venture-led-by-tbc-bank-group/ |
| 8 | OLX Brazil completes the acquisition of 100% of Grupo ZAP | OLX Group | 2020-11-19 | https://www.olxgroup.com/news/olx-brazil-completes-the-acquisition-of-100-of-grupo-zap/ |
| 9 | OLX Group successfully acquires Kiwi Finance | OLX Group | 2020-12-07 | https://www.olxgroup.com/news/olx-group-successfully-acquires-kiwi-finance-the-largest-credit-broker-in-romania/ |
| 10 | OLX Group acquires Inmokey | OLX Group | 2019-10-25 | https://www.olxgroup.com/news/olx-group-acquires-inmokey-a-solid-commitment-towards-user-oriented-technology/ |
| 11 | OLX Group acquires Obido | OLX Group | 2021-02-25 | https://www.olxgroup.com/news/olx-group-acquires-obido-an-innovative-real-estate-platform-for-the-primary-market/ |
| 12 | We fight online fraud with the power of AI | OLX Group | 2026-01-28 | https://www.olxgroup.com/?p=4590 |
| 13 | Smarter matches, faster hires: that's the power of OLX AI | OLX Group | 2026-01-27 | https://www.olxgroup.com/news/smarter-matches-faster-hires-thats-the-power-of-olx-ai/ |
| 14 | OLX launches agentic AI products (CompassGPT, AutoIQ) at CLAIM AI in Lisbon | OLX Group | body 2026-02-25; sitemap 2026-06-29 | https://www.olxgroup.com/news/olx-launches-agentic-ai-products-to-transform-property-search-and-car-sales-at-claim-ai-in-lisbon/ |
| 15 | OLX launches AutoGPT agentic AI assistant | OLX Group | 2026-04-02 | https://www.olxgroup.com/news/olx-launches-autogpt-agentic-ai-assistant-transforming-automotive-search-across-europe/ |
| 16 | OLX Group launches Otodim platform in Ukraine | OLX Group | 2026-05-13 | https://www.olxgroup.com/news/olx-group-launches-otodim-platform-in-ukraine-deepening-commitment-to-the-countrys-real-estate-market/ |
| 17 | How OLX uses AI to reduce repetitive work | OLX Group | 2026-08-28 | https://www.olxgroup.com/news/how-olx-uses-ai-to-reduce-repetitive-work/ |
| 18 | AI at OLX | OLX Group | date unknown (fetched 2026-10-19) | https://www.olxgroup.com/ai-at-olx/ |
| 19 | Olaf Zschiedrich at AWS Summit | OLX Group | 2018-06-19 | https://www.olxgroup.com/news/olaf-zschiedrich-awssummit/ |
| 20 | OLX Group news sitemap (used to enumerate 2025–26 releases) | OLX Group | 2026-10-19 | https://www.olxgroup.com/cpt-news-sitemap.xml |

**Primary: OLX Engineering blog (tech.olx.com)**

| # | Title | Author | Published | URL |
| --- | --- | --- | --- | --- |
| 21 | Does it matter how you feed an agent its context? | Raymond Gitonga | 2026-08-21 | https://tech.olx.com/does-it-matter-how-you-feed-an-agent-its-context-ee1519586520 |
| 22 | Correlation Lied to Us: Rethinking Product Impact with Causal Inference | Enderson Santos | 2026-08-04 | https://tech.olx.com/correlation-lied-to-us-rethinking-product-impact-with-causal-inference-5ba47181f7c5 |
| 23 | Handling concurrency on the Web with Web Locks API | Cesar Contreras | 2026-07-14 | https://tech.olx.com/handling-concurrency-on-the-web-with-web-locks-api-163b7e07eddd |
| 24 | Empowering Innovation Through Structure | Sara Mendes | 2026-03-18 | https://tech.olx.com/empowering-innovation-through-structure-93c15614f6d3 |
| 25 | OLX Masterclass Frontend 2026 | Isaac Queiroz | 2026-02-25 | https://tech.olx.com/olx-masterclass-frontend-2026-068299a2df50 |
| 26 | Importance of offline evaluation to guide model choice | Tiago Cabo | 2025-10-07 | https://tech.olx.com/importance-of-offline-evaluation-to-guide-model-choice-1c2be1c4599a |
| 27 | Hybrid Search — Where Keywords Meet Vectors | Inês Soveral | 2025-09-09 | https://tech.olx.com/hybrid-search-where-keywords-meet-vectors-enabling-classifieds-discovery-b7c383fe4fc4 |
| 28 | Speed with Rigor: testing smarter with group sequential design | Gabriela Lewenfus | 2025-08-05 | https://tech.olx.com/speed-with-rigor-testing-smarter-with-group-sequential-design-af962363ce90 |
| 29 | Scaling recommendations service at OLX | Jordi Esteve Sorribas | 2025-07-08 | https://tech.olx.com/scaling-recommendations-service-at-olx-db4548813e3a |
| 30 | Unlocking Flexibility in Configuration: The Power of Hydra | Catarina Goncalves | 2025-06-02 | https://tech.olx.com/unlocking-flexibility-in-configuration-the-power-of-hydra-3f9e69263bb4 |
| 31 | From RankNet to LambdaMART: Leveraging XGBoost | Enderson Santos | 2025-02-10 | https://tech.olx.com/from-ranknet-to-lambdamart-leveraging-xgboost-for-enhanced-ranking-models-cf21f33350fb |
| 32 | Generative AI at AWS Summit Madrid 2024: an OLX engineer's perspective | Juan Francisco Pinera | 2025-01-20 | https://tech.olx.com/generative-ai-at-aws-summit-madrid-2024-an-olx-engineers-perspective-4e9fcc77ca32 |
| 33 | Journey to Contract Testing through Pact | Paulo Zenida | 2024-06-24 | https://tech.olx.com/journey-to-contract-testing-through-pact-04a39a3fcc22 |
| 34 | Extracting Job Roles in Job Ads: A Journey with Generative AI | Mahnaz Namazi | 2024-01-18 | https://tech.olx.com/extracting-job-roles-in-job-ads-a-journey-with-generative-ai-e8b8cf399659 |
| 35 | Machine Learning for Delivery Time Estimation | Enderson Santos | 2023-05-19 | https://tech.olx.com/machine-learning-for-delivery-time-estimation-1-591c8df849a0 |
| 36 | Learning-To-Rank: Sorting Search Results | Ilia Ivanov | 2022-06-22 | https://tech.olx.com/learning-to-rank-sorting-search-results-b21a8bd48808 |
| 37 | Explainable AI at OLX | Viacheslav Dubrov | 2021-11-08 | https://tech.olx.com/explainable-ai-at-olx-understanding-models-by-understanding-data-c8905ee688ae |
| 38 | Item2Vec: Neural Item Embeddings to enhance recommendations | Ilia Ivanov | 2021-10-26 | https://tech.olx.com/item2vec-neural-item-embeddings-to-enhance-recommendations-1fd948a6f293 |
| 39 | Scaling Agile @ OLX Autos | Jatin Juneja | 2021-09-23 | https://tech.olx.com/scaling-agile-olx-2b2dd7b9def4 |
| 40 | JVM Profiling in Kubernetes with Java Flight Recorder | Abhinav Rohatgi | 2021-04-15 | https://tech.olx.com/jvm-profiling-in-kubernetes-with-java-flight-recorder-b39a6181a99c |
| 41 | Cassandra Compaction Trade-Offs | Satish Chandra | 2021-03-17 | https://tech.olx.com/cassandra-compaction-trade-offs-848ba51c64c0 |
| 42 | AutoSuggest Retrieval & Ranking (Part 2) | Aakash Prakash | 2020-12-22 | https://tech.olx.com/autosuggest-retrieval-ranking-part-2-14a8f50fef34 |
| 43 | Data Science at OLX | Alexey Grigorev, Andreas Merentitis | 2020-11-10 | https://tech.olx.com/data-science-at-olx-7c7406d1713f |
| 44 | Intro to our Jobs recommender service | Viacheslav Dubrov | 2020-10-28 | https://tech.olx.com/intro-to-our-jobs-recommender-service-4317b55fc075 |
| 45 | Detecting Fraud Rings with Unsupervised Learning | Hagop Boghazdeklian | 2020-06-24 | https://tech.olx.com/detecting-fraud-rings-with-unsupervised-learning-554bedf29dbf |
| 46 | Presenting Dali, an Image Processor Service | Augusto César Dias | 2020-02-25 | https://tech.olx.com/presenting-dali-an-image-processor-service-514e6be00de8 |
| 47 | A Two-Step Framework for Duplicate Detection | Alexey Grigorev | 2020-01-16 | https://tech.olx.com/a-two-step-framework-for-duplicate-detection-fbbe4c905480 |
| 48 | Ranking Ads with Machine Learning | Chandan Routray | 2019-05-14 | https://tech.olx.com/ranking-ads-with-machine-learning-ee03d7734bf4 |
| 49 | Building an AWS Serverless ML Pipeline with Step Functions | Rafael Felix Correa | 2019-04-15 | https://tech.olx.com/building-an-aws-serverless-ml-pipeline-with-step-functions-b39feed12bab |
| 50 | Understanding language through search (South Africa) | Vaibhav Sharma | 2018-11-05 | https://tech.olx.com/understanding-language-through-search-78ea37be7ac8 |
| 51 | OLX Engineering RSS feed (source text for #21–#30) | OLX / Medium | 2026-10-19 | https://tech.olx.com/feed |
| 52 | tech.olx.com sitemap (post inventory and dates) | OLX / Medium | 2026-10-19 | https://tech.olx.com/sitemap/sitemap.xml |

**Talks**

| # | Title | Publisher | Date | URL |
| --- | --- | --- | --- | --- |
| 53 | From (Big) Data Mess to Data as an Innovation Enabler (Olaf Zschiedrich, CTO) | GOTO Berlin | 2018 | https://gotopia.tech/sessions/652/from-big-data-mess-to-data-as-an-innovation-enabler |

**Secondary**

| # | Title | Publisher | Date | URL |
| --- | --- | --- | --- | --- |
| 54 | OLX | Wikipedia | accessed 2026-10-19 | https://en.wikipedia.org/wiki/OLX |
| 55 | Avito.ru | Wikipedia | accessed 2026-10-19 | https://en.wikipedia.org/wiki/Avito.ru |
| 56 | Prosus sells Avito… | Euronews / Reuters | 2022-10-14 | https://www.euronews.com/next/2022/10/14/ukraine-crisis-prosus-avito |
| 57 | Prosus looks to ditch OLX Autos business as second-hand car market slows | Fin24 / News24 | 2023-03-02 | https://www.news24.com/fin24/companies/prosus-looks-to-ditch-olx-autos-business-as-second-hand-car-market-slows-20230302 |
| 58 | OLX Group layoffs (800 jobs; OLX Autos closures) | TechCrunch | 2023-06-20 | https://techcrunch.com/2023/06/20/olx-group-layoffs |
| 59 | OLX shuts down Frontier Car Group's Berlin office | TechCrunch | 2021-03-29 | https://techcrunch.com/2021/03/29/prosus-classifieds-group-olx-shuts-down-berlins-frontier-car-group-to-focus-olx-autos-on-latam-and-asia/ |
| 60 | EMPG reveals details of merger with OLX | Wamda | 2020-06-02 | https://www.wamda.com/index.php/en/2020/06/empg-reveals-details-merger-olx |
| 61 | OLX Kazakhstan to be sold to Veon Group's Beeline for $75M | OnlineMarketplaces | 2025-10-23 | https://www.onlinemarketplaces.com/?p=104706 |
| 62 | Prosus HY 2026: Real estate revenues up 26% as OLX sees healthy growth | OnlineMarketplaces | 2025-11-24 | https://www.onlinemarketplaces.com/articles/prosus-hy-2026-real-estate-revenues-up-26-as-olx-sees-healthy-growth/ |
| 63 | OLX revenue climbs to $992m as Prosus folds classifieds into Europe | OnlineMarketplaces | 2026-06-29 | https://www.onlinemarketplaces.com/articles/olx-revenue-climbs-to-992m-as-prosus-folds-classifieds-into-europe/ |
| 64 | Aperture: Prosus FY 2026 Results | Old Mutual | 2026-07 | https://www.oldmutual.co.za/om-docs/blt9aa45c31c7ec5847/Aperture_Prosus_FY_2026_Results.pdf |
| 65 | Agent-Based AI Assistants for Enterprise and E-commerce Applications (Prosus: Tokan, OLX Magic) | ZenML LLMOps Database | 2024 | https://zenml.io/llmops-database/agent-based-ai-assistants-for-enterprise-and-e-commerce-applications |
