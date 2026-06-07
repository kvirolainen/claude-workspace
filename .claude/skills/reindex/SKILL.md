---
name: reindex
description: Audit and tidy the topics workspace against the rulebook — sync each topic's file index to disk, fix hygiene, keep root + topic CLAUDE.md lean, surface archive/merge candidates. Invoke on "reindex", "/reindex", "audit my topics", or after a burst of changes to topics/. Auto-applies safe fixes; proposes anything that could lose content.
---

# /reindex — workspace audit

Day-to-day writes drift: indexes go stale, statuses lag, CLAUDE.mds bloat. Run this on demand — after a burst of changes, or on a loose weekly/per-sprint cadence — to catch the drift no single edit is big enough to trigger. It's what keeps the structure honest at scale instead of letting it rot into a pile of markdown.

**Root** = the folder holding `CLAUDE.md` + `topics/`. Every finding cites a rule below; if it maps to no rule, don't raise it.

## Rules

- **R1 — Layout.** Topics live in `topics/<slug>/`, clean slug, no dates. Finished/irrelevant topics move to `topics/_archive/`.
- **R2 — Entry point.** Every topic has a `CLAUDE.md`: title → overview → `**When to open**` → `## Files in this topic` → optional `## Code & deploy`.
- **R3 — Altitude.** A topic's `CLAUDE.md` holds only what's *always relevant* when working on it. Situational/historical/deep detail goes in other files (`notes.md`, `research/`). App code lives in your code home; the topic only references the path + deploy.
- **R4 — Index accuracy.** `## Files in this topic` lists every meaningful file, one line each. Bulk dirs (`data/`, `research/`, `node_modules/`, `dist/`) are one summary line, never enumerated.
- **R5 — Lean root.** Root `CLAUDE.md` holds only topic-agnostic things: who the user is, the rules, preferences, the topic list (pointers only), cross-cutting tools. No `@imports`.
- **R6 — Hygiene.** Secrets only in `.env` / `.env.*`.
- **R7 — Honest overviews.** Lead with the headline status; absolute dates, not "last week"; match what the files actually say.
- **R8 — Lifecycle.** Flag self-contradictions, archive candidates (shipped / decided / stale), and merge candidates (overlapping topics) — as *proposals*, never auto-done.

## Fix policy

- **Auto-apply:** index sync (R4), hygiene (R6), root-list sync (R5), and rewrites that lose no information (R3/R7).
- **Propose only:** archives, merges, deletions, or any rewrite that might drop content.

Always report what was auto-applied.

## Procedure

1. **Scan (fast):** list `topics/*/`; check each has a `CLAUDE.md`; diff the root topic list against folders on disk; grep for secrets outside `.env`. Auto-fix the safe ones.
2. **Per topic:** read its `CLAUDE.md` + `notes.md`, compare to disk and to itself. Findings against R2–R8. (Batch topics across parallel subagents if there are many.)
3. **Root:** topic list complete + consistent, lean, most-active first.
4. **Cross-topic:** assemble archive + merge candidates with evidence.
5. **Apply + report:** `✅ Auto-fixed (N)` then `🔸 Proposed (N)` awaiting OK.
