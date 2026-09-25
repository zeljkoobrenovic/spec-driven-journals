#!/usr/bin/env python3
"""Apply the 24 September 2026 round-5 review changes to the comic script of
26-manage-technical-debt: MTD-030/012 (page 5: test before signing, nothing to
terminate on a failure, fallback starts on the switch day), MTD-004 (page 6:
portal dates split), MTD-031 (every page's caption lists the words on its boards
and cards; the intro promises exactly that).
Run generate_comic_pages.py --render afterwards, then re-letter page 05's strip 3 bubble."""
import json, re
from pathlib import Path
P = Path(__file__).resolve().parents[1] / 'posts/26-manage-technical-debt/comics.md'
text = P.read_text()
pat = re.compile(r'<!-- comic-page\n(\{.*?\n\})\n-->', re.S)
blocks = {}
for m in pat.finditer(text):
    b = json.loads(m.group(1)); blocks[b['id']] = (m, b)

# ---- MTD-031: the words lettered on each page's boards and cards, in reading order per strip
BOARDS = {
  '01-two-questions-one-wrong-answer': [
    ['How much technical debt?', 'Why not rewrite?'],
    ['Issue count', 'Percent of code', 'Carrying cost per month'],
    ['Cost carried', 'Risk carried', 'Speed lost', 'Workaround hours, old hosting', 'Incidents, unsupported, retiring', 'Lead time, deals lost']],
  '02-five-items-four-origins': [
    ['1 Invoicing tangles', '2 Reporting stack, unsupported', '3 Scheduling engine, one server', '4 AI prompt in code', '5 Vendor model retiring'],
    ['Dated shortcut: revisit on date', 'Growth outran design: tranches', 'Ageing platform: by the date', 'Retiring vendor: by the date'],
    ['About €10,000 a month', '2 invoice incidents a quarter', 'Failover: 45 minutes', '€12,000 a month not won']],
  '03-present-the-fix-by-what-it-buys': [
    ['Revenue protected or enabled', 'Cost or risk removed', 'A decision kept open'],
    ['Before', 'After', 'Incidents per quarter', 'Failover time', 'Lead time'],
    ['2 prospects: €12,000 a month', '€4,000 hosting above need', '45-minute failover', 'Core replacement: kept open']],
  '04-rewrite-tranches-or-live-with-it': [
    ['A: Rewrite the engine', '€300,000 time, €40,000 cash', 'Benefit at month 9', 'B: Tranches with gates', 'Tranche 1: €50,000 time', '€8,000 cash, benefit month 3', 'C: Live with it', 'Cost continues'],
    ['Month 0', 'Month 3', 'Month 7', 'Month 9', 'Rewrite', 'Tranche 1: €58,000', 'Gate', 'Tranche 2: €80,000'],
    ['Rewrite, month 5:', '€180,000 gone, €160,000 to decide', 'Tranche 1 done:', '€58,000 spent, failover in hand']],
  '05-the-dated-item-goes-first': [
    ['Patches ended 31 Mar 2027', 'Security review: by March 2028', 'Model retires 31 Mar 2028'],
    ['Reporting stack migration', '6 engineer-weeks, €5,000 cash', 'November–December 2027'],
    ['Deadline risk vs harm now', 'Rest: most removed per effort', 'Successor samples by 29 October']],
  '06-the-decision-and-the-gate': [
    ['Decision: stack Nov–Dec 2027', 'Then engine tranche 1, Jan–Mar', '€50,000 time + €8,000 cash', 'Rejected: rewrite', '€300,000 time + €40,000 cash'],
    ['Gate for tranche 2', 'Read 31 March 2028', 'Failover under 5 minutes', 'Hosting down €1,500 a month', 'No incident from the split', 'Lead time no worse'],
    ['Portal redesign: April–June', 'August–October if tranche 2', 'Tranche 1 engineers: named', 'Invoicing specialists: not involved']],
  '07-carried-on-purpose': [
    ['Carried: invoicing tangles', 'About €3,000 a month', 'Review every quarter'],
    ['5 items, about €10,000 monthly', 'Incidents: invoicing and engine', '€12,000 a month not won'],
    ['Rewrite, benefit month 9', '€300,000 time + €40,000 cash', 'Tranche 1, benefit month 3', '€50,000 time + €8,000 cash']],
}
MARK = "Words on the boards and cards"

def boards_paragraph(page):
    rows = BOARDS[page['id']]
    for strip, row in zip(page['strips'], rows):
        # the transcription must say exactly what the block asks the artwork to letter
        assert [s.upper() for s in row] == [s.upper() for s in strip.get('labels', [])], (page['id'], row)
    parts = [f"Strip {n}: " + "; ".join(f"“{s}”" for s in row) + "." for n, row in enumerate(rows, start=1) if row]
    return f"*{MARK}.* " + " ".join(parts)

