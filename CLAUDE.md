# Workspace root

The agent reads this file first every session, then routes to the one topic it needs — so it can reach all your work while only loading a thin slice. Replace the examples below with your own; keep the structure and the rules.

## How to operate

Ongoing work lives in **topics** — one folder per topic under `topics/<slug>/`, each with its own `CLAUDE.md` as its entry point. This root file lists the topics; it never holds their contents.

- **Read** a topic's `CLAUDE.md` before working on it — it's the map to that topic's files.
- **Write** into a topic as you go (decisions, status, findings). Add/remove a file → update that topic's file index.
- **Create** a topic only for standalone work with ongoing state: `mkdir topics/<slug>/`, give it a `CLAUDE.md`, add a line below. Default is to extend an existing topic, not spin up a new one.
- **Audit** with `/reindex` every week or sprint — it checks every index against disk and fixes drift. This is what keeps the workspace from rotting at scale.

## About

*Who this is for, role, standing preferences — anything the agent should always know.*

## Topics

- **Example Project** — a single ongoing project. → `topics/example-project/CLAUDE.md`
- **Customer Research** — a reference area that just accumulates knowledge. → `topics/customer-research/CLAUDE.md`

Finished topics move to `topics/_archive/`.

## Tools

*Cross-cutting capabilities available from any topic — scripts, MCP integrations, CLIs.*
