{id: identity-and-verification}
# 26. Who Is on the Other Side? Identity and Verification

![Who Is on the Other Side? Identity and Verification — logo](listing-systems-architecture/posts/26-identity-and-verification/assets/images/26-identity-and-verification/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Separate the three questions an identity system answers: who someone is, whether the person logging in is still that someone, and whether a business is what it claims to be. You will learn how to turn them into identity levels, verification claims and badges, how to defend accounts against takeover, and how to build one identity service for a group of marketplaces without making the brands inseparable.

> **WHY THE BUSINESS CARES:** Buyers contact strangers, and sellers hand over goods to them. Knowing a little more about who is on the other side is the cheapest trust the marketplace can buy, but every verification step also loses some honest users. The business needs friction placed where the risk is, not spread evenly across everyone.

> **WHY ARCHITECTS SHOULD CARE:** Identity is the one capability every other context depends on: insertion, messaging, payments, trust and safety, regulation and ads. A group that runs one identity system per brand cannot share a ban, cannot offer one login, and cannot prove which trader it verified. A group that merges them carelessly can no longer sell a brand.

> **KEY POINTS:**
>
> * **Identity is a set of separate claims, not one "verified" flag.** Contactability, authentication strength, proof of person and proof of business answer different questions and fail in different ways. Model each as a claim with a method, a source, a time and an expiry, and derive identity levels from the claims instead of storing a level.
> * **Ask for identity at the moment of risk, not at the door.** Browsing and saving searches need no identity. Contacting a seller, publishing a rental, receiving a payout or advertising as a trader each need a specific level. Step-up verification at those moments keeps conversion high and puts the cost where fraud concentrates. Account recovery is part of the same design, because a weak recovery path cancels a strong login.
> * **A badge is a promise to the other side, and a group identity is a commitment to the owners.** Show buyers only what was checked ("identity verified with BankID", "registered business"), and revoke the badge when the account's posture changes. Build one group identity service with brand-specific profiles and pairwise identifiers, so a brand can still be separated if it is sold.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Fast Mail for Fraudsters** — when anyone with a fresh e-mail address can message any seller, identity checks never reach the channel where scams close.
> * **Deal-Shaped Architecture** — four acquired identity systems mean four logins, four ban lists and four answers to "who is this trader", so a fraudster removed from one brand simply registers on the next.
> * **Moderation as an Afterthought** — verification added after a fraud wave, as a one-off document upload, produces badges that nobody can explain and evidence nobody can find.

Part V treats trust as a shared platform, and [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention) ended on its strongest and most expensive friction: asking users to prove who they are. This chapter decides how much a marketplace should know about its users. Most marketplaces answer that twice, badly. First they ask for almost nothing, because every registration field costs sign-ups. Then, after a fraud wave or a regulator's letter, they ask everyone for an identity document, because the incident made identity feel like the solution. Neither answer holds up. **The right amount of identity depends on what the user is about to do.** Browsing needs none. Publishing a rental in a city full of fake-rental rings needs a great deal.

The chapter separates *proofing* (establishing who someone is) from *authentication* (establishing that the person logging in is still that someone) and from *business verification* (establishing that an organization exists and is who it says it is). It turns these into identity levels and badges, follows account takeover and recovery, and then takes up the group question: one login for four brands, or four logins forever?

The result is the identity service that neighboring chapters call. [Private Sellers, Dealers and Agencies: Modeling Who Lists](#sellers-and-accounts) owns the seller account model, organizations, branches and trader status. [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention) owns risk scoring, fraud signals and step-up friction as a fraud control. [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation) owns the legal detail of the Digital Services Act (DSA) and of seller tax reporting, and builds its trader record on the business registry designed here. [From Interest to Contact: Messaging and Lead Management](#messaging-and-leads) gates contact on the identity levels defined here, and [Beyond the Contact: Payments, Shipping and Buyer Protection](#transactions-and-payments) defers to them for payees. The running example is Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)).

{id: identity-and-verification--setting-the-scene-at-veldmark-one-phone-number-two-brands}
## Setting the Scene at Veldmark: One Phone Number, Two Brands

On Sunday **7 March 2027**, a "buyer" sent Femke, a private seller in Rotterdam, a fake Tradeyard Safe Deal payment link for her **€240** city bike. The account was suspended at 20:26, seven minutes after Femke reported it ([Trust and Safety as a Platform](#trust-and-safety-architecture) tells that story). When Aisha Rahman, the Group Head of Trust & Safety, traced the account the following week, two facts stood out.

The first was that the scammer's Tradeyard account was **phone-verified**. In Tradeyard's own vocabulary that made it a "verified" account, and the app showed a small green tick next to its name. Phone verification had proved that someone controlled a mobile number for the few minutes it took to type a six-digit code.

The second was that the same number had registered a **Motorvane** private-seller account three weeks earlier. Motorvane could not know, because each Veldmark brand runs its own identity system. Nothing joined them except the fraudster.

Ingrid Halvorsen, the Group Chief Architect, asked Lucía Ortega, the Group Data Protection Officer, and Aisha to describe what each brand knew about its users. The answer took one table:

| Brand | Login methods | What "verified" means today | Business verification | Accounts (registered, about) |
| --- | --- | --- | --- | --- |
| Tradeyard | Password; Google and Apple sign-in; SMS code for some actions | Phone number confirmed by SMS | Pro sellers: VAT number at subscription, not re-checked | 46 million |
| Motorvane | Password; dealer staff on a separate dealer portal login | E-mail confirmed | Dealers: contract checks at signature only | 19 million |
| Hearthly FR/ES | Password; Hearthly.es still on Casavista's login | E-mail confirmed | New agencies checked manually by sales | 15 million |
| Keybridge | Agency staff accounts, single sign-on for large networks | Not applicable | Agency is the SaaS customer | 61,000 staff users |

About **80 million** consumer accounts sat in three identity stores, with no shared notion of who a person was. Veldmark's own analysis, matching on verified e-mail addresses, estimated that about **11 million** people held accounts on two or more brands. Three months later, in June 2027, Veldmark approved **Veldmark ID**: one login across brands with brand-specific profiles, rolling out in 2028.

Approving a login was the easy part. The questions Ingrid brought to the architecture advice forum were harder. What does "verified" mean at Veldmark? Which actions need which level? Who keeps the evidence, for how long? And if the private-equity owner sells Hearthly in 2030, can its users leave with it?

{id: identity-and-verification--concepts-identity-authentication-and-business-verification}
## Concepts: Identity, Authentication and Business Verification

{id: identity-and-verification--five-words-that-teams-use-interchangeably}
### Five words that teams use interchangeably

Identity discussions go wrong when one word stands for several things. This book uses these definitions:

| Term | Meaning | Example at Veldmark |
| --- | --- | --- |
| **Identity** | The person or organization the platform has evidence about | Femke, a natural person resident in Rotterdam |
| **Account** | The login: credentials, sessions, recovery methods | Femke's Veldmark ID account |
| **Profile** | A brand-specific persona attached to an account: display name, ratings, preferences | "Femke R." on Tradeyard; no Hearthly profile |
| **Seller account** | The commercial entity that lists: a private seller or an organization with members (owned by [Private Sellers, Dealers and Agencies: Modeling Who Lists](#sellers-and-accounts)) | Autohaus Ruhrblick on Motorvane, with nine staff users |
| **Claim** | A statement about an identity, with its evidence: "phone +31… controlled on 2 May 2027, by SMS code" | Femke's phone claim; Ruhrblick's trade-register claim |

The distinction between account and identity matters most. One person can hold several accounts, and one shared account can be used by several people (a family, a car dealership's front desk). An identity system that assumes one account per person will either block legitimate sharing or fail to see one fraudster with forty accounts.

{id: identity-and-verification--three-axes-not-one-ladder}
### Three axes, not one ladder

The clearest vocabulary for this comes from the United States National Institute of Standards and Technology (NIST). Its Digital Identity Guidelines, SP 800-63-4, finalized in July 2025, separate **identity assurance** (how confident the service is that a person is who they claim to be) from **authenticator assurance** (how confident it is that the person presenting the credential is the account holder), with a third axis for federated logins ([NIST, 2025](https://csrc.nist.gov/pubs/sp/800/63/4/final)). The guidelines are written for US government systems and oblige no marketplace to follow them, but the separation applies to any platform.

A user can be well proven and weakly authenticated: a dealer who passed a full business check five years ago and still logs in with a reused password. A user can also be strongly authenticated and unproven: an anonymous buyer with a passkey. Fraud exploits both gaps, and **a single "verification level" hides which gap is open.**

For a listing marketplace, three axes are enough:

1. **Proof of person** — what the platform knows about who a natural person is.
2. **Strength of authentication** — how hard it is for someone else to act as the account holder.
3. **Proof of business** — what the platform knows about an organization that lists or advertises.

![One green verified tick opened up into three separate gauges for proof of person, strength of login and proof of business, each at a different level.](listing-systems-architecture/posts/26-identity-and-verification/assets/images/26-identity-and-verification/three-axes-not-one-tick.jpeg)

**Figure 1:** *One "verified" tick hides three separate axes: proof of person, strength of authentication and proof of business, and fraud exploits whichever gap the tick does not show.*

{id: identity-and-verification--identity-levels}
### Identity levels

An **identity level** is a named combination of claims that a policy can require. It is a derived value, recomputed when claims are added, expire or are revoked. It is not a column someone sets. Veldmark adopted six levels for natural persons, plus a separate business ladder.

| Level | Name | Required claims | What it defeats | What it does not defeat |
| --- | --- | --- | --- | --- |
| L0 | Anonymous | None (device-scoped state only) | Nothing; none needed for browsing | — |
| L1 | Contactable | Confirmed e-mail address | Typos, trivial bots | Disposable addresses, account farms |
| L2 | Reachable | L1 plus a confirmed phone number, checked against virtual-number and recycled-number lists | Bulk account creation, because numbers cost money | SIM farms, rented numbers, SIM swap |
| L3 | Protected | L2 plus a phishing-resistant authenticator (a passkey) or a second factor | Credential phishing and stuffing for logins | Social engineering of recovery; a willing fraudster |
| L4 | Identified | L3 plus proof of person: a bank-based eID, a national eID or EU Digital Identity Wallet, or an identity document with a liveness check | Most fake-account farms; repeat offenders under new names | Stolen identities at small scale; money mules using their own names |
| L5 | Payee-verified | L4 plus a payment account in the person's name, verified by the payment provider | Payouts to accounts in other names | A real person acting as a mule |

The business ladder runs in parallel, because an organization is not a person with more documents:

| Level | Name | Required claims |
| --- | --- | --- |
| B1 | Declared trader | The seller declares it acts as a business, and provides name, address, phone, e-mail and trade-register details |
| B2 | Registered business | The trade-register entry and VAT number validated against official sources, and the person onboarding it identified at L4 |
| B3 | Accredited professional | B2 plus sector evidence: a dealer contract, a real-estate agent's professional licence where the country has one, or membership of a required redress scheme |

B1 and B2 map closely to what the DSA requires of online marketplaces before a trader can offer to EU consumers: name, address, phone and e-mail, a copy of an identification document or an electronic identification, payment account details, the trade-register number, and a self-certification, followed by "best efforts" to check the information against freely accessible official databases ([Regulation (EU) 2022/2065, Art. 30](https://eur-lex.europa.eu/eli/reg/2022/2065/oj)). [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation) covers that obligation as law. Here the point is architectural: **the trader-traceability record is a business identity claim set**, and it belongs in the identity service, not in a compliance spreadsheet.

**KYB** (know your business) is the name for the B-ladder checks. **KYC** (know your customer) is the payments-industry name for person and business checks that a regulated payment provider must run before it lets a user receive money. The two overlap but have different owners. At Veldmark, Adyen runs KYC for Safe Deal sellers, because Adyen is the licensed party. Adyen's platform documentation says it "must verify the users in your platform" before they can use capabilities such as payouts, and that it re-verifies when data changes ([Adyen, n.d.](https://docs.adyen.com/platforms/verification-overview)). Veldmark receives the verification *status* as a claim with Adyen as its source. It does not receive, and should not want, Adyen's evidence.

{id: identity-and-verification--verified-badges}
### Verified badges

A **verified badge** is a public statement the marketplace makes to one user about another. That makes it a promise, and a promise has a meaning, a scope and a liability. The rule I use: **a badge must say what was verified, by which method, and nothing more.** "Identity verified with BankID" is a badge. "Verified" is a liability, because a buyer will read it as "safe to pay", and the platform verified nothing of the kind.

Attackers value badges too. The Ofcom-commissioned expert report on fraudulent advertising and account integrity notes that account takeover is attractive because fraudsters "gain check marks, verification" along with the account ([Integrity Institute for Ofcom, 2026](https://www.ofcom.org.uk/siteassets/resources/documents/research-and-data/online-advertising/fraudulent-advertising-and-account-integrity_expert-insights-on-best-practice.pdf)). A badge on a taken-over account is worse than no badge. It amplifies the scam it was meant to prevent.

{id: identity-and-verification--architecture-the-identity-service-and-its-neighbors}
## Architecture: The Identity Service and Its Neighbors

{id: identity-and-verification--components-and-responsibilities}
### Components and responsibilities

The identity capability splits into components that change at different speeds and have different owners. Authentication changes when new authenticator technology appears. Verification changes when a vendor's price or a country's eID scheme changes. Levels and badges change when trust-and-safety policy changes.

| Component | Responsibility | Owns | Does not own |
| --- | --- | --- | --- |
| **Authentication service** | Logins, sessions, authenticators (passwords, passkeys, e-mail codes, social login), token issuance to brands through OpenID Connect | Credentials, sessions, authenticator registry | Profiles, risk scores |
| **Account recovery** | Regaining access after losing an authenticator; the most attacked flow | Recovery policies, recovery evidence | Normal login |
| **Verification orchestrator** | Runs a verification journey with the right provider for the country and level; normalizes results | Verification cases, provider adapters | The provider's raw evidence |
| **Claim store** | Every claim with method, source, assurance, time, expiry and status | Claims and their history | Documents and images |
| **Level and badge engine** | Derives identity levels from claims; decides which badges an account may show in which brand | Level rules, badge catalog | Fraud decisions |
| **Business registry** | B-ladder claims for organizations; register lookups; re-verification schedule; links to [Private Sellers, Dealers and Agencies: Modeling Who Lists](#sellers-and-accounts) organizations | Business claims, register snapshots | Contracts and packages |
| **Profile service** | Brand-specific profiles and preferences on top of one account | Display names, brand settings | Credentials |
| **Consent and privacy service** | Consents, data-subject requests, erasure fan-out | Consent records | Business data |

Two boundaries matter most. **Risk scoring lives outside identity.** [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention) reads identity levels as features and asks the identity service for a step-up. It does not write claims. **Documents live outside the claim store.** The claim says "identity document checked with liveness, provider X, case 8f3…, result pass, name match on the payee account". The image of the passport stays with the provider, for the provider's retention period, or in a sealed evidence vault if the law requires the platform to keep a copy.

![Diagram: Veldmark ID's components](listing-systems-architecture/posts/26-identity-and-verification/assets/images/26-identity-and-verification/fig02-veldmark-id-s-components-brands-authenticate.jpeg)

**Figure 2:** *Veldmark ID's components. Brands authenticate users through one service but receive brand-specific identifiers; verification providers sit behind adapters that write normalized claims; levels and badges are derived from claims and published as events to the fraud and trust-and-safety platform.*

{id: identity-and-verification--the-claim-as-the-contract}
### The claim as the contract

The most important interface in the identity service is the shape of a claim, not the login API, because every provider adapter writes one and every consumer reads one. Veldmark's claim record has these fields:

| Field | Example | Why it exists |
| --- | --- | --- |
| `claim_type` | `person.identified`, `phone.reachable`, `business.registered`, `payee.verified` | Policies require claim types, not vendors |
| `subject` | Account ID, or organization ID for business claims | Business claims attach to organizations, not to the staff member who uploaded them |
| `method` | `bank_eid`, `eudi_wallet`, `document_liveness`, `sms_otp`, `register_lookup`, `psp_kyc` | Different methods carry different assurance |
| `source` | Provider and case reference | Audit and dispute; no raw evidence |
| `attributes` | Verified given name, family name, year of birth over 18, country | Only what a policy needs (data minimization) |
| `assurance` | `low`, `substantial`, `high` | Comparable across providers and countries |
| `verified_at`, `expires_at` | 2 May 2027; 2 May 2030 | Claims age; phone numbers get recycled; businesses close |
| `status` | `valid`, `expired`, `revoked`, `disputed` | Badges must follow status |

Two design rules follow. First, **policies reference claim types and assurance, never providers.** "Private-landlord rentals in Spain require `person.identified` at `substantial`" survives a change of document vendor or the arrival of the EU Digital Identity Wallet. "Requires an Onfido check" (or any other named vendor) does not. Second, **claims carry only the attributes a policy needs.** If the only purpose is to show "identity verified", the claim needs the verified name (to match the payee account and the display name policy) and perhaps an adult flag. It does not need the document number, the date of birth or the address. The General Data Protection Regulation (GDPR) requires data to be "limited to what is necessary" and asks for data protection by design ([Regulation (EU) 2016/679, Arts. 5(1)(c) and 25](https://eur-lex.europa.eu/eli/reg/2016/679/oj)). The claim schema is where that principle is enforced.

Seller tax reporting needs more attributes, and they stay out of the general claim. Once Safe Deal makes Tradeyard a reporting platform operator under DAC7, it must collect date of birth and tax identification number for reportable sellers. That collection belongs to a separate, purpose-bound tax profile with its own retention. [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation) covers the obligation.

{id: identity-and-verification--the-claim-lifecycle}
### The claim lifecycle

Claims expire and get revoked, and the lifecycle has to model every way they end, because a badge that outlives its claim is a false statement. A phone number is reassigned to someone else. A company is dissolved. A passkey is deleted. A payment provider freezes a seller after a fraud report.

![Diagram: A claim's lifecycle](listing-systems-architecture/posts/26-identity-and-verification/assets/images/26-identity-and-verification/fig03-claim-s-lifecycle-every-transition-recomputes.jpeg)

**Figure 3:** *A claim's lifecycle. Every transition recomputes the account's identity level and badges; revocation is a first-class state, not a deletion, so the platform can later explain why a badge disappeared.*

{id: identity-and-verification--authentication-and-account-takeover}
## Authentication and Account Takeover

{id: identity-and-verification--authenticators-for-a-consumer-marketplace}
### Authenticators for a consumer marketplace

Most identity incidents begin at authentication, which happens every day for tens of millions of people; proofing happens once in a while. A marketplace needs a small set of authenticators, each with a clear role.

| Authenticator | Role | Strength | Weakness |
| --- | --- | --- | --- |
| Password | Legacy default | Familiar | Phished, reused, stuffed from other breaches |
| **E-mail one-time code or link** | Passwordless default; recovery bridge | No password to steal | Only as strong as the e-mail account |
| SMS one-time code | Phone confirmation; fallback | Ubiquitous | SIM swap, interception, SMS-pumping fraud against the platform |
| Social login (Google, Apple) | Low-friction sign-up | Delegates strength to a large provider | Account-merge risks; dependence on a third party |
| **Passkey** | Phishing-resistant login | Bound to the site; no shared secret | Device loss; support load; not universal yet |
| Bank eID (BankID, itsme, iDIN and similar) | Proofing and high-assurance step-up | Bank-grade proofing | Per-country; per-use fees; not every user has one |

A **passkey** is, in the FIDO Alliance's words, "an authentication credential based on FIDO standards" that the user unlocks with a biometric, PIN or pattern on their device. Passkeys can be synced across a user's devices through a cloud service or bound to one device, and FIDO describes them as phishing-resistant either way ([FIDO Alliance, n.d.](https://fidoalliance.org/passkeys/)). NIST's 2025 guidelines accept syncable authenticators at its middle assurance level, subject to protections on the sync service, and exclude them from the highest level because syncing conflicts with its non-exportability requirement ([NIST SP 800-63B-4, Appendix B](https://pages.nist.gov/800-63-4/sp800-63b/syncable)). For a marketplace, synced passkeys are the realistic target: strong enough to stop phishing, recoverable enough for consumers.

Mercari, the Japanese second-hand marketplace, documents that required passkeys stop large-scale phishing, at a cost in lost users and support load. In a July 2026 engineering post, Mercari described about **13 million** users with a registered passkey, and "phishing-resistant accounts" that require a passkey, allow login only with it and permit recovery only through high-assurance identity proofing. Where passkeys are required, Mercari reports that "large-scale phishing financial damages have been effectively zero"; where they are optional, losses dropped as adoption grew. Mercari also names the cost: users who cannot register a passkey leave, and users who lose one are locked out and contact support ([Mercari Engineering, 2026](https://engineering.mercari.com/en/blog/entry/20260730-bridging-the-gap-between-passwords-and-passkeys-with-risk-based-authentication/)).

Mercari's migration model is worth copying because it is gradual. Accounts move along four states: password or e-mail link, e-mail link only (password disabled), passkey or e-mail link, and passkey only. **Disabling the password is the first step, not the last.** The e-mail link acts as a bridge, so a user who never adopts a passkey still stops being phishable by password.

FINN, the Norwegian marketplace, moves in the same direction from a different starting point: its help center describes logging in to the shared Vend account with a one-time code sent to the user's e-mail address, and separately encourages two-step authentication because, "as on other digital platforms", some FINN users have had their accounts taken over by others ([FINN help center, 2024, updated 2026](https://hjelpesenter.finn.no/hc/no/articles/22642951164434-Beskytt-kontoen-din-med-totrinnsautentisering)).

{id: identity-and-verification--risk-based-authentication}
### Risk-based authentication

Strong authenticators protect accounts that use them. Risk-based authentication protects the rest. It judges each login and each sensitive action by two kinds of evidence, which Mercari calls **session posture** (signals from the device and network of this session: client integrity, network reputation, device and user-agent properties) and **account posture** (what accumulates over the account's life: authentication capabilities, verification history, behavior). Mercari combines them into one weighted verdict, and weights them differently for different decisions ([Mercari Engineering, 2026](https://engineering.mercari.com/en/blog/entry/20260730-bridging-the-gap-between-passwords-and-passkeys-with-risk-based-authentication/)).

For a listing marketplace, the sensitive actions are predictable, and each deserves its own policy:

| Sensitive action | Why attackers want it | Typical control |
| --- | --- | --- |
| Login from a new device | Entry point for takeover | Step up to passkey or e-mail code; notify on known devices |
| Change of e-mail, phone or password | Locks the owner out | Re-authenticate; notify the old contact point; delay the change of the recovery address |
| **Change of payout account** | Redirects the victim's sale proceeds | Re-authenticate at L3 or above; hold payouts for a cooling period; notify |
| Publishing many listings quickly | Uses an aged account's reputation | Velocity limits by level (see [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention)) |
| Sending messages with links or contact details | Fast Mail for Fraudsters | Message friction by level (see [From Interest to Contact: Messaging and Lead Management](#messaging-and-leads)) |
| Enabling a verified badge in a new brand | Borrowed trust | Require fresh authentication and a matching profile name |

{id: identity-and-verification--recovery-is-the-real-login}
### Recovery is the real login

Every authentication design has a back door: the flow for people who lost their password, their phone or their passkey. Attackers use it because it is weaker. If an account can be recovered by answering a support agent's questions or by receiving an SMS code, the passkey protects nothing.

Mercari's recovery rule is the strictest documented one. Users who cannot be reached by e-mail or phone prove their identity with Japan's My Number Card or with a document and a selfie, and recovery restores a passkey, e-mail address or phone number. "We do not restore passwords," the post says ([Mercari Engineering, 2026](https://engineering.mercari.com/en/blog/entry/20260730-bridging-the-gap-between-passwords-and-passkeys-with-risk-based-authentication/)). The general principle is that **recovery should require at least the assurance the account had**, and that a recovered account should return in a cautious state: badges suspended, payout changes held, until it re-establishes posture.

Group identity programs open a second back door: **pre-hijacking**. Researchers at Microsoft described pre-hijacking attacks, in which an attacker creates an account with a victim's e-mail address *before* the victim does, and keeps access after the victim later signs up or links a social login. They found at least 35 of 75 popular services vulnerable to one or more of five variants ([Sudhodanan and Paverd, USENIX Security 2022](https://arxiv.org/abs/2205.10174)). Any program that **merges accounts across brands by matching e-mail addresses** recreates the conditions for this attack. Accounts should be linked only after the user proves control of both, through authentication, not through a string match.

{id: identity-and-verification--proofing-people-methods-and-their-trade-offs}
## Proofing People: Methods and Their Trade-offs

When a policy asks for L4, the verification orchestrator has to choose a method. The choice depends on country, cost, user experience and the attribute the policy needs.

| Method | How it works | Assurance | Coverage | Cost and friction |
| --- | --- | --- | --- | --- |
| **Bank-based eID** (BankID in Norway and Sweden, itsme in Belgium, iDIN in the Netherlands) | The user authenticates with their bank's identity service; the platform receives verified attributes | High | Strong in its country; zero outside | Per-use fee; very low friction for users who have it |
| **EU Digital Identity Wallet** | The user presents attributes from a government-backed wallet, with selective disclosure | High, by design | Rolling out from the end of 2026; uneven by country | Fees and relying-party registration rules still settling |
| **Document plus liveness** | The user photographs an identity document and takes a selfie video; a vendor checks both | Substantial | Any country with machine-readable documents | Highest friction; vendor fees; demographic accuracy must be tested |
| **Payment-instrument name match** | A card or bank account in the user's name is verified by a payment provider | Substantial for payees | Anyone with a bank account | Cheap; proves account control, not innocence |
| Phone carrier lookup | Checks that a number is real, not virtual, and how long it has been held | Low | Varies by carrier | Cheap; weak against SIM farms |

FINN is the clearest documented example of a bank-based eID used for marketplace trust. Its help center, in articles first published in November 2024 and updated in October 2026, says that a user who verifies with BankID gets a symbol on the profile that buyers and sellers see when they make contact, and that "people with this symbol are experienced as safer to trade with". The user can still choose the display name, while FINN knows which BankID verified the account. Only **one** of a person's FINN users can be verified with the same BankID. Verification is mostly voluntary, but it can be required, for example to contact advertisers in some categories or for activity that needs extra security, "to protect you and others against fraud and misuse". Business advertisers do not need to verify ([FINN help center, "Why verify my user?", 2024, updated 2026](https://hjelpesenter.finn.no/hc/no/articles/22642799684754-Hvorfor-verifisere-brukeren-min); [FINN help center, "How do I become a verified user?", 2024, updated 2026](https://hjelpesenter.finn.no/hc/no/articles/22650637283858)).

Four design choices in that short description are worth copying:

1. **Verified, but pseudonymous.** The platform knows the legal identity; other users see a chosen name and a badge. Privacy and trust are not in conflict.
2. **One verified account per person.** The rule turns a proofing method into a defense against multi-accounting.
3. **Required only where risk concentrates.** Contacting advertisers in some categories, not registering.
4. **A different track for businesses.** Professional advertisers are verified as businesses, not as people.

The **EU Digital Identity Wallet** will change the method mix, but on a slower and narrower path than its publicity suggests. Regulation (EU) 2024/1183 requires each Member State to provide at least one wallet within 24 months of the entry into force of its implementing acts. The first of those acts were published on 4 December 2024, which puts the deadline at the end of 2026, consistent with the Commission's statement that wallets are due by the end of 2026 ([Regulation (EU) 2024/1183, Art. 5a](https://eur-lex.europa.eu/eli/reg/2024/1183/oj); [Commission Implementing Regulation (EU) 2024/2979](https://eur-lex.europa.eu/eli/reg_impl/2024/2979/oj); [European Commission, updated 2026](https://digital-strategy.ec.europa.eu/en/policies/eudi-regulation)). The rules for registering wallet-relying parties apply from 24 December 2026 ([Commission Implementing Regulation (EU) 2025/848](https://eur-lex.europa.eu/eli/reg_impl/2025/848/oj)).

The acceptance obligations for private companies are narrower than many product teams assume. Private relying parties must accept the wallet, on the user's request, only where Union or national law or a contract requires them to use strong user authentication for online identification, and only from 36 months after the implementing acts; small and micro enterprises are exempt. Very large online platforms under the DSA must accept it for user authentication when they require authentication ([Regulation (EU) 2024/1183, Art. 5f](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)). As of October 2026 no classifieds, real-estate or automotive marketplace is designated a very large online platform. For most marketplaces, the wallet is therefore **an option to adopt, not an obligation to meet**. It is a good option for exactly the B-ladder and L4 checks: the DSA already allows a trader to identify with "electronic identification" under the eIDAS framework instead of a document copy ([Regulation (EU) 2022/2065, Art. 30(1)(b)](https://eur-lex.europa.eu/eli/reg/2022/2065/oj)), and the wallet's selective disclosure lets a platform ask for "over 18" or "name matches" without receiving a birth date.

The architectural conclusion is that **the verification orchestrator must be pluggable by country and method**. A group operating in eight countries will run bank eIDs in some, the wallet in others, document checks as the universal fallback, and will change the mix every year. Each adapter writes the same claim.

{id: identity-and-verification--in-practice-the-group-identity-question}
## In Practice: The Group Identity Question

{id: identity-and-verification--what-a-shared-identity-looks-like-in-public}
### What a shared identity looks like in public

Schibsted's shared account, the longest-running public example of a marketplace group identity, shows what users feel when the group splits. FINN's help center describes Schibsted account as having been "the shared login solution for all Schibsted services", news media and marketplaces alike. When Schibsted split into two companies, Schibsted Media and Schibsted Marketplaces, the account was separated as well. Users who had used both media services, such as VG and Aftenposten, and marketplace services, such as FINN, ended up with **two accounts**; privacy choices that had applied to all services at once now had to be made per company; and the marketplace account moved to a new web address, so password managers no longer recognized it and some users were asked to set a new password ([FINN help center, "FAQ: Separation of Schibsted Accounts", February 2025, updated 2026](https://hjelpesenter.finn.no/hc/no/articles/24542252272018-FAQ-Separation-of-Schibsted-Accounts)).

Schibsted Marketplaces has since been renamed Vend, and FINN describes the Vend account as a shared login and payment solution for Vend services such as FINN.no, Helthjem and Morgenlevering ([FINN help center, 2025, updated 2026](https://hjelpesenter.finn.no/hc/no/articles/26512386856082-FINN-er-en-del-av-Vend-hva-betyr-det-for-deg); [FINN help center, "What is a Vend account?", updated 2026](https://hjelpesenter.finn.no/hc/no/articles/22650483740178-Hva-er-Vend-konto)).

> **INFERENCE, NOT DOCUMENTED:** The help-center texts describe the user-facing effects, not the internal design. A plausible reading, not a description of Schibsted's or Vend's systems, is that the shared identity carried user data and consents for two businesses in one store, and that separating them required deciding, per user and per data item, which company was the controller.

The lesson for a group architect is not that shared identity is wrong. FINN users kept one login across the marketplace services, and the shared account evidently served Schibsted for years. The lesson is that **a group identity is a bet on the group's shape**. When the shape changes through a demerger, a sale or a carve-out, the identity has to be cut along the new line, and users feel the cut. The [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta) case study makes the same point about shared platforms in general: the platform that a synergy case values can become a separation cost when the owners change strategy.

{id: identity-and-verification--veldmark-id-designed-to-be-cut}
### Veldmark ID: designed to be cut

Veldmark is majority-owned by a private-equity investor. Ingrid's design brief for Veldmark ID started from that fact: **assume any brand may be sold, and make the cut cheap.** The architecture advice forum adopted five rules in June 2027.

1. **One account, brand profiles.** The account holds credentials, authenticators, recovery methods and person-level claims. Each brand holds a profile with display name, ratings, favorites and brand settings. Profiles are created on first use of a brand, never in advance.
2. **Pairwise identifiers.** Each brand receives a different, stable subject identifier for the same person through OpenID Connect, so brand databases cannot be joined on a shared user ID. Cross-brand joins happen only inside the identity service and the fraud platform, under documented purposes.
3. **Controller per brand, processor for the group.** Brand data stays the brand's; Veldmark ID's operating entity processes authentication on the brands' behalf. Lucía Ortega's data map records, for every claim type, which entity is the controller.
4. **Separable by export.** A brand can be exported with its users: profiles, brand-scoped claims and a migration package that lets the buyer issue its own logins. Person-level claims a user earned in another brand do not travel unless the user consents.
5. **Keybridge stays outside.** Keybridge is a neutral SaaS business for agencies, and Veldmark committed in March 2027 not to use Keybridge agency data for Hearthly's advantage. Keybridge staff logins remain in Keybridge's own identity system, federated to agency single sign-on, and Veldmark ID never sees them.

| Option | What users see | What the group gains | What it costs | When it is right |
| --- | --- | --- | --- | --- |
| **Per-brand identity** (Veldmark in 2026) | A login per brand | Nothing shared; trivial separation | Four ban lists, four authentication stacks, no cross-brand trust | Brands with no shared users, or a group about to sell everything |
| **Shared identity, shared profile** | One account, one public persona across brands | Simple; maximal signal sharing | Privacy surprises ("why does the car site know my bike sales?"); expensive separation | Brands sold as one product family |
| **Shared identity, brand profiles, pairwise IDs** (Veldmark ID) | One login, separate personas | Shared authentication, recovery, verification and bans | Identity service is critical infrastructure; careful controller mapping | Multi-brand groups that may change shape |
| **Federation broker over brand identity providers** | Login per brand, linked on request | Gradual adoption without migration | Weakest-link security; four stacks remain | Transition state after an acquisition |

Veldmark chose the third option, and planned to pass through the fourth for Hearthly.es, whose Casavista login would be federated in 2028 and migrated in 2029.

![One shared account hub with three brand profile cards attached along dashed cut lines, one of them detached cleanly with its users.](listing-systems-architecture/posts/26-identity-and-verification/assets/images/26-identity-and-verification/identity-designed-to-be-cut.jpeg)

**Figure 4:** *Veldmark ID shares one account but gives each brand its own profile and its own identifier, so a brand that is sold can be cut out with its users.*

{id: identity-and-verification--the-barcelona-fake-rental-ring-a-policy-worth-its-cost}
### The Barcelona fake-rental ring: a policy worth its cost

The first policy built on the level model came from Hearthly Spain. In **July 2027**, **26** accounts posted **180** fake rental listings in Eixample, using photos stolen from real listings and prices about 35% below market, and asked for deposits by bank transfer outside the platform. **63** people reported losses of about **€71,000** before the listings came down. [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention) follows the detection: perceptual-hash matches against existing listings and price anomalies. The identity question was simpler and more uncomfortable. None of the 26 accounts had been asked to prove anything beyond an e-mail address, because Hearthly Spain, like Casavista before it, required nothing more of private landlords.

Aisha and Julien Marchand, Hearthly's CTO, proposed a policy for the forum: **private landlords publishing a rental in Spain must reach L4** before the listing goes live, with the name on the identity claim matching the landlord's display name. Agencies were unaffected, because they publish under B2 business claims through feeds. The forum asked for the cost before approving it. The numbers below are Veldmark's planning estimates.

| Quantity (Hearthly ES) | Estimate |
| --- | --- |
| New rental listings by private landlords per week | about 5,200 |
| Of which by landlords not yet at L4 | about 1,900 |
| Verifications started per week, after expected drop-out | about 1,600 |
| Blended cost per verification (document and liveness; Hearthly has no bank eID contract in Spain) | about €1.40 |
| Annual verification cost | about €115,000 |
| Expected drop-out of honest landlords at the verification step | 8–12% in the first quarter |
| Losses reported in one ring, July 2027 | about €71,000, plus support and reputation cost |

The forum approved the policy in September 2027 with two conditions. Drop-out had to be measured weekly against a control region, and landlords who abandoned verification had to be offered the old path through a partner agency, so that supply did not quietly shrink. The rule went live in **Q4 2027**. It did not stop fraud. It made each fake landlord cost a real, checkable identity, which is what the Barcelona ring had lacked.

{id: identity-and-verification--motorvane-from-kyb-at-signature-to-continuous-kyb}
### Motorvane: from KYB at signature to continuous KYB

Motorvane's 21,400 dealers were checked once, at contract signature, by the sales team. A pilot in June 2027 re-checked every dealer against the German trade register and the EU's VAT number validation service (VIES). It found **212** dealer accounts whose register entry had been deleted or whose VAT number no longer validated; **37** still had live listings. Most were dealerships that had closed or merged, with an employee still logged in. A few were not.

The fix was to make business claims expire. Veldmark's business registry now re-checks register and VAT claims every 90 days, re-verifies the onboarding person's L4 claim when a dealer's administrator changes, and emits a `BusinessClaimRevoked` event that suspends listing publication until the dealer's account manager resolves it. Under the DSA, a marketplace that has reason to believe a trader's information is inaccurate must ask for correction and, if it is not corrected, swiftly suspend the trader's offers to EU consumers ([Regulation (EU) 2022/2065, Art. 30(3)](https://eur-lex.europa.eu/eli/reg/2022/2065/oj)). Continuous KYB is how a platform notices.

{id: identity-and-verification--femke-s-account-rebuilt}
### Femke's account, rebuilt

Run the March incident again under Veldmark ID's level policy for Tradeyard Netherlands. The scammer's account would still be L2: e-mail confirmed, phone confirmed. Under the new policy, an L2 account younger than 30 days that sends a message containing a link to a domain outside Veldmark's allow list has the message held for a risk check, and the link rendered as text. The domain registered that day fails the check. Femke never sees the link.

Femke's own account shows what a badge should say. When Femke sold the bike through Safe Deal on 8 March, Adyen had already verified her as a payee, because Adyen must do so before it pays anyone out. In 2027 that fact lived only in Adyen and in a Safe Deal table. Under Veldmark ID it arrives as a `payee.verified` claim with Adyen as its source, and Tradeyard shows buyers the badge "Payouts verified by our payment partner". It does not show "Verified". The difference is the point.

{id: identity-and-verification--trade-offs}
## Trade-offs

{id: identity-and-verification--when-to-ask-for-identity}
### When to ask for identity

| Approach | Conversion | Fraud resistance | Data held | When it is right |
| --- | --- | --- | --- | --- |
| **Identity at registration** (everyone proves themselves) | Lowest; every casual seller pays the cost | High, but uniform | Most | Small, high-value, high-risk markets (rentals in a fraud-heavy city; high-value equipment) |
| **Identity by action** (step-up at risky moments) | High for the many; friction for the few | High where it matters | Proportional | The default for horizontal and vertical marketplaces |
| **Identity by incentive** (badges and ranking benefits for verified users) | High | Moderate; fraudsters skip it | Proportional | Complement to step-up; where buyers can choose verified sellers |
| **No identity beyond e-mail** | Highest | Low; Fast Mail for Fraudsters | Least | Never at scale for marketplaces with off-platform payment |

{id: identity-and-verification--build-buy-or-federate}
### Build, buy or federate

| Capability | Build | Buy | Comment |
| --- | --- | --- | --- |
| Authentication and sessions | Often, on a standard OIDC server | Customer identity platforms | Either works; the group must own the account data model and migration |
| Passkeys | Use platform standards (WebAuthn) | Included in most identity platforms | Do not build cryptography |
| Document and liveness checks | Rarely | Usually, from more than one vendor | Keep vendor neutrality through the claim contract |
| Bank eID and wallet adapters | Thin adapters | Aggregators exist per region | Per-country contracts and fees |
| Claim store, levels, badges | **Build** | — | This is the group's trust vocabulary; no vendor knows the policies |
| Business registry | **Build**, with register data feeds | Register data from providers | Joins identity with [Private Sellers, Dealers and Agencies: Modeling Who Lists](#sellers-and-accounts) organizations |

{id: identity-and-verification--vertical-differences}
## Vertical Differences

| Topic | General classifieds | Real estate | Automotive | Jobs (where relevant) |
| --- | --- | --- | --- | --- |
| Who lists | Mostly private sellers (78% of Tradeyard's new listings) | Mostly agencies via feeds (84% at Hearthly); private landlords are the risk | Mostly dealers (91% at Motorvane) via DMS feeds | Employers and recruiters |
| Main identity risk | Fake buyers and phishing in messaging; account takeover of aged accounts | Fake landlords and stolen photos; fake agencies | Deposit scams by fake private sellers; dealer accounts of closed businesses | Fake employers harvesting candidate data or charging fees |
| Key check | Phone and passkey for many; L4 for payees and high-risk categories | B2 or B3 for agencies; L4 for private landlords in risky markets | B2 with dealer contract; vehicle registration document for private sellers in high-value bands | B2 for employers; domain-verified e-mail for recruiters |
| Badge buyers understand | "Identity verified", "Payouts verified" | "Registered agency", professional licence where it exists | "Approved dealer", "Seller identity verified" | "Verified employer" |
| Sensitive data on the other side | Low | **High**: tenant application files with income and identity documents (Hearthly's rental services) | Medium: financing applications | **High**: CVs |

On a rental portal, identity risk runs in both directions. A fake landlord defrauds tenants, and a fake "tenant" or a careless agency can harvest tenants' identity documents from application files. Hearthly's tenant application files therefore carry their own access rules: the tenant shares a file with a specific listing, the agency sees it for a limited time, and every view is logged. Identity for the person *receiving* sensitive data matters as much as identity for the person posting a listing.

{id: identity-and-verification--failure-modes}
## Failure Modes

1. **"Verified" means five things.** A green tick for phone confirmation in one brand, for an ID check in another and for a dealer contract in a third. Buyers cannot tell, and the platform cannot defend any of them.
2. **Badges that outlive their claims.** A dealer's "approved" badge after the business closed; an "identity verified" badge after an account takeover. Badges must follow claim status and posture changes in near real time.
3. **SMS as proof of person.** A phone confirmation proves short-term control of a number. Treating it as identity hands the green tick to SIM farms, as the March 2027 scammer showed.
4. **A strong login with a weak recovery.** Passkeys for login, but support agents restore accounts after a few questions. The attacker uses the support line.
5. **Merging accounts by e-mail string.** A group identity migration that links brand accounts because the e-mail addresses match invites pre-hijacking and silently grants one person's history to another.
6. **Evidence everywhere.** Passport images in support tickets, in a vendor portal, in a data warehouse table "for analysis". Each copy is a breach waiting to happen and a GDPR minimization failure.
7. **Verification without measurement.** No one tracks drop-out at the verification step, fraud rates per level, or false rejections by document type and country. A check that rejects honest users from one country more often than others is a fairness problem as well as a conversion problem.
8. **Vendor lock-in through the data model.** Policies written as "requires vendor X check" and vendor case IDs used as user attributes. Changing vendor becomes a migration.

{id: identity-and-verification--the-chief-architect-s-view}
## The Chief Architect's View

**Decide the vocabulary centrally, the thresholds locally.** The group should own the claim types, assurance levels, identity levels and badge catalog, the way it owns the listing event contract. Brands and countries decide which actions require which level, within group guardrails, because a bike market in Rotterdam and a rental market in Barcelona carry different risks. Aisha's trust-and-safety team proposes level policies; product owns the friction; Lucía signs off the data each policy collects.

**Treat identity as tier-zero infrastructure.** When Veldmark ID is down, nobody can log in to any brand. It needs the reliability engineering of the search platform, not of an internal tool: multiple availability zones, degraded modes (existing sessions keep working; new logins queue), and a tested regional failover. [Sunday Evening Peaks: Reliability, Performance and Cost](#reliability-and-scale) covers the patterns.

**Make separability a requirement, not a hope.** Pairwise identifiers, controller mapping and brand export are cheap to build at the start and expensive to retrofit. A private-equity owner will eventually ask what it costs to sell one brand. The identity service should have an answer measured in weeks.

**Budget for verification as a variable cost.** Document checks and bank eIDs are priced per use. A policy that requires L4 for an action has a cost per listing or per payout that belongs in the business case of that policy, next to the fraud losses it prevents and the honest users it loses.

**Watch four numbers.** Account-takeover rate per 100,000 active accounts. Share of active accounts at L3 or above (passkey coverage). Drop-out rate at each verification step, by country and method. Fraud reports per 1,000 contacts, by the sender's identity level. If fraud does not fall as levels rise, the levels are measuring the wrong thing.

**Keep the EU Digital Identity Wallet on the roadmap, not on the critical path.** Build the adapter when wallets are available in a market where Veldmark operates and the fees are known. Do not design a policy that depends on wallet take-up nobody can forecast yet.

{id: identity-and-verification--questions-to-ask}
## Questions to Ask

1. What exactly does each badge in each brand promise, and could a buyer read it as "safe to pay"?
2. Which actions require which identity level, and who approved each requirement and its cost?
3. Are identity levels derived from claims with expiry and revocation, or stored as a flag someone set?
4. What assurance does account recovery require, and is it at least the assurance the account had?
5. What share of active accounts can be phished by password today, and what is the plan to reduce it?
6. Where are identity documents and selfies stored, by whom, for how long, and who can see them?
7. If we change our document-verification vendor, which policies, tables and screens change?
8. How do we link accounts across brands, and could an attacker who registered first with a victim's e-mail inherit the victim's account?
9. Which business claims do we re-check, how often, and what happens to listings when a check fails?
10. If one brand were sold next year, how would its users and their claims leave, and how long would it take?

{id: identity-and-verification--from-identity-to-obligation}
## From Identity to Obligation

Identity answers who is on the other side. Much of what this chapter built, the trader record, the business registry, the evidence trail and the minimization rules, exists because the law now asks marketplaces to know their traders and to explain their decisions. [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation) takes up those rules directly: the Digital Services Act, seller tax reporting under DAC7, ranking and consumer transparency, and the vertical rules for property and car listings, and shows how to turn them into system requirements rather than annual projects.

{id: identity-and-verification--sources-and-evidence}
## Sources and Evidence

{id: identity-and-verification--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Bridging the gap between passwords and passkeys with risk-based authentication](https://engineering.mercari.com/en/blog/entry/20260730-bridging-the-gap-between-passwords-and-passkeys-with-risk-based-authentication/) — Tatsuya Karino, Mercari Engineering, 2026. About 13 million passkey users; phishing-resistant accounts; session and account posture; recovery rules.
- [Hvorfor verifisere brukeren min? (Why verify my user?)](https://hjelpesenter.finn.no/hc/no/articles/22642799684754-Hvorfor-verifisere-brukeren-min) — FINN help center, 2024 (updated 2026). BankID verification badge, one verified user per BankID, required in some categories, not for business advertisers.
- [Hvordan blir jeg en verifisert bruker? (How do I become a verified user?)](https://hjelpesenter.finn.no/hc/no/articles/22650637283858) — FINN help center, 2024 (updated 2026). Verification flow and display-name choice.
- [Beskytt kontoen din med totrinnsautentisering (Protect your account with two-step authentication)](https://hjelpesenter.finn.no/hc/no/articles/22642951164434-Beskytt-kontoen-din-med-totrinnsautentisering) — FINN help center, 2024 (updated 2026). Account takeovers observed on FINN; consequences; two-step authentication.
- [FAQ: Separation of Schibsted Accounts](https://hjelpesenter.finn.no/hc/no/articles/24542252272018-FAQ-Separation-of-Schibsted-Accounts) — FINN help center, 2025 (updated 2026). Shared Schibsted login split into media and marketplace accounts after the company separation.
- [FINN er en del av Vend (FINN is part of Vend)](https://hjelpesenter.finn.no/hc/no/articles/26512386856082-FINN-er-en-del-av-Vend-hva-betyr-det-for-deg) and [Hva er Vend-konto? (What is a Vend account?)](https://hjelpesenter.finn.no/hc/no/articles/22650483740178-Hva-er-Vend-konto) — FINN help center, 2025 and 2024 (both updated 2026). Rename to Vend; shared login and payment account; e-mail one-time code login.
- [Verification overview (Adyen for Platforms)](https://docs.adyen.com/platforms/verification-overview) — Adyen, n.d. (current documentation). KYC of platform users before payouts; re-verification on data change.

{id: identity-and-verification--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Regulation (EU) 2022/2065 (Digital Services Act)](https://eur-lex.europa.eu/eli/reg/2022/2065/oj) — Official Journal, 2022. Art. 30 trader traceability, including electronic identification and correction or suspension; text checked against the Official Journal version.
- [Regulation (EU) 2024/1183 (European Digital Identity Framework)](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) — Official Journal, 2024. Art. 5a wallet provision; Art. 5f acceptance by private relying parties and very large online platforms.
- [Commission Implementing Regulation (EU) 2024/2979](https://eur-lex.europa.eu/eli/reg_impl/2024/2979/oj) — Official Journal, 2024. Wallet integrity and core functions; published 4 December 2024.
- [Commission Implementing Regulation (EU) 2025/848](https://eur-lex.europa.eu/eli/reg_impl/2025/848/oj) — Official Journal, 2025. Registration of wallet-relying parties; applies from 24 December 2026.
- [European Digital Identity Regulation](https://digital-strategy.ec.europa.eu/en/policies/eudi-regulation) — European Commission, updated 2026. Wallets due by the end of 2026.
- [Regulation (EU) 2016/679 (GDPR)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) — Official Journal, 2016. Data minimization (Art. 5(1)(c)) and data protection by design (Art. 25).
- [NIST SP 800-63-4, Digital Identity Guidelines](https://csrc.nist.gov/pubs/sp/800/63/4/final) — NIST, 2025. Identity, authenticator and federation assurance as separate axes.
- [NIST SP 800-63B-4, Appendix B: Syncable Authenticators](https://pages.nist.gov/800-63-4/sp800-63b/syncable) — NIST, 2025. Synced passkeys acceptable up to the middle assurance level.
- [Passkeys](https://fidoalliance.org/passkeys/) — FIDO Alliance, n.d. Definition of passkeys; synced and device-bound variants.

{id: identity-and-verification--research-and-practitioner-sources}
### Research and practitioner sources

- [Pre-hijacked accounts: an empirical study of security failures in user account creation on the web](https://arxiv.org/abs/2205.10174) — Avinash Sudhodanan and Andrew Paverd, USENIX Security, 2022. Five pre-hijacking attack types; 35 of 75 services vulnerable.
- [Fraudulent advertising and account integrity: expert insights on best practice](https://www.ofcom.org.uk/siteassets/resources/documents/research-and-data/online-advertising/fraudulent-advertising-and-account-integrity_expert-insights-on-best-practice.pdf) — Integrity Institute for Ofcom, 2026. Takeover to gain verification marks; friction between account creation and reach.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
