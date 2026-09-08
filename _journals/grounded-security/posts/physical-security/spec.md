---
status: accepted
revised: 2026-08-22
---

# Spec: Physical Security

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

Open the Hardening the Estate section: fix the bar my organization holds its
physical layer to, as a security boundary of the same rank as the network.
The post turns the Physical Security chapter checklist of the *Defensive
Security Handbook* into an operating record: secure areas behind real,
layered controls (more than one for highly sensitive areas); revocation as
disciplined as granting — badges recovered, shared codes changed, access
reviewed on role change; surveillance positioned to answer *who* and
correlated with badge logs; media tracked with classification labels and a
chain of custody; visitors and contractors identified, escorted, and
time-boxed; employees trained that politeness does not override procedure
against tailgating, badge cloning, malicious media, and pretexting; and the
whole thing run as a coordinated, tested program. The load-bearing test: no
single failed control — a held door, a cloned badge, a confident pretext —
is enough to reach sensitive systems or data.

## Audience

Security and facilities leads in my organization (so they know the bar the
physical program is held to); engineering leaders who assume the attacker is
always remote; employees who hold the boundary at every door; peer
executives auditing an office or datacenter fit-out against the record.
First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states the layered-boundary
      shape and ends with the no-single-failed-control test.
- [x] **Access controls and workplace hygiene survive** — restricted
      secure areas; locks, PIN pads, badge readers, biometrics, guards;
      multiple controls for highly sensitive areas; locked screens, cable
      locks, clear desk, locked document storage, restricted and disabled
      network jacks, clean printers, shredding.
- [x] **Surveillance-for-correlation survives** — CCTV at entrances and
      high-risk rooms, positioned for faces and badge correlation, tamper
      protection, footage reviewed and correlated with badge-access logs.
- [x] **Access maintenance survives** — audited controls, worn-keypad
      inspection, same-day badge recovery, prompt permission removal,
      shared-code changes on departure, role-change reviews, no shared PINs
      for highly sensitive areas.
- [x] **Media chain of custody survives** — secured and locked media,
      classification labels, distribution procedures, secure couriers,
      location tracking, removal approval, movement records, backup media
      protection, periodic storage inspection.
- [x] **Datacenter and equipment security survives** — lockable racks,
      centrally controlled and logged rack keys, floor-to-ceiling walls,
      ceiling-tile evaluation, remote-office equipment, locked enclosures,
      fire-safety-aware design.
- [x] **Visitor, contractor, and badge discipline survives** — sign-in/out
      with records, escorts, purpose verification, employee approval;
      contractor identification, photo ID, policy-defined and area-limited
      access, vetting confirmation; distinguishable, expiring, returned,
      promptly disabled badges.
- [x] **Social-engineering defenses survive** — training that politeness
      does not override procedure; tailgating (individual authentication,
      challenge and report); badge cloning (assume clonable, second factor
      where risk warrants, periodic testing); malicious removable media
      (untrusted found/promotional media, restricted ports, endpoint
      controls); pretexting (verify identity, work orders, unexpected
      devices, and equipment sources).
- [x] **Program management survives** — security–facilities coordination,
      physical security in assessments and penetration tests, periodic
      policy review, new-threat identification, timely gap correction,
      defense-in-depth as the closing rule.
- [x] **Credit is explicit** — References name the *Defensive Security
      Handbook* and the Physical Security chapter checklist.

## Non-goals

- Not [[user-education]] — the awareness curriculum and its metrics live
  there; this record carries only the physical-specific training content.
- Not [[phishing-response]] — pretexting is phishing in person, but the
  digital phishing program is its own record.
- Not [[asset-management]] — media tracking here assumes the inventory
  discipline that record establishes.
- Not [[windows-infrastructure]] or [[unix-servers]] — what runs inside the
  racks is hardened in those records; this one stops at the rack door.
- Not a facility-design handbook — the record fixes capabilities and tests,
  not floor plans or vendor choices.

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

- **2026-08-22** — Grounded in the Physical Security chapter checklist of
  the *Defensive Security Handbook* (Brotherston, Berlin, Reyor III), read
  through a practitioner-executive lens, as with every record in this
  journal.

## Sources

- **Internal**
  - `sources/checklists/defensive-security-handbook/Checklist_ DSH _ 09 _ Physical Security.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`).
- **External**
  - *Defensive Security Handbook*, 2nd edition — the Physical Security
    chapter checklist.

## Changelog

- **2026-08-22** — Initial spec, article, checklist, summary, and dialog
  written; spec and post agree. Status `accepted`. *(Željko, AI-mediated
  session)*
- **2026-08-22** — Post-review fixes applied (see REVIEW.md). *(Željko,
  AI-mediated session)*
