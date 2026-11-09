# TODOIST BRIDGE — HOW TO TURN ROADMAP INTO ACTIONS

**Source of truth for Todoist organization:** `reference/Todoist_document.md` v1.3.0 (09/11/2026). **Không chỉnh cấu trúc Todoist trong tài liệu này khi chưa được người dùng duyệt.**

## 1. Project mapping

| Loại việc | Todoist Project | Rule |
|---|---|---|
| Học OOP/DSA/Java/NestJS, diagnostic, bài lab | `Developer` | Board status: Backlog, Ready, In Progress, Validation, On Hold |
| Học tiếng Anh là đầu ra chính | `English` | List theo Listening/Speaking/Reading/Writing/Vocabulary |
| Task SQL/SP đã nhận tại ParadiseHR | `Work` | gắn `paradise` nếu đúng nguồn; không chuyển thành Developer |
| GLV | `GLV` | các section trách nhiệm đã có |
| Ứng tuyển, CV, quản lý job opportunity | `Self & Life` | Career & Opportunities |

**Không tạo project thứ 6** cho roadmap khi sử dụng Todoist Beginner. Theo baseline: 5 project cá nhân và 3 filters; giữ 3 filters đã chốt. Người dùng có 18 labels theo ảnh; **không thêm label mới** nếu không có nhu cầu cụ thể.

## 2. Roadmap task shape

- `title`: động từ + output cụ thể (vd. `Lập danh mục chương/lab OOP IU để chốt phạm vi SUB-OOP`).
- `description`: `Roadmap ID`, Objective, Scope, DoD, Source, Evidence, Checkpoint, Next Action.
- `labels`: dùng label đã có như `java`, `backend`, `database`, `no_ai`, `dsa`, `engineering`, `testing`; chỉ gắn cần thiết, không tagging mọi thứ.
- `priority`: theo mức ưu tiên tại thời điểm, không dùng làm chỉ số độ khó/năng lực.
- `due date`: để trống nếu không có cam kết ngày; planning suggestion không phải deadline.
- `task id`: nếu không lấy được từ Todoist thật thì `null`; không bịa URL/link ID.

## 3. Lifecycle

`proposed` (ở tài liệu) → `ready` (khi user chấp thuận tạo) → `in_progress` (khi thực sự bắt đầu) → `validation` (khi cần kiểm chứng) → `completed` (sau evidence).

Todoist task completion **không tự đánh dấu subject full** hay milestone completed. Kết quả học quay về `history` và `CURRENT_STATE`.

## 4. Sync policy

- Đây chỉ là **mapping offline**, không phải kết nối trực tiếp Todoist.
- Nếu có app connector với quyền thực thi, dùng đúng connector đã được cài và hành động được người dùng cho phép; nếu không, chỉ xuất task proposal rõ ràng để người dùng copy.
- Tránh trùng task: kiểm tra task cùng `Roadmap ID`, subject, DoD, section trước khi tạo mới.
- Không tự đổi tên/section/filter hiện có. Điểm chưa xác minh trong baseline vẫn là `unknown`.
