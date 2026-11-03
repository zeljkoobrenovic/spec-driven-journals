---
id: "CRE-180-488"
title: "Proper Configuration for all applications and frameworks"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-180-488
excerpt: "CRE 180-488 · in Technical application security controls › Configuration hardening · 8 mappings to 4 standards and tools."
tags: ASVS, NIST SSDF, OWASP Cheat Sheets, ZAP Rule
---
> **CRE**: [180-488](https://opencre.org/cre/180-488)
>
> **Part of**: [[cre-636-660]] › [[cre-233-748]]
>
> **Maps to**: [[standard-asvs]], [[standard-nist-ssdf]], [[standard-owasp-cheat-sheets]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V14.1.3](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x22-V14-Config.md#v141-build-and-deploy) | Verify that server configuration is hardened as per the recommendations of the application server and frameworks in use. | curated |

More: [[standard-asvs]]

### NIST SSDF

| ID | Section | Link |
| --- | --- | --- |
| PW.9.1 | Define a secure baseline by determining how to configure each setting that has an effect on security or a security-related setting so that the default settings are secure and do not weaken the security functions provided by the platform, network infrastructure, or services. | curated |
| PW.9.2 | Implement the default settings (or groups of default settings, if applicable), and document each setting for software administrators. | curated |

More: [[standard-nist-ssdf]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Docker Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [10058](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/GetForPostScanRule.java) | GET for POST | automatic |
| [10063-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrulesBeta/src/main/java/org/zaproxy/zap/extension/pscanrulesBeta/PermissionsPolicyScanRule.java) | Deprecated Feature Policy Header Set | automatic |
| [50007-1](https://github.com/zaproxy/zap-extensions/blob/main/addOns/graphql/src/main/java/org/zaproxy/addon/graphql/ExtensionGraphQl.java) | GraphQL Endpoint Supports Introspection | automatic |
| [50007-3](https://github.com/zaproxy/zap-extensions/blob/main/addOns/graphql/src/main/java/org/zaproxy/addon/graphql/ExtensionGraphQl.java) | GraphQL Circular Type Reference | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [180-488](https://opencre.org/cre/180-488). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
