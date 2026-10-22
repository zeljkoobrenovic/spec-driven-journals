---
status: accepted
revised: 2026-10-22
---

# Spec: Who May Do What: Identity, Authorization and Entitlements

## Intent

Show how authentication, authorization, entitlements and official register authority should work across an acquired portfolio of dealer and data products, for people and for machines. The chapter separates five gates that dealer software usually merges: the tenant boundary, relationships, entitlements, register authority and licensed purpose. Each gate gets a named owner and source of truth, and the chapter then recombines them into one decision with one audit record. It argues for one identity per person and per API client (Axleby ID on Keycloak organizations), relationship-based authorization over the dealer hierarchy (Gatekeeper on OpenFGA) with attribute conditions for limits, entitlements derived from subscriptions rather than flags, register authority as typed evidence (recognition, certificate, designated agent, customer authorization), and short-lived, scoped OAuth credentials for data clients and partners. The reader should leave able to review an identity and permission design for a dealer group, a data client or a register transaction, and to say which gate failed when access goes wrong.

Owns: **entitlement**, **relationship-based authorization**, **register authority**, **API client**. Productscape bricks: `iden` (Customer Account, Identity and Entitlements: account store, identity provider, entitlement API, authority API).

## Audience

Chief architects, platform and security leads, and product directors at dealer-software vendors, vehicle-data companies and dealer groups. They know OAuth, OIDC and SAML by name. They need the dealer-specific shape: groups and rooftops, shared logins, register certificates and customer mandates, partner integrations acting for dealers, and data clients whose credentials carry commercial and license weight.

## Success criteria

- [ ] Defines the four owned terms and the five gates in a table with owner, source of truth, change trigger and an example denial; separates release flags and configuration from entitlements.
- [ ] Compares RBAC, ABAC and ReBAC with dealer examples, cites Zanzibar (2019) and OpenFGA, and shows a small relationship model that handles groups, optional regions, private leads and expiring register agents.
- [ ] Presents the architecture (Axleby ID, tenant directory, Gatekeeper, entitlement service, authority register, Charter, decision log) with a responsibility table, at least two mermaid diagrams and a consistency/latency/freshness/availability table.
- [ ] Treats register authority with documented RDW facts (recognitions, two-year certificate, customer *machtiging* via DigiD/eHerkenning), the KBA large-customer interface and UK register credentials, and records legal actor, credential, user and customer authorization per transaction.
- [ ] Compares API keys and OAuth variants for data clients, uses RFC 9700 and RFC 8693, ties the Plate Enumeration Attack and the License Breach to credential and purpose design without contradicting their owners.
- [ ] Uses dated public evidence (Cox Bridge ID and Bridge Federation, CDK Unify, Autotrader Connect capabilities, DVSA and DVLA APIs) with inferences labeled.
- [ ] Works an Axleby example with numbers (identity inventory, Velto migration, Hartley SCIM matching, Rijnstaal client) consistent with the ledger and with [[tenancy-and-dealer-groups]] and [[onboarding-and-configuration]].
- [ ] Includes failure handling (duplicates, conflicts, incomplete records, retries, partial failures, IdP, identity and authorization outages, expired authority, leaked credentials), trade-off tables, "Across Markets", the Chief Architect's view and 6–10 questions.

## Non-goals

- The tenant hierarchy, tenant context and pool/silo/bridge ([[tenancy-and-dealer-groups]]).
- Onboarding stages, configuration and extension points ([[onboarding-and-configuration]]).
- Pricing, usage events and invoices ([[billing-and-metering]]).
- The license and purpose register and misuse detection ([[data-licensing-and-governance]]).
- Register transactions themselves and their retry queue ([[registration-and-trade-services]]).
- Attack response, bot defense and the Plate Enumeration Attack as an incident ([[vehicle-platform-security]]).
- Consumer (Odolo) accounts.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Whether Cox's Bridge ID shares roles or dealer entities across products is not public; the chapter labels its reading as inference.
- Belgian register access for dealers (WebDIV, insurer-driven submission) was not verified from a primary source.
- OpenFGA may add a Zanzibar-style consistency token; the chapter's workaround (`HIGHER_CONSISTENCY` after membership changes) should be revisited if it does.
- How European dealer-software vendors model group permissions is undocumented.

## Decision log

- **2026-10-22** — Opened with a wrong-name registration under a shared login at Velto rather than with a breach, so the chapter's question is attribution and authority, which only this chapter owns; the Cross-Tenant Lead stays with [[tenancy-and-dealer-groups]].
- **2026-10-22** — Framed authorization as five gates with separate owners instead of a single policy engine, because entitlements, register authority and licensed purpose change for commercial and legal reasons on different clocks.
- **2026-10-22** — Kept permissions and entitlements out of tokens and used relationship-based authorization with attribute conditions, accepting Gatekeeper on the request path with fail-closed rules for writes, exports and register transactions.
- **2026-10-22** — Recorded the identity inventory, Velto's register-agent designation, Hartley's SCIM matching and the credential policy in the scenario ledger for later chapters.

## Sources

- **Internal**
  - [[tenancy-and-dealer-groups]] — hierarchy, memberships, tenant context, revocation target.
  - [[onboarding-and-configuration]] — Velto's onboarding evidence and Hartley's move to Axleby ID.
  - [[dms-integration]] — Hitch's dealer authorization register.
  - [[case-cox-automotive]], [[case-auto-trader-uk]] — Bridge ID and Connect capabilities.
  - `_research/brief-saas-tenancy-billing.md`, `_research/brief-identity-registers.md`, `_research/brief-case-cox-cdk.md`, `_research/scenario-ledger.md`.
- **External**
  - Zanzibar (USENIX ATC 2019); OpenFGA documentation; Keycloak 25/26 organizations announcements (2024).
  - RFC 7644 (SCIM), RFC 8693 (token exchange), RFC 9700 (OAuth security BCP, 2025), OpenID Connect Core 1.0, NIST SP 800-63B-4 (2025), OWASP API Security Top 10 (2023).
  - RDW information folder 2026 and provider pages; KBA large-customer interface brochure (2024); DVSA MOT history and DVLA VES API documentation; StVG §39; DPPA; FTC Safeguards Rule; BetrVG §87; WOR art. 27.
  - Cox Bridge ID and Bridge Federation pages; CDK Unify page; Autotrader Connect documentation.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: Velto Appraise entitlement aligned to the pooled 46 × 25 allowance, authority register marked as owned by Axleby Trade (consistency item 31d), authorized information provider linked as a book term (item 23), Lost Leads wording aligned, American spelling. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 2 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
