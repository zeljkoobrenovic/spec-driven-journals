#!/usr/bin/env python3
"""Apply the 24 September 2026 round-2 review text changes to the comic script of
27-manage-technical-debt (MTD-005/006/011/012/013/018/020).
Edits the comic-page JSON blocks and the intro paragraph in place; run generate_comic_pages.py --render
afterwards, then --generate --overwrite for pages 02, 05 and 06."""
import json, re
from pathlib import Path
P = Path(__file__).resolve().parents[1] / 'posts/27-manage-technical-debt/comics.md'
text = P.read_text()
# ---- intro (MTD-018: name the enlargement affordance) -- done BEFORE locating blocks so offsets stay valid
old_intro = "All are fictional, and every amount and date is invented for the example."
assert text.count(old_intro) == 1
text = text.replace(old_intro, old_intro + " On a phone the lettering is small: tap or click any page to open it at full size, and the lines under each page repeat every word of its lettering.")

pat = re.compile(r'<!-- comic-page\n(\{.*?\n\})\n-->', re.S)
blocks = {}
for m in pat.finditer(text):
    b = json.loads(m.group(1)); blocks[b['id']] = (m, b)
def strips(b): return b['strips']

# ---- page 1 (MTD-005: lead time)
m, b = blocks['01-two-questions-one-wrong-answer']
b['caption'] = b['caption'].replace(
    "and speed lost (delayed changes and deals the product cannot take).",
    "and speed lost (lead time, the working days from an agreed change to its delivery, and deals the product cannot take).")
assert "lead time, the working days" in b['caption']

# ---- page 2 (MTD-013, MTD-005)
m, b = blocks['02-five-items-four-origins']
s1 = strips(b)[1]
s1['bubbles'][0]['text'] = "Item 4 was a dated shortcut, owned by me. Accountable, not necessarily wise."
s1['bubbles'][1]['text'] = "An undated one is. A close date nobody inside chose goes first."
b['caption'] = ("Larkspur's register has five items; they are the board's shortlist, and a longer register sits behind them. "
  "Item 1 is the invoicing module, the software that prepares customer bills, whose code is still tangled so that parts cannot change alone. "
  "Item 2 is the reporting stack on a version its vendor no longer fixes security holes in. Item 3 is the scheduling engine, which runs each region on one server. "
  "Item 4 is the artificial intelligence (AI) sorting feature: the prompt, the instructions sent to the AI model that sorts customers' documents, "
  "is written into the program, so every change to it needs a software release. Item 5 is the vendor retiring the AI model that feature runs on. "
  "The origin of each decides who owns it and what the remedy usually is; a deliberate shortcut recorded with a date and an owner is not a failure of record, "
  "though the record makes it accountable, not necessarily wise; an undated one is a failure. A tranche is a separately approved stage of work, so growth that outran a design is fixed in tranches, "
  "and a date nobody inside chose goes first when it is close; a distant date with little work behind it can wait. Carried, the five cost about €10,000 a month: €5,500 of cash paid to hosting providers, "
  "the companies whose servers run the software, and about €4,600 of the company's own engineering time, already on the payroll and valued at what it costs to employ the engineers. "
  "The invoicing tangles cause two customer-visible incidents a quarter, and the scheduling engine caused the year's last two incidents and takes 45 minutes to fail over, "
  "that is, to move its work to a replacement server. Its single-server design also turns away prospects, potential customers, above about 400 technicians: two this year, "
  "about €12,000 a month of revenue (sales income) not won. Sam leads finance.")
b['alt'] = ("Comic page in three strips: five cards on a pinboard read invoicing tangles, reporting stack unsupported, scheduling engine one server, AI prompt in code, "
  "and vendor model retiring, and Alex calls them the board's shortlist over a longer register; a whiteboard pairs each origin with its remedy, dated shortcut revisit on date, "
  "growth outran design tranches, ageing platform and retiring vendor by the date, while Priya calls her dated shortcut accountable but not necessarily wise and Alex says a close date nobody inside chose goes first; "
  "a second whiteboard totals the register at about €10,000 a month, two invoice incidents a quarter, a 45-minute failover and €12,000 a month not won.")

# ---- page 4 (MTD-005: frozen)
m, b = blocks['04-rewrite-tranches-or-live-with-it']
b['caption'] = b['caption'].replace("takes nine months with the old engine frozen and every risk",
                                    "takes nine months with the old engine frozen, still running but no longer changed, and every risk")
assert "still running but no longer changed" in b['caption']

# ---- page 5 (MTD-020, MTD-012, MTD-013, MTD-005)
m, b = blocks['05-the-dated-item-goes-first']
s0 = strips(b)[0]
s0['bubbles'][0]['text'] = "Our largest prospect's security review needs supported components by the end of March 2028."
s0['bubbles'][1]['text'] = "The reporting stack lost support in March, and it has no half-way state."  # simpler wording after two garbled rolls
s2 = strips(b)[2]
s2['labels'] = ["CLOSE DATES FIRST, BY DATE", "REST: COST REMOVED PER EFFORT", "SUCCESSOR TEST BY 29 NOVEMBER"]
s2['bubbles'][0]['text'] = "Same rule, longer fuse: Alex tests the successor model by 29 November."
s2['bubbles'][1]['text'] = "Four months before retirement. If it fails, customers' planners confirm each sort."
b['caption'] = ("A migration moves software from one platform or vendor to another. The reporting stack, the software that produces customer reports, "
  "sits on a framework version, the reusable software it is built on, whose vendor stopped fixing its security holes in March 2027, and the largest prospect's security review "
  "requires supported components by the end of March 2028. The supported version builds reports differently, so there is no useful half-way state: its migration is a small rewrite "
  "with the benefit at the end, the one shape in which that is right. It goes first, ahead of the scheduling engine whose carrying cost is larger, because its date is close and its work "
  "is small: six engineer-weeks, six weeks of one engineer's time or three weeks each for two, and €5,000 of cash. The rule has two parts: an item whose external date leaves little "
  "more time than the work needs, with a margin, goes first, in date order, weighed against what missing the date would cost; a distant date with little work behind it can wait behind "
  "an undated item doing harm now. The rest are ordered by the carrying cost each stage of effort would remove, across all three columns. The vendor has named the successor to the "
  "retiring artificial intelligence (AI) model; the contract lets Larkspur test it on its release samples, and Alex does so by 29 November 2027, sixty days after the notice and four "
  "months before the 31 March 2028 retirement. If the samples fail, Larkspur's own rule gives it sixty days, to 28 January, to choose between the successor, another vendor's model "
  "and the fallback, and the contract lets it end the commitment on the retirement date. The fallback is the review mode from the trial: the feature proposes a category and each "
  "customer's own planner confirms it, with no new Larkspur staff; if no model is usable on the date, customers' planners sort by hand as they did before the trial.")
