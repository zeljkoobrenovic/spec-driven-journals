---
id: "CRE-660-052"
title: "Validate max input/file sizes"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-660-052
excerpt: "CRE 660-052 · in Technical application security controls › Input and output protection › File handling › File upload · 32 mappings to 6 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets, OWASP Web Security Testing Guide (WSTG), ZAP Rule
---
> **CRE**: [660-052](https://opencre.org/cre/660-052)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-130-550]] › [[cre-621-287]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-zap-rule]]

## Related CREs

- [[cre-623-550]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V12.1.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x20-V12-Files-Resources.md#v121-file-upload) | Verify that the application will not accept large files that could fill up storage or cause a denial of service. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [147](https://capec.mitre.org/data/definitions/147.html) | XML Ping of the Death | automatic |
| [212](https://capec.mitre.org/data/definitions/212.html) | Functionality Misuse | automatic |
| [227](https://capec.mitre.org/data/definitions/227.html) | Sustained Client Engagement | automatic |
| [492](https://capec.mitre.org/data/definitions/492.html) | Regular Expression Exponential Blowup | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [400](https://cwe.mitre.org/data/definitions/400.html) | Uncontrolled Resource Consumption | curated |
| [405](https://cwe.mitre.org/data/definitions/405.html) | Asymmetric Resource Consumption (Amplification) | automatic |
| [406](https://cwe.mitre.org/data/definitions/406.html) | Insufficient Control of Network Message Volume (Network Amplification) | automatic |
| [407](https://cwe.mitre.org/data/definitions/407.html) | Inefficient Algorithmic Complexity | automatic |
| [408](https://cwe.mitre.org/data/definitions/408.html) | Incorrect Behavior Order: Early Amplification | automatic |
| [409](https://cwe.mitre.org/data/definitions/409.html) | Improper Handling of Highly Compressed Data (Data Amplification) | automatic |
| [770](https://cwe.mitre.org/data/definitions/770.html) | Allocation of Resources Without Limits or Throttling | automatic |
| [771](https://cwe.mitre.org/data/definitions/771.html) | Missing Reference to Active Allocated Resource | automatic |
| [773](https://cwe.mitre.org/data/definitions/773.html) | Missing Reference to Active File Descriptor or Handle | automatic |
| [774](https://cwe.mitre.org/data/definitions/774.html) | Allocation of File Descriptors or Handles Without Limits or Throttling | automatic |
| [776](https://cwe.mitre.org/data/definitions/776.html) | Improper Restriction of Recursive Entity References in DTDs ('XML Entity Expansion') | automatic |
| [779](https://cwe.mitre.org/data/definitions/779.html) | Logging of Excessive Data | automatic |
| [789](https://cwe.mitre.org/data/definitions/789.html) | Memory Allocation with Excessive Size Value | automatic |
| [920](https://cwe.mitre.org/data/definitions/920.html) | Improper Restriction of Power Consumption | automatic |
| [1046](https://cwe.mitre.org/data/definitions/1046.html) | Creation of Immutable Text Using String Concatenation | automatic |
| [1049](https://cwe.mitre.org/data/definitions/1049.html) | Excessive Data Query Operations in a Large Data Table | automatic |
| [1050](https://cwe.mitre.org/data/definitions/1050.html) | Excessive Platform Resource Consumption within a Loop | automatic |
| [1067](https://cwe.mitre.org/data/definitions/1067.html) | Excessive Execution of Sequential Searches of Data Resource | automatic |
| [1089](https://cwe.mitre.org/data/definitions/1089.html) | Large Data Table with Excessive Number of Indices | automatic |
| [1176](https://cwe.mitre.org/data/definitions/1176.html) | Inefficient CPU Computation | automatic |
| [1235](https://cwe.mitre.org/data/definitions/1235.html) | Incorrect Use of Autoboxing and Unboxing for Performance Critical Operations | automatic |
| [1246](https://cwe.mitre.org/data/definitions/1246.html) | Improper Write Handling in Limited-write Non-Volatile Memories | automatic |
| [1325](https://cwe.mitre.org/data/definitions/1325.html) | Improperly Controlled Sequential Memory Allocation | automatic |
| [1333](https://cwe.mitre.org/data/definitions/1333.html) | Inefficient Regular Expression Complexity | automatic |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-BUSL-09](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/10-Business_Logic_Testing/09-Test_Upload_of_Malicious_Files.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [10053](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/ApacheRangeHeaderDosScanRule.java) | Apache Range Header DoS (CVE-2011-3192) | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [660-052](https://opencre.org/cre/660-052). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
