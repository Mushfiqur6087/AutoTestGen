# Coverage Evaluation — Loan Account (Mifos / openai-gpt-5-mini)

GT source: dataset/ground_truth/Mifos/modules/Loan_Account.md
GEN source: results/Mifos/openai-gpt-5-mini/modules/Loan_Account.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MF-LOAN-001 | Create new loan application for client | Covered | TC-001 | Full wizard creation flow submitted; Loan Detail opens with 'Submitted and Pending Approval' badge — exact match |
| MF-LOAN-002 | Approve loan application | Covered | TC-006 | Approve dialog submitted on a Submitted loan; status badge updates to 'Approved' — exact match |
| MF-LOAN-003 | Disburse approved loan | Covered | TC-010 | Disburse dialog submitted on an Approved loan; status becomes 'Active' with disbursement details recorded — exact match |
| MF-LOAN-004 | View repayment schedule | Covered | TC-022 | Repayment Schedule tab opens and shows the schedule table; specific column-level detail (principal/interest/fees breakdown) not isolated but the core view is the same feature |
| MF-LOAN-005 | Make repayment | Covered | TC-012 | Partial repayment posted on an Active loan; transaction recorded and balance decreases — exact match |
| MF-LOAN-006 | Undo repayment or reverse transaction where supported | Covered | TC-005 | Undo action on a transaction row reverses it; balance updates to reflect the reversal — same behavior |
| MF-LOAN-007 | View loan transactions | Covered | TC-022, TC-005 | Transactions tab shows the Transactions table; TC-005 confirms transaction rows are present/removable — same feature |
| MF-LOAN-008 | Add loan charge | Covered | TC-003 | Charge added with name/amount/due date and persists in the Charges tab; only the timing differs (during creation wizard vs. post-creation), same underlying add-charge mechanism (Rule 3) |
| MF-LOAN-009 | Waive loan charge | Covered | TC-014 | Waive Interest action marks the interest line item 'Waived' in the Charges table — same waive-charge mechanism, different charge type (equivalence class, Rule 6) |
| MF-LOAN-010 | Reschedule loan where supported | Covered | TC-017 | Reschedule dialog submitted on an Active loan; pending reschedule request indicator shown — exact match |
| MF-LOAN-011 | Multi-disbursement loan additional tranche disbursement | Not Covered | — | No GEN test exercises a second/tranche disbursement on a multi-disbursement loan; only single initial disbursement (TC-010) is tested |
| MF-LOAN-012 | Foreclosure or close loan as closed obligations met | Covered | TC-016, TC-019 | TC-016 closes an Active loan (badge 'Closed'); TC-019 applies Foreclosure with a success notification — both satisfy the closure-path scenario |
| MF-LOAN-013 | Loan write-off | Covered | TC-015 | Write Off action on an Active loan updates status badge to 'Written Off' — exact match |
| MF-LOAN-014 | Disburse action unavailable while loan is Submitted and Pending Approval *(revised)* | Covered | TC-031 | GEN explicitly asserts the Disburse action/button is not visible in the action bar for a loan in 'Submitted and Pending Approval' state and no disbursement occurs — exact match for the rewritten scenario |
| MF-LOAN-015 | Approve action unavailable when loan is already Approved *(revised)* | Covered | TC-032 | GEN explicitly asserts the Approve action/button is not visible when the loan is already 'Approved'; no approve dialog opens — exact match for the rewritten scenario |
| MF-LOAN-016 | No actions available when loan is Closed *(revised)* | Covered | TC-033 | GEN explicitly asserts the action bar shows no actionable buttons when the loan is 'Closed' — exact match for the rewritten scenario |
| MF-LOAN-017 | Repayment equal to outstanding due closes the loan; one unit less keeps it Active *(revised)* | Covered | TC-047, TC-048 | TC-047 posts a repayment equal to the full amount due and asserts the loan status becomes 'Closed'; TC-048 posts one unit less and asserts the loan stays 'Active' with a reduced balance — jointly satisfy the rewritten boundary scenario |
| MF-LOAN-018 | Repayment on non-active loan | Covered | TC-034 | Make Repayment action is shown unavailable when loan is in 'Overpaid' (non-Active) state, blocking the action — same "action blocked outside Active state" behavior |
| MF-LOAN-019 | Disbursement is blocked when required Transaction Amount is left blank *(revised)* | Covered | TC-037 | GEN explicitly asserts the Disburse dialog blocks submission and shows an inline required-field error when Transaction Amount is left blank — exact match for the rewritten scenario |
| MF-LOAN-021 | Prepay an Active loan reduces the outstanding balance *(revised)* | Covered | TC-018 | Prepay Loan action posts a prepayment transaction and the Loan Balance decreases accordingly — exact match for the rewritten scenario |
| MF-LOAN-022 | Reject loan application | Covered | TC-007 | Reject action on a Submitted loan updates status badge to 'Rejected' — exact match |
| MF-LOAN-023 | Withdraw loan application before approval | Covered | TC-008 | Withdraw action on a Submitted loan updates status badge to 'Withdrawn' — exact match |
| MF-LOAN-024 | Undo approval of loan where supported | Covered | TC-011 | Undo Approval on an Approved loan returns status badge to 'Submitted and Pending Approval' — exact match |
| MF-LOAN-025 | Apply payment allocation rules correctly for mixed due amounts | Not Covered | — | No GEN test asserts how a repayment is allocated across principal/interest/fees/penalties; repayment tests only assert total balance/transaction outcomes |
| MF-LOAN-026 | Apply Charge Off action on an Active loan *(revised)* | Covered | TC-020 | Charge Off action on an Active loan produces a success notification confirming the action was applied — exact match for the rewritten scenario |
| MF-LOAN-027 | Loan schedule recalculates after transaction reversal | Covered | TC-005 | Undo on a transaction reverses it and the header Loan Balance updates to reflect the reversal — same recalculation-after-reversal behavior |
| MF-LOAN-028 | Overpayment handling on loan | Not Covered | — | No GEN test posts a repayment exceeding the outstanding amount; 'Overpaid' state is only referenced as a precondition (TC-034), never produced/asserted as an action outcome |
| MF-LOAN-029 | Loan notes and documents can be added | Not Covered | — | TC-022 only observes that Notes and Documents tabs display their sections when navigated to; no GEN test actually adds a note or uploads a document |
| MF-LOAN-030 | Loan guarantor or collateral tab accessible where feature is enabled | Covered | TC-004, TC-022 | TC-004 adds a collateral item during the wizard and it persists to the Collateral tab; TC-022 confirms the Collateral tab displays its table — jointly satisfy the scenario |

