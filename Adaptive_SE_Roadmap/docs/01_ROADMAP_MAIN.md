# ADAPTIVE ROADMAP — MAIN / MASTER PLAN

```yaml
roadmap_id: SE-ADAPTIVE-2026
roadmap_version: 1.0.0
as_of: 2026-11-09
owner_confirmation: provisional_bootstrap_from_user_requests
status: active_direction_not_learning_started
primary_direction: Backend Software Engineer
secondary_capabilities: [Full-stack, Systems/Cloud, Applied-AI-literacy]
principle: competencies_first_milestones_with_full_subject_anchor
execution_model: flexible_outcome_based_no_fake_deadlines
```

## 1. Career north star

Phát triển thành **Backend Software Engineer** tự chủ từ phân tích yêu cầu → thiết kế → code → test → data integrity → deploy/observe; giữ React/NextJS như lợi thế Full-stack; phát triển Cloud/DevOps để tự vận hành ứng dụng; mở đường sang Applied AI/AI Systems, Go, Thạc sĩ hoặc nghiên cứu khi có lý do phù hợp. **Không hứa mức chức danh/lương hoặc deadline đạt mục tiêu.**

Năng lực xuyên suốt: **English for Engineering**, independent coding, critical thinking, AI usage with verification, ethics/privacy, khả năng học suốt đời.

### Current vs target

- Kinh nghiệm đã có: React/TypeScript, NestJS, relational DB, enterprise workflow, LinguaPanda, eSign/e-Retire; Java/Go/Python ở mức nền tảng/tự đánh giá.
- Vấn đề cần cải thiện: code independence sau thời gian dùng AI, DSA/OS/networks, testing, security, distributed thinking và khả năng cạnh tranh nghề nghiệp.
- Target: khả năng tự làm và giải thích, không chỉ hoàn thành tutorial. Không đồng nhất target với tỷ lệ task hoàn thành.

## 2. Nguyên tắc cấu trúc

1. **Milestone = outcome + course anchor + evidence + gate.** Không phải “học xong vài chương đã xong milestone”.
2. **Mỗi milestone closure yêu cầu ít nhất một môn/miền kiến thức được hoàn tất ở phạm vi FULL đã thống nhất,** theo `docs/02_COMPETENCY_AND_COURSE_MAP.md`. Những môn cross-track chỉ “covered partly” không được ghi là hoàn tất.
3. Course anchor = đề cương học phần xác định; nếu chỉ có báo cáo thư viện IU tái dựng, phải đánh dấu `reconstructed/awaiting syllabus confirmation` và chỉ được xác nhận hoàn thành **phạm vi tái dựng đã thống nhất**, không tuyên bố hoàn thành học phần chính thức.
4. Quy trình mastery đúng ý người dùng: **PASS 1 — tự ôn toàn bộ outline → PASS 2 — diagnostic nhẹ/theo chủ đề → PASS 3 — ôn sâu, học bổ sung, thực hành & đánh giá độc lập → FINAL AUDIT**. Có thể nhảy qua chủ đề đã có bằng chứng tốt nhưng vẫn phải audit toàn bộ syllabus.
5. Milestones định hướng theo **dependency mềm** (có thể học chéo), không ấn định tháng/tuần; chỉ một focus chính, tối đa hai learning units kỹ thuật cùng lúc.
6. Học theo learning units nhỏ nhưng hoàn thành milestone bằng **tổng hợp toàn miền**, tránh học tản mạn.
7. Todoist quản lý hành động; hồ sơ này quản lý ý nghĩa/mốc, tránh tạo hàng trăm task.

## 3. Milestone Registry

| ID | Milestone | Anchor môn/miền phải FULL | Khi nào xem xét active | Trạng thái hiện tại |
|---|---|---|---|---|
| `MS-01` | Programming Autonomy & OOP | `SUB-OOP` — IU Object Oriented Programming (Java) | Candidate đầu tiên; phù hợp mong muốn Java | `candidate` — CHƯA BẮT ĐẦU |
| `MS-02` | Algorithms & Problem Solving | `SUB-DSA` — IU Data Structures and Algorithms | Có thể xen kẽ MS-01; không ép sau Java | `not_started` |
| `MS-03` | Backend Development & Data Integrity | `SUB-DBMS` — IU Principles of Database Management | Khi cần đào sâu backend/ParadiseHR | `not_started` |
| `MS-04` | Runtime, Concurrency & Linux Foundations | `SUB-OS` — IU Operating Systems | Khi các bài toán concurrency/system trở nên thiết thực | `not_started` |
| `MS-05` | Networked & Reliable Backend Systems | `SUB-CN` — IU Computer Networks | Khi làm APIs, timeouts, distributed services | `not_started` |
| `MS-06` | Software Engineering & Production Delivery | `SUB-SE` — IU Software Engineering | Sau hoặc song song tích lũy evidence sản phẩm | `not_started` |
| `MS-07` | Chuyên sâu tự chọn (Systems/AI/Go/Research) | **Chưa khóa anchor**; cần chọn **một** miền đầy đủ + syllabus/DoD trước khi active | Sau khi có trải nghiệm và market signal đủ rõ | `not_started / conditional` |

