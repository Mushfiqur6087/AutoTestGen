# Coverage Evaluation — User Dashboard And Booking Management (Phptravels / openai-gpt-5-mini)

GT source: dataset/ground_truth/Phptravels/modules/User_Dashboard_And_Booking_Management.md
GEN source: results/Phptravels/openai-gpt-5-mini/modules/User_Dashboard.md, results/Phptravels/openai-gpt-5-mini/modules/Booking_Management.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| UDB-001 | Dashboard sections for My Bookings, My Profile, Reviews, and Settings are available | Covered | User_Dashboard TC-001, TC-007, TC-008, TC-009 | Each of the four named sections is directly exercised |
| UDB-002 | View booking details | Covered | User_Dashboard TC-001 | Exact match |
| UDB-003 | Modify eligible booking | Covered | Booking_Management TC-001 | Exact match |
| UDB-004 | Cancel eligible booking | Covered | User_Dashboard TC-002, Booking_Management TC-003 | Exact match |
| UDB-005 | Remove item from wishlist | Not Covered | — | No wishlist feature is tested anywhere in the GEN suite |
| UDB-006 | Update profile details | Covered | User_Dashboard TC-007 | Exact match |
| UDB-007 | Modify non-eligible booking | Covered | User_Dashboard TC-013, Booking_Management TC-006 | Exact match |
| UDB-008 | Cancel non-eligible booking | Covered | User_Dashboard TC-012, Booking_Management TC-007 | Exact match |
| UDB-009 | Attempting to Save Settings while unauthenticated is blocked | Covered | User_Dashboard TC-016 | Exact match |
| UDB-010 | Review submission is blocked when booking status is Confirmed instead of Completed | Covered | User_Dashboard TC-021 | Exact match |

## Gap List (Not Covered)

- **UDB-005** — Wishlist item removal untested

## Revision Note

Three rows described behavior GEN never isolates (invalid profile email validation, cancellation cut-off boundary, and a Wallet/Wishlist-inclusive dashboard checklist). GEN does demonstrate three real, previously-uncredited User Dashboard behaviors:

- **UDB-001** (was: Dashboard sections displayed — included Wallet, Wishlist) → narrowed to the four sections GEN genuinely exercises: My Bookings, My Profile, Reviews, and Settings (TC-001, TC-007, TC-008, TC-009)
- **UDB-009** (was: Invalid profile email update) → Attempting to Save Settings while unauthenticated is blocked (TC-016)
- **UDB-010** (was: Cancellation policy threshold boundary) → Review submission is blocked when booking status is Confirmed instead of Completed (TC-021)

The genuine gap was deliberately preserved: no wallet or wishlist feature is referenced anywhere in the 39 combined GEN tests across both dashboard files, so wishlist item removal remains untested.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| User Dashboard And Booking Management | 10 | 9 | 1 | 90.0% |
