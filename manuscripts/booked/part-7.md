{class: part, id: part-7}
# Part VII — TRUST: Making Strangers Safe to Stay With

![Part VII — TRUST: Making Strangers Safe to Stay With — logo](stays-marketplace-architecture/posts/part-7-intro/assets/images/part-7-intro/logo.jpeg)

> **IN THIS PART, YOU WILL:** Build the trust layer of both marketplaces: the trust platform, fraud on both sides, identity and access, reviews, protection and incident response, and the regulations that become system requirements.

> **WHY THE BUSINESS CARES:** Corvane, the fictional group this book follows, lost or reimbursed €48,540 on one fake property manager and €212,000 after one extranet phishing wave in 2027. Clumsy controls cost too: declined bookings and suspended honest hosts.

> **WHY ARCHITECTS SHOULD CARE:** Trust touches every write path. When each domain keeps its own checks and its own "blocked" flag, nobody can say what was decided about a person, under which rule, or whether every system obeyed.

> **KEY POINTS:**
>
> * **Keep detection local and decisions shared.** Fraud, screening and review models belong with the brand that knows the risk. The decision and its enforcement belong to one platform with one record, and an action is done only when every consumer has confirmed it.
> * **Ask for trust in proportion to the action and the moment.** Identity levels, step-up sign-in, deferred fraud review and screening apply where a loss becomes irreversible (a payout, a virtual card, an entire home on a holiday weekend), not at the door.
> * **Write rules and promises as versioned data with evidence.** Trust policies, review eligibility, protection terms and market rules each carry a source, an effective date and an owner. Stamp the version on every decision so it can be explained, appealed, reported and reversed.

> **[FAILURE PATTERNS THIS PART ADDRESSES](#where-stay-platforms-go-wrong):**
>
> * **Trust After the Incident** — Replaces one tool per headline with one platform that new detectors plug into.
> * **The Unwatched Model** — Gives screening, fraud and review models owners, policy versions and outcome labels from claims, chargebacks and appeals.
> * **City-by-City Firefighting** — Turns each new registration regime or night cap into a rule version in one registry.

Part VI followed the money. Part VII turns to **what makes strangers willing to send it**: confidence that the home exists, the message is genuine, the review is real and someone will help when the night goes wrong.

The argument of this part is that **trust is a platform of records, not a collection of tools**. Most marketplaces accumulate trust and safety one incident at a time. These chapters build one decision record, one enforcement path, one identity layer, one review log and one rule registry, with detectors and thresholds kept per marketplace.

![Before and after: a messy drawer of separate trust tools each with its own red flag, versus one ledger-like platform with detector modules plugged in around it.](stays-marketplace-architecture/posts/part-7-intro/assets/images/part-7-intro/part-7-tools-to-platform.jpeg)

**Figure 1:** *Trust accumulated one incident at a time becomes a drawer of separate tools, each with its own blocked flag; Part VII rebuilds it as one platform of records that every detector plugs into.*

Hotels and homes differ sharply here. A hotel guest trusts a licensed, staffed, insured business, so an accommodation marketplace leaves identity checks, insurance and most short-term-rental law to the hotel. Its weak point is the supply side: hotel staff accounts, stolen and used to message real guests. A hosted-stays marketplace puts **two strangers in one home**. It verifies both, screens bookings for parties, funds a guarantee, runs two-way reviews and checks registration rules on almost every listing. An OTA (online travel agency) inherits these problems with its apartments.

![Brand detectors, Corvane ID, Ordinance and Vouch feed the Warden decision hub, which sends enforcement to consumer systems, receives receipts back, and sends reasons to statements and regulator reports.](stays-marketplace-architecture/posts/part-7-intro/assets/images/part-7-intro/part-7-trust-platform-of-records.jpeg)

**Figure 2:** *Each brand keeps its detectors; identity, reviews and market rules feed one decision record. Enforcement goes to every system that must obey, receipts come back, and each decision keeps the reason and policy version that explain it.*

Corvane builds this layer through 2027, incident by incident: The 2026 Spanish registration purge leads to **Ordinance** (March). A review-trading ring leads to **Vouch** (May). Three logins and 9.4 million stored passport images lead to **Corvane ID** (June). A fake Valencia property manager leads to **Warden** (August). A Dubrovnik party and a phishing wave test it while it is being built.

{id: part-7--chapters-in-this-part}
## Chapters in this part

[Trust as a Platform: Trust and Safety for Stays](#stays-trust-and-safety) defines **the platform the other chapters plug into**: one decision record, enforcement with receipts and statements of reasons. Its case is Turia Homes, whose suspension on Nookaway reached Roomstead 16 days late; Warden's replay avoids €31,640 of the loss. Read it when a suspension in one system does not stop the same person in the next.

[Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud) covers **fraud on both sides of the booking** and treats the partner account as the perimeter. In Roomstead's November 2027 phishing wave, 310 guests paid fraudsters who wrote from real hotel accounts; the answer is booking risk scores on Warden and Partner Shield. Read it when fraud controls sit in separate teams.

[Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access) decides **how much to know about guests, hosts and staff, and what each may do**. It separates the person from the brand account and evaluates delegation grants in one engine. Read it before planning a group login.

[Trustworthy Reviews: Collection, Integrity and Quality Operations](#reviews-and-reputation) makes **a review a fact about a completed stay**, checked before publication and kept in one event log that every score and credential derives from. Nookaway's ring of 3,610 traded reviews is the case. Read it when removing a review does not change every number built on it.

[Damage, Parties and Emergencies: Protection and Incident Response](#protection-and-incidents) treats **screening, the in-stay incident and the claim as one lifecycle on the reservation**, with protection terms as versioned policy and claims in the ledger. The Dubrovnik party, three case numbers in three tools, is the case. Read it when protection is a cost line nobody can reconcile.

[Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation) maps **short-term-rental, platform, consumer, data and AI law** onto a market policy registry, a few enforcement points and an evidence trail. Ordinance classifies the 6,900 Spanish removals in under an hour, work that took nine analysts seven weeks. Read it when a rule change or a court ruling becomes an emergency.

[Part VIII — PLATFORM: The Distributed System Underneath](#part-8) then turns to the distributed platform underneath. Begin with [Trust as a Platform: Trust and Safety for Stays](#stays-trust-and-safety).
