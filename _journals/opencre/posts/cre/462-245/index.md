---
id: "CRE-462-245"
title: "Remove unnecessary elements from external components (e.g. features, documentation, configuration)"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-462-245
excerpt: "CRE 462-245 · in Development processes for security › Supply chain management · 8 mappings to 4 standards and tools."
tags: ASVS, OWASP Cheat Sheets, OWASP Web Security Testing Guide (WSTG), ZAP Rule
---
> **CRE**: [462-245](https://opencre.org/cre/462-245)
>
> **Part of**: [[cre-616-305]] › [[cre-613-285]]
>
> **Maps to**: [[standard-asvs]], [[standard-owasp-cheat-sheets]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-zap-rule]]

## Related CREs

- [[cre-486-813]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V14.2.2](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x22-V14-Config.md#v142-dependency) | Verify that all unneeded features, documentation, sample applications and configurations are removed. | curated |

More: [[standard-asvs]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Docker Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html) | curated |
|  | [Vulnerable Dependency Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Vulnerable_Dependency_Management_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-CONF-04](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/04-Review_Old_Backup_and_Unreferenced_Files_for_Sensitive_Information.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [10058](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/GetForPostScanRule.java) | GET for POST | automatic |
| [10063-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrulesBeta/src/main/java/org/zaproxy/zap/extension/pscanrulesBeta/PermissionsPolicyScanRule.java) | Deprecated Feature Policy Header Set | automatic |
| [50007-1](https://github.com/zaproxy/zap-extensions/blob/main/addOns/graphql/src/main/java/org/zaproxy/addon/graphql/ExtensionGraphQl.java) | GraphQL Endpoint Supports Introspection | automatic |
| [50007-3](https://github.com/zaproxy/zap-extensions/blob/main/addOns/graphql/src/main/java/org/zaproxy/addon/graphql/ExtensionGraphQl.java) | GraphQL Circular Type Reference | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [462-245](https://opencre.org/cre/462-245). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
