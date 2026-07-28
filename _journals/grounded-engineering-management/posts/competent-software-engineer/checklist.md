---
timetoread: "6 min read"
---
*The working checklist behind this record — the one I hand the engineer, written in their voice. The Article tab carries the rationale and anti-patterns.*

## 1. Prioritize work

- [ ] I identify the single most important task or project each week
- [ ] I confirm my priority with my manager or team when unsure
- [ ] I deliver the top priority within the agreed timeframe
- [ ] I say "no" or renegotiate when lower-priority work threatens the top priority
- [ ] I communicate tradeoffs clearly when asked to take on extra work

## 2. Unblock yourself

- [ ] I notice when I am blocked, rather than continuing without making progress
- [ ] I use a rule of thumb: no meaningful progress after 30–60 minutes means I am blocked
- [ ] I try different approaches before asking for help: rubber-duck the problem, draw it on paper, read documentation, search online or internal resources, ask a Q&A forum or channel, use AI tools carefully and verify the answer, take a short break, or start from scratch / undo recent changes
- [ ] I ask teammates for help when needed, explaining what I already tried
- [ ] I escalate politely when blocked by another person, and preserve the relationship

## 3. Break down work

- [ ] I split large projects into epics, stories, tasks, and subtasks
- [ ] I break tasks down until each one is clear and actionable
- [ ] I identify the "golden path" or smallest useful implementation
- [ ] I separate edge cases into their own tasks
- [ ] I prioritize work that gets me closer to something shippable
- [ ] I add, remove, or revise tasks as I learn more
- [ ] I avoid spending more time managing tasks than doing the work

## 4. Estimate work

- [ ] I estimate using similar past work when possible
- [ ] I ask teammates for examples when doing something new
- [ ] I identify what is known, unknown, and risky
- [ ] I prototype before estimating unfamiliar systems or technologies
- [ ] I break work apart so each task contains fewer unknowns
- [ ] I provide worst-case estimates when uncertainty is high
- [ ] I update estimates when new information appears

## 5. Seek mentors

- [ ] I identify people I can learn from
- [ ] I look for more than one mentor: a dedicated mentor, ad hoc mentors, and internet mentors
- [ ] I ask specific questions rather than vague ones
- [ ] I learn from experienced engineers' habits, decisions, and feedback
- [ ] I verify advice from online sources or AI tools before using it

## 6. Maintain goodwill

- [ ] I try reasonable self-service steps before asking others for help
- [ ] I respect other people's time and come prepared when asking for help
- [ ] I summarize the problem, what I tried, and my next step
- [ ] I help others when they are stuck, and share useful knowledge with the team
- [ ] I thank people who help me
- [ ] I avoid working alone for long stretches when pairing or feedback would help

## 7. Take initiative

- [ ] I finish expected work before taking on extra initiatives
- [ ] I document unclear systems, decisions, or processes
- [ ] I volunteer for investigations when appropriate
- [ ] I research useful tools, frameworks, or internal systems
- [ ] I talk with my manager about upcoming work
- [ ] I offer help on smaller tasks when I have capacity
- [ ] I avoid creating distractions by starting too many side efforts

## 8. Practice coding

- [ ] I code regularly, on meaningful real-world problems
- [ ] I ask for code reviews and learn from repeated review comments
- [ ] I pair with more experienced developers when possible
- [ ] I build side projects, complete tutorials or structured training, and practice coding challenges when useful
- [ ] I read and write code consistently

## 9. Read code

- [ ] I review teammates' code even when I am not the main reviewer
- [ ] I read code outside my immediate team or company when helpful, including open-source projects using similar languages or patterns
- [ ] I understand what code does before changing it
- [ ] I take notes on unfamiliar patterns, conventions, and architecture
- [ ] I ask the original author questions when something is unclear

## 10. Write readable code

- [ ] I use clear, self-explanatory names and follow team naming and formatting conventions
- [ ] I keep functions and classes small, with well-structured classes and modules
- [ ] I apply single responsibility and avoid unnecessary complexity
- [ ] I use DRY appropriately, without over-abstracting
- [ ] I add comments where they explain "why," not obvious "what"
- [ ] I refactor continuously as code grows
- [ ] I ask others whether the code is easy to understand

## 11. Write quality code

