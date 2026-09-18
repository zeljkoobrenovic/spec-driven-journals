# Restructuring Plan — Book Flow and Framing

**Status:** working notes, not yet decided
**Date:** 2026-09-13
**Scope:** the book's framing and part structure, from the perspective of the product and engineering leader who reads it

This is a discussion document. Nothing here has been applied to `config.yaml`, `index.md`, or any chapter. It records the reasoning so the decisions can be made deliberately rather than inside an edit.

---

## 1. The framing decision (decide this first)

Everything else follows from one question: **is this a book about private equity, or a book about leading product and engineering under external ownership?**

### Where the manuscript is now

It is **PE-centric with a technology reader**. The subject is private equity; the reader happens to be a CTO. Parts I, II, V and VI all explain how the machine works. Only Part III is written in the reader's own voice, about their own work.

This is a drift from the original brief, which asked for "demystifying private equity **for** product and engineering leaders."

### The proposed correction: two steps, not one

**Step one — leader-centric rather than PE-centric.** The subject becomes *your job under this kind of ownership*; the investor is the condition, not the topic.

Reasons to take this step:

- It is what the original brief actually asked for.
- "How PE works" is a crowded shelf, competing with people who do deals for a living. "How to run product and engineering when an investor owns you" is nearly empty.
- It resolves Parts IV and V, which currently sit awkwardly because they are written from the *firm's* chair rather than the reader's.

Cost: Part I becomes explicitly instrumental — finance you need in order to argue, not finance for its own sake. The Part I introduction already says exactly this ("the arguments you will need to make later are all financial arguments in disguise"), so the frame is half-built.

**Step two — investors and investment generally, rather than private equity only.**

The reader's problem is broader than PE. A leader who needs this book is usually facing one of: a VC-backed company that just raised and now has a board, a founder-owned company taking growth equity, a buyout, a carve-out, a strategic or corporate investor — or the same company passing between two of those. The underlying skill (read the money, find who decides, argue in financial terms, extract value from the owner) transfers across all of them.

The manuscript already crosses this line. [[pt-investment-fit]] covers venture, growth, buyout, carve-out and turnaround. [[pt-how-companies-get-money]] is about how any company is financed at all. Those two chapters are already writing the broader book.

It also fixes a structural weakness: while PE is the subject, the book keeps *explaining PE*. If investors-in-general is the subject, PE becomes **the hardest case** — most leverage, shortest clock, most explicit governance — and explaining it is instrumental. That is a better posture, and it enables something the PE-only version cannot say: *what changes when the ownership type changes*, which is where much of the useful judgment lives.

### What broadening costs

| Cost | Detail | Mitigation |
| --- | --- | --- |
| Distinctiveness | "How tech leaders work with investors" is a vaguer shelf than "under PE ownership." Specificity is currently the edge. | Keep depth concentrated in PE; broaden the frame, not the treatment. |
| Evidence base | The case spine (Hilton, Skype, Visma, Toys R Us, TeamSystem) is entirely buyout/PE. Part VI would make general investor claims off PE-only evidence. | Either add a VC-backed and a growth-equity case, or state explicitly that the cases test the buyout end of the spectrum. |
| The author's own vantage | The Technology Principal thread, Productscapes, the grounding job description — all PE. That is the part only this author can write. | Keep it PE-specific and labelled as the deepest treatment, not generalized. |

### Recommendation

**Broaden the frame, keep the specialty.** Subject broad, depth concentrated:

- **Framing:** investors and ownership, not private equity alone. The promise is the reader's job under external ownership, whoever the owner is.
- **Part I becomes genuinely comparative** — "what kind of owner do you have, and what does that change" across venture, growth, buyout, carve-out, strategic and founder-held, with PE explained in the most depth because it is the most structurally demanding.
- **Parts II–V stay as designed**, but each names where ownership type changes the answer. Governance under a VC board is not governance under a majority sponsor; incentives with options are not incentives with rollover equity; sponsor leverage from a growth investor is a different menu than from a buyout firm. These are one-paragraph or one-table distinctions per chapter, not new chapters — and they are the detail that makes a book feel authoritative.
- **Be explicit that the evidence concentrates on buyouts.** The manuscript is already unusually honest about evidence limits; this is the same move.
- **Keep the PE-specific material PE-specific.** The Technology Principal, Productscapes and the case spine are the deepest treatment, not generalized claims.

The book becomes: *here is how to operate under any investor, told by someone who works at the sharpest end of it.*

### Consequences to accept

- **"Private Techuity" stops fitting as a title.** It is a PE pun; under the broader subject it promises the narrower book. See §1a for the replacement. The journal directory and the `pt-` permalink prefix are internal and can stay regardless — this is a cover-title question only.
- **Part IV gets better, not worse.** "Leveraging your investor" is richer when the investor might be a VC with a talent partner, a growth fund with a customer network, or a sponsor with an M&A team. The menu differs by owner type, and comparing them is genuinely useful.

---

## 1a. Title and terminology

### Working title (selected 2026-09-13)

> **OWNED: Product & Engineering Leadership Under Investors**

