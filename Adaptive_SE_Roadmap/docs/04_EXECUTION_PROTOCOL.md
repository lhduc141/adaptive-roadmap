# EXECUTION PROTOCOL — FROM ROADMAP TO TODAY/WEEK

## 1. Vận hành theo kết quả, không theo giờ cố định

Dựa trên `CURRENT_STATE`, chọn những tasks có thể bắt đầu hoặc một **proposed** task nhỏ nhất khi không có Ready task. Không ép học mỗi ngày, không nợ giờ; ngày nghỉ là hợp lệ.

**Một chu kỳ học:** 1 primary technical learning unit + tối đa 1 supporting technical unit. English tích hợp vào những việc đã học, không mở full curriculum song song. Work/GLV/Self & Life lấy ưu tiên thực tế cao hơn nếu có deadline thật.

### Input planner (có thể không đầy đủ)

- `scope`: today / this_week / resume / overloaded.
- `available_time`: tự nguyện cung cấp; không bắt buộc (ví dụ 15 phút / khoảng 45 phút / phiên sâu).
- `energy`: low / medium / high / unknown.
- `real_commitments`: việc có deadline thực tế hoặc lịch GLV/work người dùng cung cấp.
- `current_state` + recent history (diagnostic, last failure, changed priorities).

Nếu thiếu availability, **đưa 3 mức lựa chọn**; không khẳng định giờ trống. Nếu workload nhiều/energy thấp, trả lời một micro task hoặc nghỉ hợp lệ. Trường hợp không có READY task, đề xuất `PROP-*` và nói rõ “chưa được duyệt/tạo trong app”.

## 2. Decision algorithm (deterministic where evidence exists)

1. Đọc `last_applied_event_id`, các event mới hơn; nếu mismatch → nêu `sync needed` trước khi quyết định dựa trên tiến độ cũ.
2. Ưu tiên **deadline thực tế Work/GLV** đã xác nhận. Không tự phát sinh deadline.
3. Nếu có `in_progress`, chọn **next small action** trong unit đó. Tránh mở unit mới khi có WIP.
4. Nếu không có active: chọn từ `ready`; nếu vẫn không có thì lấy 1 `proposed` thuộc candidate primary milestone.
5. Nếu diagnostic gần nhất có misconception, chọn reinforcement/recall tương ứng trước khi chuyển topic.
6. Điều chỉnh phạm vi với mức năng lượng, không đổi career direction do 1 ngày mệt.
7. Xuất mỗi action: `ID | lý do | thời lượng tùy chọn | việc thực hiện | output/DoD | cách báo lại | Todoist routing | độ chắc chắn`.
8. Chỉ sau khi user báo hoàn thành mới ghi LS/DG & update state; nếu user yêu cầu cập nhật trực tiếp, kiểm tra file/tool khả dụng và permission.

## 3. Output ngày (không hơn 1 chính + 1 optional)

**Trả lời theo cấu trúc:**

- **Vị trí hiện tại (verified):** trạng thái gì đã chắc chắn.
- **Việc quan trọng nhất:** 1 action nhỏ (hoặc đề xuất nếu chưa có Ready).
- **Nếu ít năng lượng:** phiên 10–20 phút hoặc nghỉ.
- **Nếu có thêm năng lượng:** một bước mở rộng hợp lý, không làm phát sinh thứ tự bắt buộc.
- **DoD/Minh chứng:** rõ output nhỏ, không nói “học hết chương”.
- **Checkpoint:** user gửi nội dung gì để AI cập nhật history.

**Ví dụ MINH HỌA từ snapshot khởi tạo:**

| Năng lượng | Đề xuất chưa duyệt | Kết quả |
|---|---|---|
| Low | Đọc/ôn 1 khái niệm class/object từ nguồn OOP đã có; ghi 2 điều tự nhớ và 1 câu chưa chắc; hoặc nghỉ | Ghi chú nhỏ, không ghi topic validated |
| Medium | Tự viết ví dụ Java class/object/encapsulation và giải thích 2 design choices; hoặc rà soát 3–5 chủ đề từ slide OOP | Code/notes + câu còn vướng, chưa tính course complete |
| High | Audit phạm vi toàn bộ OOP theo slide/lab/exam rồi làm thử một bài nhỏ OOP-01 | Topic inventory có source + code tự làm; chưa tự chuyển milestone active |

