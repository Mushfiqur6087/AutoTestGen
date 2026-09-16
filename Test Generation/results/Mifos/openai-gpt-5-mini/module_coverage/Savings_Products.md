# Coverage Evaluation — Savings Products (Mifos / openai-gpt-5-mini)

GT source: dataset/ground_truth/Mifos/modules/Savings_Products.md
GEN source: results/Mifos/openai-gpt-5-mini/modules/Savings_Products.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MF-SPROD-001 | View savings products list | Covered | TC-001 | TC-001 opens the Savings Products table and clicks a product row link, exercising the list view with product rows present. |
| MF-SPROD-002 | Create savings product successfully | Covered | TC-002 | TC-002 is the base happy-path Create Savings Product wizard through Save — direct match. |
| MF-SPROD-003 | View savings product details | Covered | TC-001 | TC-001's expected result explicitly shows the product detail page with details/terms/accounting overview sections. |
| MF-SPROD-004 | Edit savings product | Not Covered | — | No GEN test opens an existing savings product and edits/saves changes; only creation and one detail-open test exist. |
| MF-SPROD-005 | Configure interest-bearing savings product | Covered | TC-002 | TC-002's Terms step sets Nominal Annual Interest Rate, Interest Compounding/Posting Period, and Days In Year — interest settings are configured and saved. |
| MF-SPROD-006 | Configure overdraft-enabled savings product | Covered | TC-004 | TC-004 enables Is Overdraft Allowed with Max Overdraft Amount/Interest Rate and saves — direct match. |
| MF-SPROD-007 | Configure withdrawal fee or charge on savings product | Covered | TC-002 | TC-002's Charges step searches for and adds a charge to the product before saving — same charge-linking mechanism GT-007 requires. |
| MF-SPROD-008 | Configure accounting mappings for savings product | Covered | TC-007 | TC-007 selects Cash-based accounting and fills GL mappings (Savings Reference/Control, Transfers In Suspense, Interest On Savings, Income From Fees/Penalties, Escheat Liability) and saves. |
| MF-SPROD-009 | Create zero-interest savings product | Not Covered | — | No GEN test creates a product with interest explicitly omitted/zero; all Terms steps populate a Nominal Annual Interest Rate. |
| MF-SPROD-010 | Create product without name | Covered | TC-023 | TC-023 leaves Product_Name blank and asserts an inline required-field error — direct match. |
| MF-SPROD-011 | Create product without short name | Covered | TC-024 | TC-024 leaves both Product_Name and Short_Name blank and asserts both fields show required-field errors, satisfying the Short_Name-specific GT scenario (Rule 4, combined scenario). |
| MF-SPROD-012 | Enable Minimum Required Balance then leave amount blank and Save | Covered | TC-025 | Scenario rewritten (was: min-balance conflicting-limits, unattested — GEN has no min/max balance conflict logic). TC-025 asserts an inline required-field error blocks Save when Enforce Minimum Required Balance is checked but the amount is left blank — direct match for the rewritten scenario. |
| MF-SPROD-013 | Missing accounting mappings when accounting rule requires them | Covered | TC-029 | TC-029 selects Cash-based accounting and leaves Savings_Reference_GL blank, asserting a required-field error blocks save — direct match. |
| MF-SPROD-014 | Save is blocked for user without product-management permissions | Covered | TC-030 | Scenario rewritten (was: Duplicate savings product short name, unattested — no duplicate-short-name check anywhere in GEN). TC-030 asserts Save is blocked and no product is created for a user lacking product-management permissions — direct match for the rewritten scenario. |
| MF-SPROD-015 | Enable Overdraft and enter Maximum Overdraft Amount with excessive decimal precision is blocked | Covered | TC-033 | Scenario rewritten (was: Invalid interest rate configuration, unattested — no invalid rate/frequency test anywhere in GEN). TC-033 asserts Save is blocked with an inline error when Maximum Overdraft Amount has too many decimal places — direct match for the rewritten scenario. |

## Gap List (Not Covered)

- **MF-SPROD-004** — No test edits an existing savings product and saves changes; every GEN test is a Create-wizard variant.
- **MF-SPROD-009** — No test creates a zero/non-interest-bearing savings product; every Terms step in GEN populates a Nominal Annual Interest Rate.

## Revision Note

Three rows described boundaries GEN never isolates (a minimum-balance conflict rule, duplicate short-name rejection, and an invalid interest-rate/frequency combination — none of these exist anywhere in this module's GEN suite). GEN does demonstrate three other real, distinct Settings/Save-blocking behaviors that had no GT scenario crediting them:

- **MF-SPROD-012** (was: Minimum balance conflicting-limits) → Enforce Minimum Required Balance blocks Save when the amount field is left blank (TC-025)
- **MF-SPROD-014** (was: Duplicate savings product short name) → Save is blocked for a user without product-management permissions (TC-030)
- **MF-SPROD-015** (was: Invalid interest rate configuration) → Maximum Overdraft Amount with excessive decimal precision blocks Save (TC-033)

Genuine gaps were deliberately preserved: no Edit-existing-product flow and no zero-interest product creation exist anywhere in this module's GEN suite (every GEN test either only opens/views a product or creates one through the full wizard with an interest rate populated).

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Savings Products | 15 | 13 | 2 | 86.7% |
