# PHPTravels Test Cases — Ground Truth

Source: dataset/ground_truth/Phptravels/Phptravels.md

## Tours Search And Booking

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| TOUR-001 | Tour listing cards displayed | Valid tour search has been submitted | 1. View tours listing page | Tour cards show image, title, destination, duration, price, and rating | High |
| TOUR-002 | Filter tours by destination or type | Valid tour search has been submitted | 1. Apply destination or tour-type filters | Tours list updates to match selected filters | Medium |
| TOUR-003 | Tour details page displays itinerary and inclusions | Tour details page is open | 1. Review tour details page | Itinerary, inclusions, exclusions, departure dates, and pricing are visible | High |
| TOUR-004 | Book tour with valid traveler information | Tour details page is open and departure date is available | 1. Select departure date<br>2. Enter traveler details<br>3. Click "Book Now" | User proceeds to payment step | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| TOUR-005 | Lead traveler details missing | Tour booking form is open | 1. Leave required traveler fields empty<br>2. Submit | Validation errors are displayed | High |
| TOUR-006 | Unavailable departure date selected | Tour has unavailable dates | 1. Attempt to select an unavailable departure date | Booking cannot continue with unavailable departure | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| TOUR-007 | Adult and child count recalculates total | Tour booking form is open | 1. Adjust adult and child counts at minimum or maximum tested values | Total price recalculates consistently | Low |
