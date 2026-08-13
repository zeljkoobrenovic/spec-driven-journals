# Review: Implementing Platforms

**Reviewed:** 2026-08-13 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

The strongest-argued of the implementation-mechanics records: the three-planes-plus-two-tests frame gives the article a memorable spine, the checklist is a thorough, well-ordered reproduction of the chapter checklist, and the comic tracks the argument faithfully with all eight panel images present. One real issue stands between this and clean spec compliance: the spec's fourth non-goal promises the record "names no specific portal, orchestrator, or cloud product", yet Kubernetes is named in the article (twice) and the checklist — the letter of the non-goal is breached even though the spirit (no endorsement) is intact. Reconcile the spec wording or the mentions; everything else is polish.

## Findings by severity

**Counts:** blocker 0 · major 1 · minor 3 · nit 1

### Blockers

- None.

### Major

- **[spec.md · Non-goals vs index.md · Rationale ¶2 and "What This Means in Practice" row 2; checklist.md §2]** The spec's fourth non-goal states the record "deliberately names no specific portal, orchestrator, or cloud product", but Kubernetes is named three times ("delegate it to tools like Kubernetes or cloud automation", "delegating to Kubernetes or cloud automation is a legitimate implementation choice", checklist §2's delegation item). The mentions are illustrative, not endorsements, and the checklist one is source-faithful — so the spec's absolute phrasing looks like the wrong side of the disagreement. *Suggest relaxing the non-goal to "not a technology endorsement — tools may be named as illustrative examples", or scrubbing the article mentions; author's call.*

### Minor

- **[index.md · Statement, bullet 1]** The three-planes bullet runs ~80 words across dense enumerations — the heaviest single lift in the Statement, and the one place a first-time reader may need a second pass. *Suggest splitting the control-plane clause into its own sentence.*
- **[index.md · Statement, bullet 1 / spec criterion 2]** The spec's anatomy criterion includes "SDLC capabilities" in the services plane, but the article never mentions them; they surface only in checklist §3. The criterion is met across modalities, but the article's services-plane sentence presents itself as the complete anatomy. *Three words fix it: "…governed user-contributed services, plus SDLC capabilities."*
- **[checklist.md · §4 heading "IDP Integration"]** "IDP" is never expanded anywhere in the post, and the section's first items are IAM, SSO, and access controls — an unprimed reader will parse IDP as Identity Provider. *Suggest "Internal Developer Platform (IDP) Integration".*

### Nits

- **[index.md · Anti-Patterns, "CRUD cosplay"]** A register spike — playful in a list whose neighbors are sober ("Day-one-only correctness", "The implicit ownership boundary"). Fine if intentional; flagged for consistency.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight blockquote |
| The anatomy survives | met | index.md · Statement b1, Figure 1; checklist.md §1–3 (SDLC capabilities only in checklist — see Minor) |
| Control-loop and orchestration ideas survive | met | index.md · Statement b2–b3, Rationale ¶2–3, Figure 2; checklist.md §5–7 |
| Traceability and ownership survive | met | index.md · Statement b4–b5, Rationale ¶4–5; checklist.md §8, §10 |
| Tenancy and scale survive | met | index.md · Statement b6, Rationale ¶6, Figure 3; checklist.md §11–14 |
| Credit is explicit | met | index.md · How to Read This, Authoritative References |

Non-goals respected: three of four. The fourth ("names no specific portal, orchestrator, or cloud product") is breached by the Kubernetes mentions (see Major).
Drift: no structural drift — the post delivers the spec's contract; the non-goal wording and the Kubernetes mentions need reconciling, but that is a one-sentence spec fix, not `status: drifted` territory.

## Cross-modality alignment

- **Facts & framing:** consistent — three planes, Observe → Analyze → Act, the two tests, three tenancy approaches, and the burst-load warning appear identically in article, checklist, and comic.
- **Terminology:** consistent — "forty-parameter template", "ClickOps", "only right on day one", "noisy neighbors", and the logical/namespace/resource isolation ladder carry across all modalities without renaming.
- **Voice & tone:** consistent first-person declarative; the comic's captions reuse the article's own sentences compressed, not reworded.
- **Coverage parity:** even for the spec's beats. Checklist §4 (IDP Integration) and §9 (Application Code and Architecture as Code) have no article echo — acceptable for the checklist's reproduce-the-source purpose, and neither is a spec criterion; noted, not counted.

## Layer-by-layer notes

### Spec

- Well-shaped contract: the "anatomy plus two tests" framing decision is logged, criteria are enumerable, and three of four non-goals fence cleanly against sibling records.
- The fourth non-goal is written more absolutely than the article (or the source-faithful checklist) can honor — the one internal inconsistency in an otherwise tight spec.

### index.md

- Excellent Statement-to-Rationale mapping: six bullets, six paragraphs, in matching order — easy to follow and easy to audit.
- The bolded thesis sentences ("A platform that provisions but does not reconcile is only right on day one", "the first unexplainable failure converts an advocate…") are quotable and earn their emphasis.
- All three figures exist on disk and are captioned; all five `[[…]]` cross-links resolve; the "Final Readiness Check" reference matches the checklist's actual final-section title.
- Highlight status DRAFT matches front-matter `status: draft:gray` and the Scope section.

### checklist.md

- Thorough and well-ordered: 14 sections plus Final Readiness Check, with nested sub-checklists (SDLC list, tenancy options, isolation levels) that keep it runnable rather than flat.
- Italic source notes are consistently descriptive and match the article's claims (control loop, tenancy approaches, burst warning).

### comics.md

- Eight panels, all image files present, captions run Panel 1–8, captions match alt text and (spot-checked) images; VERA/KAI cast consistent.
- Strong beat selection: hook (hidden complexity returns), problem (ticket platform), wrong way (forty-parameter template), principle (three planes), engine, thread-back, cost, closer (two tests) — mirrors the article with no invented claims.

## Fixes applied (2026-08-13)

- spec.md · fourth non-goal vs Kubernetes mentions — fixed: relaxed the non-goal per the reviewer's suggested direction ("tools may appear as illustrative examples, never as a recommendation"); article and checklist mentions kept as-is; spec `revised:` bumped and Changelog line added.
- index.md · Statement, bullet 1 (density) — fixed: control-plane sentence split into two clauses (reconcile; carry identity/catalog/orchestration), lightening the bullet's heaviest lift.
- index.md · Statement, bullet 1 / spec criterion 2 — fixed: services-plane sentence now ends "…governed user-contributed services, plus SDLC capabilities", completing the anatomy in the article.
- checklist.md · §4 heading — fixed: expanded to "Internal Developer Platform (IDP) Integration".
- index.md · Anti-Patterns "CRUD cosplay" — fixed: renamed to "The CRUD portal" to match the sober register of its neighbors; description unchanged.
