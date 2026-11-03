---
id: "CRE-275-483"
title: "Securely store regulated data"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-275-483
excerpt: "CRE 275-483 · in Technical application security controls › Secure data storage › Encrypt data at rest · 3 sub-requirements · 1 mapping to 1 standard and tool."
tags: PCI DSS
---
> **CRE**: [275-483](https://opencre.org/cre/275-483)
>
> **Part of**: [[cre-636-660]] › [[cre-126-668]] › [[cre-400-007]]
>
> **Maps to**: [[standard-pci-dss]]

## Where It Sits

---begin mermaid---
graph LR
  n400007["Encrypt data at rest"] --> n275483["Securely store regulated data"]
  n275483 --> n267468["Encrypt financial data at rest"]
  n275483 --> n224321["Encrypt health data at rest"]
  n275483 --> n482866["Encrypt personal data at rest"]
  style n275483 stroke-width:3px
---end mermaid---

## Contains

- [[cre-267-468]]
- [[cre-224-321]]
- [[cre-482-866]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 3.3.3 | Additional requirement for issuers and companies that support issuing services and store sensitive authentication data: Any storage of sensitive authentication data is: () Limited to that which is needed for a legitimate issuing business need and is secured. () Encrypted using strong cryptography. This bullet is a best practice until its effective date; refer to (APPLICABILITY NOTES): below for details. (CUSTOMIZED APPROACH OBJECTIVE): Sensitive authentication data is retained only as required to support issuing functions and is secured from unauthorized access. (APPLICABILITY NOTES): This requirement applies only to issuers and companies that support issuing services and store sensitive authentication data. Entities that issue payment cards or that perform or support issuing services will often create and control sensitive authentication data as part of the issuing function. It is allowable for companies that perform, facilitate, or support issuing services to store sensitive authentication data ONLY IF they have a legitimate business need to store such data. PCI DSS requirements are intended for all entities that store, process, or transmit account data, including issuers. The only exception for issuers and issuer processors is that sensitive authentication data may be retained if there is a legitimate reason to do so. Any such data must be stored securely and in accordance with all PCI DSS and specific payment brand requirements. The bullet above (for encrypting stored SAD with strong cryptography) is a best practice until 31 March 2025, after which it will be required as part of Requirement 3.3.3 and must be fully considered during a PCI DSS assessment. | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [275-483](https://opencre.org/cre/275-483). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
