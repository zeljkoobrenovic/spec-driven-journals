# Research brief: Security, privacy and regulation for commerce platforms

Prepared 7 November 2026 for chapter writers of *ORDERED: Architecting Commerce Platforms*. The brief feeds Part VIII (chapters 34 Commerce Security, 35 Privacy and Customer Data, 36 Commerce Regulation) and the trust-related passages of chapters 12 (Payments), 18 (Returns), 27 (Identity and Master Data) and 45 (AI and Agentic Commerce). It is Europe-first (EU law, with Dutch, Belgian and German specifics) with the United States as the contrast. It is platform-neutral and is not legal advice.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (7 November 2026) and supports the claim. Paraphrases stay close to the source and quoted text is quoted. The date is the source's publication date; undated product or guidance pages are marked "n.d., accessed 2026-11". EU legal texts were read as the original Official Journal texts served by the EU Publications Office (`publications.europa.eu/resource/celex/<CELEX>`), not consolidated versions; the date given is the OJ date.
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (encyclopaedia, law-firm note, trade or security press, enforcement tracker) fetched in this session, not from the primary document.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference, including every statement about how a proprietary platform works internally where the vendor has not described it, and every figure the session could not re-verify.

**Evidence age matters.** Security statistics and vendor documentation change yearly; regulation changes by amendment, delay and court decision. Sources older than about three years are flagged **(evidence age)**. The two web-skimming penalties (British Airways, Ticketmaster) date from 2020 and concern 2018 incidents; they remain the clearest public records of how skimming works, but the controls they describe predate PCI DSS v4.

**⚠ Volatility flags** mark claims likely to change within 12 months: PSD3/PSR adoption, the Digital Omnibus on data and cookies, the Digital Fairness Act, Dutch e-invoicing, the US negative-option rulemaking, the count of US state privacy laws, the Data Privacy Framework appeal, AI Act dates, and the ESPR delegated acts.

**Research limitation.** The session's shared web-search quota was exhausted after about twelve searches, and several primary sites blocked automated fetching (HTTP 403, Cloudflare challenge or "unable to fetch"): the UK ICO (both skimming penalties), the BBC, the Guardian, Wired, the Dutch Autoriteit Persoonsgegevens in English (the Dutch page was readable), the Belgian DPA's English pages (the Dutch page was readable), the CNIL's decision pages, the Federal Register and eCFR, the Commission press corner and several Commission policy pages, EUR-Lex (replaced by the Publications Office), and the EDPB guideline landing pages (replaced by the PDFs). As a result:

- The **Ticketmaster ICO penalty (£1.25m, November 2020)** could not be re-verified; only the June 2018 breach via a "third-party customer support product" was confirmed from an encyclopaedia page. The figure is left as an assumption.
- The **Dutch seven-year tax retention rule** (Belastingdienst, business.gov.nl and KVK pages all returned 404) is well known but is tagged as an assumption here; the German ten/eight/six-year rule in §147 AO was verified.
- The **ESPR 2025–2030 working plan** and the **Digital Product Passport timetable for textiles** could not be fetched from the Commission; the ESPR regulation text was verified, the plan is tagged as an assumption.
- The **Digital Fairness Act** status could not be fetched; it is noted as an expected proposal only.
- The **effective date of the FTC fake-reviews rule** (21 October 2024) could not be read from the Federal Register; the FTC press release of 14 August 2024 was verified.
- No official EU or Dutch statistic on card testing or account takeover was found; vendor and security-press figures are used and labelled.
- Nothing in this brief about Katapull or any other named company relies on non-public material.

---

## PART 1: Security threats and controls

### 1.1 The threat list, in the attacker's order of preference

Commerce platforms attract automated abuse because they expose three things an attacker can monetise without breaking in: a payment form, a login form and a catalogue. OWASP's Automated Threat Handbook names the patterns, and its identifiers are a useful shared vocabulary for chapter 34:

