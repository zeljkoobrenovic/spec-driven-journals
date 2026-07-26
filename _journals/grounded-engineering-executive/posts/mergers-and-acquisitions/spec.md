---
status: accepted
revised: 2026-07-26
---

# Spec: Operating Principle: Mergers and Acquisitions

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State how I participate in M&A as an engineering executive: strategy before
deals — no evaluation starts until the business strategy and a written,
deal-specific acquisition thesis exist; engineering due diligence is a
disciplined evaluation (implementation, IP, security, compliance, integration
mismatches, costs, culture) run against that thesis; the integration plan is
drafted before closing, not after; and my dissent, when overruled, is
documented professionally from a company perspective, not an engineering one.
The post turns the "Participating in Mergers & Acquisitions" checklist into a
durable operating principle: why engineering's job in M&A is to validate
assumptions and price integration honestly, including the final sanity check
— would I still approve the deal if I had to personally run the integration?

## Audience

CEOs, CFOs, and corp-dev peers who want to know what Engineering will and
will not sign off on in a deal; engineering leaders running their first due
diligence; my own leadership team when a deal appears. Declarative
first-person register — a vision statement, not a how-to tutorial.

## Success criteria

- [ ] **Principle is quotable** — the highlight blockquote states the
      thesis-first, integration-priced-in stance in one paragraph.
- [ ] **Rationale is argued, not asserted** — explains why deals evaluated
      without a written thesis drift, why valuation must reflect integration
      cost and risk (not just upside), and why sunk-cost bias is the failure
      mode to guard against.
- [ ] **Engineering evaluation is concrete** — the seven diligence areas
      (product implementation, IP, security, compliance, integration
      mismatches, costs & scalability, engineering culture) appear as real
      questions, not headings.
- [ ] **The checklist survives intact** — every section of the source PDF
      (business strategy, acquisition thesis, engineering evaluation, process
      discipline, integration plan, executive judgment & dissent, being
      acquired, final sanity check) appears in the Checklist tab (`checklist.md`), regrouped as
      bullets.
- [ ] **Both sides are covered** — the "If You Are Being Acquired" section
      survives as part of the principle, not dropped as an edge case.
- [ ] **Credit is explicit** — Authoritative References names Larson's *The
      Engineering Executive's Primer* and the lethain.com companion essay.

## Non-goals

- Not a treatise on engineering strategy itself — [[engineering-strategy]]
  covers how the strategy that M&A must serve gets written.
- Not a post-merger org-integration or onboarding guide —
  [[onboarding-peer-executives]] and [[engineering-onboarding]] cover
  bringing leaders and engineers in; this stays at deal evaluation and the
  integration plan.
- No legal or financial advice — deal structures, tax, and securities
  matters stay with Legal and Finance.

## Modalities

The working checklist ships as the checklist modality (`checklist.md`,
rendered as the Checklist tab). Summary/dialog/comics may be added later
per journal policy.

- [x] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [x] `comics.md` — explainer comic

## Open questions

- None.

## Decision log

- **2026-07-25** — The checklist ships as the checklist modality
  (`checklist.md`, Checklist tab) rather than an article section —
  journal-wide decision replacing the earlier embed-in-article choice.
- **2026-07-25** — Kept acquirer and acquired perspectives in one record,
  ordered acquirer-first to match the PDF; the operating principle (thesis,
  honesty about integration, documented dissent) is the same on both sides.
  Rejected: splitting "being acquired" into its own record — too thin to
  stand alone.

## Sources

- **Internal**
  - `sources/checklists/Mergers and Acquisitions.pdf` — the operating
    checklist this post is grounded in; reproduced in the Checklist tab (`checklist.md`).
- **External**
  - Will Larson, *The Engineering Executive's Primer* (O'Reilly, 2024) —
    the "Mergers and Acquisitions" chapter the checklist distills.
  - Will Larson, "Engineering's role in Mergers & Acquisitions"
    (lethain.com/engineering-in-mergers-and-acquisition/) — free companion
    essay.

## Changelog

- **2026-07-26** — Comics modality added (`comics.md`, Comic tab, shared VERA/LEO cast) and inline explainer illustrations added to the article; images generated with Gemini. *(Željko, AI-mediated session)*
- **2026-07-25** — Article and checklist modality written from this spec; spec
  and post agree. Status `draft` → `accepted`. *(Željko, AI-mediated session)*
- **2026-07-25** — Modalities and success criteria updated for the new
  checklist modality. *(Željko, AI-mediated session)*
- **2026-07-25** — Initial spec. Status `draft`. *(Željko, AI-mediated
  session)*
