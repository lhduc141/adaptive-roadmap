# HISTORY EVENT INDEX — APPEND-ONLY

| Order | Event ID | Date / precision | Type | Entity | Log file | Applied to snapshot? | Remark |
|---|---|---|---|---|---|---|---|
| 001 | `EV-20261109-001` | 2026-11-09 / day | `BOOTSTRAP` | `SE-ADAPTIVE-2026` | `history/01_CHANGELOG.md` | YES | Tạo bộ tài liệu; chưa học, chưa diagnostic, các milestone là đề xuất khởi tạo |

**Latest applied event:** `EV-20261109-001` · `CURRENT_STATE.last_applied_event_id` phải trùng. Khi thêm event sau, tăng `NNN` theo cùng ngày; không tái sử dụng ID, không viết đè entry cũ. Timestamp giờ phút để `unknown` khi không được cung cấp, không tự suy diễn.

**Other logs hiện tại:** `02_DIAGNOSTICS` = no entries; `03_LEARNING_SESSIONS` = no entries; `04_REVIEWS` = no user-confirmed review events.
