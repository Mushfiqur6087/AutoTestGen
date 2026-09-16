# Coverage Evaluation — Dashboard (Mifos / openai-gpt-5-mini)

GT source: dataset/ground_truth/Mifos/modules/Dashboard.md
GEN source: results/Mifos/openai-gpt-5-mini/modules/Dashboard.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MF-DASH-001 | Dashboard loads from Home page | Covered | TC-001 | Clicking Dashboard from the Home page opens the Dashboard with the Client Trends chart and summary cards visible — same navigate-and-load behavior; GEN's specific card labels (Amount Pending/Disbursed, Amount Collected) differ from GT's illustrative card names but the underlying "Dashboard displays summary cards after navigating from Home" behavior matches (Rule 3) |
| MF-DASH-002 | Summary cards display metrics | Not Covered | — | GEN only asserts the cards are visible (TC-001) or show a 'No Data' placeholder (TC-003, TC-009); no test verifies displayed values match known/expected data — data-accuracy of the counts is never isolated |
| MF-DASH-005 | Dashboard with no data | Covered | TC-003, TC-009 | Both explicitly assert summary cards (and the Client Trends chart) show 'No Data' when the selected office has no financial/growth records — exact match |
| MF-DASH-006 | Dashboard refresh after transaction | Not Covered | — | No GEN test performs a transaction (e.g., create client, post repayment) and refreshes the Dashboard to confirm metrics reflect the latest committed data |
| MF-DASH-007 | Search Activity on the Dashboard filters displayed activities | Covered | TC-002 | GEN explicitly asserts the Dashboard activity view is filtered to entries matching the search term — exact match for the rewritten scenario |

## Gap List (Not Covered)

- **MF-DASH-002** — Data accuracy of summary-card counts untested (only visibility and empty-state are tested)
- **MF-DASH-006** — Dashboard metrics refreshing to reflect a newly committed transaction untested

## Revision Note

One row described behavior GEN never isolates (quick-action links navigating to create/transaction pages — no such links exist anywhere in the GEN suite). GEN does demonstrate one other real, previously-uncredited Dashboard behavior:

- **MF-DASH-007** (was: Navigate from dashboard quick links) → Search Activity on the Dashboard filters displayed activities (TC-002)

Genuine gaps were deliberately preserved: summary-card data accuracy and post-transaction metric refresh are never exercised anywhere in the 9-test GEN suite.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Dashboard | 5 | 3 | 2 | 60.0% |
