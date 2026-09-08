---
status: accepted
revised: 2026-08-22
---

# Spec: Phishing Awareness and Response

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

Close the Response and Recovery section with the attack that starts most of
what incident response handles. The post turns the Phishing Awareness and
Response chapter of the *Defensive Security Handbook* into an operating
record with an unusual property: the chapter's checklist is written for
every employee, not for responders — it is the handout — and the record is
the executive commitment standing behind it. The commitments: a short
pre-click verification habit run by everyone (expectation, sender match,
urgency-as-warning-sign, credential-request suspicion, out-of-band
verification, URL checks, stop-and-ask on doubt); warning signs taught in
plain sensory language across every medium — feels funny, looks funny,
sounds funny — covering web, email, phone, and found media; a rehearsed,
blame-free after-click path (stop, report immediately, disclose exactly what
was entered, follow instructions); near-misses reported and kept, never
forwarded to coworkers; a spelled-out list of what must be reported; and a
short set of absolute rules, ending with help-desk, phishing-report, and
after-hours contact lines that are filled in, published, and current. The
load-bearing test: the employee who clicked reports it within minutes —
because they know they will be helped, not punished.

## Audience

Every employee of my organization (the checklist is their handout); the
security and IT teams who run the reporting channel and the response behind
it; peer executives who want to see what a blame-free human sensor network
concretely requires. First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states people-not-just-filters,
      the pre-click habit, out-of-band verification, the sensory warning
      signs across media, blame-free reporting for clicks and near-misses,
      the never-share-credentials absolute, the published contacts — and
      ends with the helped-not-punished test.
- [x] **The pre-click habit survives** — expectation, sender recognition,
      sender-address match, urgency and pressure as a warning sign,
      credential/financial-request suspicion, out-of-band verification of
      work-related requests, URL-and-`https://` check, and stop-and-contact-
      the-help-desk on any doubt.
- [x] **All three warning-sign families survive** — feels funny (login
      bounce-back, misbehaving website, unexpected package/delivery/payroll/
      greeting-card message, unsolicited sensitive document), looks funny
      (attachment error, macro/software/driver/media-player prompts,
      familiar site on a different URL, found removable media), sounds funny
      ("IT" asking for credentials, caller needing immediate access to an
      unreported issue, unfamiliar vendor probing systems, unusual requests
      claiming departmental authority).
- [x] **The after-click path survives** — stop interacting, enter nothing
      more, contact the help desk immediately, describe what was clicked and
      what happened, disclose whether credentials or sensitive data were
      entered, follow response instructions, and report quickly to protect
      others.
- [x] **The near-miss path survives** — report through the phishing-reporting
      process, do not forward to coworkers unless instructed, keep the
      message for review, assume others received the same attack, expect
      follow-up attempts.
- [x] **The reportable-information list and absolute rules survive** —
      credential/banking/system fishing, unexpected links and attachments,
      unauthorized access attempts, PHI and confidential-information
      requests, suspicious calls/messages/websites/media; and the key rules
      including never giving a username or password to another person.
- [x] **The contact lines survive as a commitment** — help desk, phishing
      report method, and emergency/after-hours contact kept as fill-in lines
      in the checklist and elevated in the article to an executive
      responsibility: filled in, published, current.
- [x] **Credit is explicit** — References name the *Defensive Security
      Handbook* and the Phishing Awareness and Response chapter checklist.

## Non-goals

- Not [[incident-response]] — a reported click becomes a suspected incident
  and hands off there; this record ends at the report.
- Not [[user-education]] — the broader training program that teaches and
  refreshes these habits lives there; this record is its highest-stakes
  curriculum, not its machinery.
- Not [[authentication]] — MFA and credential controls that bound the damage
  of a phished password live there.
- Not [[endpoints]] — hardening against the macro prompts, installers, and
  found media that the warning signs describe lives there.
- Not a technical email-security architecture — filters, link rewriting, and
  sandboxing are assumed and are not this record's subject; it covers what
  is engineered to get past them.

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

- **2026-08-22** — Grounded in the Phishing Awareness and Response chapter
  checklist of the *Defensive Security Handbook* (Brotherston, Berlin,
  Reyor III; 2nd edition), read through a practitioner-executive lens, as
  with every record in this journal. The chapter's employee-facing register
  is kept deliberately: the checklist stays a first-person handout, and the
  article carries the executive commitments behind it.

## Sources

- **Internal**
  - `sources/checklists/defensive-security-handbook/Checklist_ DSH _ 24 _ Phishing Awareness & Response.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`), including the fill-in contact lines.
- **External**
  - *Defensive Security Handbook*, 2nd edition — the Phishing Awareness and
    Response chapter checklist.

## Changelog

- **2026-08-22** — Initial spec, article, checklist, summary, and dialog
  written; spec and post agree. Status `accepted`. *(Željko, AI-mediated
  session)*
- **2026-08-22** — Post-review fixes applied (see REVIEW.md). *(Željko,
  AI-mediated session)*
