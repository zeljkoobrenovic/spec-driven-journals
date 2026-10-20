# Productscape Digest: Enterprise Applications and Financial Systems (generalised)

Source model: `productscape-examples/_config/product-domains/booking-holdings/finance-systems-architecture` (Productscape domain, model date 18 Oct 2026). Files read: `_domain/DOMAIN.md`, `start/config.json`, `product-bricks/product-bricks.json`, `product-bricks/product-stream.json`, `data/data-assets.json`, `product-deployments/products.json`, `product-deployments/deployment.json`, `customers/customers.json`, `customers/insights.json`, `customers/relations.json`, `customers/links.json`, `business/competition.json`, `residuality/residuality.json`, `tutorial/tutorial.json`; two of the image-prompt files were skimmed and add nothing beyond the tutorial text.

**Generalisation convention.** "The group" means a US-listed, multi-brand online travel marketplace with five brands, many legal entities, heavy European operations and a set of licensed e-money institutions. "The flagship brand" is its largest, Europe-based brand. Scale figures are kept only where they teach proportion. All such figures are FY2025 public-filing numbers that the model cites: about $26.9bn revenue, $186bn gross bookings, 1.2bn room nights, 70% of gross bookings on a merchant basis (63% the year before) and $5.3bn of deferred merchant bookings. Vendor names (SAP, Oracle, Workday, BlackLine, OneStream, Adyen, Stripe) are kept because they name **platform categories**. The model itself flags most of them as assumed, not confirmed.

**Framing of the model.** The model takes the view of a *Senior Director of Architecture, Enterprise Applications and Financial Systems*. This person is the functional head of architecture for the global finance ecosystem. They hold **final decision rights on mandatory enterprise-application standards** and lead brand engineering teams through a matrix rather than direct reporting lines.

---

## 0. Domain boundary and value exchange

**Core scope.**
- **Global finance core:** the general ledger and central-finance hub, the chart of accounts and financial master data, legal entities, intercompany and FX accounting.
- **Subledger and revenue:** a high-volume contract-accounting and billing subledger, revenue recognition (merchant vs agency, gross vs net, ASC 606), traveler funds and deferred merchant bookings.
- **Money movement:** payments-to-ledger for card-not-present cards and alternative payment methods (APMs), PSP settlement reconciliation, refunds and chargebacks, partner commission invoicing, partner payouts and bank connectivity.
- **Enterprise business applications:** source-to-pay, indirect tax (VAT, digital services taxes, travel taxes, DAC7), the tax provision and Pillar Two, treasury and FX hedging.
- **Close, reporting and controls:** close orchestration and reconciliation, consolidation and SEC reporting, planning, SOX access and control monitoring, and e-money safeguarding with regulatory reporting for the licensed payment entities.
- **Finance data and integration:** the integration hub, a brand adapter kit, the finance data platform and governed metrics.
- **Architecture governance:** decision records and a review board, standards and conformance, the application portfolio and technology ROI, target-state and dependency maps.

**Adjacent, outside the core.** The payments platform product (checkout, PSP routing, fraud scoring), owned by FinTech/payments teams. Brand booking engines. HR and travel-and-expense systems.

**Excluded.** Traveler-facing products, loyalty, martech, CRM and finance-operations staffing.

**Value exchange.** Internal customers fund the platforms through technology budgets and a cost **Transformation Program** covering modernised processes and systems and procurement optimisation. The modeled company reported about $250M of realised savings in one year and about $550M of annual run-rate savings enabled. The value is a controlled, scalable finance core:
- faster and cleaner closes;
- every payment reconciled;
- partners paid on time;
- taxes right;
- effective ICFR;
- fewer duplicate brand systems.

The architecture function "earns its place by speeding up decisions and replacing tactical workarounds with reusable patterns."

**Why the merchant shift matters architecturally.** As the agency-to-merchant mix moves (63% → 70% merchant in one year), payment, liability and reconciliation volume moves *into* the finance core. Under agency, finance only invoices commission. Under merchant, finance holds traveler money, processes refunds and disputes, pays partners and safeguards funds.

---

## 1. Domain decomposition: product bricks (24 bricks in 6 root groups)

Each brick in the model has typed modules arranged in layers (ui / interfaces / worker / service / stateless-service / integration). Each also has brick-to-brick dependencies typed *data / composition / context / control / governance*, data dependencies (own / read / consume) and external systems. Status is *invest* or *sustaining*. Below, **SoR** means the data asset for which the brick is the system of record.

### 1.1 Global Finance Core

#### Ledger and Accounting Core

**`glco` General Ledger and Central Finance Hub** (service, invest)
- **Purpose.** The single book of record for every legal entity. It is a universal-journal ledger with **parallel ledgers** for the group GAAP (US GAAP) and local statutory GAAP, period control, and the document flow from subledgers into the ledger. It is fed through a central-finance replication hub from brand and legacy ERPs, which is the classic SAP Central Finance pattern used as a bridge to S/4HANA.
- **Modules:**
  - Ledger Workspace: journal entry, document display and period status.
  - Ledger Posting and Query API: a governed API for postings, balances and document lookups, used by subledgers, close tooling and extraction.
  - Central Finance Replication Monitor: watches replication (SLT/AIF-type), surfaces failed postings and drives reprocessing.
  - Period Open/Close Controller: posting-period status per company code and ledger.
  - Universal Journal Service: the line-item journal (ACDOCA-type).
  - Central Finance Source Adapter: mapping and replication of brand and legacy postings, with harmonised master data.
- **Dependencies:**
  - coam (context): every posting is validated against the chart of accounts, cost objects and company codes.
  - entm (composition): entity, intercompany-partner and FX data.
  - brim (data): summarised subledger postings.
  - sodc (control): posting and period-change authorisations.
- **SoR:** General Ledger Journal.
- **External:** S/4HANA (runtime assumed to be RISE private cloud) and the brand/legacy ERPs. The external auditor consumes ledger extracts.

**`coam` Chart of Accounts and Financial Master Data** (full-stack, invest)
- **Purpose.** Governs the global chart of accounts, company codes, cost and profit centres, segments and **versioned mappings from brand-local charts**. Harmonised master data is the *precondition* for central-finance replication and for brand convergence. An MDG-style workflow is assumed.
- **Modules:**
  - Master Data Request Portal, with four-eyes approval.
  - Financial Master Data API: read access plus a change-event feed.
  - Master Data Change Publisher: pushes changes to the ledger, subledger, consolidation and the data platform.
  - Change Request Workflow: validation, then controller approval, then activation.
  - Financial Master Data Store.
- **Dependencies:** entm (company codes reference legal entities); sodc (requesters and approvers are checked against SoD rules).
- **SoR:** Chart of Accounts and Financial Master Data.

**`entm` Legal Entity, Intercompany and FX Accounting** (service, sustaining)
- **Purpose.** Holds the legal-entity register, including the licensed e-money entities, together with intercompany agreements and settlement, transfer-pricing charges, daily FX rates and revaluation. EUR and GBP are the principal exposures. Revaluation and intercompany elimination drive both close quality and tax outcomes.
- **Modules:**
  - Entity and Intercompany API.
  - Intercompany Matching Job: matches IC payables and receivables before close.
  - FX Rate and Revaluation Service: month-end revaluation of open items and balances.
  - Legal Entity and Intercompany Register: licences, functional currencies, IC agreements and transfer-pricing rules.
  - Market Rate Feed Adapter.
- **Dependencies:** glco (posts revaluation and IC entries); trcm (entity bank structure and hedge designations).
- **SoR:** Legal Entity and Intercompany Register. External tax and transfer-pricing advisers consume it.

#### Subledger and Revenue

**`brim` High-Volume Transaction Subledger** (service, invest; an SAP FI-CA/BRIM-type contract-accounting subledger)
- **Purpose.** Turns booking, payment, cancellation and commission events into business-partner and contract-account postings at booking scale (around a billion-plus room nights a year). It keeps transaction detail out of the GL, posts summarised entries, and provides **open-item clearing** for traveler payments, partner balances and commission receivables.
- **Modules:**
  - Subledger Posting API.
  - Booking Financial Event Consumer: **idempotent** processing of events from the integration hub.
  - GL Summarisation Job: summarises to the GL **with reconciliation keys**.
  - Convergent Charging and Invoicing: turns events into billable and postable items per brand, model and currency.
  - Contract Accounting Subledger: business partners, contract accounts, open items and clearing history.
- **Dependencies:** fint (events in); glco (summaries out); rrec (revenue schedules are driven from subledger items); itax (tax determination for invoiced items).
- **SoR:** Contract-Account Subledger Posting.

**`rrec` Revenue Recognition Engine** (service, invest)
- **Purpose.** Applies ASC 606 to merchant and agency transactions:
  - the principal-versus-agent judgement;
  - gross vs net presentation;
  - timing at check-in or at stay completion;
  - cancellations and refunds;
  - payment-facilitation revenue.

  In the modeled company, merchant revenue was about $17.8bn (+25.5%) and agency about $8.0bn (−6.5%), so this is "the most material revenue judgement in the core."
- **Modules:**
  - Revenue Recognition API.
  - Recognition Run Scheduler: daily and period-end runs that post revenue and release deferrals.
  - Recognition Rules Service: picks the recognition pattern from contract type, model, product and event.
  - Revenue Schedule Store: performance obligations and recognised/deferred amounts, with an audit trail.
- **Dependencies:** brim (items and events that create or change obligations); tfnd (composition: releases deferred merchant bookings on recognition); glco.
- **SoR:** Revenue Recognition Schedule. The external auditor consumes the evidence for the principal/agent and timing judgements.

**`tfnd` Traveler Funds and Deferred Merchant Bookings Ledger** (service, invest)
- **Purpose.** Tracks cash received from travelers **before performance**. The balance was $5.3bn at year end, up from $4.0bn, and is mostly refundable on cancellation. The brick keeps the liability **per booking**, links it to funds held by the licensed e-money entities, and releases it on stay, cancellation or payout.
- **Modules:**
  - Traveler Funds API: balances and movements by booking, entity and currency.
  - Funds Movement Consumer: applies captures, refunds, cancellations and payouts.
  - Liability Aging Job: flags stale or negative liabilities and prepares safeguarding inputs.
  - Deferred Merchant Bookings Ledger: reconciled to the subledger and to safeguarding positions.
- **Dependencies:** pevt (captures and refunds); regr (feeds traveler-funds positions to safeguarding); brim (reconciles to open items).
- **SoR:** Deferred Merchant Bookings Balance.

### 1.2 Money Movement and Settlement

#### Payments-to-Ledger

**`pevt` Payment Event Ingestion and Normalisation** (integration, invest)
- **Purpose.** Ingests card-not-present card and APM events (authorisations, captures, refunds, fees, settlements) and PSP/acquirer settlement reports. It normalises them into **one finance-ready payment record** with fee and FX components. New local methods must be **ledger-ready before launch**. The payments platform itself (checkout, routing, fraud) is upstream and out of scope.
- **Modules:**
  - Payment Record API.
  - Payment Event Consumer.
  - Settlement Report Ingestor: SFTP/API collection with completeness validation.
  - Payment Normalisation Service: maps method-, PSP- and scheme-specific formats to one canonical schema.
  - Payment Record Store: transactions, fees, interchange and settlement lines.
  - PSP and APM Adapters: one adapter per provider or method.
- **Dependencies:** fint; brim (hands over normalised payments for posting and clearing).
- **SoR:** Payment Transaction and Settlement Record.

**`psrc` Payment and PSP Settlement Reconciliation** (service, invest)
- **Purpose.** **Three-way matching** of bookings, payment transactions and PSP/bank settlements, with exception queues and aging. Merchant transaction costs rose by $381M in one year with the merchant shift, so mis-booked or unreconciled fees hit the P&L directly.
- **Modules:**
  - Reconciliation Exception Workbench: root-cause tagging.
  - Reconciliation API: match status, exceptions and **reconciliation certificates** per PSP, entity and period.
  - Matching Engine Job: rule- and tolerance-based matching.
  - Match Result Store: match groups, exceptions, write-offs and certifications.
  - Bank Statement Adapter: camt.053 / MT940.
- **Dependencies:** pevt; brim (open items to clear); bnkc (bank statements); clse (publishes certificates into the close checklist).
- **SoR:** Reconciliation Match Result.

