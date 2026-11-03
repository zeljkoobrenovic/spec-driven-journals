---
id: "CRE-623-347"
title: "Disallow shared high privileged accounts"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-623-347
excerpt: "CRE 623-347 · in Operating processes for security › Access control processes · 10 mappings to 5 standards and tools."
tags: ASVS, NIST 800-63, OWASP Cheat Sheets, PCI DSS, ZAP Rule
---
> **CRE**: [623-347](https://opencre.org/cre/623-347)
>
> **Part of**: [[cre-862-452]] › [[cre-247-250]]
>
> **Maps to**: [[standard-asvs]], [[standard-nist-800-63]], [[standard-owasp-cheat-sheets]], [[standard-pci-dss]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V2.5.4](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x11-V2-Authentication.md#v25-credential-recovery) | Verify shared or default accounts are not present (e.g. "root", "admin", or "sa"). | curated |

More: [[standard-asvs]]

### NIST 800-63

| ID | Section | Link |
| --- | --- | --- |
|  | 5.1.1.2 | curated |
|  | A.3 | curated |

More: [[standard-nist-800-63]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Choosing and Using Security Questions Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html) | curated |
|  | [Forgot Password Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 8.2.2 | Group, shared, or generic accounts, or other shared authentication credentials are only used when necessary on an exception basis, and are managed as follows: () Account use is prevented unless needed for an exceptional circumstance. () Use is limited to the time needed for the exceptional circumstance. () Business justification for use is documented. () Use is explicitly approved by management. () Individual user identity is confirmed before access to an account is granted. () Every action taken is attributable to an individual user. (CUSTOMIZED APPROACH OBJECTIVE): All actions performed by users with generic, system, or shared IDs are attributable to an individual person. (APPLICABILITY NOTES): This requirement is not intended to apply to user accounts within point-of-sale terminals that have access to only one card number at a time to facilitate a single transaction (such as IDs used by cashiers on point-of-sale terminals). | automatic |

More: [[standard-pci-dss]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [10058](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/GetForPostScanRule.java) | GET for POST | automatic |
| [10063-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrulesBeta/src/main/java/org/zaproxy/zap/extension/pscanrulesBeta/PermissionsPolicyScanRule.java) | Deprecated Feature Policy Header Set | automatic |
| [50007-1](https://github.com/zaproxy/zap-extensions/blob/main/addOns/graphql/src/main/java/org/zaproxy/addon/graphql/ExtensionGraphQl.java) | GraphQL Endpoint Supports Introspection | automatic |
| [50007-3](https://github.com/zaproxy/zap-extensions/blob/main/addOns/graphql/src/main/java/org/zaproxy/addon/graphql/ExtensionGraphQl.java) | GraphQL Circular Type Reference | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [623-347](https://opencre.org/cre/623-347). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
