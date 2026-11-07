# Research brief: Commerce business models, economics and organization

Prepared 7 November 2026 for chapter writers of *ORDERED: Architecting Commerce Platforms*. The brief feeds chapters 01 (the order's journey), 02 (business models and economics), 03 (the capability map), 28 (data and analytics), 41 (build, buy or assemble), 42 (replatforming), 43 (scale stages) and 44 (organizing commerce engineering). It is platform-neutral: Shopify, Zalando, Amazon, Target and others appear because they publish dated numbers, not because the book recommends them.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (7 November 2026) and supports the claim. Quoted text is quoted; paraphrases stay close to the source. The date is the publication date. Undated product and pricing pages are marked "n.d., accessed 2026-11".
- **[WIDELY REPORTED: url, YYYY]**: a reputable secondary source (trade press, encyclopaedia, press-release relay) that was fetched or surfaced in a search result but is not a primary document.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. Every statement about how a company organizes its teams or systems internally falls here unless the company has described it.

**Evidence age matters.** Statistics series are revised (the US Census benchmarked its e-commerce series in April 2025 and dropped non-employer firms, so pre-2025 levels are not comparable with the current series), trade bodies change methodology (the European E-commerce Report changed its method in 2025 and issued a corrigendum), and vendor pricing pages change without notice. Sources older than about three years are flagged **(evidence age)**: the Forrester B2B forecast (2022), the Target and Finish Line replatforming stories (2009–2013), Fowler's original strangler note (2004, restated 2024).

**Volatility flags.** ⚠ marks claims likely to change within 12 months: platform plan prices and fees, PSP prices, partner-program terms, quarterly statistics.

**Research limitation.** The shared web-search quota ran out near the end of the session, and several sites block automated fetching (New York Times, Star Tribune, Chain Store Age, Smithsonian, McKinsey, eBay's history page, Shopify's `/plus` and `/partners/plus` pages, Adobe's 2018 Magento release). Consequences:

- **No primary source for "IT spend as a share of revenue" in retail.** Avasant publishes a retail chapter (55 respondents, August 2025) but it is paywalled; Gartner's figures are behind a login. Secondary blogs give 2–4%; treat that range as judgement.
- **No verified replatforming story for ASOS or Boots.** Searches found ASOS outages (2014) and a paused Boots marketplace (2023), but no sourced replatforming outcome for either. Do not use them as replatforming examples unless a writer finds a primary source.
- **No vendor SLA document was fetched** (commercetools' SLA page returned 404). The only verified availability statement is Shopify's Terms of Service, which disclaim uninterrupted service.
- **No public source on typical commerce team sizes or system counts by revenue band.** The book's scale-stage shapes (ledger) remain illustrative.
- **McKinsey's 2018 subscription taxonomy** (replenishment, curation, access) could not be fetched; it is cited from memory as judgement.
- **The NetMarket 1994 sale** rests on Wikipedia's citation of the New York Times; the NYT page itself could not be fetched.

---

## PART 1: Business models and a short history

### 1.1 Business models defined

Official statistics and annual reports define the models more precisely than marketing does. The definitions below are the ones chapter 02 can lift.

| Model | Working definition | Source basis |
| --- | --- | --- |
| **B2C e-commerce** | Sales to private consumers over websites or apps. Eurostat counts "web sales" to "private consumers" separately from sales to "other enterprises and public authorities" [VERIFIED: https://ec.europa.eu/eurostat/statistics-explained/index.php?title=E-commerce_statistics, data extracted 2026-02]. | Eurostat |
| **D2C (direct-to-consumer)** | A brand selling through its own channels. VF Corporation: "Our direct-to-consumer business includes VF-operated retail stores, brand e-commerce sites, concession retail locations and other digital platforms"; DTC was 44% of VF revenue in fiscal 2026 [VERIFIED: https://www.sec.gov/Archives/edgar/data/103379/000010337926000030/vfc-20260328.htm, published 2026-05-20]. Nike's "NIKE Direct" comprises "NIKE-owned retail stores and sales through our digital platforms"; NIKE Direct revenue was $17.7bn in fiscal 2026 against $18.8bn in fiscal 2025, "primarily driven by a decrease in traffic" [VERIFIED: https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm, published 2026-07-15]. | 10-K filings |
| **Wholesale (B2B for a brand)** | Selling to retailers and distributors who resell. Columbia Sportswear's wholesale channel comprises "department store chains, internet retailers, international distributors" and others, distinct from its DTC "branded, outlet, temporary clearance and employee retail stores, brand-specific e-commerce sites and shop-in-shop retail locations" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1050797/000105079726000028/colm-20251231.htm, published 2026-02-25]. | 10-K |
| **B2B e-commerce** | Business buyers ordering electronically. Eurostat splits "web sales" (websites or apps) from "EDI-type sales" (automated messages); in 2024 EDI-type sales were 11.07% of EU enterprise turnover and web sales 8.39%, so most B2B electronic ordering is still EDI, not web shops [VERIFIED: Eurostat, as above]. Forrester defines B2B e-commerce as "the sale of B2B products by manufacturers directly to businesses" and indirectly through wholesalers and distributors, and tracks EDI as a separate transaction type [VERIFIED: http://www.forrester.com/press-newsroom/forrester-us-b2b-e-commerce-will-reach-an-estimated-3-trillion-by-2027/, published 2022-06-08] **(evidence age)**. | Eurostat, Forrester |
| **B2B2C** | A brand sells through a partner's consumer channel while keeping the consumer relationship partly or wholly. Zalando's partner business "enables brands and retailers to sell merchandise via Zalando and ABOUT YOU while maintaining full control over their offer, content and pricing"; Zalando is not the seller of record for most of it [VERIFIED: https://corporate.zalando.com/sites/default/files/media-download/zalando-se_annual-report-2025_eng_261003_s.pdf, published 2026-03]. [ASSUMPTION/JUDGEMENT] "B2B2C" has no statistical definition; the book should define it operationally as "the partner owns the storefront, the brand owns the product and price". | Zalando |
| **Marketplace selling** | Selling on someone else's marketplace. Eurostat: web sales via online marketplaces were 1.30% of EU enterprise turnover in 2024, against 7.08% via own websites or apps [VERIFIED: Eurostat, as above]. | Eurostat |
| **Marketplace operating** | Running the marketplace. Amazon: "We offer programs that enable sellers to sell their products in our stores, and fulfill orders using our services. We are not the seller of record in these transactions"; third-party seller services net sales were $172.2bn in 2025 [VERIFIED: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm, published 2026-02-06]. Marketplace Pulse estimates third-party sellers at about 61–62% of units and 69% of an estimated $830bn 2025 GMV, "estimates based on Amazon disclosures" [VERIFIED: https://www.marketplacepulse.com/articles/amazon-gmv-surpassed-800-billion-in-2025, published 2026-02-06]. Zalando's partner business share of group GMV was 32.1% in 2025 (2024: 34.2%), diluted by consolidating ABOUT YOU [VERIFIED: Zalando AR 2025]. | 10-K, annual report, analyst |
| **Omnichannel** | Stores and digital channels sharing stock, orders and customers. Target: "Our stores fulfill the majority of digitally originated sales, including shipment from stores to guests, store Order Pickup or Drive Up, and Same-Day Delivery"; stores fulfilled 97.6% of merchandise sales in 2025 [VERIFIED: https://www.sec.gov/Archives/edgar/data/27419/000002741926000016/tgt-20260131.htm, published 2026-03-11]. | 10-K |
| **Subscription commerce** | Recurring orders under a standing agreement. [ASSUMPTION/JUDGEMENT] The usual taxonomy (replenishment, curation, access) comes from McKinsey's 2018 consumer research, which could not be fetched this session; cite it only as "a widely used taxonomy". Amazon reports "Subscription services" net sales of $49.6bn in 2025 (Prime and digital subscriptions), which shows subscription as a revenue line, not a commerce model [VERIFIED: Amazon 10-K, as above]. | — |

**Vendor and merchant views of the same platform.** Shopify's 10-K: "While most merchants subscribe to our Basic and Grow plans, the majority of our gross merchandise volume ('GMV') has been generated from merchants subscribing to our Shopify Plus plan and enterprise offerings" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm, published 2026-02-11]. [ASSUMPTION/JUDGEMENT] For the vendor the product is a tenancy and GMV is the metric; for the merchant the platform is one system among a dozen and the order is the metric. Chapter 02's "merchant's view vs vendor's view" can rest on this sentence.

**For newcomers.**
- *GMV (gross merchandise value)*: the value of orders passing through a platform, including what the platform does not keep as revenue; Shopify's GMV is "the total dollar value of orders facilitated through our platform ... net of refunds" [VERIFIED: Shopify 10-K, as above].
- *Seller of record*: the party legally selling to the customer, responsible for the invoice, VAT and consumer rights; a marketplace operator usually is not.
- *EDI-type sales*: orders received as structured messages between systems rather than through a web shop.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Each model changes who makes which promise. D2C owns the whole promise chain; wholesale moves order capture into the buyer's systems (EDI, punchout) and makes price lists and terms per account the hard part; marketplace selling makes someone else's catalog and order format the contract; marketplace operating adds tenancy, payouts and seller-of-record questions; omnichannel makes store stock a sellable, which Target's 97.6% figure shows is the whole business, not an add-on. A Starting merchant has one model; a Growing merchant adds a second and discovers the first integration; the Omnichannel stage is defined by running three or four models on one stock; the Group stage runs them per brand or country and must decide what is shared.

### 1.2 A dated history

| Date | Event | Tag |
| --- | --- | --- |
| 11 Aug 1994 | NetMarket sells a Sting CD to a buyer in Philadelphia by credit card over the Internet, using PGP encryption; the New York Times called it "apparently the first retail transaction on the Internet" | [WIDELY REPORTED: https://en.wikipedia.org/wiki/NetMarket, citing NYT 1994-08-12; the NYT page could not be fetched] |
| 1994 | Jeff Bezos "founded Amazon.com in 1994"; the bookstore opened to the public in 1995 (the 1995 launch date is commonly given but was not verified from a primary source this session) | [VERIFIED: Amazon 10-K FY2025, published 2026-02-06] |
| 1995 | eBay: "Founded in 1995 in San Jose, California" | [VERIFIED: https://www.sec.gov/Archives/edgar/data/1065088/000106508826000027/ebay-20251231.htm, published 2026-02-19] |
| 28 Sep 2004 / 2006 | Shopify's company was incorporated on 28 September 2004 (as 4261607 Canada Ltd), renamed Jaded Pixel Technologies on 19 January 2006 and Shopify Inc. on 30 November 2011; Tobias Lütke "co-founded Shopify in September 2004". The commonly cited "Shopify launched in 2006" refers to the product launch, not incorporation | [VERIFIED: https://www.sec.gov/Archives/edgar/data/1594805/000159480522000011/exhibit11annualinformation.htm, published 2022-02] |
| 31 Mar 2008 | Magento's first general-availability release (public beta 31 Aug 2007; developed by Varien from 2007); eBay took full ownership in 2011; Adobe announced its $1.68bn acquisition in May 2018; Magento 2.0 shipped 17 Nov 2015 | [WIDELY REPORTED: https://en.wikipedia.org/wiki/Magento, accessed 2026-11; the GA date is marked "citation needed" there] |
| 30 Jun 2020 | Magento 1 end of life, after two postponements; merchants warned about PCI DSS exposure | [WIDELY REPORTED: https://www.helpnetsecurity.com/2020/06/29/magento-1-eol/, 2020] |
| 24 Jun 2020 | MACH Alliance announced by founding members EPAM, commercetools, Contentstack and Valtech; MACH "stands for Microservices, API-first, Cloud-Native and Headless"; a non-profit "dedicated to advocating for open, best-of-breed technology ecosystems" | [VERIFIED: https://s202.q4cdn.com/436759741/files/doc_news/2020/06/24/12951.pdf, published 2020-06-24] |
| Q2 2020 | US e-commerce jumps to 16.1% of retail sales (seasonally adjusted) from 10.8% a year earlier; e-commerce +44.5% year on year while total retail fell 3.6% | [VERIFIED: https://www2.census.gov/retail/releases/historical/ecomm/20q2.pdf, published 2020-08-18] |
| H1 2021 | Dutch online spending €14.8bn, +19% on H1 2020; online share of product spending 26% (H1 2020: 21%) | [VERIFIED: https://www.betaalvereniging.nl/wp-content/uploads/2025/09/Infographic_Thuiswinkel_Markt_Monitor_2021_HY.pdf, published 2021] |
| 2022–2025 | Normalization: German online goods sales grew 1.1% in 2024 and 3.2% in 2025, and 2025 was "the first time since 2021" that every quarter grew; Dutch online spending fell 1% in 2025 after a record 2024 | [VERIFIED: bevh and Thuiswinkel, Part 2] |

**For newcomers.**
- *Replatforming*: moving a shop and the systems behind it from one platform to another (Part 5).
- *Composable / MACH*: assembling a platform from separately bought services behind APIs rather than one suite.
- *End of life (EOL)*: the date after which a vendor stops shipping security fixes; after it, the merchant carries the risk.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] The history is a sequence of forced moves. Magento 1's EOL forced a generation of mid-market merchants to replatform in 2019–2020, exactly when the pandemic doubled their traffic; MACH was announced the same month. The normalization since 2022 (growth of 1–4% a year in NL and DE) means the Growing and Omnichannel stages now compete on margin and operations rather than on traffic, which is why OMS, returns and data chapters matter more than they did in 2021.

---

## PART 2: Market size and share, with definitional caveats

### 2.1 Europe

- **E-shoppers.** 78% of EU internet users (16–74) bought or ordered goods or services online in 2025, up from 62% in 2015. The Netherlands had one of the highest shares of buyers in the last three months (86%, behind Ireland's 87%); Germany's share rose by only 3 points between 2015 and 2025. Eurostat's definition: "The purchase of goods or services over the internet" for private use, by any device; "Payment does not have to be made online" [VERIFIED: https://ec.europa.eu/eurostat/statistics-explained/index.php?title=E-commerce_statistics_for_individuals, data extracted 2026-02].
- **Enterprises.** 23.59% of EU enterprises had e-sales in 2024 (2014: 18.93%); e-sales were 19.49% of total turnover. Within web sales, 7.08% of turnover came via own websites or apps and 1.30% via marketplaces; B2B web sales (4.34% of turnover) slightly exceeded B2C web sales (4.04%) [VERIFIED: https://ec.europa.eu/eurostat/statistics-explained/index.php?title=E-commerce_statistics, data extracted 2026-02].
- **B2C turnover.** The 2026 European E-commerce Report (Ecommerce Europe, EuroCommerce, research by the Centre for Market Insights of Amsterdam University of Applied Sciences) puts total European B2C e-commerce turnover at €911bn in 2025, +7% from €842bn (real growth 4%), with Western Europe 57% of the total and €961bn forecast for 2026; 74% of Europeans aged 16–74 bought online in 2025 [VERIFIED: https://www.eurocommerce.eu/app/uploads/2026/09/final-draft-press-release-15092026.pdf, published 2026-09-22]. The 2024 figure was corrected in October 2025 from €819bn to €842bn (base year €784bn) [VERIFIED: https://www.eurocommerce.eu/app/uploads/2025/10/final-corrigendum-press-release.pdf, published 2025-10-10]. ⚠ The series covers 38 countries and includes services; it is not comparable with the national goods-only monitors below.

### 2.2 The Netherlands

- Thuiswinkel Markt Monitor (NielsenIQ for Thuiswinkel.org and Retail Insiders, with PostNL and Betaalvereniging Nederland): Dutch consumers spent **€35.7bn online in 2025, -1%** on the record 2024; **347 million purchases**, unchanged. Product spending grew 2% while spending on services fell 5% (purchases -11%), the first services decline since 2021. Cross-border: 13% of spending and purchases, €4.5bn (+2%), 44.8m purchases (+9%) [VERIFIED: https://nielseniq.com/global/nl/news-center/2026/meer-online-productaankopen-minder-uitgaven-aan-reizen-en-evenementen-in-2025/, published 2026-03-31; translated from Dutch].
- The monitor's "online spending" excludes shipping costs and includes services (travel, tickets, insurance), which is why the headline can fall while product sales rise [VERIFIED: 2021 infographic, as above; the exclusion is printed on the infographic].
- [ASSUMPTION/JUDGEMENT] The monitor does not publish an "online share of total retail"; the 2021 infographic's 26% share of product spending is the last such figure fetched this session. Writers should not quote a current Dutch online share without a new source.

### 2.3 Germany

- **bevh (goods, gross, incl. VAT).** Online goods sales reached **€83.1bn in 2025, +3.2%** (2024: €80.6bn, +1.1%), above the association's 2.5% forecast; growth in every quarter for the first time since 2021; digital services +7.3%. Quarterly 2026: Q1 +3.6%, Q2 +5.1% (H1 +4.3%), Q3 +2.9% to about €18.5bn, with the headline that Asian platforms lost market share after the customs exemption was abolished [VERIFIED: https://www.presseportal.de/nr/52922, releases dated 2026-01-22, 2026-04-13, 2026-07-06, 2026-10-09; translated from German]. Marketplaces at €46.2bn (+4.9%) and Chinese platforms at €3.7bn (+27.2%) in 2025 come from a secondary summary [WIDELY REPORTED: https://retail-news.de/e-commerce-deutschland-umsatz-2025/, 2026].
- **HDE Online-Monitor 2026 (net).** Online retail turnover **€92.3bn, +3.9%** (+€3.5bn), online share of German retail **13.5%** (prior year 13.4%); the page states figures are net and refers to "the past year" without naming it, which from the edition is 2025 [VERIFIED: https://einzelhandel.de/online-monitor, n.d., accessed 2026-11; translated from German].
- ⚠ [ASSUMPTION/JUDGEMENT] bevh (€83.1bn gross, goods ordered by consumers, survey-based) and HDE (€92.3bn net, retail definition) measure different things; quote one and name it. The two bodies disagree every year.

### 2.4 United States

- **Census Bureau, Q2 2026 (released 18 Aug 2026).** E-commerce **$340.2bn** seasonally adjusted, **17.1% of total retail sales**, +12.2% year on year against +6.7% for total retail. Not adjusted: $329.5bn, 16.4%. The not-adjusted share was **18.3% in Q4 2025** against 15.8% in Q3 2025, which is the seasonality signal in one number. Definition: "E-commerce sales are sales of goods and services where the buyer places an order, or the price and terms of the sale are negotiated over an Internet, mobile device (M-commerce), extranet, Electronic Data Interchange (EDI) network, electronic mail, or other comparable online system. Payment may or may not be made online." Since the April 2025 benchmark, non-employer businesses are excluded [VERIFIED: https://www.census.gov/retail/mrts/www/data/pdf/ec_current.pdf, published 2026-08-18]. ⚠ The Q3 2026 release is due 19 November 2026.
- **Pandemic peak for comparison.** Q2 2020: 16.1% (adjusted), later revised; the current series' Q2 2025 value is 16.3%, so the US share took five years to return to the 2020 spike [VERIFIED: 20q2.pdf as above; ec_current.pdf as above]. [ASSUMPTION/JUDGEMENT] Because of the 2025 benchmark the two levels are not strictly comparable; present the comparison as indicative.

### 2.5 B2B e-commerce

- **Forrester (2022).** US B2B e-commerce $1.7tn in 2021, projected above $2tn in 2023 and about $3tn by 2027 (CAGR 10.7%), reaching 24% of total US B2B sales by 2027 (from 16% in 2021); EDI tracked separately at 20% of B2B transactions in 2022 rising to 21% [VERIFIED: Forrester press release, published 2022-06-08] **(evidence age; the forecast was not updated in a fetchable release)**.
- **Digital Commerce 360 (2026).** Total US manufacturing and wholesale sales were $15.12tn in 2025, +0.4% (2024: +1.0%); the article says digital channels (e-commerce sites, marketplaces, e-procurement) grew at a "double-digit pace" but gives no dollar figure and does not say whether EDI is included [VERIFIED: https://www.digitalcommerce360.com/2026/01/26/us-b2b-sales-exceed-15-trillion-2025/, published 2026-01-26]. ⚠ Secondary sites quote DC360 B2B e-commerce figures of $2.9tn (2025) and eMarketer figures of $2.3tn (2024, excluding EDI); none was verified against the original report.
- **Europe.** Eurostat's EDI-type sales (11.07% of turnover) exceeding web sales (8.39%) is the one hard B2B number for the EU [VERIFIED: Eurostat enterprises, as above].

**For newcomers.**
- *Seasonally adjusted*: a statistical smoothing that removes the regular holiday peak; "not adjusted" shows the peak.
- *Gross vs net turnover*: gross includes VAT; German e-commerce bodies report gross (bevh) or net (HDE).
- *E-procurement*: a buyer's purchasing system placing orders into a supplier's system, often by catalog punchout or EDI.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] The statistics give three design facts. First, B2B electronic ordering is mostly EDI-type, so a wholesale line at the Omnichannel stage will meet EDI before it meets a B2B web shop. Second, online share is 13–17% of retail in the three home markets, so for any retailer with stores the store is still the larger channel and the architecture must treat store stock and store orders as first-class. Third, growth has normalized to single digits, so capacity planning is about the Q4 peak (18.3% vs 15.8% share in the US; Part 3.7), not about secular growth.

---

## PART 3: Unit economics of an order

### 3.1 Conversion

- Littledata's benchmark across **438 Shopify stores** (90 days to 31 Oct 2026): **median conversion 1.3%, mean 1.9%**; the top 20% exceed 2.7%, the top 10% 3.6%; the bottom 20% are below 0.5%. Conversion is "the share of sessions that included at least one purchase", computed from Google Analytics 4 [VERIFIED: https://www.littledata.io/average/ecommerce-conversion-rate, published 2026-11-04]. ⚠ Shopify-only sample; session definitions differ by analytics tool.
- IRP Commerce's public "market data" page shows only percentage sales changes by sector, not a conversion rate or AOV, so the often-quoted IRP conversion figures could not be verified this session [VERIFIED: https://www.irpcommerce.com/IRPStrategyCenter/Public/EcommerceMarketData.aspx, n.d., accessed 2026-11].
- **Cart abandonment.** Baymard's running average is **70.22%**, the unweighted mean of 50 studies published 2006–2025; among US shoppers who abandoned for a reason other than browsing, 40% cited extra costs (shipping, tax, fees), 20% slow delivery, 19% distrust with card data, 18% forced account creation, 17% a long or complicated checkout, 17% site errors or crashes, 13% an unsatisfactory returns policy, 10% a declined card and 9% too few payment methods [VERIFIED: https://baymard.com/lists/cart-abandonment-rate, updated 2026-10-28].

### 3.2 Average order value

| Example | Value | Source |
| --- | --- | --- |
| Shopify merchants, BFCM 2025 weekend | average cart $114.70 | [VERIFIED: https://www.shopify.com/news/bfcm-data-2025, published 2025-12-02] |
| Zalando, 2025 | average basket €62.8 (GMV after cancellations and returns, incl. VAT, per order); 4.8 orders per active customer; €302.6 GMV per active customer | [VERIFIED: Zalando AR 2025] |
| Target, 2025 | average transaction amount fell 0.4%; comparable sales -2.6% | [VERIFIED: Target 10-K FY2025] |

[ASSUMPTION/JUDGEMENT] AOV is a mix figure: Zalando's €62.8 basket is a fashion marketplace with high returns; a B2B order at the ledger's €1,277 is a different object (lines, terms, approval) and should not be averaged with it.

### 3.3 Gross margin ranges (apparel, outdoor, fashion online)

| Company (fiscal year) | Gross margin | Notes | Source |
| --- | --- | --- | --- |
| VF Corporation (FY to Mar 2026) | 54.8% (FY2025: 53.5%) | brands incl. The North Face, Timberland; DTC 44% of revenue | [VERIFIED: VF 10-K, published 2026-05-20] |
| Warby Parker (2025) | 54.0% | DTC eyewear; marketing $110.2m on $871.9m revenue (12.6%) | [VERIFIED: https://www.sec.gov/Archives/edgar/data/1504776/000150477626000006/wrby-20251231.htm, published 2026-02] |
| Columbia Sportswear (2025) | 50.5% (2024: 50.2%) | "healthier inventory composition resulting in less clearance", offset by US tariffs | [VERIFIED: Columbia 10-K, published 2026-02-25] |
| ASOS (52 weeks to 31 Aug 2025) | 47.1% (statutory, from 40.0%); guidance 48–50% for FY26 | higher full-price mix, lower markdowns; GMV £2,456m (-12%) | [VERIFIED: https://www.asosplc.com/media/ikxfhqeu/asos-fy25-results-rns-final-20251120.pdf, published 2025-11-20] |
| Nike (FY to May 2026) | 42.9% (FY2025: 42.7%) | lower warehousing and logistics costs "primarily due to channel mix" | [VERIFIED: Nike 10-K, published 2026-07-15] |
| Zalando (2025) | 39.9% group (2024: 40.7%); B2C 42.3%; B2B (ZEOS logistics) 15.0% | cost-of-sales ratio 60.1% | [VERIFIED: Zalando AR 2025] |
| Target (2025) | 27.9% (2024: 28.2%) | general merchandise; "higher markdown rates" | [VERIFIED: Target 10-K, published 2026-03-11] |

[ASSUMPTION/JUDGEMENT] The ledger's 54% for Kestrel & Pine sits at the top of the range, consistent with a brand that sells mostly its own product at full price; a wholesale-heavy mix or a third-party assortment pulls it toward 40%.

### 3.4 Returns

- **NRF and Happy Returns, 2025.** Returns are projected at **$849.9bn, 15.8% of annual sales** (2024: 16.9%, $890bn); **19.3% of online sales** are expected to be returned; retailers expect 17% of holiday sales to come back; 9% of returns are fraudulent; 40% of retailers cite rising processing costs as a reason to charge for returns. Method: a survey of 2,006 consumers and of 358 e-commerce professionals at merchants above $500m revenue [VERIFIED: https://nrf.com/media-center/press-releases/consumers-expected-to-return-nearly-850-billion-in-merchandise-in-2025, published 2025-10-15]. The 2024 edition reported $890bn and that 93% of retailers called return fraud a significant issue [VERIFIED: https://nrf.com/research/2024-consumer-returns-retail-industry, published 2024-12-05].
- **Fashion online is higher.** ASOS says returns "have been a major focus area, both because of the cost they create and the friction they cause"; better size guides, more reviews and a "fair use policy in core markets" reduced its underlying returns rate by about 150 basis points in FY25 [VERIFIED: ASOS FY25 RNS, as above]. Zalando offers a return policy "of up to 30 days" and recognizes revenue net of "sales-channel and country-specific return rates" [VERIFIED: Zalando AR 2025]. [ASSUMPTION/JUDGEMENT] Neither publishes its return rate; the frequently quoted "around 50% for online fashion" is industry lore, not a verified figure.

### 3.5 Shipping cost and free-shipping thresholds

- Extra costs are the top stated reason for abandonment (40%) and slow delivery the second (20%) [VERIFIED: Baymard, as above].
- Zalando lists a "minimum order fee" among the services bundled into a retail order, i.e. small orders pay a fee instead of a free-shipping threshold [VERIFIED: Zalando AR 2025, revenue-recognition note].
- Target's paid Target Circle 360 membership gives "unlimited same-day delivery on eligible orders over $35" [VERIFIED: Target 10-K FY2025].
- [ASSUMPTION/JUDGEMENT] No public survey of European free-shipping thresholds was verified; the ledger's €75 threshold is illustrative.

### 3.6 Payment fees

- **Interchange caps (EU).** Regulation (EU) 2015/751: "Payment service providers shall not offer or request a per transaction interchange fee of more than 0,2 % of the value of the transaction for any debit card transaction" (Article 3) and "more than 0,3 % ... for any credit card transaction" (Article 4); Member States may set lower domestic caps; Articles 3 and 4 applied from 9 December 2015 [VERIFIED: http://publications.europa.eu/resource/celex/32015R0751, published 2015-05-19]. The caps cover consumer cards; commercial cards and non-EEA cards are outside them, which is why PSP prices for those are higher.
- **PSP list prices (Netherlands), ⚠ all undated pages, accessed 2026-11.**

| PSP | Standard EEA consumer card | Other | Source |
| --- | --- | --- | --- |
| Stripe | 1.5% + €0.25; premium EEA cards 2.8% + €0.25 | UK cards 2.5% + €0.25; international 3.15% + €0.25; +2% currency conversion; iDEAL €0.29 | [VERIFIED: https://stripe.com/nl/pricing, n.d.] |
| Mollie | 1.80% + €0.25; EEA commercial 2.90% + €0.25 | non-EEA 3.25% + €0.25; iDEAL/Wero €0.32; Bancontact 1.40% + €0.25; Klarna NL/BE 2.99% + €0.45 | [VERIFIED: https://www.mollie.com/pricing, n.d. (page metadata 2026-11-05)] |
| Adyen | $0.13 + Interchange++ + 0.60% for Visa/Mastercard | iDEAL $0.13 + €0.22; SEPA direct debit $0.13 + €0.27; "a minimum invoice depending on industry or business model"; fees "indicative" | [VERIFIED: https://www.adyen.com/pricing, n.d.] |
| Shopify Payments (EUR plans) | online 1.9% + €0.25 (Basic) to 1.4% + €0.25 (Plus); in-person debit 0.75% to 0.35% + €0.10 | third-party gateway fee 2% (Basic), 1% (Grow), 0.6% (Advanced), 0.2% (Plus) | [VERIFIED: https://www.shopify.com/pricing, n.d.] |

- [ASSUMPTION/JUDGEMENT] Blended pricing (Stripe, Mollie, Shopify Payments) hides interchange; Interchange++ (Adyen) exposes it. For a merchant at €27m online revenue with a €92 basket, the gap between 1.9% and 1.4% plus a fixed fee is a six-figure annual sum, which is the real reason platform tier and PSP choice are architecture-adjacent decisions.

### 3.7 Customer acquisition and retention

- Warby Parker's marketing expense was $110.2m in 2025, $95.5m in 2024 and $78.4m in 2023, against revenue of $871.9m, $771.3m and $669.8m (12.6%, 12.4%, 11.7%); its risk factors state "as we grow our customer acquisition costs may continue to rise" and that it depends "in large part, on search engines" and social platforms [VERIFIED: Warby Parker 10-K, as above].
- Zalando's retention proxies: 4.8 orders per active customer per year, unchanged from 2024; active customers 62.0m after consolidating ABOUT YOU [VERIFIED: Zalando AR 2025].
- [ASSUMPTION/JUDGEMENT] No cross-industry CAC benchmark was verified; vendor blogs claiming multi-hundred-percent CAC inflation since 2016 should not be quoted.

### 3.8 Seasonality and peaks

- **Adobe Analytics, Cyber Week 2025 (US).** Cyber Week (Thanksgiving to Cyber Monday) **$44.2bn, +7.7%**; Cyber Monday **$14.25bn, +7.1%**, with spending of **$16m per minute** between 8 and 10 pm; Black Friday $11.8bn (+9.1%); Thanksgiving $6.4bn (+5.3%); mobile 57.5% of Cyber Monday sales; BNPL $1.03bn on Cyber Monday; AI-referred traffic to retail sites +670% on Cyber Monday; peak discounts of 31% on electronics and 25% on apparel; season forecast (1 Nov–31 Dec) $253.4bn (+5.3%). Method: Adobe Analytics data on over one trillion visits to US retail sites, 100m SKUs and 18 categories [VERIFIED: https://news.adobe.com/news/2025/12/adobe-cyber-monday-hits-record, published 2025-12-02]. The final season figure of $257.8bn (+6.8%) was reported in trade press [WIDELY REPORTED: https://chainstoreage.com/adobe-holiday-e-commerce-beats-expectations-record-2578b, 2026].
- **Shopify, BFCM 2025 weekend.** $14.6bn GMV (+27%), peak **$5.1m per minute**, 81m+ consumers, 16% of orders cross-border, over 94,900 merchants with their best day ever [VERIFIED: Shopify BFCM data 2025, as above]. The platform-level request peaks for that weekend are covered in the sibling `shopify` brief; they were not re-verified here.
- **Quarterly shape.** US not-adjusted e-commerce share 18.3% in Q4 2025 vs 15.8% in Q3 2025 [VERIFIED: Census ec_current.pdf].
- Hobbycraft postponed a website relaunch from before Christmas 2012 to 2013 because, in its CEO's words, "We felt it was too risky to launch the website in peak trading at Christmas" [VERIFIED: https://retail-week.com/general-merchandise/crafts-retailer-hobbycraft-to-complete-delayed-digital-roll-out-by-summer/5046363.article, published 2013-02-19] **(evidence age)**.

**For newcomers.**
- *Conversion rate*: purchases divided by visits (sessions); 1–3% is normal for a web shop.
- *Interchange*: the fee the cardholder's bank takes from each card payment; in the EU it is capped at 0.2% (debit) and 0.3% (credit) for consumer cards.
- *BFCM / Cyber Week*: the Black Friday to Cyber Monday weekend, the annual peak for most Western consumer merchants.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Each metric pulls on a different part of the system: conversion on storefront speed, checkout steps and visible total cost (Baymard's top reasons are architecture failures: unknown shipping cost, forced accounts, errors); AOV on promotions and bundles; gross margin on markdown control, which needs one price owner; returns on a returns flow that restocks and refunds across systems (19.3% of online sales come back); payment fees on PSP choice and on whether the platform forces its own gateway; seasonality on capacity and on code freezes. The peak is the design load: a merchant whose normal day is 800 orders must plan for the day that is five to ten times that, which is where hosted platforms (Shopify absorbing $5.1m per minute) earn their fee and self-hosted ones need a test. By stage: Starting merchants inherit all of this from the hosted platform; Growing merchants first feel payment-fee and shipping-threshold economics; Omnichannel merchants feel returns and markdowns across channels; Group merchants need the metrics defined once (chapter 28).

---

## PART 4: Scale stages

### 4.1 How vendors tier their customers

- **Shopify plans (EUR, ⚠ undated page).** Basic €21/month (yearly) or €28 (monthly); Grow €59/€78; Advanced €289/€384; Plus from €2,100/month; an "Agentic" plan at €0/month with 1.9% + €0.25 card rates; POS Pro +€79/month per location; Plus is sold on "a 1- or 3-year Plus subscription" [VERIFIED: https://www.shopify.com/pricing, n.d., accessed 2026-11]. Shopify Flow's HTTP-request action is Grow and above; Functions in custom apps and advanced checkout customization need Plus (see the sibling `shopify` brief).
- **Shopify Enterprise.** Positioned "For the world's largest brands"; the page cites an EY survey of organizations "with GMVs of $50M to $500M+" and vendor claims of "33% lower average total cost of ownership" and "20% faster migrations" [VERIFIED: https://www.shopify.com/enterprise, n.d., accessed 2026-11]. [ASSUMPTION/JUDGEMENT] Shopify publishes no GMV threshold for Plus; the EY sample is the nearest public hint of the band it calls enterprise.
- **Shopware.** Community Edition free, but once shops linked to an account exceed €1m GMV over 365 days a paid plan is required to keep account and store access; Rise from €600/month; Evolve from €2,400/month; Beyond custom; "The pricing for our plans is based on your gross merchandise value (GMV) and further individual factors" [VERIFIED: https://www.shopware.com/en/pricing/, n.d., accessed 2026-11].
- **Shopify's own distribution.** Most merchants are on Basic and Grow; most GMV comes from Plus and enterprise; merchants in more than 175 countries, 44% in the US [VERIFIED: Shopify 10-K FY2025]. [ASSUMPTION/JUDGEMENT] The ledger's Omnichannel stage (€20–200m) is where a merchant crosses from a plan to a contract: Plus, Evolve/Beyond, or an enterprise suite.

### 4.2 Technology spend and team size

- Avasant's "IT Spending and Staffing Benchmarks 2025/2026, Chapter 8: Retail" (August 2025) reports on 55 respondents with revenue from $200m to over $200bn, but the percentages are paywalled [VERIFIED: https://avasant.com/report/it-spending-and-staffing-benchmarks-2025-2026-chapter-8-retail/, published 2025-08]. ⚠ Secondary blogs put retail IT spend at 2–4% of revenue [ASSUMPTION/JUDGEMENT; no primary figure].
- [ASSUMPTION/JUDGEMENT] The ledger's 5.4% (about €2.6m on €48m, including agency and salaries) is high against the 2–4% range typical of store-heavy retailers and plausible for a brand whose online share is 56% and that pays an agency retainer. Writers should present it as a judgement, not a benchmark.
- [ASSUMPTION/JUDGEMENT] No public survey of commerce engineering team sizes by revenue was found. The ledger's 14 technologists for €48m is a composite.

### 4.3 When an OMS, PIM or WMS is introduced

- **PIM (vendor view).** Akeneo's partner-authored post gives three signs: product content scattered across teams with no "single source of truth"; manual, ad hoc processes that make launching a channel (its example: an Amazon data feed) slow and dependent on a few people; and bad online experiences from inconsistent data (filters, comparisons, search, translations). It names no SKU threshold [VERIFIED: https://www.akeneo.com/blog/top-3-signs-you-need-a-pim/, n.d. (image path suggests 2022), accessed 2026-11; vendor content].
- **OMS (practitioner heuristics).** Vendor guides converge on channel count and stock-location count as the triggers ("3+ sales channels", "multiple stock locations such as a warehouse, store, 3PL, dropshipper"), not order volume [WIDELY REPORTED: https://opollo.onpoint.vn/blog/8-signs-your-brand-needs-an-order-management-system-oms, n.d.]. Target's disclosure that stores fulfil the majority of digital orders through ship-from-store, pickup and same-day delivery is the clearest public statement of what an OMS does at scale, though Target does not name its system [VERIFIED: Target 10-K FY2025].
- **WMS.** No vendor or practitioner source on WMS timing was fetched (Shopify's blog URL returned 404). [ASSUMPTION/JUDGEMENT] The practical trigger is operating an own warehouse with more than a handful of pickers, or a 3PL that cannot expose stock by location; the ledger's WMS at the Omnichannel stage follows this.
- [ASSUMPTION/JUDGEMENT] Combining the sources: PIM when the catalog is published to a third channel in a third format; OMS when stock sits in a second location that must be sold from; WMS when physical operations outgrow the ERP's stock module. The three arrive together at the Omnichannel stage, which is why the ledger's Waypoint program plans OMS and PIM introductions as migrations.

**For newcomers.**
- *Plan vs contract*: hosted platforms sell self-service monthly plans up to a point, then negotiated multi-year contracts (Shopify Plus 1- or 3-year terms).
- *OMS (order management system)*: the system that decides from which location an order is fulfilled and tracks it across channels.
- *PIM (product information management)*: the system that holds the enriched product content every channel reads.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Scale stages are defined by shape, not revenue, and the vendors' own tiers confirm it: Shopify and Shopware price by GMV and features, not by employees. The transitions are visible as fee cliffs (Shopware's €1m GMV, Shopify's third-party gateway fee from 2% to 0.2%) and as feature gates (checkout extensibility, Functions, B2B features on Evolve). A merchant should read a vendor's tiers as a map of which decisions the vendor expects at each size.

---

## PART 5: Build, buy, assemble and replatforming

### 5.1 TCO components

- Shopify's replatforming guide lists migration costs ("data migration, platform licensing, agency or partner fees, staff retraining, and downtime during transition"), ongoing costs ("hosting, security patches, maintenance, custom development, performance testing") and hidden costs ("peak-traffic surcharges, custom checkout development, additional feature licenses, content management overhead, and app or integration fees not in the original quote") [VERIFIED: https://www.shopify.com/enterprise/blog/ecommerce-replatforming, published 2026-03-18; vendor content].
- Fee components verified elsewhere in this brief: subscription (Part 4.1), GMV-based pricing (Shopware), payment processing and third-party gateway fees (Part 3.6), app revenue share (85% to developers above $1m, so the merchant pays the app price that funds it) [VERIFIED: https://help.shopify.com/en/partners/how-to-earn, n.d., accessed 2026-11], agency retainers (Part 6.3), contract terms (Plus 1- or 3-year).
- [ASSUMPTION/JUDGEMENT] The components the vendor lists omit two the merchant pays most for: the people who own integrations after the agency leaves, and the exit (re-export of data, URL redirects, re-integration). Chapter 41's TCO table should add both.

### 5.2 Public replatforming stories (dated)

| Case | What happened | Outcome | Tag |
| --- | --- | --- | --- |
| **Target (US), 2001–2011** | Amazon ran Target.com from 2001. On 7 August 2009 Target announced it would "build and manage its own online platform", taking over "e-commerce technology platform, fulfillment and guest services operations", to launch before the 2011 holiday season | On 13 September 2011, weeks after the new site launched, the Missoni collection launch crashed Target.com, which was "down most of the day"; a second outage of 2.5 hours followed on 25 October 2011, for which Target gave no reason | [VERIFIED: https://internetnews.com/news/target-parts-ways-with-amazon-com, published 2009-08-07; https://www.mprnews.org/story/2011/10/25/targets-website-crashes-again, published 2011-10-25] **(evidence age)** |
| **Finish Line (US), 2012** | Switched to new e-commerce site technology on 19 November 2012 | Reverted to the former platform, "which it had kept operable", 17 days later; the switch cost about $3m in quarterly sales "despite a 25% increase in online sales for the quarter" | [VERIFIED: https://www.retaildive.com/news/finish-line-pulls-a-u-turn-online-after-losing-3-million/87757, published 2013-01-08] **(evidence age)** |
| **Marks & Spencer (UK), 2014** | Launched a new website in 2014 | Reported an 8% fall in online sales after the launch; a trade commentator called it "a timely reminder of the risks involved in major replatforming programmes" | [VERIFIED: https://retail-week.com/opinion/-comment-mands-fall-in-online-sales-highlights-the-risks-of-replatforming/5062103.article, published 2014-07-10; paywalled beyond the lead] **(evidence age)** |
| **Hobbycraft (UK), 2012–2013** | Delayed its website relaunch past Christmas 2012 | Deliberate: "too risky to launch the website in peak trading" | [VERIFIED: Retail Week, published 2013-02-19] **(evidence age)** |
| **Hobbycraft (UK), 2022** | Replatformed with agency Astound Commerce onto Salesforce Commerce Cloud with Bazaarvoice, Global-e, Bloomreach (search and CDP), MuleSoft and Sorted; drivers: lockdown growth, omnichannel roadmap, real-time visibility across systems | The article reports the build, not launch outcomes | [VERIFIED: https://retailtechinnovationhub.com/home/2022/6/14/astound-commerce-enlists-hobbycraft-for-e-commerce-replatforming-project, published 2022-06-14; agency-sourced] |
| **Magento 1 merchants, 2020** | Vendor EOL on 30 June 2020 forced migration to Magento 2 or another platform | Merchants warned of PCI DSS non-compliance if they stayed | [WIDELY REPORTED: Help Net Security, 2020] |

- [ASSUMPTION/JUDGEMENT] The pattern across the cases: the failures were not in the new platform's features but in capacity (Target), performance (Finish Line), search visibility and customer habit (M&S), and timing (Hobbycraft avoided it). Finish Line's recovery was possible only because the old platform was kept running, which is the parallel-run argument in one sentence.
- ASOS and Boots: no sourced replatforming outcome was found (see Research limitation). Do not cite them.

### 5.3 Analyst and practitioner material on migration risk

- **Strangler fig.** Fowler's note (originally "Strangler Application", from a 2001 trip and written "a couple of years" later, retitled to stress the botanical origin) says the term "is now often used to describe a gradual approach to legacy modernization"; plans to replace a serious system wholesale "go down in flames" because replacement takes long, users cannot wait for features, and existing behaviour is hard to pin down and partly unwanted [VERIFIED: https://martinfowler.com/bliki/StranglerFigApplication.html, published 2024-08-22, restating a 2004 note].
- **Patterns of Legacy Displacement** (Cartwright, Horn, Lewis; Thoughtworks): Transitional Architecture, Legacy Mimic, Event Interception, Divert the Flow, Feature Parity, Critical Aggregator, Canary Release, Dark Launching, "Stop the World" cutover and others; delivery strategies named as "parallel run, fork on ingress and diversion of flow"; the authors warn that defining "as is" functionality "was a huge effort" and that alternatives to seam-based decomposition "all too often result in Feature Parity and Big Bang releases" [VERIFIED: https://martinfowler.com/articles/patterns-legacy-displacement/, published 2021-07-20, revised 2024-03-05].
- [ASSUMPTION/JUDGEMENT] For commerce the seams are channels and capabilities: move the B2B shop first, or search first, or the returns flow first. The Burned Bridge pattern of chapter 42 is Finish Line without the kept-operable old platform.

### 5.4 Vendor lock-in and exit: the Data Act

Regulation (EU) 2023/2854 (Data Act), Chapter VI "Switching between data processing services":

- Providers "shall take the measures provided for in Articles 25, 26, 27, 29 and 30 to enable customers to switch to a data processing service, covering the same service type, which is provided by a different provider ... or to on-premises ICT infrastructure" (Article 23).
- Contracts must set out switching rights "clearly ... in a written contract" made available before signing (Article 25), including a minimum data-retrieval period of at least 30 days and a clause guaranteeing erasure after retrieval.
- "From 12 January 2027, providers of data processing services shall not impose any switching charges on the customer for the switching process"; until then only reduced charges, "not exceed[ing] the costs ... directly linked to the switching process" (Article 29).
- Definitions: "switching" covers extracting, transforming and uploading data to another provider or on-premises; "data egress charges" are "data transfer fees charged to customers for extracting their data"; "functional equivalence" means re-establishing "a minimum level of functionality" in the destination service for shared features; "exportable data" includes input and output data and metadata generated by the customer's use.
- Exemption (Article 31): services "of which the majority of main features has been custom-built to accommodate the specific needs of an individual customer" and "not offered at broad commercial scale" are outside Articles 23(d), 29 and 30(1) and (3).
- The Regulation applies from 12 September 2025 [VERIFIED: http://publications.europa.eu/resource/celex/32023R2854, published 2023-12-22].
- ⚠ [ASSUMPTION/JUDGEMENT] "Data processing service" is defined broadly (a digital service giving on-demand access to configurable, scalable computing resources), which on its face covers SaaS. Whether a hosted commerce platform must therefore offer free switching from 2027 is an open legal question; the brief found no guidance or enforcement example. Writers should present it as "the rules point at SaaS platforms; the first cases will tell".
- **What the platform promises.** Shopify's Terms of Service (last updated 20 October 2026): services are provided "on an 'as is' and 'as available' basis without any warranty"; "Shopify does not warrant that the Services will be uninterrupted, timely, secure, or error-free"; Shopify "reserve[s] the right to modify the Services or any part thereof for any reason, without notice and at any time" [VERIFIED: https://www.shopify.com/legal/terms, published 2026-10-20]. ⚠ [ASSUMPTION/JUDGEMENT] Plus and enterprise agreements may add service levels; none was fetched.

**For newcomers.**
- *Parallel run*: running old and new systems side by side on the same input and comparing, before the old one is switched off.
- *Switching charges / egress fees*: what a provider bills for moving your data out.
- *Functional equivalence*: being able to do, in the new service, what you could do in the old one, from your exported data.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Exit cost is designed in at purchase: whether product, order and customer data can be exported in full (Data Act "exportable data"), whether URLs and search rankings survive (M&S), whether the old platform can be kept operable for a rollback (Finish Line), and whether a launch can be moved off the peak (Hobbycraft). At the Starting stage the hosted platform's export is the exit; at Growing the integrations are the exit cost; at Omnichannel the OMS and PIM introductions are migrations in their own right; at Group the question becomes which brand moves first.

---

## PART 6: Organizing commerce engineering

### 6.1 Team shapes

- *Team Topologies* (Matthew Skelton and Manuel Pais, IT Revolution Press, 7 September 2019) defines four team types: **stream-aligned** ("aligned to a flow of work from (usually) a segment of the business domain"), **enabling** ("helps a Stream-aligned team to overcome obstacles. Also detects missing capabilities"), **complicated subsystem** ("where significant mathematics/calculation/technical expertise is needed") and **platform** ("a grouping of other team types that provide a compelling internal product to accelerate delivery by Stream-aligned teams"); and three interaction modes: collaboration, X-as-a-Service and facilitation; with "Respect Cognitive Limits" as a principle [VERIFIED: https://teamtopologies.com/key-concepts and https://teamtopologies.com/book, n.d., accessed 2026-11].
- [ASSUMPTION/JUDGEMENT] For a 14-person commerce team the honest mapping is: one or two stream-aligned teams (the order journey; the B2B and store journey), an integration or platform function of two or three people that owns the iPaaS, connectors and data, and the agency as an external stream-aligned team for the storefront. "Stream-aligned by journey vs by system" is the choice chapter 44 must make explicit; the systems view (one team per vendor) is the default a vendor landscape pushes a merchant into.

### 6.2 Lightweight governance: decision records

- Nygard (15 November 2011): "An architecture decision record is a short text file in a format similar to an Alexandrian pattern", with Title, Context ("forces at play ... described as neutral facts, often in tension"), Decision ("We will ..."), Status (proposed, accepted, deprecated, superseded) and Consequences. Without a record a newcomer can only "Blindly accept the decision" or "Blindly change it"; "It's better to avoid either blind acceptance or blind reversal" [VERIFIED: https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions, published 2011-11-15].
- [ASSUMPTION/JUDGEMENT] In a commerce team the decisions worth a record are the ownership ones (which system is the system of record for stock, price, product, order), the vendor ones (why this OMS, with what exit) and the app ones (which apps may write stock). The ledger's Waypoint decisions W1–W8 are ADR-shaped.

### 6.3 Agencies, implementation partners and the vendor's partner economy

- **Shopify partner earnings (⚠ undated, subject to change at Shopify's "sole discretion").** For stores a partner builds or transfers: 20% of the monthly base platform fee plus 0.1% of monthly eligible GMV (online consumer transactions, excluding B2B, up to $100m annually), for four years. Plus or Enterprise referrals: a one-time $2,500 payout once the merchant has a signed agreement, more than $5,000 GMV and a paid first invoice. App Store: developers keep 100% of the first $1m and 85% above it (85% of everything for companies with $20m+ App Store earnings or $100m+ revenue), with a 2.9% processing fee; themes 85% [VERIFIED: https://help.shopify.com/en/partners/how-to-earn, n.d., accessed 2026-11].
- **Partner tiers.** Service and agency partners are tiered Silver, Gold, Platinum and Diamond "based on attributed GMV and attributed shops"; the older Select, Plus and Premier tiers "retire on January 1, 2027"; technology partners participate through the App Store [VERIFIED: https://help.shopify.com/partners/plus-partners, n.d., accessed 2026-11 (page describes a 4 November 2026 preview)].
- **Agency-led replatforming.** Hobbycraft's 2022 move to Salesforce Commerce Cloud was built by Astound Commerce "after a competitive pitch", using the agency's accelerator and a stack of six third-party services [VERIFIED: RTIH, published 2022-06-14].
- [ASSUMPTION/JUDGEMENT] The partner economics explain agency behaviour: an agency is paid by the platform for keeping the merchant on it and for GMV, and by the merchant for building; it is not paid for integration ownership after launch or for an exit. Chapter 44's vendor-management section should say so plainly and make the ownership map (who owns each integration after go-live) the contract's first page.

### 6.4 Vendor management and SLAs

- Shopify's standard terms disclaim uninterrupted service and reserve the right to modify the service without notice (Part 5.4) [VERIFIED: Shopify ToS, 2026-10-20]. Adyen prices carry "a minimum invoice depending on industry or business model" [VERIFIED: Adyen pricing, n.d.]. Shopify Plus is sold on one- or three-year terms [VERIFIED: Shopify pricing, n.d.].
- [ASSUMPTION/JUDGEMENT] No vendor SLA document was fetched; writers should ask for the actual Plus, commercetools or SAP agreement rather than quote a marketing uptime figure. The contract items that matter for architecture: API rate limits and versioning (the `shopify` brief), data export, notice periods for deprecations, and the Data Act switching clauses from 2027.

### 6.5 Product management in commerce teams

- [ASSUMPTION/JUDGEMENT] No primary source specific to commerce product management was fetched. The defensible statement: in a merchant, the product manager's product is the order journey, not the platform; the metrics in Part 3 (conversion, AOV, return rate, delivery promise kept) are the product metrics; the vendor's product manager optimizes GMV and tenancy. The asymmetry is why a merchant needs its own PM even when it buys everything.

### 6.6 AI coding tools in small teams

- Stack Overflow's 2025 survey: 84% of respondents use or plan to use AI tools (2024: 76%); 51% of professional developers use them daily; favourable sentiment fell to about 60% from over 70% in 2023–2024; 46% distrust the accuracy of AI output and 3% highly trust it; 66% name "AI solutions that are almost right, but not quite" as the main frustration; 31% use AI agents at work (33,662 responses to the usage question) [VERIFIED: https://survey.stackoverflow.co/2025/ai, published 2025].
- Shopify CEO Tobi Lütke's memo, circulated 7 April 2025: "Reflexive AI usage is now a baseline expectation at Shopify"; staff must show why AI cannot do a task before asking for more resources; AI competency enters performance reviews and hiring [VERIFIED: https://www.digitalcommerce360.com/2025/04/08/internal-memo-shopify-ceo-declares-ai-non-optional/, published 2025-04-08].
- DORA's 2025 report, *State of AI-assisted Software Development*: "AI's primary role is as an amplifier, magnifying an organization's existing strengths and weaknesses", with the largest returns from the "underlying organizational system rather than the tools themselves" [VERIFIED: https://dora.dev/research/2025/dora-report/, published 2025].
- [ASSUMPTION/JUDGEMENT] For a 14-person team with an agency, the implication is narrow and useful: AI tools shift the bottleneck from writing connector code to owning it (tests against sandboxes, idempotency, monitoring), which is the capability a small team lacks and an agency does not sell.

**For newcomers.**
- *Stream-aligned team*: a team that owns one flow of work end to end (an order journey), rather than one system.
- *ADR (architecture decision record)*: a one-page note of a decision, its context and its consequences, kept with the code.
- *Implementation partner / agency*: an external firm that builds and sometimes runs the storefront and integrations, usually certified and paid in part by the platform vendor.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Ownership follows money unless it is designed. At Starting, the founder owns everything and the platform's support is the team. At Growing, the agency builds the first integrations and nobody owns them after launch, which is the origin of most Omnichannel-stage incidents. At Omnichannel, the merchant must own the joins (iPaaS, OMS, data definitions) in-house even if it buys every system. At Group, a platform team serves brand-level stream-aligned teams, and the shared-vs-autonomous decision becomes the governance question.

---

## Key numbers

| Number | Value | Source | Date |
| --- | --- | --- | --- |
| EU internet users who bought online, 2025 | 78% | Eurostat | extracted 2026-02 |
| EU enterprise turnover from e-sales, 2024 | 19.49% (web 8.39%, EDI-type 11.07%) | Eurostat | extracted 2026-02 |
| European B2C e-commerce turnover, 2025 | €911bn, +7% (2024: €842bn; 2026f: €961bn) | Ecommerce Europe / EuroCommerce / CMI | 2026-09-22 |
| Dutch online consumer spending, 2025 | €35.7bn, -1%; 347m purchases; cross-border 13% | Thuiswinkel Markt Monitor (NielsenIQ) | 2026-03-31 |
| German online goods sales, 2025 (gross) | €83.1bn, +3.2% | bevh | 2026-01-22 |
| German online retail, 2025 (net) and share | €92.3bn, +3.9%; 13.5% of retail | HDE Online-Monitor 2026 | n.d. (2026) |
| US e-commerce share of retail, Q2 2026 | 17.1% adjusted ($340.2bn), +12.2% y/y; 18.3% NSA in Q4 2025 | US Census Bureau | 2026-08-18 |
| US e-commerce share, Q2 2020 (pandemic peak) | 16.1% (from 10.8%) | US Census Bureau | 2020-08-18 |
| US B2B e-commerce forecast | $1.7tn (2021) to about $3tn (2027), 24% of B2B sales | Forrester | 2022-06-08 |
| US total B2B sales, 2025 | $15.12tn, +0.4% | Digital Commerce 360 | 2026-01-26 |
| Shopify-store conversion, Oct 2026 | median 1.3%, mean 1.9% (438 stores) | Littledata | 2026-11-04 |
| Cart abandonment, average of 50 studies | 70.22%; top reason extra costs 40% | Baymard | 2026-10-28 |
| Shopify BFCM 2025 | $14.6bn GMV, $5.1m/min peak, cart $114.70, 16% cross-border | Shopify | 2025-12-02 |
| Adobe Cyber Week 2025 (US) | $44.2bn, +7.7%; Cyber Monday $14.25bn, $16m/min peak; mobile 57.5% | Adobe Analytics | 2025-12-02 |
| US returns, 2025 | $849.9bn, 15.8% of sales; 19.3% of online sales; 9% fraudulent | NRF / Happy Returns | 2025-10-15 |
| Gross margin, apparel and outdoor | VF 54.8%; Columbia 50.5%; ASOS 47.1%; Nike 42.9%; Zalando 39.9% (B2C 42.3%) | 10-Ks, RNS, annual report | 2025–2026 |
| Zalando 2025 | GMV €17.56bn; revenue €12.35bn; 62.0m active customers; 278.6m orders; basket €62.8; 4.8 orders/customer; partner share 32.1% | Zalando AR 2025 | 2026-03 |
| Amazon 2025 | third-party seller services $172.2bn; 3P about 61–62% of units, 69% of est. $830bn GMV (analyst estimate) | Amazon 10-K; Marketplace Pulse | 2026-02 |
| Target 2025 | stores fulfilled 97.6% of merchandise sales; gross margin 27.9% | Target 10-K | 2026-03-11 |
| EU interchange caps | 0.2% debit, 0.3% credit (consumer cards), applied from 9 Dec 2015 | Regulation (EU) 2015/751 | 2015-05-19 |
| PSP list prices, NL (EEA consumer cards) | Stripe 1.5% + €0.25; Mollie 1.80% + €0.25; Shopify Payments 1.9% to 1.4% + €0.25; Adyen $0.13 + IC++ + 0.60% | vendor pages | n.d., 2026-11 |
| Shopify plans (EUR) | Basic €21–28; Grow €59–78; Advanced €289–384; Plus from €2,100; third-party gateway fee 2% to 0.2% | Shopify pricing | n.d., 2026-11 |
| Shopware | Community free to €1m GMV/365 days; Rise from €600; Evolve from €2,400 | Shopware pricing | n.d., 2026-11 |
| Warby Parker marketing, 2025 | $110.2m on $871.9m revenue (12.6%); gross margin 54.0% | Warby Parker 10-K | 2026-02 |
| Finish Line, 2012 | reverted after 17 days; about $3m lost sales | Retail Dive | 2013-01-08 |
| Target, 2011 | Missoni crash 13 Sep 2011 "down most of the day"; 2.5-hour outage 25 Oct 2011 | MPR News | 2011-10-25 |
| Data Act switching charges | reduced from 11 Jan 2024; prohibited from 12 Jan 2027; Regulation applies from 12 Sep 2025 | Regulation (EU) 2023/2854 | 2023-12-22 |
| Shopify partner revenue share | 20% of subscription + 0.1% GMV for 4 years; Plus referral $2,500 one-time; apps 100%/85% | Shopify Help Center | n.d., 2026-11 |
| Developers using or planning AI tools, 2025 | 84%; 46% distrust accuracy; 66% "almost right" | Stack Overflow | 2025 |
| MACH Alliance founding | 24 Jun 2020; EPAM, commercetools, Contentstack, Valtech | EPAM press release | 2020-06-24 |

## Open questions / not verifiable

1. **Retail IT spend as a share of revenue**: no primary figure (Avasant and Gartner paywalled). The 2–4% range is judgement.
2. **Typical system counts and team sizes per scale stage**: no public survey found; the ledger's shapes are illustrative.
3. **ASOS and Boots replatforming outcomes**: not verified; do not cite.
4. **Return rates for online fashion** (Zalando, ASOS): neither publishes a rate; "about 50%" is lore.
5. **Vendor SLAs**: no SLA document fetched (commercetools 404; Shopify Plus page 404); only Shopify's standard "as is" terms are verified.
6. **Whether hosted commerce platforms are "data processing services" under the Data Act** and must offer free switching from 12 January 2027: open legal question, no guidance found.
7. **Current Dutch online share of retail**: the Markt Monitor release gives none; the 2021 infographic's 26% of product spending is the last verified share.
8. **B2B e-commerce size, current**: Forrester's figure is from 2022; DC360's 2025–2026 B2B e-commerce dollar figures were seen only in secondary summaries.
9. **Subscription commerce taxonomy and churn**: McKinsey 2018 could not be fetched.
10. **European free-shipping thresholds and shipping cost benchmarks**: no survey verified.
11. **Target's 2011 relaunch date and the role of the in-house platform in the crashes**: press at the time disagreed; the chain-of-events (2009 decision, 2011 launch, two crashes) is verified, the cause is not.
12. **Magento's first GA date** (31 March 2008): Wikipedia marks it "citation needed".

## Source list

| Title | Publisher / author | Year | URL |
| --- | --- | --- | --- |
| E-commerce statistics for individuals | Eurostat | 2026 | https://ec.europa.eu/eurostat/statistics-explained/index.php?title=E-commerce_statistics_for_individuals |
| E-commerce statistics (enterprises) | Eurostat | 2026 | https://ec.europa.eu/eurostat/statistics-explained/index.php?title=E-commerce_statistics |
| European e-commerce reaches €911 billion (press release, 2026 report) | Ecommerce Europe, EuroCommerce, CMI | 2026 | https://www.eurocommerce.eu/app/uploads/2026/09/final-draft-press-release-15092026.pdf |
| Corrigendum, European E-commerce Report 2025 | Ecommerce Europe, EuroCommerce | 2025 | https://www.eurocommerce.eu/app/uploads/2025/10/final-corrigendum-press-release.pdf |
| Meer online productaankopen, minder uitgaven aan reizen en evenementen in 2025 (Thuiswinkel Markt Monitor) | NielsenIQ for Thuiswinkel.org | 2026 | https://nielseniq.com/global/nl/news-center/2026/meer-online-productaankopen-minder-uitgaven-aan-reizen-en-evenementen-in-2025/ |
| Infographic Thuiswinkel Markt Monitor HY1 2021 | Thuiswinkel.org / Betaalvereniging | 2021 | https://www.betaalvereniging.nl/wp-content/uploads/2025/09/Infographic_Thuiswinkel_Markt_Monitor_2021_HY.pdf |
| bevh press releases (2025 results; Q1–Q3 2026) | bevh via presseportal | 2026 | https://www.presseportal.de/nr/52922 |
| E-Commerce Deutschland Umsatz 2025 | retail-news.de | 2026 | https://retail-news.de/e-commerce-deutschland-umsatz-2025/ |
| HDE Online-Monitor | Handelsverband Deutschland | 2026 | https://einzelhandel.de/online-monitor |
| Quarterly Retail E-Commerce Sales, 2nd Quarter 2026 | US Census Bureau | 2026 | https://www.census.gov/retail/mrts/www/data/pdf/ec_current.pdf |
| Quarterly Retail E-Commerce Sales, 2nd Quarter 2020 | US Census Bureau | 2020 | https://www2.census.gov/retail/releases/historical/ecomm/20q2.pdf |
| Forrester: US B2B e-commerce will reach an estimated $3 trillion by 2027 | Forrester | 2022 | http://www.forrester.com/press-newsroom/forrester-us-b2b-e-commerce-will-reach-an-estimated-3-trillion-by-2027/ |
| US B2B sales exceed $15 trillion in 2025 | Digital Commerce 360 (Mark Brohan) | 2026 | https://www.digitalcommerce360.com/2026/01/26/us-b2b-sales-exceed-15-trillion-2025/ |
| Average ecommerce conversion rate | Littledata | 2026 | https://www.littledata.io/average/ecommerce-conversion-rate |
| Ecommerce market data | IRP Commerce | n.d. | https://www.irpcommerce.com/IRPStrategyCenter/Public/EcommerceMarketData.aspx |
| 50 cart abandonment rate statistics | Baymard Institute | 2026 | https://baymard.com/lists/cart-abandonment-rate |
| BFCM data 2025 | Shopify | 2025 | https://www.shopify.com/news/bfcm-data-2025 |
| Adobe: Cyber Monday hits record $14.25 billion | Adobe | 2025 | https://news.adobe.com/news/2025/12/adobe-cyber-monday-hits-record |
| Adobe holiday e-commerce beats expectations, record $257.8B | Chain Store Age | 2026 | https://chainstoreage.com/adobe-holiday-e-commerce-beats-expectations-record-2578b |
| Consumers expected to return nearly $850 billion in merchandise in 2025 | NRF / Happy Returns | 2025 | https://nrf.com/media-center/press-releases/consumers-expected-to-return-nearly-850-billion-in-merchandise-in-2025 |
| 2024 Consumer Returns in the Retail Industry | NRF / Happy Returns | 2024 | https://nrf.com/research/2024-consumer-returns-retail-industry |
| VF Corporation Form 10-K, fiscal 2026 | VF Corporation (SEC) | 2026 | https://www.sec.gov/Archives/edgar/data/103379/000010337926000030/vfc-20260328.htm |
| Columbia Sportswear Form 10-K, 2025 | Columbia Sportswear (SEC) | 2026 | https://www.sec.gov/Archives/edgar/data/1050797/000105079726000028/colm-20251231.htm |
| NIKE Form 10-K, fiscal 2026 | NIKE, Inc. (SEC) | 2026 | https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm |
| Target Form 10-K, 2025 | Target Corporation (SEC) | 2026 | https://www.sec.gov/Archives/edgar/data/27419/000002741926000016/tgt-20260131.htm |
| Amazon Form 10-K, 2025 | Amazon.com, Inc. (SEC) | 2026 | https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm |
| eBay Form 10-K, 2025 | eBay Inc. (SEC) | 2026 | https://www.sec.gov/Archives/edgar/data/1065088/000106508826000027/ebay-20251231.htm |
| Shopify Form 10-K, 2025 | Shopify Inc. (SEC) | 2026 | https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm |
| Shopify Annual Information Form (exhibit) | Shopify Inc. (SEC) | 2022 | https://www.sec.gov/Archives/edgar/data/1594805/000159480522000011/exhibit11annualinformation.htm |
| Warby Parker Form 10-K, 2025 | Warby Parker Inc. (SEC) | 2026 | https://www.sec.gov/Archives/edgar/data/1504776/000150477626000006/wrby-20251231.htm |
| Zalando SE Annual Report 2025 | Zalando SE | 2026 | https://corporate.zalando.com/sites/default/files/media-download/zalando-se_annual-report-2025_eng_261003_s.pdf |
| ASOS plc final results, 52 weeks to 31 August 2025 (RNS) | ASOS plc | 2025 | https://www.asosplc.com/media/ikxfhqeu/asos-fy25-results-rns-final-20251120.pdf |
| Amazon GMV surpassed $800 billion in 2025 | Marketplace Pulse | 2026 | https://www.marketplacepulse.com/articles/amazon-gmv-surpassed-800-billion-in-2025 |
| Regulation (EU) 2015/751 on interchange fees | EU Publications Office | 2015 | http://publications.europa.eu/resource/celex/32015R0751 |
| Regulation (EU) 2023/2854 (Data Act) | EU Publications Office | 2023 | http://publications.europa.eu/resource/celex/32023R2854 |
| Stripe pricing (Netherlands) | Stripe | n.d. | https://stripe.com/nl/pricing |
| Mollie pricing | Mollie | n.d. | https://www.mollie.com/pricing |
| Adyen pricing | Adyen | n.d. | https://www.adyen.com/pricing |
| Shopify pricing | Shopify | n.d. | https://www.shopify.com/pricing |
| Shopify for Enterprise | Shopify | n.d. | https://www.shopify.com/enterprise |
| Shopify Terms of Service | Shopify | 2026 | https://www.shopify.com/legal/terms |
| Shopify Partner earnings | Shopify Help Center | n.d. | https://help.shopify.com/en/partners/how-to-earn |
| Shopify partner tiers (Plus Partner Program page) | Shopify Help Center | n.d. | https://help.shopify.com/partners/plus-partners |
| Ecommerce Replatforming and Migration Guide for 2026 | Shopify Enterprise blog (Michael Metcalf) | 2026 | https://www.shopify.com/enterprise/blog/ecommerce-replatforming |
| Shopware pricing | Shopware | n.d. | https://www.shopware.com/en/pricing/ |
| Top 3 signs you need a PIM | Akeneo (guest post, Sitation) | n.d. | https://www.akeneo.com/blog/top-3-signs-you-need-a-pim/ |
| 8 signs your brand needs an OMS | Opollo (vendor blog) | n.d. | https://opollo.onpoint.vn/blog/8-signs-your-brand-needs-an-order-management-system-oms |
| IT Spending and Staffing Benchmarks 2025/2026, Chapter 8: Retail | Avasant | 2025 | https://avasant.com/report/it-spending-and-staffing-benchmarks-2025-2026-chapter-8-retail/ |
| EPAM joins newly formed MACH Alliance as founding member | EPAM Systems | 2020 | https://s202.q4cdn.com/436759741/files/doc_news/2020/06/24/12951.pdf |
| NetMarket | Wikipedia (citing NYT 1994-08-12) | 2014 (retrieval) | https://en.wikipedia.org/wiki/NetMarket |
| Magento | Wikipedia | 2026 (accessed) | https://en.wikipedia.org/wiki/Magento |
| Magento 1 reaches EOL | Help Net Security | 2020 | https://www.helpnetsecurity.com/2020/06/29/magento-1-eol/ |
| Target parts ways with Amazon.com | InternetNews | 2009 | https://internetnews.com/news/target-parts-ways-with-amazon-com |
| Target's website crashes again | MPR News (AP) | 2011 | https://www.mprnews.org/story/2011/10/25/targets-website-crashes-again |
| Finish Line pulls a U-turn online after losing $3 million | Retail Dive | 2013 | https://www.retaildive.com/news/finish-line-pulls-a-u-turn-online-after-losing-3-million/87757 |
| Comment: M&S fall in online sales highlights the risks of replatforming | Retail Week | 2014 | https://retail-week.com/opinion/-comment-mands-fall-in-online-sales-highlights-the-risks-of-replatforming/5062103.article |
| Crafts retailer Hobbycraft to complete delayed digital roll-out by summer | Retail Week | 2013 | https://retail-week.com/general-merchandise/crafts-retailer-hobbycraft-to-complete-delayed-digital-roll-out-by-summer/5046363.article |
| Astound Commerce enlists Hobbycraft for e-commerce replatforming project | Retail Technology Innovation Hub | 2022 | https://retailtechinnovationhub.com/home/2022/6/14/astound-commerce-enlists-hobbycraft-for-e-commerce-replatforming-project |
| Strangler Fig Application | Martin Fowler | 2024 (orig. 2004) | https://martinfowler.com/bliki/StranglerFigApplication.html |
| Patterns of Legacy Displacement | Ian Cartwright, Rob Horn, James Lewis (martinfowler.com) | 2021, rev. 2024 | https://martinfowler.com/articles/patterns-legacy-displacement/ |
| Documenting Architecture Decisions | Michael Nygard (Cognitect) | 2011 | https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions |
| Team Topologies: key concepts; the book | Matthew Skelton, Manuel Pais | 2019 / n.d. | https://teamtopologies.com/key-concepts ; https://teamtopologies.com/book |
| 2025 Developer Survey: AI | Stack Overflow | 2025 | https://survey.stackoverflow.co/2025/ai |
| Internal memo: Shopify CEO declares AI non-optional | Digital Commerce 360 (Mark Brohan) | 2025 | https://www.digitalcommerce360.com/2025/04/08/internal-memo-shopify-ceo-declares-ai-non-optional/ |
| State of AI-assisted Software Development 2025 | DORA (Google Cloud) | 2025 | https://dora.dev/research/2025/dora-report/ |
