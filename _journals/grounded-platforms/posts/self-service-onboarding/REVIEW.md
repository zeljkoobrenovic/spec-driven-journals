# Review: Self-Service Platform Onboarding

**Reviewed:** 2026-08-20 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, summary.md, dialog.md, comics.md

## Verdict

A strong, publish-ready record. The API-first framing is carried consistently through every modality, the checklist is a faithful and complete reproduction of the source chapter's 15 sections, all twelve referenced images exist, and all ten `[[cross-links]]` resolve to real permalinks. No blockers and no majors. The single most valuable improvement: the five-name orchestrator candidate list (Argo Workflows, Tekton, Crossplane, Kratix, commercial) appears verbatim three times in the article alone — compress the second and third occurrences to "the maturity review."

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 4 · nit 4

### Blockers

None.

### Major

None.

### Minor

- **[spec.md · Success criteria]** Criteria 2–8 each bundle many obligations under one checkbox — criterion 8 ("Failure, observability, and readiness survive") packs roughly fifteen distinct items from capacity pre-checks to the maturity review. A reviewer can only mark the whole bundle met or unmet; a single dropped item is invisible. *Accept the coarse granularity knowingly, or split the largest criterion.*
- **[index.md · Rationale ¶2, Reference Stack table (last row), Scope and Revisiting]** The orchestrator candidate list — Argo Workflows, Tekton, Crossplane, Kratix, a commercial orchestrator — is named in full three times in one article (and again in checklist §15 and the dialog, where it belongs). *Keep the full list once (Rationale or Scope); elsewhere say "the maturity review."*
- **[index.md · Scope and Revisiting]** The closing sentence runs ~75 words with three nested clauses, embedding the seven comparison criteria (learning curve … cost) that checklist §15 already carries verbatim. Hard to parse in one pass. *Split into two sentences and drop the inline criteria list.*
- **[index.md · Statement, "Templates by archetype" bullet]** The bullet reaches into template internals — language/framework variants, Git storage, metadata, preview — which sits close to the spec's non-goal fence ("templates appear only as the complete unit the scaffolder provisions"). It mirrors source §9, so it is defensible, but trimming the variant/metadata detail would sharpen the [[starter-kits]] boundary. *Borderline; author's call.*

### Nits

- **[index.md · section order]** Reference Stack precedes How to Read This here (matching `platform-creation`), while `cicd-as-a-platform-service` and `starter-kits` place it after — a journal-internal inconsistency, not specific to this post.
- **[summary.md · "What it costs"]** "on somebody's pager" introduces an on-call claim no other modality states. Harmless color; fine to keep.
- **[dialog.md · "And after day zero?"]** Ana's "each one still holding quota and secrets" (immortal namespace) is a detail neither the article nor the source states. Harmless color.
- **[checklist.md · §1]** "Confirm the demo application is deployed" reproduces the handbook's tutorial-sequence prerequisite verbatim; it reads slightly oddly as an organizational checklist item, but the reproduction is deliberate and faithful.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight blockquote (API front door, one call, guardrails in bundle, complete unit, five-minute bar all present) |
| API-first design survives | met | index.md · Statement "The front door is an API" (all seven sub-items present); checklist §2 |
| The provisioning bundle survives | met | index.md · Statement "A team is one call"; checklist §3 |
| Namespace and RBAC conventions survive | met | index.md · Statement bullets 3 and "Three roles, one boundary"; checklist §§4–5 |
| Quota tiers survive | met | index.md · "Quotas are tiers, not negotiations"; checklist §6 |
| Identity integration survives | met | index.md · "Identity is wired, then reconciled" + Figure 2; checklist §7 |
| Lifecycle and the project unit survive | met | index.md · "Teams live, projects are whole"; checklist §§8–10 |
| Failure, observability, and readiness survive | met | index.md · "Failure and observability are part of the door" + Scope and Revisiting; the testing sub-list (rate-limit, quota-exhaustion, partial-failure, escalation) is carried by checklist §14 — satisfied across modalities |
| Credit is explicit | met | index.md · Authoritative References; summary.md footer; checklist intro |

Non-goals respected: yes. Templates appear as the provisioned unit (with the borderline detail noted in Minor above); CI/CD appears only as a bundle resource; day-2 infrastructure is absent; quota/cost-center labels stay guardrail-framed; [[four-pillars]] is cited as the bar, not restated.

Drift: none. Spec `status: accepted` is accurate; the Changelog and Decision log match what shipped.

## Cross-modality alignment

