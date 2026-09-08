---
status: accepted
revised: 2026-08-22
---

# Spec: Security Education

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

Fix the shape of security awareness in my organization: an ongoing education
program, not an annual compliance module. The post turns the User Education
chapter checklist (titled Security Education) of the *Defensive Security
Handbook* into an operating record: one or two clear objectives tailored to our actual threat
landscape, with executive support and cultural fit; a measured baseline of
user knowledge and behavior before the program launches, so improvement
targets are real; clear rules and a reporting path so simple that reporting
suspicious activity is the easy option; training reinforced through
repetition, spaced learning, and realistic hands-on exercises such as
phishing simulations; positive reinforcement instead of fear or shame —
users are never punished for reporting a mistake, even after clicking;
awareness exercises doubling as tests of the incident-response machinery;
and a metrics loop (sent, opened, clicked, submitted, reported) reviewed
against the baseline over time. The load-bearing test: training is judged by
behavior change against the baseline, not by course-completion rates.

## Audience

Security and engineering leaders in my organization who own the awareness
program (so they know the bar it is held to); people and communications
leaders who co-run training; peer executives who want to see what "users as
a security control" concretely means. First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states the ongoing-not-annual
      shape, the baseline-first discipline, the no-blame reporting culture,
      and the test: behavior change against the baseline, not completion
      rates.
- [x] **Program design survives** — one or two clear, achievable
      objectives; training tailored to the organization's specific risks and
      threat landscape; executive support and cultural alignment; awareness
      as an ongoing process; repetition and spaced learning; realistic
      hands-on exercises; lessons tied to everyday work.
- [x] **Baseline discipline survives** — current knowledge and behavior
      measured before launch, realistic exercises identifying common
      weaknesses, current reactions to phishing and unusual requests
      assessed, and baseline results setting measurable improvement targets.
- [x] **Rules and reporting survive** — clear, concise program rules
      consistent with policy and culture, employee and stakeholder input,
      explicit guidance on what to do about suspicious activity, and a
      reporting path that is simple and accessible.
- [x] **Training and reinforcement survive** — repeated practice, link
      verification habits, recognition of suspicious emails and
      social-engineering tactics, quick reporting of mistakes encouraged,
      examples resembling real threats, and interactive activities
      supplementing computer-based training.
- [x] **Positive reinforcement survives** — no punishment for reporting a
      mistake, reporting encouraged even after a click, good behavior
      rewarded, gamification and recognition considered, and a supportive
      environment instead of fear or shame.
- [x] **Incident-response coupling survives** — what users do after
      identifying or falling for an attack is defined; existing IR
      procedures are tested during awareness exercises; gaps and
      inefficiencies are identified; procedures and policies are updated
      from lessons learned.
- [x] **Metrics loop survives** — the full tracking set (simulated emails
      sent, opened, clicked, credentials submitted, attempts reported,
      unreported suspicious emails, training access, reporting and
      click-rate trends, progress toward goals) and the success measures:
      comparison against the original baseline, rising reporting, falling
      successful phishing and risky behavior, periodic review, topics
      adjusted to emerging threats, objectives updated with maturity.
- [x] **Final review survives as the completion check** — security as part
      of everyone's responsibility, behavior change over course completion,
      an engaging and relevant program, continuous reinforcement, and
      encouragement over punishment.
- [x] **Credit is explicit** — References name the *Defensive Security
      Handbook* and the Security Education chapter checklist.

## Non-goals

- Not [[phishing-response]] — what the organization does operationally when
  a real phish lands lives there; this record trains the humans who report
  it.
- Not [[incident-response]] — the response machinery is defined there; this
  record tests it through awareness exercises and feeds lessons back.
- Not [[policies]] — the rules users are trained on are set there; this
  record makes them understood and followed.
- Not [[security-program]] — the program that commissions and funds the
  education effort lives there.
- Not a tooling choice — phishing-simulation platforms and training vendors
  are implementation details; the commitments hold under any of them.

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

- **2026-08-22** — Grounded in the Security Education chapter checklist of
  the *Defensive Security Handbook* (Brotherston, Berlin, Reyor), read
  through a practitioner-executive lens, as with every record in this
  journal.

## Sources

- **Internal**
  - `sources/checklists/defensive-security-handbook/Checklist_ DSH _ 05 _ Education.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`), including the final review.
- **External**
  - *Defensive Security Handbook*, 2nd edition (Lee Brotherston, Amanda
    Berlin, William F. Reyor III; O'Reilly) — the User Education chapter,
    whose checklist is titled Security Education.

## Changelog

- **2026-08-22** — Initial spec, article, checklist, summary, and dialog
  written; spec and post agree. Status `accepted`. *(Željko, AI-mediated
  session)*
- **2026-08-22** — Post-review fixes applied (see REVIEW.md). *(Željko,
  AI-mediated session)*
