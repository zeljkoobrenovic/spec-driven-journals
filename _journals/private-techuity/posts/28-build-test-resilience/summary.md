**A backup that has never been restored is a hope, not evidence.** Write down what must keep working, test that the service really comes back, fund the fixes, and record what remains exposed.

![A dispatcher at a blank screen at 6am beside waiting vans, and a recovery objective of four hours and fifteen minutes; a timeline where the day-45 test takes eleven hours, blocked by a lost key and an old database and returning night-old data, then a €20K fix and a day-85 retest that passes; a card marking the whole region as still exposed and a calendar for a quarterly retest.](assets/images/28-build-test-resilience/summary-at-a-glance.jpeg)
**Figure 1:** *From the objective a dispatcher would recognise, through a failed restore and a funded fix, to a passed retest and the risk still accepted on purpose.*

At six in the morning a dispatcher at one of Larkspur’s customers opens the scheduling service, and it doesn’t load. Twenty engineers wait in their vans. What evidence does Larkspur, the book’s fictional company, have that dispatch would resume, and how soon?

Start with the business function, not the systems. Larkspur writes its **recovery objective** in words a dispatcher would recognise: if Larkspur loses its own systems, dispatch must resume within four hours, with no more than fifteen minutes of schedule updates lost. Four hours is the longest a morning’s dispatch can slip before the day is lost; fifteen minutes is what a dispatcher can re-enter from memory. The objective does not cover losing the cloud provider’s whole region, and says so.

Before the investment, specialists found that Larkspur’s backups had run without error for three years, but nobody had ever tried a full restore. The hundred-day plan funded a test at €80,000 and four engineer-weeks. On day 45 it took eleven hours instead of four. The only account that could read the backups belonged to an engineer who had left, and the backups loaded only into an old version of the database software, found on a retired machine and installed by hand. The data came back a night old. **Backups running is evidence about backups; restoring the service is evidence about the business.**

The budget was spent; the promise to customers remained. Alex, who leads technology, costed a repeatable version of each improvised fix at €20,000 and two engineer-weeks: a test environment kept on the live service’s software version, emergency access that two named people can use, and a written rehearsal the operations lead can run alone. The money came from the plan’s reserve, which only the board can release, and the board approved it.

A risk calculation can support such a decision, but it is not a profit. A 5% yearly chance of a €4 million outage implies an average loss of €200,000 a year; cutting the chance to an assumed 2% lowers it to €80,000. That €120,000 difference is a modelled reduction in exposure, never money in the accounts.

The retest on day 85 met the objective. A passed test changes the exposure; it does not remove it. Larkspur records what the test did not cover: losing the whole region, a rehearsal during the busy dispatch hours, and only two people able to run the emergency access procedure. Ines, the chief executive, **accepts that residual risk** on the board’s behalf, with a quarterly retest and about two days of the operations lead’s time protected for it each quarter.

Recovery is judged by a test the company can watch. The next chapter, [[evaluate-cloud-costs]], turns to spending it can see every month on the bill.
