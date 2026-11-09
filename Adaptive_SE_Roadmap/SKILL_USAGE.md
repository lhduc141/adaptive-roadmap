# CÁCH DÙNG 5 SKILLS VỚI CHATGPT / GEMINI / CLAUDE / AGENT KHÁC

**Tệp đã tạo là các Agent Skills dạng `SKILL.md`, KHÔNG phải các skill đã được cài đặt vào tài khoản của bạn.** Một số nền tảng cho phép cài một thư mục skill để agent tự phát hiện qua `name/description`; nền tảng khác chỉ đọc được khi bạn đính kèm tệp hoặc dán phần hướng dẫn.

## 5 skills

| Skill | Khi nào dùng |
|---|---|
| `roadmap-context-loader` | Khi mở phiên làm việc mới hoặc gửi lại docs, AI phải nắm tình trạng |
| `adaptive-study-planner` | “Hôm nay/tuần này tôi nên làm gì?” và tiếp tục sau khi nghỉ |
| `subject-mastery-coach` | Học môn cụ thể, diagnostic, chấm câu trả lời, full course audit |
| `roadmap-history-manager` | Ghi session, câu trả lời, bản sửa, migration/decision, diff |
| `market-signal-reviewer` | Khảo sát job market/AI, đề xuất điều chỉnh roadmap |

## Quy tắc cài / vận hành

1. Đọc [Agent Skills specification](https://openagentskills.dev/docs/specification) về file SKILL.md có YAML `name` và `description`.
2. Nếu sản phẩm bạn dùng có **tính năng cài custom Skills**, dùng tính năng đó để cài từng thư mục `skills/<name>/` theo hướng dẫn của ứng dụng, **không cần đưa toàn bộ profile vào nội dung skill**.
3. Nếu không có khả năng cài, hãy gửi `AGENT_ENTRY.md` và một `SKILL.md` tương ứng cùng các docs cần đọc; có thể dùng câu “Áp dụng skill này để ...”.
4. Skills **không tự cấp quyền đọc OneDrive, sửa Todoist hoặc ghi file**. Cần user upload/connector và quyền phù hợp; nếu không có, AI phải trả patch chứ không khẳng định đã sync.
5. Cập nhật skill khi workflow đổi, nhưng việc đang học và diagnostic mới nằm ở `docs/03_CURRENT_STATE.md` và `history/`, không phải sửa skill mỗi ngày.

## 3 thử nghiệm chấp nhận (self-tests)

**TEST-A — Fresh boot:** Chỉ gửi bundle, hỏi “Tôi đang ở đâu?” → nói MS-01 candidate, **chưa có học/diagnostic**, việc tiếp theo là chốt nguồn OOP; không bịa progress.

**TEST-B — Quá bận:** “Tuần này GLV/work nhiều, tôi còn 15 phút hôm nay” → đề xuất một micro-action hoặc nghỉ; không gán deadline, không mở Go/AI thêm.

**TEST-C — Diagnostic:** “Tôi vừa tự ôn OOP-03, hỏi tôi một câu” → đặt **một** câu, chờ trả lời; sau đáp án mới chấm, lưu nguyên văn, xác định lỗi; không tự kết luận môn hoàn thành.

**TEST-D — Change:** “Tôi quyết định ưu tiên Go trước Java” → chuẩn bị CR impact, chỉ áp dụng khi user xác nhận nội dung thay đổi, append event giữ lại history.

**TEST-E — Tính toàn vẹn:** State nói completed nhưng không có closure event/coverage → nêu conflict, không tự hợp thức hóa.

## Mẫu hội thoại khi muốn tiếp tục

> Tôi gửi bộ Adaptive SE Roadmap. Hãy đọc `AGENT_ENTRY.md`, dùng skill phù hợp theo mục tiêu buổi này, và không suy diễn tiến độ. Tôi muốn [lên việc hôm nay / học Java / lưu diagnostic / market review]. Dữ liệu mới của tôi là: [...].
