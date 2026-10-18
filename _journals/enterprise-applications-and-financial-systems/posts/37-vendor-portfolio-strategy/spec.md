---
status: accepted
revised: 2026-10-18
---

# Spec: Vendor Strategy and Avoiding Excessive Dependency

## Intent

Show a Chief Architect how to get the benefits of strategic finance vendors without giving up the enterprise's options. The chapter argues that vendor strategy is architecture, because roadmaps, packaging and ownership shape what the enterprise can change. It gives the reader a toolset they can apply: a three-tier vendor model with governance per tier, a five-dimension dependency analysis, a **dependency budget**, an exit-plan standard with maturity stages (DORA-grade for Northmere Pay), contract levers, rules for where abstraction pays, multi-PSP as a priced hedge, a playbook for ownership and price events, and roadmap-alignment rituals. Northmere's October 2027 vendor strategy and risk register carry the argument.

## Audience

Chief and enterprise architects, finance-systems leaders, payments-platform leads and procurement or vendor-management leads who negotiate with SAP, Workday, Oracle, BlackLine, OneStream, Adyen, Stripe and the satellite vendors. Secondary: CFOs, controllers and compliance officers for Northmere Pay-style regulated entities who need to know what a real exit plan contains.

## Success criteria

- [ ] Reader can tier a vendor as strategic, core or tactical using written criteria, and state the governance attached to each tier.
- [ ] Reader can analyze a dependency on five dimensions (functional, data, skills, contractual, regulatory) and define a dependency budget with four lines (concentration, exit time, exit cost, proprietary surface).
- [ ] Reader can list the five elements of a real exit plan, cite DORA Art. 28(8), Art. 30(3)(f) and RTS 2024/1773 Art. 10 accurately, and explain exit maturity stages.
- [ ] EU Data Act switching rights are stated with verified dates and figures (12 Sep 2025; two-month notice; 30-day transition, up to seven months; reduced charges until 12 Jan 2027, none after) and with their limits (exportable data, Art. 31 exemptions, architecture barrier).
- [ ] A contract-levers table covers renewal timing, price caps, SLAs, data portability, termination assistance, change of control, roadmap commitments, token export and DORA terms.
- [ ] Reader can apply three tests for where abstraction pays, with Northmere seams (payments adapters, canonical events, tax adapter, e-invoicing gateway, normalized matching files) and the counter-case (no wrapper around the ERP's GL).
- [ ] Northmere worked example: tiers, a seven-row risk register with exit estimates and treatments, budgets for three strategic vendors, and the Adyen, SAP and OneStream decisions followed through; numbers agree with the scenario ledger.
- [ ] Ownership-change facts (OneStream/Hg, BlackLine acquisition interest) are dated and phrased per the briefs; no prediction about BlackLine's ownership.

## Non-goals

- The original sourcing decision and selection process — [[build-versus-buy]].
- Application TCO, TIME classification and the contract calendar mechanics — [[application-portfolio]].
- The DORA program, register of information and recovery testing in general — [[resilience-and-security]].
- Multi-PSP fundamentals and orchestration options — [[payments-fundamentals]]; Adyen and Stripe specifics — [[adyen]], [[stripe]].
- The canonical event model and anti-corruption layer design — [[loosely-coupled-domains]].
- Running the transformation program — [[finance-transformation]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- BlackLine's ownership status must be re-checked before publication; the chapter phrases it "as of late 2026".
- Whether specific Data Act provisions apply to existing (pre-September 2025) SaaS contracts is left to counsel; the chapter cites commentary only.
- Kyriba, Vertex and Adyen renewal dates and all exit estimates are illustrative additions to the ledger.

## Decision log

- **2026-10-18** — Chose three tiers with "any two criteria qualify" rules over finer schemes, because tier must change behavior (owner, review cadence, exit depth, decision records).
- **2026-10-18** — Framed the dependency budget on the SRE error-budget analogy with four checkable lines, so dependency is spent deliberately rather than forbidden.
- **2026-10-18** — Treated SAP as "contain, not exit": an honest exit plan for the group GL is a complete per-period extract plus clean core, not a fictional migration; made "no wrapper around the GL" the main counter-example to over-abstraction.
- **2026-10-18** — Positioned the EU Data Act as a contract lever and checklist, not an exit strategy, because it lowers contractual barriers but not architectural ones.

## Sources

- **Internal**
  - [[application-portfolio]], [[adyen]], [[stripe]], [[payments-fundamentals]], [[onestream]], [[blackline]], [[satellite-platforms]], [[loosely-coupled-domains]], [[target-and-transition-states]], [[resilience-and-security]], [[finance-transformation]].
  - `_research/brief-ea-integration-ledger.md` §5; `brief-payments.md` Part 4; `brief-blackline-onestream.md`; `brief-sap.md` §1.3–1.5; `brief-oracle.md`; `brief-workday.md`; `brief-satellites-ai.md`; `scenario-ledger.md`.
- **External**
  - Regulation (EU) 2022/2554 (DORA) Arts. 28 and 30; Delegated Regulation (EU) 2024/1773 Art. 10; Regulation (EU) 2023/2854 (Data Act) Arts. 23, 25, 29, 31, 50 — verified on EUR-Lex.
  - OneStream completion release; BlackLine SEC exhibit; Forrester on the OneStream take-private; SAP maintenance announcements; Oracle EBS Premier Support page; Workday Prism-to-Data Cloud guide; Stripe Sessions 2026.

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(Željko Obrenović, AI-mediated session)*
- **2026-10-18** — Editorial review pass: 'leverage' replaced by 'negotiating power'; Dec 2027 convergence outcome noted; American spelling. *(AI-mediated session)*
