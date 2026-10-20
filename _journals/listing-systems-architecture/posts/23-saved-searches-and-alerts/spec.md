---
status: accepted
revised: 2026-10-20
---

# Spec: Tell Me When It Appears: Saved Searches and Alerts

## Intent

Show architects how to notify millions of users within minutes when a matching listing appears, and why alerts are a liquidity lever and a trust surface at once. The reader should leave with four ideas. A saved search is a stored, normalized, versioned query with an owner, a policy and a lifecycle. Instant alerts at scale need reverse search (percolation or an equivalent) on the listing event stream, while batch re-query is a digest strategy. Alerts should fire on entry into the match set, retract on exit and re-check availability at send time. And fan-out, channels, consent, risk gating and taxonomy migration are part of the design, not afterthoughts.

## Audience

Chief architects, search and platform leads, notification and CRM engineering leads, and product directors of classifieds, property and automotive marketplaces. They know search engines and messaging infrastructure; they need the marketplace-specific architecture, its scale arithmetic and the governance decisions.

## Success criteria

- [x] Reader can define saved search, match set, watcher, percolation and alert fan-out, and separate the four parts of a saved search (query, owner, policy, lifecycle).
- [x] Reader can compare percolate-per-event, batch re-query, structured matchers, Lucene monitor and Vespa predicates, with the scale arithmetic that rules batch re-query out for instant alerts at 31 million saved searches.
- [x] Reader can draw the target architecture (saved-search store as record, percolator projections, matcher, retraction handler, risk gate, orchestrator, channel workers, feedback) — three diagrams.
- [x] Reader can explain the entry/exit rule, the match ledger and the send-time availability check using the Rotterdam bike's 214 stale digests.
- [x] Reader knows the documented constraints of channels: FCM quotas, Android 13 notification permission, Gmail bulk-sender rules, RFC 8058 one-click unsubscribe, and the ePrivacy Article 13 question.
- [x] Price-drop alerts use the Essen Golf (1,180 watchers); the risk gate uses the Barcelona fake-rental ring; taxonomy migration uses the 1 November 2027 bikes split.
- [x] Trade-off and vertical tables, failure modes, Chief Architect's view and 6–10 questions are present; every company claim is dated.

## Non-goals

- Search engine choice, index design and reindexing — [[search-architecture]].
- Listing event contract, outbox and ordering — [[event-driven-listings]].
- Publication SLA and unpublish propagation in general — [[publication-pipeline]].
- Map, polygon and commute query semantics — [[map-search]].
- Messaging notifications and lead routing — [[messaging-and-leads]].
- Fraud detection models — [[fraud-prevention]]; legal details per market — [[marketplace-regulation]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- No classifieds operator (Marktplaats, Kleinanzeigen, leboncoin, OLX) has published its alert matching or fan-out design in the sources found; the architecture is labeled as the author's reference design.
- The REA Group percolation talk could not be read; it is not cited.
- Whether user-requested alert e-mails count as direct marketing under national ePrivacy implementations is a legal judgement per market; the chapter states Veldmark's policy and does not generalize it.

## Decision log

- **2026-10-19** — Organized the chapter around the match-set entry/exit rule and the send-time check, because the canonical Ghost Inventory example (the bike's stale digests) is the clearest teaching case and both rules generalize.
- **2026-10-19** — Recommended a hybrid (percolation for instant alerts, ledger-based digests, batch re-query as reconciliation) over pure batch, with explicit arithmetic, rather than presenting the options as equal.
- **2026-10-19** — Included the risk gate and fan-out ordering as design topics because alerts amplify fraud and decide who wins scarce listings; both are governance questions for the Chief Architect.
- **2026-10-19** — Kept the legal section to principles with Veldmark's policy, pointing to the regulation chapter, because the ePrivacy classification differs by member state.

## Sources

- **Internal**
  - [[event-driven-listings]], [[listing-aggregate]], [[publication-pipeline]] — event names, the bike's digest timeline, derived alertability.
  - [[map-search]], [[location-and-geo]], [[categories-and-taxonomies]], [[entity-resolution]], [[trust-and-safety-architecture]], [[ranking]].
  - `_research/brief-search-discovery.md` Part 11; `_research/productscape-digest.md`; `_research/scenario-ledger.md`.
- **External**
  - Elastic Rightmove case study (2025); Homegate on Elastic's blog (2024); leboncoin tech blog post on PowerMTA (2026); The Title Report on Zillow (2023).
  - Elastic and OpenSearch percolator documentation; Lucene monitor; Vespa predicate fields; Firebase quotas; Android notification permission; Gmail sender guidelines; RFC 8058; Directive 2002/58/EC.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: hand-off to [[part-5]], Tradeyard transition aligned with the Yardstick exit plan, baseline labels fixed, leboncoin source linked to the post, acronyms expanded, ePrivacy Art. 13 verified. *(AI-mediated session)*
- **2026-10-19** — Added 3 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 3 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
- **2026-10-20** — Architecture heading now names the design (a saved-search store with rebuildable percolators). *(AI-mediated session)*