Why it works: "Owned" is short, states the reader's actual condition, and carries the faint edge of the colloquial sense without committing to it — which suits a book that refuses to be either promotional or hostile about investors. The subtitle does the scoping work, naming both the reader and the setting.

Two things it costs, accepted knowingly:

- **It reads best in English.** The double meaning and the clipped one-word punch do not survive translation, and a non-native reader may take it literally. The subtitle carries the meaning on its own, so the downside is small — but the audience is substantially European technology leadership.
- **It retires "Techuity" from the cover.** Open question: is Techuity retired as a concept, or does it survive as a term inside the book? The journal directory (`private-techuity/`) and the `pt-` permalink prefix are internal and stay regardless.

Alternatives considered: *Techuity* alone (drops "Private," keeps the coinage, cheapest possible fix); *Someone Else's Money* (evocative, but a well-known film about a corporate raider); *When Investors Own Your Roadmap*; *Answering to Owners*.

### Terminology: prefer "ownership," not "investment"

**"Investment" is ambiguous in a technology book.** Engineers use it to mean *spending on a system* ("we should invest in the platform"), and the chapters use it in that sense constantly. If the framing noun and the body prose use the same word for two different things, that is avoidable friction.

House usage:

| Job | Preferred | Avoid |
| --- | --- | --- |
| The category the book is about | **investor ownership**; **investor-backed** as an adjective | "institutional investment" (academic), "sponsored ownership" (borrows a PE term of art too broadly) |
| The arrangement the reader manages | **the ownership arrangement**; **the investment relationship** | — |
| In body prose | **your owners**, **your investors** — plainest and best | abstractions where a plain noun works |
| Spending on systems | **investment** keeps this meaning | — |

Note that the existing chapter prose mostly already says "owner" and "investor" rather than "private equity." The drift toward PE sits in the part titles and part introductions, less in the body — which makes the reframe cheaper than it looks.

---

## 2. Part-by-part analysis

### Part I — Understanding private equity → comparative ownership

**Current:** `00-how-companies-get-money`, `01-capital-and-ownership`, `26-valuation-and-architecture`, `02-return-mechanics`, `03-investment-fit`, `04-cash-and-constraints`

**Verdict:** works as-is; the only part where "understanding the machine" is genuinely the job.

**Under the broader frame:** make the spine "what kind of owner do you have, and what does that change." Chapters 00 and 03 already do this; the others need PE positioned as one case treated in most depth rather than as the default. This is the part where the broadening change is largest — worth sketching first to test whether the broader book still feels like the author's.

### Part II — The investor–company relationship

**Current:** `05-governance`, `06-incentives`, `07-investor-fit`

**Problem:** the title names a relationship but not a stake.

**What the part is actually about:** who is entitled to decide, what they want, and whether you can work with them.

Candidate titles:

- **"Who Decides What You Can Do"** — reader-facing, concrete, states the stake immediately. *Recommended.*
- "Ownership, Authority, and Decision Rights" — accurate, drier.
- "Living With Your Owners" — warmer, weaker.

The existing part introduction's one-liner ("the money is settled; now find out who is actually allowed to decide") is already that title in sentence form.

### Part III — Creating value through product and technology

**Current:** `08-product-value`, `09-engineering-and-architecture`, `27-valuation-and-design`, `10-cloud-economics`, `11-security-and-resilience`, `12-data-and-ai`, `13-people-and-operating-models`, `14-acquisitions-and-carveouts`

**Problem:** the title does say "creating value," but the introduction reads as generic tech-to-business translation that would be true with no investor anywhere. The fix is the frame more than the title: this is where **the investment thesis becomes engineering work**.

Candidate title: **"Turning the Investment Thesis Into Product and Engineering Work"** — long, but it names what makes the part specific.

**On length:** eight chapters, by far the largest part. Leave it. It is the reader's own job, and length there signals priority correctly. (A split into "value mechanics" — 08, 09, 27 — and "specific arenas" — 10–14 — remains available if the part becomes unwieldy.)

### Part IV — The Technology Principal's work → working the ownership structure

**Current:** `15-technology-principal`, `16-diligence-and-thesis`, `22-first-hundred-days`, `18-execution-and-exit`

**The proposal:** flip from "here is what a Technology Principal does" to "**here is how to use the investment structure to your advantage**" — sponsor support, the firm's network, bootstrapping, acceleration of product development, of engineering, and of team growth.

This converts the most inside-baseball section into the most actionable, and it is the strongest idea on the list.

**How much is actually new — less than it first appears.** Reading the section headings, three of the four Principal chapters already carry substantial company-side content:

- `16-diligence-and-thesis` ends on "Diligence Ends When Management Accepts the Findings"
- `22-first-hundred-days` is explicitly about converting findings into a *company-owned funded plan*
- `18-execution-and-exit` has "Portfolio Collaboration Must Earn Its Time" and "Escalate Through a Defined Path"

Those are already about the company using the relationship; they are narrated from the adviser's chair. **Flipping the point of view is an editing job, not a rewrite.**

