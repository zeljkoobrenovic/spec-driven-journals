---
id: "CRE-184-284"
title: "Log all security relevant events"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-184-284
excerpt: "CRE 184-284 · in Technical application security controls › Logging and error handling › Log relevant · 10 mappings to 4 standards and tools."
tags: ASVS, CWE, OWASP Proactive Controls, PCI DSS
---
> **CRE**: [184-284](https://opencre.org/cre/184-284)
>
> **Part of**: [[cre-636-660]] › [[cre-842-876]] › [[cre-402-706]]
>
> **Maps to**: [[standard-asvs]], [[standard-cwe]], [[standard-owasp-proactive-controls]], [[standard-pci-dss]]

## Related CREs

- [[cre-836-068]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V7.1.3](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x15-V7-Error-Logging.md#v71-log-content) | Verify that the application logs security relevant events including successful and failed authentication events, access control failures, deserialization failures and input validation failures. | curated |

More: [[standard-asvs]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [778](https://cwe.mitre.org/data/definitions/778.html) | Insufficient Logging | curated |

More: [[standard-cwe]]

### OWASP Proactive Controls

| ID | Section | Link |
| --- | --- | --- |
|  | [C5](https://owasp-top-10-proactive-controls-2018.readthedocs.io/en/latest/c5-validate-all-inputs.html) | curated |
|  | [C7](https://owasp-top-10-proactive-controls-2018.readthedocs.io/en/latest/c7-enforce-access-controls.html) | curated |

More: [[standard-owasp-proactive-controls]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 5.3.4 | Audit logs for the anti-malware solution(s) are enabled and retained in accordance with Requirement 10.5.1. (CUSTOMIZED APPROACH OBJECTIVE): Historical records of anti-malware actions are immediately available and retained for at least 12 months. | automatic |
| 10.2 | Audit logs are implemented to support the detection of anomalies and suspicious activity, and the forensic analysis of events. | automatic |
| 10.2.1 | Audit logs are enabled and active for all system components and cardholder data. (CUSTOMIZED APPROACH OBJECTIVE): Records of all activities affecting system components and cardholder data are captured. | automatic |
| 10.2.1.6 | Audit logs capture the following: () All initialization of new audit logs, and () All starting, stopping, or pausing of the existing audit logs. (CUSTOMIZED APPROACH OBJECTIVE): Records of all changes to audit log activity status are captured. | automatic |
| 10.2.1.7 | Audit logs capture all creation and deletion of system-level objects. (CUSTOMIZED APPROACH OBJECTIVE): Records of alterations that indicate a system has been modified from its intended functionality are captured. | automatic |
| 10.4.1 | The following audit logs are reviewed at least once daily: () All security events. () Logs of all system components that store, process, or transmit CHD and/or SAD. () Logs of all critical system components. () Logs of all servers and system components that perform security functions (for example, network security controls, intrusion-detection systems/intrusion-prevention systems (IDS/IPS), authentication servers). (CUSTOMIZED APPROACH OBJECTIVE): Potentially suspicious or anomalous activities are quickly identified to minimize impact. | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [184-284](https://opencre.org/cre/184-284). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
