# Claude Workspace — a self-maintaining workspace for Claude Code

One entry point for everything you're working on. A root file points your agent to every project; each project carries its own index. The agent reaches all your work but only loads the slice it needs — so it stays sharp as you pile more in, instead of getting dumber as its context fills up (context rot).

Three rules are the whole idea:

1. **Index, don't dump.** The root `CLAUDE.md` lists projects and points to them — never their contents.
2. **Every project carries its own index.** Each `topics/<slug>/` has a `CLAUDE.md` the agent reads before the rest.
3. **Sweep on a cadence.** The `/update` skill re-scans each working session and writes what actually happened — decisions, findings, status changes — into the right files, fixing anything now stale or contradictory. This is the part the toy "second brain" setups skip — and why they don't survive scale.

Three skills do the maintenance:

- **`/update`** — end-of-session capture sweep. Everything durable from the conversation lands in the right topic, the indexes stay true, and the latest discussion wins over stale notes.
- **`/wrap`** — the one command to end every session. It decides by itself whether anything still needs capturing (if so it runs the `/update` sweep), then closes the session via a small Stop hook (`scripts/wrap_close_hook.py`). You never have to judge whether an update is due.
- **`/task`** — for multi-session work with real stages. One living spec file per task in `tasks/` (stage, plan, decision log — resumable cold), nudged through Backlog → Spec → In Progress → Code Review → Testing → Done. The spec file *is* the tracker; wire in Linear/Jira later if you want, the depth stays in the file.

## What's in here

```
CLAUDE.md                       root: the rules + your topic list
topics/
  example-project/              an active project (status, decisions, maybe code)
  customer-research/            a reference area that just accumulates knowledge
tasks/                          living spec files for /task, one per task
.claude/skills/update/          the session sweep that keeps it honest
.claude/skills/task/            the staged task workflow
.claude/skills/wrap/            end-of-session: capture if needed, then close
.claude/settings.json           registers the Stop hook /wrap uses to close
scripts/wrap_close_hook.py      that hook
```

## Use it

1. Copy this folder into your work. (Built for [Claude Code](https://claude.com/claude-code), where `CLAUDE.md` loads automatically — adapt the filename for other agents.)
2. Fill in the `About` and `Tools` sections of the root `CLAUDE.md`; delete the two example topics.
3. Add your own: `mkdir topics/<slug>/`, give it a `CLAUDE.md`, add a line to the root list.
4. End every session with `/wrap` (or run `/update` mid-session to capture without closing); use `/task` for anything that spans sessions.

Everything else is yours to fine-tune.
