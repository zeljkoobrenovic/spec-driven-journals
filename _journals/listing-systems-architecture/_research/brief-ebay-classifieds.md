# Research brief: eBay Classifieds Group and its brands (history, shared platforms, sale, aftermath)

Prepared 19 October 2026 for chapter writers of *LISTED: Architecting Large-Scale Classifieds and Marketplace Platforms*. This brief covers how eBay assembled a global classifieds portfolio (2004–2020), what is publicly known about how those sites were engineered and how much technology they shared, how the portfolio was sold to Adevinta (2020–2021), and what happened to each brand afterwards. It ends with lessons on multi-country shared platforms versus strong local brands.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched during this research session (October 2026) and supports the claim. The date is the publication date of the source, not the fetch date. Paraphrases stay close to the source. Quoted text is quoted.
- **[WIDELY REPORTED: url, YYYY]**: a reputable secondary source (trade press, Wikipedia, consumer-protection body, law-firm deal note), not primary documentation.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. All architectural inference about proprietary systems carries this tag. Chapter writers should re-verify it before printing it as fact, or present it explicitly as a judgement.

**How Medium posts were read.** Medium article pages return HTTP 403 to automated fetchers. Recent posts in the *Berlin Tech Blog (by Kleinanzeigen and mobile.de)* and *Marktplaats Technology* publications were read in full through the publications' RSS feeds (`https://medium.com/feed/berlin-tech-blog`, `https://medium.com/feed/marktplaats-technology`). Older Berlin Tech Blog posts no longer in the feed were read from Internet Archive snapshots of the article URL. Both routes are marked VERIFIED with the article's own URL and publication date. Where a snapshot was used, the source list says so.

**Research limitations.**

1. The session's shared web-search quota ran out partway through. After that point only direct fetches of known URLs were possible. Topics affected: the 2016 Motors.co.uk acquisition, the 2020 CarsGuide/Autotrader Australia acquisition, Gumtree UK's ownership after 2021, Kijiji Canada's ownership in 2025–2026, Marktplaats's platform history after 2017, and the "Comaas" and "BOLT" platform names.
2. **Two platform names in the commissioning brief could not be verified at all.** "Comaas" (Common Marketplace as a Service) and "BOLT" returned no matching public source in any search run. They may be internal code names that were never published. **Do not print either name** without a primary source (a conference talk, an engineering blog post, or a public repository). See Part 9.
3. eBay Classifieds Group (eCG) never ran a single group-level engineering blog that this research could find. Engineering evidence is scattered across brand blogs (Berlin, Amsterdam), a GitHub organization, conference talks and job postings. That scatter is itself evidence about how the group was organized (see Part 4).

**Volatility flags.** ⚠ marks claims likely to change within 12 months: ownership, brand names, product names, payment-partner relationships and fee limits.

---

## PART 1: Timeline of the portfolio (2004–2026)

### 1.1 Acquisitions and launches under eBay

