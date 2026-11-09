---
name: market-signal-reviewer
description: Research current Vietnam/HCMC software engineering job-market signals and future technology trends, compare with roadmap baseline, and propose evidence-backed changes without rewriting the user's career plan prematurely.
metadata:
  version: "1.0.0"
---

# Market Signal Reviewer

## Purpose

Give the roadmap an evidence-based adaptation loop. Never turn a single job board snapshot or AI hype into a career reset.

## Research procedure

1. Read `docs/06_MARKET_BASELINE.md`, `docs/01_ROADMAP_MAIN.md`, recent `history/04_REVIEWS.md` and `history/01_CHANGELOG.md`.
2. If current information is required and web tools are available, browse official industry reports, dated primary sources, and current job posts. If unavailable, say analysis is based on baseline only; do not pretend to verify today's openings.
3. Prefer HCM/Vietnam **Junior/early-mid** role samples; use 15–25 concrete JDs where feasible, with links/date/seniority. Separate required vs preferred skills, job title vs text, industry, work experience and English requirement.
4. Compare Backend Java/Node/Go, Full-stack, Platform/Cloud, Applied AI, Data roles. Note sampling bias, multi-stack positions, duplicates, layoffs/market changes and publication dates.
5. Distinguish `OBSERVATION`, `INTERPRETATION`, `SCENARIO FORECAST` and `RECOMMENDATION`.
6. Recommend `maintain` or `CR-...` with explicit impact on course modules and trade-offs; user decides.
7. Append `RV` market review only when user requests saving; update baseline/main only after change approved.

## Output contract

- `As-of date; geography; sample/method`.
- `Observed demand`: source-linked, comparable metrics; don't compare different denominators directly.
- `Role skill signals`: concrete hard requirements and trend.
- `Future scenarios`: 2–3 uncertainty scenarios, not unsupported precise 2031 predictions.
- `Fit against current skills`: preserve NestJS/RDBMS leverage and energy constraints.
- `Recommendation`: keep/adjust direction + confidence + whether CR is proposed.

## Guardrails

- GitHub contributor share ≠ hiring market share.
- Aggregate Java title count ≠ all Java job demand.
- Global WEF/BLS forecasts ≠ Vietnam hiring fact.
- Do not promise ads-free career, guaranteed salary, immunity from AI automation or automatic task edits.
