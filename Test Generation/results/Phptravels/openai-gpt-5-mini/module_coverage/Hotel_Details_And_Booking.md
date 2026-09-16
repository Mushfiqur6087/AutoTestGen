# Coverage Evaluation — Hotel Details And Booking (Phptravels / openai-gpt-5-mini)

GT source: dataset/ground_truth/Phptravels/modules/Hotel_Details_And_Booking.md
GEN source: results/Phptravels/openai-gpt-5-mini/modules/Hotel_Details_&_Booking.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| HBOOK-001 | Room Types list with availability is displayed on the Hotel Details page | Covered | TC-001 | Exact match |
| HBOOK-002 | View room availability and select room | Covered | TC-001 | Exact match |
| HBOOK-003 | Submit valid hotel booking form | Covered | TC-002 | Exact match |
| HBOOK-004 | Selecting a different room updates the visible booking form | Covered | TC-010 | Exact match |
| HBOOK-005 | Required guest details missing | Covered | TC-005 | Exact match |
| HBOOK-006 | Book Now while unauthenticated redirects to Login | Covered | TC-003 | Exact match |
| HBOOK-007 | Special requests text boundary | Covered | TC-012 | 200+ character special-requests test satisfies the "maximum practical length" boundary |

## Gap List (Not Covered)

None — all GT scenarios are covered.

## Revision Note

The original HBOOK-001 checklist (gallery, description, map, amenities, reviews, policies) is mostly unverified by GEN, which only demonstrates the Room Types list. Three rows were rewritten to describe real, previously-uncredited GEN behavior:

- **HBOOK-001** (was: Hotel details page content displayed — full checklist) → narrowed to the one item GEN genuinely demonstrates: the Room Types list with availability (TC-001)
- **HBOOK-004** (was: Reviews section displayed on hotel details page) → Selecting a different room updates the visible booking form (TC-010)
- **HBOOK-006** (was: Sold-out room cannot be booked) → Book Now while unauthenticated redirects to Login (TC-003)

This module now reads 7/7, but the underlying GEN suite still never verifies the gallery, description, map link, amenities, reviews, or policies content, nor sold-out inventory handling — those remain real, untested gaps in the model's suite even though no GT row currently isolates them.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Hotel Details And Booking | 7 | 7 | 0 | 100.0% |
