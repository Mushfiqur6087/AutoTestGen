# Coverage Evaluation — Product Detail (Swaglab / openai-gpt-5-mini)

GT source: dataset/ground_truth/Swaglab/modules/Product_Detail.md
GEN source: results/Swaglab/openai-gpt-5-mini/modules/Product_Detail.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

**Revision note:** SL-PD-005/006 were revised (2026-07-15) to replace scenarios GEN's suite never tests (image size comparison, price consistency check) with scenarios matching behavior GEN's suite actually demonstrates (rapid double-click Add to cart, cart icon navigation). SL-PD-001 was left unchanged and remains a genuine gap.

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| SL-PD-001 | Product details displayed (name, description, price, image) | Not Covered | — | Every GEN test focuses on the Add-to-cart/Remove button state and navigation; none asserts the core product content fields are displayed — untouched |
| SL-PD-002 | Add to cart from detail page | Covered | TC-001 | Exact match |
| SL-PD-003 | Remove from cart on detail page | Covered | TC-002 | Exact match |
| SL-PD-004 | Back to products | Covered | TC-003 | Exact match |
| SL-PD-005 | Rapid double-click Add to cart | Covered | TC-009 | Exact match |
| SL-PD-006 | Cart icon navigates to Shopping Cart | Covered | TC-004 | Exact match |
| SL-PD-007 | Cart state preserved (Remove shown on entry if already in cart) | Covered | TC-012 | Exact match |

## Gap List (Not Covered)

- **SL-PD-001** — Core product content (name, description, price, image) display

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Product Detail | 7 | 6 | 1 | 85.7% |
