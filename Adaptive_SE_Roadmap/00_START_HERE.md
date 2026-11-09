# ADAPTIVE SOFTWARE ENGINEERING ROADMAP — START HERE

**Bản phát hành:** `v1.0.0` · **Ngày khởi tạo:** `2026-11-09` · **Ngôn ngữ:** Vietnamese + technical English.
**Mục tiêu:** giúp người học/AI biết **đang hướng tới đâu → đang ở đâu → cần làm gì hôm nay/tuần này → đã thay đổi thế nào**; không biến roadmap thành thời khóa biểu cứng.

> Đây là **bộ hồ sơ khởi tạo**, KHÔNG phải bằng chứng đã bắt đầu học hoặc đạt bất cứ môn/milestone nào. Mọi tác vụ gợi ý đều là **PROPOSED**, chưa được thực hiện hoặc ghi vào Todoist.

## 1. Bản đồ thư mục

| Tài liệu | Trách nhiệm | Cập nhật khi nào |
|---|---|---|
| `AGENT_ENTRY.md` | Hướng dẫn bootstrapping AI mỗi lần nhận bộ hồ sơ | Khi giao thức đọc/ghi đổi |
| `docs/01_ROADMAP_MAIN.md` | Career direction, milestones, đích đến và tiêu chí closure | Chỉ khi quyết định thay đổi roadmap đã được duyệt |
| `docs/02_COMPETENCY_AND_COURSE_MAP.md` | Map năng lực ↔ môn IU/đề cương ↔ chủ đề ↔ minh chứng | Khi xác minh/đổi phạm vi môn |
| `docs/03_CURRENT_STATE.md` | Trạng thái hiện tại, WIP, focus, blockers, next actions và availability | Sau mỗi sự kiện thực tế/duyệt đề xuất |
| `docs/04_EXECUTION_PROTOCOL.md` | Quy tắc chọn việc ngày/tuần, học ba lượt và chống burnout | Khi cơ chế vận hành đổi |
| `docs/05_CONTEXT_PROFILE.md` | Snapshot cá nhân và dự án, links sang nguồn chi tiết | Khi người dùng bổ sung thông tin |
| `docs/06_MARKET_BASELINE.md` | Cơ sở thị trường, nguồn, tín hiệu, ngưỡng rà soát | Theo market review có chứng cứ |
| `docs/07_TODOIST_BRIDGE.md` | Mapping Roadmap → Todoist, KHÔNG tự coi là sync | Khi quy tắc Todoist được người dùng đổi |
| `docs/08_DATA_CONTRACT.md` | Quy tắc provenance, event, IDs, merge và phân quyền AI | Khi giao thức dữ liệu đổi |
| `history/00_EVENT_INDEX.md` | Danh mục sự kiện và thứ tự áp dụng | Cùng lúc với event mới |
| `history/01_CHANGELOG.md` | Quyết định/migration thay đổi: before → after → why → impact | Append-only |
| `history/02_DIAGNOSTICS.md` | Câu hỏi, câu trả lời **nguyên văn**, feedback, score, evidence | Append-only khi đã làm |
| `history/03_LEARNING_SESSIONS.md` | Kết quả buổi học, nguồn, lỗi, hành động kế | Append-only khi đã làm |
| `history/04_REVIEWS.md` | Weekly/market/energy reviews, quyết định | Append-only |
| `subjects/SUB-OOP_COVERAGE.md` | Ledger môn OOP ban đầu với từng topic, 3 lượt học và gate | Theo evidence sau khi bắt đầu |
| `templates/` | Mẫu record dùng điền ở tương lai, KHÔNG phải dữ liệu thật | Chỉ khi format đổi |
| `skills/*/SKILL.md` | Agent Skills để AI thực hiện workflow nhất quán | Version độc lập |
| `reference/` | File hồ sơ nguồn (bản sao tài liệu người dùng đã cung cấp) và chỉ mục IU | Chỉ cập nhật có provenance |
| `scripts/validate_docs.py` | Kiểm tra tính toàn vẹn cơ bản của hồ sơ | Chạy nếu môi trường hỗ trợ Python |

## 2. Thứ tự đọc bắt buộc (khi người dùng hỏi hôm nay/tuần này)

