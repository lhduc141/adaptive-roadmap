---
title: "Todoist Personal Operating System — Master Specification"
version: "1.3.0"
status: "CONFIGURATION BASELINE — 18 UI-confirmed labels; filters frozen; task-authoring and AI-agent contract defined; no roadmap started"
last_updated: "2026-11-09"
source_of_truth: "This Markdown file (manual maintenance)"
app: "Todoist Beginner (Free)"
language: "vi-VN"
---

# TODOIST PERSONAL OPERATING SYSTEM
## Tài liệu cấu hình & vận hành dài hạn (Master Specification)

> **Mục đích:** Đây là tài liệu gốc để chuẩn hóa cách tổ chức **Projects → Sections → Tasks/Subtasks → Labels/Priority → Filters** trong Todoist. Sử dụng khi tạo task, cập nhật quy trình, thêm label, thay đổi filter, chuyển công việc giữa các lĩnh vực, hoặc xây roadmap học tập sau này.
>
> **Phân biệt rõ:** `✅ Đã xác nhận qua ảnh` · `📋 Đã thống nhất về thiết kế` · `🔎 Chưa kiểm chứng trực tiếp trên tài khoản` · `🧪 Đề xuất để thử`.
>
> **Trạng thái khi lập tài liệu (09/11/2026):** Người dùng **chưa bắt đầu triển khai roadmap học tập**. Không đánh dấu bất kỳ bài học nào là đã hoàn thành; không coi bản kế hoạch bên dưới là năng lực đã được kiểm chứng.

---

## 0. Executive Summary — Đọc phần này khi cần khởi động lại

- **5 lĩnh vực:** `Developer`, `English`, `Work` (trước đây gọi là `Working`), `GLV`, `Self & Life`.
- **Developer:** Backend-first; củng cố Computer Science, khôi phục năng lực tự code; **thứ tự mong muốn mới nhất là Java → NestJS → Go** (cần diagnostic để chốt độ sâu, nhịp và mức ôn song song). Frontend chủ yếu ôn và duy trì.
- **Career/Job Search:** thuộc `Self & Life`; technical interview practice có thể thuộc `Developer`; việc thực tế đã nhận làm thuộc `Work`.
- **Todoist Board:** `Developer` và `Work` dùng Section theo **trạng thái**; ba project còn lại dùng **List** theo **nhóm trách nhiệm/kỹ năng**.
- **Labels đã xác nhận qua ảnh mới nhất (18/18):** `paradise`, `event`, `follow_up`, `engineering`, `interview`, `go`, `java`, `nestjs`, `no_ai`, `backend`, `database`, `devops`, `dsa`, `frontend`, `integration`, `security`, `systems`, `testing`. Màu được đối chiếu với dropdown thực tế và danh mục màu Todoist API; chi tiết ở Chương 4.
- **GLV:** sections theo trách nhiệm thực tế: `Lớp Thêm Sức 3B`, `Khối TS`, `Ban Trực`, `Công việc chung`. **ParadiseHR:** công việc trong `Work` dùng label nguồn **`paradise`** (đã tạo trên Todoist), không đổi ngầm thành `source_paradisehr`. Khi có đơn vị mới, tạo label nguồn riêng chỉ khi có công việc thực tế.
- **Filters hiện tại (3):** `Next Actions`, `Independent Practice`, `Pending & Follow-ups` — **giữ nguyên, không thêm hoặc điều chỉnh trong giai đoạn chuẩn bị**. Query thực tế chưa xác nhận trực tiếp.
- **Phần lớn task không có ngày đến hạn:** chỉ gán ngày khi có cam kết, hạn thực tế hoặc tự nguyện lập kế hoạch cho ngày đó. Không dùng deadline giả để tạo áp lực.
- **Workflow vận hành:** `Capture → Clarify → Organize → Execute → Update/Review` với thời điểm linh hoạt.
- **Quy tắc kiểm soát:** 18 labels là **ảnh chụp cấu hình hiện tại** (không có nghĩa task nào cũng cần nhãn). Chỉ bổ sung label thứ 19 khi có nhu cầu truy xuất thực tế; không tạo nhãn cho từng màn hình, hàm SQL, ngôn ngữ hay sinh hoạt cá nhân. **Task title/description/subtask/comment** có chuẩn riêng tại Chương 7 và **hợp đồng Gemini** tại Chương 15.

### Bộ công cụ nào làm gì?

| Thành phần | Câu hỏi nó trả lời | Không dùng để |
|---|---|---|
| Project | Đây là trách nhiệm/lĩnh vực nào? | Mỗi bài học hoặc từng công ty ứng tuyển |
| Section | Task đang ở bước nào (Board), hoặc thuộc nhóm nào (List)? | Vừa lưu trạng thái vừa lưu toàn bộ chuyên ngành cùng lúc |
| Task | Kết quả độc lập cần hoàn thành là gì? | Ghi một mục tiêu khổng lồ như “Học hết Backend” |
| Subtask | Các bước tạo ra kết quả của task | Chia đến mức thao tác 1 phút vô nghĩa |
| Label | Thuộc tính **xuyên project/section** giúp truy hồi/lọc | Lặp lại toàn bộ project hoặc trạng thái đã có |
| Priority | Việc nào cần được ưu tiên **hiện tại**? | Chỉ độ khó, độ dài, hay đánh giá giá trị con người |
| Date | Có sự kiện/hạn phải chú ý ngày nào? | Bắt học mỗi ngày đúng giờ khi lịch không ổn định |
| Filter | Tôi muốn nhìn **nhóm task nào từ nhiều nơi**? | Làm nơi lưu dữ liệu độc lập hoặc thay thế project |

---

## 1. Mục tiêu và giới hạn thiết kế

### 1.1. Mục tiêu cá nhân đã xác nhận

1. **Khôi phục năng lực Software Development độc lập:** phân tích, thiết kế, viết code, debug, kiểm thử, lý giải quyết định kỹ thuật trước khi tham khảo AI.
2. **Phát triển sự nghiệp:** tìm vị trí Backend/Full-stack phù hợp; ưu tiên Backend nhưng không đánh mất năng lực Full-stack.
3. **Nâng tiếng Anh phục vụ công việc:** nền tảng IELTS 5.5; ưu tiên khả năng sử dụng trong giao tiếp chuyên môn và phỏng vấn.
4. **Duy trì công việc thực tế:** đang thực tập Paradise HR, trọng tâm SQL/Stored Procedure và HTML/CSS/JavaScript theo kiến trúc hiện có.
5. **Duy trì GLV và Self & Life:** nhiệm vụ giáo lý viên, sức khỏe, gia đình/không gian sống, tài chính, sinh hoạt cá nhân.

### 1.2. Ràng buộc

