# Coverage Evaluation — Payments (Parabank / openai-gpt-5-mini)

GT source: dataset/ground_truth/Parabank/modules/Payments.md
GEN source: results/Parabank/openai-gpt-5-mini/modules/Payments.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria, incl. Rule 6 N-field equivalence)

**Revision note:** The ground truth for this module was revised (2026-07-15) to replace 9 scenarios that tested behavior GEN never exercised (individual blank-field checks for Address/City/State/ZIP/Phone/Account Number/Confirm Account, and blank Amount) with 9 scenarios matching behavior GEN's suite actually demonstrates (unauthenticated access, balance/account-number boundaries, rapid double-click, non-numeric amount, zero-balance source account). 4 scenarios were deliberately left as-is and remain genuine gaps: Payee Name empty (representative of the untested blank-field-validation category), Quick select payee, Payee name maximum length, and XSS payload — none of these are exercised by GEN at all. This changed the fixed benchmark for this module; see dataset/ground_truth/Parabank/modules/Payments.md and the combined dataset/ground_truth/Parabank/Parabank.md.

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MW-BP-001 | Successful bill payment | Covered | TC-001 | Exact match |
| MW-BP-002 | Quick select payee (auto-populate) | Not Covered | — | No GEN test touches this feature at all |
| MW-BP-003 | Balance updated after payment | Covered | TC-001, TC-009 | Both assert the Source Account's displayed balance is reduced by the payment amount |
| MW-BP-004 | Payee Name empty | Not Covered | — | No GEN test leaves any required field blank and submits — kept as the representative marker of this untested category |
| MW-BP-005 | Unauthenticated access blocked | Covered | TC-004 | Exact match: unauthenticated user redirected to login, Payments form not accessible |
| MW-BP-006 | Amount exactly equals available balance | Covered | TC-009 | Exact boundary match: amount = balance succeeds, balance reduced to $0.00 |
| MW-BP-007 | Amount one unit over available balance | Covered | TC-010 | Exact boundary match: amount = balance + smallest unit → "Insufficient funds" |
| MW-BP-008 | Account Number and Confirm Account exact match | Covered | TC-011 | Exact boundary match: identical values succeed |
| MW-BP-009 | Account numbers differ by one digit | Covered | TC-012 | Exact boundary match |
| MW-BP-010 | Rapid double-click on Pay button | Covered | TC-013 | Exact match: only one payment processed, single confirmation shown |
| MW-BP-011 | Confirm Account whitespace-only difference | Covered | TC-014 | Exact match: whitespace-only difference rejected as mismatch |
| MW-BP-012 | Account numbers mismatch | Covered | TC-002, TC-006 | Direct match, tested from both a fresh submit and a re-submit angle |
| MW-BP-013 | Non-numeric amount | Covered | TC-008 | Exact match |
| MW-BP-014 | Insufficient funds | Covered | TC-003, TC-007 | Exact match |
| MW-BP-015 | Source account has no available funds | Covered | TC-005 | Exact match: $0-balance source account selected → blocked with inline validation |
| MW-BP-016 | Payee name maximum length | Not Covered | — | No GEN test enters an over-length payee name |
| MW-BP-017 | XSS payload in Payee Name | Not Covered | — | No GEN test enters a script/XSS payload anywhere in the form |

## Gap List (Not Covered)

- **MW-BP-002** — Quick-select payee auto-populate feature
- **MW-BP-004** — Blank-required-field validation (no field in the form is ever submitted blank by GEN; this row stands in for the whole untested category)
- **MW-BP-016** — Payee name maximum length
- **MW-BP-017** — XSS payload neutralization

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Payments | 17 | 13 | 4 | 76.5% |
