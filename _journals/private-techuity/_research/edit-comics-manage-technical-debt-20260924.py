#!/usr/bin/env python3
"""Apply the 24 September 2026 round-1 review text changes to the comic script of
27-manage-technical-debt (MTD-001/002/003/005/006/009/010/011/012/013/014/017/019).
Edits the comic-page JSON blocks in place; run generate_comic_pages.py --render afterwards."""
import json, re
from pathlib import Path
P = Path(__file__).resolve().parents[1] / 'posts/27-manage-technical-debt/comics.md'
text = P.read_text()
pat = re.compile(r'<!-- comic-page\n(\{.*?\n\})\n-->', re.S)
blocks = {}
for m in pat.finditer(text):
    b = json.loads(m.group(1)); blocks[b['id']] = (m, b)

def strips(b): return b['strips']

# ---- page 1
m, b = blocks['01-two-questions-one-wrong-answer']
strips(b)[1]['bubbles'][0]['text'] = "Debt is the extra cost we carry each month because of how it's built."
b['caption'] = ("Every amount and date in this comic is invented for the example. Larkspur is a fictional company that sells "
  "scheduling software; an investor owns a large stake in it, and the board is the group of directors that oversees the "
  "company. Technical debt is the extra cost a company carries because its software was built, or has aged, in ways that "
  "make it slower, riskier or dearer to change than it needs to be; the word is a metaphor, not a loan. Morgan advises the "
  "investor; Alex leads technology; Priya leads product. A carrying cost is what an item costs the company while it remains, "
  "in three columns: cost carried (euros per month), risk carried (incidents, unsupported parts, dated retirements) and speed "
  "lost (delayed changes and deals the product cannot take). The last two keep their own units and are read alongside the "
  "money, not added to it.")
b['alt'] = ("Comic page in three strips: Morgan hands Alex a note asking how much technical debt and why not rewrite, and Alex says "
  "a count or a percentage answers neither; three cards read issue count and percent of code, both struck through, and carrying "
  "cost per month in bold, while Alex says debt is the extra cost carried each month because of how the software is built; a "
  "whiteboard shows three columns, cost carried with workaround hours and old hosting, risk carried with incidents, unsupported "
  "and retiring, and speed lost with lead time and deals lost.")

# ---- page 2
m, b = blocks['02-five-items-four-origins']
strips(b)[0]['bubbles'][0]['text'] = "Five items: the board's shortlist. The full register behind it is longer."
strips(b)[2]['labels'] = ["ABOUT €10,000 A MONTH", "2 INVOICE INCIDENTS A QUARTER", "FAILOVER: 45 MINUTES", "€12,000 A MONTH NOT WON"]
strips(b)[2]['bubbles'][0]['text'] = "Carried, the five cost about €10,000 a month: €5,500 cash, €4,600 of our time."
b['caption'] = ("Larkspur's register has five items; they are the board's shortlist, and a longer register sits behind them. The origin "
  "of each decides who owns it and what the remedy usually is; a deliberate shortcut recorded with a date and an owner is not a "
  "failure of record, an undated one is. A tranche is a separately approved stage of work, so growth that outran a design is fixed "
  "in tranches. Carried, the five cost about €10,000 a month: €5,500 of cash paid to hosting providers and about €4,600 of the "
  "company's own engineering time, valued at what it costs to employ the engineers. The invoicing tangles cause two customer-visible "
  "incidents a quarter, and the scheduling engine, which runs each region on one server, caused the year's last two incidents and "
  "takes 45 minutes to fail over, that is, to move its work to a replacement server. Its single-server design also turns away "
  "prospects, potential customers, above about 400 technicians: two this year, about €12,000 a month of revenue not won. Sam leads finance.")
b['alt'] = ("Comic page in three strips: five cards on a pinboard read invoicing tangles, reporting stack unsupported, scheduling engine one "
  "server, AI prompt in code, and vendor model retiring, and Alex calls them the board's shortlist over a longer register; a whiteboard "
  "pairs each origin with its remedy, dated shortcut revisit on date, growth outran design tranches, ageing platform and retiring vendor by "
  "the date; a second whiteboard totals the register at about €10,000 a month, two invoice incidents a quarter, a 45-minute failover and "
  "€12,000 a month not won.")

