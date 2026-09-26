#!/usr/bin/env python3
"""Apply the 24 September 2026 round-3 review text changes to the comic script of
27-manage-technical-debt (MTD-004/005/012/013/020/024).
Edits the comic-page JSON blocks in place (captions split into short paragraphs); run
generate_comic_pages.py --render afterwards, then --retext for page 02 and --generate --overwrite for page 05."""
import json, re
from pathlib import Path
P = Path(__file__).resolve().parents[1] / 'posts/27-manage-technical-debt/comics.md'
text = P.read_text()
pat = re.compile(r'<!-- comic-page\n(\{.*?\n\})\n-->', re.S)
blocks = {}
for m in pat.finditer(text):
    b = json.loads(m.group(1)); blocks[b['id']] = (m, b)

# ---- page 1 (MTD-004: split the caption)
m, b = blocks['01-two-questions-one-wrong-answer']
b['caption'] = (
  "Every amount and date in this comic is invented for the example. Larkspur is a fictional company that sells scheduling software; an investor owns a large stake in it, and the board is the group of directors that oversees the company. Morgan advises the investor; Alex leads technology; Priya leads product.\n\n"
  "Technical debt is the extra cost a company carries because its software was built, or has aged, in ways that make it slower, riskier or dearer to change than it needs to be; the word is a metaphor, not a loan. A carrying cost is what an item costs the company while it remains, in three columns: cost carried (euros per month), risk carried (service failures, unsupported parts, dated retirements) and speed lost (lead time, the working days from an agreed change to its delivery, and deals the product cannot take). The last two keep their own units and are read alongside the money, not added to it.")

# ---- page 2 (MTD-024, MTD-013, MTD-004)
m, b = blocks['02-five-items-four-origins']
s1 = b['strips'][1]
assert s1['bubbles'][1]['text'] == "An undated one is. A close date nobody inside chose goes first."
s1['bubbles'][1]['text'] = "Undated shortcuts are failures of record. Outside dates are weighed against harm now."
b['caption'] = (
  "Larkspur's register has five items; they are the board's shortlist, and a longer register sits behind them. Item 1 is the invoicing module, the software that prepares customer bills, whose code is still tangled so that parts cannot change alone. Item 2 is the reporting stack on a version its vendor no longer fixes security holes in. Item 3 is the scheduling engine, which runs each region on one server. Item 4 is the artificial intelligence (AI) sorting feature: the prompt, the instructions sent to the AI model that sorts customers' documents, is written into the program, so every change to it needs a software release. Item 5 is the vendor retiring the AI model that feature runs on.\n\n"
  "The origin of each decides who owns it and what the remedy usually is. A deliberate shortcut recorded with a date and an owner is not a failure of record, though the record makes it accountable, not necessarily wise; an undated one is a failure. A tranche is a separately approved stage of work, so growth that outran a design is fixed in tranches. A date set from outside the company, by a vendor or a prospect, is weighed first: what missing it would cost against the harm undated items are doing now, so a close date with little time to spare goes first, and a distant date with little work behind it can wait.\n\n"
  "Carried, the five cost about €10,000 a month: €5,500 of cash paid to hosting providers, the companies whose servers run the software, and about €4,600 of the company's own engineering time, already on the payroll and valued at what it costs to employ the engineers. The invoicing tangles cause two customer-visible incidents a quarter, and the scheduling engine caused the year's last two incidents and takes 45 minutes to fail over, that is, to move its work to a replacement server. Its single-server design also turns away prospects, potential customers, above about 400 technicians: two this year, about €12,000 a month of revenue (sales income) not won. Sam leads finance.")
b['alt'] = ("Comic page in three strips: five cards on a pinboard read invoicing tangles, reporting stack unsupported, scheduling engine one server, AI prompt in code, "
  "and vendor model retiring, and Alex calls them the board's shortlist over a longer register; a whiteboard pairs each origin with its remedy, dated shortcut revisit on date, "
  "growth outran design tranches, ageing platform and retiring vendor by the date, while Priya calls her dated shortcut accountable but not necessarily wise and Alex says undated shortcuts are failures of record and outside dates are weighed against harm now; "
  "a second whiteboard totals the register at about €10,000 a month, two invoice incidents a quarter, a 45-minute failover and €12,000 a month not won.")

# ---- page 3 (MTD-004: split the caption)
m, b = blocks['03-present-the-fix-by-what-it-buys']
b['caption'] = b['caption'].replace(" The board rarely sees the failures a fix prevented,", "\n\nThe board rarely sees the failures a fix prevented,").replace(" For the engine, a failover,", "\n\nFor the engine, a failover,")
assert b['caption'].count("\n\n") == 2