**`cbkf` Refund, Chargeback and Dispute Accounting** (full-stack, sustaining)
- **Purpose.** Accounts for refunds, scheme chargebacks, APM disputes and representment outcomes, including recovery from partners where the contract allows. Each dispute stage must post correctly to the subledger and to revenue, and losses must be provisioned.
- **Modules:**
  - Dispute Accounting Console: financial impact, liability owner and posting status.
  - Dispute Accounting API.
  - Dispute Event Consumer.
  - Dispute Case Ledger: stages, amounts, liability and recovery.
- **Dependencies:** pevt; brim; rrec (revenue is adjusted for refunds and lost disputes).
- **SoR:** Chargeback and Refund Case. External: card schemes and PSP dispute services.

#### Partner Settlement

**`pinv` Partner Commission Invoicing and Collections** (full-stack, sustaining)
- **Purpose.** Invoices agency-model partners for commission and collects it by direct debit, card or bank transfer, with dunning and dispute handling. Agency revenue is about $8bn and is almost entirely accommodation commission.
- **Modules:**
  - Partner Invoice and Dispute Console.
  - Partner Invoicing API, serving partner extranets.
  - Commission Billing Run: periodic billing of completed stays, with tax.
  - Dunning and Collections Service.
  - Partner Invoice Store.
  - **E-Invoicing Gateway Adapter**: mandated formats and clearance models.
- **Dependencies:** brim (composition: commission items and open items); itax (VAT on commission); psrc (reconciled incoming payments clear invoices).
- **SoR:** Partner Commission Invoice.

**`pout` Partner Payout Orchestration** (full-stack, invest)
- **Purpose.** Calculates and schedules payouts to merchant-model partners, net of commission, by bank transfer or **virtual card**. It honours payout terms, currencies, holds and fraud checks. Payout accuracy and timing are a primary partner-experience lever and a working-capital lever.
- **Modules:**
  - Payout Operations Console: calendar, holds, failed payouts, bank-detail changes.
  - Partner Payout API.
  - Payout Scheduler: batches by currency, method and cut-off, then releases to the payment factory.
  - Payout Calculation Service: net of commission, taxes and adjustments.
  - Payout Instruction Store.
- **Dependencies:** tfnd (releases funds held); brim (partner balances); bnkc (composition); trcm (liquidity and FX funding).
- **SoR:** Partner Payout Instruction **and** Partner Bank and Payout Details, the latter under change control. External: a virtual-card issuing provider (assumed).

**`bnkc` Bank Connectivity and Payment Factory** (integration, sustaining)
- **Purpose.** The central payment factory for outgoing payments (partner payouts, supplier payments, intercompany) and incoming statements. It handles format conversion (pain.001 and local formats), dual-approval workflow, the sanctions-screening hand-off, and connectivity over SWIFT and host-to-host channels.
- **Modules:**
  - Payment Factory API.
  - Payment File Dispatcher: works within bank cut-offs.
  - Payment Approval Workflow: dual approval and limit checks.
  - Payment Batch Store: batches, approvals, acknowledgements and statements.
  - Bank Channel Adapter.
- **Dependencies:** trcm (accounts, signatories, positions); sodc (approver rights).
- **Shared** by partner settlement, source-to-pay and treasury.

### 1.3 Enterprise Business Applications

#### Source-to-Pay

**`s2pp` Procurement and Supplier Management** (full-stack, invest)
- **Purpose.** Source-to-contract and requisition-to-order for indirect spend (cloud, marketing services, software, real estate, professional services), with supplier onboarding and risk checks. A SaaS procurement suite is assumed.
- **Modules:**
  - Buying Channel: guided buying and catalogues.
  - Procurement API.
  - Supplier Onboarding Workflow: tax IDs, bank details, risk and sanctions checks.
  - Supplier and Contract Store.
  - Procurement Suite Adapter.
- **Dependencies:** coam (coding); apin (POs feed invoice matching).
- **SoR:** Supplier Master and Contract.

**`apin` Accounts Payable and E-Invoice Automation** (full-stack, sustaining)
- **Purpose.** Captures supplier invoices (PDF, Peppol, clearance models), runs two- and three-way matching, routes exceptions and schedules payment runs. EU ViDA e-invoicing is a named complexity risk.
- **Modules:**
  - Invoice Exception Inbox.
  - Payables API.
  - Invoice Capture Consumer, including OCR.
  - Invoice Matching Service: tolerances and tax checks.
  - Payables Ledger Store.
  - E-Invoice Network Adapter.
- **Dependencies:** s2pp; itax (input VAT); bnkc; glco.
- **SoR:** AP Invoice and Payment.

#### Tax and Treasury

**`itax` Indirect Tax Determination and Reporting** (service, invest)
- **Purpose.** Determines VAT/GST on commissions and merchant sales, **digital services taxes** (1.5–10% of in-jurisdiction revenue) and travel transaction taxes. It prepares returns and platform reporting such as EU DAC7. The modeled company carried a $337M accrual for one country's indirect-tax matters in one year and $89M of other indirect-tax expense the next. The tax engine vendor is assumed.
- **Modules:**
  - Tax Determination API: real-time and batch.
  - Returns and Platform Reporting Job: VAT, DST and DAC7.
  - Tax Rules Engine: jurisdiction, product, model and party rules.
  - Tax Determination Record Store: **every determination with its inputs, rule version and result**, for audit.
  - Tax Authority Filing Adapter.
- **Dependencies:** entm (registrations and establishments); fdbx (aggregates for DST and DAC7); glco (tax-account reconciliation).
- **SoR:** Indirect Tax Determination Record.

**`gtax` Tax Provision and Global Minimum Tax** (service, invest)
- **Purpose.** The quarterly and annual income-tax provision under US GAAP, plus OECD Pillar Two (GloBE) calculations, built from ledger, entity and payroll data.
- **Modules:**
  - Tax Provision Workbench.
  - Tax Provision API: ETR per jurisdiction.
  - Tax Data Collection Job.
  - Provision and Pillar Two Dataset: versioned, with evidence.
- **Dependencies:** glco (trial balances); entm; cnsl (provision feeds the consolidated statements).
- **SoR:** Tax Provision and Pillar Two Dataset.

**`trcm` Treasury, Cash and FX Hedge Management** (full-stack, sustaining)
- **Purpose.** Daily global cash positioning, liquidity forecasting, FX exposure capture and hedge management (derivatives plus EUR-denominated debt). The TMS vendor is assumed.
- **Modules:**
  - Treasury Dashboard.
  - Treasury API.
  - Cash Positioning Job: intraday and end-of-day.
  - Exposure and Hedge Service: exposures, designations, confirmations.
  - Treasury Position Store.
  - TMS Adapter.
- **Dependencies:** bnkc; entm; tfnd (traveler funds in the liquidity view); glco (hedge-accounting entries).
- **SoR:** Cash Position and FX Exposure.

### 1.4 Close, Reporting and Controls

#### Close and Consolidation

**`clse` Close Orchestration and Account Reconciliation** (full-stack, invest; modeled on a BlackLine-type close SaaS, assumed)
- **Purpose.** Runs the month-end and quarter-end close calendar across all entities and brands:
  - task lists with owners and deadlines;
  - balance-sheet reconciliations;
  - **subledger-to-GL tie-outs**;
  - journal-entry review and certification.
- **Modules:**
  - Close Workspace.
  - Close and Reconciliation API.
  - Balance and Subledger Loader: GL trial balances, subledger totals, PSP settlement totals and bank balances.
  - Auto-Match and Variance Engine: rules, thresholds and proposed explanations.
  - Close Task and Reconciliation Store: preparer/reviewer sign-offs.
  - Close SaaS Adapter: also posts reconciling journals back to the ledger.
- **Dependencies:** glco; brim; psrc (settlement reconciliation as supporting evidence); ctlm (control: certifications become SOX evidence).
- **SoR:** Account Reconciliation and Close Task.

**`cnsl` Consolidation and External Reporting** (service, invest; modeled on a OneStream-type consolidation SaaS, assumed)
- **Purpose.** Consolidates entity ledgers into group results under US GAAP:
  - currency translation;
  - intercompany elimination;
  - segment and brand views;
  - the disclosure data behind the annual and quarterly reports (merchant, agency and advertising revenue lines; deferred merchant bookings).
- **Modules:**
  - Consolidation API.
  - Disclosure and Reporting Console: top-side adjustments and tie-outs.
  - Consolidation Run Orchestrator.
  - Consolidation Engine and Cube: entity, account, brand and segment.
  - Consolidation SaaS Adapter: SAP and the disclosure-management tool.
- **Dependencies:** glco; entm; clse (control: **consolidation starts only when close certifications are complete**); rrec (revenue disaggregation).
- **SoR:** Consolidated Financial Statement. External: the SEC EDGAR filing agent (XBRL), investor relations and the auditor.

**`fpna` Planning, Forecasting and Performance Management** (full-stack, sustaining)
- **Purpose.** The annual plan, rolling forecasts and scenarios by brand, segment and cost centre. Revenue forecasts are **driver-based**: room nights, gross bookings, take rate, merchant mix. The brick also tracks transformation savings. It shares the dimensional model with consolidation.
- **Modules:** Planning Workspace; Plan and Forecast API; Actuals and Driver Loader; Planning Model Store.
- **Dependencies:** cnsl; fdbx; fmet (governed metric definitions).
- **SoR:** Plan and Forecast Dataset.

#### Controls and Regulatory Compliance

**`sodc` Access Governance and Segregation of Duties** (service, sustaining)
- **Purpose.** Role design, access requests, periodic access reviews, SoD rulesets and **firefighter (emergency) access logging** for SAP and connected finance applications. This is the ITGC evidence base for SOX 404.
- **Modules:**
  - Access and SoD API: checks proposed assignments *and system designs*.
  - Access Review Console.
  - Role and Usage Collector.
  - Ruleset and Access Register: conflicts and mitigating controls.
  - Identity and GRC Adapter: IdP via SCIM/SAML, plus SAP GRC.
- **Dependencies:** ctlm; glco; stdg (governance: mandatory access/SoD standards).
- **SoR:** User Access and SoD Ruleset.

**`ctlm` Control Monitoring and Audit Evidence** (full-stack, invest)
- **Purpose.** The single register of SOX key controls mapped to processes, systems and risks. It runs automated control monitoring and covers evidence collection, the testing workflow and deficiency tracking for management's ICFR assessment.
- **Modules:**
  - Controls Workspace.
  - Control and Evidence API.
  - Automated Control Monitor: config changes, journal thresholds, interface completeness.
  - Control and Evidence Register: RCM, test plans, evidence, deficiencies.
- **Dependencies:** sodc; clse; glco (manual journals, config changes); **adrr (governance: decisions that change controlled systems trigger a control impact assessment)**.
- **SoR:** SOX Control and Evidence Record. External: the auditor's evidence portal and audit committee reporting.

**`regr` E-Money Safeguarding and Regulatory Reporting** (service, invest)
- **Purpose.** Calculates and evidences **daily safeguarding** of customer funds held by the licensed e-money institutions (one is licensed by a national central bank in the EU). It also produces prudential and regulatory returns and prepares for PSD3/PSR.
- **Modules:**
  - Safeguarding and Returns API.
  - Regulatory Reporting Console.
  - Daily Safeguarding Calculator: relevant funds per entity from subledger balances, compared with safeguarded bank balances.
  - Safeguarding Position Store: shortfalls, reconciliations, return versions.
  - Regulator Submission Adapter.
- **Dependencies:** tfnd; trcm (safeguarding account balances); entm (licence attributes); ctlm.
- **SoR:** Safeguarded Funds Position.

### 1.5 Finance Data and Integration Platform

#### Integration

**`fint` Finance Integration Hub** (integration, invest)
- **Purpose.** The governed event, API and file backbone between brand booking platforms, the payments platform and the finance core. It:
  - receives booking, cancellation and modification events;
  - **validates them against the canonical financial event contract**;
  - enriches them with entity and account-derivation keys;
  - **guarantees complete, exactly-once delivery** to the subledger, with **control totals per source**.
- **Modules:**
  - Financial Event Intake API: sync and batch.
  - Financial Event Stream: durable, partitioned, **with replay**.
  - Subledger Router: idempotency keys and retries.
  - Contract Validator and Enricher.
  - **Delivery Ledger and Control Totals**: per-source, per-day counts and amounts received, rejected, delivered and replayed.
  - File and Batch Gateway: managed file transfer for bank, PSP and vendor batches.
- **Dependencies:** brim; coam; fdbx; stdg (enforces the canonical event standard).
- **SoR:** Booking Financial Event. Runtime: a Kafka-class platform (assumed). The brand booking platforms and the payments platform publish into it.

