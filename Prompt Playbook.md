# ADAPTIVE SE ROADMAP — PROMPT PLAYBOOK (GIT EDITION)

**Phiên bản chuyển đổi:** 2026-11-09 · **Nguồn:** `https://github.com/lhduc141/adaptive-roadmap` · **Clone URL:** `https://github.com/lhduc141/adaptive-roadmap.git` · **Branch mặc định:** `main`

Tài liệu này chuyển cơ chế **gửi full ZIP/files** sang **đọc từ repository GitHub**. Giữ tinh thần của `Prompt Playbook.md` gốc (Roadmap v1.0.0). Đây chỉ là hướng dẫn prompt; **không thay thế** các quy tắc trong `AGENT_ENTRY.md`, `docs/08_DATA_CONTRACT.md`, `docs/03_CURRENT_STATE.md`.

> **Quan trọng:** URL GitHub không tự cấp quyền đọc mọi file, không tạo đồng bộ liên tục và không cấp quyền ghi. AI chỉ được nói đã đọc/ghi những gì công cụ thực sự truy cập hoặc thực thi được. Nếu không truy cập được repo hoặc file bắt buộc, báo rõ và yêu cầu cách cấp dữ liệu thay thế; **không tự suy đoán state**.

## 0. Quy ước chung: lấy dữ liệu từ Git

**Repository duy nhất để tra cứu:** `https://github.com/lhduc141/adaptive-roadmap` (đọc bản mới nhất của `main`, trừ khi tôi chỉ định commit/tag/branch khác).

**Khi bắt đầu chat mới hoặc khi cần đồng bộ:**

1. Xác nhận repo tồn tại, quyền truy cập, branch và **commit SHA** đang đọc. Ưu tiên kết nối GitHub có quyền đọc; nếu có Git CLI được phép dùng, có thể `git clone`/`git fetch`; nếu chỉ có web thì mở các file thực sự đọc được. Không tự nhận đã clone chỉ vì mở trang GitHub.
2. Liệt kê cấu trúc repository. **Tìm `AGENT_ENTRY.md` thực tế** để xác định `ROADMAP_ROOT` (thư mục cha của file); không mặc định nó nằm ở repo root. Repository hiện có thư mục cấp gốc `Adaptive_SE_Roadmap/`, nhưng vị trí cụ thể các file bên trong cần được kiểm chứng ở mỗi môi trường.
3. Đọc trước: `<ROADMAP_ROOT>/AGENT_ENTRY.md`, `docs/08_DATA_CONTRACT.md`, `docs/03_CURRENT_STATE.md`, `docs/01_ROADMAP_MAIN.md`, `history/00_EVENT_INDEX.md` (các đường dẫn sau tính tương đối từ `ROADMAP_ROOT`). Tiếp đó chỉ đọc file `subjects/`, `templates/`, `history/`, docs, log hoặc skill liên quan đến yêu cầu hiện tại.
4. Kiểm tra roadmap version, `last_applied_event_id`, latest **accepted event** và trạng thái có bằng chứng; đối chiếu event index với current state. **Commit mới nhất ≠ event học tập đã chấp thuận mới nhất.** Nếu có mâu thuẫn, báo rõ nguồn và không tự sửa.
5. Nêu nguồn đã đọc bằng đường dẫn file + branch/SHA; tách **verified state**, **user-reported**, **proposal**, **uncertain/blocked**. Không coi task gợi ý là task Ready, không coi học qua là mastery, không coi file truy cập thất bại là file không tồn tại.
6. **Mặc định READ-ONLY.** Khi cần cập nhật, xuất đề xuất chỉnh sửa/diff để tôi duyệt. Chỉ sửa file khi tôi có yêu cầu rõ ràng và bạn có công cụ ghi thực tế; không tự commit, push, merge, thay đổi milestone hoặc cập nhật Todoist. Khi không thể ghi, cung cấp patch Markdown có thể áp dụng thủ công.

**Nếu có terminal và quyền mạng:**

```bash
git clone --depth 1 --branch main https://github.com/lhduc141/adaptive-roadmap.git
cd adaptive-roadmap
git rev-parse HEAD
find . -type f -name 'AGENT_ENTRY.md'
```

Đây là **ví dụ thao tác**, không phải bằng chứng rằng công cụ AI đã clone thành công. Với repo đã clone, `git fetch origin main` và kiểm tra trạng thái local trước khi đồng bộ; không reset hoặc ghi đè các thay đổi chưa commit.

