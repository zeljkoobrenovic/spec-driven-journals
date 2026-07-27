---
status: accepted
revised: 2026-07-26
---

# Spec: The Four Fundamental Team Topologies

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State how I constrain organizational vocabulary to exactly four team types:
stream-aligned teams that own a flow of change end to end (the overwhelming
majority), enabling teams that grow capability in other teams and then step
away, complicated-subsystem teams only where deep specialism genuinely
demands one, and platform teams that run the platform as an internal product
whose job is to make stream-aligned teams faster. The post turns the *Team
Topologies* "Four Fundamental Team Topologies" checklist into an operating
principle: most teams stream-aligned (roughly 6:1 to 9:1 against everything
else), no vague "support"/"ops"/"shared services" teams without a clear
topology, platform as a product starting from a thinnest viable platform,
and a deliberate conversion path for legacy team types (infrastructure,
component, tooling, support, architecture).

## Audience

My leadership bench and peer executives (so team charters and reorg
proposals are judged against a fixed vocabulary, not invented ad hoc);
engineering leaders comparing operating models. First-person declarative.

## Success criteria

- [ ] **Principle is quotable** — highlight states the four types and the
      stream-aligned majority in one paragraph.
- [ ] **All four types are explicit** — stream-aligned, enabling,
      complicated-subsystem, platform each appear with their defining
      behavior (own the flow / grow-then-leave / justified specialism /
      platform as a product).
- [ ] **The numbers survive** — the roughly 6:1 to 9:1 stream-aligned
      ratio; the thinnest viable platform framing.
- [ ] **Conversion is included** — legacy team types (infrastructure,
      component, tooling, support, architecture) get an explicit fate under
      the four-type vocabulary.
- [ ] **The checklist survives intact** — all PDF sections reproduced in
      the Checklist tab (`checklist.md`), items and numbers preserved.
- [ ] **Credit is explicit** — References name Skelton & Pais, *Team
      Topologies* (IT Revolution Press, 2019) and the authors' site.

## Non-goals

- Not a reorg playbook or a target org chart for any specific company.
- Not [[team-interaction-modes]] — that sibling record covers *how* the
  four types interact (collaboration, X-as-a-Service, facilitating); this
  one covers *what* the types are.
- Not [[team-first-boundaries]] — that sibling covers cognitive load and
  boundary sizing; this one covers the type vocabulary.
- Not [[organizational-design]] — that appendix record covers sizing and
  investment mechanics; this one covers the taxonomy of team purposes.
- No claim that the 6:1–9:1 ratio is a law — it is a default that shifts
  the burden of proof.

## Modalities

The working checklist ships as the checklist modality (`checklist.md`,
rendered as the Checklist tab). Summary/dialog may be added later per
journal policy.

- [x] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [x] `comics.md` — explainer comic

## Open questions

- None.

## Decision log

- **2026-07-26** — This is an **appendix record**: grounded in Matthew
  Skelton & Manuel Pais, *Team Topologies: Organizing Business and
  Technology Teams for Fast Flow* (IT Revolution Press, 2019) rather than
  Will Larson's *The Engineering Executive's Primer*. The record reads the
  book's team-design material through an executive lens and complements the
  Primer-grounded records.
- **2026-07-26** — Framed the record around vocabulary as a constraint:
  the load-bearing idea is that limiting the organization to four team
  types forces every team's purpose to be explicit, and the conversion
  section is where the principle bites on an existing organization.

## Sources

- **Internal**
  - `sources/checklists/appendix/team-topologies/Checklist_ Team
    Topologies _ Four Fundamental Team Topologies.pdf` — the operating
    checklist; reproduced in the Checklist tab (`checklist.md`).
- **External**
  - Matthew Skelton & Manuel Pais, *Team Topologies: Organizing Business
    and Technology Teams for Fast Flow* (IT Revolution Press, 2019) — the
    chapters on the four fundamental topologies this record distills.

## Changelog

- **2026-07-26** — Comics modality staged (`comics.md`, Comic tab, shared
  VERA/LEO cast) with pending panel blocks; inline illustration
  placeholders staged in the article. *(Željko, AI-mediated session)*
- **2026-07-26** — Article and checklist written from this spec; spec and
  post agree. Status `draft` → `accepted`. *(Željko, AI-mediated session)*
- **2026-07-26** — Initial spec for the appendix record. Status `draft`.
  *(Željko, AI-mediated session)*
