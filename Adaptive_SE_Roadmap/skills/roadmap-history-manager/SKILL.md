---
name: roadmap-history-manager
description: Create audited, append-only roadmap migrations, diagnostic Q&A records, learning-session logs, and synchronized current-state updates. Use when the user reports progress, changes a milestone, requests history updates, or asks to compare roadmap versions.
metadata:
  version: "1.0.0"
---

# Roadmap History Manager

## Core principle

`history/` is the event ledger; `docs/03_CURRENT_STATE.md` is a materialized snapshot. Preserve all prior records. Do not invent learning events, diagnostic answers, task completion or exact timestamps.

## Steps for a write

1. Load `docs/08_DATA_CONTRACT.md`, `history/00_EVENT_INDEX.md`, latest related log and `docs/03_CURRENT_STATE.md`.
2. Classify input as `LEARNING_SESSION`, `DIAGNOSTIC`, `ROADMAP_CHANGE`, `COURSE_VERIFIED`, `MILESTONE_VERIFIED`, `REVIEW`, or `CORRECTION`.
3. Extract **only observed/user-supplied facts**, distinguish `reported`, `assessed`, `proposed`.
4. Deduplicate against recent events; allocate stable `EV-YYYYMMDD-NNN` and record ID; date precision may be day-only if no time known.
5. If proposed scope/career/milestone change: draft `CR` with before/after/reason/evidence/impact; do not apply without approval.
6. If user asks to save and tool allows: append record into correct log; update event index; update `MAIN` and `CURRENT_STATE` atomically as far as supported; validate consistency. For inaccessible files, return **copy-ready patches** and state no file was changed.
7. Verify: last event ID matches snapshot; no completed course without mandatory full coverage; no fabricated dates/evidence.

## Correction / rollback

Never delete or overwrite incorrect event. Append `CORRECTION` referring to offending `event_id` with before/after/reason and affected records; recompute `CURRENT_STATE`. If a session/answer contains a typo, preserve original in history and add clarification/correction with references.

## Diagnostic record requirements

Follow `templates/DIAGNOSTIC_RECORD.md`: exact question and raw answer, rubric, score 0–4 or `null`, feedback, assistance level, topic ID, version; link to session/source if possible. If no response, no diagnostic result.

## Examples

- “Hôm nay tôi đã đọc OOP inheritance và làm bài lab A” → propose session record, mark `reviewed` only when user provides meaningful evidence; **don't** mark course complete.
- “Đổi hướng sang Go vì JD mới” → CR only, with JD evidence and impact, await approval.
- “Bài diagnostic trước chấm sai” → append correction; keep original preserved.
- “Đã chốt môn OOP hoàn thành” → verify coverage and integration gate; if missing, list missing topics instead of granting completion.
