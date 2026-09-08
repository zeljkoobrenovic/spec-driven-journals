---
status: accepted
revised: 2026-08-22
---

# Spec: Databases

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

Fix the bar my organization holds its databases to — the systems where a
security failure becomes the headline. The post turns the Databases chapter
of the *Defensive Security Handbook* into an operating record: every critical
database is known, classified, and owned; access follows least privilege with
privileged access logged, reviewed, and managed; sensitive data is encrypted
at rest, in transit, and in backups, with keys stored separately, rotated,
and owned; secrets are never hardcoded and passwords never stored in
plaintext; SQL injection is treated as an application problem with database
consequences; unauthorized access and insider threats are both planned for;
exfiltration paths are closed and watched; configurations are hardened
against recognized standards and vulnerabilities patched on a defined clock;
activity is logged with someone owning the alerts; backups restore and
databases sit inside DR planning with defined RTO/RPO; cloud databases meet
the same bar as on-premises ones under a correctly read shared-responsibility
model; governance assigns ownership, standards, minimum requirements,
documented exceptions, and tracked risks; and database breaches are in the
incident-response plan, with third parties, acquisitions, and legacy systems
held to the same scrutiny. The load-bearing test, verbatim from the chapter:
five questions — what data do we have and where is it, who can access it and
why, how is it protected, how would we detect misuse or compromise, can we
recover quickly — answered clearly for every critical database, or the
organization has a database-security governance gap.

## Audience

Engineering leads and DBAs in my organization who own databases (so they know
the bar each database is held to); security engineers auditing data-layer
posture; peer executives who want to see what "we protect the data where it
lives" concretely means. First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states the database bar end to
      end and closes with the chapter's five-questions governance test.
- [x] **Architecture and classification survive** — knowing where critical
      and sensitive data is stored; which technologies are in use
      (relational, NoSQL, cloud-managed, serverless, self-managed); which
      databases are business-critical; who owns and operates each; the
      on-premises versus cloud security implications and the shared
      responsibility model; data classified by sensitivity, databases
      containing customer, personal, financial, credential, IP, and
      operationally critical data identified, and the highest-risk databases
      receiving the strongest protection.
- [x] **Access control and PAM survive** — authentication versus
      authorization, least privilege, tightly restricted administrative
      privileges, prompt removal of former employees and unnecessary
      accounts, strong authentication for privileged access, securely
      managed service accounts, no shared administrator accounts; privileged
      access logged and monitored, PAM considered for critical systems,
      periodic privileged-account review, application accounts without
      administrator or system-level privileges.
- [x] **Encryption and secrets survive** — encryption at rest, in transit
      (TLS), and of backups; TDE understood; keys stored separately from
      data, rotated, access-controlled, and owned, through a key- or
      secrets-management solution; passwords never in plaintext, hashing
      versus encryption, salted password hashing; no hardcoded credentials,
      a centralized secrets manager, and rotation without major disruption.
- [x] **Attack modes survive** — SQL injection (parameterized queries, input
      validation, least-privileged application accounts, secure coding
      standards, security testing); unauthorized access (brute force,
      credential stuffing, password reuse, dictionary attacks, stolen
      credentials; strong policies, MFA for administrative access, lockout
      and rate limiting, authentication-failure monitoring, default
      credentials removed); insider threats (malicious versus accidental,
      job-based access, privileged-user monitoring, separation of duties,
      export controls, role-change reviews); data leakage and exfiltration
      (no unnecessary public exposure, protected communications, secured
      backups/exports/snapshots/replicas, production data restricted in
      dev/test, bulk-download monitoring, cloud misconfiguration awareness).
- [x] **Operations survive** — hardening against documented standards with
      CIS Benchmarks and DISA STIGs named, least functionality, restricted
      network connectivity, configuration reviews; vulnerability and patch
      management with defined patch timelines, compensating controls, and
      tracked remediation; logging, monitoring, and detection with SIEM/XDR
      forwarding, defined alerts, sufficient retention, and a named alert
      owner; backup and recovery with encryption, restricted access,
      attacker-resistant copies, RTO/RPO, and tested restoration;
      availability and resilience including redundancy, failover, failure
      planning, and inclusion in DR/BC planning.
- [x] **Cloud, governance, incident response, and third parties survive** —
      cloud database inventory by provider, provider-versus-organization
      responsibilities, IAM review, no unnecessary public endpoints, network
      controls, encryption/logging/backups/monitoring enabled, continuous
      misconfiguration review; governance with per-database ownership,
      documented standards, minimum requirements across the eight named
      areas, periodic reviews, documented exceptions, and management-level
      risk tracking; database breaches in the IR plan with the
      what/who/when/how-much/which-credentials questions answerable;
      third-party, acquisition, and legacy scrutiny including supplier
      agreements and post-merger remediation.
- [x] **The question sets survive** — the chapter's seventeen "questions
      you should be able to answer" and the five-question priority reminder,
      reproduced in the checklist.
- [x] **Credit is explicit** — References name the *Defensive Security
      Handbook*, the Databases chapter checklist, and the standards the
      chapter names (CIS Benchmarks, DISA STIGs).

## Non-goals

- Not [[authentication]] — MFA, lockout, and password policy here apply at
  the database layer; the organization-wide identity model lives there.
- Not [[secure-software-development]] — SQL injection is stated here as a
  database consequence; the secure coding practice that prevents it lives
  there.
- Not [[disaster-recovery]] — RTO, RPO, and tested restoration here cover
  databases specifically; the organization-wide DR discipline lives there.
- Not [[cloud-infrastructure]] — cloud databases here must meet the same bar
  as on-premises; the cloud estate's own record lives there.
- Not a platform mandate — named technologies (MySQL, PostgreSQL, SQL
  Server, MongoDB) are the worked example; the commitments are stated at the
  capability level.

## Modalities

The working tool ships as the checklist modality (`checklist.md`, rendered
as the Checklist tab).

- [x] `checklist.md` — operational checklist
- [x] `summary.md` — management summary
- [x] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic *(added later with the visual layer)*

## Open questions

- None.

## Decision log

- **2026-08-22** — Grounded in the Databases chapter checklist of the
  *Defensive Security Handbook*, read through a practitioner-executive lens,
  as with every record in this journal.

## Sources

- **Internal**
  - `sources/checklists/defensive-security-handbook/Checklist_ DSH _ 13 _ Databases.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`), including the questions-you-should-be-able-to-answer
    section and the priority reminder.
- **External**
  - *Defensive Security Handbook*, 2nd edition (Lee Brotherston, Amanda
    Berlin, and William F. Reyor III; O'Reilly) — the Databases chapter.

## Changelog

- **2026-08-22** — Initial spec, article, checklist, summary, and dialog
  written; spec and post agree. Status `accepted`. *(Željko, AI-mediated
  session)*
- **2026-08-22** — Post-review fixes applied (see REVIEW.md). *(Željko,
  AI-mediated session)*
