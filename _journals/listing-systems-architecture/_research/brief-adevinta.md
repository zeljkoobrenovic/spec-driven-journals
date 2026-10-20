# Research brief: Adevinta and its Schibsted origins

Prepared 19 October 2026 for chapter writers of *LISTED: Architecting Large-Scale Classifieds and Marketplace Platforms*. Adevinta is documented here because it is the clearest public case of one company running the full cycle of classifieds architecture. It started as a federation of locally built marketplaces. It acquired a second federation (eBay Classifieds Group) of comparable size, tried to converge the two onto shared platforms, and then, under private-equity ownership, deliberately reversed course and split into standalone marketplaces. The book does not endorse Adevinta's choices. It uses the record because few groups have published so much engineering and financial evidence across a full centralize/decentralize swing.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM-DD]**: fetched during this research session (19 October 2026), and the page supports the claim. Paraphrases stay close to the source, and quoted text is quoted. The date is the page's publication date. For annual reports it is the publication date or the period covered, whichever the document makes clear.
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (trade press, law-firm deal notes, Wikipedia, vendor case studies), not from primary documentation.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference, not checked against a source in this session. All architectural inferences about proprietary Adevinta systems carry this tag. Chapter writers should re-verify these before printing them as fact, or present them explicitly as judgements.

**Volatility flags.** ⚠ marks facts likely to change within 12 months: ownership, portfolio composition, product names, sale processes and headcount. All such facts are stated "as of 19 October 2026" unless another date is given.

**Research limitations (read this first).**

1. **The search budget ran out partway through.** The session's shared web-search quota was used up after about 30 searches. After that point, all evidence came from direct fetches of URLs found earlier, or of first-party pages on adevinta.com. As a result:
   - **Not researched at all:** Kleinanzeigen's and Marktplaats' own engineering blogs, and mobile.de engineering posts.
   - **Recovered late:** leboncoin's tech blog was read through its Medium RSS feed (recent 2026 posts only). Marktplaats' payment naming was checked in a single late search; the product is "Kopersbescherming", not "Gelijk betalen".
   - **Researched only partly:** Finn.no and Blocket founding details.
2. **Some first-party PDFs were read locally.** The 2019 and 2023 annual reports and the 2024 and 2025 strategic reports of Aurelia UK Feederco Ltd were downloaded through WebFetch and converted locally with `pdftotext`. Citations to them are VERIFIED against the extracted text.
3. **Technical evidence ages quickly.** Most engineering posts cited here date from 2019–2025. Under the 2025 decentralization (Part 6), the central platforms they describe may since have been split up, handed to individual marketplaces, or retired. Treat every "Adevinta runs X centrally" statement as true *at the post's date* only.

---

## PART 1: Timeline at a glance

