# COMPETENCY MAP & IU SUBJECT COVERAGE CONTRACT

**Phiên bản:** `1.0.0` · **Status:** `provisional subject inventory`.

> Toàn bộ topic outline bên dưới được khái quát từ `reference/IU_COURSE_INDEX.md`, nguồn chính `BAO_CAO_CHUONG_TRINH_CNTT_DAI_HOC_QUOC_TE.md` trong `Documentations.zip` người dùng cung cấp. Báo cáo này tự nêu rằng đó **không phải syllabus chính thức** và một số tài liệu chưa có văn bản đọc được. Phải đối chiếu với đề cương/slide/lab mà người dùng lựa chọn trước khi xác nhận FULL.

## A. Competency IDs

| ID | Competency | Mức đích tương đối | Milestones sử dụng | Minh chứng |
|---|---|---|---|---|
| `CMP-CODE` | Independent Programming, OOP, Debugging | Core | MS-01/02 | Java project, tests, explanation độc lập |
| `CMP-ALGO` | Data Structures, Algorithmic Thinking | Core | MS-02 | code, complexity, new problem |
| `CMP-DATA` | Relational Models, SQL, Transactions | Core | MS-03 | schema, plans, concurrency lab |
| `CMP-BACKEND` | APIs, Domain Logic, Integrations | Core | MS-03/05/06 | service with automated tests |
| `CMP-RUNTIME` | OS, memory, process, threading | Core | MS-04 | concurrency/scheduling/system lab |
| `CMP-NET` | Networking and Networked Services | Core | MS-05 | packet traces and failure analysis |
| `CMP-RELIABILITY` | Distributed Systems and Observability | Core (longer-term) | MS-05/06 | retries, failure tests, metrics |
| `CMP-QUALITY` | SE, Testing, Security, Maintainability | Core | MS-01/03/06 | test suites/design docs/review |
| `CMP-DELIVERY` | Linux, Containers, CI/CD, Cloud literacy | Working | MS-04/06 | build/deploy/runbook |
| `CMP-ENGLISH` | Technical English | Working→Core | continuous | spoken walkthrough/tech writing |
| `CMP-AI` | Applied AI/AI evaluation | Exploration→Working | MS-07 | measured AI pipeline |
| `CMP-RESEARCH` | Experimental methods/reading papers | Exploration→Working | MS-07 | research note/design/analysis |

## B. Mẫu coverage cho toàn môn

Mỗi môn có một **Full-Coverage Ledger** theo `templates/SUBJECT_COVERAGE_TEMPLATE.md`. Mỗi topic phải có:

- `topic_id`, `mandatory | variant | optional` (chốt scope trước);
- `pass1_status`, `diagnostic_ref`, `pass3_status`, `validation_ref`, `artifact_ref`;
- `status`: `not_started | reviewed | diagnosed | reinforced | validated`;
- `scope_evidence` — syllabus/lecture/lab/source URI và phiên bản.

**Không suy diễn từ curriculum report rằng đã xem hết mọi slide/lab.** Đánh dấu `required_scope_confirmation: true` cho tất cả các subject ban đầu.

## C. Course inventory — anchor môn FULL

### `SUB-OOP` — Object Oriented Programming (IU report: môn 03)

**Anchor milestone:** MS-01 · **Scope status:** `reconstructed / awaiting course-version selection` · **Current:** `not_started`.

| Topic ID | Cấu phần đầy đủ cần audit | Độ bao phủ kỳ vọng |
|---|---|---|
| OOP-01 | Java language/class syntax; classes, objects, constructors, fields/methods, access modifiers | Mandatory baseline |
| OOP-02 | Control flow, overloading, package/encapsulation | Mandatory baseline |
| OOP-03 | Inheritance, polymorphism, overriding, abstract class, interface | Mandatory baseline |
| OOP-04 | Arrays, ArrayList, generic classes, generic collections | Mandatory baseline |
| OOP-05 | Exceptions, error handling | Mandatory baseline |
| OOP-06 | GUI/JFrame/JPanel, event handling where course version includes them | Variant — **must resolve** |
| OOP-07 | SOLID & object-oriented design principles | Variant — **must resolve** |
| OOP-08 | Command/Observer/Decorator and other patterns in chosen lectures | Variant — **must resolve** |
| OOP-09 | JSoup/web scraping or final game project in relevant version | Variant — **must resolve** |
| OOP-10 | Whole-course lab/exam synthesis, independent design | Mandatory validation |