**The genuine gap** is the *sponsor-leverage inventory*: what a firm can actually supply (operating partners, portfolio peer networks, hiring reach, shared tooling, M&A machinery, benchmark data, capital sequencing), how to ask for it, and what accepting it costs you. Scattered pieces exist — [[pt-technology-capability-as-product]]'s "accelerator small enough to use," [[pt-security-and-resilience]]'s "Shared Support Can Spread Risk or Concentrate It," [[pt-people-and-operating-models]]'s location and talent material, [[pt-investor-fit]]'s "Make the Support Offer Reviewable" — but nothing collects them from the receiving end.

**Estimated work:** two new chapters, plus a point-of-view pass on 15–18. Not five new chapters.

Proposed title: **"Working the Ownership Structure."**

### Part V — Productscapes → appendix

**Current:** `19-investment-firm-as-product`, `20-technology-capability-as-product`

**Verdict:** move to an appendix, keep it labelled as the author's hypothesis.

The reason is stronger than length: the part's own introduction opens by disclaiming itself — "read this sceptically," "it is a hypothesis," "no evidence here shows that adopting them improves returns or company outcomes." A part that begins by disclaiming itself belongs after the argument, not inside it. As an appendix it stays a distinctive contribution without interrupting the reader's spine.

### New Part V — through the ownership cycle

The Part IV rewrite creates an orphan problem: diligence, first-100-days and execution-and-exit are *lifecycle* chapters, and they are arguably the most useful material in the book for a reader who has just been acquired.

Written from the reader's chair, these chapters answer "what happens to me, in what order": being diligenced, the first hundred days as the company rather than the adviser, the long middle, and preparing for exit. That is a spine, and it is currently buried inside the Principal's part.

### Part VI — Durable value, success, and failure

**Current:** `26-hilton-and-skype`, `27-visma`, `28-toys-r-us`, `29-teamsystem`, `24-durable-value`

**Problem:** the title states a conclusion; the part is really evidence-testing.

Candidate titles:

- "Lessons From the Field" — warmer. *Recommended.*
- "Testing the Argument Against Real Companies" — more accurate.
- "What the Record Shows"

---

## 3. Proposed shape

| | Part | Chapters | Change |
| --- | --- | --- | --- |
| I | Understanding investors and ownership | 00, 01, 26, 02, 03, 04 | comparative reframe; renumber |
| II | **Who decides what you can do** | 05, 06, 07 | retitle + introduction reframe |
| III | **Turning the thesis into product and engineering work** | 08, 09, 27, 10, 11, 12, 13, 14 | retitle + introduction reframe |
| IV | **Working the ownership structure** | 15 (company-side rewrite), + 2 new: *what an investor can supply* / *asking for it, and what it costs* | new part |
| V | **Through the ownership cycle** | 16, 17, 18 (point-of-view flip) | new part from old Part IV |
| VI | **Lessons from the field** | 21, 22, 23, 25, 24 | retitle only |
| App. | Productscapes: a hypothesis | 19, 20 | demoted from Part V |

Reader question per part:

- **I** — What is this machine, and which kind of owner do I have?
- **II** — Who am I answerable to now?
- **III** — How does my work become value?
- **IV** — What can I get out of this?
- **V** — What happens to me, and when?
- **VI** — Did any of this hold?

---

## 4. Housekeeping to do regardless

**Folder numbering no longer matches reading order.** Chapters 26 and 27 are numbered last but placed early — 26 sits third in Part I, 27 fourth in Part III. Folder 26 is the money primer that everything else depends on, so the numbering is actively misleading. Renumber the folders to match reading order; `permalink:` values stay put, so no URLs break and no `[[…]]` cross-links need touching.

---

## 5. Open questions

1. **Framing: broaden to investors generally, or stay PE-only?** Recommendation above is to broaden. If yes, the cover title needs revisiting and Part I needs the comparative reframe.

2. **Part IV — commit or defer?** Two new chapters plus a point-of-view pass on 15. If committing, write `spec.md` first (per the repository's spec-driven convention) so the scope of "leveraging the structure" is agreed before drafting.

3. **The Technology Principal's fate.** Under the proposed shape, chapter 15 is rewritten as "who is across the table and what they can do for you" — which serves the reader but loses the Principal as a vantage point. Alternative: keep 15 largely as-is inside Part IV and add the two sponsor-leverage chapters around it, so both sides of the table are visible. Slightly less clean; more honest to the author's own career direction. A third option is to keep the Principal as a recurring "from the other side of the table" note in each part rather than a part of its own.

4. **Case-spine breadth.** If the frame broadens, does Part VI add a VC-backed or growth-equity case, or does it state explicitly that the evidence tests the buyout end only?

5. **Part titles.** Working titles proposed above; cheapest thing to change and the place the author will have the strongest opinion.

---

## 6. Suggested next step

Sketch **Part I under the comparative frame** first. It is where the broadening change is largest, and it will show quickly whether the broader book still feels like the author's.

After that, drafting the six part introductions against the proposed shape is the fastest way to read the book's spine and surface structural problems — and it is fully reversible, since no chapter or config file moves.
