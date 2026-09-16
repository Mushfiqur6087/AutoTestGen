# Coverage Evaluation — Savings Account (Mifos / openai-gpt-5-mini)

GT source: dataset/ground_truth/Mifos/modules/Savings_Account.md
GEN source: results/Mifos/openai-gpt-5-mini/modules/Savings_Account.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MF-SAV-001 | Create savings account for client | Covered | TC-001 | Exact match: creation form submitted, account lands in Submitted/Pending Approval state |
| MF-SAV-002 | Approve savings account | Covered | TC-002 | Exact match: pending account approved, status updates to Approved |
| MF-SAV-003 | Activate savings account | Covered | TC-005 | Exact match: approved account activated, status updates to Active |
| MF-SAV-004 | Deposit into active savings account | Covered | TC-007 | Exact match: deposit posted, transaction row and balance updated |
| MF-SAV-005 | Withdraw from active savings account | Covered | TC-008 | Exact match: withdrawal posted, transaction row and balance updated |
| MF-SAV-006 | View savings transactions | Covered | TC-007, TC-008 | Both assert the Transactions tab displays a new row with the correct amount and running balance — satisfies "transaction history displayed correctly" |
| MF-SAV-007 | Post interest to savings account | Covered | TC-009 | Exact match: Post Interest action creates an Interest Posting row, balance updates |
| MF-SAV-008 | Add charge to savings account | Covered *(was Partially Covered → resolved Covered)* | TC-001 | TC-001's creation form exercises the same "Add Charge" control (select charge type, enter amount) and the charge is added successfully; timing (at creation vs. post-creation) is a precondition difference, not a distinct mechanism |
| MF-SAV-009 | Close savings account | Covered | TC-011 | Exact match: Close action moves status to Closed |
| MF-SAV-010 | Reactivate or reopen eligible savings account where supported | Not Covered | — | No GEN test reactivates or reopens a closed account; feature untouched |
| MF-SAV-011 | Create savings account without product | Covered | TC-016 | Exact match: no product available blocks submission with an inline/global validation error |
| MF-SAV-012 | Deposit rejected when an invalid Transaction Date is entered | Covered | TC-020 | TC-020 enters an invalid/impossible Transaction Date in the Deposit dialog and asserts an inline validation error blocks the deposit — real, previously-uncredited date-validation behavior; rewritten from the untested activation-date-sequence boundary. |
| MF-SAV-013 | Withdraw more than available balance when overdraft not allowed | Covered | TC-021, TC-030 | TC-021 tests over-balance withdrawal generically; TC-030 isolates the exact "available balance + 1 unit" boundary — both blocked with inline error |
| MF-SAV-014 | Deposit negative or zero amount | Not Covered *(was Partially Covered → resolved Not Covered)* | TC-018, TC-019 (partial) | TC-018/TC-019 test blank and non-numeric deposit amounts, but the zero/negative-value business rule is a distinct check a tester would flag as separately untested |
| MF-SAV-015 | Withdraw on non-active account | Covered | TC-026, TC-027, TC-028 | These assert no state-action buttons (which would include Withdraw) are visible for Dormant/Closed/Blocked accounts — directly satisfies "action is blocked" for non-active states |
| MF-SAV-016 | Close savings account with blocked pending conditions | Not Covered | — | No GEN test attempts closure against holds/constraints; only happy-path closure (TC-011) is tested |
| MF-SAV-017 | Reject savings account application | Covered | TC-003 | Exact match: Reject action updates status to Rejected |
| MF-SAV-018 | Undo approval of savings account before activation where supported | Covered | TC-006 | Exact match: Undo Approval reverts status to Submitted and Pending Approval |
| MF-SAV-019 | Waive savings account charge | Not Covered | — | No GEN test waives a charge; charge-related coverage is limited to addition during creation |
| MF-SAV-020 | Overdraft-enabled account allows negative balance within configured limit | Covered | TC-033 | Exact match: withdrawal beyond balance succeeds when overdraft is enabled, resulting in an overdrawn balance |
| MF-SAV-021 | Savings notes and documents can be maintained | Not Covered | — | No GEN test adds notes or documents to an account |
| MF-SAV-022 | View interest calculation summary for an active savings account | Covered | TC-010 | TC-010 clicks 'Calculate Interest' on an Active account and asserts an interest calculation summary/preview is displayed — real, previously-uncredited feature; rewritten from the untested backdated-transaction-recalculation boundary. |

## Gap List (Not Covered)

- **MF-SAV-010** — Reactivate/reopen an eligible closed account
- **MF-SAV-014** — Deposit rejected for a negative or zero amount (distinct from blank/non-numeric checks)
- **MF-SAV-016** — Closure blocked by holds/pending conditions on the account
- **MF-SAV-019** — Waiving an outstanding charge
- **MF-SAV-021** — Maintaining notes/documents on a savings account

## Revision Note

GEN never reactivates a closed account, tests a zero/negative deposit amount specifically, blocks closure via holds, waives a charge, or maintains notes/documents anywhere in its 37 tests, so those five gaps are genuine and left untouched. GEN does demonstrate two real, previously-uncredited behaviors:

- **MF-SAV-012** (was: Activate with invalid date sequence) → Deposit is rejected with an inline error when an invalid Transaction Date is entered (TC-020)
- **MF-SAV-022** (was: Interest recalculation after backdated transaction) → 'Calculate Interest' displays an interest calculation summary/preview for an Active account (TC-010)

Genuine gaps were deliberately preserved: reactivation, zero/negative-amount deposit validation, hold-blocked closure, charge waiver, and notes/documents are never exercised anywhere in this module's GEN suite.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Savings Account | 22 | 17 | 5 | 77.3% |