**Nếu chỉ có link và trình duyệt:** đọc từng file từ giao diện hoặc URL raw mà công cụ thực sự hỗ trợ; khi bị giới hạn, báo danh sách file chưa đọc. Nếu repo private hoặc tool không hỗ trợ truy cập, kết nối GitHub (nếu có) hoặc gửi đúng các file thiếu, không mặc định phải upload toàn bộ ZIP.

---

## 1. Initialize / resume — khởi tạo hoặc tiếp tục một cuộc trò chuyện mới

> **Repo:** `https://github.com/lhduc141/adaptive-roadmap` (`main`). Hãy truy cập repository bằng công cụ có sẵn và thực hiện quy trình tại mục 0. Tìm `ROADMAP_ROOT` từ `AGENT_ENTRY.md`, đọc các tài liệu authority (`AGENT_ENTRY.md`, `docs/08_DATA_CONTRACT.md`, `docs/03_CURRENT_STATE.md`, `docs/01_ROADMAP_MAIN.md`, `history/00_EVENT_INDEX.md`) và history/subject liên quan; áp dụng skill phù hợp nếu thực sự truy cập được. Trả về: branch + commit SHA đã xác minh, roadmap version, latest accepted event, `last_applied_event_id`, verified state, đề xuất chưa duyệt, blocker, next action, file thiếu/xung đột. Phân biệt cái đã đọc và chưa đọc; không tự tạo tiến độ, sửa milestone hoặc Todoist. Chọn **một hành động tiếp theo** phù hợp. Nếu không truy cập đủ file, dừng việc kết luận state và chỉ ra chính xác phần cần bổ sung.

## 2. Today — một hành động cụ thể

> Dựa trên **bản mới nhất đọc được từ GitHub repo** `https://github.com/lhduc141/adaptive-roadmap` (`main`), đồng bộ `docs/03_CURRENT_STATE.md`, `history/00_EVENT_INDEX.md`, history gần nhất, `docs/04_EXECUTION_PROTOCOL.md`, và `docs/07_TODOIST_BRIDGE.md` nếu có. Áp dụng `adaptive-study-planner` nếu có thể truy cập. Hôm nay tôi có khoảng **[... phút / không chắc]**, năng lượng **[thấp/vừa/cao]**, việc bắt buộc **[...]**, điều vướng **[...]**. Chọn **một việc quan trọng nhất** và một phương án nhẹ (hoặc nghỉ); ghi Objective, Definition of Done (DoD), nguồn học, bằng chứng cần gửi, checkpoint. Không đặt deadline giả định, không tự tạo task hoặc đổi state chỉ vì đã đề xuất. Nếu chưa đọc được state, báo rõ trước khi cá nhân hóa.

## 3. This week — mục tiêu linh hoạt

> Từ GitHub repo `https://github.com/lhduc141/adaptive-roadmap` (`main`), đọc current state, accepted events và các việc còn dở theo `ROADMAP_ROOT` đã kiểm chứng. Tuần này tôi dự kiến **[ít/vừa/nhiều thời gian/chưa biết]**, có cam kết **[...]**. Đề xuất tối đa **hai learning outcomes**, không bắt buộc gắn ngày. Với mỗi outcome: next actions nhỏ, DoD, low-energy alternative, điều kiện dừng, cách ưu tiên nếu bị gián đoạn. Phân biệt **proposal** và **Ready task**; không tự cập nhật Git hoặc Todoist.

## 4. Start / continue a subject — học môn hoặc topic

> Dùng GitHub repo `https://github.com/lhduc141/adaptive-roadmap` (`main`) làm nguồn; tìm và đọc `subjects/SUB-..._COVERAGE.md` tương ứng trong `ROADMAP_ROOT`, syllabus/source thực sự có sẵn, diagnostic/session logs mới nhất. Dùng `subject-mastery-coach` nếu truy cập được. Môn **[SUB-OOP / SUB-DBMS / ...]**, topic **[...]**, learning pass **[Pass1/Pass2/Pass3/chưa rõ]**. Xác định prerequisite và mandatory coverage còn thiếu. Pass1: để tôi tự ôn và làm ví dụ. Pass2: **mỗi lượt chỉ một câu/bài**, chờ trả lời, không đưa đáp án trước. Pass3: đào sâu misconceptions, đưa bài kiểm chứng mới. Không tự đánh dấu subject complete; dẫn file/commit làm cơ sở.

