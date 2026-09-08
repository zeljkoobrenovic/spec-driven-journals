---
status: accepted
revised: 2026-08-22
---

# Spec: Introduction

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

Open the Grounded Security journal: explain that it is my defensive-security
operating model written down as records — one record per source chapter
checklist — covering the program before the tools (creating it, asset
management, policies, standards and procedures, user education, compliance),
what happens when it goes wrong (incident response, disaster recovery,
phishing), hardening the estate (physical, Windows, Unix, endpoints,
databases, cloud), identity and the network (authentication, network
security, segmentation, IDS/IPS), and the continuous loop (vulnerability
management, secure development, OSINT and purple teaming, logging and
monitoring, the extra mile). Give the reader the map of the five sections,
say where the material comes from (Lee Brotherston, Amanda Berlin, and
William F. Reyor III's *Defensive Security Handbook*, 2nd edition), and
explain how to read the journal: article for the argument, Checklist tab for
the runnable part.

## Audience

Security and infrastructure engineers in my organization (so they know the
bar defensive work is held to); application-team leads whose systems live
inside the defended estate (so they know what they are held to and what to do
when something goes wrong); peer executives comparing operating models;
anyone building their own model from the same source.

## Success criteria

- [x] **The journal's charter is stated** — my defensive-security operating
      model as records, not a book report; first person; each record names
      its revisiting conditions.
- [x] **The single-source structure is explicit** — the *Defensive Security
      Handbook*'s 24 chapter checklists as the ground truth, the records as
      my commitments read through a practitioner-executive lens, credit
      explicit and per record.
- [x] **The map lists every record** with `[[slug]]` cross-links by section,
      and names the seams between sections (asset management under the
      hardening baselines, logging under incident response, education and
      phishing response as the same threat before and after the click).
- [x] **The reading guide works for each audience** — security and
      infrastructure engineers, application-team leads, executives, the
      reader with an active incident, model builders.
- [x] **Credit is explicit** — the book and all three authors named in the
      references.

## Non-goals

- Not a summary of the book — each record carries its own material; this
  post is only the map.
- Not a threat assessment, a risk register, or a statement about any
  specific system or incident — the records are the model, not the audit.
- Not the sibling journals' ground: platforms, engineering management,
  people-management tools, and the executive operating model live in their
  own journals.

## Modalities

- [ ] `checklist.md` — operational checklist *(no checklist by design; the intro is the map, not a record)*
- [x] `summary.md` — management summary
- [x] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic *(added later)*

## Open questions

- None.

## Decision log

- **2026-08-22** — Journal created with 24 records from the chapter
  checklists of Lee Brotherston, Amanda Berlin, and William F. Reyor III,
  *Defensive Security Handbook: Best Practices for Securing Infrastructure*,
  2nd edition (O'Reilly, 2024) — read through a practitioner-executive lens,
  as with the sibling journals.
- **2026-08-22** — Five thematic sections rather than the book's chapter
  order: program, response and recovery, hardening, identity and network,
  assess and improve — the executive's questions, with the seams between
  them cross-linked record to record.

## Sources

- **Internal**
  - `sources/checklists/defensive-security-handbook/` — twenty-four chapter
    checklists from the *Defensive Security Handbook*, 2nd edition.
- **External**
  - Lee Brotherston, Amanda Berlin, and William F. Reyor III, *Defensive
    Security Handbook: Best Practices for Securing Infrastructure*, 2nd
    edition (O'Reilly, 2024).

## Changelog

- **2026-08-22** — Initial spec and article written; summary and dialog
  modalities added (TL;DR and Conversation tabs, Ana/Ben dialog cast). Spec
  and post agree. Status `accepted`. *(Željko, AI-mediated session)*
- **2026-08-22** — Post-review fixes applied (see REVIEW.md). *(Željko,
  AI-mediated session)*