**`bonb` Brand Finance Adapter Kit** (development, invest)
- **Purpose.** Reusable SDKs, mapping templates, test harnesses and an onboarding playbook. With them a brand or a newly acquired business can publish canonical events and map its local chart to the global core **without bespoke point-to-point integrations**. It is "the main lever for converging disparate brand finance stacks."
- **Modules:**
  - Brand Onboarding Portal: go-live checklist.
  - Onboarding API.
  - **Contract Certification Runner**: replays sample brand events through validation and a posting simulation.
  - Mapping and Onboarding Register.
  - Brand Event SDK: client libraries in brand languages, with idempotency and control totals.
- **Dependencies:** fint; coam; stdg; tsrm (reports onboarding progress against the target state).

#### Finance Data

**`fdbx` Finance Data Platform** (service, invest; "FinDB" in the model, assumed)
- **Purpose.** Curated analytical finance data: **booking-to-ledger lineage**, subledger detail, payments and settlement, tax and close data. Datasets are governed and access-controlled for analytics, **audit sampling** and planning.
- **Modules:**
  - Finance Dataset API: row-level entity and brand security.
  - Finance Ingestion Pipelines.
  - **Data Quality and Lineage Checker**: completeness, balance and lineage between source events, subledger and ledger.
  - Curated Finance Lakehouse: raw, conformed and curated layers.
  - SAP and SaaS Extractor: CDC.
- **SoR:** Finance Analytical Dataset.

**`fmet` Finance Metrics and Management Reporting** (full-stack, sustaining)
- **Purpose.** Governed definitions and dashboards (gross bookings, take rate, merchant mix, close days, cost-to-serve) so that brand, corporate and board reporting use **one definition per number**.
- **Modules:** Management Dashboards; Metric Definition and Query API; Metric Catalogue (owners, logic, versions).
- **Dependencies:** fdbx; cnsl (management metrics reconcile to reported results).
- **SoR:** Finance Metric Definition.

### 1.6 Architecture Governance and Portfolio

**`adrr` Architecture Decision Records and Review Board** (full-stack, invest)
- **Purpose.** Workflow and register for architecture decisions:
  - intake of business drivers;
  - **BITS requirements** (business, information, technical, solution);
  - options with cost-benefit and risk analysis for (S)VP audiences;
  - review-board scheduling;
  - the head of architecture's final decision rights on mandatory global standards;
  - follow-up of decision outcomes.

  It targets decision velocity and fewer unresolved cross-programme dependencies.
- **Modules:**
  - Decision Workspace.
  - Decision Register API: links decisions to changes and controls.
  - Decision SLA Monitor: escalates.
  - **Review Board Workflow**: routes by materiality to team level, architecture board or senior-director decision rights.
  - Decision Record Store: context, BITS, options, decision, rationale, consequences, **review dates**.
- **Dependencies:** stdg; apmx; tsrm; ctlm (decisions on SOX-relevant systems trigger a control impact assessment).

**`stdg` Standards, Patterns and Conformance Checks** (service, invest)
- **Purpose.** The catalogue of mandatory global standards and reusable patterns:
  - canonical financial events;
  - **idempotent posting**;
  - **subledger-to-GL reconciliation**;
  - **clean-core SAP extension**;
  - **SoD-by-design**;
  - data residency;
  - resilience tiers.

  It runs automated and attested conformance checks, and manages **waivers with expiry**.
- **Modules:**
  - Standards and Conformance API.
  - Standards Catalogue Console.
  - **Conformance Scanner**: interface contracts, SAP custom-code clean-core rules (ATC), resilience-tier tags; integrated with CI.
  - Standards and Waiver Register.
- **Dependencies:** apmx; adrr (standards are approved through decision records); ctlm (SOX-relevant breaches feed control monitoring).

**`apmx` Application Portfolio and Technology ROI** (full-stack, sustaining)
- **Purpose.** The inventory of enterprise and finance applications across brands, with:
  - ownership, lifecycle and capability mapping;
  - run cost, licence and contract data;
  - risk (SOX relevance, vendor end of support);
  - **programme value cases (baseline vs realised)**;
  - a target-state disposition per application (tolerate / invest / migrate / eliminate).
- **Modules:**
  - Portfolio Explorer: duplication heat-maps.
  - Portfolio API.
  - Cost and Contract Loader: cloud, licence and contract costs.
  - Portfolio and Value Register.
  - EA Tool Adapter: LeanIX-class tooling, optional.
- **Dependencies:** s2pp (software contracts); fpna (programme budgets and savings baselines); tsrm.

**`tsrm` Target-State Architecture and Dependency Map** (service, invest)
- **Purpose.** Versioned current, transition ("plateau") and target-state architectures, with cross-programme and cross-brand dependency maps. The aim is to make ambiguity and unresolved dependencies visible and owned on the biggest initiatives (ERP convergence, merchant growth, brand onboarding).
- **Modules:**
  - Target-State API.
  - Architecture Modeling Console.
  - **Dependency Risk Analyzer**: unresolved, circular or late dependencies.
  - Architecture State Repository.
- **Dependencies:** apmx; adrr (**unresolved dependencies become decision requests**); bonb.

### 1.7 Cross-cutting architectural patterns embedded in the bricks

- **Detail in the subledger, summaries in the GL**, with reconciliation keys so every summary is traceable.
- A **canonical financial event contract**, validated at one hub, with idempotency, replay, exactly-once delivery and **per-source control totals**. Completeness is a control in its own right.
- **Three-way match:** booking ↔ payment/PSP settlement ↔ bank.
- **Per-booking liability ledger** for customer funds, linked to regulated-entity safeguarding.
- **A shared payment factory** for all outbound money, with dual approval, sanctions screening and change-controlled beneficiary data.
- **A central tax engine** that records each determination with its rule version.
- **Close gating:** consolidation does not start until close certifications are complete.
- **Controls designed in:** SoD checked at design time, decisions carry SOX impact, and standards breaches feed control monitoring.
- **Clean core:** extensions sit outside the ERP behind APIs, enforced by code inspection in CI.
- **Governance as product:** ADRs, standards with expiring waivers, a portfolio with value tracking, and a target state with a dependency analyser.

---

## 2. Product streams, roadmap themes and the strategic spine

### 2.1 Twelve outcome-based streams (four groups)

Each stream has its outcomes, the bricks it composes, and a stepwise flow. Every step names its key facts, its pain points and the bricks that carry it.

**A. Order-to-Cash and Money Movement**

1. **Merchant Booking to Recognised Revenue** (fint, pevt, brim, rrec, tfnd, psrc, glco). This is now the dominant flow.
   - *Outcomes:* every merchant booking is traceable from payment to revenue; deferred merchant bookings reconcile to the subledger at every close; revenue is recognised at the right time and on the right basis.
   - *Steps:*
     1. Publish the booking as a canonical event carrying brand, entity, currency, partner and model. Pains: per-brand file formats; late or duplicate events break counts.
     2. Capture the payment and its settlement. Pains: each PSP or APM reports fees, FX and timing differently; settlement lags capture by days.
     3. Post to the contract-account subledger and record the DMB liability. Pains: volume grows with room nights; mapping errors surface only at summarisation.
     4. Recognise revenue on performance, at check-in or travel date and **net where agent**. Note that *cancellations reverse the liability rather than revenue*. Pains: the principal/agent judgement differs by product (stays, flights, cars); policy changes need re-runs across open bookings.
     5. Three-way reconcile, with fees and FX split to the right accounts. Pains: unmatched items age into write-offs; manual break handling during close.
     6. Summarise to the GL and prove completeness. Pain: subledger-to-GL differences found late.

2. **Agency Commission Invoice to Cash** (fint, brim, pinv, itax, psrc, glco).
   - *Outcomes:* complete and correct invoices; fewer disputes; receivables reconcile.
   - *Steps:*
     1. Accrue commission on stayed bookings. No-shows and cancellations adjust the base; partners mark no-shows late.
     2. Determine VAT, which depends on partner location and business status. Missing or invalid VAT IDs and varying e-invoicing mandates cause problems.
     3. Issue the periodic invoice with booking-level detail, visible in the partner extranet. Disputes arise when stay data differ.
     4. Collect by direct debit or bank transfer, dun overdue items, and **net against merchant payouts** where possible. Small balances are costly to chase and payment references are often missing.
     5. Clear receivables, summarise to the GL and feed bad-debt reserves from aging. Unapplied cash distorts aging.

3. **Partner Payout On Time and Accurate** (pout, bnkc, tfnd, brim, trcm, regr).
   - *Steps:*
     1. Calculate the net payout: gross minus commission and payment fees, with timing commonly tied to check-in. Pains: bank details change often; adjustments arrive after payout.
     2. Fund the run from the right entity and currency. Treasury tops up and hedges, and the **safeguarding check runs before client funds are released**.
     3. Pay by bank transfer (H2H/SWIFT) or virtual card. Pains: invalid details; country cut-offs.
     4. Confirm and clear partner payables. Returned payments are re-queued, and often age without owners.
     5. Report safeguarded funds, reconciled daily. Pain: different regulators and templates per entity.

4. **Refund and Chargeback to Ledger** (cbkf, pevt, brim, rrec, psrc).
   - *Steps:*
     1. Receive the refund instruction or chargeback notification. Reason codes differ by scheme and method, and notices often arrive after the stay.
     2. Link to the original booking, payment and payout: has the partner already been paid? Links go missing on modified bookings.
     3. Decide liability (traveler, partner or brand) and represent where justified. Evidence deadlines are short.
     4. Account. A refund reverses the deferred liability *or* revenue; losses and scheme fees are booked separately; reversal rules differ for merchant and agency.
     5. Reconcile chargeback debits to cases. **PSP netting hides individual debits.**

**B. Enterprise Operations**

5. **Procure to Pay a Supplier** (s2pp, apin, itax, bnkc, coam).
   - *Outcomes:* more spend on contract; touchless invoices; no duplicate or fraudulent payments.
   - *Steps:* guided intake, coded to the global CoA (slow intake drives off-contract buying) → source and onboard with sanctions, tax and bank checks (duplicate suppliers across brands) → PO and receipt (services rarely receipted on time) → capture and match, with tax validated (format proliferation from e-invoicing mandates) → payment run per entity and currency (**changed supplier bank details are a fraud vector**).

6. **Indirect Tax Determination to Filing** (itax, gtax, brim, fdbx, entm).
   - *Steps:* determine at transaction time, with different tax bases for merchant and agency (rules change often; location evidence is incomplete) → post tax lines with jurisdiction and rate (entity/jurisdiction mismatch) → aggregate and reconcile to the ledger before filing, since DST and DAC7 need revenue and partner data by jurisdiction → file VAT, DST and DAC7 with an audit trail → feed exposures into the provision and Pillar Two. A key pain: "**disputes and audits outlast the systems that created the data.**"

7. **Cash Positioning and FX Hedging** (trcm, bnkc, entm, regr, fdbx).
   - *Steps:* collect statements, intraday where available (smaller banks are often missing) → **separate safeguarded from operating cash** → forecast from payouts and receipts, using DMB as a leading indicator of future payouts (accuracy drops in peak season) → compute exposure and hedge within policy (exposure data assembled from spreadsheets) → hedge accounting and revaluation (ineffective hedges discovered late).

**C. Record-to-Report and Assurance**

8. **Record-to-Report Month-End Close** (clse, glco, entm, brim, cnsl, ctlm).
   - *Steps:* cut off and summarise subledgers → accruals and adjustments ("**manual journals are the largest error source**") → reconcile balance-sheet accounts by risk rating, with subledger-to-GL proofs → IC matching and FX revaluation → consolidate, with flux review by brand.

9. **Quarterly SEC Reporting and SOX Attestation** (cnsl, ctlm, sodc, clse, fmet).
   - *Steps:* draft statements and disclosures → test key controls (automated controls are tested once per change) → access reviews ("reviewers rubber-stamp large lists") → package evidence (repeated requests) → sub-certifications from brands and functions, then the CEO/CFO certification.

10. **Plan, Forecast and Review Performance** (fpna, fdbx, fmet, cnsl).
    - *Steps:* load actuals (restated after load) → driver plans built on room nights, ADR, take rate and marketing (driver definitions differ by brand) → monthly reforecast and FX/demand scenarios (shadow spreadsheets) → reviews on shared dashboards ("debates about whose number is right").

**D. Platform Evolution and Governance**

