---
status: accepted
revised: 2026-08-22
---

# Spec: Standards and Procedures

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

Fix the shape of the documentation layer that sits below policy in my
organization's security program. The post turns the Standards and Procedures
chapter checklist of the *Defensive Security Handbook* into an operating
record: a four-level documentation hierarchy where policy explains why,
standards define what, procedures identify who/when/where, and work
instructions explain how; standards written in mandatory language (must,
shall, will) and specific enough to implement consistently; requirements
documented once and referenced everywhere; procedures written for their
intended audience with ordered steps, verified assumptions, and room for
judgment; every document carrying version information, an owner, an approver,
purpose, scope, requirements, and related-document links; documents stored in
one approved repository where the authoritative version is unambiguous; and
nothing published without a quality review. The load-bearing test: a new
employee can find the authoritative document and apply it correctly without
asking anyone.

## Audience

Security and engineering leaders in my organization who own policies,
standards, and procedures (so they know the documentation bar I hold them
to); document owners writing or reviewing standards; auditors and peer
executives who want to see what "documentation replaces tribal knowledge"
concretely means. First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states the four-level hierarchy
      (why / what / who-when-where / how), the mandatory-language rule, the
      write-once discipline, and the test: a new employee can find and apply
      the authoritative document without asking anyone.
- [x] **Documentation hierarchy survives** — policy explains why, standards
      define what, procedures identify who performs activities and when and
      where, work instructions/guidelines/SOPs explain how; each document at
      the correct level; related documents clearly linked.
- [x] **Standards discipline survives** — technology-specific requirements
      without procedural detail; mandatory language (must/shall/will) and no
      ambiguous wording where a requirement is mandatory; specific enough for
      consistent implementation; common requirements documented once and
      referenced; standards maintained separately where that improves
      usability; central changes without touching multiple policies; regular
      technical-accuracy review.
- [x] **Procedure quality survives** — procedures explain how standards are
      implemented on specific technologies, with enough detail for the
      intended audience; platform-specific variants where needed; ordered
      steps, active voice, explicit and verified assumptions, concise
      wording, commands and examples where needed, judgment allowed where
      prescription is impractical, and review by people who understand both
      the technology and the audience.
- [x] **Knowledge-distribution goal survives** — consistent implementation
      across teams and systems, reduced reliance on institutional knowledge,
      employees finding information without specific individuals, documents
      understandable outside the authoring team, repetition minimized.
- [x] **Regulatory and management frame survives** — applicable laws,
      regulations, contracts, and frameworks identified; documents supporting
      compliance obligations and producible in an audit; management
      endorsement and recorded approvals.
- [x] **Required document contents survive** — version information, owner
      and approver, purpose/overview, scope with exclusions, clearly
      identified requirements, related-document references; consistent
      naming; an approved repository where the authoritative version is
      unambiguous and superseded versions are archived.
- [x] **Final quality review survives as the completion check** —
      readability, no conflicts with higher-level policy, correct
      implementation down the hierarchy, validated technical content, SME
      review, recorded approvals, a review date, and publication to the
      relevant users.
- [x] **Credit is explicit** — References name the *Defensive Security
      Handbook* and the Standards and Procedures chapter checklist.

## Non-goals

- Not [[policies]] — the why-layer above the standards sits there; this
  record starts where policy ends and mandates how standards and procedures
  implement it.
- Not [[security-program]] — the program that commissions this documentation
  layer and gives it executive backing lives there.
- Not [[compliance]] — which external regulations and frameworks apply is
  decided there; this record makes the documentation able to face them.
- Not [[user-education]] — teaching people to follow the documents is that
  record; this one makes the documents followable.
- Not a template pack — the record fixes what every document must contain,
  not the file format or tooling it is written in.

## Modalities

The working tool ships as the checklist modality (`checklist.md`, rendered
as the Checklist tab).

- [x] `checklist.md` — operational checklist
- [x] `summary.md` — management summary
- [x] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic (added later with the journal's visual
      layer)

## Open questions

- None.

## Decision log

- **2026-08-22** — Grounded in the Standards and Procedures chapter checklist
  of the *Defensive Security Handbook* (Brotherston, Berlin, Reyor), read
  through a practitioner-executive lens, as with every record in this
  journal.

## Sources

- **Internal**
  - `sources/checklists/defensive-security-handbook/Checklist_ DSH _ 04 _ Standards.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`), including the final quality review.
- **External**
  - *Defensive Security Handbook*, 2nd edition (Lee Brotherston, Amanda
    Berlin, William F. Reyor III; O'Reilly) — the Standards and Procedures
    chapter.

## Changelog

- **2026-08-22** — Initial spec, article, checklist, summary, and dialog
  written; spec and post agree. Status `accepted`. *(Željko, AI-mediated
  session)*
- **2026-08-22** — Post-review fixes applied (see REVIEW.md). *(Željko,
  AI-mediated session)*
