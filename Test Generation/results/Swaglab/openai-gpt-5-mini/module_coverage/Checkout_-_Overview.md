# Coverage Evaluation — Checkout - Overview (Swaglab / openai-gpt-5-mini)

GT source: dataset/ground_truth/Swaglab/modules/Checkout_-_Overview.md
GEN source: results/Swaglab/openai-gpt-5-mini/modules/Checkout_-_Overview.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

**Revision note:** SL-CHK2-001, 002, 006, 007, 008 were revised (2026-07-15). SL-CHK2-001/002/007/008 replaced scenarios GEN's suite never tests (item list display, specific payment/shipping text) with scenarios matching behavior GEN's suite actually demonstrates (unauthenticated access, empty-cart Finish block, rapid double-click Finish, browser Back after Finish). SL-CHK2-006 was rewritten in place to match GEN's actual tested destination (Shopping Cart) rather than the mismatched Inventory destination. SL-CHK2-003 and 004 were left unchanged — the "totals displayed but never verified for correctness" finding remains a genuine, distinctive gap.

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| SL-CHK2-001 | Unauthenticated access blocked | Covered | TC-003 | Exact match |
| SL-CHK2-002 | Finish blocked with empty cart | Covered | TC-004 | Exact match |
| SL-CHK2-003 | Tax calculated (typically 8%) | Not Covered | — | Tax is asserted as displayed, never verified as correctly calculated |
| SL-CHK2-004 | Total correct (Item Total + Tax) | Not Covered | — | Total is asserted as displayed and consistent across pages (TC-001), never verified as the correct sum |
| SL-CHK2-005 | Finish purchase | Covered | TC-001 | Exact match |
| SL-CHK2-006 | Cancel from overview returns to Shopping Cart | Covered | TC-002 | Exact match (GT rewritten to match GEN's actually-tested destination) |
| SL-CHK2-007 | Rapid double-click Finish | Covered | TC-006 | Exact match |
| SL-CHK2-008 | Browser Back after Finish | Covered | TC-007 | Exact match |
| SL-CHK2-009 | Price breakdown clearly labeled | Covered | TC-001 | TC-001 explicitly verifies Item total, Tax, and Total are displayed — functionally the same claim as "clearly labeled" |

## Gap List (Not Covered)

- **SL-CHK2-003, 004** — Neither total figure is verified for *correctness*, only for being displayed/consistent across pages — a recurring superficial-test pattern in this module

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Checkout - Overview | 9 | 7 | 2 | 77.8% |
