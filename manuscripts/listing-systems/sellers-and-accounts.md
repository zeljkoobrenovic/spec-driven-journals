{id: sellers-and-accounts}
# 12. Private Sellers, Dealers and Agencies: Modeling Who Lists

![Private Sellers, Dealers and Agencies: Modeling Who Lists — logo](listing-systems-architecture/posts/12-sellers-and-accounts/assets/images/12-sellers-and-accounts/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Model the supply side of a marketplace, from a private seller with one bike to an agency network with fourteen branches, five of them franchised. You will see how organizations, branches, users, roles and integrations fit together, why trader status has to be a governed attribute, and how a multi-brand group can share identity without merging every account.

> **WHY THE BUSINESS CARES:** Professional sellers pay most of the bills in vertical marketplaces, and they buy as organizations: a dealer group with several sites, an agency network with franchisees, a head office that pays for some branches but not others. An account model that cannot represent them produces wrong invoices, misrouted leads and reviews attached to the wrong business, and it fails the trader rules in EU consumer and platform law.

> **WHY ARCHITECTS SHOULD CARE:** The seller account is referenced by almost every other context: listings, leads, entitlements, billing, trust, regulation and analytics. Its identifiers end up in feeds, invoices and regulatory reports. Getting its shape wrong is expensive to fix, because every one of those contexts has copied it.

> **KEY POINTS:**
>
> * **Who acts, who is responsible, who pays and who is shown are four separate questions.** A user logs in and acts; a legal entity is the trader and is responsible; a billing account pays; a storefront or branch is what buyers see. Model each one explicitly. In simple cases they collapse into a single record; in an agency network with franchisees, none of them coincide.
> * **Trader status is a governed attribute, not a checkbox.** It decides which consumer law applies, what the listing must disclose, what must be verified under the EU Digital Services Act and, once payments run through the platform, what is reported to tax authorities. Store the declaration, the evidence, the verification result and the history, and run a process for private sellers who behave like traders.
> * **Organizations own listings; integrations are principals; groups share identity, not accounts.** Staff come and go, so listings belong to the organization and are assigned to branches. A software vendor posting for 500 agencies is one client with 500 scoped grants. Across a group, share the login and the verified legal-entity facts, and keep brand accounts separate, with purpose limits on how they are linked.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Entitlement Spaghetti** — when the account hierarchy does not say who bought a package for which branches, every service that checks entitlements makes up its own answer.
> * **The Acquisition Archipelago** — each acquired brand brings its own seller accounts, and the group cannot even count how many businesses it serves.
> * **Feed Roulette** — integrations authenticated with shared passwords and no scoped grants cannot be told apart, throttled or revoked one dealer at a time.

Part II has modeled the listing as an aggregate with its category, attributes, media and location; the last governed subdomain it references is the seller account, and "seller" means something different in every vertical. On a general classifieds site it usually means a person with a phone number. On a real-estate portal it means an agency branch, staffed by agents, owned by a company that may be one franchisee in a national network, publishing through a software vendor's feed. On an automotive marketplace it means a dealer group with several sites, a DMS (dealer management system) vendor that uploads the stock, a head office that negotiates the package, and salespeople who answer the leads.

Most marketplaces start with the first meaning and extend it one exception at a time, until the "user" table has a company name column, a parent-user ID for branches, a "pro" flag, a VAT number field and a shared login for the DMS vendor. **The account model is the place where marketplaces most often confuse identity with commerce.** This chapter builds a model that keeps them separate from the start and still collapses to "one person selling one bike". Later chapters build on it: entitlements attach to its accounts and branches ([Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements)), leads route through its branches ([From Interest to Contact: Messaging and Lead Management](#messaging-and-leads)), and partner feeds authenticate as its integration principals ([Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion)).

The chapter works through the model with Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)): Femke, a private seller on Tradeyard; Autohaus Ruhrblick, a dealer on Motorvane; and Agence Rhône Habitat, an agency network that lists on Hearthly and runs its business on Keybridge.

{id: sellers-and-accounts--setting-the-scene-at-veldmark-fourteen-branches-three-wrong-answers}
## Setting the Scene at Veldmark: Fourteen Branches, Three Wrong Answers

In May 2027, Agence Rhône Habitat publishes the three-room flat in Lyon 7e that later becomes this book's example of entity resolution. Agence Rhône Habitat (fictional) is a network of **14 branches** around Lyon. Nine are operated directly by the parent company; **five are franchisees**, separate companies that use the network's brand under contract. The agency manages its listings in Keybridge, Veldmark's agent CRM, which publishes them to Hearthly and to two competing portals.

The same week, the network's head of digital sends Claire Fontaine, Hearthly's CEO, a letter listing three problems:

1. **The wrong trader.** On Hearthly, listings from the five franchise branches show the parent company's name, registration number and address in the trader-information panel. Legally, each franchisee is the trader for its own listings.
2. **Reviews in the wrong place.** Buyer reviews of one franchisee, including some angry ones, appear on the profile of the whole network and on every branch page.
3. **An agent who left.** An agent who left the Villeurbanne branch in February still "owns" 212 listings on Hearthly. New leads for those listings go to her personal e-mail address, which she had used to create her Hearthly login in 2023.

A fourth problem is one Hearthly finds itself: the five franchisees' subscriptions are invoiced to the parent company, which has started refusing to pay them.

Julien Marchand, Hearthly's CTO, traces all four to one design decision. Hearthly's account model has a single entity, the **advertiser**, which is simultaneously the login, the legal identity, the billing party, the public profile and the owner of listings. Branches are advertisers with a parent-advertiser pointer. Users are e-mail addresses attached to an advertiser. Feeds authenticate as the advertiser. The model was built for single-office agencies and has been stretched to cover networks, franchises and staff turnover.

![Left, one strained figure balances a login key, legal document, invoice, profile card and listings; right, five figures each hold one of them.](listing-systems-architecture/posts/12-sellers-and-accounts/assets/images/12-sellers-and-accounts/one-advertiser-five-hats.jpeg)

**Figure 1:** *Hearthly's advertiser was at once login, legal identity, billing party, public profile and listing owner; separating those roles fixes the wrong trader, misplaced reviews, orphaned listings and wrong invoices.*

Ingrid Halvorsen, Veldmark's Group Chief Architect, sees the same shape in every brand. Tradeyard has user accounts with a "business" flag. Motorvane has dealer accounts keyed by its customer number, with sites added as sub-accounts and DMS vendors logging in with dealers' credentials. Keybridge, a SaaS product, has a proper tenant and user model, but with no link to anything else in the group, by design. With Veldmark ID due for approval in June 2027 and a group product catalog due in 2028 ([Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements)), the account model has to be settled first, because both depend on it.

{id: sellers-and-accounts--concepts-the-vocabulary-of-supply}
## Concepts: The Vocabulary of Supply

{id: sellers-and-accounts--private-and-professional-sellers}
### Private and professional sellers

A **private seller** is a person selling their own goods outside any trade or business. A **professional seller** (dealer, agency, merchant, developer, employer) sells in the course of a business. The distinction matters commercially, because professionals pay subscriptions and need tooling ([Serving the Pros: Dealer, Agent and Merchant Tooling](#professional-seller-tooling)). It matters even more legally.

In EU law the term is **trader**. The Digital Services Act (DSA) imposes **trader traceability** on online platforms that allow consumers to conclude distance contracts with traders. Before a trader can use the service, the platform must obtain "the name, address, telephone number and email address of the trader", a copy of an identification document or electronic identification, "the payment account details of the trader", the trade register and registration number where applicable, and a self-certification that the trader only offers compliant products or services. The platform must "make best efforts to assess whether the information … is reliable and complete", keep the information securely "for a period of six months after the end of the contractual relationship with the trader concerned" and then delete it. It must show the name and contact details, the registration and the self-certification to buyers "at least" where the product or service is presented ([Regulation (EU) 2022/2065, Art. 30](https://eur-lex.europa.eu/eli/reg/2022/2065/oj), applying since 17 February 2024).

Whether a classifieds site that only connects buyers and sellers lets consumers "conclude distance contracts" is arguable; the safe reading, used throughout this book, is that its trader listings are in scope. [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation) owns the legal analysis. This chapter's concern is what the obligations do to the data model:

| Regulation | What depends on trader status | Data the account model must hold |
| --- | --- | --- |
| DSA Art. 30 (trader traceability) | Onboarding gate, verification, display on listings, retention and deletion | Legal name, address, contacts, ID evidence, payment account, register number, self-certification, verification status and dates, end of relationship |
| EU consumer law (Modernisation Directive, applying from 28 May 2022) | Marketplaces must tell consumers whether the counterparty is a trader, based on the counterparty's own declaration, and that consumer rights do not apply when it is not ([European Commission](https://commission.europa.eu/law/law-topic/consumer-protection-law/consumer-contract-law/consumer-rights-directive_en), n.d.) | Seller's declaration, its date, and what was shown to the buyer |
| EU Platform-to-Business Regulation | Business users get ranking transparency and complaint handling | Which accounts are business users |
| EU DAC7 tax reporting | Once the platform knows the consideration paid to sellers, it reports sellers above the threshold to tax authorities. Goods sellers with fewer than 30 sales and €2,000 or less in the period are excluded ([Belastingdienst](https://belastingdienst.nl/wps/wcm/connect/en/business/content/information-for-platform-operators-dac7), n.d.) | Name, address, date of birth or registration, tax identifiers, financial account, quarterly consideration and fees, per seller and Member State |
| US INFORM Consumers Act (for comparison) | High-volume third-party sellers on marketplaces that process their payments must be verified, and larger ones disclosed ([FTC, 2023](https://www.ftc.gov/business-guidance/resources/informing-businesses-about-inform-consumers-act)) | Verified identity, bank account, tax ID, annual re-certification |

**One verified record serves many laws**, each with its own view of it. The obligations also grow with the business model: a pure lead-generation classifieds site sits mostly outside DAC7 and INFORM, but **launching in-platform payments brings seller reporting with it**, because the platform then knows what each seller was paid. Tradeyard Safe Deal is that change ([Beyond the Contact: Payments, Shipping and Buyer Protection](#transactions-and-payments)).

{id: sellers-and-accounts--trader-status-as-a-governed-attribute}
### Trader status as a governed attribute

**Trader status** is the platform's record of whether a seller account acts as a trader. It has four parts:

1. **Declaration** — what the seller said, when, in which flow, with which wording on screen.
2. **Evidence** — register extracts, VAT numbers, ID documents, eID results, payment-account checks.
3. **Verification result** — the platform's assessment, by which method, at which date, with an expiry or re-check date.
4. **Platform assessment** — whether the platform's own signals agree with the declaration.

The fourth part is where marketplaces most often have nothing. A private seller who lists 400 phone cases a year in their original packaging is very likely a trader, whatever they declared. The account model needs a **reclassification process**: signals (listing volume, new goods in volume, repeated identical listings, business-like descriptions, high Safe Deal turnover) open a case; the seller is asked to confirm or explain; the outcome changes the status, the display and the obligations, and is recorded. The signals belong to trust and safety ([Trust and Safety as a Platform](#trust-and-safety-architecture)); the status, the case outcome and its history belong to the account.

{id: sellers-and-accounts--organizations-branches-and-networks}
### Organizations, branches and networks

An **organization** is a legal entity that sells: a company, a sole trader's business, a public body. It is the trader, signs contracts and is the subject of business verification ([Who Is on the Other Side? Identity and Verification](#identity-and-verification) covers KYB, know-your-business checks). Industry practice and published reference models add three more levels:

- **Branch** (also site, location, rooftop, office): a physical place of business with its own address, opening hours, staff, inventory and lead routing. Branches usually belong to one organization.
- **Network** (franchise, brand group, dealer group): an umbrella across *several* organizations that share a brand. A franchise network is not a legal parent of its franchisees, which is why a model that makes branches children of one legal entity fails.
- **Storefront** or **profile**: the public identity shown to buyers (name, logo, description, ratings). It may correspond to a branch, an organization or a network brand.

Public portal interfaces use the same levels. Rightmove's Real Time Datafeed specification gives each software provider a **Network ID** and each agent office a **Branch ID** with sales and lettings channels; a call "will be rejected if sending a channel to which the branch does not have access", and the feed provider must be authorized for each branch ([Rightmove RTDF specification v1.4.1, 2023](https://media.rightmove.co.uk/ps/pdf/guides/adf/Rightmove_Real_Time_Datafeed_Specification.pdf)).

The choice of commercial unit (branch, forecourt, dealer, organization) is a modeling decision that shows up in investor reporting. Rightmove's commercial unit is the branch: its average revenue per advertiser (ARPA) is defined as revenue from agency and new-homes advertisers divided by the number of advertisers, and it reported 16,385 agency branches at the end of 2025 ([Rightmove results announcement, 2026](https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf)). Autotrader UK reports its unit as retailer forecourts (13,942 on average in FY26) with an average revenue per retailer of £2,995 a month ([Autotrader FY26 results, 2026](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf)).

{id: sellers-and-accounts--users-roles-and-memberships}
### Users, roles and memberships

A **user** is a person who logs in. In a group with a shared login, the user is a Veldmark ID identity ([Who Is on the Other Side? Identity and Verification](#identity-and-verification) owns authentication). A user is not a seller. A user has **memberships**: a relation to an organization, scoped to the whole organization or to specific branches, carrying roles such as administrator, lister, lead handler, finance or read-only. A private seller is a user whose only membership is to their own personal seller account.

Two rules follow from separating users from organizations:

1. **Listings are owned by the seller account and assigned to a branch; users are only the last editor.** When the Villeurbanne agent leaves, her membership ends; the 212 listings stay with the branch and are reassigned, and her lead routing ends with her membership.
2. **People can belong to several organizations.** An agent who moves between agencies, a consultant who manages listings for three dealers, an owner of two franchises: one user, several memberships, no duplicate logins.

{id: sellers-and-accounts--integration-principals}
### Integration principals

An **integration principal** is a software client that acts on behalf of sellers: a real-estate CRM, a DMS vendor, a feed aggregator, a listing tool. It is not a user and not a seller.

mobile.de's public Seller API keeps integration principals separate from sellers. Integration is through **Transfer Service Providers** (the DMS and inventory-tool vendors that upload for dealers) or through self-uploading dealers. Providers serving more than ten customers must supply contractual and technical contacts, their software, a VAT ID and customer numbers before access is granted, and every ad must name the dealer's customer number. API credentials are independent of sellers, and an API user sees only the sellers linked to it ([mobile.de Seller API](https://services.mobile.de/manual/seller-api.html), n.d.).

OAuth makes the same separation. The OAuth 2.0 Security Best Current Practice (RFC 9700, January 2025) requires exact-match redirect URIs, recommends PKCE for all clients, forbids the implicit grant, says the resource-owner password grant "MUST NOT be used", and recommends sender-constrained, audience-restricted tokens ([IETF RFC 9700, 2025](https://www.rfc-editor.org/rfc/rfc9700.html)). In listing terms: a third-party tool acting for one agency uses the authorization-code flow, with the agency's administrator consenting to scopes; a contracted feed vendor uses client credentials with grants bound to specific organizations and branches. **A vendor serving 500 dealers is one client with 500 grants, not 500 shared passwords.**

![Left, a vendor carries a tangled ring of dealers' keys; right, the vendor holds one client badge with scoped permission tickets to each dealer.](listing-systems-architecture/posts/12-sellers-and-accounts/assets/images/12-sellers-and-accounts/one-client-many-grants.jpeg)

**Figure 2:** *An integration vendor serving many dealers should be one client with a scoped grant per dealer, never a collection of shared seller passwords.*

{id: sellers-and-accounts--architecture-the-seller-account-model}
## Architecture: The Seller Account Model

{id: sellers-and-accounts--one-entity-per-question}
### One entity per question

![Diagram: Eight entities, each answering one question](listing-systems-architecture/posts/12-sellers-and-accounts/assets/images/12-sellers-and-accounts/fig03-eight-entities-each-answering-one-question.jpeg)

**Figure 3:** *Eight entities, each answering one question. Users act, legal entities are responsible, contracts pay, and storefronts are shown; seller accounts tie them to one brand, branches tie them to a place, networks group traders under one umbrella, and integrations get scoped grants instead of logins.*

Each entity answers one question and lives in one place:

| Entity | Answers | Key attributes | Lives in |
| --- | --- | --- | --- |
| **User** | Who acts? | Identity ID, verified contact points, authentication methods | Group identity ([Who Is on the Other Side? Identity and Verification](#identity-and-verification)) |
| **Legal entity** | Who is responsible? | Legal name, register and number, VAT or tax IDs, registered address, verification evidence and status | Group business party registry |
| **Seller account** | Who sells on this brand? | Brand, seller type (private or professional), trader status record, lifecycle state, contact preferences, link to a legal entity or to a private user | Brand account service |
| **Branch** | Where, and who handles it? | Address and location ([Where Is It? Location, Geocoding and Privacy](#location-and-geo)), opening hours, channels (sale, rent), lead routing rules, assigned staff | Brand account service |
| **Commercial contract and billing account** | Who pays, for what? | Contracting party, invoiced party, packages, covered branches, price list, payment terms | Product catalog, entitlements and billing ([Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements)) |
| **Storefront** | Who is shown? | Display name, logo, description, ratings, the trader information that must be displayed | Brand account service, rendered by the brand |
| **Network** | Which brand umbrella? | Network name, member legal entities, shared display assets | Brand account service |
| **Integration principal** | Which software acts? | Client ID, vendor legal entity, grants per seller account, branch and scope, quotas | Group integration platform ([Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion)) |

In the simple cases, most of this collapses. Femke is a user with one private seller account; there is no legal entity, branch, contract or storefront beyond her public profile. A single-office agency is one legal entity, one seller account, one branch, one contract and one storefront. The model costs nothing in the simple case and is essential in the complex one.

{id: sellers-and-accounts--agence-rhone-habitat-modeled-correctly}
### Agence Rhône Habitat, modeled correctly

| Element | Before (Hearthly 2027) | After |
| --- | --- | --- |
| Legal entities | One advertiser record for the network | Six: the parent company and five franchisees, each with its register number and its own verification |
| Seller accounts on Hearthly | 1 parent advertiser and 13 child advertisers | Six seller accounts, one per legal entity |
| Branches | 14 child advertisers | 14 branches: 9 under the parent's account, 1 each under the franchisees' |
| Network | Implicit in the parent pointer | One network, "Agence Rhône Habitat", grouping the six legal entities for display |
| Contracts and billing | One contract, invoiced to the parent | Six contracts: the parent's covers its 9 branches; each franchisee pays for its own |
| Trader information on listings | Parent's details on every listing | The legal entity that owns the listing's seller account |
| Reviews | Pooled at network level | Attached to the branch, shown at branch level; network page shows a clearly labeled aggregate |
| Users | 61 e-mail logins, 7 of them former staff | Users with memberships scoped to branches; leavers' memberships ended by the agency's administrators |
| Integration | Keybridge authenticated as the parent advertiser | Keybridge is an integration principal with grants for the 14 branches, scoped to listings and leads |

A franchise network is a display and commercial concept, not a legal hierarchy, and the trader rules follow the legal hierarchy. The table is Veldmark's illustration, but any franchise network has the same shape.

![One brand umbrella over six separate legal entities: a parent building with nine branches and five franchisee buildings with one branch each.](listing-systems-architecture/posts/12-sellers-and-accounts/assets/images/12-sellers-and-accounts/franchise-network-not-hierarchy.jpeg)

**Figure 4:** *Agence Rhône Habitat is one network over six legal entities: the parent runs nine branches, and each of the five franchisees is its own trader with one branch.*

{id: sellers-and-accounts--account-lifecycle}
### Account lifecycle

A **seller account lifecycle** is the set of states an account passes through, from registration to erasure. It differs for private and professional accounts mainly in the onboarding gate.

![Diagram: A seller account's lifecycle](listing-systems-architecture/posts/12-sellers-and-accounts/assets/images/12-sellers-and-accounts/fig05-seller-account-s-lifecycle-professional-accounts.jpeg)

**Figure 5:** *A seller account's lifecycle. Professional accounts pass a verification gate before their listings go live, private accounts can be reclassified into it, and closing an account starts retention clocks rather than deleting data at once.*

Three transitions need explicit design:

- **Reclassification** (Active to UnderReview to Onboarding) is how a private account becomes a trader. Its listings may stay visible during the case, but new listings beyond a volume limit wait until verification completes.
- **Suspension** must propagate. A suspended account's listings leave search, its integration grants stop working, its scheduled bumps stop and its pending leads are handled. [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline) owns unpublish propagation; the account service owns the event that triggers it. Every restriction is also a moderation decision that needs a statement of reasons under the DSA ([Trust and Safety as a Platform](#trust-and-safety-architecture)).
- **Closed to Erased** is not one clock but several. DSA trader data is kept for six months after the relationship ends and then deleted. Invoices follow accounting retention rules, which are much longer. Fraud block lists may keep hashed identifiers longer, with a documented justification. The account service has to know which data class follows which clock, and [System of Record and Read Models: Listing Data Management](#listing-data-management) has to propagate erasure to every copy.

{id: sellers-and-accounts--contact-preferences-and-lead-routing}
### Contact preferences and lead routing

Contact options belong to the branch and the seller account, not to the listing alone: which channels are open (chat, masked phone, e-mail form, viewing or test-drive booking), opening hours, whether phone numbers are shown or masked, and who receives a lead. A dealer's lead for a car on its Bochum site goes to the Bochum sales team's queue, not to whoever uploaded the car. [From Interest to Contact: Messaging and Lead Management](#messaging-and-leads) owns lead objects and routing; the account model provides the routing rules and their owners.

For private sellers, contact preferences are also safety controls. A new private account whose phone number is hidden until it has some history, and whose messages go through on-platform chat, is harder to use for the off-platform scams described in [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention).

{id: sellers-and-accounts--reputation-and-ratings}
### Reputation and ratings

Where ratings attach is a modeling decision with legal weight:

| Attach ratings to | Works for | Breaks when |
| --- | --- | --- |
| The user | Private sellers and buyers | A professional's staff change; the rating follows a person, not the business |
| The seller account | Single-entity businesses | A franchise network pools ratings across separate traders |
| The branch | Agencies and dealer groups with several sites | Buyers want a single network view (offer it as a labeled aggregate) |
| The individual agent | Real estate, where buyers choose agents | The agent leaves; ratings must stay with the branch or move with the agent by an explicit rule |

EU consumer law, as amended by the 2019 Modernisation Directive, requires a business that gives access to consumer reviews to say whether and how it checks that they come from people who actually used or bought the product (Article 7(6) of the Unfair Commercial Practices Directive, inserted by [Directive (EU) 2019/2161](https://eur-lex.europa.eu/eli/dir/2019/2161/oj)). A marketplace that shows ratings of sellers should therefore record, with each rating, what made the reviewer eligible: a completed Safe Deal transaction, a lead followed by a confirmed viewing, or nothing at all.

{id: sellers-and-accounts--in-practice-documented-patterns-and-three-veldmark-accounts}
## In Practice: Documented Patterns and Three Veldmark Accounts

{id: sellers-and-accounts--documented-patterns-at-real-marketplaces}
### Documented patterns at real marketplaces

The public record on seller models is thin; most of it is in partner API documentation and investor reports, not engineering blogs.

- **mobile.de** separates the seller from the commercial account (a seller ID and a customer number), documents a "multi-locations" resource for dealers with several sites, and treats transfer service providers as separate principals linked to the sellers they serve ([mobile.de Seller API](https://services.mobile.de/manual/seller-api.html), n.d.). This is the clearest public example of integration principals with scoped access.
- **Rightmove's** feed specification models a network (software provider) by branch (office) by channel (sales or lettings) tenancy, authenticated with mutual TLS client certificates issued by Rightmove ([Rightmove RTDF specification v1.4.1, 2023](https://media.rightmove.co.uk/ps/pdf/guides/adf/Rightmove_Real_Time_Datafeed_Specification.pdf)). Its leads and performance calls are also scoped by branch. Rightmove's customer checks and its requirement that agents belong to a redress scheme act as know-your-business controls: Rightmove says it carries out checks on all its customers before they can advertise ([Rightmove guide](https://www.rightmove.co.uk/guides/?p=385), n.d.).
- **CarGurus** defines a paying dealer as "a dealer account with an active, paid subscription at the end of a defined period" and reported 34,409 paying dealers at the end of 2025 ([CarGurus Form 10-K, 2026](https://www.sec.gov/Archives/edgar/data/1494259/000119312526059435/carg-20251231.htm)). The definition is a reminder that the commercial unit is an account with a contract, not a legal entity.
- **The Bundeskartellamt's clearance on 8 October 2026** of mobile.de's acquisition of Carwow's German business noted that dealers and consumers often use several platforms in parallel and that many platforms let dealers export their data to other platforms; its main stated reasons for clearance were Carwow's new-car focus and competition from AutoScout24 ([Bundeskartellamt, 2026](https://www.bundeskartellamt.de/SharedDocs/Meldung/DE/Pressemitteilungen/2026/10_08_2026_mobile_carwow.html)). Dealers keep their data portable across marketplaces, and the integration-principal model is how a marketplace accepts that.

> **INFERENCE, NOT DOCUMENTED:** None of these sources describes the internal account schema of the companies concerned. The seller account model in this chapter is a reference architecture derived from their public interfaces and from regulatory requirements, not a description of any company's systems.

{id: sellers-and-accounts--femke-a-private-seller}
### Femke, a private seller

Femke's Tradeyard account in March 2027 is a user record with an e-mail address, a verified phone number and a postcode. Under the target model:

- She is a user with one membership: her own private seller account on Tradeyard Netherlands. When Veldmark ID rolls out in 2028, the same identity gives her a separate Motorvane profile if she ever sells a car, but no Motorvane seller account until she creates one.
- Her trader status is "private, self-declared" with the date and the wording shown in the insertion flow. Her listings show "Private seller", which is the consumer-law disclosure that EU law asks marketplaces to make.
- Her sale of the city bike for €225 through Safe Deal "pay at pickup" counts towards DAC7. She makes four Safe Deal sales in 2027 for €610 in total, well under both thresholds, so Tradeyard collects nothing beyond what Safe Deal itself needs.
- Her public profile shows her first name, her district (not her postcode; see [Where Is It? Location, Geocoding and Privacy](#location-and-geo)), her member-since date and ratings from completed Safe Deal transactions, each marked as verified by a transaction.

The accounts Tradeyard's reclassification job flags only look like Femke's. In 2026, about **18,000** Tradeyard Netherlands accounts declared as private each published more than 100 listings; a sample review by Aisha Rahman's trust team found that most were resellers (an illustrative Veldmark figure). Each of them is a trader the platform has not verified and whose buyers have been told, wrongly, that consumer rights do not apply. The reclassification process is the fix, and it is also a revenue opportunity: reclassified traders are the obvious prospects for Tradeyard's professional subscriptions.

{id: sellers-and-accounts--autohaus-ruhrblick-a-dealer}
### Autohaus Ruhrblick, a dealer

Autohaus Ruhrblick (fictional) is one legal entity with two sites, Essen and Bochum, and a DMS from a vendor that serves about 1,900 of Motorvane's dealers. In the target model:

- **Legal entity:** Autohaus Ruhrblick GmbH, verified against the commercial register when it signed its contract in 2019, which until Motorvane's June 2027 re-check pilot was the only check Motorvane ran on dealers ([Who Is on the Other Side? Identity and Verification](#identity-and-verification)). In the target model the registry re-verifies it on a schedule (every 90 days for business claims), including its VAT ID against the EU's VAT information exchange system.
- **Seller account:** one Motorvane Germany account, professional, trader status verified.
- **Branches:** Essen and Bochum, each with its address, opening hours and lead routing: e-mail leads to each site's sales inbox, calls to its tracked number, test-drive bookings to its calendar.
- **Contract:** one dealer package (Motorvane's Pro 150: 150 listing slots for €1,450 a month) covering both branches, with the slots shared between them ([Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements)).
- **Integration principal:** the DMS vendor's client, with a grant for both branches, scoped to listings write and statistics read. The vendor cannot read leads, because Autohaus Ruhrblick has not consented to that scope.

When the dealer lists the 2021 Volkswagen Golf on Wednesday 14 April 2027, the listing is owned by the seller account, assigned to the Essen branch, and its provenance records the DMS vendor's client as the writer. The 23 raw leads in ten days (19 after deduplicating repeat contacts from the same buyers) go to the Essen queues. The trader-information panel on the listing shows the GmbH's name, address, register number and self-certification, which is what DSA Art. 30(7) asks for. When the feed's removal arrives 26 hours after the sale on 29 April, the delay is a problem for [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion), not for the account model, but the account model is what lets Motorvane measure feed latency per integration principal and per dealer and raise it with the right vendor.

{id: sellers-and-accounts--overlap-across-brands-poland}
### Overlap across brands: Poland

Tradeyard Poland's cars section and Motorvane Poland compete for the same dealers, one of the eight problems Veldmark starts 2027 with. Nobody knows how many dealers are customers of both, because the two brands' accounts share no identifiers. Matching the two brands' professional accounts on the Polish tax identification number (NIP) in a one-off analysis finds about **2,900 dealers with active accounts on both**, about 40% of them on paid packages with both brands (an illustrative Veldmark figure).

The number is a strategic fact, not just a data-quality one: it is the population for any decision to move car supply from Tradeyard to Motorvane in Poland, and it is why the group needs a registry of legal entities that both brands can read. It is also a warning about what not to do with the registry, which is the subject of the next section.

{id: sellers-and-accounts--group-wide-identity-versus-per-brand-accounts}
## Group-Wide Identity Versus Per-Brand Accounts

A multi-brand group has three realistic options for who-lists data:

| Option | What is shared | Strengths | Weaknesses | When it is right |
| --- | --- | --- | --- | --- |
| **Separate accounts per brand** | Nothing | Brand autonomy; no cross-brand data-protection questions; easy to sell a brand | Duplicate logins; no group view of customers; KYB done several times; bans evaded by moving brands | Groups that are portfolios held for sale, not platforms |
| **Shared identity and party registry, brand accounts** | The login (group identity) and verified legal-entity facts | One login; KYB once; group customer view possible; brands keep their commercial relationship | Purpose limits and access control on the links between brand accounts must be designed and enforced | Groups building a shared platform beneath separate brands, like Veldmark's "share platforms, not products" |
| **One group account across brands** | Everything: one customer account, one contract, one profile | One commercial relationship; cross-brand bundles | Brands lose control of their customer relationships; data-protection and competition questions; hard to divest | Groups that run one brand in several verticals |

Veldmark chooses the middle option, and the Keybridge case shows why the purpose limits matter. In March 2027, Veldmark committed that **no Keybridge agency data is used by Hearthly for ranking or sales targeting**, with access controls and an annual independent review. Agence Rhône Habitat is both a Keybridge customer and a Hearthly advertiser. A shared registry of legal entities will link the two accounts, because the same company is the trader in both. The question is what that link may be used for.

![Diagram: Share identity and verified legal facts, not commercial data](listing-systems-architecture/posts/12-sellers-and-accounts/assets/images/12-sellers-and-accounts/fig06-share-identity-verified-legal-facts-not.jpeg)

**Figure 6:** *Share identity and verified legal facts, not commercial data. The registry gives every brand the same verified trader record; Keybridge reaches Hearthly only as an integration principal with scoped grants, and its CRM data never crosses the dashed line.*

The rules Veldmark writes into the decision record:

1. **The registry holds public-register and verification facts only**: legal name, register number, tax IDs, registered address, verification status and evidence references. It holds no packages, prices, revenues, leads or listing counts.
2. **Brand accounts link to registry entries, not to each other.** A query "which brands is this company a customer of?" is a privileged report, available to group finance and to approved strategy analyses such as the Poland overlap, not an API that brand sales tools can call.
3. **Keybridge reads and writes verification facts but nothing else.** Its CRM data, its customers' leads from other portals and its customers' listings on competing portals stay in Keybridge. Keybridge acts on Hearthly only as an integration principal, with the same grants any other software vendor would get.
4. **Every cross-brand use of the registry is logged** and included in the annual independent review of the Keybridge commitment.

The data-protection side is owned by Lucía Ortega's team: for private users, Veldmark ID links profiles across brands only when the user uses more than one brand, and brand-specific data stays with the brand. The competition side is for counsel, but the architecture should make the commitment checkable.

{id: sellers-and-accounts--trade-offs}
## Trade-offs

{id: sellers-and-accounts--modeling-private-sellers}
### Modeling private sellers

| Option | How it works | Strengths | Weaknesses |
| --- | --- | --- | --- |
| **User with a seller flag** | The user record is the seller | Simplest; fits a C2C-only site | Breaks at the first professional; reclassification means a migration |
| **Degenerate organization of one** | Every seller is an organization; private sellers have one member and no legal-entity data | One model for every seller | Private sellers carry fields that make no sense for them; risk of collecting business data from consumers |
| **Seller account linked to either a user or a legal entity** | The seller account is the common entity; it references a private user or a legal entity | Clean privacy boundary; reclassification is a relink plus verification | Two link types to handle in every consumer of the account |

I recommend the third option. It keeps private sellers' data minimal, makes reclassification an explicit operation and lets the trader rules attach to legal entities, where they belong.

{id: sellers-and-accounts--who-owns-a-listing}
### Who owns a listing

| Owner | Works for | Breaks when |
| --- | --- | --- |
| The user who created it | Private sellers | Staff leave; listings orphaned or follow the person |
| The seller account | Most businesses | Multi-site businesses need branch-level routing, statistics and entitlements |
| The seller account, assigned to a branch | Agencies, dealer groups, networks | Nothing structural; requires branch maintenance by the seller |

{id: sellers-and-accounts--integration-authentication}
### Integration authentication

| Option | Strengths | Weaknesses |
| --- | --- | --- |
| Seller's own credentials shared with the vendor | No work for the platform | Cannot scope, rotate, throttle or revoke per vendor; violates RFC 9700's ban on the password grant in spirit and in letter |
| Static API key per vendor | Simple | Usually all-or-nothing access; keys leak and live forever |
| Mutual TLS certificate per vendor with branch authorization | Strong, used by Rightmove's feed | Certificate lifecycle to manage; coarse scopes |
| OAuth clients with grants per seller account, branch and scope | Fine-grained, revocable, auditable; seller consent possible | More moving parts; needs a consent and grant-management user interface |

{id: sellers-and-accounts--vertical-differences}
## Vertical Differences

| Dimension | General classifieds | Real estate | Automotive | Jobs |
| --- | --- | --- | --- | --- |
| Typical supply | Mostly private sellers (78% of new Tradeyard listings); small traders | Agencies and developers; private landlords in rentals | Dealers dominate; private sellers a minority | Employers and staffing agencies |
| Commercial unit | Account, sometimes none | Branch (office) | Dealer or forecourt | Employer account; sometimes per job slot |
| Hierarchy depth | Shallow | Deep: network, franchisee, branch, agent | Group, legal entity, site | Group, company, recruiter |
| Who acts | The seller | Agents and back-office staff, mostly via software | Sales staff; DMS uploads | Recruiters; applicant-tracking systems |
| Integration principals | Few | About 160 vendors for Hearthly; agent CRMs | DMS vendors; 88% of Motorvane dealer listings via DMS feeds | Applicant-tracking systems; job aggregators |
| Individual professional identity | Rare | The agent matters to buyers; licensing regimes vary by country | Salesperson rarely shown | The recruiter is often shown |
| Trader questions | Private-versus-trader reclassification is the main issue | Agency KYB; private landlords as possible traders | Dealer KYB; private sellers who trade cars | Employer verification; fake job ads |

Real estate is the vertical where the hierarchy is deepest and the individual agent is a visible, rated person, often under a professional licensing regime in the country concerned. Automotive is where integration principals matter most, because most stock arrives from DMS vendors. General classifieds is where the trader boundary is hardest to police, because the population is huge and the signals are behavioral.

{id: sellers-and-accounts--failure-modes}
## Failure Modes

1. **Listings owned by users.** Staff turnover orphans listings or routes leads to people who left, as with the Villeurbanne agent. Ownership belongs to the seller account; users are editors.
2. **The trader flag as a checkbox.** A boolean set once at sign-up, with no evidence, no date, no wording record and no reclassification, cannot answer a regulator and lets resellers pose as private sellers.
3. **The legal hierarchy assumed to equal the display hierarchy.** Franchisees displayed under the network's legal identity give buyers the wrong trader and the wrong contact for consumer claims.
4. **Billing hierarchy assumed to equal the legal hierarchy.** Head offices pay for some branches and not others; contracts must name the branches they cover.
5. **Shared credentials for integrations.** Vendors logging in as dealers cannot be told apart, throttled or revoked one dealer at a time, and every password reset breaks a feed.
6. **Suspension that does not propagate.** A suspended account's listings stay searchable, its feeds keep writing and its scheduled bumps keep running: Ghost Inventory with an enforcement problem attached.
7. **One retention clock.** Deleting all of a closed account's data at once loses invoices that must be kept; keeping all of it forever breaks the DSA's six-month deletion rule for trader data.
8. **Merging across brands by e-mail address.** Matching accounts on an e-mail address across brands links people who never asked to be linked, and in Veldmark's case could breach the Keybridge commitment. Link through the identity the user chose to use, and through verified legal entities with purpose limits.
9. **Pooled reputation.** Ratings aggregated across separate traders make good franchisees pay for bad ones and mislead buyers about who they are dealing with.

{id: sellers-and-accounts--the-chief-architect-s-view}
## The Chief Architect's View

The seller account is a supporting domain in the language of [Bounded Contexts for Marketplaces: Where One Listing Becomes Many Models](#bounded-contexts): no buyer chooses a marketplace for its account model. But almost every core domain depends on it, so a group should standardize it early, before the product catalog, entitlements and messaging copy their own versions.

**Decision 1: one supply-side model for all brands.** Users, legal entities, seller accounts, branches, networks, contracts, storefronts and integration principals, with the meanings in this chapter. Each brand implements it in its own account service on its own timeline, but the identifiers and events (SellerAccountCreated, TraderStatusChanged, BranchAdded, MembershipEnded, AccountSuspended) follow one group contract. The product catalog and entitlement service due in Q2 2028 attaches entitlements to seller accounts and branches as defined here; without that, [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements) would be building on four different meanings of "customer".

**Decision 2: a group business party registry, launched with Veldmark ID.** Approved at the architecture advice forum in August 2027, owned by the identity platform team, live with Veldmark ID in 2028. It holds verified legal-entity facts and evidence references, serves DSA trader traceability, consumer-law declarations, P2B business users and DAC7 for every brand, and runs re-verification on a schedule. The purpose rules above are part of the decision record.

**Decision 3: trader status is shared between accounts and trust.** The account service owns the status and its history; the trust-and-safety platform owns the reclassification signals and cases. Aisha Rahman and the account platform's product lead jointly own the policy, with Lucía Ortega's team signing off on what is displayed to buyers.

**Decision 4: integrations get grants, not passwords.** Every brand moves feed and API partners to client credentials or certificates with grants per seller account and branch, starting with Motorvane's DMS vendors in 2028. This is also what makes per-vendor feed quality measurable ([Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion)).

What to watch: the share of professional listings whose seller has a verified trader record (target 100%); reclassification cases opened and resolved per month; orphaned listings (owned by an account with no active member); integration principals still using shared credentials; and the volume of cross-brand registry queries, which should stay small and fully logged.

The condition under which this is too much: a single-brand, C2C-only marketplace without payments can live with users and a trader declaration for a long time. It stops being enough the day the first dealer asks for a second login.

{id: sellers-and-accounts--questions-to-ask}
## Questions to Ask

1. For any listing, can we say which user last changed it, which legal entity is the trader, which contract pays for its visibility and which branch handles its leads?
2. What happens to a professional's listings and leads when the employee who created them leaves?
3. Where is trader status stored, with what evidence, and how is a private seller who behaves like a trader detected and reclassified?
4. Does the trader information on each listing come from the legal entity that is actually responsible, including for franchisees?
5. How do integration partners authenticate, and can we revoke one partner's access to one dealer without affecting anyone else?
6. Which data classes of a closed account follow which retention clock, and who deletes what when?
7. Where do ratings attach, and what makes a rating eligible to be shown as verified?
8. Across our brands, can we count how many businesses we serve, and who is allowed to ask that question?
9. If we launched in-platform payments in a new country tomorrow, could we produce the seller data that tax reporting would require?
10. Which other services hold their own copy of the account hierarchy, and which of them would disagree with the account service today?

{id: sellers-and-accounts--from-the-listing-to-its-supply}
## From the Listing to Its Supply

With the listing, its taxonomy, attributes, media, location and seller modeled, Part II's account of the thing being sold is complete. [Part III — SUPPLY: Getting Inventory In](#part-3) turns to how that supply actually arrives, through forms, APIs and bulk feeds from thousands of partners, starting with [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion).

{id: sellers-and-accounts--sources-and-evidence}
## Sources and Evidence

{id: sellers-and-accounts--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Seller API manual](https://services.mobile.de/manual/seller-api.html) — mobile.de, n.d. Transfer service providers, seller and customer identifiers, multi-locations, linked-seller access.
- [Real Time Datafeed Specification v1.4.1](https://media.rightmove.co.uk/ps/pdf/guides/adf/Rightmove_Real_Time_Datafeed_Specification.pdf) — Rightmove, 2023. Network, branch and channel tenancy; mutual TLS; branch-scoped leads and performance.
- [Results announcement for the year to 31 December 2025](https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf) — Rightmove, 2026. ARPA definition per advertiser; 16,385 agency branches.
- [Rightmove guide on customer checks](https://www.rightmove.co.uk/guides/?p=385) — Rightmove, n.d. Pre-advertising customer checks and redress-scheme membership for agents.
- [Full-year results FY26](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf) — Autotrader Group, 2026. Retailer forecourts and average revenue per retailer.
- [Form 10-K for 2025](https://www.sec.gov/Archives/edgar/data/1494259/000119312526059435/carg-20251231.htm) — CarGurus, 2026. Paying-dealer definition and count.
- [Bundeskartellamt clears mobile.de's acquisition of carwow.de](https://www.bundeskartellamt.de/SharedDocs/Meldung/DE/Pressemitteilungen/2026/10_08_2026_mobile_carwow.html) — Bundeskartellamt, 2026. Dealer multi-homing and data export as constraints on market power.

{id: sellers-and-accounts--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Regulation (EU) 2022/2065 (Digital Services Act), Article 30](https://eur-lex.europa.eu/eli/reg/2022/2065/oj) — European Union, 2022. Trader traceability: data to collect, best-efforts verification, six-month retention and display; quotations checked against the Official Journal text.
- [Directive (EU) 2019/2161 (Modernisation or Omnibus Directive)](https://eur-lex.europa.eu/eli/dir/2019/2161/oj) — European Union, 2019. Trader declaration on online marketplaces (new Art. 6a of the Consumer Rights Directive) and review-verification information (new Art. 7(6) of the Unfair Commercial Practices Directive).
- [Consumer Rights Directive](https://commission.europa.eu/law/law-topic/consumer-protection-law/consumer-contract-law/consumer-rights-directive_en) — European Commission, n.d. Modernisation Directive amendments applying from 28 May 2022, including obligations of online marketplaces.
- [Information for platform operators (DAC7)](https://belastingdienst.nl/wps/wcm/connect/en/business/content/information-for-platform-operators-dac7) — Belastingdienst, n.d. Reportable activities, seller data and the de minimis rule.
- [Informing Businesses about the INFORM Consumers Act](https://www.ftc.gov/business-guidance/resources/informing-businesses-about-inform-consumers-act) — US Federal Trade Commission, 2023. High-volume seller verification and disclosure.
- [RFC 9700: Best Current Practice for OAuth 2.0 Security](https://www.rfc-editor.org/rfc/rfc9700.html) — IETF, 2025. Grant types, PKCE, sender-constrained tokens.

{id: sellers-and-accounts--research-and-practitioner-sources}
### Research and practitioner sources

- *Productscape domain models for general listings and real-estate marketplaces* — the author's research digest, 2026. Seller entity, storefront and intermediary models; professional personas and integration partners.
- The book's research briefs on listing data, trust and regulation, real-estate portals and monetization, 2026 — summaries of the primary sources above and of EU consumer-law provisions on trader declarations and reviews.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
