---
status: draft
revised: 2026-05-20
---

# Spec: Team Topologies as the Operating Vocabulary

> Filled in during the second pass over backfilled specs. Status `draft`.

## Intent

State that Organization uses **Team Topologies as the shared operating
vocabulary** for engineering organisation design. **Stream-aligned
teams are the default.** Platform, enabling, and complicated-subsystem
teams are explicit exceptions used to reduce cognitive load and
accelerate flow. **Interaction modes** — collaboration, X-as-a-service,
facilitating — must be **named rather than left implicit**.

## Audience

- **Engineering leadership** designing the org structure.
- **Engineering managers** placing teams in topology types.
- **Architecture group** evaluating cognitive-load proposals.
- **New joiners** learning the org vocabulary.

## Success criteria

- [ ] Reader can name the **four team types** (stream-aligned,
      platform, enabling, complicated-subsystem).
- [ ] Reader can name the **three interaction modes** (collaboration,
      X-as-a-service, facilitating).
- [ ] Reader knows stream-aligned is **the default**, the others are
      exceptions justified by cognitive-load reduction.
- [ ] Reader knows interaction modes must be **explicit**.

## Non-goals

- Mandating Team Topologies for every conversation.
- Replacing existing team names.

## Open questions

- How strict to be about "complicated-subsystem" classification.

## Decision log

- **2026-05-20** — Chose **Team Topologies vocabulary**. Considered
  Spotify-style chapters/tribes; rejected because Spotify's model
  is famously hard to copy without context.
- **2026-05-20** — Required **explicit interaction modes**.
  Considered leaving them implicit; rejected because implicit
  interactions degrade into collaboration-as-default and burn out
  platform teams.

## Sources

- **Internal**
  - [[stream-aligned-product-teams]] — the default team type.
  - [[platform-and-devops-operating-model]] — applies platform
    teams.
  - [[team-size-and-composition]] — companion sizing record.
- **External**
  - Matthew Skelton & Manuel Pais, *Team Topologies*.

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
- **2026-05-20** — Initial spec created.
