# Coverage Evaluation — Search And Filters (Phptravels / openai-gpt-5-mini)

GT source: dataset/ground_truth/Phptravels/modules/Search_And_Filters.md
GEN source: results/Phptravels/openai-gpt-5-mini/modules/Search_&_Filters.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| FILTER-001 | Filter sidebar controls displayed on listing pages | Covered | TC-001–TC-021 | Extensively exercised across every listing type, implying filter groups and sort controls render |
| FILTER-002 | Result count updates after applying filter | Covered | TC-001–TC-017 | Each filter test explicitly asserts the displayed result count updates |
| FILTER-003 | Active filter tag can be removed | Covered | TC-020 | Exact match |
| FILTER-004 | Clear all filters resets listing | Covered | TC-021 | Exact match (Reset all filters) |
| FILTER-005 | Sorting control reorders results | Covered | TC-018, TC-019 | Exact match |
| FILTER-006 | Filter combination returns no results | Not Covered | — | No GEN test applies a restrictive combination that yields zero results with an empty-state assertion |
| FILTER-007 | Reset all filters is blocked when no search has been executed | Covered | TC-022 | Exact match |

## Gap List (Not Covered)

- **FILTER-006** — Zero-result filter combination / empty-state untested

## Revision Note

FILTER-007 originally asked for range-slider extreme-bound behavior GEN never isolates (it only tests a generic price range and an invalid min>max range). GEN does demonstrate a real, previously-uncredited precondition-block behavior:

- **FILTER-007** (was: Price or time range filter at extreme bounds) → Reset all filters is blocked when no search has been executed (TC-022)

The genuine gap was deliberately preserved: no GEN test applies a restrictive filter combination that yields zero results with an empty-state assertion.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Search And Filters | 7 | 6 | 1 | 85.7% |
