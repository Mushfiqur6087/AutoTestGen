# PHPTravels Test Cases — Ground Truth

Source: dataset/ground_truth/Phptravels/Phptravels.md

## Flights Search And Booking

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FLIGHT-001 | Flight listing displays itinerary cards | Valid flight search has been submitted | 1. View flight listing page | Airline, times, stops, price, and selection controls are displayed for each result | High |
| FLIGHT-002 | Flight filters work | Valid flight search has been submitted | 1. Apply airline, stops, or departure-time filters | Flight results update to match selected filters | High |
| FLIGHT-003 | View flight details from listing | Valid flight search has been submitted | 1. Click "View Details" | Expanded or detailed fare information is displayed | Medium |
| FLIGHT-004 | Proceed to flight booking with valid passenger data | Flight has been selected | 1. Enter valid passenger details<br>2. Accept terms if required<br>3. Continue | User proceeds to payment step | High |
| FLIGHT-005 | Round-trip search shows outbound and return selections | Valid round-trip search has been submitted | 1. Review results | Outbound and return itineraries are displayed | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FLIGHT-006 | Required passenger field missing | Flight booking form is open | 1. Leave a required passenger field empty<br>2. Continue | Validation error is displayed | High |
| FLIGHT-007 | Passport expiry too soon | Flight booking form is open for travel requiring passport | 1. Enter passport expiry less than six months from travel date<br>2. Continue | Validation error indicates passport validity is insufficient | High |
| FLIGHT-008 | Invalid passport number format | Flight booking form is open | 1. Enter invalid passport format<br>2. Continue | Validation error is displayed | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FLIGHT-009 | One-way trip boundary on booking flow | Valid one-way flight search has been submitted | 1. Complete one-way flight selection<br>2. Continue to booking | Booking flow proceeds without requiring return leg data | Low |
