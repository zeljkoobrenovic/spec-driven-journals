{class: part, id: part-10}
# Part X — PRACTICE: How Others Built It

![Part X — PRACTICE: How Others Built It — logo](stays-marketplace-architecture/posts/part-10-intro/assets/images/part-10-intro/logo.jpeg)

> **IN THIS PART, YOU WILL:** Test the book's patterns against four public cases: Booking.com, Airbnb, Expedia Group with Vrbo, and the Asian online travel agencies (OTAs) Agoda and Trip.com, separating what was documented, and when, from interpretation.

> **WHY THE BUSINESS CARES:** These are the competitors and channels every stays business measures itself against, and their filings price their choices: Expedia lowered its 2024 guidance in May 2024, citing Vrbo's slower-than-anticipated recovery after re-platforming.

> **WHY ARCHITECTS SHOULD CARE:** Parts I–IX argue from principles and a fictional group; here the argument meets evidence the author did not design.

> **KEY POINTS:**
>
> * **The record is richest on contracts and platforms, and silent on the engines the book cares most about.** Booking.com publishes its connectivity contract and Airbnb its payments history, but no company documents its availability engine, calendar concurrency or reservation state machine.
> * **Hotels and homes stay different underneath convergence.** Booking.com carries about 3.9 million homes on a room-type model with home-specific seams; Expedia's 2026 partner API still sells Vrbo homes as single-unit, uncached offers; Airbnb rebuilt billing tied to "a reservation for a stay" before selling services and hotels.
> * **Contracts and money models outlive the technology underneath.** Booking.com's connectivity contract survived its move from Perl on bare metal toward Kubernetes and AWS, custody shaped Airbnb's payments more than any technology choice, and regulators now read ranking and commission as architecture.

