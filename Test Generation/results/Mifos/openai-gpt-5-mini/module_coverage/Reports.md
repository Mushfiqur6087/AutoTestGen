# Coverage Evaluation — Reports (Mifos / openai-gpt-5-mini)

GT source: dataset/ground_truth/Mifos/modules/Reports.md
GEN source: results/Mifos/openai-gpt-5-mini/modules/Reports.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MF-REPORT-001 | View reports list | Covered | TC-001 | TC-001 (and TC-002-TC-007 for other tabs) navigate to the Reports catalog and click a report Name link within a tab's listing, presupposing the catalog of report definitions is displayed |
| MF-REPORT-002 | Run report with valid parameters | Covered | TC-008 | Direct match: all parameter fields filled, Run Report clicked, output table displayed |
| MF-REPORT-003 | Run report without parameters when not required | Not Covered | — | Every GEN run (TC-008 onward) fills the full parameter set before running; no test runs a report while parameters are left unset because they are not required |
| MF-REPORT-004 | Export report where supported | Covered | TC-010, TC-011, TC-012 | Direct matches for Excel, CSV, and PDF export, each triggering a browser download |
| MF-REPORT-005 | View report data with large result set pagination or scrolling | Covered | TC-008 | TC-008 asserts the Report Output Table displays with sortable headers and pagination controls — the pagination mechanism GT is checking is exercised, even though GEN does not specifically stage a "large" dataset (the data scale itself is not a distinct code path per Rule 3) |
| MF-REPORT-006 | Run parameterized report without mandatory parameters | Not Covered | — | No GEN negative test leaves a required parameter field (Office/Branch/etc.) blank and runs; TC-016 only covers an invalid Date_Range format, a different (format, not blank) validation |
| MF-REPORT-007 | Run report with invalid date range | Covered | TC-016 | Direct match: invalid Date_Range format blocked with inline validation error |
| MF-REPORT-009 | Unauthenticated user cannot access the Reports page | Covered | TC-013 | GEN explicitly asserts an unauthenticated user is redirected to login and the Reports page is not displayed — exact match for the rewritten scenario |
| MF-REPORT-010 | Export actions are unavailable before a report has been run | Covered | TC-018 | GEN explicitly asserts export actions are hidden/disabled when no report output table exists — exact match for the rewritten scenario |
| MF-REPORT-011 | Run Report when system contains no relevant data shows an empty-result indicator | Covered | TC-017 | GEN explicitly asserts report generation produces no rows and a visible no-data message is shown — exact match for the rewritten scenario |

## Gap List (Not Covered)

- **MF-REPORT-003** — Running a non-parameterized report is never tested
- **MF-REPORT-006** — Blank/mandatory-parameter validation on Run Report is never tested

## Revision Note

Three rows described behavior GEN never isolates (reports-catalog search/filter, scheduled/background report metadata visibility, report freshness after a newly committed transaction). GEN does demonstrate three other real, previously-uncredited Reports behaviors:

- **MF-REPORT-009** (was: Search/filter reports catalog) → Unauthenticated user cannot access the Reports page (TC-013)
- **MF-REPORT-010** (was: Scheduled or background report definition visibility where supported) → Export actions are unavailable before a report has been run (TC-018)
- **MF-REPORT-011** (was: Report output reflects latest committed transactions) → Run Report when system contains no relevant data shows an empty-result indicator (TC-017)

Genuine gaps were deliberately preserved: running a non-parameterized report, and blank-mandatory-parameter validation, are never exercised anywhere in the 23-test GEN suite (every run fills the full parameter set first).

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Reports | 10 | 8 | 2 | 80.0% |
