# PHPTravels Test Cases — Ground Truth

Source: dataset/ground_truth/Phptravels/Phptravels.md

## Offers And Deals

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| OFFER-001 | Offers page content displayed | None | 1. Open Offers page | Hero banner, category filters, destination controls, and offer cards are visible | High |
| OFFER-002 | Filter offers by category | Offers page is open | 1. Select a category tab or filter | Visible offers update to match selected category | Medium |
| OFFER-003 | Offer Book Now action applies deal | Valid offer exists | 1. Click "Book Now" on an offer | Offer is applied and user is redirected to relevant booking or listing flow | High |
| OFFER-004 | Newsletter subscription with valid email | Offers page is open | 1. Enter valid email<br>2. Click "Subscribe" | Subscription confirmation message is displayed | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| OFFER-005 | Newsletter subscription with invalid email | Offers page is open | 1. Enter invalid email<br>2. Click "Subscribe" | Validation error is displayed | Medium |
| OFFER-006 | Expired offer cannot be applied | Expired offer exists | 1. Attempt to use expired offer | Offer is rejected or clearly marked as unavailable | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| OFFER-007 | Offer validity date boundary | Offer expires today or at a known cut-off time | 1. Attempt to use the offer near expiration time | Offer acceptance or rejection matches the documented validity boundary | Low |