> Đây là **bản đồ mốc**, không phải thứ tự buộc học xong 6 môn mới được viết backend. Việc lập trình backend/Java/Spring/NestJS, testing, English và job search có thể được thực hành qua nhiều mốc. Mỗi môn là một *anchor of completeness*, không phải toàn bộ kết quả milestone.

### MS-01 — Programming Autonomy & OOP

**Outcome:** có khả năng tự tổ chức và triển khai Java program, giải thích lựa chọn OOP, xử lý exception/generics và tự sửa lỗi thay vì chỉ dựa vào AI.

**Course anchor:** `SUB-OOP`, đầy đủ đề cương OOP IU được xác nhận. Baseline thư viện: class/object, constructors/access, overloading, inheritance, polymorphism, abstraction/interface, collections/generics, exceptions; một số bộ có GUI, SOLID, design patterns, JSoup. **Biến thể GUI/SOLID/patterns không được âm thầm bỏ:** phải chọn bộ môn/giảng viên làm chuẩn và ghi scope cho từng phần.

**Non-anchor applied extensions:** JDK tools, IDE/debugger, unit testing, Java memory basics, Java coding conventions, independent practice. NestJS dùng để đối chiếu nếu hữu ích.

**Closure gate:** tất cả mandatory topics của `SUB-OOP` reviewed/diagnosed/reinforced/validated; có bài lab Java độc lập + tests + một bài design mới giải thích trade-offs; có log và scope audit. Không cho điểm/chuyển done trước.

### MS-02 — Algorithms & Problem Solving

**Outcome:** lựa chọn đúng cấu trúc dữ liệu, phân tích chi phí thời gian/bộ nhớ, cài thuật toán và giải một bài mới độc lập.

**Course anchor:** `SUB-DSA` IU đầy đủ: complexity, arrays/linked lists, stacks/queues, sorting/searching, recursion, trees, hash tables, graph basics và mọi chương bắt buộc còn lại sau audit syllabus. Không thay thế full-course gate bằng “100 LeetCode”.

**Extensions:** problem decomposition, constraints/edge cases, property-based testing và Java collections trade-offs.

**Closure gate:** coverage 100% mandatory topics, tổng hợp data-structure selection, coding exam/lab và giải thích complexity/test bằng code mình làm.

### MS-03 — Backend Development & Data Integrity

**Outcome:** tự thiết kế một backend service có DB, API contract, validation, transactions, auth, tests; xử lý data consistency và concurrency đúng.

**Course anchor:** `SUB-DBMS` đầy đủ từ data model/ER, relational algebra, SQL, FDs, normalization đến query optimization, concurrency/transactions và recovery tùy đề cương. Công việc Stored Procedure chỉ là nguồn bài toán, không chứng minh tự động full course.

**Extensions:** Java/Spring Boot, NestJS, API design, automated tests, security, pagination, DB migration, schema evolution. **Learning module API có thể bắt đầu trước khi DBMS full**.

**Closure gate:** `SUB-DBMS` completed theo contract + backend artifact độc lập với migrations/tests + giải thích ít nhất một concurrency/performance trade-off.

### MS-04 — Runtime, Concurrency & Linux Foundations

**Outcome:** hiểu process/thread, scheduling, synchronization, memory, filesystem và biết áp dụng vào debugging backend Linux.

**Course anchor:** `SUB-OS` đầy đủ: processes, threads/synchronization, CPU scheduling, deadlock, memory, virtual memory, I/O, file systems/disk; bổ sung phần đề cương còn thiếu sau xác minh.

**Extensions:** Linux CLI, processes/permissions, resource monitoring, Java/Node concurrency, Docker namespaces/cgroups ở mức hiểu cơ chế.

**Closure gate:** `SUB-OS` full coverage + lab mô phỏng concurrency hoặc scheduling/memory + mô tả root cause của một runtime failure.

### MS-05 — Networked & Reliable Backend Systems

**Outcome:** phân tích end-to-end request qua DNS/HTTP/TLS/TCP, troubleshoot network failure/timeouts, thiết kế retry/idempotency/queue có kiểm chứng.

**Course anchor:** `SUB-CN` Computer Networks đầy đủ: layered model, application/transport, IP addressing/subnet/routing, link/Ethernet cùng các phần bắt buộc còn lại của syllabus chuẩn.

