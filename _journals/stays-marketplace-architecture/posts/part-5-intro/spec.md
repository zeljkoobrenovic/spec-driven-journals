---
status: accepted
revised: 2026-10-21
---

# Spec: Part V — BOOKING: Making and Keeping the Reservation

## Intent

Orient the reader to Part V: why the reservation is the object that crosses every boundary in the book and must be designed as a contract before it is built as a service, where hotels (delivery to a PMS, reported stay outcomes) and homes (often nothing to deliver, request to book, inferred stays, door codes) differ, and what each of the five chapters decides. Frame it through the Corvane systems and cases the chapters use (Turnstile and the checkout attempt key, Stayline, the policy engine and disruption registry, Threadline, Harbor).

Productscape domains: the union of the part's chapters (TAM book, rsrv, self, trip, msgc, supp; HSM book, trip, reso, grev triggers).

## Audience

Chief architects, booking, reservations and customer-service platform leads, and engineering directors responsible for the booking path.

## Success criteria

- [ ] Opens with IN THIS PART, WHY THE BUSINESS CARES, WHY ARCHITECTS SHOULD CARE, KEY POINTS (exactly three) and a FAILURE PATTERNS callout using exact names linked to where-stay-platforms-go-wrong.html.
- [ ] States the argument (the reservation as a cross-boundary contract) and names where hotels and homes differ in this part.
- [ ] One mermaid diagram (a state diagram of the reservation's journey) with a Figure caption.
- [ ] A "Chapters in this part" list with one paragraph per chapter in config order, each linking the chapter and saying what it decides.
- [ ] Corvane facts match the ledger and chapters: 212 duplicates (198 charged) on 14 January 2027, Miradouro's nineteen rejected reservations in July 2027, the 5–7 June 2027 strike, the "[hidden]" door code in August 2027, King's Day and Harbor.
- [ ] Ends with a hand-off to [[checkout-orchestration]]; 500–900 words of body.

## Non-goals

Teaching sagas, state machines, policy models or support tooling (the chapters own them); payments and refunds mechanics ([[part-6]]); external factual claims.

## Modalities

Article only for now.

## Open questions

None.

## Decision log

- 2026-10-21: Modeled on LISTED's part introductions, with a mermaid diagram and a paragraph-per-chapter list, per the BOOKED brief.
- 2026-10-21: Failure patterns: Lost at the Front Desk, Policy Spaghetti and Built for Sunny Days, each named by at least three of the part's five chapters.
- 2026-10-21: A state diagram rather than a flowchart, because the part's through-line is one object's lifecycle.

## Sources

`config.yaml`, `PLAN.md`, `_research/scenario-ledger.md`, and the callouts, leads, Setting the Scene sections and Chief Architect's views of [[checkout-orchestration]], [[reservation-lifecycle]], [[changes-and-cancellations]], [[trip-and-messaging]] and [[customer-service]]. No external factual claims.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: fictional-Corvane note added; links, figure and hand-off verified. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 1 mermaid diagram to an illustration and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