b['alt'] = ("Comic page in three strips: a timeline marks patches ended 31 March 2027, security review by March 2028, and model retires 31 March 2028; a card reads reporting stack "
  "migration, six engineer-weeks and €5,000 cash, November to December 2027, and Ines says it goes before item 3 because the date is close and the work is small; a whiteboard gives "
  "the sequencing rule, close dates first by date, rest by cost removed per effort, successor test by 29 November, and Ines says that if the test fails customers' planners confirm each sort.")

# ---- page 6 (MTD-006, MTD-011)
m, b = blocks['06-the-decision-and-the-gate']
s0 = strips(b)[0]
s0['scene'] = ("One decision sheet is pinned flat high on the wall, above everyone's heads, its heading and five lines of lettering facing the reader; "
  "it is the only lettered object. Below it Ines sits at a desk signing a plain page that carries only ruled lines. Alex stands at the right of the desk. "
  "No head, hand, pen or bubble covers the lettering.")
s0['labels'] = ["DECISION: STACK NOV–DEC 2027", "THEN ENGINE TRANCHE 1, JAN–MAR", "€50,000 TIME + €8,000 CASH",
                "REJECTED: REWRITE", "€300,000 TIME + €40,000 CASH"]
s0['label_notes'] = "The five labels are the five lines of the sheet, top to bottom; the third line prices tranche 1 and the fifth prices the rejected rewrite."
s2 = strips(b)[2]
s2['scene'] = ("A pinboard high on the wall, above everyone's heads with exactly three index cards pinned side by side in one row with clear gaps; the first card carries "
  "two lines of lettering, the other two one line each. Sam, at the left, gestures up at the first card with an open hand. Alex, at the right, points up at the third card. "
  "No head, hand, marker or bubble covers the lettering.")
s2['labels'] = ["PORTAL REDESIGN: APRIL–JUNE", "AUGUST–OCTOBER IF TRANCHE 2", "TRANCHE 1 ENGINEERS: NAMED", "INVOICING SPECIALISTS: NOT INVOLVED"]
s2['label_notes'] = "The first two labels are the two lines of the first card; the third and fourth labels are the second and third cards."
s2['bubbles'][0]['text'] = "Portal engineers: migration, then tranche 1. Redesign in April, or August if tranche 2."
b['alt'] = ("Comic page in three strips: Ines signs a decision sheet reading stack November to December 2027, then engine tranche 1 January to March at €50,000 of time plus "
  "€8,000 of cash, rejected rewrite at €300,000 of time plus €40,000 of cash, and Alex says tranche 2 is a conditional line released only on the gate's evidence; a whiteboard "
  "states the gate for tranche 2, read 31 March 2028, failover under five minutes, hosting down €1,500 a month, no incident from the split, lead time no worse, while Alex says "
  "the split is live by 29 February with one month observed and all four must pass together; three cards read portal redesign April to June, August to October if tranche 2, "
  "tranche 1 engineers named, invoicing specialists not involved, and Sam says the redesign starts in April, or August if tranche 2 runs.")
b['caption'] = ("Ines, the chief executive, may approve spending inside the plan the board has adopted and below a limit the board set; that is her delegation. She authorizes the "
  "reporting-stack migration and the November model test under it. Tranche 1 of the engine, about €50,000 of the company's own engineering time plus €8,000 of cash and two named "
  "engineers for a quarter, is requested in the 2028 plan the board approves in January; tranche 2 is requested in the same plan as a conditional line that Ines may release only "
  "against the gate's evidence, which the board sees in April. The rejected rewrite is priced on the same basis, about €300,000 of engineering time plus €40,000 of cash; it would have "
  "been outside any approved plan, so a board decision on its own. The split goes live by 29 February 2028, March is one month of live operation, and the gate is read on 31 March: all "
  "four conditions must pass at the same reading, any unmet condition blocks tranche 2 until every condition is re-read and passes, and an incident means fixing its cause and "
  "observing one further clean month. Lead time, the working days from an agreed change to its delivery, must be no worse: a safeguard, not a gain. The two engineers named for the "
  "customer portal redesign, the rebuild of the website customers use, spend six engineer-weeks on the migration in November and December and build tranche 1 from January to March; "
  "the redesign, originally January to March, moves to April to June if the work stops after tranche 1, and to August to October if tranche 2 starts in April, later still if approval "
  "or the gate slips; its owner is told so.")

# ---- write blocks back
for pid, (m, b) in sorted(blocks.items(), key=lambda kv: kv[1][0].start(), reverse=True):
    text = text[:m.start(1)] + json.dumps(b, ensure_ascii=False, indent=2) + text[m.end(1):]
P.write_text(text)
print('comics blocks updated')