| Date | Event | Evidence |
| --- | --- | --- |
| 1990s–2000s | Schibsted builds or acquires local classifieds sites: FINN.no (Norway), Blocket (Sweden), InfoJobs (Spain), leboncoin (France, founded 28 April 2006), Subito (Italy), willhaben (Austria, a 50/50 JV with Styria founded in 2006) | leboncoin date [WIDELY REPORTED: https://en.wikipedia.org/wiki/Leboncoin, 2026]. willhaben JV and founding year [VERIFIED: Adevinta AR 2023 (https://live.euronext.com/sites/default/files/company_press_releases/attachments_oslo/2024/04/26/616971_Adevinta%20AR%202023.pdf), published 2024-04-26]. Others: [ASSUMPTION/JUDGEMENT] |
| Oct 2009 | Schibsted acquires 100% of InfoJobs | [WIDELY REPORTED: https://en.wikipedia.org/wiki/Schibsted, citing an Oct 2009 article] |
| 2016 | Schibsted investor material pitches "one global product and tech organization" | [WIDELY REPORTED: financialfilings.com summary of the Q3 2016 investor presentation, 2016]. Primary slide not fetched |
| 25 Feb 2019 | Schibsted shareholders approve the demerger. Non-Nordic marketplaces become **Adevinta** | [VERIFIED: https://vend.com/news/introducing-adevinta-an-international-family-of-local-digital-marketplaces, published 2019-02-25] |
| 10 Apr 2019 | Adevinta lists on Oslo Børs at NOK 78/share. Schibsted retains about 60% | [WIDELY REPORTED: https://www.clearygottlieb.com/news-and-insights/news-listing/adevinta-asa-issues-largest-ipo-in-the-nordic-region-in-10-years, 2019] |
| 21 Jul 2020 | Adevinta agrees to acquire eBay Classifieds Group (eCG): US$2.5bn cash plus 540m shares; eBay to hold 44% of the capital and about 33% of the votes | [WIDELY REPORTED: https://insideretail.com.au/news/ebay-sells-gumtree-as-part-of-us9bn-classifieds-deal-202007, 2020-07] |
| 2 Jun 2021 | Shpock sold to Russmedia Equity Partners (a UK CMA remedy) | [VERIFIED: https://adevinta.com/press-releases/adevinta-completes-acquisition-of-ebay-classifieds-group/, published 2021-06-25/30] |
| 25 Jun 2021 | eCG acquisition completes. eCG Denmark sold to Schibsted for about €278m | [VERIFIED: same] |
| 1 Dec 2021 | Gumtree UK and Motors.co.uk sold to O3 Industries and Novum Capital (CMA remedy) | [VERIFIED: https://adevinta.com/press-releases/adevinta-sells-gumtree-uk-and-motors-co-uk-to-o3-industries-and-novum-capital/, published 2021-12-01] |
| Jul 2022 | Gumtree South Africa sold to Impresa Capital | [WIDELY REPORTED: onlinemarketplaces.com, 2022]. Not fetched |
| 25 Aug 2022 | Gumtree Australia, CarsGuide and Autotrader Australia sold to The Market Herald for US$60m | [VERIFIED: https://adevinta.com/press-releases/adevinta-asa-ade-adevinta-announces-sale-of-gumtree-australia-carsguide-and-autotrader-australia/, published 2022-08-25] |
| Sep 2022 | Vivanuncios and Segundamano (Mexico) sold to Navent | [VERIFIED (trade press): https://www.onlinemarketplaces.com/articles/adevinta-sells-vivanuncios-and-segundamano-to-navent-group, published 2022-09-27] |
| 2023 | eBay Kleinanzeigen is rebranded **Kleinanzeigen**. Hungary exited (Sep 2023). Kufar (Belarus) exited. Operating model "verticalized" | [VERIFIED: Adevinta AR 2023] |
| 21 Nov 2023 | Permira/Blackstone-led consortium (Aurelia Bidco Norway AS) offers NOK 115/share | [VERIFIED: https://vend.com/news/schibsted-supports-the-voluntary-offer-for-adevinta-reducing-its-stake-in-adevinta-by-60, published 2023-11-21] |
| 29–30 May 2024 | Offer settles (about 94.8% of capital). Compulsory acquisition of the remainder. Delisting follows | [VERIFIED: https://adevinta.com/press-releases/adevinta-asa-ade-completion-of-the-voluntary-offer-for-all-issued-and-outstanding-ordinary-class-a-shares-in-adevinta-asa/, published 2024-05-29] |
| Jul 2024 | Work begins on a new Target Operating Model, "empowering local marketplaces" | [VERIFIED: Aurelia UK Feederco Ltd Strategic Report 2024 (https://adevinta.com/wp-content/uploads/2025/04/Strategic-Report-2024-Aurelia-UK-Feederco-Ltd-FS.docx.pdf), published 2025-04] |
| Mar 2025 | Adevinta's 50% willhaben stake sold to a Styria/Sprints JV (reported value about €500m) | [VERIFIED (trade press): https://www.onlinemarketplaces.com/articles/funding-and-investment-roundup-adevinta-justmovein-rea-group-tomo-mortgage/, published 2025-03-13] |
| 21 Jul 2025 | Sale of Adevinta Spain to EQT announced | [VERIFIED: https://adevinta.com/press-releases/adevinta-announces-sale-of-its-spanish-business-to-eqt/, published 2025-07-21] |
| 18 Sep 2025 | Scout24 agrees to buy Fotocasa and Habitaclia from EQT (EV about €153m) | [VERIFIED: https://www.scout24.com/en/news-media/news/detail/scout24-acquires-spanish-online-real-estate-platforms-fotocasa-and-habitaclia, published 2025-09-18] |
| Oct 2025 | FT reports a "dual track" (IPO or sale) for mobile.de at up to about €10bn | [WIDELY REPORTED: https://www.pymnts.com/?p=3112865, 2025-10-08] |
| 1 Nov 2025 | L'argus (France) divested | [VERIFIED: Aurelia UK Feederco Ltd Strategic Report 2025 (https://adevinta.com/wp-content/uploads/2026/05/Strategic-Report-2025-Aurelia-UK-Feederco-Ltd.pdf), published 2026-05] |
| 2025 | Group "evolved from a centralised structure to a decentralised, standalone operating model" | [VERIFIED: Strategic Report 2025] |
| 27 Feb 2026 | Spain sale to EQT completes (gain about €1.1bn). €1.55bn dividend and €470m capital return paid in March 2026 | [VERIFIED: Strategic Report 2025] |
| 9 Mar 2026 | Tech blog reports a decision to deploy Claude Code to "over 2,000 software engineers" | [VERIFIED: https://adevinta.com/techblog/a-pragmatic-evaluation-of-software-engineering-ai-tooling/, published 2026-03-09] |

---

## PART 2: Schibsted origins (the "copy-paste" federation)

### 2.1 What Schibsted built

Schibsted, a Norwegian media group, moved its growth focus from media to online classifieds in the 2000s. The anchor sites were FINN.no (Norway), Blocket (Sweden), Tori.fi (Finland) and InfoJobs (Spain) [WIDELY REPORTED: https://en.wikipedia.org/wiki/Schibsted, 2026].

- **The Blocket platform.** Schibsted's international expansion is widely described as having been built "on the Blocket platform". A 2012 Nieman Lab piece is quoted as saying Schibsted ran classifieds in 28 countries on it [WIDELY REPORTED: search summary of https://www.niemanlab.org/2012/02/looking-to-europe-for-news-industry-innovation-part-2-schibsteds-stunning-classifieds-and-services-business/, 2012-02. The fetch itself returned HTTP 403, so this was **not** verified].
- **The playbook.** [ASSUMPTION/JUDGEMENT] The standard industry account is that Schibsted launched or bought a generalist site in each country, ran it on a shared Blocket-derived code base with free private listings, and monetized later through professional verticals (motors, real estate, jobs) and display advertising. leboncoin (2006) and Subito (2007) are usually given as examples. Treat this as industry lore unless a primary Schibsted document is found.
- **willhaben.** Founded in 2006 by Schibsted and Styria Medien AG as a 50/50 joint venture [VERIFIED: Adevinta AR 2023, p. 25].
- **leboncoin.** Founded 28 April 2006 by Schibsted. Since 2018 it has acted as a trusted third party for consumer-goods and holiday-rental transactions, with Adyen as its payment partner [WIDELY REPORTED: https://en.wikipedia.org/wiki/Leboncoin, 2026].

### 2.2 The tension already visible in 2016–2019

- **2016: "one global product and tech organization".** Schibsted's Q3 2016 investor presentation carried a slide with that heading [WIDELY REPORTED: financialfilings.com search summary, 2016]. In the Q4 2016 release, the CEO named improved classifieds "components and platforms" as essential [WIDELY REPORTED: same].
- **2017: a reorganization.** The Q3 2017 report described a new model meant to "strengthen local execution and global scale" [WIDELY REPORTED: same]. [ASSUMPTION/JUDGEMENT] The phrasing already pairs the two forces that drive the next decade: local autonomy and global scale.
- **2019: Adevinta names the tradeoff explicitly.** Its first annual report as a listed company said:
  > "While one of our historic success formulas has been local autonomy and decentralised capacity in product and technology, we are adopting a centralised strategy to data and analytics. This one area where investment requirements are large and the technology is uniform, and where the maxim 'built once; used many times' clearly applies. Our ambition is to provide our marketplaces with centrally developed components so they can offer outstanding data driven products locally." [VERIFIED: Adevinta Annual Report 2019 (https://adevinta.com/app/uploads/2021/10/adevinta-annual-report-2019.pdf), published 2020]

  The same report says Adevinta "intends to continue devoting resources to develop scalable components… creating value through central product and technology development aligned closely with local on-the-ground technical expertise". It also records that HQ/Other EBITDA losses grew in 2019 because of "investments in scalable tech and data" [VERIFIED: same].

**Key lesson anchor.** Adevinta's own 2019 rule for what to centralize was *areas with large investment needs and uniform technology* (data and analytics). Product surfaces stayed local. That is a sharper decision rule than "centralize everything shared", and chapter writers can quote it.

### 2.3 The FINN.no lineage of Adevinta's platform tooling

FIAAS ("Finn Infrastructure As A Service") was built at FINN.no, a Schibsted company that stayed with Schibsted and did not join Adevinta.

- **FINN.no at KubeCon EU 2017** [VERIFIED: https://raw.githack.com/mm-k8s-ug/kubecon-slides/master/slides/2017-kubecon-eu/ (FINN.no/Schibsted slide deck), presented 2017-03]:
  - 120 developers, 350 microservices, 1,200 deployments per week, and a median of 6 minutes from push to deploy.
  - Growth over time: services 3 → 350, developers 40 → 130, deployments 1/week → 1,000/week.
  - FIAAS adoption at FINN was 26% at the time.
  - FIAAS replaced roughly 147 lines of Kubernetes manifests with a short `fiaas.yaml`.
- **FIAAS is open source and maintained.** The core component, fiaas-deploy-daemon, is an Apache-2.0 Kubernetes operator. It reconciles an `Application` custom resource (API group `fiaas.schibsted.io/v1`) from a minimal config file plus defaults [VERIFIED: https://github.com/fiaas/fiaas-deploy-daemon, page footer 2026].
- **Adevinta adopted it.** Galo Navarro's November 2019 talk says FIAAS was created about seven years earlier "at a Norwegian marketplace" (finn.no) and open-sourced in early 2019 [VERIFIED: https://varoa.net/paas/infrastructure/platform/kubernetes/cloud/2020/01/02/talk-how-to-build-a-paas-for-1500-engineers.html, published 2020-01-02].
- **It is still the golden-path abstraction.** In 2023 Adevinta still called FIAAS its "Golden Path" deployment abstraction on SCHIP [VERIFIED: https://adevinta.com/techblog/how-we-joined-forces-to-enable-gpu-serving-for-our-ai-solutions/, published 2023-08-08]. The 2025 PlatformCon abstract lists FIAAS and the "Common Platform UI" as a phase in the platform's evolution [VERIFIED: https://2025.platformcon.com/sessions/8-years-of-kubernetes-platform-evolution-do-s-and-don-ts, session 2025-06-26].

**Lesson anchor.** The deployment abstraction that ran across Adevinta's 20+ marketplaces was built by one local marketplace and then promoted to group level. The same pattern recurs with Fisher (Part 4.4).

---

## PART 3: Corporate structure and portfolio, 2019–2026

### 3.1 The 2019 demerger and listing

- **The demerger.** On 25 February 2019 Schibsted shareholders voted to demerge Schibsted's marketplaces outside the Nordics into Adevinta, with an Oslo listing planned for 10 April 2019 [VERIFIED: https://vend.com/news/introducing-adevinta-an-international-family-of-local-digital-marketplaces, published 2019-02-25].
- **The footprint.** Adevinta had marketplaces in 16 countries across Europe, Latin America and North Africa, and about 1.5 billion visits per month. Brands named at the time included leboncoin, InfoJobs, Subito, Jófogás and Segundamano [VERIFIED: same].
- **The IPO.** Price NOK 78. Schibsted kept about 60% after the offering, and tickers ADEA/ADEB later collapsed to ADE. It was described as the largest Norwegian IPO since 2006 [WIDELY REPORTED: Cleary Gottlieb and Wiersholm deal notes, 2019].
- **2019 segments** (operating revenues, € million) [VERIFIED: Adevinta AR 2019, Note 6]:

| Segment | 2019 revenue | Contents |
| --- | --- | --- |
| France | 357.4 | leboncoin, A Vendre A Louer, Videdressing, Locasun, PayCar, L'Argus |
| Spain | 182.0 | InfoJobs, coches.net, Fotocasa, Habitaclia, Milanuncios, Vibbo |
| Brazil (100% basis) | 86.0 | OLX Brazil JV (equity-accounted) and InfoJobs Brazil |
| Global Markets | 124.2 | Subito, InfoJobs Italy, Daft, DoneDeal, Adverts, Hasznaltauto, Jófogás, Fincaraiz, Yapo, Segundamano, Kufar, Tayara, Avito.ma, Corotos, Shpock |
| Other/HQ | 13.4 | "central functions including central product and technology development" |
| Eliminations | (82.7) | OLX Brazil JV adjustment |
| **Total** | **680.3** | |

  The 2019 report also says leboncoin "launched a transactional business model in some of the generalist categories with good early results" [VERIFIED: AR 2019].

### 3.2 The eBay Classifieds Group acquisition (2020–2021)

- **The deal (announced July 2020).** US$2.5bn cash plus 540 million Adevinta shares. eBay would hold 44% of the capital and about 33% of the votes [WIDELY REPORTED: https://insideretail.com.au/news/ebay-sells-gumtree-as-part-of-us9bn-classifieds-deal-202007, 2020-07-23].
  - **Brands acquired:** Autotrader (AU), Bilbasen, CarsGuide, DBA, 2dehands/2ememain, eBay Kleinanzeigen, Gumtree, Kijiji, Marktplaats, mobile.de, Automobile.it, Motors.co.uk and Vivanuncios.
  - **Countries:** 13, including Australia, Canada, Denmark, Germany, Italy, Mexico, the Netherlands, the UK and South Africa.
- **Completion (25 June 2021)** [VERIFIED: https://adevinta.com/press-releases/adevinta-completes-acquisition-of-ebay-classifieds-group/, published 2021-06]:
  - eBay received 342,474,251 class A shares (about 33.3% of voting shares) and 197,520,228 non-voting class B shares, about 44% of capital in total.
  - Scale claimed: #1 positions in 16 countries, about one billion people covered, about three billion monthly visits, and pro forma 2019 revenue of about €1.6bn.
  - Targeted run-rate cost synergies of **€130–165m after three years**.
  - Brent Mclean was named Chief Product & Technology Officer.
- **Regulator-driven divestments (UK CMA).** In June 2021 the CMA accepted undertakings requiring the sale of Shpock and of Gumtree UK together with Motors.co.uk [VERIFIED: Gumtree UK sale release, 2021-12-01].
  - Shpock went to Russmedia Equity Partners (2 June 2021).
  - Gumtree UK and Motors.co.uk went to O3 Industries and Novum Capital (1 December 2021).
- **Non-regulatory adjustment.** eCG Denmark (DBA, Bilbasen) was sold to Schibsted for about €278m [VERIFIED: completion release]. Those brands therefore stayed in the Nordic, Schibsted-owned perimeter.

**What was not sold for regulators.** [VERIFIED by absence in the CMA-related releases fetched] Kijiji (Canada), Gumtree Australia and Vivanuncios were **not** regulatory remedies. They were sold, or kept, later as strategic portfolio choices:

| Asset | Fate | Evidence |
| --- | --- | --- |
| Gumtree UK and Motors.co.uk | Sold Dec 2021 (CMA remedy) | [VERIFIED: release 2021-12-01] |
| Shpock | Sold Jun 2021 (CMA remedy) | [VERIFIED: completion release] |
| eCG Denmark | Sold to Schibsted, Jun 2021 | [VERIFIED: completion release] |
| Gumtree South Africa | Sold Jul 2022 to Impresa Capital | [WIDELY REPORTED: onlinemarketplaces.com, 2022] |
| Gumtree AU, CarsGuide, Autotrader AU | Sold Aug 2022 for US$60m (discontinued operations since Q3 2021) | [VERIFIED: release 2022-08-25] |
| Vivanuncios, Segundamano (MX) | Sold Sep 2022 to Navent; impact "immaterial" | [VERIFIED (trade press): 2022-09-27] |
| Hungary (Használtautó.hu, Jófogás, Autónavigátor) | Exited Sep 2023 | [VERIFIED: AR 2023] |
| Kufar (Belarus) | Exited by 2023 (excluded from 2023 comparables) | [VERIFIED: AR 2023 footnote]. Date and buyer not researched |
| Kijiji Canada | **Retained** as of Oct 2026 ⚠ | [VERIFIED: https://adevinta.com/brands/, fetched 2026-10-19; Strategic Report 2025] |
| Gumtree Ireland, Poland, Singapore; Kijiji Italy | **Not researched** | Open question |

The rationale given for the 2022 sales was a strategic review that focused growth on "five core European markets: Benelux, France, Germany, Italy and Spain", reduced complexity, and used the proceeds to improve leverage [VERIFIED: Gumtree AU release, 2022-08-25].

### 3.3 The 2023 shape: verticals and "Growing at Scale"

From Adevinta Annual Report 2023 (published 26 April 2024) [all VERIFIED: AR 2023]:

- **Headline numbers.** Revenue €1,826m (+11%). EBITDA €651m (+19%). Average FTEs 5,409. About 5,200 employees excluding JVs.
- **Strategy and structure.** The "Growing at Scale" strategy had four pillars: (1) focus on five core geographic markets; (2) concentrate on high-quality verticals; (3) "become fully transactional in Re-Commerce"; (4) leverage technology and transform advertising. In 2023 the company "redesigned the operating model and created a robust structure organised by verticals": Mobility, Re-Commerce, and Real Estate & Emerging Verticals.
- **Revenue by segment and category** (Note 6, € million):

| 2023 | France | mobile.de | European Markets | International Markets | Other/HQ | Total |
| --- | --- | --- | --- | --- | --- | --- |
| Classifieds | 413 | 408 | 510 | 69 | – | 1,399 |
| Advertising | 62 | 24 | 204 | 21 | 2 | 312 |
| Transactional | 73 | 0 | 30 | – | – | 103 |
| Total revenue | 548 | 432 | 744 | 90 | 12 | 1,826 |

| 2022 | France | mobile.de | European Markets | International Markets | Other/HQ | Total |
| --- | --- | --- | --- | --- | --- | --- |
| Classifieds | 371 | 315 | 456 | 84 | – | 1,226 |
| Advertising | 67 | 28 | 209 | 30 | 4 | 337 |
| Transactional | 53 | – | 15 | 0 | – | 69 |
| Total revenue | 492 | 342 | 681 | 114 | 14 | 1,644 |

- **Segment contents.** European Markets = Kleinanzeigen, Marktplaats, 2dehands/2ememain, Spain, Italy, Ireland (Distilled SCH: Daft, DoneDeal, Adverts). willhaben is equity-accounted and excluded. International Markets = Kijiji Canada. OLX Brazil is a 50/50 JV and not consolidated.
- **Per-vertical commentary:**
  - Mobility revenue +20%, "spearheaded by" mobile.de.
  - Real Estate +8%.
  - Re-Commerce transactional revenue grew "more than 50% year-on-year".
  - France: EBITDA margin fell two points "mainly reflecting the evolution of the business mix with an increasing share of transaction services and a decreasing share of highly profitable advertising revenues".
- **Transactional revenue accounting.** It covers "payment facilitation and delivery". Adevinta engages third parties and applies an agent/principal test: it books net where it lacks control of the service and gross where it has control (price discretion, its own customer support). Revenue is recognized at a point in time, on delivery receipt or completion of payment facilitation. The definition of transactional revenue is payment revenue (buyer fee), delivery revenue, and other.
- **Scale indicators:**
  - leboncoin: more than 72m live ads and more than 28m monthly unique visitors.
  - mobile.de: about 40,000 dealers, 1.3m live listings, 107m visits per month.
  - Kleinanzeigen: more than 50m live ads and more than 35m monthly unique users.
  - Marktplaats: more than 8m monthly unique visitors and 350k new ads per day.
- **Q1 2024.** Transactional revenue was €33m, up 31% year on year. "Platform convergence project progressing well and according to plan" [VERIFIED: https://adevinta.com/press-releases/adevinta-asa-ade-adevinta-reports-strong-q1-financial-performance-in-soft-macro-environment/, published 2024-05-28].

**Monetization reading.** [ASSUMPTION/JUDGEMENT] Transactional revenue was only 5.6% of group revenue in 2023 (103/1,826), despite years of investment. In France it was 13% (73/548), and it diluted the margin. mobile.de earned almost all its revenue from classifieds (dealer listings). That is the classic picture: verticals (B2C listings, dealer subscriptions) pay the bills, and generalist C2C transactions are a growth bet with lower margins.

### 3.4 The 2023–2024 take-private

- **The offer.** Announced 21 November 2023 by Aurelia Bidco Norway AS at NOK 115/share, an equity value of about NOK 141bn [VERIFIED: AR 2023]. The bidders were Permira and Blackstone with General Atlantic and TCV as co-investors. Permira, eBay and Schibsted together held about 72.3% at the time [VERIFIED: vend.com release, 2023-11-21].
- **Schibsted's part.** Schibsted held 28.1%. It sold 60% of that stake (208,240,307 shares, about 17%) for about NOK 24bn and rolled about 11.1% into an indirect stake of about 13.6% in the bidder [VERIFIED: same].
- **eBay's part.** eBay rolled 177,115,591 shares (reduced from 202,115,591) [VERIFIED: completion release, 2024-05-29].
- **Settlement and squeeze-out.** Settled 29 May 2024 with the offeror holding 94.79% of capital. Compulsory acquisition of the rest was resolved on 30 May 2024 [VERIFIED: completion and compulsory-acquisition releases, 2024-05-29/30].
- **Ownership after closing.** ⚠ Vend Marketplaces (formerly Schibsted Marketplaces) held about 14% of Adevinta in June 2025 and received €336m from a debt-refinancing distribution [VERIFIED (trade press): https://www.onlinemarketplaces.com/articles/vend-receives-e336-million-in-proceeds-from-adevinta-debt-refinancing-deal/, published 2025-06-02]. Schibsted was renamed Vend in 2025 after selling its media business to the Tinius Trust [WIDELY REPORTED: Wikipedia, 2026].
- **Reporting entity.** The group now reports through Aurelia UK Feederco Ltd. The adevinta.com footer reads "Aurelia Netherlands TargetCo B.V." [VERIFIED: https://adevinta.com/about, fetched 2026-10-19].

### 3.5 The break-up (2025–2026) ⚠

| Change | Detail | Evidence |
| --- | --- | --- |
| willhaben (AT) | 50% stake sold to a Styria Media Group/Sprints JV, announced 13 Mar 2025. Terms undisclosed (Bloomberg: about €500m valuation). Close expected Q2 2025 | [VERIFIED (trade press): onlinemarketplaces.com, 2025-03-13]. Completion not verified |
| Adevinta Spain | Milanuncios, Fotocasa, Habitaclia, InfoJobs, coches.net and motos.net sold to EQT. Announced 21 Jul 2025, **completed 27 Feb 2026**, gain about €1.1bn | [VERIFIED: release 2025-07-21; Strategic Report 2025] |
| Fotocasa/Habitaclia | Onward sale EQT → Scout24 at EV about €153m (2025E revenue about €60m, EBITDA about €11m), conditional on EQT's closing. Reported complete by Mar 2026 | [VERIFIED: Scout24 release 2025-09-18]. [WIDELY REPORTED: https://www.onlinemarketplaces.com/articles/investment-and-ma-roundup-scout24-acquires-fotocasa/, 2026-03-06] |
| L'argus (FR) | Divested effective 1 Nov 2025 | [VERIFIED: Strategic Report 2025, footnote 5] |
| mobile.de | IPO-or-sale "dual track" reported by the FT (Oct 2025), up to about €10bn, possible Frankfurt listing around mid-2026. **No completed transaction found** as of 19 Oct 2026. Still listed on adevinta.com/brands | [WIDELY REPORTED: pymnts.com, 2025-10-08]. [VERIFIED: brands page fetched 2026-10-19] |
| OLX Brasil (50/50 JV with Prosus) | Still listed among Adevinta brands (OLX Brasil, Zap). No sale found | [VERIFIED: https://adevinta.com/brands/, fetched 2026-10-19] |
| Remaining portfolio | Germany (mobile.de, Kleinanzeigen), France (leboncoin plus Agriaffaires, MachineryZone, Truckscorner, A Vendre A Louer), Benelux (Marktplaats, 2dehands/2ememain), Italy (Subito, Automobile.it), Canada (Kijiji), and the Brazil JV | [VERIFIED: Strategic Report 2025; brands page] |

- **2025 results.** Revenue from continuing operations €1,891m. Adjusted EBITDA €865m from continuing operations, €970m including Spain. The group reports "over 50 million monthly unique users" against "over 120 million" in 2024, a difference that reflects both scope and metric definition. Headcount was 4,439 in December 2025, against an average of 5,173 in 2024 [VERIFIED: Strategic Report 2025].
- **Scale in 2025:**
  - mobile.de: 1.6m listings and more than 140m visits per month.
  - Kleinanzeigen: more than 58m live ads.
  - leboncoin: more than 88m live ads and more than 30m monthly unique visitors.
  - Marktplaats: more than 10m monthly unique visitors.
  - Kijiji: more than 4m ads.

  [VERIFIED: Strategic Report 2025]
- **A capability transfer inside the remaining group.** On 3 March 2026 the group set up a Spanish branch to provide software development and product research "under the instruction and for the account of Kleinanzeigen.de GmbH" [VERIFIED: Strategic Report 2025, Events after the reporting period]. [ASSUMPTION/JUDGEMENT] This reads as Barcelona-based central engineering being re-homed under a marketplace rather than under a group function. It is a concrete trace of how decentralization is carried out in legal entities.

---

## PART 4: Engineering — the shared-platform era (2019–2024)

The Adevinta tech blog (adevinta.com/techblog, about 90 posts from August 2022 to March 2026) and associated talks are the primary record. **Name check against the brief's prompts:**

- **"SCHIP" is real.** It is the multi-tenant Kubernetes distribution.
- **"Common Platform" is real.** It is the PaaS umbrella and the name of the team that runs SCHIP.
- **"Unicorn" does not appear in any source fetched.** The real name is **"Unicron"**: "KFP-Unicron", a CLI for Kubeflow Pipelines, and "Unicron" as a training platform. Do not print "Unicorn".
- **"Sch-Platform" was not found.**
- **"Global Components" appears only on a third-party business-template site.** It is not an Adevinta source. Do not cite it.

### 4.1 Common Platform and SCHIP (Kubernetes PaaS)

**Platform timeline from primary sources:**

| Date of evidence | State | Evidence |
| --- | --- | --- |
| Nov 2019 talk, published 2020-01 | "Common Platform": a golden-path PaaS for about 1,500 engineers across about 20 marketplace companies. Toolchain: GitHub, Travis, Artifactory, Spinnaker, FIAAS, Kubernetes, Prometheus, Datadog, Sumologic, ELK. Multi-tenant, multi-region clusters on EC2. Onboarding UI wires up CI/CD, namespaces and observability in about 10 minutes. Voluntary adoption with embedded migration help | [VERIFIED: varoa.net talk write-up, 2020-01-02]. [VERIFIED: https://adevinta.com/es/cuentos/articulos/how-to-build-and-scale-an-internal-paas-for-1500-engineers-galo-navarro/, 2020-01-13] |
| Jan 2020 | More than 50 teams sharing one cluster. Kubernetes in production for three years (versions 1.5.2 → 1.14) | [VERIFIED: https://adevinta.com/es/cuentos/articulos/the-challenges-of-multi-tenancy-in-a-k8s-cluster-thibault-jamet/, 2020-01-13] |
| Feb 2020 | About 200 Spanish microservices (Milanuncios, InfoJobs, Fotocasa, Habitaclia…) migrating from a NetflixOSS EC2 platform (Eureka/Ribbon/Zuul) to Kubernetes. The custom controller "Eurek8s" bridges discovery, so no code changes are needed | [VERIFIED: https://varoa.net/kubernetes/eureka/paas/microservices/loadbalancing/2020/02/12/eureka-kubernetes.html, 2020-02-12] |
| Jun 2023 | SCHIP serves "more than 4,000 developers" and about 5,000 applications. Graviton/ARM nodes offered transparently, defaulting to x86 when an image is multi-arch | [VERIFIED: https://adevinta.com/techblog/transparently-providing-arm-nodes-to-4000-engineers/, 2023-06-06] |
| Sep 2023 | SCHIP is a "multi-tenant, multi-region Kubernetes distribution" with more than 30 production clusters. It moved from kube-aws (stuck at 1.15) to **EKS**. Blue-green cluster upgrades were replaced by in-place control-plane upgrades plus serialized node rebuilds (about 5 min per node; the largest cluster, about 200 nodes, took 6–8 h) | [VERIFIED: https://adevinta.com/techblog/unpacking-the-complexities-of-kubernetes-upgrades-beyond-the-one-click-update/, 2023-09-27] |
| Sep 2023 | A traffic operator uses Route 53 weighted records to shift traffic between HA clusters ("reducing the blast radius"). Cited figures: 60k req/s, 20 customers, 30 clusters | [VERIFIED: https://adevinta.com/techblog/achieve-a-smaller-blast-radius-with-highly-available-kubernetes-clusters/, 2023-09-04] |
| Aug 2023 | GPU serving moved from SageMaker to SCHIP, with KEDA autoscaling on Prometheus metrics. The "Common Platform Team (CPR)" runs SCHIP | [VERIFIED: GPU serving post, 2023-08-08] |
| Aug 2024 / Feb 2025 | Policy engine moved from Gatekeeper/OPA to Kyverno | [VERIFIED: tech blog index titles, 2024-08-07 and 2025-02-12] |
| Oct 2024 | Fully migrated from EKS managed node groups to Karpenter: "over 2,000 Kubernetes nodes and 30 clusters across 25 marketplaces". Up to €30k/month potential savings from moving Intel to AMD instances | [VERIFIED: https://adevinta.com/techblog/the-karpenter-effect-redefining-our-kubernetes-operations/, 2024-10-08] |
| Jun 2025 | PlatformCon retrospective: 8 years of Kubernetes, 30+ clusters in 4 regions, 5,000+ developers, 400k req/s. Path: self-hosted multi-tenant → FIAAS and Common Platform UI → managed control plane → in-place upgrades. Lessons framed around Hyrum's Law | [VERIFIED: PlatformCon 2025 session page, 2025-06-26] |

**Cloud governance (Dec 2024)** [VERIFIED: https://adevinta.com/techblog/multi-cloud-governance-at-scale/, 2024-12-17]:

- 732 AWS accounts and 425 GCP projects, up from fewer than 150 AWS accounts in 2019.
- A 12-person Cloud Governance team (FinOps and GovOps squads) runs a Catalogue API, an Organisations API (accounts → teams → cost centres) and a self-service Cloud Management portal.
- AWS SSO with customer-managed policies, and IPAM-allocated base VPCs.
- Stated principle: "You build it, you run it (and you pay for it)".

**Cloud consolidation (2023)** [VERIFIED: AR 2023, "Investing in technology"]:

- Infrastructure consolidated "to a single public cloud vendor for our EU5 businesses" (AWS). Canada moved to GCP. Most EU5 on-premise platforms moved in 2023.
- Plans for 2024: "close three of four data centre footprints" and "onboard most product platforms onto Adevinta's common internal development platform".
- Target: 100% cloud-native by 2025.

**Reference-architecture inference.** [ASSUMPTION/JUDGEMENT] The published record matches a hub-and-spoke internal developer platform:

- **The hub** is a central team owning a Kubernetes distribution (SCHIP) with a golden-path deploy abstraction (FIAAS), ingress, DNS, logging, IAM and policy SLOs.
- **The tenants** are marketplace product teams, isolated by namespace and account, while the platform shares multi-tenant clusters across regions.
- **The economics** are a fleet-level lever. ARM, AMD and Karpenter moves are worth tens of thousands of euros a month only because roughly 2,000 nodes are pooled.
- **The weakness.** Upgrade blast radius and Hyrum's Law: thousands of applications depend on incidental platform behavior. The 2025 talk itself frames this as the lesson.

No public source describes how SCHIP has been split, or not, since the 2025 decentralization. ⚠

### 4.2 Data platform: central lake to data mesh

- **2019 stance.** Data and analytics were the explicitly centralized domain ("built once; used many times") [VERIFIED: AR 2019].
- **Central big-data platform on AWS (2022–2023).** Posts describe Amazon EMR (on EKS, on EC2 and Serverless), S3 and Glue, an Apache Kyuubi SQL gateway on EKS serving notebooks, Tableau, Hue and dbt [VERIFIED: https://adevinta.com/techblog/integrating-apache-kyuubi-with-elastic-mapreduce-emr/, 2023-10-25]. Related titles: "Practical tricks and tips to reduce AWS EMR costs" (2022-11-15), "Inferring Kafka topic format during JSON deserialization" (2022-11-02), "Lakehouse and Warehouse: sharing data between environments" (2023-10-10) [VERIFIED: tech blog index].
- **Adevinta Spain's platform (CompaaS team).** A Databricks lakehouse in a medallion layout (bronze = source-aligned, silver = aggregated, gold = consumer-aligned data products).
  - Declarative ingestion with **data contracts**, and internal frameworks Poseidon (distributed pipelines), Hermes (non-distributed), "Transform It Yourself" (dbt/SQL) and Atenea (prototyping).
  - About three years of evolution "to a lakehouse that supports data mesh principles".
  - "This mesh has become the link that unifies all our domains into a single platform."

  [VERIFIED: https://adevinta.com/techblog/from-lakehouse-architecture-to-data-mesh/, 2024-12-10]. See also "Evolving from a Data Platform to a Data Products Platform" [VERIFIED: 2023-09-13] and "Creating source-aligned data products in Adevinta Spain" (2024-11-05) [VERIFIED: index].
- **Benelux.** "Artemis", built by analysts, monitors more than 140 product metrics using Prophet forecasts, Databricks scheduling, S3 storage and Slack alerts. It caught an iOS leads drop (about 100k leads/day, about €41k/day) within a day [VERIFIED: https://adevinta.com/techblog/artemis-fostering-autonomy-in-monitoring-data-quality/, 2024-06-25].
- **Real-time analytics.** A vendor case study says Adevinta ran Apache Beam on Google Dataflow with Pub/Sub and adopted ClickHouse Cloud (about 80bn rows) [WIDELY REPORTED: https://clickhouse.com/blog/serving-real-time-analytics-across-marketplaces-at-adevinta (vendor), 2023-04]. Not fetched.
- **Catalog.** DataHub customer story, ingesting metadata from Kafka, S3, Snowflake and dbt [WIDELY REPORTED: datahub.com (vendor), date unknown]. Not fetched.

**Reading.** [ASSUMPTION/JUDGEMENT] Even the most centralizable domain (data) drifted toward federated ownership with a shared substrate. Each marketplace, starting with Spain, built domain data products with contracts on a common lakehouse. That federated shape is what made the 2025–2026 carve-outs feasible, at least for data.

### 4.3 ML platform and shared ML services ("Cognition")

- **ML Golden Path (Aug 2024).** Core layer: an ML Bootstrap Template (Copier CLI or Backstage UI) and "KFP-Unicron", a Typer CLI to lint, test, run and deploy Kubeflow Pipelines. MLflow serves as model registry, on Kubernetes [VERIFIED: https://adevinta.com/techblog/adevintas-machine-learning-golden-path/, 2024-08-20].
  - The redesign came because by January 2023 the platform was "more of a set of scattered tooling rather than an integrated workspace".
  - Governance is federated: a central ML Tooling Catalogue, plus team-specific catalogues whose components can be promoted to the central one.
  - Named marketplace users: Adevinta Spain, leboncoin, Marktplaats, Subito.
- **"Text in Image" OCR service (Mar 2023).** A shared ML API run by the central Cognition team "across Adevinta marketplaces" [VERIFIED: https://adevinta.com/techblog/text-in-image-2-0-improving-ocr-service-with-paddleocr/, 2023-03-06].
  - Purpose: moderation, catching insults, hidden messages, phone numbers, emails and URLs inside ad images, plus search.
  - Moved from FOTS to PaddleOCR on SageMaker: benchmark accuracy 0.4 → 0.8, 7.5× lower latency.
  - Volume: 100m → 330m requests/month.
  - Claimed 12× cheaper than an external OCR API.
- **Other shared Cognition models.** Text detection, car classification and background removal on marketplace images, plus a next-generation image-embedding service [VERIFIED: GPU serving post, 2023-08-08].
- **YAMS media delivery service.** Run by the Data & Analytics Tribe, it serves "over 800 million images, documents, and videos daily". A logging diet (Vector transforms) cut OpenSearch costs 35% [VERIFIED: https://adevinta.com/techblog/the-300-bytes-that-saved-millions-optimising-logging-at-scale/, 2024-07-09]. This is the image service the brief asked about. No other architecture detail is published.

### 4.4 Experimentation: ten tools to one

- **The starting point.** In 2021 Adevinta ran 22 marketplaces, each with its own A/B tool: "Every team had its own tool for A/B testing, resulting in inefficiencies, redundancy and escalating costs." [VERIFIED: https://adevinta.com/techblog/from-ten-to-one-streamlining-experimentation-tooling-at-adevinta/, 2024-10-01]
- **The decision.** A hybrid: keep building the in-house platform and use a third-party tool to bridge the transition in some marketplaces. The decision was made through a cross-functional working group and a scoring matrix with a 3–5-year horizon.
- **The benchmark (Nov 2023)** compared experiments per tech FTE across 21 companies. Its conclusion: "keep building our Experimentation Platform (aka Houston)". Companies running large volumes of experiments rely on internal platforms [VERIFIED: https://adevinta.com/techblog/benchmarking-on-experimentation-tooling/, 2023-11-28].
- **Fisher**, a Python analysis package, was built by **Marktplaats** and then adopted into Houston as the shared toolkit. "Nightingale", a central stats-engine service, uses it.
  - It supports t-tests, CUPED variance reduction and multiple-testing corrections.
  - More than 90% of Marktplaats experiments used Fisher within a year, and analyst hands-on time fell to about 3 h per experiment.

  [VERIFIED: https://adevinta.com/techblog/how-we-matured-fisher-our-a-b-testing-package/, 2023-08-22]
- **Streaming results.** "An alternative approach to A/B test results calculation: Streaming" (2023-11-30) [VERIFIED: index title only].

### 4.5 Search and AI-assisted search

Evidence on the core search engines of leboncoin, Kleinanzeigen or Marktplaats (indexing, ranking, Elasticsearch or Solr topology) was **not found** in this session. The leboncoin Medium blog was blocked, and the other blogs could not be searched for. What is published:

- **Kleinanzeigen search data pipeline (Jan 2025).** "Team Search" uses Debezium CDC from MySQL into Kafka, then a SQL aggregation step, a compacted Kafka topic as a cache of the latest record per user, and HTTP enrichment, producing a denormalized per-user document. Throughput is about 3k events/s end to end in full replays (the figures within the article are inconsistent) [VERIFIED: https://adevinta.com/techblog/make-data-migration-easy-with-debezium-and-apache-kafka/, 2025-01-28].
- **coches.net natural-language car search (Nov 2024).** The LLM converts free text into the site's existing filter parameters; it does not run the search. A cheap moderation pre-classifier comes first. The model is Claude Haiku on Amazon Bedrock with few-shot prompts. Built in 15 days, about 20k invocations/day, about €19/day. "Adoption is still limited." [VERIFIED: https://adevinta.com/techblog/from-filters-to-phrases-our-ai-revolution-in-car-search/, 2024-11-12]
- **leboncoin AI search assistant (Nov 2024).** A conversational assistant that maps needs to keywords, categories and filters. Early stage, no metrics; users "not aware of the benefits" [VERIFIED: https://adevinta.com/techblog/why-would-i-need-an-ai-search-assistant/, 2024-11-19].
- **Central conversational-search prototype (Jan 2024).** A multi-LLM chain (gpt-3.5-turbo for conversation, extraction, guidance and knowledge-graph steps) over the existing search API, with a SPARQL knowledge graph used as a post-filter. Cars only, tailored to France. Not put into production [VERIFIED: https://adevinta.com/techblog/transforming-e-commerce-with-a-conversational-search-assistant-powered-by-large-language-models/, 2024-01-03].
- **leboncoin visual search.** Vector DB, 200 ms target, about 80m listings [WIDELY REPORTED: Zilliz customer page (vendor), date unknown]. Embedding-based retrieval with ANN in Elasticsearch [WIDELY REPORTED: Le Monde Informatique, 2023]. Neither was fetched.

**leboncoin's own tech blog (2026, via the Medium RSS feed).** The feed was read in full for the six most recent posts. They show leboncoin running its own infrastructure organization on AWS as of 2026, not a group platform [VERIFIED: https://medium.com/feed/leboncoin-tech-blog, posts dated 2026-06-03 to 2026-10-13]:

- **Infrastructure self-service bot "BotISS"** (2026-09-29). Built on the Strands SDK with Claude Sonnet 4.5 on Bedrock. It opens Terraform PRs for DNS and similar requests. The feed summary gives about 10 infrastructure engineers supporting about 700 people in about 70 feature teams.
- **Redis → Valkey migration** (2026-06-24). More than 100 ElastiCache instances, almost a billion keys, no backend changes.
- **Transactional email** (2026-06-03). About 12m emails/day moved from 20 Postfix servers to PowerMTA on AWS, with the IP range brought over via BYOIP.
- **"Spark" design system** (2026-07-16). About 60 feature teams on Web, iOS and Android.
- **No search or payments posts** among them.

[ASSUMPTION/JUDGEMENT] A marketplace-owned infra team that provisions with Terraform and AWS-native services is consistent with the 2025 "standalone operating model" (Part 5.3). Whether leboncoin still runs workloads on SCHIP is not stated.

**Pattern.** [ASSUMPTION/JUDGEMENT] Every published LLM search feature keeps the existing structured search as the system of record, and the LLM only produces filters or queries. This is the right architectural seam for listings. It preserves facet correctness, caching and ranking, and it bounds cost (about €19/day at coches.net scale).

### 4.6 Messaging, trust and safety, disputes

- **Chat and moderation were early global components.** "Historically, the team's focus was on consolidating enabling capabilities such as cloud and data, and overarching elements such as chat and moderation." [VERIFIED: AR 2023, "Investing in technology"] No architecture post on the shared messaging service was found.
- **Dispute management back office (Feb 2023).** Built as a reusable component "that can be plugged into any marketplace" for transaction disputes (item not as described, broken, not delivered) [VERIFIED: https://adevinta.com/techblog/from-hello-world-to-a-dispute-management-back-office/, 2023-02-02]:
  - It ingests per-marketplace events (Kafka, SQS, REST) and normalizes them into a common model.
  - The API layer is Kotlin/Ktor. The frontend uses React and MUI with Webpack Module Federation micro-frontends, so marketplaces can add their own features.
  - The demo used Subito and Milanuncios data.
  - Design constraint: "We couldn't hardcode anything… or make any assumptions."
- **Document rasterization for safe sharing** (2023-05-25) [VERIFIED: index title only].

**Reference-architecture inference.** [ASSUMPTION/JUDGEMENT] The dispute tool is the canonical shape for a cross-marketplace capability: an anti-corruption ingestion layer per tenant, a canonical event model, and extensible micro-frontends. Its cost is that every marketplace must emit good transaction events, so the global component depends on local event quality.

### 4.7 Developer productivity and AI tooling

- **The 2025 pilot.** 77 engineers in 14 squads across leboncoin, mobile.de, Kleinanzeigen and Marktplaats (May–June 2025, 165 tasks). Self-reported productivity gains: Claude Code about 43%, Cursor about 24%, GitHub Copilot about 1%.
- **The decision.** Deploy Claude Code to "over 2,000 software engineers".
- **Caveats the authors state.** One month, subjective estimates, small sample. [VERIFIED: https://adevinta.com/techblog/a-pragmatic-evaluation-of-software-engineering-ai-tooling/, 2026-03-09]
- **Engineer counts across sources** (useful as a decentralization signal, with caution about definitions):
  - "1,500 engineers" (2019 talk title).
  - "more than 4,000 developers" on SCHIP (2023).
  - "over 5,000 developers" (2025 PlatformCon abstract, likely cumulative or historical).
  - "over 2,000 software engineers" (2026).

  [ASSUMPTION/JUDGEMENT] The drop from 4,000+ to 2,000+ coincides with the eCG integration peak, then the divestments (Spain alone was a large engineering site) and the 2025 headcount reduction to 4,439 employees. Definitions differ, so do not print a precise "engineers lost" number.

---

## PART 5: The organizational swings

### 5.1 Phase map

| Phase | Years | Organizing principle | Evidence |
| --- | --- | --- | --- |
| Federated copy-paste | ~2006–2015 | Local sites on a Blocket-derived base. Strong local autonomy | [ASSUMPTION/JUDGEMENT]; Nieman 2012 [unverified] |
| Global product & tech push | 2016–2018 | "One global product and tech organization" (Schibsted) | [WIDELY REPORTED: Schibsted 2016 investor material] |
| Selective centralization | 2019–2020 | Local product autonomy; central data/analytics and scalable components; a voluntary PaaS | [VERIFIED: AR 2019; Navarro 2020] |
| Integration and consolidation | 2021–2023 | eCG absorbed; €130–165m synergy target; cloud and data-centre consolidation; shared chat, moderation, data and ML; ten experimentation tools to one | [VERIFIED: completion release; AR 2023; tech blog] |
| Verticalization and platform convergence | 2023–mid-2024 | Organization by verticals (Mobility, Re-Commerce, Real Estate); **leboncoin and Kleinanzeigen platforms to become "a unified global platform"** for generalist marketplaces | [VERIFIED: AR 2023; Q1 2024 release] |
| Decentralization and break-up | Jul 2024–2026 | New Target Operating Model "empowering local marketplaces"; central functions ramped down; IP "localised"; sale of willhaben and Spain; mobile.de dual track | [VERIFIED: Strategic Reports 2024 and 2025] |

### 5.2 The convergence decision (2023), in Adevinta's words

> "Historically, the team's focus was on consolidating enabling capabilities such as cloud and data, and overarching elements such as chat and moderation. However, the compelling case for stronger consolidation prompted a change in this strategy. The core rationale lies in a pronounced overlap in customer needs across all of Adevinta's markets and the technical complexity inherent in expected user experiences. Rather than individually addressing local market customer needs — such as the full transactional journey, AI-assisted search and modern approaches to first-party advertising and personalised marketing — the team has opted to avoid duplicating these investments… In collaboration, Kleinanzeigen, leboncoin and global teams embarked on transforming the two platforms into a unified global platform to support Adevinta's generalist marketplaces." [VERIFIED: AR 2023, p. 26]

The CEO letter adds "the creation of a multi-tenant platform… building shared capabilities across automation, cloud, data, IT enterprise services and cybersecurity" and "scaling the best elements of each marketplace across all our platforms" [VERIFIED: AR 2023, CEO letter].

**Analyst reading.** [ASSUMPTION/JUDGEMENT] This is the boldest consolidation step in the record. It moves from sharing *enabling* capabilities (infrastructure, data, chat, moderation) to sharing the *product platform itself* for two large generalist marketplaces in different countries, languages and legal regimes, each with its own transactional stack. Whether it shipped is not publicly documented. The Q1 2024 release says only that it was "progressing well and according to plan" [VERIFIED]. No later source confirms delivery.

### 5.3 The reversal (2024–2025), in Adevinta's words

> "The Group has evolved from a centralised structure to a decentralised, standalone operating model, empowering each marketplace to operate with greater independence, accountability and focus. This transition has included the ramp-down of central functions, the transfer of key capabilities, the localisation of intellectual property, and the realignment of reporting structures." [VERIFIED: Strategic Report 2025, p. 3]

Supporting traces:

- **Plans framed as market-specific.** The group says its focus has "increasingly centred on initiatives with the greatest potential for scalable, market-specific impact" [VERIFIED: same].
- **A temporary cost spike from running two sets of services.** "Cloud provider emissions… more than doubled; this is expected to mainly reflect a temporary spike linked to our ongoing decentralisation, which required parallel running of central and local services during a transitional period." [VERIFIED: Strategic Report 2025, p. 24–25]
- **Risks named in advance.** The 2024 risk register already lists "operational decentralisation (which may affect areas such as… trust and fraud) and data decentralisation" [VERIFIED: Strategic Report 2024].
- **Carve-out support.** EQT's release on Spain promises to help Adevinta Spain "as it transforms into a fully independent company", with EY as "carve-out advisor" [VERIFIED: https://www.inderes.fi/releases/eqt-to-acquire-adevintas-spanish-online-classifieds-businesses, 2025-07-21].

**Analyst reading.** [ASSUMPTION/JUDGEMENT] For private-equity owners pursuing break-up value (Spain €2bn, willhaben about €500m, mobile.de up to €10bn reported), shared platforms are a *liability*: they create entanglement, transitional services, IP-ownership questions and double running costs at exit. The same shared platform that the 2021 synergy case valued became a separation cost in 2025. The technical lesson is not "centralization was wrong". It is that **platform topology must match the capital strategy**, and that separability (tenant-scoped data, per-tenant accounts, portable deploy abstractions, clean IP ownership) is a design requirement whenever ownership might change.

---

## PART 6: The transactional pivot

### 6.1 What is documented

| Marketplace | Transactional capabilities | Evidence |
| --- | --- | --- |
| leboncoin | Transactional model launched in some generalist categories in 2019. Acts as trusted third party since 2018. Adyen is the payment partner. Transactional revenue €73m in 2023 (€53m in 2022) | [VERIFIED: AR 2019; AR 2023 Note 6]. [WIDELY REPORTED: Wikipedia leboncoin, 2026] |
| Kleinanzeigen | "Sicher bezahlen": agree in chat → "Angebot machen" or "Direkt kaufen". **Adyen holds funds up to 14 days** until the buyer confirms receipt, then auto-releases. Buyer fee; seller free for Direkt kaufen. Methods: card, Apple Pay, Google Pay, PayPal, bank/Sofort. Integrated DHL/Hermes labels and automatic tracking. Buyer protection for not shipped, not as described, counterfeit, wrong item or incomplete | [VERIFIED: https://themen.kleinanzeigen.de/sicher-bezahlen/, fetched 2026-10-19, date unknown] |
| Kleinanzeigen strategy | "Strong ambitions to become a full transactional leader in German Re-Commerce" after the 2023 rebrand | [VERIFIED: AR 2023] |
| Marktplaats | Transactional services launched in 2017, shipping in 2019, buyer protection; second shipping company integrated in 2022; home shipping for a second carrier in 2023 | [VERIFIED: AR 2023, p. 25] |
| Marktplaats product naming | The original escrow-style option **"Gelijk Oversteken"** was withdrawn in April 2022 as "not safe enough". Its successor, **"Kopersbescherming"** (buyer protection), works through the PSP **Online Payment Platform (OPP)**, which holds the money until a week after receipt and pays the seller on day 8 if there are no complaints. The buyer pays a 5% fee; the seller pays nothing. Usage is optional and in-platform messaging only. The brief's "Gelijk betalen" does not exist under that name | [VERIFIED: https://radar.avrotros.nl/artikel/dit-is-de-vervanger-voor-de-gelijk-oversteken-functie-van-marktplaats-52677, published 2022-04-25]. ⚠ Fee and terms may have changed since |
| 2dehands/2ememain | Not documented in fetched sources | Open |
| Subito, Milanuncios | On-platform buy/pay/ship flows feed the shared dispute back office | [VERIFIED: dispute post, 2023-02-02] |
| mobile.de | Transactional revenue about €0 in 2023. Monetization is dealer classifieds plus financing and leasing services | [VERIFIED: AR 2023 Note 6; Strategic Report 2025] |
| Group | Transactional revenue €69m (2022) → €103m (2023) → Q1 2024 €33m (+31%). "Becoming fully transactional in Re-Commerce" was a strategic pillar | [VERIFIED: AR 2023; Q1 2024 release] |

- **Shipping is visible in emissions data.** The 2025 report discusses shipment-volume-driven Scope 3 emissions for Kleinanzeigen, Subito, Marktplaats/2dehands-2ememain, leboncoin and Milanuncios, so all five run shipping integrations [VERIFIED: Strategic Report 2025, p. 25].
- **Transactional services cost money to run.** Rising "direct costs from transactional services (such as payment and shipping service provider costs)" drove up other expenses [VERIFIED: AR 2023].

### 6.2 Architecture inference

[ASSUMPTION/JUDGEMENT] The public evidence fits a common C2C escrow pattern:

- **Payments.** The marketplace does not hold funds. A licensed PSP (Adyen, for Kleinanzeigen and leboncoin) holds them under its marketplace or platform product.
- **The marketplace's own role.** It owns the offer/accept state machine in chat, the buyer-fee pricing, carrier label generation and tracking, the release timer (14 days at Kleinanzeigen), and dispute handling.
- **Revenue recognition.** The agent/principal accounting note implies per-market contract structures. Some services are booked gross, which means the marketplace is principal for the service and runs its own support.
- **Why centralization looked attractive.** The full transactional journey was exactly what the 2023 convergence plan said it would stop duplicating.
- **Why decentralization reverses it.** Under the 2025 decentralized model, each market's PSP contracts, carriers and consumer-law regimes argue for local ownership again.

Chapter writers should cross-reference the book's payments chapter for PSP marketplace models.

---

## PART 7: Lessons on platform consolidation after acquisitions

1. **The 2019 rule is a good default.** Centralize where "investment requirements are large and the technology is uniform" (data, infrastructure). Keep product surfaces local [VERIFIED: AR 2019].
2. **A voluntary, product-managed PaaS with embedded migration engineers can reach about 1,500 → 4,000+ developers without a mandate** [VERIFIED: Navarro 2020; ARM post 2023]. Migration tooling that needs no code changes (Eurek8s) carries the adoption [VERIFIED: 2020-02-12].
3. **Fleet pooling is where central platforms pay.** About 2,000 nodes across 30 clusters made the ARM, AMD and Karpenter moves worth doing [VERIFIED: 2023-06-06; 2024-10-08]. The same pooling enlarges upgrade blast radius and Hyrum's-Law coupling [VERIFIED: 2023-09-27; PlatformCon 2025].
4. **Many of the best global components start as local inventions.** FIAAS came from FINN.no and Fisher from Marktplaats [VERIFIED]. A "promote to central catalogue" path, as in the ML Golden Path, institutionalizes this [VERIFIED: 2024-08-20].
5. **Tool sprawl after acquisitions is measurable and fixable,** for example ten A/B tools across 22 marketplaces. The fix is an explicit build/buy decision with a bridging vendor [VERIFIED: 2024-10-01].
6. **Shared ML services work best for narrow, uniform tasks** such as OCR, image embeddings and media delivery, and at real volume (330m OCR calls/month; 800m media objects/day) [VERIFIED: 2023-03-06; 2024-07-09].
7. **Cross-marketplace product components need an anti-corruption ingestion layer** and extensible UIs. They inherit each market's event quality [VERIFIED: dispute post 2023-02-02; inference ASSUMPTION/JUDGEMENT].
8. **Converging whole product platforms is a different class of bet** from sharing infrastructure. Adevinta announced leboncoin + Kleinanzeigen convergence in 2023, and no public evidence shows it completed before the 2025 reversal [VERIFIED: AR 2023; Q1 2024; absence ASSUMPTION/JUDGEMENT].
9. **Capital strategy dictates platform topology.** Break-up-oriented owners turned shared platforms into separation costs: double running, IP localization, carve-out advisors [VERIFIED: Strategic Report 2025; EQT release].
10. **Design for separability from day one:**
    - tenant-scoped cloud accounts and cost centres (Adevinta had about 1,157 accounts and projects mapped to cost centres);
    - per-domain data products with contracts;
    - portable deploy abstractions.

    These make divestment cheaper [VERIFIED: 2024-12-17; 2024-12-10; inference ASSUMPTION/JUDGEMENT].
11. **Transactional C2C raises revenue but dilutes margin,** and it is operationally heavy (PSP and carrier costs, support, disputes). In France it took the EBITDA margin down two points [VERIFIED: AR 2023].
12. **LLM search should sit in front of structured search, not replace it** (LLM → filters). It is cheap, but adoption is slow [VERIFIED: coches.net 2024-11-12; leboncoin 2024-11-19].
13. **Regulators shape the post-acquisition footprint as much as strategy does.** The UK CMA forced the Gumtree UK, Motors.co.uk and Shpock sales, so overlapping platforms in the same country never needed technical integration [VERIFIED: 2021-12-01].

---

## Key lessons for the book (summary list)

1. **Centralize the uniform, expensive layers; localize the product.** Adevinta's own 2019 rule [VERIFIED: AR 2019].
2. **Platform-as-product with voluntary adoption scales.** Golden paths, about 10-minute onboarding, embedded migration support and zero-code-change bridges took the platform to thousands of engineers [VERIFIED: Navarro 2020; Eurek8s 2020; ARM 2023].
3. **Pooling delivers fleet economics but couples tenants.** Plan upgrade strategy (blue-green vs in-place), multi-cluster traffic shifting and Hyrum's-Law hygiene [VERIFIED: SCHIP posts 2023–2024; PlatformCon 2025].
4. **Harvest local inventions into the global platform.** FIAAS and Fisher prove the path [VERIFIED].
5. **Consolidate duplicated tools with an explicit build/buy/bridge decision** [VERIFIED: experimentation 2023–2024].
6. **Shared ML and media services pay off for narrow, high-volume tasks** (OCR, embeddings, media delivery) [VERIFIED: Cognition and YAMS posts].
7. **Cross-tenant product services need canonical event models and extensible micro-frontends** [VERIFIED: dispute post]. The design judgement is [ASSUMPTION/JUDGEMENT].
8. **Product-platform convergence across countries is high-risk.** Announce it only with a plan that survives a change of owner [VERIFIED: AR 2023]. The outcome is [ASSUMPTION/JUDGEMENT].
9. **Ownership and capital strategy can flip the economics of shared platforms within two years.** Design for separability [VERIFIED: Strategic Report 2025; EQT carve-out].
10. **Transactional C2C is a margin-dilutive, PSP-mediated escrow architecture.** Keep the money with a licensed PSP and own the state machine, logistics and disputes [VERIFIED: Kleinanzeigen Sicher bezahlen; AR 2023].
11. **Federated data ownership on a shared lakehouse survives reorganizations better than a central lake** [VERIFIED: Adevinta Spain posts 2023–2024]. The comparison is [ASSUMPTION/JUDGEMENT].
12. **Put LLMs in front of structured search as query/filter translators** [VERIFIED: coches.net; leboncoin].
13. **Antitrust remedies pre-empt integration in overlapping markets.** Model regulatory divestments into post-merger architecture plans [VERIFIED: CMA-driven sales].

---

## Open questions / not publicly documented

- **leboncoin + Kleinanzeigen convergence.** Did the "unified global platform" for generalist marketplaces ship, partly or fully? What was its architecture (shared backend with per-market frontends? one codebase?), and what happened to it under the 2025 decentralization? No public source was found after Q1 2024.
- **SCHIP after 2025.** Is it still one multi-tenant platform for the remaining marketplaces, or was it split per marketplace? How was Adevinta Spain carved out of SCHIP, the data lake and the shared accounts, and was there a transitional services agreement? EQT and Adevinta mention only "transition" support.
- **Global messaging/chat and moderation services.** The AR 2023 says they were consolidated, but no architecture post was found.
- **Core search engines** (leboncoin, Kleinanzeigen, Marktplaats, mobile.de). Technology, ranking and index topology were not researched; this is a gap caused by the search budget.
- **Marketplace engineering blogs.** The Kleinanzeigen, Marktplaats and mobile.de blogs were not researched. Only recent posts from the leboncoin blog were read, through its RSS feed. Try `https://medium.com/feed/<publication>` for the others.
- **Transactional product names and dates.**
  - 2dehands' payment product name, and whether Marktplaats' OPP-based Kopersbescherming still uses OPP in 2026.
  - The launch date of Kleinanzeigen "Sicher bezahlen".
  - leboncoin's secure-payment and delivery launch dates beyond "2018/2019".
- **Divestments not checked:** Gumtree Ireland, Poland and Singapore; Kijiji Italy; Kufar (buyer and date); the remaining LatAm and North Africa assets (Yapo, Fincaraiz, Corotos, Tayara, Avito.ma) after 2019.
- **mobile.de.** IPO or sale outcome as of October 2026 ⚠.
- **willhaben.** Completion date of the sale ⚠.
- **OLX Brasil JV.** Status after 2025 ⚠. The brands page still lists it.
- **Schibsted-era Blocket platform.** Primary documentation of the shared platform and the copy-paste rollout model, and the founding and acquisition years of Finn.no, Blocket, Subito, Milanuncios and Fotocasa.
- **eCG synergies.** Whether the €130–165m target was reported as achieved, and how much came from technology consolidation.
- **Monetization per vertical in 2020–2021.** The annual reports for those years were not fetched. The 2022 annual report URL returned 404.

---

## Source list

| # | Title | Publisher | Date | URL |
| --- | --- | --- | --- | --- |
| 1 | Introducing Adevinta, an international family of local digital marketplaces | Schibsted/Vend | 2019-02-25 | https://vend.com/news/introducing-adevinta-an-international-family-of-local-digital-marketplaces |
| 2 | Adevinta ASA issues largest IPO in the Nordic region in 10 years (search summary only) | Cleary Gottlieb | 2019 | https://www.clearygottlieb.com/news-and-insights/news-listing/adevinta-asa-issues-largest-ipo-in-the-nordic-region-in-10-years |
| 3 | Adevinta Annual Report 2019 (PDF) | Adevinta | 2020 | https://adevinta.com/app/uploads/2021/10/adevinta-annual-report-2019.pdf |
| 4 | eBay sells Gumtree as part of US$9bn classifieds deal | Inside Retail | 2020-07-23 | https://insideretail.com.au/news/ebay-sells-gumtree-as-part-of-us9bn-classifieds-deal-202007 |
| 5 | Acquisition of eBay Classifieds Group complete | Adevinta | 2021-06-25/30 | https://adevinta.com/press-releases/adevinta-completes-acquisition-of-ebay-classifieds-group/ |
| 6 | Adevinta sells Gumtree UK and Motors.co.uk to O3 Industries and Novum Capital | Adevinta | 2021-12-01 | https://adevinta.com/press-releases/adevinta-sells-gumtree-uk-and-motors-co-uk-to-o3-industries-and-novum-capital/ |
| 7 | Adevinta announces sale of Gumtree Australia, CarsGuide and Autotrader Australia | Adevinta | 2022-08-25 | https://adevinta.com/press-releases/adevinta-asa-ade-adevinta-announces-sale-of-gumtree-australia-carsguide-and-autotrader-australia/ |
| 8 | Adevinta sells Vivanuncios and Segundamano to Navent Group | Online Marketplaces | 2022-09-27 | https://www.onlinemarketplaces.com/articles/adevinta-sells-vivanuncios-and-segundamano-to-navent-group |
| 9 | Adevinta Annual Report 2023 (PDF) | Adevinta / Euronext | 2024-04-26 | https://live.euronext.com/sites/default/files/company_press_releases/attachments_oslo/2024/04/26/616971_Adevinta%20AR%202023.pdf |
| 10 | Schibsted supports the voluntary offer for Adevinta, reducing its stake by 60% | Schibsted/Vend | 2023-11-21 | https://vend.com/news/schibsted-supports-the-voluntary-offer-for-adevinta-reducing-its-stake-in-adevinta-by-60 |
| 11 | Adevinta in €14 billion buyout led by Blackstone and Permira | Cleary Gottlieb | 2023-11 | https://clearygottlieb.com/news-and-insights/news-listing/adevinta-in-14-billion-buyout-led-by-blackstone-and-permira-holdings-limited |
| 12 | Adevinta reports strong Q1 financial performance in soft macro environment | Adevinta | 2024-05-28 | https://adevinta.com/press-releases/adevinta-asa-ade-adevinta-reports-strong-q1-financial-performance-in-soft-macro-environment/ |
| 13 | Completion of the voluntary offer for all issued and outstanding class A shares in Adevinta ASA | Adevinta | 2024-05-29 | https://adevinta.com/press-releases/adevinta-asa-ade-completion-of-the-voluntary-offer-for-all-issued-and-outstanding-ordinary-class-a-shares-in-adevinta-asa/ |
| 14 | Compulsory acquisition of shares in Adevinta ASA (search summary) | Adevinta | 2024-05-30 | https://adevinta.com/press-releases/adevinta-asa-ade-compulsory-acquisition-of-shares-in-adevinta-asa/ |
| 15 | Strategic Report 2024, Aurelia UK Feederco Ltd (PDF) | Adevinta | 2025-04 | https://adevinta.com/wp-content/uploads/2025/04/Strategic-Report-2024-Aurelia-UK-Feederco-Ltd-FS.docx.pdf |
| 16 | Strategic Report 2025, Aurelia UK Feederco Ltd (PDF) | Adevinta | 2026-05 | https://adevinta.com/wp-content/uploads/2026/05/Strategic-Report-2025-Aurelia-UK-Feederco-Ltd.pdf |
| 17 | Annual reports index | Adevinta | fetched 2026-10-19 | https://adevinta.com/finance/annual-reports/ |
| 18 | Funding and investment roundup: Adevinta (willhaben) | Online Marketplaces | 2025-03-13 | https://www.onlinemarketplaces.com/articles/funding-and-investment-roundup-adevinta-justmovein-rea-group-tomo-mortgage/ |
| 19 | Vend receives €336 million in proceeds from Adevinta debt refinancing | Online Marketplaces | 2025-06-02 | https://www.onlinemarketplaces.com/articles/vend-receives-e336-million-in-proceeds-from-adevinta-debt-refinancing-deal/ |
| 20 | Adevinta announces sale of its Spanish business to EQT | Adevinta | 2025-07-21 | https://adevinta.com/press-releases/adevinta-announces-sale-of-its-spanish-business-to-eqt/ |
| 21 | EQT to acquire Adevinta's Spanish online classifieds businesses | EQT via Inderes | 2025-07-21 | https://www.inderes.fi/releases/eqt-to-acquire-adevintas-spanish-online-classifieds-businesses |
| 22 | EQT agrees to acquire Adevinta's Spanish assets | Online Marketplaces | 2025-07-21 | https://www.onlinemarketplaces.com/articles/eqt-agrees-to-acquire-adevintas-spanish-assets/ |
| 23 | Scout24 acquires Spanish online real estate platforms Fotocasa and Habitaclia | Scout24 | 2025-09-18 | https://www.scout24.com/en/news-media/news/detail/scout24-acquires-spanish-online-real-estate-platforms-fotocasa-and-habitaclia |
| 24 | Investment and M&A roundup: Scout24 acquires Fotocasa | Online Marketplaces | 2026-03-06 | https://www.onlinemarketplaces.com/articles/investment-and-ma-roundup-scout24-acquires-fotocasa/ |
| 25 | Adevinta considers IPO or sale of mobile.de (relaying the FT) | PYMNTS | 2025-10-08 | https://www.pymnts.com/?p=3112865 |
| 26 | About Adevinta | Adevinta | fetched 2026-10-19 | https://adevinta.com/about |
| 27 | Brands | Adevinta | fetched 2026-10-19 | https://adevinta.com/brands/ |
| 28 | Press room | Adevinta | fetched 2026-10-19 | https://adevinta.com/press-room/ |
| 29 | Schibsted | Wikipedia | fetched 2026-10-19 | https://en.wikipedia.org/wiki/Schibsted |
| 30 | Leboncoin | Wikipedia | fetched 2026-10-19 | https://en.wikipedia.org/wiki/Leboncoin |
| 31 | Marktplaats.nl | Wikipedia | fetched 2026-10-19 | https://en.wikipedia.org/wiki/Marktplaats.nl |
| 32 | Looking to Europe for news industry innovation, part 2 (not fetched, 403) | Nieman Lab | 2012-02 | https://www.niemanlab.org/2012/02/looking-to-europe-for-news-industry-innovation-part-2-schibsteds-stunning-classifieds-and-services-business/ |
| 33 | Continuous delivery while migrating to Kubernetes (FINN.no, KubeCon EU 2017 slides) | FINN.no / Schibsted | 2017-03 | https://raw.githack.com/mm-k8s-ug/kubecon-slides/master/slides/2017-kubecon-eu/Lessons%20Learned%20From%20Maintaining%20Continuous%20Delivery%20While%20Migrating%20From%20a%20Static%20Infrastructure%20to%20Kubernetes%20%5BB%5D%20-%20Audun%20Fauchald%20Strand%20&%20%C3%98yvind%20Ingebrigtsen%20%C3%98vergaard,%20FINN.no%20%20Schibsted%20-%20finn-no-kubecon.pdf |
| 34 | fiaas-deploy-daemon | GitHub (FIAAS) | fetched 2026-10-19 | https://github.com/fiaas/fiaas-deploy-daemon |
| 35 | How to build a PaaS for 1500 engineers (talk write-up) | Galo Navarro (varoa.net) | 2020-01-02 | https://varoa.net/paas/infrastructure/platform/kubernetes/cloud/2020/01/02/talk-how-to-build-a-paas-for-1500-engineers.html |
| 36 | How to build and scale an internal PaaS for 1,500 engineers | Adevinta Stories | 2020-01-13 | https://adevinta.com/es/cuentos/articulos/how-to-build-and-scale-an-internal-paas-for-1500-engineers-galo-navarro/ |
| 37 | The challenges of multi-tenancy in a K8s cluster | Adevinta Stories | 2020-01-13 | https://adevinta.com/es/cuentos/articulos/the-challenges-of-multi-tenancy-in-a-k8s-cluster-thibault-jamet/ |
| 38 | Migrating an Eureka-based microservice fleet to Kubernetes | Galo Navarro (varoa.net) | 2020-02-12 | https://varoa.net/kubernetes/eureka/paas/microservices/loadbalancing/2020/02/12/eureka-kubernetes.html |
| 39 | How organisations cripple engineering teams with good intentions (checked; no Adevinta content) | Galo Navarro (varoa.net) | 2024-01-09 | https://varoa.net/2024/01/09/how-organisations-cripple-engineering-teams-with-good-intentions.html |
| 40 | 8 years of Kubernetes platform evolution: Do's and don'ts | PlatformCon 2025 | 2025-06-26 | https://2025.platformcon.com/sessions/8-years-of-kubernetes-platform-evolution-do-s-and-don-ts |
| 41 | Adevinta Tech Blog index, pages 1–10 | Adevinta | 2022-08 to 2026-03 | https://adevinta.com/techblog/ |
| 42 | Text in Image 2.0: improving OCR service with PaddleOCR | Adevinta Tech Blog | 2023-03-06 | https://adevinta.com/techblog/text-in-image-2-0-improving-ocr-service-with-paddleocr/ |
| 43 | From Hello World to a Dispute Management back office | Adevinta Tech Blog | 2023-02-02 | https://adevinta.com/techblog/from-hello-world-to-a-dispute-management-back-office/ |
| 44 | Transparently providing ARM nodes to 4,000 engineers | Adevinta Tech Blog | 2023-06-06 | https://adevinta.com/techblog/transparently-providing-arm-nodes-to-4000-engineers/ |
| 45 | How we joined forces to enable GPU serving for our AI solutions | Adevinta Tech Blog | 2023-08-08 | https://adevinta.com/techblog/how-we-joined-forces-to-enable-gpu-serving-for-our-ai-solutions/ |
| 46 | How we matured Fisher, our A/B testing package | Adevinta Tech Blog | 2023-08-22 | https://adevinta.com/techblog/how-we-matured-fisher-our-a-b-testing-package/ |
| 47 | Achieve a smaller blast radius with highly available Kubernetes clusters | Adevinta Tech Blog | 2023-09-04 | https://adevinta.com/techblog/achieve-a-smaller-blast-radius-with-highly-available-kubernetes-clusters/ |
| 48 | Evolving from a Data Platform to a Data Products Platform | Adevinta Tech Blog | 2023-09-13 | https://adevinta.com/techblog/evolving-from-a-data-platform-to-a-data-products-platform/ |
| 49 | Unpacking the complexities of Kubernetes upgrades: beyond the one-click update | Adevinta Tech Blog | 2023-09-27 | https://adevinta.com/techblog/unpacking-the-complexities-of-kubernetes-upgrades-beyond-the-one-click-update/ |
| 50 | Working in a multidisciplinary machine learning team to bring value to our users | Adevinta Tech Blog | 2023-10-17 | https://adevinta.com/techblog/working-in-a-multidisciplinary-machine-learning-team-to-bring-value-to-our-users/ |
| 51 | Integrating Apache Kyuubi with Elastic MapReduce (EMR) | Adevinta Tech Blog | 2023-10-25 | https://adevinta.com/techblog/integrating-apache-kyuubi-with-elastic-mapreduce-emr/ |
| 52 | Benchmarking on experimentation tooling | Adevinta Tech Blog | 2023-11-28 | https://adevinta.com/techblog/benchmarking-on-experimentation-tooling/ |
| 53 | Six months with Adevinta | Adevinta Tech Blog | 2022-12-14 | https://adevinta.com/techblog/six-months-with-adevinta/ |
| 54 | Transforming e-commerce with a conversational search assistant powered by LLMs | Adevinta Tech Blog | 2024-01-03 | https://adevinta.com/techblog/transforming-e-commerce-with-a-conversational-search-assistant-powered-by-large-language-models/ |
| 55 | Centralisation and distribution: when one node is enough | Adevinta Tech Blog | 2024-05-28 | https://adevinta.com/techblog/centralisation-and-distribution-when-one-node-is-enough/ |
| 56 | Artemis: fostering autonomy in monitoring data quality | Adevinta Tech Blog | 2024-06-25 | https://adevinta.com/techblog/artemis-fostering-autonomy-in-monitoring-data-quality/ |
| 57 | The 300 bytes that saved millions: optimising logging at scale | Adevinta Tech Blog | 2024-07-09 | https://adevinta.com/techblog/the-300-bytes-that-saved-millions-optimising-logging-at-scale/ |
| 58 | Adevinta's Machine Learning Golden Path | Adevinta Tech Blog | 2024-08-20 | https://adevinta.com/techblog/adevintas-machine-learning-golden-path/ |
| 59 | From ten to one: streamlining experimentation tooling at Adevinta | Adevinta Tech Blog | 2024-10-01 | https://adevinta.com/techblog/from-ten-to-one-streamlining-experimentation-tooling-at-adevinta/ |
| 60 | The Karpenter effect: redefining our Kubernetes operations | Adevinta Tech Blog | 2024-10-08 | https://adevinta.com/techblog/the-karpenter-effect-redefining-our-kubernetes-operations/ |
| 61 | From filters to phrases: our AI revolution in car search | Adevinta Tech Blog | 2024-11-12 | https://adevinta.com/techblog/from-filters-to-phrases-our-ai-revolution-in-car-search/ |
| 62 | Why would I need an AI search assistant? | Adevinta Tech Blog | 2024-11-19 | https://adevinta.com/techblog/why-would-i-need-an-ai-search-assistant/ |
| 63 | From Lakehouse architecture to data mesh | Adevinta Tech Blog | 2024-12-10 | https://adevinta.com/techblog/from-lakehouse-architecture-to-data-mesh/ |
| 64 | Multi-cloud governance at scale | Adevinta Tech Blog | 2024-12-17 | https://adevinta.com/techblog/multi-cloud-governance-at-scale/ |
| 65 | Make data migration easy with Debezium and Apache Kafka | Adevinta Tech Blog | 2025-01-28 | https://adevinta.com/techblog/make-data-migration-easy-with-debezium-and-apache-kafka/ |
| 66 | A pragmatic evaluation of software engineering AI tooling | Adevinta Tech Blog | 2026-03-09 | https://adevinta.com/techblog/a-pragmatic-evaluation-of-software-engineering-ai-tooling/ |
| 67 | Sicher bezahlen | Kleinanzeigen | fetched 2026-10-19, date unknown | https://themen.kleinanzeigen.de/sicher-bezahlen/ |
| 68 | Serving real-time analytics across marketplaces at Adevinta (vendor; not fetched) | ClickHouse | 2023-04 | https://clickhouse.com/blog/serving-real-time-analytics-across-marketplaces-at-adevinta |
| 69 | leboncoin visual search case study (vendor; not fetched) | Zilliz | date unknown | https://zilliz.com/customers/leboncoin |
| 70 | leboncoin tech blog RSS feed (6 posts, Jun–Oct 2026) | leboncoin / Medium | 2026-06-03 to 2026-10-13 | https://medium.com/feed/leboncoin-tech-blog |
| 71 | Dit is de vervanger voor de 'Gelijk Oversteken' functie van Marktplaats | AVROTROS Radar | 2022-04-25 | https://radar.avrotros.nl/artikel/dit-is-de-vervanger-voor-de-gelijk-oversteken-functie-van-marktplaats-52677 |
