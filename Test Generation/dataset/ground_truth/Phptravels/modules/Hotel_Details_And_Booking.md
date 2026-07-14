# PHPTravels Test Cases — Ground Truth

Source: dataset/ground_truth/Phptravels/Phptravels.md

## Hotel Details And Booking

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HBOOK-001 | Hotel details page content displayed | Hotel details page is open | 1. Review hotel details page | Gallery, description, map link, amenities, room availability, reviews, and policies are visible | High |
| HBOOK-002 | View room availability and select room | Hotel details page is open and rooms are available | 1. Review room options<br>2. Click "Select" or "Book Now" on an available room | Booking form opens for the chosen room | High |
| HBOOK-003 | Submit valid hotel booking form | Room selection form is open | 1. Enter valid guest information<br>2. Review price breakdown<br>3. Click booking continuation button | User proceeds to payment step | High |
| HBOOK-004 | Reviews section displayed on hotel details page | Hotel details page is open | 1. Scroll to reviews area | Aggregate rating and individual reviews are visible | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HBOOK-005 | Required guest details missing | Hotel booking form is open | 1. Leave required guest fields empty<br>2. Submit booking form | Validation errors are displayed and form is not submitted | High |
| HBOOK-006 | Sold-out room cannot be booked | Hotel details page includes sold-out inventory | 1. Attempt to select a sold-out room | Booking action is blocked and room remains unavailable | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HBOOK-007 | Special requests text boundary | Hotel booking form is open | 1. Enter special requests at maximum practical length<br>2. Continue booking | Text is accepted or validated consistently at the boundary | Low |