# ---- page 3
m, b = blocks['03-present-the-fix-by-what-it-buys']
strips(b)[2]['bubbles'][0]['text'] = "For the engine: two prospects, oversized servers, a 45-minute failover: a month's downtime allowance."
b['caption'] = ("A reduction project is presented the way the board reads any investment: the revenue it protects or enables (sales the "
  "product could make or keep), the cost or risk it removes and, only where a real dated decision is being kept open, the decision it "
  "preserves. None of the three can be priced exactly, so the work is judged on the register columns it moves, measured before and "
  "after. The board rarely sees the failures a fix prevented, because a prevented failure is invisible while the effort sits on this "
  "quarter's budget; the after column is the answer. For the engine, a failover, moving its work to a replacement server, takes 45 "
  "minutes; Larkspur promises its service is usable 99.9% of the month, which allows about 43 minutes of downtime, so one real failover "
  "would use the whole month's allowance. The two-second promise for confirming an appointment is a separate measure, response time, "
  "which this work does not change. Ines is the chief executive.")
b['alt'] = ("Comic page in three strips: three cards read revenue protected or enabled, cost or risk removed, and a decision kept open; a "
  "before-and-after table lists incidents per quarter, failover time and lead time with empty cells, while Sam says nobody gets credit "
  "for a failure that never happened; four cards for the scheduling engine read two prospects €12,000 a month, €4,000 hosting above need, "
  "45-minute failover, and core replacement kept open, and Alex calls the 45-minute failover a month's downtime allowance.")

# ---- page 4
m, b = blocks['04-rewrite-tranches-or-live-with-it']
s0 = strips(b)[0]
s0['labels'] = ["A: REWRITE THE ENGINE", "€300,000 TIME, €40,000 CASH", "BENEFIT AT MONTH 9",
                "B: TRANCHES WITH GATES", "TRANCHE 1: €50,000 TIME", "€8,000 CASH, BENEFIT MONTH 3",
                "C: LIVE WITH IT", "COST CONTINUES"]
s0['bubbles'][0]['text'] = "Three ways to reduce item 3, on one basis: staff time, cash, benefit date."
s0['bubbles'][1]['text'] = "A rewrite buys nothing before month nine. Tranche 1 buys failover at three."
s1 = strips(b)[1]
s1['labels'] = ["MONTH 0", "MONTH 3", "MONTH 7", "MONTH 9", "REWRITE", "TRANCHE 1: €58,000", "GATE", "TRANCHE 2: €80,000"]
s1['label_notes'] = ("The four MONTH labels sit over the four ticks, left to right; REWRITE is lettered on the long upper bar; "
                     "TRANCHE 1: €58,000 on the first lower bar, GATE beside the barrier, TRANCHE 2: €80,000 on the second lower bar.")
s2 = strips(b)[2]
s2['labels'] = ["REWRITE, MONTH 5:", "€180,000 GONE, €160,000 TO DECIDE", "TRANCHE 1 DONE:", "€58,000 SPENT, FAILOVER IN HAND"]
s2['bubbles'][0]['text'] = "Month five of a rewrite: €180,000 gone either way; only the €160,000 left counts."
b['caption'] = ("For the scheduling engine, a rewrite (replacing the system with a new one) takes nine months with the old engine frozen "
  "and every risk arriving at one switch-over; it costs about €300,000 of the company's own engineering time plus €40,000 of "
  "additional cash, about €340,000 in all. A tranche is a separately approved stage of the work; a gate is the check, agreed in "
  "advance, that must pass before the next tranche is funded. Tranche 1 splits the schedule computation so it can fail over: about "
  "€50,000 of time plus €8,000 of cash, benefit at month three. Tranche 2 gives the largest customers their own servers: about "
  "€70,000 of time plus €10,000 of cash, benefit at month seven, about €138,000 for both stages together; replacing the core stays a "
  "later decision. Living with it keeps the carrying cost. Money already spent is gone the moment it is spent, whether or not any "
  "benefit has arrived, so it should not tip the next decision: five months into the rewrite about €180,000 is gone and nothing has "
  "been bought yet, and only the remaining €160,000 and the benefit still to come should decide whether to continue. After tranche 1 "
  "the remaining decision is only about tranche 2.")
b['alt'] = ("Comic page in three strips: three cards compare A, rewrite the engine, €300,000 of staff time and €40,000 of cash with the "
  "benefit at month nine, B, tranches with gates, tranche 1 at €50,000 of time plus €8,000 of cash with failover at month three, and "
  "C, live with it, cost continues; a timeline with ticks at months 0, 3, 7 and 9 shows one long rewrite bar ending in a single flag "
  "against two tranche bars labelled tranche 1 €58,000 and tranche 2 €80,000 with flags at months 3 and 7 and a gate between; a "
  "whiteboard reads rewrite month 5, €180,000 gone and €160,000 to decide, against tranche 1 done, €58,000 spent and failover in hand.")

