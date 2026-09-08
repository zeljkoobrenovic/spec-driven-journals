---
status: accepted
revised: 2026-08-22
---

# Spec: Secure Software Development

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

Fix how my organization builds software that is secure by construction rather
than secured at the end. The post turns the Secure Software Development
chapter of the *Defensive Security Handbook* into an operating record:
language selection treated as a security decision with the risks of each
language family understood; documented secure coding standards applied
consistently, with user-supplied input defined broadly and never processed
unvalidated — type, length, range, and relational validity checked, approved
libraries used for security-sensitive work, and standards set for
cryptography, database access, memory management, network communication,
error handling, authentication, audit logging, and access management;
security testing running throughout development, not only at release —
automated static analysis in the pipeline with secret detection, automated
dynamic testing against the running application, and systematic peer review,
each covering the others' blind spots; security incorporated into every
stage of a six-stage SDLC from training through requirements, architecture
and threat modeling, coding, testing, and release with operational handoff;
and a final review gate before production. The load-bearing test is the
chapter's Final Review: standards followed, input validated, testing
complete, security in every stage, known vulnerabilities remediated or
formally addressed.

## Audience

Engineering teams and their leads in my organization (so they know the bar
every codebase and release is held to); security engineers embedding into the
SDLC; peer executives who want to see what "we build security in" concretely
commits an engineering organization to. First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states built-in over bolted-on,
      validation-before-processing, testing-throughout, and
      security-in-every-stage, ending with the final review as the release
      gate.
- [x] **Language selection survives** — security as a criterion in language
      choice; built-in protections evaluated; memory-safe languages
      preferred where practical; per-language risks understood and the
      language-specific considerations kept (assembly only when necessary;
      C/C++ pointer and memory discipline against buffer overflows,
      use-after-free, double-free; Go's protections and the `unsafe`
      package avoided; Rust ownership; Python/Ruby/Perl input validation
      despite automatic memory management; PHP insecure-feature avoidance).
- [x] **Secure coding guidelines survive** — documented standards applied
      consistently; user-supplied input defined broadly (networks, files,
      command line, GUI, peripherals); never processed without validation;
      type, length, range, and relational checks; invalid data rejected;
      approved libraries for security-sensitive tasks; standards for
      cryptography, database access, memory management, network
      communication, error handling, authentication, audit logging, and
      access management; secure session management for web applications;
      client–server communication security requirements.
- [x] **Testing trio survives** — security testing before release and
      throughout development; static analysis scanning source without
      executing it, integrated into CI/CD, run on changed code, findings
      reviewed for false positives, memory and unsafe-function checks,
      secret detection for committed passwords, tokens, API keys, and
      private keys, and the honest limit that static misses design-level
      flaws; dynamic testing against the running application with varied
      inputs, injection and output-handling checks, and its coverage limits
      named; peer review that is systematic, verified, staffed with
      language- and vulnerability-appropriate reviewers, and combined with
      automated testing rather than substituting for it.
- [x] **Six-stage SDLC survives** — training (secure development, threat
      modeling, security testing, privacy); requirements (security
      requirements identified with functional ones, mandatory not optional,
      documented, visible); architecture and design (expectations before
      coding, encryption and access-control placement, sensitive-data
      handling, threat modeling, attack methods, design review, attack
      surface reduction); code and build (approved architecture, chosen
      language, standards, practices, approved libraries and tools); test
      and review (functionality plus security testing, multiple methods,
      defects documented and severity-assessed, vulnerable code returned,
      fixes retested); release (formal process, final security review,
      defects addressed, operational documentation, incident-response and
      business-continuity procedures, handoff to support teams).
- [x] **Final review survives as the gate** — standards documented and
      followed, input validated, appropriate static/dynamic/manual testing
      complete, security in every SDLC stage, known vulnerabilities
      remediated or formally addressed, ready for final security review
      before production.
- [x] **Credit is explicit** — References name the *Defensive Security
      Handbook* and the Secure Software Development chapter checklist.

## Non-goals

- Not [[vulnerability-management]] — managing vulnerabilities across the
  running estate lives there; this record reduces what that program finds by
  building fewer defects in.
- Not [[standards-and-procedures]] — the general machinery for writing and
  maintaining organizational standards lives there; the secure coding
  standard is one instance of it.
- Not [[user-education]] — the organization-wide awareness program lives
  there; the developer training in this record is stage one of the SDLC,
  role-specific and technical.
- Not [[authentication]] — the organization's identity and access baseline
  lives there; this record requires applications to carry authentication and
  access-management standards, not to redesign the identity layer.
- Not [[databases]] — database hardening lives there; this record governs
  the code that talks to the database, including its database-access
  standard.
- Not a tool mandate — static and dynamic analyzers and secret scanners are
  named as capabilities; any toolchain with the same properties satisfies
  the record.

## Modalities

The working tool ships as the checklist modality (`checklist.md`, rendered
as the Checklist tab).

- [x] `checklist.md` — operational checklist
- [x] `summary.md` — management summary
- [x] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic (added later)

## Open questions

- None.

## Decision log

- **2026-08-22** — Grounded in the Secure Software Development chapter
  checklist of the *Defensive Security Handbook* (Brotherston, Berlin,
  Reyor), read through a practitioner-executive lens, as with every record
  in this journal.

## Sources

- **Internal**
  - `sources/checklists/defensive-security-handbook/Checklist_ DSH _ 19 _ Secure Software Development.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`), including the final review.
- **External**
  - *Defensive Security Handbook*, 2nd edition — the Secure Software
    Development chapter checklist.

## Changelog

- **2026-08-22** — Initial spec, article, checklist, summary, and dialog
  written; spec and post agree. Status `accepted`. *(Željko, AI-mediated
  session)*
- **2026-08-22** — Post-review fixes applied (see REVIEW.md). *(Željko,
  AI-mediated session)*
