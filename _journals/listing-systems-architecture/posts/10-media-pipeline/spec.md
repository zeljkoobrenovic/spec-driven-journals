---
status: accepted
revised: 2026-10-20
---

# Spec: Photos Sell: Media Pipelines for Listings

## Intent

Show architects how to design one media pipeline for a listing marketplace group: three ways in (direct upload, partner feeds, back office and generated media), one sanitizing and hashing path, on-demand derivatives behind a CDN, lifecycle and retention driven by the listing's state, and perceptual hashing used as shared trust infrastructure. The reader should be able to explain where media costs and media risks come from, and plan the changes that reduce both.

## Audience

Chief and principal architects, platform and infrastructure leads, trust-and-safety engineering leads and engineering directors of marketplaces that store and serve large image archives. They know object storage, CDNs and event-driven processing; they need the listing-specific design: media identity, feed media, privacy in photos, duplicate and stolen-image detection, retention classes and the cost model.

## Success criteria

- [ ] Reader can explain why listings store media IDs and an order, never URLs, and define asset, original, master, derivative, image service, content addressing and perceptual hash.
- [ ] Reader can lay out the pipeline stages and say which block publication, which run before a listing is searchable and which run after.
- [ ] Reader can name the privacy risks in listing media (EXIF GPS, faces, plates, occupied interiors, generated images) and the controls, including AI Act Article 50 provenance.
- [ ] Reader can compare pre-generated renditions with on-demand derivatives and state the three rules that keep on-demand generation safe and affordable.
- [ ] Reader can design retention classes and storage tiering that follow the listing lifecycle, with cloud minimum durations in mind.
- [ ] Reader can describe layered duplicate detection (exact, PDQ, embeddings, human review), the allowlist, and why the same match means fraud in one context and a merge in another.
- [ ] Reader can follow Hearthly's numbers (1.8 billion images, €6.2M to €3.6M run cost) and the Barcelona lesson that a match must feed a decision able to hold the listing.
- [ ] Every company claim is dated and sourced; inferences are labeled.

## Non-goals

- Moderation policy, queues and enforcement — [[trust-and-safety-architecture]]; fraud typology — [[fraud-prevention]].
- Duplicate clustering and canonical entities — [[entity-resolution]].
- Location precision and address privacy beyond photo metadata — [[location-and-geo]].
- Publication timing budgets — [[publication-pipeline]]; model serving — [[ml-platform]]; generative listing creation — [[ai-in-listing-systems]].
- Platform-wide retention machinery — [[listing-data-management]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- OLX's duplicate-detection and triplet-loss posts and Adevinta's image-format post (reported YAMS storage above 3 PB) could not be fetched; verify in a browser before quoting specifics.
- Whether virtual staging falls under the AI Act Article 50(4) deployer disclosure duty needs legal confirmation; the chapter states only the provenance requirement.
- Whether YAMS still serves Adevinta's former marketplaces after the 2025–2026 break-up is not public.

## Decision log

- **2026-10-19** — Built the chapter around one pipeline with three entry doors, rather than separate chapters' worth of upload, feed and moderation detail, so the media contract (IDs, masters, events) is the through-line.
- **2026-10-19** — Recommended sanitized masters over keeping raw originals by default, with an explicit exception path; chose Femke's EXIF case to make the privacy point concrete.
- **2026-10-19** — Paired the cost story (Hearthly's bill) with the trust story (Barcelona) in one scene, because the same design changes (content addressing, shared hash index, check timing) address both.
- **2026-10-19** — Kept the group hash index as the first shared component and excluded Keybridge-handled media from it, to stay consistent with the March 2027 neutrality decision.

## Sources

- **Internal**
  - [[attribute-schemas]], [[entity-resolution]], [[trust-and-safety-architecture]], [[publication-pipeline]], [[location-and-geo]] — neighbouring chapters and hand-off.
  - `_research/brief-listing-data-ingestion.md` (Part 9), `brief-platform-data-ml.md` (3.2, 10.3), `brief-trust-safety-regulation.md` (3.4, 5.10), `brief-olx.md` (4.7), `brief-real-estate-portals.md` (B.2, B.3), `brief-automotive.md` (A.2, A.3), `scenario-ledger.md`.
- **External**
  - OLX Engineering, Dali (2020) and Web Locks (2026) — on-demand image processing; upload duplication.
  - Adevinta Tech Blog (2023–2025) — YAMS, OCR service, shared GPU serving, malformed-PDF lesson.
  - Rightmove RTDF v1.4.1; mobile.de Seller-API — feed media contracts and images as valuation input.
  - Meta PDQ documentation and 2019 release; imgproxy; thumbor; ClamAV; ExifTool.
  - Google Cloud Storage and Amazon S3 storage-class documentation; caniuse AVIF/WebP; Google Merchant image minimum.
  - EU AI Act Article 50; Autotrader FY26 results; CoStar and Zillow FY2025 10-Ks; Zillow ZInD; Google NIMA.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: AI Act Article 50 date hedged against later amendments, scene wording tightened, reading time corrected; Autotrader FY26 Co-Driver figures and the Google Merchant 500 × 500 image minimum re-verified. *(AI-mediated session)*
- **2026-10-19** — Added 3 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 2 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
