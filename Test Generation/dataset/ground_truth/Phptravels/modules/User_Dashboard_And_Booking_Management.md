# PHPTravels Test Cases — Ground Truth

Source: dataset/ground_truth/Phptravels/Phptravels.md

## User Dashboard And Booking Management

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| UDB-001 | Dashboard sections displayed | Logged in as authenticated user | 1. Open dashboard | My Bookings, My Profile, Wallet, Wishlist, Reviews, and Settings sections are available | High |
| UDB-002 | View booking details | Logged in and at least one booking exists | 1. Open My Bookings<br>2. Click "View Details" | Booking detail page opens with status, traveler data, and pricing breakdown | High |
| UDB-003 | Modify eligible booking | Logged in and modifiable booking exists | 1. Open booking details<br>2. Click "Modify"<br>3. Change eligible details<br>4. Confirm changes | Booking updates successfully and confirmation is shown | High |
| UDB-004 | Cancel eligible booking | Logged in and cancellable booking exists | 1. Open booking details<br>2. Click "Cancel"<br>3. Confirm cancellation | Booking status changes to cancelled and refund details are displayed | High |
| UDB-005 | Remove item from wishlist | Logged in and wishlist is not empty | 1. Open Wishlist<br>2. Click "Remove" on an item | Item is removed from wishlist | Medium |
| UDB-006 | Update profile details | Logged in | 1. Open My Profile<br>2. Update editable fields<br>3. Save | Profile information is updated successfully | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| UDB-007 | Modify non-eligible booking | Logged in and non-modifiable booking exists | 1. Open booking details for restricted booking<br>2. Attempt modification | Modification is blocked and policy feedback is displayed | Medium |
| UDB-008 | Cancel non-eligible booking | Logged in and non-cancellable booking exists | 1. Open booking details for restricted booking<br>2. Attempt cancellation | Cancellation is blocked and applicable policy is displayed | Medium |
| UDB-009 | Invalid profile email update | Logged in | 1. Enter invalid email format in profile<br>2. Save | Validation error is displayed | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| UDB-010 | Cancellation policy threshold boundary | Logged in and booking has a free-cancellation deadline | 1. Attempt cancellation near the policy cut-off time | Refund amount and policy messaging match the applicable boundary rules | Low |
