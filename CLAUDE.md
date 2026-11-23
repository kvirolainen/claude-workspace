# Workspace root

The agent reads this file first every session, then routes to the one topic it needs — so it can reach all your work while only loading a thin slice. Replace the examples below with your own; keep the structure and the rules.

## How to operate

Ongoing work lives in **topics** — one folder per topic under `topics/<slug>/`, each with its own `CLAUDE.md` as its entry point. This root file lists the topics; it never holds their contents.

- **Read** a topic's `CLAUDE.md` before working on it — it's the map to that topic's files.
- **Write** into a topic as you go (decisions, status, findings). Add/remove a file → update that topic's file index.
- **Create** a topic only for standalone work with ongoing state: `mkdir topics/<slug>/`, give it a `CLAUDE.md`, add a line below. Default is to extend an existing topic, not spin up a new one.
- **Sweep** with `/update` before wrapping up a working session — it captures the session's decisions, findings, and status changes into the right files and fixes anything now stale or contradictory. This is what keeps the workspace from rotting at scale. Simplest habit: end every session with `/wrap` — it runs the sweep only if something is uncaptured, then closes the session.
- **Track** multi-session work with `/task` — one living spec file per task in `tasks/` (stage, plan, decision log), staged Backlog → Spec → In Progress → Code Review → Testing → Done.

## About

*Who this is for, role, standing preferences — anything the agent should always know.*

## Topics

- **Example Project** — a single ongoing project. → `topics/example-project/CLAUDE.md`
- **Customer Research** — a reference area that just accumulates knowledge. → `topics/customer-research/CLAUDE.md`

Finished topics move to `topics/_archive/`.

## Tools

*Cross-cutting capabilities available from any topic — scripts, MCP integrations, CLIs.*
