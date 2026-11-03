---
id: "CRE-653-242"
title: "Enforce schema on type/contents of structured data"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-653-242
excerpt: "CRE 653-242 · in Technical application security controls › Input and output protection › Input validation · 139 mappings to 7 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets, OWASP Proactive Controls, OWASP Web Security Testing Guide (WSTG), ZAP Rule
---
> **CRE**: [653-242](https://opencre.org/cre/653-242)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-010-308]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-owasp-proactive-controls]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V5.1.4](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x13-V5-Validation-Sanitization-Encoding.md#v51-input-validation) | Verify that structured data is strongly typed and validated against a defined schema including allowed characters, length and pattern (e.g. credit card numbers, e-mail addresses, telephone numbers, or validating that two related fields are reasonable, such as checking that suburb and zip/postcode match). | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [3](https://capec.mitre.org/data/definitions/3.html) | Using Leading 'Ghost' Character Sequences to Bypass Input Filters | automatic |
| [7](https://capec.mitre.org/data/definitions/7.html) | Blind SQL Injection | automatic |
| [8](https://capec.mitre.org/data/definitions/8.html) | Buffer Overflow in an API Call | automatic |
| [9](https://capec.mitre.org/data/definitions/9.html) | Buffer Overflow in Local Command-Line Utilities | automatic |
| [10](https://capec.mitre.org/data/definitions/10.html) | Buffer Overflow via Environment Variables | automatic |
| [13](https://capec.mitre.org/data/definitions/13.html) | Subverting Environment Variable Values | automatic |
| [14](https://capec.mitre.org/data/definitions/14.html) | Client-side Injection-induced Buffer Overflow | automatic |
| [22](https://capec.mitre.org/data/definitions/22.html) | Exploiting Trust in Client | automatic |
| [23](https://capec.mitre.org/data/definitions/23.html) | File Content Injection | automatic |
| [24](https://capec.mitre.org/data/definitions/24.html) | Filter Failure through Buffer Overflow | automatic |
| [28](https://capec.mitre.org/data/definitions/28.html) | Fuzzing | automatic |
| [31](https://capec.mitre.org/data/definitions/31.html) | Accessing/Intercepting/Modifying HTTP Cookies | automatic |
| [42](https://capec.mitre.org/data/definitions/42.html) | MIME Conversion | automatic |
| [43](https://capec.mitre.org/data/definitions/43.html) | Exploiting Multiple Input Interpretation Layers | automatic |
| [45](https://capec.mitre.org/data/definitions/45.html) | Buffer Overflow via Symbolic Links | automatic |
| [46](https://capec.mitre.org/data/definitions/46.html) | Overflow Variables and Tags | automatic |
| [47](https://capec.mitre.org/data/definitions/47.html) | Buffer Overflow via Parameter Expansion | automatic |
| [52](https://capec.mitre.org/data/definitions/52.html) | Embedding NULL Bytes | automatic |
| [53](https://capec.mitre.org/data/definitions/53.html) | Postfix, Null Terminate, and Backslash | automatic |
| [63](https://capec.mitre.org/data/definitions/63.html) | Cross-Site Scripting (XSS) | automatic |
| [64](https://capec.mitre.org/data/definitions/64.html) | Using Slashes and URL Encoding Combined to Bypass Validation Logic | automatic |
| [66](https://capec.mitre.org/data/definitions/66.html) | SQL Injection | automatic |
| [67](https://capec.mitre.org/data/definitions/67.html) | String Format Overflow in syslog() | automatic |
| [71](https://capec.mitre.org/data/definitions/71.html) | Using Unicode Encoding to Bypass Validation Logic | automatic |
| [72](https://capec.mitre.org/data/definitions/72.html) | URL Encoding | automatic |
| [73](https://capec.mitre.org/data/definitions/73.html) | User-Controlled Filename | automatic |
| [78](https://capec.mitre.org/data/definitions/78.html) | Using Escaped Slashes in Alternate Encoding | automatic |
| [79](https://capec.mitre.org/data/definitions/79.html) | Using Slashes in Alternate Encoding | automatic |
| [80](https://capec.mitre.org/data/definitions/80.html) | Using UTF-8 Encoding to Bypass Validation Logic | automatic |
| [81](https://capec.mitre.org/data/definitions/81.html) | Web Server Logs Tampering | automatic |
| [83](https://capec.mitre.org/data/definitions/83.html) | XPath Injection | automatic |
| [85](https://capec.mitre.org/data/definitions/85.html) | AJAX Footprinting | automatic |
| [88](https://capec.mitre.org/data/definitions/88.html) | OS Command Injection | automatic |
| [101](https://capec.mitre.org/data/definitions/101.html) | Server Side Include (SSI) Injection | automatic |
| [104](https://capec.mitre.org/data/definitions/104.html) | Cross Zone Scripting | automatic |
| [108](https://capec.mitre.org/data/definitions/108.html) | Command Line Execution through SQL Injection | automatic |
| [109](https://capec.mitre.org/data/definitions/109.html) | Object Relational Mapping Injection | automatic |
| [110](https://capec.mitre.org/data/definitions/110.html) | SQL Injection through SOAP Parameter Tampering | automatic |
| [120](https://capec.mitre.org/data/definitions/120.html) | Double Encoding | automatic |
| [135](https://capec.mitre.org/data/definitions/135.html) | Format String Injection | automatic |
| [136](https://capec.mitre.org/data/definitions/136.html) | LDAP Injection | automatic |
| [153](https://capec.mitre.org/data/definitions/153.html) | Input Data Manipulation | automatic |
| [182](https://capec.mitre.org/data/definitions/182.html) | Flash Injection | automatic |
| [209](https://capec.mitre.org/data/definitions/209.html) | XSS Using MIME Type Mismatch | automatic |
| [230](https://capec.mitre.org/data/definitions/230.html) | Serialized Data with Nested Payloads | automatic |
| [231](https://capec.mitre.org/data/definitions/231.html) | Oversized Serialized Data Payloads | automatic |
| [250](https://capec.mitre.org/data/definitions/250.html) | XML Injection | automatic |
| [261](https://capec.mitre.org/data/definitions/261.html) | Fuzzing for garnering other adjacent user/sensitive data | automatic |
| [267](https://capec.mitre.org/data/definitions/267.html) | Leverage Alternate Encoding | automatic |
| [473](https://capec.mitre.org/data/definitions/473.html) | Signature Spoof | automatic |
| [588](https://capec.mitre.org/data/definitions/588.html) | DOM-Based XSS | automatic |
| [664](https://capec.mitre.org/data/definitions/664.html) | Server Side Request Forgery | automatic |
| [676](https://capec.mitre.org/data/definitions/676.html) | NoSQL Injection | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [20](https://cwe.mitre.org/data/definitions/20.html) | Improper Input Validation | curated |
| [15](https://cwe.mitre.org/data/definitions/15.html) | External Control of System or Configuration Setting | automatic |
| [73](https://cwe.mitre.org/data/definitions/73.html) | External Control of File Name or Path | automatic |
| [102](https://cwe.mitre.org/data/definitions/102.html) | Struts: Duplicate Validation Forms | automatic |
| [103](https://cwe.mitre.org/data/definitions/103.html) | Struts: Incomplete validate() Method Definition | automatic |
| [104](https://cwe.mitre.org/data/definitions/104.html) | Struts: Form Bean Does Not Extend Validation Class | automatic |
| [105](https://cwe.mitre.org/data/definitions/105.html) | Struts: Form Field Without Validator | automatic |
| [106](https://cwe.mitre.org/data/definitions/106.html) | Struts: Plug-in Framework not in Use | automatic |
| [107](https://cwe.mitre.org/data/definitions/107.html) | Struts: Unused Validation Form | automatic |
| [108](https://cwe.mitre.org/data/definitions/108.html) | Struts: Unvalidated Action Form | automatic |
| [109](https://cwe.mitre.org/data/definitions/109.html) | Struts: Validator Turned Off | automatic |
| [110](https://cwe.mitre.org/data/definitions/110.html) | Struts: Validator Without Form Field | automatic |
| [111](https://cwe.mitre.org/data/definitions/111.html) | Direct Use of Unsafe JNI | automatic |
| [112](https://cwe.mitre.org/data/definitions/112.html) | Missing XML Validation | automatic |
| [113](https://cwe.mitre.org/data/definitions/113.html) | Improper Neutralization of CRLF Sequences in HTTP Headers ('HTTP Request/Response Splitting') | automatic |
| [114](https://cwe.mitre.org/data/definitions/114.html) | Process Control | automatic |
| [117](https://cwe.mitre.org/data/definitions/117.html) | Improper Output Neutralization for Logs | automatic |
| [119](https://cwe.mitre.org/data/definitions/119.html) | Improper Restriction of Operations within the Bounds of a Memory Buffer | automatic |
| [120](https://cwe.mitre.org/data/definitions/120.html) | Buffer Copy without Checking Size of Input ('Classic Buffer Overflow') | automatic |
| [121](https://cwe.mitre.org/data/definitions/121.html) | Stack-based Buffer Overflow | automatic |
| [122](https://cwe.mitre.org/data/definitions/122.html) | Heap-based Buffer Overflow | automatic |
| [123](https://cwe.mitre.org/data/definitions/123.html) | Write-what-where Condition | automatic |
| [124](https://cwe.mitre.org/data/definitions/124.html) | Buffer Underwrite ('Buffer Underflow') | automatic |
| [125](https://cwe.mitre.org/data/definitions/125.html) | Out-of-bounds Read | automatic |
| [126](https://cwe.mitre.org/data/definitions/126.html) | Buffer Over-read | automatic |
| [127](https://cwe.mitre.org/data/definitions/127.html) | Buffer Under-read | automatic |
| [129](https://cwe.mitre.org/data/definitions/129.html) | Improper Validation of Array Index | automatic |
| [130](https://cwe.mitre.org/data/definitions/130.html) | Improper Handling of Length Parameter Inconsistency | automatic |
| [134](https://cwe.mitre.org/data/definitions/134.html) | Use of Externally-Controlled Format String | automatic |
| [170](https://cwe.mitre.org/data/definitions/170.html) | Improper Null Termination | automatic |
| [179](https://cwe.mitre.org/data/definitions/179.html) | Incorrect Behavior Order: Early Validation | automatic |
| [180](https://cwe.mitre.org/data/definitions/180.html) | Incorrect Behavior Order: Validate Before Canonicalize | automatic |
| [181](https://cwe.mitre.org/data/definitions/181.html) | Incorrect Behavior Order: Validate Before Filter | automatic |
| [190](https://cwe.mitre.org/data/definitions/190.html) | Integer Overflow or Wraparound | automatic |
| [415](https://cwe.mitre.org/data/definitions/415.html) | Double Free | automatic |
| [416](https://cwe.mitre.org/data/definitions/416.html) | Use After Free | automatic |
| [466](https://cwe.mitre.org/data/definitions/466.html) | Return of Pointer Value Outside of Expected Range | automatic |
| [470](https://cwe.mitre.org/data/definitions/470.html) | Use of Externally-Controlled Input to Select Classes or Code ('Unsafe Reflection') | automatic |
| [554](https://cwe.mitre.org/data/definitions/554.html) | ASP.NET Misconfiguration: Not Using Input Validation Framework | automatic |
| [606](https://cwe.mitre.org/data/definitions/606.html) | Unchecked Input for Loop Condition | automatic |
| [622](https://cwe.mitre.org/data/definitions/622.html) | Improper Validation of Function Hook Arguments | automatic |
| [647](https://cwe.mitre.org/data/definitions/647.html) | Use of Non-Canonical URL Paths for Authorization Decisions | automatic |
| [680](https://cwe.mitre.org/data/definitions/680.html) | Integer Overflow to Buffer Overflow | automatic |
| [781](https://cwe.mitre.org/data/definitions/781.html) | Improper Address Validation in IOCTL with METHOD_NEITHER I/O Control Code | automatic |
| [785](https://cwe.mitre.org/data/definitions/785.html) | Use of Path Manipulation Function without Maximum-sized Buffer | automatic |
| [786](https://cwe.mitre.org/data/definitions/786.html) | Access of Memory Location Before Start of Buffer | automatic |
| [787](https://cwe.mitre.org/data/definitions/787.html) | Out-of-bounds Write | automatic |
| [788](https://cwe.mitre.org/data/definitions/788.html) | Access of Memory Location After End of Buffer | automatic |
| [805](https://cwe.mitre.org/data/definitions/805.html) | Buffer Access with Incorrect Length Value | automatic |
| [806](https://cwe.mitre.org/data/definitions/806.html) | Buffer Access Using Size of Source Buffer | automatic |
| [822](https://cwe.mitre.org/data/definitions/822.html) | Untrusted Pointer Dereference | automatic |
| [823](https://cwe.mitre.org/data/definitions/823.html) | Use of Out-of-range Pointer Offset | automatic |
| [824](https://cwe.mitre.org/data/definitions/824.html) | Access of Uninitialized Pointer | automatic |
| [825](https://cwe.mitre.org/data/definitions/825.html) | Expired Pointer Dereference | automatic |
| [1173](https://cwe.mitre.org/data/definitions/1173.html) | Improper Use of Validation Framework | automatic |
| [1174](https://cwe.mitre.org/data/definitions/1174.html) | ASP.NET Misconfiguration: Improper Model Validation | automatic |
| [1284](https://cwe.mitre.org/data/definitions/1284.html) | Improper Validation of Specified Quantity in Input | automatic |
| [1285](https://cwe.mitre.org/data/definitions/1285.html) | Improper Validation of Specified Index, Position, or Offset in Input | automatic |
| [1286](https://cwe.mitre.org/data/definitions/1286.html) | Improper Validation of Syntactic Correctness of Input | automatic |
| [1287](https://cwe.mitre.org/data/definitions/1287.html) | Improper Validation of Specified Type of Input | automatic |
| [1288](https://cwe.mitre.org/data/definitions/1288.html) | Improper Validation of Consistency within Input | automatic |
| [1289](https://cwe.mitre.org/data/definitions/1289.html) | Improper Validation of Unsafe Equivalence in Input | automatic |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Mass Assignment Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Proactive Controls

| ID | Section | Link |
| --- | --- | --- |
|  | [C5](https://owasp-top-10-proactive-controls-2018.readthedocs.io/en/latest/c5-validate-all-inputs.html) | curated |

More: [[standard-owasp-proactive-controls]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-INPV-00](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [10026](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrulesBeta/src/main/java/org/zaproxy/zap/extension/pscanrulesBeta/ServletParameterPollutionScanRule.java) | HTTP Parameter Override | automatic |
| [10030](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/UserControlledCharsetScanRule.java) | User Controllable Charset | automatic |
| [10031](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/UserControlledHTMLAttributesScanRule.java) | User Controllable HTML Element Attribute (Potential XSS) | automatic |
| [10043](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/UserControlledJavascriptEventScanRule.java) | User Controllable JavaScript Event (XSS) | automatic |
| [10051](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/RelativePathConfusionScanRule.java) | Relative Path Confusion | automatic |
| [10107](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/HttPoxyScanRule.java) | Httpoxy - Proxy Header Misuse | automatic |
| [20014](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/HttpParameterPollutionScanRule.java) | HTTP Parameter Pollution | automatic |
| [20017](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/SourceCodeDisclosureCve20121823ScanRule.java) | Source Code Disclosure - CVE-2012-1823 | automatic |
| [20018](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/RemoteCodeExecutionCve20121823ScanRule.java) | Remote Code Execution - CVE-2012-1823 | automatic |
| [100018](https://github.com/zaproxy/community-scripts/blob/main/passive/RPO.js) | Relative Path Overwrite | automatic |
| [100044-1](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesAlpha/src/main/zapHomeFiles/scripts/scripts/active/SuspiciousInputTransformation.js) | Suspicious Input Transformation - Quote Consumption | automatic |
| [100044-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesAlpha/src/main/zapHomeFiles/scripts/scripts/active/SuspiciousInputTransformation.js) | Suspicious Input Transformation - Arithmetic Evaluation | automatic |
| [100044-3](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesAlpha/src/main/zapHomeFiles/scripts/scripts/active/SuspiciousInputTransformation.js) | Suspicious Input Transformation - Expression Evaluation | automatic |
| [100044-4](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesAlpha/src/main/zapHomeFiles/scripts/scripts/active/SuspiciousInputTransformation.js) | Suspicious Input Transformation - Template Evaluation | automatic |
| [100044-5](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesAlpha/src/main/zapHomeFiles/scripts/scripts/active/SuspiciousInputTransformation.js) | Suspicious Input Transformation - EL Evaluation | automatic |
| [100044-6](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesAlpha/src/main/zapHomeFiles/scripts/scripts/active/SuspiciousInputTransformation.js) | Suspicious Input Transformation - Unicode Normalisation | automatic |
| [100044-7](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesAlpha/src/main/zapHomeFiles/scripts/scripts/active/SuspiciousInputTransformation.js) | Suspicious Input Transformation - URL Decoding Error | automatic |
| [100044-8](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesAlpha/src/main/zapHomeFiles/scripts/scripts/active/SuspiciousInputTransformation.js) | Suspicious Input Transformation - Unicode Byte Truncation | automatic |
| [100044-9](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesAlpha/src/main/zapHomeFiles/scripts/scripts/active/SuspiciousInputTransformation.js) | Suspicious Input Transformation - Unicode Case Conversion | automatic |
| [100044-10](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesAlpha/src/main/zapHomeFiles/scripts/scripts/active/SuspiciousInputTransformation.js) | Suspicious Input Transformation - Unicode Combining Diacritic | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [653-242](https://opencre.org/cre/653-242). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
