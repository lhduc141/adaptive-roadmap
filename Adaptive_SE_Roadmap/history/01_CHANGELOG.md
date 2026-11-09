# ROADMAP CHANGELOG — MIGRATION STYLE / APPEND-ONLY

> Dành cho các thay đổi **roadmap** và event được duyệt; không ghi đè migration. State hiện tại xem ở `docs/03_CURRENT_STATE.md`; log giải thích *vì sao* state thành như thế.

## EV-20261109-001 — Bootstrap adaptive roadmap v1.0.0

```yaml
event_id: EV-20261109-001
date: 2026-11-09
time_precision: day
actor: AI-drafted_from_user_explicit_request
type: BOOTSTRAP
entity_id: SE-ADAPTIVE-2026
before: no_adaptive_roadmap_document_set
change: create_portable_markdown_roadmap_and_skills
after: roadmap_document_set_v1_0_0
reason: user_requires_milestones_full_subject_mastery_history_and_daily_weekly_planning
approval_scope: user_requested_creation_not_approval_of_every_recommendation
status: applied_as_document_bootstrap
related_files:
  - docs/01_ROADMAP_MAIN.md
  - docs/02_COMPETENCY_AND_COURSE_MAP.md
  - docs/03_CURRENT_STATE.md
  - history/00_EVENT_INDEX.md
reconciled: true
```

**Nội dung nền:** bỏ mô hình trước đó gán 6 sprints/12 tuần và khối lượng cao; chuyển sang roadmap outcome-based với milestone, full-course anchor, Pass1→Pass2→Pass3→final audit, không deadline giả. `Core-Plan.md` còn làm **historical reference**, không phải plan hiện hành.

**Tính xác nhận:** người dùng đã yêu cầu xây bộ tài liệu và skill theo mô hình này. Nội dung milestone cụ thể và `MS-01` là candidate được AI đề xuất từ các cuộc trao đổi; **chưa xác nhận đã bắt đầu, chưa hoàn tất khóa học nào**.

**Evidence refs:** user current conversation; `reference/Detail-Information.md`, `reference/My_Projects.md`, `reference/Todoist_document.md`, `reference/Core-Plan.md`, `reference/IU_COURSE_INDEX.md`; web benchmark in `docs/06_MARKET_BASELINE.md`.

**Before → after:**

| Field | Before | After |
|---|---|---|
| planning logic | 6 sprints/12 tuần trong tài liệu cũ | adaptive milestones không deadline |
| full course completion | chưa quy định gate chung trong bản cũ | source-bound full coverage + 3 passes + integration validation |
| daily/week help | phân chia thời gian/sprint | current-state + last history + energy constraints |
| diagnostics | đề xuất tổng thể/kiểm tra | topic-level after self-review, append-only Q/A |
| market updates | thảo luận định hướng | review có timestamp/source/limitations và change request |

**Checkpoint:** đợi người dùng xác nhận lựa chọn course version OOP và activation/điều chỉnh candidate `MS-01`, không tạo bất cứ task hay history học tập nào trước khi có báo cáo thực tế.

---

<!-- Append future events BELOW. Do not edit EV-20261109-001. -->
