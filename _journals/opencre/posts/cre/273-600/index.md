---
id: "CRE-273-600"
title: "Segregate components of differing trust levels"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-273-600
excerpt: "CRE 273-600 · in Operating processes for security › Facilities management › Network security · 33 mappings to 5 standards and tools."
tags: ASVS, CAPEC, Cloud Controls Matrix, CWE, PCI DSS
---
> **CRE**: [273-600](https://opencre.org/cre/273-600)
>
> **Part of**: [[cre-862-452]] › [[cre-850-376]] › [[cre-467-784]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cloud-controls-matrix]], [[standard-cwe]], [[standard-pci-dss]]

## Related CREs

- [[cre-724-770]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V1.14.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x10-V1-Architecture.md#v11-secure-software-development-lifecycle) | Verify the segregation of components of differing trust levels through well-defined security controls, firewall rules, API gateways, reverse proxies, cloud-based security groups, or similar mechanisms. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [57](https://capec.mitre.org/data/definitions/57.html) | Utilizing REST's Trust in the System Resource to Obtain Sensitive Data | automatic |
| [94](https://capec.mitre.org/data/definitions/94.html) | Adversary in the Middle (AiTM) | automatic |
| [161](https://capec.mitre.org/data/definitions/161.html) | Infrastructure Manipulation | automatic |
| [383](https://capec.mitre.org/data/definitions/383.html) | Harvesting Information via API Event Monitoring | automatic |
| [466](https://capec.mitre.org/data/definitions/466.html) | Leveraging Active Adversary in the Middle Attacks to Bypass Same Origin Policy | automatic |
| [481](https://capec.mitre.org/data/definitions/481.html) | Contradictory Destinations in Traffic Routing Schemes | automatic |
| [501](https://capec.mitre.org/data/definitions/501.html) | Android Activity Hijack | automatic |
| [589](https://capec.mitre.org/data/definitions/589.html) | DNS Blocking | automatic |
| [590](https://capec.mitre.org/data/definitions/590.html) | IP Address Blocking | automatic |
| [612](https://capec.mitre.org/data/definitions/612.html) | WiFi MAC Address Tracking | automatic |
| [613](https://capec.mitre.org/data/definitions/613.html) | WiFi SSID Tracking | automatic |
| [615](https://capec.mitre.org/data/definitions/615.html) | Evil Twin Wi-Fi Attack | automatic |
| [662](https://capec.mitre.org/data/definitions/662.html) | Adversary in the Browser (AiTB) | automatic |
| [697](https://capec.mitre.org/data/definitions/697.html) | DHCP Spoofing | automatic |

More: [[standard-capec]]

### Cloud Controls Matrix

| ID | Section | Link |
| --- | --- | --- |
| IVS-08 | Network Architecture Documentation | curated |

More: [[standard-cloud-controls-matrix]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [923](https://cwe.mitre.org/data/definitions/923.html) | Improper Restriction of Communication Channel to Intended Endpoints | curated |
| [291](https://cwe.mitre.org/data/definitions/291.html) | Reliance on IP Address for Authentication | automatic |
| [297](https://cwe.mitre.org/data/definitions/297.html) | Improper Validation of Certificate with Host Mismatch | automatic |
| [300](https://cwe.mitre.org/data/definitions/300.html) | Channel Accessible by Non-Endpoint | automatic |
| [419](https://cwe.mitre.org/data/definitions/419.html) | Unprotected Primary Channel | automatic |
| [420](https://cwe.mitre.org/data/definitions/420.html) | Unprotected Alternate Channel | automatic |
| [421](https://cwe.mitre.org/data/definitions/421.html) | Race Condition During Access to Alternate Channel | automatic |
| [422](https://cwe.mitre.org/data/definitions/422.html) | Unprotected Windows Messaging Channel ('Shatter') | automatic |
| [925](https://cwe.mitre.org/data/definitions/925.html) | Improper Verification of Intent by Broadcast Receiver | automatic |
| [939](https://cwe.mitre.org/data/definitions/939.html) | Improper Authorization in Handler for Custom URL Scheme | automatic |
| [940](https://cwe.mitre.org/data/definitions/940.html) | Improper Verification of Source of a Communication Channel | automatic |
| [941](https://cwe.mitre.org/data/definitions/941.html) | Incorrectly Specified Destination in a Communication Channel | automatic |
| [942](https://cwe.mitre.org/data/definitions/942.html) | Permissive Cross-domain Security Policy with Untrusted Domains | automatic |
| [1275](https://cwe.mitre.org/data/definitions/1275.html) | Sensitive Cookie with Improper SameSite Attribute | automatic |
| [1299](https://cwe.mitre.org/data/definitions/1299.html) | Missing Protection Mechanism for Alternate Hardware Interface | automatic |

More: [[standard-cwe]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 2.2.3 | Primary functions requiring different security levels are managed as follows: () Only one primary function exists on a system component, OR () Primary functions with differing security levels that exist on the same system component are isolated from each other, OR () Primary functions with differing security levels on the same system component are all secured to the level required by the function with the highest security need. (CUSTOMIZED APPROACH OBJECTIVE): Primary functions with lower security needs cannot affect the security of primary functions with higher security needs on the same system component. | automatic |
| A1.1 | Multi-tenant service providers protect and separate all customer environments and data. | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [273-600](https://opencre.org/cre/273-600). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