- Không có khung giờ học cố định; có tuần rảnh, có tuần rất bận.
- Không yêu cầu Todoist Pro. **Theo Todoist, Beginner có 5 personal projects, 3 custom filters; hỗ trợ List/Board và labels.** [Nguồn](https://www.todoist.com/pricing/).
- Ưu tiên duy trì việc sử dụng ứng dụng hơn “độ hoàn hảo” của metadata.
- Không tự tạo roadmap 6–12 tháng hoặc tự gán năng lực hiện tại khi chưa có diagnostic assessment.
- Không đưa dữ liệu công ty nhạy cảm, khách hàng, credential, source code nội bộ trái phép vào Todoist/AI. Task dùng mô tả công việc mức phù hợp và link đến nguồn được phép truy cập.

### 1.3. Phạm vi ngoài tài liệu

Tài liệu này là **hệ thống vận hành Todoist**, không phải giáo trình Java/Go/SQL, không phải lịch học cứng, không phải bản chấm điểm năng lực. Các chương trình học cụ thể về sau nên có tài liệu riêng và liên kết ngược đến đây.

---

## 2. Project Registry — Danh mục 5 Project

| Project chuẩn | Chế độ | Trách nhiệm chính | Không nên chứa | Tình trạng |
|---|---|---|---|---|
| `Developer` | **Board** | CS fundamentals, Backend engineering, kỹ năng FE cần duy trì, technical practice, coding interview labs, personal engineering projects | Ứng tuyển đơn thuần, chuẩn bị email HR, việc phòng ốc | 📋 Thiết kế thống nhất |
| `English` | **List** | Nghe, nói, đọc, viết; English for work; kiểm tra tiến bộ | Task kỹ thuật thuần không liên quan ngôn ngữ | 📋 Thiết kế thống nhất |
| `Work` | **Board** | ParadiseHR (`paradise`), công việc đã nhận làm, freelance, giao việc/feedback/triển khai | Tìm job mới, CV tổng thể, task ôn học riêng | 📋 Tên chuẩn; 🔎 chưa xác minh UI đã đổi từ `Working` |
| `GLV` | **List** | Chuẩn bị bài giáo lý, tổ chức sinh hoạt, phối hợp, nguồn học liệu | Toàn bộ việc phát triển cá nhân không liên quan GLV | 📋 Thiết kế thống nhất |
| `Self & Life` | **List** | Career & Opportunities, sức khỏe, tài chính, dọn dẹp, phát triển lối sống | Bài lab Backend và task giao từ công ty | 📋 Thiết kế thống nhất |

**Quy tắc định tuyến công việc khi dễ nhầm:**

| Tình huống | Đặt ở |
|---|---|
| Ôn OOP Java để giải bài độc lập | `Developer` |
| Tự làm API mini-demo bằng Spring/Go | `Developer` |
| Luyện thuật toán hoặc system design để phỏng vấn | `Developer` |
| Tìm công ty, đọc JD, chỉnh CV, gửi hồ sơ, theo dõi HR | `Self & Life → Career & Opportunities` |
| Sửa Stored Procedure đang được giao tại Paradise HR | `Work` |
| Tìm hiểu nguyên lý transaction để hiểu SP tốt hơn, ngoài task giao | `Developer` |
| Luyện nói tiếng Anh mô tả một dự án | `English` |
| Soạn giáo án GLV và gửi người phụ trách | `GLV` |
| Dọn phòng, đi khám, kiểm soát chi tiêu | `Self & Life` |

> **Giới hạn quan trọng:** Với Todoist Free, không tạo một project Todoist mới cho mỗi project code/công ty/khóa học. Dùng task, subtask, section, label, link tài liệu trước. Nếu một công việc quá phức tạp để quản lý hiệu quả trong giới hạn này, ghi nhận nhu cầu tái cấu trúc; không âm thầm biến các section khác mục đích.

---

## 3. Section Registry — Cấu trúc bên trong Project

> **Phần này là cấu trúc mục tiêu**, chưa xác nhận tất cả section đã được tạo thật trong tài khoản. Nên giữ **tên section ổn định**, vì custom filters tham chiếu chúng.

### 3.1. Developer — Board/Kanban theo trạng thái

| Thứ tự | Section | Định nghĩa | Điều kiện vào/ra |
|---:|---|---|---|
| 01 | `Backlog` | Chưa ưu tiên; ý tưởng, nội dung kiến thức, bài thực hành tương lai | Chuyển sang `Ready` khi có đầu ra cụ thể và điều kiện thực hiện rõ |
| 02 | `Ready` | Đủ thông tin, có thể bắt đầu khi rảnh | Chuyển `In Progress` khi thực sự bắt đầu |
| 03 | `In Progress` | Đang tự học, viết code, triển khai bài lab | Chuyển `Validation` khi tạo được đầu ra cần kiểm tra |
| 04 | `Validation` | Kiểm tra khả năng tự làm, test, giải thích lại không xem đáp án | **Complete** nếu đạt tiêu chí; nếu chưa đạt, quay `In Progress` hoặc tạo next action |
| 05 | `On Hold` | Tạm dừng có lý do (thiếu nguồn, đổi ưu tiên, blocker) | Có điều kiện tiếp tục mới đưa lại `Ready` |

**Luồng:** `Backlog → Ready → In Progress → Validation → Complete` (có thể `On Hold` ở bất kỳ bước phù hợp). **Không cần cột `Done`**, Todoist có thao tác Complete riêng.

**WIP (khuyến nghị, không phải luật):** 1–2 learning units ở `In Progress`. Không mở đồng thời Java, Go, NestJS và DSA ở mức sâu nếu khiến việc nào cũng dang dở.

**Định nghĩa hoàn thành cho bài học:** (1) tự giải thích được ý chính, (2) thực hành, (3) có output/test/ghi chú lỗi, (4) tự đánh giá điều còn thiếu. Không yêu cầu đủ cả bốn nếu task vốn chỉ là một hoạt động nhỏ; riêng bài lab năng lực nên có minh chứng.

### 3.2. Work — Board/Kanban theo trạng thái

| Thứ tự | Section | Định nghĩa | Điều kiện ra |
|---:|---|---|---|
| 01 | `Backlog` | Yêu cầu công việc, ý tưởng cải tiến chưa được xử lý | Đủ thông tin + sẵn sàng ưu tiên → `Ready` |
| 02 | `Ready` | Đã rõ yêu cầu, quyền truy cập, dependency chính | Bắt đầu thực hiện → `In Progress` |
| 03 | `In Progress` | Đang thiết kế, code, kiểm thử, trao đổi | Gửi review → `Review`; chờ người khác → `Waiting`; hoàn tất nội bộ → Complete theo quy trình |
| 04 | `Waiting` | Chờ phản hồi, dữ liệu, quyền truy cập, quyết định ngoài quyền kiểm soát | Có phản hồi → quay lại bước thích hợp |
| 05 | `Review` | Kết quả cần kiểm tra, nghiệm thu, xác nhận, sửa theo feedback | Đạt yêu cầu → Complete; có lỗi → `In Progress` |

**Luồng thường gặp:** `Backlog → Ready → In Progress → Review → Complete`; `Waiting` là nhánh phụ, **không bắt buộc** mọi task đi qua.

**WIP mềm:** 2–3 công việc chủ động, tùy lượng việc thực tập và deadline thực tế. Việc thuộc `Waiting` phải ghi đang chờ gì, ai/cơ chế nào quyết định, và điều kiện follow-up nếu có. **Source convention mới:** task ParadiseHR gắn thêm `paradise` (Olive Green); kỹ thuật xử lý thể hiện qua `database`/`frontend`/`integration`... `paradise` không phải tên project và không thay đổi thứ tự Kanban. Cần phân biệt source label với domain label.

### 3.3. English — List theo kỹ năng

**Sections đề xuất:** `Listening`, `Speaking`, `Reading`, `Writing`, `Vocabulary & Grammar`.

- Một task = một hoạt động có đầu ra: ví dụ “Ghi âm 2 phút giới thiệu kiến trúc REST API và tự nghe lại”.
- Không cần labels trùng với tên section (ví dụ `speaking`) lúc khởi đầu.
- Có thể bổ sung `English for Work` thành section riêng **chỉ khi** task chuyên môn nhiều và thường xuyên; ban đầu các bài đó vẫn có thể xếp theo kỹ năng.
- Chưa quy định lịch luyện IELTS hoặc ngày thi.

### 3.4. GLV — List theo trách nhiệm (cập nhật v1.2.0)

**Bốn sections mục tiêu đã thống nhất qua trao đổi**, trạng thái thực tế trong Todoist **chưa được ảnh UI xác nhận**:

| Section | Phạm vi | Ví dụ task | Label điển hình |
|---|---|---|---|
| `Lớp Thêm Sức 3B` | Lớp giáo lý thuộc khối lãnh nhận bí tích; bài dạy, lớp, học viên và tài liệu | `Thêm Sức 3B — Soạn câu hỏi thảo luận cho bài học ...` | Không cần; `event` nếu là chương trình đặc biệt |
| `Khối TS` | Các công việc khối TS được giao; **không tự suy diễn nghĩa viết tắt TS** | `Khối TS — Chuẩn bị nội dung chương trình ...` | `event` khi tổ chức hoạt động |
| `Ban Trực` | Nề nếp, kỷ luật, điều phối trực, theo dõi hoặc báo cáo vấn đề | `Ban Trực — Tổng hợp tình hình nề nếp ...` | `follow_up` khi cần trao đổi lại |
| `Công việc chung` | Việc liên quan nhiều vai trò hoặc không thuộc rõ ba section trên | `GLV — Xác nhận lịch họp với người phụ trách` | `follow_up` hoặc `event` nếu phù hợp |

**Quy tắc GLV:** Một nhiệm vụ phải có một vị trí chính; không sao chép cùng nhiệm vụ sang ba sections. Việc phối hợp đa khối dùng subtasks, description hoặc link tham chiếu. `event` = công tác tổ chức chương trình/sự kiện, **không có nghĩa mọi buổi dạy thường lệ đều bắt buộc gắn `event`**. Sự kiện đã chốt ngày mới gắn ngày thực tế. GLV là **List theo trách nhiệm**, không áp Kanban trạng thái.

### 3.5. Self & Life — List theo trách nhiệm (cập nhật v1.2.0)

**Sections mục tiêu:**

| Section | Phạm vi | Dùng label khi nào? |
|---|---|---|
| `Career & Opportunities` | Tìm JD, sửa CV, theo dõi ứng tuyển, HR interview, thương lượng offer | `interview` cho hoạt động phỏng vấn; `follow_up` khi chủ động cần hỏi lại |
| `Health & Fitness` | Vận động, tập luyện, chăm sóc thể chất | Thông thường **không label** `exercise`, `fitness` |
| `Personal Care` | Giấc ngủ, tự chăm sóc, thói quen cá nhân | Thông thường không label |
| `Home & Organization` | Dọn phòng, sắp xếp góc làm việc, việc nhà | Thông thường **không label** `cleaning` |
| `Finance` | Thu chi, ngân sách, tiết kiệm, mua sắm có kế hoạch | Không cần label `finance` vì trùng Section |
| `Personal Goals & Review` | Mục tiêu khác, review hệ thống và việc cá nhân | Chỉ gắn label nếu có thuộc tính xuyên project thật sự |

**Quy tắc Self:** Không ép công việc sinh hoạt vào deadline giả. Ví dụ `Dọn bàn làm việc` hoặc `Hoàn thành một buổi tập` là task độc lập, không phải nhãn. Recurring chỉ dùng với các việc có chu kỳ thực tế muốn duy trì; không tự suy diễn lịch tập cố định.

### 3.6. Project & Section Descriptions — Đưa quy tắc vào ngay trong Todoist (đề xuất, chưa xác minh UI đã nhập)

Todoist hiện hỗ trợ **mô tả của Project và Section** trên các gói; đây là nơi ngắn gọn để người dùng hoặc AI có kết nối hợp lệ hiểu chính xác ý nghĩa của từng danh mục ([Projects](https://www.todoist.com/help/todoist/features/introduction-to-projects-TLTjNftLM), [Sections](https://www.todoist.com/help/todoist/features/introduction-to-sections-rOrK0aEn)). Đừng dán cả Master vào Description: mô tả nên gọn và trỏ đến Master khi cần.

**Project descriptions đề xuất để copy (chỉ là bản nháp, chưa áp dụng trực tiếp):**

| Project | Description ngắn |
|---|---|
| Developer | `Backend-first skill recovery and growth: CS fundamentals, Java → NestJS → Go, DBMS, coding practice, evidence-based competency. Technical interview labs here; job applications elsewhere. Board sections represent status.` |
| English | `Improve English for professional communication, interviews and independent practice. Sections are Listening, Speaking, Reading, Writing, Vocabulary & Grammar; flexible, output-based tasks.` |
| Work | `Actual committed work: ParadiseHR and other accepted assignments. Board follows Backlog → Ready → In Progress → Review/Waiting → Complete. Source label paradise for ParadiseHR work; keep confidential materials out.` |
| GLV | `Giáo lý viên: Lớp Thêm Sức 3B, Khối TS, Ban Trực và Công việc chung. Sections represent responsibilities; event/follow_up only when applicable.` |
| Self & Life | `Personal responsibilities and career operations: job applications, wellness, home organization, finance, and personal goals. No artificial schedules for flexible tasks.` |

**Section description cho hai Board:**

| Project | Section | Mô tả một câu |
|---|---|---|
| Developer | Backlog | `Ideas/learning needs not yet selected; do not mark as actively being studied.` |
| Developer | Ready | `Defined learning units with objective, source and validation criteria; can start independently.` |
| Developer | In Progress | `Actively studying or building; limit concurrent work and leave checkpoints.` |
| Developer | Validation | `Validate with independent explanation, runnable artifact/tests or self-assessment before completing.` |
| Developer | On Hold | `Paused with an explicit reason and resumption condition.` |
| Work | Backlog | `Captured real requests; requirements or priority not yet finalized.` |
| Work | Ready | `Confirmed scope, dependencies and expected result; ready to work.` |
| Work | In Progress | `Actively implementing or testing an actual assignment.` |
| Work | Waiting | `Blocked on external information, access, confirmation or feedback; record what is awaited.` |
| Work | Review | `Submitted for testing, feedback or acceptance; complete only after appropriate verification.` |

**Lưu ý:** Các descriptions tiếng Anh ở trên nhằm gọn và dễ dùng cho Gemini; không bắt buộc đổi tên project/section hoặc mô tả tiếng Việt bạn thích. Nếu bạn chỉnh mô tả trong UI, cập nhật Master khi có thay đổi mang ý nghĩa workflow.

---

## 4. Labels Registry — Cấu hình đã xác nhận v1.3.0

> **Trạng thái xác minh ngày 09/11/2026:** Ảnh chụp mới nhất xác nhận **18 labels được tạo trong Todoist**. Tên **`paradise`** phải giữ nguyên đúng như giao diện; `source_paradisehr` là tên từng được đề xuất trong trao đổi trước nhưng **không phải label đang dùng**. Ảnh Edit label xác nhận chính xác `paradise = Olive Green`, `event = Yellow`, `engineering = Green`, `no_ai = Violet`, `backend = Blue`; ảnh danh sách có các màu tương ứng cho 13 label còn lại. Không tự cho rằng đã gắn nhãn cho bất kỳ task nào.

### 4.1. Todoist Color Registry — Tên màu theo hệ thống chính thức

**Nguồn chuẩn:** [Todoist API v1, mục Colors](https://developer.todoist.com/api/v1/) định nghĩa `id`, `name` và mã màu. Tài liệu [Introduction to labels](https://www.todoist.com/help/todoist/features/introduction-to-labels-dSo2eE) xác nhận việc chọn màu khi tạo/sửa label. Hex là mã màu API chuẩn, **không phải màu pixel đo từ screenshot trong dark mode**.

| Tên màu hiển thị trong Todoist | API color name | ID | Mã hex API | Chức năng trong hệ thống hiện tại |
|---|---|---:|---|---|
| **Olive Green** | `olive_green` | 34 | `#949C31` | Nguồn công việc ParadiseHR |
| **Yellow** | `yellow` | 33 | `#B29104` | Hoạt động/chủ động theo dõi: `event`, `follow_up` |
| **Green** | `green` | 36 | `#369307` | Hướng công nghệ/kỹ năng và phỏng vấn |
| **Violet** | `violet` | 43 | `#CA3FEE` | Quy tắc tự thực hành: `no_ai` |
| **Blue** | `blue` | 41 | `#4180FF` | Các domain kỹ thuật và công cụ |

**Phân biệt màu và nghiệp vụ:** màu là ký hiệu thị giác, không phải trạng thái hoặc độ ưu tiên; hai label trùng màu vẫn có ý nghĩa khác nhau. Không gán nghĩa 'P1' cho label màu vàng/đỏ. Nếu dropdown hiển thị màu khác về sắc độ, đối chiếu **tên màu**, không so pixel. Các màu khả dụng khác (chưa cần dùng) gồm `red`, `orange`, `lime_green`, `mint_green`, `teal`, `sky_blue`, `light_blue`, `grape`, `lavender`, `magenta`, `salmon`, `charcoal`, `grey`, `taupe`, `berry_red`.

### 4.2. Inventory — 18 label ĐÃ TỒN TẠI trên UI

| # | Label chính xác | Màu UI | Nhóm logic | Định nghĩa/ranh giới | Khi nào gắn | Xác minh |
|---:|---|---|---|---|---|---|
| 01 | `paradise` | **Olive Green** | Source | Việc thực tế ParadiseHR trong Work; không phải skill | Mọi task thuộc nguồn ParadiseHR; kết hợp 0–2 domain labels nếu có ích | ✅ Ảnh danh sách + Edit |
| 02 | `event` | **Yellow** | Activity | Tổ chức sự kiện/chương trình | GLV hoặc Self có một hoạt động tổ chức thực sự; không phải mọi buổi học | ✅ Ảnh danh sách + Edit |
| 03 | `follow_up` | **Yellow** | Action | Cần **chủ động** liên hệ/nhắc/kiểm tra phản hồi | Có hành động liên hệ cụ thể và đối tượng/điều kiện chờ | ✅ Ảnh danh sách |
| 04 | `engineering` | **Green** | Discipline | OOP, SOLID, design patterns, clean code, architecture practice | Kỹ năng thiết kế/phương pháp kỹ nghệ là trọng tâm | ✅ Ảnh danh sách + Edit |
| 05 | `interview` | **Green** | Career | Phỏng vấn kỹ thuật hoặc HR, mock interviews | Công việc trực tiếp chuẩn bị/đi phỏng vấn; không phải mọi việc tìm job | ✅ Ảnh danh sách |
| 06 | `go` | **Green** | Technology | Go language, runtime, concurrency, HTTP services | Track/bài lab dùng Go là công nghệ chính | ✅ Ảnh danh sách |
| 07 | `java` | **Green** | Technology | Java Core/JVM/Spring | Track/bài lab Java hoặc Spring là công nghệ chính | ✅ Ảnh danh sách |
| 08 | `nestjs` | **Green** | Technology | NestJS/TypeScript Backend | Task NestJS có nhu cầu truy lại theo framework | ✅ Ảnh danh sách |
| 09 | `no_ai` | **Violet** | Learning Protocol | Tự phân tích/code/debug **trước khi** xin AI giải hộ | Lab/diagnostic có tiêu chí tự lực rõ; không tự động áp cho việc công ty | ✅ Ảnh danh sách + Edit |
| 10 | `backend` | **Blue** | Technical Domain | API, server-side services, business logic | Chủ đề chính ở server/backend | ✅ Ảnh danh sách + Edit |
| 11 | `database` | **Blue** | Technical Domain | DBMS, schema, SQL, Stored Procedure, index, transactions | Công việc chính thao tác database | ✅ Ảnh danh sách |
| 12 | `devops` | **Blue** | Technical Domain | CI/CD, Docker, deployment, operations/cloud | Trọng tâm là triển khai/vận hành | ✅ Ảnh danh sách |
| 13 | `dsa` | **Blue** | Technical Domain | Algorithms, data structures, complexity | Tự luyện thuật toán hoặc phân tích độ phức tạp | ✅ Ảnh danh sách |
| 14 | `frontend` | **Blue** | Technical Domain | HTML/CSS/JS/React, DOM, browser UI | Trọng tâm giao diện và tương tác client | ✅ Ảnh danh sách |
| 15 | `integration` | **Blue** | Technical Domain | Giao tiếp giữa thành phần: Ajax wrapper ↔ procedure; services/APIs | Trọng tâm là điểm giao tiếp/interface/contract giữa hệ thống | ✅ Ảnh danh sách |
| 16 | `security` | **Blue** | Technical Domain | Validation, auth, authorization, web security | Trọng tâm bảo mật | ✅ Ảnh danh sách |
| 17 | `systems` | **Blue** | Technical Domain | OS, networking, distributed systems, design | Trọng tâm hệ thống/hạ tầng khái niệm | ✅ Ảnh danh sách |
| 18 | `testing` | **Blue** | Technical Domain | Unit/integration/E2E/regression tests | Việc chính tạo/thiết kế/đánh giá kiểm thử | ✅ Ảnh danh sách |

**Chú ý:** `integration` là nhãn liên kết giữa các hệ thống, còn `testing` có thể đề cập integration tests. Không gắn `integration` chỉ vì tên bài kiểm thử là “integration test”.

### 4.3. Taxonomy bốn chiều và source tag

| Dimension | Nguồn sự thật | Ví dụ |
|---|---|---|
| Area (lĩnh vực) | Project | `Developer`, `Work`, `GLV` |
| Workflow/responsibility | Section | `In Progress`, `Ban Trực` |
| Source/technical topic/special action | Label | `paradise`, `database`, `no_ai` |
| Execution urgency | Priority/date | P1–P4, ngày hẹn/hạn thực tế |

Một task `Work → In Progress` có thể gắn **`paradise` + `database`**. `paradise` trả lời **việc từ đơn vị nào**, `database` trả lời **kỹ thuật chính là gì**. Khi có nguồn thứ hai trong Work, chỉ tạo thêm label nguồn khi đã có task thực sự; cách đặt tên nguồn mới phải quyết định trong Change Request, không tự suy ra `source_*` là mẫu bắt buộc. **Không đổi nhãn `paradise` thành `source_paradisehr` khi chưa có quyết định và di chuyển nhãn an toàn.**

### 4.4. Quy tắc áp nhãn — Tránh over-tagging

1. Không bắt buộc tất cả task có nhãn. Mặc định **0–2 label/task**, đôi khi **3** khi có *source + technical domain + action* hoặc *technology + domain + no_ai*. Đây là quy ước, **không phải giới hạn Todoist**.
2. Work/ParadiseHR: gắn `paradise` cho task của đơn vị này; thêm `database` **hoặc** `frontend` khi có trọng tâm; thêm `integration` nếu xử lý luồng kết nối. Nếu việc chỉ là họp/nhắc việc từ ParadiseHR: `paradise` là đủ.
3. Developer: chọn domain (như `engineering`, `database`, `dsa`) + technology (`java`, `go`, `nestjs`) nếu cần + `no_ai` cho phần tự luyện.
4. English: không cần nhãn listening/speaking vì sections đã có. `interview` chỉ khi bài thực hành phỏng vấn cụ thể.
5. GLV: sections `Lớp Thêm Sức 3B`, `Khối TS`, `Ban Trực`, `Công việc chung`; chỉ thêm `event`/`follow_up` khi tác vụ có tính chất đó.
6. Self & Life: dọn phòng, tập thể dục, tài chính không cần label; Career dùng `interview` và `follow_up` khi cần.
7. `follow_up` **không đồng nghĩa** mọi việc ở Work/Waiting: dùng khi cần bạn chủ động kiểm tra hoặc liên hệ lại. Waiting có thể chứa việc tạm dừng thụ động.
8. Không dùng label thể hiện trạng thái `ready`, `in_progress`, `done`, độ ưu tiên `urgent`, ngày hoặc thời lượng `t15/t30` khi đã có cấu trúc đáp ứng.
9. Không thêm label 19+ chỉ vì gặp một công nghệ/màn hình/công ty mới; ghi tên cụ thể trong Task title hoặc Description trước. Khi xuất hiện nhóm task đủ lớn cần truy xuất, mở Change Request.
10. **Không gắn `no_ai` cho việc thực tế nếu cần tuân thủ chính sách công ty hoặc xử lý thông tin nội bộ**. Tách bài học mô phỏng ở Developer với việc giao từ Work.

### 4.5. Label Matrix theo Project — Ví dụ được chuẩn hóa

| Project → Section | Task mẫu | Labels | Giải thích |
|---|---|---|---|
| Developer → Ready | `Java Core — Tự triển khai Map và xử lý key trùng` | `java`, `dsa`, `no_ai` | Dùng Java để tự học Collections |
| Developer → Ready | `DBMS — Chuẩn hóa quan hệ từ 1NF đến 3NF` | `database`, `no_ai` | Kỹ năng DBMS và tự làm |
| Developer → Validation | `Spring Boot — Viết test transaction rollback cho service demo` | `java`, `testing`, `no_ai` | Kiểm chứng bằng test |
| Work → In Progress | `ParadiseHR / Chấm công — Viết SP truy vấn theo phòng ban` | `paradise`, `database` | Nguồn + kỹ thuật chính |
| Work → In Progress | `ParadiseHR / Chấm công — Sửa bố cục bảng từ HTML sinh bởi DB` | `paradise`, `frontend` | UI là trọng tâm |
| Work → Review | `ParadiseHR / Chấm công — Kiểm tra Ajax wrapper nhận kết quả SP` | `paradise`, `integration` | Luồng giao tiếp chính |
| Work → Waiting | `ParadiseHR / Chấm công — Xác nhận nghiệp vụ tính công` | `paradise`, `follow_up` | Chủ động xác nhận; không mặc định backend |
| GLV → Lớp Thêm Sức 3B | `Soạn câu hỏi thảo luận cho bài giáo lý sắp tới` | *(không cần)* | Section đã phân biệt |
| GLV → Khối TS | `Chuẩn bị checklist cho chương trình sinh hoạt` | `event` | Tổ chức chương trình |
| GLV → Ban Trực | `Xác nhận lịch trực với người phụ trách` | `follow_up` | Chủ động liên hệ |
| Self & Life → Home & Organization | `Dọn và phân loại khu vực bàn làm việc` | *(không cần)* | Việc cá nhân đơn lẻ |
| Self & Life → Career & Opportunities | `Theo dõi phản hồi ứng tuyển vị trí Backend` | `follow_up` | Chủ động kiểm tra phản hồi |

### 4.6. Quy trình cập nhật labels trong tương lai

- Khi **đổi màu**: ghi cả *Display color* và *API color name*; mọi task gắn nhãn này vẫn được phân loại như cũ. Không dùng màu để mã hóa một priority mới.
- Khi **đổi tên**: tìm các custom filters, lệnh Quick Add, tài liệu mẫu và các automation/agent có tham chiếu cũ; chuẩn bị mapping và kiểm thử sau cập nhật.
- Khi **thêm nguồn công việc**: ưu tiên đặt tên theo tên ngắn được người dùng xác nhận; không tự sinh slug và tự gắn vào mọi task.
- Khi **xóa nhãn**: kiểm tra các task đang dùng và rủi ro với task đã hoàn thành; Todoist có thể khôi phục nhãn cũ khi uncomplete một task từng gắn nhãn đã xóa ([Help Center](https://www.todoist.com/help/todoist/features/introduction-to-labels-dSo2eE)).
- Khi **Gemini/AI đọc label**: ưu tiên tên chính xác, không suy luận từ màu; màu chỉ là thông tin hỗ trợ.

### 4.7. Validation checklist — Cấu hình ảnh ngày 09/11

- [x] 18 tên label tồn tại trên ảnh danh sách.
- [x] 5 tên/màu đã xác nhận cụ thể qua cửa sổ Edit (`paradise`, `event`, `engineering`, `no_ai`, `backend`).
- [x] Nhóm Blue/Green/Yellow của các label còn lại xác nhận ở mức hiển thị qua ảnh danh sách; nếu cần xác nhận *tên dropdown cụ thể từng nhãn*, mở Edit và kiểm tra.
- [ ] Kiểm thử ít nhất một task Work với `paradise` + `database` (chưa có ảnh task).
- [ ] Kiểm tra 3 filters có query đang lưu thực tế (vẫn chưa thấy trên ảnh).
- [ ] Xác nhận project/section descriptions đã được nhập ở Todoist (chưa có bằng chứng UI).

---

## 5. Filter Registry — 3 bộ lọc hiện có (ĐÓNG BĂNG, không mở rộng lúc này)

**Quyết định mới ngày 09/11/2026: Không thêm filter hoặc điều chỉnh cấu hình filter trong giai đoạn này. Phần bên dưới chỉ giữ để tham chiếu và quản lý thay đổi sau này.**

**✅ Đã thấy trong ảnh:** 3 tên filter tồn tại: `Next Actions`, `Independent Practice`, `Pending & Follow-ups` (tổng `USED 3/3`).

**🔎 Chưa xác minh:** Query và Description thực tế bên trong UI. Bảng dưới là **cấu hình mục tiêu đã đề xuất trong hội thoại**, không tuyên bố đã có trong Todoist. Cần mở Edit từng filter → kiểm tra `Query` → `Preview` trước khi đánh dấu `Verified`.

| Filter | Mục tiêu sử dụng | Suggested color | Favorite? | Query chuẩn mục tiêu |
|---|---|---|---|---|
| `Next Actions` | Những task P1/P2 có thể hành động, không nằm trong backlog/on hold/waiting | Blue | On | `(p1 \| p2) & !/*Backlog* & !/*On Hold* & !/*Waiting*` |
| `Independent Practice` | Các bài `no_ai` đang có thể thực hiện hoặc kiểm chứng | Purple | On | `%no_ai & !/*Backlog* & !/*On Hold* & !/*Waiting*` |
| `Pending & Follow-ups` | Việc cần chủ động follow-up hoặc Work đang Waiting | Orange | On | `%follow_up \| /*Waiting*` |

### 5.1. Queries nguyên văn để copy (không escape dấu `|`)

**Next Actions**

```text
(p1 | p2) & !/*Backlog* & !/*On Hold* & !/*Waiting*
```

**Independent Practice**

```text
%no_ai & !/*Backlog* & !/*On Hold* & !/*Waiting*
```

**Pending & Follow-ups**

```text
%follow_up | /*Waiting*
```

**Nguồn cú pháp:** [Todoist — Introduction to filters (cập nhật 06/11/2026)](https://www.todoist.com/help/todoist/features/introduction-to-filters-V98wIH). Các toán tử `&`, `|`, `!`, `%`, `/` và wildcard `*` được nêu trong tài liệu. Ví dụ `/*Work*` bắt các section chứa “Work”, nên `/*Waiting*` và `/*Backlog*` phù hợp với section có tiền tố đánh số.

### 5.2. Mô tả nên điền trong Add/Edit filter

**Next Actions:** `Các công việc P1/P2 hiện có thể chủ động xử lý; loại trừ Backlog, On Hold và Waiting.`

**Independent Practice:** `Bài thực hành cần tự tư duy/code/debug trước khi sử dụng AI; chỉ gồm các task chưa bị tạm hoãn hoặc chờ.`

**Pending & Follow-ups:** `Các việc cần chủ động liên hệ, kiểm tra phản hồi hoặc đang ở trạng thái Waiting.`

### 5.3. Cách hiểu đúng và các giới hạn

- `Next Actions` **không phải** danh sách tất cả việc đến hạn. Task P3 có ngày đến hạn vẫn xem qua Today/Upcoming. Nếu thấy hay bỏ sót, đánh giá lại quy trình chứ không mặc định filter bị lỗi.
- `Independent Practice` không yêu cầu P1/P2: một bài độc lập ở P3 vẫn có thể xuất hiện khi sẵn sàng thực hành.
- `Pending & Follow-ups` gồm `follow_up` **hoặc** bất kỳ Section tên có chứa `Waiting`; một task có cả hai điều kiện không cần nhập hai lần.
- Tên section thay đổi có thể làm filter sai: ví dụ đổi `Waiting` thành `Blocked` sẽ khiến `/*Waiting*` không còn khớp.
- Query theo section là **xuyên project**. Nếu sau này một project khác thêm section `Backlog`, nó cũng bị loại khỏi `Next Actions`; điều này là chủ đích hiện tại.
- **Todoist filters hiển thị active tasks, không tạo bản ghi lịch sử hoàn thành**, không lọc nội dung comment. Dùng comment hoặc log riêng để theo dõi tiến bộ học tập.
- Không có task khớp có thể là **đúng**, nhất là khi chưa bắt đầu học. Không tự thêm task mẫu vào lịch thật chỉ để làm filter có dữ liệu.

### 5.4. Bộ test bắt buộc khi tạo/sửa Filter

| Test | Dữ liệu thử | Next Actions | Independent Practice | Pending & Follow-ups |
|---|---|---:|---:|---:|
| F01 | Developer / Ready / P1 / `database + no_ai` | ✅ | ✅ | — |
| F02 | Developer / Backlog / P1 / `no_ai` | — | — | — |
| F03 | Developer / On Hold / P2 / `no_ai` | — | — | — |
| F04 | Work / Waiting / P2 / không label | — | — | ✅ |
| F05 | Self & Life / Career / P3 / `follow_up` | — | — | ✅ |
| F06 | English / Speaking / P2 / không label | ✅ | — | — |
| F07 | Work / Review / P2 / không label | ✅ | — | — |
| F08 | Developer / Validation / P3 / `no_ai` | — | ✅ | — |
| F09 | Developer / Ready / P3 / không label | — | — | — |

**Quy trình kiểm thử không làm bẩn dữ liệu:** Tạo task demo có prefix `[TEST]` → kiểm tra Preview/đúng filter → xóa task thử hoặc Complete nếu muốn lưu test. Sau khi kiểm thử điền `Last verified` vào nhật ký thay đổi. Khi chưa kiểm thử, ghi `Unverified`.

### 5.5. Khi nào mới thay đổi bộ 3 filters?

- Có một tập công việc cần xem **hầu như mỗi lần** mở Todoist nhưng hiện phải tìm thủ công, và không giải quyết được bằng Search/Project/Today/Upcoming.
- Có filter gần như không bao giờ dùng trong một thời gian đủ dài → cân nhắc thay thế, không tạo theo sở thích nhất thời.
- Giới hạn 3 filters (Free): muốn thêm filter phải **cân nhắc bỏ/thay** một filter hiện có.
- Ghi lại query cũ, query mới, nguyên nhân, test hồi quy và ngày chỉnh sửa trước khi sửa.

---

## 6. Priority, Date, Recurring & Favorites

### 6.1. Priority (quy ước cá nhân)

| Priority | Ý nghĩa vận hành | Ví dụ |
|---|---|---|
| P1 | Cấp thiết/quan trọng nhất, có thể hành động ngay hoặc hạn gần | Hoàn thiện task công việc cần bàn giao thực tế |
| P2 | Quan trọng và sẵn sàng làm | Tự viết lab SQL, chuẩn bị CV cho cơ hội phù hợp |
| P3 | Có giá trị nhưng chưa là tâm điểm | Khám phá một công nghệ, nâng cấp portfolio |
| P4 | Mặc định, ý tưởng/chưa ưu tiên | Backlog nghiên cứu dài hạn |

Đừng gán P1 cho mọi bài học. **P1/P2 biểu diễn ưu tiên thực thi, không phải cấp độ khó.** Nếu một task chờ người khác, chuyển `Waiting` và đừng xem Priority như một lời nhắc ép thực hiện.

### 6.2. Date

- **Không ngày:** mặc định cho bài học, bài lab, task cá nhân có thể làm bất kỳ lúc nào.
- **Có ngày:** deadline khách quan, lịch sự kiện GLV, cuộc hẹn/phỏng vấn, ngày phải follow-up đã thống nhất, hoặc kế hoạch ngày do bạn chủ động chọn.
- **Recurring task:** chỉ cho việc thực sự lặp lại và có giá trị theo chu kỳ; không tạo “học Java 20:00 mỗi ngày” khi thời gian không cố định.
- **Today/Upcoming:** xem các nhiệm vụ có ngày; `Next Actions` xem những việc ưu tiên có thể hành động mà không cần lịch giả.

### 6.3. Favorites

- Đưa **ba filters** vào Favorites nếu thường xuyên dùng.
- Labels không cần Favorites mặc định.
- Không Favorite tràn lan mọi project/section nếu sidebar thành quá dài.

---

## 7. Task Standard — Quy chuẩn tạo và viết task

### 7.1. Anatomy của một task chất lượng

1. **Title:** động từ + đầu ra cụ thể, không mơ hồ.
2. **Project + Section:** lưu đúng lĩnh vực và trạng thái/nhóm.
3. **Description:** ngữ cảnh, input, phạm vi, tiêu chí hoàn thành, nguồn học/reference, lưu ý blocker.
4. **Subtasks:** 2–5 bước có ý nghĩa nếu task tương đối lớn; task đơn giản không cần subtask.
5. **Priority:** ưu tiên tại thời điểm hiện tại; không phải mặc định P1.
6. **Labels:** chỉ gắn những thuộc tính có ích để lọc/truy xuất.
7. **Date:** tùy chọn, không điền khi không có mốc thực sự.
8. **Evidence:** link repository/commit, SQL demo, ảnh kết quả, ghi chú/tự đánh giá; tránh đưa dữ liệu nội bộ nhạy cảm.
9. **Next Action/Checkpoint:** ghi lại bước tiếp theo khi task cần nhiều phiên.

### 7.2. Naming Convention

**Task học thuật:** `[Chủ đề] — [Hành động + đầu ra]`

- `DBMS — Vẽ ERD và xác định cardinality từ đề bài`
- `Java Core — Tự implement class quản lý nhân viên bằng OOP`
- `Go — Tự viết HTTP handler có validation và tests`
- `NestJS — Tự debug lỗi DI trong module demo`

**Task công việc:** `[Nguồn/feature] — [Việc + kết quả]`

- `Paradise HR — Viết và kiểm thử SP lấy dữ liệu chấm công`
- `Freelance ABC — Hoàn thiện API danh sách đơn hàng`

**Job Search:** `[Hành động] — [Company / Role]`

- `Ứng tuyển — Company A / Backend Developer`
- `Chuẩn bị vòng kỹ thuật — Company B / Full-stack Developer`

**English:** `[Kỹ năng] — [Bài tập cụ thể]`

- `Speaking — Ghi âm 2 phút mô tả một API đã triển khai`
- `Listening — Nghe hội thoại công việc và tóm tắt ý chính`

**GLV:** `[Hoạt động] — [Kết quả]`, ví dụ `GLV — Soạn 5 câu hỏi thảo luận cho bài giáo lý`.

**Self & Life:** `[Hành động nhỏ có thể hoàn thành]`, ví dụ `Dọn góc bàn làm việc`, không ghi `Sống khoa học hơn` làm task.

### 7.3. Mẫu description — Task học tập

```markdown
## Objective
- [Tôi cần tự làm được gì?]

## Scope / Prerequisites
- [Chủ đề, tài liệu, điều kiện cần]

## Deliverable / Definition of Done
- [Kết quả chạy được hoặc giải thích được]
- [Cách tự test và tự đối chiếu]

## Rules
- Tự phân tích và thử trước khi sử dụng AI (nếu có no_ai)
- Không sao chép đáp án khi chưa thử giải

## Evidence
- [Link notes / repo / SQL / test]

## Checkpoint
- Đã làm:
- Đang vướng:
- Next action:
```

### 7.4. Mẫu description — Task công việc

```markdown
## Context / Requirement
- [Mục tiêu nghiệp vụ, phạm vi, nguồn yêu cầu]

## Input / Dependencies
- [Điều kiện đầu vào, quyền, dữ liệu demo, tài liệu được phép dùng]

## Acceptance Criteria
- [Kết quả nghiệm thu được]
- [Test cases / validation]

## Blockers / Waiting
- [Đang chờ gì? Ai xác nhận? Khi nào nên follow-up?]

## Evidence / Delivery
- [Link task/JIRA/repo/PR/chứng cứ không nhạy cảm]

## Next action
- [Bước cụ thể để tiếp tục]
```

### 7.5. Mẫu description — Job application

```markdown
## Opportunity
- Company / Role:
- JD URL:
- Location / Work mode:
- Fit / Concerns:

## Action steps
- [ ] Đọc JD và ghi yêu cầu quan trọng
- [ ] Cập nhật CV phù hợp (không làm sai lệch kinh nghiệm)
- [ ] Gửi hồ sơ
- [ ] Ghi ngày gửi và kênh liên hệ
- [ ] Follow-up nếu hợp lý

## Progress / Notes
- Trạng thái trao đổi:
- Người liên hệ (nếu phù hợp):
- Bước tiếp theo:
```

### 7.6. Mẫu progress comment (ngắn, dùng khi kết thúc một phiên)

```text
Đã làm: ...
Đang vướng: ...
Next action: ...
Evidence: ...
```

**Điều quan trọng:** Không yêu cầu ghi comment dài cho task chỉ mất vài phút. Ghi checkpoint cho task nhiều phiên hoặc bài thực hành đang đánh giá năng lực.

### 7.7. Playbook — Work / ParadiseHR

**Kiến trúc theo mô tả người dùng (chưa kiểm tra code thực tế):** Stored Procedure thực hiện truy vấn/xử lý nghiệp vụ; có cơ chế/procedure/function trong Database sinh HTML để hiển thị UI gồm `div`, CSS `<style>` và JavaScript `<script>`; phía client có wrapper Ajax gọi xử lý tương tự API, do người khác xây sẵn. **Không khẳng định** tất cả màn hình có cùng cấu trúc hoặc dùng REST/Axios trực tiếp. **Mọi task thuộc ParadiseHR có source label `paradise` (Olive Green)**; các label Blue bổ sung thể hiện domain kỹ thuật chính.

| Loại nhiệm vụ | Title gợi ý | Labels ưu tiên | DoD tối thiểu |
|---|---|---|---|
| Stored Procedure / SQL | `ParadiseHR — Viết SP lấy danh sách nhân sự theo điều kiện` | `paradise`, `database` | Đúng tham số, dữ liệu demo, test case và tình huống rỗng/sai |
| Sinh HTML từ DB | `ParadiseHR — Sửa cấu trúc HTML của màn hình ...` | `paradise`, `frontend` (thêm `database` nếu sửa cả logic sinh HTML) | HTML hợp lệ theo framework nội bộ, hiển thị đúng |
| CSS/div UI | `ParadiseHR — Chỉnh bố cục màn hình ...` | `paradise`, `frontend` | Kiểm tra hiển thị theo yêu cầu |
| Ajax/Script | `ParadiseHR — Kiểm tra script gọi SP và cập nhật kết quả` | `paradise`, `integration` (thêm `frontend` nếu trọng tâm là UI) | Luồng input → gọi xử lý → response → UI chạy đúng |
| Regression/debug | `ParadiseHR — Tái hiện và sửa lỗi ...` | `paradise` + domain liên quan, `testing` nếu trọng tâm là test | Có bước tái hiện, kết quả trước/sau và regression |
| Review/chờ phối hợp | `ParadiseHR — Xác nhận logic ... với người phụ trách` | `paradise`, `follow_up` nếu phải chủ động liên hệ | Nêu người/điều kiện chờ, bước tiếp theo |

**Ranh giới:** Đây là công việc thực tế, khác với task tự học ở Developer. Không paste SQL, dữ liệu nhân viên, nghiệp vụ hoặc tài liệu nội bộ nhạy cảm lên Todoist nếu không được phép; chỉ ghi mô tả, mã công việc hoặc link được phê duyệt.

**Work Board:** `Backlog → Ready → In Progress → Review → Complete`, `Waiting` khi phụ thuộc người khác. Khi công việc có cả SP và UI, có thể là **một task với subtasks** nếu cùng một chức năng/DoD; tách thành nhiều tasks nếu mỗi phần bàn giao độc lập, có tiến độ riêng.

### 7.8. Playbook — GLV theo ba trách nhiệm

| Section | Task mẫu | DoD minh họa | Nhãn khi cần |
|---|---|---|---|
| Lớp Thêm Sức 3B | `Thêm Sức 3B — Soạn nội dung bài ...` | Bài dạy và câu hỏi được chuẩn bị | Không cần |
| Khối TS | `Khối TS — Lập danh sách chuẩn bị chương trình ...` | Checklist, người phụ trách, nội dung được xác nhận | `event` |
| Ban Trực | `Ban Trực — Tổng hợp việc cần xử lý trong buổi trực ...` | Danh sách vấn đề và hướng xử lý được cập nhật | `follow_up` nếu có người cần liên hệ |
| Công việc chung | `GLV — Xác nhận lịch hoạt động ...` | Có xác nhận cuối cùng | `follow_up`, `event` nếu liên quan chương trình |

Lịch giáo lý/sự kiện **chỉ đặt ngày khi xác nhận thật**. Việc thường lệ không cần mọi lần gắn `event` hay `follow_up`.

### 7.9. Playbook — Self & Life

- `Home & Organization`: `Dọn khu vực bàn làm việc` — hoàn thành sau khi sắp xếp khu vực được chọn; **không label**.
- `Health & Fitness`: `Hoàn thành một buổi vận động` — định nghĩa loại hình/mức vận động phù hợp bản thân trước khi tạo recurring; **không label**.
- `Finance`: `Rà soát chi tiêu và phân loại khoản cần xử lý` — đầu ra một bản tổng hợp/nhóm chi phí; **không label**.
- `Career & Opportunities`: `Ứng tuyển — Company / Backend Developer` — link JD, CV gửi, kênh/nội dung follow-up; dùng `interview` ở bước phỏng vấn, `follow_up` khi cần chủ động liên hệ.
- Các task nhỏ không cần description template đầy đủ; chỉ cần hành động rõ, phù hợp thời gian linh hoạt. Không biến Todoist thành lịch giờ cố định.

---

### 7.10. Task Authoring Standard v1.3 — Mục tiêu và cấp độ chi tiết

**Mục đích:** Mỗi task phải dễ hiểu với **chính bạn sau 1–3 tháng**, dễ lựa chọn khi rảnh, có thể tiếp tục sau khi dừng và đủ thông tin để một AI khác (Gemini) **đọc đúng mà không đoán**. Todoist là nơi điều phối hành động, không phải wiki chứa toàn bộ code/spec.

**Ba cấp độ nhập task** (chọn cấp nhẹ nhất đủ dùng):

| Mức | Loại công việc | Yêu cầu tối thiểu | Ví dụ |
|---|---|---|---|
| **L1 — Quick Capture** | Nhớ ra việc, chưa phân tích | Title tạm có thể hiểu; Inbox; chưa cần label | `Hỏi lịch sinh hoạt Khối TS` |
| **L2 — Actionable Task** | Việc rõ ràng, làm trong một/lần vài phiên | Title hành động, project/section, output hoặc DoD ngắn, priority hợp lý | `Soạn 5 câu hỏi giáo lý cho bài X` |
| **L3 — Structured Task** | Việc kỹ thuật/phức tạp, có phụ thuộc, nhiều bước | Title, Context, Scope, Inputs, DoD, subtasks, evidence, checkpoint | `Chấm công — Sửa SP tính công theo quy tắc đã xác nhận` |

**Mẫu tổng quát:** `ACTION + TARGET/CONTEXT + VERIFIABLE RESULT` (động từ + đối tượng + kết quả có thể kiểm tra). Hạn chế các động từ mơ hồ như `học`, `xem`, `nghiên cứu` đứng một mình nếu không có đầu ra. Không thêm P1/label/ngày vào chính tên nếu Todoist đã có thuộc tính tương ứng.

### 7.11. Title Convention — Viết tiêu đề có thể hành động ngay

**Template:** `[Area / Module / Feature] — [Động từ + đối tượng] [→ kết quả]` (prefix chỉ dùng khi giúp nhận diện). Tiếng Việt là ngôn ngữ mặc định, giữ tên công nghệ/field/khái niệm bằng tiếng Anh khi chính xác hơn. Dấu `—` phân cách ngữ cảnh và hành động, tránh quá nhiều dấu `/` trừ khi là mã nghiệp vụ.

| Không nên | Nên dùng | Vì sao |
|---|---|---|
| `Học Java` | `Java Core — Tự viết ứng dụng CLI quản lý danh sách nhân viên` | Có output kiểm chứng |
| `Ôn DB` | `DBMS — Giải 3 bài về Functional Dependencies và candidate keys` | Đúng phạm vi và kết quả |
| `Làm phần Payroll` | `Payroll — Sửa SP tổng hợp dữ liệu theo điều kiện đã xác nhận` | Xác định thành phần cần thay |
| `Fix UI` | `Chấm công — Sửa layout bảng khi dữ liệu vượt chiều rộng` | Có lỗi/điều kiện cụ thể |
| `Luyện IELTS` | `Speaking — Ghi âm 2 phút giải thích một REST API và tự đánh giá` | Có minh chứng |
| `Giáo lý` | `Thêm Sức 3B — Soạn 5 câu hỏi thảo luận cho bài ...` | Đầu ra cụ thể |
| `Tập thể dục` | `Hoàn thành một buổi vận động theo bài tập đã chọn` | Có thể complete một lần |
| `Tìm việc` | `Chọn 5 JD Backend phù hợp và ghi yêu cầu chung` | Hành động rõ ràng |

**Tiêu chí title đạt:** (1) nhìn riêng vẫn hiểu làm gì; (2) chứa động từ khả thi; (3) không nhồi toàn bộ yêu cầu nghiệp vụ vào title; (4) tránh `...` hoặc `XYZ` khi đã biết tên thật; (5) không gắn ngày giả.

### 7.12. Title by project — Quy ước thực tế

| Project | Quy ước | Ví dụ |
|---|---|---|
| Developer | `[Course/Technology] — [Deliverable/assessment]` | `Java Core — Tự viết Comparable Comparator và kiểm thử sắp xếp` |
| English | `[Skill] — [Practice + output]` | `Speaking — Ghi âm self-introduction cho Backend interview` |
| Work | `[Source / Feature] — [Action + expected output]` | `ParadiseHR / Chấm công — Kiểm thử SP lấy công theo phòng ban` |
| GLV | `[Responsibility] — [Action + output]` | `Ban Trực — Tổng hợp các vấn đề cần trao đổi trong buổi trực` |
| Self & Life | `[Action + concrete scope]` | `Dọn khu vực tủ sách và phân loại tài liệu không dùng` |

**Mã tham chiếu:** Nếu đã có ticket/code chính thức (Jira, nội bộ...), ghi mã thật trong title hoặc mô tả khi được phép. Nếu chưa có, **không tự bịa mã ticket**. `DEV-001` trong bản nháp chỉ là local planning ID, không phải Todoist task ID.

### 7.13. Description — Cấu trúc, quy tắc độ dài và cách dùng

Todoist cho phép **task description tối đa 16.384 ký tự**, hỗ trợ lưu ngữ cảnh và liên kết; mô tả có thể được tìm qua Search ([Help Center](https://www.todoist.com/help/todoist/features/add-a-task-description-in-todoist-rOryWIHn)). Tránh sử dụng hết giới hạn; nếu có design spec dài, lưu trong repository/tài liệu và đặt link truy cập được phép.

**Tách ba trường có chức năng khác nhau:**

| Thành phần | Chứa gì | Không nên chứa |
|---|---|---|
| **Description** (ổn định) | Mục tiêu, phạm vi, quy tắc, acceptance criteria, nguồn và dependencies | Nhật ký mỗi lần chỉnh code dài dần theo thời gian |
| **Subtasks** (checklist) | Các bước có thể hoàn thành riêng nhưng thuộc cùng một outcome | Bản copy description, mỗi dòng là hành động vụn vặt |
| **Comments / Checkpoints** (theo thời gian) | Đã thử gì, lỗi, feedback, quyết định, kết quả từng phiên, bước tiếp | Spec chính liên tục thay đổi không có bản tổng hợp |

**Mẫu L2 — Dùng hằng ngày:**

```text
Mục tiêu: ...
Hoàn thành khi: ...
Nguồn/Link: ... (nếu có)
```

**Mẫu L3 — Chuẩn kỹ thuật:**

```markdown
## Context
- Vấn đề / lý do cần thực hiện:
- Nguồn yêu cầu / tài liệu:

## Objective & Scope
- Kết quả mong muốn:
- Trong phạm vi:
- Ngoài phạm vi:

## Input / Dependencies
- Dữ liệu giả / môi trường / quyền / khái niệm tiên quyết:
- Phụ thuộc / cần xác nhận:

## Acceptance Criteria / Definition of Done
- [ ] Điều kiện kiểm tra 1
- [ ] Điều kiện kiểm tra 2
- [ ] Test case âm / ngoại lệ phù hợp

## Evidence
- Link source / commit / notes / ảnh kết quả / file demo (chỉ khi được phép):

## Next Action
- Bước nhỏ cụ thể để tiếp tục:
```

Todoist hỗ trợ định dạng văn bản, nhưng tài liệu Markdown ở đây là **mẫu nội dung**; khi dán vào giao diện cần kiểm tra cách hiển thị thực tế. Không giả định Markdown checkbox trong Description tự trở thành Subtasks. Muốn check từng bước trong Todoist hãy tạo **subtask thật**.

### 7.14. Subtasks, Parent Tasks, Milestones — Khi nào tách một việc

- **Single task:** Có một kết quả dễ xác nhận; có thể thực hiện trọn vẹn và đánh dấu.
- **Task + 2–5 subtasks:** Cùng một deliverable, nhưng gồm các bước có thể kiểm tra (phân tích → triển khai → test → kiểm chứng).
- **Nhiều peer tasks:** Khác deliverable, owner, deadline, blockers hoặc có thể bàn giao/test độc lập (ví dụ một API và một report tách riêng).
- **Learning module dài:** Lưu roadmap ở tài liệu riêng, đưa **learning units** thành tasks cụ thể; không tạo task không bao giờ hoàn thành như `Học hết Backend`.
- **Milestone:** Chỉ coi là một bước kiểm chứng rõ (ví dụ `Java Core — Tự hoàn thiện bài đánh giá OOP`) nếu có outcome; không complete khi chưa đạt.
- **Subtask trên Board:** Todoist cho hiển thị/complete subtasks trên card nhưng không kéo thả subtasks trực tiếp giữa các cột; quản lý trạng thái bằng **parent task**, xem chi tiết nếu cần chỉnh thứ tự ([Board Help](https://www.todoist.com/help/todoist/features/use-the-board-layout-in-todoist-AiAVsyEI)).
- **Completion rule:** Parent được complete khi **DoD chính đạt**; hoàn thành mọi subtask không tự chứng minh output đúng nếu thiếu acceptance test.

### 7.15. Priority, Date, Deadline, Recurring — Các quy tắc dễ nhầm

| Thuộc tính | Khi nào dùng | Khi nào không dùng |
|---|---|---|
| P1 | Việc thực sự cần ưu tiên và có thể hành động; ít việc | Mọi bài học quan trọng về lâu dài |
| P2 | Việc có giá trị, sẵn sàng thực hiện | Ngụ ý phải hoàn thành trong ngày |
| P3 | Backlog có giá trị nhưng chưa phải tâm điểm | Đổi thành P1 chỉ để thấy nhiều trong filter |
| P4 | Ý tưởng/chưa ưu tiên | Dùng để đánh giá năng lực con người |
| **Date** | Ngày định làm/nhắc do chủ động chọn hoặc sự kiện xác định | Dùng như deadline giả khi lịch không cố định |
| **Deadline** | Deadline độc lập do bên ngoài ấn định, nếu plan hỗ trợ | Không giả định tài khoản Free dùng được Deadline như Pro |
| **Recurring** | Việc thực sự lặp lại cần được nhắc | Bài học theo số thứ tự nên làm một lần; streak cưỡng ép |

Theo tài liệu Todoist, Date và Deadline là hai khái niệm khác nhau; **Deadline là tính năng của plan trả phí**. Với Beginner, deadline bên ngoài cần được giữ trong **Description**, đồng thời có thể đặt ngày task phù hợp để nhắc, nhưng phải ghi rõ không nhầm đó là ngày khởi động công việc ([Get Started](https://www.todoist.com/help/todoist/get-started/get-started-with-todoist-OgNNJR)).

### 7.16. Quick Add → Clarify → Execute → Update — Hướng dẫn thao tác thực tế

1. **Capture nhanh:** Khi nhớ ra việc, chỉ viết title ngắn trong Inbox, không bận tâm metadata.
2. **Clarify:** Trước khi làm, mở task; sửa title thành một hành động có kết quả; xác định project/section, tối thiểu DoD.
3. **Choose Priority:** Dựa trên cam kết và mức phù hợp hiện tại, không phải độ khó.
4. **Attach Labels:** Sử dụng 18 label đã có, thường 0–2; Work ParadiseHR có `paradise`.
5. **Break down:** Chỉ tạo subtasks khi cần; có thể làm sau khi đọc yêu cầu.
6. **Execute:** Với Board chuyển `Ready → In Progress` khi thực sự bắt đầu; nếu chỉ là capture chưa action thì để Backlog.
7. **Update:** Task chưa xong thì comment 2–4 dòng checkpoint; task Waiting có nguyên nhân/đối tượng phụ thuộc.
8. **Complete:** Chỉ khi đạt DoD; cập nhật evidence/decision rồi complete.

**Quick Add (trên web):** `Q` khi ứng dụng được focus; `#` chọn Project, `/` chọn Section, `%` chọn label, `p1`...`p4` chọn Priority; dùng menu gợi ý để xác nhận, không nhập cú pháp bừa khiến ký tự còn nguyên trong tên. Todoist có natural-language date parsing: nếu chuỗi title bị hiểu nhầm thành ngày, bỏ lựa chọn ngày đó trước khi Save ([Quick Add](https://www.todoist.com/help/todoist/features/use-task-quick-add-in-todoist-va4Lhpzz), [Shortcuts](https://www.todoist.com/help/todoist/features/use-keyboard-shortcuts-in-todoist-Wyovn2)).

**Mẫu thao tác (không cần nhập các ký hiệu nếu dùng UI):**

```text
Title: ParadiseHR / Chấm công — Sửa SP lấy dữ liệu theo phòng ban
Project: Work
Section: Ready
Labels: paradise, database
Priority: P2
Date: [để trống nếu chưa có ngày]
Description: Có tiêu chí kiểm tra cụ thể, dữ liệu demo, người yêu cầu, nguồn tham chiếu được phép dùng.
```

### 7.17. Comments & Checkpoints — Lưu gì sau mỗi phiên

Todoist Comments được lưu **theo trình tự thời gian** và có thể chứa ghi chú/tệp đính kèm ([Comments Help](https://www.todoist.com/help/todoist/features/add-comments-or-files-to-tasks-in-todoist-CwiA50)). Không dùng comments làm kho chứa secrets hoặc dữ liệu khách hàng.

**Mẫu checkpoint:**

```text
[CHECKPOINT] YYYY-MM-DD
Done: ...
Observed / Tested: ...
Blocked / Open question: ...
Next action: ...
Evidence: ...
```

**Mẫu handoff/review ở Work:**

```text
[REVIEW] YYYY-MM-DD
Delivered: ...
Test cases: ...
Awaiting: ...
Owner to confirm: ... (chỉ khi được biết)
Next action after feedback: ...
```

**Mẫu học độc lập (Developer):**

```text
[LEARNING] YYYY-MM-DD
Attempted without AI: ...
Result / Failed cases: ...
Self-assessed autonomy (0–3, provisional): ...
Questions to review: ...
Next independent attempt: ...
```

Các mức 0–3 là **tự đánh giá**, không phải chứng nhận kỹ năng; nếu chưa có thực hành, ghi `Not assessed`.

### 7.18. Project-specific playbooks — Task mẫu có đủ trường

#### Case A — ParadiseHR: Stored Procedure + UI theo cơ chế thực tế

```yaml
title: "ParadiseHR / Chấm công — Sửa kết quả tìm kiếm theo phòng ban"
project: "Work"
section: "Ready"
labels: ["paradise", "database"]
priority: "P2"
date: null
context: "Màn hình gọi cơ chế xử lý SP từ JavaScript/Ajax wrapper có sẵn; cần xác nhận tên SP và điều kiện lọc từ task thực tế."
objective: "Kết quả truy vấn theo phòng ban trả đúng dữ liệu và được hiển thị như yêu cầu."
acceptance_criteria:
  - "Truyền đúng tham số đã xác nhận"
  - "Có dữ liệu hợp lệ, dữ liệu rỗng và điều kiện sai đều được xử lý phù hợp"
  - "Không gây hồi quy chức năng liên quan"
subtasks:
  - "Đọc yêu cầu và kiểm tra luồng gọi (được phép)"
  - "Tái hiện tình huống với dữ liệu test"
  - "Sửa logic SP hoặc giao diện đúng phạm vi"
  - "Thử lại và ghi bằng chứng không nhạy cảm"
notes: "Đây là ví dụ minh họa, KHÔNG phải ticket ParadiseHR đang tồn tại."
```

Nếu thực tế chủ yếu sửa script/Ajax, chuyển domain từ `database` sang `integration` hoặc `frontend` đúng trọng tâm. Nếu một việc lớn có hai deliverables độc lập (SP và giao diện), tách hai tasks, gắn `paradise` cho cả hai.

#### Case B — Developer: Bài học Java tự đánh giá

```yaml
title: "Java Core — Tự implement bài toán Employee Management bằng OOP"
project: "Developer"
section: "Ready"
labels: ["java", "engineering", "no_ai"]
priority: "P2"
date: null
objective: "Tự áp dụng class, encapsulation và collection vào chương trình Java nhỏ."
acceptance_criteria:
  - "Chạy được chương trình với dữ liệu giả"
  - "Tự giải thích được thiết kế các lớp và lý do phân chia trách nhiệm"
  - "Tự viết/kiểm thử tối thiểu tình huống hợp lệ và không hợp lệ"
  - "Ghi lại điểm đã tra tài liệu và điểm cần cải thiện"
evidence: "Link repository cá nhân hoặc ghi chú (sẽ bổ sung sau, không bịa link)."
```

#### Case C — English / GLV / Self (L2)

| Project/Section | Title | Description L2 / DoD | Labels |
|---|---|---|---|
| English / Speaking | `Speaking — Ghi âm mô tả một tính năng Backend bằng tiếng Anh` | Tạo ghi âm; tự nghe và ghi 3 chỗ cần sửa | Không cần |
| GLV / Lớp Thêm Sức 3B | `Soạn 5 câu hỏi ôn tập cho bài giáo lý ...` | Có 5 câu hỏi, phù hợp mục tiêu bài và được rà soát | Không cần |
| GLV / Khối TS | `Chuẩn bị danh sách việc cho hoạt động ...` | Checklist phân công và mục cần xác nhận | `event` |
| GLV / Ban Trực | `Xác nhận phân công trực với người phụ trách` | Có phản hồi hoặc xác định next action theo dõi | `follow_up` |
| Self & Life / Home & Organization | `Sắp xếp lại khu vực bàn làm việc` | Bề mặt sạch, đồ vật phân loại và có vị trí | Không cần |
| Self & Life / Career & Opportunities | `Điều chỉnh CV cho vị trí Backend tại công ty ...` | CV phù hợp JD thực tế, không khai kinh nghiệm sai, chuẩn bị file gửi | Không cần; `interview` chỉ khi phỏng vấn |

### 7.19. DoD & Task Quality Review — Checklist trước khi tạo hàng loạt

- [ ] Có hành động cụ thể, kết quả đủ nhỏ để complete?
- [ ] Title không chỉ là một chủ đề như `Học backend`?
- [ ] Scope/DoD đủ để vài tuần sau đọc vẫn hiểu?
- [ ] Đã chọn đúng Project và Section theo quy ước?
- [ ] Labels chỉ lấy từ registry 18; **không tự tạo nhãn thứ 19**?
- [ ] `paradise` được gắn cho việc thuộc ParadiseHR, không dùng sai ở Developer?
- [ ] Priority phản ánh ưu tiên **hiện tại**, không gắn P1 tùy tiện?
- [ ] Không có date/deadline giả hoặc thông tin ngày AI tự đoán?
- [ ] Tách subtasks hợp lý; không tạo 15 vi bước cho việc đơn giản?
- [ ] Có bằng chứng/điều kiện test cho learning/technical tasks?
- [ ] Không làm lộ thông tin nội bộ hoặc dữ liệu cá nhân nhạy cảm?
- [ ] Nếu công việc chưa đủ thông tin, chọn Inbox/Backlog hoặc yêu cầu xác minh; **không tự điền đáp án**?

---

## 8. Learning Architecture — Cách chuẩn bị roadmap mà không tạo task tràn lan

### 8.1. Định hướng đã xác nhận

- **Primary:** Backend Engineering, đủ khả năng làm việc độc lập và ứng tuyển Backend/Full-stack.
- **Depth:** Đi từ fundamentals đến advanced có thực hành và kiểm chứng, không chỉ xem video hoặc đọc tài liệu.
- **Tech stack muốn phát triển (cập nhật 09/11):** **Java → NestJS → Go**. Đây là **thứ tự mong muốn để thẩm định**, không có nghĩa chỉ học xong ngôn ngữ này mới được dùng ngôn ngữ kia. Tận dụng kinh nghiệm NestJS hiện có để phục hồi lập trình độc lập, tránh học lại không cần thiết.
- **Frontend:** ôn tập và duy trì, không chạy song song một roadmap FE nâng cao trừ khi mục tiêu nghề nghiệp thay đổi.
- **Current study topic:** Principles of Database Management (DBMS), đang ở giai đoạn chuẩn bị hệ thống học tập.
- **English:** nâng giao tiếp nghề nghiệp, chưa xây calendar IELTS cố định.

### 8.2. Cấp độ quản lý học tập

| Cấp độ | Ở đâu lưu? | Ví dụ |
|---|---|---|
| Direction | Tài liệu roadmap riêng, liên kết trong Todoist | Backend-first; Java/Spring; Go; NestJS |
| Track/Module | Tài liệu roadmap / mô tả một parent task | DBMS, OOP, API Design, Testing |
| Learning unit | Task Todoist | `DBMS — Chuẩn hóa schema đến BCNF` |
| Action steps | Subtasks | Đọc đề → Tự làm → Test → Giải thích |
| Learning evidence | Repo/notes/comment | ERD, SQL script, tests, giải thích |
| Competency verification | Assessment/learning tracker riêng | Tự làm đạt mức nào, lỗi hệ thống gì |

### 8.3. Mức độ tự chủ (quy ước chẩn đoán sau này)

| Mức | Biểu hiện |
|---|---|
| 0 | Chưa thể bắt đầu hoặc không nhớ phương pháp |
| 1 | Làm được với nhiều gợi ý/có đáp án dẫn dắt |
| 2 | Tự làm với tài liệu tham khảo, còn cần kiểm tra nhiều |
| 3 | Tự triển khai, test và giải thích được phương án |

**Không tự gán mức 3** cho chủ đề chỉ vì từng học hoặc từng làm ở công ty. Chưa có bài chẩn đoán thực hành = chưa kết luận năng lực hiện tại.

### 8.4. Tiêu chí trước khi nhập loạt task học tập

- [ ] Đã kiểm tra năng lực hiện tại ở các mảng trọng tâm.
- [ ] Đã chọn thứ tự ưu tiên học dựa trên mục tiêu nghề nghiệp và skill gaps thực tế.
- [ ] Mỗi learning unit có kết quả đầu ra, điều kiện hoàn thành và bài thực hành.
- [ ] Backlog khởi đầu vừa đủ; không import tất cả môn đại học vào Todoist.
- [ ] Không gắn ngày bắt buộc chỉ vì một roadmap có thứ tự nội dung.

---

## 9. Operating Rituals — Tập thói quen sử dụng Todoist không phụ thuộc giờ

### 9.1. Capture (ngay khi phát sinh)

- Suy nghĩ ra việc mới → **Quick Add vào Inbox**, gõ nhanh một câu có thể hiểu được.
- **Không bắt buộc** lựa chọn đúng project/label/priority khi capture.
- Nếu đang làm việc sâu, capture xong quay về công việc; không sa đà tối ưu Todoist.

### 9.2. Clarify & Organize (khi chuẩn bị thực hiện hoặc khi rảnh)

- Mở Inbox, tự hỏi: *Việc này có hành động cụ thể không?*
  - **Không:** xóa, đưa ý tưởng vào note hoặc viết thành một hành động rõ ràng.
  - **Có:** chọn project, section, priority và nhãn nếu cần.
- Nếu hành động lớn hơn một kết quả rõ ràng, chia thành task/subtask.
- **Không** có quy tắc phải xử lý Inbox đúng một giờ/ngày.

### 9.3. Execute (trước lúc học hoặc làm việc)

- Có lịch hẹn/hạn thật → xem **Today/Upcoming** trước.
- Không có hạn gấp → mở **Next Actions** hoặc `Developer → Ready` để chọn 1 việc.
- Khi muốn tập code độc lập → mở **Independent Practice**.
- Khi cần kiểm tra phản hồi → mở **Pending & Follow-ups**.
- Khi bắt đầu một việc trên Board, kéo từ `Ready` sang `In Progress`.

### 9.4. Close the loop (sau phiên làm việc)

- Xong thật → Complete.
- Chưa xong → cập nhật một checkpoint `Đã làm / Vướng / Next action`.
- Chờ bên ngoài → `Waiting` hoặc `follow_up` theo đúng quy ước.
- Tạm ngừng học → `On Hold` có lý do; không để hàng loạt task nằm mãi `In Progress`.

### 9.5. Review linh hoạt theo sự kiện

| Trigger | Hoạt động gợi ý | Có bắt buộc đúng giờ không? |
|---|---|---|
| Bắt đầu phiên học | Chọn 1 task `Ready` | Không |
| Kết thúc phiên học | Lưu checkpoint và evidence | Không |
| Có ngày rảnh hơn bình thường | Dọn Inbox, tái cân bằng P1/P2 | Không |
| Sắp phỏng vấn/đổi công việc | Rà soát `Career & Opportunities` | Theo ngày thực tế |
| Có nhiều task Waiting | Rà soát điều kiện follow-up | Theo nhu cầu |
| Sau một chặng học hoàn thành | Đánh giá thực hành, điều chỉnh backlog | Theo milestone |

**Bước khởi động thói quen:** Trong 10 lần tiếp theo mở Todoist, chỉ cần tập 3 hành vi: `capture → chọn task → update/complete`. Không theo streak; mục tiêu là giảm thao tác và không quên bước tiếp theo.

---

## 10. Change Management — Cách cập nhật hệ thống về sau

### 10.1. Nguyên tắc cập nhật

1. **Nhìn hệ thống thật trước khi sửa.** Ảnh chụp chỉ chứng minh phần giao diện được nhìn thấy; không suy ra Query/Description không hiển thị.
2. **Không thay đổi thầm lặng:** mỗi thay đổi quan trọng vào `Change Log`.
3. **Giữ tên chuẩn ổn định:** đặc biệt các sections như `Backlog`, `Waiting`, `On Hold` vì filter có phụ thuộc.
4. **Đánh giá tác động:** sửa label có thể ảnh hưởng các filter; sửa section có thể thay đổi tập task hiển thị; xóa project ảnh hưởng toàn bộ task trong đó.
5. **Chỉnh cấu hình trước, nhập task sau:** tránh sinh nhiều task rồi phát hiện phân loại sai.
6. **Thêm ít, kiểm tra trước, rồi mở rộng.** Khi quy tắc chưa rõ, ghi là candidate thay vì tạo ngay.

### 10.2. Checklist thay đổi Label

- [ ] Xác định nhu cầu sử dụng (ví dụ cần filter tasks testing xuyên Backend/Frontend).
- [ ] Kiểm tra có trùng Project, Section, Title hoặc label đã có không.
- [ ] Chốt tên lowercase, `snake_case`, không nhập dấu `%` vào tên.
- [ ] Chọn màu theo nhóm; không sử dụng màu như một thông tin nghiệp vụ độc lập.
- [ ] Tìm các task hiện tại cần gắn nhãn (nếu có).
- [ ] Kiểm tra các filters dùng label này.
- [ ] Cập nhật `Labels Registry` và Change Log.

### 10.3. Checklist thay đổi Filter

- [ ] Lý do thay đổi và tập task muốn thấy/không muốn thấy.
- [ ] Ghi query cũ và query mới.
- [ ] Kiểm tra cú pháp theo tài liệu Todoist mới nhất.
- [ ] Preview với task mẫu có cả positive và negative cases.
- [ ] Kiểm tra filter còn tương thích với tên section/label hiện tại.
- [ ] Vì giới hạn 3 filters Free, xác nhận filter nào bị thay thế (nếu thêm mới).
- [ ] Ghi kết quả test + ngày xác nhận trong registry/log.

### 10.4. Checklist thay đổi Project/Section

- [ ] Lĩnh vực mới có thật sự độc lập lâu dài không, hay chỉ là task/section mới?
- [ ] Có ảnh hưởng giới hạn 5 personal projects không?
- [ ] Nếu đổi tên Section, tìm tất cả Filter Query tham chiếu tên cũ.
- [ ] Xem task ở section cũ sẽ được chuyển sang đâu.
- [ ] Tạo bảng mapping `Old → New` nếu gộp/đổi cấu trúc.
- [ ] Cập nhật Project Registry, Section Registry, Filter test cases, Change Log.

### 10.5. Checklist nhập một loạt task mới

- [ ] Đã có nhu cầu và scope rõ ràng, tránh nhập để “cho đủ danh sách”.
- [ ] Tách objective dài hạn và task có đầu ra nhỏ.
- [ ] Có tiêu chí Complete rõ ràng cho mỗi learning/practical task.
- [ ] Không tự gán Completed, Progress hoặc mức năng lực.
- [ ] Labels không lặp trạng thái Section.
- [ ] Ngày chỉ đặt khi cần.
- [ ] Kiểm tra task mẫu trong ba Filters trước khi nhập hàng loạt.

### 10.6. Quy trình versioning cho file này

Dùng `MAJOR.MINOR.PATCH`:

- **MAJOR:** đổi kiến trúc project/section hoặc phương pháp vận hành căn bản (`2.0.0`).
- **MINOR:** thêm/bớt labels, filters, task templates, workflow quy mô vừa (`1.1.0`).
- **PATCH:** sửa mô tả, ví dụ, typo, làm rõ quy tắc (`1.0.1`).

Khi cập nhật: sửa header `version/last_updated`, thay nội dung registry, thêm entry log, ghi mục đã xác minh thực tế và mục vẫn đang chờ xác minh. **Không ghi các thay đổi chưa thao tác vào cột “đã áp dụng trên Todoist”.**

### 10.7. Mẫu Change Request

```markdown
## CR-YYYYMMDD-001 — [Tên thay đổi]
- Người đề xuất:
- Mục tiêu:
- Thành phần: Project / Section / Label / Filter / Task Standard
- Trạng thái: Proposed / Approved / Applied / Verified / Reverted
- Before:
- After:
- Impacted items:
- Migration steps:
- Validation / test cases:
- Ngày áp dụng:
- Ghi chú:
```

---

## Bản cập nhật vận hành 09/11/2026 — Plan Before Execution (v1.1.0; LƯU LỊCH SỬ)

> **Historical record, superseded in part by v1.3.0:** nội dung dưới đây phản ánh quyết định tại v1.1/v1.2; khi khác với Chương 4 v1.3, **Chương 4 và Snapshot v1.3 là nguồn hiện hành**. Đặc biệt, số lượng 13/17 và ý định chưa thêm `paradise` đã lỗi thời; ảnh mới xác nhận 18 labels và `paradise`.

> **Trạng thái:** Đã thống nhất các định hướng ở mức quyết định cá nhân; chưa tạo task học tập thực tế, chưa xác nhận các label mới đã thêm vào Todoist. Ngày 09/11 dành cho **thiết kế và phân loại**, không phải hạn hoàn thành toàn bộ Backend roadmap.

### A. Ưu tiên hiện tại

1. Khôi phục khả năng Software Development độc lập (tự phân tích → viết code → debug → kiểm thử; AI chỉ review/gợi ý sau khi tự thử).
2. Nâng năng lực Backend để tìm công việc phù hợp, vẫn duy trì cơ hội ứng tuyển Full-stack.
3. Cải thiện English for Work và Technical Interview.
4. Duy trì nhiệm vụ Paradise HR; riêng GLV và Self & Life không bỏ qua nhưng tránh biến thành gánh nặng hành chính.

### B. Phân vai rõ giữa Developer, Work, Career

- **Developer**: học nền tảng, lab Java/Spring, ôn NestJS, tìm hiểu Go, ôn các môn IU và FE tối thiểu. Không gắn deadline giả cho bài học.
- **Work**: task thật tại Paradise HR (gắn `paradise`); mỗi task có nghiệp vụ, đầu vào, đầu ra, cách kiểm tra, phụ thuộc, trạng thái. Luồng hiện được người dùng mô tả: **Stored Procedure / DB function → HTML (div)/CSS/JS → tương tác AJAX qua wrapper có sẵn**; **chi tiết kỹ thuật từng màn hình còn phải xác nhận sau**. Không đồng nhất kiến trúc này với một REST service thông thường.
- **Self & Life → Career & Opportunities**: tìm JD, chọn vị trí, cập nhật CV, nộp đơn, theo dõi phản hồi HR; bài luyện technical interview thuộc Developer.

### C. Labels — Trạng thái HIỆN HÀNH v1.3.0

- **Đã xác minh 18 labels trong UI** ở Chương 4 và Snapshot Chương 14. Không còn nhãn nào trong registry đang chờ tạo.
- **Nguồn ParadiseHR:** `paradise` (Olive Green) đã có thực tế; gắn vào các việc Work từ đơn vị này. Không đổi tự động sang `source_paradisehr`.
- **Nhãn hoạt động:** `event` và `follow_up` màu Yellow; `no_ai` màu Violet.
- **Nhãn công nghệ/kỹ năng:** `engineering`, `interview`, `java`, `go`, `nestjs` màu Green; các domain còn lại màu Blue. Chi tiết tên màu UI/API ở Chương 4.
- **GLV** dùng Sections `Lớp Thêm Sức 3B`, `Khối TS`, `Ban Trực`, `Công việc chung`; **Self & Life** quản lý việc dọn phòng/tập luyện/finance bằng Sections, không nhãn dư thừa.
- **Giữ nguyên ba filters**, query đã đề xuất chưa được kiểm chứng qua ảnh Edit/Preview.

### D. Các kiến thức từ kho IU — ưu tiên để chẩn đoán, CHƯA tạo chương trình học

- **Core:** Object-Oriented Programming, Data Structures and Algorithms, Principles of Database Management, Web Application Development, Software Engineering.
- **Systems:** Operating Systems, Computer Networks, Scalable and Distributed Computing, System & Network Security.
- **Foundational support:** Discrete Mathematics, Theoretical Models in Computing, Computer Architecture, Probability/Statistics, Computer Security.
- **Optional later:** AI/Data Mining, lĩnh vực phụ trợ theo năng lực thực tế và tín hiệu tuyển dụng. Chỉ dựa vào kho tài liệu có môn học không có nghĩa người dùng hiện còn thành thạo nội dung đó.

### E. Chuẩn Task/DoD

Một task cần đủ: **Action verb + Object + Result**. Trong Description lưu `Context / Input`, `Output`, `Definition of Done`, `Next action` (khi đang dở). Subtasks dùng cho các bước có thể kiểm tra.

**Ví dụ đề xuất để đưa vào Todoist sau khi rà soát:**

| ID tham chiếu | Project / Section gợi ý | Tên task | Labels | Đầu ra cần có |
|---|---|---|---|---|
| PLAN-01 | Self & Life / Personal Goals | Kiểm kê các cam kết hiện tại và việc tồn đọng | — | Danh sách đầu việc chưa xử lý |
| DEV-01 | Developer / Ready | Đối chiếu các môn IU với yêu cầu Backend/Full-stack và chọn nhóm phải ôn | `engineering` | Skill inventory ưu tiên, không phải toàn bộ syllabus |
| DEV-02 | Developer / Ready | Kiểm tra lại khả năng tự viết Java Core bằng bài thực hành ngắn | `java`, `no_ai` | Code tự viết + các lỗi gặp phải |
| DEV-03 | Developer / Backlog | Thiết kế bài thực hành DBMS tự giải | `database`, `no_ai` | Đề bài, dataset giả và tiêu chí kiểm chứng |
| DEV-04 | Developer / Backlog | Kiểm kê những phần NestJS đã từng làm và hiện còn tự làm được | `backend` | Ma trận known/rusty/unknown |
| WRK-01 | Work / Ready | Liệt kê các task thực tế Paradise HR và trạng thái hiện tại | — | Mỗi nhiệm vụ có yêu cầu, phụ thuộc, bước tiếp |
| WRK-02 | Work / Backlog | Vẽ luồng xử lý cho một màn hình mẫu từ DB đến HTML/CSS/JS/AJAX | `database`, `frontend` | Sơ đồ kiến trúc đã xác minh trên code được phép dùng |
| ENG-01 | English / Speaking | Tự ghi âm giới thiệu một dự án phần mềm bằng tiếng Anh | — | File ghi âm/bản tự đánh giá |
| CAR-01 | Self & Life / Career & Opportunities | Rà soát CV và chọn các nhóm JD Backend/Full-stack để đối chiếu | — | Khoảng trống kỹ năng và định hướng ứng tuyển |
| GLV-01 | GLV | Liệt kê hoạt động và cam kết GLV đang mở | — | Danh sách nghĩa vụ + mốc bắt buộc |

**Không import tất cả vào Today.** Các task chẩn đoán chỉ chuyển Ready khi có thể thực hiện thực sự, không đặt ngày nếu chưa có deadline thật.

### F. Checklist cho ngày tổ chức hệ thống 09/11 (theo kết quả, không theo giờ)

1. [ ] Brain dump trong Todoist Inbox: tất cả việc thực sự đang chờ; chưa gắn labels hàng loạt.
2. [ ] Rà lại 5 project, sections, chỉ sửa những gì gây nhầm lẫn.
3. [ ] Giữ nguyên ba filter; **18 labels đã xác minh**. Khi nhập task, gắn theo quy tắc Chương 4, không tạo label mới hoặc sửa filter tùy tiện.
4. [ ] Kiểm kê nhiệm vụ ParadiseHR, GLV (Thêm Sức 3B, Khối TS, Ban Trực), việc cá nhân, Career bằng các task có hành động cụ thể.
5. [ ] Chọn các môn IU trọng điểm, dựng bản đồ kiến thức Java → NestJS → Go mức **module** (chưa phân rã toàn bộ bài học).
6. [ ] Viết một số task đầu tiên có `Definition of Done` và `Next action`; kiểm tra có thể bắt đầu mà không phải hỏi lại "làm gì?".
7. [ ] Chọn tối đa 1–3 task P1/P2 thực sự có thể làm tiếp; cập nhật Inbox; tránh ép giờ học.

**Definition of Done cho ngày planning:** 5 project rõ ràng, các task thực tế được ghi nhận, các labels có mục đích, roadmap ở mức module, một tập việc Ready nhỏ có thể bắt đầu ngay lần kế tiếp. Không đo thành công bằng số lượng task nhập vào.

### G. Signals nghề nghiệp 2026–2031 (chỉ dùng để ưu tiên kiểm chứng)

- WEF Future of Jobs Report 2025 dự báo software developers vẫn thuộc các nhóm nghề công nghệ tăng trưởng nhanh đến 2030, đồng thời kỹ năng liên quan AI, dữ liệu, network/security và tư duy phân tích gia tăng tầm quan trọng: https://www.weforum.org/publications/the-future-of-jobs-report-2025
- Một theo dõi tin tuyển dụng tại Việt Nam cập nhật 31/10/2026 ghi nhận Java được nêu trong tiêu đề vị trí nhiều hơn Go trong một mẫu quan sát; không dùng thống kê này để kết luận chắc chắn mức cầu toàn thị trường 2031: https://www.vitx.global/insights/vietnam-hiring-pulse
- **Hành động:** ưu tiên CS foundations, SQL, testing, backend architecture, security, debugging, English; đánh giá Java/Spring trước, ôn NestJS dựa trên dự án cũ, rồi mở rộng Go khi có nền tảng và bằng chứng thực hành.

---

## 11. Change Log & Decision Log

| Ngày | Version | Thay đổi/Quyết định | Applied in Todoist? | Verification |
|---|---|---|---|---|
| 2026-11-09 | 1.0.0 | Tạo tài liệu master; xác lập cấu trúc 5 lĩnh vực, quy chuẩn sections, labels, filters, task templates và change management | Tài liệu: Có; cấu trúc project/section: chưa xác nhận toàn bộ | Spec baseline |
| 2026-11-09 | 1.0.0 | Ghi nhận 7 labels và 3 filters nhìn thấy trong ảnh | Có tên labels/filter | ✅ Tên/màu tương đối đã quan sát |
| 2026-11-09 | 1.0.0 | Ghi 3 filter queries chuẩn mục tiêu trong tài liệu | Chưa xác nhận UI đã lưu các query này | 🔎 Cần Edit + Preview |
| 2026-11-09 | 1.0.0 | Quyết định tách Job Search vào Self & Life, Developer chỉ luyện năng lực kỹ thuật, Work dành cho việc thực tế | Thiết kế đã thống nhất; chưa kiểm tra task đã được chuyển | 📋 |
| 2026-11-09 | 1.0.0 | Không tạo labels thời gian/phương thức hoặc roadmap learning hàng loạt lúc này | Chủ trương quản lý | 📋 |
| 2026-11-09 | 1.1.0 | Chốt Java → NestJS → Go là thứ tự mong muốn; đề xuất thêm `engineering`, `java`; giữ 3 filters không sửa; thêm checklist ngày lập kế hoạch, task chuẩn và quy ước ParadiseHR | Đề xuất/tài liệu tại thời điểm v1.1.0; **sau đó ảnh UI xác nhận đã có** `engineering`, `java` | 📋 + ✅ ảnh mới nhất |
| 2026-11-09 | 1.2.0 | Đối chiếu ảnh UI: xác nhận 13 labels; chốt registry 17 với 4 label chưa xác nhận UI (`testing`, `security`, `devops`, `event`); cập nhật GLV theo 3 vai trò + công việc chung; chuẩn hóa mapping ParadiseHR, Self & Life, task playbooks và change rules | **Tài liệu: đã cập nhật. Todoist: 13 label xác nhận qua ảnh; 4 label chưa xác nhận đã tạo.** | ✅/📋 phân biệt trạng thái |
| 2026-11-09 | **1.3.0** | Xác nhận **18 labels** qua ảnh; gắn label nguồn `paradise` màu Olive Green; chuẩn hóa chính xác tên màu theo API; thêm chuẩn tạo task chi tiết, examples và quy tắc Gemini/AI đọc/soạn/ghi task. | **Tài liệu: đã cập nhật. Todoist: nhãn đã nhìn thấy, không tự tạo/sửa task hoặc filter.** | ✅ Labels; 🔎 task inventory/queries chưa kiểm |

### Open Questions / Những gì cần xác nhận ở các lần sau

- [ ] Project trong giao diện đã đổi từ `Working` thành `Work` chưa?
- [ ] Sections nào đã tạo thật trong cả 5 project, đặc biệt GLV `Lớp Thêm Sức 3B`, `Khối TS`, `Ban Trực`, `Công việc chung`?
- [ ] 3 filters đang dùng **Query thực tế** nào? Đã Preview với tập test chưa?
- [ ] Thói quen capture/update/complete hoạt động đến đâu sau thời gian sử dụng thực tế?
- [ ] Năng lực Java, Go, NestJS hiện tại sau diagnostic assessment?
- [x] `testing`, `security`, `devops`, `event` đã được tạo và nhìn thấy trong ảnh mới nhất.
- [x] `paradise` đã tồn tại, màu **Olive Green** đúng như cửa sổ Edit.
- [ ] Đã có task ParadiseHR thực tế được gắn nhãn `paradise` chưa? (chưa thấy ảnh task)
- [ ] Mục tiêu nghề nghiệp cụ thể và English diagnostic đã đủ rõ để viết roadmap chưa?

---

## 12. Prompt cập nhật tài liệu — Có thể copy dùng trong các cuộc trò chuyện sau

```text
Bạn đang hỗ trợ tôi quản lý Todoist Personal Operating System.
File Todoist_document_v1.3.0.md (hoặc bản Master mới nhất) đính kèm là nguồn cấu hình gốc.

Yêu cầu thay đổi mới:
[Điền yêu cầu]

Hãy thực hiện theo thứ tự:
1) Đọc toàn bộ registry và phân biệt ĐÃ ÁP DỤNG / ĐÃ THỐNG NHẤT / CHƯA XÁC MINH.
2) Phân tích liệu thay đổi có cần thiết hay đang trùng với Project/Section/Label/Priority hiện có; **dùng Label Registry v1.3 (18 labels) và màu API đúng tên**.
3) Chỉ rõ Before → After; danh sách task, label, filter hoặc section bị ảnh hưởng.
4) Đề xuất thao tác Todoist cụ thể, query chính xác (nếu có), test cases và phương án rollback.
5) Cập nhật chính file Markdown: version, last_updated, registry, open questions, change log.
6) Trả về FILE MARKDOWN HOÀN CHỈNH mới để tôi lưu làm phiên bản gốc tiếp theo.

Không tự cho rằng đã thao tác thành công trong Todoist nếu không có xác nhận công cụ/UI.
Không tạo thêm labels, filters hoặc projects nếu không có use case rõ ràng; không đổi tên `paradise` hoặc sinh `source_paradisehr` ngầm.
Không lên lịch cứng cho những task học tập không có deadline.
```

---

## 13. Official Todoist Documentation — Tham khảo khi UI hoặc cú pháp thay đổi

> Đã đối chiếu công khai ngày **09/11/2026**. Tài liệu Todoist có thể thay đổi; cần kiểm tra lại khi sửa filter quan trọng hoặc khi ứng dụng thay đổi tính năng.

1. [Introduction to filters](https://www.todoist.com/help/todoist/features/introduction-to-filters-V98wIH) — Query syntax, priority, labels, section, wildcard, supported/unsupported cases; Last updated 06/11/2026.
2. [Introduction to labels](https://www.todoist.com/help/todoist/features/introduction-to-labels-dSo2eE) — Tạo/sửa/xóa labels, `%` notation; Last updated 04/09/2026.
3. [Use the board layout](https://www.todoist.com/help/todoist/features/use-the-board-layout-in-todoist-AiAVsyEI) — Section là cột, quản lý task dạng Board; Last updated 04/11/2026.
4. [Introduction to projects](https://www.todoist.com/help/todoist/features/introduction-to-projects-TLTjNftLM) — Project, favorites, cấu trúc và tổ chức; Last updated 05/11/2026.
5. [Usage limits in Todoist](https://www.todoist.com/help/account-and-billing/plans/usage-limits-in-todoist-e5rcSY) — Giới hạn plan.
6. [Todoist Pricing](https://www.todoist.com/pricing/) — Beginner/Pro và số lượng personal projects/custom filters.
7. [Todoist API v1 — Colors](https://developer.todoist.com/api/v1/) — bảng màu chuẩn IDs/names/hex: `blue`, `green`, `olive_green`, `yellow`, `violet`.
8. [Introduction to tasks](https://www.todoist.com/help/todoist/features/introduction-to-tasks-080OAXric) — đặt tên task bắt đầu với động từ, chia nhỏ task.
9. [Add a task description](https://www.todoist.com/help/todoist/features/add-a-task-description-in-todoist-rOryWIHn) — description (16.384 ký tự), Search descriptions, Quick Add.
10. [Use Task Quick Add](https://www.todoist.com/help/todoist/features/use-task-quick-add-in-todoist-va4Lhpzz) — `%` labels, `#` project, natural dates.
11. [Use keyboard shortcuts](https://www.todoist.com/help/todoist/features/use-keyboard-shortcuts-in-todoist-Wyovn2) — keyboard shortcuts desktop/web.
12. [Add comments or files](https://www.todoist.com/help/todoist/features/add-comments-or-files-to-tasks-in-todoist-CwiA50) — checkpoints và nhật ký theo thời gian.
13. [Introduction to sections](https://www.todoist.com/help/todoist/features/introduction-to-sections-rOrK0aEn) — section descriptions.
14. [Introduction to projects](https://www.todoist.com/help/todoist/features/introduction-to-projects-TLTjNftLM) — project descriptions.
15. [Todoist API v1 & official CLI](https://developer.todoist.com/api/v1/) — API/CLI dành cho integrations, có hướng dẫn Gemini skill nhưng **không hàm ý Gemini đã kết nối**.

---

## 14. Snapshot để đồng bộ trong tương lai

```yaml
configuration_snapshot:
  date: "2026-11-09"
  version: "1.3.0"
  app: Todoist
  assumed_plan: Beginner
  roadmap_started: false
  projects_target: ["Developer", "English", "Work", "GLV", "Self & Life"]
  projects_actual_status: partially_unverified
  board_projects: ["Developer", "Work"]
  list_projects: ["English", "GLV", "Self & Life"]
  labels_verified_count: 18
  labels_target_count: 18
  labels_seen_in_ui:
    - paradise
    - event
    - follow_up
    - engineering
    - interview
    - go
    - java
    - nestjs
    - no_ai
    - backend
    - database
    - devops
    - dsa
    - frontend
    - integration
    - security
    - systems
    - testing
  label_colors_verified_by_edit_dialog:
    paradise: olive_green
    event: yellow
    engineering: green
    no_ai: violet
    backend: blue
  label_colors_observed_by_list:
    follow_up: yellow
    interview: green
    go: green
    java: green
    nestjs: green
    database: blue
    devops: blue
    dsa: blue
    frontend: blue
    integration: blue
    security: blue
    systems: blue
    testing: blue
  label_source_convention: "paradise (exact existing name), not source_paradisehr"
  glv_sections_target: ["Lớp Thêm Sức 3B", "Khối TS", "Ban Trực", "Công việc chung"]
  glv_sections_verified_in_ui: false
  work_primary_source: ParadiseHR
  paradise_hr_workflow_description_verified_from_user: true
  paradise_hr_code_architecture_verified: false
  filters_seen_in_ui: ["Next Actions", "Independent Practice", "Pending & Follow-ups"]
  filters_frozen: true
  filter_queries_verified_in_ui: false
  task_inventory_verified: false
  ai_agent_policy: "draft_and_validate_before_write; never_invent_tasks_or_deadlines"
  key_principle: flexible_task_based_progress_not_fixed_hour_schedule
```

**Kết luận vận hành:** Todoist quản lý các hành động có thể hoàn thành; tài liệu Master lưu kiến trúc và quy tắc; source/repo/notes lưu kiến thức và bằng chứng; Gemini/AI chỉ được hành động trên dữ liệu đã xác minh và quyền được cấp.

---

## 15. Gemini / AI Task Agent Contract — Quy chuẩn AI đọc và tạo task

> **Mục tiêu:** Sau này bạn có thể tải file này vào Gemini cùng dữ liệu Todoist (qua export/connector/API/CLI nếu được người dùng cho phép), yêu cầu phân tích và đề xuất task mà không lệch cấu trúc. **Không giả định Gemini tự có quyền đọc/ghi Todoist.** Chỉ đọc được nếu có đầu vào hoặc tích hợp thực sự được xác nhận. Sự tồn tại của API/CLI không có nghĩa đã kết nối.

### 15.1. Thứ tự nguồn sự thật

1. **Ảnh/UI hoặc Todoist export/API mới nhất đã được xác nhận:** trạng thái thực tế của task, project, label, section, query.
2. **Master v1.3.0 này:** quy tắc đặt tên, phân loại, màu, behavior, consent boundaries.
3. **Thông tin người dùng mới nhất:** nhiệm vụ/ưu tiên/doD/chốt deadline cụ thể.
4. **Tài liệu nguồn/brief/ticket được phép chia sẻ:** dữ liệu yêu cầu và evidence.
5. **Suy luận của AI:** chỉ được đề xuất, phải ghi rõ `Assumption/Needs confirmation`.

Khi có mâu thuẫn: báo khác biệt, **không âm thầm sửa**; không tự biến task được đề xuất thành task đã có. Lịch sử trong Chương 11 chỉ là log, không được lấy quyết định cũ 13/17 labels làm cấu hình hiện hành.

### 15.2. Chế độ hoạt động và mức quyền

| Mode | Được làm | Không được làm |
|---|---|---|
| **READ_ONLY** | Đọc, nhóm, tóm tắt, phát hiện lỗi metadata, chỉ ra blockers | Tạo/sửa/complete/delete task |
| **DRAFT** (mặc định) | Đề xuất danh sách task có đủ metadata, DoD và next action | Ghi trực tiếp vào Todoist khi chưa được cho phép |
| **APPLY_APPROVED** | Sau khi người dùng duyệt, dùng kết nối xác nhận để tạo/sửa đúng các mục được duyệt | Thay đổi ngoài danh sách, tự động thêm label/filter/project |
| **RECONCILE** | Đối chiếu bản nháp với task hiện có, phát hiện trùng/lệch | Tạo bản sao task, merge/delete khi chưa được phép |

**Các hành động nhạy cảm phải được duyệt riêng:** delete, complete hàng loạt, đổi tên Project/Section/Label, thay Filter Query, gắn ngày hàng loạt, di chuyển task có link ngoài hoặc chỉnh priority P1 hàng loạt. Không bao giờ yêu cầu người dùng gửi API token/secret vào nội dung task hoặc chat thông thường.

### 15.3. Schema trung gian chuẩn — KHÔNG phải CSV native Todoist

```yaml
schema_version: "1.0"
operation: "create" # create | update | no_change | needs_review
local_ref: "DRAFT-WRK-001" # unique within proposal, KHÔNG phải Todoist task ID
todoist_task_id: null # only if obtained from real Todoist UI/API/export
title: "ParadiseHR / Module — Hành động + kết quả"
project: "Work"
section: "Ready"
priority: "P2"
labels: ["paradise", "database"] # MUST be subset of 18 registered names
date: null # ISO-8601 date only when confirmed
external_deadline: null # informational; not a paid Todoist Deadline field
parent_task_ref: null
description:
  context: "Yêu cầu đã xác minh"
  objective: "Kết quả mong muốn"
  scope_in: ["..."]
  scope_out: []
  prerequisites: []
  acceptance_criteria: ["..."]
  evidence: []
  next_action: "..."
subtasks:
  - title: "Bước nhỏ có thể kiểm tra"
    completed: false
comment_draft: null
source:
  kind: "user_instruction" # user_instruction | Todoist_UI | approved_document | inference
  reference: null
  verified: true
confidence: "high" # high | medium | low
needs_confirmation: []
```

**Quy tắc dữ liệu:** `todoist_task_id` không được suy diễn từ title; nếu trống, trước khi create phải kiểm tra task trùng ở cùng Project/Section theo title/mục tiêu/source. Mã `local_ref` chỉ phục vụ trao đổi và chống nhầm trong bản đề xuất. Không biến YAML này thành cú pháp nhập trực tiếp Todoist. Nếu import CSV, dùng đúng template CSV của Todoist và kiểm tra thứ tự priority/indent vì định dạng import có quy ước riêng ([CSV docs](https://www.todoist.com/help/account-and-billing/security/import-or-export-a-project-as-a-csv-file-in-todoist-YC8YvN)).

### 15.4. Deterministic routing — Đưa task vào đúng nơi

1. Nếu là **học/ôn/đánh giá kỹ năng** → `Developer`; nếu tiếng Anh là mục tiêu đầu ra chính → `English`.
2. Nếu là **nhiệm vụ công việc đã nhận** → `Work`; từ ParadiseHR → thêm label `paradise`.
3. Nếu là **GLV** → một trong bốn sections theo trách nhiệm, **không** tạo nhãn vai trò.
4. Nếu là **ứng tuyển, CV, HR/career administration** → `Self & Life / Career & Opportunities`; technical interview lab → `Developer`.
5. Nếu là việc **sinh hoạt/sức khỏe/finance** → section Self & Life tương ứng; không thêm label vô ích.
6. Nếu chưa biết project/source/acceptance criteria: giữ `Inbox` hoặc **DRAFT needs_review**, không tự đoán.
7. Với Board: dùng `Backlog` nếu thiếu yêu cầu/không ưu tiên; `Ready` khi đủ điều kiện bắt đầu; `In Progress` chỉ khi người dùng xác nhận đang thực hiện; `Waiting`/`Review` khi đúng trạng thái có bằng chứng. **Không tự đánh dấu task hoàn thành hoặc công việc đã được nghiệm thu.**

### 15.5. Bắt buộc kiểm tra trước khi Gemini đề xuất task

- [ ] Có nguồn rõ ràng cho yêu cầu; phân biệt yêu cầu thật với ví dụ minh họa.
- [ ] Title bắt đầu với hành động và có output.
- [ ] Mọi label trong registry 18, đúng chính tả; source ParadiseHR dùng `paradise`.
- [ ] Project/Section hợp lệ và đúng chức năng.
- [ ] P1/P2 không được gán tùy tiện; không đặt ngày nếu người dùng không yêu cầu.
- [ ] DoD/test đủ để xác minh hoàn thành; không bịa testcase nghiệp vụ.
- [ ] Tránh duplicate/split thiếu lý do hoặc bỏ qua dependency.
- [ ] Không chứa credentials, dữ liệu khách hàng, source nội bộ trái phép.
- [ ] Nếu thiếu thông tin, `needs_confirmation` rõ ràng; vẫn có thể tạo **DRAFT** với một next action để xác minh.
- [ ] Có kế hoạch diff/rollback khi định thay đổi task hiện có.

### 15.6. Prompt dùng khi yêu cầu Gemini ĐỌC task

```text
Bạn là Task Auditor cho Todoist Personal Operating System.
Nguồn quy tắc: file Todoist_document_v1.3.0.md đính kèm.
Nguồn dữ liệu công việc: Todoist export / danh sách task / kết quả connector mà tôi cung cấp riêng.
Mode = READ_ONLY. Không được tự ghi/sửa/hoàn thành/xóa task.

Thực hiện:
1. Đọc registry 5 project, 18 labels, các sections và workflows. Nêu mức độ truy cập dữ liệu thực tế.
2. Phân loại task theo Project → Section → Labels → Priority, giữ nguyên task IDs nếu có.
3. Chỉ ra title mơ hồ, task trùng, thiếu DoD, labels sai, waiting không có next action và deadline chưa xác minh.
4. Đề xuất chỉnh sửa Before → After, mức tự tin và nguồn chứng minh. Không tự thêm nhãn hoặc dự án.
5. Nếu dữ liệu không có task/completed history, nói rõ không đủ dữ liệu để kết luận tiến độ.
6. Trả về báo cáo và bảng changes DRAFT, chưa thực thi.
```

### 15.7. Prompt dùng khi yêu cầu Gemini VIẾT task

```text
Bạn là Task Author cho Todoist Personal Operating System.
Đọc file Todoist_document_v1.3.0.md, đặc biệt Chương 4, 7 và 15.
Mode = DRAFT. Chỉ tạo bản nháp, không gửi API hoặc chỉnh Todoist khi tôi chưa duyệt.

Dữ liệu đầu vào:
- Yêu cầu/công việc thực tế: [dán brief hoặc mô tả]
- Bằng chứng/nguồn: [link/file được phép chia sẻ]
- Priority/date đã xác nhận (nếu có): [...]

Đầu ra cho mỗi task:
- local_ref; title; project; section; labels; priority; date
- description: Context, Objective, Scope, Dependencies, Acceptance Criteria, Evidence, Next Action
- subtasks khi thật sự cần
- source, verified, confidence, needs_confirmation

Quy tắc:
- Không suy đoán ticket, deadline, status, dữ liệu khách hàng hay tên SP chưa được xác minh.
- Chỉ dùng 18 labels hiện có; task ParadiseHR dùng `paradise`.
- Không tạo thêm project/filter/label.
- Không dùng ngày học cố định; ưu tiên backlog có thể thực hiện linh hoạt.
- Nếu đầu vào chưa đủ, xuất một DRAFT có bước 'Xác minh yêu cầu' thay vì bịa nghiệp vụ.
- So sánh với danh sách task hiện tại nếu được cung cấp, đánh dấu nguy cơ trùng.
```

### 15.8. Nếu muốn Gemini trực tiếp thao tác Todoist trong tương lai

Todoist có **API v1** và **CLI chính thức**; tài liệu Todoist API có hướng dẫn cài CLI và skill dành cho Gemini (`td skill install gemini`). Đây chỉ là **khả năng tích hợp**, không có nghĩa Gemini đã tự kết nối với tài khoản. Muốn thực thi, bạn phải thiết lập kết nối/ủy quyền theo hướng dẫn của công cụ đó và xác nhận các quyền thao tác. **Không lưu token vào tài liệu Master, task hoặc nhật ký**, ưu tiên cơ chế xác thực/credential manager chính thức. Nguồn: [Todoist API & CLI](https://developer.todoist.com/api/v1/).

---

## 16. Audit & Regression Scenarios — Bộ test tài liệu khi thay đổi sau này

| Test ID | Tình huống | Kết quả đúng |
|---|---|---|
| REG-01 | Có task Work nguồn ParadiseHR | `paradise` + domain phù hợp, không tự tạo `source_paradisehr` |
| REG-02 | Có task tập thể dục | `Self & Life / Health & Fitness`, không gắn nhãn không cần thiết |
| REG-03 | Có task GLV Ban Trực | `GLV / Ban Trực`, `follow_up` chỉ khi cần liên hệ |
| REG-04 | Có bài Java tự luyện | `Developer`, `java`, `no_ai` và domain nếu cần, không đặt date giả |
| REG-05 | Có task chờ duyệt Work | `Waiting` hoặc `Review` đúng trạng thái, không tự complete |
| REG-06 | Gemini đọc một ticket thiếu acceptance criteria | Trả `needs_confirmation`, không bịa kết quả |
| REG-07 | Gemini được yêu cầu tạo task đã tồn tại | Trả `possible_duplicate` và đề nghị update/reconcile thay vì create ngay |
| REG-08 | Đổi tên `paradise` | Yêu cầu migration plan và phê duyệt, không đổi âm thầm |
| REG-09 | Chỉnh section `Waiting` | Kiểm tra ảnh hưởng 3 filter queries, không tự sửa filter |
| REG-10 | Tạo title `Học Java` | Yêu cầu phân rã thành đầu ra cụ thể trước khi đưa Ready |
| REG-11 | Có 18 labels nhưng màu khác sắc độ trên dark mode | Dựa tên màu UI/API, không tự suy từ pixel |
| REG-12 | Thực hành chưa có bài test/bằng chứng | Không đánh dấu mức năng lực 3 hay task hoàn thành |

**Quy trình cập nhật v1.3+**: (1) đọc snapshot mới nhất → (2) tạo Change Request/Before–After → (3) cập nhật registry và task standards → (4) chạy checklist REG-01..12 → (5) tăng version và ghi Change Log → (6) chỉ cập nhật Todoist khi người dùng yêu cầu và kết nối thực tế cho phép.
