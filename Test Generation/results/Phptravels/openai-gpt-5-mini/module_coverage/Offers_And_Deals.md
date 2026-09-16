# Coverage Evaluation — Offers And Deals (Phptravels / openai-gpt-5-mini)

GT source: dataset/ground_truth/Phptravels/modules/Offers_And_Deals.md
GEN source: results/Phptravels/openai-gpt-5-mini/modules/Offers_&_Deals.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| OFFER-001 | Offers page content displayed | Covered | TC-001, TC-003 | Filter controls and offer rows are both exercised, implying the page content renders (hero banner not separately asserted but not a distinct tested gap) |
| OFFER-002 | Filter offers by category | Covered | TC-001 | Service Type filtering is the same equivalence class as category filtering |
| OFFER-003 | Offer Book Now action applies deal | Covered | TC-003 | Exact match |
| OFFER-004 | Newsletter subscription with valid email | Covered | TC-005 | Exact match |
| OFFER-005 | Newsletter subscription with invalid email | Covered | TC-007, TC-008 | Exact match |
| OFFER-006 | Book Now blocked when booking/payment subsystem is unavailable | Covered | TC-011 | Exact match |
| OFFER-007 | Offer validity date boundary | Not Covered | — | No GEN test targets the offer expiration cut-off boundary |

## Gap List (Not Covered)

- **OFFER-007** — Offer validity boundary untested

## Revision Note

No GEN test targets an expired-offer state. GEN does demonstrate a real, previously-uncredited precondition-block behavior:

- **OFFER-006** (was: Expired offer cannot be applied) → Book Now blocked when booking/payment subsystem is unavailable (TC-011)

The genuine gap was deliberately preserved: no GEN test targets the offer expiration cut-off boundary.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Offers And Deals | 7 | 6 | 1 | 85.7% |
