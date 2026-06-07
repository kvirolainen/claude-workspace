# Agent Workspace — a self-maintaining workspace for your AI agent

One entry point for everything you're working on. A root file points your agent to every project; each project carries its own index. The agent reaches all your work but only loads the slice it needs — so it stays sharp as you pile more in, instead of getting dumber as its context fills up (context rot).

Three rules are the whole idea:

1. **Index, don't dump.** The root `CLAUDE.md` lists projects and points to them — never their contents.
2. **Every project carries its own index.** Each `topics/<slug>/` has a `CLAUDE.md` the agent reads before the rest.
3. **Audit on a cadence.** The `/reindex` skill checks every index against disk and fixes drift. This is the part the toy "second brain" setups skip — and why they don't survive scale.

## What's in here

```
CLAUDE.md                       root: the rules + your topic list
topics/
  example-project/              an active project (status, decisions, maybe code)
  customer-research/            a reference area that just accumulates knowledge
.claude/skills/reindex/         the audit that enforces the rules
```

## Use it

1. Copy this folder into your work. (Built for [Claude Code](https://claude.com/claude-code), where `CLAUDE.md` loads automatically — adapt the filename for other agents.)
2. Fill in the `About` and `Tools` sections of the root `CLAUDE.md`; delete the two example topics.
3. Add your own: `mkdir topics/<slug>/`, give it a `CLAUDE.md`, add a line to the root list.
4. Run `/reindex` weekly to keep it honest.

Everything else is yours to fine-tune.
