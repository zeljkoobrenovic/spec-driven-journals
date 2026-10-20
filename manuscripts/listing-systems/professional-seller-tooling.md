{id: professional-seller-tooling}
# 17. Serving the Pros: Dealer, Agent and Merchant Tooling

![Serving the Pros: Dealer, Agent and Merchant Tooling — logo](listing-systems-architecture/posts/17-professional-seller-tooling/assets/images/17-professional-seller-tooling/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Learn what professional sellers need from a marketplace (inventory operations, performance and ROI reporting, lead management, pricing and market insight, team permissions and integrations) and how to architect it as a workspace over shared systems of record. You will also see why software sold to professionals, such as an agent CRM, creates a conflict of interest with the portal, and how to design that conflict out.

> **WHY THE BUSINESS CARES:** Professionals pay most of the bills in automotive and real estate. They renew when they can prove that the marketplace produced sales, and they downgrade quietly when they cannot. Pro tooling is where that proof is made or lost, and where a portal either becomes part of the professional's daily workflow or stays a cost line.

> **WHY ARCHITECTS SHOULD CARE:** Pro tools read from every domain at once: listings, leads, statistics, entitlements, prices and accounts. Built carelessly, they become a second system of record with numbers that disagree with billing and with the professional's own CRM. Built well, they are a thin workspace and an API surface that partners can build on.

> **KEY POINTS:**
>
> * **Professionals buy outcomes and judge them with their own systems.** A dealer or agency compares the marketplace's lead count with its CRM and its sales. Statistics, lead exports and invoices must come from the same events, carry the same identifiers and survive that comparison, or the renewal conversation is lost before it starts.
> * **Pro tooling is a workspace, not a system of record.** Inventory, leads, entitlements and accounts belong to their domains. The pro workspace composes them for one organization, with permissions that follow its hierarchy, and exposes the same capabilities through APIs, because many professionals will use them from partner software rather than from the portal.
> * **Software sold to professionals must be neutral by architecture.** When the group also sells the CRM that publishes to competing portals, neutrality has to be enforced by separate tenancy, API parity, data boundaries and audit evidence. In the EU, the Platform-to-Business Regulation already requires portals to describe their data access and any differentiated treatment of their own services.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Vanity Liquidity** — pro dashboards that report views and impressions instead of contacts, leads and sales sell exposure the professional cannot convert, and renewals fail.
> * **Feed Roulette** — professional feeds without visible validation and error reports leave dealers and agents to discover missing stock from their customers.
> * **Entitlement Spaghetti** — pro features gated by package checks scattered across the tooling make it impossible to say what a professional bought and what they received.

A private seller visits a marketplace a few times a year. A dealer or an estate agent lives in it. Their sales staff open the lead inbox before their e-mail, their managers read the weekly statistics before the board meeting, and their integration partner pushes inventory every few minutes. For these customers the marketplace is not a website. It is **one of the systems their business runs on**, next to their dealer management system (DMS) or agency CRM, and they judge it the way they judge their other systems: by whether its numbers reconcile.

This chapter closes Part III's supply chain at the point where the professionals check it. [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion) and [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline) brought their stock in; pro tooling is where they see what that stock produced, and where the marketplace's liquidity becomes visible to the people who pay for it. A Motorvane dealer pays for listing slots and prominence; what they want to know is how many qualified buyers each car produced and how many of those bought. A Hearthly agency pays a subscription; what it wants to know is whether the portal brought it sellers and tenants.

This chapter owns three terms. **Pro tooling** is the set of products a marketplace gives professional sellers to run their business on it: inventory and visibility operations, performance and ROI reporting, lead management, pricing and market insight, team and account administration, and the APIs behind all of them. **Lead management for pros** is the professional's side of a lead: receiving, assigning, answering, qualifying and recording the outcome of buyer contacts, inside the portal or in the professional's own CRM. **Pro SaaS** (software as a service) is software sold to professionals as a product in its own right, such as an agent CRM or a dealer website builder, usable whether or not the professional lists on the group's portals. The lead itself, conversations and lead routing belong to [From Interest to Contact: Messaging and Lead Management](#messaging-and-leads); packages and entitlements to [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements); the organization model to [Private Sellers, Dealers and Agencies: Modeling Who Lists](#sellers-and-accounts); feeds to [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion).

{id: professional-seller-tooling--setting-the-scene-at-veldmark-two-arguments-in-one-week}
## Setting the Scene at Veldmark: Two Arguments in One Week

It is the second week of June 2027 at Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)). Two arguments about professional tooling reach Ingrid Halvorsen, the Group Chief Architect, in the same week.

