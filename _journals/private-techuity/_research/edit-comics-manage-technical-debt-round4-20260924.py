#!/usr/bin/env python3
"""Apply the 24 September 2026 round-4 review changes to the comic script of
27-manage-technical-debt (MTD-029 page 4 timeline; MTD-012/020 page 5 fallback caption).
Run generate_comic_pages.py --render afterwards, then correct page 04's artwork."""
import json, re
from pathlib import Path
P = Path(__file__).resolve().parents[1] / 'posts/27-manage-technical-debt/comics.md'
text = P.read_text()
pat = re.compile(r'<!-- comic-page\n(\{.*?\n\})\n-->', re.S)
blocks = {}
for m in pat.finditer(text):
    b = json.loads(m.group(1)); blocks[b['id']] = (m, b)

# ---- page 4 (MTD-029): one dated scale, each bar ending exactly at its month tick
m, b = blocks['04-rewrite-tranches-or-live-with-it']
s = b['strips'][1]
s['scene'] = ("A long horizontal timeline high on the wall, above everyone's heads, with exactly four tick marks in total, one tick directly under each of the four labels and no other tick anywhere. "
  "Above the line lies one long plain bar reaching exactly from the first tick to the fourth, with one small flag standing at its right end directly above the fourth tick. "
  "Below the line lie two shorter plain bars on one scale: the first runs exactly from the first tick to the second tick and ends in a small flag directly under the second tick, with a small closed barrier gate right beside that flag; "
  "the second starts at the second tick and ends exactly under the third tick, with a small flag standing directly under the third tick; no bar extends past its tick. "
  "Sam, at the left, and Alex, at the right, stand below the timeline and gesture up at it with open hands. No head, hand, marker or bubble covers the lettering.")
s['label_notes'] = ("The four MONTH labels sit over the four ticks, left to right; REWRITE is lettered on the long upper bar; TRANCHE 1: €58,000 on the first lower bar, GATE beside the barrier at month 3, "
  "TRANCHE 2: €80,000 on the second lower bar, which ends at the MONTH 7 tick.")
b['alt'] = ("Comic page in three strips: three cards compare A, rewrite the engine, €300,000 of staff time and €40,000 of cash with the benefit at month nine, B, tranches with gates, "
  "tranche 1 at €50,000 of time plus €8,000 of cash with failover at month three, and C, live with it, cost continues; a timeline with ticks at months 0, 3, 7 and 9 shows one long rewrite bar "
  "ending in a single flag at month 9, against a tranche 1 bar labelled €58,000 ending in a flag at month 3 with a gate beside it, and a tranche 2 bar labelled €80,000 running from month 3 to a flag at month 7; "
  "a whiteboard reads rewrite month 5, €180,000 gone and €160,000 to decide, against tranche 1 done, €58,000 spent and failover in hand.")

# ---- page 5 (MTD-020, MTD-012): notice versus effect; three fallback branches
m, b = blocks['05-the-dated-item-goes-first']
paras = b['caption'].split("\n\n")
assert paras[2].startswith("The vendor's notice of 30 September 2027") and paras[3].startswith("The fallback is the review mode")
paras[2] = paras[2].replace(
  "So Alex runs the samples by 29 October, and on a failure Sam gives the notice by 29 November, whatever replacement is chosen;",
  "So Alex runs the samples by 29 October, and on a failure Sam gives the notice by 29 November, whatever replacement is chosen. The notice does not stop the payments at once: the commitment ends on the 31 March 2028 retirement date, and every payment up to then stays owed.")
paras[2] = paras[2].replace(" The old model runs until the 31 March 2028 retirement, so nothing changes for customers before then.",
  " The old model runs until the retirement date, so nothing changes for customers before then.")
paras[2] = paras[2].replace("Larkspur's own decision between the successor, another vendor's model and the fallback falls on the same date.",
  "Larkspur's own decision between another vendor's model and the fallback falls on the same date.")
assert "every payment up to then stays owed" in paras[2]
paras[3] = ("After the retirement date, what the feature runs on depends on what was tested. A model that passed the samples keeps sorting automatically. "
  "A model that was tested and failed can carry the review mode from the trial: the feature proposes a category and each customer's own planner confirms it, with no new Larkspur staff. "
  "The mode still needs a model; it starts customer by customer, and only where Priya has confirmed that the planner has the time and has agreed the changed service and fee. "
  "If no model was tested at all, or a customer's planner has no time, that customer's sorting is suspended and documents go back to sorting by hand, agreed with the customer that day. "
  "Sam prices the chosen model's usage, which is at list price once the commitment ends, against the AI budget the board approved.")
b['caption'] = "\n\n".join(paras)

for bid in sorted(blocks, key=lambda k: blocks[k][0].start(), reverse=True):
    m, b = blocks[bid]
    text = text[:m.start(1)] + json.dumps(b, ensure_ascii=False, indent=2) + text[m.end(1):]
P.write_text(text)
print('comics.md blocks updated')
