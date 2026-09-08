---
status: accepted
revised: 2026-08-22
---

# Spec: OSINT and Purple Teaming

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

Give the Assess and Improve section its self-assessment engine: fix the shape
of how my organization looks at itself the way an attacker would — and drills
its defenses against what it finds. The post turns the OSINT and Purple
Teaming chapter of the *Defensive Security Handbook* into an operating record:
nothing runs without written authorization, defined scope, rules of
engagement, and an emergency stop; OSINT is the defender's mirror, sweeping
physical assets, email and personnel exposure, the external attack surface,
document metadata, public web content, social media, and breach data;
investigation is disciplined — sources recorded, facts separated from
assumptions, no more personal data collected than necessary, reproducible by
another analyst; purple-team exercises are planned with expected detections
recorded before testing begins, red simulates realistic attacker behavior
within scope while blue proves alerts fire and logs support investigation;
and every gap found becomes an owned, deadlined, retested fix. The
load-bearing test: an exercise is not finished until red activity has been
compared with blue detections and every gap has an owner, a deadline, and a
retest.

## Audience

Security leads running self-assessment programs in my organization (so they
know the authorization and remediation bar they are held to); engineering
leaders whose teams' public footprint is part of the attack surface; peer
executives who want to see what "test your own defenses" concretely means as
defense, not theater. First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states the see-yourself-as-the-
      attacker-sees-you shape, the authorization frame, and the finish-line
      test: every gap owned, deadlined, and retested.
- [x] **Authorization and scope survive** — written approval before any
      OSINT, penetration testing, or purple-team exercise; systems, domains,
      networks, accounts, and locations in scope defined; rules of engagement
      and prohibited activities documented; privacy, legal, and ethical
      requirements established; stakeholders notified with escalation
      procedures; a controlled lab for techniques that could disrupt
      production.
- [x] **The full exposure sweep survives** — physical assets and disposal,
      shoulder surfing and workspace checks; email and personnel exposure
      including decoy/canary accounts and awareness training; the external
      attack surface (domains, IPs, DNS, OS/software versions, admin
      interfaces, cloud services, unnecessary services, change tracking);
      document and image metadata; public web content including exposed
      configuration and backup files and a removal process; personal and
      social-media exposure including remote-work guidance; breach exposure
      with unique passwords, MFA, prompt resets, and credential monitoring.
- [x] **Investigation discipline survives** — an OSINT framework organizing
      categories, source and reliability recorded per finding, confirmed
      facts separated from assumptions, minimal collection of personal
      information, findings reproducible by another analyst, tools supporting
      but never replacing judgment; the Maltego and Shodan reviews kept as
      scoped, authorized worked examples.
- [x] **The purple-team loop survives** — planning with the control under
      test, red/blue responsibilities, objectives and measurable success
      criteria, communication and emergency-stop procedures, and expected
      detections recorded before testing; red realistic and minimally
      disruptive with evidence preserved and hard stop on scope or safety
      limits; blue verifying alerts, log sufficiency, time to identify,
      escalation, containment, and telemetry gaps; the responder/coerced-
      authentication lab exercise with its authorization and hardening
      follow-through; the post-exercise review with ranked findings,
      remediation owners and deadlines, detection and training updates,
      retesting, and lessons recorded.
- [x] **Continuous improvement survives** — footprint monitored regularly,
      exposure reassessed after major change, exercises repeated
      periodically, regressions tracked, new attacker techniques
      incorporated, every weakness treated as an opportunity to strengthen
      defenses.
- [x] **Credit is explicit** — References name the *Defensive Security
      Handbook* and the OSINT and Purple Teaming chapter checklist.

## Non-goals

- Not [[vulnerability-management]] — scanning, prioritizing, and patching
  known weaknesses is the standing pipeline; this record is the adversarial
  lens that finds what the pipeline cannot see.
- Not [[logging-and-monitoring]] — the detection estate the blue team
  exercises here is designed and operated there.
- Not [[incident-response]] — purple teaming rehearses the escalation and
  containment machinery; the machinery itself is that record.
- Not [[user-education]] — the awareness training that OSINT findings feed is
  the standing program defined there.
- Not an offensive-security charter — everything in this record is the
  defender's self-assessment, run under written authorization, on systems my
  organization owns or is explicitly authorized to test.

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

- **2026-08-22** — Grounded in the OSINT and Purple Teaming chapter checklist
  of the *Defensive Security Handbook*, read through a practitioner-executive
  lens, as with every record in this journal.

## Sources

- **Internal**
  - `sources/checklists/defensive-security-handbook/Checklist_ DSH _ 20 _ OSINT and Purple Teaming.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`).
- **External**
  - *Defensive Security Handbook*, 2nd edition (Lee Brotherston, Amanda
    Berlin, and William F. Reyor III) — the OSINT and Purple Teaming chapter.

## Changelog

- **2026-08-22** — Initial spec, article, checklist, summary, and dialog
  written; spec and post agree. Status `accepted`. *(Željko, AI-mediated
  session)*
- **2026-08-22** — Post-review fixes applied (see REVIEW.md). *(Željko,
  AI-mediated session)*
