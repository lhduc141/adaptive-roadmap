# ADAPTIVE SE ROADMAP — PROMPT PLAYBOOK

**Companion guide to Roadmap v1.0.0** · Created: 2026-11-09  
This file is an optional prompt reference. It does not supersede `AGENT_ENTRY.md`, `docs/08_DATA_CONTRACT.md`, or `docs/03_CURRENT_STATE.md`.

## 0. What to provide

- **New conversation / reset:** latest full roadmap ZIP, or at least `AGENT_ENTRY.md`, `docs/08_DATA_CONTRACT.md`, `docs/03_CURRENT_STATE.md`, `docs/01_ROADMAP_MAIN.md`, `history/00_EVENT_INDEX.md`, and relevant recent logs.
- **Today / this week:** current state + recent history, plus real availability, energy, constraints; include `docs/04_EXECUTION_PROTOCOL.md` and `docs/07_TODOIST_BRIDGE.md` if accessible.
- **Course learning / assessment:** relevant `subjects/SUB-..._COVERAGE.md`, source syllabus/lectures, latest related diagnostic/session logs.
- **Update progress:** objective evidence (code, test output, explanation, written answer), whether AI helped, duration if known, difficulties and next checkpoint. Never send secrets or unauthorized work files.
- **Roadmap change:** current roadmap, history, requested change, reason, impact and recent market sources if market-related.

If working in a single continuing chat and files are still accessible, do not resend unchanged files. If a new chat is missing documents, attach the latest package or select the saved files explicitly.

## 1. Initialize / resume a new chat

> Tôi gửi bộ Adaptive SE Roadmap mới nhất. Đọc `AGENT_ENTRY.md`, `docs/08_DATA_CONTRACT.md`, `docs/03_CURRENT_STATE.md`, `docs/01_ROADMAP_MAIN.md`, `history/00_EVENT_INDEX.md` và các history / subject liên quan; áp dụng skill thích hợp nếu đọc được. Xác nhận version, event mới nhất, trạng thái verified, đề xuất chưa duyệt, blocker và next action. Nêu file thiếu/xung đột. Không tự tạo tiến độ, thay đổi milestone hoặc Todoist. Sau đó đề xuất một hành động tiếp theo phù hợp.

## 2. Today: one concrete action

> Dùng `adaptive-study-planner` theo bộ Roadmap mới nhất. Hôm nay tôi có khoảng **[... phút / không chắc]**, năng lượng **[thấp/vừa/cao]**, công việc bắt buộc **[...]**, điều đang vướng **[...]**. Hãy chọn **một việc quan trọng nhất**, một phương án nhẹ (hoặc nghỉ nếu phù hợp); ghi Objective, DoD, nguồn học, bằng chứng cần gửi lại và checkpoint. Không đặt deadline, không tự tạo task, không đổi state chỉ vì đã đề xuất.

## 3. This week: flexible outcomes

> Đọc current state, events và việc đang dở. Tuần này tôi dự kiến có **[ít/vừa/nhiều thời gian hoặc chưa biết]**, có các cam kết **[...]**. Đề xuất tối đa **hai learning outcomes**, không gán ngày thứ cụ thể; cho từng outcome: các next actions nhỏ, DoD, low-energy alternative, điều kiện dừng và việc ưu tiên nếu tuần bị gián đoạn. Phân biệt đề xuất mới và task đã Ready.

## 4. Start or continue a subject

> Dùng `subject-mastery-coach` cho **[SUB-OOP / SUB-DBMS / ...]**, topic **[...]**, learning pass **[Pass1/Pass2/Pass3/chưa rõ]**. Kiểm tra subject coverage và syllabus/source đang dùng; nêu prerequisite và full subject coverage còn thiếu. Hướng dẫn phần phù hợp. Nếu là Pass1, để tôi tự ôn và tự làm ví dụ. Nếu là Pass2, chỉ hỏi một câu/bài một lần, không đưa đáp án trước. Nếu Pass3, đào sâu misconceptions và cho bài kiểm chứng mới. Không tự đánh dấu subject complete.

## 5. Diagnostic: record exact answers