## 5. Diagnostic — ghi nguyên văn câu trả lời

> Từ repo `https://github.com/lhduc141/adaptive-roadmap` (`main`), đọc source/subject coverage, các diagnostic liên quan và `templates/DIAGNOSTIC_RECORD.md` thực sự có trong `ROADMAP_ROOT`. Diagnostic cho **[subject/topic]**: hỏi từng câu và chờ trả lời; lưu **nguyên văn** câu trả lời của tôi trong bản nháp. Phân loại correct/partial/incorrect/uncertain và lý do; rubric 0–4 chỉ khi đủ evidence; ghi rõ AI đã hỗ trợ ở mức nào. Cuối phiên, soạn bản ghi đúng template, đề xuất ôn Pass3; **không sửa history hoặc CURRENT_STATE** khi chưa có yêu cầu và quyền ghi rõ ràng. Nếu không truy cập template, báo và dùng draft có nhãn chưa đối chiếu.

## 6. Finish a session — ghi log và chuẩn bị thay đổi

> Dựa vào repo `https://github.com/lhduc141/adaptive-roadmap` (`main`) tại commit đã xác minh, đọc current state, event index, history liên quan và `templates/LEARNING_SESSION_RECORD.md` nếu có. Tôi đã học **[subject/topic/pass]**; làm **[...]**; evidence/code/test **[...]**; khó khăn **[...]**; AI hỗ trợ **[...]**; năng lượng **[...]**; thời gian thực tế **[.../không rõ]**. Đối chiếu DoD, phân biệt completed/partial/unverified. Soạn `LEARNING_SESSION_RECORD` và event ID `LS-YYYYMMDD-NNN` chưa trùng (kiểm tra index trước). Cho tôi **diff đề xuất** cho event mới, `history/00_EVENT_INDEX.md`, `docs/03_CURRENT_STATE.md`; đánh dấu **chưa áp dụng** trước khi được duyệt. Sau khi tôi xác nhận và công cụ có quyền ghi: áp dụng event → cập nhật index → đồng bộ current state → validate. Không tuyên bố đã lưu, commit hay push nếu chưa thực hiện và kiểm tra được.

## 7. Course / milestone audit — kiểm toán chứng cứ

> Đọc contract, `subjects/`, syllabus/source, diagnostic/session records và milestone liên quan từ GitHub repo `https://github.com/lhduc141/adaptive-roadmap` (`main`) sau khi xác định `ROADMAP_ROOT`. Audit **[subject/milestone]**: lập coverage matrix từng mandatory topic, Pass1/2/3 evidence, bài tổng hợp, applied milestone outcome; chỉ rõ mục thiếu hoặc chưa verified. Chỉ **đề xuất** `verified_complete` khi đạt gate và có xác nhận người học. Không suy luận mastery từ việc từng học IU, xem slide hoặc đã có project. Nêu file/commit được kiểm tra và những file chưa truy cập được.

## 8. Market review / change request — khảo sát thị trường

> Lấy baseline, roadmap, history và mục tiêu nghề nghiệp từ GitHub repo `https://github.com/lhduc141/adaptive-roadmap` (`main`) trước khi nghiên cứu web. Dùng `market-signal-reviewer` nếu có; ưu tiên thị trường Việt Nam/TP.HCM, đúng cấp bậc early-career, phân biệt job ads/employer surveys/forecasts và ngày nguồn. So sánh với baseline **[ngày]** trong repo; đánh giá Backend, Java/NestJS/Go, Systems/Cloud, AI và mức độ chắc chắn. Nếu cần thay đổi, xuất `CHANGE_REQUEST` gồm before/after/reason/evidence/impact để duyệt; **không tự sửa roadmap/history hoặc push Git**. Đừng coi nhận định thị trường là trạng thái học tập đã verified.

## 9. Update personal context — cập nhật bối cảnh

> Đọc `docs/05_CONTEXT_PROFILE.md`, hồ sơ gốc và history liên quan từ GitHub repo `https://github.com/lhduc141/adaptive-roadmap` (`main`), sau khi xác định `ROADMAP_ROOT`. Thông tin mới: **[...]**. So sánh với dữ liệu trong repo, phân loại **verified / self-reported / uncertain**, chỉ ra đường dẫn và nội dung cần chỉnh; chuẩn bị diff. Chỉ cập nhật khi tôi yêu cầu và công cụ có quyền ghi; ghi event khi thay đổi kế hoạch/ưu tiên theo contract. Không tự xem kinh nghiệm tôi kể là mastery đã đánh giá. Không đưa dữ liệu riêng tư/nhạy cảm lên repo public mà chưa kiểm tra.

