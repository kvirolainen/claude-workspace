#!/usr/bin/env python3
"""Stop hook: close a Claude Code session after /wrap finished its reply.

/wrap's last step writes ~/.cache/claude-wrap/<session_id> containing the session's CLAUDE_PID. Claude Code runs this
after every reply, in every session. With no marker for this session it exits at once: no output, no tokens. With a
fresh marker (under MAX_AGE), it removes the marker and sends SIGTERM to that Claude a moment later, after the reply is
on screen and any other Stop hooks have run. An old marker (left by an interrupted /wrap) is removed and ignored, so a
later normal reply never closes the session.
"""
import json
import os
import subprocess
import sys
import time

DIR = os.path.expanduser("~/.cache/claude-wrap")
MAX_AGE = 600     # seconds; /wrap writes the marker as its very last step
DELAY = 2         # let any other Stop hooks finish first


def main():
    try:
        sid = json.load(sys.stdin).get("session_id") or ""
    except Exception:  # noqa: BLE001
        return
    marker = os.path.join(DIR, os.path.basename(sid))
    if not sid or not os.path.isfile(marker):
        return
    fresh = time.time() - os.path.getmtime(marker) < MAX_AGE
    pid = open(marker).read().strip()
    os.remove(marker)
    if not fresh or not pid.isdigit():
        return
    # Background session: killing the process leaves it under "Completed" and the next message resumes it.
    # Use Claude Code's own commands instead: stop it, then remove it from the list (transcript kept,
    # `claude --resume` still lists it).
    short = os.path.basename(sid)[:8]
    if os.path.isdir(os.path.expanduser("~/.claude/jobs/" + short)):
        cli = os.path.expanduser("~/.local/bin/claude")
        cli = cli if os.path.exists(cli) else "claude"
        subprocess.Popen(["/bin/sh", "-c", "sleep {d}; '{c}' stop {s}; sleep 1; '{c}' rm {s}".format(d=DELAY, c=cli, s=short)],
                         start_new_session=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return
    # Only ever signal a Claude process — a stale or reused PID must not hit anything else.
    comm = subprocess.run(["ps", "-o", "comm=", "-p", pid], capture_output=True, text=True).stdout.strip()
    # Foreground: …/claude. Background sessions: …/share/claude/versions/<ver>, whose basename is just the
    # version number, so match the full path too.
    if "claude" not in os.path.basename(comm) and "/claude/versions/" not in comm:
        return
    subprocess.Popen(["/bin/sh", "-c", "sleep {}; kill -TERM {}".format(DELAY, pid)],
                     start_new_session=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


if __name__ == "__main__":
    main()
