# Coverage Evaluation — Accounting Rules & Financial Activity Mappings (Mifos / openai-gpt-5-mini)

GT source: dataset/ground_truth/Mifos/modules/Accounting_Rules_&_Financial_Activity_Mappings.md
GEN source: results/Mifos/openai-gpt-5-mini/modules/Accounting_Rules_&_Financial_Activity_Mappings.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MF-FAM-001 | View financial activity mappings | Covered | TC-005, TC-006 | TC-005 shows a new mapping row appearing in the Financial Activity Mappings table; TC-006 explicitly navigates to that page and inspects the table/dropdown — confirms existing mappings are displayed. |
| MF-FAM-002 | Create or update financial activity to GL mapping | Covered | TC-005 | TC-005 selects an unmapped Financial Activity and a GL Account and submits, asserting the mapping is saved and visible — covers the "create" branch of this create-or-update scenario. |
| MF-FAM-003 | View accounting rules configuration | Covered | TC-001 | TC-001 navigates to the Accounting Rules page and opens an existing rule from the table, confirming configured rules are listed and viewable. |
| MF-FAM-004 | Edit accounting rule setting | Covered | TC-003 | TC-003 opens an existing rule, changes the Rule Name and/or a checkbox, saves, and asserts the Rule Detail view reflects the updated values. |
| MF-FAM-005 | Save mapping without required GL account | Covered | TC-008 | TC-008 leaves GL_Account blank when creating a mapping and asserts an inline required-field validation error blocks submission. |
| MF-FAM-006 | Map financial activity to invalid or incompatible GL account | Not Covered | — | GEN's only mapping-negative test (TC-009) covers re-mapping an already-mapped activity, not selecting a GL account of an incompatible type/classification; no test exercises GL-account-type compatibility validation. |
| MF-FAM-008 | Product/account posting uses configured financial activity mapping | Not Covered | — | No GEN test performs a linked transaction and verifies the resulting journal entries use the mapped GL account; this suite only covers mapping CRUD. |
| MF-FAM-009 | Updating mapping affects future transactions without corrupting historical entries | Not Covered | — | No GEN test changes a mapping and then compares historical vs. new transaction postings. |
| MF-FAM-010 | Accounting rules visible state matches enabled features | Not Covered | — | No GEN test varies feature-enablement state and checks that only relevant accounting rules/settings are shown and editable. |

## Gap List (Not Covered)

- **MF-FAM-006** — No test maps a Financial Activity to a GL account of an incompatible type/classification.
- **MF-FAM-008** — No test verifies actual transaction posting uses the configured mapped GL account.
- **MF-FAM-009** — No test verifies historical entries remain unaffected after a mapping update.
- **MF-FAM-010** — No test verifies accounting-rule visibility tracks enabled/disabled features.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Accounting Rules & Financial Activity Mappings | 9 | 5 | 4 | 55.6% |
