# Coverage Evaluation — Checkout - Confirmation (Swaglab / openai-gpt-5-mini)

GT source: dataset/ground_truth/Swaglab/modules/Checkout_-_Confirmation.md
GEN source: results/Swaglab/openai-gpt-5-mini/modules/Checkout_-_Confirmation.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

**Revision note:** SL-CHK3-004/005 were revised (2026-07-15) to replace scenarios GEN's suite never tests (success image, dispatch message) with scenarios matching behavior GEN's suite actually demonstrates (checkout-not-completed blocks Confirmation access, Back Home then add item updates cart). SL-CHK3-001 was left unchanged and remains a genuine gap.

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| SL-CHK3-001 | Confirmation displayed after completing checkout | Not Covered | — | Every GEN test in this module treats "confirmation message displayed" as a given *precondition*, never as the asserted *result* of completing checkout — per the anti-pattern note, a passing precondition doesn't count as coverage of the behavior it's a precondition for. The actual checkout-completion action belongs to the Checkout - Overview module, out of scope here |
| SL-CHK3-002 | Cart cleared after order | Covered | TC-001, TC-004 | Both explicitly assert the cart shows an empty state (no items, no badge count) after the order — same underlying rule, verified via the post-Back-Home Inventory view rather than a direct cart view (Rule 3) |
| SL-CHK3-003 | Back to products | Covered | TC-001 | Exact match: Back Home returns to Product Inventory |
| SL-CHK3-004 | Confirmation blocked if checkout not completed | Covered | TC-003 | Exact match |
| SL-CHK3-005 | Back Home then add item updates cart | Covered | TC-007 | Exact match |

## Gap List (Not Covered)

- **SL-CHK3-001** — Confirmation message as an asserted *result* of completing checkout (only ever assumed as a precondition in this module's suite)

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Checkout - Confirmation | 5 | 4 | 1 | 80.0% |