1. `AGENT_ENTRY.md` → `docs/08_DATA_CONTRACT.md`.
2. `docs/03_CURRENT_STATE.md` → `docs/01_ROADMAP_MAIN.md`.
3. `docs/04_EXECUTION_PROTOCOL.md` → `docs/02_COMPETENCY_AND_COURSE_MAP.md` (phần đang học).
4. `docs/05_CONTEXT_PROFILE.md` + bản gốc `reference/Detail-Information.md`, `reference/My_Projects.md` nếu cần chi tiết.
5. `history/00_EVENT_INDEX.md` + các entry gần nhất trong change/diagnostic/session/review liên quan.
6. Với lịch cụ thể phải xác nhận lịch/availability; nếu không có, đề xuất theo ba kịch bản năng lượng, KHÔNG giả định lịch trống.

Chỉ đọc toàn bộ kho tài liệu IU khi chuẩn bị **học môn cụ thể** hoặc kiểm tra toàn bộ course coverage. Đừng tải lại hàng MB mỗi lần hỏi 20 phút học gì.

## 3. Cách yêu cầu AI trong tương lai (có thể sao chép)

**Ngày:** “Hãy nạp `AGENT_ENTRY.md` và các tài liệu bắt buộc. Theo trạng thái, lịch/sức lực tôi cung cấp, cho tôi 1 việc chính và 1 phương án nhẹ cho hôm nay. Không thay trạng thái hoặc ghi lịch sử nếu tôi chưa báo đã làm.”

**Tuần:** “Đọc bộ roadmap, diagnostic/session gần nhất và Todoist bridge. Đề xuất tối đa 2 learning outcomes cho tuần này, theo mức năng lượng. Chỉ dùng task có trạng thái Ready hoặc đề xuất rõ ràng.”

**Học:** “Dùng skill `subject-mastery-coach` cho môn `[mã]`, chủ đề `[mã]`. Tôi đang ở lượt `[1/2/3]`. Hướng dẫn theo phạm vi, không đưa đáp án trước bài diagnostic.”

**Ghi lịch sử:** “Tôi đã làm X, kết quả Y, câu trả lời Z. Dùng skill `roadmap-history-manager` chuẩn bị change/session/diagnostic record và patch trạng thái; cho xem diff trước khi áp dụng nếu chưa có quyền sửa file.”

**Review thị trường:** “Dùng skill `market-signal-reviewer` rà soát các JD và báo cáo mới; đề xuất change request, không tự đổi career direction.”

## 4. Cách chuyển file giữa các AI

- **Cách ổn định nhất:** giải nén, giữ nguyên cây thư mục; gửi `AGENT_ENTRY.md`, `docs/01...`, `docs/03...`, `history/00...` và file history mới nhất. Với học môn cụ thể, gửi thêm `docs/02...` và bộ nguồn tương ứng.
- Nếu nền tảng nhận ZIP và đọc được, gửi cả ZIP. **Đừng giả định mọi AI tự giải nén hoặc tự kích hoạt các skill.** Khi không có chức năng cài Skills, hãy đính kèm `SKILL.md` liên quan và yêu cầu AI áp dụng.
- Để giảm số file upload, có thể chỉ gửi 4 file: `AGENT_ENTRY`, `ROADMAP_MAIN`, `CURRENT_STATE`, `history` liên quan; AI phải báo thiếu nếu không có thông tin để đánh giá chính xác.
- Người dùng là nguồn xác nhận cuối cùng. AI không được tự tạo tiến độ, việc đã làm, câu trả lời hay điểm số.

## 5. Cơ sở thiết kế

- `reference/Todoist_document.md` v1.3.0: 5 project hiện có, 18 nhãn, 3 filters, quy tắc không deadline giả và WIP nhẹ.
- `reference/Detail-Information.md`, `reference/My_Projects.md`, `reference/Core-Plan.md`: hồ sơ năng lực/dự án và kế hoạch lịch cứng cần thay thế.
- `reference/IU_COURSE_INDEX.md`: chỉ mục từ báo cáo kho tài liệu IU, **không phải syllabus chính thức**.
- Nguồn tham khảo bên ngoài: [Agent Skills specification](https://openagentskills.dev/docs/specification), [SFIA 9](https://sfia-online.org/en/sfia-9/responsibilities), [CS2023](https://csed.acm.org/knowledge-areas/), [ITviec 2026](https://itviec.com/blog/bao-cao-tac-dong-ai-tuyen-dung-it-viet-nam-2026/).
