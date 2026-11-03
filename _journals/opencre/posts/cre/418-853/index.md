---
id: "CRE-418-853"
title: "Monitor unusual activities on system"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-418-853
excerpt: "CRE 418-853 · in Technical application security controls › Robust business logic › Detect and prevent unusual activity · 12 mappings to 4 standards and tools."
tags: ASVS, CWE, OWASP Proactive Controls, PCI DSS
---
> **CRE**: [418-853](https://opencre.org/cre/418-853)
>
> **Part of**: [[cre-636-660]] › [[cre-854-643]] › [[cre-552-588]]
>
> **Maps to**: [[standard-asvs]], [[standard-cwe]], [[standard-owasp-proactive-controls]], [[standard-pci-dss]]

## Related CREs

- [[cre-623-550]]
- [[cre-058-083]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V11.1.7](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x19-V11-BusLogic.md#v111-business-logic-security) | Verify that the application monitors for unusual events or activity from a business logic perspective. For example, attempts to perform actions out of order or actions which a normal user would never attempt. | curated |

More: [[standard-asvs]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [754](https://cwe.mitre.org/data/definitions/754.html) | Improper Check for Unusual or Exceptional Conditions | curated |
| [252](https://cwe.mitre.org/data/definitions/252.html) | Unchecked Return Value | automatic |
| [253](https://cwe.mitre.org/data/definitions/253.html) | Incorrect Check of Function Return Value | automatic |
| [273](https://cwe.mitre.org/data/definitions/273.html) | Improper Check for Dropped Privileges | automatic |
| [354](https://cwe.mitre.org/data/definitions/354.html) | Improper Validation of Integrity Check Value | automatic |
| [394](https://cwe.mitre.org/data/definitions/394.html) | Unexpected Status Code or Return Value | automatic |
| [476](https://cwe.mitre.org/data/definitions/476.html) | NULL Pointer Dereference | automatic |
| [690](https://cwe.mitre.org/data/definitions/690.html) | Unchecked Return Value to NULL Pointer Dereference | automatic |

More: [[standard-cwe]]

### OWASP Proactive Controls

| ID | Section | Link |
| --- | --- | --- |
|  | [C9](https://owasp-top-10-proactive-controls-2018.readthedocs.io/en/latest/c9-implement-security-logging-monitoring.html) | curated |

More: [[standard-owasp-proactive-controls]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 10.4 | Audit logs are reviewed to identify anomalies or suspicious activity. | automatic |
| 10.4.2 | Logs of all other system components (those not specified in Requirement 10.4.1) are reviewed periodically. (CUSTOMIZED APPROACH OBJECTIVE): Potentially suspicious or anomalous activities for other system components (not included in 10.4.1) are reviewed in accordance with the entity’s identified risk. (APPLICABILITY NOTES): This requirement is applicable to all other in-scope system components not included in Requirement 10.4.1. | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [418-853](https://opencre.org/cre/418-853). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
