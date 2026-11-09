# TEMPLATE — DIAGNOSTIC RECORD (DO NOT TREAT AS ACTUAL ANSWER)

```yaml
diagnostic_id: DG-YYYYMMDD-NNN
event_id: EV-YYYYMMDD-NNN
date: YYYY-MM-DD
time_precision: day | minute
subject_id: SUB-XXX
milestone_id: MS-XX
topic_id: XXX-01
pass: 2
question_type: concept | application | debugging | tradeoff | integration
assistance: none | hinted | assisted
response_status: answered | skipped | not_asked
score: null # only integer 0..4 after actual answer
confidence: unverified
```

**Câu hỏi nguyên văn:** (do AI đưa ra trước khi lộ đáp án)

> [insert exact question]

**Câu trả lời người dùng NGUYÊN VĂN:**

> [insert exact response; or `not_answered`]

**Rubric / expected elements:** ...

**Đánh giá dựa trên bằng chứng:**

- Correct components: ...
- Missing/inaccurate components: ...
- Misconceptions and why: ...
- Feedback category: `correct | partial | incorrect | uncertain`
- Score and evidence: `0..4 | null`, lý do cụ thể.
- Suggested reinforcement: ...
- Follow-up question/practice: ...
- Do NOT upgrade to course completed on one answer.
