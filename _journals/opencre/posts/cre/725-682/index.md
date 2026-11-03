---
id: "CRE-725-682"
title: "Enable configurable alert against usage anomalies"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-725-682
excerpt: "CRE 725-682 · in Technical application security controls › Robust business logic › Detect and prevent unusual activity · 6 mappings to 5 standards and tools."
tags: ASVS, CWE, OWASP Cheat Sheets, OWASP Web Security Testing Guide (WSTG), PCI DSS
---
> **CRE**: [725-682](https://opencre.org/cre/725-682)
>
> **Part of**: [[cre-636-660]] › [[cre-854-643]] › [[cre-552-588]]
>
> **Maps to**: [[standard-asvs]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-pci-dss]]

## Related CREs

- [[cre-623-550]]
- [[cre-842-876]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V11.1.8](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x19-V11-BusLogic.md#v111-business-logic-security) | Verify that the application has configurable alerting when automated attacks or unusual activity is detected. | curated |

More: [[standard-asvs]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [390](https://cwe.mitre.org/data/definitions/390.html) | Detection of Error Condition Without Action | curated |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Abuse Case Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-BUSL-$$](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/10-Business_Logic_Testing/README.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 11.6.1 | A change- and tamper-detection mechanism is deployed as follows: () To alert personnel to unauthorized modification (including indicators of compromise, changes, additions, and deletions) to the HTTP headers and the contents of payment pages as received by the consumer browser. () The mechanism is configured to evaluate the received HTTP header and payment page. () The mechanism functions are performed as follows: – At least once every seven days OR – Periodically (at the frequency defined in the entity’s targeted risk analysis, which is performed according to all elements specified in Requirement 12.3.1). (CUSTOMIZED APPROACH OBJECTIVE): E-commerce skimming code or techniques cannot be added to payment pages as received by the consumer browser without a timely alert being generated. Anti-skimming measures cannot be removed from payment pages without a prompt alert being generated. (APPLICABILITY NOTES): The intention of this requirement is not that an entity installs software in the systems or browsers of its consumers, but rather that the entity uses techniques such as those described under Examples in the Guidance column to prevent and detect unexpected script activities. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. | automatic |
| A3.2.6 | Mechanisms are implemented for detecting and preventing cleartext PAN from leaving the CDE via an unauthorized channel, method, or process, including mechanisms that are: () Actively running. () Configured to detect and prevent cleartext PAN leaving the CDE via an unauthorized channel, method, or process. () Generating audit logs and alerts upon detection of cleartext PAN leaving the CDE via an unauthorized channel, method, or process. PCI DSS Reference: Scope of PCI DSS Requirements, Requirement 12 (CUSTOMIZED APPROACH OBJECTIVE): This requirement is not eligible for the customized approach. | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [725-682](https://opencre.org/cre/725-682). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