- **OAT-001 Carding**: "Multiple payment authorisation attempts to verify the validity of bulk stolen payment card data." Partial card data with unknown expiry or CVC is OAT-010 Card Cracking; using validated cards to buy goods is OAT-012 Cashing Out [VERIFIED: https://owasp.github.io/www-project-automated-threats-to-web-applications/assets/oats/EN/OAT-001_Carding, n.d., accessed 2026-11].
- The same handbook lists OAT-002 Token Cracking (coupon and voucher codes), OAT-005 Scalping, OAT-008 Credential Stuffing, OAT-011 Scraping, OAT-019 Account Creation and OAT-021 Denial of Inventory, among 21 threat events [VERIFIED: same page].
- **Credential stuffing** is "the automated injection of stolen username and password pairs" to "fraudulently gain access to user accounts"; OWASP names multi-factor authentication as a primary countermeasure [VERIFIED: https://community.owasp.org/attacks/Credential_stuffing, n.d., accessed 2026-11].

**For newcomers.** *Card testing (carding)*: an attacker runs many small payments or card-save attempts to find which stolen card numbers still work. *Credential stuffing*: trying username/password pairs leaked from one site on another, at machine speed. *Account takeover (ATO)*: any route by which an attacker ends up logged in as a real customer or staff member.

### 1.2 Card testing: what the PSPs say

Stripe's documentation is the clearest public description:

- "Card testing is a type of fraudulent activity where someone tries to determine whether stolen card information is valid so that they can use it to make purchases." Other names are "carding", "account testing", "enumeration" and "card checking" [VERIFIED: https://docs.stripe.com/disputes/prevention/card-testing, n.d., accessed 2026-11].
- Attackers prefer **card setup** (saving a card) to payments because setup authorisations "don't typically show up on cardholder statements"; when they do pay, they use small amounts [VERIFIED: same page].
- Consequences listed by Stripe: disputes and early fraud warnings, **higher decline rates that persist after the attack** ("A high decline rate might damage the reputation of your business with card issuers and card networks"), extra authorisation and dispute fees, infrastructure strain, and polluted business data [VERIFIED: same page].
- Symptoms: a spike in failed or blocked payments, a spike in HTTP 402 responses, and low-value payments "often with nonsensical customer names and emails" [VERIFIED: same page].
- Stripe states that "simple firewall rules or filters based on a single heuristic such as IP addresses are usually not sufficient"; its hosted Payment Element and Checkout carry "rate limiters, AI models, CAPTCHA triggers"; merchants on custom integrations should add CAPTCHA (server-side validated), require login or session validation before payment, add rate limits (for example on new customers per IP per day), limit cards per account, and avoid retrying cards saved by fraudulent customers because "this repeats the original attack" [VERIFIED: same page].
- Leaked **secret keys** are a direct card-testing vector: "When your credentials are leaked or stolen, card testers can create payments and set up cards using your secret key" [VERIFIED: same page].

Adyen's equivalent knowledge-hub page returned 404 in this session; its PCI guide confirms the same division of labour (see 1.6). [ASSUMPTION/JUDGEMENT] Every major PSP offers velocity rules and automated card-testing suppression on its hosted components; the merchant's residual exposure is on any endpoint it builds itself that can trigger an authorisation.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Card testing is the clearest argument for keeping the authorisation call behind a PSP-hosted component and a rate-limited, authenticated path, not a bare server endpoint that any script can hit. Starting: use the hosted checkout and accept the PSP's defaults. Growing: add CAPTCHA and velocity rules the moment guest checkout or a headless storefront exposes an authorisation endpoint. Omnichannel: treat card-testing detection as an operational alert (402 spike, decline rate) with a runbook (block, refund, rotate keys). Group: centralise PSP accounts and key management so a leaked key in one brand cannot generate authorisations for all.

### 1.3 Account takeover, bots and scraping: the numbers (with care)

- Imperva's 2025 Bad Bot Report page states that "automated traffic has surpassed human activity, accounting for 51% of all web traffic", with "bad bots now making up 37% of all internet traffic"; it gives no retail-specific measurement, only a single customer testimonial [VERIFIED: https://www.imperva.com/resources/resource-library/reports/2025-bad-bot-report/, n.d. (2025 edition), accessed 2026-11] ⚠ vendor figure.
- Akamai's *State of the Internet: Digital Fraud and Abuse Report 2025* reported a "300% year-over-year surge in AI-driven bot traffic" and that "The commerce industry logged more than 25 billion bot requests in a two-month span" [WIDELY REPORTED: https://www.securityinfowatch.com/cybersecurity/press-release/55327981/akamai-reports-300-surge-in-ai-bot-traffic-disrupting-digital-businesses, 2025] ⚠ vendor press release relayed by trade press.
- Cloudflare Radar's 2025 year-in-review returned 403 in this session; no Cloudflare figure is used.

[ASSUMPTION/JUDGEMENT] Vendor bot statistics measure the vendor's own customer base and are not population estimates; writers should quote them as "a vendor report says" and never as a market fact. The durable, source-independent point is that automated traffic is a majority of requests on many commerce sites, and that scraping (price and stock), inventory hoarding (carts held during drops), scalping and credential stuffing are economically rational for attackers because the catalogue, cart and login are public.

**For newcomers.** *Bot management*: a service (CDN or edge) that classifies requests as human, good bot or bad bot from signals such as fingerprint, behaviour and reputation, and then blocks, challenges or rate-limits. *Rate limiting*: capping how many requests a client may make per unit time to an endpoint. *Scraping*: automated copying of catalogue, price and availability data.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Inventory-hoarding bots turn the cart's reservation model into an attack surface: the longer a cart holds stock, the cheaper denial of inventory becomes (link to the availability chapter). Scraping is often tolerated for SEO and comparison engines, so the control is selective (challenge on cart and checkout, allow on product pages). Starting: the hosted platform's built-in bot filtering. Growing: a CDN with bot management in front of the storefront and the login. Omnichannel: per-endpoint policies (login, cart, checkout, APIs) and a reservation TTL that assumes abuse. Group: shared edge policy and a central security team.

### 1.4 Web skimming (Magecart) and the two British penalties

- **British Airways (2018 breach, 2020 penalty).** An attacker first entered BA's network on 22 June 2018 using a stolen third-party (Swissport) login without multi-factor authentication, found a saved privileged credential, and between 14 and 25 August 2018 added 22 lines of JavaScript to the payment pages that sent customers' card details to an attacker-controlled site. Roughly 429,612 people's data was potentially accessible; about 244,000 had names, addresses, card numbers and CVVs exposed. The ICO announced an intended fine of £183.39m in 2019 and issued a final £20m penalty on 16 October 2020 (a £30m starting figure reduced for mitigation and COVID-19 hardship). The ICO cited "poor security arrangements"; card details had also been logged unnecessarily since December 2015 [WIDELY REPORTED: https://en.wikipedia.org/wiki/British_Airways_data_breach, 2020 (citing the ICO penalty notice of 16 October 2020)] **(evidence age: 2018 incident)**.
- **Ticketmaster (2018).** In June 2018 Ticketmaster told 40,000 UK customers it had found "malicious software" on a third-party customer-support product it used; customers who bought tickets between February and June 2018 might have been affected [WIDELY REPORTED: https://en.wikipedia.org/wiki/Ticketmaster, 2018 section, accessed 2026-11]. [ASSUMPTION/JUDGEMENT] The ICO's £1.25m penalty of November 2020 for this breach, and the finding that a bank had warned Ticketmaster months earlier, are widely reported but could not be re-verified in this session (ICO site blocked).

The lesson that survives both: the skimmer did not break the PSP; it ran in the shopper's browser on the merchant's page, loaded by a script the merchant (or a vendor) put there.

**For newcomers.** *Web skimming / Magecart*: malicious JavaScript on a checkout page that copies what the shopper types into the card fields and sends it to the attacker; "Magecart" is the collective name for the groups doing it. *Content Security Policy (CSP)*: an HTTP header that tells the browser which script sources a page may load. *Subresource Integrity (SRI)*: a hash on a script tag so the browser refuses a changed file.

### 1.5 PCI DSS v4.0.1 and the two script requirements

- PCI DSS v4.0.1 was published on 11 June 2024 as a limited revision; "PCI DSS v4.0 will be retired on 31 December 2024"; "This limited revision does not impact the effective date of these new requirements" (31 March 2025) [VERIFIED: https://blog.pcisecuritystandards.org/just-published-pci-dss-v4-0-1, published 2024-06-11].
- Requirements **6.4.3** (payment-page scripts authorised, integrity-checked and inventoried with a business justification) and **11.6.1** (a change-and-tamper detection mechanism for payment pages and security-relevant HTTP headers) "address e-skimming attacks"; they were best practice until 31 March 2025 and required after. The Council **removed 6.4.3 and 11.6.1 from SAQ A** but added an SAQ A eligibility criterion that the merchant confirm its site is "not susceptible to attacks from scripts that could affect the merchant's e-commerce systems" (self-confirmed, via a third party, or via the compliant payment processor); "these requirements were only removed from SAQ A, and they are still in the standard" [VERIFIED: https://blog.pcisecuritystandards.org/coffee-with-the-council-podcast-guidance-for-pci-dss-e-commerce-requirements-effective-after-31-march-2025, published 2025-03-26].
- Adyen's implementation guidance for merchants who are not SAQ A-eligible: deploy a CSP first in report-only mode, then blocking with `script-src` and `frame-src`; keep a script inventory with business reasons (Adyen, Google Pay, PayPal domains plus the merchant's own); use SRI on Adyen-hosted scripts; collect CSP violation reports as the 11.6.1 alert source ("These events are considered valid alerts and 'indicators of compromise'"). The 3-D Secure script process is exempted from 6.4.3. The page says it "does not apply if you are eligible for Self-Assessment Questionnaire A (SAQ A)" [VERIFIED: https://docs.adyen.com/development-resources/pci-dss-compliance-guide/script-security/, n.d., accessed 2026-11].
- Stripe's security guide makes the general point: "Including JavaScript from other sites makes your security dependent on theirs"; it also requires TLS 1.2+ on payment pages, webhook signature verification and allowlisting Stripe's IPs [VERIFIED: https://docs.stripe.com/security/guide, n.d., accessed 2026-11].

### 1.6 PCI DSS scope, SAQ types, hosted fields and shared responsibility

- Stripe's PCI guide (Dutch-language edition read; translated): merchant levels are set by card volume (Level 1 above 6 million Visa or Mastercard transactions a year; Level 2 1–6 million; Levels 3–4 below), and the SAQ follows the integration: **SAQ A** for Checkout or Elements ("So customers' card data never reaches your servers"), **SAQ A-EP** for a card form hosted on the merchant's own site with Stripe.js v2, SAQ C for terminals, SAQ C-VT for manual dashboard entry, and **SAQ D** for a direct API integration, "the most challenging SAQ there is" [VERIFIED: https://stripe.com/guides/pci-compliance, n.d., accessed 2026-11].
- Stripe: "PCI compliance is a shared responsibility and applies to both Stripe and your business"; handling raw PANs can mean meeting "more than 300 security controls"; card brand, last four digits and expiry returned by the API are out of scope and may be stored [VERIFIED: https://docs.stripe.com/security/guide, n.d., accessed 2026-11].
- Adyen: "Adyen is solely responsible for the security of cardholder data only as soon as Adyen receives the data"; "You are responsible for making sure that cardholder data is secure and protected before the data reaches Adyen"; merchants must hold each service provider's Attestation of Compliance and manage them under requirement 12.8; "PCI DSS is not a single event, but a continuous, ongoing process" [VERIFIED: https://docs.adyen.com/development-resources/pci-dss-compliance-guide/, n.d., accessed 2026-11].
- **Shopify**: "Shopify is certified Level 1 PCI DSS compliant", with SOC 2 Type II and SOC 3 reports; on privacy, "Shopify does what it can to set you up for success, but there are also steps you will need to take on your own" [VERIFIED: https://www.shopify.com/security, n.d., accessed 2026-11]. Its PCI page says the certification "extends by default to all stores powered by Shopify" and covers the store, cart and hosting [VERIFIED: https://www.shopify.com/pci-compliant, n.d., accessed 2026-11].
- **BigCommerce (Commerce)**: "maintains Level 1 PCI DSS Attestations of Compliance as both a Merchant and a Service Provider", with SOC 1/2/3 and ISO/IEC 27001:2022, 27017, 27018, 27701, 22301 and 42001:2023 listed; the responsibility split is stated only at a high level ("You stay in control—while we ensure the platform beneath you stays trusted") [VERIFIED: https://security.bigcommerce.com/, n.d., accessed 2026-11] ⚠ certification lists change.
- **Adobe Commerce on cloud infrastructure** publishes an explicit shared-responsibility model: Adobe maintains secure core code, hardens the OS, sets global WAF rules and "maintains PCI certification for the infrastructure and services"; the merchant secures "custom code and integrations with third-party applications", applies "security and other patches to all custom extensions and code", applies core patches ("applying patches is the merchant's responsibility"), manages user access, keeps dependencies on supported versions and handles its own incidents; the cloud and CDN providers secure network, hypervisor, data centres and CDN WAF [VERIFIED: https://experienceleague.adobe.com/en/docs/commerce-operations/security-and-compliance/shared-responsibility, n.d., accessed 2026-11].

| Integration pattern | Who sees the PAN | Typical SAQ (per Stripe/Adyen guidance) | What the merchant still owns |
| --- | --- | --- | --- |
| PSP-hosted checkout page (redirect) | PSP only | SAQ A | Site integrity (script susceptibility statement), admin access, order data |
| Hosted fields / iframe components (Elements, Drop-in) | PSP only; merchant page frames the fields | SAQ A, if eligibility criteria met | Everything on the page around the iframe: CSP, script inventory, headers |
| Merchant-hosted form posting via PSP JS | Merchant page collects, PSP tokenises | SAQ A-EP | Page security, scripts, tamper detection (6.4.3, 11.6.1) |
| Direct API with raw card data | Merchant servers | SAQ D or full RoC | Full cardholder-data environment |

[ASSUMPTION/JUDGEMENT] The table is the analyst's synthesis of the two PSP guides; the SAQ actually required is set by the acquirer, not by the PSP's documentation.

**For newcomers.** *PCI DSS*: the card brands' security standard for anyone who stores, processes or transmits card data; "scope" is the set of systems it applies to. *SAQ*: Self-Assessment Questionnaire, the form a smaller merchant completes to attest compliance; SAQ A is the lightest, SAQ D the heaviest. *Hosted fields*: card input boxes served by the PSP inside an iframe on the merchant's page, so the card number never touches the merchant's code or servers.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] The whole design goal is to keep the PAN out of the merchant's systems: tokens in, never card numbers. Starting: hosted checkout, SAQ A, nothing to build. Growing: hosted fields in a custom checkout; the CSP and script inventory become real work. Omnichannel: terminals (SAQ C / P2PE) and multiple PSPs; the Attestation-of-Compliance file for every provider is an asset to maintain. Group: one PCI programme across brands, or a tokenisation layer (network tokens or a PSP-agnostic vault) so the group is not locked to one PSP's tokens.

### 1.7 Admin compromise, MFA, API keys and secrets

- Shopify: staff "can set up two-step authentication for their own individual accounts"; "The store owner can't activate two-step authentication for any other staff member"; Shopify may require it on an account, in which case it "can't be turned off while it applies"; Shopify Plus organisations can require a secure sign-in method for all users; SMS can no longer be newly set up; and for Shopify Payments, "Without two-step authentication activated, your account will be less secure and your payouts might be placed on hold" [VERIFIED: https://help.shopify.com/en/manual/your-account/account-security/two-step-authentication, n.d., accessed 2026-11].
- Stripe's key guidance: "Never put secret API keys in source code" ("Bad actors continuously scan public repositories for Stripe API keys"); use a secrets vault or environment variables; use **restricted keys** with least privilege (for example read-only dispute access for a third party); rotate periodically; restrict keys by IP, ASN or country; audit request logs; treat any exposure as compromise and rotate immediately; Stripe may proactively deactivate detected exposed keys [VERIFIED: https://docs.stripe.com/keys-best-practices, n.d., accessed 2026-11].
- The British Airways entry point was a third-party login without MFA [WIDELY REPORTED: Wikipedia, as above].

**For newcomers.** *MFA / two-step authentication*: a second proof (app code, security key, passkey) beyond the password. *Restricted API key*: a credential limited to specific API resources and permissions. *Secrets vault*: a service that stores credentials outside the code and logs every access.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] The commerce admin is the highest-value login on the estate: it can change payout accounts, add scripts to the checkout and export customers. Starting: MFA on every admin and PSP login, no shared accounts. Growing: SSO with enforced MFA, restricted keys per integration, a vault, rotation. Omnichannel: per-system service accounts for every integration (OMS, WMS, ERP, marketplace connectors) so a leak is attributable and revocable. Group: central identity provider, key inventory, and a rule that no integration may hold a key broader than its job.

### 1.8 App, script and platform supply-chain risk

- **Polyfill.io (June 2024).** Sansec reported on 25 June 2024 that cdn.polyfill.io, embedded by "100K+ sites", had been bought by a Chinese company in February 2024 together with its GitHub account and was injecting malware that redirected mobile users to a betting site via a fake Google Analytics domain; the code evaded detection by skipping admin users and delaying when analytics tools were present. Sansec's advice: remove all polyfill.io references and "Use CSP monitoring to gain visibility into the code your users load" [VERIFIED: https://sansec.io/research/polyfill-supply-chain-attack, published 2024-06-25].
- **CosmicSting (CVE-2024-34102, Adobe Commerce/Magento, 2024).** Sansec describes a CVSS 9.8 flaw that lets attackers "read any of your files, such as passwords and other secrets", forge API access and inject scripts; Adobe released the fix on 11 June (initially rated low severity, raised to critical on 8 July), with a hotfix on 21 August invalidating old encryption keys; Sansec counted campaigns breaching thousands of stores in single days in October and November [VERIFIED: https://sansec.io/research/cosmicsting, n.d. (2024 timeline), accessed 2026-11].
- The two lessons for Part VIII: a third-party script is third-party code with the shopper's session, and a self-hosted platform's security is bounded by the merchant's patch cadence (see Adobe's shared-responsibility statement in 1.6).

**For newcomers.** *Supply-chain risk*: the risk that code you did not write (an app, a plugin, a CDN-hosted script) is compromised and runs with your privileges. *Patch cadence*: how fast a merchant applies vendor security fixes.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Hosted SaaS platforms remove the patching burden but not the app-and-script burden; self-hosted platforms add both. Starting: install few apps, remove unused ones. Growing: a script inventory (PCI 6.4.3 as a forcing function) and a CSP. Omnichannel: app review as a procurement step (data access, webhooks, scopes), staging for app updates, dependency pinning in headless front ends. Group: an allow-list of vendors and a central CSP/SRI policy.

### 1.9 Refund abuse, coupon abuse and incident response

- NRF and Happy Returns projected US retail returns at "$890 billion in 2024" and found "A majority (93%) of retailers said retail fraud and other exploitive behavior is a significant issue for their business" [VERIFIED: https://nrf.com/research/2024-consumer-returns-retail-industry, published 2024-12-05] (survey of retailers; no loss figure given).
- Coupon abuse is OAT-002 Token Cracking in OWASP's taxonomy (see 1.1).
- [ASSUMPTION/JUDGEMENT] Refund and coupon abuse are policy-abuse problems rather than intrusion problems: the controls are in the order and returns systems (refund-to-original-method only, inspection before refund, one-time codes bound to a customer, velocity on code redemptions) and in customer identity (chapter 27), not at the network edge. Incident response for commerce should pre-write three runbooks: card-testing wave, skimmer found on checkout, admin account compromised.

---

## PART 2: Privacy and customer data

### 2.1 Controller, processor and the commerce supply chain

- GDPR Art. 4(7): a "controller" is the body which "alone or jointly with others, determines the purposes and means of the processing of personal data"; Art. 4(8): a "processor" is a body "which processes personal data on behalf of the controller". The GDPR applies from 25 May 2018 (Art. 99(2)) [VERIFIED: https://publications.europa.eu/resource/celex/32016R0679, published 2016-05-04].
- Art. 28 requires the processor relationship to be governed by a contract and sets its contents (see Art. 28(3)); the fine ceiling for the core infringements is "up to 20 000 000 EUR, or in the case of an undertaking, up to 4 % of the total worldwide annual turnover" (Art. 83(5)) [VERIFIED: same text].
- EDPB Guidelines 07/2020 (version 2.0, adopted 7 July 2021) draw the line: "Decisions on the purpose of the processing are clearly always for the controller to make"; "Essential means" (which data, for how long, who receives it, whose data) "are to be determined by the controller", while "Non-essential means" ("the choice for a particular type of hard- or software or the detailed security measures") "may be left to the processor to decide on" [VERIFIED: https://www.edpb.europa.eu/system/files/2023-10/EDPB_guidelines_202007_controllerprocessor_final_en.pdf, published 2021-07-07].

Applied to commerce [ASSUMPTION/JUDGEMENT, following the EDPB tests]: the merchant is the controller of its customers' data; the hosted commerce platform, the PSP (for the merchant's order data, though PSPs are usually independent controllers for the payment itself), the 3PL, the e-mail service and most apps are processors; a marketplace is a controller for the marketplace's own customer relationship; a carrier is typically an independent controller for the delivery. Writers should present these as the usual outcome of the test, not as a rule.

- Platform practice: Shopify requires every App Store app to subscribe to three compliance webhooks: `customers/data_request` (the app must provide the customer's data to the store owner), `customers/redact` ("Shopify sends the payload 10 days after the deletion request") and `shop/redact` ("48 hours after a store owner uninstalls your app"); apps must "Complete the action within 30 days of receiving the request", verify the HMAC signature, and may decline redaction where legally required to retain data [VERIFIED: https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance, n.d., accessed 2026-11].
- Shopify's protected-customer-data programme gates name, address, phone and e-mail behind approval; all apps using customer data must "Process only the minimum personal data required", "Limit your processing of personal data to the stated purposes", "respect and apply customer consent decisions", "Apply retention periods" and "Encrypt data at rest and in transit"; apps using the four identifying fields must also meet level-2 controls (backups, test/production separation, access logging, incident response) [VERIFIED: https://shopify.dev/docs/apps/launch/protected-customer-data, n.d., accessed 2026-11].

**For newcomers.** *Controller*: the organisation that decides why and how personal data is used (the merchant). *Processor*: an organisation that handles the data only on the controller's instructions (the platform, the 3PL). *Data processing agreement (DPA)*: the Art. 28 contract between them.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Every integration in the commerce map is also a data flow with a legal role. The system-of-record map (Part I) should be annotated with "controller/processor/independent controller" per system; this is the input to the DPA inventory, the records of processing, and the deletion fan-out in 2.4. Starting: the platform's standard DPA and its app vetting. Growing: a DPA register and a rule that no app is installed without one. Omnichannel: a data-flow map maintained with the integration map. Group: a privacy function that owns both.

### 2.2 Lawful bases: the order vs the marketing

- GDPR Art. 6(1) lists the bases: consent (a), contract performance (b), legal obligation (c), vital interests (d), public task (e) and legitimate interests (f) [VERIFIED: GDPR text, as above].
- The ePrivacy Directive's soft opt-in for existing customers: where a business obtains e-mail contact details "in the context of the sale of a product or a service", it "may use these electronic contact details for direct marketing of its own similar products or services provided that customers clearly and distinctly are given the opportunity to object, free of charge and in an easy manner" at collection and in each message (Art. 13(2)) [VERIFIED: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02002L0058-20091219, consolidated 2009-12-19] **(evidence age: 2002/2009 text; national transpositions differ)**.

[ASSUMPTION/JUDGEMENT] In commerce terms: order processing, delivery, invoicing and warranty rest on contract and legal obligation; fraud prevention and basic analytics usually on legitimate interests; newsletters on consent or the soft opt-in for similar products; profiling for personalised marketing and cross-site tracking on consent. The design consequence is that the order record and the marketing profile need separate lawful bases, separate retention clocks and separate deletion behaviour, even when they refer to the same person.

### 2.3 Consent, cookies and tracking: ePrivacy, the EDPB and three national regulators

- The ePrivacy rule (Art. 5(3), as amended in 2009): "the storing of information, or the gaining of access to information already stored, in the terminal equipment of a subscriber or user is only allowed on condition that the subscriber or user concerned has given his or her consent, having been provided with clear and comprehensive information", with exceptions for transmission and for services "explicitly requested" by the user [VERIFIED: https://publications.europa.eu/resource/celex/32009L0136, published 2009-12-18].
- EDPB Guidelines 05/2020 on consent (adopted 4 May 2020): "access to services and functionalities must not be made conditional on the consent of a user to the storing of information... (so called cookie walls)"; "actions such as scrolling or swiping through a webpage or similar user activity will not under any circumstances satisfy the requirement of a clear and affirmative action" [VERIFIED: https://www.edpb.europa.eu/system/files/documents/files/file1/edpb_guidelines_202005_consent_en.pdf, published 2020-05-04].
- EDPB Guidelines 2/2023 on the technical scope of Art. 5(3) (version 2.0, adopted 7 October 2024) bring **URL and pixel tracking**, **local processing** and **tracking based on IP only** within the rule: a tracking pixel's "sole purpose is to automatically establish a communication by the client to the host of the pixel"; and for IP-only tracking, "Unless the entity can ensure that the IP address does not originate from the terminal equipment of a user or subscriber, it has to take all the steps pursuant to the Article 5(3) ePD" [VERIFIED: https://www.edpb.europa.eu/system/files/documents/2024-10/edpb_guidelines_202302_technical_scope_art_53_eprivacydirective_v2_en_0.pdf, published 2024-10-07].
- **Netherlands (Autoriteit Persoonsgegevens; Dutch page, translated):** functional cookies need no consent but must be disclosed; "limited analytical cookies" with no or little privacy impact need no consent under the Telecommunicatiewet (Art. 11.7a); tracking cookies require prior information and consent; and on cookie walls, "If you refuse tracking cookies you cannot access the website or app. Refusing tracking cookies has adverse consequences for you. That is why these kinds of cookie walls are prohibited under the GDPR" [VERIFIED: https://www.autoriteitpersoonsgegevens.nl/themas/internet-slimme-apparaten/cookies, n.d., accessed 2026-11].
- **Belgium (Gegevensbeschermingsautoriteit; Dutch page, translated, last updated 17 November 2023):** only two categories are exempt from consent: strictly necessary functional cookies "such as for temporarily storing the language choice, cookie preferences or the contents of the shopping basket" and strictly necessary technical cookies (for example load-balancing session cookies); consent "is not valid if it is obtained by means of a pre-ticked box that the user must untick to refuse", and continuing to browse is not consent; cookies must be grouped by specific purpose, with own and third-party advertising/profiling as separate purposes [VERIFIED: https://www.gegevensbeschermingsautoriteit.be/burger/thema-s/internet/cookies, published 2023-11-17].
- **Germany:** the national transposition is the TDDDG (formerly TTDSG, §25); the DSK's guidance could not be fetched in this session [ASSUMPTION/JUDGEMENT; same substantive rule as above].
- **Server-side tagging** [ASSUMPTION/JUDGEMENT, following the EDPB technical-scope reading]: moving the tag manager to the merchant's own server changes who receives the data first, not whether consent is needed; the browser is still instructed to emit identifiers (cookies, pixel loads, fingerprint-like IP use), so Art. 5(3) still applies to the storage/access step and the GDPR to what follows. Writers should present server-side tagging as a data-governance improvement (the merchant controls what is forwarded), never as a consent bypass.
- **Pending reform** ⚠: the Commission's Digital Omnibus proposal (November 2025) would add Art. 88a GDPR for terminal-equipment storage and access with four no-consent purposes (transmission, requested service, audience measurement, security), require a one-click refuse, bar re-asking for six months after a refusal, and (Art. 88b) require controllers to honour "automated and machine-readable" signals that non-SME browsers must offer; one law firm's reading is that the "audience measurement" exemption is narrow and "the long-awaited end of cookie banners as such is not yet in sight" [WIDELY REPORTED: https://www.osborneclarke.com/insights/digital-omnibus-reshapes-eu-cookie-rules-leaves-banner-fatigue-largely-intact, 2025-12-10]. It is a proposal, not law.

**For newcomers.** *Consent management platform (CMP)*: the banner and the record behind it, which stores each visitor's choices per purpose and tells tags whether they may fire. *Tracking pixel*: a tiny image or script request whose only job is to tell a third party that you were here. *Soft opt-in*: the ePrivacy rule that lets a shop e-mail existing customers about similar products if every message offers an easy opt-out.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Consent is state that must travel: from the CMP to the tag layer, to the CDP or marketing platform, to the store (POS sign-ups) and to the apps. Starting: the platform's cookie banner and marketing-consent checkbox at checkout. Growing: a CMP with per-purpose consent, consent stored on the customer record, and a rule that no tool fires before consent. Omnichannel: consent as an attribute of the golden record (chapter 27) with a timestamp, source and version, synchronised to every outbound marketing system. Group: one consent model across brands and countries, with national differences (NL limited analytics exemption, BE purpose grouping) as configuration.

### 2.4 Data subject requests across many systems

- Controllers must act on access, rectification, erasure and other requests "without undue delay and in any event within one month of receipt of the request", extendable by two months for complex or numerous requests (Art. 12(3)) [VERIFIED: GDPR text, as above].
- Shopify's design (2.1) is the practical model: the platform fans a request out to every app with customer data and expects each to complete within 30 days [VERIFIED: Shopify compliance webhooks, as above].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] A deletion request on an omnichannel estate touches the commerce platform, OMS, WMS (shipping labels), ERP (invoices), PSP (payment records), carriers, marketplaces, e-mail and SMS tools, the CDP, the data warehouse, support ticketing and backups. Each has a different answer: erase, pseudonymise, or retain under a legal obligation (invoice and tax records, see 2.5; fraud evidence). The architecture need is an identity index (which systems hold this person, under which ids) and a request orchestrator that records what each system did. This is the "deletion that touches nine systems" scenario the chapter plans; nine is illustrative.

### 2.5 Retention vs tax retention

- **Germany:** §147 AO requires books, records, inventories, annual accounts and the opening balance sheet to be kept for ten years ("zehn Jahre"); accounting vouchers (Buchungsbelege) for eight years ("acht Jahre"); other records including commercial letters for six years; the period starts at the end of the calendar year of the record and does not expire while the records matter for taxes still open [VERIFIED: https://www.gesetze-im-internet.de/ao_1977/__147.html, n.d. (current text), accessed 2026-11]. [ASSUMPTION/JUDGEMENT] The eight-year voucher period dates from the 2025 Bürokratieentlastungsgesetz IV; not re-verified.
- **Netherlands:** [ASSUMPTION/JUDGEMENT] the general fiscal retention duty is seven years for basic records (ledger, debtors, creditors, stock, purchase and sales administration, payroll) and ten years for immovable property; the official pages (Belastingdienst, business.gov.nl, KVK) all returned 404 in this session, so writers should re-verify before quoting.
- **Belgium:** [ASSUMPTION/JUDGEMENT] ten years for accounting records and invoices (VAT Code Art. 60); not verified in this session.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] The order record and the invoice are tax records and outlive the customer relationship; the marketing profile does not. The clean pattern is to split the person from the transaction: keep invoices and orders with pseudonymised customer references for the fiscal period, and erase or anonymise the customer profile, addresses and behavioural data on request or at the end of their own retention period. Backups need a documented, bounded exception.

### 2.6 International transfers: DPF, SCCs and the pending appeal

- The Commission's adequacy decision for the EU-US Data Privacy Framework is Implementing Decision (EU) 2023/1795 of 10 July 2023; it concludes that "the United States ensures an adequate level of protection for personal data transferred under the EU-U.S. DPF" on the basis of certification by US organisations to the DPF Principles [VERIFIED: https://publications.europa.eu/resource/celex/32023D1795, published 2023-09-20].
- The Commission's page adds that the US safeguards "also facilitate the use of other tools, such as standard contractual clauses and binding corporate rules" [VERIFIED: https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/eu-us-data-transfers_en, n.d., accessed 2026-11].
- The modern SCCs are Commission Implementing Decision (EU) 2021/914 of 4 June 2021 [VERIFIED: https://publications.europa.eu/resource/celex/32021D0914, published 2021-06-07].
- The General Court dismissed Philippe Latombe's annulment action on 3 September 2025 (T-553/23, ECLI:EU:T:2025:831); the appeal was lodged on 31 October 2025 as Case C-703/25 P and asks the Court of Justice to set the judgment aside and annul Decision 2023/1795 [VERIFIED: https://publications.europa.eu/resource/celex/62025CN0703, published 2025-12-22 (OJ C/2025/6610)]. The General Court rejected the pleas on the Data Protection Review Court's independence and on bulk collection; law-firm advice is to keep SCCs as a contractual fallback [WIDELY REPORTED: https://www.lewissilkin.com/insights/2025/09/03/transatlantic-trouble-not-this-time-latombes-challenge-to-eu-us-data-transfers-fails, 2025-09-03] ⚠ appeal pending.

**For newcomers.** *Adequacy decision*: a Commission finding that a country's protection is good enough for data to flow without extra contracts. *SCCs*: Commission-approved contract clauses that make a transfer lawful where there is no adequacy. *DPF*: the 2023 EU-US arrangement under which certified US companies receive EU data.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Most commerce stacks transfer to the US somewhere (analytics, e-mail, support, cloud). The architecture asset is a transfer inventory keyed to the integration map, with the mechanism (DPF certification, SCCs, EU hosting) per vendor, so a court decision becomes a filter on a list rather than a discovery project.

### 2.7 Enforcement in commerce (dated)

- **British Airways, £20m, ICO, 16 October 2020** (web skimming; see 1.4) [WIDELY REPORTED: Wikipedia, 2020].
- **Amazon France Logistique, €32m, CNIL, decision 23 January 2024**, for warehouse scanner monitoring that measured work interruptions, 31-day retention of productivity data judged disproportionate, inadequate information to staff and insufficiently secured video software (Arts. 5(1)(c), 6, 12, 13, 32); the Conseil d'État later reduced the fine to €15m [WIDELY REPORTED: https://www.enforcementtracker.com/ETid-2192, 2024–2026] ⚠ reduction reported by one source.
- **Sephora, $1.2m, California Attorney General, 24 August 2022** (CCPA): Sephora let third parties install trackers on its site and app, which the AG treated as a sale of personal information without notice, and it did not honour Global Privacy Control opt-out signals; the settlement requires honouring GPC and fixing service-provider agreements [VERIFIED: https://oag.ca.gov/news/press-releases/attorney-general-bonta-announces-settlement-sephora-part-ongoing-enforcement, published 2022-08-24].
- [ASSUMPTION/JUDGEMENT] Other commerce-relevant fines are widely known but were not re-verified here: Carrefour (CNIL, 2020, retention and cookies), Amazon Europe Core (Luxembourg CNPD, 2021, €746m, advertising), Ticketmaster (ICO, 2020).

### 2.8 US state privacy laws

- The IAPP's 2025 state tracker chart lists 19 comprehensive consumer privacy laws signed, from California (2018, effective 1 January 2020) through Colorado, Connecticut, Delaware, Indiana, Iowa, Kentucky, Minnesota, Montana, Nebraska, New Hampshire, New Jersey, Oregon, Rhode Island, Tennessee, Texas, Utah and Virginia, with effective dates running to 1 January 2026 [VERIFIED: https://prod.iapp.org/media/pdf/resource_center/State_Comp_Privacy_Law_Chart.pdf, 2025 edition, accessed 2026-11] ⚠ the 2026 count may be higher; the tracker page itself was last updated 8 September 2026 [VERIFIED: https://iapp.org/resources/article/us-state-privacy-legislation-tracker/, updated 2026-09-08].
- **CCPA/CPRA** applies to for-profit businesses doing business in California that have "a gross annual revenue of over $25 million", or handle data of 100,000 or more residents or households, or derive 50% or more of revenue from selling personal information; rights include know, delete, correct, opt out of sale or sharing, limit sensitive data and non-discrimination; "one acceptable method for consumers to opt-out of sales or sharing is via a user-enabled global privacy control" [VERIFIED: https://oag.ca.gov/privacy/ccpa, n.d., accessed 2026-11].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] The US model is opt-out of "sale or sharing" plus a browser signal (GPC), where the EU model is opt-in consent; a platform serving both needs a consent/preference record that can express both states per jurisdiction, and a tag layer that reads a browser signal as well as a banner choice.

---

## PART 3: Regulation as requirements (official texts and dates of application)

### 3.1 EU consumer law: Consumer Rights Directive, Omnibus, price indication, UCPD

- **Consumer Rights Directive 2011/83/EU** (applies to contracts concluded after 13 June 2014): the consumer "shall have a period of 14 days to withdraw from a distance or off-premises contract, without giving any reason" (Art. 9(1)); if the trader fails to inform about the right, the period extends to 12 months (Art. 10); the trader must reimburse "without undue delay and in any event not later than 14 days from the day on which he is informed of the consumer's decision to withdraw" (Art. 13(1)) and may withhold reimbursement until the goods are back or proof of return is supplied (Art. 13(3)); the consumer must send the goods back within 14 days (Art. 14(1)); and if ordering means pressing a button, it "shall be labelled in an easily legible manner only with the words 'order with obligation to pay' or a corresponding unambiguous formulation" (Art. 8(2)) [VERIFIED: https://publications.europa.eu/resource/celex/32011L0083, published 2011-11-22].
- **Omnibus Directive (EU) 2019/2161** (transposition by 28 November 2021, applied from **28 May 2022**): adds Art. 6a to the Price Indication Directive, "Any announcement of a price reduction shall indicate the prior price", where "The prior price means the lowest price applied by the trader during a period of time not shorter than 30 days prior to the application of the price reduction" (Member States may shorten it for goods on sale under 30 days and for progressive reductions); makes "main parameters determining ranking" and whether reviews come from "consumers who have actually used or purchased the product" material information; blacklists stating that reviews are from real purchasers "without taking reasonable and proportionate steps to check" and "Submitting or commissioning another... to submit false consumer reviews"; and requires disclosure "that the price was personalised on the basis of automated decision-making" [VERIFIED: https://publications.europa.eu/resource/celex/32019L2161, published 2019-12-18].
- **Price Indication Directive 98/6/EC**: "The selling price and the unit price shall be indicated for all products", the unit price being "the final price, including VAT and all other taxes, for one kilogramme, one litre, one metre..." (Arts. 2–3) [VERIFIED: https://publications.europa.eu/resource/celex/31998L0006, published 1998-03-18] **(evidence age: amended by Omnibus)**.
- **UCPD 2005/29/EC** is the general unfair-practices framework the Omnibus amends; the fake-review and ranking rules above live in it [VERIFIED: Omnibus text, as above].

**For newcomers.** *Right of withdrawal*: the EU consumer's 14-day right to return a distance purchase for any reason. *Prior price (Omnibus)*: the lowest price in the 30 days before a sale, which must be shown with any discount claim. *Unit price*: price per kilo, litre or metre shown next to the selling price.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] These are requirements on data, not just on pages: the pricing system must keep a 30-day price history per SKU per country to compute the prior price; the returns system must compute the 14-day windows from the right events (delivery, withdrawal notice, receipt of goods) and release refunds within 14 days (chapter 18); the review system must record provenance (verified purchase) and expose how ranking works; the checkout button label is a localisation requirement. Starting: platform defaults, checked per country. Growing: price history in the PIM/pricing service. Omnichannel: the same rules applied on marketplaces and in store returns. Group: a regulatory calendar owner (3.12).

### 3.2 European Accessibility Act (Directive (EU) 2019/882)

- "e-commerce services" means "services provided at a distance, through websites and mobile device-based services by electronic means and at the individual request of a consumer with a view to concluding a consumer contract" (Art. 3(30)); Member States apply the measures **from 28 June 2025** (Art. 31(2)); service providers may continue to use products lawfully in use before that date until **28 June 2030** (Art. 32(1)); "Microenterprises providing services shall be exempt" (Art. 4(5)), a microenterprise employing fewer than 10 persons with turnover or balance sheet not exceeding €2m (Art. 3(23)); Annex I requires e-commerce services to provide "identification methods, electronic signatures, security, and payment services which are perceivable, operable, understandable and robust" [VERIFIED: https://publications.europa.eu/resource/celex/32019L0882, published 2019-06-07].
- The Commission's page lists the covered products and services, including e-commerce, banking services and e-books, and notes that Member States had to transpose by June 2022 [VERIFIED: https://commission.europa.eu/strategy-and-policy/policies/justice-and-fundamental-rights/disability/union-equality-strategy-rights-persons-disabilities-2021-2030/european-accessibility-act_en, n.d., accessed 2026-11].
- **US contrast:** the DOJ's ADA Title II web rule (published 24 April 2024) requires state and local governments' web content and apps to meet WCAG 2.1 AA, with compliance dates extended by an interim final rule of 20 April 2026 to 26 April 2027 (populations of 50,000 or more) and 26 April 2028 (smaller); it does not directly cover private businesses [VERIFIED: https://www.ada.gov/resources/2024-03-08-web-rule/, 2024, updated 2026]. Private-sector exposure is litigation: UsableNet counted "5,114 ADA digital accessibility lawsuits" in 2025 (3,195 federal, 1,919 in New York and California state courts), with e-commerce at 70% of filings, "36 percent of the top 500 eCommerce retailers" receiving at least one suit, and 1,427 suits against companies already sued [VERIFIED: https://info.usablenet.com/2025-year-end-digital-accessibility-lawsuit-report-plain-text, published 2025-12 (data to 15 December 2025)] ⚠ vendor count.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Accessibility is a storefront-delivery and checkout requirement (Part VII) that the EU now enforces by law and the US by lawsuit; the technical content in both is WCAG 2.1 AA. Headless storefronts and third-party checkout, payment and identity widgets must each be accessible, which makes vendor conformance statements a procurement item.

### 3.3 Digital Services Act (Regulation (EU) 2022/2065)

- The DSA applies from **17 February 2024** (Art. 93(2)). Art. 30 "Traceability of traders": platforms allowing consumers to conclude distance contracts with traders must, before the trader may sell, obtain the trader's name, address, telephone and e-mail; an identification document or electronic identification; "the payment account details of the trader"; the trade-register number; and "a self-certification by the trader committing to only offer products or services that comply with the applicable rules of Union law"; the platform must make best efforts to verify this before allowing use. Art. 25 bans interfaces designed in a way that "deceives or manipulates the recipients"; Art. 31 "Compliance by design" requires the interface to let traders provide pre-contractual, compliance and product-safety information [VERIFIED: https://publications.europa.eu/resource/celex/32022R2065, published 2022-10-27].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] For a merchant selling on marketplaces, Art. 30 is an onboarding data set it must supply and keep current per marketplace (chapter 20); for a merchant operating its own marketplace or dropship programme, it is a seller-onboarding and KYB workflow with verification and periodic re-certification. Art. 31 is why marketplace listing APIs demand manufacturer and responsible-person fields.

### 3.4 General Product Safety Regulation (Regulation (EU) 2023/988)

- Applies from **13 December 2024**. Art. 4: a product offered online is "made available on the market if the offer is targeted at consumers in the Union". Art. 19 requires every online or distance offer to "clearly and visibly indicate" (a) the manufacturer's name and postal and electronic address, (b) where the manufacturer is outside the Union, the responsible person's name and addresses, (c) "information allowing the identification of the product, including a picture of it, its type and any other product identifier", and (d) any warning or safety information in a language the consumer can easily understand. Art. 22(9) requires marketplaces to design their interface so traders can provide this information per product [VERIFIED: https://publications.europa.eu/resource/celex/32023R0988, published 2023-05-23].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] GPSR turns manufacturer identity, responsible person and safety warnings into mandatory product attributes that must be present on every channel. They belong in the PIM as structured fields (chapter 7) and must be syndicated to marketplaces; missing values should block publication.

### 3.5 Packaging and Packaging Waste Regulation (Regulation (EU) 2025/40) and EPR

- The PPWR applies from **12 August 2026** (Art. 71). Art. 45: "Producers shall have extended producer responsibility" for packaging "that they make available for the first time on the territory of a Member State"; harmonised material-composition labels apply from 12 August 2028 or 24 months after the implementing acts, whichever is later (Art. 12); recital text addresses the producer established in another Member State or third country selling by distance contract and the application of DSA Art. 30 traceability to platforms [VERIFIED: https://publications.europa.eu/resource/celex/32025R0040, published 2025-01-22].
- National registers already exist: Germany's LUCID Packaging Register states "If you are distributing packaged goods in Germany, you have to be registered with the LUCID Packaging Register", with system participation and volume reporting as further duties [VERIFIED: https://www.verpackungsregister.org/en/, n.d., accessed 2026-11]. [ASSUMPTION/JUDGEMENT] The Dutch (Verpact/Afvalfonds) and Belgian (Fost Plus) schemes impose equivalent registration and fee reporting; not verified here.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] EPR fees are computed from packaging weight by material per country of sale, which means the product and the shipment need packaging data (the WMS knows the carton, the PIM knows the sales packaging) and the order needs the destination country; cross-border sellers need a register number per country. This is a reporting data product, not a storefront feature.

### 3.6 Ecodesign for Sustainable Products Regulation (Regulation (EU) 2024/1781) and the Digital Product Passport

- The ESPR defines the "digital product passport" as "a set of data specific to a product that includes the information specified in the applicable delegated act... accessible via electronic means through a data carrier" (Art. 2(28)); the Commission must set up a registry of unique identifiers by **19 July 2026** (Art. 13); and "From 19 July 2026, the destruction of unsold consumer products as listed in Annex VII shall be prohibited" (Art. 25(1); Annex VII covers apparel, clothing accessories and footwear), with disclosure duties on discarded unsold products for all but micro and small enterprises [VERIFIED: https://publications.europa.eu/resource/celex/32024R1781, published 2024-06-28].
- [ASSUMPTION/JUDGEMENT] ⚠ The Commission's 2025–2030 working plan (April 2025) names textiles and apparel, furniture, tyres, mattresses, iron and steel and aluminium as priorities, with the first product delegated acts (textiles) expected around 2027 and DPP obligations following their transition periods; the plan could not be fetched in this session and writers must verify dates before stating them.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] The DPP will make product identity (GTIN, model, batch) and a resolvable identifier on the item a data obligation: the PIM becomes the passport's source and the returns/disposition flow must prove unsold apparel was not destroyed (chapter 18). Apparel brands are first in line.

### 3.7 NIS2 and the Dutch Cyberbeveiligingswet

- NIS2 (Directive (EU) 2022/2555) applies to entities of a type in Annex I or II "which qualify as medium-sized enterprises" or larger (Art. 2(1)); Annex II "Digital providers" lists "Providers of online marketplaces"; Member States had to apply their measures from 18 October 2024; significant incidents require an early warning "within 24 hours", an incident notification "within 72 hours" and a final report within a month (Art. 23(4)) [VERIFIED: https://publications.europa.eu/resource/celex/32022L2555, published 2022-12-27].
- The Netherlands: the Eerste Kamer approved the Cyberbeveiligingswet (Cbw) and the Wet weerbaarheid kritieke entiteiten on 7 July 2026; both entered into force on **15 August 2026**; the Cbw replaces the Wbni, covers essential and important entities in 18 sectors, and imposes registration via mijn.ncsc.nl ("This is mandatory as of 15 August", translated), a duty of care, a reporting duty and board accountability with training [VERIFIED: https://www.rijksoverheid.nl/actueel/nieuws/2026/07/07/cyberbeveiligingswet-en-wet-weerbaarheid-kritieke-entiteiten-vanaf-15-augustus-2026-van-kracht, published 2026-07-07].
- Related: the Cyber Resilience Act (Regulation (EU) 2024/2847) applies from 11 December 2027, with vulnerability and incident reporting (Art. 14) from 11 September 2026 [VERIFIED: https://publications.europa.eu/resource/celex/32024R2847, published 2024-11-20].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] An ordinary retailer is usually out of NIS2 scope; a marketplace operator, a commerce SaaS vendor or a managed-service provider of medium size or larger is in it. For the merchant, NIS2 arrives through suppliers: the platform, 3PL software and integration vendors will pass on incident-notification and supply-chain-security clauses, so the 24/72-hour clocks become contract terms the merchant's incident process must meet.

### 3.8 AI Act (Regulation (EU) 2024/1689) as amended by the Digital Omnibus on AI (Regulation (EU) 2026/1744)

- Original Art. 113: general application from 2 August 2026; Chapters I–II (prohibitions, AI literacy) from 2 February 2025; GPAI, governance and penalties from 2 August 2025. Art. 50(1): providers must ensure that AI systems "intended to interact directly with natural persons" inform people "that they are interacting with an AI system, unless this is obvious"; Art. 50(2): generated content must be "marked in a machine-readable format and detectable as artificially generated" [VERIFIED: https://publications.europa.eu/resource/celex/32024R1689, published 2024-07-12].
- The Digital Omnibus on AI, Regulation (EU) 2026/1744 of 8 July 2026 (OJ 24 July 2026, in force on the third day), moves high-risk obligations to **2 December 2027** for Annex III systems and **2 August 2028** for Annex I systems; new prohibitions in Art. 5(1)(ba)/(bb) apply from 2 December 2026; generative systems placed on the market before 2 August 2026 must meet Art. 50(2) by 2 December 2026 [VERIFIED: https://publications.europa.eu/resource/celex/32026R1744, published 2026-07-24].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] For commerce, the live obligations are transparency ones: a shopping assistant or support bot must say it is a bot (Art. 50(1)), and AI-generated product images or copy need machine-readable marking (50(2)). Most recommendation, search and fraud models are not high-risk; worker-monitoring features in warehouse software (Annex III 4(b)) are the exception to watch. Chapter 45 should present agentic commerce against these dates.

### 3.9 Data Act (Regulation (EU) 2023/2854)

- Applies from **12 September 2025** (Art. 50); the switching chapter applies to contracts concluded after that date and from 12 September 2027 to older contracts; switching charges are defined and phased out (Art. 29) [VERIFIED: https://publications.europa.eu/resource/celex/32023R2854, published 2023-12-22].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] For merchants, the Data Act is an exit right: SaaS commerce, OMS and WMS contracts signed after September 2025 must allow switching with bounded notice and data retrieval. Writers in Part X (replatforming) should cite it as the legal floor under the "can we get our data out" question.

### 3.10 Payments: PSD2 SCA, the RTS, PSD3/PSR status

- PSD2 (Directive (EU) 2015/2366) applied from 13 January 2018 (Art. 115(2)); Art. 97 requires strong customer authentication when the payer initiates an electronic payment [VERIFIED: https://publications.europa.eu/resource/celex/32015L2366, published 2015-12-23].
- The RTS (Delegated Regulation (EU) 2018/389) applies from 14 September 2019 and allows exemptions for low-value remote transactions (not exceeding EUR 30, Art. 16) and for transaction risk analysis where the PSP's fraud rate is below the reference rate and the amount is under the exemption threshold value, provided no abnormal spending, unusual device, malware, known fraud scenario, abnormal location or high-risk payee is detected (Art. 18) [VERIFIED: https://publications.europa.eu/resource/celex/32018R0389, published 2018-03-13].
- **PSD3/PSR** ⚠: proposed June 2023; Council mandate 18 June 2025; provisional agreement with Parliament on 27 November 2025; Coreper confirmation 22 April 2026; both files still listed as open in the Presidency's state of play for the 9 November 2026 ECOFIN [VERIFIED: https://data.consilium.europa.eu/doc/document/ST-15005-2026-INIT/en/pdf, published 2026-10-29]. The agreement's content as summarised by Parliament: PSPs that fail to implement appropriate fraud prevention "will be liable for covering customers' losses"; PSPs "will be required to check that a payee's name and unique identifier match" and refuse on mismatch; online platforms must compensate PSPs if they were notified of fraudulent content and did not remove it; all charges disclosed before payment; retailers may offer €100–150 cash withdrawals without purchase [VERIFIED: https://www.europarl.europa.eu/news/en/press-room/20251121IPR31540/payment-services-deal-more-protection-from-online-fraud-and-hidden-fees, published 2025-11-21].
- Instant Payments Regulation (EU) 2024/886: euro-area PSPs had to receive instant credit transfers by 9 January 2025 and apply verification of payee by 9 October 2025 [VERIFIED: https://publications.europa.eu/resource/celex/32024R0886, published 2024-03-19].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] SCA is why the European checkout must be designed for a 3-D Secure redirect or challenge in the middle of payment, and why saved-card and agent-initiated flows need a merchant-initiated-transaction or exemption strategy (chapters 12 and 45). PSD3/PSR will not change that mechanism but shifts fraud liability toward PSPs and adds verification of payee to bank transfers, which affects invoice and SEPA flows in B2B.

### 3.11 E-invoicing mandates at a glance

- **Belgium:** from 1 January 2026 "all Belgian enterprises liable to VAT will have to use structured electronic invoices" between each other, exchanged over Peppol; "Sending a PDF invoice by e-mail or via a platform will no longer be enough"; invoices to private individuals are out of scope, but B2C-only businesses must still be able to receive [VERIFIED: https://einvoice.belgium.be/en/article/structured-electronic-invoices-between-companies-are-compulsory-2026, published 2024-09-18]. Fines for lacking the technical means to issue and receive: €1,500 (first), €3,000 (second), €5,000 (following), under the Royal Decree of 8 July 2025 [VERIFIED: https://einvoice.belgium.be/en/FAQ/specific-questions-about-e-invoicing, n.d., accessed 2026-11].
- **Germany** (BMF FAQ, translated): e-invoices are the rule for domestic B2B supplies from 1 January 2025; "In the period from 1 January 2025 to 31 December 2026 all invoice issuers may choose to issue another invoice instead of an e-invoice"; "With a prior-year turnover of the issuer up to 800,000 euro this period extends to the end of 2027"; EDI procedures that are not e-invoices may be used until the end of 2027; B2C supplies are excluded; XRechnung and ZUGFeRD from 2.0.1 (except MINIMUM and BASIC-WL) qualify [VERIFIED: https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html, n.d., accessed 2026-11].
- **Netherlands** ⚠: on 11 September 2026 the cabinet chose mandatory e-invoicing for domestic and cross-border B2B from **1 July 2030** and domestic reporting from **1 July 2031**, with the small-business scheme (turnover up to €20,000) exempt; a draft bill goes to consultation "this autumn" and to the Tweede Kamer "before summer 2027" (translated) [VERIFIED: https://www.rijksoverheid.nl/actueel/nieuws/2026/09/11/kabinet-kiest-voor-invoering-e-facturatie-en-rapportage-voor-bedrijven, published 2026-09-11].
- **ViDA:** Council Directive (EU) 2025/516 amends the VAT Directive with effect from 1 July 2030 for the EU-wide e-invoicing and digital-reporting rules (Art. 5 provisions; "They shall apply those measures from 1 July 2030") [VERIFIED: https://publications.europa.eu/resource/celex/32025L0516, published 2025-03-25].

(Chapter 22 owns the EDI and Peppol detail; this brief supplies only the dates.)

### 3.12 Geo-blocking and the Right to Repair

- **Geo-blocking Regulation (EU) 2018/302** applies from 3 December 2018; a trader "shall not... block or limit a customer's access to the trader's online interface for reasons related to the customer's nationality, place of residence or place of establishment", nor redirect without explicit consent, and must keep the originally requested version accessible (Art. 3) [VERIFIED: https://publications.europa.eu/resource/celex/32018R0302, published 2018-03-02] **(evidence age: 2018)**.
- **Right to Repair Directive (EU) 2024/1799**: Member States apply the measures from **31 July 2026**; the amendment to the Sale of Goods Directive applies to contracts concluded after that date; manufacturers must repair goods subject to Union repairability requirements and may not refuse for purely economic reasons; a European online repair platform with national sections is set up [VERIFIED: https://publications.europa.eu/resource/celex/32024L1799, published 2024-07-10].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Geo-blocking means country redirects must be consent-based and the storefront must remain reachable; it does not oblige cross-border delivery. Right to Repair touches the after-sales and returns flow for covered product categories (mainly electronics and appliances), so apparel merchants are mostly affected only through the extended legal-guarantee logic.

### 3.13 United States: sales tax, marketplace sellers, FTC rules

- **South Dakota v. Wayfair (21 June 2018, 5–4)** overruled the physical-presence rule of *Quill*; South Dakota's law reached sellers delivering more than $100,000 of goods or services into the state or 200 or more separate transactions a year; "the physical presence rule of Quill is unsound and incorrect" [VERIFIED: https://www.law.cornell.edu/supremecourt/text/17-494, published 2018-06-21]. [ASSUMPTION/JUDGEMENT] Nearly every state now applies economic-nexus thresholds and "marketplace facilitator" laws under which the marketplace collects and remits; thresholds vary by state and change.
- **INFORM Consumers Act**, effective 27 June 2023: a high-volume third-party seller is one with "200 or more separate sales or transactions" of new or unused consumer products and "$5,000 or more in gross revenues" in any continuous 12-month period in the past 24 months; marketplaces must collect bank account, tax ID and contact information within 10 days, verify it, require annual certification, and suspend non-responders after a 10-day notice; sellers with "annual gross revenues of $20,000 or more" must have full name, physical address and contact details disclosed on listings; violations carry "civil penalties of $53,088 per violation for online marketplaces" and state attorneys general may enforce [VERIFIED: https://www.ftc.gov/business-guidance/resources/informing-businesses-about-inform-consumers-act, n.d., accessed 2026-11] ⚠ penalty amount is inflation-adjusted.
- **FTC fake-reviews rule**: announced 14 August 2024 (5–0 vote); bans fake or AI-generated reviews, "compensation or other incentives conditioned on the writing of consumer reviews" with a particular sentiment, undisclosed insider reviews, company-controlled "independent" review sites, review suppression by "unfounded or groundless legal threats, physical threats, intimidation" and buying "fake indicators of social media influence"; effective 60 days after Federal Register publication, with civil penalties for knowing violators [VERIFIED: https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials, published 2024-08-14]. [ASSUMPTION/JUDGEMENT] The rule is codified at 16 CFR Part 465 and took effect 21 October 2024; the Federal Register could not be fetched.
- **Negative option / "click to cancel"** ⚠: the FTC's 2024 rule was vacated by the Eighth Circuit in July 2025 on procedural grounds, which reinstated the 1973 Negative Option Rule covering only prenotification plans; in March 2026 the FTC issued a new Advance Notice of Proposed Rulemaking asking whether to extend the rule to automatic renewals, continuity plans and free-trial conversions; "No new requirements take effect today"; state automatic-renewal laws continue to multiply [WIDELY REPORTED: https://www.jdsupra.com/legalnews/ftc-relaunches-negative-option-6871835/, 2026-03-13]. [ASSUMPTION/JUDGEMENT] ROSCA (2010) remains the federal basis for online subscription enforcement.
- **ADA litigation**: see 3.2.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] US sales tax is a tax-engine problem (chapter 15): nexus per state, product taxability, marketplace-collected vs seller-collected. INFORM is a marketplace onboarding and disclosure data set mirroring DSA Art. 30. Subscription commerce in the US needs a cancellation path as easy as sign-up regardless of the federal rule, because state laws require it.

### 3.14 Pending EU files to watch ⚠

- **Digital Omnibus (data)** — proposal of November 2025 amending GDPR, ePrivacy, Data Act and NIS2 reporting (see 2.3) [WIDELY REPORTED: Osborne Clarke, 2025-12-10].
- **Digital Fairness Act** — [ASSUMPTION/JUDGEMENT] the Commission has consulted on a proposal addressing dark patterns, addictive design, personalisation and subscription practices; the status page could not be fetched; no adopted text exists as of this brief.
- **PSD3/PSR** — formal adoption pending (3.10).
- **ESPR delegated acts and DPP** — timing unverified (3.6).

---

## PART 4: The regulatory calendar and the Long Fuse

### 4.1 Regulatory calendar as of November 2026

| Date | Instrument | What applies | Source tag |
| --- | --- | --- | --- |
| 13 Jun 2014 | Consumer Rights Directive 2011/83/EU | 14-day withdrawal, 14-day refund, "order with obligation to pay" | VERIFIED (OJ 2011) |
| 25 May 2018 | GDPR | Controller/processor duties, one-month DSR deadline, fines to 4% | VERIFIED (OJ 2016) |
| 3 Dec 2018 | Geo-blocking Regulation | No nationality-based blocking or forced redirect | VERIFIED (OJ 2018) |
| 14 Sep 2019 | PSD2 RTS on SCA | Strong customer authentication and exemptions | VERIFIED (OJ 2018) |
| 28 May 2022 | Omnibus Directive | 30-day prior price, ranking and review transparency, personalised-price disclosure | VERIFIED (OJ 2019) |
| 27 Jun 2023 | INFORM Consumers Act (US) | Marketplace seller verification and disclosure | VERIFIED (FTC) |
| 10 Jul 2023 | EU-US DPF adequacy | Transfers to certified US firms; appeal C-703/25 P pending | VERIFIED (OJ 2023; OJ C 2025) |
| 17 Feb 2024 | Digital Services Act | Trader traceability (Art. 30), compliance by design (Art. 31), no deceptive interfaces (Art. 25) | VERIFIED (OJ 2022) |
| 2024 (Oct, per FTC: 60 days after FR) | FTC fake-reviews rule (US) | Ban on fake, incentivised and suppressed reviews | VERIFIED (FTC, Aug 2024); date ASSUMPTION |
| 18 Oct 2024 | NIS2 (national application) | Risk management, 24/72-hour reporting, supply-chain clauses | VERIFIED (OJ 2022) |
| 13 Dec 2024 | GPSR | Manufacturer/responsible person and safety info on every online offer | VERIFIED (OJ 2023) |
| 1 Jan 2025 | Germany e-invoicing | Must be able to receive e-invoices | VERIFIED (BMF) |
| 2 Feb 2025 | AI Act prohibitions and AI literacy | | VERIFIED (OJ 2024) |
| 31 Mar 2025 | PCI DSS v4.0.1 future-dated requirements | 6.4.3 and 11.6.1 mandatory (not in SAQ A, but SAQ A eligibility statement) | VERIFIED (PCI SSC) |
| 28 Jun 2025 | European Accessibility Act | E-commerce services accessible; micro-enterprise exemption; legacy products to 2030 | VERIFIED (OJ 2019) |
| 12 Sep 2025 | Data Act | Cloud switching rights for new contracts | VERIFIED (OJ 2023) |
| 9 Oct 2025 | Instant Payments Regulation | Verification of payee (euro area) | VERIFIED (OJ 2024) |
| 1 Jan 2026 | Belgium e-invoicing | Structured B2B e-invoices over Peppol; fines €1,500/3,000/5,000 | VERIFIED (einvoice.belgium.be) |
| 19 Jul 2026 | ESPR | Ban on destroying unsold apparel and footwear (Annex VII); DPP registry due | VERIFIED (OJ 2024) |
| 31 Jul 2026 | Right to Repair Directive | National application | VERIFIED (OJ 2024) |
| 2 Aug 2026 | AI Act general application (transparency Art. 50) | | VERIFIED (OJ 2024, 2026) |
| 12 Aug 2026 | PPWR | Packaging rules and EPR framework apply | VERIFIED (OJ 2025) |
| 15 Aug 2026 | Dutch Cyberbeveiligingswet | NIS2 in force in NL: registration, duty of care, reporting | VERIFIED (Rijksoverheid) |
| 11 Sep 2026 | Cyber Resilience Act Art. 14 | Vulnerability and incident reporting for products with digital elements | VERIFIED (OJ 2024) |
| 2 Dec 2026 | AI Act (Omnibus) | New prohibitions; Art. 50(2) marking for pre-existing generative systems | VERIFIED (OJ 2026) |
| 1 Jan 2027 | Germany e-invoicing | Issuance mandatory for issuers above €800k prior-year turnover | VERIFIED (BMF) |
| 26 Apr 2027 | ADA Title II web rule (US, larger governments) | WCAG 2.1 AA; private sector by litigation | VERIFIED (ada.gov) |
| 2 Dec 2027 | AI Act high-risk (Annex III) | | VERIFIED (OJ 2026) |
| 11 Dec 2027 | Cyber Resilience Act | Full application | VERIFIED (OJ 2024) |
| 1 Jan 2028 | Germany e-invoicing | Issuance mandatory for all; EDI transition ends | VERIFIED (BMF) |
| 2 Aug 2028 | AI Act high-risk (Annex I) | | VERIFIED (OJ 2026) |
| 12 Aug 2028 (or later) | PPWR harmonised labels | | VERIFIED (OJ 2025) |
| 28 Jun 2030 | EAA transition ends | Legacy products no longer grandfathered | VERIFIED (OJ 2019) |
| 1 Jul 2030 | ViDA; Netherlands e-invoicing (planned) | EU e-invoicing and digital reporting; NL B2B mandate (bill pending) | VERIFIED (OJ 2025; Rijksoverheid) ⚠ |
| 1 Jul 2031 | Netherlands domestic reporting (planned) | | VERIFIED (Rijksoverheid) ⚠ |
| Pending | PSD3/PSR; Digital Omnibus (data); Digital Fairness Act; DPF appeal; US negative-option rule | | ⚠ |

[ASSUMPTION/JUDGEMENT] Dates are application dates from the texts above; national transpositions of directives (CRD, Omnibus, EAA, NIS2, Right to Repair) can differ in detail and timing.

### 4.2 The Long Fuse: lessons for the chapter

[ASSUMPTION/JUDGEMENT] The pattern the book calls the Long Fuse is visible in every row above: regulation is announced years before it applies, then arrives as a data requirement on a specific date. Lessons the evidence supports:

1. **Most rules are data requirements, not page requirements.** Prior price needs 30 days of price history; GPSR needs manufacturer and responsible-person fields; DSA Art. 30 and INFORM need seller KYB records; EPR needs packaging weights per material per country; the DPP needs a resolvable product identifier. Put them in the system of record, not in the template.
2. **Dates slip, scope does not.** The AI Act's high-risk dates moved by over a year (Omnibus 2026/1744); PCI's 6.4.3/11.6.1 were softened for SAQ A at the last moment; the Dutch e-invoicing mandate moved to 2030 before it was even a bill. Plan to the scope, schedule to the date, and keep the calendar live.
3. **Transposition multiplies the calendar.** One directive becomes 27 laws with different dates (Belgium 2026 and Germany 2025–2028 for e-invoicing; the Netherlands' Cbw in August 2026 for NIS2). A merchant selling in NL, BE and DE tracks three calendars.
4. **Courts and appeals are calendar events too.** Wayfair created sales-tax nexus overnight; the Eighth Circuit removed a federal rule; the DPF appeal could do the same for transfers.
5. **The platform absorbs some of it, never all of it.** PCI scope, cookie banners, withdrawal flows and accessibility of the hosted checkout come with a hosted platform; price history, product safety fields, EPR reporting, DSR fan-out, consent propagation and contract clauses with every vendor do not.
6. **Owner, list, date.** The practical artefact is a regulatory calendar with an owner per row, the data and systems each row touches, and the date; chapter 36's Kestrel & Pine calendar for 2027 should be built from the table in 4.1.

---

## Key numbers

| Number | Meaning | Source and date |
| --- | --- | --- |
| 14 days / 14 days / 12 months | Withdrawal period; refund deadline; extension when not informed | CRD 2011/83/EU, OJ 2011 |
| 30 days | Look-back for the "prior price" in a price-reduction announcement | Omnibus 2019/2161, applied 28 May 2022 |
| 28 Jun 2025 / 28 Jun 2030 | EAA application; end of transition for legacy products | Directive 2019/882, OJ 2019 |
| <10 staff and ≤€2m | EAA micro-enterprise service exemption | Directive 2019/882 |
| 17 Feb 2024 | DSA application (Art. 30 trader traceability) | Regulation 2022/2065 |
| 13 Dec 2024 | GPSR application | Regulation 2023/988 |
| 12 Aug 2026 | PPWR application | Regulation 2025/40 |
| 19 Jul 2026 | ESPR ban on destroying unsold apparel and footwear | Regulation 2024/1781 |
| 24 h / 72 h / 1 month | NIS2 early warning, notification, final report | Directive 2022/2555 |
| 15 Aug 2026 | Dutch Cyberbeveiligingswet in force | Rijksoverheid, 7 Jul 2026 |
| 2 Aug 2026; 2 Dec 2027; 2 Aug 2028 | AI Act general application; Annex III high-risk; Annex I high-risk | Regulations 2024/1689 and 2026/1744 |
| 12 Sep 2025 | Data Act application | Regulation 2023/2854 |
| EUR 30 | SCA low-value remote exemption ceiling | RTS 2018/389 |
| 27 Nov 2025; 22 Apr 2026 | PSD3/PSR provisional agreement; Coreper confirmation (adoption pending) | Council 15005/26, 29 Oct 2026 |
| 1 Jan 2026; €1,500/3,000/5,000 | Belgian B2B e-invoicing mandate; fines | einvoice.belgium.be |
| €800,000; end 2026 / end 2027 | German issuance transition threshold and dates | BMF FAQ |
| 1 Jul 2030; 1 Jul 2031 | Planned Dutch e-invoicing and reporting mandates | Rijksoverheid, 11 Sep 2026 |
| 10 / 8 / 6 years | German retention: books; vouchers; other records | §147 AO |
| 1 month (+2) | GDPR deadline for data subject requests | GDPR Art. 12(3) |
| €20m or 4% | GDPR maximum fine (core infringements) | GDPR Art. 83(5) |
| 10 days; 48 hours; 30 days | Shopify customer-redact delay; shop-redact delay; app completion window | shopify.dev, n.d. |
| £20m (from £183.39m proposed); ~429,612 people | BA penalty and affected individuals | Wikipedia citing ICO, 2020 |
| €32m → €15m | Amazon France Logistique CNIL fine and reduction | enforcementtracker, 2024–26 |
| $1.2m | Sephora CCPA settlement | California AG, 24 Aug 2022 |
| 19 | US comprehensive state privacy laws on the IAPP 2025 chart | IAPP, 2025 ⚠ |
| $100,000 or 200 transactions | South Dakota nexus thresholds upheld in Wayfair | SCOTUS, 21 Jun 2018 |
| 200 sales and $5,000; $20,000; $53,088 | INFORM high-volume seller; disclosure threshold; per-violation penalty | FTC, n.d. |
| 5,114; 70%; 36% | 2025 US ADA web lawsuits; e-commerce share; top-500 retailers sued | UsableNet, Dec 2025 |
| 31 Mar 2025 | PCI DSS 6.4.3 and 11.6.1 mandatory | PCI SSC, 2025 |
| 100K+ sites; Feb 2024; 25 Jun 2024 | Polyfill.io embedders; domain sale; disclosure | Sansec, 2024 |
| 51% / 37% | Automated share of web traffic / bad-bot share (vendor) | Imperva 2025 report ⚠ |
| 300%; 25 billion | AI-bot traffic growth; commerce bot requests in two months (vendor) | Akamai via trade press, Nov 2025 ⚠ |
| $890bn; 93% | Projected 2024 US retail returns; retailers calling returns fraud significant | NRF, 5 Dec 2024 |

## Open questions / not verifiable

- The Ticketmaster ICO penalty (amount, date, the bank-warning timeline) was not re-verified; the ICO site is behind a bot challenge.
- The Dutch seven-year retention rule and the Belgian ten-year rule were not verified (official pages 404 or not fetched).
- The ESPR working plan and the textiles DPP timetable were not fetched; the "around 2027" delegated-act expectation is an assumption.
- The Digital Fairness Act's status and planned adoption date were not fetched.
- The effective date of the FTC fake-reviews rule (21 October 2024) and its CFR citation were not read from the Federal Register.
- No official statistic on card testing, account takeover or skimming frequency in the EU was found; all bot and fraud figures are vendor-sourced.
- Whether Adyen's documentation now assigns SAQ A to Drop-in/Components in all cases (its PCI-levels page returned 404) is unknown; the mapping in 1.6 rests on Stripe's guide and Adyen's script-security page.
- The IAPP 2025 chart predates several 2025–2026 state laws; the November 2026 count is unknown.
- Whether the Digital Omnibus (data) has moved beyond proposal stage in the Council or Parliament by November 2026 was not verified.
- Whether PSD3/PSR were formally adopted between 29 October and 7 November 2026 was not checked beyond the Council's state-of-play note.

## Source list

Official EU texts (EU Publications Office, Official Journal; year is OJ year):
- Directive 2011/83/EU (Consumer Rights), 2011, https://publications.europa.eu/resource/celex/32011L0083
- Directive (EU) 2019/2161 (Omnibus), 2019, https://publications.europa.eu/resource/celex/32019L2161
- Directive 98/6/EC (Price Indication), 1998, https://publications.europa.eu/resource/celex/31998L0006
- Directive 2005/29/EC (Unfair Commercial Practices), 2005, https://publications.europa.eu/resource/celex/32005L0029
- Directive (EU) 2019/882 (European Accessibility Act), 2019, https://publications.europa.eu/resource/celex/32019L0882
- Regulation (EU) 2022/2065 (Digital Services Act), 2022, https://publications.europa.eu/resource/celex/32022R2065
- Regulation (EU) 2023/988 (General Product Safety), 2023, https://publications.europa.eu/resource/celex/32023R0988
- Regulation (EU) 2025/40 (Packaging and Packaging Waste), 2025, https://publications.europa.eu/resource/celex/32025R0040
- Regulation (EU) 2024/1781 (Ecodesign for Sustainable Products), 2024, https://publications.europa.eu/resource/celex/32024R1781
- Directive (EU) 2022/2555 (NIS2), 2022, https://publications.europa.eu/resource/celex/32022L2555
- Regulation (EU) 2024/2847 (Cyber Resilience Act), 2024, https://publications.europa.eu/resource/celex/32024R2847
- Regulation (EU) 2024/1689 (AI Act), 2024, https://publications.europa.eu/resource/celex/32024R1689
- Regulation (EU) 2026/1744 (Digital Omnibus on AI), 2026, https://publications.europa.eu/resource/celex/32026R1744
- Regulation (EU) 2023/2854 (Data Act), 2023, https://publications.europa.eu/resource/celex/32023R2854
- Directive (EU) 2015/2366 (PSD2), 2015, https://publications.europa.eu/resource/celex/32015L2366
- Delegated Regulation (EU) 2018/389 (RTS on SCA), 2018, https://publications.europa.eu/resource/celex/32018R0389
- Regulation (EU) 2024/886 (Instant Payments), 2024, https://publications.europa.eu/resource/celex/32024R0886
- Council Directive (EU) 2025/516 (ViDA), 2025, https://publications.europa.eu/resource/celex/32025L0516
- Regulation (EU) 2018/302 (Geo-blocking), 2018, https://publications.europa.eu/resource/celex/32018R0302
- Directive (EU) 2024/1799 (Right to Repair), 2024, https://publications.europa.eu/resource/celex/32024L1799
- Regulation (EU) 2016/679 (GDPR), 2016, https://publications.europa.eu/resource/celex/32016R0679
- Directive 2009/136/EC (amending ePrivacy Art. 5(3)), 2009, https://publications.europa.eu/resource/celex/32009L0136
- Directive 2002/58/EC (ePrivacy, consolidated 2009), EUR-Lex, https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02002L0058-20091219
- Commission Implementing Decision (EU) 2023/1795 (EU-US DPF adequacy), 2023, https://publications.europa.eu/resource/celex/32023D1795
- Commission Implementing Decision (EU) 2021/914 (SCCs), 2021, https://publications.europa.eu/resource/celex/32021D0914
- Appeal C-703/25 P, Latombe v Commission, OJ C/2025/6610, 2025, https://publications.europa.eu/resource/celex/62025CN0703
- Council of the EU, doc. 15005/26, state of play for ECOFIN 9 Nov 2026, 2026, https://data.consilium.europa.eu/doc/document/ST-15005-2026-INIT/en/pdf
- European Parliament press release, "Payment services deal", 2025, https://www.europarl.europa.eu/news/en/press-room/20251121IPR31540/payment-services-deal-more-protection-from-online-fraud-and-hidden-fees
- European Commission, EU-US data transfers page, n.d., https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/eu-us-data-transfers_en
- European Commission, European Accessibility Act page, n.d., https://commission.europa.eu/strategy-and-policy/policies/justice-and-fundamental-rights/disability/union-equality-strategy-rights-persons-disabilities-2021-2030/european-accessibility-act_en

EU and national regulators and guidance:
- EDPB, Guidelines 07/2020 on controller and processor, v2.0, 2021, https://www.edpb.europa.eu/system/files/2023-10/EDPB_guidelines_202007_controllerprocessor_final_en.pdf
- EDPB, Guidelines 05/2020 on consent, 2020, https://www.edpb.europa.eu/system/files/documents/files/file1/edpb_guidelines_202005_consent_en.pdf
- EDPB, Guidelines 2/2023 on the technical scope of Art. 5(3) ePrivacy, v2.0, 2024, https://www.edpb.europa.eu/system/files/documents/2024-10/edpb_guidelines_202302_technical_scope_art_53_eprivacydirective_v2_en_0.pdf
- Autoriteit Persoonsgegevens, "Cookies" (Dutch), n.d., https://www.autoriteitpersoonsgegevens.nl/themas/internet-slimme-apparaten/cookies
- Gegevensbeschermingsautoriteit (Belgium), "Cookies en andere traceringsmiddelen" (Dutch), 2023, https://www.gegevensbeschermingsautoriteit.be/burger/thema-s/internet/cookies
- Bundesministerium der Finanzen, FAQ E-Rechnung (German), n.d., https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html
- §147 Abgabenordnung, gesetze-im-internet.de, current, https://www.gesetze-im-internet.de/ao_1977/__147.html
- FPS Finance Belgium, e-invoicing mandate article, 2024, https://einvoice.belgium.be/en/article/structured-electronic-invoices-between-companies-are-compulsory-2026
- FPS Finance Belgium, e-invoicing FAQ (fines), n.d., https://einvoice.belgium.be/en/FAQ/specific-questions-about-e-invoicing
- Rijksoverheid, Cyberbeveiligingswet in force 15 Aug 2026, 2026, https://www.rijksoverheid.nl/actueel/nieuws/2026/07/07/cyberbeveiligingswet-en-wet-weerbaarheid-kritieke-entiteiten-vanaf-15-augustus-2026-van-kracht
- Rijksoverheid, cabinet decision on e-invoicing, 2026, https://www.rijksoverheid.nl/actueel/nieuws/2026/09/11/kabinet-kiest-voor-invoering-e-facturatie-en-rapportage-voor-bedrijven
- Zentrale Stelle Verpackungsregister, LUCID, n.d., https://www.verpackungsregister.org/en/

Security standards and vendors:
- PCI SSC blog, "Just Published: PCI DSS v4.0.1", 2024, https://blog.pcisecuritystandards.org/just-published-pci-dss-v4-0-1
- PCI SSC blog, "Guidance for PCI DSS e-commerce requirements effective after 31 March 2025", 2025, https://blog.pcisecuritystandards.org/coffee-with-the-council-podcast-guidance-for-pci-dss-e-commerce-requirements-effective-after-31-march-2025
- OWASP, Automated Threat OAT-001 Carding (with index of OATs), n.d., https://owasp.github.io/www-project-automated-threats-to-web-applications/assets/oats/EN/OAT-001_Carding
- OWASP, Credential stuffing, n.d., https://community.owasp.org/attacks/Credential_stuffing
- Stripe Docs, "Protect yourself from card testing", n.d., https://docs.stripe.com/disputes/prevention/card-testing
- Stripe Docs, "Integration security guide", n.d., https://docs.stripe.com/security/guide
- Stripe Docs, "Best practices for managing secret API keys", n.d., https://docs.stripe.com/keys-best-practices
- Stripe, PCI compliance guide (Dutch edition), n.d., https://stripe.com/guides/pci-compliance
- Adyen Docs, PCI DSS compliance guide, n.d., https://docs.adyen.com/development-resources/pci-dss-compliance-guide/
- Adyen Docs, Script security for ecommerce, n.d., https://docs.adyen.com/development-resources/pci-dss-compliance-guide/script-security/
- Shopify, Security, n.d., https://www.shopify.com/security
- Shopify, PCI compliance, n.d., https://www.shopify.com/pci-compliant
- Shopify Help Center, Two-step authentication, n.d., https://help.shopify.com/en/manual/your-account/account-security/two-step-authentication
- Shopify.dev, Privacy law compliance webhooks, n.d., https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance
- Shopify.dev, Protected customer data, n.d., https://shopify.dev/docs/apps/launch/protected-customer-data
- BigCommerce (Commerce) Trust Center, n.d., https://security.bigcommerce.com/
- Adobe Experience League, Adobe Commerce shared responsibility, n.d., https://experienceleague.adobe.com/en/docs/commerce-operations/security-and-compliance/shared-responsibility
- Sansec, "Polyfill supply chain attack hits 100K+ sites", 2024, https://sansec.io/research/polyfill-supply-chain-attack
- Sansec, "CosmicSting", 2024, https://sansec.io/research/cosmicsting
- Imperva, 2025 Bad Bot Report (landing page), 2025, https://www.imperva.com/resources/resource-library/reports/2025-bad-bot-report/
- SecurityInfoWatch (Akamai press release), "Akamai Reports 300% Surge in AI Bot Traffic", 2025, https://www.securityinfowatch.com/cybersecurity/press-release/55327981/akamai-reports-300-surge-in-ai-bot-traffic-disrupting-digital-businesses
- NRF and Happy Returns, "2024 Consumer Returns in the Retail Industry", 2024, https://nrf.com/research/2024-consumer-returns-retail-industry

Enforcement, courts and US sources:
- Wikipedia, "British Airways data breach" (citing ICO penalty notice of 16 Oct 2020), accessed 2026, https://en.wikipedia.org/wiki/British_Airways_data_breach
- Wikipedia, "Ticketmaster" (2018 breach section), accessed 2026, https://en.wikipedia.org/wiki/Ticketmaster
- CMS GDPR Enforcement Tracker, ETid-2192 (Amazon France Logistique), 2024–2026, https://www.enforcementtracker.com/ETid-2192
- Lewis Silkin, "Latombe's challenge to EU-US data transfers fails", 2025, https://www.lewissilkin.com/insights/2025/09/03/transatlantic-trouble-not-this-time-latombes-challenge-to-eu-us-data-transfers-fails
- Osborne Clarke, "Digital Omnibus reshapes EU cookie rules", 2025, https://www.osborneclarke.com/insights/digital-omnibus-reshapes-eu-cookie-rules-leaves-banner-fatigue-largely-intact
- California Attorney General, Sephora settlement, 2022, https://oag.ca.gov/news/press-releases/attorney-general-bonta-announces-settlement-sephora-part-ongoing-enforcement
- California Attorney General, CCPA page, n.d., https://oag.ca.gov/privacy/ccpa
- IAPP, US State Privacy Legislation Tracker chart, 2025, https://prod.iapp.org/media/pdf/resource_center/State_Comp_Privacy_Law_Chart.pdf
- IAPP, US State Privacy Legislation Tracker page, updated 2026-09-08, https://iapp.org/resources/article/us-state-privacy-legislation-tracker/
- Cornell LII, South Dakota v. Wayfair, Inc., 2018, https://www.law.cornell.edu/supremecourt/text/17-494
- FTC, "Informing Businesses about the INFORM Consumers Act", n.d., https://www.ftc.gov/business-guidance/resources/informing-businesses-about-inform-consumers-act
- FTC, press release on the final rule banning fake reviews, 2024, https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials
- Kelley Drye via JD Supra, "FTC Relaunches Negative Option Rulemaking", 2026, https://www.jdsupra.com/legalnews/ftc-relaunches-negative-option-6871835/
- US DOJ, ADA Title II web accessibility rule, 2024 (updated 2026), https://www.ada.gov/resources/2024-03-08-web-rule/
- UsableNet, 2025 Year-End Digital Accessibility Lawsuit Report (plain text), 2025, https://info.usablenet.com/2025-year-end-digital-accessibility-lawsuit-report-plain-text