Đây **không phải kế hoạch đã được người dùng nhận làm**, và không giả định người dùng có thời gian trống ngày 09/11.

## 4. Output tuần (outcome menu, không lịch theo thứ)

- `Week context`: ngày/tuần, commitments đã xác nhận; nếu không có, không tự gán ngày thứ Hai/Chủ nhật.
- `Maximum 2 outcomes`, ưu tiên hoàn thành phần đang dở; mỗi outcome có 1–3 next actions nhỏ và optional energy modes.
- `Carry-over` chỉ giữ outcome còn quan trọng; không chuyển mọi task chưa làm thành overdue.
- `Stop condition`: nếu workload biến động hoặc việc học tăng stress, giảm scope/cho phép pause.
- `Review trigger`: khi có session thực tế hoặc cuối chu kỳ người dùng muốn review, không nhất thiết đúng Chủ nhật.

**Ví dụ tuần đầu MINH HỌA (không phải lịch cam kết):** outcome A chốt `SUB-OOP` scope; outcome B bắt đầu Pass1 OOP-01 khi nguồn đã chọn. English lồng vào giải thích ngắn; không add Go, Python, Spring, DSA, Kubernetes như các track full song song.

## 5. Three-pass mastery protocol — theo mong muốn người học

### PASS 1 — Self Review (tự ôn lần đầu)

- Mục tiêu: phục hồi kiến thức toàn bộ subject theo outline; đọc/ôn độc lập, ghi quick notes, làm example nhỏ.
- Chưa đưa test khó tràn lan; không phát sinh chục task con trước khi user sẵn sàng.
- Output: bảng topic status `reviewed`, những chỗ chưa hiểu, link source, 1–2 ví dụ.

### PASS 2 — Lightweight Diagnostic (theo topic)

- Chỉ hỏi **1 câu một lần** hoặc một bài tập nhỏ tương ứng các topic vừa ôn. Phân biệt concept, application, debugging, trade-off.
- Không đưa đáp án trước; ghi câu trả lời nguyên văn, rubric 0–4, feedback có evidence.
- Mục tiêu là tìm lỗ hổng **để điều chỉnh Pass 3**, không tạo một kỳ sát hạch mọi môn đại học.
- Có thể đánh giá tích lũy từng topic, không cần chờ ôn xong toàn bộ chương trình.

### PASS 3 — Deep Reinforcement + Transfer

- Ôn lại những topic có lỗ hổng, học sâu/tradeoffs, làm bài tập/lab, tự giải thích, viết tests, sửa lỗi.
- Kết thúc topic: independent task/unseen variant, proof, recorded mistakes + next revisit cue.
- Dùng spaced recall khi thuận tiện, không biến thành lịch deadline bắt buộc.

### FINAL COURSE / MILESTONE AUDIT

- **Course:** toàn bộ mandatory chapters + biến thể đã chốt, đủ 3 pass/evidence, bài tổng hợp, trạng thái `verified_complete (scope)`.
- **Milestone:** course anchor full **và** applied milestone outcome demonstrated; người dùng duyệt, event closure, snapshot đồng bộ.
- Không chỉ làm 1 mini-project hoặc xong 1 môn là tự đóng MS nếu thiếu điều kiện còn lại.

## 6. AI use policies

- **Learning/Independent:** người học tự attempt/sơ đồ giải pháp trước; khi bí, AI gợi ý theo mức hint, không dump full solution; review code sau khi hoàn thành. Nếu AI-assisted, đánh dấu evidence là assisted.
- **Production/Work:** AI có thể giúp code/test/research theo policy nơi làm việc; không chia sẻ dữ liệu cấm, tự review/validate.
- **Error handling:** nếu không có dữ liệu mới, AI không được bịa session; có thể cho 1 bài học/gợi ý nhưng không được tự log nó là done.

## 7. Anti-burnout rules

- Low energy = một bước nhỏ hoặc nghỉ, không mắc nợ.
- Không đưa 1–2 bài LeetCode mỗi ngày như quy định; DSA là subject/skill cần luyện có đích.
- Chỉ cập nhật trọng tâm khi có trường hợp rõ: workload, priority, major market signal, user preference; ghi lý do vào history.
- Khi người dùng thấy quá tải, giảm WIP và scope trước khi tăng mục tiêu; không phán xét.