11. **Onboard a Brand onto the Global Finance Core** (bonb, fint, coam, glco, brim, tsrm, stdg).
    - *Flow:* assess → decide → map → integrate → **parallel-run for at least one close** → cut over and decommission with an archive.
    - *Pains:* inventories are out of date; local reporting needs drive exceptions; matrixed brand teams have their own roadmaps; parallel-run differences are hard to explain; "**legacy kept alive for reporting**."

12. **Govern an Architecture Decision to Conformance** (adrr, stdg, apmx, tsrm, sodc).
    - *Steps:* intake and triage by impact (SOX, regulatory, cost, cross-brand; pain: unclear who decides) → options using reusable patterns, portfolio cost data and the BITS view (pain: options lack cost data) → control and SoD impact (pain: discovered after go-live) → decide and record, with decision rights, board SLAs and **rationale plus expiry** (pain: decisions made in meetings and never recorded) → conformance checks at design and release, with **time-boxed exceptions** (pain: exceptions become permanent).

### 2.2 The strategic spine (domain level)

- **Year 1, govern and stabilise.**
  - Raise decision velocity with one decision record, a review board and mandatory standards.
  - Make payments-to-ledger complete for cards and APMs.
  - Publish the financial-systems target state and a portfolio ROI baseline.
- **Year 3, one global finance core.**
  - Converge brand ledgers and settlement onto the ERP core (central-finance hub, clean core) through the adapter kit and canonical financial events.
  - Run tax determination and e-invoicing as shared services.
  - Retire bespoke brand finance stacks.
- **Year 5, continuous, real-time finance.**
  - Continuous close.
  - AI-assisted reconciliation and controls with auditable evidence.
  - Real-time cash and liability views.
  - New brands and markets onboarded as configuration.

### 2.3 Per-persona product strategy (Year 1 / 3 / 5 themes and milestones)

| Persona | Vision | Y1 theme and milestones | Y3 theme and milestones | Y5 theme and milestones |
| --- | --- | --- | --- | --- |
| Finance leadership | One trusted, timely global view; the estate gets simpler and cheaper every year without weakening controls | *Transparent portfolio, governed investment*: portfolio baseline; target-state map; decision records mandatory above a threshold | *Converged finance core*: all brands on the global CoA; shared S2P; four-day close | *Continuous accounting and self-service insight*: daily soft close; governed metric layer; spreadsheet key controls retired |
| Technology leadership | Architecture is the fastest route to a good platform decision | *Decision service and portfolio baseline*: review board with published decision rights; ADR repository; app inventory | *Self-service standards and convergence*: conformance checks in pipelines; target state per capability; adapter kit used by every brand | *Value-steered architecture*: benefits dashboards linked to decisions; post-implementation reviews standard; portfolio under 200 apps |
| Controller | The close becomes a short confirmation of numbers already reconciled | *Reconciled subledger backbone*: daily SL-to-GL reconciliation for flagship merchant flows; close cockpit; posting rules version-controlled | *One subledger for all brands*: remaining brands on it; revenue rules for every payment method; four-day close | *Continuous accounting*: intraday SL postings; continuous IC matching; three-day close |
| Tax and treasury | Tax determined once by one engine; every currency and account visible each morning | *One tax engine, one cash position*: flagship EU VAT on the shared engine; daily cash position by 09:00 CET; DST base from ledger data | *Rules as configuration*: all brands on the tax service; ViDA readiness; Pillar Two dataset from entity ledgers | *Continuous tax and treasury*: near real-time e-reporting; automated hedge proposals; audit portal with lineage |
| Partner settlement | One platform settles every partner correctly, on time, explainably | *Reliable payouts*: bank-detail change controls with step-up checks; single exception queue; two brands on shared payouts | *Shared partner O2C*: booking reference on every invoice line; net settlement of commission against payouts; local payout rails in top markets | *Partner-explainable settlement*: partner statement API matching the ledger; payout method choice; predictive dispute prevention |
| Procurement and AP | Negotiate savings once, realise them everywhere | *One buying channel*: shared supplier master with tax and bank validation; guided buying; spend analytics | *Touchless payables*: EU e-invoicing readiness; all brands on the suite; contract-price invoice validation | *Autonomous S2P*: policy auto-approval; dynamic discounting; continuous supplier risk monitoring |
| SOX and controls | Controls are a property of the architecture | *Controls visible in the architecture*: control register mapped to the portfolio; SOX section mandatory in ADRs; evidence hub for close | *Continuous control monitoring*: 50% of key controls tested by monitoring; completeness controls on all brand feeds; auditor reliance on automated controls | *Controls as code*: control patterns in pipelines; new entities inherit controls; no repeat findings |
| Brand finance engineering | Brands plug in via versioned contracts; brand engineers build travel products, not ledgers | *Contracts before code*: canonical event schema v1; adapter kit with harness; decision SLA for brands | *Brands on one core*: more brands on the shared SL; all entities on the global CoA; contract versioning enforced in CI | *Self-service onboarding*: acquisition onboarded within a quarter; no brand-local ledgers; adapter kit run as inner source |
| Payments platform | One payments-to-ledger contract; every cent reconciles daily | *One P2L record*: all PSPs ingested automatically; daily three-way match published to the close; break queue with owners | *Finance-ready by design*: standard accounting patterns for card and APM; readiness gate in the launch process; PSD3/PSR absorbed in contracts | *Real-time money visibility*: intraday reconciliation; cross-brand FX netting; fee validation for every PSP contract |

---

## 3. Data assets

### 3.1 Physical stores (12)

| Store | Kind | Technology (status) | Classification |
| --- | --- | --- | --- |
| ERP finance DB | operational DB | S/4HANA universal journal and master data on HANA, private cloud (RISE assumed) | restricted |
| Contract-accounting store | operational DB | FI-CA/BRIM tables on HANA | restricted |
| Finance event streams | event stream | managed Kafka-compatible topics (booking-financial, payment-settlement, payout, tax) | confidential |
| Finance lakehouse | analytical | cloud lakehouse or warehouse (name assumed) | confidential |
| Payments-to-ledger operational DB | operational DB | relational: normalised payments, settlement files, match results, disputes | restricted |
| Partner settlement DB | operational DB | relational **with field-level encryption**: invoices, payouts, tokenised bank details | restricted |
| Treasury management system | SaaS tenant | TMS (vendor not disclosed) | restricted |
| Close and consolidation SaaS | SaaS tenants | close/recon tenant plus consolidation/planning tenant (assumed BlackLine, OneStream) | restricted |
| Source-to-pay SaaS | SaaS tenant | procurement suite integrated with ERP AP | confidential |
| GRC and controls repository | operational DB | SAP GRC plus a controls repository | restricted |
| Finance document archive | object store | **immutable WORM with retention lock**: invoices, statements, filings, evidence packs | restricted |
| Architecture repository | operational DB | EA tool plus docs-as-code | internal |

### 3.2 Canonical data assets (24), with system of record and lineage

Format: asset, then kind and system-of-record brick, then business meaning, then derived-from, legal tags, retention and key governance. Residency is EU for all of them.

**Ledger and master data**
- **General Ledger Journal**: transactional; SoR glco. *"The book of record for every reported number."*
  - Derived from: the subledger postings, revenue schedules and AP.
  - Legal and governance: SOX and statutory; 10-year retention; finance and auditors only, via SoD-checked roles.
  - Interfaces: a posting API (validated, balanced postings) and a `journal-posted` event.
- **Chart of Accounts and Financial Master Data**: reference; SoR coam. *"The shared vocabulary that makes brand numbers comparable."*
  - Changes only via the governed workflow; a `master-data-changed` event.
  - Retention: life of the entity plus 10 years.
- **Legal Entity and Intercompany Register**: reference; SoR entm. *"Who owes whom inside the group, in which currency."*
  - Legal tags: SOX, transfer pricing.

**Order-to-cash and revenue**
- **Booking Financial Event**: an event; SoR fint. *"The single finance contract every brand emits."*
  - Lifecycle states: created / modified / cancelled / stayed.
  - Carries amounts, currencies, merchant/agency model, entity, partner and tax attributes.
  - Interfaces: a versioned event schema, plus a **fallback batch file** for brands not yet event-enabled.
  - Governance: GDPR (traveler and partner data); 7 years after the stay date; **traveler identifiers pseudonymised after 24 months**.
- **Contract-Account Subledger Posting**: transactional; SoR brim; derived from booking events and payments. *"The open-item truth behind each partner and payment balance."* Emits `subledger-summarised`. 10 years.
- **Revenue Recognition Schedule**: derived; SoR rrec; derived from booking events and subledger postings. Per-booking performance obligations, gross/net and merchant/agency treatment, recognition dates, cancellation reversals. Legal: SOX, ASC 606. Emits a daily `revenue-recognised` event.
- **Deferred Merchant Bookings Balance**: derived; SoR tfnd; derived from booking events and payments. Held by entity, currency and expected recognition date, with refund exposure. Legal: SOX, EMD2. Roll-forward API.

**Payments and settlement**
- **Payment Transaction and Settlement Record**: transactional; SoR pevt. Captures, refunds, fees, interchange and settlement-batch lines.
  - **Card data is tokenised: network tokens and last four digits only; no PAN in finance systems.**
  - Legal: PCI DSS, GDPR, PSD2, SOX. Raw PSP files are ingested daily and a `payment-settled` event is emitted.
- **Reconciliation Match Result**: derived; SoR psrc; derived from booking, payment and subledger records. *"Proof that every payment reached the ledger."* Emits `break-raised`. 7 years.
- **Chargeback and Refund Case**: SoR cbkf. Scheme reason codes and liability allocation between company and partner. *"Who bears each lost or returned payment."*

**Partner settlement**
- **Partner Commission Invoice**: SoR pinv; derived from booking events and tax determinations. Monthly, with lines per stay. Legal: VAT; 10 years; statutory e-invoice formats.
- **Partner Payout Instruction**: SoR pout. Net amount, currency, method, value date, status; emits `payout-status-changed`. Legal: PSD2, EMD2.
- **Partner Bank and Payout Details**: master data; SoR pout. **Sensitive.** Beneficiary accounts, verification status and DAC7 seller identifiers. Field-level encrypted; *"the most fraud-sensitive partner data"*; every change is audited and dual-verified. Legal: GDPR, DAC7, AML.

**Enterprise operations**
- **Supplier Master and Contract**: SoR s2pp; replicated to the ERP.
- **AP Invoice and Payment**: SoR apin; held in the ERP, with the procurement SaaS as the capture point; e-invoicing tags.
- **Indirect Tax Determination Record**: SoR itax. Per-transaction jurisdiction, **rule version**, basis and evidence; DAC7 extracts. Retained for 10 years or the local statute, whichever is longer.
- **Tax Provision and Pillar Two Dataset**: SoR gtax; held in the lakehouse; derived from the GL and the entity register.
- **Cash Position and FX Exposure**: SoR trcm; derived from payouts, DMB and AP. Legal: EMIR.

**Close, reporting and controls**
- **Account Reconciliation and Close Task**: SoR clse; derived from the GL and match results. *"Proof each balance was checked before results are released."*
- **Consolidated Financial Statement**: SoR cnsl. XBRL tagging; **MNPI until filed, with insider-list controls**; permanent retention.
- **Plan and Forecast Dataset**: SoR fpna. MNPI.
- **User Access and SoD Ruleset**: SoR sodc. Employee personal data; firefighter access; certifications.
- **SOX Control and Evidence Record**: SoR ctlm; derived from access and reconciliation records.
- **Safeguarded Funds Position**: regulatory; SoR regr; derived from DMB and cash positions. Daily relevant-funds calculation and safeguarding-account reconciliation. Retained per licence conditions, minimum 5 years.

**Analytics and architecture**
- **Finance Analytical Dataset**: SoR fdbx; derived from the GL, booking events and payments. Ledger-tied, transaction-grain data; pseudonymised; **MNPI fenced before results release**.
- **Finance Metric Definition**: SoR fmet. *"One definition per number"*, with lineage.
- **Architecture Decision Record**: SoR adrr; permanent; *"shared with auditors when a control relies on it."*
- **Architecture Standard and Pattern**: SoR stdg; derived from ADRs; SOX-tagged; machine-checkable rules.
- **Application Portfolio Inventory**: SoR apmx. Owner, lifecycle, cost, SOX relevance and disposition (tolerate / invest / migrate / eliminate).

### 3.3 Canonical events and interfaces named in the model

`booking-financial-event` (versioned per lifecycle change), `payment-settled`, `subledger-summarised`, `revenue-recognised`, `journal-posted`, `master-data-changed`, `break-raised` and `payout-status-changed`.

