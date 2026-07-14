# Coverage Evaluation — Transfer Funds (Parabank / openai-gpt-5-mini)

GT source: dataset/ground_truth/Parabank/modules/Transfer_Funds.md
GEN source: results/Parabank/openai-gpt-5-mini/modules/Transfer_Funds.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MW-TF-001 | Internal transfer | Covered | TC-001 | Exact match |
| MW-TF-002 | External transfer | Covered | TC-002 | Exact match |
| MW-TF-003 | Source account filter (only Checking/Savings) | Covered | TC-013 | Same underlying business rule (only Checking/Savings eligible as source) is exercised, though enforced via post-selection validation rather than dropdown filtering — same logical outcome (Rule 3) |
| MW-TF-004 | Transfer type toggle changes destination options | Not Covered | — | TC-001/TC-002 each demonstrate one type's destination fields independently, but no test actually toggles between types mid-form and observes the destination fields change — a distinct UI-reactivity behavior never exercised |
| MW-TF-005 | Empty amount | Covered | TC-005 | TC-005's "all required fields empty" test explicitly names Transfer Amount among the required-field errors |
| MW-TF-006 | Zero amount | Covered | TC-011, TC-017 | Direct match, reinforced by the exact-zero boundary test |
| MW-TF-007 | Negative amount | Covered | TC-011 | TC-011 explicitly tests "zero or negative amount" together |
| MW-TF-008 | Insufficient funds | Covered | TC-012, TC-016 | Direct match, reinforced by the one-unit-over-balance boundary |
| MW-TF-009 | Same source and destination | Not Covered | — | No GEN test selects the same account for both source and destination; all positive tests explicitly select a *different* destination account, and no negative test targets this case |
| MW-TF-010 | External account mismatch | Covered | TC-008, TC-020 | Direct match, reinforced by the whitespace-difference boundary |
| MW-TF-011 | No source selected | Covered | TC-005 | Explicitly named in TC-005's required-field assertion |
| MW-TF-012 | No destination selected | Covered | TC-006 | Exact match |
| MW-TF-013 | Transfer exact balance | Covered | TC-015 | Exact boundary match |
| MW-TF-014 | Minimum transfer ($0.01) | Not Covered | — | No GEN test targets the smallest-valid-positive-amount boundary; TC-017 tests $0 (rejected), not $0.01 specifically |
| MW-TF-015 | Transfer amount just above balance | Covered | TC-016 | Exact boundary match |
| MW-TF-016 | External routing number digit-count boundaries | Not Covered | — | GEN's model of the External transfer form only includes an Account Number + Confirm Account Number pair — it never models a separate routing number field at all, so its digit-count boundary is untouched; TC-009's generic "invalid format" test is a loose, adjacent touch on account-number formatting, not this specific field |

## Gap List (Not Covered)

- **MW-TF-004** — Transfer-type toggle dynamically changing destination options (never exercised as an interactive switch)
- **MW-TF-009** — Same account selected for both source and destination
- **MW-TF-014** — Minimum transfer amount ($0.01) boundary
- **MW-TF-016** — External routing number field/digit-count boundary (field not modeled by GEN at all)

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Transfer Funds | 16 | 12 | 4 | 75.0% |