**The first comes from Essen.** Autohaus Ruhrblick, the dealer that sold the 2021 Volkswagen Golf through Motorvane in April, is up for renewal. It pays **€1,450 a month** for Motorvane's "Pro 150" package with 150 listing slots, above Motorvane's average of about €927 per dealer (see [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements) and [How Listing Marketplaces Make Money](#monetization-models)). Its sales director has compared the Golf's numbers. Motorvane's dealer portal, **Dealer Hub**, shows **23 leads** in the first ten days. The dealer's CRM received **14**. The sales director's conclusion is that Motorvane counts generously and the package is worth less than its price; the proposal on the table is a downgrade to a smaller package. Felix Brandt, Motorvane's CTO, wants funding to rebuild Dealer Hub, which runs on a reporting database fed nightly from three lead systems.

**The second comes from Lyon.** Keybridge, the agent CRM that Veldmark acquired in 2024, publishes listings for its 9,800 agency customers to many portals, including Hearthly's competitors. One of those agencies is Agence Rhône Habitat, a 14-branch network whose Lyon branch listed the Lyon apartment in May. Emma Laurent, Keybridge's founder and general manager, wants to launch a "portal performance" report that shows each agency how many leads each portal produced per listing. Claire Fontaine, Hearthly's CEO, asks a reasonable-sounding question at the next leadership meeting: could Hearthly see the aggregated comparison, to learn where it underperforms?

The March 2027 decision on Keybridge is clear on principle: **no Keybridge agency data is used by Hearthly for ranking or sales targeting**, with access controls and an annual independent review. It says nothing about how. Ingrid's task is to answer both arguments with one design: what professionals need, how the tooling should be built, and how a group that sells software to professionals keeps that software neutral.

{id: professional-seller-tooling--concepts-what-professionals-need}
## Concepts: What Professionals Need

{id: professional-seller-tooling--the-professional-s-jobs}
### The professional's jobs

The productscape reference model of a general listings marketplace, a generic model and not a description of any company, gives its professional-merchant persona three jobs: operate inventory and visibility at scale, convert demand into qualified transactions, and prove value to justify continued spend. Its fears are equally specific: "paying for exposure without measurable return" and a feed sync that "has silently dropped half their stock". The real-estate model adds a job that has no equivalent for dealers: an agency must first **win mandates** from owners before it has anything to list, so prospecting and valuation tools are part of its toolkit.

Table 1 maps those jobs to capabilities and to documented products.

| Professional job | Capability | Documented example |
| --- | --- | --- |
| Operate inventory at scale | Portfolio view, bulk edit, feed health and error reports, listing quality checks | mobile.de's Seller API exposes listing quality checks and statistics ([mobile.de Seller API](https://services.mobile.de/manual/seller-api.html), n.d., accessed 2026) |
| Create listings efficiently | Assisted listing creation from photos, decoded data and generated text | Autotrader's Co-Driver "anecdotally" cut listing time from 28 to 5 minutes; 86% of retailers had used a Co-Driver tool ([Autotrader FY2026 results](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf), May 2026) |
| Control visibility | Buy and apply paid products per listing or per branch | Rightmove's feed applies premium and featured listings through the same API as property data ([Rightmove RTDF](https://media.rightmove.co.uk/ps/pdf/guides/adf/Rightmove_Real_Time_Datafeed_Specification.pdf), v1.4.1, November 2023) |
| Convert demand | Lead inbox, assignment, reply assistance, call handling, CRM export | mobile.de's Lead Manager drafts 45% of written replies with AI and offers a Lead API into existing CRMs ([mobile.de newsroom](https://newsroom.mobile.de/plattform-update-sommer-2026/), July 2026) |
| Price to sell | Price ratings, days-to-sell forecasts, price simulation | mobile.de's coming "Preis-Planer" simulates price changes in 2% steps against days on market, price rating and search position ([mobile.de newsroom](https://newsroom.mobile.de/plattform-update-sommer-2026/), July 2026) |
| Win supply (real estate) | Valuation tools, seller-lead detection, prospecting maps | AVIV's Ultimmo offer, as described in 2022 (the current offer may have changed), combined an estimation tool, seller-prospect detection among buyer contacts and a prospecting map ([MySweetImmo](https://www.mysweetimmo.com/2022/11/03/pros-de-limmo-aviv-group-lance-ultimmo-une-offre-pour-capter-vendeurs-et-acheteurs/), November 2022) |
| Prove value | Performance statistics, ROI reports, account management | Rightmove's feed offers branch and property performance calls ([Rightmove RTDF](https://media.rightmove.co.uk/ps/pdf/guides/adf/Rightmove_Real_Time_Datafeed_Specification.pdf)); CarGurus' account managers provide "ROI tracking" ([CarGurus 10-K](https://www.sec.gov/Archives/edgar/data/1494259/000119312526059435/carg-20251231.htm), filed February 2026) |
| Run a team | Users, roles, branches, lead ownership | mobile.de lists "multi-locations" among its Seller API resources ([mobile.de Seller API](https://services.mobile.de/manual/seller-api.html)) |

**Table 1:** *Eight professional jobs and the capabilities that serve them. Every row has a public example, and every row reads from more than one domain.*

**Pro tooling is a composition problem**: no row of the table lives in one service. A statistics page reads listings, events, leads and entitlements; a lead inbox reads conversations, call records, accounts and the listing.

{id: professional-seller-tooling--outcome-not-exposure}
### Outcome, not exposure

The professional's real question is causal: *what did the marketplace produce that I would not have had otherwise?* Two pieces of public evidence show how hard that question is.

- **Self-selection distorts package dashboards.** In an August 2026 post, OLX's engineers describe how professional sellers choose a package when they publish, and naive metrics made premium-package ads "appear to perform worse" than cheaper ones. After propensity-score matching, moving from the cheapest to the most expensive package was associated with **97.4%** more conversions, and a comparison with a randomized test found the matched estimates consistently higher than the experimental ones, a sign of remaining confounding ([OLX tech blog](https://tech.olx.com/correlation-lied-to-us-rethinking-product-impact-with-causal-inference-5ba47181f7c5), August 2026).
- **Incumbents report outcomes, not views.** Rightmove's 2025 results claim its products deliver "7 out of 10 vendor instructions within resale, and 8 out of 10 tenants for lettings properties" ([Rightmove FY2025 results](https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf), February 2026). Autotrader reports that full reservations through Deal Builder "continue to be the very best enquiries in terms of conversion to sale" ([Autotrader FY2026 results](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf), May 2026).

The architecture therefore needs a **performance funnel per listing, branch and organization**, from impressions through detail views and contacts to deduplicated leads and, where the data exists, outcomes. Views and impressions belong in the funnel as diagnostics, not as the headline. A dashboard whose top number is views is the Vanity Liquidity pattern served to a paying customer.

{id: professional-seller-tooling--the-lead-from-the-professional-s-side}
### The lead from the professional's side

[From Interest to Contact: Messaging and Lead Management](#messaging-and-leads) defines a **lead** as a buyer contact with commercial intent attached to a listing and a seller. From the professional's side, a lead has a lifecycle the marketplace often cannot see: it is assigned to a salesperson, answered, qualified, turned into an appointment and won or lost, usually in the professional's CRM. Figure 1 shows that lifecycle as the pro workspace should model it.

![Diagram: The professional's lead lifecycle](listing-systems-architecture/posts/17-professional-seller-tooling/assets/images/17-professional-seller-tooling/fig01-professional-s-lead-lifecycle-marketplace-records.jpeg)

**Figure 1:** *The professional's lead lifecycle. The marketplace records Received, Merged, Assigned and Responded itself; the later states usually happen in the professional's CRM and come back only through an integration. ROI reporting is only as good as that return path.*

**Response time** and **outcome** are the two measurements in the figure that matter most. Response time is the one the marketplace can see and the professional can improve; mobile.de's 2026 lead-performance report tracks exactly response time, response rate and processing status. Outcome is the one the professional sees and the marketplace needs; without it, ROI is an estimate.

{id: professional-seller-tooling--pro-saas-and-the-neutrality-problem}
### Pro SaaS and the neutrality problem

Many marketplace groups also sell software to professionals. Scout24's "Transaction Enablement" line, covering the Propstack CRM and the Sprengnetter and bulwiengesa data and valuation businesses, earned €106.6 million in 2025 ([Scout24 preliminary FY2025 results](https://www.scout24.com/media/scout24/Investor_Relations/Berichte_und_Praesentationen/2025/Scout24_Preliminary_IR_News_Q4_FY_2025_results_DE.pdf), February 2026). Zillow's FY2025 annual report lists its agent CRM Follow Up Boss, which added AI message suggestions, call summaries and "intelligent lead routing" ([Zillow 10-K](https://www.sec.gov/Archives/edgar/data/1617640/000161764026000015/z-20251231.htm), filed February 2026). In US automotive, Cox Automotive's brands include the Autotrader.com marketplace alongside vAuto inventory software, the Dealertrack DMS and the VinSolutions CRM ([Cox Automotive](https://www.coxautoinc.com/), n.d.). Cars.com runs dealer websites for about 7,700 dealers through Dealer Inspire and D2C Media ([Cars.com 10-K](https://www.sec.gov/Archives/edgar/data/1683606/000119312526076546/cars-20251231.htm), filed February 2026).

Owning that software brings an advantage and a conflict. The advantage: the software sits where listings originate, and switching CRMs is painful. The conflict: **the CRM that creates a professional's listings knows what the professional publishes to every competitor**, how each portal performs and which sellers are about to come to market. If the portal can see that, competing portals and the professionals themselves have reason to distrust both products.

{id: professional-seller-tooling--architecture-a-workspace-over-systems-of-record}
## Architecture: A Workspace Over Systems of Record

{id: professional-seller-tooling--three-properties-of-the-pro-workspace}
### Three properties of the pro workspace

The reference architecture I recommend (Figure 2) has three properties: the pro workspace owns no business records, every capability is available through the same API the partners use, and statistics are computed from the same event stream as billing.

![Diagram: The pro workspace composes domain services for one organization](listing-systems-architecture/posts/17-professional-seller-tooling/assets/images/17-professional-seller-tooling/fig02-pro-workspace-composes-domain-services-one.jpeg)

**Figure 2:** *The pro workspace composes domain services for one organization. The portal UI, the app and partner software reach the same capabilities through one gateway with organization-scoped tokens. Statistics, the lead ledger and billing all consume one event stream, so their numbers can be reconciled.*

The pieces, and why each sits where it does:

- **Pro API gateway.** One entry point for the portal's own front ends and for partners. Tokens are scoped to an organization and, where needed, a branch and a capability (listings write, leads read). The productscape model gives the partner surface its own gateway, sandbox and developer portal with "certification and SLA controls", which matches what the public portals document.
- **Pro workspace backend.** A backend-for-frontend that composes listing, lead, entitlement, account, insight and statistics data for one organization. It caches, but it does not own; if it disappears, no record is lost. This is the defense against the second system of record.
- **Lead ledger.** One store of deduplicated leads across channels (messages, tracked calls, bookings, reservations), with a stable lead identifier and a buyer-deduplication key. [How Listing Marketplaces Make Money](#monetization-models) proposes it at Motorvane as the basis for any per-lead billing; here it is also the basis for the inbox, the statistics and the CRM export.
- **Performance read model.** Aggregates exposure, views, contacts and leads per listing, branch and organization from events. It is a read model in the sense of [System of Record and Read Models: Listing Data Management](#listing-data-management), rebuildable from the stream.
- **Insights and valuation.** Price ratings, days-to-sell forecasts and demand data, served from the vertical capabilities described in [Same Platform, Different Physics: How Listing Verticals Differ](#vertical-requirements) (vehicle price rating at Motorvane, Valuo at Hearthly).

{id: professional-seller-tooling--inventory-operations-show-the-professional-what-the-pipeline-did}
### Inventory operations: show the professional what the pipeline did

Most professional inventory arrives by feed, so the most valuable inventory tool is often not an editor but a **mirror of the ingestion pipeline**: which records arrived, which were rejected and why, which are waiting for images, which are live and which were removed. The productscape model's partner persona fears "opaque moderation or validation failures"; mobile.de's API returns errors as stable keys with arguments; Autotrader's developer portal documents validation errors such as a vehicle rejected because the UK Driver and Vehicle Licensing Agency (DVLA) classifies it as a category A or B write-off ([Autotrader Connect](https://developers.autotrader.co.uk/), n.d.). [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion) owns the feed contract and error reports. The pro tooling's job is to make that report readable by a sales manager, not only by an integration engineer, because the manager is the one who notices that a car is missing. Feed Roulette is a tooling failure as much as an ingestion failure.

Bulk operations follow the same rule. A bulk price change of 200 cars is a batch of commands against the listing service, executed asynchronously, with a job record the professional can inspect. It is not a direct write by the workspace into a listing table.

{id: professional-seller-tooling--performance-and-roi-one-event-stream-three-consumers}
### Performance and ROI: one event stream, three consumers

The professional, the sales team and billing must see the same numbers. That is only possible if **statistics, leads and delivery records are derived from the same events with the same identifiers**: listing ID, organization and branch, lead ID, buyer-deduplication key and the paid product that was active at the time. [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements) requires delivery records ("what was sold versus delivered") for every paid product; the pro statistics page should be a view over those same records, so that a "Top listing" bought on Monday shows the impressions it actually produced.

![One event stream with shared identifiers feeds the dealer's dashboard, the sales team and billing, which all show the same chart; a faded inset shows nightly copies that disagree.](listing-systems-architecture/posts/17-professional-seller-tooling/assets/images/17-professional-seller-tooling/one-stream-three-consumers.jpeg)

**Figure 3:** *Statistics, leads and delivery records derived from one event stream with the same identifiers let the professional, the sales team and billing see the same numbers.*

Three design rules follow.

1. **Count leads after deduplication, and show the raw contacts beside them.** Hiding the deduplication makes the marketplace look generous; showing both makes the rule auditable.
2. **Separate observed facts from estimates.** Views and leads are observed. "Sales attributed to Motorvane" is an estimate, unless the professional's system confirms the sale. Label estimates as such, and show the method.
3. **Do not compare packages naively.** As the OLX case shows, professionals self-select into packages. A tool that tells a dealer "premium listings perform worse" because premium was bought for hard-to-sell cars will cost the marketplace revenue and credibility. Comparative claims need matching or experiments; [Testing a Two-Sided Market: Experimentation Platforms](#experimentation) owns the methods.

{id: professional-seller-tooling--lead-management-inbox-inside-export-outside}
### Lead management: inbox inside, export outside

Professionals split into two groups: those who work leads in the portal's inbox and those who work them in their own CRM. The architecture must serve both with the same lead object.

- **Inside**, the inbox is a view over the lead ledger and the conversation store, with assignment rules that follow the organization hierarchy, reply assistance and response-time tracking. mobile.de's 2026 update adds AI reply suggestions, a WhatsApp channel tied to the listing and an AI phone assistant; in the pilot, 91% of answered calls came outside opening hours and one in three became a qualified lead ([mobile.de newsroom](https://newsroom.mobile.de/plattform-update-sommer-2026/), July 2026).
- **Outside**, a Lead API and webhooks deliver every lead, from every channel, with its stable identifier, to the professional's CRM. mobile.de describes its Lead API as transferring leads "directly and securely into existing CRM systems". Autotrader publishes Messages, Calls and Deals APIs for the same purpose ([Autotrader Connect](https://developers.autotrader.co.uk/)).
- **Back**, an outcome channel lets the CRM or DMS report qualification, appointments and sales. For vehicles, the VIN makes this unusually reliable: a sale recorded in the dealer's DMS can be matched to the listing and its leads without asking anyone to fill in a form. For property, the return path depends on the agency's software and on consent.

Lead data is personal data about the buyer. When the lead is exported, the professional becomes responsible for it in its own systems; the marketplace must know which leads were exported to which integration and under which terms, so that erasure requests and complaints can be handled. Autotrader's "Buying Signals" model, which scores enquiry intent from "verified but anonymised sales transactions and consumer interactions" ([Autotrader FY2026 results](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf)), shows the direction: the lead object will carry model outputs, which then become part of what is exported and must be explainable.

{id: professional-seller-tooling--pricing-and-market-insight-a-control-loop-not-a-widget}
### Pricing and market insight: a control loop, not a widget

Price tools turn the marketplace's market data into pricing advice for each professional. CarGurus tells dealers the smallest price cut needed to reach the next deal-rating band ("Next Best Deal Rating") and sells PriceVantage, ML pricing software that uses "VIN-level activity, turn-time predictions, lead potential, market days' supply" ([CarGurus 10-K](https://www.sec.gov/Archives/edgar/data/1494259/000119312526059435/carg-20251231.htm), filed February 2026). Autotrader's API computes a "price adjusted days to sell" for a proposed price ([Autotrader Connect](https://developers.autotrader.co.uk/)). mobile.de's Preis-Planer links price steps explicitly to search position.

Two architectural consequences follow; both are my inference from the published designs. First, **these tools create a feedback loop**: when dealers price to band boundaries, the market distribution the model learns from shifts, so the valuation owner must monitor clustering at band edges. Second, **the insight is computed from all professionals' data and shown to each one**. That is legitimate and valuable, but it is also exactly the kind of aggregated data whose access the EU's Platform-to-Business Regulation asks portals to describe (see below). The insight service should know, for every output, which population it was computed from and which access rule applies.

{id: professional-seller-tooling--team-branches-and-permissions}
### Team, branches and permissions

Professional accounts are hierarchies: a legal entity, brands, branches, users and integrations. [Private Sellers, Dealers and Agencies: Modeling Who Lists](#sellers-and-accounts) owns the model; the pro tooling is its main consumer and enforces three rules: **listings and leads belong to the organization, not to the salesperson**, so a departing employee's inbox is reassigned rather than lost; **permissions are scoped to branch and capability**, so the Lyon branch of Agence Rhône Habitat cannot reprice the Villeurbanne branch's listings; and **integrations are principals**, with their own scopes and audit trail. The OAuth 2.0 Security Best Current Practice (RFC 9700, January 2025) gives the baseline for partner tokens: authorization code with Proof Key for Code Exchange (PKCE) for third-party tools acting for a professional, no password grant, and sender-constrained or rotated refresh tokens ([RFC 9700](https://www.rfc-editor.org/rfc/rfc9700.html), January 2025).

{id: professional-seller-tooling--the-partner-api-as-a-product}
### The partner API as a product

For many professionals the marketplace's own UI is secondary. Autotrader reports that its data is "integrated with over 220 technology partners", with an average of **155 million** calls a month on its technology and data services, up from 91 million a year earlier ([Autotrader FY2026 results](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf), May 2026). Its developer portal announces breaking changes at least 30 days ahead and defines what counts as breaking ([Autotrader Connect](https://developers.autotrader.co.uk/)). Rightmove's feed gives each software provider a network identifier and each agent office a branch identifier, and authenticates with Rightmove-issued client certificates ([Rightmove RTDF](https://media.rightmove.co.uk/ps/pdf/guides/adf/Rightmove_Real_Time_Datafeed_Specification.pdf)).

My judgement is that **the pro API is a product with its own customers**: software vendors. It needs versioning and deprecation rules, a sandbox, certification, per-integration rate limits and its own reliability objectives. The Bundeskartellamt's October 2026 decision clearing mobile.de's acquisition of Carwow's German business noted that dealers multi-home and that "many platforms offer dealers data export to other platforms" ([Bundeskartellamt](https://www.bundeskartellamt.de/SharedDocs/Meldung/DE/Pressemitteilungen/2026/10_08_2026_mobile_carwow.html), October 2026). In feed-driven verticals inventory is not exclusive, so the quality of the integration surface is part of what makes a professional choose one portal's workflow over another's.

{id: professional-seller-tooling--neutrality-by-design-when-the-group-sells-the-crm}
## Neutrality by Design: When the Group Sells the CRM

{id: professional-seller-tooling--what-the-law-already-asks}
### What the law already asks

The EU's Platform-to-Business (P2B) Regulation, (EU) 2019/1150, has applied to online intermediation services since 12 July 2020. Two of its articles bear directly on a group that sells pro SaaS. **Article 7** requires a description of "any differentiated treatment which they give, or might give" to goods or services offered by the provider itself or "any business users which that provider controls" compared with other business users, covering access to data, ranking, remuneration and "technical interfaces" ([Regulation (EU) 2019/1150, Art. 7](https://www.legislation.gov.uk/eur/2019/1150/article/7/adopted)). **Article 9** requires a description of the technical and contractual access to data that business users and consumers provide or generate, including whether the provider has access, whether business users have access "including in aggregated form", and whether data is provided to third parties ([Regulation (EU) 2019/1150, Art. 9](https://www.legislation.gov.uk/eur/2019/1150/article/9/adopted)). The European Commission proposed repealing the regulation in November 2025, citing overlap with the Digital Services Act and Digital Markets Act; as of October 2026 that is a proposal ([European Commission](https://digital-strategy.ec.europa.eu/en/policies/platform-business-trading-practices), updated July 2026).

Whatever happens to the regulation, its articles describe the questions a neutral design must answer. **Can the portal see the CRM's data? Does the CRM get better interfaces to the portal than its competitors? Does the portal's ranking treat the CRM's listings differently?** A design that cannot answer each with evidence is not neutral, whatever its policy says.

{id: professional-seller-tooling--the-four-controls}
### The four controls

Neutrality is enforceable when it rests on four architectural controls, each of which produces evidence.

| Control | What it means | Evidence it produces |
| --- | --- | --- |
| **Separate tenancy** | The SaaS runs in its own accounts, identity realm and data stores; no portal service has credentials to them | Infrastructure inventory; access-policy exports; quarterly access reviews |
| **API parity** | The SaaS publishes to the group's portal through the same public feed API, with the same fields, limits and service levels as any other vendor | Contract tests run against the public API; integration configuration diff; support-ticket SLAs by vendor |
| **Data boundary** | Data flows from the SaaS to the portal only as the listing payloads the agency chose to publish; data from the portal to the SaaS only through the public lead and performance APIs available to every vendor | Data-flow inventory; data-catalog tags on every dataset; egress logs |
| **Ranking blindness** | Portal ranking, sales and pricing systems carry no feature that identifies the publishing software | Feature inventories of ranking and sales models; model cards; review of sales-targeting queries |

**Table 2:** *Four controls that turn a neutrality promise into checkable architecture. Each produces evidence an independent reviewer can test.*

The controls cost something. API parity means the group's own CRM cannot ship a portal feature its competitors cannot also use, which slows integration work the product team would like to do. Separate tenancy means duplicate infrastructure and no shared customer database. Those costs are the price of selling software to customers who also buy from the portal's competitors.

{id: professional-seller-tooling--veldmark-worked-example-the-golf-s-23-leads-and-keybridge-s-report}
## Veldmark Worked Example: The Golf's 23 Leads and Keybridge's Report

{id: professional-seller-tooling--reconciling-the-golf}
### Reconciling the Golf

Felix's team reconstructs the Golf's ten days from the three lead systems, as the lead-ledger design in [How Listing Marketplaces Make Money](#monetization-models) proposed. Table 3 shows the result.

| Channel | Contacts in Dealer Hub | After deduplication (one buyer, one listing, 14 days) | Reached the dealer's CRM | Why the CRM count differs |
| --- | --- | --- | --- | --- |
| E-mail and messages | 14 | 14 | 14 | Exported by the nightly e-mail lead export |
| Tracked phone calls | 7 | 4 (three callers had already e-mailed) | 0 | Calls rang the showroom through a tracked number and were never exported |
| Test-drive bookings | 2 | 1 (one booker had already e-mailed) | 0 | Bookings stayed in Dealer Hub's calendar |
| **Total** | **23** | **19** | **14** | |

**Table 3:** *Three counts of the same demand. Dealer Hub reported raw contacts; the dealer's CRM saw only e-mails. Neither number was the number the dealer needed.*

Both sides were wrong, in different directions. Dealer Hub's 23 counted the same buyers more than once. The dealer's 14 missed every phone and booking lead. The honest number was **19 unique buyers**, and one more fact closes the loop: the car's VIN appears in the record of the 29 April sale that Autohaus Ruhrblick's DMS exported the next morning, and the buyer's e-mail address matches one of the 19. The sale can be attributed to a Motorvane lead with evidence, not estimated.

![Two scoreboards, 23 raw contacts in the dealer portal and 14 leads in the dealer's CRM, feed one ledger of 19 unique buyers, one of whom is matched to the car's sale.](listing-systems-architecture/posts/17-professional-seller-tooling/assets/images/17-professional-seller-tooling/golf-three-counts.jpeg)

**Figure 4:** *Dealer Hub's 23 counted some buyers twice and the dealer's 14 missed every call and booking; the honest number was 19 unique buyers, and a VIN match tied the sale to one of them.*

Felix's rebuild becomes four specific changes rather than a new portal.

1. **Dealer Hub's lead view becomes a read model of the lead ledger**, showing raw contacts and deduplicated leads side by side, with the rule stated.
2. **The Lead API and webhooks export all channels**, not only e-mail, each lead with its stable ID, channel and deduplication key. Calls carry duration and a recording consent flag; bookings carry the slot.
3. **A sale-matching feed** lets dealers' DMSs, or their integration vendors, report sales by VIN. Matching is opt-in per dealer and reported back in Dealer Hub as "confirmed sales from Motorvane leads".
4. **Statistics move from the nightly reporting database to the event stream**, so the statistics page, the lead ledger and the package delivery records agree within minutes.

The renewal conversation changes with the numbers. Over the same quarter, Autohaus Ruhrblick's 150 slots produced 1,610 deduplicated leads and, among dealers that opt in to sale matching, about one confirmed sale for every twelve leads; the downgrade is withdrawn. The numbers are illustrative, but the mechanism is not: **the professional renewed because both systems finally told the same story.**

{id: professional-seller-tooling--keybridge-s-portal-performance-report}
### Keybridge's portal performance report

Emma's report is useful to agencies and legitimate for Keybridge. The question is what data it uses and who sees the result. Figure 5 shows the boundary Ingrid's team designs.

![Diagram: Keybridge's neutrality boundary](listing-systems-architecture/posts/17-professional-seller-tooling/assets/images/17-professional-seller-tooling/fig05-keybridge-s-neutrality-boundary-keybridge-publishes.jpeg)

**Figure 5:** *Keybridge's neutrality boundary. Keybridge publishes to Hearthly through the same public API as any other vendor and receives Hearthly's leads and statistics through the same public APIs as everyone else. The portal performance report is computed inside Keybridge, per agency, and shown only to that agency. No Hearthly system can read Keybridge's data.*

The design answers Claire's question: **no**. Hearthly cannot see the cross-portal comparison, aggregated or not, because it is computed from data agencies entrusted to Keybridge, including data from Hearthly's competitors. Hearthly can learn where it underperforms the way any portal can: from its own data, from agency feedback and from public market research. The decision record notes the alternative Claire raised, an "anonymized benchmark" sold to Hearthly, and rejects it. Even anonymized, it would be Keybridge agency data used for Hearthly's sales targeting, which the March decision forbids, and it would undermine Keybridge's position with every agency that multi-lists.

Three implementation details make the boundary auditable.

- **Keybridge is treated as one of Hearthly's roughly 160 software vendors.** It uses the same feed API, the same error reports and the same support queue. A contract test suite, run monthly against the public API with Keybridge's credentials and with a test vendor's credentials, proves that both receive the same fields and limits.
- **Hearthly's data catalog tags every dataset with its origin.** Listings published through Keybridge are tagged as such for operational support only. The ranking feature store and sales tools are barred, by policy checked in their deployment pipelines, from reading that tag.
- **The annual independent review receives a standard evidence pack**: access-policy exports for both clouds, egress logs between Keybridge and Hearthly, the contract-test results, the data-flow inventory and the feature inventories of Hearthly's ranking and sales models. Lucía Ortega, the group's data-protection officer and regulatory lead, owns the pack and the P2B descriptions it supports.

The separate clouds (Keybridge on Azure, Hearthly on Google Cloud) help, but they are not the control. If Veldmark later moves both to AWS, the controls must survive the move, which is why they are written as policies and tests rather than as a consequence of hosting.

{id: professional-seller-tooling--trade-offs-build-integrate-or-own}
## Trade-offs: Build, Integrate or Own

A group decides, per capability, whether to build pro tools itself, to let partners provide them through APIs, or to own a SaaS product that professionals use beyond the portal. Table 4 compares the three.

| Option | What it means | Strengths | Weaknesses | When it is right |
| --- | --- | --- | --- | --- |
| **Build in the portal** | Inbox, statistics, bulk tools and insights in the portal's own workspace | Direct control of the experience; tightly tied to the marketplace's data; differentiates the portal | Competes with professionals' existing software; must match CRM features to be used | Capabilities only the portal can provide: its statistics, its price ratings, its paid products, its leads |
| **Integrate through APIs** | Expose capabilities to the CRMs, DMSs and websites professionals already use | Meets professionals where they work; partners carry feature breadth; scales across verticals | Partners own the daily relationship; the portal's UI is used less; API product costs | Professionals with established software ecosystems, which is most dealers and agencies |
| **Own pro SaaS** | Sell a CRM, DMS or website product to professionals, including for competing portals | Revenue line; presence at the origin of listings; switching costs | Neutrality obligations and their costs; separate product and sales motion; distrust if handled badly | Markets where the group can run the SaaS as a neutral, separately governed business |

**Table 4:** *Three ways to serve professionals. Most groups need the first for portal-specific capabilities and the second for everything else; the third is a separate business with its own rules.*

The rule I use is: **build what only the portal knows, expose everything through the API, and own SaaS only if you are prepared to run it as if a competitor owned the portal.** The middle row is the one most often under-funded. A portal that invests in its own inbox but not in its Lead API ends up with a feature most professionals do not use and a CRM integration they complain about.

Owning SaaS also changes the economics of a group exit. [After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation) and Adevinta's 2024–2026 decentralization ([Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta)) show that businesses sold separately must be separable; a pro SaaS product built with separate tenancy is easier to sell, or to keep, than one entangled with the portal.

{id: professional-seller-tooling--vertical-differences}
## Vertical Differences

Professional tooling varies more across verticals than almost any other capability, because professionals' businesses differ.

| Vertical | The professional | System they already run | What they need most from the portal | Typical tension |
| --- | --- | --- | --- | --- |
| Automotive | Dealer with sales staff, often several sites | DMS and dealer CRM, often from the same vendor | Feed reliability, lead export across channels, price ratings and days-to-sell, sale matching | Platform-controlled states on dealer stock, as with Autotrader's Deal Builder rollout pause in late 2025 |
| Real estate | Agency or network with branches and agents | Agency CRM or transaction software that multi-lists to portals | Seller leads and valuation tools, branch statistics, viewing requests, mandate support | The portal or its parent owning the CRM; agencies withholding supply |
| General classifieds | Shop or small business selling goods | Shop system, sometimes none | Bulk listing, storefront page, simple statistics, paid visibility | Trader obligations: DSA traceability for every professional account |
| Jobs | Employer or recruitment agency | Applicant tracking system | Applicant flow into the ATS, budget and pacing controls, candidate matching | Performance billing disputes over clicks and applications |
| Recommerce | Professional reseller | Inventory spreadsheet or reseller tool | Pro channel with trader status, shipping and payout tools | Separating traders from private sellers; Vinted allows commercial selling only through Vinted Pro |

**Table 5:** *The professional and their existing system decide what the portal must provide. In automotive and real estate, the integration surface matters as much as the portal's own tools.*

In real estate and recommerce, pro tooling does more than save the professional time. In **real estate**, supply acquisition is part of the professional's job, so valuation and seller-lead tools are pro tooling: Rightmove describes its Opportunity Manager as predicting "potential vendors from their usage of the Rightmove platform" ([Rightmove FY2025 results](https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf)). In **recommerce**, Vinted gives the reason it routes commercial sellers into a separate Pro channel: "businesses have legal obligations that private sellers don't" ([Vinted newsroom](https://company.vinted.com/newsroom/qa-commercial-selling), September 2026). Pro tooling there is first a compliance boundary and only then a productivity product.

{id: professional-seller-tooling--failure-modes}
## Failure Modes

**The second system of record.** The pro portal grows its own listing tables, lead tables and statistics database, filled by nightly jobs. Within a year its numbers differ from billing, from the listing service and from the professional's CRM, and nobody can say which is right. Dealer Hub's nightly reporting database was this pattern in early form.

**Statistics that flatter.** Raw contacts reported as leads, views as the headline, estimates shown as facts. The professional's CRM eventually disagrees, and the portal's credibility goes with it. Vanity Liquidity, sold to the customer who pays.

**Leads that stop at the portal's edge.** E-mail leads are exported; calls, bookings and chat are not. The professional undercounts the portal's value and then downgrades, as Autohaus Ruhrblick nearly did.

**Feature gating in the front end.** "Premium statistics" or "AI replies" are switched on by checks of the package name scattered through the workspace code. A package redesign then breaks features in unpredictable ways, and no one can prove which customers received what. Entitlement checks belong in [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements), read through one interface.

**An API treated as a side project.** Breaking changes without notice, no sandbox, error messages only engineers can read. Partners pass the pain to professionals, and professionals blame the portal. The productscape partner persona's fear is exactly this: "breaking changes disrupting merchant inventory".

**Neutrality by promise.** The group's CRM gets an early-access endpoint "temporarily", a portal analyst gets read access to a CRM dataset "for a one-off analysis", and the ranking model gains a feature that correlates with the publishing software. Each step is small; together they are the end of neutrality, and in the EU they are also differentiated treatment that should have been described.

**Rolling out platform-controlled states without consent.** A "reserved" flag, an automatic price suggestion or an AI agent that answers buyers on the professional's behalf changes how the professional runs their business. Autotrader's own account of pausing Deal Builder's auto-rollout, holding listening sessions and introducing "request a reservation" is the documented reminder ([Autotrader FY2026 results](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf)). Per-organization configuration and reversibility belong in the design.

{id: professional-seller-tooling--the-chief-architect-s-view}
## The Chief Architect's View

At group level, pro tooling raises three decisions that brand teams cannot make alone.

**What to decide.**

- **Which pro capabilities are shared engines and which are brand front ends.** In the language of [Same Platform, Different Physics: How Listing Verticals Differ](#vertical-requirements), the lead ledger, the performance read model, the pro API gateway and the developer portal are layer-2 engines; Dealer Hub and Hearthly's agency workspace are layer-4 products. A group that shares the front end forces one vertical's workflow on another's professionals.
- **The pro API as a governed product**: versioning and deprecation policy, certification, rate limits, service levels and an owner with a roadmap that includes partners.
- **The neutrality regime for any pro SaaS the group owns**: the four controls, the evidence pack, the reviewer and the escalation path when a brand asks for an exception.

**Who decides.** Brand product teams decide their workspaces. The group platform owns the shared engines and the API product. The architecture advice forum decides when a brand asks to bypass an engine or to read data across the neutrality boundary, and its decision records are part of the review evidence. Group legal and the data-protection officer own the P2B descriptions of data access and differentiated treatment.

**What to watch.**

- **Reconciliation gaps.** For a sample of professionals, the difference between portal-reported leads and leads received by their CRM. A gap above a few percent is a defect, not a disagreement.
- **Lead export coverage.** The share of leads, by channel, that reached an integration. Channels below full coverage are where the portal's value disappears.
- **Response time and outcome return.** Median first response per professional, and the share of leads with a reported outcome. The first improves liquidity; the second makes ROI measurable.
- **API health as partners see it.** Error rates by error key, breaking changes announced on time, certification lead time.
- **Neutrality incidents.** Every access request that crosses the SaaS boundary, granted or refused, with the reason.

Professionals increasingly reach marketplaces through software and, from 2025–2026, through AI agents. As of 2026, Autotrader and OLX have shipped apps inside ChatGPT, Rightmove has submitted one, and mobile.de's call assistant answers buyers for dealers. **The pro API will be called by agents acting for professionals as well as by CRMs**, which raises the stakes on scoped authorization, explainable outputs and audit trails. [AI Across the Listing Lifecycle](#ai-in-listing-systems) takes this up.

{id: professional-seller-tooling--questions-to-ask}
## Questions to Ask

1. For a sample of our largest professional customers, do our lead counts match the leads their CRM received, by channel? If not, where do they diverge?
2. Does every lead channel (messages, calls, bookings, chat, reservations) reach the Lead API and webhooks with a stable identifier and a deduplication key?
3. Are our pro statistics, our lead ledger and our paid-product delivery records computed from the same events?
4. Which numbers on our pro dashboards are observed and which are estimates, and does the dashboard say so?
5. Does our pro workspace own any business record that does not exist in a domain service?
6. Can a professional's software do everything our own pro UI can do, through a documented, versioned API?
7. How do we tell partners about breaking changes, and how long is the notice?
8. Where are package and entitlement checks performed in the pro tooling, and could we list every feature a given customer is entitled to?
9. If we own software sold to professionals, which data can the portal see, which interfaces does that software get that competitors do not, and what evidence would prove our answers to an independent reviewer?
10. Which platform-controlled states or automated actions do our tools apply to professionals' inventory or leads, and can each professional switch them off?

{id: professional-seller-tooling--from-supply-to-discovery}
## From Supply to Discovery

This chapter closes Part III. The supply chain is now complete: listings come in through forms and feeds, are normalized and enriched, are recognized when they describe the same thing, are published within a freshness target, and are managed by the professionals who supply most of the value. [Part IV — DISCOVERY: Matching Intent to Inventory](#part-4) turns to the other side of the market: matching buyers' intent to that inventory. Its first chapter, [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture), asks how to build search for millions of short-lived listings with rich filters, and why the index that serves them must never become the system of record.

{id: professional-seller-tooling--sources-and-evidence}
## Sources and Evidence

{id: professional-seller-tooling--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Full year results for the year ended 31 March 2026](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf) — Autotrader Group plc, 2026. Co-Driver, Buying Signals, Deal Builder and its rollout pause, 220 partners and 155 million monthly API calls.
- [Autotrader Connect developer documentation](https://developers.autotrader.co.uk/) — Autotrader, n.d. (accessed 2026). Stock, Messages, Calls and Deals APIs; validation errors; 30-day breaking-change policy; days-to-sell.
- [Seller API documentation](https://services.mobile.de/manual/seller-api.html) — mobile.de, n.d. (accessed 2026). Statistics, listing quality checks, multi-locations, integrator model.
- [Plattform-Update Sommer 2026](https://newsroom.mobile.de/plattform-update-sommer-2026/) — mobile.de, 2026. Lead Manager AI replies, lead-performance report, Lead API, call assistant, Preis-Planer.
- [CarGurus Form 10-K for FY2025](https://www.sec.gov/Archives/edgar/data/1494259/000119312526059435/carg-20251231.htm) — CarGurus, Inc., 2026. Next Best Deal Rating, PriceVantage, account managers and ROI tracking.
- [Cars.com Form 10-K for FY2025](https://www.sec.gov/Archives/edgar/data/1683606/000119312526076546/cars-20251231.htm) — Cars.com Inc., 2026. Dealer websites through Dealer Inspire and D2C Media.
- [Cox Automotive](https://www.coxautoinc.com/) — Cox Automotive, n.d. Marketplace alongside inventory, DMS and CRM software.
- [Rightmove Real Time Datafeed specification v1.4.1](https://media.rightmove.co.uk/ps/pdf/guides/adf/Rightmove_Real_Time_Datafeed_Specification.pdf) — Rightmove, 2023. Network and branch tenancy, certificates, performance and lead calls, paid products through the feed.
- [Rightmove FY2025 results](https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf) — Rightmove plc, 2026. Outcome claims and Opportunity Manager.
- [Zillow Group Form 10-K for FY2025](https://www.sec.gov/Archives/edgar/data/1617640/000161764026000015/z-20251231.htm) — Zillow Group, 2026. Follow Up Boss capabilities.
- [Scout24 preliminary FY2025 results](https://www.scout24.com/media/scout24/Investor_Relations/Berichte_und_Praesentationen/2025/Scout24_Preliminary_IR_News_Q4_FY_2025_results_DE.pdf) — Scout24 SE, 2026. Transaction Enablement revenue including the Propstack CRM.
- [Pros de l'immo : AVIV Group lance Ultimmo](https://www.mysweetimmo.com/2022/11/03/pros-de-limmo-aviv-group-lance-ultimmo-une-offre-pour-capter-vendeurs-et-acheteurs/) — MySweetImmo, 2022 (trade press). Agent offer with estimation and prospecting tools.
- [Correlation lied to us: rethinking product impact with causal inference](https://tech.olx.com/correlation-lied-to-us-rethinking-product-impact-with-causal-inference-5ba47181f7c5) — OLX Tech, 2026. Self-selection into packages and matched estimates.
- [Keeping second-hand at the heart of Vinted](https://company.vinted.com/newsroom/qa-commercial-selling) — Vinted Group, 2026. Commercial selling only through Vinted Pro.

{id: professional-seller-tooling--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Regulation (EU) 2019/1150, Article 7](https://www.legislation.gov.uk/eur/2019/1150/article/7/adopted) — EU text as adopted, 2019. Differentiated treatment of the provider's own services.
- [Regulation (EU) 2019/1150, Article 9](https://www.legislation.gov.uk/eur/2019/1150/article/9/adopted) — EU text as adopted, 2019. Description of data access, including aggregated data.
- [Platform-to-business trading practices](https://digital-strategy.ec.europa.eu/en/policies/platform-business-trading-practices) — European Commission, 2026. Application since July 2020 and the November 2025 repeal proposal.
- [RFC 9700: Best Current Practice for OAuth 2.0 Security](https://www.rfc-editor.org/rfc/rfc9700.html) — IETF, 2025. Baseline for partner tokens.
- [Freigabe: Übernahme Carwow durch mobile.de](https://www.bundeskartellamt.de/SharedDocs/Meldung/DE/Pressemitteilungen/2026/10_08_2026_mobile_carwow.html) — Bundeskartellamt, 2026. Dealer multi-homing and data export as competitive constraints.

{id: professional-seller-tooling--research-and-practitioner-sources}
### Research and practitioner sources

- Productscape domain models for a general listings marketplace and a real-estate marketplace (author's sibling repository, 2026). Professional and integration-partner personas, jobs, fears and partner integration surfaces. Generic models, not descriptions of any company.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