File interfaces: PSP settlement files, brand batch extracts (fallback), bank statements (MT940/camt.053), payment files (pain.001), e-invoices (Peppol and clearance), tax return extracts, regulatory returns, provision workpapers and consolidation packs.

### 3.4 Main data flow (lineage spine)

1. A brand booking platform emits a booking financial event to the integration hub, which validates, enriches, applies control totals and sends it on to the subledger and the lakehouse.
2. The payments platform and PSP files feed payment normalisation, which produces the payment record. That record goes to the subledger for clearing and to reconciliation.
3. The subledger feeds the revenue schedule and the DMB balance. The DMB balance feeds safeguarding and treasury.
4. The subledger summarises to the GL. The GL feeds close reconciliation, then consolidation, then the disclosures.
5. Evidence from close, access and reconciliation flows into the control register.
6. GL, events and payments flow into the analytical dataset, which feeds metrics, tax aggregates (DST/DAC7) and planning drivers.

### 3.5 Ownership and governance themes

Every asset has exactly one system-of-record brick. Classification, legal tags, security criticality and access scope are explicit. Critical assets are:
- the GL;
- the subledger;
- the revenue schedule;
- DMB;
- payments;
- payout instructions;
- partner bank details;
- cash and FX;
- access/SoD;
- the consolidated statements;
- safeguarding.

Retention is mostly 10 years (statutory/SOX/tax) or 7 years for operational records. Filed statements, ADRs and standards are kept permanently.

---

## 4. Deployments and products: which platform plays which role

### 4.1 Ten internal products (bundles of bricks)

| Product | Bricks | Primary customers |
| --- | --- | --- |
| Global Finance Core | glco, coam, entm | finance leadership, controller |
| Subledger and Revenue Platform | brim, rrec, tfnd | controller, payments |
| Payments-to-Ledger Service | pevt, psrc, cbkf | payments, controller |
| Partner Settlement Platform | pinv, pout, bnkc | settlement ops, tax/treasury |
| Source-to-Pay Suite | s2pp, apin (+ bnkc) | procurement/AP |
| Tax and Treasury Systems | itax, gtax, trcm (+ bnkc) | tax/treasury |
| Close, Consolidation and Reporting Workbench | clse, cnsl, fpna | controller, finance leadership |
| Controls and Regulatory Compliance Hub | sodc, ctlm, regr | SOX lead, payments |
| Finance Data and Integration Platform | fint, bonb, fdbx, fmet | brand finance engineering, finance leadership, payments |
| Architecture Governance Service | adrr, stdg, apmx, tsrm | technology leadership, brand finance engineering, SOX lead |

### 4.2 Runtime channels: the coexistence pattern

- **ERP runtime: S/4HANA private cloud (RISE assumed).** Hosts glco, coam, entm, brim, rrec, tfnd, itax, gtax, trcm and sodc. These are deployed as SAP configuration, custom code and integration content, alongside the FI-CA/BRIM and GRC instances with central-finance replication. *Tax, treasury and access governance are modeled as running in or against the SAP landscape, even though external TMS and tax engines are assumed as vendors.*
- **Internal cloud platform (Kubernetes).** Hosts pevt, psrc, cbkf, pinv, pout, bnkc, fint, bonb, ctlm, regr, adrr, stdg, apmx and tsrm as containerised services, workers and APIs. **Payments-to-ledger, partner settlement, the integration hub, regulatory reporting and the governance tools are custom-built** around the ERP.
- **Finance data platform (lakehouse).** Hosts fdbx and fmet, plus the matching jobs of psrc, which runs in both channels.
- **Vendor SaaS tenants.** Host clse and cnsl (close and consolidation, i.e. BlackLine/OneStream-type), fpna (planning) and s2pp/apin (source-to-pay).
- **Finance workspace.** An internal finance portal plus the SAP Fiori launchpad, with SSO and role-based UIs (payout, dispute, AP, close, planning, controls, ADR, portfolio and metrics consoles).

**Vendor role mapping as modeled.**
- **SAP S/4HANA plus Central Finance.** Global GL and hub. **FI-CA/BRIM** is the high-volume subledger and convergent invoicing; SAP revenue accounting is assumed for schedule posting; **SAP MDG** (assumed) handles master data; **SAP GRC** handles access control; **ATC** does clean-core checks.
- **BlackLine-class** close/reconciliation SaaS sits beside the ERP GL (assumed).
- **OneStream-class** consolidation, reporting and planning SaaS (assumed).
- **Oracle Fusion / NetSuite** are alternative finance cores, often found in acquired or smaller brands, and serve as a renewal benchmark.
- **Workday** is a contender for adjacent slots (HCM, spend, planning) and an alternative core for greenfield or acquired entities.
- **Adyen / Stripe** are PSP categories whose settlement reports, fees and dispute data feed payments-to-ledger. Stripe is also positioned as an *API-first finance tooling reference* (billing, revenue recognition and treasury APIs) that challenges ERP-centric subledger designs.
- **Custom builds** cover the integration hub, payments normalisation, reconciliation, payouts, safeguarding, the adapter kit and the governance tools.
- **Other categories:** Kafka-class streaming, a cloud lakehouse, a BI semantic layer, a LeanIX-class EA tool, a TMS, a tax-content engine, a virtual-card issuer, a sanctions-screening service, a market-data FX feed, and supplier-risk data.

**Coexistence patterns visible in the model.**
1. **Central Finance as a bridge.** Non-converged brand and legacy ERPs replicate into the central ledger while convergence proceeds. Replication failures are monitored and reprocessed.
2. **ERP core plus specialist SaaS** for close, consolidation, planning and S2P, connected by adapters, with reconciling journals posted back to the ERP.
3. **Custom high-volume edge** (events, payments, matching, payouts) feeding the ERP subledger through idempotent, control-totalled contracts.
4. **Clean core.** Extensions are kept out of the ERP behind APIs.
5. **Parallel runs** of at least one or two closes before cutover, plus fallback batch files for brands that are not yet event-enabled.

---

## 5. Customers and stakeholders (generalised roles)

The model has nine personas in five groups, each with cares, wins, fears, jobs-to-be-done, a journey story and two KPI pyramids. All KPI values are **modeled seed values**, not reported figures. The current→target pairs below are illustrative but useful as benchmark-shaped examples.

Customer relations: leadership funds and prioritises technology. Technology sets standards for brand engineering. Brand engineering feeds transactions to the controller. Payments feeds settlement data to the controller and funds payouts for settlement ops. Settlement draws liquidity from treasury. Treasury provides tax and FX positions to the controller. AP posts payables to the controller. The controller reports to leadership. The SOX lead assures the controller and sets control requirements for technology. Settlement raises exceptions with payments. Leadership sets savings targets for procurement.

### 5.1 Group finance leadership (CFO, CAO, VP Finance)
- **Cares about:** one set of numbers across brands and entities; a short, predictable SEC cycle; transformation savings; systems that keep pace with the merchant shift; ROI on multi-year programmes.
- **Wins them:** board-ready cost/benefit/risk options; releases that each remove manual work or a legacy system; proof that speed has not weakened controls.
- **Fears:** a material weakness or restatement caused by a system change; a programme that never retires legacy; brand stacks multiplying run cost; a missed filing.
- **Jobs:** steer on one trusted global view; deliver savings without raising control risk.
- **Journey trigger:** two brands' revenue manually re-mapped at quarter-end, and a business case that cannot name the systems to be switched off. The trial was one bounded decision, consolidating two brands' payables onto shared S2P.
- **KPIs:**
  - Decision-ready global view: 78→95%.
  - Reporting timeliness: 9→6 days. Close completion day: 7→4. Late subledger feeds: 11→2 a month. Manual pack adjustments: 35→5.
  - Brand-to-group reconciliation: 88→99%. Unmapped account balances: $42M→$5M. Conflicting metric versions: 18→2.
  - Finance cost-to-serve: 0.95%→0.75% of revenue. Systems run cost: $210M→$170M. Overlapping finance apps: 34→15. Cloud cost per million postings: $38→$26. Bespoke interfaces: 160→60.
  - Legacy systems decommissioned: 6→20. Touchless transaction rate: 70→90%. Spreadsheet-based controls: 220→80.

### 5.2 Technology and FinTech leadership (CTO, SVP FinTech, brand CTOs)
- **Cares about:** fast cross-brand decisions; engineering capacity spent on differentiating work; clear ownership across the matrix; architecture that survives regulation (PSD3/PSR, DMA, tax).
- **Wins them:** two or three costed options with a recommendation; patterns adopted without escalation; a critical-path dependency map; reviews that take days, not weeks.
- **Fears:** an ivory-tower bottleneck; late dependencies; each brand rebuilding the same integrations; decisions reopened because the rationale was never recorded.
- **Journey trigger:** a cross-brand payouts initiative stalled two months over "extend the brand ledger vs use the global subledger." The trial was the first ADR, with three costed options and a recommendation in ten working days.
- **KPIs:**
  - Decisions per quarter: 14→30. Lead time: 32→10 days. Board turnaround: 10→3 days. Reopened: 18→5%. Recorded rationale: 40→100%.
  - Delivery conformance: 62→90%. Unresolved critical dependencies: 24→6.
  - Portfolio ROI ratio: 1.4→2.5. Application count: 310→200. Apps retired: 12→40 a year. Duplicate capabilities across brands: 48→15. Benefits tracked to decisions: 30→90%. Post-implementation reviews: 25→80%.

### 5.3 Global controller and record-to-report lead
- **Cares about:** subledgers that reconcile to the GL *daily*; correct gross/net and timing; a holding close calendar; few audit adjustments; consistent CoA and entities.
- **Wins them:** summarised, complete, traceable SL postings; automated reconciliations with exception queues; **accounting rules versioned and tested before a new payment method goes live**; a close cockpit.
- **Fears:** unexplained payment↔SL↔GL differences; revenue in the wrong period after cancellations; a change that breaks a key control during close.
- **Journey trigger:** the quarter-end DMB tie-out took a team four days of spreadsheets and left an unexplained residual. The trial was one entity in parallel for two closes, with daily investigation.
- **KPIs:**
  - Clean close: 75→95%. Close: 7→4 days. Auto-matched reconciliation items: 72→95%. Spreadsheet reconciliations: 900→150.
  - SL→GL posting latency: 30h→4h. Failed postings per close: 320→40. SL→GL differences: $8M→$0.5M. Bookings traceable to postings: 90→99.9%.
  - Revenue in the correct period: 98.5→99.9%. Manual revenue adjustments: 60→10 a quarter.
  - Manual JEs: 4,200→1,500 a month. Top-side consolidation entries: 140→40. Audit adjustments: 14→4 a year. Journal approvals bypassed: 9→0. Posting rules under version control: 45→100%. Rule changes tested before go-live: 60→100%.

### 5.4 Tax and treasury lead
- **Cares about:** correct tax on every booking, commission and supplier invoice; lineage from transaction to return; a daily cash and FX position; segregated safeguarded funds; fast adoption of ViDA and DAC7.
- **Wins them:** one shared engine instead of brand rule tables; filings generated from the ledger; positions ready before the morning funding call; new jurisdictions added by configuration.
- **Fears:** another multi-year assessment; rules live in a country before the systems support them; unhedged exposure found after month-end; Pillar Two data that cannot be traced.
- **Journey trigger:** a tax audit found inconsistent VAT between two brands for the same stay type, and lineage could not be shown in time. The trial ran one brand and three EU countries in parallel for a quarter.
- **KPIs:**
  - Determination accuracy: 96.5→99.5%. Share on the central engine: 55→95%. Jurisdictions: 38→90.
  - Tax-to-ledger reconciliation: 88→99%. Manual tax adjustments: 140→30.
  - Bank accounts on automated statements: 78→97%. Cash forecast accuracy: 86→95%. Payout forecast error: 7.5→3%.
  - Leakage: $48M→$15M. Filings built outside the system: 35→5%. Days to answer an audit request: 21→5.
  - Hedged share of exposure: 70→85%. Exposure data latency: 36h→6h. Idle cash above buffer: $650M→$250M. Same-day payout funding: 80→97%.

