# TEMPLATE — SUBJECT FULL COVERAGE LEDGER (COPY WHEN OPENING A SUBJECT)

> Template only. Do not use `[x]` until actual evidence exists.

```yaml
subject_id: SUB-XXX
linked_milestone_id: MS-XX
subject_title: "..."
source_of_syllabus: "..."
scope_type: official_course_syllabus | agreed_reconstructed_scope
scope_version: "..."
source_verification_status: not_verified
course_status: not_started
pass: null
completed_topics: []
completion_claim: none
```

| Topic ID | Mandatory/Variant/Optional | Source chapter/lab | Pass1 self review | DG refs & findings | Pass3 reinforcement | Validation refs | Topic status |
|---|---|---|---|---|---|---|---|
| XXX-01 | to_confirm | not_checked | not_started | none | not_started | none | not_started |

## Full-Course Closure Audit

- [ ] Chốt version syllabus/giảng viên/bộ tài liệu; đánh dấu official vs reconstructed.
- [ ] Liệt kê đầy đủ chapter/lecture/lab/exam và unresolved variants.
- [ ] 100% topics mandatory có evidence Pass1/Pass2/Pass3 + validation, hoặc lý do exception đã duyệt và hiệu chỉnh scope.
- [ ] Có một bài tổng hợp ứng dụng/giải thích/bài mới không có AI implementation trước.
- [ ] Diagnostic log có Q/A nguyên văn và đánh giá.
- [ ] Evidence files/links tồn tại; người dùng xác nhận completion.
- [ ] Tạo event `COURSE_VERIFIED`; snapshot update đúng ID/version.
- [ ] Nếu chỉ là reconstructed scope: ghi rõ `(agreed reconstructed scope)` trong conclusion.

## Next resume checkpoint

- `last_topic`: ...
- `last_action`: ...
- `next_smallest_action`: ...
- `blockers`: ...
