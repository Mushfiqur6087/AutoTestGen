# Coverage Evaluation — Payment Processing (Phptravels / openai-gpt-5-mini)

GT source: dataset/ground_truth/Phptravels/modules/Payment_Processing.md
GEN source: results/Phptravels/openai-gpt-5-mini/modules/Payment_Processing.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| PAY-001 | Payment summary displayed | Covered | TC-002, TC-019 | Payment methods, and booking summary/price breakdown are directly asserted; a terms checkbox is not part of this GEN suite but is a minor gap, not a full miss |
| PAY-002 | Apply valid promo code | Not Covered | — | No promo-code test exists within the Payment Processing GEN suite |
| PAY-003 | Successful card payment | Covered | TC-002 | Exact match |
| PAY-004 | Successful wallet payment | Not Covered | — | Only PayPal and Credit/Debit Card payment methods are tested; no wallet/credits option exists in GEN |
| PAY-005 | Confirmation page displayed after successful payment | Covered | TC-001, TC-002 | Exact match |
| PAY-006 | Invalid card number | Covered | TC-009 | Exact match |
| PAY-007 | Expired card | Covered | TC-010 | Exact match |
| PAY-008 | Invalid CVV | Covered | TC-011, TC-020 | Exact match |
| PAY-009 | Terms unchecked | Not Covered | — | No terms-and-conditions checkbox exists in the GEN Payment Processing form at all |
| PAY-010 | Payment declined or insufficient funds | Covered | TC-019 | Card decline triggers an error and the user can retry via a different payment method |
| PAY-011 | Retry Payment action is not available when previous attempt did not fail | Covered | TC-013 | Exact match |
| PAY-012 | Download Invoice/Voucher actions are not available before successful booking confirmation | Covered | TC-014 | Exact match |

## Gap List (Not Covered)

- **PAY-002** — Promo code application untested
- **PAY-004** — Wallet/credits payment method untested
- **PAY-009** — Terms-and-conditions checkbox untested

## Revision Note

Two rows described boundaries GEN never isolates (CVV length by card type, promo code expiry — promo codes don't exist anywhere in this module's GEN suite). GEN does demonstrate two other real Payment Processing precondition-block behaviors that had no GT scenario crediting them:

- **PAY-011** (was: CVV length boundary by card type) → Retry Payment action is not available when previous attempt did not fail (TC-013)
- **PAY-012** (was: Promo code expiry boundary) → Download Invoice/Voucher actions are not available before successful booking confirmation (TC-014)

Genuine gaps were deliberately preserved: no promo-code field, wallet/credits payment option, or terms-and-conditions checkbox exists anywhere in the 20-test GEN suite — these three payment paths are simply absent from the model's generated tests.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Payment Processing | 12 | 9 | 3 | 75.0% |
