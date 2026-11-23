---
name: wrap
description: End the session — "/wrap", "wrap up", "wrap it". Decides by itself whether anything from this session still needs capturing (if not, one line; if so, runs the /update sweep), then closes this Claude Code session automatically once the reply is on screen. For capture without closing, use /update.
---

# /wrap — capture if needed, then close the session

Type `/wrap` at the end of **every** session and never judge whether an update is needed. The agent makes that
call. Then the session closes by itself.

## 1 · Triage (always, quick)

Re-scan the whole conversation. Is there anything durable that is **not yet written to a file**: a decision, a
correction, a new rule or preference, a status change, a new file that needs indexing? Check the destination files
before deciding. Items captured during the session don't count.

- **Nothing left** → skip to step 3. Do not run the sweep.
- **Something left** → step 2.

## 2 · Sweep (only when triage found something)

Read `.claude/skills/update/SKILL.md` and run its Steps 1–5. Keep the report short. Lead with what was written,
and drop the empty sections.

## 3 · Close

Make this your **last tool call**, after everything else is written:

```bash
mkdir -p ~/.cache/claude-wrap && echo "$CLAUDE_PID" > ~/.cache/claude-wrap/"$CLAUDE_CODE_SESSION_ID"
```

Then write the final reply: one line for the triage outcome (or the short sweep report), ending with
`Closing the session.` The Stop hook (`scripts/wrap_close_hook.py`, registered in `.claude/settings.json`) closes
the session about 2 s after the reply is done. The conversation stays on disk, so `claude --resume` reopens it.

If `CLAUDE_PID` or `CLAUDE_CODE_SESSION_ID` is empty (e.g. a headless `claude -p` run), skip the marker and say
the session can't self-close here.
