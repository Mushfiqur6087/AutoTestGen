# PHPTravels Test Cases — Ground Truth

Source: dataset/ground_truth/Phptravels/Phptravels.md

## Hotels Search And Listing

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HOTEL-001 | Hotel listing page displays search summary and results count | Valid hotel search has been submitted | 1. View hotel listing page | Search summary, total results count, filters, and sorting controls are visible | High |
| HOTEL-002 | Hotel cards display expected content | Valid hotel search has been submitted | 1. View hotel listing page | Each hotel card shows image, name, location, rating, price, and action button | High |
| HOTEL-003 | Sort hotels by price | Valid hotel search has been submitted | 1. Change sort to "Price: Low to High" or "Price: High to Low" | Hotel results reorder according to selected sort | Medium |
| HOTEL-004 | Filter hotels by star rating or facilities | Valid hotel search has been submitted | 1. Apply star or facility filters | Hotel results update to match selected filters | High |
| HOTEL-005 | Open hotel details from listing | Valid hotel search has been submitted | 1. Click hotel name or "View Details" | Hotel details page opens | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HOTEL-006 | Search with non-matching destination | None | 1. Search for destination with no available properties | Empty-state or no-results feedback is shown | Medium |
| HOTEL-007 | Invalid hotel date range from listing edit | Listing page is open with editable search summary | 1. Set check-out before check-in<br>2. Apply search | Validation prevents invalid search update | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HOTEL-008 | Price range slider minimum and maximum bounds | Hotel listing page is open | 1. Drag slider to minimum and maximum ends | Result set updates correctly at both range extremes | Low |
| HOTEL-009 | Clear all hotel filters | One or more filters are active | 1. Click "Clear All Filters" | Filters reset and full unfiltered listing returns | Medium |