- [ ] I use the right level of abstraction — no excessive tiny classes or unnecessary layers
- [ ] I hide implementation details when it reduces complexity
- [ ] I handle errors consistently
- [ ] I validate inputs, especially user inputs, and treat external inputs as potentially malicious
- [ ] I expect invalid responses from functions, APIs, or systems
- [ ] I expect exceptions and error states, and handle unknown API or system states explicitly
- [ ] I prefer safe defaults when response states are unclear

## 12. Become proficient in a language

- [ ] I learn the language fundamentals deeply: syntax, types, data structures, and control flow
- [ ] I learn standard error-handling approaches
- [ ] I understand memory management and performance basics, and how the language compiles or runs
- [ ] I learn the main framework used with the language
- [ ] I go deeper than "just enough to ship"
- [ ] I learn a second language when useful, and compare language strengths and weaknesses

## 13. Debug effectively

- [ ] I use debugger tools in my IDE: breakpoints, variable inspection, stepping into/over/out of functions, call stacks
- [ ] I use conditional breakpoints or watchpoints when helpful
- [ ] I learn from experienced developers while they debug
- [ ] I use logging when a debugger is unavailable, and paper debugging for complex logic
- [ ] I write tests to reproduce bugs
- [ ] I confirm the root cause before fixing

## 14. Refactor regularly

- [ ] I refactor my own code after it works
- [ ] I act on refactoring ideas from code reviews
- [ ] I read through code to identify confusing or duplicated areas, and keep a prioritized list of refactoring opportunities
- [ ] I use IDE refactoring tools
- [ ] I start with small refactors and test after each one
- [ ] I refactor tests as well as production code
- [ ] I avoid large risky refactors without a safety net
- [ ] I make refactoring an everyday habit

## 15. Test thoroughly

- [ ] I test code before requesting review or committing
- [ ] I manually verify behavior when needed
- [ ] I think through edge cases, and confirm stakeholder expectations for unusual cases
- [ ] I write automated tests when practical
- [ ] I learn unit, integration, screenshot, and end-to-end testing
- [ ] I add regression tests for bugs
- [ ] I treat testing as part of development, not a separate afterthought

## 16. Master your local environment

- [ ] I learn my IDE or editor deeply: shortcuts for frequent actions, formatting and linting, search, replace, refactor, and navigation features
- [ ] I configure my color scheme and workflow for comfort
- [ ] I learn how to run, debug, and test quickly
- [ ] I use hot reload or fast feedback loops where available, and avoid slow edit-compile-run cycles
- [ ] I use playgrounds or scratch environments for quick experiments

## 17. Learn frequently used tools

- [ ] I learn Git fundamentals: branching, rebasing, merging, conflict resolution, cherry-picking — and use a Git client or the command line confidently
- [ ] I learn command-line basics: navigating files and directories, running scripts and tools, searching files, setting environment variables
- [ ] I learn enough regular expressions for search and editing
- [ ] I learn basic SQL: SELECT, FROM, WHERE, ORDER BY, GROUP BY, HAVING, joins, and views
- [ ] I use AI coding assistants carefully, and save useful prompts or workflows
- [ ] I understand company-specific tools and systems
- [ ] I create a personal productivity cheat sheet

## 18. Iterate quickly

- [ ] I read existing code before changing it, and ask someone to walk me through unfamiliar systems
- [ ] I draw classes, modules, and connections, and share my code map with teammates
- [ ] I record useful "aha" moments in a cheat sheet
- [ ] I understand the CI/CD pipeline and know how to access its logs
- [ ] I know how to access production logs, dashboards, and metrics, and safe processes for debugging production data
- [ ] I make small, focused pull requests when possible
- [ ] I summarize pull requests clearly: screenshots or examples for UI changes, covered and uncovered edge cases
- [ ] I request code reviews instead of waiting too long, and ask for feedback on my work
- [ ] I compare my output and pace with team norms without treating it as a competition

## 19. Quick weekly self-review

- [ ] Did I deliver my most important work?
- [ ] Did I ask for help early enough when blocked?
- [ ] Did I break work into clear, shippable pieces?
- [ ] Did I communicate estimates, risks, and delays?
- [ ] Did I write readable, tested code?
- [ ] Did I learn something about the codebase, language, tools, or team?
- [ ] Did I get feedback from code review, pairing, users, or production?
- [ ] Did I help someone else or add goodwill to the team?
- [ ] Did I improve my workflow or tools?
