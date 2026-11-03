---
id: "CRE-782-234"
title: "Clear policy compliant I/O requirements"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-782-234
excerpt: "CRE 782-234 · in Governance processes for security › Security Analysis and documentation › Security requirements · 227 mappings to 6 standards and tools."
tags: ASVS, CAPEC, CWE, ISO 27001, OWASP Cheat Sheets, ZAP Rule
---
> **CRE**: [782-234](https://opencre.org/cre/782-234)
>
> **Part of**: [[cre-567-755]] › [[cre-766-162]] › [[cre-004-517]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-iso-27001]], [[standard-owasp-cheat-sheets]], [[standard-zap-rule]]

## Related CREs

- [[cre-503-455]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V1.5.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x10-V1-Architecture.md#v15-input-and-output-architecture) | Verify that input and output requirements clearly define how to handle and process data based on type, content, and applicable laws, regulations, and other policy compliance. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [3](https://capec.mitre.org/data/definitions/3.html) | Using Leading 'Ghost' Character Sequences to Bypass Input Filters | automatic |
| [6](https://capec.mitre.org/data/definitions/6.html) | Argument Injection | automatic |
| [7](https://capec.mitre.org/data/definitions/7.html) | Blind SQL Injection | automatic |
| [8](https://capec.mitre.org/data/definitions/8.html) | Buffer Overflow in an API Call | automatic |
| [9](https://capec.mitre.org/data/definitions/9.html) | Buffer Overflow in Local Command-Line Utilities | automatic |
| [10](https://capec.mitre.org/data/definitions/10.html) | Buffer Overflow via Environment Variables | automatic |
| [13](https://capec.mitre.org/data/definitions/13.html) | Subverting Environment Variable Values | automatic |
| [14](https://capec.mitre.org/data/definitions/14.html) | Client-side Injection-induced Buffer Overflow | automatic |
| [15](https://capec.mitre.org/data/definitions/15.html) | Command Delimiters | automatic |
| [24](https://capec.mitre.org/data/definitions/24.html) | Filter Failure through Buffer Overflow | automatic |
| [28](https://capec.mitre.org/data/definitions/28.html) | Fuzzing | automatic |
| [34](https://capec.mitre.org/data/definitions/34.html) | HTTP Response Splitting | automatic |
| [42](https://capec.mitre.org/data/definitions/42.html) | MIME Conversion | automatic |
| [43](https://capec.mitre.org/data/definitions/43.html) | Exploiting Multiple Input Interpretation Layers | automatic |
| [45](https://capec.mitre.org/data/definitions/45.html) | Buffer Overflow via Symbolic Links | automatic |
| [46](https://capec.mitre.org/data/definitions/46.html) | Overflow Variables and Tags | automatic |
| [47](https://capec.mitre.org/data/definitions/47.html) | Buffer Overflow via Parameter Expansion | automatic |
| [51](https://capec.mitre.org/data/definitions/51.html) | Poison Web Service Registry | automatic |
| [52](https://capec.mitre.org/data/definitions/52.html) | Embedding NULL Bytes | automatic |
| [53](https://capec.mitre.org/data/definitions/53.html) | Postfix, Null Terminate, and Backslash | automatic |
| [64](https://capec.mitre.org/data/definitions/64.html) | Using Slashes and URL Encoding Combined to Bypass Validation Logic | automatic |
| [67](https://capec.mitre.org/data/definitions/67.html) | String Format Overflow in syslog() | automatic |
| [71](https://capec.mitre.org/data/definitions/71.html) | Using Unicode Encoding to Bypass Validation Logic | automatic |
| [72](https://capec.mitre.org/data/definitions/72.html) | URL Encoding | automatic |
| [76](https://capec.mitre.org/data/definitions/76.html) | Manipulating Web Input to File System Calls | automatic |
| [78](https://capec.mitre.org/data/definitions/78.html) | Using Escaped Slashes in Alternate Encoding | automatic |
| [79](https://capec.mitre.org/data/definitions/79.html) | Using Slashes in Alternate Encoding | automatic |
| [80](https://capec.mitre.org/data/definitions/80.html) | Using UTF-8 Encoding to Bypass Validation Logic | automatic |
| [83](https://capec.mitre.org/data/definitions/83.html) | XPath Injection | automatic |
| [84](https://capec.mitre.org/data/definitions/84.html) | XQuery Injection | automatic |
| [101](https://capec.mitre.org/data/definitions/101.html) | Server Side Include (SSI) Injection | automatic |
| [105](https://capec.mitre.org/data/definitions/105.html) | HTTP Request Splitting | automatic |
| [108](https://capec.mitre.org/data/definitions/108.html) | Command Line Execution through SQL Injection | automatic |
| [120](https://capec.mitre.org/data/definitions/120.html) | Double Encoding | automatic |
| [135](https://capec.mitre.org/data/definitions/135.html) | Format String Injection | automatic |
| [250](https://capec.mitre.org/data/definitions/250.html) | XML Injection | automatic |
| [267](https://capec.mitre.org/data/definitions/267.html) | Leverage Alternate Encoding | automatic |
| [273](https://capec.mitre.org/data/definitions/273.html) | HTTP Response Smuggling | automatic |
| [276](https://capec.mitre.org/data/definitions/276.html) | Inter-component Protocol Manipulation | automatic |
| [277](https://capec.mitre.org/data/definitions/277.html) | Data Interchange Protocol Manipulation | automatic |
| [278](https://capec.mitre.org/data/definitions/278.html) | Web Services Protocol Manipulation | automatic |
| [279](https://capec.mitre.org/data/definitions/279.html) | SOAP Manipulation | automatic |
| [468](https://capec.mitre.org/data/definitions/468.html) | Generic Cross-Browser Cross-Domain Theft | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [707](https://cwe.mitre.org/data/definitions/707.html) | Improper Neutralization | curated |
| [15](https://cwe.mitre.org/data/definitions/15.html) | External Control of System or Configuration Setting | automatic |
| [20](https://cwe.mitre.org/data/definitions/20.html) | Improper Input Validation | automatic |
| [37](https://cwe.mitre.org/data/definitions/37.html) | Path Traversal: '/absolute/pathname/here' | automatic |
| [42](https://cwe.mitre.org/data/definitions/42.html) | Path Equivalence: 'filename.' (Trailing Dot) | automatic |
| [43](https://cwe.mitre.org/data/definitions/43.html) | Path Equivalence: 'filename....' (Multiple Trailing Dot) | automatic |
| [45](https://cwe.mitre.org/data/definitions/45.html) | Path Equivalence: 'file...name' (Multiple Internal Dot) | automatic |
| [46](https://cwe.mitre.org/data/definitions/46.html) | Path Equivalence: 'filename ' (Trailing Space) | automatic |
| [49](https://cwe.mitre.org/data/definitions/49.html) | Path Equivalence: 'filename/' (Trailing Slash) | automatic |
| [50](https://cwe.mitre.org/data/definitions/50.html) | Path Equivalence: '//multiple/leading/slash' | automatic |
| [52](https://cwe.mitre.org/data/definitions/52.html) | Path Equivalence: '/multiple/trailing/slash//' | automatic |
| [53](https://cwe.mitre.org/data/definitions/53.html) | Path Equivalence: '\multiple\\internal\backslash' | automatic |
| [54](https://cwe.mitre.org/data/definitions/54.html) | Path Equivalence: 'filedir\' (Trailing Backslash) | automatic |
| [56](https://cwe.mitre.org/data/definitions/56.html) | Path Equivalence: 'filedir*' (Wildcard) | automatic |
| [73](https://cwe.mitre.org/data/definitions/73.html) | External Control of File Name or Path | automatic |
| [74](https://cwe.mitre.org/data/definitions/74.html) | Improper Neutralization of Special Elements in Output Used by a Downstream Component ('Injection') | automatic |
| [75](https://cwe.mitre.org/data/definitions/75.html) | Failure to Sanitize Special Elements into a Different Plane (Special Element Injection) | automatic |
| [76](https://cwe.mitre.org/data/definitions/76.html) | Improper Neutralization of Equivalent Special Elements | automatic |
| [77](https://cwe.mitre.org/data/definitions/77.html) | Improper Neutralization of Special Elements used in a Command ('Command Injection') | automatic |
| [78](https://cwe.mitre.org/data/definitions/78.html) | Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection') | automatic |
| [79](https://cwe.mitre.org/data/definitions/79.html) | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') | automatic |
| [80](https://cwe.mitre.org/data/definitions/80.html) | Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic XSS) | automatic |
| [81](https://cwe.mitre.org/data/definitions/81.html) | Improper Neutralization of Script in an Error Message Web Page | automatic |
| [82](https://cwe.mitre.org/data/definitions/82.html) | Improper Neutralization of Script in Attributes of IMG Tags in a Web Page | automatic |
| [83](https://cwe.mitre.org/data/definitions/83.html) | Improper Neutralization of Script in Attributes in a Web Page | automatic |
| [84](https://cwe.mitre.org/data/definitions/84.html) | Improper Neutralization of Encoded URI Schemes in a Web Page | automatic |
| [85](https://cwe.mitre.org/data/definitions/85.html) | Doubled Character XSS Manipulations | automatic |
| [86](https://cwe.mitre.org/data/definitions/86.html) | Improper Neutralization of Invalid Characters in Identifiers in Web Pages | automatic |
| [87](https://cwe.mitre.org/data/definitions/87.html) | Improper Neutralization of Alternate XSS Syntax | automatic |
| [88](https://cwe.mitre.org/data/definitions/88.html) | Improper Neutralization of Argument Delimiters in a Command ('Argument Injection') | automatic |
| [89](https://cwe.mitre.org/data/definitions/89.html) | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') | automatic |
| [90](https://cwe.mitre.org/data/definitions/90.html) | Improper Neutralization of Special Elements used in an LDAP Query ('LDAP Injection') | automatic |
| [91](https://cwe.mitre.org/data/definitions/91.html) | XML Injection (aka Blind XPath Injection) | automatic |
| [93](https://cwe.mitre.org/data/definitions/93.html) | Improper Neutralization of CRLF Sequences ('CRLF Injection') | automatic |
| [94](https://cwe.mitre.org/data/definitions/94.html) | Improper Control of Generation of Code ('Code Injection') | automatic |
| [95](https://cwe.mitre.org/data/definitions/95.html) | Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection') | automatic |
| [96](https://cwe.mitre.org/data/definitions/96.html) | Improper Neutralization of Directives in Statically Saved Code ('Static Code Injection') | automatic |
| [97](https://cwe.mitre.org/data/definitions/97.html) | Improper Neutralization of Server-Side Includes (SSI) Within a Web Page | automatic |
| [99](https://cwe.mitre.org/data/definitions/99.html) | Improper Control of Resource Identifiers ('Resource Injection') | automatic |
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
| [116](https://cwe.mitre.org/data/definitions/116.html) | Improper Encoding or Escaping of Output | automatic |
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
| [138](https://cwe.mitre.org/data/definitions/138.html) | Improper Neutralization of Special Elements | automatic |
| [140](https://cwe.mitre.org/data/definitions/140.html) | Improper Neutralization of Delimiters | automatic |
| [141](https://cwe.mitre.org/data/definitions/141.html) | Improper Neutralization of Parameter/Argument Delimiters | automatic |
| [142](https://cwe.mitre.org/data/definitions/142.html) | Improper Neutralization of Value Delimiters | automatic |
| [143](https://cwe.mitre.org/data/definitions/143.html) | Improper Neutralization of Record Delimiters | automatic |
| [144](https://cwe.mitre.org/data/definitions/144.html) | Improper Neutralization of Line Delimiters | automatic |
| [145](https://cwe.mitre.org/data/definitions/145.html) | Improper Neutralization of Section Delimiters | automatic |
| [146](https://cwe.mitre.org/data/definitions/146.html) | Improper Neutralization of Expression/Command Delimiters | automatic |
| [147](https://cwe.mitre.org/data/definitions/147.html) | Improper Neutralization of Input Terminators | automatic |
| [148](https://cwe.mitre.org/data/definitions/148.html) | Improper Neutralization of Input Leaders | automatic |
| [149](https://cwe.mitre.org/data/definitions/149.html) | Improper Neutralization of Quoting Syntax | automatic |
| [150](https://cwe.mitre.org/data/definitions/150.html) | Improper Neutralization of Escape, Meta, or Control Sequences | automatic |
| [151](https://cwe.mitre.org/data/definitions/151.html) | Improper Neutralization of Comment Delimiters | automatic |
| [152](https://cwe.mitre.org/data/definitions/152.html) | Improper Neutralization of Macro Symbols | automatic |
| [153](https://cwe.mitre.org/data/definitions/153.html) | Improper Neutralization of Substitution Characters | automatic |
| [154](https://cwe.mitre.org/data/definitions/154.html) | Improper Neutralization of Variable Name Delimiters | automatic |
| [155](https://cwe.mitre.org/data/definitions/155.html) | Improper Neutralization of Wildcards or Matching Symbols | automatic |
| [156](https://cwe.mitre.org/data/definitions/156.html) | Improper Neutralization of Whitespace | automatic |
| [157](https://cwe.mitre.org/data/definitions/157.html) | Failure to Sanitize Paired Delimiters | automatic |
| [158](https://cwe.mitre.org/data/definitions/158.html) | Improper Neutralization of Null Byte or NUL Character | automatic |
| [159](https://cwe.mitre.org/data/definitions/159.html) | Improper Handling of Invalid Use of Special Elements | automatic |
| [160](https://cwe.mitre.org/data/definitions/160.html) | Improper Neutralization of Leading Special Elements | automatic |
| [161](https://cwe.mitre.org/data/definitions/161.html) | Improper Neutralization of Multiple Leading Special Elements | automatic |
| [162](https://cwe.mitre.org/data/definitions/162.html) | Improper Neutralization of Trailing Special Elements | automatic |
| [163](https://cwe.mitre.org/data/definitions/163.html) | Improper Neutralization of Multiple Trailing Special Elements | automatic |
| [164](https://cwe.mitre.org/data/definitions/164.html) | Improper Neutralization of Internal Special Elements | automatic |
| [165](https://cwe.mitre.org/data/definitions/165.html) | Improper Neutralization of Multiple Internal Special Elements | automatic |
| [166](https://cwe.mitre.org/data/definitions/166.html) | Improper Handling of Missing Special Element | automatic |
| [167](https://cwe.mitre.org/data/definitions/167.html) | Improper Handling of Additional Special Element | automatic |
| [168](https://cwe.mitre.org/data/definitions/168.html) | Improper Handling of Inconsistent Special Elements | automatic |
| [170](https://cwe.mitre.org/data/definitions/170.html) | Improper Null Termination | automatic |
| [172](https://cwe.mitre.org/data/definitions/172.html) | Encoding Error | automatic |
| [173](https://cwe.mitre.org/data/definitions/173.html) | Improper Handling of Alternate Encoding | automatic |
| [174](https://cwe.mitre.org/data/definitions/174.html) | Double Decoding of the Same Data | automatic |
| [175](https://cwe.mitre.org/data/definitions/175.html) | Improper Handling of Mixed Encoding | automatic |
| [176](https://cwe.mitre.org/data/definitions/176.html) | Improper Handling of Unicode Encoding | automatic |
| [177](https://cwe.mitre.org/data/definitions/177.html) | Improper Handling of URL Encoding (Hex Encoding) | automatic |
| [179](https://cwe.mitre.org/data/definitions/179.html) | Incorrect Behavior Order: Early Validation | automatic |
| [180](https://cwe.mitre.org/data/definitions/180.html) | Incorrect Behavior Order: Validate Before Canonicalize | automatic |
| [181](https://cwe.mitre.org/data/definitions/181.html) | Incorrect Behavior Order: Validate Before Filter | automatic |
| [182](https://cwe.mitre.org/data/definitions/182.html) | Collapse of Data into Unsafe Value | automatic |
| [190](https://cwe.mitre.org/data/definitions/190.html) | Integer Overflow or Wraparound | automatic |
| [228](https://cwe.mitre.org/data/definitions/228.html) | Improper Handling of Syntactically Invalid Structure | automatic |
| [229](https://cwe.mitre.org/data/definitions/229.html) | Improper Handling of Values | automatic |
| [230](https://cwe.mitre.org/data/definitions/230.html) | Improper Handling of Missing Values | automatic |
| [231](https://cwe.mitre.org/data/definitions/231.html) | Improper Handling of Extra Values | automatic |
| [232](https://cwe.mitre.org/data/definitions/232.html) | Improper Handling of Undefined Values | automatic |
| [233](https://cwe.mitre.org/data/definitions/233.html) | Improper Handling of Parameters | automatic |
| [234](https://cwe.mitre.org/data/definitions/234.html) | Failure to Handle Missing Parameter | automatic |
| [235](https://cwe.mitre.org/data/definitions/235.html) | Improper Handling of Extra Parameters | automatic |
| [236](https://cwe.mitre.org/data/definitions/236.html) | Improper Handling of Undefined Parameters | automatic |
| [237](https://cwe.mitre.org/data/definitions/237.html) | Improper Handling of Structural Elements | automatic |
| [238](https://cwe.mitre.org/data/definitions/238.html) | Improper Handling of Incomplete Structural Elements | automatic |
| [239](https://cwe.mitre.org/data/definitions/239.html) | Failure to Handle Incomplete Element | automatic |
| [240](https://cwe.mitre.org/data/definitions/240.html) | Improper Handling of Inconsistent Structural Elements | automatic |
| [241](https://cwe.mitre.org/data/definitions/241.html) | Improper Handling of Unexpected Data Type | automatic |
| [415](https://cwe.mitre.org/data/definitions/415.html) | Double Free | automatic |
| [416](https://cwe.mitre.org/data/definitions/416.html) | Use After Free | automatic |
| [462](https://cwe.mitre.org/data/definitions/462.html) | Duplicate Key in Associative List (Alist) | automatic |
| [463](https://cwe.mitre.org/data/definitions/463.html) | Deletion of Data Structure Sentinel | automatic |
| [464](https://cwe.mitre.org/data/definitions/464.html) | Addition of Data Structure Sentinel | automatic |
| [466](https://cwe.mitre.org/data/definitions/466.html) | Return of Pointer Value Outside of Expected Range | automatic |
| [470](https://cwe.mitre.org/data/definitions/470.html) | Use of Externally-Controlled Input to Select Classes or Code ('Unsafe Reflection') | automatic |
| [554](https://cwe.mitre.org/data/definitions/554.html) | ASP.NET Misconfiguration: Not Using Input Validation Framework | automatic |
| [564](https://cwe.mitre.org/data/definitions/564.html) | SQL Injection: Hibernate | automatic |
| [606](https://cwe.mitre.org/data/definitions/606.html) | Unchecked Input for Loop Condition | automatic |
| [621](https://cwe.mitre.org/data/definitions/621.html) | Variable Extraction Error | automatic |
| [622](https://cwe.mitre.org/data/definitions/622.html) | Improper Validation of Function Hook Arguments | automatic |
| [624](https://cwe.mitre.org/data/definitions/624.html) | Executable Regular Expression Error | automatic |
| [626](https://cwe.mitre.org/data/definitions/626.html) | Null Byte Interaction Error (Poison Null Byte) | automatic |
| [627](https://cwe.mitre.org/data/definitions/627.html) | Dynamic Variable Evaluation | automatic |
| [641](https://cwe.mitre.org/data/definitions/641.html) | Improper Restriction of Names for Files and Other Resources | automatic |
| [643](https://cwe.mitre.org/data/definitions/643.html) | Improper Neutralization of Data within XPath Expressions ('XPath Injection') | automatic |
| [644](https://cwe.mitre.org/data/definitions/644.html) | Improper Neutralization of HTTP Headers for Scripting Syntax | automatic |
| [647](https://cwe.mitre.org/data/definitions/647.html) | Use of Non-Canonical URL Paths for Authorization Decisions | automatic |
| [652](https://cwe.mitre.org/data/definitions/652.html) | Improper Neutralization of Data within XQuery Expressions ('XQuery Injection') | automatic |
| [680](https://cwe.mitre.org/data/definitions/680.html) | Integer Overflow to Buffer Overflow | automatic |
| [694](https://cwe.mitre.org/data/definitions/694.html) | Use of Multiple Resources with Duplicate Identifier | automatic |
| [781](https://cwe.mitre.org/data/definitions/781.html) | Improper Address Validation in IOCTL with METHOD_NEITHER I/O Control Code | automatic |
| [785](https://cwe.mitre.org/data/definitions/785.html) | Use of Path Manipulation Function without Maximum-sized Buffer | automatic |
| [786](https://cwe.mitre.org/data/definitions/786.html) | Access of Memory Location Before Start of Buffer | automatic |
| [787](https://cwe.mitre.org/data/definitions/787.html) | Out-of-bounds Write | automatic |
| [788](https://cwe.mitre.org/data/definitions/788.html) | Access of Memory Location After End of Buffer | automatic |
| [790](https://cwe.mitre.org/data/definitions/790.html) | Improper Filtering of Special Elements | automatic |
| [791](https://cwe.mitre.org/data/definitions/791.html) | Incomplete Filtering of Special Elements | automatic |
| [792](https://cwe.mitre.org/data/definitions/792.html) | Incomplete Filtering of One or More Instances of Special Elements | automatic |
| [793](https://cwe.mitre.org/data/definitions/793.html) | Only Filtering One Instance of a Special Element | automatic |
| [794](https://cwe.mitre.org/data/definitions/794.html) | Incomplete Filtering of Multiple Instances of Special Elements | automatic |
| [795](https://cwe.mitre.org/data/definitions/795.html) | Only Filtering Special Elements at a Specified Location | automatic |
| [796](https://cwe.mitre.org/data/definitions/796.html) | Only Filtering Special Elements Relative to a Marker | automatic |
| [797](https://cwe.mitre.org/data/definitions/797.html) | Only Filtering Special Elements at an Absolute Position | automatic |
| [805](https://cwe.mitre.org/data/definitions/805.html) | Buffer Access with Incorrect Length Value | automatic |
| [806](https://cwe.mitre.org/data/definitions/806.html) | Buffer Access Using Size of Source Buffer | automatic |
| [822](https://cwe.mitre.org/data/definitions/822.html) | Untrusted Pointer Dereference | automatic |
| [823](https://cwe.mitre.org/data/definitions/823.html) | Use of Out-of-range Pointer Offset | automatic |
| [824](https://cwe.mitre.org/data/definitions/824.html) | Access of Uninitialized Pointer | automatic |
| [825](https://cwe.mitre.org/data/definitions/825.html) | Expired Pointer Dereference | automatic |
| [838](https://cwe.mitre.org/data/definitions/838.html) | Inappropriate Encoding for Output Context | automatic |
| [914](https://cwe.mitre.org/data/definitions/914.html) | Improper Control of Dynamically-Identified Variables | automatic |
| [917](https://cwe.mitre.org/data/definitions/917.html) | Improper Neutralization of Special Elements used in an Expression Language Statement ('Expression Language Injection') | automatic |
| [943](https://cwe.mitre.org/data/definitions/943.html) | Improper Neutralization of Special Elements in Data Query Logic | automatic |
| [1173](https://cwe.mitre.org/data/definitions/1173.html) | Improper Use of Validation Framework | automatic |
| [1174](https://cwe.mitre.org/data/definitions/1174.html) | ASP.NET Misconfiguration: Improper Model Validation | automatic |
| [1236](https://cwe.mitre.org/data/definitions/1236.html) | Improper Neutralization of Formula Elements in a CSV File | automatic |
| [1284](https://cwe.mitre.org/data/definitions/1284.html) | Improper Validation of Specified Quantity in Input | automatic |
| [1285](https://cwe.mitre.org/data/definitions/1285.html) | Improper Validation of Specified Index, Position, or Offset in Input | automatic |
| [1286](https://cwe.mitre.org/data/definitions/1286.html) | Improper Validation of Syntactic Correctness of Input | automatic |
| [1287](https://cwe.mitre.org/data/definitions/1287.html) | Improper Validation of Specified Type of Input | automatic |
| [1288](https://cwe.mitre.org/data/definitions/1288.html) | Improper Validation of Consistency within Input | automatic |
| [1289](https://cwe.mitre.org/data/definitions/1289.html) | Improper Validation of Unsafe Equivalence in Input | automatic |
| [1336](https://cwe.mitre.org/data/definitions/1336.html) | Improper Neutralization of Special Elements Used in a Template Engine | automatic |
| [1426](https://cwe.mitre.org/data/definitions/1426.html) | Improper Validation of Generative AI Output | automatic |
| [1427](https://cwe.mitre.org/data/definitions/1427.html) | Improper Neutralization of Input Used for LLM Prompting | automatic |

More: [[standard-cwe]]

### ISO 27001

| ID | Section | Link |
| --- | --- | --- |
| 5.31 | Legal, statutory, regulatory and contractual requirements | curated |

More: [[standard-iso-27001]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Abuse Case Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html) | curated |
|  | [Deserialization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [100029](https://github.com/zaproxy/community-scripts/blob/main/active/cve-2019-5418.js) | File Content Disclosure (CVE-2019-5418) | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [782-234](https://opencre.org/cre/782-234). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
