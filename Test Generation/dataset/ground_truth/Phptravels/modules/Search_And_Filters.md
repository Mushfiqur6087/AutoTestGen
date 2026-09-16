# PHPTravels Test Cases — Ground Truth

Source: dataset/ground_truth/Phptravels/Phptravels.md

## Search And Filters

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FILTER-001 | Filter sidebar controls displayed on listing pages | User is on a hotels, flights, tours, or cars listing page | 1. Review the listing page sidebar | Filter groups and sort controls are visible | High |
| FILTER-002 | Result count updates after applying filter | User is on a listing page with available filters | 1. Apply one or more filters | Result count updates to reflect the filtered result set | High |
| FILTER-003 | Active filter tag can be removed | One or more filters are active | 1. Remove an active filter tag | Corresponding filter is cleared and results refresh | Medium |
| FILTER-004 | Clear all filters resets listing | One or more filters are active | 1. Click "Clear All Filters" | All active filters are cleared and listing resets to the default state | Medium |
| FILTER-005 | Sorting control reorders results | User is on a listing page | 1. Select a different sort option | Result ordering updates according to the selected sort | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FILTER-006 | Filter combination returns no results | User is on a listing page | 1. Apply a restrictive combination of filters | Empty-state or zero-results feedback is displayed | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FILTER-007 | Reset all filters is blocked when no search has been executed | User is on a listing page but has not executed a search and no results are loaded | 1. Locate the "Reset all filters" control in the Active Filters Summary panel<br>2. Click the "Reset all filters" button | Reset all filters is blocked: the control is disabled or an inline message indicates a search must be executed first; results are not refreshed | Low |