> Hãy tiến hành diagnostic cho **[subject/topic]** dựa trên môn và tài liệu đã xác định. Hỏi từng câu, chờ tôi trả lời. Với mỗi câu, giữ **nguyên văn** câu trả lời của tôi; nhận xét correct/partial/incorrect/uncertain, giải thích lý do, dùng rubric 0–4 khi có đủ evidence, ghi phần AI đã hỗ trợ. Cuối phiên, soạn bản ghi phù hợp `templates/DIAGNOSTIC_RECORD.md` và đề xuất bước ôn Pass3; không sửa history hoặc CURRENT_STATE khi chưa có quyền/yêu cầu rõ ràng.

## 6. Finish a session: log and apply change carefully

> Tôi vừa học **[subject/topic/pass]**. Tôi đã làm **[...]**, kết quả hoặc code/test **[...]**, khó khăn **[...]**, AI đã giúp **[mức độ]**, mức năng lượng **[...]**, thời gian thực tế **[.../không rõ]**. Hãy đối chiếu với DoD, phân biệt completed vs partial. Soạn một `LEARNING_SESSION_RECORD`, event ID hợp lệ nếu chưa trùng, bản cập nhật `CURRENT_STATE` và `history/00_EVENT_INDEX.md`. Cho tôi xem changelog/diff. Chỉ tuyên bố đã cập nhật tệp khi bạn thực sự ghi và kiểm tra được file; nếu không, xuất Markdown patch để tôi áp dụng.

## 7. Course / milestone audit

> Kiểm tra đủ toàn bộ subject/milestone **[...]** theo course contract đã thỏa thuận. Lập coverage matrix từng mandatory topic, Pass1/2/3 evidence, bài tổng hợp và applied milestone outcome. Nêu tất cả mục thiếu hoặc chưa verified. Chỉ đề xuất `verified_complete` nếu đạt đủ gate và có xác nhận người học; không suy ra từ việc đã xem slide, từng học IU hay đã làm project.

## 8. Market review / change request

> Dùng `market-signal-reviewer` rà soát bằng nguồn cập nhật, ưu tiên Việt Nam/TP.HCM và đúng cấp bậc early-career; tách job ads, employer surveys và forecasts. So sánh với baseline **[ngày]** trong roadmap. Cho biết công nghệ/kỹ năng nào tăng hoặc giảm nhu cầu, độ chắc chắn và tác động đến mục tiêu Backend, Java/NestJS/Go, Systems/Cloud, AI. Nếu cần đổi, xuất `CHANGE_REQUEST` có before/after/reason/evidence/impact; không tự sửa roadmap hay history khi tôi chưa chấp thuận.

## 9. Update personal context

> Thông tin mới về tôi: **[...]**. Hãy so sánh với `docs/05_CONTEXT_PROFILE.md` và hồ sơ gốc. Phân loại verified / self-reported / uncertain; nêu file, đoạn và nội dung cần sửa; cập nhật nếu tôi yêu cầu và tool cho phép, đồng thời ghi event nếu làm thay đổi kế hoạch/ưu tiên. Không tự coi kinh nghiệm mới kể là mastery đã đánh giá.

## 10. Restart after an interruption

> Tôi đã gián đoạn **[...]**. Đọc latest state và event mới nhất; tìm checkpoint còn giá trị, blocker và next action nhỏ nhất. Đừng cộng dồn task quá hạn hoặc yêu cầu học bù. Nếu trạng thái đã cũ/xung đột, nêu rõ và đề xuất một bước tái khởi động nhẹ; chỉ tăng scope khi tôi xác nhận có thời gian và năng lượng.

## 11. Safe handoff / file maintenance

- Use **latest accepted event** and `last_applied_event_id` rather than relying on ZIP modified date.
- Keep `history/*.md` append-only. Apply accepted event -> update `history/00_EVENT_INDEX.md` -> sync `docs/03_CURRENT_STATE.md` -> validate.
- Preserve stable IDs: milestone `MS-..`, subject `SUB-..`, diagnostic `DG-YYYYMMDD-NNN`, learning session `LS-YYYYMMDD-NNN`.
- If running without write access, output a proposed patch, not a false claim of saving.
- No confidential company code/data, client records, access tokens, credentials, or unauthorized attachments.
- One primary learning action per day request; at most two weekly outcomes; no fake due dates.

