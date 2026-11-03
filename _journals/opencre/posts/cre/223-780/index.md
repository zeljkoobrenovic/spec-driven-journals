---
id: "CRE-223-780"
title: "Secret storage"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-223-780
excerpt: "CRE 223-780 · in Technical application security controls › Secure data storage · 12 sub-requirements · 9 mappings to 4 standards and tools."
tags: DevSecOps Maturity Model (DSOMM), OWASP Cheat Sheets, OWASP WrongSecrets, SAMM
---
> **CRE**: [223-780](https://opencre.org/cre/223-780)
>
> **Part of**: [[cre-636-660]] › [[cre-126-668]]
>
> **Maps to**: [[standard-devsecops-maturity-model-dsomm]], [[standard-owasp-cheat-sheets]], [[standard-owasp-wrongsecrets]], [[standard-samm]]

## Where It Sits

---begin mermaid---
graph LR
  n126668["Secure data storage"] --> n223780["Secret storage"]
  n223780 --> n774888["Do not store secrets in the code"]
  n223780 --> n821832["Ensure keys and passwords are replaceable"]
  n223780 --> n767435["Set the highest feasible iteration count for…"]
  n223780 --> n078427["Set the highest feasible work factor for bcrypt"]
  n223780 --> n881321["Store credentials securely"]
  n223780 --> n783255["Store cryptographic keys securely"]
  n223780 --> n622203["Store passwords salted and hashed"]
  n223780 --> n340375["Use a dedicated secrets management solution"]
  n223780 --> n032213["Use an isolated security module for cryptogra…"]
  n223780 --> n508702["Use key vaults"]
  n223780 --> n077781["Use separately stored secret salt (pepper)"]
  n223780 --> n082530["Use unique random salt with sufficient entrop…"]
  style n223780 stroke-width:3px
---end mermaid---

## Contains

- [[cre-774-888]]
- [[cre-821-832]]
- [[cre-767-435]]
- [[cre-078-427]]
- [[cre-881-321]]
- [[cre-783-255]]
- [[cre-622-203]]
- [[cre-340-375]]
- [[cre-032-213]]
- [[cre-508-702]]
- [[cre-077-781]]
- [[cre-082-530]]

## Related CREs

- [[cre-633-428]]
- [[cre-170-772]]
- [[cre-473-177]]
- [[cre-287-305]]
- [[cre-543-428]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### DevSecOps Maturity Model (DSOMM)

| ID | Section | Link |
| --- | --- | --- |
| [0ff45fb8-7eef-46ed-9b3a-84c955cd7060](https://dsomm.owasp.org/activity-description?uuid=0ff45fb8-7eef-46ed-9b3a-84c955cd7060) | Infrastructure Hardening: Usage of encryption at rest | automatic |
| [94a96f79-8bd6-4904-97c0-994ff88f176a](https://dsomm.owasp.org/activity-description?uuid=94a96f79-8bd6-4904-97c0-994ff88f176a) | Deployment: Handover of confidential parameters | automatic |
| [746025a6-dbfb-4087-a000-e46acab64ee1](https://dsomm.owasp.org/activity-description?uuid=746025a6-dbfb-4087-a000-e46acab64ee1) | Infrastructure Hardening: Usage of an security account | automatic |
| [ad23be9c-5661-4f1f-81a3-5a5dc7061629](https://dsomm.owasp.org/activity-description?uuid=ad23be9c-5661-4f1f-81a3-5a5dc7061629) | Infrastructure Hardening: Usage of edge encryption at transit | automatic |
| [df428c9d-efa0-4226-9f47-a15bb53f822b](https://dsomm.owasp.org/activity-description?uuid=df428c9d-efa0-4226-9f47-a15bb53f822b) | Deployment: Environment depending configuration parameters (secrets) | automatic |
| [ecb0184c-6bc9-45da-bbbb-a983797ffc93](https://dsomm.owasp.org/activity-description?uuid=ecb0184c-6bc9-45da-bbbb-a983797ffc93) | Infrastructure Hardening: Usage of internal encryption at transit | automatic |

More: [[standard-devsecops-maturity-model-dsomm]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Secrets Management Cheat Sheet](https://github.com/OWASP/CheatSheetSeries/tree/master/cheatsheets/Secrets_Management_Cheat_Sheet.md) | automatic |

More: [[standard-owasp-cheat-sheets]]

### OWASP WrongSecrets

| ID | Section | Link |
| --- | --- | --- |
|  | [Training](https://github.com/commjoen/wrongsecrets) | automatic |

More: [[standard-owasp-wrongsecrets]]

### SAMM

| ID | Section | Link |
| --- | --- | --- |
| [I-SD-B](https://owaspsamm.org/model/implementation/secure-deployment/stream-b) | Secret Management | curated |

More: [[standard-samm]]

## Source

Generated from the OpenCRE catalogue entry [223-780](https://opencre.org/cre/223-780). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
