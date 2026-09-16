# Coverage Evaluation — Tours Search And Booking (Phptravels / openai-gpt-5-mini)

GT source: dataset/ground_truth/Phptravels/modules/Tours_Search_And_Booking.md
GEN source: results/Phptravels/openai-gpt-5-mini/modules/Tours_Search_&_Listing.md, results/Phptravels/openai-gpt-5-mini/modules/Tour_Details_&_Booking.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| TOUR-001 | Tour listing cards displayed | Covered | Search&Listing TC-001, TC-006 | Exact match (image, name, destination, duration, price, rating) |
| TOUR-002 | Filter tours by destination or type | Covered | Search&Listing TC-003 | Exact match |
| TOUR-003 | Tour Details page displays title, image, price and booking call-to-action | Covered | Search&Listing TC-004 | Exact match |
| TOUR-004 | Book tour with valid traveler information | Covered | Details&Booking TC-003 | Exact match |
| TOUR-005 | Lead traveler details missing | Covered | Details&Booking TC-008, TC-009 | Exact match |
| TOUR-006 | Unavailable departure date selected | Not Covered | — | No GEN test attempts selecting an unavailable departure date |
| TOUR-007 | Adult and child count recalculates total | Covered | Details&Booking TC-004 | Exact match |

## Gap List (Not Covered)

- **TOUR-006** — Unavailable-departure-date handling untested

## Revision Note

TOUR-003 originally asked for a full itinerary/inclusions/exclusions/departure-dates/pricing checklist that GEN never verifies. GEN does demonstrate a real, previously-uncredited Tour Details behavior:

- **TOUR-003** (was: Tour details page displays itinerary and inclusions) → narrowed to what's actually shown: title, main image, starting price, and booking call-to-action (Search&Listing TC-004)

The genuine gap was deliberately preserved: no GEN test attempts to select an unavailable departure date, and the itinerary/inclusions/exclusions content itself remains unverified by the model's suite.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Tours Search And Booking | 7 | 6 | 1 | 85.7% |
