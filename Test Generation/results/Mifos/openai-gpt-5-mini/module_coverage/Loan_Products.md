# Coverage Evaluation — Loan Products (Mifos / openai-gpt-5-mini)

GT source: dataset/ground_truth/Mifos/modules/Loan_Products.md
GEN source: results/Mifos/openai-gpt-5-mini/modules/Loan_Products.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MF-LPROD-001 | View loan products list | Covered | TC-001, TC-007 | TC-001 locates a row in the products table and TC-007's filter test explicitly asserts "Loan Products table displays only rows matching..." — the list-rendering mechanism is directly asserted, not merely presupposed |
| MF-LPROD-002 | Create loan product successfully | Covered | TC-002, TC-003 | Both complete the create wizard and assert a new row appears in the listing with the entered Name/Short Name |
| MF-LPROD-003 | View loan product detail (terms, charges, accounting, configuration) | Not Covered | TC-001 (partial), TC-003 (partial) | TC-001 only asserts title + Edit button; TC-003 only confirms the Accounting section (method + GL mappings) renders on the detail view — Terms and Charges sections are never asserted as displayed, a distinct UI-state gap a tester would flag |
| MF-LPROD-004 | Edit loan product | Covered | TC-004, TC-005 | Both open the edit wizard, change a field, save, and assert the detail view reflects the updated value |
| MF-LPROD-005 | Create declining balance loan product | Not Covered | — | TC-002/TC-003 only set "<Interest Method> (use available options)" as an unspecified placeholder with no assertion tied to the calculation method; the declining-balance-specific configuration and its "correct calculation configuration" outcome are never isolated or asserted |
| MF-LPROD-006 | Create flat interest loan product | Not Covered | — | Same generic, unasserted interest-method placeholder as above; the flat-interest-specific boundary is never isolated |
| MF-LPROD-007 | Unauthenticated user cannot access Loan Products page | Covered | TC-015 | GEN explicitly asserts an unauthenticated user is redirected to login and the Loan Products listing is inaccessible — exact match for the rewritten scenario |
| MF-LPROD-008 | Configure accounting mappings for loan product | Covered | TC-003, TC-005 | Both select a non-None accounting method, fill Fund Source/Loan Portfolio/Interest On Loans mappings, save, and assert the mappings display on the detail view |
| MF-LPROD-011 | Create product without product name | Covered | TC-008, TC-009 | TC-009 leaves Product Name blank specifically and asserts an inline required-field error; TC-008 reinforces via the combined blank-fields case |
| MF-LPROD-012 | Create product without short name | Covered | TC-008 | TC-008 leaves both Product Name and Short Name blank and asserts inline required errors on both fields — the required-field validation mechanism is directly exercised on Short Name |
| MF-LPROD-013 | Principal Amount Default outside the configured minimum/maximum range is blocked | Covered | TC-014 | GEN explicitly asserts Save is blocked with an inline error when the Principal Amount Default falls outside the configured min/max range — exact match for the rewritten scenario |
| MF-LPROD-014 | Invalid Start Date format prevents progressing through the wizard | Covered | TC-010 | GEN explicitly asserts an invalid Start Date format blocks progressing to the next wizard step — exact match for the rewritten scenario |
| MF-LPROD-015 | Missing mandatory accounting mappings when accounting enabled | Covered | TC-011 | Exact match: selects a non-None Accounting Method, leaves Fund Source and other GL dropdowns blank, asserts Save is blocked with inline required errors |
| MF-LPROD-017 | Cancelling the Create Loan Product wizard discards entered changes | Covered | TC-006 | GEN explicitly asserts clicking Cancel closes the wizard with no new row created in the listing — exact match for the rewritten scenario |

## Gap List (Not Covered)

- **MF-LPROD-003** — Product detail view's Terms and Charges sections are never asserted as displayed (only Accounting is confirmed)
- **MF-LPROD-005** — Declining-balance interest method configuration/calculation not isolated or asserted
- **MF-LPROD-006** — Flat interest method configuration/calculation not isolated or asserted

## Revision Note

Four rows described boundaries GEN never isolates (principal min>max as an inverted range, interest-rate min>max range, charge retention/storage on save, invalid/zero repayment frequency). GEN does demonstrate four other real, previously-uncredited Loan Products behaviors:

- **MF-LPROD-007** (was: Configure loan product charges) → Unauthenticated user cannot access Loan Products page (TC-015)
- **MF-LPROD-013** (was: Create product with principal min greater than principal max) → Principal Amount Default outside the configured minimum/maximum range is blocked (TC-014)
- **MF-LPROD-014** (was: Create product with interest rate min greater than max) → Invalid Start Date format prevents progressing through the wizard (TC-010)
- **MF-LPROD-017** (was: Invalid repayment frequency values) → Cancelling the Create Loan Product wizard discards entered changes (TC-006)

Genuine gaps were deliberately preserved: the product detail view's Terms/Charges sections, and interest-method-specific (declining balance vs. flat) configuration and calculation, are never isolated or asserted anywhere in the 24-test GEN suite.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Loan Products | 14 | 11 | 3 | 78.6% |