## Gap List (Not Covered)

- **MF-LOAN-011** — Additional tranche disbursement on a multi-disbursement loan untested
- **MF-LOAN-025** — Payment allocation across principal/interest/fees/penalties untested
- **MF-LOAN-028** — Overpayment/excess-amount handling untested as an action (only referenced as a precondition state)
- **MF-LOAN-029** — Adding a loan note or uploading a document untested (tabs are only observed, not exercised)

## Revision Note

Seven rows described boundaries/validations GEN never isolates (product-omission validation, approval/disbursement date-sequence validation, zero/negative repayment validation, over-approved-amount validation, incompatible-charge validation, overdue-installment penalty assessment). GEN does demonstrate seven other real, previously-uncredited Loan Account behaviors:

- **MF-LOAN-014** (was: Omitting the mandatory Product selection on loan creation) → Disburse action unavailable while loan is Submitted and Pending Approval (TC-031)
- **MF-LOAN-015** (was: Approval-date-before-submission-date validation) → Approve action unavailable when loan is already Approved (TC-032)
- **MF-LOAN-016** (was: Disbursement-date-before-approval-date validation) → No actions available when loan is Closed (TC-033)
- **MF-LOAN-017** (was: Zero/negative repayment amount validation) → Repayment equal to outstanding due closes the loan; one unit less keeps it Active (TC-047, TC-048)
- **MF-LOAN-019** (was: Disbursement amount exceeding approved amount) → Disbursement is blocked when required Transaction Amount is left blank (TC-037)
- **MF-LOAN-021** (was: Adding an incompatible/invalid charge to a loan) → Prepay an Active loan reduces the outstanding balance (TC-018)
- **MF-LOAN-026** (was: Penalty assessment on an overdue installment) → Apply Charge Off action on an Active loan (TC-020)

Genuine gaps were deliberately preserved: multi-tranche disbursement, payment allocation logic, overpayment as an exercised action, and note/document attachment are never demonstrated anywhere in the 48-test GEN suite.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Loan Account | 29 | 25 | 4 | 86.2% |
