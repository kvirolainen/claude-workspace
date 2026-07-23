---
name: task
description: Pick up a tracked task — the next live item or a specific one. Maintains a living spec file in tasks/ and nudges work through Backlog → Spec → In Progress → Code Review → Testing → Done. Invoke on "/task", "/task <ID>", "/task update", "/task create", "/task list", or when the user asks to pick up / create / update a tracked task. For session-wide capture into topics use /update instead.
---

# /task — living-spec task workflow

Multi-session work needs more than a topic's notes: a stage, a plan, a decision log a fresh session can resume from cold. `/task` keeps all of that in **one living spec file per task** under `tasks/` — the spec file *is* the tracker. (If you use an external tracker — Linear, Jira, GitHub Issues — mirror only a short status line there; the spec file stays the source of truth for depth.)

**Spec files:** `tasks/<ID>-<slug>.md`, flat. IDs are `T-<n>` — next `n` = highest existing + 1.

## Invocation forms

- `/task` — pick the most "live" task: In Progress first, then Spec, then Backlog, most recently updated first. Skip Done.
- `/task <ID>` — jump to a specific task.
- `/task update` — full-session sweep into the current task's spec.
- `/task create [extra context]` — create a new task from the current conversation.
- `/task list` — all tasks at a glance (ID, title, stage, updated), from the spec files' Status lines.

## Stages

`Backlog → Spec → In Progress → Code Review → Testing → Done` — tracked in the spec's Status line, which is the source of truth.

**Nudge, don't block.** Two moments can silently skip a stage: locking a plan without real discussion, and marking Done without an actual review/testing pass on record. In both cases flag it **once** and ask — then respect the answer either way, and don't ask again in the same session for the same skip.

## Create (`/task create`)

**Title** — short human-readable summary, max ~10 words. **Topic** — infer the related topic from the conversation against the root topic list; it goes in the Status line.

```markdown
# <Title>

## Status
_Stage: Backlog · Updated: <today> · Topic: topics/<slug>/_

## Problem / Goal
<synthesis from the conversation — what we're building and why>

## Plan
_Not yet locked — pending discussion._

## Decisions
_(none yet)_

## Progress
_(none yet)_

## Open Questions
<if any, else omit>
```

After creating, show `Created [<ID>]: <title>` and ask if the user wants to start now. Then stop.

## Pick up (`/task`, `/task <ID>`)

Read the spec — that's the primary session context. Show the ID, title, stage, and spec content, then continue from wherever the stage says.

- **Backlog** → discussion before code. A locked spec needs an actual **Plan** — an approach in 2-3 sentences, not a restated goal. If all there's been is a one-line "yeah build X", nudge once: "Want to talk through the approach first, or just go?" Once discussion has produced a concrete plan, write **Plan** and set the stage to **Spec**.
- **Spec** → the plan was locked in a prior session — re-read it, confirm it still holds, start building.
- **In Progress** → resume from **Progress** + **Decisions**.

## In flight

Flip Backlog/Spec → **In Progress** automatically on the first real code edit for the task. Log notable decisions into **Decisions** as they land (newest first, dated, with the why).

## Code Review

When the implementation feels functionally complete: set the stage to **Code Review** and run a **fresh review pass on the diff** — a code-review skill if available, otherwise a fresh-context subagent reviewing the diff. Not a same-context re-read: the fresh pass is what makes this stage worth more than the model checking its own work. Fix what it finds; note the outcome in **Progress**.

## Testing → Done

Set the stage to **Testing** once review is clean, then actually verify before looping the user in — verification is task-shaped:

- **UI / web change**: walk the golden path + an edge case, report what was observed, ask the user to spot-check.
- **Script or automation**: run it for real (or against representative input), check the output makes sense.
- **Non-code task** (doc, research, config): collapse Code Review + Testing into one self-check (read it back, verify links/facts) — no review theater on work with no code.
- If something genuinely can't be verified here (user's device, visual judgment, prod access, a third party), name exactly what they must check — never a generic "please test".

**Before Done:** the spec should show a completed review + testing pass (nudge once if fast-tracked), and any code repos touched should be committed — a task isn't done if the fix only exists on disk. Then set the stage to **Done**.

**After Done, update the relevant topic** — fold the task's durable outcomes into the topic per the spec's Topic line: file-index changes, status changes, a dated notes entry tagged `[<ID>]` (what shipped, key decisions, gotchas). Skip silently if the task changed no topic's durable state.

## Updating the spec

Update on: explicit `/task update`, after writing real code, on any stage transition (always), or after a significant decision.

**An explicit `/task update` is a full-session sweep, not an incremental touch-up.** Re-scan the *entire* session: every decision (with reasoning), every concrete finding, everything blocked and on what. Blocked items need enough detail to resume cold. Update `Plan` / `Decisions` / `Progress` / `Open Questions`, refresh the Status line's stage + date. `Decisions` and `Progress` stay newest-first; append, never rewrite history.

After updating, say briefly what changed (e.g. "Stage → Code Review, spec updated.").

## Notes

- Tasks are for multi-session work with real stages. Quick asks and conversation → no task; topics + `/update` already cover those.
