# Research brief: Domains, regulation and how consequences change required controls

Prepared 28 October 2026 for chapter writers of *Architecting Agentic Systems*. The brief is vendor-neutral. Its question is narrow: **when an agent works in a given domain, which consequences change the controls the architecture must provide?** It covers EU and US regulation, court and regulator decisions, public-sector automation failures, customer-facing liability, documented enterprise deployments, and the documented architecture and measured productivity of coding agents.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page or document was fetched in this session (28 October 2026) and supports the claim. Paraphrases stay close to the source, and quoted text is quoted. The date is the source's publication date, not the fetch date. Undated documentation pages are marked "n.d., accessed 2026-10".
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (law-firm alert, press, university case summary, regulator summary written by another body), not from the primary text.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. Every architectural recommendation falls here, as does any statement about how a company's system works internally that the company has not described.

**Evidence age matters.** Regulation in this field moved a great deal in 2025–2026. Three things a writer working from 2024 memory would get wrong:

1. The EU AI Act's Annex III high-risk obligations **do not apply from 2 August 2026**. The Digital Omnibus on AI (Regulation (EU) 2026/1744) moved them to **2 December 2027** (Annex I product-embedded systems: **2 August 2028**).
2. The US Federal Reserve's **SR 11-7 was superseded on 17 April 2026** by SR 26-2, which **explicitly puts generative and agentic AI models out of scope**.
3. FDA's 2022 Clinical Decision Support guidance was **superseded in January 2026** by a revised final guidance that relaxes the single-recommendation position.

Sources older than about 18 months are flagged. The public-benefits cases (Robodebt, Dutch childcare benefits, MiDAS) are 2013–2023 events and **were not LLM systems**; they are cited for what they show about automated decision-making at scale, not about models.

**Research limitation.** Several primary sites refused automated fetches (HTTP 403 or timeouts): the Robodebt Royal Commission website, the Dutch Data Protection Authority (Autoriteit Persoonsgegevens), HHS's HIPAA guidance pages, PCAOB standards pages, CanLII and the BC Civil Resolution Tribunal (Moffatt v. Air Canada), the Michigan Attorney General's press release, and the ABA's own PDF of Formal Opinion 512. For these the brief uses secondary sources and tags them WIDELY REPORTED. The proposed GDPR amendments in the wider Digital Omnibus package (including Article 22) could not be confirmed against a final text; secondary sources contradict each other. Klarna's 2025 IPO prospectus was not read. No documented enterprise agent deployment beyond Klarna was verified to primary-source standard in this session.

**Volatility flags.** ⚠ marks claims likely to change within 12 months: application dates, pending legislation, guidance status (draft vs final), product feature names and settings, and vendor numbers.

---

## PART 1: The frame — consequence, not domain label, drives controls

### 1.1 The argument in one table

[ASSUMPTION/JUDGEMENT] The analyst's synthesis of Parts 2–6. A domain matters to the architecture through **five consequence properties**, not through its name.

| Consequence property | What it asks | Where it is legally anchored (examples) | Control it forces |
| --- | --- | --- | --- |
| **Legal or similarly significant effect on a person** | Does the output decide or strongly shape a decision about a natural person? | GDPR Art. 22; AI Act Annex III + Art. 86; SCHUFA C-634/21 | Human intervention route, contestation, explanation of the system's role |
| **Irreversibility** | Can the effect be undone cheaply and completely? | (Implicit in all; explicit in AI Act Art. 14(4)(d) "override or reverse") | Approval before commit; compensation path; hold periods |
| **Asymmetry of power / burden of proof** | Must the affected person prove the system wrong? | Robodebt, MiDAS, Dutch childcare benefits | Agency carries the evidential burden; no "debt by default" |
| **Professional duty of the human in the loop** | Is a licensed person accountable for the output? | Rule 11 (Mata v. Avianca); ABA Op. 512; FDA CDS criterion 4 | Verifiable sources; human must be able to review the basis |
| **Representation to the public** | Does the organisation speak through the agent? | Moffatt v. Air Canada; AI Act Art. 50 | Grounding on authoritative policy; disclosure; organisation owns the words |

### 1.2 What this means for the book

- [ASSUMPTION/JUDGEMENT] The same agent pattern (retrieve, reason, call a tool) needs different controls in a coding sandbox and in a benefits office. The difference is not model quality; it is **who bears the cost of an error, how fast it can be reversed, and who must be able to explain it**.
- [ASSUMPTION/JUDGEMENT] Regulation rarely names an architecture. It names **properties** — logs that allow traceability, oversight that allows override, information that allows interpretation. The architect's job is to map each property to a component.

**Durable vs volatile.** Durable: consequence-driven control selection; the five properties above. Volatile: which statute applies on which date (⚠ see Part 2).

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Classify every agent action by consequence property at design time, store the classification next to the tool definition, and let the classification (not the model) select the approval, logging and reversal path.

---

## PART 2: EU AI Act — high-risk categories and obligations

### 2.1 Annex III categories relevant to agentic systems

The AI Act (Regulation (EU) 2024/1689) lists stand-alone high-risk uses in Annex III. The ones that agentic enterprise systems most often touch:

| Annex III point | Wording (abridged quote) | Typical agentic use that could fall in scope |
| --- | --- | --- |
| 4(a) Employment | "AI systems intended to be used for the recruitment or selection of natural persons" | CV screening agent, interview scheduling that filters candidates |
| 4(b) Employment | "AI systems intended to be used to make decisions affecting terms of work-related relationships" (incl. promotion, termination, task allocation, monitoring) | HR copilot that drafts performance outcomes; workforce allocation agent |
| 5(a) Public benefits | "to evaluate the eligibility of natural persons for essential public assistance benefits and services" | Benefits caseworker assistant |
| 5(b) Credit | "AI systems intended to be used to evaluate the creditworthiness of natural persons" (fraud detection excluded) | Lending-ops agent that scores or pre-decides applications |
| 5(c) Insurance | "risk assessment and pricing in relation to natural persons in the case of life and health insurance" | Underwriting assistant |
| 5(d) Emergency | "evaluate and classify emergency calls by natural persons" | Triage agent |

