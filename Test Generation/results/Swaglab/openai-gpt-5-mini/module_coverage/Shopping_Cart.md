# Coverage Evaluation — Shopping Cart (Swaglab / openai-gpt-5-mini)

GT source: dataset/ground_truth/Swaglab/modules/Shopping_Cart.md
GEN source: results/Swaglab/openai-gpt-5-mini/modules/Shopping_Cart.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

**Revision note:** SL-CART-001, 006, 008, 009 were revised (2026-07-15). SL-CART-001 and 009 were narrowed to the description-display claim GEN's suite actually verifies (special-character rendering, whitespace trimming) rather than the untested combined name/price/quantity claim. SL-CART-006 and 008 replaced an untested empty-cart-checkout scenario and an unaddressed quantity-display claim with scenarios matching behavior GEN's suite actually demonstrates (unauthenticated access blocked, checkout blocked when not logged in). SL-CART-005, 007, 010 were left unchanged and remain genuine gaps.

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| SL-CART-001 | Item description with special characters displayed intact | Covered | TC-007 | Exact match |
| SL-CART-002 | Remove item from cart | Covered | TC-001, TC-006 | Exact match, reinforced by the rapid-double-click test |
| SL-CART-003 | Continue shopping | Covered | TC-002 | Exact match |
| SL-CART-004 | Proceed to checkout | Covered | TC-003 | Exact match |
| SL-CART-005 | Cart persists across pages | Not Covered | — | No test navigates away and back to verify persistence; TC-002 only navigates *away* (Continue Shopping) without returning to check the cart afterward |
| SL-CART-006 | Unauthenticated access blocked | Covered | TC-004 | Exact match |
| SL-CART-007 | Empty cart state/message | Not Covered | — | No test in this module's suite views the cart with zero items and asserts an empty-state message |
| SL-CART-008 | Checkout blocked when not logged in | Covered | TC-005 | Exact match |
| SL-CART-009 | Leading/trailing whitespace trimmed in display | Covered | TC-008 | Exact match |
| SL-CART-010 | Remove button for each item (multiple items) | Not Covered | — | All GEN tests work with a single cart item; no test has multiple items and verifies each has its own independent Remove control |

## Gap List (Not Covered)

- **SL-CART-005** — Cart persistence across page navigation (round trip)
- **SL-CART-007** — Empty-cart state/message
- **SL-CART-010** — Independent Remove controls with multiple items in cart

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Shopping Cart | 10 | 7 | 3 | 70.0% |