# ---- page 5 (MTD-030, MTD-012)
def edit_page5(b):
    paras = b['caption'].split("\n\n")
    if not paras[2].startswith("The vendor's notice of 30 September 2027 named"):
        return  # already applied
    # blocks['05-the-dated-item-goes-first']
    assert paras[2].startswith("The vendor's notice of 30 September 2027") and paras[3].startswith("After the retirement date")
    paras[2] = ("The vendor's notice of 30 September 2027 retires the artificial intelligence (AI) model that sorts customers' documents on 31 March 2028, names its successor and gives Larkspur usable access to it the same day. "
      "It arrives before Larkspur has signed its planned commitment, an agreement to make fixed monthly payments to the vendor through 2028 in return for a discount, which Ines is due to sign in November. "
      "So the test comes first. Alex runs the successor on the release-gate samples, the documents the feature had to sort correctly before release, by 29 October, and Ines signs only if it passes. "
      "If it fails, nothing is signed and no fixed payment is owed, and Larkspur chooses by 29 November between another vendor's model tested on the same samples and the failed successor. "
      "Had access come later, every date would move with it, and the choice would still be made by 31 January 2028.")
    new4 = ("The old model stays available until 31 March, but the switch is planned for February, leaving March to put right anything that goes wrong; what customers get changes on that switch day. "
      "A model that passed the samples keeps sorting automatically. A model that was tested and failed can carry the review mode from the trial: the feature proposes a category and each customer's own planner confirms it, with no new Larkspur staff. "
      "The mode still needs a model, and it starts only where Priya has confirmed that the planner has the time and has agreed the changed service and fee; other customers' sorting is suspended from the switch day.")
    new5 = ("If no model was tested at all, there is nothing to switch to: sorting is suspended for every customer on 31 March, with the changed service agreed beforehand, and documents go back to sorting by hand. "
      "Sam prices the chosen model's usage against the AI budget the board approved; anything beyond it needs the board.")
    paras[3:4] = [new4, new5]
    b['caption'] = "\n\n".join(paras)
    bub = b['strips'][2]['bubbles'][1]
    assert bub['who'] == 'Ines' and bub['text'].startswith('Fail, and Sam gives notice')
    bub['text'] = "Fail, and I sign nothing. We choose by 29 November, switch in February."
    old_alt = "and Ines says that if they fail Sam gives notice by 29 November and the old model runs until March."
    assert old_alt in b['alt']
    b['alt'] = b['alt'].replace(old_alt, "and Ines says that if they fail she signs nothing, a replacement is chosen by 29 November and the switch comes in February.")


# ---- page 6 (MTD-004, MTD-031): gate conditions in words; portal dates one step at a time
def edit_page6(b):
    paras = b['caption'].split("\n\n")
    if "it moves to April to June" in b["caption"]:
        return  # already applied
    # blocks['06-the-decision-and-the-gate']
    assert paras[2].startswith("The split goes live by 29 February 2028") and paras[3].startswith("The two engineers named")
    paras[2] = ("The split goes live by 29 February 2028, March is one month of live operation, and the gate is read on 31 March. Four conditions must all pass at that reading: "
      "a failover rehearsed in under five minutes; the March hosting bill at least €1,500 a month below the bill before the split; no incident caused by the split; and lead time, the working days from an agreed change to its delivery, no worse than before, a safeguard rather than a gain. "
      "Any unmet condition blocks tranche 2 until every condition is re-read and passes; an incident means fixing its cause and observing one further clean month.")
    paras[3:4] = [
      "The two engineers named for the customer portal redesign, the rebuild of the website customers use, spend six engineer-weeks on the migration in November and December, then build tranche 1 from January to March.",
      "The redesign was planned for January to March. If the work stops after tranche 1, it moves to April to June. If tranche 2 starts in April, it moves to August to October. It moves later still if approval or the gate slips, and its owner is told so."]
    b['caption'] = "\n\n".join(paras)


edit_page5(blocks['05-the-dated-item-goes-first'][1])
edit_page6(blocks['06-the-decision-and-the-gate'][1])

# ---- every page: append (or refresh) the boards-and-cards paragraph
for bid, (m, b) in blocks.items():
    paras = [p for p in b['caption'].split("\n\n") if not p.lstrip('*').startswith(MARK)]
    b['caption'] = "\n\n".join(paras + [boards_paragraph(b)])

for bid in sorted(blocks, key=lambda k: blocks[k][0].start(), reverse=True):
    m, b = blocks[bid]
    text = text[:m.start(1)] + json.dumps(b, ensure_ascii=False, indent=2) + text[m.end(1):]

# ---- intro promise (MTD-031)
old_intro = "tap or click any page to open it at full size, and the lines under each page repeat every word of its lettering."
text = text.replace(old_intro, "tap or click any page to open it at full size. Under each page, the caption ends with the words on its boards and cards, and the lines below repeat every speech bubble.")
P.write_text(text)
print('comics.md blocks updated')
