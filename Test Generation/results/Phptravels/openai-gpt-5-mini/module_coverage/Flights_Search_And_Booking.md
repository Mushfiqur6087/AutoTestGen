# Coverage Evaluation — Flights Search And Booking (Phptravels / openai-gpt-5-mini)

GT source: dataset/ground_truth/Phptravels/modules/Flights_Search_And_Booking.md
GEN source: results/Phptravels/openai-gpt-5-mini/modules/Flights_Search_&_Listing.md, results/Phptravels/openai-gpt-5-mini/modules/Flight_Booking.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| FLIGHT-001 | Flight listing displays itinerary cards | Covered | Search&Listing TC-001, TC-002 | Airline, times, price, and Select control are shown per result |
| FLIGHT-002 | Flight filters work | Covered | Search&Listing TC-004 | Exact match (stops filter) |
| FLIGHT-003 | View flight details from listing | Covered | Search&Listing TC-003 | Exact match (baggage, fare rules, seat availability expand) |
| FLIGHT-004 | Proceed to flight booking with valid passenger data | Covered | Flight_Booking TC-001 | Exact match |
| FLIGHT-005 | Round-trip search summary displays both outbound and return travel dates | Covered | Search&Listing TC-001 | Exact match |
| FLIGHT-006 | Required passenger field missing | Covered | Flight_Booking TC-005, TC-006, TC-007 | Exact match |
| FLIGHT-007 | Passport expiry too soon | Not Covered | — | No GEN test checks passport expiry relative to travel date (the 6-month validity business rule) |
| FLIGHT-008 | Invalid passport number format | Covered | Flight_Booking TC-012 | Emoji/control-character passport number rejection is the same equivalence class as format validation |
| FLIGHT-009 | Continue is blocked without a selected itinerary and passenger count | Covered | Flight_Booking TC-010 | Exact match |

## Gap List (Not Covered)

- **FLIGHT-007** — Passport-expiry-vs-travel-date business rule untested

## Revision Note

Two rows described behavior GEN never isolates (distinct outbound/return itinerary display, one-way flow skipping return-leg data). GEN does demonstrate two other real Flights behaviors that had no GT scenario crediting them:

- **FLIGHT-005** (was: Round-trip search shows outbound and return selections) → narrowed to what's actually shown: the search summary header displays both outbound and return travel dates for a round-trip search (Search&Listing TC-001)
- **FLIGHT-009** (was: One-way trip boundary on booking flow) → Continue is blocked without a selected itinerary and passenger count (Flight_Booking TC-010)

The genuine gap was deliberately preserved: no GEN test validates passport expiry against the travel date's six-month rule.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Flights Search And Booking | 9 | 8 | 1 | 88.9% |
