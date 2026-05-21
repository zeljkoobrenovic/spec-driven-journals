---
status: draft
revised: 2026-05-20
---

# Spec: Claude Code Policy for Software Development

> Filled in during the second pass over backfilled specs. Status `draft`.

## Intent

State a practical policy for **accountable agentic coding**: human
review, data classification, approved tools, permission modes, hooks,
audit trails, incident handling. The rules are paired with **executable
mechanisms** — allowlists, registries, audit trails.

## Audience

- **Developers** accepting AI-generated changes.
- **Security and compliance** ensuring controls work.
- **AI Engineering Enablement** wiring the mechanisms.

## Success criteria

- [ ] Reader knows policy starts with **human accountability**.
- [ ] Reader knows rules are **paired with executable mechanisms**.
- [ ] Reader can identify data classification and audit
      requirements.

## Non-goals

- Defining specific Skills/MCP allowlists.
- Replacing security policy outside AI.

## Open questions

- Audit-trail granularity.

## Decision log

- **2026-05-20** — Made policy **paired with mechanisms**.
  Considered policy-as-text-only; rejected because that drifts.

## Sources

- **Internal**
  - [[operating-model]] — operates the policy.
  - [[claude-code-enablement]] — encodes the policy.
  - [[ai-policy]] (decisions log) — same shape, strategic record.
- **External**
  - OWASP LLM Top 10.
  - NIST AI RMF.

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
- **2026-05-20** — Initial spec created.
