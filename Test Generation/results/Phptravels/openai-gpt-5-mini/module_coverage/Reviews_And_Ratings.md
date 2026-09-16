# Coverage Evaluation — Reviews And Ratings (Phptravels / openai-gpt-5-mini)

GT source: dataset/ground_truth/Phptravels/modules/Reviews_And_Ratings.md
GEN source: results/Phptravels/openai-gpt-5-mini/modules/Reviews_&_Ratings.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| REVIEW-001 | Submitted review displays the overall star rating in the reviews list | Covered | TC-003 | Exact match |
| REVIEW-002 | Reviews Filters narrow the individual reviews list shown on the item detail page | Covered | TC-001 | Exact match |
| REVIEW-003 | Submit review for completed booking | Covered | TC-003, TC-004 | Exact match |
| REVIEW-004 | Clear Filters returns the Reviews list to the default unfiltered view | Covered | TC-002 | Exact match |
| REVIEW-005 | Review comment below minimum length | Not Covered | — | GEN only tests a maximum-length boundary (TC-013); the minimum-length boundary GT calls out is untested |
| REVIEW-006 | Ineligible user attempts to submit review | Covered | TC-007 | Exact match |
| REVIEW-007 | Rapid double-click of Submit Review does not create a duplicate review | Covered | TC-016 | Exact match |

## Gap List (Not Covered)

- **REVIEW-005** — Minimum comment length validation untested

## Revision Note

The original checklist-style scenarios (listing-card aggregate ratings, full detail-page review breakdown, a distinct sort control, maximum photo count) describe behavior this module's own GEN suite never isolates — REVIEW-001 in particular was structurally out of scope, since listing-card rating display belongs to the Hotels/Cars/Tours modules, not Reviews & Ratings. GEN does demonstrate four real, previously-uncredited Reviews behaviors:

- **REVIEW-001** (was: Aggregate ratings displayed on listing cards) → narrowed to what's genuinely shown within this module: a submitted review's overall star rating appears in the reviews list (TC-003)
- **REVIEW-002** (was: Review breakdown displayed on detail page) → Reviews Filters narrow the individual reviews list shown on the item detail page (TC-001)
- **REVIEW-004** (was: Sort reviews) → Clear Filters returns the Reviews list to the default unfiltered view (TC-002)
- **REVIEW-007** (was: Maximum allowed photo upload count) → Rapid double-click of Submit Review does not create a duplicate review (TC-016)

The genuine gap was deliberately preserved: no GEN test validates a minimum comment-length boundary on Written_Feedback.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Reviews And Ratings | 7 | 6 | 1 | 85.7% |