[VERIFIED: https://artificialintelligenceact.eu/annex/3/, n.d., accessed 2026-10] (consolidated reading site; wording cross-checked against the Official Journal text fetched from the EU Publications Office, CELEX 32024R1689).

- **The Article 6(3) derogation.** An Annex III system is *not* high-risk where it "does not pose a significant risk of harm … including by not materially influencing the outcome of decision making", if it performs "a narrow procedural task", improves "the result of a previously completed human activity", detects decision patterns without replacing human assessment "without proper human review", or performs "a preparatory task". But "an AI system referred to in Annex III shall always be considered to be high-risk where the AI system performs profiling of natural persons." A provider relying on the derogation "shall document its assessment" before placing it on the market [VERIFIED: http://publications.europa.eu/resource/celex/32024R1689, published 2024-07-12].
- [ASSUMPTION/JUDGEMENT] The derogation is the most architecturally important clause for agents. An agent that *drafts* a summary for a human who then decides may qualify as "preparatory"; an agent that *ranks* candidates is profiling and is always high-risk. Whether the agent's output "materially influences" the outcome is partly a design choice (what the human sees first, whether they can see the raw inputs, whether the default is accept).

### 2.2 Application dates after the Digital Omnibus on AI ⚠

| Provision | Original date | Date after Regulation (EU) 2026/1744 |
| --- | --- | --- |
| Prohibited practices (Art. 5), AI literacy (Art. 4) | 2 Feb 2025 | Unchanged; two **new** prohibitions (non-consensual intimate imagery, CSAM generation) apply from **2 Dec 2026** |
| GPAI model obligations | 2 Aug 2025 | Unchanged |
| Transparency (Art. 50) | 2 Aug 2026 | Applies from 2 Aug 2026; Art. 50(2) **marking** gets a transition to **2 Dec 2026** for generative systems already on the market before 2 Aug 2026 |
| High-risk, Annex III (Art. 6(2)) — Chapter III Sections 1–3 | 2 Aug 2026 | **2 Dec 2027** |
| High-risk, Annex I (Art. 6(1)) — product-embedded | 2 Aug 2027 | **2 Aug 2028** |

- The Omnibus is "Regulation (EU) 2026/1744 … of 8 July 2026 amending Regulations (EU) 2024/1689, (EU) 2018/1139 and (EU) 2023/1230 … (Digital Omnibus on AI)", published in the Official Journal L series on 24.7.2026 [VERIFIED: http://publications.europa.eu/resource/celex/32026R1744, published 2026-07-24].
- Amended Art. 113: "Chapter III, Sections 1, 2, and 3, with the exception of Article 6(5), shall apply from: (i) 2 December 2027 as regards AI systems classified as high-risk pursuant to Article 6(2) and Annex III; and (ii) 2 August 2028 as regards AI systems classified as high-risk pursuant to Article 6(1) and Annex I" [VERIFIED: http://publications.europa.eu/resource/celex/32026R1744, published 2026-07-24].
- The recital's stated reason: the original 2 August 2026 date risked "a significant increase in implementation costs" without the supporting standards and guidance being ready [VERIFIED: same, 2026-07-24].
- Generative systems placed on the market before 2 August 2026 "shall take the necessary steps in order to comply with Article 50(2) by 2 December 2026" [VERIFIED: same, 2026-07-24].
- Article 4 (AI literacy) was **softened**: from an obligation to "ensure" AI literacy to "Providers and deployers of AI systems shall take measures to support the development of AI literacy of their staff" [VERIFIED: same, 2026-07-24].
- Registration of Art. 6(3) "not high-risk" self-assessments in the EU database was retained but simplified [VERIFIED: same, 2026-07-24].
- Entry into force on the third day after publication, i.e. 27 July 2026 [VERIFIED: same; date also reported by https://natlawreview.com/article/eu-digital-omnibus-ai-enters-force, published 2026-07-31].
- [WIDELY REPORTED: https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-omnibus-vii-deadline-delay-20260/, 2026] Commentators describe the new date as a schedule change, not a reprieve: harmonised standards and conformity-assessment preparation continue.

**Writer's warning.** Do not write "high-risk obligations apply from August 2026". As of 28 October 2026 the Annex III obligations have **not yet applied**; they apply from 2 December 2027. Art. 50 transparency **does** apply now.

### 2.3 The obligations that bite on agent architecture

All quotes below are from the Official Journal text of Regulation (EU) 2024/1689 [VERIFIED: http://publications.europa.eu/resource/celex/32024R1689, published 2024-07-12]. The Omnibus did not rewrite Articles 9 and 12–15 in the passages quoted (checked by text search of the Omnibus; [ASSUMPTION/JUDGEMENT] a full article-by-article diff was not performed).

| Article | What it requires (quoted or close paraphrase) | Architectural reading [ASSUMPTION/JUDGEMENT] |
| --- | --- | --- |
| **Art. 9 Risk management** | "a continuous iterative process planned and run throughout the entire lifecycle", covering intended use **and** "reasonably foreseeable misuse", with residual risk "judged to be acceptable" | Evaluation suites and red-team results are risk-management evidence, not just QA artefacts; prompt injection is "foreseeable misuse" |
| **Art. 12 Record-keeping** | systems "shall technically allow for the automatic recording of events (logs) over the lifetime of the system", enabling identification of risk situations, post-market monitoring, and deployer monitoring under Art. 26(5) | Trace every model call, tool call, retrieved document reference and human approval with a correlation ID; logs are a product feature, not an ops convenience |
| **Art. 13 Transparency to deployers** | operation "sufficiently transparent to enable deployers to interpret a system's output and use it appropriately"; instructions for use must state accuracy metrics, foreseeable risk circumstances and "where applicable, the technical capabilities … to provide information that is relevant to explain its output" | An agent's provider must document what tools it can call, what data it sees, and its measured failure modes |
| **Art. 14 Human oversight** | "effectively overseen by natural persons"; measures "commensurate with the risks, level of autonomy and context of use"; overseers must be able to understand limits, "remain aware of the possible tendency of … over-relying on the output … (automation bias)", interpret output, and "decide … not to use the high-risk AI system or to otherwise disregard, override or reverse the output" and to interrupt it | Override and stop must be real controls on the action path, not a comment box; "level of autonomy" is explicitly a scaling variable |
| **Art. 15 Accuracy, robustness, cybersecurity** | "appropriate level of accuracy, robustness, and cybersecurity … consistently … throughout their lifecycle"; accuracy metrics declared; "as resilient as possible regarding errors, faults or inconsistencies"; resilience "against attempts by unauthorised third parties to alter their use, outputs or performance"; feedback-loop mitigation for systems that keep learning | Prompt injection and tool poisoning are Art. 15(5) issues; model or prompt changes need regression evidence |
| **Art. 26 Deployer duties** | assign oversight to people with "the necessary competence, training and authority"; monitor operation; keep logs "of at least six months"; employers must inform workers' representatives and affected workers before workplace use (26(7)); deployers of Annex III systems making or assisting decisions about people "shall inform the natural persons" (26(11)) | Retention floor of six months for agent traces under the deployer's control; worker-notice is a launch gate for HR agents |
| **Art. 27 FRIA** | public bodies, private entities providing public services, and deployers of 5(b) credit and 5(c) insurance systems must perform a fundamental-rights impact assessment before deployment | Benefits and lending agents need an FRIA artefact before go-live |
| **Art. 50 Transparency for certain AI systems** | systems "intended to interact directly with natural persons" must inform them "that they are interacting with an AI system, unless this is obvious" | Customer-facing agents must disclose; applies from 2 Aug 2026 ⚠ |
| **Art. 86 Right to explanation** | an affected person subject to a deployer's decision "on the basis of the output from a high-risk AI system listed in Annex III" with legal or similarly significant adverse effect may obtain "clear and meaningful explanations of the role of the AI system in the decision-making procedure and the main elements of the decision taken" | The trace must let the deployer reconstruct *the AI system's role*, not just the final answer |

- Art. 14(5) adds a "four-eyes" rule for remote biometric identification (Annex III point 1(a)): no action unless the identification "has been separately verified and confirmed by at least two natural persons" [VERIFIED: http://publications.europa.eu/resource/celex/32024R1689, 2024-07-12]. [ASSUMPTION/JUDGEMENT] This is the Act's only explicit dual-control rule; it is a useful template for irreversible agent actions elsewhere, but it is not legally required outside biometrics.
- Art. 12(3) lists the **minimum** log fields only for biometric identification (period of use, reference database, matched input, identity of verifying persons) [VERIFIED: same]. [ASSUMPTION/JUDGEMENT] For other Annex III systems the Act sets purposes, not fields; harmonised standards (⚠ still in preparation per the Omnibus recitals) are expected to fill this gap.

**Durable vs volatile.** Durable: logging for traceability, oversight with real override, documented limits, robustness against manipulation — these principles predate the Act and appear in sector rules. Volatile ⚠: application dates (already moved once), harmonised standards, Commission guidelines on Art. 6 classification, the exact scope of Art. 4.

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- Build to Arts. 12–14 now even though Annex III applies from December 2027: retrofitting traceability into an agent that was not designed for it is expensive, and 2027 is one product cycle away.
- Treat "level of autonomy" (Art. 14(3)) as a configuration dimension per tool and per tenant, so oversight can be increased without code changes.
- Keep the Art. 6(3) assessment as a versioned artefact tied to the agent's tool list. Adding a tool that ranks or decides about people can flip the classification.

---

## PART 3: GDPR Article 22 and the SCHUFA judgment

### 3.1 The text

- GDPR Art. 22(1): "The data subject shall have the right not to be subject to a decision based solely on automated processing, including profiling, which produces legal effects concerning him or her or similarly significantly affects him or her." Exceptions in 22(2): necessary for a contract, authorised by law with safeguards, or explicit consent. Under 22(3), for the contract and consent routes the controller must provide "at least the right to obtain human intervention on the part of the controller, to express his or her point of view and to contest the decision" [VERIFIED: http://publications.europa.eu/resource/celex/32016R0679, published 2016-05-04].

### 3.2 SCHUFA (C-634/21), CJEU, 7 December 2023

- The Court (First Chamber) ruled that "the automated establishment, by a credit information agency, of a probability value based on personal data … concerning his or her ability to meet payment commitments in the future constitutes 'automated individual decision-making' within the meaning of [Art. 22(1)], where a third party, to which that probability value is transmitted, draws strongly on that probability value to establish, implement or terminate a contractual relationship with that person" [VERIFIED: http://publications.europa.eu/resource/celex/62021CJ0634, published 2023-12-07].
- [ASSUMPTION/JUDGEMENT] The architectural lesson is that **the "decision" can sit upstream of the human who formally decides**. If a downstream human "draws strongly" on a score, the score itself is the automated decision. An agent that produces a recommendation which loan officers, HR staff or caseworkers routinely accept is at risk of the same reading, even if a human clicks "approve". A human in the loop who rubber-stamps does not take the system out of Art. 22.
- [ASSUMPTION/JUDGEMENT] Evidence that oversight is real — override rates, time spent per decision, cases where the human disagreed — is therefore not only an Art. 14 AI Act matter but also the main defence that a decision is not "solely" automated.

### 3.3 Pending GDPR changes ⚠

- The Commission proposed a wider Digital Omnibus on 19 November 2025 including GDPR amendments; one proposal would clarify that an automated decision may be taken even where a human could reach the same outcome [WIDELY REPORTED: https://www.gibsondunn.com/eu-digital-omnibus-package-a-first-look-at-the-commission-draft-proposals/, 2025].
- EDRi reported in March 2026 that "the proposal to weaken Article 22 … is no longer present" in the text then under negotiation [WIDELY REPORTED: https://edri.org/our-work/the-digital-omnibus-a-step-back-from-the-brink-but-the-risks-remain/, 2026-03]. Another secondary source describes a May 2026 provisional agreement that keeps a reworded Art. 22. **Not verified; the two accounts conflict.** Writers should cite the 2016 text and flag that amendments are pending.

**Durable vs volatile.** Durable: the right to human intervention and contestation for significant automated decisions; SCHUFA's "draws strongly" test (a CJEU interpretation, binding on national courts). Volatile ⚠: the wording of Art. 22 if the GDPR omnibus is adopted.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Provide a contest-and-review path as a first-class workflow (ticket, reviewer assignment, re-run with the person's submitted facts), measure whether reviewers actually depart from the agent's recommendation, and store the inputs the agent used so a reviewer can see them.

---

## PART 4: Sector rules — healthcare, finance, legal

### 4.1 Healthcare: FDA clinical decision support (CDS) and AI-enabled device software

- **Revised CDS guidance, January 2026.** FDA issued a revised final "Clinical Decision Support Software" guidance on 6 January 2026, superseding the September 2022 version, without a formal comment period [WIDELY REPORTED: https://www.cooley.com/news/insight/2026/2026-01-20-automation-bias-and-clinical-practice-fda-makes-incremental-updates-to-clinical-decision-support-software-guidance, 2026-01-20]. The FDA guidance page lists the document as **Final**, docket FDA-2017-D-6569, with content "current as of 01/29/2026" [VERIFIED: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/clinical-decision-support-software, published 2026-01]. ⚠ One secondary source says a further revision was issued 29 January 2026; this could not be confirmed and may simply be a page update.
- **The four statutory criteria** (FD&C Act §520(o)(1)(E)) for non-device CDS: (1) does not acquire, process or analyse a medical image or signal; (2) displays, analyses or prints medical information; (3) supports or provides recommendations to a health-care professional (HCP); (4) lets the HCP "independently review the basis" for the recommendations so they do not rely primarily on them [WIDELY REPORTED: Cooley, 2026-01-20].
- **What changed from 2022.** The 2022 guidance effectively required more than one recommendation; the 2026 guidance says a **single recommendation** can be non-device CDS. Risk scores are no longer strictly barred. Time-critical outputs (requiring immediate response) still tend to be device functions, now analysed under criteria 3 and 4. Automation bias is discussed under criterion 4 [WIDELY REPORTED: Cooley, 2026-01-20]. The guidance remains HCP-facing only; patient-facing tools such as symptom checkers got no new policy [WIDELY REPORTED: https://www.cov.com/en/news-and-insights/insights/2026/01/5-key-takeaways-from-fdas-revised-clinical-decision-support-cds-software-guidance, 2026-01].
- **LLMs are not specifically addressed** in the commentary read [WIDELY REPORTED: Cooley, 2026-01-20]. [ASSUMPTION/JUDGEMENT] For a generative clinical assistant, criterion 4 is the hard one: an HCP can only "independently review the basis" if the agent shows the sources and data it used. An LLM's free-text rationale is not obviously "the basis".
- **AI-enabled device software functions.** "Artificial Intelligence-Enabled Device Software Functions: Lifecycle Management and Marketing Submission Recommendations" is still a **draft** (January 2025; docket FDA-2024-D-4488; "Not for implementation") as of this fetch [VERIFIED: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/artificial-intelligence-enabled-device-software-functions-lifecycle-management-and-marketing, published 2025-01-07]. ⚠ Finalisation was expected; check before citing.
- The separate guidance on **Predetermined Change Control Plans (PCCP)** for AI-enabled device software functions was finalised in December 2024 [WIDELY REPORTED: https://healthcareitnews.com/node/555567, 2024]. [ASSUMPTION/JUDGEMENT] A PCCP is the regulatory form of "pre-agreed change envelope": the closest existing analogue to letting an agent's model or prompt change without a new submission.
- **HIPAA minimum necessary.** 45 CFR 164.502(b): when using, disclosing or requesting PHI, a covered entity or business associate "must make reasonable efforts to limit protected health information to the minimum necessary to accomplish the intended purpose of the use, disclosure, or request." It does **not** apply to disclosures to a provider for treatment, to the individual, under authorisation, to HHS, or as required by law [VERIFIED: https://www.law.cornell.edu/cfr/text/45/164.502, n.d., accessed 2026-10]. 45 CFR 164.514(d)(2) requires identifying "persons or classes of persons … in its workforce who need access" and "the category or categories of protected health information to which access is needed" [VERIFIED: https://www.law.cornell.edu/cfr/text/45/164.514, n.d., accessed 2026-10].
- [ASSUMPTION/JUDGEMENT] Minimum necessary maps directly onto agent **context assembly**: an agent is a "class of person" in the workforce sense, and the retrieval layer must limit which PHI categories it can pull per task. "Give the agent the whole chart in case it helps" is the anti-pattern. The treatment exception is narrow and does not cover, for example, billing or operations agents.
- ⚠ HHS proposed a HIPAA Security Rule update in January 2025 (not verified in this session; status unknown).

### 4.2 Finance: SOX and segregation of duties; model risk management

- **SOX §404 does not mention segregation of duties.** 15 U.S.C. 7262(a) requires management to state its responsibility for "an adequate internal control structure and procedures for financial reporting" and to assess its effectiveness; (b) requires auditor attestation [VERIFIED: https://www.law.cornell.edu/uscode/text/15/7262, n.d., accessed 2026-10]. Segregation of duties (SoD) is a control expectation that comes from the internal-control frameworks (COSO) and audit practice used to assess §404, not from the statute [ASSUMPTION/JUDGEMENT; the PCAOB AS 2201 page returned 403].
- [ASSUMPTION/JUDGEMENT] For finance-operations agents the SoD question is concrete: **an agent that can both create a vendor and approve a payment to it collapses two duties into one identity.** Auditors will ask whether the agent's service identity holds conflicting entitlements, and whether a human approval is genuinely independent. The control is identity-level (separate service principals per duty, non-overlapping tool sets), not prompt-level.
- **SR 11-7 has been replaced.** SR 26-2, "Revised Guidance on Model Risk Management", dated 17 April 2026, issued jointly by the Federal Reserve, FDIC and OCC, "supersedes and replaces" SR 11-7 (4 April 2011) and SR 21-8 (BSA/AML models, 2021). It "is expected to be most relevant to banking organizations with over $30 billion in total assets" and emphasises "a risk-based approach" [VERIFIED: https://www.federalreserve.gov/supervisionreg/srletters/sr2602.htm, published 2026-04-17].
- **Generative and agentic AI are explicitly out of scope.** The attachment states: "Generative AI and agentic AI models are novel and rapidly evolving. As such, they are not within the scope of this guidance. Nonetheless, a banking organization's risk management and governance practices should guide the determination of appropriate governance and controls for any tools, processes, or systems not covered in this document. However, the principles described in this guidance apply to traditional statistical and quantitative models and non-generative, non-agentic AI models" [VERIFIED: https://www.federalreserve.gov/supervisionreg/srletters/SR2602a1.pdf, published 2026-04-17].
- SR 26-2 defines a model as "a complex quantitative method, system, or approach that applies statistical, economic, or financial theories to process input data into quantitative estimates", excluding "deterministic rule-based processes" [VERIFIED: same]. It keeps **"effective challenge"** — "critical analysis conducted by objective experts" with "sufficient independence" and "the organizational standing and influence to effect any change" — and keeps vendor models in scope: "the principles of model risk management remain applicable" even without access to vendor code or data [VERIFIED: same].
- Parallel actions: OCC Bulletin 2026-13 and FDIC FIL-15-2026 [WIDELY REPORTED: https://www.orrick.com/en/Insights/2026/04/Agencies-Overhaul-Model-Risk-Management-Guidance-for-Banks-Heres-What-Changed, 2026-04].
- [ASSUMPTION/JUDGEMENT] This creates a **governance gap that the book should name**: US bank supervisors have no model-risk guidance for LLM agents as of October 2026. Banks will likely extend SR 11-7-style practice (inventory, tiering, independent validation, ongoing monitoring) by analogy, as the "Nonetheless" sentence invites. A credit-related agent used in the EU is still Annex III 5(b) high-risk from December 2027.

### 4.3 Legal: Mata v. Avianca and ABA Formal Opinion 512

- **Mata v. Avianca, Inc.**, No. 22-cv-1461 (PKC) (S.D.N.Y.), Opinion and Order on Sanctions, Judge P. Kevin Castel, 22 June 2023. The court wrote that "there is nothing inherently improper about using a reliable artificial intelligence tool for assistance. But existing rules impose a gatekeeping role on attorneys to ensure the accuracy of their filings. Rule 11." The respondents "abandoned their responsibilities when they submitted non-existent judicial opinions with fake quotes and citations created by the artificial intelligence tool ChatGPT, then continued to stand by the fake opinions after judicial orders called their existence into question" [VERIFIED: https://storage.courtlistener.com/recap/gov.uscourts.nysd.575368/gov.uscourts.nysd.575368.54.0.pdf, published 2023-06-22].
- Sanctions: letters to the client and to "each judge falsely identified as the author of the fake" opinions, attaching the order and transcripts; and "A penalty of $5,000 is jointly and severally imposed on Respondents" [VERIFIED: same]. Evidence age: 2023, a chat assistant, not an agent — the principle (the human signatory owns the output) is durable.
- [ASSUMPTION/JUDGEMENT] The aggravating factor was not the hallucination but the **failure to verify after a challenge**. For legal-research agents, the architectural answer is citation resolution against an authoritative database as a hard post-condition: an unresolvable citation blocks the draft rather than being flagged in prose.
- **ABA Formal Opinion 512, "Generative Artificial Intelligence Tools"**, ABA Standing Committee on Ethics and Professional Responsibility, 29 July 2024 — the committee's first formal opinion on lawyers' AI use [WIDELY REPORTED: https://thebarexaminer.ncbex.org/article/fall-2024/generative-artificial-intelligence-tools/, 2024]. As summarised by a committee member: the degree of review required "will necessarily depend on the GAI tool and the specific task that it performs"; "a client's informed consent is required prior to inputting information relating to the representation" into self-learning tools and "Boilerplate waivers will not suffice"; "Managerial lawyers must establish clear policies regarding the law firm's permissible use of GAI"; and lawyers "may not charge clients for time necessitated by their own inexperience" [WIDELY REPORTED: same, 2024]. ABA opinions are not binding law; state bars adopt their own rules [WIDELY REPORTED: https://zuva.ai/blog/aba-formal-opinion-512/, 2024].
- [ASSUMPTION/JUDGEMENT] The informed-consent point is an **architecture** constraint: whether client data is used to train or persists across tenants decides whether consent is needed. Zero-retention, tenant-isolated deployments change the ethics analysis, so the data-flow diagram belongs in the firm's AI policy.

**Durable vs volatile.** Durable: minimum necessary; SoD; independent challenge of models; the professional signatory owns the output; HCP must be able to review the basis. Volatile ⚠: FDA guidance status and wording; SR 26-2's AI exclusion (likely to be revisited); state bar rules.

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- Healthcare: purpose-scoped retrieval per task; show sources to the clinician by default; treat time-critical recommendations as device-grade.
- Finance: one service identity per duty; no agent identity holds create-and-approve over the same object; inventory agents in the model-risk register even though SR 26-2 excludes them.
- Legal: deterministic citation verification as a gate; no client data into tools that train on it without consent.

---

## PART 5: Cautionary cases — automated public-benefits decisions (not LLM systems)

These three cases are **rule-based or classical-ML systems from 2013–2020**. They are in the book because agentic systems are now being proposed for the same casework, and the failure mechanisms — reversed burden of proof, missing human review, unexplained risk flags, incentives to recover money — do not depend on the model type.

### 5.1 Australia: Robodebt (Royal Commission report, 7 July 2023)

- The scheme used "income averaging" of annual tax-office income across fortnights to assess benefit overpayments going back to 2010–11. It continued until November 2019, when debts stopped being raised solely on averaged income; a class action was settled in 2020 and averaging-based debts were reduced to zero; the Prime Minister apologised in June 2020. The Royal Commission's Final Report (released 7 July 2023) found the scheme "produced inaccurate results and did not comply with the income calculation provisions of the Social Security Act" [WIDELY REPORTED: https://www.apra.gov.au/sites/default/files/2024-02/Robodebt%20Royal%20Commision%20-%20Overview%20of%20Final%20Report.pdf, 2024-02] (an overview written by APRA, not the report itself).
- Commissioner's preface (quoted in the overview): "It is remarkable how little interest there seems to have been in ensuring the Scheme's legality, how rushed its implementation was, how little thought was given to how it would affect welfare recipients…" and on "the ineffectiveness of what one might consider institutional checks and balances" [WIDELY REPORTED: same].
- 57 recommendations, including reform of automated decision-making legislation and a body to monitor and audit automated decision-making; "Robodebt was a crude and cruel mechanism, neither fair nor legal, and it made many people feel like criminals." The class action settlement exceeded A$720 million; it covered about 430,000 debts [WIDELY REPORTED: https://lsj.com.au/articles/crude-cruel-and-unlawful-robodebt-royal-commission-findings/, 2023-08-09].
- The ADM recommendations are numbered 17.1 (legislative framework, review path) and 17.2 (monitoring and audit body) [WIDELY REPORTED: search summaries of https://aph.gov.au/About_Parliament/Parliamentary_departments/Parliamentary_Library/FlagPost/2023/July/Robodebt-RC-legislative-recommendations, 2023; the page itself returned 403].
- [ASSUMPTION/JUDGEMENT] Lesson for agents: **the method was wrong in law before any software ran**. No amount of accuracy engineering fixes an action the organisation has no authority to take. An agent's tool list must be derived from what the organisation is legally permitted to do, reviewed by counsel.

### 5.2 Netherlands: childcare benefits scandal (toeslagenaffaire)

- The tax authority introduced an algorithmic risk-classification system in 2013 to flag incorrect childcare-benefit claims. Nationality was a risk factor; Amnesty describes the system as self-learning, reinforcing bias in a "discriminatory loop"; civil servants reviewing flagged cases "were not told why the system had assigned a high risk score" — a "black box system" producing "a black hole of accountability". Tens of thousands of parents were falsely accused of fraud; the government resigned in January 2021 [VERIFIED: https://www.amnesty.org/en/latest/news/2021/10/xenophobic-machines-dutch-child-benefit-scandal/, published 2021-10-25].
- The Dutch DPA fined the Tax and Customs Administration €2.75 million in December 2021 for discriminatory and unlawful processing of (dual) nationality data [WIDELY REPORTED: https://iapp.org/news/a/dutch-dpa-fines-tax-authority-2-75m-euros, 2021; https://dutchnews.nl/2021/12/tax-office-fined-e2-7m-for-discriminating-against-dual-national-families, 2021-12]. A separate €3.7 million fine followed in April 2022 for a fraud-suspect blacklist [WIDELY REPORTED: https://dutchnews.nl/2022/04/tax-office-fined-e3-7m-for-breaking-privacy-law-with-fraud-suspect-blacklist, 2022-04].
- [ASSUMPTION/JUDGEMENT] Lesson: **human review without the reason for the flag is not oversight**. This is exactly what AI Act Art. 14(4)(a)–(c) now requires (understand limits, be aware of automation bias, interpret the output). An agent that escalates to a human must hand over the evidence and the features that drove the escalation, not just a label.

### 5.3 Michigan: MiDAS unemployment-fraud determinations (2013–2015)

- Michigan's Unemployment Insurance Agency deployed the Michigan Integrated Data Automated System (MiDAS) to detect fraud; it "wrongly accused approximately 40,000 Michiganders of fraud between 2013 and 2015" and stripped benefits; "the system's error rate reached 93%"; "neither the agency nor the state itself could offer evidence backing MiDAS's fraud claims". The Court of Claims approved a $20 million settlement in *Bauserman v. Michigan UIA* for about 3,000 claimants in late January 2024 [WIDELY REPORTED: https://stpp.fordschool.umich.edu/sites/stpp/files/2024-08/stpp-midas-explainer.pdf, 2024-08] (a University of Michigan student case summary).
- Secondary reporting attributes the 93% figure to a state review of determinations made with no human involvement, versus 44% where a human was involved [WIDELY REPORTED: https://www.govtech.com/health/michigan-makes-amends-for-falsely-accusing-thousands-of-unemployment-fraud.html, 2017]. ⚠ The 44% contrast was not verified against the state's own review.
- [ASSUMPTION/JUDGEMENT] Lesson: **an automated determination that triggers penalties and collection must carry its evidence**. If the system cannot show why it decided, the organisation cannot defend the decision. For agents, this is the case for persisting the tool outputs and retrieved records that support each action, not only the final summary.

**Durable vs volatile.** Durable: all three lessons. The cases are old and settled; the numbers will not change. Volatile: national ADM legislation in Australia and the Netherlands that followed (not researched here).

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- No agent action that creates a debt, penalty or loss of benefit without a human decision that has the evidence in front of it.
- The burden of proof stays with the organisation: the agent must attach evidence, and absence of evidence must default to "no adverse action".
- Monitor the **reversal rate** of agent-assisted adverse decisions on appeal; it is the leading indicator all three schemes ignored.

---

## PART 6: Customer-facing liability and documented deployments

### 6.1 Moffatt v. Air Canada, 2024 BCCRT 149 (14 February 2024)

- An Air Canada website chatbot told a customer he could apply for a bereavement fare retroactively; the policy said otherwise. The BC Civil Resolution Tribunal held the airline liable for negligent misrepresentation: the airline is responsible for information on its website whether on a static page or via a chatbot; the customer had no reason to know one part of the site was accurate and another not; the airline did not take reasonable care to ensure the chatbot was accurate. The customer was awarded $650.88 in damages [WIDELY REPORTED: https://www.mltaikins.com/insights/that-wasnt-me-that-was-my-chatbot, 2024-05-24]. The tribunal called Air Canada's argument that the chatbot was responsible for its own actions "a remarkable submission" [WIDELY REPORTED: https://www.law360.ca/ca/articles/1804075, 2024]. Total ordered including interest and fees was reported as about CA$812 [WIDELY REPORTED: https://foxbusiness.com/lifestyle/air-canada-chatbot-gave-customer-wrong-info-airline-pay, 2024].
- It is not public whether the chatbot used an LLM [ASSUMPTION/JUDGEMENT; none of the sources read say so]. The decision is a small-claims tribunal ruling, not binding precedent, but it is widely cited.
- [ASSUMPTION/JUDGEMENT] Lesson: **the organisation owns every statement its agent makes**. Policy statements (refunds, eligibility, prices) should be generated from, or checked against, the authoritative policy source, and an agent that cannot ground a policy answer should hand off rather than paraphrase.

### 6.2 Klarna AI assistant: the 2024 claim and the 2025 qualification ⚠

- **The claim (vendor press release, 27 February 2024).** Klarna's OpenAI-powered assistant had "2.3 million conversations, two-thirds of Klarna's customer service chats" in its first month; doing "the equivalent work of 700 full-time agents"; customer satisfaction "on par with human agents"; "25% drop in repeat inquiries"; resolution "in less than 2 mins compared to 11 mins previously"; "23 markets, 24/7", "more than 35 languages"; "estimated to drive a $40 million USD in profit improvement to Klarna in 2024" [VERIFIED: https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/, published 2024-02-27].
- These are **company-reported, unaudited, first-month figures**, and the profit number is an estimate [ASSUMPTION/JUDGEMENT]. The satisfaction comparison method was not described.
- **The qualification (May 2025).** CEO Sebastian Siemiatkowski told Bloomberg: "As cost unfortunately seems to have been a too predominant evaluation factor when organizing this, what you end up having is lower quality", and "Really investing in the quality of the human support is the way of the future for us." A Klarna spokesperson told Fortune "we're very much still AI-first"; the company was piloting freelance human agents (two had started) [WIDELY REPORTED: https://www.fortune.com/2025/05/09/klarna-ai-humans-return-on-investment, 2025-05-09].
- **How to describe it.** It is a partial walk-back on quality and staffing strategy, **not** a withdrawal of the assistant; press headlines saying Klarna "replaced AI with humans" overstate it [ASSUMPTION/JUDGEMENT, based on the Fortune and tech.co reporting]. Evidence age: 2024–2025; current share of chats handled by the assistant was not verified.
- [ASSUMPTION/JUDGEMENT] Lesson: **headline deflection numbers measure cost, not outcome quality**. Evaluation of support agents needs quality metrics (re-contact, escalation correctness, complaint rate, sampled human grading), and the business case should be judged on those.

### 6.3 Other documented deployments

- No other enterprise agent deployment with public outcome numbers was verified to primary-source standard in this session. Writers using vendor case studies (support-platform resolution rates, bank copilot hours saved) should tag them as vendor claims and state what was measured and by whom [ASSUMPTION/JUDGEMENT].

**Durable vs volatile.** Durable: organisational liability for agent statements; disclosure duties (AI Act Art. 50 ⚠ in force Aug 2026); the distinction between cost metrics and quality metrics. Volatile ⚠: any vendor's deployment numbers.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Ground policy answers on a versioned policy store and log which version answered; disclose the agent; design human handoff as a measured path, not a failure; track quality metrics before claiming savings.

---

## PART 7: Coding agents — documented architecture and measured effect

Coding agents are the domain with the **lowest external consequence per action and the best reversibility** (version control, review, CI), which is why they are the most autonomous agents in production. They are also the domain where the most public, primary documentation of control architecture exists.

### 7.1 Claude Code (Anthropic) ⚠ product details change frequently

- **Permission modes.** `default` (labelled Manual; prompts on first use of each tool), `acceptEdits` (auto-accepts edits and common filesystem commands within the working directories), `plan` (reads and explores, does not edit source), `auto` ("a background classifier … checks that they align with your request" before actions such as shell commands and network requests), `dontAsk` (auto-denies anything that would prompt; pre-approved tools still run), `bypassPermissions` (skips prompts except for actions no mode auto-approves) [VERIFIED: https://code.claude.com/docs/en/permissions, n.d., accessed 2026-10].
- **Rule evaluation.** "Rules are evaluated in order: deny, then ask, then allow. The first match in that order determines the outcome, and rule specificity doesn't change the order." A bare tool name in a deny rule removes the tool from the model's context entirely [VERIFIED: same]. Read/Edit deny rules do not apply to arbitrary subprocesses (e.g. a Python script that opens files itself): "For OS-level enforcement that blocks all processes from accessing a path, enable the sandbox" [VERIFIED: same].
- **Hooks.** Events include `PreToolUse`, `PostToolUse`, `PermissionRequest`, `SubagentStart`/`SubagentStop`, `Stop`, `SessionStart`, and others. Hook types: `command`, `http`, `mcp_tool`, `prompt`, and experimental `agent`. A `PreToolUse` hook blocks a call with exit code 2 or with JSON `permissionDecision: "deny"`; "Exit 0 with no output means no decision" — a hook can deny but silence does not approve [VERIFIED: https://code.claude.com/docs/en/hooks, n.d., accessed 2026-10]. Important caveat: "A non-zero exit other than 2 is a non-blocking error"; a timed-out `PreToolUse` hook does not block unless `onFailure: "block"` is set; the docs advise using the permission system, not hooks, for hard allow/deny rules [VERIFIED: same].
- **Subagents.** Each runs "in its own context window" with its own system prompt, model and tool allowlist (`tools`) or denylist (`disallowedTools`); subagents can spawn subagents up to three layers by default; "Only the subagent's final report returns to the main conversation" [VERIFIED: https://code.claude.com/docs/en/sub-agents, n.d., accessed 2026-10].
- **Sandboxing.** Off by default. Filesystem isolation (writes limited to working and added directories; protected paths such as `.claude/settings` and `.mcp.json` stay write-denied) and network isolation (traffic through a local proxy checking hostnames against `allowedDomains`, which starts empty). macOS uses Seatbelt; Linux/WSL2 use bubblewrap plus a network namespace; native Windows is not supported. Not covered: built-in file and web tools (governed by permission rules), hooks, local MCP servers and other helper processes, which "run with full access". An escape hatch `dangerouslyDisableSandbox` lets the model retry a command unsandboxed, approved according to the permission mode; it can be disabled with `allowUnsandboxedCommands: false` [VERIFIED: https://code.claude.com/docs/en/sandboxing, n.d., accessed 2026-10]. Reads are allowed across most of the machine by default, including credential files, unless restricted [VERIFIED: same].
- **Vendor claim:** "In our internal usage, we've found that sandboxing safely reduces permission prompts by 84%." No method given [VERIFIED: https://www.anthropic.com/engineering/claude-code-sandboxing, published 2025-10-20]. Treat as a vendor engineering claim.
- **MCP** servers are configured per user, project or organisation; managed settings can restrict them [VERIFIED (configuration surface only): https://code.claude.com/docs/en/permissions, n.d., accessed 2026-10]. Protocol details belong to the tools brief.

### 7.2 OpenAI Codex CLI ⚠

- **Sandbox modes:** `read-only`, `workspace-write` (the "Auto" preset: edit and run commands in the workspace), `danger-full-access` (no sandbox). **Approval policies:** `on-request` (sandboxed commands run; escalations such as writes outside the workspace or network need approval), `never` (no prompts; sandbox still applies), a granular policy, and an `approvals_reviewer` that can be `"user"` or `"auto_review"` (a reviewer agent). The older `untrusted` policy is **retired** [VERIFIED: https://learn.chatgpt.com/codex/agent-approvals-security, n.d., accessed 2026-10].
- **Defaults:** network off locally; writes limited to the workspace; version-controlled folders start in `workspace-write` + `on-request`, others `read-only`. OS mechanisms: Seatbelt on macOS, `bwrap` plus `seccomp` on Linux, MXC preferred on Windows. `.git`, `.codex`, `.agents` and `.aws` are protected read-only inside writable roots [VERIFIED: same].
- **Hooks:** `SessionStart`, `SessionEnd`, `PreToolUse`, `PermissionRequest`, `PostToolUse`, `PreCompact`, `PostCompact`, `UserPromptSubmit`, `SubagentStart`, `SubagentStop`, `Stop`, `Interrupt`; `PreToolUse` can deny a supported tool call; `PostToolUse` cannot undo a command that already ran; hooks are enabled by default [VERIFIED: https://learn.chatgpt.com/codex/hooks, n.d., accessed 2026-10]. Subagents and MCP have documentation pages that were not read.
- Evidence age: both vendors' docs are living pages; the Codex docs moved domain (developers.openai.com → learn.chatgpt.com) during 2026 [VERIFIED: redirect observed in this session].

### 7.3 Convergence between the two

| Control | Claude Code | Codex CLI |
| --- | --- | --- |
| OS sandbox | Seatbelt / bubblewrap; off by default | Seatbelt / bwrap+seccomp; on by default for workspace-write |
| Network default | Proxy allowlist (empty) when sandbox on | Off |
| Protected config paths | `.claude/settings`, `.mcp.json`, shell rc files | `.git`, `.codex`, `.agents`, `.aws` |
| Model-judged approvals | `auto` mode classifier | `auto_review` reviewer agent |
| Pre-execution hook that can deny | `PreToolUse` | `PreToolUse` |
| Escape hatch | `dangerouslyDisableSandbox` | `danger-full-access` |

[ASSUMPTION/JUDGEMENT] Two independent vendors converged on the same layered design: **OS-level sandbox as the hard boundary, rule-based permissions as policy, hooks as organisation-specific policy, and a model-based reviewer to reduce prompt fatigue**. Both document that the model-based layer is not the boundary. This is the strongest available evidence for the book's "bound the component" thesis, from the domain with the most deployment experience.

### 7.4 Research agents: SWE-agent and OpenHands

- **SWE-agent** (Yang et al., arXiv 2405.15793, v1 6 May 2024, v3 11 Nov 2024): introduces the "agent-computer interface (ACI)" — purpose-built commands for editing files, navigating repositories and running tests — arguing LM agents are a new kind of end user that benefits from purpose-built interfaces. Reported pass@1 of 12.5% on SWE-bench and 87.7% on HumanEvalFix, state of the art at the time [VERIFIED: https://arxiv.org/abs/2405.15793, published 2024-05-06]. Evidence age: >2 years; the numbers describe 2024 models and are long superseded. The durable finding is that **interface design for the agent changes outcomes**.
- **OpenHands** (formerly OpenDevin; Wang et al., arXiv 2407.16741, v3 18 Apr 2025; ICLR 2025): an open platform for agents that write code, use a command line and browse, with sandboxed execution, multi-agent coordination and 15 integrated benchmarks including SWE-bench and WebArena [VERIFIED: https://arxiv.org/abs/2407.16741, published 2024-07-23]. Peer-reviewed (ICLR 2025).

### 7.5 Measured productivity: METR and DORA

- **METR RCT (Becker, Rush, Barnes, Rein; arXiv 2507.09089, 12 July 2025).** 16 experienced open-source developers, 246 tasks in mature repositories they knew well (about 5 years' prior experience); tasks randomly assigned to allow or disallow AI; tools mainly Cursor Pro with Claude 3.5/3.7 Sonnet. "Allowing AI actually increases completion time by 19%." Developers forecast a 24% speedup beforehand and believed afterwards they had been sped up 20%; economics and ML experts predicted 39% and 38% reductions [VERIFIED: https://arxiv.org/abs/2507.09089, published 2025-07-12]. Preprint. Limitations: small n; one population (experts in familiar, mature codebases); early-2025 tools; the authors examined 20 possible contributing factors.
- **METR follow-up (24 February 2026).** A larger study from August 2025 (57 developers, 143 repositories, 800+ tasks; median 10 years' experience). Returning developers: estimated speedup 18%, CI reported as −38% to +9%; new developers: 4%, CI −15% to +9%. METR says the data gives only "very weak evidence": a growing share of developers refused to work without AI, and 30–50% withheld tasks they did not want to do without AI, so the estimate is likely a lower bound. METR is changing its design (shorter experiments, observational transcript analysis, fixed tasks) [VERIFIED: https://metr.org/blog/2026-02-24-uplift-update/, published 2026-02-24]. ⚠ The CI sign convention in the post's summary should be checked against METR's figure before quoting.
- **DORA 2025, "State of AI-assisted Software Development"** (Google Cloud, 23 September 2025): survey of "nearly 5,000 technology professionals" plus over 100 hours of qualitative data; 90% use AI at work; more than 80% believe it increased their productivity; 30% report little or no trust in AI-generated code; AI adoption now has a **positive** relationship with delivery throughput and product performance but "continues to have a negative relationship with software delivery stability" [VERIFIED: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report, published 2025-09-23]. Its headline framing: AI is "an amplifier", "magnifying an organization's existing strengths and weaknesses" [VERIFIED: https://dora.dev/research/2025/dora-report/, n.d., accessed 2026-10]. The DORA AI Capabilities Model names seven capabilities that amplify AI's benefits [VERIFIED (count only): same]; the names were not readable in this session. [ASSUMPTION/JUDGEMENT, from memory of the report] They are a clear AI stance, healthy data ecosystems, AI-accessible internal data, strong version control, small batches, user-centric focus and quality internal platforms — verify before quoting.
- **How the two disagree.** METR measures task time in a controlled experiment; DORA measures self-reported perception and survey correlations. METR's 2025 result shows perception can be the opposite of measurement. DORA's stability finding is consistent with "more change, same safety net" [ASSUMPTION/JUDGEMENT].

**Durable vs volatile.** Durable: layered control (OS sandbox → rules → hooks → model reviewer); ACI design matters; self-reported productivity is unreliable; AI raises change volume and so stresses stability controls. Volatile ⚠: every product setting name, default and mode in 7.1–7.2; benchmark numbers; the METR effect size, which is moving and currently unmeasurable by their design.

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- Copy the coding-agent stack into other domains: hard isolation at the OS or network layer, declarative rules, organisation hooks, and only then a model-based reviewer.
- Do not justify autonomy with self-reported productivity; measure task outcomes and stability (change-failure rate, rework) before raising autonomy.
- Coding agents are permissive because reversibility is cheap (git, CI, review). Where reversibility is expensive (Parts 4–6), the same autonomy is not justified.

---

## Key numbers

| Number | What it measured | Source | Date |
| --- | --- | --- | --- |
| 2 Dec 2027 | Application of AI Act high-risk obligations for Annex III systems (was 2 Aug 2026) | Reg. (EU) 2026/1744 | 2026-07-24 |
| 2 Aug 2028 | Application for Annex I (product-embedded) high-risk systems | Reg. (EU) 2026/1744 | 2026-07-24 |
| 2 Dec 2026 | Deadline for Art. 50(2) marking for generative systems on the market before 2 Aug 2026; new Art. 5 prohibitions | Reg. (EU) 2026/1744 | 2026-07-24 |
| ≥ 6 months | Minimum log retention for deployers of high-risk systems (Art. 26(6)) | Reg. (EU) 2024/1689 | 2024-07-12 |
| 2 persons | Separate verification required for remote biometric ID actions (Art. 14(5)) | Reg. (EU) 2024/1689 | 2024-07-12 |
| >$30 bn | Bank asset size for which SR 26-2 is "most relevant" | Federal Reserve SR 26-2 | 2026-04-17 |
| $5,000 | Rule 11 sanction in Mata v. Avianca (plus letters to client and judges) | S.D.N.Y. order | 2023-06-22 |
| CA$650.88 | Damages in Moffatt v. Air Canada (≈ CA$812 with interest/fees) | ML Taikins; Fox Business | 2024 |
| 57 | Robodebt Royal Commission recommendations | LSJ | 2023-08-09 |
| > A$720 m | Robodebt class-action settlement; ~430,000 debts | LSJ | 2023-08-09 |
| €2.75 m | Dutch DPA fine on Tax Administration (nationality processing) | IAPP; DutchNews | 2021-12 |
| ~40,000 / 93% | People wrongly accused by MiDAS / reported error rate | UMich STPP case summary | 2024-08 |
| $20 m | Bauserman v. Michigan UIA settlement, ~3,000 claimants | UMich STPP | 2024-08 |
| 2.3 m / ⅔ / 700 FTE | Klarna assistant first-month conversations, share of chats, claimed FTE equivalent (vendor claim) | Klarna press release | 2024-02-27 |
| 84% | Reduction in permission prompts from sandboxing, Anthropic internal usage (vendor claim, method not given) | Anthropic engineering | 2025-10-20 |
| +19% | Task completion time with AI, 16 experienced OSS devs, early-2025 tools | METR, arXiv 2507.09089 | 2025-07-12 |
| −24% / −20% | Developers' forecast and post-hoc belief about time change (opposite sign to measured) | METR | 2025-07-12 |
| 18% / 4% | Follow-up speedup estimates (returning / new devs), METR calls it "very weak evidence" | METR blog | 2026-02-24 |
| 90% / >80% / 30% | DORA: use AI at work / believe it raised productivity / little or no trust in AI code | Google Cloud blog | 2025-09-23 |
| 12.5% | SWE-agent SWE-bench pass@1 (2024 models; superseded) | arXiv 2405.15793 | 2024-05 |

## Where sources disagree

- **GDPR Art. 22 amendments.** EDRi (March 2026) says the weakening was dropped; another secondary source describes a May 2026 provisional agreement with a reworded Art. 22. Neither verified against an official text.
- **FDA CDS revision date.** Law firms say 6 January 2026; the FDA page shows "current as of 01/29/2026"; one source claims a second revision on 29 January.
- **Klarna.** Press framed May 2025 as a reversal ("rehires humans"); Klarna said it is "still AI-first" and only two freelance agents had started. The 2024 numbers are vendor claims never independently audited.
- **MiDAS.** Sources give system costs of $46m, $47m and $52m, and approval of the $20m settlement in January 2023 or January 2024 (the university summary says late January 2024).
- **Robodebt recommendation count.** Most sources say 57; one law-firm note says 56.
- **METR vs DORA.** Controlled measurement (slowdown in 2025; weak, possibly positive in 2026) versus self-report (>80% feel more productive). Not a contradiction of fact, but of method; the book should prefer measured outcomes.
- **Human in the loop as protection.** Vendors and deployers often treat a human approval step as taking a system out of "automated decision" territory; SCHUFA's "draws strongly" test and the Dutch case suggest a rubber-stamp human does not.

## Open questions / not verifiable

- Final text and status of the GDPR changes in the wider Digital Omnibus (⚠ pending).
- Whether FDA has finalised the AI-enabled device software functions lifecycle guidance (draft as of this fetch).
- Exact wording of Robodebt recommendations 17.1 and 17.2 (primary site unreachable).
- Primary text of ABA Formal Opinion 512 (ABA PDF returned 403; relied on a committee member's summary).
- The full text of Moffatt v. Air Canada (CanLII and the CRT site returned 403); whether the chatbot was an LLM.
- Whether OCC/FDIC or the Fed will issue separate guidance on generative/agentic AI models after SR 26-2's exclusion.
- Harmonised standards under the AI Act for logging (Art. 12) and human oversight (Art. 14): not yet published as of the Omnibus recitals.
- The names of the seven DORA AI capabilities (not readable on the fetched pages).
- Any enterprise agent deployment (beyond Klarna) with audited, primary-sourced outcome numbers.
- Codex CLI subagent and MCP architecture pages (not read).
- HHS's proposed 2025 HIPAA Security Rule update and its status.

## Source list

| Title | Author / publisher | Year | URL | Type |
| --- | --- | --- | --- | --- |
| Regulation (EU) 2024/1689 (Artificial Intelligence Act) | European Parliament and Council | 2024 | http://publications.europa.eu/resource/celex/32024R1689 | regulation |
| Regulation (EU) 2026/1744 (Digital Omnibus on AI) | European Parliament and Council | 2026 | http://publications.europa.eu/resource/celex/32026R1744 | regulation |
| AI Act Annex III (consolidated reading site) | Future of Life Institute (artificialintelligenceact.eu) | n.d. | https://artificialintelligenceact.eu/annex/3/ | regulation (secondary rendering) |
| EU Digital Omnibus on AI enters into force | National Law Review | 2026 | https://natlawreview.com/article/eu-digital-omnibus-ai-enters-force | press (legal) |
| CSA research note: EU AI Act omnibus deadline delay | Cloud Security Alliance | 2026 | https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-omnibus-vii-deadline-delay-20260/ | press (analysis) |
| Regulation (EU) 2016/679 (GDPR) | European Parliament and Council | 2016 | http://publications.europa.eu/resource/celex/32016R0679 | regulation |
| Judgment in Case C-634/21 (SCHUFA Holding) | Court of Justice of the EU | 2023 | http://publications.europa.eu/resource/celex/62021CJ0634 | court decision |
| EU Digital Omnibus Package – first look | Gibson Dunn | 2025 | https://www.gibsondunn.com/eu-digital-omnibus-package-a-first-look-at-the-commission-draft-proposals/ | press (legal) |
| The Digital Omnibus: a step back from the brink | EDRi | 2026 | https://edri.org/our-work/the-digital-omnibus-a-step-back-from-the-brink-but-the-risks-remain/ | press (advocacy) |
| Clinical Decision Support Software (guidance page) | US FDA | 2026 | https://www.fda.gov/regulatory-information/search-fda-guidance-documents/clinical-decision-support-software | regulation (guidance) |
| Automation Bias and Clinical Practice: FDA updates CDS guidance | Cooley | 2026 | https://www.cooley.com/news/insight/2026/2026-01-20-automation-bias-and-clinical-practice-fda-makes-incremental-updates-to-clinical-decision-support-software-guidance | press (legal) |
| 5 key takeaways from FDA's revised CDS guidance | Covington | 2026 | https://www.cov.com/en/news-and-insights/insights/2026/01/5-key-takeaways-from-fdas-revised-clinical-decision-support-cds-software-guidance | press (legal) |
| AI-Enabled Device Software Functions: Lifecycle Management and Marketing Submission (draft) | US FDA | 2025 | https://www.fda.gov/regulatory-information/search-fda-guidance-documents/artificial-intelligence-enabled-device-software-functions-lifecycle-management-and-marketing | regulation (draft guidance) |
| FDA finalizes AI-enabled device PCCP guidance | Healthcare IT News | 2024 | https://healthcareitnews.com/node/555567 | press |
| 45 CFR 164.502 | LII / Cornell (eCFR text) | n.d. | https://www.law.cornell.edu/cfr/text/45/164.502 | regulation |
| 45 CFR 164.514 | LII / Cornell (eCFR text) | n.d. | https://www.law.cornell.edu/cfr/text/45/164.514 | regulation |
| 15 U.S.C. 7262 (SOX §404) | LII / Cornell | n.d. | https://www.law.cornell.edu/uscode/text/15/7262 | regulation |
| SR 26-2: Revised Guidance on Model Risk Management | Federal Reserve Board | 2026 | https://www.federalreserve.gov/supervisionreg/srletters/sr2602.htm | regulation (supervisory guidance) |
| SR 26-2 Attachment: Supervisory Guidance on Model Risk Management | Fed, FDIC, OCC | 2026 | https://www.federalreserve.gov/supervisionreg/srletters/SR2602a1.pdf | regulation (supervisory guidance) |
| Agencies overhaul model risk management guidance | Orrick | 2026 | https://www.orrick.com/en/Insights/2026/04/Agencies-Overhaul-Model-Risk-Management-Guidance-for-Banks-Heres-What-Changed | press (legal) |
| Mata v. Avianca, Opinion and Order on Sanctions (ECF 54) | US District Court, S.D.N.Y. | 2023 | https://storage.courtlistener.com/recap/gov.uscourts.nysd.575368/gov.uscourts.nysd.575368.54.0.pdf | court decision |
| Generative Artificial Intelligence Tools (on ABA Formal Op. 512) | W. Muchman, The Bar Examiner (NCBE) | 2024 | https://thebarexaminer.ncbex.org/article/fall-2024/generative-artificial-intelligence-tools/ | press (professional) |
| ABA Formal Opinion 512 | Zuva | 2024 | https://zuva.ai/blog/aba-formal-opinion-512/ | press |
| Robodebt Royal Commission – Overview of Final Report | APRA | 2024 | https://www.apra.gov.au/sites/default/files/2024-02/Robodebt%20Royal%20Commision%20-%20Overview%20of%20Final%20Report.pdf | incident report (summary) |
| Crude, cruel and unlawful: Robodebt Royal Commission findings | Law Society Journal (NSW) | 2023 | https://lsj.com.au/articles/crude-cruel-and-unlawful-robodebt-royal-commission-findings/ | press (legal) |
| Xenophobic machines: Dutch child benefit scandal | Amnesty International | 2021 | https://www.amnesty.org/en/latest/news/2021/10/xenophobic-machines-dutch-child-benefit-scandal/ | incident report |
| Dutch DPA fines tax authority €2.75M | IAPP | 2021 | https://iapp.org/news/a/dutch-dpa-fines-tax-authority-2-75m-euros | press |
| Tax office fined €2.7m for discriminating against dual national families | DutchNews | 2021 | https://dutchnews.nl/2021/12/tax-office-fined-e2-7m-for-discriminating-against-dual-national-families | press |
| Tax office fined €3.7m for fraud suspect blacklist | DutchNews | 2022 | https://dutchnews.nl/2022/04/tax-office-fined-e3-7m-for-breaking-privacy-law-with-fraud-suspect-blacklist | press |
| Case over Michigan UIA's faulty automated system finally settled | G. Carr, Univ. of Michigan STPP | 2024 | https://stpp.fordschool.umich.edu/sites/stpp/files/2024-08/stpp-midas-explainer.pdf | incident report (case summary) |
| Michigan makes amends for falsely accusing thousands | GovTech | 2017 | https://www.govtech.com/health/michigan-makes-amends-for-falsely-accusing-thousands-of-unemployment-fraud.html | press |
| That wasn't me, that was my chatbot | MLT Aikins | 2024 | https://www.mltaikins.com/insights/that-wasnt-me-that-was-my-chatbot | press (legal) |
| Court rejects Air Canada's 'remarkable' denial of liability | Law360 Canada | 2024 | https://www.law360.ca/ca/articles/1804075 | press (legal) |
| Air Canada chatbot gave a customer wrong info | Fox Business | 2024 | https://foxbusiness.com/lifestyle/air-canada-chatbot-gave-customer-wrong-info-airline-pay | press |
| Klarna AI assistant handles two-thirds of customer service chats in its first month | Klarna | 2024 | https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/ | press (vendor) |
| Klarna AI humans return on investment | Fortune | 2025 | https://www.fortune.com/2025/05/09/klarna-ai-humans-return-on-investment | press |
| Configure permissions | Anthropic (Claude Code docs) | n.d. | https://code.claude.com/docs/en/permissions | docs |
| Hooks reference | Anthropic (Claude Code docs) | n.d. | https://code.claude.com/docs/en/hooks | docs |
| Subagents | Anthropic (Claude Code docs) | n.d. | https://code.claude.com/docs/en/sub-agents | docs |
| Sandboxing | Anthropic (Claude Code docs) | n.d. | https://code.claude.com/docs/en/sandboxing | docs |
| Making Claude Code more secure and autonomous with sandboxing | Anthropic | 2025 | https://www.anthropic.com/engineering/claude-code-sandboxing | engineering post |
| Agent approvals and security | OpenAI (Codex docs) | n.d. | https://learn.chatgpt.com/codex/agent-approvals-security | docs |
| Hooks | OpenAI (Codex docs) | n.d. | https://learn.chatgpt.com/codex/hooks | docs |
| SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering | Yang et al. | 2024 | https://arxiv.org/abs/2405.15793 | paper (preprint) |
| OpenHands: An Open Platform for AI Software Developers as Generalist Agents | Wang et al. | 2024/2025 | https://arxiv.org/abs/2407.16741 | paper (ICLR 2025) |
| Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity | Becker, Rush, Barnes, Rein (METR) | 2025 | https://arxiv.org/abs/2507.09089 | paper (preprint) |
| We are Changing our Developer Productivity Experiment Design | METR | 2026 | https://metr.org/blog/2026-02-24-uplift-update/ | engineering post (research update) |
| Announcing the 2025 DORA report | Google Cloud | 2025 | https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report | engineering post (survey research) |
| State of AI-assisted Software Development 2025 | DORA | 2025 | https://dora.dev/research/2025/dora-report/ | survey report |
