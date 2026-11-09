# CURRENT STATE — MATERIALIZED SNAPSHOT

```yaml
schema_version: "1.0.0"
snapshot_as_of: "2026-11-09"
last_applied_event_id: "EV-20261109-001"
roadmap_version: "1.0.0"
status: "bootstrap_no_learning_started"
career_direction: "Backend Software Engineer"
primary_candidate_milestone: "MS-01"
primary_candidate_subject: "SUB-OOP"
active_milestone_id: null
active_subject_id: null
active_learning_unit_ids: []
current_subject_pass: null
verified_completed_milestones: []
verified_completed_subjects: []
most_recent_diagnostic_id: null
most_recent_learning_session_id: null
availability: "unknown"
energy: "unknown"
workload: "unknown"
source_quality: "self-report plus docs; no independent diagnostic"
```

> Tính đến lúc bootstrap, **không có bằng chứng đã bắt đầu học theo roadmap mới**. Project cũ và kinh nghiệm đã có vẫn được ghi nhận trong PROFILE, nhưng không biến thành `done` của milestone mới.

## 1. Milestone state (không có completion inferred)

| Milestone | State | Course anchor | Pass | Evidence | Next decision |
|---|---|---|---|---|---|
| `MS-01` | `candidate` | `SUB-OOP` | chưa bắt đầu | profile: Java basic; chưa đánh giá | Phê duyệt activation + chọn course version/source |
| `MS-02` | `not_started` | `SUB-DSA` | chưa bắt đầu | đã học DSA ở IU, chưa audit | Để backlog |
| `MS-03` | `not_started` | `SUB-DBMS` | chưa bắt đầu | SQL thực hành tốt, chưa full audit | Có thể lấy ví dụ từ ParadiseHR khi mở |
| `MS-04` | `not_started` | `SUB-OS` | chưa bắt đầu | self-reported gap | Để backlog |
| `MS-05` | `not_started` | `SUB-CN` | chưa bắt đầu | từng học networks/Go TCP | Để backlog |
| `MS-06` | `not_started` | `SUB-SE` | chưa bắt đầu | kinh nghiệm SE thực tế | Để backlog |
| `MS-07` | `not_started` | chưa chọn | chưa bắt đầu | Applied AI project; chưa research track selection | Chọn khi phù hợp |

## 2. Focus / WIP

- **Đang học (confirmed):** *Không có learning unit nào được người dùng xác nhận active*.
- **Candidate:** `MS-01/SUB-OOP` (Java + OOP) dựa trên định hướng mong muốn.
- **Support option:** `SUB-DBMS` — transactions/concurrency; đây là **đề xuất**, không phải subject active.
- **English:** mục tiêu xuyên suốt, chưa có buổi học hoặc lịch cố định được ghi nhận.
- **Job/career operation:** không tự khẳng định đang ứng tuyển hoặc cần nộp CV tuần này.

## 3. Hành động đề xuất khởi động (chưa được tạo trong Todoist)

| Proposed ID | Độ ưu tiên | Hành động | Điều kiện chấp thuận | DoD | Todoist |
|---|---|---|---|---|---|
| `PROP-BOOT-001` | Primary | Chọn bộ tài liệu OOP IU chuẩn (năm/giảng viên nếu có), tạo `SUB-OOP` coverage ledger | User xác nhận muốn active MS-01 | Có chapter/lecture/lab/exam inventory và variant list | `Developer / Ready` **chỉ sau khi duyệt** |
| `PROP-BOOT-002` | Primary successor | Self-review (Pass 1) OOP-01: Java class/object/encapsulation | Có thể bắt đầu song song khi người dùng chọn học OOP; chưa xác nhận full syllabus thì không đóng môn | Giải thích, viết ví dụ code nhỏ và ghi câu còn vướng | Chưa tạo |
| `PROP-BOOT-003` | Optional support | Nêu lại một case transaction/locking (đã ẩn dữ liệu thật) trong Stored Procedure | Khi rảnh và cần liên hệ Work → Developer | Có giả định + câu hỏi concurrency + plan kiểm chứng | Chưa tạo |
| `PROP-BOOT-004` | Optional English | Giải thích kỹ thuật 3–5 phút (nói/viết) về OOP hoặc DB transaction | Sau khi đã có topic học | Có bản ghi chú/recording tự quản lý và cải thiện 1–2 điểm | Chưa tạo |

**Không gán deadline hoặc thời gian hoàn thành.** Các mục này là seed để AI chọn việc theo năng lượng, không có nghĩa bạn bắt buộc làm ngay tất cả.

## 4. Blockers / unknowns

- Chưa biết **lịch bận/ngày rảnh và mức năng lượng hiện tại**. Khi được hỏi “hôm nay làm gì”, nếu chưa cung cấp chỉ đưa 3 lựa chọn (low/medium/deep), không dựng lịch giả.
- Chưa chốt nguồn môn `SUB-OOP` phiên bản nào là canonical; danh sách topic đang là bản tái dựng từ nhiều bộ.
- Không có diagnostic answers/marks hay session logs mới; thiếu evidence nên không xếp hạng mastery.
- Chưa xác minh Todoist task inventory/current status trong app. Chỉ có baseline thông số và quy ước của `reference/Todoist_document.md`.
- Không có kết quả market review mới sau baseline 09/11/2026; không tự thay đổi định hướng dựa trên kiến thức chung.

## 5. Handoff token — cập nhật khi có sự kiện thực tế

- `last_verified_action`: none since bootstrap
- `active_next_action`: none confirmed (candidate `PROP-BOOT-001`)
- `where_to_resume`: thống nhất source OOP → chọn LU đầu tiên → Pass 1 self review
- `next_allowed_mutation`: người dùng xác nhận activation hoặc cung cấp kết quả buổi học; ghi event rồi cập nhật snapshot
- `last_history_check`: `history/00_EVENT_INDEX.md` `EV-20261109-001`

### Quy tắc ghi trạng thái

Sau mỗi learning session/diagnostic/chấp thuận thay đổi: append history trước, rồi cập nhật snapshot. `CURRENT_STATE` không phải nơi viết nhận xét dài hoặc Q/A; liên kết đến event để audit.