## 10. Restart after interruption — tái khởi động nhẹ

> Truy cập GitHub repo `https://github.com/lhduc141/adaptive-roadmap` (`main`), đọc latest verified state và latest **accepted event**, tìm checkpoint còn giá trị, blockers và next action nhỏ nhất. Tôi đã gián đoạn **[...]**. Không cộng dồn quá hạn hay ép học bù. Nếu state cũ/xung đột, nêu rõ; đề xuất một bước nhẹ, chỉ tăng scope khi tôi xác nhận thời gian/năng lượng. Không thay đổi file chỉ vì đang tái khởi động.

## 11. Safe handoff / Git maintenance — quy tắc không được bỏ qua

- **Nguồn thật:** kiểm tra URL, branch, commit SHA, `ROADMAP_ROOT`, roadmap version và `last_applied_event_id` mỗi lần reload; **không lấy thời gian sửa ZIP hoặc chỉ commit mới nhất để suy luận tiến độ**.
- **History append-only:** không sửa/xóa event cũ. Với event đã được chấp thuận: append history → cập nhật `history/00_EVENT_INDEX.md` → đồng bộ `docs/03_CURRENT_STATE.md` → validate.
- **ID ổn định:** milestone `MS-..`, subject `SUB-..`, diagnostic `DG-YYYYMMDD-NNN`, learning session `LS-YYYYMMDD-NNN`; kiểm tra trùng trước khi đề xuất ID.
- **Không ghi tự động:** read-only trừ khi có phê duyệt và write capability; xuất patch/diff nếu thiếu quyền. Đối với Git, commit/push là hai hành động riêng, chỉ làm khi được yêu cầu rõ; không tạo PR/merge ngoài yêu cầu.
- **Chống ghi đè:** trước khi áp dụng patch, kiểm tra branch/SHA và file hiện tại còn khớp baseline. Nếu branch đã thay đổi, diff lại và yêu cầu xác nhận thay vì overwrite.
- **Không dữ liệu mật:** không đưa lên repo public mã nguồn công ty, dữ liệu khách hàng, token, mật khẩu, thông tin tài khoản hoặc file không có quyền chia sẻ. Rà soát `Chat Record/` và `Files/` trước khi chia sẻ công khai.
- **Learning scope:** mỗi ngày một primary action; tối đa hai weekly outcomes; không tự đặt deadline giả.
- **Chỉ báo cáo điều đã làm:** phân biệt `read successfully`, `not accessible`, `proposed`, `applied locally`, `committed`, `pushed`; không mô tả chúng như một trạng thái duy nhất.

## 12. Prompt kiểm tra truy cập GitHub (dùng khi mở chat mới)

> Kiểm tra quyền truy cập của bạn vào `https://github.com/lhduc141/adaptive-roadmap` trên branch `main`. Hãy báo: (1) bạn thực sự có thể đọc được bao nhiêu cấp thư mục và file nào; (2) `ROADMAP_ROOT` tìm được ở đâu; (3) branch và commit SHA nếu xác minh được; (4) bạn có **read-only, write, hay không có Git integration**; (5) bạn có thể tạo patch, commit hoặc push không; (6) những file bắt buộc chưa đọc được. **Chưa phân tích trạng thái học tập và tuyệt đối không chỉnh sửa repository ở bước này.**

## 13. Cách sử dụng nhanh

1. **Chat mới:** gửi prompt ở **mục 1** (hoặc mục 12 nếu muốn test access trước). Không cần gửi ZIP khi AI có thể đọc trực tiếp đủ nguồn từ Git.
2. **Hằng ngày/tuần:** dùng prompt ở **mục 2/3** và điền availability/energy/constraints.
3. **Học và assessment:** dùng mục **4/5/7**; chỉ tải syllabus hoặc evidence ngoài repo nếu Git chưa chứa chúng.
4. **Kết thúc buổi học:** dùng mục **6**; rà soát diff, xác nhận trước khi ghi. Với giao diện read-only, tự áp dụng patch vào repo theo workflow Git của bạn.
5. **Lần sau:** AI đọc lại commit/state mới nhất từ Git. **Không có cơ chế cập nhật tự động chỉ nhờ một URL trong prompt**.
