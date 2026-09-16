# Coverage Evaluation — Share Products (Mifos / openai-gpt-5-mini)

GT source: dataset/ground_truth/Mifos/modules/Share_Products.md
GEN source: results/Mifos/openai-gpt-5-mini/modules/Share_Products.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MF-SHPROD-001 | View share products list | Covered | TC-001, TC-003 | TC-001 asserts a new row appears in the Share Products table after creation; TC-003 locates and opens a row from that table — the list-rendering mechanism is directly exercised |
| MF-SHPROD-002 | Create share product successfully | Covered | TC-001, TC-002 | Both complete the 7-step wizard and assert a new row appears with the entered Product Name/Short Name |
| MF-SHPROD-003 | View share product detail (pricing, share limits, settings) | Covered | TC-003, TC-002, TC-009 | TC-009 explicitly asserts the detail page's Market Prices table shows the entered pricing row; TC-002 asserts the Accounting settings/mappings render on the detail view; TC-003 confirms the detail view opens — pricing and settings are directly asserted even though "share limits" specifically is not |
| MF-SHPROD-004 | Edit share product | Not Covered | TC-004, TC-006 (partial) | TC-004/TC-006 only open the Edit wizard and confirm the Product Name is pre-loaded — neither changes a field, saves, nor asserts "changes are saved successfully"; opening the editor is a precondition for editing, not the edit-and-save behavior itself |
| MF-SHPROD-005 | Configure dividend settings on share product | Not Covered | TC-001 (partial) | TC-001's Settings step only "optionally" checks Allow Dividends for Inactive Clients with no assertion tied to it anywhere in the Expected Result; no test confirms dividend configuration is retained |
| MF-SHPROD-006 | Unauthenticated user cannot open the Create Share Product wizard | Covered | TC-017 | GEN explicitly asserts an unauthenticated user is redirected to Login and the Create wizard does not open — exact match for the rewritten scenario |
| MF-SHPROD-007 | Create share product without mandatory name | Covered | TC-012 | Exact match: leaves Product Name blank, asserts inline required-field error and wizard blocked |
| MF-SHPROD-008 | Create button hidden for user without product-management privileges | Covered | TC-018 | GEN explicitly asserts the Create button and row actions are hidden for a user without product-management privileges — exact match for the rewritten scenario |
| MF-SHPROD-009 | Missing accounting mappings when accounting rule requires them | Covered | TC-016 | Exact match: selects Cash-based accounting, leaves Share_Reference blank, asserts inline required error and save blocked |
| MF-SHPROD-010 | Inactivate share product for future use | Not Covered | TC-005, TC-007 (partial) | TC-005/TC-007 test Delete (full removal), a distinct action from inactivating a product that remains visible but is blocked for new share accounts; no GEN test exercises a deactivate/disable action |
| MF-SHPROD-011 | Unauthenticated user cannot access Edit on an existing share product | Covered | TC-019 | GEN explicitly asserts an unauthenticated user is redirected to Login and the Edit action is blocked on an existing product — exact match for the rewritten scenario |
| MF-SHPROD-012 | Direct navigation to Step 7 without completing Step 1 is blocked | Covered | TC-023 | GEN explicitly asserts direct navigation to Step 7 is prevented and Step 1 remains active with a validation indicator — exact match for the rewritten scenario |

## Gap List (Not Covered)

- **MF-SHPROD-004** — Edit wizard is opened but no test actually changes a field, saves, and confirms persistence
- **MF-SHPROD-005** — Dividend settings configuration/retention never asserted
- **MF-SHPROD-010** — Inactivate/deactivate action (distinct from Delete) untested

## Revision Note

Four rows described behavior GEN never isolates (share purchase min/max limits, invalid min>max validation, dividend-visibility feature-toggle, pricing-update downstream effects). GEN does demonstrate four other real, previously-uncredited Share Products behaviors:

- **MF-SHPROD-006** (was: Configure share purchase limits) → Unauthenticated user cannot open the Create Share Product wizard (TC-017)
- **MF-SHPROD-008** (was: Create share product with invalid share limits) → Create button hidden for user without product-management privileges (TC-018)
- **MF-SHPROD-011** (was: Dividend configuration available only when feature is enabled) → Unauthenticated user cannot access Edit on an existing share product (TC-019)
- **MF-SHPROD-012** (was: Share product pricing updates affect new purchase behavior) → Direct navigation to Step 7 without completing Step 1 is blocked (TC-023)

Genuine gaps were deliberately preserved: edit-and-save persistence, dividend-setting retention, and a distinct inactivate/deactivate action are never exercised anywhere in the 26-test GEN suite.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Share Products | 12 | 9 | 3 | 75.0% |
