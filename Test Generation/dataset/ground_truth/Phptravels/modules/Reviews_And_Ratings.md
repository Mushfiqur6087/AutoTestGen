# PHPTravels Test Cases — Ground Truth

Source: dataset/ground_truth/Phptravels/Phptravels.md

## Reviews And Ratings

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REVIEW-001 | Aggregate ratings displayed on listing cards | User is on a hotel, tour, or car listing page | 1. Review listing cards | Rating score, label, and review count are displayed | High |
| REVIEW-002 | Review breakdown displayed on detail page | Hotel, tour, or car detail page is open | 1. Scroll to the reviews section | Aggregate score, category breakdown, and individual reviews are visible | High |
| REVIEW-003 | Submit review for completed booking | Logged in user has an eligible completed booking | 1. Open review submission flow<br>2. Enter valid ratings and comment<br>3. Submit review | Review is submitted successfully or queued for moderation | High |
| REVIEW-004 | Sort reviews | Detail page has multiple reviews | 1. Change review sort option | Review list updates according to selected order | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REVIEW-005 | Review comment below minimum length | Logged in user is on review submission form | 1. Enter comment shorter than the minimum length<br>2. Submit review | Validation error is displayed | Medium |
| REVIEW-006 | Ineligible user attempts to submit review | Logged in user does not have a completed booking for the item | 1. Attempt to access or submit review form | Review submission is blocked | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REVIEW-007 | Maximum allowed photo upload count | Logged in user is on review submission form | 1. Upload the maximum allowed number of photos<br>2. Submit review | Upload is accepted at the allowed boundary | Low |
