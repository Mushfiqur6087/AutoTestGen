# PHPTravels Test Cases — Ground Truth

Source: dataset/ground_truth/Phptravels/Phptravels.md

## User Dashboard And Booking Management

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| UDB-001 | Dashboard sections for My Bookings, My Profile, Reviews, and Settings are available | Logged in as authenticated user | 1. Open dashboard | My Bookings, My Profile, Reviews, and Settings sections are available | High |
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
| UDB-009 | Attempting to Save Settings while unauthenticated is blocked | User is not authenticated, Settings page URL is accessible directly | 1. Navigate directly to the Settings section URL without logging in<br>2. Attempt to interact with settings controls (e.g., click Save Settings) | User is redirected to the login page or shown an authentication prompt; Save Settings action is not performed and settings are not updated | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| UDB-010 | Review submission is blocked when booking status is Confirmed instead of Completed | Authenticated user has a booking with Selected_Booking_Status == Confirmed | 1. Locate the booking row whose status is Confirmed<br>2. Attempt to click an action to open the Review Submission Form for that booking | Action is blocked; the Review Submission Form is not displayed and no submit option is available for that booking | Low |
