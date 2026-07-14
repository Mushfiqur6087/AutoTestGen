# Coverage Evaluation — Investments (Parabank / openai-gpt-5-mini)

GT source: dataset/ground_truth/Parabank/modules/Investments.md
GEN source: results/Parabank/openai-gpt-5-mini/modules/Investments.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MW-INV-001 | View portfolio snapshot (holdings, market value, unrealized gain/loss) | Not Covered *(was Partially Covered → resolved Not Covered)* | TC-001, TC-002 (partial) | TC-001/TC-002 only assert the portfolio panel updates as a side-effect after executing a trade (quantity/market value visible); no test ever asserts "unrealized gain/loss" is displayed, and no test views the snapshot as a standalone read-only check — a distinct, never-asserted data field |
| MW-INV-002 | Buy funds | Covered | TC-001 | Exact match: Buy action, symbol, quantity, funding account, execute → success with order ID |
| MW-INV-003 | Sell funds | Covered | TC-002 | Exact match: Sell action, symbol, quantity ≤ owned, destination account, submit → success |
| MW-INV-004 | Fund symbol autocomplete | Covered | TC-001, TC-002, TC-003, TC-024 | TC-001–003 steps require entering a symbol into "the Fund Symbol autocomplete and select the matching result," implying suggestions appear; TC-024 exercises the no-suggestions boundary for an invalid input, confirming the same mechanism |
| MW-INV-005 | Invalid fund symbol | Covered | TC-024 | TC-024 enters a non-matching symbol and asserts a visible "symbol does not exist" / no-results validation error — same logical path as GT (fixture/data differs: long string vs. plain non-existent symbol, ignorable per Rule 3) |
| MW-INV-006 | Zero quantity | Covered | TC-017 | Exact boundary match: quantity = 0 → inline error "must be greater than 0" |
| MW-INV-007 | Insufficient buying power | Covered | TC-009 | Exact match |
| MW-INV-008 | Sell more than owned | Covered | TC-010, TC-019 | TC-010 is the direct match; TC-019 reinforces with the one-unit-over boundary |
| MW-INV-009 | Create weekly plan | Covered | TC-003, TC-020, TC-022 | Frequency dropdown steps explicitly name "Weekly or Monthly" as the selectable option exercised — same equivalence class (Rule 6), both frequencies are within the tested path |
| MW-INV-010 | Create monthly plan | Covered | TC-003, TC-020, TC-022 | Same reasoning as MW-INV-009 |
| MW-INV-011 | Past start date | Covered | TC-012 | Exact match, identical error message asserted |
| MW-INV-012 | Below minimum contribution | Covered | TC-013, TC-023 | TC-013 direct match; TC-023 reinforces with the one-unit-below boundary |
| MW-INV-013 | Insufficient funding balance | Covered | TC-014 | Exact match |
| MW-INV-014 | Start date exactly today | Covered | TC-021 | GT's expected result is stated loosely ("handled based on cutoff rules"); TC-021 exercises this exact boundary and asserts a concrete blocked outcome, a valid instance of "handled" |
| MW-INV-015 | Sell exact total shares owned | Covered | TC-018 | TC-018 tests quantity = entire share balance → success; balance-reaches-zero is the direct implication of selling 100% of holdings |

## Gap List (Not Covered)

- **MW-INV-001** — Standalone portfolio snapshot view; specifically, "unrealized gain/loss" is never asserted anywhere in the GEN suite

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Investments | 15 | 14 | 1 | 93.3% |
