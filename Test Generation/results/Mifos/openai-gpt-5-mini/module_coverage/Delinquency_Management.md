# Coverage Evaluation — Delinquency Management (Mifos / openai-gpt-5-mini)

GT source: dataset/ground_truth/Mifos/modules/Delinquency_Management.md
GEN source: results/Mifos/openai-gpt-5-mini/modules/Delinquency_Management.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MF-DELINQ-001 | View delinquency buckets or ranges | Covered | TC-001, TC-003 | TC-001/TC-003 navigate to the Ranges/Buckets pages and click an existing row's link, presupposing and exercising the list being rendered (Rule 7: specific action implies the general list view) |
| MF-DELINQ-002 | Create delinquency bucket successfully | Covered | TC-004 | Direct match: Bucket Name entered, ranges added via Add Row, Create clicked, new row appears in the Buckets table |
| MF-DELINQ-003 | Create a delinquency range independently of a bucket, specifying Minimum and Maximum Age Days | Covered | TC-002 | Revised scenario; TC-002 directly creates a standalone Delinquency Range (distinct entity from a Bucket) entering Classification, Minimum and Maximum Age Days, and asserts the new row appears with those values |
| MF-DELINQ-004 | View delinquent loans grouped by bucket | Not Covered | — | GEN is scoped entirely to Ranges/Buckets configuration; no test views delinquent loans or their bucket categorization |
| MF-DELINQ-005 | Delinquency bucket creation is blocked when no Loan Products exist to link to | Covered | TC-011 | Revised (narrowed) scenario; TC-011 directly asserts bucket creation is blocked with a visible error when no Loan Products exist to link to, which is the loan-product-linkage behavior GEN actually demonstrates |
| MF-DELINQ-006 | Create bucket with overlapping ranges | Not Covered | — | No GEN test constructs overlapping min/max ranges within a bucket or across ranges |
| MF-DELINQ-007 | Create bucket with invalid min/max range | Covered | TC-018 | TC-018 enters Minimum_Age_Days greater than Maximum_Age_Days and asserts submission is blocked with an inline validation error — same min/max boundary rule and equivalence class regardless of "bucket" vs "range" wording |
| MF-DELINQ-008 | Delinquency Bucket creation is blocked for users lacking configuration/admin privileges | Covered | TC-010 | Revised scenario; TC-010 directly asserts creation is blocked with a visible authorization error when the user lacks configuration/admin privileges — a real business-rule block, matching the "business rule blocks unsafe change" spirit of the original row |
| MF-DELINQ-009 | Create delinquency range with boundary configurations: open-ended Maximum Age Days and single-day range where Maximum equals Minimum | Covered | TC-012, TC-013 | Revised scenario; TC-012 creates a range with Maximum Age Days left blank (open-ended) and TC-013 creates a range where Maximum equals Minimum (single-day range) — both boundary creations succeed exactly as described |
| MF-DELINQ-010 | Create delinquency range and bucket with very long text and special characters/emoji in name fields | Covered | TC-016, TC-017 | Revised scenario; TC-016 enters 200+ character strings in Classification and Bucket Name and asserts no truncation, TC-017 enters special characters/emoji in Classification and Range Label and asserts verbatim display — jointly satisfy the revised row |

## Gap List (Not Covered)

- **MF-DELINQ-004** — Viewing delinquent loans grouped by bucket is never tested; GEN never leaves the Ranges/Buckets configuration screens to view actual loan records
- **MF-DELINQ-006** — Overlapping range validation is never tested; no GEN test constructs two ranges/rows with overlapping min/max boundaries

## Revision Note

Five rows described bucket/loan lifecycle behaviors GEN never exercises (editing an existing bucket, saving a product-side classification link, business-rule-blocked delete/disable, repayment-driven recategorization, write-off removal from the delinquency population — GEN never touches loan records or edit flows, only Range/Bucket creation and viewing). GEN does demonstrate five other real, previously-uncited behaviors:

- **MF-DELINQ-003** (was: Edit delinquency bucket) → Creating a standalone Delinquency Range, a distinct entity/flow from Bucket creation (TC-002)
- **MF-DELINQ-005** (was: Configure delinquency classification linked to loan product) → narrowed to: Bucket creation is blocked when no Loan Products exist to link to (TC-011)
- **MF-DELINQ-008** (was: Delete or disable bucket in active use) → Bucket creation is blocked for users lacking configuration/admin privileges — a genuine business-rule block (TC-010)
- **MF-DELINQ-009** (was: Delinquency categorization updates after repayment) → Range creation supports open-ended and single-day boundary configurations (TC-012, TC-013)
- **MF-DELINQ-010** (was: Write-off/closure removes loan from population) → Range/Bucket creation handles very long text and special characters/emoji in name fields (TC-016, TC-017)

Genuine gaps were deliberately preserved: GEN never views delinquent loans grouped by bucket (MF-DELINQ-004), and never constructs overlapping ranges (MF-DELINQ-006) — both require behavior entirely absent from the GEN suite.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Delinquency Management | 10 | 8 | 2 | 80.0% |
