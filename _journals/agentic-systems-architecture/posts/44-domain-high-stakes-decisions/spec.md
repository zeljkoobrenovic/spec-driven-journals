---
status: accepted
revised: 2026-10-28
---

# Spec: High-Stakes Decisions: Clinical and Public-Benefits Agents

## Intent

Close Part XI with the far end of the consequence range: work where an agent's output can injure a patient or take away a citizen's benefits. The chapter shows, through two reference designs worked end to end (a clinical decision-support and documentation agent, and a public-benefits casework agent, both design examples from the author's interview project), that the model becomes a drafter and evidence gatherer inside a deterministic pipeline: rules decide or veto, an accountable human owns every adverse outcome, failures default toward the outcome that does not harm the person, and the record is built so that the affected person and an independent reviewer can contest the decision. It ties these choices to the regulation that makes them obligations and to the documented, mostly non-LLM failures of automated public decision-making, and ends with what transfers to other domains, Ostrell included.

## Audience

Architects, principal engineers and technical leaders who design or review agents that shape decisions about people (healthcare, public services, and by extension HR, credit and insurance), and risk owners who must sign their controls. They know the platform machinery from earlier chapters; they need to see which parts become stricter and which become domain policy.

## Success criteria

- [ ] Reader can describe each design's consequence profile and explain why human review capacity, not compute, is the binding constraint.
- [ ] Reader can separate the deterministic layer's three roles (decide, veto, screen), and can state the gating predicate and fail-safe direction for each design, including why "fail closed" must not mean "deny" in benefits.
- [ ] Reader can map EU AI Act Annex III and Arts. 6(3), 12, 14, 26, 27 and 86 (with the Regulation (EU) 2026/1744 dates), GDPR Art. 22 and *SCHUFA*, the January 2026 FDA CDS guidance and HIPAA minimum necessary to components.
- [ ] Reader can follow both end-to-end sequence diagrams and the benefits two-axis lifecycle, and can name the book's adaptations of each source (consistency rulings 6–8 and 17).
- [ ] Reader can work through at least three failure scenarios with detection, containment and recovery.
- [ ] Reader can fill in a controls table (tier, oversight, evaluation, audit) per action class.
- [ ] Reader can explain Robodebt, the Dutch childcare-benefits scandal and MiDAS as non-LLM cautionary cases and map each mechanism to a control.
- [ ] Reader will not treat a human click as removing a system from Art. 22 without measured, real review.

## Non-goals

- Approval-gate design, approval fatigue and the automation-bias literature: [[human-oversight-and-bounded-autonomy]].
- Policy enforcement points and evidence-log mechanics: [[policy-enforcement-and-audit]].
- Idempotency, unknown outcomes and retries: [[retries-idempotency-and-concurrency]]; injection defenses: [[prompt-injection-defense]].
- The research-lab design (wet-lab boundary), used only as a comparison point.
- Legal advice; legal readings are the author's architectural interpretation.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- GDPR Article 22 amendments in the wider Digital Omnibus: secondary sources conflict; re-check before any revision.
- FDA AI-enabled device software lifecycle guidance was a draft at the time of research; check whether it has been finalized.
- Whether an EU clinical tool lands in Annex I (MDR route, 2 August 2028) depends on device class; the chapter states this as the author's reading.
- MiDAS settlement year (January 2023 vs 2024) and the 93% vs 44% contrast rest on secondary sources.

## Decision log

- **2026-10-28** — Kept Ostrell to a short framing (Tomas Verhoef reviewing the designs before Peoplepoint drafts performance summaries, an Annex III 4(b) use) and a "Back to Ostrell" close, so the domain examples stay clearly labeled as interview design examples.
- **2026-10-28** — Adopted a decide/veto/screen taxonomy for the deterministic layer and a per-domain fail-safe direction, resolving the sources' shared "the model cannot override" label (consistency ruling 7).
- **2026-10-28** — Adapted the benefits design: `confirm_adverse | override_to_eligible | request_more_evidence`, version-checked idempotent decisions bound to a package hash (ruling 6), extraction abstention (ruling 8), an explanation validator with template fallback, a PII-access audit, a sampled favorable path and a remand transition. Adapted the clinical design: combined safety/calibration outcome, calibration curve as a versioned artifact, three separate status records, `warn` acknowledgements as new records (ruling 17).
- **2026-10-28** — Recommended legible decision tables over policy as code in a contestability-first domain, presented as an open trade-off.

## Sources

- **Internal**
  - [[autonomy-and-consequence]], [[human-oversight-and-bounded-autonomy]], [[policy-enforcement-and-audit]], [[evidence-for-autonomy]], [[versioning-agent-systems]] — the mechanisms this chapter applies.
  - Scenario ledger — Peoplepoint scope, the A0 rule for employment decisions (consistency ruling 27), Closewise abstention cases, Answerdesk second-reviewer sampling.
  - Interview designs: `agentic-healthcare-platform` (steps 1–7), `agentic-public-benefits-platform` (steps 1–7), `agentic-research-platform` (step 4) — design examples only.
- **External**
  - Regulation (EU) 2024/1689 and 2026/1744; GDPR; CJEU C-634/21 (*SCHUFA*); FDA CDS guidance (2026) with Cooley and Covington summaries; 45 CFR 164.502 and 164.514.
  - Robodebt (APRA overview; LSJ), Amnesty (2021) and IAPP on the Dutch case, University of Michigan STPP on MiDAS.
  - Goh et al. (JAMA Network Open, 2024); Asgari et al. (npj Digital Medicine, 2025); Goddard et al. (2012).

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: aligned employment decisions to A0 and performance-summary drafts to an internal draft outside any action class (ruling 27); second-reviewer sampling 5% → 10%; corrected the Robodebt settlement wording; clarified decide/veto/screen against ruling 7; dated the Annex III application to Regulation (EU) 2026/1744. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-28** — Final figure-fix pass: Figure 3 (clinical sequence) replaced the plain mermaid screenshot with an illustration; all 15 messages checked. *(AI-mediated session)*
