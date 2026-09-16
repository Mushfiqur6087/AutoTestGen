# Coverage Evaluation — Hotels Search And Listing (Phptravels / openai-gpt-5-mini)

GT source: dataset/ground_truth/Phptravels/modules/Hotels_Search_And_Listing.md
GEN source: results/Phptravels/openai-gpt-5-mini/modules/Hotels_Search_&_Listing.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| HOTEL-001 | Hotel listing page displays search summary and results count | Covered | TC-001, TC-002, TC-005 | Search summary, filters, and sort controls are each exercised, jointly demonstrating the listing header area |
| HOTEL-002 | Hotel cards display expected content | Covered | TC-001 | Card shows name, location, rating, thumbnail, price; action button covered via TC-006's Book Now |
| HOTEL-003 | Sort hotels by price | Covered | TC-005 | Exact match (equivalence class covers both sort directions) |
| HOTEL-004 | Filter hotels by star rating or facilities | Covered | TC-002 | Exact match |
| HOTEL-005 | Open hotel details from listing | Covered | TC-006 | Book Now opens the combined Hotel Details & Booking page — same equivalence class as "View Details" |
| HOTEL-006 | Search with non-matching destination | Not Covered | — | No GEN test searches a destination with zero results |
| HOTEL-007 | Invalid hotel date range from listing edit | Covered | TC-013 | Same underlying cross-field date validation as the initial search form, exercised fixture-agnostically |
| HOTEL-008 | Price range slider minimum and maximum bounds | Not Covered | — | TC-014 tests a non-numeric price value, not the slider's extreme-bound behavior GT calls out |
| HOTEL-009 | Clear all hotel filters | Covered | TC-004 | Exact match (Reset all) |

## Gap List (Not Covered)

- **HOTEL-006** — Non-matching destination / empty-state search untested
- **HOTEL-008** — Price range slider min/max extremes untested

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Hotels Search And Listing | 9 | 7 | 2 | 77.8% |
