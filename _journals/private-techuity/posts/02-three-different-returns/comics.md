<!-- comic-style
{
  "cast": "MORGAN: a thoughtful investor technology adviser with short dark hair and a green jacket, used in the fund scenarios. ALEX: a practical CTO with curly hair and blue rolled-up sleeves. SAM: a CFO with round glasses and an amber cardigan. PRIYA: a product leader with straight dark hair and plum sleeves. INES: a CEO with short grey hair and a navy jacket. All are fictional; none represents a person in a real case.",
  "style": "Clean editorial explainer comic, dark ink outlines, restrained green, blue, and amber accents on warm white, generous space, readable short speech bubbles, expressive people and simple physical metaphors. No photorealism, logos, dense charts, or title text. Keep the same character appearances throughout the journal."
}
-->

**Comic.** Leaders inside the company judge progress by customers and earnings; an investor judges the same company by the return on its holding. The panels follow one fictional **buyout**: a **fund**, a pool of investors’ money run by a manager, buys a controlling share of a company using its own money plus borrowed money.

The company’s performance is measured by **EBITDA**, earnings before interest, taxes, depreciation and amortization: operating earnings before borrowing costs, income taxes and the accounting charges that spread the cost of equipment and similar assets over years. It is an earnings measure, not cash in hand. A buyer prices the business as a **multiple** of EBITDA (10× means €10 of price per €1 of annual EBITDA), and the lenders are repaid out of that price before the fund, as owner, receives what is left.

The panels hold the company’s performance completely fixed, EBITDA up from €10m to €15m and debt down from €60m to €40m (the repayment is a separate assumption about cash left after necessary spending), and show three investor outcomes that differ only in the price a buyer pays. The “about x% a year” figures are compounded annual rates for one investment paid in and one sale receipt five years later; the simplified example has no investor payments in between and ignores fees and taxes on the sale. Then the panels show why a sale result cannot say how much engineering contributed.

Morgan is an investor’s adviser in the fund scenarios; Alex leads technology, Priya leads product, and Sam leads finance. All are fictional. Comparative scenarios use separate assumptions. Historical cases are discussed through documents; the scenes do not reenact real events.

<!-- comic-panel
{
  "id": "01-scene",
  "status": "generated",
  "asset": "assets/images/02-three-different-returns/comic-01-scene.jpeg",
  "aspect_ratio": "16:9",
  "prompt": "Panel 1 of an explainer comic. Morgan places a business model beside a share certificate. Use one speech bubble with the exact words: \"Company value and equity differ.\" Convey: Fictional buyout: the fund pays €100m for a business earning €10m of EBITDA, €60m borrowed and €40m of its own. Five years later EBITDA is €15m and debt is €40m. What the business is worth and what the fund gets are different amounts, because the lenders are repaid first; the fund’s share of what remains is its equity.",
  "alt": "Comic panel: Morgan holds a company folder and a separate equity certificate.",
  "caption": "Fictional buyout: the fund pays €100m for a business earning €10m of EBITDA, €60m borrowed and €40m of its own. Five years later EBITDA is €15m and debt is €40m. What the business is worth and what the fund gets are different amounts, because the lenders are repaid first; the fund’s share of what remains is its equity.",
  "generation": {
    "model": "gemini-3-pro-image-preview",
    "reference_id": "owned-cast-20260913",
    "sha256": "59fd4db0497298adb6145f37e768acbfc6820f15e5ac2000bd7038fdbec94790"
  }
}
-->

![Comic panel: Morgan holds a company folder and a separate equity certificate.](assets/images/02-three-different-returns/comic-01-scene.jpeg)

**Panel 1:** Fictional buyout: the fund pays €100m for a business earning €10m of EBITDA, €60m borrowed and €40m of its own. Five years later EBITDA is €15m and debt is €40m. What the business is worth and what the fund gets are different amounts, because the lenders are repaid first; the fund’s share of what remains is its equity.

*Dialogue:* “Company value and equity differ.”