| Date | Event | Evidence |
| --- | --- | --- |
| 26 Jan 2004 (closed 1 Apr 2004) | eBay buys **mobile.de** (Hamburg, founded 1996, vehicle classifieds) for about €121m in cash (about US$150m) | [WIDELY REPORTED: https://sec.gov/Archives/edgar/data/1065088/000095013404005653/f98218exv99w1.htm, 2004] (eBay earnings exhibit, surfaced in search but not fetched). Brand page: "Founded in Hamburg 1996 > Acquired by eBay in 2004 > Joined eBay Classifieds Group in 2008" [VERIFIED: https://web.archive.org/web/20140925074736/http://www.ebayclassifiedsgroup.com:80/brands-mobilede.html, 2014-09 snapshot] |
| 10 Nov 2004 | eBay acquires **Marktplaats.nl** (founded 1999, Emmeloord) from Het Goed Beheer BV for about €225m in cash (about US$290m); "over one million active listings at any given time"; to be run "as a separate business" | [VERIFIED: https://www.sec.gov/Archives/edgar/data/0001065088/000129993304001734/exhibit1.htm, published 2004-11-10] |
| Feb 2005 | **Kijiji** launches in Montreal and Quebec City, Italy and Taiwan; expands across Canada in November 2005 | [VERIFIED: https://web.archive.org/web/20140925120537/http://www.ebayclassifiedsgroup.com:80/brands-kijiji.html, 2014-09 snapshot]. Wikipedia says Kijiji "operated under Marktplaats BV" [WIDELY REPORTED: https://en.wikipedia.org/wiki/Kijiji, 2026] |
| May 2005 | eBay acquires **Gumtree** (founded London, March 2000, for Australian/NZ/South African expatriates) | [VERIFIED: https://web.archive.org/web/20140925120527/http://www.ebayclassifiedsgroup.com:80/brands-gumtree.html, 2014-09 snapshot]. Wikipedia reports eBay disclosed "$81.6 million for three classified sites" (Gumtree, LoQUo, OpusForum) [WIDELY REPORTED: https://en.wikipedia.org/wiki/Gumtree, 2026] |
| 2005 | eBay acquires **LoQUo** (Barcelona, founded 2002); "Intoko Spain acquired by eBay in 2005 and merged with LoQUo" | [VERIFIED: https://web.archive.org/web/20140925120542/http://www.ebayclassifiedsgroup.com:80/brands-loquo.html, 2014-09 snapshot] |
| June 2005 | eBay acquires OpusForum (German classifieds) | [WIDELY REPORTED: https://en.wikipedia.org/wiki/Kijiji, 2026] |
| 2007 | Gumtree sites exist in Australia, Singapore, Ireland, NZ, Poland and South Africa by this date | [VERIFIED: Gumtree brand page above] |
| 2007 | Kijiji in selected US cities; rebranded "eBay Classifieds" in the US in 2010 | [WIDELY REPORTED: https://en.wikipedia.org/wiki/Kijiji, 2026] |
| 2008 | Kijiji China renamed Baixing; Kijiji India became Quikr | [WIDELY REPORTED: same] |
| 6 Oct 2008 | eBay acquires **Den Blå Avis (dba.dk)** and **Bilbasen** (Denmark) for about US$390m. At that date eBay's "Global Classifieds" unit had "five major brands" (Kijiji, Gumtree, Marktplaats, LoQUo, mobile.de) in more than 20 countries and 1,000 cities | [VERIFIED: https://www.ebayinc.com/stories/news/ebay-acquires-leading-classifieds-companies-in-denmark/, published 2008-10-06] |
| June 2009 | ECG website: "seven unique brands" (BilBasen, dba.dk, Gumtree, Kijiji, LoQUo, Marktplaats.nl, mobile.de) in "more than 1000 cities and 20 countries" | [VERIFIED: https://web.archive.org/web/20090605000000/http://www.ebayclassifiedsgroup.com:80/, 2009-06 snapshot] |
| 9 Sep 2009 | **eBay Kleinanzeigen** launches in Germany. Kijiji listings are folded in; the Kijiji site keeps only contact ads and holiday rentals. Listings to be free; revenue from paid highlighting and advertising | [VERIFIED: https://www.itreseller.ch/Artikel/62877/Ebay_forciert_Kleinanzeigengeschaeft.html, published 2009-09-09] |
| 2010 | mobile.de launches automobile.it and automobile.fr | [VERIFIED: mobile.de brand page above] |
| July 2013 | eBay acquires **2dehands.be / 2ememain.be** (Belgium). Founded 1997 in Groningen, launched in Belgium 2000, market leader since 2010; 5.5m monthly unique visitors, 3.2m listings, more than 6,000 categories, bilingual Dutch/French search and listing | [VERIFIED: https://web.archive.org/web/20130825000000/http://ebayclassifiedsgroup.com/2dehands-be-2ememain-be, 2013-08 snapshot] |
| 2013 | **iBazar** launched as the group's Mexico classifieds platform | [VERIFIED: https://www.ebayinc.com/stories/news/ebay-classifieds-expands-mexico-acquires-vivanuncios/, published 2015-01-28] |
| Sep 2014 | ECG claims "eleven brands" across 1,000+ cities: 2dehands/2ememain, alaMaula, BilBasen, dba.dk, eBay Classifieds (incl. eBay Kleinanzeigen and eBay Annunci), Gumtree, iBazar, Kijiji, LoQUo, Marktplaats.nl, mobile.de | [VERIFIED: https://web.archive.org/web/20140926000000/http://www.ebayclassifiedsgroup.com:80/aboutus.html, 2014-09 snapshot] |
| 28 Jan 2015 | ECG acquires **Vivanuncios** (Mexico; founded 2006 as Vivastreet Mexico, rebranded 2013) from W3 Ltd. iBazar is retired and its users migrated to Vivanuncios "over the next several weeks". Group now "ten other local brands across 24 countries" | [VERIFIED: https://www.ebayinc.com/stories/news/ebay-classifieds-expands-mexico-acquires-vivanuncios/, published 2015-01-28] |
| Apr–May 2015 | Kijiji Hong Kong and Kijiji Taiwan close | [WIDELY REPORTED: https://en.wikipedia.org/wiki/Kijiji, 2026] |
| 2015 | mobile.de acquires the Motor-Talk forum | [WIDELY REPORTED: https://www.pplaw.com/en/transactions/pp-advises-management-sale-motor-talk-gmbh-mobilede-gmbh, date unknown] (surfaced in search, not fetched) |
| ~2016 | **Motors.co.uk** becomes part of Gumtree UK | [WIDELY REPORTED: https://www.ecommercebytes.com/?p=11565, date unknown] (surfaced in search, not fetched). ⚠ Acquisition date not verified; search quota exhausted |
| 6 Dec 2016 | ECG GM Alessandro Coppo announces eBay marketplace inventory to be shown on Gumtree AU (tested 2016), Gumtree UK and eBay Kleinanzeigen (by end 2016), and shared motors seller tools (from eBay's Cargigi acquisition) for Kijiji Canada and Gumtree South Africa | [VERIFIED: https://www.ebayinc.com/stories/news/integrating-ebay-inventory-on-classified-sites-for-consumers-globally/, published 2016-12-06] |
| Nov 2018 | Kijiji launches **Kijiji Autos**, a separate car-shopping platform | [WIDELY REPORTED: https://en.wikipedia.org/wiki/Kijiji, 2026] |
| 2020 | ECG acquires CarsGuide and Autotrader Australia from Cox Automotive | [WIDELY REPORTED: https://www.onlinemarketplaces.com/articles/adevinta-sells-gumtree-australia-in-60m-deal, 2022] (surfaced in search, not fetched) |
| Aug 2020 | ECG site lists brands: Autotrader, BilBasen, CarsGuide, DBA, 2dehands-2ememain, eBay Kleinanzeigen, Gumtree (AU, SG, ZA, UK), Kijiji (Canada), Marktplaats.nl, mobile.de and automobile.it, Motors.co.uk, Vivanuncios | [VERIFIED: https://web.archive.org/web/20200808000000/https://www.ebayclassifiedsgroup.com/, 2020-08 snapshot] |

**Pattern.** eBay built the portfolio in two ways. It **bought national leaders** (Marktplaats, mobile.de, Gumtree, dba/Bilbasen, 2dehands, Vivanuncios) and kept their local brands. It **launched greenfield sites under a group brand** (Kijiji, then eBay Kleinanzeigen and eBay Classifieds) in markets where it had no leader. The bought leaders mostly survived and grew. Several of the greenfield launches (Kijiji US, Hong Kong, Taiwan, China, India, Japan; iBazar) were closed, rebranded or sold. [ASSUMPTION/JUDGEMENT, drawn from the timeline above]

### 1.2 Scale snapshots (self-reported, as of date)

| Brand | Date | Self-reported figures | Evidence |
| --- | --- | --- | --- |
| Marktplaats | Sep 2014 | reaches 74% of Dutch online population; >350,000 new ads/day; ~6.5m monthly UVs; ~8m live listings; 2.2bn page views/month | [VERIFIED: https://web.archive.org/web/20140925120557/http://www.ebayclassifiedsgroup.com:80/brands-marktplaatsnl.html, 2014-09 snapshot] |
| Marktplaats | Nov 2017 | "over a million unique visitors, approximately 400 thousand new advertisements, several hundred thousand transactions" per typical day; 53% of the Netherlands visited monthly in 2016 (NOBO) | [VERIFIED: https://medium.com/marktplaats-technology/the-marktplaats-journey-becoming-the-best-version-of-ourselves-5ece9829f13f, published 2017-11-07] |
| Kijiji (all countries) | Sep 2014 | ~200m monthly visits; ~10m live listings; ~250,000 ads/day; ~2.5bn page views/month | [VERIFIED: Kijiji brand page, 2014-09 snapshot] |
| Gumtree (all countries) | Sep 2014 | >200m visits/month; >5m live listings; >200,000 new ads/day | [VERIFIED: Gumtree brand page, 2014-09 snapshot] |
| mobile.de | Sep 2014 | 65m visits/month; 1.4m live vehicle listings; >40,000 dealers; >90% of German dealers registered | [VERIFIED: mobile.de brand page, 2014-09 snapshot] |
| eBay Kleinanzeigen | 2009 → 2019 | built "to process 10K new ads per day", launched with ~700K live ads; by 2019: 34m+ live ads, up to 1m new + 1m edited ads/day, 45m saved searches, peak >50k requests/s | [VERIFIED: https://medium.com/berlin-tech-blog/microservices-and-kafka-part-2-b37dd08a7d8f, published 2019-10-28] |
| Kleinanzeigen | May 2023 | >36m users/month; >50m ads on average | [VERIFIED: https://adevinta.com/press-releases/adevintas-eBay-kleinanzeigen-is-now-kleinanzeigen/, published 2023-05-16] |
| Kleinanzeigen | Jun 2025 | 33.6m unique visitors/month, 714m visits | [VERIFIED: https://medium.com/berlin-tech-blog/handling-user-migration-with-debezium-apache-kafka-and-a-synchronization-algorithm-with-cycle-3c239b32326f, published 2025-06-04] |
| 2dehands/2ememain | Aug 2013 | 5.5m monthly UVs; 280m page views/month; 3.2m listings | [VERIFIED: 2dehands page, 2013-08 snapshot] |
| Vivanuncios | Jan 2015 | 15m monthly visits; 500,000–800,000 live ads | [VERIFIED: eBay Vivanuncios release, 2015-01-28; brand page 2015-02 snapshot] |

Self-reported marketing figures use different definitions (visits vs unique visitors vs users). Do not compare them across brands or years without saying so. [ASSUMPTION/JUDGEMENT]

---

## PART 2: The sale to Adevinta (2020–2021)

### 2.1 Announcement (21 July 2020)

- **Consideration:** about US$9.2bn in total: US$2.5bn in cash plus about 540 million Adevinta shares. That gave eBay about 44% of Adevinta's equity and a ~33.3% voting stake, making it the largest shareholder [VERIFIED: https://www.sec.gov/Archives/edgar/data/1065088/000155278120000426/e20435_ex99-1.htm, published 2020-07-21].
- **Expected close:** Q1 2021. Synergies estimated at **US$150–185m per year within three years** [VERIFIED: same].
- **Scope:** the release names Mobile.de, Gumtree, Marktplaats, dba, Bilbasen, Kijiji, 2dehands, 2ememain, Vivanuncios, Automobile.it, Motors.co.uk, Autotrader (Australia), Carsguide (Australia) and eBay Kleinanzeigen. The combined group would have "solid market positions in 20 countries", 1 billion people covered and 3 billion monthly visits [VERIFIED: same].
- **Denmark:** Schibsted (Adevinta's then-majority owner) would buy eCG's Danish business (dba.dk, Bilbasen.dk) after closing [VERIFIED: same].
- **Technology:** the release says only that eCG innovates "across its product portfolio and advertising technology platform". eBay and Adevinta "will continue to partner in key areas post-closing to ensure a seamless transition" [VERIFIED: same]. It gives no detail on how the shared technology would be separated from eBay.

### 2.2 UK competition review

- **Concern.** The CMA's SLC decision of 16 February 2021 found that Adevinta's **Shpock** and eCG's **Gumtree** compete closely in UK "generalist" classifieds. It also found that both compete with **eBay.co.uk**, and that Gumtree "has significant potential to compete with eBay Marketplace in the UK in the counterfactual where absent the Merger it would be independent of eBay" [VERIFIED: https://assets.publishing.service.gov.uk/media/606de28fe90e076f520fecdb/Adevinta-eBay_-_Decision_that_UILs_offer_may_be_acceptable.pdf, decision 2021-03-02, published 2021-04-08].
- **Remedy package (undertakings in lieu):** [VERIFIED: same]
  - All shares in Gumtree.com Ltd, including Motors.co.uk Ltd. The package covers the platforms, tangible and intangible assets, employees, leaseholds, contracts and goodwill, and is sold debt-free.
  - All shares in Finderly GmbH (Shpock), covering Austria, Germany and the UK.
  - **"Adevinta and eBay have offered to provide transitional services in relation to Shpock and Gumtree UK respectively."**
  - An **upfront-buyer condition** for Shpock. The Gumtree purchaser had to be approved by the CMA.
- **Acceptance:** the CMA accepted the undertakings on 2 June 2021. Shpock was sold to Russmedia Equity Partners the same day [VERIFIED: https://adevinta.com/press-releases/adevinta-completes-acquisition-of-ebay-classifieds-group/, published 2021-06-25].

**Architecture note.** A transitional-services commitment in a carve-out usually means the divested business still depends on the seller's shared infrastructure, operations or software at signing. The CMA text confirms that TSAs were offered. It does not say what they covered. [VERIFIED for the TSA offer; ASSUMPTION/JUDGEMENT for the interpretation]

### 2.3 Completion (25 June 2021)

[VERIFIED: https://adevinta.com/press-releases/adevinta-completes-acquisition-of-ebay-classifieds-group/, published 2021-06-25]

- eBay received US$2.5bn in cash, 342,474,251 Class A shares and 197,520,228 non-voting Class B shares (about 44% of share capital in total).
- Pro forma 2019 revenue was about €1.6bn. Run-rate cost synergies were now guided at **€130–165m** after three years.
- eCG's Denmark businesses went to a Schibsted subsidiary for about €278m.
- The combined group held #1 positions in 16 countries.

### 2.4 Post-completion divestments

| Date | Asset | Buyer | Notes | Evidence |
| --- | --- | --- | --- | --- |
| 2 Jun 2021 | Shpock (AT, DE, UK) | Russmedia Equity Partners | CMA remedy | [VERIFIED: Adevinta completion release] |
| 1 Dec 2021 | Gumtree UK + Motors.co.uk | O3 Industries (New York family fund) + Novum Capital (Frankfurt PE) | CMA remedy. In 2020 the pair made up about 7% of eCG revenue and about 4% of Adevinta's | [VERIFIED: https://adevinta.com/press-releases/adevinta-sells-gumtree-uk-and-motors-co-uk-to-o3-industries-and-novum-capital/, published 2021-12-01] |
| 25 Nov 2021 | Australia and South Africa put up for sale; Kijiji Canada put under strategic review | — | Announced with Q3 2021 results | [VERIFIED: https://www.onlinemarketplaces.com/articles/mixed-q3-for-adevinta-as-it-announces-renewed-investments-and-divestments/, published 2021-11] |
| Mar–Apr 2022 | Gumtree Poland closed (7 Apr 2022) | — | — | [WIDELY REPORTED: https://en.wikipedia.org/wiki/Gumtree, 2026] |
| Jul 2022 | Gumtree South Africa | Impresa Capital | undisclosed | [WIDELY REPORTED: same] |
| 25 Aug 2022 | Gumtree Australia, CarsGuide, Autotrader Australia | The Market Herald | US$60m cash. Rationale: focus on "five core European markets" and leverage. Adevinta to support the business "during the transition" | [VERIFIED: https://adevinta.com/press-releases/adevinta-announces-sale-of-gumtree-australia-carsguide-and-autotrader-australia, published 2022-08-25] |
| 26 Sep 2022 | Vivanuncios + Segundamano (Mexico) | Navent Group (operator of Inmuebles24) | brands to keep operating separately; impact "immaterial" | [WIDELY REPORTED: https://onlinemarketplaces.com/articles/adevinta-sells-vivanuncios-and-segundamano-to-navent-group, 2022]. The GlobeNewswire release returned HTTP 403 |

⚠ **Later ownership not verified.**
- One low-authority source claims Gumtree UK has been owned by 58.com and Ocean Link since late 2024. This could not be confirmed. Do not print it.
- The Market Herald reportedly renamed itself Gumtree Australia Markets Ltd (ASX: GUM) in 2025 [WIDELY REPORTED: https://garnetmarketplace.com/marketplaces/gumtree-au.html, date unknown]. This is unverified.

### 2.5 What Adevinta kept, and what happened to Adevinta

- **Kept:** mobile.de, eBay Kleinanzeigen (later Kleinanzeigen), Marktplaats, 2dehands/2ememain and automobile.it inside the five core European markets (France, Germany, Benelux, Spain, Italy) [VERIFIED: https://www.onlinemarketplaces.com/articles/adevinta-grows-revenue-progresses-verticalization-plan-in-2023-as-private-equity-takeover-looms/, published 2024-02-29]. Kijiji Canada was kept outside the core.
- **Kijiji impairment:** Adevinta recorded a **€147m impairment** on Kijiji. It cited "increased competition in the Canadian classifieds market" and negative effects from a new mobile app rolled out in 2023 [VERIFIED: same]. ⚠ No sale of Kijiji was found as of October 2026, but the search quota ran out before this could be checked thoroughly.
- **Verticalized organization:** from 1 January 2024, Adevinta organized around growth pillars including Mobility, Re-commerce, and Real Estate & Emerging Verticals. Plans "to converge assets onto the same tech platforms" were reported as "progressing well" [VERIFIED: same].
- **Take-private:** a consortium led by Permira and Blackstone offered about NOK 140bn in equity value (about €14bn including debt) in November 2023 [WIDELY REPORTED: https://freshfields.de/news/2023/11/freshfields-advises-permira-and-blackstone-on-take-private-of-online-classifieds-business-adevinta, 2023]. It completed in May 2024 with delisting from Oslo Børs. eBay reportedly kept about 20% and Schibsted about 13.6–16% via the holding structure [WIDELY REPORTED: https://www.vernimmen.com/Read/Vernimmen_Letter/Letter_158.html, 2024]. ⚠ Neither source was fetched. Cross-check with the Adevinta brief (`brief-adevinta.md`).

---

## PART 3: Brand aftermath

### 3.1 eBay Kleinanzeigen → Kleinanzeigen

- **16 May 2023:** eBay Kleinanzeigen became **Kleinanzeigen**. The rebrand had been announced in July 2022. It brought a new logo (a green "K") and a new domain, kleinanzeigen.de, with "the previous domain [to] remain accessible for several more years" [VERIFIED: https://adevinta.com/press-releases/adevintas-eBay-kleinanzeigen-is-now-kleinanzeigen/, published 2023-05-16].
- Users did not need to register again, and existing payment options carried over [WIDELY REPORTED: https://www.netzwelt.de/news/216898-kleinanzeigen-neu-ohne-ebay-namen.html, 2023] (surfaced in search, not fetched).
- **Engineering consequence (mobile.de):** a 2025 Berlin Tech Blog interview describes a later mobile.de Android rebrand. It needed a refactor first: dissolving legacy components, adopting Material Components, token-based colors and dark mode. "The rebranding itself was the final step and took only two weeks to implement once the base refactoring was done", and the work removed "technical debt from 8 years ago" [VERIFIED: https://medium.com/berlin-tech-blog/rebranding-on-android-apps-behind-the-scenes-57b8a58c294a, published 2025-07-19]. This post is about **mobile.de's** app, not Kleinanzeigen's. It is still a usable analogue for what a brand change costs a multi-brand app estate.

**Lesson.** Removing a former parent's brand needs work in three places: domains (redirects that last for years for SEO and bookmarks), identity (no forced re-registration) and design systems (themes driven by tokens). The domain was kept alive for "several more years". [ASSUMPTION/JUDGEMENT, built on the verified facts above]

### 3.2 Marktplaats and the Benelux multi-tenant platform

- A recent Adevinta job posting says Marktplaats (NL), 2dehands and 2ememain (BE) "are hosted on a multi-tenant platform, operated from our Amsterdam location" [VERIFIED: https://portfoliojobs.tcv.com/companies/adevinta-2/jobs/64812161-business-development-customer-success-operations-smb, posted "6+ months ago" as of 2026-10]. ⚠ This is recruiter copy, not a technical account. It is the only public statement found that the Belgian sites share Marktplaats's platform.
- An undated Xebia consultancy case study says "Marktplaats for example needed to clean up legacy code while Subito had newer tech" [WIDELY REPORTED: https://xebia.com/de/articles/adevinta-cloud-migration-revolutionizes-data-solution/, date unknown] (surfaced in search, not fetched).
- No Marktplaats engineering blog post after 2017 was found. The *Marktplaats Technology* Medium publication contains only two posts (Part 4.2), and the Wayback CDX index shows no others.

### 3.3 Kijiji

- From 2016 onwards Kijiji added Kijiji For Business, eBay listings in search (January 2017), mandatory registration (July 2017), in-app messaging (December 2017), Kijiji Autos (November 2018) and user reviews (November 2019) [WIDELY REPORTED: https://en.wikipedia.org/wiki/Kijiji, 2026].
- See Part 2.5 for the strategic review and the impairment.

### 3.4 Gumtree UK, Gumtree Australia, Vivanuncios

All three left Adevinta between 2021 and 2022 (Part 2.4). After those sales, no public engineering evidence was found about how their platforms were separated from eCG/Adevinta systems. This is a material evidence gap (Part 9).

---

## PART 4: How eCG was organized (what the public record shows)

### 4.1 A federation of national businesses with group functions

The public evidence points to a **group holding company with strong national (or regional) businesses**, not a single centralized product organization:

- **Kept separate on purpose.** eBay said at acquisition that Marktplaats would be operated "as a separate business" [VERIFIED: eBay 8-K exhibit, 2004-11-10].
- **Kijiji grew out of Marktplaats.** It launched as an eBay start-up "under Marktplaats BV" [WIDELY REPORTED: https://en.wikipedia.org/wiki/Kijiji, 2026]. This suggests the Amsterdam organization incubated the greenfield brand. Without primary evidence, that remains [ASSUMPTION/JUDGEMENT].
- **Group-level engineering jobs, 2009–2011** (Wayback snapshots of ebayclassifiedsgroup.com/careers):
  - *Senior Developer – Kijiji Platform* (Italy, 2010): PHP and Java, Symfony/Zend/Spring, MySQL, jQuery, fluent Italian [VERIFIED: https://web.archive.org/web/20100218000000/http://www.ebayclassifiedsgroup.com:80/careers/job-openings/senior-developer-kijiji-platform, 2010-02 snapshot].
  - *Senior Developer – Local Classifieds Product Development Teams* (2009): Java, Tomcat/JBoss, Hibernate, REST, Oracle/MySQL, JSP/Velocity/Freemarker [VERIFIED: https://web.archive.org/web/20090814000000/http://www.ebayclassifiedsgroup.com:80/careers/job-openings/senior-developer-local-classifieds-product-development-teams, 2009-08 snapshot].
  - *Staff Software Engineer, Kijiji US* (San Jose, 2011): "Collaborate with development teams of sister Classifieds platform to improve efficiency and reusability. Design / implement solution that can be reused by other Classifieds platforms" [VERIFIED: https://web.archive.org/web/20110119000000/http://www.ebayclassifiedsgroup.com:80/careers/job-openings/staff-software-engineer-kijiji-us, 2011-01 snapshot].
  - *Technology Director Local Classifieds* (Gumtree, London, 2011): drive "a variety of eCommerce platforms that form the portfolio of the group" and "Liaise with counterparts across the group to leverage existing technology components as applicable" [VERIFIED: https://web.archive.org/web/20111020000000/http://www.ebayclassifiedsgroup.com:80/careers/job-openings/technology-director-local-classifieds, 2011-10 snapshot].
- **Plural platforms.** The job filter lists "eBay Classifieds Global" as a separate hiring entity next to the brands [VERIFIED: same snapshots]. The wording "sister Classifieds platform" (2011) and "a variety of eCommerce platforms" (2011) indicates **several platforms, with reuse encouraged**, rather than one mandated stack, at least in 2009–2011. [VERIFIED for the wording; ASSUMPTION/JUDGEMENT for the interpretation]
- **A Berlin hub shared by two brands.** Kleinanzeigen and mobile.de jointly publish the Berlin Tech Blog ("written by developers, engineers, testers and many more from Kleinanzeigen and mobile.de in Berlin") [VERIFIED: https://medium.com/berlin-tech-blog/rebranding-on-android-apps-behind-the-scenes-57b8a58c294a, publication footer, 2025-07-19]. Its predecessor domain was `ebaytech.berlin` [VERIFIED: https://medium.com/berlin-tech-blog/microservices-and-kafka-part-2-b37dd08a7d8f, resource list, 2019-10-28].
- **A group SRE function.** A HashiConf 2018 speaker introduced himself as "site reliability engineer at the eBay Classifieds Group, Global Motors vertical" [VERIFIED: https://hashicorp.com/resources/ebay-hashistack-fully-containerized-platform-iac, published 2018-11-19].

**Amsterdam/Berlin hubs: what can and cannot be said.**
- *Can be said:* Marktplaats and the Benelux platform are run from Amsterdam (job ad, Part 3.2). Kleinanzeigen and mobile.de engineering sit together in Berlin (blog). A group "Global Motors vertical" existed by 2018 (HashiConf). Gumtree hired group-level technology leaders in London (2011).
- *Cannot be said without more sources:* that eCG formally ran "two hubs", which brands each hub served, or how group and brand engineering reported to each other.

### 4.2 Group-level open source (GitHub organization `eBayClassifiedsGroup`)

The organization's repositories, listed via the GitHub API in this session [VERIFIED: https://api.github.com/orgs/eBayClassifiedsGroup/repos, fetched 2026-10-19]:

| Repository | Created | Last push | What it shows |
| --- | --- | --- | --- |
| `nsnitro` | 2011-11 | 2020-05 | Python library for Citrix NetScaler (load balancers in own data centers) |
| `graphite-news`, `graphite-hoverbox` | 2014 | 2014 | Graphite metrics tooling |
| **`PanteraS`** | 2014-11 | 2021-10 | "PaaS – Platform as a Service in a box"; 199 stars |
| `marathon_deploy`, `panteras_api`, `registrator` fork | 2015 | 2016–2020 | Deploy tooling around Mesos/Marathon |
| `orlo`, `orloclient` | 2015 | 2017 | "REST API to record release information" |
| `KomPaaS` | 2015-11 | 2017 | "Compact PaaS – PoC small based golang app PaaS closed in one container" |
| `cassandra-reaper` fork, `cassandra-health-check` | 2016-09 | 2016 | Cassandra repair and health tooling |
| `apache-spark-deb`, `polscan`, `sensu-puppet`, `nagios_tools`, `ammonitrix-*` | 2016 | 2016–2017 | Debian packaging, policy checks, monitoring |
| `update-ts-references` | 2020-08 | 2026-06 | TypeScript monorepo helper; 70 stars; still maintained |
| **`reference-client-move`** | 2020-09 | 2020-12 | "A reference client implementation for eCG Motors Vertical" |
| **`reference-move-webhook-receiver`** | 2020-09 | 2022-07 | "Reference Implementation of a MoVe Webhook Receiver" |

**PanteraS architecture** [VERIFIED: https://github.com/eBayClassifiedsGroup/PanteraS (README fetched via raw.githubusercontent.com), release 0.4.4, repo created 2014-11]:
- Mesos + Marathon + ZooKeeper for orchestration.
- Consul for key/value, monitoring, service directory and registry, with Registrator automating registration.
- Fabio (and Traefik in slave mode) for load balancing with generated config.
- Recommended high-availability setup: three master containers. Multi-datacenter support via `consul join -wan`.
- Positioned as running "on your laptop, test and production systems without hassle".

**HashiStack at the Global Motors vertical** (HashiConf, 2018) [VERIFIED: https://hashicorp.com/resources/ebay-hashistack-fully-containerized-platform-iac, published 2018-11-19]:
- Terraform provisions networks and instances on an **OpenStack private cloud**. Every employee gets a dev tenant that mirrors production.
- Stateless front-facing apps run on PanteraS.
- **Nomad** runs stateful workloads (databases, Kafka) and batch jobs, "after having poor results with stateful applications on PanteraS".
- Vault and ZooKeeper are kept *outside* the schedulers.

**MoVe ("eCG Motors Vertical")** [VERIFIED: https://github.com/eBayClassifiedsGroup/reference-client-move and https://github.com/eBayClassifiedsGroup/reference-move-webhook-receiver, READMEs fetched, repos 2020-09]:
- A partner-facing **Listing API** for dealers and integrators. The spec was published at `api.ecgmove.com/docs/spec/listings`; that host no longer resolves (fetch failed, October 2026).
- Integration requirements: sandbox credentials, an assigned `partnerId`, and **IP whitelisting** for public API access.
- An outbound **webhook contract**: MoVe pushes events for **listings, dealers, promotions and "enriched listings"** to partner endpoints. Payload types are generated from the public API spec (`ecg.move.sellermodel.*`).
- Built as a Java Gradle project with Jersey/JAX-RS clients and a Spring Boot receiver.

**Reference-architecture inference (not documented):** MoVe looks like a **shared motors-vertical platform** that eCG built to serve several national car marketplaces. The likely tenants are Kijiji Autos (launched November 2018) and possibly the Australian Autotrader and CarsGuide assets bought in 2020. The public repositories do not name the consuming brands. Nothing found says whether mobile.de used MoVe. [ASSUMPTION/JUDGEMENT]

---

## PART 5: Engineering evidence by brand

### 5.1 Marktplaats (Amsterdam)

**Search: replacing eBay's Voyager with Elasticsearch (2015)** [VERIFIED: https://medium.com/marktplaats-technology/replacing-our-legacy-search-engine-with-elasticsearch-4ad03aeceb3d, republished 2017-09-19; originally by Frank Laan, 15 Dec 2015, on Marktplaats's old tech blog]

- **Legacy:** Voyager "was developed internally by eBay in the USA and was introduced at Marktplaats 6–7 years ago" (so around 2008–2009). It was fast and scaled "just add hardware". eBay itself "has moved on from Voyager several years ago", development had stopped, and it "has almost become a black box for us".
- **Group coordination:** "Marktplaats and other eBay Classifieds Group (eCG) companies facing similar problems have been working together to look at other technologies to replace Voyager and other legacy systems used for search." They chose Elasticsearch for its features and for community and commercial support. This matches the ECG data-and-architecture director's Elastic{ON} 2015 Amsterdam talk, where "Elasticsearch was the natural pick" [VERIFIED: https://www.elastic.co/elasticon/tour/2015/amsterdam/ebay-classified-group-and-a-scalable-flexible-search-platform-to-build-on, 2015, date not on page].
- **Platform architecture (as of 2015):** a service-oriented architecture with services for users, email, ad indexing and search, communicating via **Apache Thrift** and **asynchronous messaging over ActiveMQ or Kafka**.
- **Migration method:**
  1. Build new services behind the *same interfaces* as the legacy ones.
  2. Reuse "several hundred integration and acceptance tests".
  3. Do a first basic production index three weeks into development.
  4. Replay *recorded* user queries against indices built from a copy of the production database, in small random batches every five minutes. They chose this over live shadow traffic because an index that changes underneath makes differences impossible to reproduce.
  5. Ramp traffic: 1% on a Friday, 50% by the end of the next week, then 100% with Voyager kept warm.
- **Outcome:** zero downtime, 2–3 developers, 3 months. Many test failures came from "hidden functionality in other parts of the system that we couldn't detect in the code of the legacy services". "At no point did we consider going back."

**Organization: "Journey Teams" (2016–2017)** [VERIFIED: https://medium.com/marktplaats-technology/the-marktplaats-journey-becoming-the-best-version-of-ourselves-5ece9829f13f, published 2017-11-07]

- Product teams used to align to business units, each product owner with a "huge backlog". These were replaced by cross-functional **Journey Teams** organized around the customer journey. Teams included product, technology, marketing, customer relations, product analytics and data science.
- The company moved to OKRs: no more than three company Objectives and four Key Results per Objective, with KRs refreshed quarterly. Developers rotate into a team that "drives the technical strategy".
- The Head of Technology says that with this way of working "the platform has been changed from a set of monolithic services to microservices, allowing teams to deliver 10x faster each year" (self-reported).

**Payments: "Gelijk Oversteken" with Online Betaalplatform (2017)**

- June 2017: Marktplaats launched a payment service through partner **Online Betaalplatform (OBP)**. OBP verifies users' bank and personal data and links them to Marktplaats accounts. Higher amounts need extra identity checks (passport or iDIN). Access was rolled out to iDEAL users in groups [VERIFIED: https://www.emerce.nl/nieuws/marktplaats-faciliteert-onderling-betalen, published 2017-06-26].
- November 2017: "Gelijk Oversteken" opened to all users after a two-month test [VERIFIED: https://retailtrends.nl/news/pdf/50855, published 2017-11-28].
  - Escrow flow: payment request via iDEAL in chat → money held in an OBP intermediary account → seller ships with track & trace → OBP pays out on receipt.
  - Auto-release after seven days if the buyer does not confirm. Refund if the parcel never arrives and the seller cannot prove shipment.
  - Fee: buyer pays 2% plus €0.40.
- ⚠ The current Marktplaats flow ("Betaalverzoek" in messages, iDEAL | Wero, shipping labels, *Kopersbescherming*) is described only by low-authority sources [WIDELY REPORTED: https://www.ordertracker.com/nl/vervoerders/marktplaats, date unknown] (not fetched). Verify on help.marktplaats.nl before printing.

### 5.2 eBay Kleinanzeigen / Kleinanzeigen (Berlin)

**Platform evolution, 2009–2019** [VERIFIED: https://medium.com/berlin-tech-blog/microservices-and-kafka-part-2-b37dd08a7d8f, published 2019-10-28, Andre Charton, Head of Search]

- **2009 architecture:** "a plain old database backend", "a search backend based on Apache Solr™ (with a Master/Slave setup)", and web servers. Built for 10K new ads/day; launched with about 700K live ads. The core system ("the monolith") was Java.
- **2015:** introduced **Kafka "to break out from the monolith"**. The first use case was **saved searches with push notifications**, which "with MySQL" could not be done in real time at scale. Every important event, command or entity update became a message. By 2019: 45m saved searches and up to 1m new ads/day.
- **Kafka as storage:** the Elasticsearch search cluster (34m+ live ads, up to 1m new and 1m edited ads/day) can be **fully rebuilt from a compacted Kafka topic in under 30 minutes**. That covers recovery and schema changes.
- **Streaming:** user behavior feeds a home feed "consumed like a stream".

**Personalized home feed v1: Kafka Streams + Elasticsearch (2018)** [VERIFIED: https://medium.com/berlin-tech-blog/building-a-home-feed-with-kafka-streams-and-elasticsearch-894bd5e9b80d, published 2018-06-07; also a Berlin Buzzwords session]

- They chose on-demand feed computation over materialized feeds because ads are short-lived.
- **Kafka Streams** computes user features in near real time: top locations, favorite categories, recent searches.
- Elasticsearch builds candidates with "More Like This" on recently viewed items, re-runs past searches, finds trending items nearby and new items in favorite categories. Results are weighted and mixed.
- About **20 parallel Elasticsearch queries per feed request**, so the team flagged ES cluster size as the scaling concern.

**Home feed v2: Elasticsearch → Vespa (2026)** [VERIFIED: https://medium.com/berlin-tech-blog/from-elasticsearch-to-vespa-rebuilding-the-kleinanzeigen-homepage-feed-part-1-b6164e366ab8, published 2026-05-22; Part 2: https://medium.com/berlin-tech-blog/from-elasticsearch-to-vespa-rebuilding-the-kleinanzeigen-homepage-feed-part-2-3582ea51d4ee, published 2026-05-26; Fashion: https://medium.com/berlin-tech-blog/rebuilding-the-kleinanzeigen-homepage-feed-a-deep-dive-into-fashion-796ff379481a, published 2026-09-06]

- **Problem:** "we were doing too much work outside the search engine". Profile learning, scoring and retrieval were spread across services, with a round trip for each signal.
- **Deployment:**
  - Vespa Cloud on AWS in a European region, with a production-mirroring staging environment.
  - Private connectivity via an enclave (AWS PrivateLink, token auth, separate AWS accounts for staging and production).
  - Separate read and write containers over one content cluster.
- **Three schemas:**
  - `ads`: attributes as a weighted set of `field.value` tokens.
  - `user_category_profile`: one document per user per category, holding click-derived weights, recent keywords, clicked IDs, geo and explicit preferences.
  - `relations`: a global per-category config with field weights and token similarity groups.
- **Profile updates happen inside Vespa.** Document processors update profiles on each click: decay, merge, trim. **WAND** retrieval runs over attribute vectors. "No external profile store. No service hop at query time."
- **Explicit preferences** arrive via Kafka. A second WAND query is normalized to the same L2 scale and merged 50/50. Fashion moved to "seed weight injection" plus a labeled WAND under a RANK operator.
- **Semantic retrieval:** a German dense model with **binary-quantized embeddings in HNSW (Hamming distance)**. There is one vector per recent keyword (not one centroid), computed at write time. Production embeds on GPU; staging uses a quantized CPU model.
- **Lessons the team stated:**
  - Normalize WAND scores before merging.
  - Document processors removed "an entire class of consistency problems" with external profile stores.
  - Infrastructure took longer than expected.
  - Offline evaluation is the next step.
- **State in 2026:** live for Motors, Fashion, and Home & Garden. "The Elasticsearch path is gone." The first Fashion A/B test was only on par with legacy and needed a different retrieval design.

**Whole-platform migration to "a new system" (published 2025)** [VERIFIED: https://medium.com/berlin-tech-blog/handling-user-migration-with-debezium-apache-kafka-and-a-synchronization-algorithm-with-cycle-3c239b32326f, published 2025-06-04, MD Sayem Ahmed; read from an Internet Archive snapshot of 2025-11-27]

- "KA recently migrated the whole platform to a new system": a new system ran **in parallel** with the legacy one. All user data was migrated, then users were switched **incrementally**, with rollback to legacy possible. **The post does not name either platform, and does not say whether the new system is an Adevinta group platform.** Do not say it is. ⚠
- **Data dependencies drove the order:** core user data (IDs, authentication, profile) first, then ads, transactions and messages.
- **A reverse proxy** routes each user's traffic to legacy or new based on migration state.
- **No dual writes:** they used asynchronous streaming. A sync delay of up to one minute was "a business decision".
- **The transactional outbox was rejected.** Millions of user updates per day would overwhelm polling. There was an ordering risk with Spring transactional event listeners. And there was a risk of missing write paths in a legacy code base with debt.
- **Debezium CDC on MySQL, with workarounds:**
  - The production cluster used **statement-based binlogs without GTID** across two data centers.
  - The team added two new row-format replicas (one per DC) behind a proxy, and ran Debezium against them without making it cluster-aware.
  - Failover meant recreating the connector config topic and snapshotting tables.
  - Binlog retention was raised to at least seven days.
- **Migration state machine on an "Emigrant" entity:** IDENTIFIED → ELIGIBLE → MIGRATION_REQUESTED → MIGRATED → TRANSITIONED.
  - State changes are themselves captured by Debezium, so each step is a small atomic commit.
  - Retries are done by resetting state to ELIGIBLE. Account creation is idempotent.
  - A `user-migrated` topic notifies downstream migrations.
- **Bi-directional sync loops** (an update ping-ponging between the systems) were broken with a logical clock: the JPA `@Version` field, not timestamps.
- **The mapping and sync logic was built as a modular monolith**, to use MySQL ACID transactions.

**Cassandra counters (2022)** [VERIFIED: https://medium.com/berlin-tech-blog/optimising-counters-in-apache-cassandra-604a81dd6866, published 2022-05-13, Swen Fuhrmann]

- "Apache Cassandra is widely used at eBay Kleinanzeigen". A visit-counter service uses Cassandra counter columns (Cassandra 3.x).
- The cluster runs **"in a private cloud where the disk IO is limited"**.
- Fix: chunk size cut from 64 KB to 4 KB (with read-ahead reduced) and counter cache raised from 50 MB to 480 MB. Disk reads dropped by about 90%. The lesson: understand the bottleneck before adding nodes.
- Also listed as a Planet Cassandra use case [VERIFIED: https://planetcassandra.org/usecases/ebay-kleinanzeigen/393/, date unknown].

**Payments: "Sicher bezahlen" and "Direkt kaufen"**

- **29 Oct 2020:** "Sicher bezahlen" launched for all users. Mechanics at launch [VERIFIED: https://onlinemarketing.de/?p=214785, published 2020-10-29]:
  - The purchase price is held for **14 days** and released when the buyer confirms receipt.
  - The buyer pays a fee based on price. Sellers pay nothing.
  - Sellers must ship insured with proof of postage.
  - Disputes are mediated via "Online Payment Plattform".
  - Initially limited to toys, phones, and PCs/notebooks.
- **22 Sep 2022:** **"Direkt kaufen"** lets buyers purchase without messaging first. Sellers opt in per listing. The buyer picks shipping, then payment (instant bank transfer or card; invoice planned). The Sicher bezahlen cap rose from €1,000 to €2,000 [VERIFIED: https://www.iphone-ticker.de/direkt-kaufen-ebay-kleinanzeigen-fuehrt-neue-funktion-ein-198917/, published 2022-09-22]. ⚠ Limits change.
- **Payment provider:** sellers must register with **OPP (Online Payment Platform)**, described as Kleinanzeigen's DNB-licensed B2B payment provider for platforms [VERIFIED: https://t3n.de/news/?p=1565510, published 2023-07-20].
- **Consumer view:** the Verbraucherzentrale app test notes OPP payment confirmation can take four to seven business days, transactions freeze on dispute, and the app is tracking-heavy [VERIFIED: https://www.verbraucherzentrale.de/umwelt-haushalt/apptest-kleinanzeigen-kreislaufwirtschaft-mit-hintertuer-99396, reviewed 2024-09, page state 2025-09-18].
- **Not PayPal.** No evidence was found that "Sicher bezahlen" runs on PayPal. Consumer warnings concern scammers pushing PayPal "Friends and Family" *outside* the platform flow [WIDELY REPORTED: https://www.infranken.de/ratgeber/technik/internet-handy/miese-betrugsmasche-auf-kleinanzeigen-bei-dieser-forderung-solltest-du-stutzig-werden-art-5366143, date unknown] (not fetched).

**Shared payments partner across Amsterdam and Berlin.**
- Worldline's September 2022 press release, on buying a 40% stake in **Online Payment Platform B.V.** (Delft, founded 2011, payment institution licence 2014, 60+ employees, 100+ marketplaces), names **Marktplaats and eBay Kleinanzeigen** as clients, along with Gumtree. Worldline holds a call option on the remaining 60% in 2026 [VERIFIED: https://worldline.com/de-at/home/top-navigation/media-relations/press-release/pr-2022_09_09_01, published 2022-09-29]. ⚠ Check whether that 2026 option was exercised.
- "Online Betaalplatform" (Marktplaats, 2017) and "Online Payment Platform" (Kleinanzeigen, 2020) appear to be the same company under its Dutch and English names. This is [ASSUMPTION/JUDGEMENT], but it is strongly suggested by the Worldline client list.
- This makes C2C escrow a capability **shared through one external partner**, not built twice. [ASSUMPTION/JUDGEMENT]

### 5.3 mobile.de (Berlin)

- **Recommender systems (2018):** about 1.5m cars on the platform. The recommender "infers user preferences from billions of interactions and hundreds of features". Views, bookmarks and dealer contacts are treated as implicit feedback of increasing strength. The post explores deep learning for recommendations [VERIFIED: https://medium.com/berlin-tech-blog/deep-learning-for-recommender-systems-48c786a20e1a, published 2018-02-05, Marcel Kurovski].
- **Learning to rank (2024):**
  - Over 1m listings. The top 100 must be found "within a few milliseconds" while honoring "exposure guarantees made to our premium dealers".
  - The old LTR ran inside Elasticsearch through the native ranking plugin. That caused upgrade friction, manual model deployment and limited experimentation.
  - It was decoupled into a **Python ranking microservice**. A pairwise XGBoost model beat the pointwise model in an A/B test.
  - [VERIFIED: https://medium.com/berlin-tech-blog/better-search-relevance-using-learning-to-rank-at-mobile-de-bb3b0fa7d52d, published 2024-02-26, Manish Saraswat]
- **Graph ML for fraud (2026):** a user-to-user graph built from shared attributes (device IDs and others chosen with Customer Service). Each edge type has a weight and a **maximum group size** to suppress super-nodes. Text-similarity and temporal-burst edges are added. **Node2Vec** (128-dimensional, p = q = 1) feeds **XGBoost** with tabular features. New users are inserted into the same graph at inference [VERIFIED: https://medium.com/berlin-tech-blog/guilt-by-association-how-graph-ml-exposes-hidden-malicious-networks-e7722bcf2a14, published 2026-04-07, Akshay Paliwal, mobile.de].
- **MLOps on two clouds (2026):**
  - Production "sales probability" scoring service, run online and in batch.
  - Current stack: Airflow (Cloud Composer), self-hosted MLflow on a VM with Cloud SQL Postgres, artifacts in GCS, and **online serving as pods on a Kubernetes cluster on AWS**.
  - A Vertex AI proof of concept found consolidation is feasible and tracking is cheaper, but online serving was "significantly more expensive" and deployment slower [VERIFIED: https://medium.com/berlin-tech-blog/running-a-real-time-scoring-service-comparing-best-of-breed-mlops-to-vertex-ai-14e2641b9832, published 2026-06-09].
- **GenAI for dealers (2026):**
  - "AI Smart Reply" in the dealer Lead Management System: a classify → generate → reflect pipeline on Gemini Flash-Lite, a DeepEval offline harness, and Kotlin/Spring Boot integration [VERIFIED: https://medium.com/berlin-tech-blog/from-inbox-to-intelligence-building-and-evaluating-an-ai-reply-assistant-for-automotive-dealers-32f18acde878, published 2026-10-13].
  - AI dealer-rating summaries that began at "innovation days" [VERIFIED: https://medium.com/berlin-tech-blog/building-ai-powered-dealer-rating-summaries-at-mobile-de-d9dec9d4afe7, published 2026-05-26].
- **Cloud modernization:** an adesso reference describes migrating mobile.de infrastructure to "a scalable cloud environment (e.g. AWS/GCP)" and refactoring Java Spring Boot microservices to 12-factor [WIDELY REPORTED: https://www.adesso.de/en/adesso-branch-solutions/handel/referenzen/reference-mobile-de.jsp, date unknown] (surfaced in search, not fetched).

### 5.4 Berlin hub architecture culture (2018)

- *Data consistency in microservices:* sagas, compensating actions, idempotency and **reconciliation** "familiar to engineers who have worked in the financial domain" [VERIFIED: https://medium.com/berlin-tech-blog/data-consistency-in-microservices-architecture-bf99ba31636f, published 2018-09-05, Grygoriy Gonchar].
- *Software architects and autonomous teams:* "A Software Architect should never make a decision that the team can effectively make on their own". The architect's job is to replicate success stories across teams, find the weakest link, and keep decisions pragmatic [VERIFIED: https://medium.com/berlin-tech-blog/software-architects-and-autonomous-teams-328138202df1, published 2018-08-02].
- *Picking technology stacks:* warns against "needless complexity" in microservice stack choices and favors technologies that are part of "a shared architectural goal" [VERIFIED: https://medium.com/berlin-tech-blog/picking-technology-stacks-2c4e138c12c8, published 2018-12-12].

### 5.5 Gumtree, Kijiji, Vivanuncios (shared-platform era)

No first-hand engineering publication was found for Gumtree UK, Gumtree Australia, Kijiji Canada or Vivanuncios. What exists:

- 2016: eBay inventory exposed on Gumtree AU/UK and Kleinanzeigen, and eBay's motors seller tools shared with Kijiji and Gumtree ZA. This was "integrating and cooperating at its technology infrastructure level", "sharing data analytics, consumer insights, and predictive intelligence know-how" [VERIFIED: eBay Inc. 2016-12-06 post].
- 2015: Vivanuncios absorbed iBazar's users. This was a platform consolidation within one country, completed in weeks [VERIFIED: eBay Inc. 2015-01-28 release].
- 2011: Gumtree London hired a group technology director to "leverage existing technology components" across the portfolio [VERIFIED: job snapshot].

**Reference-architecture inference (not documented).** The commissioning brief asks whether Kijiji, Gumtree AU and Vivanuncios ran on a common eCG platform. The pattern is consistent with that:
- greenfield brands launched from one organization (Kijiji under Marktplaats BV);
- iBazar shut down quickly in favor of an acquired platform;
- a "Global Motors vertical" with a partner API;
- the CMA's need for eBay transitional services when Gumtree UK was carved out.

A shared generalist platform serving the non-European horizontals is therefore **plausible**. **No public source found in this session confirms it, names it, or says which brands ran on it.** Treat "BOLT" and "Comaas" as unverified. [ASSUMPTION/JUDGEMENT]

---

## PART 6: Recurring technology choices across eCG brands (as evidenced)

| Concern | Evidence | Era |
| --- | --- | --- |
| Search engine | eBay **Voyager** at Marktplaats (~2008–2015) → **Elasticsearch** (2015), coordinated across eCG companies. **Solr** master/slave at Kleinanzeigen (2009) → Elasticsearch (by 2018) → **Vespa** for the home feed (2026). mobile.de LTR in an ES plugin → Python ranking service (2024) | Parts 5.1–5.3 |
| Messaging / streaming | ActiveMQ + Kafka + Thrift at Marktplaats (2015). Kafka from 2015 at Kleinanzeigen (saved searches, storage, streams). Debezium CDC (2025) | 5.1, 5.2 |
| Datastores | MySQL (Kleinanzeigen, statement binlogs, two DCs). Cassandra (Kleinanzeigen counters; group Cassandra tooling 2016). Oracle/MySQL in 2009 group job specs | 4.1, 4.2, 5.2 |
| Compute | Own data centers with NetScaler (2011–). OpenStack private cloud + Mesos/Marathon (PanteraS) + Nomad (2014–2018). AWS Kubernetes and GCP managed services at mobile.de (2026). Vespa Cloud on AWS at Kleinanzeigen (2026) | 4.2, 5.2, 5.3 |
| Languages | Java dominant (monoliths, Spring/Hibernate). PHP at Kijiji Italy (2010). Kotlin/Spring Boot and Python ML services (2024–2026). TypeScript monorepos (2020–) | 4.1, 5.3 |
| C2C payments | One external escrow PSP (OPP/OBP) for Marktplaats (2017) and Kleinanzeigen (2020), later part-owned by Worldline | 5.1, 5.2 |

**Evidence age.** The 2015–2019 material describes systems that the same teams have since replaced (Voyager, Solr, Kafka-Streams-plus-ES home feeds, PanteraS) or migrated away from (the Kleinanzeigen legacy platform, 2025). Use it as history, not as the current state.

---

## PART 7: Multi-country shared platforms vs local brands, as this case shows it

### 7.1 What was shared, and what stayed local

| Layer | Shared across brands? | Evidence |
| --- | --- | --- |
| Brand, domain, local product decisions | **Local.** Marktplaats run "as a separate business"; national brands kept | 2004 8-K; brand pages |
| Organization and planning | Mostly local (Marktplaats Journey Teams, Berlin architecture culture). Group functions existed (eCG Global, Global Motors vertical, group CTO-type roles) | 5.1, 5.4, 4.1 |
| Search technology | **Coordinated choice, local implementation.** eCG companies jointly evaluated Voyager replacements; each migrated itself | 5.1 |
| Infrastructure and PaaS | **Group-built tools** (PanteraS, Terraform/OpenStack, monitoring) released under one GitHub organization | 4.2 |
| Vertical platform (motors) | **Shared platform with partner APIs** (MoVe) | 4.2 |
| eBay marketplace integration | **Group-level programs** (inventory sharing, motors tools) | 2016 eBay post |
| Payments | **Shared external partner** (OPP) | 5.1, 5.2, Worldline |
| Regional multi-tenant | **Benelux:** Marktplaats + 2dehands + 2ememain on one multi-tenant platform | 3.2 |

### 7.2 Divestment exposes platform coupling

- The CMA remedy depended on eBay providing **transitional services** to the Gumtree UK buyer [VERIFIED: CMA 2021].
- Adevinta promised to support Gumtree Australia "during the transition" [VERIFIED: Adevinta 2022].
- Adevinta exited the Australian, Mexican, South African and UK horizontals within about 18 months, while keeping the large European assets it could converge onto its own platforms [VERIFIED: divestment table; 2024 "converge assets onto the same tech platforms"].

**Judgement.** Brands that ran on group-shared components were the ones that needed TSAs when sold. Brands with large, self-sufficient national platforms (Marktplaats, Kleinanzeigen, mobile.de) became the assets Adevinta built its "core markets" around. Self-sufficiency kept strategic options open. [ASSUMPTION/JUDGEMENT]

### 7.3 Inherited parent technology is a liability once the parent moves on

Marktplaats ran a search engine built by eBay US that eBay itself had abandoned, with dwindling in-house knowledge ("almost become a black box"). The fix was coordinated across the group but carried out per brand [VERIFIED: 5.1]. A shared platform owned by a distant parent can turn into **orphaned legacy** faster than local code. [ASSUMPTION/JUDGEMENT]

---

## PART 8: Key lessons for the book

1. **Buy the national leader and keep its brand; greenfield group brands are fragile.** The acquired leaders (Marktplaats, mobile.de, Gumtree UK, 2dehands) remained valuable. Many group-brand launches (Kijiji US/HK/TW/CN/IN, iBazar, the Kijiji name in Germany) were closed, renamed or sold. *Evidence: [VERIFIED] ECG brand pages 2009–2020; eBay releases 2008/2015; [WIDELY REPORTED] Kijiji Wikipedia.*
2. **Coordinate technology choices across brands, but let each brand migrate itself.** eCG companies jointly picked Elasticsearch to replace Voyager. Marktplaats migrated with 2–3 engineers in 3 months behind unchanged interfaces. *Evidence: [VERIFIED] Marktplaats 2015/2017 post; Elastic{ON} 2015.*
3. **Shadow-test search migrations with recorded queries against frozen index copies, not live dual-reads.** Reproducibility beats realism when indices change every second. *Evidence: [VERIFIED] Marktplaats Voyager post.*
4. **The first scalable event-driven use case wins trust for the event backbone.** Kleinanzeigen introduced Kafka for saved-search alerts (45m saved searches) and then used it for storage (ES rebuild in under 30 minutes from compacted topics) and streaming feeds. *Evidence: [VERIFIED] Berlin Tech Blog 2019.*
5. **Make the search index disposable.** If an index can be rebuilt from a durable, compacted log in minutes, schema changes and recovery become routine. *Evidence: [VERIFIED] 2019 post.*
6. **Move personalization state into the serving engine when round trips dominate.** Kleinanzeigen's Vespa rebuild put profile updates, WAND retrieval and ANN ranking in one cluster, removing the external profile store. It still had to normalize scores carefully and redesign Fashion. *Evidence: [VERIFIED] Berlin Tech Blog 2026 (three posts).*
7. **Whole-platform replatforming is a per-user strangler migration, not a cut-over.** A reverse proxy routes by user, there is an explicit per-user state machine, async CDC instead of dual writes, rollback by user, and loop-breaking with logical clocks. *Evidence: [VERIFIED] Kleinanzeigen Debezium post, 2025.*
8. **Legacy database configuration constrains modern integration patterns.** Statement-based binlogs and no GTID forced CDC workarounds (row-format replicas behind a proxy). Platform hygiene is a prerequisite for data mobility. *Evidence: [VERIFIED] same.*
9. **Group-built PaaS can fit stateless services but struggle with stateful ones.** eCG's Mesos/Marathon PaaS (PanteraS) needed Nomad for databases and Kafka, with Vault and ZooKeeper outside the schedulers. *Evidence: [VERIFIED] PanteraS README; HashiConf 2018.*
10. **Verticals are where shared multi-country platforms pay off most clearly.** eCG's Global Motors vertical exposed a partner Listing API and webhooks (listings, dealers, promotions) for integrators across markets. *Evidence: [VERIFIED] MoVe reference repos 2020; inference about tenants is [ASSUMPTION/JUDGEMENT].*
11. **Buy C2C escrow; don't build it.** Marktplaats and Kleinanzeigen both used the same Dutch licensed payment institution for escrow-style "pay safely" flows: hold until receipt confirmed, auto-release windows, buyer-side fees. *Evidence: [VERIFIED] Emerce 2017; RetailTrends 2017; onlinemarketing.de 2020; t3n 2023; Worldline 2022.*
12. **Plan for divestment: shared components become TSAs and regulatory conditions.** The CMA required eBay transitional services for Gumtree UK. Every shared dependency is a separation cost at exit. *Evidence: [VERIFIED] CMA decision 2021; Adevinta releases 2021–2022.*
13. **A parent's abandoned platform is a hidden risk in a portfolio company.** Voyager became a black box at Marktplaats once eBay moved on. *Evidence: [VERIFIED] Marktplaats post.*
14. **Brand separation from a former parent takes years of domain redirects and design-system work.** Kleinanzeigen kept the old domain alive "for several more years". App rebrands took two weeks only after token-based theming was in place. *Evidence: [VERIFIED] Adevinta 2023 release; Berlin Tech Blog 2025 (mobile.de).*
15. **Ranking in marketplaces must encode commercial commitments.** mobile.de's LTR balances relevance against "exposure guarantees" in dealer packages, which pushed ranking into a separately deployable service. *Evidence: [VERIFIED] mobile.de LTR post 2024.*

---

## PART 9: Open questions / not publicly documented

1. **"Comaas" and "BOLT".** No public source found for either name as an eCG platform. Needed: a talk, repository or engineering post naming the platform, its tenants (Kijiji? Gumtree AU/UK? Vivanuncios? 2dehands?), its stack, and its fate after 2021.
2. **Which brands shared which platform before 2021.** Only the Benelux multi-tenant platform (Marktplaats/2dehands/2ememain) is stated publicly, and only in a job ad.
3. **What Kleinanzeigen's 2025 "new system" is.** It is unnamed. Is it an Adevinta group platform, a Kleinanzeigen rebuild, or a convergence with another Adevinta brand?
4. **How Gumtree UK, Gumtree AU and Vivanuncios were technically separated** after sale (TSA scope, duration, re-platforming).
5. **eCG's formal organization:** whether Amsterdam and Berlin were formal group "hubs", how group engineering (eCG Global, Global Motors) related to brand CTOs, and headcount.
6. **What MoVe served:** which national motors sites used it, whether mobile.de did, and what replaced `api.ecgmove.com`.
7. **Marktplaats engineering after 2017.** Search, recommendations, ML moderation/fraud, cloud migration. No first-hand publications found. The trust-and-safety and recommendations items in the commissioning brief are therefore uncovered for Marktplaats.
8. **Kleinanzeigen trust-and-safety ML.** None found in the Berlin feed. The graph-ML fraud post is mobile.de's.
9. **Current payment and shipping flows** on Marktplaats (Betaalverzoek, iDEAL | Wero, Kopersbescherming) and Kleinanzeigen (current fees and caps). Also whether Worldline exercised its 2026 option on OPP. ⚠
10. **Ownership as of October 2026:** Kijiji Canada (any sale after the 2021 review and the €147m impairment), Gumtree UK (the claimed 2024 sale), Gumtree Australia. ⚠
11. **Exact acquisition dates and prices** for Motors.co.uk (about 2016) and CarsGuide/Autotrader AU (2020). Search quota ran out.
12. **"Hackdays".** mobile.de "innovation days" are documented (2026). eCG-wide hackathons are suggested only by a 2015 `deployment-hackathon` repository [VERIFIED: GitHub API listing]. No narrative source.

---

## PART 10: Source list

All fetched 2026-10-19 unless noted. "Feed" = full text read via the publication's Medium RSS feed. "Snapshot" = read via an Internet Archive capture of the page.

**Primary: company, regulator, filings**

| Title | Publisher | Date | URL |
| --- | --- | --- | --- |
| eBay Acquires Dutch Company Marktplaats.nl (8-K Ex. 99) | eBay Inc. / SEC | 2004-11-10 | https://www.sec.gov/Archives/edgar/data/0001065088/000129993304001734/exhibit1.htm |
| eBay Acquires Leading Classifieds Companies in Denmark | eBay Inc. | 2008-10-06 | https://www.ebayinc.com/stories/news/ebay-acquires-leading-classifieds-companies-in-denmark/ |
| eBay Classifieds Expands in Mexico, Acquires Vivanuncios | eBay Inc. | 2015-01-28 | https://www.ebayinc.com/stories/news/ebay-classifieds-expands-mexico-acquires-vivanuncios/ |
| Integrating eBay Inventory on Classified Sites for Consumers Globally | eBay Inc. (A. Coppo) | 2016-12-06 | https://www.ebayinc.com/stories/news/integrating-ebay-inventory-on-classified-sites-for-consumers-globally/ |
| eBay–Adevinta transaction press release (8-K Ex. 99.1) | eBay Inc. / SEC | 2020-07-21 | https://www.sec.gov/Archives/edgar/data/1065088/000155278120000426/e20435_ex99-1.htm |
| Anticipated acquisition by Adevinta of eBay Classifieds Group: decision that undertakings might be accepted (ME/6897/20) | UK CMA | 2021-03-02 (pub. 2021-04-08) | https://assets.publishing.service.gov.uk/media/606de28fe90e076f520fecdb/Adevinta-eBay_-_Decision_that_UILs_offer_may_be_acceptable.pdf |
| Acquisition of eBay Classifieds Group complete | Adevinta | 2021-06-25 | https://adevinta.com/press-releases/adevinta-completes-acquisition-of-ebay-classifieds-group/ |
| Adevinta sells Gumtree UK and Motors.co.uk to O3 Industries and Novum Capital | Adevinta | 2021-12-01 | https://adevinta.com/press-releases/adevinta-sells-gumtree-uk-and-motors-co-uk-to-o3-industries-and-novum-capital/ |
| Adevinta announces sale of Gumtree Australia, CarsGuide and Autotrader Australia | Adevinta | 2022-08-25 | https://adevinta.com/press-releases/adevinta-announces-sale-of-gumtree-australia-carsguide-and-autotrader-australia |
| Adevinta's eBay Kleinanzeigen is now Kleinanzeigen | Adevinta | 2023-05-16 | https://adevinta.com/press-releases/adevintas-eBay-kleinanzeigen-is-now-kleinanzeigen/ |
| Worldline to acquire 40% stake in Online Payment Platform | Worldline | 2022-09-29 | https://worldline.com/de-at/home/top-navigation/media-relations/press-release/pr-2022_09_09_01 |
| eBay Classifieds Group website: home | eBay Inc. | 2009-06 snapshot | https://web.archive.org/web/20090605000000/http://www.ebayclassifiedsgroup.com:80/ |
| ECG: About Us | eBay Inc. | 2014-09 snapshot | https://web.archive.org/web/20140926000000/http://www.ebayclassifiedsgroup.com:80/aboutus.html |
| ECG brand pages: Kijiji, Gumtree, Marktplaats.nl, mobile.de, LoQUo | eBay Inc. | 2014-09 snapshots | https://web.archive.org/web/20140925120537/http://www.ebayclassifiedsgroup.com:80/brands-kijiji.html (and sibling `brands-*.html` pages) |
| ECG brand page: Vivanuncios | eBay Inc. | 2015-02 snapshot | https://web.archive.org/web/20150203064905/http://www.ebayclassifiedsgroup.com:80/brands-vivanuncios.html |
| ECG brand page: eBay Kleinanzeigen | eBay Inc. | 2017-01 snapshot | https://web.archive.org/web/20170128005119/http://www.ebayclassifiedsgroup.com:80/brands-ebaykleinanzeigen.html |
| ECG brand page: 2dehands.be – 2ememain.be | eBay Inc. | 2013-08 snapshot | https://web.archive.org/web/20130825000000/http://ebayclassifiedsgroup.com/2dehands-be-2ememain-be |
| ECG website: home (brand list) | eBay Inc. | 2020-08 snapshot | https://web.archive.org/web/20200808000000/https://www.ebayclassifiedsgroup.com/ |
| ECG job postings (Senior Developer Kijiji Platform; Local Classifieds Product Development; Staff SWE Kijiji US; Technology Director Local Classifieds) | eBay Inc. | 2009-08 to 2011-10 snapshots | https://web.archive.org/web/20100218000000/http://www.ebayclassifiedsgroup.com:80/careers/job-openings/senior-developer-kijiji-platform (and siblings cited in Part 4.1) |
| Adevinta job posting (Benelux multi-tenant platform) | Adevinta via TCV portfolio jobs | "6+ months ago" as of 2026-10 | https://portfoliojobs.tcv.com/companies/adevinta-2/jobs/64812161-business-development-customer-success-operations-smb |

**Primary: engineering**

| Title | Publisher | Date | URL |
| --- | --- | --- | --- |
| eBayClassifiedsGroup repositories (API listing) | GitHub | fetched 2026-10-19 | https://api.github.com/orgs/eBayClassifiedsGroup/repos |
| PanteraS README | eBay Classifieds Group (GitHub) | repo 2014-11; v0.4.4 | https://github.com/eBayClassifiedsGroup/PanteraS |
| Reference Client for MoVe Listing API | eBay Classifieds Group (GitHub) | 2020-09 | https://github.com/eBayClassifiedsGroup/reference-client-move |
| Reference MoVe Webhook Receiver | eBay Classifieds Group (GitHub) | 2020-09 (push 2022-07) | https://github.com/eBayClassifiedsGroup/reference-move-webhook-receiver |
| eBay's HashiStack: fully containerized platform with IaC (R. Rackow) | HashiCorp | 2018-11-19 | https://hashicorp.com/resources/ebay-hashistack-fully-containerized-platform-iac |
| eBay Classifieds Group and a scalable, flexible search platform (P. Maas) | Elastic | 2015 (date not on page) | https://www.elastic.co/elasticon/tour/2015/amsterdam/ebay-classified-group-and-a-scalable-flexible-search-platform-to-build-on |
| Replacing our legacy search engine with elasticsearch (F. Laan) | Marktplaats Technology (Medium), feed | 2017-09-19 (orig. 2015-12-15) | https://medium.com/marktplaats-technology/replacing-our-legacy-search-engine-with-elasticsearch-4ad03aeceb3d |
| The Marktplaats Journey: becoming the best version of ourselves | Marktplaats Technology (Medium), feed | 2017-11-07 | https://medium.com/marktplaats-technology/the-marktplaats-journey-becoming-the-best-version-of-ourselves-5ece9829f13f |
| Microservices and Kafka — Part 2 (A. Charton) | Berlin Tech Blog, snapshot | 2019-10-28 | https://medium.com/berlin-tech-blog/microservices-and-kafka-part-2-b37dd08a7d8f |
| Building a home feed with Kafka Streams and Elasticsearch | Berlin Tech Blog, snapshot | 2018-06-07 | https://medium.com/berlin-tech-blog/building-a-home-feed-with-kafka-streams-and-elasticsearch-894bd5e9b80d |
| Optimising Counters in Apache Cassandra (S. Fuhrmann) | Berlin Tech Blog, snapshot | 2022-05-13 | https://medium.com/berlin-tech-blog/optimising-counters-in-apache-cassandra-604a81dd6866 |
| Handling User Migration with Debezium, Apache Kafka, and a Synchronization Algorithm with Cycle… (M. S. Ahmed) | Berlin Tech Blog, snapshot 2025-11-27 | 2025-06-04 | https://medium.com/berlin-tech-blog/handling-user-migration-with-debezium-apache-kafka-and-a-synchronization-algorithm-with-cycle-3c239b32326f |
| From Elasticsearch to Vespa: Rebuilding the Kleinanzeigen Homepage Feed — Part 1 | Berlin Tech Blog, feed | 2026-05-22 | https://medium.com/berlin-tech-blog/from-elasticsearch-to-vespa-rebuilding-the-kleinanzeigen-homepage-feed-part-1-b6164e366ab8 |
| From Elasticsearch to Vespa — Part 2 | Berlin Tech Blog, feed | 2026-05-26 | https://medium.com/berlin-tech-blog/from-elasticsearch-to-vespa-rebuilding-the-kleinanzeigen-homepage-feed-part-2-3582ea51d4ee |
| Rebuilding the Kleinanzeigen Homepage Feed — a deep dive into Fashion | Berlin Tech Blog, feed | 2026-09-06 | https://medium.com/berlin-tech-blog/rebuilding-the-kleinanzeigen-homepage-feed-a-deep-dive-into-fashion-796ff379481a |
| Deep Learning for Recommender Systems (M. Kurovski) | Berlin Tech Blog, snapshot | 2018-02-05 | https://medium.com/berlin-tech-blog/deep-learning-for-recommender-systems-48c786a20e1a |
| Better search relevance using Learning to Rank at mobile.de (M. Saraswat) | Berlin Tech Blog, snapshot | 2024-02-26 | https://medium.com/berlin-tech-blog/better-search-relevance-using-learning-to-rank-at-mobile-de-bb3b0fa7d52d |
| Guilt by Association: How Graph ML Exposes Hidden Malicious Networks (A. Paliwal) | Berlin Tech Blog, feed | 2026-04-07 | https://medium.com/berlin-tech-blog/guilt-by-association-how-graph-ml-exposes-hidden-malicious-networks-e7722bcf2a14 |
| Running a Real-Time Scoring Service: Comparing Best-of-Breed MLOps to Vertex AI | Berlin Tech Blog, feed | 2026-06-09 | https://medium.com/berlin-tech-blog/running-a-real-time-scoring-service-comparing-best-of-breed-mlops-to-vertex-ai-14e2641b9832 |
| From Inbox to Intelligence: AI Reply Assistant for Automotive Dealers | Berlin Tech Blog, feed | 2026-10-13 | https://medium.com/berlin-tech-blog/from-inbox-to-intelligence-building-and-evaluating-an-ai-reply-assistant-for-automotive-dealers-32f18acde878 |
| Building AI-Powered Dealer Rating Summaries at Mobile.de | Berlin Tech Blog, feed | 2026-05-26 | https://medium.com/berlin-tech-blog/building-ai-powered-dealer-rating-summaries-at-mobile-de-d9dec9d4afe7 |
| Rebranding on Android Apps — Behind the Scenes (H. Olukoye) | Berlin Tech Blog, snapshot | 2025-07-19 | https://medium.com/berlin-tech-blog/rebranding-on-android-apps-behind-the-scenes-57b8a58c294a |
| Data consistency in microservices architecture (G. Gonchar) | Berlin Tech Blog, snapshot | 2018-09-05 | https://medium.com/berlin-tech-blog/data-consistency-in-microservices-architecture-bf99ba31636f |
| Software architects & autonomous teams (G. Gonchar) | Berlin Tech Blog, snapshot | 2018-08-02 | https://medium.com/berlin-tech-blog/software-architects-and-autonomous-teams-328138202df1 |
| Picking technology stacks (M. Czeladka) | Berlin Tech Blog, snapshot | 2018-12-12 | https://medium.com/berlin-tech-blog/picking-technology-stacks-2c4e138c12c8 |
| eBay Kleinanzeigen Cassandra use case | Planet Cassandra | date unknown | https://planetcassandra.org/usecases/ebay-kleinanzeigen/393/ |

**Secondary: press, consumer bodies, reference**

| Title | Publisher | Date | URL |
| --- | --- | --- | --- |
| Ebay forciert Kleinanzeigengeschäft | IT Reseller | 2009-09-09 | https://www.itreseller.ch/Artikel/62877/Ebay_forciert_Kleinanzeigengeschaeft.html |
| Marktführer: Zehn Jahre Ebay-Kleinanzeigen | FashionUnited | 2019-09-06 | https://fashionunited.de/nachrichten/einzelhandel/marktfuehrer-zehn-jahre-ebay-kleinanzeigen/2019090632984 |
| Marktplaats faciliteert onderling betalen | Emerce | 2017-06-26 | https://www.emerce.nl/nieuws/marktplaats-faciliteert-onderling-betalen |
| Gelijk Oversteken rollout (PDF) | RetailTrends | 2017-11-28 | https://retailtrends.nl/news/pdf/50855 |
| eBay Kleinanzeigen "Sicher bezahlen" launch | onlinemarketing.de | 2020-10-29 | https://onlinemarketing.de/?p=214785 |
| "Direkt kaufen": eBay Kleinanzeigen führt neue Funktion ein | iphone-ticker.de | 2022-09-22 | https://www.iphone-ticker.de/direkt-kaufen-ebay-kleinanzeigen-fuehrt-neue-funktion-ein-198917/ |
| Kleinanzeigen.de ermöglicht Sofortkauf – doch die Funktion hat einen Haken | t3n | 2023-07-20 | https://t3n.de/news/?p=1565510 |
| App-Test »Kleinanzeigen«: Kreislaufwirtschaft mit Hintertür? | Verbraucherzentrale | reviewed 2024-09; page 2025-09-18 | https://www.verbraucherzentrale.de/umwelt-haushalt/apptest-kleinanzeigen-kreislaufwirtschaft-mit-hintertuer-99396 |
| Mixed Q3 for Adevinta as it Announces Renewed Investments and Divestments | OnlineMarketplaces | 2021-11 | https://www.onlinemarketplaces.com/articles/mixed-q3-for-adevinta-as-it-announces-renewed-investments-and-divestments/ |
| Adevinta Grows Revenue and Progresses Verticalization Plan in 2023 | OnlineMarketplaces | 2024-02-29 | https://www.onlinemarketplaces.com/articles/adevinta-grows-revenue-progresses-verticalization-plan-in-2023-as-private-equity-takeover-looms/ |
| Used car search website Motors.co.uk is sold… | Car Dealer Magazine | 2021-12-06 | https://cardealermagazine.co.uk/used-car-search-website-motors-co-uk-is-sold-following-6-6bn-deal-to-take-over-ebay-classifieds-group/246118 |
| Kijiji | Wikipedia | fetched 2026-10-19 | https://en.wikipedia.org/wiki/Kijiji |
| Gumtree | Wikipedia | fetched 2026-10-19 | https://en.wikipedia.org/wiki/Gumtree |

**Surfaced in search but not fetched (do not upgrade to VERIFIED without fetching):** eBay mobile.de earnings exhibit (sec.gov f98218exv99w1.htm, 2004); Vivanuncios/Navent coverage (onlinemarketplaces.com, 2022); Freshfields take-private note (2023); Vernimmen Letter 158 (2024); netzwelt.de rebrand article (2023); adesso mobile.de reference; Xebia Adevinta case study; garnetmarketplace.com Gumtree AU profile; pplaw.com Motor-Talk transaction; ecommercebytes ?p=11565 (Motors.co.uk); infranken.de scam warning; ordertracker.com Marktplaats page.
