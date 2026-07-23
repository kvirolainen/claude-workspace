---
name: update
description: End-of-session (or mid-session) capture sweep — make sure everything from THIS conversation is written into the right topics, traceable from the root CLAUDE.md, current, and non-contradictory. Invoke on "/update", "update", "write this down", "capture the session", or before wrapping up a long working session.
---

# /update — session capture sweep

The workspace rule is "capture as you go," but long sessions drift — decisions land in conversation and never make it into a topic, statuses go stale mid-discussion, a finding supersedes something written an hour earlier. `/update` is the sweep that closes those gaps for **this session only**.

**Scope guard:** `/update` looks at what this session touched or discussed. It never audits untouched topics or restructures the workspace.

## Step 1 — Full-session sweep

Re-scan the **entire** conversation, not just the last stretch. Collect every item worth persisting:

- **Decisions** — with the reasoning, not just the conclusion.
- **Findings** — concrete facts: numbers, comparisons, root causes, research results.
- **Status changes** — anything that moved a topic's state forward (shipped, bought, contacted, blocked, parked).
- **Blocked / parked items** — with enough detail that a future session can resume cold: what was attempted, why it's blocked, what unblocks it.
- **New facts about the user / preferences** — feedback on how to work, tools, voice, standing constraints.
- **New files or scripts created this session** — anything that needs an index entry.

If the session covered a lot of ground, the capture should reflect that — a tiny update after a long, dense session is a sign something got missed.

## Step 2 — Route each item

For each item, decide its destination using the root rules:

| Item | Destination |
|---|---|
| Topic-specific decision / finding / status | That topic's `notes.md` (or the file the topic's CLAUDE.md says holds it) |
| Always-relevant change to a topic's map (status headline, new file, deploy change) | That topic's `CLAUDE.md` |
| Broadly-applicable fact or preference that compresses to a one-liner | Root `CLAUDE.md` (About / Tools) |
| Genuinely standalone new work with ongoing state | New topic (follow the root's "Create" rule exactly — default is extend, not spin up) |
| Conversation-only detail (trivia, dead ends with no lesson) | Nowhere — deliberately skip |

## Step 3 — Diff against what's already written

Before writing, **read the destination file(s)**. The session may have already captured some items as it went — don't duplicate:

- Already captured accurately → skip.
- Captured but now stale/superseded by later discussion → **update in place** (statuses, decisions that got reversed). Never leave both the old and new claim standing.
- Not captured → append/insert in the file's existing style. Use absolute dates (2026-07-20, not "today").

**Contradiction check** is the point of this step: the latest discussion wins. If a topic's overview says "deciding" and the session decided, fix the overview. If notes say X and we learned ¬X, correct the note (a brief "superseded <date>: …" is fine where history matters; silent correction is fine where it doesn't).

## Step 4 — Traceability & root health (touched content only)

For every topic written to in Step 3:

1. **Root topic list** — the topic has a line, and that line still matches reality (≤~15 words). New topic → add the line.
2. **Topic file index** — if files were added/removed in the topic this session, its CLAUDE.md file index reflects that.
3. **Topic overview** — leads with the current headline status, consistent with what notes.md now says.

And for root `CLAUDE.md` itself:

4. **Root staleness** — if the session contradicted or outdated anything in root (About facts, Tools, a topic line), fix it — latest discussion wins here too.
5. **Altitude corrections** — if the session revealed something sitting at the wrong level, move it: a root detail that turned out to be topic-specific → down into the topic; a topic fact the session needed inline and that's truly universal + one-liner-sized → up into root. Move, never duplicate. Only for content this session actually touched.

## Step 5 — Report

Compact, grouped by destination:

```
## /update — <YYYY-MM-DD>

### Written
- topics/<slug>/notes.md — <decision/finding, one line each>
- topics/<slug>/CLAUDE.md — status "X" → "Y"; +<file> in index
- root CLAUDE.md — <new preference/fact>

### Corrected (was contradictory/stale)
- topics/<slug>/... — "<old>" → "<new>"

### Skipped on purpose
- <conversation-only items, one line> (omit section if none)
```

If the session was chatty with nothing durable, say so in one line — don't manufacture capture.

## Notes

- Everything here is auto-apply — these are established facts from the session itself, not speculation. The only propose-first case is creating a **new topic** when the fit is unclear: ask where it belongs.
- For per-task capture into a spec file, use `/task update` instead; `/update` sweeps the session into **topics**. Both can run at session end.
