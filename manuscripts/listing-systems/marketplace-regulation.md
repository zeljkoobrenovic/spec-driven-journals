{id: marketplace-regulation}
# 27. Rules of the Marketplace: DSA, DAC7 and Vertical Regulation

![Rules of the Marketplace: DSA, DAC7 and Vertical Regulation — logo](listing-systems-architecture/posts/27-marketplace-regulation/assets/images/27-marketplace-regulation/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Work out which EU and national rules apply to which parts of a listing marketplace, and why the answer changes when the marketplace adds payments. You will turn the Digital Services Act, the platform-to-business and consumer rules, GDPR, DAC7 seller reporting and vertical disclosure rules into system requirements, and follow Veldmark's statement-of-reasons and DAC7 pipelines from decision to submission.

> **WHY THE BUSINESS CARES:** Fines under the Digital Services Act can reach 6% of worldwide turnover, and consumer-law fines for widespread infringements at least 4% of turnover in the countries concerned. The larger cost is slower: every new rule handled as a one-off project consumes the roadmap, and a feature such as in-platform payment can quietly switch on obligations that nobody budgeted.

> **WHY ARCHITECTS SHOULD CARE:** Regulation now specifies data models, event flows and retention periods: what a decision record must contain, how long trader data may be kept, what must be shown on a listing page, and which numbers must be reproducible a year later. Those requirements cut across insertion, ranking, ads, messaging, payments and data, and they differ by country.

> **KEY POINTS:**
>
> * **The marketplace's features decide which laws apply.** A pure lead-generation classifieds site sits inside some rules (DSA moderation duties, ranking transparency, platform-to-business fairness) and largely outside others (trader traceability as an online marketplace, DAC7). Adding in-platform payment, checkout or shipping moves it inside. Every transaction feature is also a regulatory decision, and should be reviewed as one.
> * **Most obligations ask for the same few artifacts.** One decision record feeds statements of reasons, the Transparency Database, appeals and transparency reports. One trader record serves DSA traceability, platform-to-business duties, consumer disclosures and DAC7. A small set of disclosure surfaces covers ranking, advertising and trader information. Build these once, as components, and treat each law as a view of them.
> * **Compliance by design means evidence by design.** Regulators ask what happened, months later, and expect the same answer twice. Keep an obligation register linked to controls and evidence queries, make every regulated number computable from the event log, express country differences as configuration, and retain each data class for exactly as long as the law requires, then delete it.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Moderation as an Afterthought** — when statements of reasons and transparency reports are built as exporters after the fact, each brand produces different numbers and none can be reproduced.
> * **Multiplier Creep** — paid bumps and top positions that are not labeled and not described in the ranking disclosures are now a consumer-law infringement as well as a relevance problem.
> * **The Copy-Paste Country** — implementing each country's rules in a separate code path multiplies every later change; country differences belong in configuration over shared components.

Until about 2020, regulation reached most classifieds architects as a legal review at the end of a project: a privacy notice, a cookie banner, a clause in the terms. That is no longer possible. The European Union's **Digital Services Act** (DSA), applicable to all platforms since 17 February 2024, specifies what a moderation decision record must contain, how quickly notices must be handled and what must be submitted to a Commission database. **DAC7**, the EU directive on platform seller reporting, specifies a quarterly per-seller aggregation of payments. Consumer law specifies what a search results page must explain about its ranking. Energy-performance law specifies fields on property listings. **The regulation is now partly written in the vocabulary of systems design**, and the architect who waits for legal review will rebuild the same thing four times.

This chapter maps the regulations that shape listing marketplaces and turns them into requirements. It is not legal advice, and it does not replace counsel; national transposition, guidance and case law change the details. It concentrates on the EU, where Veldmark operates, and treats the UK and US rules more briefly for groups with brands there. Its claim is that the obligations look numerous but ask for a small number of architectural artifacts, and that **compliance by design** (building those artifacts as reusable components with evidence built in) is cheaper than compliance by project.

Part V treats trust as a shared platform, and this chapter explains why the law now shapes that platform. The decision record from [Trust and Safety as a Platform](#trust-and-safety-architecture) and the trader record from [Who Is on the Other Side? Identity and Verification](#identity-and-verification) are the artifacts most of these rules ask for, and the labeling and tax rules set here bind the payments, paid products and advertising of Part VI. Neighboring chapters own the machinery this chapter regulates. [Trust and Safety as a Platform](#trust-and-safety-architecture) owns the moderation pipeline, the decision service and enforcement propagation. [Who Is on the Other Side? Identity and Verification](#identity-and-verification) owns identity levels, KYB and the business registry. [Beyond the Contact: Payments, Shipping and Buyer Protection](#transactions-and-payments) owns the payment flows that bring DAC7 into scope, and [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) and [Selling Attention: Display, Native and Retail-Media Advertising](#advertising-platforms) own the systems whose disclosures this chapter specifies. The running example is Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)).

{id: marketplace-regulation--setting-the-scene-at-veldmark-five-exporters-and-one-report}
## Setting the Scene at Veldmark: Five Exporters and One Report

In **February 2027**, Lucía Ortega, Veldmark's Group Data Protection Officer and regulatory lead, had a deadline. Under the Commission's implementing regulation on DSA transparency reports, the first full harmonized reporting period ran from 1 January to 31 December 2026, and reports were due no later than two months after the period ended ([Commission Implementing Regulation (EU) 2024/2835](https://eur-lex.europa.eu/eli/reg_impl/2024/2835/oj)). For Veldmark that meant one report per online platform, Tradeyard, Motorvane and Hearthly, on the Commission's template, by the end of February.

Lucía collected the inputs from five places, because each brand and country produced its own statements of reasons: Yardstick's template for Tradeyard Netherlands and Belgium, two vendor exports for Poland and Portugal, Motorvane's hand-built tool and two Hearthly exporters. The numbers did not agree with themselves. Tradeyard Netherlands had submitted about **20,000** statements of reasons a week to the DSA Transparency Database from listing removals alone, yet its moderation log counted removals differently: an edit that was rejected and then accepted counted once in one system and twice in the other. Motorvane counted "dealer listing paused for missing data" as a restriction in one quarter and not in the next. Hearthly Spain had no record of whether its decisions were automated.

Ingrid Halvorsen, who had joined as Group Chief Architect that month, read the draft report and asked two questions. *If the Dutch regulator asks us next year how we got this number, can we produce it again from the same data?* And *what else are we obliged to do that we have not built at all?* Lucía's answer to the first was no. Her answer to the second was a list, which became the obligation register later in this chapter. The shared trust-and-safety platform that went live for Tradeyard Netherlands and Belgium in November 2027 was designed against that list.

{id: marketplace-regulation--concepts-who-is-the-marketplace-in-law}
## Concepts: Who Is the Marketplace in Law?

{id: marketplace-regulation--legal-roles-are-defined-by-features}
### Legal roles are defined by features

EU digital regulation does not regulate "classifieds sites". It regulates roles, defined by what a service does. One marketplace can hold several roles at once, and each role carries its own obligations.

| Role | Defined in | What triggers it | Example at Veldmark |
| --- | --- | --- | --- |
| **Hosting service** | DSA Art. 3 | Storing information provided by users | Every brand; Keybridge too, for agency data |
| **Online platform** | DSA Art. 3 | Hosting that also disseminates user information to the public | Tradeyard, Motorvane, Hearthly |
| **Platform allowing consumers to conclude distance contracts with traders** | DSA Section 4 (Arts. 29–32) | Consumers can contract with traders through the platform | Tradeyard (pro sellers, Safe Deal); arguably Motorvane and Hearthly for trader listings |
| **Very large online platform** | DSA Art. 33 | 45 million or more average monthly active EU recipients, and designation | None (no classifieds marketplace is designated as of October 2026) |
| **Online intermediation service** | P2B Regulation Art. 2 | Lets business users offer to consumers "with a view to facilitating the initiating of direct transactions … irrespective of where those transactions are ultimately concluded" | All three consumer brands, for dealers, agencies and pro sellers |
| **Online marketplace** | Consumer Rights Directive and UCPD, as amended by the Omnibus Directive | Lets consumers conclude distance contracts with traders or consumers | Tradeyard Safe Deal; contestable for lead-only flows |
| **Reporting platform operator** | DAC7 (Directive (EU) 2021/514) | Connects sellers with users for relevant activities, beyond only listing or advertising | Tradeyard, for Safe Deal transactions only |
| **Controller** | GDPR | Determining the purposes and means of processing personal data | Each brand's operating entity |

Sources: [DSA](https://eur-lex.europa.eu/eli/reg/2022/2065/oj); [P2B Regulation (EU) 2019/1150](https://eur-lex.europa.eu/eli/reg/2019/1150/oj); [Omnibus Directive (EU) 2019/2161](https://eur-lex.europa.eu/eli/dir/2019/2161/oj); [DAC7, Council Directive (EU) 2021/514](https://eur-lex.europa.eu/eli/dir/2021/514/oj); the list of designated very large online platforms ([European Commission, updated 15 October 2026](https://digital-strategy.ec.europa.eu/en/policies/list-designated-vlops-and-vloses)).

The table holds the most important architectural fact in this chapter: some definitions explicitly cover **lead generation**, and others turn on a contract concluded through the platform. The platform-to-business (P2B) Regulation applies "irrespective of where those transactions are ultimately concluded", and the Unfair Commercial Practices Directive's (UCPD) ranking-information rule, inserted by the Omnibus Directive, applies to search results "irrespective of where transactions are ultimately concluded" ([Directive (EU) 2019/2161, Art. 3](https://eur-lex.europa.eu/eli/dir/2019/2161/oj)). The definitions that turn on whether **a contract is concluded through the platform** are the DSA's trader-traceability section, the Consumer Rights Directive's marketplace information duties and, through its definition of "platform", DAC7, which excludes software that "exclusively" allows users "to list or advertise" a relevant activity or processes payments without further intervention ([Council Directive (EU) 2021/514, Annex V, Section I](https://eur-lex.europa.eu/eli/dir/2021/514/oj)).

My working rule as an architect is to **assume the contract-based rules apply to every listing published by a trader**. Whether a pure classifieds listing with a contact button "allows consumers to conclude distance contracts with traders" is a question for counsel, but building trader traceability for dealers and agencies costs little and being wrong costs much. The second part of the rule is to **treat every transaction feature as a perimeter change** that triggers a regulatory review before launch. Safe Deal, shipping labels, deposits, rental applications with payment and online car reservation all qualify.

![A marketplace building with only a contact button in an inner zone, moving across a dashed boundary into an outer zone after adding payment, shipping and checkout modules.](listing-systems-architecture/posts/27-marketplace-regulation/assets/images/27-marketplace-regulation/features-move-the-perimeter.jpeg)

**Figure 1:** *Lead generation sits inside some rules; adding payment, checkout or shipping moves the marketplace across the perimeter into trader traceability, marketplace duties and DAC7, so every transaction feature is also a regulatory decision.*

{id: marketplace-regulation--small-company-exemptions-do-not-help-a-group}
### Small-company exemptions do not help a group

The DSA exempts micro and small enterprises from most online-platform duties and from the marketplace section (Arts. 19 and 29), and the P2B Regulation exempts small enterprises from its complaint-handling system (Art. 11(5)). Both refer to Commission Recommendation 2003/361/EC, whose linked-enterprise rules make a small marketplace owned by a large group part of that group. **A newly acquired local marketplace should be assumed to lose any exemption at acquisition**, and its compliance gap belongs in the integration plan.

{id: marketplace-regulation--the-obligation-the-control-and-the-evidence}
### The obligation, the control and the evidence

Three terms make regulation tractable for architects:

- An **obligation** is a duty stated in a legal source, with an article reference, a jurisdiction and applicability conditions: "DSA Art. 17(1): provide a statement of reasons for any restriction of visibility of a recipient's information, where electronic contact details are known."
- A **control** is the system behavior that meets it: "The decision service emits a statement-of-reasons event for every decision with a visibility, monetary, provision or account restriction."
- **Evidence** is the data that proves the control worked: "For any period, the count of restriction decisions equals the count of statements sent plus the count of documented exceptions, with the query that computes both."

**Compliance by design** is the practice of building controls into the platform's components, with the evidence query written at the same time as the control. **Compliance by project** builds an exporter to satisfy each new obligation. The first is more expensive for the first law and cheaper for every law after it.

{id: marketplace-regulation--the-digital-services-act-as-a-set-of-system-requirements}
## The Digital Services Act as a Set of System Requirements

The DSA is the regulation that most changes listing-system architecture, because it regulates the moderation process itself. The table maps the articles that bind a non-designated online platform with trader listings to the components that implement them. Article text was checked against the Official Journal version of [Regulation (EU) 2022/2065](https://eur-lex.europa.eu/eli/reg/2022/2065/oj).

| Article | Obligation in brief | System requirement | Owning component |
| --- | --- | --- | --- |
| 14 Terms and conditions | Describe content-moderation policies, procedures and tools, "including algorithmic decision-making and human review", in clear language, publicly and in machine-readable form | Policy registry publishes user-facing policy text per brand and country; versioned | Policy registry ([Trust and Safety as a Platform](#trust-and-safety-architecture)) |
| 15 and 24(1) Transparency reports | Annual reports on orders, notices, own-initiative moderation, automated tools with accuracy indicators, complaints, out-of-court disputes and suspensions; Commission templates | All figures computed from decision and notice events, by reporting period, reproducibly | Reporting views over the evidence store |
| 16 Notice and action | Electronic notice mechanism; required notice elements; confirmation of receipt; decision notified with redress options; timely, diligent, non-arbitrary handling; disclose automated means | Notice as an entity with lifecycle and notifier communications | Case management |
| 17 Statement of reasons | Clear, specific reasons to the affected user for removal, disabling, **demotion**, restriction of payments, suspension of service or account; facts, automation, legal or contractual ground, redress | Every restricting decision produces a statement from the decision record | Decision service; statement-of-reasons service |
| 20 and 21 Complaints and disputes | Free, electronic complaints for at least six months after the decision; reversal of unfounded decisions; decided under qualified staff supervision, "not solely on the basis of automated means"; escalation to certified out-of-court bodies | Appeals linked to original decisions; human decision step; evidence kept through the window; case export for dispute bodies | Appeals service |
| 22 Trusted flaggers | Notices from flaggers designated by Digital Services Coordinators get priority | Registry of trusted flaggers from the Commission's database; priority queue; flagger quality metrics | Case management |
| 23 Misuse | Suspend, after a warning, users who frequently post manifestly illegal content, and notifiers who frequently send manifestly unfounded notices | Strike counters per account and notifier; warnings; policy in the terms | Decision service |
| 24(2) Active recipients | Publish average monthly active EU recipients at least every six months | A defined, audited metric from the data platform | [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform) |
| 24(5) Transparency Database | Submit statements of reasons "without undue delay", without personal data | PII-free submission pipeline with idempotency | Statement-of-reasons service |
| 25 Interface design | No interfaces that deceive or manipulate users or impair free and informed decisions | Design review for flows such as cancellation, consent and upsell | Product design governance |
| 26 Advertising | Mark each ad in real time; show on whose behalf it is presented and who paid; meaningful information on targeting parameters; no profiling ads based on special-category data | Paid placements, including sponsored listings, carry labels and "why am I seeing this" | [Selling Attention: Display, Native and Retail-Media Advertising](#advertising-platforms); listing rendering |
| 27 Recommender transparency | Main parameters of recommender systems and options to change them, in the terms | Ranking and recommendation parameter documentation per surface; user-selectable sort options | [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking), [Recommendations for Inventory That Disappears](#recommendations) |
| 30 Trader traceability | Collect and check trader identity, ID or electronic identification, payment account, register number and self-certification before trading; correct or suspend; keep six months after the relationship ends, then delete; display name, address, contact, register and self-certification to users | Business registry with checks and lifecycle deletion; trader panel on listings | [Who Is on the Other Side? Identity and Verification](#identity-and-verification) |
| 31 Compliance by design | Interface lets traders provide product identification, trader marks, and labeling and product-safety information; best efforts to check before offers go live; reasonable efforts at random checks against official databases | Listing schema fields for safety and labeling; random-check job | [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas); trust and safety |
| 32 Right to information | When an illegal product or service was sold, inform consumers who bought it in the last six months, or publish a notice | Record which consumers bought or contacted per listing; notification job | Payments and messaging |

Three entries in the table catch ranking, payments and seller-data teams by surprise.

**Demotion is a restriction.** Article 17 lists "demoting content" among the restrictions that need a statement of reasons, and the Transparency Database has a decision value for it, `DECISION_VISIBILITY_CONTENT_DEMOTED` ([DSA Transparency Database API documentation](https://transparency.dsa.ec.europa.eu/page/api-documentation)). A ranking feature that quietly pushes suspected scam listings down the results is a moderation decision. [Trust and Safety as a Platform](#trust-and-safety-architecture) puts such demotions behind the decision service for that reason.

**Payment holds are restrictions too.** "Suspension, termination or other restriction of monetary payments" is in the same list. A Safe Deal payout held by fraud rules is a decision that needs a statement of reasons, unless it falls under a different legal regime the platform can name.

**Trader traceability is a data lifecycle, not a form.** Article 30 requires the platform to store the trader information "for a period of six months after the end of the contractual relationship" and then to delete it ([Regulation (EU) 2022/2065, Art. 30(5)](https://eur-lex.europa.eu/eli/reg/2022/2065/oj)). That is a deletion obligation with a trigger (the relationship ends) and a timer, and it conflicts with any team that keeps dealer documents "just in case".

{id: marketplace-regulation--the-statement-of-reasons-as-a-data-contract}
### The statement of reasons as a data contract

The Commission's Transparency Database is the most concrete regulatory interface a classifieds architect will build against. Its API accepts single statements or batches of up to **100** per call, and a batch fails as a whole if any statement fails validation. Required fields include the decision ground, content type, category, content and application dates, the facts relied on, the source of the decision, whether detection and decision were automated, the territorial scope and a **platform unique identifier** (`puid`) of up to 500 characters, and at least one restriction field. The vocabulary is fixed: restriction values such as `DECISION_VISIBILITY_CONTENT_REMOVED` or `DECISION_ACCOUNT_SUSPENDED`; grounds `DECISION_GROUND_ILLEGAL_CONTENT` or `DECISION_GROUND_INCOMPATIBLE_CONTENT`; sources from `SOURCE_ARTICLE_16` to `SOURCE_VOLUNTARY`; automation from `AUTOMATED_DECISION_FULLY` to `AUTOMATED_DECISION_NOT_AUTOMATED`; and 16 categories, among them `STATEMENT_CATEGORY_SCAMS_AND_FRAUD` and `STATEMENT_CATEGORY_UNSAFE_AND_PROHIBITED_PRODUCTS` ([DSA Transparency Database API documentation, n.d.](https://transparency.dsa.ec.europa.eu/page/api-documentation)). Submissions must not contain personal data (DSA Art. 24(5)).

The database operates at scale: for the 180 days to 19 October 2026, the database held about **4.4 billion** statements from 375 platforms, 41% of them fully automated decisions ([DSA Transparency Database](https://transparency.dsa.ec.europa.eu/), accessed 19 October 2026).

> **INFERENCE, NOT DOCUMENTED:** The database's schema is, in effect, a regulator-defined moderation event model. A platform whose internal decision record cannot be mapped field by field onto it will end up maintaining a translation layer that loses information. The cheaper design is to adopt the regulatory vocabulary for the fields it covers and extend it for internal needs.

Veldmark's decision record, owned by the shared trust-and-safety platform, maps to the statement as follows:

| Decision record field (internal) | Statement field (Transparency Database) | Transformation |
| --- | --- | --- |
| `decision_id` | `puid` | Identity; the idempotency key for resubmission |
| `action` (remove, disable, demote, label, hold payout, suspend account) | `decision_visibility`, `decision_monetary`, `decision_provision`, `decision_account` | Mapping table, one action to one or more values |
| `policy_id` and `policy_version` | `incompatible_content_ground` or `illegal_content_legal_ground` | Policy registry supplies ground text per language |
| `reason_facts` (templated, may contain names) | `decision_facts` | PII stripping: names, phone numbers, addresses, IBANs removed or generalized |
| `source` (user notice, trusted flagger, detector, sample) | `source_type` | Mapping |
| `detected_by` and `decided_by` | `automated_detection`, `automated_decision` | Derived from detector and reviewer fields |
| `territorial_scope` | `territorial_scope` | Country overlay of the policy |
| `seller_type` | `account_type` | `ACCOUNT_TYPE_BUSINESS` or `ACCOUNT_TYPE_PRIVATE`, from trader status |
| `content_created_at`, `applied_at` | `content_date`, `application_date` | Dates |

{id: marketplace-regulation--veldmark-s-statement-of-reasons-pipeline}
### Veldmark's statement-of-reasons pipeline

The pipeline that replaced the five exporters has four stages (look up the ground text, send the user's statement and store it as evidence, strip personal data, submit in batches keyed by decision ID), and one rule: **the user's statement and the database submission are two views of one decision, generated from the same record.**

![Diagram: One decision, two statements](listing-systems-architecture/posts/27-marketplace-regulation/assets/images/27-marketplace-regulation/fig02-one-decision-two-statements-user-receives.jpeg)

**Figure 2:** *One decision, two statements. The user receives the full statement with redress options; the Commission's database receives a version stripped of personal data, batched and keyed by the decision ID, so retries never create duplicates and every submission can be traced back to its decision.*

Throughput is not the hard part. In 2027 Veldmark's three consumer platforms generated about **61,000** restricting decisions a week: listing removals and demotions, message withholdings, payout holds and account suspensions, with Tradeyard Netherlands' roughly 20,000 weekly listing removals the largest single source. At 100 statements per batch that is only about 610 API calls a week. Three other things are hard:

1. **Atomic batch failure.** One malformed statement fails 99 good ones. Veldmark validates every statement against the published schema before batching and quarantines failures for repair, so a template bug in one country does not stall the others.
2. **Personal data in free text.** Reviewers' notes and templated facts contain names, phone numbers and addresses. The stripper combines pattern detection for phone numbers, e-mail addresses, IBANs and postcodes with a rule that `decision_facts` may only be assembled from policy-registry templates and structured fields, never from free reviewer text.
3. **Exceptions are decisions too.** The DSA does not require a statement where the platform has no electronic contact details for the user, or for "deceptive high-volume commercial content" ([Regulation (EU) 2022/2065, Art. 17(2)](https://eur-lex.europa.eu/eli/reg/2022/2065/oj)). Veldmark's policy registry defines which bot-flood rejections count as the second case, and the decision record stores the exception and its reason, so the count of decisions still reconciles with the count of statements.

One decision shows both views. At 20:26 on Sunday 7 March 2027, Tradeyard Netherlands suspended the account that had sent Femke a fake Safe Deal payment link (the incident is told in [Trust and Safety as a Platform](#trust-and-safety-architecture)). Under the 2027 pipeline, the decision record carries `action = suspend_account`, policy `POL-FRAUD-PAYLINK` version 2, source "user report under the terms", detection not automated, decision partly automated (an analyst confirmed a rule hit), scope NL. The account holder receives a statement in Dutch citing the contractual ground and the complaint route. The database receives `DECISION_ACCOUNT_SUSPENDED`, `DECISION_GROUND_INCOMPATIBLE_CONTENT`, `STATEMENT_CATEGORY_SCAMS_AND_FRAUD`, `SOURCE_TYPE_OTHER_NOTIFICATION`, `AUTOMATED_DECISION_PARTIALLY`, territorial scope `NL`, and facts that describe "a message containing a link to a website imitating the platform's payment service", with no domain name, user name or phone number. The domain, the message and the analyst's identity stay in the evidence store, where an appeal, a police request or a regulator can reach them.

{id: marketplace-regulation--transparency-reports-from-the-event-log}
### Transparency reports from the event log

The implementing regulation fixes the reporting period for non-designated platforms at the calendar year, requires publication within two months of its end, and requires the reports to stay publicly available for at least five years ([Commission Implementing Regulation (EU) 2024/2835, Arts. 2 and 3](https://eur-lex.europa.eu/eli/reg_impl/2024/2835/oj)). Its templates ask, among much else, for counts of notices by category and by trusted flaggers, actions by legal and contractual basis, median times, complaints and reversals, and a qualitative description of automated tools with indicators of their accuracy.

The rule I would apply is that **every number in a regulatory report is a saved query over immutable events**, versioned with the report. Veldmark's report for 2027, published in February 2028, was the first produced this way: the evidence store held decision, notice, complaint and enforcement events with their policy and model versions, and each template cell was generated by a named query whose definition was published internally with the report. The answer to Ingrid's February question changed from "no" to "yes, here is the query and the snapshot it ran on".

![Five mismatched exporters pouring ill-fitting pieces onto one report, contrasted with one event log feeding a saved query that produces two identical reports.](listing-systems-architecture/posts/27-marketplace-regulation/assets/images/27-marketplace-regulation/five-exporters-versus-one-log.jpeg)

**Figure 3:** *In February 2027 five exporters produced numbers that did not agree; computed as saved queries over one event log, the 2027 report gives the same answer every time it is run.*

{id: marketplace-regulation--ranking-advertising-and-consumer-transparency}
## Ranking, Advertising and Consumer Transparency

Four overlapping sources regulate how a marketplace orders and labels what users see. Read together, they ask for three disclosure surfaces.

| Source | What it requires | Who it protects |
| --- | --- | --- |
| P2B Regulation Art. 5 | In the terms for business users: the main ranking parameters and the reasons for their relative importance; where business users can influence ranking against payment, a description of those possibilities and their effects; no obligation to disclose algorithms or information that would enable manipulation | Dealers, agencies, pro sellers |
| UCPD Art. 7(4a) (Omnibus) | For search results from different traders or consumers, general information on the main ranking parameters and their relative importance, in a section directly reachable from the results page, "irrespective of where transactions are ultimately concluded" | Consumers |
| UCPD Annex I, point 11a (Omnibus) | Blacklisted: search results that do not clearly disclose paid advertising or payment specifically for higher ranking | Consumers |
| DSA Arts. 26 and 27 | Real-time ad labels with advertiser, payer and targeting information; recommender parameters and options in the terms | All users |
| Consumer Rights Directive Art. 6a (Omnibus) | On online marketplaces, before a consumer is bound: ranking parameters; whether the seller is a trader, based on the seller's declaration; that consumer rights do not apply if not; how obligations are split | Consumers in marketplace contracts |

Sources: [Regulation (EU) 2019/1150](https://eur-lex.europa.eu/eli/reg/2019/1150/oj); [Directive (EU) 2019/2161](https://eur-lex.europa.eu/eli/dir/2019/2161/oj); [Regulation (EU) 2022/2065](https://eur-lex.europa.eu/eli/reg/2022/2065/oj).

The three surfaces that satisfy these rules are:

1. **A ranking explanation** per search surface and sort option, in consumer language, reachable from the results page, generated from the same parameter documentation that the ranking team maintains, and a longer business-user version in the professional terms. It must say how paid products (bumps, top positions, depth products) affect order. [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) owns the parameters; this chapter owns the obligation that they be described.
2. **Labels on every paid placement**: sponsored listings, top-ad slots, highlighted listings that are boosted, and display ads, each with "on whose behalf" and "why am I seeing this". Whether a private seller's €4.99 bump is an "advertisement" in the DSA sense is a question for counsel. Under the UCPD blacklist, an undisclosed paid ranking boost is unlawful either way, so Veldmark labels every paid boost. That is also the strongest structural defense against **Multiplier Creep**: a boost that must be labeled is a boost someone has to justify.
3. **Seller status on every listing**: private or trader, from the seller's declaration, with the trader information panel that DSA Art. 30(7) requires for traders and the consumer-rights notice that CRD Art. 6a requires on marketplaces. One field, set at account level and confirmed per listing, drives all three. [Private Sellers, Dealers and Agencies: Modeling Who Lists](#sellers-and-accounts) owns trader status.

The P2B Regulation adds two process rules for business users that belong in the professional-seller platform. Changes to the terms must be notified at least 15 days before they apply, and terminating a business user's whole service requires a statement of reasons at least 30 days in advance, except for repeated infringements or legal obligations ([Regulation (EU) 2019/1150, Arts. 3 and 4](https://eur-lex.europa.eu/eli/reg/2019/1150/oj)). For Motorvane, terminating a dealer for unpaid invoices is therefore a workflow with a notice timer, not a switch an account manager flips. In November 2025 the Commission proposed repealing the P2B Regulation, citing its overlap with the DSA and the Digital Markets Act, and says its ranking guidelines would remain in application ([European Commission, updated 2 July 2026](https://digital-strategy.ec.europa.eu/en/policies/platform-business-trading-practices)). Until the repeal is adopted, the rules apply, and the same capabilities are needed for the DSA anyway.

{id: marketplace-regulation--price-reductions-and-reviews}
### Price reductions and reviews

Two Omnibus rules reach listing features that rarely get legal review.

**Price-reduction announcements.** The Omnibus Directive inserted into the Price Indication Directive a rule that any announcement of a price reduction must show the prior price, meaning the lowest price the trader applied in a period of at least 30 days before the reduction ([Directive (EU) 2019/2161, Art. 2](https://eur-lex.europa.eu/eli/dir/2019/2161/oj)). The obligation is the trader's, and Member States may set different periods. A portal that automatically shows "price reduced" badges on dealer listings is presenting that announcement on the trader's behalf. When the Essen Volkswagen Golf's price fell from **€21,900** to **€21,400** on Thursday 22 April 2027, Motorvane's badge needed the lowest price in the previous 30 days from the listing's price history, not the immediately preceding price. The difference matters only for a dealer who raises a price briefly before "cutting" it, which is exactly the case the rule exists for. The price history in [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate) has to keep every price with its effective time for this reason.

**Consumer reviews.** Where a trader gives access to consumer reviews, the UCPD treats as material whether and how it ensures that reviews come from consumers who actually used or bought the product, and blacklists claiming that reviews are genuine without "reasonable and proportionate steps" to check, as well as submitting or commissioning fake reviews ([Directive (EU) 2019/2161, Art. 3](https://eur-lex.europa.eu/eli/dir/2019/2161/oj)). FINN shows one documented design: ratings between buyer and seller are given after a deal, and both sides' ratings are published at the same time, or after three weeks, so neither party sees the other's rating before giving its own ([FINN help center, 2024, updated 2026](https://hjelpesenter.finn.no/hc/no/articles/22650860254994-Vurderinger-mellom-Kj%C3%B8per-og-Selger-p%C3%A5-FINN-no)). Veldmark ties Tradeyard ratings to a completed Safe Deal or a conversation with a confirmed handover, and logs the check as evidence of the steps taken.

{id: marketplace-regulation--gdpr-retention-minimization-and-address-privacy}
## GDPR: Retention, Minimization and Address Privacy

For listing systems, three principles of the General Data Protection Regulation (GDPR) produce the most architecture: **data minimization** (personal data "limited to what is necessary"), **storage limitation**, and **accountability**, the duty to be able to demonstrate compliance ([Regulation (EU) 2016/679, Art. 5](https://eur-lex.europa.eu/eli/reg/2016/679/oj)).

The design that works is **retention per data class**, because other laws require keeping data the GDPR would have the platform delete, while fraud prevention wants to keep it longer still. The GDPR's recitals recognize processing "strictly necessary for the purposes of preventing fraud" as a legitimate interest (recital 47), which supports fraud retention but does not make it unlimited. Each class gets a stated legal basis, a trigger and a timer, enforced by deletion jobs whose runs are themselves logged.

| Data class (Veldmark) | Legal driver | Trigger and retention | Notes |
| --- | --- | --- | --- |
| DSA trader-traceability data | DSA Art. 30(5) | Six months after the trader relationship ends, then delete | Deletion is mandatory, not optional |
| Moderation evidence (content snapshot, rule and model versions, reviewer) | DSA Arts. 17, 20 and 21; defense of claims | At least six months after the user is informed (complaint window), extended while an appeal, out-of-court dispute or legal claim is open | Default 12 months at Veldmark |
| Hashed block-list identifiers for accounts terminated for fraud | GDPR legitimate interest (fraud prevention), DPIA | Two years (Veldmark policy, see [Trust and Safety as a Platform](#trust-and-safety-architecture)) | Hashes and decision references only |
| DAC7 seller data and reports | DAC7 and national transposition | National record-keeping periods apply; typically years, not months | Separate, purpose-bound tax profile |
| Messages | Contract, fraud prevention | Per brand policy; shorter for content, longer for metadata linked to fraud cases | [From Interest to Contact: Messaging and Lead Management](#messaging-and-leads) |

Two GDPR issues are specific to listing marketplaces. **Address privacy**: an exact address on a private seller's or landlord's listing exposes where valuables or empty homes are. Show a postcode area or a jittered map pin for private sellers by default ([Where Is It? Location, Geocoding and Privacy](#location-and-geo) owns precision rules). For traders, DSA Art. 30(7) requires the trader's address to be shown, which is uncomfortable for sole traders working from home; the US INFORM Consumers Act has an explicit home-address exception for some sellers, but I found no equivalent in Art. 30. **Automated decisions**: an automated account suspension can be a decision that "similarly significantly affects" a person under GDPR Art. 22, which then requires safeguards including human intervention and the right to contest. The DSA's appeal process provides much of that, and the two should be designed as one mechanism.

{id: marketplace-regulation--dac7-when-payments-turn-a-marketplace-into-a-tax-reporter}
## DAC7: When Payments Turn a Marketplace into a Tax Reporter

{id: marketplace-regulation--what-dac7-requires}
### What DAC7 requires

DAC7 extended the EU's directive on administrative cooperation in tax to digital platforms. A **reporting platform operator** must collect information on its sellers, verify it, and report it to the tax authority each year; the authorities exchange it with the sellers' Member States of residence. The key definitions, from Annex V of [Council Directive (EU) 2021/514](https://eur-lex.europa.eu/eli/dir/2021/514/oj):

- **Relevant activities** are the rental of immovable property (including parking spaces), personal services, the **sale of goods**, and the rental of any mode of transport, carried out for consideration.
- **Consideration** is compensation "net of any fees, commissions or taxes withheld or charged by the Reporting Platform Operator" that is paid or credited to a seller, "the amount of which is known or reasonably knowable by the Platform Operator".
- An **excluded seller** includes one for which the operator facilitated **fewer than 30** sales of goods **and** total consideration of **not more than €2,000** in the period. Both conditions must hold, and the exclusion applies to goods only. Large-scale property rental entities (more than 2,000 rentals of one property listing) and listed companies are also excluded.
- For each reportable seller the operator reports identity (name, primary address, tax identification number with the issuing Member State, date of birth for individuals, VAT and business registration numbers where they exist), the financial account identifier where available, and **per quarter** the total consideration, the number of relevant activities, and the fees, commissions or taxes withheld or charged.
- Due diligence must be completed by **31 December** of the reportable period, and the report submitted by **31 January** of the following year. The first reportable period was 2023; sellers already registered on 1 January 2023 had until the end of the second period.

The definition of "platform" carries the exclusion that matters most for classifieds: it does not include software that, "without any further intervention in carrying out a Relevant Activity", exclusively processes payments, lets users list or advertise, or redirects users to a platform. A classifieds site that only lists is outside DAC7. A classifieds site that collects the price and pays the seller knows the consideration, and is inside.

{id: marketplace-regulation--veldmark-s-dac7-pipeline}
### Veldmark's DAC7 pipeline

Tradeyard Safe Deal brought Veldmark into DAC7. Motorvane and Hearthly only list and advertise, and Hearthly's rental services (tenant application files) do not collect or pay rent, so neither is a reporting platform operator for its classifieds. Veldmark contracts Safe Deal through Tradeyard B.V., a Dutch entity, for all three Safe Deal countries, so Tradeyard reports to the Dutch tax administration for sellers in the Netherlands, Belgium and Poland, and the authorities exchange the data onward.

The 2026 figures show why DAC7 is mostly a filtering problem. Safe Deal processed **11.6 million** transactions with a GMV of about **€1.02 billion** in 2026. Veldmark's planning estimates for the reportable population were:

| Quantity (Safe Deal, 2026) | Estimate |
| --- | --- |
| Distinct sellers paid through Safe Deal | about 1.3 million |
| Sellers with 30 or more sales, or consideration above €2,000 | about 21,000 |
| Of which with complete, validated tax identification number and date of birth by 30 November | about 17,500 |
| Reminder cycles needed for the rest | two, plus payout holds for non-responders as the terms allow |

The buyer protection fee is charged to the buyer, not withheld from the seller, so it does not reduce consideration. Femke's city bike is a useful edge case. She sold it for **€225** on Monday 8 March 2027, and the buyer paid the **€11.95** fee on top. Her consideration is €225, and with one sale in the year she is an excluded seller. If she sold 30 items through Safe Deal in 2027, even small ones, she would become reportable, and Tradeyard would need her tax identification number before 31 December.

![Diagram: Veldmark's DAC7 pipeline](listing-systems-architecture/posts/27-marketplace-regulation/assets/images/27-marketplace-regulation/fig04-veldmark-s-dac7-pipeline-payment-ledger.jpeg)

**Figure 4:** *Veldmark's DAC7 pipeline. The payment ledger provides the quarterly consideration; identity claims and the payment provider supply verified identity and account data; a separate tax profile collects what only tax law needs; the report goes to the tax authority and the same data goes to each seller.*

Three architectural lessons came out of building it. **Aggregate from the ledger, not from orders**, because consideration is what was paid or credited, net of fees, in the quarter it was paid. **Ask early**: the pipeline flags sellers approaching the threshold (20 sales or €1,500) so due diligence starts before the deadline rather than in December. **Keep the tax profile separate**: tax identification numbers and dates of birth are collected for one purpose, under tax law, and must not leak into the general identity claims or the analytics warehouse. [Beyond the Contact: Payments, Shipping and Buyer Protection](#transactions-and-payments) covers the ledger, and RECONCILED's [Payments-to-Ledger: Draining the Suspense Swamp](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/payments-to-ledger.html) covers the accounting integration.

**The decision to launch in-platform payments is also a tax-reporting decision**, outside the EU as well as inside it: under the US INFORM Consumers Act, only sales made through the marketplace with payment processed by it count toward the high-volume seller threshold (below).

{id: marketplace-regulation--vertical-rules-property-and-vehicles}
## Vertical Rules: Property and Vehicles

Horizontal rules govern the marketplace. Vertical rules govern the listing, and they arrive as fields.

{id: marketplace-regulation--energy-performance-in-property-listings}
### Energy performance in property listings

The recast Energy Performance of Buildings Directive requires Member States to ensure that buildings or units offered for sale or rent have an energy performance certificate, and that its energy performance indicator and class are "stated in online and offline advertisements, including in property search portal websites" ([Directive (EU) 2024/1275, Art. 20(4)](https://eur-lex.europa.eu/eli/dir/2024/1275/oj)). Member States had to transpose most of the directive by **29 May 2026**. The recast names property portals explicitly, which removes any argument that the duty belongs only to the advertiser.

France's rules show what national law adds. According to the French government's public-service site, property advertisements must show both the energy class and the climate class of the *diagnostic de performance énergétique* (DPE), must label homes rated F or G as having excessive energy consumption, and must show an estimate of annual energy costs for standard use with the reference year of the energy prices; fines reach €3,000, or €15,000 for a company. Homes rated G may not be newly let since 1 January 2025, with F following in 2028 and E in 2034, and changes to the calculation from 1 January 2026 can move a home's class without any change to the building ([Service-Public.fr, 2026](https://www.service-public.gouv.fr/particuliers/vosdroits/F16096)).

The **Lyon apartment** shows the consequences for Hearthly. The 68 m² T3 in Lyon 7e, listed in May 2027 at **€389,000** with DPE class **D**, arrived through two software vendors and Keybridge. Each feed carried the energy class; one did not carry the climate class and none carried the estimated annual energy cost in a structured field. Hearthly's ingestion therefore applies four rules:

1. **DPE fields are mandatory structured attributes** for French residential listings: energy class, climate class, energy indicator, estimated annual cost range with its reference year, and certificate date.
2. **A missing field blocks publication with feedback to the feed**, rather than publishing an incomplete ad. In May 2027 about 3.8% of Hearthly France's incoming feed listings failed this check, most of them from two vendors whose schemas predated the cost field.
3. **Values carry effective dates**, because a recalculation can change the class. The listing shows the certificate's current value and keeps the history.
4. **Class constrains category**: a G-rated home cannot be published as a new long-term rental in France, so the validator rejects that combination.

**Regulated attributes need an owner who tracks the law**, because the schema will change on the regulator's timetable, not the product team's. [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas) owns the schema mechanics; [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion) owns feed feedback.

{id: marketplace-regulation--vehicle-listings}
### Vehicle listings

Automotive rules are more fragmented, and most apply to dealers rather than to portals. In Germany, the passenger-car energy consumption labeling ordinance (Pkw-EnVKV), which transposes Directive 1999/94/EC, requires manufacturers and dealers who create or use promotional material for **new** passenger cars to state energy consumption, CO2 emissions and the CO2 class, with specific rules for material distributed in electronic form; it was last amended in March 2026 ([Pkw-EnVKV, § 5, as amended 2 March 2026](https://www.gesetze-im-internet.de/pkw-envkv/BJNR103700004.html)). For Motorvane, that means structured fields for new and near-new cars in the dealer feed, validated on ingestion and displayed in the listing, with the same "missing field blocks publication" rule as Hearthly's DPE. The Essen Golf, a 2021 car with 48,000 km, is a used car and outside that rule. Other vehicle duties (mileage, accident history, price inclusiveness) come mostly from national consumer and unfair-competition law and differ by country.

{id: marketplace-regulation--beyond-the-eu-uk-and-us-rules-in-brief}
## Beyond the EU: UK and US Rules in Brief

The UK and US rules differ from the EU's in structure, but they reward the same components. Veldmark operates only in the EU; many groups do not.

| Rule | Scope | Key requirement | Component it reuses |
| --- | --- | --- | --- |
| UK Online Safety Act 2023, illegal-content duties | User-to-user services, including classifieds | Fraud is a priority offence (Schedule 7); risk assessments were due by 16 March 2025 and safety measures apply from 17 March 2025 | Moderation pipeline, risk assessment, evidence |
| UK Online Safety Act, fraudulent-advertising duties | Paid-for ads on categorized services | Prevent, minimize and remove fraudulent paid ads; Ofcom's codes consulted in July–October 2026, final statement expected by mid-2027 | Ad review; whether paid listing upgrades count is an open question for counsel |
| UK Digital Markets, Competition and Consumers Act 2024 | Consumer reviews, from 6 April 2025 | Ban on fake reviews and on hosting reviews without reasonable steps to check they are genuine; the regulator can fine up to 10% of global turnover | Review anchoring and evidence |
| US INFORM Consumers Act | Online marketplaces with high-volume third-party sellers of new or unused consumer products | 200 or more sales and $5,000 or more in 12 months, counting only marketplace-processed sales; collect and verify bank, tax ID and contact information; disclose identity for sellers above $20,000; reporting channel on listings | Business registry, payment ledger |
| US Fair Housing Act advertising rule (24 CFR § 100.75) | Housing advertisements | No words, photos or targeting that indicate a preference based on protected characteristics | Listing-text classifiers; ad-delivery audits |

Sources: [Online Safety Act 2023, Schedule 7](https://www.legislation.gov.uk/ukpga/2023/50/schedule/7); [Ofcom, illegal harms statement, 2024](https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/statement-protecting-people-from-illegal-harms-online); [Ofcom, fraudulent advertising consultation, 2026](https://www.ofcom.org.uk/online-safety/online-fraud/consultation-fraudulent-advertising-code-of-practice); [Which?, 2025](https://www.which.co.uk/news/article/fake-reviews-and-sneaky-fees-banned-under-new-law-campaigned-for-by-which-aLzVp4g0S76D); [US Federal Trade Commission, INFORM guidance, 2023](https://www.ftc.gov/business-guidance/resources/informing-businesses-about-inform-consumers-act); [24 CFR § 100.75](https://www.law.cornell.edu/cfr/text/24/100.75).

INFORM repeats the DAC7 pattern. Because only marketplace-processed sales count, and because most classifieds traffic is used goods, a US lead-generation classifieds site is largely outside it. Payments bring it in.

{id: marketplace-regulation--compliance-as-architecture}
## Compliance as Architecture

{id: marketplace-regulation--five-components-that-serve-every-law}
### Five components that serve every law

The obligations in this chapter form a long list, but they ask for only five systems.

| Component | Serves | Key property |
| --- | --- | --- |
| **Obligation register** | Every regulation | Machine-readable: obligation ID, source and article, jurisdiction, applicability conditions, control, owner, evidence query, review date |
| **Decision record and evidence store** | DSA Arts. 15–24; GDPR accountability; P2B Art. 4; Online Safety Act | Immutable, versioned, retained per data class |
| **Trader and business registry** | DSA Arts. 30–32; P2B business users; CRD Art. 6a seller status; DAC7; INFORM | One verified record, many regulatory views |
| **Disclosure surfaces** | DSA Arts. 26–27 and 30(7); P2B Art. 5; UCPD Art. 7(4a) and Annex I 11a; CRD Art. 6a; energy and vehicle labeling | Generated from documented parameters and structured fields, never hand-written per page |
| **Regulatory reporting views** | DSA transparency reports and active-recipient counts; DAC7 reports | Saved, versioned queries over the event log and ledger; reproducible |

![Diagram: Compliance by design](listing-systems-architecture/posts/27-marketplace-regulation/assets/images/27-marketplace-regulation/fig05-compliance-design-each-obligation-register-points.jpeg)

**Figure 5:** *Compliance by design. Each obligation in the register points to a control in a shared component and to an evidence query; country differences enter as configuration; reports and control tests are computed from the same data, so the register always knows which obligations are demonstrably met.*

{id: marketplace-regulation--country-differences-as-configuration}
### Country differences as configuration

The DSA is a regulation and applies directly, but enforcement, penalties and many adjacent rules are national: what counts as illegal content in Poland differs from France, consumer-law transposition differs, DAC7 reporting formats and record-keeping differ, and energy-label rules differ by country. The tempting implementation is a code path per country. That is **The Copy-Paste Country**, and it makes the next change cost eight times as much, once per country.

Veldmark expresses country differences as data. The policy registry holds legal grounds per country; the attribute schema holds mandatory regulated fields per country and category; the disclosure templates hold language and placement per country; the reporting views hold format and authority per country. Engineers change components. Lucía's team, with counsel, changes configuration, through reviewed pull requests against the registry, and the obligation register records which configuration implements which obligation. [One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms) covers the tenancy model this relies on.

{id: marketplace-regulation--trade-offs}
## Trade-offs

| Approach | Strengths | Weaknesses | When it is right |
| --- | --- | --- | --- |
| **Compliance by project** (one exporter or feature per law) | Fast for the first deadline; no platform dependency | Numbers disagree; every new law repeats the work; evidence is reconstructed | A single small marketplace facing one deadline |
| **Local compliance per brand** | Close to local law and language | Four implementations of the same EU regulation; inconsistent decisions across brands | Brands about to be sold, or regulators that differ fundamentally |
| **Shared compliance-by-design components with country configuration** | One implementation per obligation type; reproducible evidence; cheaper next law | Up-front investment; a platform team becomes critical to every brand's compliance | Multi-brand, multi-country groups (Veldmark) |
| **Compliance vendor (RegTech) for specific obligations** | Speed; maintained templates (for example DAC7 report generation or Transparency Database submission) | Data leaves the platform; the vendor sees only what it is sent; lock-in | A narrow, standardized output with a stable schema |

{id: marketplace-regulation--vertical-differences}
## Vertical Differences

| Topic | General classifieds | Real estate | Automotive |
| --- | --- | --- | --- |
| Main horizontal exposure | DSA moderation volume; trader traceability for pro sellers; DAC7 once payments exist | DSA for agencies; trader panels; P2B for agency subscriptions | DSA and P2B for dealers; dealer termination notice periods |
| Vertical listing rules | Product safety for goods (DSA Art. 31 random checks) | Energy class and indicator in every ad (EPBD Art. 20(4)); French DPE detail; fair-housing language in the US | CO2 and consumption labeling for new cars (Pkw-EnVKV in Germany); price and mileage rules |
| DAC7 | In scope with in-platform payment for goods | Only if the platform collects rent | Only if the platform processes sale payments |

{id: marketplace-regulation--failure-modes}
## Failure Modes

1. **Exporters instead of records.** Each brand builds a statement-of-reasons exporter from its own logs. The numbers disagree and cannot be regenerated, which is the February 2027 situation at Veldmark.
2. **Silent demotion.** A ranking team down-ranks suspicious listings without a decision record. No statement of reasons is sent, the transparency report undercounts restrictions, and the practice is invisible until a complaint arrives.
3. **Unlabeled boosts.** A "top listing" product that is not visibly marked in results, or a ranking explanation that does not mention paid products. That is both **Multiplier Creep** and a blacklisted practice.
4. **Payments launched without the tax view.** A transaction feature goes live, and the team learns of DAC7 in November, with no tax profile, no seller data and two months to collect it from thousands of sellers.
5. **Trader data kept forever.** Dealer and agency documents retained long after the relationship ended, in breach of DSA Art. 30(5), because nobody owned the deletion trigger.
6. **Law in code.** A country's legal ground, field or label written into a service. Every legal change becomes a release, and every country becomes a fork.
7. **Personal data in the public database.** Free-text reviewer notes copied into `decision_facts` turn a submission into a data breach in a public, searchable database.

{id: marketplace-regulation--the-chief-architect-s-view}
## The Chief Architect's View

**Own the map, not the law.** The Chief Architect does not interpret regulation; counsel does. The architect owns the mapping from obligations to components and evidence, and the obligation register is the artifact that makes it visible. At Veldmark, the register has two owners: Lucía Ortega for the legal content and Ingrid's architecture team for the control and evidence columns. Every cross-brand decision record that touches a regulated capability cites the obligations it affects.

**Put regulatory review into the product lifecycle at the right moment.** The moments that change Veldmark's legal perimeter are predictable: a new transaction feature, a new paid ranking product, a new data-sharing arrangement between brands, an acquisition, a new country. Each triggers a review before design is final, not before launch. Safe Deal's Polish launch in 2026 would have been cheaper if the DAC7 tax profile had been designed with it.

**Fund the shared components as platform, not as compliance overhead.** The decision record, trader registry, disclosure surfaces and reporting views are also what trust and safety, professional seller tooling, ranking and finance need. Funding them as "compliance" makes them the first cut in a bad year. Funding them as platform capabilities with compliance as one consumer makes them durable.

**Watch the regulatory pipeline.** As of October 2026, the Commission has proposed repealing the P2B Regulation, is preparing a Digital Fairness Act on dark patterns, personalization and unfair pricing practices following its 2024 fitness check of consumer law, and EU Digital Identity Wallets are due by the end of 2026 ([European Commission, Review of EU consumer law, n.d.](https://commission.europa.eu/law/law-topic/consumer-protection-law/review-eu-consumer-law_en)). None of these changes the five components. Each changes their configuration. That is the test of whether the architecture is right.

**Measure compliance like reliability.** Veldmark tracks, per brand and month: the share of restricting decisions with a statement sent and submitted, the median time from decision to submission, the share of trader accounts with complete, current traceability data, the share of regulated listings with all mandatory fields, and the number of obligations in the register whose evidence query passed. A falling number is an incident, with an owner.

{id: marketplace-regulation--questions-to-ask}
## Questions to Ask

1. Which of our features let consumers conclude contracts or pay through the platform, and which laws did each feature bring into scope?
2. Does every restricting decision, including demotions and payout holds, produce a decision record and a statement of reasons, and how do we prove the counts match?
3. Could we regenerate last year's transparency report from stored events and get the same numbers?
4. What personal data could reach the Transparency Database through free-text fields, and what prevents it?
5. Where is trader-traceability data stored, who deletes it six months after a relationship ends, and when did that job last run?
6. Do our ranking explanations mention every paid product that affects order, and is every paid boost labeled in results?
7. If we launched in-platform payment in another country next quarter, when would DAC7 due diligence start, and from which ledger would the consideration come?
8. Which regulated listing fields exist per country and vertical, who tracks changes in the law, and what happens to a listing that lacks one?
9. Which country rules are implemented in code rather than configuration, and what would it cost to change each?
10. Is there an obligation register, and for how many obligations can we show a passing evidence query today?

{id: marketplace-regulation--from-trust-to-money}
## From Trust to Money

Part V has built the trust machinery of a listing marketplace: the shared trust-and-safety platform, fraud prevention, identity and verification, and, in this chapter, the regulation that now specifies much of it. Several of its threads point forward. Payments change the legal perimeter, labels govern paid placements, and trader records feed billing as well as compliance. [Part VI — MONEY: Conversion and Monetization](#part-6) turns to how marketplaces convert trust into revenue, starting with the moment a buyer decides to contact a seller, in [From Interest to Contact: Messaging and Lead Management](#messaging-and-leads).

{id: marketplace-regulation--sources-and-evidence}
## Sources and Evidence

{id: marketplace-regulation--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Vurderinger mellom Kjøper og Selger på FINN.no (Ratings between buyer and seller)](https://hjelpesenter.finn.no/hc/no/articles/22650860254994-Vurderinger-mellom-Kj%C3%B8per-og-Selger-p%C3%A5-FINN-no) — FINN help center, 2024 (updated 2026). Ratings published simultaneously after a deal.

{id: marketplace-regulation--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Regulation (EU) 2022/2065 (Digital Services Act)](https://eur-lex.europa.eu/eli/reg/2022/2065/oj) — Official Journal, 2022. Arts. 3, 14–33, 52 and 93; text checked against the Official Journal version retrieved through the EU Publications Office.
- [Commission Implementing Regulation (EU) 2024/2835](https://eur-lex.europa.eu/eli/reg_impl/2024/2835/oj) — Official Journal, 2024. Transparency-report templates, calendar-year periods, two-month publication, five-year availability.
- [DSA Transparency Database](https://transparency.dsa.ec.europa.eu/) and [API documentation](https://transparency.dsa.ec.europa.eu/page/api-documentation) — European Commission, accessed 19 October 2026 and n.d. Volumes; field vocabulary; batches of 100; `puid` rules.
- [Supervision of the designated very large online platforms and search engines](https://digital-strategy.ec.europa.eu/en/policies/list-designated-vlops-and-vloses) — European Commission, updated 15 October 2026. No classifieds marketplace designated.
- [Regulation (EU) 2019/1150 (platform-to-business)](https://eur-lex.europa.eu/eli/reg/2019/1150/oj) — Official Journal, 2019. Definitions, Arts. 3, 4, 5, 11; applies from 12 July 2020.
- [Platform-to-business trading practices](https://digital-strategy.ec.europa.eu/en/policies/platform-business-trading-practices) — European Commission, updated 2026. Proposed repeal; guidelines remain.
- [Directive (EU) 2019/2161 (Omnibus)](https://eur-lex.europa.eu/eli/dir/2019/2161/oj) — Official Journal, 2019. Price-reduction rule; UCPD Art. 7(4a), 7(6), Annex I points 11a, 23b, 23c; CRD Art. 6a; fines of at least 4%; applies from 28 May 2022.
- [Council Directive (EU) 2021/514 (DAC7)](https://eur-lex.europa.eu/eli/dir/2021/514/oj) — Official Journal, 2021. Platform definition and exclusions; relevant activities; consideration; excluded sellers; reporting content and deadlines.
- [Regulation (EU) 2016/679 (GDPR)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) — Official Journal, 2016. Art. 5 principles; Art. 22 automated decisions; recital 47 on fraud prevention.
- [Directive (EU) 2024/1275 (Energy Performance of Buildings, recast)](https://eur-lex.europa.eu/eli/dir/2024/1275/oj) — Official Journal, 2024. Art. 20(4) energy class in advertisements including property portals; transposition by 29 May 2026.
- [Diagnostic de performance énergétique (DPE)](https://www.service-public.gouv.fr/particuliers/vosdroits/F16096) — Service-Public.fr, French government, 2026. DPE advertising content, fines, rental bans, calculation changes.
- [Pkw-Energieverbrauchskennzeichnungsverordnung (Pkw-EnVKV)](https://www.gesetze-im-internet.de/pkw-envkv/BJNR103700004.html) — German Federal Ministry of Justice, as amended 2026. § 5 advertising duties for new passenger cars.
- [Online Safety Act 2023, Schedule 7](https://www.legislation.gov.uk/ukpga/2023/50/schedule/7) — legislation.gov.uk, 2023. Fraud as a priority offence.
- [Statement: protecting people from illegal harms online](https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/statement-protecting-people-from-illegal-harms-online) — Ofcom, 2024 (updated 2026). Risk-assessment and safety-measure dates.
- [Consultation: fraudulent advertising codes of practice](https://www.ofcom.org.uk/online-safety/online-fraud/consultation-fraudulent-advertising-code-of-practice) — Ofcom, 2026. Paid-ad fraud duties; timeline.
- [Informing businesses about the INFORM Consumers Act](https://www.ftc.gov/business-guidance/resources/informing-businesses-about-inform-consumers-act) — US Federal Trade Commission, 2023 (edited 2025). Thresholds, verification and disclosure duties.
- [24 CFR § 100.75, discriminatory advertisements](https://www.law.cornell.edu/cfr/text/24/100.75) — Cornell Legal Information Institute, n.d. US fair-housing advertising rule.
- [Review of EU consumer law](https://commission.europa.eu/law/law-topic/consumer-protection-law/review-eu-consumer-law_en) — European Commission, n.d. Fitness check and the planned Digital Fairness Act.

{id: marketplace-regulation--research-and-practitioner-sources}
### Research and practitioner sources

- [Fake reviews and sneaky fees banned under new law](https://www.which.co.uk/news/article/fake-reviews-and-sneaky-fees-banned-under-new-law-campaigned-for-by-which-aLzVp4g0S76D) — Which?, 2025. DMCC Act review rules from 6 April 2025; fines up to 10% of global turnover.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
