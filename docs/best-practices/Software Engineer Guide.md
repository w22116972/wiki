# Software Engineer Guide

## Choice of company

- Prefer which offers career paths above staff engineer
    - e.g. Big Tech > Freelancer, small company, public sector, nonprofit, outsourcing company, academia
- Prefer top of regional/international market over top of local market
- Prefer profit center team (directly generate revenue for busniess) over cost center team (operate smoothly)
    - By just displaying impact on revenue generation
    - e.g. Ads is Google profit center, infra is Google cost center
    - Cost center team in Big Tech is exceptional (still big impact on revenue)

## Self

- be seen as someone who "Get things done"
  - plenty of impactful projects
- keep a work log
  - format: date, project, task, time spent, result
  - use it to write resume

## Mindset

If you must wait for a teacher before you can learn something, you aren't hungry enough and will probably NOT find a software job
Your degree or certification means nothing. It's your disciplined daily practice, on increasingly tougher, practical problems, that gets you jobs.
Universities are too slow and far behind in technology, compared to what companies actually need.

You quickly hit questions that no one else (including your teachers or bosses) can answer but you.
Get used to solving problems alone.

Much of software engineering is like being a lawyer, since bosses and teammates often ask you tough, critical questions on why you wrote code your way. Be prepared to strongly, persuasively defend your code decisions.
You must convince yourself that yours is the best solution, with limited time/money, that the company needs.


---

# Achieve Better Performance Review Results

## Gather context and set goals early

- Identify manager's goal, team's goal, company's goal

## Keep Following Habits

- Keep a work log
- Keep a list of accomplishments(wins)

Offer your manager a summary of your work before the review meeting

---

## Onboarding

- Ask future manager for a list of things to learn
- Clarify goals with manager for first month,  3 months, 6 months, 1 year
- Keep work log, weekly report, monthly report

---

## GTD

Why building a reputation for getting things done is important?
- Accelerate my learning and career growth because I will be given more challenging projects.
- More autonomy because manager views me as reliable and no need of hand-holding

Focus on the most important tasks on list and make habit of always completing the #1 priority

Estimate time for each task and track time spent

Reliable engineer cares deeply about edge cases.

Debugging
- Use break points to step in/over/out.
- Use conditional break points, watch points, and exception break points.
- Ignore certain condition N times before it breaks
- Change variable value while debugging
- Evaluate expression while debugging
- Skip between threads
- Drop to a frame(https://stackoverflow.com/questions/2367816/when-using-the-java-debugger-in-intellij-what-does-drop-frame-mean)
  - To explore different paths of execution without having to restart the application or a particular lengthy process that led to the current stack
  - only local variables are reset
  - 这个功能可以重新跳到当前方法的开始处重新执行，并且所有上下文变量的值也回到那个时候。不一定是当前方法，可以点击当前调用栈中的任何一个frame跳到那里(除了最开始的那个frame）。主要用途是所有变量状态快速恢复到方法开始时候的样子重新执行一遍，即可以一遍又一遍地在那个你关注的上下文中进行多次调试(结合改变变量值等其它功能），而不用重来一遍调试到哪里了。当
    然，原来执行过程中产生的副作用是不可逆的
- learn thru outage
  - learn to access and analyze prod logs, locating code responsible for certain business logic
  - research historical outage to learn

Create personal productivity cheat sheet

- Avoid defeat by to-do list, some tasks will eventually be unimportant
- When it is done, it is properly done with
  - written spec, test plans, all edge cases covered, what is out of scope, monitoring/alerting to feature, automatic tests

---

### Onboard

- learn where prod logs are stored
- learn where to find system's dashboard
  - get access, learn how to query
- learn how services are deployed to prod and how to manage
  - where infra config are stored
- learn how secrets are stored
- learn how certs are set up
- Onboarding documentation
  - high-level overview of the system, responsibilities, and how to interact with other services
  - how to modify and deploy code
  - how to test and validate changes
  - how to deploy to prod
  - how to monitor prod systems
  - how alerting works
  - tips on how to debug system if prod fails

### After project planning is completed

- Test plan
  - how to test system
  - which edges cases are essential
- Rollout plan
  - how system be rolled out to prod
  - which feature flag will be used
- Migration plan
  - how to migrate from one system to another
  - phases of migration
  - how will it be validated that new system works correctly before traffic is moved to it

### Interface documentation

- how to use API
- list of endpoints, input each one expects, expected output
- error codes and messages returned
- code sample on using API

---

# Engineer’s Survival Guide

Use data to convince others

First working prototype always wins

Visibility is everything

- avoid people’s direct message
- sharing status updates
- commenting on public posts

Taking responsibility and ownership

- any issue related to your own project, you must take responsibility

Always consider whether there is a tool that can do your task faster and better and fewer mistakes

Use “acked” to reply others instead of spending time on replying with full answer

Don’t redesign a working system
