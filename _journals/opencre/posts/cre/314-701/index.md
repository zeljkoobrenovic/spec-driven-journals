---
id: "CRE-314-701"
title: "Whitelist file extensions served by web tier"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-314-701
excerpt: "CRE 314-701 · in Technical application security controls › Input and output protection › File handling › File download · 21 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Web Security Testing Guide (WSTG), ZAP Rule
---
> **CRE**: [314-701](https://opencre.org/cre/314-701)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-130-550]] › [[cre-040-843]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V12.5.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x20-V12-Files-Resources.md#v125-file-download) | Verify that the web tier is configured to serve only files with specific file extensions to prevent unintentional information and source code leakage. For example, backup files (e.g. .bak), temporary working files (e.g. .swp), compressed files (.zip, .tar.gz, etc) and other extensions commonly used by editors should be blocked unless required. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [21](https://capec.mitre.org/data/definitions/21.html) | Exploitation of Trusted Identifiers | automatic |
| [31](https://capec.mitre.org/data/definitions/31.html) | Accessing/Intercepting/Modifying HTTP Cookies | automatic |
| [39](https://capec.mitre.org/data/definitions/39.html) | Manipulating Opaque Client-based Data Tokens | automatic |
| [59](https://capec.mitre.org/data/definitions/59.html) | Session Credential Falsification through Prediction | automatic |
| [60](https://capec.mitre.org/data/definitions/60.html) | Reusing Session IDs (aka Session Replay) | automatic |
| [150](https://capec.mitre.org/data/definitions/150.html) | Collect Data from Common Resource Locations | automatic |
| [639](https://capec.mitre.org/data/definitions/639.html) | Probe System Files | automatic |
| [650](https://capec.mitre.org/data/definitions/650.html) | Upload a Web Shell to a Web Server | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [552](https://cwe.mitre.org/data/definitions/552.html) | Files or Directories Accessible to External Parties | curated |
| [219](https://cwe.mitre.org/data/definitions/219.html) | Storage of File with Sensitive Data Under Web Root | automatic |
| [220](https://cwe.mitre.org/data/definitions/220.html) | Storage of File With Sensitive Data Under FTP Root | automatic |
| [433](https://cwe.mitre.org/data/definitions/433.html) | Unparsed Raw Web Content Delivery | automatic |
| [527](https://cwe.mitre.org/data/definitions/527.html) | Exposure of Version-Control Repository to an Unauthorized Control Sphere | automatic |
| [528](https://cwe.mitre.org/data/definitions/528.html) | Exposure of Core Dump File to an Unauthorized Control Sphere | automatic |
| [529](https://cwe.mitre.org/data/definitions/529.html) | Exposure of Access Control List Files to an Unauthorized Control Sphere | automatic |
| [530](https://cwe.mitre.org/data/definitions/530.html) | Exposure of Backup File to an Unauthorized Control Sphere | automatic |
| [539](https://cwe.mitre.org/data/definitions/539.html) | Use of Persistent Cookies Containing Sensitive Information | automatic |
| [553](https://cwe.mitre.org/data/definitions/553.html) | Command Shell in Externally Accessible Directory | automatic |

More: [[standard-cwe]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-BUSL-08](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/10-Business_Logic_Testing/08-Test_Upload_of_Unexpected_File_Types.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [10095](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/BackupFileDisclosureScanRule.java) | Backup File Disclosure | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [314-701](https://opencre.org/cre/314-701). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
