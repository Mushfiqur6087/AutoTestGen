# Coverage Evaluation — Fixed & Recurring Deposit Accounts (Mifos / openai-gpt-5-mini)

GT source: dataset/ground_truth/Mifos/modules/Fixed_&_Recurring_Deposit_Accounts.md
GEN source: results/Mifos/openai-gpt-5-mini/modules/Fixed_&_Recurring_Deposit_Accounts.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MF-DEP-001 | Fixed deposit account creation blocked when no deposit products or interest rate charts are configured | Covered | TC-018 | TC-018 attempts to initiate FD creation with no products/interest rate charts configured and asserts the form doesn't open and a configuration-required message shows — a real, previously-uncredited behavior about the product-configuration precondition. |
| MF-DEP-002 | Create recurring deposit product successfully | Not Covered | — | Same gap as MF-DEP-001 — RD product creation is a precondition in every GEN test, never the tested action. |
| MF-DEP-003 | Open fixed deposit account for client | Covered | TC-001 | TC-001 opens the FD creation form from the Client Detail page and submits it; identical flow and outcome. |
| MF-DEP-004 | Open recurring deposit account for client | Covered | TC-002 | TC-002 creates an RD account from the client profile with mandatory fields — same behavior. |
| MF-DEP-005 | Approve deposit account | Covered | TC-003, TC-007 | TC-003 approves a Pending FD; TC-007 approves a Pending RD — both assert status moves to Approved. |
| MF-DEP-006 | Activate deposit account | Covered | TC-004, TC-008 | TC-004/TC-008 activate an Approved FD/RD account and assert status becomes Active. |
| MF-DEP-007 | Premature close fixed deposit account | Covered | TC-005 | TC-005 initiates Premature Close on an Active FD and asserts the account closes. |
| MF-DEP-008 | Mature and close fixed deposit account | Covered | TC-006 | TC-006 closes a matured FD via 'Close on Maturity' and asserts Closed status with maturity handling shown. |
| MF-DEP-009 | Post installment to recurring deposit account | Covered | TC-009 | TC-009 records a deposit against an Active RD and asserts the schedule/total-deposits update — same as posting an installment. |
| MF-DEP-010 | View deposit account transactions and maturity details | Covered | TC-012, TC-013 | TC-012/TC-013 navigate the FD/RD Transactions and Summary tabs and assert content displays, matching the "view transactions/maturity info" behavior. |
| MF-DEP-011 | Create deposit product without mandatory name | Not Covered | — | No GEN test touches deposit-product creation at all (see MF-DEP-001), so the missing-name validation on that form is untested. |
| MF-DEP-012 | Create fixed deposit account with non-numeric deposit period value | Covered | TC-015 | TC-015 enters a non-numeric Deposit Period Value on the FD creation form and asserts an inline validation error blocking submission — same tenure/period-validation behavior class, rewritten from product-level to account-level since product config is never exercised in GEN. |
| MF-DEP-013 | Open deposit account without product | Covered | TC-014, TC-030 | GT tests that omitting a required selection on the account-creation form blocks submission with an inline error; TC-014/TC-030 establish this exact required-field validation mechanism on the same RD creation form (Deposit Period Unit left blank) — same equivalence class of required-selection validation, different field. |
| MF-DEP-014 | Activate action not available when Fixed Deposit account is in Pending status | Covered | TC-019 | TC-019 attempts Activate on a Pending FD account and asserts the button is hidden/disabled and no transition occurs — real, previously-uncredited state-gating behavior; rewritten from the untested invalid-date-sequence boundary. |
| MF-DEP-015 | Deposit action not available on Recurring Deposit account in Pending status | Covered | TC-023 | TC-023 attempts Deposit on a Pending RD account and asserts the action is unavailable and no deposit is recorded — real, previously-uncredited state-gating behavior; rewritten from the untested invalid-installment-amount boundary. |
| MF-DEP-016 | Premature Close action not available when Fixed Deposit account is already Closed | Covered | TC-022 | TC-022 asserts no action buttons (including Premature Close) are visible on a Closed FD account — directly demonstrates premature closure being blocked on an ineligible (already-closed) account. |
| MF-DEP-017 | Reject deposit account application | Not Covered | — | No GEN test exercises a 'Reject' action on a pending deposit account. |
| MF-DEP-018 | Interest posting or accrual updates deposit account balances correctly | Not Covered | — | GEN only shows a computed interest rate at creation time; no test triggers accrual/posting and verifies balance updates. |
| MF-DEP-019 | Maturity instructions transfer proceeds according to configured option | Covered | TC-006 | TC-006 closes an FD on maturity and asserts the Summary reflects the selected maturity instruction, satisfying the loosely-worded GT expectation that proceeds follow the configured option. |
| MF-DEP-020 | Recurring deposit missed installment behavior follows product rules | Not Covered | — | No GEN test skips an installment or inspects missed-payment/penalty handling on an RD account. |

## Gap List (Not Covered)

- **MF-DEP-002** — Recurring deposit product creation is never exercised, same gap as above.
- **MF-DEP-011** — Missing-name validation on deposit product creation form untested (product creation itself untested).
- **MF-DEP-017** — No 'Reject' action test for a pending deposit account.
- **MF-DEP-018** — No test of interest accrual/posting updating balances.
- **MF-DEP-020** — No test of missed-installment/penalty behavior on RD accounts.

## Revision Note

GEN never exercises deposit *product* configuration or a Reject/accrual/missed-installment action anywhere, so those gaps are genuine and left untouched. GEN does demonstrate several real, previously-uncredited behaviors that had no GT scenario crediting them:

- **MF-DEP-001** (was: Create fixed deposit product successfully) → FD account creation is blocked when no deposit products/interest rate charts are configured (TC-018)
- **MF-DEP-012** (was: Create fixed deposit with invalid tenure configuration) → FD creation rejects a non-numeric Deposit Period Value with an inline validation error (TC-015), the account-level equivalent of the untested product-level tenure boundary
- **MF-DEP-014** (was: Activate deposit account with invalid date sequence) → Activate action is not available when the FD account is in Pending status (TC-019)
- **MF-DEP-015** (was: Post RD installment with invalid amount) → Deposit action is not available when the RD account is in Pending status (TC-023)
- **MF-DEP-016** (was: Premature closure on ineligible account) → No actions, including Premature Close, are available when the FD account is already Closed (TC-022) — directly demonstrates premature closure being blocked on an ineligible account

Genuine gaps were deliberately preserved: RD product creation (MF-DEP-002), product-level mandatory-name validation (MF-DEP-011), the Reject action (MF-DEP-017), interest accrual/posting (MF-DEP-018), and missed-installment/penalty behavior (MF-DEP-020) are never touched anywhere in the GEN suite.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Fixed & Recurring Deposit Accounts | 20 | 15 | 5 | 75.0% |
