---
status: accepted
revised: 2026-10-18
---

# Spec: SAP S/4HANA: One Journal, Clean Core

## Intent

Explain what role SAP S/4HANA plays in an enterprise finance architecture and how to implement and integrate it well, at the depth a Chief Architect needs to make decisions: editions and RISE, the Universal Journal and what "single source of truth" really changes, ledgers, currencies, organizational structures, document splitting, FI-CA and BRIM for high volume, Central Finance, Group Reporting, MDG, integration surfaces, clean core and extensibility levels, migration approaches, release cadence and maintenance, shared responsibility under RISE, and Joule. The reader should leave able to say what belongs inside the SAP core and what outside, when to use FI-CA versus a custom subledger, what Central Finance can and cannot do, and how to measure and fund clean core. Northmere's SAP core anchors the chapter: an upgrade deadline, a custom-code remediation plan with a fitness function, and the SAP-level view of the 2027 Q4 Central Finance versus accounting-hub decision.

## Audience

Chief and enterprise architects, finance-systems and SAP solution architects, integration architects and finance-transformation leaders who own or depend on an S/4HANA core. Assumes architectural experience; defines SAP and accounting terms on first use.

## Success criteria

- [ ] Opens with the standard callouts, exactly three KEY POINTS and three failure patterns (Customization Concrete, The Swiss-Army ERP, The Borrowed Roadmap).
- [ ] Gives the 2025 renames once (Public Edition → SAP Cloud ERP, Private Edition → SAP Cloud ERP Private), treats RISE as a commercial bundle, and includes an edition trade-off table.
- [ ] Explains the Universal Journal with what it changes and what it does not, ledgers, currencies, organizational structures and document splitting (cautiously), with a Northmere ledger design and the Lisbon commission as a summary line.
- [ ] Shows FI-CA's totals-record and reconciliation-key posting with a worked agency invoice journal, and a FI-CA-versus-custom-subledger table linking [[designing-financial-ledgers]].
- [ ] Presents Central Finance mechanics, uses and limits, and both 2027 Q4 options at SAP level with a diagram and a table, leaving the decision open and general coexistence to [[multiple-erps]].
- [ ] Covers clean-core models and levels A–D as documented by SAP, and Northmere's remediation plan with a quarterly fitness function.
- [ ] States maintenance dates with sources and "as of October 2026"; separates generally available AI from announcements.
- [ ] Three mermaid diagrams; Questions to ask; Sources and Evidence grouped; Northmere numbers agree with the scenario ledger.

## Non-goals

- General ERP coexistence and convergence economics ([[multiple-erps]]).
- Custom ledger engineering and open-source ledger options ([[designing-financial-ledgers]]).
- The accounting of the examples ([[accounting-for-architects]]) and consolidation mechanics ([[onestream]]).
- The modernization pattern catalog ([[modernization-patterns]]) and the incremental SFP migration ([[incremental-modernization]]).
- SAP licensing metrics, RISE tiers and FUE ratios (unverified and contract-specific).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- End of mainstream maintenance for S/4HANA 2025 is not stated; verify in SAP's Product Availability Matrix before adding.
- Central Finance and FI-CA mechanics rest partly on SAP Learning and SAP consultants' blogs; re-check help.sap.com for the cited release before print.
- BRIM component names and BlackLine–SAP relationship may change; re-verify at publication.

## Decision log

- **2026-10-18** — Framed S/4HANA as "book of record, not the whole finance platform" with an inside/beside/outside table, rather than a module tour, so the chapter answers where SAP belongs.
- **2026-10-18** — Presented the 2027 Q4 decision as "where accounting logic lives" (documents versus rules) with Dana leaning to the hub but recording reversal conditions; rejected settling the decision here because [[multiple-erps]] owns the pattern choice.
- **2026-10-18** — Used the reported end-2027 mainstream maintenance of release 2022 as the scene's forcing date, citing a user-group source, rather than an unverified date for release 2025.
- **2026-10-18** — Kept ACDOCA and other SAP internals to the documented minimum; FI-CA posting described from SAP Learning, not from table-level detail.

## Sources

- **Internal**
  - [[custom-finance-platforms]] — SFP summarization, the FI-CA recommendation and the 2027 volume test.
  - [[finance-data-architecture]] — 3,900-account chart, master-data hub, partner hub.
  - [[oracle-fusion]], [[workday]] — the other ERPs in the convergence decision.
  - `_research/brief-sap.md`, `_research/productscape-digest.md`, `_research/scenario-ledger.md`.
- **External**
  - SAP News on maintenance strategy (2020, 2022), transition option (2025, updated October 2026), clean-core levels (August 2025) and Sapphire 2026 announcements.
  - SAP Learning on Private Edition upgrades, currency types, document splitting, FI-CA general-ledger integration, BRIM and extensibility.
  - SAP Press and SAPinsider on the Universal Journal, ledgers and Group Reporting; UK and Ireland SAP User Group on release 2022 maintenance; CIO on public ERP failure cases.

## Changelog

- **2026-10-18** — Initial spec and article written in an AI-mediated session from the SAP research brief, with additional verification of FI-CA ledger integration, document splitting and release 2022 maintenance.
- **2026-10-18** — Editorial review pass: forward notes on the superseded FI-CA merchant-subledger recommendation and the Dec 2027 accounting-hub decision, canonical SAP News URLs for three short links, American spelling, timetoread. *(AI-mediated session)*
- **2026-10-18** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-19** — Title renamed from "SAP S/4HANA: The Enterprise Finance Core" to "SAP S/4HANA: One Journal, Clean Core" at the author's request. *(AI-mediated session)*
