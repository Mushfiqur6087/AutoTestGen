# Coverage Evaluation — Support Center (Parabank / openai-gpt-5-mini)

GT source: dataset/ground_truth/Parabank/modules/Support_Center.md
GEN source: results/Parabank/openai-gpt-5-mini/modules/Support_Center.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MW-SC-001 | Send message successfully | Covered | TC-001 | Exact match |
| MW-SC-002 | Send with attachment | Covered | TC-002, TC-015 | Direct match, reinforced by the uppercase-extension boundary |
| MW-SC-003 | Empty subject | Covered | TC-012 | Exact boundary match |
| MW-SC-004 | Empty message body | Covered | TC-006, TC-017 | Direct match, reinforced by the whitespace-only boundary |
| MW-SC-005 | Invalid attachment type | Covered | TC-008, TC-016 | Direct match, reinforced by the no-extension boundary |
| MW-SC-006 | Category dropdown shows all options | Not Covered | — | No GEN test asserts the dropdown's full option list (Account/Technical/Security/Other) — tests only select *a* category, never verify all are present |
| MW-SC-007 | Schedule callback | Covered | TC-003, TC-004 | Exact match |
| MW-SC-008 | Phone pre-filled | Covered | TC-003 | TC-003 explicitly confirms the Phone Number field shows the prefilled number |
| MW-SC-009 | Date too soon | Covered | TC-009, TC-019 | Direct match, reinforced by the one-day-early boundary |
| MW-SC-010 | Invalid phone format | Covered | TC-010 | Exact match |
| MW-SC-011 | Email confirmation received | Not Covered | — | TC-018 only parenthetically notes "(email confirmation will be sent)" as an unverified side comment — no GEN test actually checks an inbox or asserts receipt |
| MW-SC-012 | Callback time overlapping EOD cutoff | Not Covered | — | No GEN test selects a time window at the end-of-day boundary; existing boundary tests target the date cutoff, not the time-window cutoff |
| MW-SC-013 | Concurrent message submissions (2 tabs) | Covered | TC-020 | TC-020 tests the same underlying concern — near-simultaneous duplicate submission attempts are prevented from creating duplicate tickets — via rapid double-click rather than two tabs (Rule 3: same logical path, different trigger mechanism) |
| MW-SC-014 | Extremely large attachment (>50MB) | Not Covered | — | No GEN test uploads an oversized file; existing attachment tests cover type/extension, not size |

## Gap List (Not Covered)

- **MW-SC-006** — Category dropdown's full option list never verified
- **MW-SC-011** — Email confirmation receipt never actually asserted
- **MW-SC-012** — Callback time-window end-of-day cutoff boundary
- **MW-SC-014** — Oversized attachment (>50MB) validation

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Support Center | 14 | 10 | 4 | 71.4% |