<!-- comic-panel
{
  "id": "02-scene",
  "status": "generated",
  "asset": "assets/images/02-three-different-returns/comic-02-scene.jpeg",
  "aspect_ratio": "16:9",
  "prompt": "Panel 2 of an explainer comic. Sam, who has a full head of short brown hair (not bald) and round glasses, holds a price tag marked 10× and stands beside one framed chart on an easel. Inside the frame, on the left, a single straight dark line rising steadily from lower left to upper right with the label EARNINGS written once above it; on the right, exactly five plain dark navy bars of equal width that get shorter step by step from left to right, with the label DEBT written once above them. Count the bars: five. No other labels, no numbers, no repeated words, no colors on the bars. Alex looks on, facing the viewer. Use one speech bubble with the exact words: \"Ten times: one hundred and ten million.\" Convey: Outcome one. A buyer pays the same 10× multiple: €15m × 10 = €150m, less €40m of debt. The fund receives €110m, 2.75 times its €40m, about 22% a year. Earnings up, debt down, price per euro unchanged.",
  "alt": "Comic panel: Sam holds a 10× price tag beside a chart with a rising earnings line and shrinking debt bars, while Alex looks on.",
  "caption": "Outcome one. A buyer pays the same 10× multiple: €15m × 10 = €150m, less €40m of debt. The fund receives €110m, 2.75 times its €40m, about 22% a year. Earnings up, debt down, price per euro unchanged.",
  "generation": {
    "model": "gemini-3-pro-image-preview",
    "reference_id": "owned-cast-20260913",
    "sha256": "65134fc65a33c72c39ca65e9ffec1af6349305ca7b79b5f187277a331bbeec01"
  }
}
-->

![Comic panel: Sam holds a 10× price tag beside a chart with a rising earnings line and shrinking debt bars, while Alex looks on.](assets/images/02-three-different-returns/comic-02-scene.jpeg)

**Panel 2:** Outcome one. A buyer pays the same 10× multiple: €15m × 10 = €150m, less €40m of debt. The fund receives €110m, 2.75 times its €40m, about 22% a year. Earnings up, debt down, price per euro unchanged.

*Dialogue:* “Ten times: one hundred and ten million.”

<!-- comic-panel
{
  "id": "03-scene",
  "status": "generated",
  "asset": "assets/images/02-three-different-returns/comic-03-scene.jpeg",
  "aspect_ratio": "16:9",
  "prompt": "Panel 3 of an explainer comic. Alex proudly holds a plain blank report and Sam, with his short brown hair and round glasses, holds a larger price tag marked 12×; between them stands one framed chart on an easel. Inside the frame, on the left, a single straight line rising steadily from lower left to upper right with the label EARNINGS written once above it; on the right, exactly five plain bars that get shorter step by step from left to right with the label DEBT written once above them. No other labels, no numbers, no repeated words. Use one speech bubble with the exact words: \"Twelve times. Same team, same numbers.\" Convey: Outcome two. Same EBITDA, same debt, but a buyer pays 12×: €180m less €40m. The fund receives €140m, 3.5 times its money, about 28% a year. Calling this proof of exceptional engineering confuses the exit price with the company’s work.",
  "alt": "Comic panel: Alex proudly holds a report beside the same chart with a rising earnings line and shrinking debt bars, while Sam holds a larger 12× price tag.",
  "caption": "Outcome two. Same EBITDA, same debt, but a buyer pays 12×: €180m less €40m. The fund receives €140m, 3.5 times its money, about 28% a year. Calling this proof of exceptional engineering confuses the exit price with the company’s work.",
  "generation": {
    "model": "gemini-3-pro-image-preview",
    "reference_id": "owned-cast-20260913",
    "sha256": "2cf7e97a8950650240ec936734d142156a8fa746e70af6419b38d95227d0fa52"
  }
}
-->

![Comic panel: Alex proudly holds a report beside the same chart with a rising earnings line and shrinking debt bars, while Sam holds a larger 12× price tag.](assets/images/02-three-different-returns/comic-03-scene.jpeg)

**Panel 3:** Outcome two. Same EBITDA, same debt, but a buyer pays 12×: €180m less €40m. The fund receives €140m, 3.5 times its money, about 28% a year. Calling this proof of exceptional engineering confuses the exit price with the company’s work.

*Dialogue:* “Twelve times. Same team, same numbers.”

<!-- comic-panel
{
  "id": "04-scene",
  "status": "generated",
  "asset": "assets/images/02-three-different-returns/comic-04-scene.jpeg",
  "aspect_ratio": "16:9",
  "prompt": "Panel 4 of an explainer comic. Sam, who has a full head of short brown hair (not bald, not shaved) and round glasses, holds a smaller price tag marked 7×, and Alex, facing the viewer, looks puzzled at one framed chart on an easel. Inside the frame, on the left, a single straight dark line rising steadily from lower left to upper right with the label EARNINGS written once above it; on the right, exactly five plain dark navy bars of equal width that get shorter step by step from left to right, with the label DEBT written once above them. Count the bars: five. No other labels, no numbers, no repeated words, no colors on the bars. Use one speech bubble with the exact words: \"Seven times. Same team, same numbers.\" Convey: Outcome three. Same EBITDA, same debt, but a buyer pays only 7×: €105m less €40m. The fund receives €65m, 1.6 times its money, about 10% a year. Calling this a failed transformation confuses the exit price with the company’s work.",
  "alt": "Comic panel: Sam holds a smaller 7× price tag beside the same chart with a rising earnings line and shrinking debt bars, while Alex looks at the unchanged chart, puzzled.",
  "caption": "Outcome three. Same EBITDA, same debt, but a buyer pays only 7×: €105m less €40m. The fund receives €65m, 1.6 times its money, about 10% a year. Calling this a failed transformation confuses the exit price with the company’s work.",
  "generation": {
    "model": "gemini-3-pro-image-preview",
    "reference_id": "owned-cast-20260913",
    "sha256": "375a027cfa4174e363ab5d1a1b1817b17a76643abc9d0a4547d77cb80c7e38f4"
  }
}
-->

