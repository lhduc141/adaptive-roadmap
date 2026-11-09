# DATA CONTRACT — SOURCE OF TRUTH, VERSIONING & HISTORY

## 1. Vai trò dữ liệu

- `docs/01_ROADMAP_MAIN.md`: kế hoạch **đích đến/milestones**, không phải trạng thái đã học.
- `docs/03_CURRENT_STATE.md`: **materialized snapshot** (như một bảng trạng thái hiện tại được cập nhật từ sự kiện đã chấp thuận).
- `history/*.md`: **append-only evidence/event records**, giống migration/audit log. Không viết đè lịch sử.
- `docs/02_COMPETENCY_AND_COURSE_MAP.md`: syllabus/coverage contracts; `reference/` chứa tài liệu gốc được cung cấp, không đồng nghĩa năng lực.
- `templates/`: chỉ là mẫu, tuyệt đối không tính là trải nghiệm/diagnostic thật.

## 2. Source precedence / conflict resolution

Nguồn xác nhận mạnh nhất: (a) user statement/evidence gần nhất trong cuộc trò chuyện; (b) log sự kiện đã được duyệt, có timestamp; (c) current state khớp event cuối; (d) main/subject contract; (e) nguồn hồ sơ; (f) đề xuất chưa duyệt; (g) giả định của AI.

Nếu Current State nói done nhưng history không có evidence: ghi `CONFLICT — NEEDS_RECONCILIATION`; không âm thầm đánh dấu done. Nếu history mới hơn current state: nêu cần `REPLAY/SYNC`, không tự coi snapshot là latest.

## 3. ID ổn định

- Milestone: `MS-01`, `MS-02`, ...; không đổi ID khi đổi tên.
- Subject: `SUB-OOP`, `SUB-DSA`, `SUB-DBMS`, `SUB-OS`, `SUB-CN`, `SUB-SE`.
- Competency: `CMP-CODE`, `CMP-DATA`, `CMP-BACKEND`, ...
- Learning Unit: `LU-SUB-OOP-001`, `LU-SUB-DBMS-001` ...; chỉ sinh thêm khi thật sự cần.
- Event: `EV-YYYYMMDD-NNN`; Change Request: `CR-YYYYMMDD-NNN`; diagnostic: `DG-YYYYMMDD-NNN`; session: `LS-YYYYMMDD-NNN`; review `RV-YYYYMMDD-NNN`.
- Các ID trong `templates/` là **placeholders**; chưa thực thi.

## 4. Trạng thái hợp lệ

- Roadmap milestone: `not_started | candidate | active | paused | validation | completed | superseded`.
- Subject/course: `not_started | pass1_self_review | pass2_diagnostic | pass3_reinforcement | validation | verified_complete`.
- Unit: `backlog | ready | in_progress | validation | completed | on_hold`.
- Proposed tasks: `proposed` (nằm ngoài state active; KHÔNG quy đổi thành `ready` nếu chưa được phê duyệt).
- Knowledge evidence: `self_reported | observed | assessed | unverified`.

## 5. Migration/Change event bắt buộc

Một event hợp lệ chứa: `event_id`, `timestamp (+07:00) nếu được biết, hoặc date + time_precision=day nếu giờ chưa được cung cấp`, `actor`, `type`, `entity_id`, `before`, `after`, `reason`, `evidence_refs`, `decision_status`, `affected_files`, `checkpoint`. Với thay đổi lớn cần liên kết `change_request_id`, thị trường thì ghi nguồn/ngày/cấp bậc/vùng/mẫu/giới hạn.

Cập nhật được thực hiện theo thứ tự có thể audit:

1. AI đề xuất change request (nêu diff). User duyệt (hoặc trực tiếp ra lệnh sửa).
2. Ghi event mới vào changelog/history đúng loại; **không sửa event cũ**.
3. Cập nhật `MAIN`/`COURSE_MAP` nếu đổi kế hoạch; cập nhật `CURRENT_STATE` nếu thay trạng thái.
4. Cập nhật `history/00_EVENT_INDEX.md` và `last_applied_event_id` trong `CURRENT_STATE`.
5. Kiểm tra ID, trạng thái, DoD, source; nếu có xung đột thì dừng thay đổi đó và yêu cầu reconcile.

Khi không có công cụ ghi file: xuất **patch/record Markdown** để người dùng lưu. Không tuyên bố đã ghi vào file hay đã tạo task Todoist.

## 6. Diagnostic và assessment evidence

- Không tự dựng câu trả lời người học. Q/A phải ghi **nguyên văn** (chỉ bỏ thông tin bí mật nếu cần và ghi lý do).
- `response_status`: `answered | skipped | not_asked`.
- Thang 0–4: `0` chưa biết, `1` nhận diện khi gợi ý, `2` tự giải thích + ví dụ, `3` vận dụng bài quen thuộc, `4` giải bài mới + trade-off + kiểm chứng. `null` khi chưa đánh giá.
- Feedback tách `correct`, `partial`, `incorrect`, `uncertain`, kèm lý do, misconceptions, evidence, follow-up.
- Nếu AI đã lỡ gợi ý đáp án trước, đánh giá có thể mất tính độc lập: đánh dấu `assisted` và giảm mức chứng cứ, **không tự cho score 4**.
- Lịch sử lần diagnostic cũ được giữ nguyên; lần mới bổ sung entry, không ghi đè điểm cũ.

## 7. Mastery / course-completion gate

**Không thể đánh dấu `verified_complete` một môn nếu thiếu một trong các điều kiện:**

1. Syllabus/course contract được xác định (phiên bản, nguồn, topic inventory, phạm vi chính thức hay tái dựng).
2. **Tất cả chủ đề bắt buộc** của khóa học đã có trạng thái `covered+validated`; các chủ đề biến thể/nguồn chưa rõ phải được đánh dấu, không lờ đi.
3. Pass 1 self-review được ghi; Pass 2 diagnostic theo topic có evidence; Pass 3 reinforcement sau diagnostic được ghi.
4. Có **tổng kiểm tra tích hợp** độc lập gồm giải thích + bài tập / lab / ứng dụng + xử lý một bài toán chưa gặp.
5. Tồn tại session/diagnostic/artifact refs và milestone closure decision được người dùng duyệt.

Nếu nguồn chỉ là **báo cáo tái dựng** không phải syllabus chính thức, trạng thái chứng nhận chỉ được viết là `verified_complete (agreed reconstructed scope)`; KHÔNG viết “đã hoàn tất môn IU chính thức”.

## 8. Idempotency & privacy

- Nếu nhận lại cùng event/diagnostic ID, không append trùng; kiểm tra record đã có.
- Nếu có bản zip cũ và patch mới, ưu tiên latest event đã được chấp thuận, không dùng ngày sửa file để suy ra kết quả học.
- Không lưu source nội bộ không được phép, mật khẩu, token, dữ liệu khách hàng; chỉ lưu mã task, hướng xử lý đã khái quát hóa, artifact được phép chia sẻ.
- Tự đánh giá năng lực KHÔNG phải dữ liệu kiểm chứng; tách `self_reported` khỏi `assessed`.
