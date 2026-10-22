---
status: accepted
revised: 2026-10-22
---

# Spec: AI Across the Stay: Agents, Assistants and Automation

## Intent

Show a Chief Architect where generative AI and agents act in a stays marketplace and what architecture keeps them controlled. The chapter's argument: **put AI in front of the marketplace's contracts, never in place of them** (places, offers, policies, reservations and trust decisions come from the systems of record through registered tools); **agentic booking needs an explicit booking authority** (a human final click by default, a signed mandate with named constraints by exception, and an actor chain on the reservation); and **AI is governed by the consequence of its actions** (five side-effect classes, one register of built and bought AI uses, claim checking against the systems of record). It owns **agentic booking** and **AI governance (stays)**. It covers the documented record 2023–2026 (Booking.com, Trip.com, Expedia Group, Airbnb, MCP, AP2, apps inside ChatGPT), AI for hosts and partners, AI in trust, evaluation, cost, liability (*Moffatt v. Air Canada*) and EU rules (AI Act Article 50, GDPR, consumer law, DSA), with the AI Act classification left to [[stays-ml-platform]].

Productscape domains covered: none as a dedicated brick; cross-cutting over TAM `deal` (presentation), `home`, customer service and partner tools, and HSM `insp`, `data` and host tools, as the AI layer over them. The agent channel is an [ADDED] extension of demand-side distribution ([[demand-channels]]).

## Audience

Chief architects, heads of distribution, ML and AI platform leads, product leaders for search, support and partner tools at OTAs and hosted-stays marketplaces. They know what a language model, retrieval and tool calling are. They need the stays-specific shape: which facts must never come from a model, how to let third-party agents book safely, and how to govern many AI uses across two brands.

## Success criteria

- [ ] Reader can define assistant, agent, tool and agentic booking, and sort AI uses by who they act for and what they can change.
- [ ] Reader can cite the dated public record (2023–2026) and state its three readings: model in front of the stack, ungrounded answers as the documented failure, the front door moving to assistants.
- [ ] Reader can draw the AI layer (Figure 2) and explain what agent-facing tools must return: place candidates with an ambiguity flag, binding quotes with a platform-written summary, evaluated (not generated) policies.
- [ ] Reader can apply the five side-effect classes and the rule that an AI may never do what a first-line human in the same role could not.
- [ ] Reader can compare handoff and mandate authority, and explain why autonomous agent booking is unsafe for hosted stays for now.
- [ ] The Corvane case runs from the Porto booking (14 September 2027, €304; pilot sweep 1,610 bookings, 9 wrong-place, €2,870) to the 19 October 2027 forum decisions and Frontdoor v2 with a before/after table.
- [ ] Reader can name the liability principle (*Moffatt v. Air Canada*, 2024) and the EU rules that apply, with dates.
- [ ] Trade-off table, Hotels and Homes table with judgement, failure modes, Chief Architect's view and questions are present.

## Non-goals

- Support assistant design, contact drivers and recovery decisioning: [[customer-service]].
- ML platform, model registry tiers and the AI Act high-risk classification: [[stays-ml-platform]].
- Generated property content rules: [[content-and-media]].
- Metasearch, affiliate APIs and landing pages: [[demand-channels]].
- Delegation grants and the token-exchange model: [[identity-accounts-and-access]].
- Trust and fraud models themselves: [[stays-trust-and-safety]], [[travel-fraud]].
- Developer productivity and internal coding agents (mentioned only as a use class).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- How strong customer authentication applies to agent-initiated card payments in the EU is not settled; the chapter tells readers to design for step-up. Revisit when PSD3/PSR texts and scheme rules for agentic payments are final.
- Expedia's Romie discontinuation rests on one low-confidence secondary report; replace with a primary source if one appears.
- Airbnb's participation in third-party assistant platforms was not verified and is not discussed.

## Decision log

- **2026-10-21** — Framed the chapter around consequence classes and booking authority rather than a catalog of AI features, so it complements [[customer-service]] and [[stays-ml-platform]] instead of repeating them.
- **2026-10-21** — Set the Corvane story in Roomstead's agent channel (third-party assistants via an MCP server) because agentic booking is the use the contract names and no other chapter owns it; the "wrong Porto" uses the real village of Porto in Corse-du-Sud as the ambiguous place.
- **2026-10-21** — Kept AI Act classification brief and linked to [[stays-ml-platform]], which already maps Annex III and Article 5; this chapter covers Article 50, liability and agent contracts.
- **2026-10-21** — Included a short Hotels and Homes section although Part IX does not require one, because booking authority differs sharply between the two marketplaces.

## Sources

Internal: [[customer-service]], [[stays-ml-platform]], [[availability-engine]], [[changes-and-cancellations]], [[identity-accounts-and-access]], [[destinations-and-maps]], [[content-and-media]], [[extranets-and-host-tools]], [[stays-trust-and-safety]], [[travel-fraud]], [[stays-marketplace-economics]], [[demand-channels]], [[evolving-the-platform]].

External: Booking.com AgentHub and onboarding-agent posts (2026); Booking Holdings press releases (2023, 2024) and 10-K FY2025; Expedia Group Technology posts on agentic operating model and AI principles (2026); Airbnb shareholder letters (2025–2026), 10-K FY2025 and evaluation post (2026); Trip.com TripGenie (2023); Anthropic MCP announcement (2024); Google Cloud AP2 (2025); TechCrunch on apps inside ChatGPT (2025); Regulation (EU) 2024/1689 and the AI Act Service Desk timeline; GDPR; DSA; RFC 8693; *Moffatt v. Air Canada*, 2024 BCCRT 149.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: Format cleanup; figures checked against the ledger and the Airbnb Q2 2026 letter. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 5,647 → 5,361 prose words; opening now ties the chapter to Part IX and the previous hand-off; Failure Modes compressed to one-line pointers; repeated restatements in the lead, Corvane decisions 2, 4 and 5, Hotels and Homes and the Chief Architect's view cut; spec success criterion fixed to cite Figure 2 for the AI layer. *(AI-mediated session)*
