---
id: "CRE-435-702"
title: "Communication encryption"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-435-702
excerpt: "CRE 435-702 · in Technical application security controls › Secure communication · 2 sub-requirements · 2 mappings to 2 standards and tools."
tags: DevSecOps Maturity Model (DSOMM), PCI DSS
---
> **CRE**: [435-702](https://opencre.org/cre/435-702)
>
> **Part of**: [[cre-636-660]] › [[cre-278-646]]
>
> **Maps to**: [[standard-devsecops-maturity-model-dsomm]], [[standard-pci-dss]]

## Contains

- [[cre-527-034]]
- [[cre-426-842]]

## Related CREs

- [[cre-170-772]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### DevSecOps Maturity Model (DSOMM)

| ID | Section | Link |
| --- | --- | --- |
| [ad23be9c-5661-4f1f-81a3-5a5dc7061629](https://dsomm.owasp.org/activity-description?uuid=ad23be9c-5661-4f1f-81a3-5a5dc7061629) | Infrastructure Hardening: Usage of edge encryption at transit | automatic |

More: [[standard-devsecops-maturity-model-dsomm]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 4.2.2 | PAN is secured with strong cryptography whenever it is sent via end-user messaging technologies. (CUSTOMIZED APPROACH OBJECTIVE): Cleartext PAN cannot be read or intercepted from transmissions using end-user messaging technologies. (APPLICABILITY NOTES): This requirement also applies if a customer, or other third-party, requests that PAN is sent to them via end-user messaging technologies. There could be occurrences where an entity receives unsolicited cardholder data via an insecure communication channel that was not intended for transmissions of sensitive data. In this situation, the entity can choose to either include the channel in the scope of their CDE and secure it according to PCI DSS or delete the cardholder data and implement measures to prevent the channel from being used for cardholder data. | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [435-702](https://opencre.org/cre/435-702). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
