{id: media-pipeline}
# 10. Photos Sell: Media Pipelines for Listings

![Photos Sell: Media Pipelines for Listings — logo](listing-systems-architecture/posts/10-media-pipeline/assets/images/10-media-pipeline/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Follow a listing photo from a phone, a browser or a partner's server through validation, sanitization, hashing, classification, derivative generation, delivery and deletion. You will see where media costs come from, how perceptual hashing catches stolen photos, and how Veldmark plans to cut Hearthly's media bill while closing the gap that let a fake-rental ring operate for days.

> **WHY THE BUSINESS CARES:** Photos are the first thing a buyer judges and the main thing a fraudster steals. Listings with good photos get more contacts, galleries are most of a marketplace's delivered bytes, and stored images become one of the larger lines on the infrastructure bill, growing faster than live listings.

> **WHY ARCHITECTS SHOULD CARE:** The media pipeline touches security (malicious files), privacy (location in photo metadata, faces, number plates), trust (stolen and duplicate photos), search quality (cover photos, quality scores), feeds (media pulled by URL) and cost (storage tiers and CDN delivery). Decisions made for one of these, such as storing every rendition forever, quietly set the cost and risk of all the others.

> **KEY POINTS:**
>
> * **A listing references media IDs, not URLs, and media has its own lifecycle.** Give every asset a content-derived identity, a sanitized master, a moderation state and a retention class. Then CDN changes, format changes and deletions are media-service operations, not listing migrations.
> * **Generate derivatives on demand at the edge; store originals deliberately.** Pre-generating every size and format multiplies storage and freezes yesterday's formats. An image service behind a CDN produces AVIF, WebP or JPEG at the size each device needs, while lifecycle rules move originals of ended listings to colder storage and delete them when their retention ends.
> * **Hashes are trust infrastructure, not housekeeping.** Exact hashes remove duplicate uploads; perceptual hashes and embeddings find stolen photos across sellers, listings and brands. A match that cannot hold a listing, carries no seller context or covers only one brand lets fraud run for days.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Seeing Double** — Re-pulled feed images, reposted listings and multi-agency listings fill storage and search with copies that only hashing can recognize.
> * **Moderation as an Afterthought** — Image matches that only create queue items while the listing goes live let stolen photos, contact details and prohibited content reach buyers first.
> * **Ghost Inventory** — Photos of removed or sold listings stay reachable on the CDN and in caches long after the listing is gone, which is also a privacy problem.

Listing marketplaces are, measured in bytes, image businesses. A text listing is a few kilobytes; its photos are several megabytes, multiplied by every derivative size, every format and every year the platform keeps them. Buyers scroll galleries before they read descriptions, and professional sellers judge a portal partly by how well it presents their photography. **Media is the largest body of listing data, and usually the least governed.**

The media pipeline is the set of systems that accepts photos, videos, floor plans and documents, makes them safe, understands them, stores them and serves them. In most marketplaces it grew in stages: an upload endpoint, a resizing job, a CDN in front, then classifiers and duplicate detection bolted on as fraud and quality problems appeared. Each stage was reasonable. Together they often produce a system that stores far more than it needs, serves formats a decade old, and checks for stolen photos too late to stop the fraud that uses them.

Part II models the listing as a small aggregate that references governed subdomains by ID, and media is the largest of them. This chapter designs its pipeline as one system with one contract: media IDs, sanitized masters and a `MediaReady` event that feeds, trust and safety, ranking and image models all depend on. It builds on the listing aggregate in [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate) and the attribute contract in [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas), hands moderation policy to [Trust and Safety as a Platform](#trust-and-safety-architecture) and duplicate clustering to [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution), and follows Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)), through Hearthly's media bill and the fake-rental ring that its image checks caught too late.

{id: media-pipeline--setting-the-scene-at-veldmark-1-8-billion-images-and-a-fake-rental-ring}
## Setting the Scene at Veldmark: 1.8 Billion Images and a Fake-Rental Ring

It is September 2027. Julien Marchand, Hearthly's CTO, brings two documents to Ingrid Halvorsen, the Group Chief Architect.

The first is the media bill. Veldmark stores about **6.4 billion images** across its brands and adds about **9.5 million a day**. Hearthly, with 2.6 million live listings, stores **1.8 billion** of them, on Google Cloud Storage behind Cloud CDN. Hearthly's media run cost in 2026 was about **€6.2 million**: about €2.6 million for storage, €2.8 million for CDN delivery and cache fill, and €0.8 million for processing and fetching images from partner feeds. The storage line grew 19% in 2026 while Hearthly's live listings grew 4%.

Three causes are visible in the numbers. First, about 84% of Hearthly's listings arrive through feeds from about 160 real-estate software vendors, and many connectors re-send every photo URL on every update without a change marker; Hearthly re-downloads the photos and stores each as a new object. A sample showed that about **38%** of stored originals are byte-for-byte copies of another stored image. Second, the French platform pre-generates **nine JPEG renditions** of every image at upload and keeps them as long as the original. Third, nothing is ever deleted: about **96%** of stored images belong to listings that are no longer live.

![An iceberg whose small visible tip holds live listing photos, while a huge submerged mass holds copies and repeated renditions of old photos.](listing-systems-architecture/posts/10-media-pipeline/assets/images/10-media-pipeline/media-iceberg.jpeg)

**Figure 1:** *About 96% of Hearthly's 1.8 billion stored images belong to listings that are no longer live, and about 38% of originals are byte-for-byte copies of another stored image.*

The second document is the review of the **Barcelona fake-rental ring**. In **July 2027**, **26** accounts posted **180** fake rental listings in Eixample on Hearthly.es, using photos stolen from real listings, priced about **35%** below market, and asking for deposits by bank transfer outside the platform. Perceptual-hash matches against existing listings, combined with price anomalies, exposed the ring, but only after **63** people had reported losses totaling about **€71,000**. The media part of the review is uncomfortable because detection worked: Hearthly Spain's hash index matched the first stolen photos within minutes of upload. The match did not hold the listing; it created a "possible duplicate" item in a general moderation queue while the listing went live. The hash service returned a distance and nothing else, so reviewers could not tell a stolen photo from a second agency marketing the same flat. And the index held only Hearthly.es images, so photos copied from other portals or from Veldmark's other brands were never compared. [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention) tells the decision side of the story.

Ingrid's question to the architecture advice forum is the chapter's question: **what does one media pipeline for the group look like, such that it stores less, serves faster, protects sellers' privacy and catches stolen photos before buyers see them?**

{id: media-pipeline--concepts-assets-masters-derivatives-and-hashes}
## Concepts: Assets, Masters, Derivatives and Hashes

Several costly mistakes in media systems come from treating different things as one.

- A **media asset** is one piece of listing media: a photo, a video, a floor plan, a 3D tour reference or a document such as an energy certificate or a CV. It has an identity, an owner, a type, a moderation state, rights metadata and a retention class, independent of any URL.
- The **original** is the file as received. The **master** is the sanitized version the platform keeps: re-encoded, orientation applied, metadata stripped. I recommend storing the master and, in most cases, not keeping the original at all.
- A **derivative** (or rendition) is a version of the master at a given size, crop, format and quality, possibly with a watermark. Derivatives are disposable: they can always be regenerated from the master.
- An **image service** generates derivatives on request from a URL that encodes the transformation, typically behind a CDN that caches the results. The open-source imgproxy and thumbor are common examples; imgproxy is built on libvips and uses signed URLs to prevent abuse ([imgproxy](https://github.com/imgproxy/imgproxy), n.d.; [thumbor](https://github.com/thumbor/thumbor), n.d.).
- **Content addressing** derives an asset's storage key from a cryptographic hash of its bytes, such as SHA-256. Identical uploads collapse to one stored object, and a derivative URL built from the hash never changes, so it can be cached indefinitely.
- A **perceptual hash** is a short fingerprint computed from an image's visual content, so that re-compressed, resized or lightly edited copies produce similar fingerprints. Two images are compared by the Hamming distance between their hashes: the number of differing bits. Meta's PDQ, open-sourced in 2019, is the most widely used public algorithm for this ([Meta, open-source photo and video matching](https://about.fb.com/news/2019/08/open-source-photo-video-matching/), 2019).
- The **media pipeline** is the end-to-end system: upload or fetch, validation, sanitization, hashing, classification and moderation, master storage, derivative delivery, lifecycle and deletion.

**A listing stores media IDs and an order, never URLs.** This is the most important design rule. If listings hold URLs, every CDN change, domain change, format change or watermark change becomes a migration of millions of listing records, and deleting a photo means finding every place a URL was copied. If listings hold IDs, those are media-service operations. The same rule appears in reference designs and in public partner APIs: mobile.de's Seller-API has clients pre-upload images, receive references, and then reference those in the ad ([mobile.de Seller-API](https://services.mobile.de/manual/seller-api.html), n.d.).

{id: media-pipeline--architecture-the-upload-to-edge-pipeline}
## Architecture: The Upload-to-Edge Pipeline

Media arrives through three doors, and the pipeline behind them should be one.

**Mobile and web uploads** from private sellers and professionals. In the common pattern, the client asks the media service for a short-lived, pre-signed upload URL to object storage, uploads directly, and receives a media ID. The upload completes asynchronously, and the media service processes the file when storage reports it. This keeps large files away from application servers and lets uploads resume on poor mobile connections. Resumable uploads have their own traps: OLX described in 2026 how users with several browser tabs open each tried to resume the same large upload, duplicating objects in storage, and how it used the Web Locks API so that only one tab proceeds ([OLX Engineering, Web Locks API](https://tech.olx.com/handling-concurrency-on-the-web-with-web-locks-api-163b7e07eddd), 2026). Server-side content addressing is the backstop: a duplicate upload costs bandwidth, not storage.

**Partner feeds** from dealer management systems and real-estate software. Some standards bundle media with the data; OpenImmo's XML exchange typically ships images zipped with the XML file over FTP ([OpenImmo](https://www.openimmo.de/), n.d.). Others have the portal pull media by URL. Rightmove's Real Time Datafeed accepts up to 999 media items per property and 20 MB per image, deletes an image when its URL is removed from an update, and, when the sender supplies a media update date, "will not re-retrieve images on the same URLs if they have the same media update date", which the specification says "relieves pressure on the client's image servers" ([Rightmove Real Time Datafeed specification v1.4.1](https://media.rightmove.co.uk/ps/pdf/guides/adf/Rightmove_Real_Time_Datafeed_Specification.pdf), 2023). That one field is the difference between a feed that fetches changed images and one that fetches everything every time. Hearthly's re-download problem is the cost of not requiring it, or of not using HTTP conditional requests and content hashes when the sender does not provide it.

**Back-office and generated media**: moderator edits, virtual staging, AI-generated listing videos, floor plans redrawn by a vendor. These enter through the same API with their provenance recorded.

![Diagram: One pipeline behind three doors](listing-systems-architecture/posts/10-media-pipeline/assets/images/10-media-pipeline/fig02-one-pipeline-behind-three-doors-files.jpeg)

**Figure 2:** *One pipeline behind three doors. Files land in quarantine, are gated, re-encoded and hashed before anything else sees them, and reach buyers only as derivatives generated by the image service from a sanitized master. The hash index and classifiers feed the trust decision that the publication pipeline waits for.*

The stages, and the evidence behind each:

| Stage | What happens | Blocks publication? | Notes and evidence |
| --- | --- | --- | --- |
| 1. Quarantine | File lands in a bucket nothing else reads | — | Nothing downstream touches unvalidated bytes |
| 2. Gate | Check type by content (magic bytes), size, and dimensions *before* full decoding | Yes | imgproxy checks image type before downloading fully and real dimensions before decoding, to guard against "image bombs" |
| 3. Sanitize | Decode, apply orientation, re-encode to a master format; strip EXIF, XMP and trailing bytes | Yes | Re-encoding discards payloads hidden in metadata or after the image data |
| 4. Malware scan | For documents (PDF floor plans, energy certificates, CVs) | Yes, for documents | ClamAV describes itself as "not a traditional anti-virus or endpoint security suite"; use it as one layer |
| 5. Hash | SHA-256 for exact duplicates; PDQ for near-duplicates | Exact: no; perceptual: by policy | Exact match links to the existing master |
| 6. Classify | Quality, OCR, prohibited content, category hints, room type or vehicle angle | By policy | Feeds moderation, ranking and gallery order |
| 7. Decide | Trust rules combine hash matches, classifier output and listing context | Yes, for blocking outcomes | Owned by [Trust and Safety as a Platform](#trust-and-safety-architecture) |
| 8. Deliver | Image service generates derivatives; CDN caches them | — | Immutable, content-addressed URLs |
| 9. Delete | Purge derivatives from CDN, delete master by retention class, keep hashes by policy | — | Retention classes below |

Two public lessons shape the gate and the document path. First, in a 2025 post, Adevinta's InfoJobs team described its shared media service, YAMS, returning HTTP 500 errors for PDFs produced by a regional public employment service; each failing file was two complete PDFs joined together, with a duplicate header and stale cross-reference offsets, and the failures had been classified as internal faults instead of file-format errors ([Adevinta Tech Blog, "Engineers to the rescue"](https://medium.com/adevinta-tech-blog/engineers-to-the-rescue-when-your-public-employment-service-makes-it-impossible-to-apply-for-jobs-b2ad6f5c29e6), 2025). The general rule: **a malformed file is a client error with an actionable message**, and where the source is a third party the seller cannot control, the pipeline should offer repair. Second, in jobs and real estate the document path carries personal data. CVs, energy certificates and battery-health certificates for electric cars, which mobile.de accepts as PDF, JPEG or PNG up to 10 MB, are media assets with personal data and their own retention rules ([mobile.de Seller-API](https://services.mobile.de/manual/seller-api.html), n.d.).

{id: media-pipeline--what-blocks-publication-and-what-does-not}
### What blocks publication, and what does not

Which checks block publication is a product decision. If every check is synchronous, a seller with twenty photos waits; if every check is asynchronous, stolen photos go live. The split I use:

- **Synchronous with the upload** (seconds): gate, sanitize, exact hash, a fast perceptual-hash lookup against the hash index, and a fast prohibited-content classifier. These are cheap and decisive.
- **Before the listing becomes searchable** (within the publication budget): the full trust decision for listings in high-risk segments (rentals, high-value vehicles, new accounts), combining hash matches with price anomalies and account signals. [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline) owns the budget; Veldmark's target for Tradeyard is 90 seconds at p95.
- **After publication** (minutes to hours): quality scoring, room and angle classification, gallery reordering suggestions, embedding-based similarity for heavily edited copies, and re-scoring when other listings arrive.

The Barcelona ring sat in the second row's gap: the comparison ran within minutes, but its result was a queue item, not an input to a decision that could hold the listing.

{id: media-pipeline--privacy-what-photos-reveal}
## Privacy: What Photos Reveal

A listing photo carries more personal data than its seller realizes, and the platform is the one accountable for publishing it.

**Metadata.** EXIF GPS tags can record latitude, longitude, altitude, timestamp and the direction the camera faced ([ExifTool GPS tags](https://exiftool.org/TagNames/GPS.html), n.d.). A private seller who photographs a bike in their hallway publishes their home's coordinates unless the pipeline strips them. When Femke listed her **€240** city bike on Tradeyard NL on **Sunday 7 March 2027**, her phone embedded the coordinates of her Rotterdam home in all six photos. Tradeyard strips EXIF before generating derivatives, so buyers never saw them, but its image service kept the unmodified originals, with GPS intact, for the lifetime of the account. One misconfigured bucket would expose them. Stripping must happen before the master is written, and the raw original should not be kept unless a documented purpose requires it, with restricted access and a short retention. Location privacy for the listing itself, the approximate pin, is [Where Is It? Location, Geocoding and Privacy](#location-and-geo)'s subject; the photo is a second path to the same data.

![A bike photo with a hidden map pin to the seller's home passes through a sanitizer that removes the location before the clean master is stored.](listing-systems-architecture/posts/10-media-pipeline/assets/images/10-media-pipeline/photo-carries-home-location.jpeg)

**Figure 3:** *A phone photo can carry the seller's home coordinates, so metadata must be stripped before the master is written, and the raw original should not be kept.*

**Content.** Photos show faces (sellers, tenants, children), number plates, documents on desks, family photos on walls and the layout of an occupied home. A common practice is to detect and blur number plates and faces in vehicle and property photos, at least for private sellers, and to flag interiors of occupied rentals for tenant consent. The detection is a classifier; the policy, including when blurring is mandatory, belongs to the data protection lead.

**Generated and edited images.** Virtual staging, sky replacement and AI-generated listing videos bring marking and disclosure duties. Article 50 of the EU AI Act, which applies from **2 August 2026** under the regulation as adopted in 2024 (check for later amendments to its timeline), requires providers of systems that generate synthetic images to mark outputs in a machine-readable way, and deployers of systems that generate or manipulate images resembling existing places or objects in a way that could falsely appear authentic to disclose it ([EU AI Act, Article 50](https://artificialintelligenceact.eu/article/50/), 2024). Whether a virtually staged room falls under the deployer duty is a question for counsel; the architectural consequence holds either way. **Provenance is a media attribute**: the pipeline must record whether an image is a photograph, an edited photograph or generated, and the listing must be able to display that.

**Deletion.** When a listing is removed for fraud, sold or deleted by the seller, its derivatives must stop being served. That means purging CDN caches, not only deleting the master: a content-addressed URL cached for a year at the edge outlives a deleted object for exactly that year. This is the media form of **Ghost Inventory**, and it is also a privacy failure when the seller exercised a right to erasure. Retention of hashes after deletion is a separate decision, covered below.

{id: media-pipeline--derivatives-formats-and-the-cdn}
## Derivatives, Formats and the CDN

Whether to store renditions or generate them decides a large part of the media bill.

**Pre-generated renditions** are computed at upload in a fixed set of sizes and formats and stored beside the master. They are simple to serve and need no compute at request time. Their costs grow with every image ever stored, they lock in the formats chosen at the time, and adding a new size or format means reprocessing the entire archive.

**On-demand derivatives** are generated by an image service when first requested and then cached by the CDN. OLX described this design in 2020: a CDN in front serving "around 80%" of traffic from cache, with the remaining requests, "millions of requests a day" and about 30,000 per second at peak on the busiest cluster, reaching an on-demand image processor that resizes, rotates, watermarks, re-encodes and compresses. OLX replaced a thumbor-based processor, which needed "~6000 pods" at peak, with **Dali**, a Rust service that first used OpenCV and then libvips, and that handled about twice thumbor's load per instance ([OLX Engineering, "Presenting Dali"](https://tech.olx.com/presenting-dali-an-image-processor-service-514e6be00de8), 2020). The post is from 2020, and OLX's current system is not public. The design is still the reference pattern.

Modern formats make on-demand generation more valuable. As of October 2026, AVIF is supported by about 96% of browsers in use globally and WebP by about 97% ([Can I use: AVIF](https://caniuse.com/avif); [Can I use: WebP](https://caniuse.com/webp), accessed 2026-10-19). An image service can choose the format per request, from the browser's `Accept` header or through `<picture>` sources, with JPEG as the fallback. A platform that pre-generated JPEGs in 2018 serves those JPEGs until it reprocesses its archive.

![Left, shelves of nine stored renditions per photo fill a warehouse; right, one master feeds an image service and cache that create sizes on request.](listing-systems-architecture/posts/10-media-pipeline/assets/images/10-media-pipeline/renditions-vs-on-demand.jpeg)

**Figure 4:** *Pre-generated renditions grow with every image ever stored and lock in old formats; one master plus on-demand derivatives behind a CDN serves modern formats without storing them.*

Three rules keep on-demand generation affordable and safe.

1. **Bound the variant space.** Allow a fixed set of widths, crops, qualities and formats, not arbitrary parameters. Every distinct URL is a cache entry and a potential cache miss; unbounded parameters are both a cost problem and a denial-of-service vector.
2. **Sign transformation URLs.** Only the platform can mint a derivative URL, so outsiders cannot ask the image service to render arbitrary sizes. imgproxy's signed URLs are the public example.
3. **Make URLs immutable.** A derivative URL built from the master's content hash and the transformation never changes meaning, so it can carry a long cache lifetime. Changing an image means a new hash and a new URL, not a cache purge. Deletion is the exception and needs an explicit purge.

Outbound channels set floors on derivatives. Google Merchant Center will enforce a minimum of 500 × 500 pixels for product images from **31 January 2027** ([Google Merchant Center product data specification](https://support.google.com/merchants/answer/7052112), n.d.). Any marketplace that syndicates listings to shopping channels needs to know, per listing, whether it has an image that meets the floor; that is a derived media attribute, and its absence is a feed error, not a surprise.

{id: media-pipeline--storage-tiers-and-the-media-lifecycle}
## Storage Tiers and the Media Lifecycle

Most stored listing images are never viewed again after their listing ends. Cloud object stores price that pattern explicitly. Google Cloud Storage offers Standard, Nearline, Coldline and Archive classes with minimum storage durations of none, 30, 90 and 365 days, retrieval fees for the colder classes, and an Autoclass option that manages transitions automatically ([Google Cloud Storage classes](https://docs.cloud.google.com/storage/docs/storage-classes), updated 2026-10-13). Amazon S3's Standard-IA has a 30-day minimum and Glacier Instant Retrieval a 90-day minimum, both with millisecond access and per-GB retrieval charges; S3 Intelligent-Tiering moves objects not accessed for 30 consecutive days to an infrequent-access tier and after 90 days to an archive instant-access tier ([Amazon S3 storage classes](https://aws.amazon.com/s3/storage-classes/), n.d.).

The minimum durations matter for media more than for most data. An image deleted from Archive after two months is billed for twelve. The lifecycle policy must therefore follow the **listing's** lifecycle, which only the platform knows, rather than access patterns alone.

![Diagram: A media asset's lifecycle follows its listing](listing-systems-architecture/posts/10-media-pipeline/assets/images/10-media-pipeline/fig05-media-asset-s-lifecycle-follows-listing.jpeg)

**Figure 5:** *A media asset's lifecycle follows its listing. Dormant media stays in warm storage for relisting and disputes; archived media moves to a cold class; deletion purges derivatives from the CDN and removes the master, while hashes may be kept under their own documented retention.*

Retention classes make the lifecycle explicit and defensible. A workable set:

| Class | Applies to | Master retention after the listing ends | Hash retention | Rationale |
| --- | --- | --- | --- | --- |
| Standard listing media | Photos of ordinary listings | 12–24 months, warm then cold | Longer, documented | Relisting, disputes, fraud investigations |
| Removed for fraud | Media of listings removed by trust and safety | For the appeal window and investigations | Kept on block lists | Evidence; future matching |
| Erasure requested | Media covered by a deletion request | Delete promptly, purge CDN | Only if a separate legal basis applies | Data-protection rights |
| Documents | CVs, certificates, identity-bearing files | Shortest workable period | Usually none | High personal-data content |
| Professional archives | Agency or dealer media under contract | As the contract specifies | As policy | Contractual rights |

The hash-retention column is where privacy and fraud prevention meet. A perceptual hash of a removed scam listing's photos is valuable for years, because the same stolen photos return. A hash is still derived from personal data in some cases, so its retention needs a documented purpose and legal basis; fraud prevention is the usual one. [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation) covers the legal framework and [System of Record and Read Models: Listing Data Management](#listing-data-management) the platform-wide retention machinery.

{id: media-pipeline--perceptual-hashing-finding-the-same-photo-twice}
## Perceptual Hashing: Finding the Same Photo Twice

Duplicate and stolen photos are two problems with opposite policies, and the hashing layer must serve both.

- **The same seller reusing photos** (reposting a listing, or a dealer listing two similar cars with the same studio shots) is a spam or ranking-abuse problem at worst, and often legitimate.
- **Different sellers using the same photos** is a strong fraud signal in rentals and high-value goods, where scammers copy real listings, and a normal event in real-estate sales, where several agencies market the same property, sometimes with the same photographer's pictures.

The layered design that public evidence supports has four levels.

1. **Exact match** by SHA-256. Free, certain, defeated by any re-encoding.
2. **Perceptual hash** by PDQ or similar. PDQ's documentation recommends discarding hashes with a quality score of 49 or less, because flat or featureless images produce unreliable hashes, and starting with a match threshold of Hamming distance 31 or less, tuned on one's own data; the algorithm can produce additional hashes for rotations and flips, but "does not guarantee exact rotational invariance" ([PDQ documentation, ThreatExchange repository](https://github.com/facebook/ThreatExchange/tree/main/pdq), n.d.). Perceptual hashes survive re-compression and resizing and are weaker against crops, overlays and mirroring.
3. **Embedding similarity** from an image model, with approximate nearest-neighbor search, for copies that have been cropped, watermarked, color-shifted or deliberately perturbed. OLX has published work on detecting image duplicates with perceptual hashes on Elasticsearch, and on a triplet-loss network trained to catch fraudsters who augment images to evade hashing; those posts could not be accessed directly for this book and are known through search summaries (OLX Engineering, n.d.).
4. **Human review** for the gray zone between thresholds.

![Diagram: Layered duplicate detection](listing-systems-architecture/posts/10-media-pipeline/assets/images/10-media-pipeline/fig06-layered-duplicate-detection-cheap-checks-run.jpeg)

**Figure 6:** *Layered duplicate detection. Cheap checks run first; the same match leads to different actions depending on who the sellers are and which segment the listing is in. A copied photo is a fraud signal for a new account's rental and a clustering feature for three agencies selling the same flat.*

The allowlist in Figure 6 is not optional. Manufacturer press images in new-car listings, developer renderings in new-build real estate and catalog photos in recommerce legitimately appear on thousands of listings. Without an allowlist, the detector floods moderators and is switched off.

The hash index is also the clearest case for **sharing across brands**. A photo stolen from a Hearthly France listing and reused on Hearthly.es, or a car photo moved from Motorvane to Tradeyard Poland's car section, is invisible to a per-brand index. The index is small (a PDQ hash is a few dozen bytes) and the matching service is generic, while the decisions stay with each brand's trust rules. The Lyon apartment shows the other side: when **three agencies** listed the same 68 m² flat in **May 2027**, two of them used the same set of photographer's images, and the perceptual-hash matches were among the strongest signals [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution) used to cluster the listings into one canonical property. The same signal that blocks a scam supports a legitimate merge, which is why the hashing service reports matches and leaves the decision to the consumer.

{id: media-pipeline--understanding-images-quality-order-text-and-content}
## Understanding Images: Quality, Order, Text and Content

Beyond safety, image models score quality, order galleries, read text in photos and fill attributes, and each changes how a listing performs.

**Quality scoring** predicts whether a photo is sharp, well exposed and appealing. Google's NIMA model, published in 2017, predicts a distribution of human ratings for technical and aesthetic quality and is the standard public reference for such scores ([Google Research, "Introducing NIMA"](https://research.google/blog/introducing-nima-neural-image-assessment/), 2017). OLX described in 2020 seller recommendations based on photo count, blur and darkness ([OLX, "Data Science at OLX"](https://tech.olx.com/data-science-at-olx-7c7406d1713f), 2020). Quality scores feed ranking features, seller nudges and cover-photo selection; [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) decides how much weight they deserve.

**Ordering and cover selection** decide what a buyer sees first. Autotrader UK reported in its FY2026 results that its Co-Driver tools, which generate descriptions and tag, order and optimize images, had made 700,000 "smart image re-orders" and generated 1.9 million descriptions ([Autotrader Group FY26 results](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf), 2026). In automotive the classifier labels angles (front three-quarter, interior, dashboard with odometer); in real estate it labels rooms (living room, kitchen, façade, floor plan). Ordering is a suggestion to professional sellers, who often care about their gallery, and a default for private sellers.

**Text in images** is both a moderation signal and a search signal. Adevinta's 2023 engineering post on its OCR service described detecting insults, hidden messages, URLs, e-mail addresses and phone numbers in ad images, with volume growing from more than 100 million to 330 million requests a month, accuracy on an internal benchmark rising from 0.4 to 0.8 after a move to PaddleOCR models, and a cost about twelve times lower than an external OCR API ([Adevinta Tech Blog, "Text in Image 2.0"](https://adevinta.com/techblog/text-in-image-2-0-improving-ocr-service-with-paddleocr/), 2023). Phone numbers written on a photo are the classic way to route buyers off-platform, the first step of many scams described in [From Interest to Contact: Messaging and Lead Management](#messaging-and-leads).

**Content and attribute signals.** Classifiers detect prohibited items, nudity and weapons, predict categories and fill attributes. Adevinta described in 2023 a shared team running a text detector, a car classifier, a background remover and an image classifier for its marketplaces on shared GPU serving ([Adevinta Tech Blog, GPU serving](https://adevinta.com/techblog/how-we-joined-forces-to-enable-gpu-serving-for-our-ai-solutions/), 2023). mobile.de's documentation shows images feeding valuation itself: its price rating is recalculated "including the image data" when images arrive after the ad, and mobile.de recommends uploading images first ([mobile.de Seller-API](https://services.mobile.de/manual/seller-api.html), n.d.). So a `MediaReady` event must reach the models that depend on images, and listing-level outputs must be recomputed when it does. [Models in Production: ML Platforms and Use Cases](#ml-platform) owns the serving infrastructure.

{id: media-pipeline--video-3d-tours-and-floor-plans}
## Video, 3D Tours and Floor Plans

Richer media shows up mostly in real estate and automotive in the public record, and it behaves differently from photos.

- **Video** needs transcoding to adaptive streaming formats (HLS or DASH), poster frames, frame and audio moderation, and much more storage and egress per asset. Meta's catalog format accepts up to 20 video URLs per item ([Meta catalog product fields](https://developers.facebook.com/docs/marketing-api/catalog/reference), n.d.). An OLX news item from February 2026 describes AI-powered listing videos; its content was not accessible for this book.
- **3D tours and panoramas** are usually produced and hosted by specialist providers and embedded. CoStar's FY2025 annual report records the completion of its acquisition of Matterport, a 3D-capture company, on 28 February 2025 ([CoStar Group FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1057352/000105735226000020/csgp-20251231.htm), 2026), and Zillow's FY2025 annual report describes its Showcase tier with interactive floor plans and 3D touring ([Zillow Group FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1617640/000161764026000015/z-20251231.htm), 2026). mobile.de's Seller-API lists interior and exterior "Auto Panorama" images among its resources. For most marketplaces, a tour is an external media object with its own lifecycle, consent and moderation, referenced by the listing like any other asset.
- **Floor plans** are images that carry data. Zillow's ZInD dataset, presented in 2021, contains 67,448 panoramas and 2,737 floor plans of 1,575 homes for academic use ([Zillow ZInD](https://github.com/zillow/zind), n.d.); it is evidence of research investment, not a description of Zillow's production pipeline. A floor plan can yield room counts and surface areas, which become attribute values with model provenance, checked against the seller's stated living area under the rules in [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas).

The architectural rule for all three: **one media model, several processing profiles.** A video is a media asset with a transcoding profile, a tour is an asset of type "external embed" with a provider and a consent record, and a floor plan is an image with an extraction profile. A separate system for each type multiplies deletion, moderation and privacy work.

{id: media-pipeline--in-practice-public-examples-and-veldmark-s-plan}
## In Practice: Public Examples and Veldmark's Plan

Public evidence on listing media pipelines is uneven but consistent. **Adevinta** runs a shared media service, YAMS ("Your Adevinta Media Service"), which a 2024 engineering post described as a service that "all of the marketplaces in Adevinta rely on" to deliver "more than 800 million images, documents and videos daily" ([Adevinta Tech Blog, logging at scale](https://adevinta.com/techblog/the-300-bytes-that-saved-millions-optimising-logging-at-scale/), 2024); a further post, not accessible for this book and known through a search summary, reportedly put its storage at more than 3 petabytes, with on-the-fly resizing, cropping, watermarking and format conversion. Given the break-up of Adevinta's portfolio from 2025, whether YAMS still serves all of its former marketplaces is not public. **OLX** documented the CDN-plus-on-demand-processor pattern and its scale in 2020. **Rightmove** documented a pull-by-URL feed contract with change detection. **mobile.de** documented pre-uploaded image references, per-seller image limits and images as valuation inputs. Together they describe the same architecture: IDs not URLs, sanitized masters, on-demand derivatives, change-aware feed fetching and models downstream of a media-ready event.

> **INFERENCE, NOT DOCUMENTED:** None of these companies has published its full storage tiering or retention policy for listing images. The lifecycle and retention classes in this chapter are a reference design, not a description of any of their systems.

{id: media-pipeline--veldmark-hearthly-s-media-plan-in-numbers}
### Veldmark: Hearthly's media plan in numbers

Veldmark's forum approved a group media decision in **November 2027**, and Hearthly is its first large adopter. All figures are fictional.

**One contract, staged infrastructure.** The group media platform defines one media API (upload, fetch-by-URL, attach, order, delete), one asset model with retention classes, one derivative URL scheme and one `MediaReady` event on the group event backbone. The platform runs on AWS, the group's primary cloud. Hearthly stays on Google Cloud through 2028 under the ledger's cloud decisions, so it runs the same media service code against Google Cloud Storage, and its storage moves only when Hearthly's broader platform does. The **group perceptual-hash index** is the first shared component, live for all brands in **Q1 2028**, because it needs no storage migration at all: brands send hashes, not images.

**Hearthly's four changes.**

1. **Content addressing and change-aware fetching.** Originals become masters keyed by SHA-256, and feed fetchers send conditional requests and compare hashes before storing anything. Connectors that support a media change date, as Rightmove's contract does, must send it from the 2028 feed contract version onward. The 38% of byte-identical copies, about **680 million** objects, are collapsed into references.
2. **No stored renditions.** The nine pre-generated JPEG renditions are replaced by an image service behind Cloud CDN, serving AVIF or WebP with JPEG fallback in six bounded widths. In a September 2027 test on Hearthly France, bytes delivered per gallery view fell by about **38%** at equal visual quality, which is what moves the CDN line.
3. **Lifecycle by listing state.** Masters of listings ended more than 90 days ago move to Coldline; after 24 months they move to Archive and are deleted when their retention class ends. Twenty-four months reflects how often the same property is relisted by the same agency in France. Masters of fraud removals and documents follow their own classes.
4. **Hash check before searchable, for rentals.** On Hearthly.es and Hearthly France, rental listings with a PDQ match to a different seller's image, or to a hash on the fraud block list, are held for the trust decision within the publication budget instead of producing a queue item while the listing goes live. Each match now carries the relationship between the two sellers (same account, same agency group, known co-listing agency or unrelated), which is what reviewers lacked in July. The index covers all of Veldmark's brands from Q1 2028.

The cost effect, as planned for the end of 2028:

| Line | 2026 actual | End-2028 plan | Main driver |
| --- | --- | --- | --- |
| Stored data | about 5.4 PB | about 2.3 PB | Dedup, no stored renditions, deletion by retention class |
| Storage cost | €2.6M | €1.1M | Less data; most of the rest in Coldline and Archive |
| CDN delivery and cache fill | €2.8M | €1.9M | Modern formats, bounded sizes, higher cache hit ratio |
| Processing and feed fetching | €0.8M | €0.6M | Fewer re-downloads; on-demand compute partly offsets |
| **Total media run cost** | **€6.2M** | **€3.6M** | About **€2.6M a year** toward Common Ground's €38M run-cost target |

The processing line falls least, because on-demand derivative generation costs compute that pre-generation did not. That is the honest trade: Hearthly pays a little more compute per request to stop paying storage for nine renditions of 1.8 billion images forever.

The plan also closes Tradeyard's privacy finding: from the November 2027 decision, no brand stores raw originals with metadata. Tradeyard's existing originals are being rewritten as sanitized masters, a backfill over about 2.9 billion images that runs into 2028.

{id: media-pipeline--trade-offs}
## Trade-offs

| Decision | Option A | Option B | Choose A when | Choose B when |
| --- | --- | --- | --- | --- |
| Derivatives | Pre-generated and stored | Generated on demand, cached at the CDN | Very small catalogs; no compute available at the edge | Large archives; formats and sizes still evolving (almost always) |
| Original files | Keep raw originals | Keep only sanitized masters | A documented need (legal evidence, professional photography contracts), with restricted access | Default; removes metadata risk |
| Feed media | Pull by URL | Push with the data (ZIP, multipart upload) | Senders host images reliably and supply change markers | Senders cannot host images; batch exchange is the norm (OpenImmo-style) |
| Perceptual check timing | Before searchable | After publication | High-risk segments (rentals, new accounts, high-value goods) | Low-risk segments where publication speed matters more |
| Hash index scope | Group-wide | Per brand | Brands share fraud patterns or supply (almost always within a group) | Legal separation is required, as for a neutral SaaS such as Keybridge |
| Media service ownership | One group platform | One per brand | Shared cloud and team capacity; similar media types | Brands on different clouds with no near-term convergence (then share the contract first) |
| Rich media | Host and process in-house | Embed from specialist providers | Video at scale is core to the product | 3D tours and specialist formats; low volume per listing |

The **hash index scope** row needs one qualification at Veldmark. Keybridge, the neutral agent SaaS, publishes agency listings to Hearthly's competitors, and the March 2027 decision bars using Keybridge agency data for Hearthly's ranking or sales targeting. Hashes of Keybridge-handled media therefore do not enter the group index; the listings Keybridge sends to Hearthly are hashed by Hearthly on arrival, like any other feed.

{id: media-pipeline--vertical-differences}
## Vertical Differences

| Dimension | General classifieds | Real estate | Automotive | Jobs | Recommerce |
| --- | --- | --- | --- | --- | --- |
| Media per listing | Few phone photos | Many professional photos (up to 999 per listing in Rightmove's feed), floor plans, tours | Many dealer photos, panoramas, sometimes video | Logos, rarely photos; CVs and documents from applicants | Several phone photos, often standardized |
| Main source | Direct upload | Feeds, pulled by URL or zipped | DMS feeds and dealer apps | Employer systems; applicant uploads | Direct upload |
| Main fraud use | Stolen photos for fake goods | Stolen photos for fake rentals | Stolen photos for deposit scams on non-existent cars | Fake employer branding; malicious documents | Stolen photos; counterfeit goods |
| Privacy risk | EXIF location of homes; faces | Occupied interiors; tenants; address | Number plates; dealer staff | CVs: personal and sensitive data | Faces, homes |
| Image models | Category and attribute hints, prohibited items | Room type, quality, floor-plan extraction | Angle, damage, odometer reading | Document parsing | Category, brand, condition |
| Legitimate duplicates | Rare | Common (multi-agency listings) | Some (manufacturer images, same dealer group) | Common (agencies reposting the same job) | Catalog photos |

The jobs column is the reminder that a shared media service must handle documents, not only images, as Adevinta's InfoJobs case showed. [Same Platform, Different Physics: How Listing Verticals Differ](#vertical-requirements) has the wider comparison.

{id: media-pipeline--failure-modes}
## Failure Modes

1. **URLs in listings.** Listings store CDN URLs; a CDN migration or domain change becomes a data migration across every listing and every partner that copied them.
2. **Storing everything forever.** No retention classes, nine renditions per image, and every feed re-download stored as a new object. Storage grows with time instead of with live inventory.
3. **Raw originals with metadata.** Derivatives are stripped, but the stored originals keep GPS coordinates and are one misconfigured bucket away from a breach.
4. **Matches that decide nothing.** Perceptual-hash matches that only create queue items, carry no seller context or cover a single brand let stolen-photo fraud run until victims report it.
5. **No allowlist.** Manufacturer, developer and stock images flood the duplicate detector, moderators stop trusting it, and it is turned off.
6. **Deletion without purge.** The master is deleted but cached derivatives keep serving for months; removed fraud listings and erased personal photos remain reachable.
7. **Unbounded transformations.** An image service that renders any size or quality on request becomes both a cost leak and an attack surface.
8. **Malformed files as server errors.** Bad uploads produce 500 errors, alerts and retries instead of a clear error the seller or partner can act on.
9. **Models that never hear about images.** Valuations, quality scores and category predictions computed before photos arrive are never recomputed, because no event tells them the media is ready.

{id: media-pipeline--the-chief-architect-s-view}
## The Chief Architect's View

Media is one of the easiest capabilities to share in a marketplace group and one of the most expensive to leave unshared. The decisions I would take to the forum:

**Share the contract first, the infrastructure second.** A common asset model, media API, derivative URL scheme and `MediaReady` event cost little and make every later consolidation cheaper. Storage and image services can follow cloud decisions at their own pace. The hash index and classifiers can be shared from day one, because they process fingerprints and model calls, not storage.

**Set retention as policy, with owners.** Retention classes need sign-off from the data protection lead, Lucía Ortega at Veldmark, and from trust and safety, Aisha Rahman, because each wants something different from the same bytes. Write the classes down, implement them as lifecycle rules, and audit them.

**Watch five numbers.** **Stored bytes per live listing** (it should be flat, not rising); **bytes delivered per gallery view**; **CDN cache hit ratio**; **time from upload to `MediaReady`** at p95; and **share of image matches against unrelated sellers that reach a decision before the listing is contactable**. The last one is the number the Barcelona review was really about.

**Plan for generated media.** Edited and generated listing images are already arriving: staged rooms, cleaned backgrounds, videos generated from photos. The pipeline must record provenance per asset, carry it to the listing page and to outbound feeds, and keep the original photograph where a buyer might reasonably need to see it. [AI Across the Listing Lifecycle](#ai-in-listing-systems) takes up the product side.

**Keep neutrality boundaries in the media layer too.** Shared fraud infrastructure is a strong case for sharing, but where a group has committed to separation, as Veldmark has for Keybridge, the boundary must be enforced in the hash index and the classifiers, not only in ranking.

{id: media-pipeline--questions-to-ask}
## Questions to Ask

1. Do listings store media IDs or URLs, and what would a CDN or domain change cost today?
2. Where is metadata stripped, and do any stored files still contain GPS coordinates or other EXIF data?
3. How many stored bytes per live listing does the platform hold, and how has that changed over the last two years?
4. Are derivatives generated on demand or stored? Which formats are served, and to what share of traffic?
5. Do feed fetchers detect unchanged media, or re-download and re-store everything on each update?
6. When are perceptual-hash checks run relative to publication, and against which brands' images?
7. What retention class applies to the media of a sold listing, a fraud removal, an erasure request and an applicant's CV, and who signed off?
8. When a listing is removed, how long do its images remain reachable on the CDN?
9. Which models depend on images, and are they recomputed when media arrives or changes?
10. How does the platform record and display whether an image is a photograph, an edited photograph or generated?

{id: media-pipeline--from-pictures-to-place}
## From Pictures to Place

Photos show what an item is; the listing also has to say where it is. Location drives search, maps, trust signals and privacy risks of its own, and photos are only one way to leak it. [Where Is It? Location, Geocoding and Privacy](#location-and-geo) takes up geocoding, precision and the privacy of a seller's address.

{id: media-pipeline--sources-and-evidence}
## Sources and Evidence

{id: media-pipeline--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Presenting Dali, an image processor service](https://tech.olx.com/presenting-dali-an-image-processor-service-514e6be00de8) — OLX Engineering, 2020 — CDN share, peak request rates, thumbor pods, the Rust and libvips replacement.
- [Handling concurrency on the web with Web Locks API](https://tech.olx.com/handling-concurrency-on-the-web-with-web-locks-api-163b7e07eddd) — OLX Engineering, 2026 — duplicate uploads from resumable uploads across browser tabs.
- [Engineers to the rescue: when your public employment service makes it impossible to apply for jobs](https://medium.com/adevinta-tech-blog/engineers-to-the-rescue-when-your-public-employment-service-makes-it-impossible-to-apply-for-jobs-b2ad6f5c29e6) — Adevinta Tech Blog, 2025 — YAMS document handling and malformed-PDF errors.
- [The 300 bytes that saved millions: optimising logging at scale](https://adevinta.com/techblog/the-300-bytes-that-saved-millions-optimising-logging-at-scale/) — Adevinta Tech Blog, 2024 — YAMS delivering more than 800 million media objects a day for all Adevinta marketplaces.
- [How we joined forces to enable GPU serving for our AI solutions](https://adevinta.com/techblog/how-we-joined-forces-to-enable-gpu-serving-for-our-ai-solutions/) — Adevinta Tech Blog, 2023 — shared image models across marketplaces.
- [Text in Image 2.0: improving OCR service with PaddleOCR](https://adevinta.com/techblog/text-in-image-2-0-improving-ocr-service-with-paddleocr/) — Adevinta Tech Blog, 2023 — OCR service volumes, accuracy and cost.
- [Real Time Datafeed specification v1.4.1](https://media.rightmove.co.uk/ps/pdf/guides/adf/Rightmove_Real_Time_Datafeed_Specification.pdf) — Rightmove, 2023 — media pulled by URL, limits, media update date.
- [Seller-API documentation](https://services.mobile.de/manual/seller-api.html) — mobile.de, n.d. — pre-uploaded image references, battery-health certificates, price rating recalculated with images, Auto Panorama.
- [Full-year results FY26](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf) — Autotrader Group plc, 2026 — Co-Driver image re-orders and descriptions.
- [Zillow Group Form 10-K for FY2025](https://www.sec.gov/Archives/edgar/data/1617640/000161764026000015/z-20251231.htm) — Zillow Group, 2026 — Showcase, interactive floor plans and 3D touring.
- [CoStar Group Form 10-K for FY2025](https://www.sec.gov/Archives/edgar/data/1057352/000105735226000020/csgp-20251231.htm) — CoStar Group, 2026 — Matterport acquisition completed 28 February 2025.
- [Data Science at OLX](https://tech.olx.com/data-science-at-olx-7c7406d1713f) — OLX Engineering, 2020 — photo-quality recommendations for sellers.
- [ZInD: Zillow Indoor Dataset](https://github.com/zillow/zind) — Zillow, n.d. (presented 2021) — panoramas and floor plans for research.

{id: media-pipeline--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [PDQ documentation](https://github.com/facebook/ThreatExchange/tree/main/pdq) — Meta, ThreatExchange repository, n.d. — quality and distance thresholds; rotation handling.
- [Open-sourcing photo- and video-matching technology](https://about.fb.com/news/2019/08/open-source-photo-video-matching/) — Meta, 2019 — PDQ and TMK+PDQF release.
- [imgproxy](https://github.com/imgproxy/imgproxy) — imgproxy, n.d. — type and dimension checks against image bombs; signed URLs; metadata stripping.
- [thumbor](https://github.com/thumbor/thumbor) — thumbor project, n.d. — on-demand imaging with smart cropping.
- [ClamAV documentation](https://docs.clamav.net/) — Cisco Talos, n.d. — scope of the open-source scanner.
- [GPS tags](https://exiftool.org/TagNames/GPS.html) — ExifTool, n.d. — location data in photo metadata.
- [Can I use: AVIF](https://caniuse.com/avif) and [WebP](https://caniuse.com/webp) — caniuse.com, accessed 2026-10-19 — browser support shares.
- [Storage classes](https://docs.cloud.google.com/storage/docs/storage-classes) — Google Cloud, updated 2026 — classes, minimum durations, Autoclass.
- [Amazon S3 storage classes](https://aws.amazon.com/s3/storage-classes/) — Amazon Web Services, n.d. — minimum durations and Intelligent-Tiering transitions.
- [Product data specification](https://support.google.com/merchants/answer/7052112) — Google Merchant Center, n.d. — 500 × 500 pixel image minimum from 31 January 2027.
- [Catalog product fields reference](https://developers.facebook.com/docs/marketing-api/catalog/reference) — Meta, n.d. — up to 20 videos per item.
- [OpenImmo](https://www.openimmo.de/) — OpenImmo e.V., n.d. — media zipped with XML for exchange.
- [EU AI Act, Article 50](https://artificialintelligenceact.eu/article/50/) — Regulation (EU) 2024/1689, unofficial reproduction, 2024 — marking of synthetic images and deep-fake disclosure; applies from 2 August 2026.

{id: media-pipeline--research-and-practitioner-sources}
### Research and practitioner sources

- [Introducing NIMA: Neural Image Assessment](https://research.google/blog/introducing-nima-neural-image-assessment/) — Google Research, 2017 — image quality scoring as a rating distribution.
- OLX Engineering posts on image duplicate detection and triplet-loss fraud detection — OLX, n.d. — known through search summaries only; the originals were not accessible for this book.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
