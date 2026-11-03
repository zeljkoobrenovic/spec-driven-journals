---
id: "CRE-732-148"
title: "Vulnerability management"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-732-148
excerpt: "CRE 732-148 · in Operating processes for security › Improvement management · 43 mappings to 7 standards and tools."
tags: Cloud Controls Matrix, DevSecOps Maturity Model (DSOMM), ISO 27001, NIST 800-53 v5, NIST SSDF, PCI DSS, SAMM
---
> **CRE**: [732-148](https://opencre.org/cre/732-148)
>
> **Part of**: [[cre-862-452]] › [[cre-010-678]]
>
> **Maps to**: [[standard-cloud-controls-matrix]], [[standard-devsecops-maturity-model-dsomm]], [[standard-iso-27001]], [[standard-nist-800-53-v5]], [[standard-nist-ssdf]], [[standard-pci-dss]], [[standard-samm]]

## Related CREs

- [[cre-613-286]]
- [[cre-463-577]]
- [[cre-433-442]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### Cloud Controls Matrix

| ID | Section | Link |
| --- | --- | --- |
| AIS-07 | Application Vulnerability Remediation | curated |
| TVM | Threat & Vulnerability Management | curated |

More: [[standard-cloud-controls-matrix]]

### DevSecOps Maturity Model (DSOMM)

| ID | Section | Link |
| --- | --- | --- |
| [0c10a7f7-f78f-49f2-943d-19fdef248fed](https://dsomm.owasp.org/activity-description?uuid=0c10a7f7-f78f-49f2-943d-19fdef248fed) | Consolidation: Fix based on accessibility | automatic |
| [0ec92899-a5cb-4649-984b-2fb1d6c784ad](https://dsomm.owasp.org/activity-description?uuid=0ec92899-a5cb-4649-984b-2fb1d6c784ad) | Test KPI: Number of vulnerabilities/severity/layer | automatic |
| [2b7cc923-bdaf-43e3-8fb4-a995b7783969](https://dsomm.owasp.org/activity-description?uuid=2b7cc923-bdaf-43e3-8fb4-a995b7783969) | Consolidation: Treatment of defects per protection requirement | automatic |
| [7a82020c-94d1-471c-bbd3-5f7fe7df4876](https://dsomm.owasp.org/activity-description?uuid=7a82020c-94d1-471c-bbd3-5f7fe7df4876) | Consolidation: Advanced visualization of defects | automatic |
| [7bb70764-9392-4462-935d-e55b2e148199](https://dsomm.owasp.org/activity-description?uuid=7bb70764-9392-4462-935d-e55b2e148199) | Dynamic depth for infrastructure: Test of the configuration of cloud environments | automatic |
| [8a442d8e-0eb1-4793-a513-571aef982edd](https://dsomm.owasp.org/activity-description?uuid=8a442d8e-0eb1-4793-a513-571aef982edd) | Monitoring: Alerting | automatic |
| [8f2b4d5a-3c1e-4b7a-9d8f-2e6c4a1b5d7f](https://dsomm.owasp.org/activity-description?uuid=8f2b4d5a-3c1e-4b7a-9d8f-2e6c4a1b5d7f) | Consolidation: Artifact-based false positive treatment | automatic |
| [9cac3341-fe83-4079-bef2-bfc4279eb594](https://dsomm.owasp.org/activity-description?uuid=9cac3341-fe83-4079-bef2-bfc4279eb594) | Consolidation: Treatment of defects with medium severity | automatic |
| [9e3a7c2f-1b4d-4e8a-a5c6-7f2b9d1e3a8c](https://dsomm.owasp.org/activity-description?uuid=9e3a7c2f-1b4d-4e8a-a5c6-7f2b9d1e3a8c) | Consolidation: Global false positive treatment | automatic |
| [44f2c8a9-4aaa-4c72-942d-63f78b89f385](https://dsomm.owasp.org/activity-description?uuid=44f2c8a9-4aaa-4c72-942d-63f78b89f385) | Consolidation: Treatment of defects with high or critical severity | automatic |
| [51f3fce5-b5c8-4683-8c41-e785fe4f3b5f](https://dsomm.owasp.org/activity-description?uuid=51f3fce5-b5c8-4683-8c41-e785fe4f3b5f) | Test KPI: SLA per criticality | automatic |
| [55f4c916-3a34-474d-ad96-9a9f7a4f6a83](https://dsomm.owasp.org/activity-description?uuid=55f4c916-3a34-474d-ad96-9a9f7a4f6a83) | Consolidation: Simple visualization of defects | automatic |
| [77ffc53e-9f3d-41f4-92d3-02f04f9b6b0f](https://dsomm.owasp.org/activity-description?uuid=77ffc53e-9f3d-41f4-92d3-02f04f9b6b0f) | Test KPI: Patching mean time to resolution via production | automatic |
| [85ba5623-84be-4219-8892-808837be582d](https://dsomm.owasp.org/activity-description?uuid=85ba5623-84be-4219-8892-808837be582d) | Consolidation: Usage of a vulnerability management system | automatic |
| [86d490b9-d798-4a5b-a011-ab9688014c46](https://dsomm.owasp.org/activity-description?uuid=86d490b9-d798-4a5b-a011-ab9688014c46) | Test KPI: Patching mean time to resolution via PR | automatic |
| [27337442-e4b1-4e87-8dc9-ce86fbb79a39](https://dsomm.owasp.org/activity-description?uuid=27337442-e4b1-4e87-8dc9-ce86fbb79a39) | Consolidation: Reproducible defect tickets | automatic |
| [aaffa73f-59f6-4267-b0ab-732f3d13e90d](https://dsomm.owasp.org/activity-description?uuid=aaffa73f-59f6-4267-b0ab-732f3d13e90d) | Consolidation: Integration in development process | automatic |
| [b2f77606-3e6c-41e9-b72d-7c0b1d3d581d](https://dsomm.owasp.org/activity-description?uuid=b2f77606-3e6c-41e9-b72d-7c0b1d3d581d) | Consolidation: Treatment of all defects | automatic |
| [bc548cba-cb82-4f76-bd4b-325d9d256279](https://dsomm.owasp.org/activity-description?uuid=bc548cba-cb82-4f76-bd4b-325d9d256279) | Test KPI: Number of vulnerabilities/severity | automatic |
| [c1acc8af-312e-4503-a817-a26220c993a0](https://dsomm.owasp.org/activity-description?uuid=c1acc8af-312e-4503-a817-a26220c993a0) | Consolidation: Simple false positive treatment | automatic |
| [c922981b-65ed-40f3-a947-96fee9a0125f](https://dsomm.owasp.org/activity-description?uuid=c922981b-65ed-40f3-a947-96fee9a0125f) | Test KPI: Generation of response statistics | automatic |
| [ce970c9b-da94-41cf-bd78-8c15357b7e8e](https://dsomm.owasp.org/activity-description?uuid=ce970c9b-da94-41cf-bd78-8c15357b7e8e) | Consolidation: Integration of vulnerability issues into the development process | automatic |
| [cf0d600e-114d-4887-9059-d81c53805f0d](https://dsomm.owasp.org/activity-description?uuid=cf0d600e-114d-4887-9059-d81c53805f0d) | Test KPI: Fix rate per repo/product | automatic |
| [d6f06ae8-401a-4f44-85df-1079247fa030](https://dsomm.owasp.org/activity-description?uuid=d6f06ae8-401a-4f44-85df-1079247fa030) | Monitoring: Targeted alerting | automatic |
| [dccf1949-b9a8-4ce8-b992-6a4a7f3a623a](https://dsomm.owasp.org/activity-description?uuid=dccf1949-b9a8-4ce8-b992-6a4a7f3a623a) | Dynamic depth for infrastructure: Test for unauthorized installation | automatic |

More: [[standard-devsecops-maturity-model-dsomm]]

### ISO 27001

| ID | Section | Link |
| --- | --- | --- |
| 8.8 | Management of technical vulnerabilities | curated |

More: [[standard-iso-27001]]

### NIST 800-53 v5

| ID | Section | Link |
| --- | --- | --- |
|  | [SI-2 Flaw Remediation](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SI-2) | curated |

More: [[standard-nist-800-53-v5]]

### NIST SSDF

| ID | Section | Link |
| --- | --- | --- |
| RV.1.1 | Gather information from software acquirers, users, and public sources on potential vulnerabilities in the software and third-party components that the software uses, and investigate all credible reports. | curated |
| RV.2.1 | Analyze each vulnerability to gather sufficient information about risk to plan its remediation or other risk response. | curated |
| RV.2.2 | Plan and implement risk responses for vulnerabilities. | curated |
| RV.3.1 | Analyze identified vulnerabilities to determine their root causes. | curated |
| RV.3.2 | Analyze the root causes over time to identify patterns, such as a particular secure coding practice not being followed consistently. | curated |
| RV.3.3 | Review the software for similar vulnerabilities to eradicate a class of vulnerabilities, and proactively fix them rather than waiting for external reports. | curated |

More: [[standard-nist-ssdf]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 6.3 | Security vulnerabilities are identified and addressed. | automatic |
| 6.3.1 | Security vulnerabilities are identified and managed as follows: () New security vulnerabilities are identified using industry-recognized sources for security vulnerability information, including alerts from international and national computer emergency response teams (CERTs). () Vulnerabilities are assigned a risk ranking based on industry best practices and consideration of potential impact. () Risk rankings identify, at a minimum, all vulnerabilities considered to be a high-risk or critical to the environment. () Vulnerabilities for bespoke and custom, and third-party software (for example operating systems and databases) are covered. (CUSTOMIZED APPROACH OBJECTIVE): New system and software vulnerabilities that may impact the security of account data or the CDE are monitored, cataloged, and risk assessed. (APPLICABILITY NOTES): This requirement is not achieved by, nor is it the same as, vulnerability scans performed for Requirements 11.3.1 and 11.3.2. This requirement is for a process to actively monitor industry sources for vulnerability information and for the entity to determine the risk ranking to be associated with each vulnerability. | automatic |
| 6.4.1 | For public-facing web applications, new threats and vulnerabilities are addressed on an ongoing basis and these applications are protected against known attacks as follows: () Reviewing public-facing web applications via manual or automated application vulnerability security assessment tools or methods as follows: – At least once every 12 months and after significant changes. – By an entity that specializes in application security. – Including, at a minimum, all common software attacks in Requirement 6.2.4. – All vulnerabilities are ranked in accordance with requirement 6.3.1. – All vulnerabilities are corrected. – The application is re-evaluated after the corrections OR () Installing an automated technical solution(s) that continually detects and prevents web-based attacks as follows: – Installed in front of public-facing web applications to detect and prevent webbased attacks. – Actively running and up to date as applicable. – Generating audit logs. – Configured to either block web-based attacks or generate an alert that is immediately investigated. (CUSTOMIZED APPROACH OBJECTIVE): Public-facing web applications are protected against malicious attacks. (APPLICABILITY NOTES): This assessment is not the same as the vulnerability scans performed for Requirement 11.3.1 and 11.3.2. This requirement will be superseded by Requirement 6.4.2 after 31 March 2025 when Requirement 6.4.2 becomes effective. | automatic |
| 11.3 | External and internal vulnerabilities are regularly identified, prioritized, and addressed. | automatic |
| 11.3.1.1 | All other applicable vulnerabilities (those not ranked as high-risk or critical per the entity’s vulnerability risk rankings defined at Requirement 6.3.1) are managed as follows: () Addressed based on the risk defined in the entity’s targeted risk analysis, which is performed according to all elements specified in Requirement 12.3.1. () Rescans are conducted as needed. (CUSTOMIZED APPROACH OBJECTIVE): Lower ranked vulnerabilities (lower than high or critical) are addressed at a frequency in accordance with the entity’s risk. (APPLICABILITY NOTES): The timeframe for addressing lower-risk vulnerabilities is subject to the results of a risk analysis per Requirement 12.3.1 that includes (minimally) identification of assets being protected, threats, and likelihood and/or impact of a threat being realized. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. | automatic |
| 11.3.2 | External vulnerability scans are performed as follows: () At least once every three months. () By a PCI SSC Approved Scanning Vendor (ASV). () Vulnerabilities are resolved and ASV Program Guide requirements for a passing scan are met. () Rescans are performed as needed to confirm that vulnerabilities are resolved per the ASV Program Guide requirements for a passing scan. (CUSTOMIZED APPROACH OBJECTIVE): This requirement is not eligible for the customized approach. (APPLICABILITY NOTES): For initial PCI DSS compliance, it is not required that four passing scans be completed within 12 months if the assessor verifies: 1) the most recent scan result was a passing scan, 2) the entity has documented policies and procedures requiring scanning at least once every three months, and 3) vulnerabilities noted in the scan results have been corrected as shown in a re-scan(s). However, for subsequent years after the initial PCI DSS assessment, passing scans at least every three months must have occurred. ASV scanning tools can scan a vast array of network types and topologies. Any specifics about the target environment (for example, load balancers, third-party providers, ISPs, specific configurations, protocols in use, scan interference) should be worked out between the ASV and scan customer. Refer to the ASV Program Guide published on the PCI SSC website for scan customer responsibilities, scan preparation, etc. | automatic |

More: [[standard-pci-dss]]

### SAMM

| ID | Section | Link |
| --- | --- | --- |
| [I-DM-A](https://owaspsamm.org/model/implementation/defect-management/stream-a) | Defect Tracking | curated |
| [I-DM-B](https://owaspsamm.org/model/implementation/defect-management/stream-b) | Metrics and Feedback | curated |

More: [[standard-samm]]

## Source

Generated from the OpenCRE catalogue entry [732-148](https://opencre.org/cre/732-148). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