### 5.5 Partner settlement and receivables operations lead
- **Cares about:** right amount, promised date; low unapplied cash and overdue commission; explainable lines; correct bank details; scaling without headcount.
- **Wins them:** one payout orchestration across brands, currencies and methods; automatic cash application; exceptions routed with the source booking; partner statements that match the ledger.
- **Fears:** a failed run leaving thousands unpaid; payouts to fraudulently changed bank details; disputes piling up.
- **Journey trigger:** a legacy brand payout job failed silently over a holiday weekend. The trial moved one brand's EUR payouts, in parallel for two cycles.
- **KPIs:**
  - Straight-through payouts: 86→97%. Run failures: 5→0. Corrections per 10k: 14→2. Bank returns: 0.9→0.3%.
  - Invoice dispute rate: 3.2→1%. Auto cash application: 78→95%. Direct-debit coverage: 55→75%.
  - Cost per settlement: $0.62→$0.40. Low-cost local rails: 64→85%. Virtual-card share: 22→30%.
  - Commission DSO: 34→25 days. Partners with net settlement: 30→60%. Write-offs: $38M→$20M.

### 5.6 Procurement and payables operations lead
- **Cares about:** spend on contract; touchless invoices with correct tax; no duplicate or fraudulent payments; one supplier record shared by procurement, AP and tax.
- **Fears:** maverick spend; supplier bank-detail fraud; e-invoicing mandates arriving early; brand P2P stacks that never converge.
- **Journey trigger:** a savings target, but spend data from five brands' tools are not comparable.
- **KPIs:**
  - Spend under management: 68→88%. No-PO invoices: 28→8%. Approval cycle: 52h→16h.
  - Touchless: 52→85%. E-invoice share: 35→80%. On-time payment: 88→97%.
  - Off-contract spend: 18→6%. Duplicates caught pre-payment: 85→99%. Supplier bank changes verified: 90→100%. Discounts captured: 40→80%.

### 5.7 SOX and internal controls lead
- **Cares about:** no material weakness or significant deficiency; controls designed in; evidence ready before it is asked for; clean SoD; knowing which changes touch in-scope controls.
- **Wins them:** automated application controls with system evidence; one control register mapped to systems, flows and owners; reviews that flag SOX impact *before build*; continuous monitoring rather than quarter-end sampling.
- **Fears:** a migration that silently breaks a key control; unevidenced spreadsheet reconciliations; SoD conflicts from emergency access; **auditor findings on completeness of the merchant revenue population**.
- **Journey trigger:** a brand payments integration went live mid-quarter without a control-matrix update, and merchant revenue completeness was nearly a significant deficiency. The trial ran continuous monitoring on payments-to-ledger reconciliation controls in parallel, shared with the auditor.
- **KPIs:**
  - Automated control share: 38→60%. Interfaces with completeness controls: 72→95%. Brand feeds with record-count checks: 65→95%. Key reports validated: 80→100%.
  - Evidence retrieval: 4→1 days. Changes with SOX impact assessed: 60→100%. Post-release control failures: 6→1.
  - Testing hours: 38k→24k. Controls tested by monitoring: 15→50%. Duplicate controls across brands: 85→30. Remediation time: 64→30 days. Repeat findings: 4→0.

### 5.8 Brand finance engineering lead (matrixed)
- **Cares about:** shipping the brand roadmap; stable integration contracts; not rebuilding ledger, tax or reconciliation logic; being heard when standards do not fit.
- **Wins them:** an adapter kit with schemas, mappings and test harnesses; fast decisions; self-service onboarding with SLAs; **standards that come with reference implementations**.
- **Fears:** a central mandate that freezes delivery for a year; owning a fragile bespoke integration; blame for issues caused upstream; standards changing mid-programme.
- **Journey trigger:** a hand-built feed broke twice during a close, and the team spends a third of its time on finance plumbing. During evaluation the team checked whether brand-specific products (e.g. restaurant deposits, flight bundles) fit the canonical model.
- **KPIs:**
  - Onboarding: 60→20 engineer-weeks. Adapter reuse: 35→80%. Custom transformations per brand: 140→40. Parallel run: 4→2 closes.
  - First-pass conformance: 55→85%. Standards with a reference implementation: 30→80%.
  - Brand ledgers retired: 2→8. Brand time on finance plumbing: 30→10%. Contract-breaking upstream changes: 6→1.

### 5.9 Payments platform product lead (including the licensed e-money entities)
- **Cares about:** launching methods and markets fast; every payment, refund and chargeback reconciling; cost, authorisation rate and fraud loss; safeguarding obligations.
- **Wins them:** **a finance-readiness checklist and a standard accounting pattern for new payment methods**; automated three-way matching; early finance and tax input; one P2L contract across PSPs.
- **Fears:** an APM blocked for months by finance set-up; growing unreconciled PSP balances; PSD3/PSR rework; a safeguarding breach.
- **Journey trigger:** new local wallets were ready, but finance needed three months for accounts, mapping and reconciliation.
- **KPIs:**
  - Reconciliation completeness: 95.5→99.5%. PSP settlement coverage: 80→100%. APMs on the canonical schema: 60→100%.
  - Break ageing: 9→2 days. Breaks over 30 days: 4,200→300. Auto-classified breaks: 35→80%.
  - Time to finance-ready launch: 12→3 weeks. Controls ready at launch: 55→100%.
  - Payment cost and loss: 1.9%→1.6% of payment value. Chargebacks linked to a booking: 70→98%. Representment win rate: 38→55%.
  - PSP fee accuracy: 92→99.5%. Fee schedules machine-readable: 45→100%. FX cost: 28→18 bps. Local-currency settlement: 62→80%. FX netted before hedging: 40→70%.

---

## 6. Tutorial concepts (teaching material, kept in substance)

The tutorial is called "Following the money." Its audience is an intelligent adult with no accounting background. **Learning goals:**
- why one booking creates many records;
- agency vs merchant;
- why cash received is not revenue;
- what reconciliation and the close are, and why auditors care;
- why a multi-brand company needs shared standards and an architecture function.

**Framing analogy.** Friends settling holiday costs need a list of payments, an agreement on who owes what, and a moment to check against bank statements. *Where the analogy breaks:* a company settles continuously, in dozens of currencies, with millions of counterparties, under rules that decide *when* money counts as income. It must also prove to auditors that the *process* is reliable, not just that the totals look plausible.

**Participants.**
- The traveler: wants a clear price, a familiar payment method and fast refunds.
- The property or partner: wants to be paid on time, to understand deductions, and to get correct invoices and tax documents.
- Brands and their payments teams, including regulated e-money institutions: want fast launches, low cost and fraud, and to avoid being blocked by finance.
- Finance teams: want an on-time close, explainable numbers, correct tax and cash visibility.
- Auditors, regulators and investors: want evidence of completeness and accuracy, and a process that cannot easily be bypassed.
- Architects and engineers: want clear decisions and standards, fewer one-off integrations, and change that does not break controls.

### The nine concepts

1. **Ledger and journal entry.** A ledger is the official record of what the company owns, owes, earns and spends. Each change is a double-entry journal entry (debit one account, credit another) so the books always balance. *Example:* a traveler's €300 arrives, so cash at bank +300 and "money owed onward" +300; nothing has been earned yet. *Why it matters:* every published number is a sum of entries, so a missing, duplicated or misposted entry flows straight into the statements.

2. **Agency model vs merchant model.**
   - *Agency:* the traveler pays the property, usually at the stay, and the platform later invoices commission. In the example the guesthouse charges €300 and receives a €45 commission invoice.
   - *Merchant:* the platform collects €300 at booking, holds it, and pays the property €255 after deducting its share.

   *Why it matters:* the two produce completely different finance work. Agency is invoicing and collection. Merchant is handling travelers' payments, refunds and disputes, holding funds and paying partners. A rising merchant share means a fast-growing merchant workload.

3. **Revenue recognition.** Under ASC 606 (US GAAP), revenue is recorded when the promise is delivered, not when cash arrives. *Example:* booked and paid in March for a July stay, the commission is revenue in July; a full-refund cancellation is never revenue. *Why it matters:* receiving money and earning money are different events. Systems must track millions of bookings waiting to be earned and restate them on every change. The model's richer form covers the principal-vs-agent judgement, gross vs net presentation, timing at check-in or stay completion, payment-facilitation revenue, and the point that **policy changes need re-runs across open bookings**.

4. **Deferred merchant bookings.** Cash received for trips not yet taken, recorded as a liability because most of it will be paid to partners or refunded. For the modeled company this was about $5.3bn, up from $4.0bn. *Why it matters:* this is a large, moving pool of other people's money. Finance must say at any moment how much is held, for which bookings, in which entity and currency. Regulated payment entities may need to **safeguard** it, i.e. keep it separate and protected.

5. **Subledger and general ledger.** The GL holds totals by account and is the source of the statements. A subledger holds the detail of one area (every booking-level payment, refund and payout) and passes summarised totals to the GL. *Example:* tens of millions of booking payments a month in the subledger become a few thousand summarised GL entries, each traceable back. *Why it matters:* putting every booking in the GL would make it slow and unreadable. The design works **only if every summary can be traced to its details**. High-volume contract-accounting and billing tools (FI-CA/BRIM-type) exist for this.

6. **Payment service provider, settlement and chargeback.** A PSP processes card and online payments. For card-not-present payments it authorises and then, days later, **settles**: one net batch, minus fees, with a file listing what is included. A **chargeback** is a reversal by the cardholder's bank after a dispute. *Example:* €300 paid Monday; Thursday's single deposit covers thousands of payments net of fees; two months later the bank reverses €300 ("room not as described"). *Why it matters:* money does not arrive when, or in the amount, the booking screen suggests. Each APM (wallets, local bank transfers) has its own timing and file formats, so **every new method adds matching work**.

7. **Reconciliation.** Checking that two records which should agree do agree, and explaining any differences. *Example:* expected bookings vs the PSP settlement file vs the bank. If €1,000 is missing, is it a fee, a chargeback, a timing difference or an error? *Why it matters:* this is how a company knows its records match reality. Accumulated unexplained differences threaten the published numbers and signal leakage. A knowledge-check adds that fees and next-batch timing are harmless explanations, while missing payments and unrecorded chargebacks are urgent.

8. **Month-end close and internal controls.** The close is the routine of completing records, reconciling, adjusting and producing the period's statements. Controls are the checks built into it: approvals, reconciliations and restricted access. *Example:* separation of duties means no one person may both create a supplier and approve payments to it; the system enforces this and auditors test that it works. *Why it matters:* Sarbanes-Oxley requires management to report on ICFR, and for large filers an auditor attests to it. **Any change to a financial system can affect a control, so system change is compliance work.**

9. **Architecture decision and target state.** A decision is a recorded choice about how systems fit together, e.g. which system is the source of truth for a record type. The target state is the agreed multi-year picture, and standards are the rules teams follow to get there. *Example decision:* "every brand sends booking financial events in one common format to one integration hub, and only the central subledger calculates revenue." A brand that wants its own revenue calculator needs an **explicit, time-limited exception**. *Why it matters:* without shared decisions each brand solves the same problem differently and finance translates between versions. With them, work moves faster without weakening controls.

### History (teaching selection)
- **1990s, integrated ERP.** Departmental programs gave way to a shared database, which created the expectation of shared master records (accounts, suppliers, entities). Much of today's architecture work is keeping those consistent through growth and acquisition.
- **2002, Sarbanes-Oxley.** Executives certify reports and must report on ICFR. Systems stopped being only about efficiency: *who can change what, and what evidence is kept*, became legal concerns.
- **2015–2019, PSD2 and SCA.** More payment types, providers and rules; more change is coming.
- **2016 onward, ERP core modernisation.** At the flagship brand: ERP on an in-memory DB, then Simple Finance in 2016, then an S/4HANA journey via Central Finance from 2019. The lesson: a core accounting move is a multi-year programme that must keep the books running, and decisions taken then shape the landscape for a decade.
- **2024–2025, agency to merchant**, combined with a cost Transformation Program. Payment, reconciliation and payout volumes multiply while costs are being cut.

