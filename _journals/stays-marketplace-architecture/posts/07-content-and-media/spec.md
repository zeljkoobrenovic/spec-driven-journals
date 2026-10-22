---
status: accepted
revised: 2026-10-22
---

# Spec: Describing a Stay: Content, Media and Property Mapping

## Intent

Show how a stays marketplace turns supplier feeds and host-written listings into descriptions that guests can trust and compare, and how an OTA recognizes the same hotel and room arriving from several suppliers. The reader should leave treating content as a governed catalog (field-level provenance, precedence, verification state, versioned snapshots), treating policies and fees as structured data rendered into text, and treating property and room mapping as an entity-resolution service with stable identifiers, review queues and measured accuracy. The chapter owns **content mapping**, **content score** and **media pipeline (stays)**.

Productscape domains covered: TAM `cont` (Content & Policy Studio), TAM `medi` (Property Media Pipeline), HSM `lista` (Listing Authoring & Content), plus the [ADDED] content-mapping and translation gaps the digest identifies.

## Audience

Chief architects, principal engineers and supply, content and data leads at OTAs and hosted-stays marketplaces who own content ingestion, the property page's data, wholesale supply integration or listing quality, and who must decide what content machinery a multi-brand group should share.

## Success criteria

- [ ] Reader can name the five content sources (extranet, connectivity content APIs, wholesale/GDS feeds, host editor, vacation-rental software API) and the trust problem of each.
- [ ] Reader can explain field-level provenance, precedence and verification state, and why reservations should reference a content version.
- [ ] Reader can argue why cancellation terms, fees, registration numbers and accessibility claims are rendered from structured data rather than written or machine-translated.
- [ ] Reader can sketch the mapping pipeline (normalize, block, score, threshold, review, registry, room mapping) and explain why unmapped rooms are unsellable.
- [ ] The Corvane Brightwell example shows numbers that add up (41,000 = 32,200 matched + 8,410 new + 390 rejected) and the measured error rates behind them.
- [ ] Every real-company claim (Airbnb photo classification 2018, Translation Engine 2021, Booking.com Photo API, Expedia Rapid content, Trip.com hotel matching) carries a dated source; vendor accuracy claims are marked as such.
- [ ] The "Hotels and Homes" section ends in a specific judgement: share the machinery (media, translation, policy rendering, hash index, mapping engine), not the content model.
- [ ] Reader will not mistake vendor mapping IDs for a system of record.

## Non-goals

- The model of property, room type, unit and listing itself — [[property-and-listing-model]].
- Onboarding funnels, verification and readiness checks — [[partner-onboarding]].
- ARI and content message transport, certification and channel managers — [[connectivity-and-channel-managers]].
- Rate conditions and the rate-plan model — [[rates-and-availability-model]].
- Review collection and moderation — [[reviews-and-reputation]].
- Enforcement against fake listings — [[stays-trust-and-safety]].
- Generic media pipeline and entity-resolution machinery — LISTED's [[media-pipeline]] and [[entity-resolution]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- How Booking.com, Expedia and Trip.com map wholesale and affiliate supply internally is not public; revisit if any publishes a design.
- Current state of Airbnb's photo-classification and translation systems (the public posts are from 2018–2021).
- ~~Whether a later chapter (`converging-two-marketplaces`) formally adds the shared content services to One Stay's scope.~~ Answered: capability map v2 (December 2027) adopted all five; the article now says so.

## Decision log

- **2026-10-21** — Used a wholesale (bedbank) feed as the Corvane case instead of a channel-manager content migration, because mapping is the OTA-specific problem the contract adds and the numbers make the duplicate-vs-false-merge trade-off concrete.
- **2026-10-21** — Put policy rendering in this chapter as a content concern ("render, do not write") while leaving policy semantics to `changes-and-cancellations`, so Policy Spaghetti is addressed where the free text originates.
- **2026-10-21** — Kept generic media and entity-resolution mechanics short and linked to LISTED, spending the depth on stays-specific parts (room-level galleries, room mapping, provenance).
- **2026-10-21** — Recommended sharing content machinery but not the content model, consistent with the ledger's One Stay decision not to share supply models.

## Sources

- **Internal**
  - [[property-and-listing-model]], [[connectivity-and-channel-managers]], [[stays-ranking]], [[converging-two-marketplaces]] — neighboring ownership.
  - `_research/brief-supply-connectivity.md` (Parts 1, 2, 6), `brief-host-partner-guest-service.md` (translation, accessibility, host tools), `brief-search-discovery.md` (categories, ranking disclosure), `productscape-digest.md` (`cont`, `medi`, `lista`, gaps).
- **External**
  - Yao, Zhu and Siclait, *Categorizing Listing Photos at Airbnb* (2018) — weak labels from captions, validation of room counts.
  - Booking.com, *Understanding the Photo API* (live 2026) — room-level galleries, smart ordering, no overlay.
  - Expedia Group, Rapid content API and Vrbo integration guide (live 2026) — catalog file for mapping, refresh cadences.
  - Airbnb 2021 Winter Release — Translation Engine and accessibility review.
  - Gimmonix and Vervotech (2026) — mapping failure modes (vendor claims).
  - Regulation (EU) 2024/1028; Directive 2005/29/EC — registration display and misleading information.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: aligned the five shared content services with capability map v2 (media pipeline and translation already shared in v1; hash index in media pipeline; policy text from Clause; Concord engine shared from 2028), corrected the Booking.com Home-provider sunset to `OTA_HotelInvNotif` only, verified RMA and Photo API claims, flagged older Airbnb evidence, expanded OTA and STR. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 2 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-21** — Figure fixes: regenerated the render-policy figure without the till and payment card. *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 7,556 → 7,484 prose words; opening now places the chapter in Part II (supply as master data with many writers, after property-and-listing-model and partner-onboarding); "Content scoring at Roomstead and Nookaway" promoted from an In Practice subsection to its own section; generic openers and repeated sentences cut. *(AI-mediated session)*
- **2026-10-22** — Second sharpening pass: 7,556 → 6,755 prose words cumulative since HEAD (7,484 → 6,755 this pass); lead no longer restates the callouts or the ownership of neighbouring chapters; Failure Modes compressed to one-line pointers (their facts moved into Source adapters, Translation and The mapping pipeline); Chief Architect's view no longer re-argues the Hotels and Homes judgement and its regulation paragraph moved into the regulation paragraph of the body; repeated definitions and recaps cut. No headings renamed, no figures touched. *(AI-mediated session)*
