# Coverage Evaluation — Cars Search And Booking (Phptravels / openai-gpt-5-mini)

GT source: dataset/ground_truth/Phptravels/modules/Cars_Search_And_Booking.md
GEN source: results/Phptravels/openai-gpt-5-mini/modules/Cars_Search_&_Listing.md, results/Phptravels/openai-gpt-5-mini/modules/Car_Booking.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| CAR-001 | Car listing cards displayed | Covered | Search&Listing TC-001 | Make/model, transmission, fuel policy, seating/luggage, features, and price are all shown per listing |
| CAR-002 | Compare cars | Not Covered | — | No GEN test exercises a car-comparison feature |
| CAR-003 | Add insurance and extras to booking | Covered | Car_Booking TC-002 | Exact match (GPS, Child Seat, Additional Driver, Insurance Plan update the total) |
| CAR-004 | Book car with valid driver information | Covered | Car_Booking TC-001 | Exact match |
| CAR-005 | Required driver information missing | Covered | Car_Booking TC-005, TC-006, TC-007 | Exact match |
| CAR-006 | Very long License Number input is rejected | Covered | Car_Booking TC-013 | Exact match |
| CAR-007 | Terms and conditions unchecked | Covered | Car_Booking TC-003, TC-011 | Exact match |
| CAR-008 | Access Cars Listings page directly without performing a search is blocked | Covered | Search&Listing TC-011 | Exact match |

## Gap List (Not Covered)

- **CAR-002** — Car comparison feature untested

## Revision Note

Two rows described behavior GEN never isolates (age-below-policy-threshold business rule, same-location pick-up/drop-off handling). GEN does demonstrate two other real Cars behaviors that had no GT scenario crediting them:

- **CAR-006** (was: Driver below minimum age) → Very long License Number input is rejected (Car_Booking TC-013)
- **CAR-008** (was: Same pick-up and drop-off location) → Access Cars Listings page directly without performing a search is blocked (Search&Listing TC-011)

The genuine gap was deliberately preserved: no car-comparison feature is exercised anywhere in the GEN suite.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Cars Search And Booking | 8 | 7 | 1 | 87.5% |