**Extensions:** HTTP behavior, API gateway/reverse proxy, caching, timeout/backoff, queues, microservice boundaries; introductory distributed systems (không coi đã hoàn tất môn SDC nếu chưa học đủ syllabus).

**Closure gate:** `SUB-CN` full coverage + packet/network lab, failure-mode report và backend reliability test.

### MS-06 — Software Engineering & Production Delivery

**Outcome:** thực hiện end-to-end một feature/service từ requirements, design, implementation, testing, release, observability, postmortem/quality review.

**Course anchor:** `SUB-SE` IU Software Engineering đầy đủ: process/Agile, requirements engineering, modeling, architecture, implementation, testing, maintenance/evolution, cùng đề cương được xác minh.

**Extensions:** OOAD, architecture decision records, CI/CD, Docker, security review, observability, collaboration/code review. OOAD chưa được xem là full-course trừ khi có gate riêng.

**Closure gate:** `SUB-SE` full coverage + project evidence có requirements, design rationale, tests, delivery runbook và retrospective. Không đòi khẳng định đã có production commercial traffic.

### MS-07 — Exploration / Specialization (conditional)

**Không mở ngay.** Khi có tín hiệu sở thích/market/academic goals, chọn **một** đề tài sâu và chốt *syllabus equivalent* trước (VD. Applied AI systems, Systems/Go, Data Engineering, nghiên cứu). Kết quả gồm working project/experiments, validation và phản biện. **Không bắt tất cả 4 nhánh cùng lúc.**

## 4. Cross-cutting tracks (không phải milestone độc lập)

- **Java → NestJS → Go:** Java là hướng phát triển mới; NestJS là lợi thế thực chiến đang duy trì; Go sau theo demand/interest. Python khi Applied AI/Data yêu cầu. Thứ tự là ưu tiên tương đối, không cấm học chéo.
- **English:** đọc docs/paper, viết technical notes, thuyết trình project, nghe technical discussions; không ép IELTS test prep nếu không có yêu cầu chương trình.
- **Independent coding & AI:** mỗi unit có phần tự làm trước, AI tham gia sau để review/gợi ý. Production work cho phép AI hỗ trợ nhưng yêu cầu review/test.
- **Career/Job:** khảo sát JD và ứng tuyển thuộc `Self & Life / Career & Opportunities` trong Todoist; học kỹ thuật thuộc `Developer`.
- **Research/Master:** nhánh dài hạn; đọc papers/experiments theo hứng thú và sức lực. Không đặt bài báo/đăng ký Thạc sĩ là prerequisite của backend.

## 5. No fixed timeline & closure rules

- Không có ngày bắt đầu/kết thúc bắt buộc cho milestone. Khi không học, trạng thái có thể là `paused`, không tự tăng backlog debt.
- Trong 1 chu kỳ, **1 primary unit + tối đa 1 supporting unit**, không mở 4 ngôn ngữ song song.
- **Không hoàn tất MS chỉ vì hoàn thành anchor course;** phải đạt cả applied milestone outcome. Ngược lại **không hoàn tất MS khi anchor course chưa đủ full coverage**. Hai điều kiện phải đồng thời đúng.
- Tiêu chuẩn course closure nằm ở `docs/08_DATA_CONTRACT.md` và bảng chủ đề nằm ở `docs/02_COMPETENCY_AND_COURSE_MAP.md`.
- Mỗi closure tạo history event có checklist + artifact refs + quyết định.

## 6. Đổi hướng thế nào

- Review ưu tiên học linh hoạt khi work/energy thay đổi; review skill-market theo quý. Career target chỉ đổi khi có case rõ về fit, cơ hội, bằng chứng xu hướng và trade-off.
- Không lấy lời khuyên từ bản `Core-Plan.md` cũ (6 sprints / 12 weeks, 42h) làm deadline.
- Current candidate đầu tiên: `MS-01`, `SUB-OOP`, **chưa bắt đầu**; câu hỏi tiếp theo không phải “học hết 7 milestone khi nào” mà là “lấy được syllabus & nguồn của SUB-OOP, mở learning unit đầu tiên như thế nào”.

## 7. Nguồn benchmark (để kiểm chứng, không thay thế hồ sơ cá nhân)

- [ACM/IEEE-CS/AAAI CS2023](https://csed.acm.org/knowledge-areas/) — bản đồ knowledge areas.
- [SFIA 9](https://sfia-online.org/en/sfia-9/responsibilities) — responsibility/autonomy/complexity.
- [ITviec AI & IT hiring Vietnam 2026](https://itviec.com/blog/bao-cao-tac-dong-ai-tuyen-dung-it-viet-nam-2026/) — 2026 enterprise survey.
- [GitHub Octoverse 2026](https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/) — hoạt động lập trình/AI adoption, **không đồng nhất với job demand**.
