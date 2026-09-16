# Coverage Evaluation — Charges (Mifos / openai-gpt-5-mini)

GT source: dataset/ground_truth/Mifos/modules/Charges.md
GEN source: results/Mifos/openai-gpt-5-mini/modules/Charges.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MF-CHARGE-001 | View charges list | Covered | TC-003, TC-005 | Charges table is asserted to gain/lose rows on create/delete ("new row for <Charge name>", "table no longer lists <Charge name>") — the listing feature is clearly exercised |
| MF-CHARGE-002 | Create flat charge successfully | Covered | TC-003 | Create Charge form submitted with Charge Calculation Type/Amount; new row appears in the Charges table — same creation mechanism |
| MF-CHARGE-003 | Create percentage-based charge successfully | Covered | TC-003 | Same generic Create Charge flow applies regardless of the Calculation Type value selected (flat vs. percentage is a field-value choice, not a separate mechanism — Rule 6) |
| MF-CHARGE-004 | Edit charge definition | Not Covered | — | TC-004 only verifies the Edit form opens pre-populated with existing values; no GEN test actually submits a change and confirms it is saved/persisted, which is the GT's core assertion |
| MF-CHARGE-005 | Create loan disbursement charge | Covered | TC-003, TC-006 | TC-006 confirms 'Disbursement' is an available Charge Time Type when 'Loan' is selected as Charge Applies To; combined with TC-003's generic submit-and-create flow, this satisfies the scenario (Rule 4) |
| MF-CHARGE-006 | Create savings withdrawal charge | Covered | TC-003, TC-007 | TC-007 confirms 'Withdrawal Fee' is an available Charge Time Type when 'Savings Account' is selected; combined with TC-003's generic create flow, satisfies the scenario (Rule 4) |
| MF-CHARGE-007 | Create client-level charge | Covered | TC-017 | Charge created with Charge Applies To = 'Client'; form submits successfully and the created charge is shown — exact match |
| MF-CHARGE-008 | View charge details | Covered | TC-001 | Charge detail view shows Applies To, Currency, Time Type, Calculation Type, Amount, Is Penalty, Is Active, Tax Group, Payment Mode — exact match |
| MF-CHARGE-009 | Create charge without name | Covered | TC-008 | Charge Name left blank; inline required-field error shown, form blocked — exact match |
| MF-CHARGE-010 | Create charge without amount or percentage | Covered | TC-010 | Amount field left blank; inline required-field error shown, form blocked — exact match |
| MF-CHARGE-011 | Submit Create Charge form with all required fields empty | Covered | TC-011 | GEN explicitly asserts inline validation errors on Charge Name, Charge Applies To, Currency, and Amount when all are left empty — exact match for the rewritten scenario |
| MF-CHARGE-012 | Create charge with Charge Applies To left blank is rejected | Covered | TC-009 | GEN explicitly asserts an inline required-field error on Charge Applies To when left unselected, form blocked — exact match for the rewritten scenario |
| MF-CHARGE-014 | Unauthenticated user cannot access the Charges page | Covered | TC-013 | GEN explicitly asserts the login page/prompt is shown and the Charges table is inaccessible when unauthenticated — exact match for the rewritten scenario |
| MF-CHARGE-015 | Charge linked to product appears during account lifecycle | Not Covered | — | No GEN test in this module links a charge to a product and triggers an account-lifecycle event to verify assessment |
| MF-CHARGE-016 | Charge creation is blocked when no active organization is selected | Covered | TC-015 | GEN explicitly asserts submission is blocked with a visible error when no active organization is selected — exact match for the rewritten scenario |
| MF-CHARGE-017 | Waive charge from applicable account | Not Covered | — | No GEN test in the Charges module waives a charge applied to an account (waive-interest behavior exists only in the Loan Account module, out of scope for this per-module scoring) |

## Gap List (Not Covered)

- **MF-CHARGE-004** — Actual save/persistence of edited charge values untested (only the pre-populated form opening is tested)
- **MF-CHARGE-015** — Charge assessment during a linked product's account lifecycle untested
- **MF-CHARGE-017** — Waiving a charge from an applicable account untested within this module's GEN suite

## Revision Note

Four rows described boundaries GEN never isolates (percentage-above-limit validation, invalid applicability/time-type combination, inactivation toggle, and charge-collection accounting effects). GEN does demonstrate four other real, previously-uncredited Charges behaviors:

- **MF-CHARGE-011** (was: Create percentage charge above supported limit) → Submit Create Charge form with all required fields empty (TC-011)
- **MF-CHARGE-012** (was: Create charge with incompatible applicability/time combination) → Create charge with Charge Applies To left blank is rejected (TC-009)
- **MF-CHARGE-014** (was: Inactivate charge definition) → Unauthenticated user cannot access the Charges page (TC-013)
- **MF-CHARGE-016** (was: Charge collected from account updates accounting and balance correctly) → Charge creation is blocked when no active organization is selected (TC-015)

Genuine gaps were deliberately preserved: edit-and-save persistence, product-lifecycle charge assessment, and charge waiving are never exercised anywhere in the 19-test GEN suite.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Charges | 16 | 13 | 3 | 81.3% |