# ---- page 5
m, b = blocks['05-the-dated-item-goes-first']
b['title'] = "A close date goes first"
s0 = strips(b)[0]
s0['labels'] = ["PATCHES ENDED 31 MAR 2027", "SECURITY REVIEW: BY MARCH 2028", "MODEL RETIRES 31 MAR 2028"]
s1 = strips(b)[1]
s1['bubbles'][0]['text'] = "Small rewrite, benefit at the end: right only when no half-way step exists."
s1['bubbles'][1]['text'] = "It goes before item 3: the date is close and the work is small."
s2 = strips(b)[2]
s2['labels'] = ["CLOSE DATES FIRST, BY DATE", "REST: COST REMOVED PER EFFORT", "SUCCESSOR TEST BY 15 JANUARY"]
s2['bubbles'][0]['text'] = "Same rule, longer fuse: the successor model is tested by 15 January."
s2['bubbles'][1]['text'] = "Ten weeks before retirement, with a fallback if it fails: people confirm each sort."
b['caption'] = ("A migration moves software from one platform or vendor to another. The reporting stack, the software that produces "
  "customer reports, sits on a framework version, the reusable software it is built on, that has been unsupported since March 2027, "
  "and the largest prospect's security review requires supported components by the end of March 2028. The supported version builds "
  "reports differently, so there is no useful half-way state: its migration is a small rewrite with the benefit at the end, the one "
  "shape in which that is right. It goes first, ahead of the scheduling engine whose carrying cost is larger, because its date is "
  "close and its work is small: six engineer-weeks, one person working one week each, and €5,000 of cash. The rule has two parts: "
  "items whose external date is closer than the work needs go first, in date order; the rest are ordered by the carrying cost each "
  "stage of effort would remove, across all three columns. The vendor has named the successor to the retiring AI model; Larkspur "
  "tests it on its release samples by 15 January 2028, about ten weeks before the retirement. If it fails, a decision is due within "
  "sixty days, and the fallback is a review mode in which a person confirms every classification the model proposes.")
b['alt'] = ("Comic page in three strips: a timeline marks patches ended 31 March 2027, security review by March 2028, and model retires "
  "31 March 2028; a card reads reporting stack migration, six engineer-weeks and €5,000 cash, November to December 2027, and Ines says "
  "it goes before item 3 because the date is close and the work is small; a whiteboard gives the sequencing rule, close dates first by "
  "date, rest by cost removed per effort, successor test by 15 January.")

# ---- page 6
m, b = blocks['06-the-decision-and-the-gate']
s0 = strips(b)[0]
s0['bubbles'][1]['text'] = "Tranche 2 is a conditional line, released only on the gate's evidence."
s1 = strips(b)[1]
s1['labels'] = ["GATE FOR TRANCHE 2", "READ 31 MARCH 2028", "FAILOVER UNDER 5 MINUTES", "HOSTING DOWN €1,500 A MONTH",
                "NO INCIDENT FROM THE SPLIT", "LEAD TIME NO WORSE"]
s1['bubbles'][0]['text'] = "Live by 29 February, one month observed. All four pass together, or none."
s1['bubbles'][1]['text'] = "Any miss blocks tranche 2 until every condition is read again and passes."
s2 = strips(b)[2]
s2['labels'] = ["PORTAL REDESIGN: APRIL, NOT JANUARY", "TRANCHE 1 ENGINEERS: NAMED", "INVOICING SPECIALISTS: NOT INVOLVED"]
s2['bubbles'][0]['text'] = "The two portal engineers do the migration, then tranche 1. Their redesign starts April."
b['caption'] = ("Ines, the chief executive, may approve spending inside the plan the board has adopted and below a limit the board set; "
  "that is her delegation. She authorizes the reporting-stack migration and the January model test under it. Tranche 1 of the engine, "
  "€8,000 of cash and two named engineers for a quarter, is requested in the 2028 plan the board approves in January; tranche 2 is "
  "requested in the same plan as a conditional line that Ines may release only against the gate's evidence, which the board sees in "
  "April. A rewrite at €340,000 would have been outside any approved plan, so a board decision on its own. The split goes live by 29 "
  "February 2028, March is one month of live operation, and the gate is read on 31 March: all four conditions must pass at the same "
  "reading, any unmet condition blocks tranche 2 until every condition is re-read and passes, and an incident means fixing its cause "
  "and observing one further clean month. Lead time no worse is a safeguard, not a gain. The two engineers named for the customer "
  "portal redesign, the rebuild of the website customers use, spend six engineer-weeks on the migration in November and December and "
  "build tranche 1 from January to March; the redesign, originally January to March, starts in April, and its owner is told so.")
