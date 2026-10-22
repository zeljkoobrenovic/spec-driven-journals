{class: part, id: part-5}
# Part V — TRUST: Keeping the Marketplace Safe

![Part V — TRUST: Keeping the Marketplace Safe — logo](listing-systems-architecture/posts/part-5-intro/assets/images/part-5-intro/logo.jpeg)

> **IN THIS PART, YOU WILL:** Architect trust and safety as a platform, stop fraud from fake listings to payment-link scams, decide how much to know about users and how to verify it, and turn the Digital Services Act and related rules into system requirements.

> **WHY THE BUSINESS CARES:** A scammed buyer rarely comes back, and a wrongly blocked seller tells other sellers. Since 2024 every EU moderation decision is also a record a regulator can ask about, and fines under the [Digital Services Act](https://eur-lex.europa.eu/eli/reg/2022/2065/oj) can reach 6% of worldwide turnover.

> **WHY ARCHITECTS SHOULD CARE:** Trust touches insertion, search, messaging, alerts, payments and ads. Without one decision record, one propagation path and one identity model, a group cannot say what it removed, why, or whether the removal took effect.

> **KEY POINTS:**
>
> * **Trust and safety is a platform of separate functions joined by one decision record.** Policy, detection, decision, enforcement and review change at different speeds. Share the machinery, keep policy local, and count an enforcement action as done only when every consumer has applied it.
> * **Fraud is caught at the setup, by scoring actors and adding friction in proportion to risk.** In classifieds the money usually leaves by bank transfer. Link listings, accounts, devices, payment accounts and photos, and ask for identity at the moment of risk, not at the door.
> * **Regulation asks for a few artifacts, built once.** A decision record, a trader record, disclosure surfaces and reproducible reports serve most obligations, and every regulated number should be computable again from the event log.

> **[FAILURE PATTERNS THIS PART ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Moderation as an Afterthought** — Replaces a queue bolted onto insertion with a platform that produces evidence by design.
> * **Fast Mail for Fraudsters** — Puts link, pattern and identity controls into the channel where scams close.
> * **Deal-Shaped Architecture** — Replaces four ban lists and four logins with shared signals and one group identity.

Part IV built surfaces that put listings in front of buyers within seconds. Fraudsters exploit that speed: a fake rental that reaches saved searches in minutes reaches the most motivated victims first. Part V turns to **the trust that makes contact between strangers possible**.

This part argues that trust is **a platform capability, not a team with a queue**. Most marketplaces build it in the order incidents arrive, and a decade later the group has four moderation stacks that cannot share a signal. These chapters replace that history with one design: shared decision service, signals and evidence; local policy, thresholds and legal grounds.

![Four separate moderation stacks on the left contrasted with one shared trust platform carrying four brands, each with its own rulebook, on the right.](listing-systems-architecture/posts/part-5-intro/assets/images/part-5-intro/trust-shared-platform-local-policy.jpeg)

**Figure 1:** *Part V replaces four moderation stacks that cannot share a signal with one shared decision service, signals and evidence, while each brand keeps its own policy, thresholds and legal grounds.*

{id: part-5--chapters-in-this-part}
## Chapters in this part

| Chapter | The question it answers | Read it when… |
| --- | --- | --- |
| [Trust and Safety as a Platform](#trust-and-safety-architecture) | How should trust and safety be architected across listings, users, messages and transactions? | Each brand runs its own moderation stack, or removals never reach alerts and caches. |
| [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention) | How do marketplaces detect and stop fraud, from fake listings to payment scams? | Scams close in your messaging, or fraud signals land in separate queues. |
| [Who Is on the Other Side? Identity and Verification](#identity-and-verification) | How much should a marketplace know about its users, and how does it verify it? | You are designing a group login, verified badges or business checks. |
| [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation) | Which regulations shape the architecture, and how do they become requirements? | A transparency report cannot be reproduced, or a payments feature will move your legal perimeter. |

{id: part-5--how-this-part-connects}
## How this part connects

Trust reads the lifecycle and enforcement overlay from [Part II — LISTING: Modeling the Thing Being Sold](#part-2), the publication gate from [Part III — SUPPLY: Getting Inventory In](#part-3) and the discovery surfaces from [Part IV — DISCOVERY: Matching Intent to Inventory](#part-4), all of which must obey its decisions. It hands three threads to [Part VI — MONEY: Conversion and Monetization](#part-6). Messaging is where scams close. In-platform payments bring DAC7 seller reporting into scope. Trader records feed billing as well as compliance.

{id: part-5--the-veldmark-thread}
## The Veldmark thread

Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)), starts 2027 with four trust-and-safety stacks, four identity systems and five sources of statements of reasons. Two 2027 incidents show what that split costs. On 7 March 2027 a fake Safe Deal payment link reached Femke sixteen minutes after her first buyer contact. In July a Barcelona ring of 26 accounts posted 180 fake rentals, and 63 people lost about €71,000. Ingrid Halvorsen's team, with Aisha Rahman and Lucía Ortega, decides:

- **Veldmark ID** (June 2027): one login across brands with brand profiles, designed so that a sold brand can be cut out;
- an **obligation register** that maps the DSA and related rules to controls and evidence queries;
- a **shared trust-and-safety platform**, live for Tradeyard NL and BE in November 2027, with a cross-brand block list of hashed identifiers;
- **first-contact friction** on Tradeyard (December 2027).

By the end of Part V you should be able to say, for any enforcement decision, who made it, under which policy version, where it propagated and how you would prove all three a year later. Begin with [Trust and Safety as a Platform](#trust-and-safety-architecture).
