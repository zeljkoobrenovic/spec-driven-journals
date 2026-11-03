---
id: "CRE-356-282"
title: "Minimize sensitive data scattering and retention"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-356-282
excerpt: "CRE 356-282 · in Technical application security controls › Robust business logic · 3 mappings to 2 standards and tools."
tags: NIST 800-53 v5, PCI DSS
---
> **CRE**: [356-282](https://opencre.org/cre/356-282)
>
> **Part of**: [[cre-636-660]] › [[cre-854-643]]
>
> **Maps to**: [[standard-nist-800-53-v5]], [[standard-pci-dss]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### NIST 800-53 v5

| ID | Section | Link |
| --- | --- | --- |
|  | [SI-21 Information Refresh](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SI-21) | curated |

More: [[standard-nist-800-53-v5]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 3.2.1 | Account data storage is kept to a minimum through implementation of data retention and disposal policies, procedures, and processes that include at least the following: () Coverage for all locations of stored account data. () Coverage for any sensitive authentication data (SAD) stored prior to completion of authorization. This bullet is a best practice until its effective date; refer to (APPLICABILITY NOTES): below for details. () Limiting data storage amount and retention time to that which is required for legal or regulatory, and/or business requirements. () Specific retention requirements for stored account data that defines length of retention period and includes a documented business justification. () Processes for secure deletion or rendering account data unrecoverable when no longer needed per the retention policy. () A process for verifying, at least once every three months, that stored account data exceeding the defined retention period has been securely deleted or rendered unrecoverable. (CUSTOMIZED APPROACH OBJECTIVE): Account data is retained only where necessary and for the least amount of time needed and is securely deleted or rendered unrecoverable when no longer needed. (APPLICABILITY NOTES): Where account data is stored by a TPSP (for example, in a cloud environment), entities are responsible for working with their service providers to understand how the TPSP meets this requirement for the entity. Considerations include ensuring that all geographic instances of a data element are securely deleted. The bullet above (for coverage of SAD stored prior to completion of authorization) is a best practice until 31 March 2025, after which it will be required as part of Requirement 3.2.1 and must be fully considered during a PCI DSS assessment. | automatic |
| 3.3.1.1 | The full contents of any track are not retained upon completion of the authorization process. (CUSTOMIZED APPROACH OBJECTIVE): This requirement is not eligible for the customized approach. (APPLICABILITY NOTES): In the normal course of business, the following data elements from the track may need to be retained: () Cardholder name. () Primary account number (PAN). () Expiration date. () Service code. To minimize risk, store securely only these data elements as needed for business. | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [356-282](https://opencre.org/cre/356-282). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