- **Facts & framing:** consistent — 63-character DNS-safe names, `POST /api/v1/teams`, `platform:teams:create`, three tiers, three roles, 409/503/429, backoff with jitter, three product metrics, and the five-minute bar are identical everywhere they appear.
- **Terminology:** consistent — "front door," "bundle," "complete developer unit," "queue tax," "the portal that ate the platform," "retry is the recovery procedure" travel intact across article, summary, dialog, and comic captions.
- **Voice & tone:** consistent — first-person declarative in article and summary; Ana/Ben split matches the journal's dialog convention; VERA/KAI comic register matches sibling posts.
- **Coverage parity:** even — every Statement beat lands in summary and dialog appropriately compressed; the comic carries the five core beats (API-first, one call, idempotency, guardrails, five-minute test) plus the queue-tax hook. No modality introduces a beat the spec lacks (the two nits above are color, not claims).

## Layer-by-layer notes

### Spec

- Well-formed against the template: Intent, Audience, checkable criteria, five fenced non-goals with owning records, Decision log explaining the API-first framing choice, Sources naming the exact PDF (including the note that the handbook series skips number 06).
- The criteria are transcription-heavy — effectively the entire source checklist restated as prose — which makes checking possible but coarse (see Minor). This matches the section's established pattern.
- Internal consistency is good: Intent's "one call / idempotent / five minutes" spine reappears verbatim in criteria and both Decision-log entries.

### index.md

- House record shape fully observed: DRAFT status highlight matching `status: draft:gray`, Statement → Reference Stack → How to Read This → Rationale → practice table → Anti-Patterns → Related Records → Scope → References. Headings are Title Case.
- Rationale is the strongest section — each paragraph earns a distinct claim (real-or-fake, replaceability, idempotency, guardrails-at-birth, identity drift, repo≠project, acceptance test) with the quotable "Idempotency is the difference between self-service and self-harm."
- All three figures exist under `assets/images/self-service-onboarding/` and are captioned; the eight anti-patterns each pair a name with a mechanism, matching the journal register.
- The only real friction: triple repetition of the orchestrator list and the overlong closing sentence (see Minor).

### checklist.md

- Faithful and complete against the source: all 15 sections present in order, item coverage essentially verbatim (spot-checked §§1, 2, 5, 6, 9, 11, 14, 15 — no invented obligations, no dropped items). Sensible light edits only (e.g. §2's first item rephrased without changing meaning).
- Two added cross-links ([[observability-implementation]], [[cicd-as-a-platform-service]]) both resolve — good house-style integration.
- Runnable as written; the closing five-minute bar sentence ties it back to the record.

### summary.md

- ~430 words, inside the modality target; leads with the decision and the bar; the What changes / What it costs / What we are not doing structure serves a leadership reader well.
- "What it costs" is a genuinely honest cost section (production service, up-front engineering, lifecycle teeth) rather than a restatement of benefits.

### dialog.md

- Ben presses with real objections ("Five minutes sounds like a demo number," "Nobody replaces their portal," "That's not a risk, it's a schedule") and Ana answers from the record — the voices stay distinct throughout.
- The DNS-label explanation of the 63-character rule is the dialog earning its keep: it explains a constraint the article only states.
- Covers every load-bearing beat plus all five non-goal handoffs in the closing section; the final one-sentence takeaway lands the thesis.

### comics.md

- Nine panels, hook → problem → wrong way → principle → mechanism → safeguard → guardrails → unit → closer: a clean arc with consistent door/crate visual metaphors.
- All nine panel images exist; captions match their alt text; cast block matches the journal's VERA/KAI convention.

## Fixes applied (2026-08-20)

- **[minor · spec.md]** skipped — coarse bundled success criteria are the section's established pattern (journal-wide convention, decided by orchestrator); the review confirms no criterion factually contradicts the modalities.
- **[minor · index.md]** Orchestrator candidate list de-duplicated: full list (Argo Workflows, Tekton, Crossplane, Kratix, commercial) kept once in Rationale ¶2; Reference Stack last row now reads "Decided by the maturity review"; Scope and Revisiting now references the maturity review without restating the candidates. Checklist §15 and the dialog keep the list, as the review intends.
- **[minor · index.md]** Overlong Scope and Revisiting closing sentence split into two sentences; the inline seven-criteria comparison list dropped (pointed at the Checklist tab, which carries it verbatim).
- **[minor · index.md]** skipped — "Templates by archetype" detail is marked borderline / author's call by the review; it mirrors source §9 and was left as written.
- **[nit · index.md]** skipped — Reference Stack / How to Read This section order is a journal-internal inconsistency across posts, not specific to this record; reordering here would trade one inconsistency for another.
- **[nit · summary.md]** skipped — "on somebody's pager" is harmless color the review says is fine to keep.
- **[nit · dialog.md]** skipped — Ana's "each one still holding quota and secrets" is harmless color per the review.
- **[nit · checklist.md]** skipped — §1's demo-application prerequisite is a deliberate, faithful reproduction of the source checklist.
