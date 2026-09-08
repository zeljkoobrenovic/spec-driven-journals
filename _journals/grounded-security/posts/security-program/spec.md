---
status: accepted
revised: 2026-08-22
---

# Spec: Creating a Security Program: Risk Before Tools

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

Open The Security Program section: fix the shape of how a security program in
my organization is created — before any tool is bought. The post turns the
"Creating a Security Program" chapter of the *Defensive Security Handbook*
into an operating record: the program starts from purpose, business
objectives, and a chosen framework (NIST CSF 2.0's Identify, Protect, Detect,
Respond, Recover, Govern functions); responsibility is structured into
executive, risk, security, and auditing functions with cross-team
coordination; the baseline security posture is documented before it is
improved; threats and risks are assessed and calculated (Risk = Likelihood ×
Impact) into a maintained risk register; every risk receives an explicit
treatment — avoided, remediated, transferred, or accepted with a named
approver and an expiry; governance closes the loop through policies,
compliance tracking, reporting, training, and continuous improvement; work is
prioritized into tiered milestones from quick wins to multiyear goals; and
the program rehearses through security use cases, kill-chain mapping,
tabletop exercises, and technical drills. The load-bearing test: every major
risk has an owner, a treatment decision, and a review date in a maintained
risk register — and the program itself is periodically reassessed.

## Audience

Security and engineering leaders in my organization standing up or auditing a
security program (so they know the bar); team leads asked to own a risk or a
milestone; peer executives who want to see what "risk before tools" concretely
means. First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states the program shape end to
      end (framework, structured responsibility, documented baseline,
      calculated risk, explicit treatment, tiered milestones, rehearsal) and
      the risk-register test.
- [x] **Groundwork and framework survive** — purpose and business objectives
      first; NIST CSF 2.0 and its six functions named; compliance and
      regulatory requirements identified; the warning against blindly
      applying standards that do not fit; documented initial scope.
- [x] **Team structure survives** — executive leadership (CIO or CISO) with
      organization-wide authority, funding, and milestone approval; a risk
      team with a framework where appropriate (NIST RMF, OCTAVE); a security
      team owning daily operations and specialist roles; an independent
      auditing function; cross-team coordination, with roles combined in
      smaller organizations and separated as they grow.
- [x] **Baseline posture survives** — the full documentation sweep: policies
      and procedures, endpoints, licensing and certificates, internet
      footprint, network infrastructure, logging and monitoring, ingress and
      egress, vendors, applications.
- [x] **Risk assessment and treatment survive** — scoped assessments,
      critical assets and threats identified (including the common-threat
      list), scans and reviews conducted, likelihood and impact rated 1–5,
      Risk = Likelihood × Impact recorded in the register; the four
      treatments (avoid, remediate, transfer, accept) with acceptance
      requiring justification, approval, compensating controls, and a review
      date; risk monitored as standing work.
- [x] **Governance and prioritization survive** — documented risk-management
      policies, regulatory tracking, reporting channels to management and
      board, training and awareness, continuous improvement; prioritization
      by rank, business context, and low-cost/high-impact wins; milestones in
      four tiers from quick wins to long term.
- [x] **Rehearsal survives** — roughly three high-priority security use
      cases converted into playbooks; attacks mapped to the Cyber Kill Chain
      stage by stage; tabletop exercises with preparation, materials,
      execution, and follow-up; technical drills (backup restoration,
      DR, failover, IR procedures); team skill development including labs,
      CTFs, and mentoring; the program completion review reproduced.
- [x] **Credit is explicit** — References name the *Defensive Security
      Handbook* and the "Creating a Security Program" chapter checklist.

## Non-goals

- Not [[asset-management]] — the baseline documentation here is a one-time
  sweep to ground the program; the standing asset-management program with a
  single source of truth lives there.
- Not [[policies]] — governance here says documented policies must exist; the
  document discipline (language, contents, lifecycle) lives there.
- Not [[compliance]] — regulatory requirements are identified here; the full
  compliance frame lives there.
- Not [[incident-response]] — use cases, playbooks, and tabletop exercises
  are established here; the incident-response operating model lives there.
- Not [[vulnerability-management]] — scans inform the risk assessment here;
  the standing scan-triage-remediate loop lives there.
- Not a tool selection — the record deliberately contains no product choices;
  the program is designed before anything is bought.

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

- **2026-08-22** — Grounded in the "Creating a Security Program" chapter
  checklist of the *Defensive Security Handbook* (Lee Brotherston, Amanda
  Berlin, and William F. Reyor III), read through a practitioner-executive
  lens, as with every record in this journal.

## Sources

- **Internal**
  - `sources/checklists/defensive-security-handbook/Checklist_ DSH _ 01 _ Creating a Security Program.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`), including the program completion review.
- **External**
  - *Defensive Security Handbook*, 2nd edition — the "Creating a Security
    Program" chapter checklist.

## Changelog

- **2026-08-22** — Initial spec, article, checklist, summary, and dialog
  written; spec and post agree. Status `accepted`. *(Željko, AI-mediated
  session)*
- **2026-08-22** — Post-review fixes applied (see REVIEW.md). *(Željko,
  AI-mediated session)*