### Walkthrough: a fictional €300 merchant booking
1. The traveler pays €300 in March for July. The PSP authorises, and a booking event goes to finance with who, property, entity, amount, currency and stay dates. That event is the raw material for every later record, so it must mean the same thing in every brand.
2. Three days later the PSP deposits one net amount with a settlement file. Finance matches booking to file and file to bank (the three-way match), and records €300 as cash and DMB, not income. *Watch out:* a new local method launched before its settlement files can be auto-matched piles up unexplained items.
3. In May the traveler shortens the stay and gets €100 back. Held funds drop to €200, and both the expected payout and the platform's share are recalculated. *Watch out:* if the refund is processed in payments but the booking change reaches finance late, the subledger briefly shows the old amount, reconciliation flags it, and someone must explain it before close.
4. The stay happens in July. €30 (15% of €200) becomes revenue and €170 becomes a payable to the property. Tax systems determine which taxes apply to the platform's fee and where.
5. The payout groups the property's completed stays, applies deductions, and pays €170 by bank transfer with a statement. That payout must be matched to the bank again.
6. Close: the subledger summarises to the GL, accounts are reconciled, differences reviewed, and controls confirmed (e.g. no payout bank-detail change without a second approval). At quarter end, brands and entities are consolidated. An auditor can trace a reported line back to the booking.
7. An architecture question: another brand records partial refunds differently and needs manual adjustment every month. It goes to the review board (shared refund events into the central subledger, and by when?). Options are compared on cost, risk and benefit, the decision is recorded, and conformance is tracked. *"One-off workarounds are cheap once and expensive forever."*

### Value, incentives and conflict
- **Why invest.** Correct, fast systems let the company pay partners reliably, publish on time, meet tax and regulatory duty and understand performance. Weak systems show up as manual work, delayed closes, tax penalties, payment losses and audit findings. The modeled company's $337M indirect-tax accrual is noted with the caveat that not every tax dispute is a systems problem.
- **Who pays.** The operating budget: licences, cloud, engineers and finance staff. The return is avoided cost, reduced risk and growth without proportional hiring.
- **Where interests pull apart.** Payments and brands want speed; finance and controls want "reconciled and controlled from day one"; brands have legacy preferences; vendors want full-suite lock-in. Architecture finds "the smallest design that lets the launch go ahead without unreconciled money building up."

### Challenges (each with trade-off and common approach)
- **High volume, little room for error.** Booking-level detail is traceable but costly; summarisation is cheap but hides errors. One cent of FX rounding per booking becomes a noticeable unexplained amount. *Approach:* a high-volume subledger, summarisation and automated rules. The subledger and its feeds then become critical systems that must never fall behind.
- **Many brands, many histories.** A big-bang move is risky; staying separate means duplicated cost forever. *Approach:* a shared event format, a target state, adapters and step-by-step retirement. This needs recorded, enforced decisions and senior cross-brand backing.
- **Payments keep changing.** Waiting slows the business; launching first leaves unreconciled money. *Approach:* make "finance ready" part of every payment launch, with a checklist and a translation layer into one format, at an upfront cost per method.
- **Changing systems without breaking controls.** Controls live in configuration, so modernisation can silently remove one (e.g. a new payout tool lets support edit bank details without the old second approval). Strict change approval slows delivery; loose approval risks findings. *Approach:* controls inside the architecture standards and early control-impact review, which requires architects and controls specialists to share a vocabulary.
- **Taxes that depend on where and who.** DSTs of 1.5–10%; a city tourist tax on the stay vs VAT place-of-supply rules on the fee. Hard-coding goes stale; a central engine becomes a dependency for every flow. *Approach:* one shared determination service fed by complete booking data, logging each decision. It is only as good as its input data.

### Misconceptions
- "Payment = earned." In fact most of it is owed or refundable, and only the share earned on delivery is revenue.
- "Financial systems are software you buy." In fact the difficulty lives in the connections and in agreeing what each record means.
- "Right totals = right books." Offsetting errors can hide, so completeness and process must be shown.
- "EA is drawing diagrams." Here it is making and enforcing decisions on source of truth, mandatory standards and multi-year investments.

### Takeaways, knowledge checks and next questions
- **Takeaways:** a booking creates a chain of records; money received ≠ money earned; reconciliation and controls are proof; the merchant shift multiplies work; shared decisions turn workarounds into scalable designs.
- **Knowledge-check highlight:** if a brand proposes its own revenue calculation, the review asks about cost and risk vs the shared subledger, how it would be reconciled and controlled, and whether any exception is time-limited with a convergence plan.
- **Next questions for practitioners:**
  - Which system is the source of truth for revenue, partner payables and cash, and who decides?
  - How many manual adjustments are made each close, and what causes them upstream?
  - What does a new payment method need from finance before launch?
  - Which brands still run their own finance tools, and what is the plan for each?
  - How are controls reviewed when a system changes?

---

## 7. Residuality stressors and architectural responses

The **naive architecture** in the model: each brand runs its own ledger feeds, payout logic, tax rules and reconciliations, brand data reaches the ERP through spreadsheets and point-to-point interfaces, and decisions are taken per programme with no shared record.

The **residual architecture**:
- a clean-core global finance hub fed by canonical financial events through one hub and adapter kit;
- a high-volume subledger, a traveler-funds ledger and automated payments-to-ledger reconciliation;
- tax determination and e-invoicing as shared services;
- entity- and jurisdiction-tagged finance data;
- control evidence captured by default;
- a governed decision record, standards and portfolio that make change repeatable.

| Stressor (group, status) | Detection signal | Attractor (what goes wrong) | Response | Residue (what survives) | Impacts |
| --- | --- | --- | --- | --- | --- |
| **PSD3 / Payment Services Regulation** (regulation, candidate) | Final texts, EBA RTS, licence conditions; named as a 10-K risk | Each brand patches its own payment and safeguarding logic; reconciliation breaks; reports built by hand | Model regulated flows once: payment events carry **entity, licence and safeguarding attributes**; safeguarding and reporting read from the reconciled ledger | Canonical payment event with regulatory attributes; entity-aware safeguarding ledger | pevt, regr, tfnd; launch time at risk from re-certification; PSP reporting must carry new data |
| **EU VAT in the Digital Age** (e-invoicing, digital reporting, platform deemed-supplier) (regulation, candidate) | Adoption and member-state transposition | Tax logic copied into each brand's invoicing; formats bolted on per country; missed filings | Central tax determination as a service for commission, merchant and supplier invoices; e-invoice exchange via the hub | **One tax service and one e-invoice gateway shared by O2C and P2P** | itax, pinv, apin, fint; determination accuracy |
| **Pillar Two and spreading DSTs** (regulation, candidate) | OECD adoption, new DSTs, audits | Provision in spreadsheets from manual extracts; each new tax becomes a project | Entity-level, jurisdiction-tagged datasets in the data platform feed provision and top-up calculations | **Jurisdiction and entity dimensions on every finance dataset**; reusable tax data mart | gtax, entm, fdbx; exposure and penalties |
| **Brand acquisition or carve-out** (corporate, integrated) | M&A announcements, integration mandates | Another ERP and payout engine run in parallel for years; consolidation via spreadsheet mappings | Onboard through the adapter kit: map to the global CoA, stream canonical events, **consolidate from day one**, retire legacy on a dated plan | Repeatable onboarding pattern with templates and a retirement playbook | bonb, coam, cnsl; onboarding stream becomes repeatable; in-house substitute retired |
| **ERP maintenance deadlines and cloud subscription terms** (vendor, integrated) | Maintenance announcements, renewal windows, pricing | Big-bang migration under deadline; custom code copied as-is; run cost rises without simplification | **Keep the clean core**: central finance as hub; extensions outside the core behind APIs; dated decommission plan per legacy system | Clean-core standard, extension patterns, portfolio run-cost view | glco, stdg, apmx; negotiating leverage with the incumbent; alternative ERP as benchmark |
| **Agency-to-merchant shift accelerates** (market, already survived) | Merchant share, merchant revenue growth, DMB growth | SL volumes, payout liabilities and breaks grow faster than teams; the close slips | Scale the subledger and P2L for merchant volume; automate payout-liability tracking and three-way matching | Volume-proof merchant flow: event-driven SL, automated reconciliation, traveler-funds ledger. *Reuses the acquisition and clean-core residues* | brim, psrc, pout, tfnd; close speed; payout timeliness |
| **AI agents book trips and run finance tasks** (technology, candidate) | AI-assisted booking; AI in finance ops; auditor guidance on AI in controls | AI tools added per team with no lineage or control evidence, so auditors cannot rely on them | Allow AI only through governed data, logged decisions and control evidence; **treat agent-created bookings as normal canonical events** | Governed AI patterns: lineage from the data platform, decision logging, evidence capture in control monitoring | ctlm, fdbx, adrr; evidence readiness; automation savings |
| **Major PSP or acquirer outage or settlement-file failure** (dependency, integrated) | Incident notices, missing or malformed files, sudden unmatched volume | Unreconciled balances pile up, payouts stop, the close is late, controls fail | **Treat settlement files as contracts** with completeness checks, replay and quarantine; reconcile per PSP with tolerance rules; keep payouts funded from the traveler-funds ledger | Settlement completeness controls, replayable ingestion, per-PSP reconciliation | pevt, psrc, bnkc (fallback payment routes); unreconciled value; PSP dependency |

Status values in the model: *candidate* (proposed residue), *integrated* (designed in) and *already-survived* (the stressor has happened and the architecture coped).

The links page also names the **EU Digital Markets Act gatekeeper designation** as a regulatory constraint on data and payment flows, but no stressor is built from it.

---

## 8. Vendor and competition landscape

**Framing.** The group is a *buyer* of these vendors, not their competitor. The landscape shows which platforms compete for the architecture's slots and what leverage each brings. *Inclusion:* ERP and finance-suite vendors that could host the core; the close and consolidation specialists reported in a third-party listing; global PSPs whose data feed P2L; in-house build as the main substitute. *Excluded:* SIs and implementation partners, niche tax-content and treasury vendors without verifiable metrics, and the group's own payment entities. *Caveat:* the figures below are company-wide, use different currencies, metrics and fiscal years, are **not comparable**, and say nothing about the group's own spend.

