---
status: accepted
revised: 2026-08-22
---

# Spec: Policies: What Must Be Achieved, in Writing

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

Fix the shape of security policy in my organization: policy states what must
be achieved, in mandatory language, as a governed and living document —
implementation detail belongs to standards and procedures. The post turns the
"Policies" chapter of the *Defensive Security Handbook* into an operating
record: every policy has a purpose tied to a security objective and promotes
consistent behavior; the language is clear, concise, and binding — must,
will, shall, do; never should, try, mostly — with permitted exceptions
documented; every policy carries the required document contents (version,
effective date, revision history, owner, approver, roles, scope, policy
statements, references); coverage is deliberate across the chapter's full
policy list from acceptable use to industry-specific requirements; policies
are managed as a set — separate manageable documents, framework-aligned,
centrally stored under revision control with formal review and approval,
communicated to affected personnel, with backup and physical copies for
outages and disaster recovery; and policies are living documents, reviewed
at least annually and after significant change, with obsolete versions
archived so nobody follows outdated requirements. The load-bearing test: any
employee can find the current approved version of the policy that applies to
them and understand what it requires — and nobody can find an obsolete one.

## Audience

Security and engineering leaders in my organization who write or approve
policies (so they know the bar); policy owners maintaining the set; auditors
and peer executives who want to see what separates a policy from an opinion.
First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states the what-not-how split,
      the mandatory-language rule, the governed-document contents, the
      living-document lifecycle, and the findability test.
- [x] **Policy foundation survives** — purpose tied to a security objective,
      consistent behavior, accessibility, clear expectations and boundaries,
      regulatory/compliance/audit support, alignment with the overall
      posture, management endorsement.
- [x] **Language discipline survives** — clear, simple, concise statements;
      focus on what must be achieved with implementation left to procedures
      and standards; must/will/shall/do for mandatory requirements;
      should/try/mostly avoided; exceptions documented; no legalese; short
      paragraphs and bullets.
- [x] **Required document contents survive** — version number, effective
      date, revision history, owner, approver, roles and responsibilities,
      executive sign-off where required, purpose, scope, actual policy
      statements, references to related documents and to regulatory
      requirements, consistent naming conventions.
- [x] **Coverage list survives** — the chapter's full policy-coverage list,
      from acceptable use through industry-specific and regulatory policies,
      reproduced in the checklist.
- [x] **Policy management survives** — separate manageable documents,
      framework alignment, central accessible storage, revision control,
      formal review and approval process, communication to affected
      personnel, backup copies for outages, physical copies of critical
      policies.
- [x] **Living-document lifecycle survives** — at least annual review,
      review after significant business/technology/regulatory/security
      change, updates recorded, re-approval obtained, alignment with
      current business objectives verified, obsolete versions removed or
      archived.
- [x] **Credit is explicit** — References name the *Defensive Security
      Handbook* and the "Policies" chapter checklist.

## Non-goals

- Not [[standards-and-procedures]] — the how lives there; this record is the
  reason policy stays at the what.
- Not [[security-program]] — the governance frame that calls for documented
  policies lives there; this record is the document discipline it delegates.
- Not [[compliance]] — policies must support regulatory and audit
  requirements; the compliance frame itself lives there.
- Not [[user-education]] — policies are communicated to affected personnel
  here; training people to live them is there.
- Not the content of each named policy — this record governs the shape and
  lifecycle of the policy set, not the substance of, say, the incident
  response policy (that substance lives in [[incident-response]] and its
  neighbors).

## Modalities

The working tool ships as the checklist modality (`checklist.md`, rendered
as the Checklist tab).

- [x] `checklist.md` — operational checklist
- [x] `summary.md` — management summary
- [x] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic (added later with the visual layer)

## Open questions

- None.

## Decision log

- **2026-08-22** — Grounded in the "Policies" chapter checklist of the
  *Defensive Security Handbook* (Lee Brotherston, Amanda Berlin, and
  William F. Reyor III), read through a practitioner-executive lens, as with
  every record in this journal.

## Sources

- **Internal**
  - `sources/checklists/defensive-security-handbook/Checklist_ DSH _ 03 _ Policies.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`).
- **External**
  - *Defensive Security Handbook*, 2nd edition — the "Policies" chapter
    checklist.

## Changelog

- **2026-08-22** — Initial spec, article, checklist, summary, and dialog
  written; spec and post agree. Status `accepted`. *(Željko, AI-mediated
  session)*
- **2026-08-22** — Post-review fixes applied (see REVIEW.md). *(Željko,
  AI-mediated session)*
