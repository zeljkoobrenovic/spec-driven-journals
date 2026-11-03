---
id: "CRE-483-715"
title: "White-list HTTP methods"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-483-715
excerpt: "CRE 483-715 · in Technical application security controls › Input and output protection › Validate HTTP request headers · 8 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Web Security Testing Guide (WSTG), ZAP Rule
---
> **CRE**: [483-715](https://opencre.org/cre/483-715)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-541-441]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V14.5.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x22-V14-Config.md#v145-http-request-header-validation) | Verify that the application server only accepts the HTTP methods in use by the application/API, including pre-flight OPTIONS, and logs/alerts on any requests that are not valid for the application context. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [500](https://capec.mitre.org/data/definitions/500.html) | WebView Injection | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [749](https://cwe.mitre.org/data/definitions/749.html) | Exposed Dangerous Method or Function | curated |
| [618](https://cwe.mitre.org/data/definitions/618.html) | Exposed Unsafe ActiveX Method | automatic |
| [782](https://cwe.mitre.org/data/definitions/782.html) | Exposed IOCTL with Insufficient Access Control | automatic |

More: [[standard-cwe]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-CONF-06](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/06-Test_HTTP_Methods.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [10110](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrulesBeta/src/main/java/org/zaproxy/zap/extension/pscanrulesBeta/JsFunctionScanRule.java) | Dangerous JS Functions | automatic |
| [90028](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/InsecureHttpMethodScanRule.java) | Insecure HTTP Method | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [483-715](https://opencre.org/cre/483-715). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
