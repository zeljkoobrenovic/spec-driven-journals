---
status: accepted
revised: 2026-10-28
---

# Spec: Side Effects: When Agents Touch the World

## Intent

Show architects how to design the boundary where a model's proposal becomes a fact in someone else's system. The chapter must land one separation, *intent* versus *execution*: deterministic code freezes each proposed effect into an immutable, hashed **action object**, and validation, approval, limits, idempotency, execution, verification and audit all refer to that object. It must define the **receipt** and its strengths (accepted, applied, settled or delivered) and separate it from read-back verification; define the **dry run** and the preview and what each proves; classify actions as reversible, compensable, irreversible or **external commitment**; and show that statements to customers are side effects, with a code-enforced rule that replies state an action's outcome only from its recorded state. After reading, the reader can review an agent's write path stage by stage and say which control attaches where.

## Audience

Software architects, principal engineers and platform leads who design tool brokers, agent runtimes and customer-facing agents, and the risk owners who sign off what an agent may do. They know outboxes, idempotent APIs and reconciliation; they need to know what changes when the arguments come from a variable, steerable model and when the agent's words bind the company.

## Success criteria

- [ ] Reader can list the fields of an action object (identity and hash, effect, authority, dependencies, risk, execution, presentation) and the five rules that make it work (built by code, immutable per version, executed from the stored object, expiring, naming its executor).
- [ ] Reader can walk the propose–validate–approve–execute–verify pipeline and name the single owner of each stage, none of them the model.
- [ ] Reader can distinguish a receiver's dry run, a simulated preview and a receipt, and state which receipt level closes a given action class.
- [ ] Reader can classify actions as reversible, compensable, irreversible or external commitment and choose the default control for each.
- [ ] Reader can explain *Moffatt v. Air Canada* in one paragraph, with its limits, and design a reply rule that keeps statements about actions true.
- [ ] The Ostrell example is worked end to end with ledger numbers (A2 ≤ €250, daily hold thresholds, Dealroom's A1 quotes and the CRM's superseded-price check, Closewise's posting key).
- [ ] Failure table names detection, containment and recovery; the Across Domains table is specific and ends with a platform-versus-policy judgement.
- [ ] Reader will not leave thinking a receipt proves the effect matches what was approved, or that MCP annotations enforce anything.

## Non-goals

- Idempotency keys, the `unknown` attempt state, retry layers and concurrency guards — [[retries-idempotency-and-concurrency]].
- Durable waits, timers and activities around approvals — [[durable-agent-execution]].
- Compensation design, sagas, kill switches — [[partial-failure-and-compensation]].
- Approval design and approver measurement in depth — [[human-oversight-and-bounded-autonomy]].
- Tool schemas and annotations — [[tool-contracts]]; the broker and registry — [[tool-ecosystems-and-mcp]].
- Delegated identity and credential scoping — [[agent-identity-and-least-privilege]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No published study measures the effect of action objects, previews or read-back verification on wrong agent side effects; revisit if one appears.
- Whether a court outside British Columbia adopts the *Moffatt* reasoning for an LLM-based agent (none verified as of October 2026).
- How MCP's confirmation mechanisms (elicitation, annotations) evolve after the 2026-07-28 revision, and whether any become enforceable.

## Decision log

- **2026-10-28** — Introduced the Promised Credit (April–May 2027) as a local Ostrell incident so the chapter's scene is about words as side effects, rather than retelling the Double Credit, which [[retries-idempotency-and-concurrency]] owns.
- **2026-10-28** — Made verification by read-back a separate stage after the receipt, and graded receipts by strength, because a receipt proves acceptance, not that the effect matches the approved object.
- **2026-10-28** — Defined the action object's lifecycle as wrapping the attempt state machine of chapter 24 instead of redefining `unknown`, keeping consistency items 4–6 in one place; the idempotency key covers the object version, consistent with Closewise's entry-version key.
- **2026-10-28** — Treated "human executes in their own tool" (Dealroom quotes) as an executor field on the same action object rather than a separate mechanism, consistent with consistency items 14 (staging store) and 15 (authorization separate from execution).

## Sources

- **Internal**
  - [[tool-contracts]], [[tool-ecosystems-and-mcp]], [[retries-idempotency-and-concurrency]], [[durable-agent-execution]], [[partial-failure-and-compensation]], [[task-state-and-checkpoints]], [[provenance-and-freshness]], [[evidence-for-autonomy]], [[prompt-injection-defense]].
  - `_research/brief-reliability-recovery.md` (parts 3, 5, 9, 11), `brief-domains-regulation.md` (parts 1, 4.3, 6.1), `brief-security-oversight.md` (1.2, 1.3, 2.7, 5.3–5.4), `brief-tools-execution.md` (3.5, 8); `consistency-issues.md` items 4–6, 14–15.
  - Interview designs (design examples): agentic-support-platform (`action-gate`, `txn-safety`), agentic-sales-platform (`send-gate`), agentic-finance-platform (`ledger`, `idempotency`), agentic-legal-platform, agentic-healthcare-platform (`gate`), agentic-public-benefits-platform (`gate`, `audit-appeal`), agentic-research-platform (`gate`).
- **External**
  - *Moffatt v. Air Canada*, 2024 BCCRT 149; *Mata v. Avianca* (S.D.N.Y., 2023).
  - Kubernetes dry-run documentation; Terraform `apply` documentation; transactional outbox (Richardson).
  - Garcia-Molina and Salem, *Sagas* (1987); OWASP LLM06 (2025); Meta Agents Rule of Two (2025); Beurer-Kellner et al. (2025).
  - Press accounts of the Replit (2025), DataTalks.Club (2026) and PocketOS (2026) deletions.
  - EU AI Act Article 14; MCP tools specification (2026-07-28).

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: worked example aligned with the credit tool contract (TCK-/VIS- refs, reason `missed_visit`, policy amount from the contract; €420 as `goodwill_other`); A1 approval expiry aligned to 4 working hours to the billing desk queue (ruling 25, was 24 h); A2 second-reviewer sample 10% (was one in twenty); per-visit and one-active-proposal-per-ticket credit limits (ruling 21); manifest label `ad-2027.10.2` in the action object; "turn" to "exchange" (ruling 19); PocketOS claim corrected to what Euronews reports; "Next" heading removed. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-28** — Final figure-fix pass: Figure 4 (action lifecycle) corrected: added the Voided to end arrow. *(AI-mediated session)*
