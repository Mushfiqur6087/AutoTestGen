# PHPTravels Test Cases — Ground Truth

Source: dataset/ground_truth/Phptravels/Phptravels.md

## Reviews And Ratings

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REVIEW-001 | Submitted review displays the overall star rating in the reviews list | User has submitted a post-stay review with an overall rating | 1. Submit a review with a valid overall star rating<br>2. View the Reviews list for the listing | The new review appears in the Reviews list showing the submitted overall star rating | High |
| REVIEW-002 | Reviews Filters narrow the individual reviews list shown on the item detail page | Item detail page is open with review data available | 1. Select a rating, date range, and traveler type in the Reviews Filters form<br>2. Click "Apply Filters" | The Reviews list updates to show only individual reviews matching the selected criteria; unrelated reviews are no longer visible | High |
| REVIEW-003 | Submit review for completed booking | Logged in user has an eligible completed booking | 1. Open review submission flow<br>2. Enter valid ratings and comment<br>3. Submit review | Review is submitted successfully or queued for moderation | High |
| REVIEW-004 | Clear Filters returns the Reviews list to the default unfiltered view | Filters are currently applied in the Reviews Filters form | 1. Click the Clear Filters button | All filter controls are cleared and the Reviews list displays the default unfiltered set of reviews | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REVIEW-005 | Review comment below minimum length | Logged in user is on review submission form | 1. Enter comment shorter than the minimum length<br>2. Submit review | Validation error is displayed | Medium |
| REVIEW-006 | Ineligible user attempts to submit review | Logged in user does not have a completed booking for the item | 1. Attempt to access or submit review form | Review submission is blocked | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REVIEW-007 | Rapid double-click of Submit Review does not create a duplicate review | User is authenticated and has a completed booking eligible for review | 1. Fill required review fields with valid values<br>2. Click Submit Review twice in rapid succession | Second submission attempt is blocked; only one new review appears in the Reviews list | Low |
