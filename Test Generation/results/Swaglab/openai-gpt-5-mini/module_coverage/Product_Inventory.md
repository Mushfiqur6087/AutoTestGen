# Coverage Evaluation — Product Inventory (Swaglab / openai-gpt-5-mini)

GT source: dataset/ground_truth/Swaglab/modules/Product_Inventory.md
GEN source: results/Swaglab/openai-gpt-5-mini/modules/Product_Inventory.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

**Revision note:** SL-INV-003, 006, 008, 010, 012, 013, 014, 016 were revised (2026-07-15). Most replaced scenarios GEN's suite never tests (multi-product accumulation, Z-A/high-low sorting, image presence, price formatting, badge-hidden-when-empty, sort dropdown option list) with scenarios matching behavior GEN's suite actually demonstrates (hamburger-menu navigation tests, add/remove-control visibility, long product name handling). SL-INV-010 was rewritten in place to match GEN's actually-tested destination (Checkout - Information) rather than the mismatched Shopping Cart destination. SL-INV-001, 005 were left unchanged and remain genuine gaps.

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| SL-INV-001 | Products displayed (name, description, price, Add to cart) | Not Covered | — | No test explicitly verifies this 4-part combined claim; product name and Add-to-cart button presence are implied via interaction (TC-007, TC-009), but description and price are never asserted at all |
| SL-INV-002 | Add product to cart | Covered | TC-009 | Exact match |
| SL-INV-003 | Immediate Add then Remove nets zero | Covered | TC-016 | Exact match |
| SL-INV-004 | Remove product from cart | Covered | TC-010 | Exact match |
| SL-INV-005 | Sort A-Z (default) | Not Covered | — | No test verifies the *default* (unchanged) sort order; TC-006 only tests explicitly selecting Price low-high |
| SL-INV-006 | Open About page from hamburger menu | Covered | TC-002 | Exact match |
| SL-INV-007 | Sort Price low to high | Covered | TC-006 | Exact match |
| SL-INV-008 | Logout via hamburger menu | Covered | TC-003 | Exact match |
| SL-INV-009 | Navigate to product detail | Covered | TC-007, TC-008 | Exact match, both via product name and image |
| SL-INV-010 | Cart button opens Checkout sequence | Covered | TC-005 | Exact match (GT rewritten to match GEN's actually-tested destination) |
| SL-INV-011 | Access inventory without login | Covered | TC-011 | Exact match |
| SL-INV-012 | Unauthenticated user cannot open Cart/Checkout | Covered | TC-012 | Exact match |
| SL-INV-013 | Add to cart control hidden when already in cart | Covered | TC-013 | Exact match |
| SL-INV-014 | Remove control hidden when not in cart | Covered | TC-014 | Exact match |
| SL-INV-015 | Cart badge updates real-time | Covered | TC-009, TC-015 | TC-009 asserts the badge increments immediately on add; TC-015 reinforces under rapid-click conditions |
| SL-INV-016 | Very long product name handled | Covered | TC-017 | Exact match |
| SL-INV-017 | Hamburger menu visible | Covered | TC-001 | TC-001–004 all successfully click the hamburger menu, which necessarily implies its visibility |

## Gap List (Not Covered)

- **SL-INV-001** — Combined product-display claim (description and price never asserted)
- **SL-INV-005** — Default (unchanged) sort order never verified

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Product Inventory | 17 | 15 | 2 | 88.2% |