Nếu chọn bản môn có GUI/patterns/final game, không loại bỏ các phần đó rồi tuyên bố full course. Nếu có bằng chứng chúng là nguồn bổ trợ ngoài syllabus đã chọn, ghi lý do và link.

### `SUB-DSA` — Data Structures and Algorithms (môn 04)

**Anchor:** MS-02 · **Current:** `not_started`.

| Topic ID | Topic inventory |
|---|---|
| DSA-01 | Algorithmic complexity, recurrence/Big O, space/time trade-off |
| DSA-02 | Arrays, linked lists, representation & operations |
| DSA-03 | Stacks, queues, implementations & use cases |
| DSA-04 | Recursion/recursive algorithms |
| DSA-05 | Searching, elementary & advanced sorting, complexity |
| DSA-06 | Binary trees, BST and traversals as covered |
| DSA-07 | Hash tables/hash functions/collisions |
| DSA-08 | Graphs, representation/traversal and syllabus-specific algorithms |
| DSA-09 | Remaining mandatory chapters identified after comparing lectures/exams (e.g., heaps, shortest paths if actually taught) |
| DSA-10 | Integrated novel problem + implementation and complexity audit |

### `SUB-DBMS` — Principles of Database Management (môn 20)

**Anchor:** MS-03 · **Current:** `not_started`.

| Topic ID | Topic inventory |
|---|---|
| DB-01 | DBMS architecture; relational model; relational algebra; NULL semantics |
| DB-02 | ER/EER, entity/relationship/constraints, ER→relational mapping |
| DB-03 | SQL DDL/DML, join, nested query, set ops, aggregation, views |
| DB-04 | Advanced SQL: integrity, authorization, dynamic/embedded/procedural features |
| DB-05 | Keys, FDs, closure; lossless decomposition; normalization 1NF→BCNF; multivalued dependencies if required |
| DB-06 | Transactions, serializability, recoverability, isolation, concurrent execution |
| DB-07 | Query processing, costing, optimization, joins & execution plan |
| DB-08 | JDBC/client-server/database application design in chosen course version |
| DB-09 | Recovery/indexing/storage chapters if present in selected syllabus: verify before closure |
| DB-10 | Whole-course schema/query/transaction performance lab |

### `SUB-OS` — Operating Systems (môn 13)

**Anchor:** MS-04 · **Current:** `not_started`.

| Topic ID | Topic inventory |
|---|---|
| OS-01 | Overview, processes, process states and OS management |
| OS-02 | Threads, scheduling models, SMP concepts |
| OS-03 | Synchronization, mutex/semaphore, race, deadlock/starvation |
| OS-04 | CPU scheduling including multi-level feedback/real-time if course version requires |
| OS-05 | Memory management, paging/segmentation, virtual memory |
| OS-06 | I/O, disks, file systems, directories, secondary storage |
| OS-07 | Security/protection and remaining chapters after syllabus review |
| OS-08 | Integrated case/lab and explanation of failure/resource trade-offs |

### `SUB-CN` — Computer Networks (môn 14)

**Anchor:** MS-05 · **Current:** `not_started`.

| Topic ID | Topic inventory |
|---|---|
| CN-01 | Layered architecture, OSI/TCP-IP, encapsulation |
| CN-02 | Application-layer protocols, HTTP/DNS as taught |
| CN-03 | Transport: TCP/UDP, reliability, congestion/flow control as taught |
| CN-04 | Network layer: IPv4/IPv6 (if syllabus), subnetting, VLSM, routing |
| CN-05 | Data-link layer: Ethernet, switching, shared-media access |
| CN-06 | Wireless/physical and network/security topics only if included in selected core course |
| CN-07 | Packet analysis, addressing/routing labs and total coverage audit |

