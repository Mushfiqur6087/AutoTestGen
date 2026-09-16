# Coverage Evaluation — Share Account (Mifos / openai-gpt-5-mini)

GT source: dataset/ground_truth/Mifos/modules/Share_Account.md
GEN source: results/Mifos/openai-gpt-5-mini/modules/Share_Account.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MF-SHARE-001 | Create share account for client | Covered | TC-001 | TC-001 submits a new Share Account application from Client Detail with product/quantity/date — direct match. |
| MF-SHARE-002 | Approve share account application | Covered | TC-002 | TC-002 approves a Pending share account with Approved Shares/Date and asserts status 'Approved' — direct match. |
| MF-SHARE-003 | Activate share account | Covered | TC-004 | TC-004 activates an Approved share account and asserts status 'Active' — direct match. |
| MF-SHARE-004 | Purchase shares | Covered | TC-006 | TC-006 applies additional shares to an Active account and asserts the totals/transaction row update — direct match for "purchase shares". |
| MF-SHARE-005 | Redeem shares | Covered | TC-007 | TC-007 redeems shares from an Active account and asserts the redemption transaction row — direct match. |
| MF-SHARE-006 | View share transactions | Covered | TC-006, TC-007 | Both tests open the Purchased Shares/transactions tab and assert new rows appear, satisfying the "history is displayed" requirement (dividend history not shown, but GT states the requirement loosely across purchase/redemption/dividend). |
| MF-SHARE-007 | Post dividend to eligible share account | Not Covered | — | No GEN test triggers or posts a dividend anywhere in the suite. |
| MF-SHARE-008 | Close share account | Covered | TC-008 | TC-008 closes an Active share account and asserts status 'Closed' — direct match. |
| MF-SHARE-009 | Purchase shares below minimum allowed quantity | Covered | TC-012, TC-025 | GEN tests the minimum-quantity boundary at the share-application step (Requested Shares below/at minimum, blocked with inline error) rather than at the "Apply Additional Shares" step; this is a precondition/flow difference, not a different business rule, so credit is given per Core Principle guidance not to withhold Covered over precondition framing. |
| MF-SHARE-010 | Redeem blocked when client has no linked savings account for crediting redemption | Covered | TC-019 | Scenario rewritten (was: Redeem more shares than held, unattested — no over-holdings redemption test in GEN). TC-019 asserts redemption is blocked with a visible error when the client has no linked savings account to credit — direct match for the rewritten scenario. |
| MF-SHARE-011 | Purchase or redeem on non-active share account | Covered | TC-022 | TC-022 asserts the Redeem Shares action is unavailable while the account is in Approved (non-active) state — satisfies the "redeem on non-active account is blocked" clause of the combined GT scenario. |
| MF-SHARE-012 | Undo Approval on an Approved share account reverts it to Pending | Covered | TC-005 | Scenario rewritten (was: Activate share account with invalid date order, unattested — GEN's Activate test is happy-path only with no date field). TC-005 asserts Undo Approval reverts an Approved account to status 'Pending' and clears Approved-state fields — direct match for the rewritten scenario. |
| MF-SHARE-013 | Reject share account application | Covered | TC-003 | TC-003 rejects a Pending application and asserts status 'Rejected' — direct match. |
| MF-SHARE-014 | Share balance/value display updates after transactions | Covered | TC-006 | TC-006 explicitly asserts "Total approved shares... updates to reflect the addition" after a purchase transaction — matches the core "summary reflects updated holdings" requirement. |
| MF-SHARE-015 | Dividend posting respects eligible holdings and effective rules | Not Covered | — | No dividend feature is exercised anywhere in the GEN suite (consistent with MF-SHARE-007 gap). |

## Gap List (Not Covered)

- **MF-SHARE-007** — Dividend posting is entirely untested; no dividend action or transaction appears anywhere in this module's GEN suite.
- **MF-SHARE-015** — Dividend-eligibility/rule correctness is untested (dividend feature untested overall, consistent with MF-SHARE-007).

## Revision Note

Two rows described boundaries GEN never isolates (redemption exceeding current holdings, invalid activation-date ordering — Activate in GEN has no date field at all). GEN does demonstrate two other real, distinct behaviors that had no GT scenario crediting them:

- **MF-SHARE-010** (was: Redeem more shares than held) → Redemption is blocked when the client has no linked savings account to credit (TC-019)
- **MF-SHARE-012** (was: Activate share account with invalid date order) → Undo Approval reverts an Approved account to Pending status (TC-005)

Genuine gaps were deliberately preserved: dividend posting (MF-SHARE-007, MF-SHARE-015) is not exercised anywhere in this module's GEN suite — no dividend action, dialog, or transaction row appears in any of the 31 GEN test cases.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Share Account | 15 | 13 | 2 | 86.7% |