b['alt'] = ("Comic page in three strips: Ines signs a decision sheet reading stack November to December 2027, then engine tranche 1, "
  "January to March 2028 with €8,000 cash, rejected rewrite at €340,000, and Alex says tranche 2 is a conditional line released only on "
  "the gate's evidence; a whiteboard states the gate for tranche 2, read 31 March 2028, failover under five minutes, hosting down €1,500 a "
  "month, no incident from the split, lead time no worse, while Alex says the split is live by 29 February with one month observed and all "
  "four must pass together; three cards read portal redesign April not January, tranche 1 engineers named, invoicing specialists not involved.")

# ---- page 7
m, b = blocks['07-carried-on-purpose']
s1 = strips(b)[1]
s1['labels'] = ["5 ITEMS, ABOUT €10,000 MONTHLY", "INCIDENTS: INVOICING AND ENGINE", "€12,000 A MONTH NOT WON"]
s1['bubbles'][1]['text'] = "Five items: about €10,000 a month, incidents from two of them, €12,000 not won."
s2 = strips(b)[2]
s2['scene'] = ("On a table stand exactly two upright cards side by side with a clear gap, each with a heading and one line of lettering "
               "facing the reader; they are the only props on the table. Morgan, at the left of the table, looks at the cards. Alex, at "
               "the right of the table, gestures at the second card with an open hand. Nothing covers the lettering.")
s2['labels'] = ["REWRITE, BENEFIT MONTH 9", "€300,000 TIME + €40,000 CASH", "TRANCHE 1, BENEFIT MONTH 3", "€50,000 TIME + €8,000 CASH"]
s2['label_notes'] = "The first two labels are the heading and line of the left card; the last two are the heading and line of the right card."
s2['bubbles'][1]['text'] = "Nine frozen months and nothing bought until month nine. Tranche 1: failover by March."
b['caption'] = ("Some debt is worth carrying, and saying so is honest. The invoicing module's remaining tangles cost about €3,000 a month "
  "of the company's own engineering time and two incidents a quarter, and removing them would take the two specialists the company can "
  "least spare; the item is carried with a written reason and a review date, which makes it a decision rather than neglect. Morgan's "
  "two questions are answered from the register and the tranche plan: five items on three columns, about €10,000 a month of which "
  "€5,500 is cash, incidents from the invoicing module and the engine, €12,000 a month of revenue not won; and a first tranche that "
  "buys failover by March for about €50,000 of staff time and €8,000 of cash, against a rewrite of about €300,000 of staff time and "
  "€40,000 of cash whose benefit arrives only at month nine.")
b['alt'] = ("Comic page in three strips: Ines holds a card reading carried, invoicing tangles, about €3,000 a month, review every quarter, "
  "and says some debt is worth carrying; Morgan asks how much technical debt Larkspur has and Alex answers with three cards, five items "
  "about €10,000 monthly, incidents from invoicing and engine, €12,000 a month not won; Morgan asks why not rewrite and two cards compare "
  "the rewrite, benefit at month nine, €300,000 of time plus €40,000 of cash, with tranche 1, benefit at month three, €50,000 of time "
  "plus €8,000 of cash.")

# ---- write back (last match first so offsets stay valid)
out = text
for pid, (m, b) in sorted(blocks.items(), key=lambda kv: -kv[1][0].start()):
    out = out[:m.start(1)] + json.dumps(b, ensure_ascii=False, indent=2) + out[m.end(1):]
# intro
out = out.replace("Seven pages show Larkspur answering with a register of five items, each with a monthly carrying cost in three columns, and funding the first fix in tranches released by measured gates, with one dated item going first and one item deliberately carried.",
 "Seven pages show Larkspur answering with a register of five items, each with a carrying cost in three columns, what it costs to keep each month, what risk it carries and what it slows, and funding the first fix in tranches, separately approved stages of work, each released by a gate, an agreed check that the previous stage worked, with one dated item going first and one item deliberately carried.")
P.write_text(out)
# word-limit check
for pid,(m,b) in blocks.items():
    for i,s in enumerate(b['strips']):
        for bb in s['bubbles']:
            assert len(bb['text'].split())<=14, (pid,i,bb['text'])
        for l in s['labels']:
            assert len(l.split())<=5, (pid,i,l)
print('comics.md blocks updated; limits ok')
