{class: part, id: part-9}
# Part IX — LEADERSHIP: The Chief Architect's Agenda

![Part IX — LEADERSHIP: The Chief Architect's Agenda — logo](stays-marketplace-architecture/posts/part-9-intro/assets/images/part-9-intro/logo.jpeg)

> **IN THIS PART, YOU WILL:** Take the decisions that belong to the group, not to any one domain: whether hotels and homes share a platform, how engineering is organized and governed, how a live booking monolith is retired, where AI assistants and agents may act, and how the platform stays coherent over a decade.

> **WHY THE BUSINESS CARES:** Corvane, the fictional group this book follows, approved €145 million for its One Stay program in April 2027. By December the CFO counted more than twenty shared systems where the board had approved seven lines, and the CEO asked what the group would be fixing in 2032.

> **WHY ARCHITECTS SHOULD CARE:** Parts II to VIII each ended with a judgement about what to share and who owns it. Those judgements only hold if someone keeps them in one place, gives each one an owner and moves the live platform toward them without losing a reservation.

> **KEY POINTS:**
>
> * **Share what follows the guest, the money and the law; keep what follows how supply is counted.** Identity, payments, tax, trust, messaging, data and the offer and reservation contracts become shared. Supply engines, connectivity and ranking stay with each type of supply, chosen by supply segment rather than by brand.
> * **Contracts outlast engines, teams and models.** The offer, the versioned reservation, the ledger and the place and policy registries are what migrations move first, what AI agents call as tools and what a successor engine must read. Engines, monoliths and models are replaceable behind them.
> * **Govern with records, not slogans.** A convergence register, an ownership catalog, three classes of decision, an AI use-case register and five fitness functions with named owners turn "one platform" and "future-proof" into decisions a board can check each year.

> **[FAILURE PATTERNS THIS PART ADDRESSES](#where-stay-platforms-go-wrong):**
>
> * **The Hotel-Shaped Home** — Replaces the "one platform" proposal with a register that keeps two supply engines and records why, so the merger pressure of each new cost review starts from evidence.
> * **Lost at the Front Desk** — Gives reservation delivery a journey owner, and moves millions of future reservations between systems without losing their partner identifiers or delivery state.
> * **The Unwatched Model** — Puts every model and every AI assistant or agent channel in one register with an owner, a consequence class and an evaluation against the systems of record.

Parts II to VIII designed a stays marketplace domain by domain. Part IX steps up to **the decisions only the group can take**: what is built once, who builds it, how the platform gets there while it keeps selling, and how it stays coherent after the people who designed it have moved on.

The argument of this part is that **the Chief Architect's main product is a small set of governed records**. A board's seven lines, an org chart, a migration date and an AI policy are each easy to approve and hard to keep true. Each chapter turns one of them into a record with owners, review dates and numbers.

![Slogans floating away as speech bubbles on the left; on the right the same ideas filed as binders with owners and review dates on a shelf of governed records.](stays-marketplace-architecture/posts/part-9-intro/assets/images/part-9-intro/p9-slogans-to-records.jpeg)

**Figure 1:** *A board slogan is easy to approve and hard to keep true; each chapter of this part turns one into a record with owners, review dates and numbers.*

Hotels and homes do not converge as neatly as a board paper suggests. Booking.com sells millions of homes and Airbnb sells boutique hotels. But the hard parts stay different: room-type inventory fed by hotel software against one calendar per home, a hotel's PMS (property-management system) holding a copy of every booking against a host's phone, a median booking window of 18 days at Roomstead against 41 at Nookaway. The guest-facing commitment converges; the supply machinery, the supply-side teams and the migration risks do not.

![A board question leads to a convergence register, which feeds org design, the Keystone exit plan and the AI register; all three feed fitness functions, and an orange arrow returns breaches to the register.](stays-marketplace-architecture/posts/part-9-intro/assets/images/part-9-intro/p9-governance-loop.jpeg)

**Figure 2:** *The board's question becomes a register of what is shared; owners, a migration plan and AI controls follow from it, and five fitness functions report each year whether the promise is kept, sending breaches back to the register.*

Corvane takes these decisions in the second half of 2027: the AI use-case register and Frontdoor v2 (October and November), One Stay Org Design v1 (19 October), and in December the register's first annual review, the Keystone Exit Plan and the five fitness functions.

{id: part-9--chapters-in-this-part}
## Chapters in this part

[One Platform or Two? Converging Hotels and Homes](#converging-two-marketplaces) answers **whether hotels and homes should share one platform** with a three-grade register: shared engine, shared contract, brand-specific. Corvane's register moves from 16 shared engines, 6 shared contracts and 26 brand-specific capabilities to 23, 6 and 20, and the review rules that Nookaway's 2028 boutique hotels run on the hotel engine. Read it when "one platform" appears in a board paper.

[Who Owns What: Organizing Engineering for Stays](#organizing-stays-engineering) decides **who owns journeys, engines and contracts**, and governs decisions by blast radius. Hotel Miradouro's missing reservations, touched by five teams and owned by none, and a five-week forum queue lead to Org Design v1: about 1,750 engineers in 190 teams. Read it when an incident crosses four teams and nobody owns the outcome.

[Changing the Engine in Flight: Modernizing a Live Stays Marketplace](#modernizing-a-live-marketplace) retires **a booking monolith that is still selling**. Keystone holds about 5.6 million future reservations; the first comparison finds 31,400 differences in five classes. The answer: contract first, market cohorts, arrival-date batches and a signed point of no return. Read it before setting a cutover date.

[AI Across the Stay: Agents, Assistants and Automation](#ai-in-travel-stays) puts **AI in front of the marketplace's contracts, never in place of them**. An assistant books a traveler into Porto in Corsica instead of Porto in Portugal, and the review finds 23 AI uses, 8 without an owner. Frontdoor v2 adds place ambiguity, binding quotes and an explicit booking authority. Read it before opening the platform to agents.

[Built for the Next Disruption: Evolving a Stays Platform Over a Decade](#evolving-the-platform) closes the book's argument with **stressor analysis and five stays fitness functions**: price accuracy, double-booking rate, reservation delivery, time to payout and cost per booking. Corvane traces nine stressors and runs an Algarve wildfire tabletop on existing parts. Read it when a board asks what the platform will survive.

[Part X — PRACTICE: How Others Built It](#part-10) then tests the book's patterns against four companies' public record. Begin with [One Platform or Two? Converging Hotels and Homes](#converging-two-marketplaces).
