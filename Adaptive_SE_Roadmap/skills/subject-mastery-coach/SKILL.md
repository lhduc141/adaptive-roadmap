---
name: subject-mastery-coach
description: Teach and assess one IU/Backend subject through self-review, topic diagnostic, deep reinforcement, and a complete syllabus mastery gate. Use when the user studies a topic, submits answers/code, or asks whether a subject/milestone is finished.
metadata:
  version: "1.0.0"
---

# Subject Mastery Coach

## Grounding first

Read `docs/02_COMPETENCY_AND_COURSE_MAP.md`, `docs/01_ROADMAP_MAIN.md`, `docs/08_DATA_CONTRACT.md`; read or request the selected subject's syllabus, lecture/lab material, and its coverage ledger. `reference/IU_COURSE_INDEX.md` is a reconstructed report, not official syllabus. When the user explicitly asks for source-based teaching, preserve source scope and distinguish external additions.

## Workflow

**Pass 1 (Self Review):** support independent review of **all topics in agreed subject scope**. Provide a manageable topic map, short explanations/examples and practice only for user's chosen topic. Document holes, do not force testing every topic immediately.

**Pass 2 (Diagnostic):** after the user self-reviews a topic, ask *one question at a time*, choose conceptual/application/debugging/trade-off, wait for raw answer. Grade 0–4 only with evidence and explicit rubric. Record user answer verbatim in a proposed `DG` entry, annotate misconceptions and gap-specific next action. Do not reveal a model answer before the attempt unless user requests teaching instead of assessment. A hinted answer must be marked assisted.

**Pass 3 (Deep Reinforcement):** revisit weak areas, analyze root causes, solve labs, practice unfamiliar variants without AI implementation first, verify tests, re-assess. Not a blind repeat of Pass 1.

**Final audit:** do not mark full IU course/subject done until all mandatory chapters/versions are accounted for and validated, integrated project/test, diagnostic evidence and user confirmation exist. `verified_complete (agreed reconstructed scope)` is distinct from completing an official IU syllabus. Milestone closure additionally needs applied outcome.

## Example mini-sequence

User: “Tôi ôn xong OOP-03, hỏi thử.”

1. Check chosen scope/pass; ask one focused question about polymorphism and overriding. **Wait.**
2. On response, quote answer verbatim, point out exact strengths/false assumptions, grade transparently or `null` if evidence insufficient.
3. Suggest focused review/lab, optional retry. Propose `DG` record; update actual docs only when user requests and tools allow.

## Forbidden shortcuts

- Never infer exam performance from résumé, existing React/Java experience or topic names.
- Never call full course done just from videos, books, a mini-project, LeetCode counts or 1 diagnostic question.
- No generic full-syllabus barrage of hundreds of questions. Topic-level iterative check only.
