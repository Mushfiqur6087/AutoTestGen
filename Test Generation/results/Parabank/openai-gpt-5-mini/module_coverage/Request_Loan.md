# Coverage Evaluation — Request Loan (Parabank / openai-gpt-5-mini)

GT source: dataset/ground_truth/Parabank/modules/Request_Loan.md
GEN source: results/Parabank/openai-gpt-5-mini/modules/Request_Loan.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria, incl. Rule 6 N-field/entity equivalence)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MW-RL-001 | Personal loan approved | Covered | TC-001 | Exact match |
| MW-RL-002 | Auto loan approved | Covered | TC-003 | Exact match |
| MW-RL-003 | Home loan approved | Covered | TC-004 | Exact match |
| MW-RL-004 | Loan type cards show APR/ranges | Not Covered | — | No GEN test asserts the cards' specific APR percentages or ranges are displayed — untouched content-verification check |
| MW-RL-005 | Personal loan below minimum | Covered | TC-006, TC-016 | Direct match, reinforced by the one-unit-below boundary |
| MW-RL-006 | Personal loan above maximum | Covered | TC-007 (equivalence) | No test hardcodes a Personal amount above $50,000, but the identical "amount exceeds type maximum → rejected" mechanism is directly proven for Auto (TC-007), and the range-validation pattern is independently proven for minimum on all three loan types — same equivalence class (Rule 6), same parameterized logic, different entity |
| MW-RL-007 | Auto loan below minimum | Covered | TC-018 | Exact boundary match: 4999 (one below Auto's 5000 minimum) blocked |
| MW-RL-008 | Auto loan above maximum | Covered | TC-007 | Exact match |
| MW-RL-009 | Home loan below minimum | Covered | TC-020 | Exact boundary match: 49999 (one below Home's 50000 minimum) blocked |
| MW-RL-010 | Home loan above maximum | Covered | TC-007 (equivalence) | Same reasoning as MW-RL-006 — maximum-rejection mechanism proven via Auto, minimum proven directly for Home |
| MW-RL-011 | Down payment >= loan | Covered | TC-010 | Exact match |
| MW-RL-012 | Insufficient collateral (< 20%) | Covered | TC-012, TC-024 | Direct match, reinforced by the one-unit-below-20% boundary |
| MW-RL-013 | Down payment < 10% | Covered | TC-009, TC-022 | Direct match, reinforced by the one-unit-below-10% boundary |
| MW-RL-014 | No loan type selected | Covered | TC-014 | TC-014's "all fields empty" test explicitly names Loan Type among the fields asserted to show a required-field error |
| MW-RL-015 | No collateral account | Covered | TC-014 | Same test explicitly names Collateral Account among the required-field errors |
| MW-RL-016 | Exact minimum Personal ($1,000) | Covered | TC-015 | Exact boundary match |
| MW-RL-017 | Exact maximum Personal ($50,000) | Covered | TC-002 | TC-002 is explicitly designed to test "the lower or upper bound within 1000-50000" — the upper-bound instantiation directly targets this exact boundary (Rule 3 fixture agnosticism) |
| MW-RL-018 | Exactly 10% down payment | Covered | TC-021 | Exact boundary match |
| MW-RL-019 | Non-numeric loan amount | Covered | TC-013 | Exact match |
| MW-RL-020 | Down payment exactly one cent below 10% | Covered | TC-022 | Exact boundary match |

## Gap List (Not Covered)

- **MW-RL-004** — Loan type cards' specific APR percentages and amount ranges are never asserted

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Request Loan | 20 | 19 | 1 | 95.0% |