> **[FAILURE PATTERNS THIS PART ADDRESSES](#where-stay-platforms-go-wrong):**
>
> * **The Hotel-Shaped Home** — Booking.com's grafted home seams, Vrbo's slow recovery on a hotel-led front end and Airbnb's stay-shaped billing show it from three directions.
> * **Phantom Availability** — Agoda's price cache and Expedia's opposite rules for hotel copies and Vrbo calendars show what selling from a copy demands.
> * **Pay-to-Rank Creep** — Booking.com's disclosed commission and program influences drew three regulators, and Agoda sells a ranking boost whose bounds are not public.

[Built for the Next Disruption: Evolving a Stays Platform Over a Decade](#evolving-the-platform) closed the book's argument. Part X asks **whether it survives contact with what real companies built and published**. The cases are not company profiles; each asks what the record implies for an architect who is not that company.

{id: part-10--how-to-read-the-cases}
## How to read the cases

Part X follows stricter evidence rules than Parts I–IX. Every statement is one of three kinds.

| Kind of statement | How you recognize it |
| --- | --- |
| **Documented fact** | Source and publication year in the sentence or the timeline. A 2017 talk is a 2017 talk: true at the date of its source, and no later. |
| **The author's interpretation** | Marked "my reading", or placed in the Chief Architect's view. |
| **Reference-architecture inference** | Only in a callout labeled `INFERENCE, NOT DOCUMENTED`. It describes how a system *could* be built, never how a company *did* build it. |

Each case has a **Where the Public Evidence Stops** table. **The depth of each case follows the evidence, not the importance of the company.**

![A cutaway building with lit upper rooms labeled Contracts, Platforms and Payments, and a dark basement labeled Engines that an architect's flashlight cannot reach.](stays-marketplace-architecture/posts/part-10-intro/assets/images/part-10-intro/part-10-lit-and-dark-record.jpeg)

**Figure 1:** *The public record is richest on contracts, platforms and payments, and silent on the availability engines, calendars and reservation state machines the book cares most about.*

Corvane, the fictional travel group this book follows ([Meet Corvane: Two Marketplaces, One Group](#meet-corvane)), appears only in each case's final comparison. Roomstead is not a disguised Booking.com or Expedia, and Nookaway is not a disguised Airbnb or Vrbo. Keeping them apart stops the record from being stretched to fit the fiction.

{id: part-10--the-cases-side-by-side}
## The cases side by side

| Company | Marketplace type | Payment model | Documented architecture themes | Evidence strength |
| --- | --- | --- | --- | --- |
| **Booking.com** | Accommodation marketplace; 3.9 million of its 4.4 million properties are homes (2025) | Agency shifting to merchant: 70% of Booking Holdings' gross bookings merchant (2025) | Published connectivity contract; about 1,000 parallel experiments (2026); Perl to Node.js behind experiments | Strong and dated; dark on availability search |
| **Airbnb** | Hosted stays, adding services, experiences and hotels (2025–2026) | Merchant of record; holds funds until check-in ($12.2 billion, June 2026) | Monorail to a GraphQL data mesh; payments rebuilt around the bill; search research | Strong on platforms, payments and search; silent on the calendar |
| **Expedia Group and Vrbo** | Both: about 1.2 million hotels and other properties, 2.4 million Vrbo homes (2025) | Merchant or agency for hotels; Vrbo pre-paid, with schedules and deposits | One front end for three brands (2021–2023); shared services (2026); distinct Vrbo rules in the partner API | Precise in filings and partner APIs; inventory engines not public |
| **Agoda and Trip.com** | OTAs built around Asia-Pacific demand | Agoda: pay now or later. Trip.com: agent, with allotment and on-request contracts | Agoda: price cache, rationed supplier queries, cross-data-center deduplication. Trip.com: hotel matching | Agoda: engineering-rich. Trip.com: one filing and three repositories |

![Four case folders each pointing to the book claim it tests, all claims converging on a verdict scale, and a dashed arrow to a pencil-sketched fictional Corvane compared last.](stays-marketplace-architecture/posts/part-10-intro/assets/images/part-10-intro/part-10-cases-test-claims.jpeg)

**Figure 2:** *Each case tests one of the book's claims against the public record and reaches a verdict before fictional Corvane enters the comparison.*

{id: part-10--chapters-in-this-part}
## Chapters in this part

[Booking.com: Experimentation, Connectivity and the Agency Model at Scale](#case-booking-com) reads **the best-documented accommodation marketplace**: a supply contract that outlived a technology era, experimentation as the way the platform changes, and commission and ranking turned into compliance. It qualifies one claim: a room-type model can carry homes at scale, at the cost of grafted seams. Read it when you design a partner contract or a ranking policy.

[Airbnb: From Monolith to Platform for Hosted Stays](#case-airbnb) traces **the hosted-stays reference case** from 2016 to 2026: the Monorail migration, payments built around custody and then the bill, one-unit search research, trust as a product and the expansion beyond homes. Its calendar is never described. Read it before you decide custody or migrate a monolith.

[Expedia Group and Vrbo: Consolidating Brands Onto One Platform](#case-expedia-vrbo) follows **one group consolidating a hotel brand and a homes brand** onto one front end, through the May 2024 guidance cut. Its partner API shows convergence stopping at the offer. Read it before a brand re-platforming; Corvane's Mariana Costa uses it to set a 3% booking guardrail on Nookaway's 2028 migration.

[Agoda and Trip.com: Asian OTAs at Scale](#case-agoda-trip-com) sets **an engineering-rich record beside a filing-only one**. Agoda shows the price cache, booking for partial failure and a port that carried old coupling into new code; Trip.com tests what an architect can conclude from a 20-F. Read it when you sell from a copy, or are tempted to fill a gap in the evidence.

The Reference section then maps coverage ([Domain Coverage: From Productscape Models to Chapters](#domain-coverage)) and offers templates ([Field Kit: Templates for the Stays Architect](#toolkit)). By the end of Part X you should know which patterns the record supports, which it qualifies and where it is silent. Begin with [Booking.com: Experimentation, Connectivity and the Agency Model at Scale](#case-booking-com).