| Vendor | Category | Positioning in the model | Stats (source) |
| --- | --- | --- | --- |
| **SAP** (Walldorf) | global leader | Incumbent ERP core: HANA, Simple Finance, S/4HANA via Central Finance, FI-CA/BRIM. RISE and end of ECC standard maintenance shape the convergence timeline and run cost | FY2025 revenue €36.80bn; cloud €21.02bn; Cloud ERP Suite €18.12bn; current cloud backlog €21.05bn ([source](https://www.nasdaq.com/press-release/sap-quarterly-statement-q4-2025-2026-01-29)) |
| **Oracle** (Austin) | global leader | Fusion Cloud ERP and NetSuite as alternative finance cores, often in acquired or smaller brands; benchmark in ERP renewals | FY2026 (to 31 May 2026) revenue $67.4bn; cloud $34.0bn; cloud apps SaaS $15.9bn ([source](https://www.oracle.com/news/announcement/q4fy26-earnings-release-2026-06-10/)) |
| **Workday** (Pleasanton) | challenger | Cloud HCM plus financials; contender for adjacent slots (HR, spend, planning) and alternative core for greenfield or acquired entities | FY2026 (to 31 Jan 2026) revenue $9.552bn; subscription $8.833bn ([source](https://investor.workday.com/news-and-events/press-releases/news-details/2026/Workday-Announces-Fiscal-2026-Fourth-Quarter-and-Full-Year-Financial-Results/default.aspx)) |
| **BlackLine** (Woodland Hills) | niche | Close, account reconciliation and intercompany specialist; competes with SAP's own close tooling for the close-orchestration slot | FY2025 GAAP revenue $700.4M ([source](https://investors.blackline.com/news-releases/news-release-details/blackline-announces-fourth-quarter-and-full-year-2025-financial)) |
| **OneStream** (Birmingham, MI) | niche | Unified consolidation, reporting and planning; competes with SAP Group Reporting and planning suites; **pending acquisition by a private-equity firm (Hg) affects vendor-risk and roadmap decisions** | FY2025 revenue $601.9M; subscription $550.0M ([source](https://www.onestream.com/news/onestream-announces-fourth-quarter-and-fiscal-year-2025-financial-results/)) |
| **Adyen** (Amsterdam) | global leader | Global CNP and APM platform with travel/OTA offerings; represents the PSP category feeding P2L reconciliation | H2 2025 processed volume €745bn (+12%); net revenue +17% ([source](https://www.adyen.com/press-and-media/adyen-publishes-h2-2025-financial-results-3pgu2)); travel page https://adyen.com/landing/online-travel-agencies |
| **Stripe** (South San Francisco / Dublin) | global leader | PSP *and* API-first finance tooling (billing, revenue recognition, treasury APIs) that challenges ERP-centric subledger designs | 2025 TPV about $1.9tn (+34%), self-reported ([source](https://stripe.com/newsroom/news/stripe-2025-update)) |
| **In-house build** (brand-specific ledgers, settlement engines, reconciliation tools) | substitute | Fast locally, but duplicates spend, fragments controls and slows convergence; "every convergence decision weighs against it" | none |

**Implied slot map for a book.** The slots are: ERP core and GL; high-volume subledger and billing; revenue recognition; close and reconciliation; consolidation and planning; S2P; tax engine; TMS; PSPs; and custom edge services. Vendor links: SAP S/4HANA Finance https://www.sap.com/products/financial-management/s4hana-finance.html; Central Finance https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/?q=central%20finance; FI-CA/BRIM https://learning.sap.com/courses/implementing-sap-financial-contract-accounting/describing-sap-billing-and-revenue-innovation-management-sap-brim-; RISE https://www.sap.com/products/erp/rise.html. Vendor IR and newsroom links appear in the competition file (sap.com/investors, investor.oracle.com, investor.workday.com, investors.blackline.com, investor.onestream.com, investors.adyen.com, stripe.com/newsroom).

---

## 9. Facts vs assumptions, and all source URLs

### 9.1 Facts the model treats as sourced (from public filings, releases or job postings)
- Scale: about $26.9bn revenue, $186.1bn gross bookings and 1,235M room nights (FY2025).
- Merchant share 70% (vs 63%). Merchant revenue $17,755M (+25.5%); agency revenue $7,968M (−6.5%), almost entirely accommodation commission.
- DMB of $5,270M (vs $4,031M), mostly refundable.
- Merchant transaction costs +$381M. Payment-facilitation revenue (card processing rebates, customer processing fees) is part of merchant revenue.
- Transformation Program: about $250M savings in 2025; about $550M run-rate enabled; $205M of transformation costs; scope covers processes and systems, workforce, procurement and real estate.
- Marketing spend about $8.2bn.
- ICFR effective at 31 Dec 2025, with an external auditor attestation under SOX 404(b) and no material Q4 change.
- Indirect tax: $337M accrual (2024) for one country's matters and $89M (2025) of other matters. DSTs 1.5–10%. ViDA and PSD3/PSR named as risks. $257M remaining transition-tax liability. OECD reform referenced.
- EUR and GBP are the principal FX exposures, hedged with derivatives and EUR debt; FX added about 3 points to revenue growth.
- The group's financial-services arm comprises licensed e-money institutions, one licensed by the Central Bank of Ireland and intending to trade from 2025.
- An APM partnership for Asian local payment methods (January 2025).
- The flagship brand's ERP history: HANA, then Simple Finance (Feb 2016), then S/4HANA via Central Finance (2019), with FI-CA and BRIM in the stack (from job postings).
- The group is designated an EU DMA gatekeeper.
- The role description: final decision rights on mandatory standards; objectives of decision velocity, target-state quality, fewer unresolved dependencies, and moving from tactical workarounds to scalable designs without compromising controls; a BITS requirements framing; (S)VP-level cost-benefit options.

### 9.2 Explicitly flagged assumptions
- **All KPI values are modeled seed values.**
- The team model (132 people in 14 teams) is invented.
- BlackLine, OneStream, "FinDB", SAP RISE and IFRS 15 wording come from an **unverified third-party listing**. The group reports under US GAAP (ASC 606).
- S/4HANA and Central Finance progress, and which brands are on it, is not public.
- The PSPs used, beyond the APM partnership, are unconfirmed; Adyen and Stripe are categories.
- Brick internals (modules, stores, dependencies) are inferred from standard finance-system patterns, not from internal documentation.
- Vendors for tax engine, TMS, S2P, planning, GRC tooling, VCC issuer, EA tool, BI, streaming and lakehouse are all assumed.
- SAP MDG and SAP revenue accounting are assumed.
- The stressors PSD3/PSR, ViDA, Pillar Two and AI agents are plausible scenarios grounded in 10-K risk factors, not announced programmes.
- Stream flow details are "modeled from public disclosures and common practice."

### 9.3 All source URLs in the model
- 10-K FY2025: https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm
- Q4/FY2025 earnings release: https://s201.q4cdn.com/865305287/files/doc_financials/2025/q4/Q4-25-BKNG-Earnings-Release.pdf
- Investor relations: https://ir.bookingholdings.com/
- Financial-services arm: https://www.bookingholdings.com/about/financial-services/
- E-money licence article: https://thecurrency.news/articles/161660/how-ireland-slots-into-bookings-fintech-ambitions/
- APM partnership: https://www.businesswire.com/news/home/20250114445080/en
- SAP FI job postings: https://www.themuse.com/jobs/bookingcom/sap-fi-specialist-18567f and https://www.efinancialcareers.com/jobs-Netherlands-Amsterdam-SAP_FI_Specialist_FinTech.id24600255
- Architecture role description (careers page): https://www.bookingholdings.com/careers/
- Unverified third-party listing: https://jobs.weekday.works/wkdyodt36e
- SAP: https://www.sap.com/products/financial-management/s4hana-finance.html ; https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/?q=central%20finance ; https://learning.sap.com/courses/implementing-sap-financial-contract-accounting/describing-sap-billing-and-revenue-innovation-management-sap-brim- ; https://www.sap.com/products/erp/rise.html
- Regulation and standards: DMA gatekeepers https://digital-markets-act.ec.europa.eu/gatekeepers_en ; PSD3/PSR https://finance.ec.europa.eu/regulation-and-supervision/financial-services-legislation/implementing-and-delegated-acts/payment-services-directive_en ; OECD Pillar Two https://www.oecd.org/en/topics/sub-issues/global-minimum-tax.html ; ViDA https://taxation-customs.ec.europa.eu/taxation/vat/vat-digital-age_en ; PCAOB AS 2201 https://pcaobus.org/oversight/standards/auditing-standards/details/AS2201 ; SOX https://www.congress.gov/bill/107th-congress/house-bill/3763 ; PSD2 https://eur-lex.europa.eu/eli/dir/2015/2366/oj
- Vendors: https://www.nasdaq.com/press-release/sap-quarterly-statement-q4-2025-2026-01-29 ; https://www.oracle.com/news/announcement/q4fy26-earnings-release-2026-06-10/ ; https://investor.workday.com/news-and-events/press-releases/news-details/2026/Workday-Announces-Fiscal-2026-Fourth-Quarter-and-Full-Year-Financial-Results/default.aspx ; https://investors.blackline.com/news-releases/news-release-details/blackline-announces-fourth-quarter-and-full-year-2025-financial ; https://www.onestream.com/news/onestream-announces-fourth-quarter-and-fiscal-year-2025-financial-results/ ; https://www.adyen.com/press-and-media/adyen-publishes-h2-2025-financial-results-3pgu2 ; https://adyen.com/landing/online-travel-agencies ; https://stripe.com/newsroom/news/stripe-2025-update
- Vendor home and IR pages: sap.com, sap.com/investors/en.html, news.sap.com, oracle.com/erp, investor.oracle.com, oracle.com/news, workday.com, investor.workday.com, newsroom.workday.com, blackline.com, investors.blackline.com, onestream.com, investor.onestream.com, adyen.com, investors.adyen.com, stripe.com

---

## 10. Gaps relative to a full book on enterprise architecture and financial systems

**Accounting and ledger depth**
- No worked journal entries beyond the €300 example: no T-accounts for merchant vs agency, DMB release, refunds after payout, chargeback loss, PSP fee accrual, FX revaluation or intercompany elimination.
- No **posting-rule / account-determination design** (event → posting rule → accounts), no CoA design principles (segments, natural accounts, dimensions), and no treatment of multi-GAAP or parallel-ledger mechanics.
- No **IFRS 15 vs ASC 606** comparison, despite the IFRS wording in the unverified listing.
- Little on contract modifications, variable consideration, breakage, loyalty points or gift cards, or the principal/agent indicators (control, inventory risk, pricing discretion) in detail.
- Accruals, cut-off rules and late-arriving events (bitemporal "as-of" vs "as-at" accounting) are not discussed.
- Nothing on ledger immutability, reversal vs correction semantics, or event sourcing as an accounting pattern.

**Custom ledgers and subledgers**
- The model is ERP-centric. There is no in-house ledger design (double-entry data model, balance computation, idempotency keys, sequence and gap control, sharding, hot accounts), no comparison with **open-source or API ledgers** (e.g. TigerBeetle, Formance, Modern Treasury, Stripe Ledger), and no build-vs-buy criteria for subledgers.
- No subledger-to-GL summarisation granularity strategy (by day, account, entity or currency) and no reconciliation-key design.

**Payments-to-ledger**
- No breakdown of interchange and scheme fees (IC++ vs blended), acquiring models, payment facilitation and marketplace (split) payments, or payfac regulation.
- No virtual-card issuing economics.
- No settlement-file formats by PSP, no multi-currency settlement or FX-at-settlement accounting, no rolling reserves or holdbacks, no partial captures or incremental authorisations, and no network tokens or SCA exemptions in finance terms.
- Little on refunds after payout (partner clawback and negative balances), or on payout netting mechanics and their accounting.
- Fraud and AML transaction monitoring, and sanctions screening beyond a hand-off, are thin.

**Reconciliation and close**
- No matching-algorithm detail (one-to-many, many-to-many, tolerance design, fuzzy matching, ML classification), no break taxonomy, and no write-off governance and thresholds.
- No close calendar example (day −3 to day +N), no account risk-rating method, and no flux-analysis thresholds.
- The continuous-close architecture (soft close, intraday postings) is named but not explained.

**Consolidation and reporting**
- No minority interest, equity accounting, purchase-price allocation or M&A accounting; no XBRL or disclosure-management tooling detail; no segment-reporting logic; no management vs statutory reporting reconciliation.

**Tax**
- No VAT place-of-supply rules for accommodation vs intermediation, no marketplace deemed-supplier mechanics in detail, no tax engine integration patterns (real-time call vs batch, caching, fallback), no e-invoicing models compared (Peppol post-audit vs clearance in IT/ES/PL/FR), no transfer-pricing mechanics, and no Pillar Two data model (GloBE income, covered taxes, safe harbours, QDMTT).

**Treasury**
- Bank account management, in-house bank and netting centres, cash pooling, hedge-accounting designations (cash-flow vs net-investment), counterparty risk and EMIR reporting are only named.

**Enterprise applications breadth**
- **Workday and Oracle Fusion are only positioned, not modeled.** HCM/payroll-to-GL, T&E, fixed assets and leases (ASC 842), project accounting, revenue for advertising products, and the order-to-cash for B2B and advertising customers are all missing.
- No ERP migration strategy comparison (greenfield vs brownfield vs selective/bluefield, Central Finance vs direct conversion), no RISE vs on-prem economics, no BTP/side-by-side extension patterns, and no SAP clean-core levels.

**Integration**
- No iPaaS vs custom vs event-mesh comparison, no schema versioning and compatibility rules for the canonical event, no CDC from ERP, no outbox pattern, no DLQ/quarantine operations playbook, and no MFT security details.

**Data and analytics**
- No data-mesh vs central finance data team discussion, no metric-layer technology, no data contracts, no data-quality SLAs per asset, and no MNPI wall-crossing process.

**Governance and organisation**
- No real ADR examples or template (beyond the BITS fields), no worked review-board charter (decision rights matrix or RACI), no waiver lifecycle example, and no TIME/disposition method.
- No architecture team operating model or sizing (the team model was excluded from the files read), no FinOps for SaaS licences, and no vendor management or exit strategy (beyond the OneStream acquisition risk).

**Controls and security**
- No ITGC domain breakdown (access, change, operations, SDLC), no SOC 1 reliance on SaaS vendors, no IPE/key-report validation method, and no audit-trail and logging standard.
- No **controls-as-code** example and no AI-in-controls guidance details.
- No PCI DSS scope-reduction architecture beyond tokenisation, and no data residency and GDPR erasure vs retention conflict handling.

**Resilience and operations**
- Resilience tiers are named but not defined. There are no RTO/RPO for finance systems, no close-time disaster scenarios, no ERP upgrade cadence, no performance and volume testing for peak season, and no observability for financial pipelines (completeness SLOs).

**Other gaps**
- **Regulatory breadth:** UK and US equivalents (FCA safeguarding rules, state money-transmitter licences), APAC regimes for APMs, CSRD/ESG reporting data, DORA (EU operational resilience for financial entities, relevant to e-money institutions), and the AI Act implications for finance AI are absent.
- **AI:** only one stressor. No concrete use cases (reconciliation break classification, invoice capture, flux commentary, close agents), no model-risk or audit evidence pattern, and no agentic-booking finance implications beyond "treat as canonical events."
- **Quantitative economics:** no TCO model, business case template or benchmark data (close-days distributions, cost per invoice). All KPIs are seed values.