### `SUB-SE` — Software Engineering (môn 22)

**Anchor:** MS-06 · **Current:** `not_started`.

| Topic ID | Topic inventory |
|---|---|
| SE-01 | Lifecycle and software process models, Agile/Scrum |
| SE-02 | Requirements engineering, elicitation, specification and change management |
| SE-03 | Modeling: use cases, class/sequence/behavior diagrams where covered |
| SE-04 | Software architecture/system design and design decisions |
| SE-05 | Implementation practices, version control, collaboration |
| SE-06 | Software testing and quality, reliability |
| SE-07 | Maintenance/evolution and release/change management |
| SE-08 | Project artifacts: proposal, plan, requirement spec, testing plan, user guide |
| SE-09 | Whole-course case project and integrated evidence review |

## D. Non-anchor knowledge (học chọn lọc; KHÔNG tự coi là completed subject)

- `SUB-OOAD`: use cases, UML, class/activity/sequence diagrams, design patterns (IU môn 21) — hỗ trợ MS-01/06. Nếu muốn khẳng định hoàn tất OOAD, mở riêng **full-course gate** tương tự.
- `SUB-WEB`: HTML/CSS/JS, Servlet/JSP, cookies/sessions, JDBC, JavaBeans, MVC, XML, AJAX và lab (IU môn 19). React practical ≠ completion của syllabus Web cũ.
- `SUB-SNA`: Linux/UNIX, shell, permissions, boot/services, monitoring, TCP/IP/DNS, virtualization/containers (IU môn 28) — hỗ trợ MS-04/06.
- `SUB-SDC`: theo IU báo cáo môn 17, chủ yếu cloud/Hadoop/MapReduce/Spark/PySpark; nguồn trích xuất **chỉ 5/23 files**. Không gọi đó là full coverage modern distributed systems. Nên học nguyên lý concurrency/consistency/failure riêng nếu mục tiêu Backend, và audit syllabus nếu muốn hoàn tất môn IU.
- `SUB-FCDS`: hashing, symmetric/asymmetric cryptography, RSA/DH, relevant security labs — hỗ trợ security. Không tự triển khai crypto thật trong app.
- `SUB-AI`, `SUB-DM`, Probability/Statistics, Discrete Math, Programming Languages — ưu tiên khi chọn AI/Data/Research hoặc khi thiếu nền tảng học thuật.

## E. Cách lập Full Coverage Ledger thực tế

1. Chọn **một** học phần chuẩn và phiên bản tài liệu (mã/môn/năm/giảng viên nếu có); nếu không xác minh được, chọn phạm vi *reconstructed* và ghi rõ.
2. Đối chiếu toàn bộ chương slide/lecture, labs, assignments, exam topics; thêm topic còn thiếu vào bảng, không chỉ dựa vào danh sách tóm tắt này.
3. Với mỗi topic học lần lượt self-review → nhẹ diagnostic → reinforcement → validate. Có thể làm diagnostic nhiều lần, nhưng các lần đều ghi history.
4. Ghi evidence trong từng topic row; **không dùng `covered` thay cho `validated`**.
5. Tổng kiểm tra tích hợp cả môn + đối chiếu exclusions/variants; nếu thiếu source, `blocked/unknown` thay vì đánh dấu complete.
6. Chỉ khi đủ full-course closure và applied milestone outcome mới đưa milestone sang completed.

> **Important:** Bảng này là **khung sơ bộ có thể triển khai và mở rộng**, không có tuyên bố đã xác nhận đầy đủ đề cương giảng dạy IU. Những danh sách trên phải được cập nhật qua một migration khi một phiên bản syllabus thực tế được chọn.