![Comic panel: Sam holds a smaller 7× price tag beside the same chart with a rising earnings line and shrinking debt bars, while Alex looks at the unchanged chart, puzzled.](assets/images/02-three-different-returns/comic-04-scene.jpeg)

**Panel 4:** Outcome three. Same EBITDA, same debt, but a buyer pays only 7×: €105m less €40m. The fund receives €65m, 1.6 times its money, about 10% a year. Calling this a failed transformation confuses the exit price with the company’s work.

*Dialogue:* “Seven times. Same team, same numbers.”

<!-- comic-panel
{
  "id": "05-scene",
  "status": "generated",
  "asset": "assets/images/02-three-different-returns/comic-05-scene.jpeg",
  "aspect_ratio": "16:9",
  "prompt": "Panel 5 of an explainer comic. Sam starts a new worksheet labelled Minority example, apart from the earlier buyout calculation, while Alex counts share blocks. Use one speech bubble with the exact words: \"New funding can change the percentage.\" Convey: Separate fictional minority example: an investor holds 200 of Larkspur’s 1,000 shares, 20%. The company then sells 250 new shares to another investor while the first investor keeps its 200, so the total is 1,250 and the first investor’s holding falls to 16%. With equal rights to the sale proceeds, €20m of proceeds gives this investor €3.2m.",
  "alt": "Comic panel: Sam starts a new worksheet labelled Minority example, apart from the earlier buyout calculation, while Alex counts share blocks.",
  "caption": "Separate fictional minority example: an investor holds 200 of Larkspur’s 1,000 shares, 20%. The company then sells 250 new shares to another investor while the first investor keeps its 200, so the total is 1,250 and the first investor’s holding falls to 16%. With equal rights to the sale proceeds, €20m of proceeds gives this investor €3.2m.",
  "generation": {
    "model": "gemini-3-pro-image-preview",
    "reference_id": "owned-cast-20260913",
    "sha256": "56f8700a539e19790d2bea218b6a423a6cf91b89cd8da873e14c2909d747079b"
  }
}
-->

![Comic panel: Sam starts a new worksheet labelled Minority example, apart from the earlier buyout calculation, while Alex counts share blocks.](assets/images/02-three-different-returns/comic-05-scene.jpeg)

**Panel 5:** Separate fictional minority example: an investor holds 200 of Larkspur’s 1,000 shares, 20%. The company then sells 250 new shares to another investor while the first investor keeps its 200, so the total is 1,250 and the first investor’s holding falls to 16%. With equal rights to the sale proceeds, €20m of proceeds gives this investor €3.2m.

*Dialogue:* “New funding can change the percentage.”

<!-- comic-panel
{
  "id": "06-scene",
  "status": "generated",
  "asset": "assets/images/02-three-different-returns/comic-06-scene.jpeg",
  "aspect_ratio": "16:9",
  "prompt": "Panel 6 of an explainer comic. Alex tests the plan beneath a lower valuation sign. Use one speech bubble with the exact words: \"Does the business still improve?\" Convey: A sale price cannot say how much engineering contributed to earnings. Gather that evidence on the way, and test whether an improvement still pays if the sale price is lower or the owner holds the business longer.",
  "alt": "Comic panel: Alex tests the plan beneath a lower valuation sign.",
  "caption": "A sale price cannot say how much engineering contributed to earnings. Gather that evidence on the way, and test whether an improvement still pays if the sale price is lower or the owner holds the business longer.",
  "generation": {
    "model": "gemini-3-pro-image-preview",
    "reference_id": "owned-cast-20260913",
    "sha256": "87683dc57dd3822d65b2a81add19fdee63e8d8cab3ded94b6578844d5e911b99"
  }
}
-->

![Comic panel: Alex tests the plan beneath a lower valuation sign.](assets/images/02-three-different-returns/comic-06-scene.jpeg)

**Panel 6:** A sale price cannot say how much engineering contributed to earnings. Gather that evidence on the way, and test whether an improvement still pays if the sale price is lower or the owner holds the business longer.

*Dialogue:* “Does the business still improve?”
