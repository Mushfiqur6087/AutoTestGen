# PHPTravels Test Cases — Ground Truth

Source: dataset/ground_truth/Phptravels/Phptravels.md

## Cars Search And Booking

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| CAR-001 | Car listing cards displayed | Valid car search has been submitted | 1. View car listing page | Vehicle image, category, features, rental company, and pricing are visible | High |
| CAR-002 | Compare cars | Valid car search has been submitted | 1. Select compare option for multiple cars | Comparison view or comparison data is displayed | Medium |
| CAR-003 | Add insurance and extras to booking | Car booking form is open | 1. Select insurance or extras<br>2. Review total | Total price updates to include selected options | High |
| CAR-004 | Book car with valid driver information | Car booking form is open | 1. Enter valid driver details<br>2. Accept terms<br>3. Continue | User proceeds to payment step | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| CAR-005 | Required driver information missing | Car booking form is open | 1. Leave required driver fields empty<br>2. Continue | Validation errors are displayed | High |
| CAR-006 | Driver below minimum age | Car booking form is open | 1. Enter age below minimum policy threshold<br>2. Continue | Booking is blocked or age surcharge/policy message is shown | High |
| CAR-007 | Terms and conditions unchecked | Car booking form is open | 1. Fill valid data<br>2. Leave terms unchecked<br>3. Continue | Booking does not proceed and terms validation is shown | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| CAR-008 | Same pick-up and drop-off location | Car booking form is open | 1. Set same pick-up and drop-off location<br>2. Continue | Booking flow handles same-location return consistently | Low |
