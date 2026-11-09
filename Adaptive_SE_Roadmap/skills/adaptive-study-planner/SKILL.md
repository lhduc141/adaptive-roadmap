---
name: adaptive-study-planner
description: Generate flexible, energy-aware today/this-week learning actions from the user's current roadmap state, mastery gates, and history without invented deadlines or progress. Use for daily planning, weekly planning, or resuming after a break.
metadata:
  version: "1.0.0"
---

# Adaptive Study Planner

## Inputs

Read `docs/03_CURRENT_STATE.md`, `docs/04_EXECUTION_PROTOCOL.md`, `docs/01_ROADMAP_MAIN.md`, current course row in `docs/02_COMPETENCY_AND_COURSE_MAP.md`, and recent `history/03_LEARNING_SESSIONS.md` + `history/02_DIAGNOSTICS.md`. For Todoist mapping read `docs/07_TODOIST_BRIDGE.md`.

Optional direct user inputs: `energy`, `available_time`, real work/GLV commitments, specific topic preference. If user asks *today* use actual local date/time if an authorized tool exists; otherwise don't invent a calendar slot.

## Selection algorithm

1. Prioritize confirmed urgent commitments over voluntary learning; do not create work tasks not in available records.
2. If an active unit exists, resume its checkpoint. Else choose one `ready` unit; else propose one candidate unit clearly labeled `PROPOSED`.
3. If a diagnostic has a weakness, reinforce it before introducing a new topic unless user explicitly chooses otherwise.
4. At most one primary action + one optional supporting action; if no availability, give low/medium/high modes **not three mandatory tasks**.
5. For *this week*, propose <=2 outcomes with 1–3 selectable actions each, no weekday binding or fake deadlines. Past week omissions don't create debt.
6. Every action: stable subject/unit reference, reason, steps, output/DoD, way to report completion, Todoist project/section (only if created/confirmed).
7. Never mark a task started/done or write history just for having suggested it.

## Output template

- **Current verified:** [version, milestone, pass, last real evidence].
- **Main action:** `[ID]` — [task and reason, 1–3 steps, DoD]. State `Ready` or `Proposed`.
- **Low energy:** [micro version / rest].
- **More time available:** [stretch optional].
- **Report back:** [what user should send for history].
- **No false claims:** say when Todoist sync is not available.

## User stories

- “Hôm nay mệt, có 15 phút” → choose one smallest continuation or rest; don't create a whole Java schedule.
- “Tuần này bận GLV, SQL work” → cap outcomes; keep WIP; no calendar days invented.
- “Tuần trước tôi nghỉ hết” → resume prior checkpoint; no catch-up debt or reset milestone.

## Guardrails

Energy unknown is not high. Stop if an active unit conflicts with a later event; ask reconciliation or provide safe proposal. Don't leak business code or privileged docs.
