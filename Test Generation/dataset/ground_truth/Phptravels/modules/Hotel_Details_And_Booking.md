# PHPTravels Test Cases — Ground Truth

Source: dataset/ground_truth/Phptravels/Phptravels.md

## Hotel Details And Booking

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HBOOK-001 | Room Types list with availability is displayed on the Hotel Details page | Hotel details page is open with stay dates and guest count selected | 1. Review the Room Types list on the Hotel Details page | Room Types list is visible, showing each available room type ready for selection | High |
| HBOOK-002 | View room availability and select room | Hotel details page is open and rooms are available | 1. Review room options<br>2. Click "Select" or "Book Now" on an available room | Booking form opens for the chosen room | High |
| HBOOK-003 | Submit valid hotel booking form | Room selection form is open | 1. Enter valid guest information<br>2. Review price breakdown<br>3. Click booking continuation button | User proceeds to payment step | High |
| HBOOK-004 | Selecting a different room updates the visible booking form | Hotel details page is open with one room already selected and the Booking form visible | 1. Click Select Room for a different room type | Booking form updates to show the newly selected room's details, replacing the previous selection | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HBOOK-005 | Required guest details missing | Hotel booking form is open | 1. Leave required guest fields empty<br>2. Submit booking form | Validation errors are displayed and form is not submitted | High |
| HBOOK-006 | Book Now while unauthenticated redirects to Login | Hotel details page is open, a room is selected, and the Booking form is visible; user is not logged in | 1. Fill the Booking form with valid guest details<br>2. Click "Book Now" | The Login page is displayed, requiring the user to authenticate before completing the booking | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HBOOK-007 | Special requests text boundary | Hotel booking form is open | 1. Enter special requests at maximum practical length<br>2. Continue booking | Text is accepted or validated consistently at the boundary | Low |