# ---- page 4 (MTD-004: split the caption)
m, b = blocks['04-rewrite-tranches-or-live-with-it']
b['caption'] = b['caption'].replace(" A tranche is a separately approved stage of the work;", "\n\nA tranche is a separately approved stage of the work;").replace(" Money already spent is gone the moment it is spent,", "\n\nMoney already spent is gone the moment it is spent,")
assert b['caption'].count("\n\n") == 2

# ---- page 5 (MTD-020, MTD-012, MTD-013, MTD-005)
m, b = blocks['05-the-dated-item-goes-first']
b['title'] = "A close date, weighed and put first"
s2 = b['strips'][2]
s2['labels'] = ["DEADLINE RISK VS HARM NOW", "REST: MOST REMOVED PER EFFORT", "SUCCESSOR SAMPLES BY 29 OCTOBER"]
s2['bubbles'][0]['text'] = "Same rule, longer fuse: Alex runs the samples on the successor by 29 October."
s2['bubbles'][1]['text'] = "Fail, and Sam gives notice by 29 November. The old model runs until March."
b['alt'] = ("Comic page in three strips: a timeline marks patches ended 31 March 2027, security review by March 2028, and model retires 31 March 2028; a card reads reporting stack migration, six engineer-weeks and €5,000 cash, November to December 2027, and Ines says it goes before item 3 because the date is close and the work is small; a whiteboard gives the sequencing rule, deadline risk versus harm now, the rest by most removed per effort, successor samples by 29 October, and Ines says that if they fail Sam gives notice by 29 November and the old model runs until March.")
b['caption'] = (
  "A migration moves software from one platform or vendor to another. The reporting stack, the software that produces customer reports, sits on a framework version, the reusable software it is built on, whose vendor stopped fixing its security holes in March 2027, and the largest prospect's security review requires supported components by the end of March 2028. The supported version builds reports differently, so there is no useful half-way state: its migration is a small rewrite with the benefit at the end, the one shape in which that is right. It goes first, ahead of the scheduling engine whose carrying cost is larger, because its date is close and its work is small: six engineer-weeks, six weeks of one engineer's time or three weeks each for two, and €5,000 of cash.\n\n"
  "The rule has two parts. An item whose outside date leaves little more time than the work needs, with a margin for overrun, is weighed first: what missing the date would cost against the harm undated items are doing now; items brought forward go in date order, and a distant date with little work behind it can wait behind an undated item doing harm now. The rest are ordered by the cost, risk and delay each stage of effort would remove, across all three columns.\n\n"
  "The vendor's notice of 30 September 2027 named the successor to the retiring artificial intelligence (AI) model and gave Larkspur usable access to it the same day. The contract lets Larkspur test the successor on its release-gate samples, the documents the feature had to sort correctly before release, and, if they fail, end the commitment, its agreement to make fixed monthly payments through 2028, by giving notice within sixty days of access. So Alex runs the samples by 29 October, and on a failure Sam gives the notice by 29 November, whatever replacement is chosen; Larkspur's own decision between the successor, another vendor's model and the fallback falls on the same date. Had access come later, every date would move with it. The old model runs until the 31 March 2028 retirement, so nothing changes for customers before then.\n\n"
  "The fallback is the review mode from the trial: the feature proposes a category and each customer's own planner confirms it, with no new Larkspur staff. It starts, customer by customer, only when the feature moves to a model that has not passed the samples, at the latest on the retirement date, and only where Priya has confirmed that the customer's planner has the time and has agreed the changed service and fee. Where no model is usable or no planner has the time, that customer's sorting is suspended and documents go back to sorting by hand, agreed with the customer that day.")

# ---- page 6 (MTD-020: October test; MTD-004: split the caption)
m, b = blocks['06-the-decision-and-the-gate']
assert "the November model test" in b['caption']
b['caption'] = b['caption'].replace("the November model test", "the October model test")
b['caption'] = b['caption'].replace(" The rejected rewrite is priced on the same basis,", "\n\nThe rejected rewrite is priced on the same basis,").replace(" The split goes live by 29 February 2028,", "\n\nThe split goes live by 29 February 2028,").replace(" The two engineers named for the customer portal redesign,", "\n\nThe two engineers named for the customer portal redesign,")
assert b['caption'].count("\n\n") == 3

# ---- page 7 (MTD-004: split the caption)
m, b = blocks['07-carried-on-purpose']
b['caption'] = b['caption'].replace(" Morgan's two questions are answered", "\n\nMorgan's two questions are answered")
assert b['caption'].count("\n\n") == 1

# write back, last block first so offsets stay valid
for bid in sorted(blocks, key=lambda k: blocks[k][0].start(), reverse=True):
    m, b = blocks[bid]
    text = text[:m.start(1)] + json.dumps(b, ensure_ascii=False, indent=2) + text[m.end(1):]
P.write_text(text)
print('comics.md blocks updated')
