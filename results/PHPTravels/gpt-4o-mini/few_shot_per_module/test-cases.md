# Test Cases — PHPTravels

Generated: 2026-06-04T15:04:52.598970Z  
Model: gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 21 | 88 | 26 | 29 | 33 | 55 | 33 | 0 |

## Home Page & Search

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Search for hotels with valid destination and date range | User is on the PHPTravels home page | 1. Click the Hotels tab on the search widget<br>2. Enter 'New York' in the Destination field<br>3. Select '2023-12-01' as the check-in date and '2023-12-05' as the check-out date<br>4. Set 1 room and 2 guests (1 adult, 1 child)<br>5. Click the Search button | User is redirected to the hotel listing page showing available hotels for New York from December 1 to December 5; each card displays hotel name, rating, and starting price per night | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Search for flights with missing departure city | User is on the PHPTravels home page | 1. Click the Flights tab on the search widget<br>2. Leave the Departure City field empty<br>3. Enter 'Los Angeles' in the Arrival City field<br>4. Select '2023-12-10' as the travel date<br>5. Set 1 adult passenger<br>6. Click Search | An inline validation error is shown on the Departure City field; no flight search is initiated | high |
| TC-004 |  | Search for cars with invalid drop-off date before pick-up date | User is on the PHPTravels home page | 1. Click the Cars tab on the search widget<br>2. Enter 'Los Angeles' in the Pick-up Location field<br>3. Select '2023-12-10' as the Pick-up Date<br>4. Select '2023-12-09' as the Drop-off Date<br>5. Click Search | An inline validation error is shown indicating that the Drop-off Date must be after the Pick-up Date; no car search is initiated | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Search for tours with a travel date range of the same day | User is on the PHPTravels home page | 1. Click the Tours tab on the search widget<br>2. Enter 'Paris' in the Destination field<br>3. Select today's date as both the start and end date for the travel date range<br>4. Click Search | User is redirected to the tours listing page; results show available tours in Paris for today, or an appropriate message if no tours are available | medium |
| TC-005 |  | Search for flights with maximum passenger count | User is on the PHPTravels home page | 1. Click the Flights tab on the search widget<br>2. Enter 'New York' in the Departure City field<br>3. Enter 'London' in the Arrival City field<br>4. Select '2023-12-15' as the travel date<br>5. Set 9 adults, 5 children, and 2 infants as the passenger count<br>6. Click Search | User is redirected to the flight listing page showing available flights for the specified passenger count, or an appropriate message if no flights are available | medium |

---

## User Registration

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Register a new account with valid details | User is on the Registration page | 1. Fill in First Name, Last Name, Email, and Mobile Number with valid values<br>2. Enter a valid password in the Password field<br>3. Enter the same password in the Confirm Password field<br>4. Fill in Address and select a Country from the dropdown<br>5. Check the Terms and Conditions checkbox<br>6. Click Register | User is automatically logged in and redirected to their dashboard; a success message is displayed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 |  | Register a new account with an invalid email format | User is on the Registration page | 1. Fill in First Name, Last Name, and Mobile Number with valid values<br>2. Enter an invalid email format in the Email field<br>3. Enter a valid password in the Password field<br>4. Enter the same password in the Confirm Password field<br>5. Fill in Address and select a Country from the dropdown<br>6. Check the Terms and Conditions checkbox<br>7. Click Register | An inline validation error is shown on the Email field; the account is not created | high |
| TC-008 |  | Register a new account with a password that does not match the confirmation field | User is on the Registration page | 1. Fill in First Name, Last Name, Email, and Mobile Number with valid values<br>2. Enter <password> in the Password field<br>3. Enter a different value in the Confirm Password field<br>4. Fill in Address and select a Country from the dropdown<br>5. Check the Terms and Conditions checkbox<br>6. Click Register | An inline validation error is shown on the Confirm Password field; the account is not created | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 |  | Register a new account with maximum length fields | User is on the Registration page | 1. Fill in First Name and Last Name with maximum allowed characters<br>2. Enter a valid email with maximum allowed length<br>3. Enter a valid password with maximum allowed length<br>4. Enter the same password in the Confirm Password field<br>5. Fill in Address with maximum allowed characters and select a Country from the dropdown<br>6. Enter a valid Mobile Number<br>7. Check the Terms and Conditions checkbox<br>8. Click Register | User is automatically logged in and redirected to their dashboard; a success message is displayed | medium |
| TC-010 |  | Register a new account with empty fields | User is on the Registration page | 1. Leave all fields empty<br>2. Click Register | Inline validation errors are shown for all required fields; the account is not created | medium |

---

## User Login

Total: **3** (positive: 1, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 |  | Login with valid credentials | User is on the Login page | 1. Enter a valid email address in the Email field<br>2. Enter the correct password in the Password field<br>3. Click the Login button | User is redirected to their dashboard or the page they were previously trying to access | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 |  | Login with invalid credentials | User is on the Login page | 1. Enter an invalid email address in the Email field<br>2. Enter an incorrect password in the Password field<br>3. Click the Login button | An error message is displayed indicating invalid credentials; the Password field is cleared | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 |  | Login after multiple failed attempts requiring CAPTCHA | User is on the Login page, User has failed to login multiple times | 1. Enter a valid email address in the Email field<br>2. Enter an incorrect password in the Password field<br>3. Click the Login button multiple times to trigger CAPTCHA<br>4. Complete the CAPTCHA verification<br>5. Enter the correct password in the Password field<br>6. Click the Login button | User is redirected to their dashboard or the page they were previously trying to access after successful CAPTCHA verification | medium |

---

## Forgot Password

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-014 |  | Request password reset with a valid email | User is on the Forgot Password page | 1. Enter a valid email address that exists in the system in the Email field<br>2. Click the Reset Password button | A confirmation message is shown indicating that a reset link has been sent to the email address; user remains on the Forgot Password page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 |  | Request password reset with an email that does not exist | User is on the Forgot Password page | 1. Enter an email address that does not exist in the system in the Email field<br>2. Click the Reset Password button | An error message is displayed indicating that the email address is not found; the form remains editable | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-016 |  | Request password reset with an empty email field | User is on the Forgot Password page | 1. Leave the Email field empty<br>2. Click the Reset Password button | An error message is displayed indicating that the email field cannot be empty; the form remains editable | medium |
| TC-017 |  | Request password reset with an email at maximum length | User is on the Forgot Password page | 1. Enter an email address with the maximum allowed length (e.g., 254 characters) in the Email field<br>2. Click the Reset Password button | A confirmation message is shown indicating that a reset link has been sent to the email address; user remains on the Forgot Password page | medium |

---

## Hotels Search & Listing

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-018 |  | Search for hotels with valid destination and date range | User is on the PHPTravels home page | 1. Click the Hotels tab on the search widget<br>2. Enter 'New York' in the Destination field<br>3. Select '2023-12-01' as the check-in date and '2023-12-05' as the check-out date<br>4. Set 1 room and 2 guests<br>5. Click the Search button | User is redirected to the hotel listing page showing available hotels for New York from December 1 to December 5; each card displays hotel name, location, star rating, thumbnail image, starting price per night, amenity icons, and a Book Now button | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-019 |  | Search for hotels with missing destination | User is on the PHPTravels home page | 1. Click the Hotels tab on the search widget<br>2. Leave the Destination field empty<br>3. Select '2023-12-01' as the check-in date and '2023-12-05' as the check-out date<br>4. Set 1 room and 2 guests<br>5. Click the Search button | An error message is displayed indicating that the destination field is required; the user remains on the same page | high |
| TC-021 |  | Search for hotels with invalid date range (check-out before check-in) | User is on the PHPTravels home page | 1. Click the Hotels tab on the search widget<br>2. Enter 'Miami' in the Destination field<br>3. Select '2023-12-05' as the check-in date and '2023-12-01' as the check-out date<br>4. Set 1 room and 2 guests<br>5. Click the Search button | An error message is displayed indicating that the check-out date must be after the check-in date; the user remains on the same page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-020 |  | Search for hotels with check-in date equal to check-out date | User is on the PHPTravels home page | 1. Click the Hotels tab on the search widget<br>2. Enter 'Los Angeles' in the Destination field<br>3. Select '2023-12-01' as both the check-in and check-out date<br>4. Set 1 room and 1 guest<br>5. Click the Search button | User is redirected to the hotel listing page; results show available hotels for December 1, or an appropriate message if no hotels are available | medium |
| TC-022 |  | Search for hotels with maximum number of rooms and guests | User is on the PHPTravels home page | 1. Click the Hotels tab on the search widget<br>2. Enter 'Chicago' in the Destination field<br>3. Select '2023-12-01' as the check-in date and '2023-12-10' as the check-out date<br>4. Set 5 rooms and 10 guests (2 adults and 8 children)<br>5. Click the Search button | User is redirected to the hotel listing page showing available hotels for Chicago from December 1 to December 10; results accommodate the specified number of rooms and guests | medium |

---

## Hotel Details & Booking

Total: **4** (positive: 1, negative: 2, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-023 |  | Book a room with valid user details | User is logged in, User is on the hotel details page | 1. Select a room type from the available options<br>2. Enter stay dates in the check-in and check-out fields<br>3. Set the number of guests<br>4. Fill in First Name, Last Name, Email, and Phone Number with valid values<br>5. Optionally enter a Special Request<br>6. Click the Book Now button | User is redirected to the payment page with a summary of the selected hotel, room type, stay dates, guest count, and price breakdown | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-024 |  | Attempt to book a room without being logged in | User is on the hotel details page | 1. Select a room type from the available options<br>2. Enter stay dates in the check-in and check-out fields<br>3. Set the number of guests<br>4. Fill in First Name, Last Name, Email, and Phone Number with valid values<br>5. Click the Book Now button | User is shown an error message indicating that they must be logged in to book a room | high |
| TC-026 |  | Book a room with missing required fields | User is logged in, User is on the hotel details page | 1. Select a room type from the available options<br>2. Enter stay dates in the check-in and check-out fields<br>3. Set the number of guests<br>4. Leave First Name and Last Name fields empty<br>5. Click the Book Now button | Inline validation errors are shown for the First Name and Last Name fields; the booking is not processed | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-025 |  | Book a room with maximum length of special requests | User is logged in, User is on the hotel details page | 1. Select a room type from the available options<br>2. Enter stay dates in the check-in and check-out fields<br>3. Set the number of guests<br>4. Fill in First Name, Last Name, Email, and Phone Number with valid values<br>5. Enter a Special Request with maximum allowed characters<br>6. Click the Book Now button | User is redirected to the payment page with a summary of the selected hotel, room type, stay dates, guest count, and price breakdown, including the special request | medium |

---

## Flights Search & Listing

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-027 |  | Search for flights with valid input | User is on the PHPTravels home page | 1. Click the Flights tab on the search widget<br>2. Select 'One-way' as the trip type<br>3. Enter 'New York' in the Departure City field<br>4. Enter 'Los Angeles' in the Arrival City field<br>5. Select a valid travel date in the Travel Date field<br>6. Set 1 adult passenger<br>7. Select 'Economy' as the cabin class<br>8. Click Search | User is redirected to the flight listing page showing available flights with airline logo, name, departure and arrival times, total duration, number of stops, price per passenger, and a Select button for each flight | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-028 |  | Search for flights with missing departure city | User is on the PHPTravels home page | 1. Click the Flights tab on the search widget<br>2. Select 'Round-trip' as the trip type<br>3. Leave the Departure City field empty<br>4. Enter 'Los Angeles' in the Arrival City field<br>5. Select a valid travel date in the Travel Date field<br>6. Set 1 adult passenger<br>7. Select 'Business' as the cabin class<br>8. Click Search | An inline validation error is shown for the Departure City field; no search is performed | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-029 |  | Search for flights with maximum passenger count | User is on the PHPTravels home page | 1. Click the Flights tab on the search widget<br>2. Select 'Multi-city' as the trip type<br>3. Enter 'New York' in the Departure City field<br>4. Enter 'Los Angeles' in the Arrival City field<br>5. Select a valid travel date in the Travel Date field<br>6. Set 9 adult passengers, 2 children, and 1 infant<br>7. Select 'Premium Economy' as the cabin class<br>8. Click Search | User is redirected to the flight listing page showing available flights for the specified number of passengers; results are displayed correctly | medium |
| TC-030 |  | Search for flights with same departure and arrival city | User is on the PHPTravels home page | 1. Click the Flights tab on the search widget<br>2. Select 'One-way' as the trip type<br>3. Enter 'New York' in the Departure City field<br>4. Enter 'New York' in the Arrival City field<br>5. Select a valid travel date in the Travel Date field<br>6. Set 1 adult passenger<br>7. Select 'Economy' as the cabin class<br>8. Click Search | User is redirected to the flight listing page; results show no available flights or an appropriate message indicating no flights can be booked for the same departure and arrival city | medium |

---

## Flight Booking

Total: **3** (positive: 1, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-031 |  | Book a flight with valid passenger details | User is on the Flight Booking page | 1. Verify the itinerary summary is displayed correctly<br>2. Enter 'Mr' in the Title field<br>3. Enter 'John' in the First Name field<br>4. Enter 'Doe' in the Last Name field<br>5. Enter '1990-01-01' in the Date of Birth field<br>6. Enter 'A12345678' in the Passport Number field<br>7. Enter '2030-01-01' in the Passport Expiry field<br>8. Enter 'john.doe@example.com' in the Email field<br>9. Enter '1234567890' in the Phone field<br>10. Click Continue | User is redirected to the payment page with a summary of the booking and fare breakdown | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-032 |  | Attempt to book a flight with missing required fields | User is on the Flight Booking page | 1. Verify the itinerary summary is displayed correctly<br>2. Leave the Title field empty<br>3. Enter 'John' in the First Name field<br>4. Enter 'Doe' in the Last Name field<br>5. Leave the Date of Birth field empty<br>6. Leave the Passport Number field empty<br>7. Leave the Passport Expiry field empty<br>8. Enter 'john.doe@example.com' in the Email field<br>9. Enter '1234567890' in the Phone field<br>10. Click Continue | Inline validation errors are shown for the empty required fields; the user cannot proceed to the payment page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-033 |  | Book a flight with a passport number at the maximum length | User is on the Flight Booking page | 1. Verify the itinerary summary is displayed correctly<br>2. Enter 'Mr' in the Title field<br>3. Enter 'John' in the First Name field<br>4. Enter 'Doe' in the Last Name field<br>5. Enter '1990-01-01' in the Date of Birth field<br>6. Enter 'A123456789012345' in the Passport Number field<br>7. Enter '2030-01-01' in the Passport Expiry field<br>8. Enter 'john.doe@example.com' in the Email field<br>9. Enter '1234567890' in the Phone field<br>10. Click Continue | User is redirected to the payment page with a summary of the booking and fare breakdown, indicating that the maximum length for the passport number is accepted | medium |

---

## Tours Search & Listing

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-034 |  | Search for tours with valid destination and travel dates | User is on the Tours Search page | 1. Enter <destination> in the Destination field<br>2. Select <start date> and <end date> for travel dates<br>3. Choose <tour type> from the dropdown<br>4. Enter <duration> in days<br>5. Set <budget range><br>6. Click the Search button | User is redirected to the tours listing page showing available tours for the selected criteria; each card displays tour image, name, destination, duration, starting price per person, a brief description, availability status, and traveler rating | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-035 |  | Search for tours with missing destination | User is on the Tours Search page | 1. Leave the Destination field empty<br>2. Select <start date> and <end date> for travel dates<br>3. Choose <tour type> from the dropdown<br>4. Enter <duration> in days<br>5. Set <budget range><br>6. Click the Search button | An inline validation error is shown on the Destination field; no tours are displayed | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-036 |  | Search for tours with maximum budget range | User is on the Tours Search page | 1. Enter <destination> in the Destination field<br>2. Select <start date> and <end date> for travel dates<br>3. Choose <tour type> from the dropdown<br>4. Enter <duration> in days<br>5. Set budget range to the maximum allowable value<br>6. Click the Search button | User is redirected to the tours listing page; results show available tours within the maximum budget range, or an appropriate message if no tours are available | medium |
| TC-037 |  | Search for tours with a duration of zero days | User is on the Tours Search page | 1. Enter <destination> in the Destination field<br>2. Select <start date> and <end date> for travel dates<br>3. Choose <tour type> from the dropdown<br>4. Enter 0 in the Duration field<br>5. Set <budget range><br>6. Click the Search button | User is redirected to the tours listing page; results may show an appropriate message indicating that a duration of zero days is not valid, or display tours with a minimum duration if applicable | medium |

---

## Tour Details & Booking

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-038 |  | Book a tour with valid details | User is on the Tour Details page | 1. Select a departure date from the available options<br>2. Specify the number of travelers (adults and children)<br>3. Click the Book Now button<br>4. Fill in traveler names, contact details, and any special requirements<br>5. Review the total cost breakdown<br>6. Click Confirm Booking | User receives a booking confirmation message and is redirected to the booking summary page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-039 |  | Attempt to book a tour without selecting a departure date | User is on the Tour Details page | 1. Leave the departure date field empty<br>2. Specify the number of travelers (adults and children)<br>3. Click the Book Now button | An error message is displayed indicating that the departure date is required; the booking process does not proceed | high |
| TC-041 |  | Book a tour with invalid contact details | User is on the Tour Details page | 1. Select a departure date from the available options<br>2. Specify the number of travelers (adults and children)<br>3. Click the Book Now button<br>4. Enter invalid contact details (e.g., incorrect email format)<br>5. Click Confirm Booking | An error message is displayed indicating that the contact details are invalid; the booking process does not proceed | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-040 |  | Book a tour with maximum number of travelers | User is on the Tour Details page | 1. Select a departure date from the available options<br>2. Specify the maximum number of travelers allowed (e.g., 10 adults and 10 children)<br>3. Click the Book Now button<br>4. Fill in traveler names, contact details, and any special requirements<br>5. Review the total cost breakdown<br>6. Click Confirm Booking | User receives a booking confirmation message and is redirected to the booking summary page; total cost reflects the maximum number of travelers | medium |
| TC-042 |  | Book a tour with special requirements exceeding character limit | User is on the Tour Details page | 1. Select a departure date from the available options<br>2. Specify the number of travelers (adults and children)<br>3. Click the Book Now button<br>4. Fill in traveler names and contact details<br>5. Enter a special requirement that exceeds the maximum character limit<br>6. Click Confirm Booking | An error message is displayed indicating that the special requirements exceed the character limit; the booking process does not proceed | medium |

---

## Cars Search & Listing

Total: **3** (positive: 1, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-043 |  | Search for cars with valid pick-up and drop-off details | User is on the PHPTravels home page | 1. Click the Cars tab on the search widget<br>2. Enter <pick-up location> in the Pick-up Location field<br>3. Enter <drop-off location> in the Drop-off Location field<br>4. Select <pick-up date> and <pick-up time><br>5. Select <drop-off date> and <drop-off time><br>6. Enter <driver age><br>7. Click the Search button | User is redirected to the car listing page showing available vehicles grouped by category; each listing displays vehicle image, make and model, transmission type, fuel policy, seating and luggage capacity, feature icons, price per day, total rental cost, and a Book Now button | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-044 |  | Search for cars with missing pick-up location | User is on the PHPTravels home page | 1. Click the Cars tab on the search widget<br>2. Leave the Pick-up Location field empty<br>3. Enter <drop-off location> in the Drop-off Location field<br>4. Select <pick-up date> and <pick-up time><br>5. Select <drop-off date> and <drop-off time><br>6. Enter <driver age><br>7. Click the Search button | An error message is displayed indicating that the Pick-up Location is required; the search is not executed | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-045 |  | Search for cars with pick-up and drop-off dates set to the same day and time | User is on the PHPTravels home page | 1. Click the Cars tab on the search widget<br>2. Enter <pick-up location> in the Pick-up Location field<br>3. Enter <drop-off location> in the Drop-off Location field<br>4. Select today's date as the pick-up date and time<br>5. Select the same date and time as the drop-off date and time<br>6. Enter <driver age><br>7. Click the Search button | User is redirected to the car listing page; results show available vehicles for the same-day rental, or an appropriate message if no vehicles are available | medium |

---

## Car Booking

Total: **3** (positive: 1, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-046 |  | Successfully book a car with valid details | User is on the Car Booking page | 1. Enter valid Driver Full Name<br>2. Enter valid Age (e.g., 30)<br>3. Enter valid License Number<br>4. Select valid License Issue Country<br>5. Enter valid Email<br>6. Enter valid Phone Number<br>7. Select rental period and pick-up/drop-off locations and times<br>8. Choose an insurance plan<br>9. Accept the terms and conditions<br>10. Click Confirm Booking | User is redirected to the payment page with a summary of the booking details and pricing breakdown | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-047 |  | Attempt to book a car with an invalid email format | User is on the Car Booking page | 1. Enter valid Driver Full Name<br>2. Enter valid Age<br>3. Enter valid License Number<br>4. Select valid License Issue Country<br>5. Enter invalid Email (e.g., 'user@domain')<br>6. Enter valid Phone Number<br>7. Select rental period and pick-up/drop-off locations and times<br>8. Choose an insurance plan<br>9. Accept the terms and conditions<br>10. Click Confirm Booking | An inline validation error is shown on the Email field; the booking is not processed | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-048 |  | Book a car with the minimum age requirement | User is on the Car Booking page | 1. Enter valid Driver Full Name<br>2. Enter minimum valid Age (e.g., 18)<br>3. Enter valid License Number<br>4. Select valid License Issue Country<br>5. Enter valid Email<br>6. Enter valid Phone Number<br>7. Select rental period and pick-up/drop-off locations and times<br>8. Choose an insurance plan<br>9. Accept the terms and conditions<br>10. Click Confirm Booking | User is redirected to the payment page with a summary of the booking details and pricing breakdown, confirming that booking is allowed for the minimum age | medium |

---

## Visa Services

Total: **3** (positive: 1, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-049 |  | View visa requirements for valid nationality and destination country | User is on the Visa Services page | 1. Select a valid Nationality from the dropdown<br>2. Select a valid Destination Country from the dropdown<br>3. Click the 'View Requirements' button | The system displays the visa requirements including visa type, processing time, required documents, and fees for the selected nationality and destination country | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-050 |  | Submit visa application with missing required fields | User is on the Visa Application form page | 1. Fill in Full Name, Passport Number, and Date of Birth with valid values<br>2. Leave the Passport Expiry Date field empty<br>3. Fill in Nationality, Email, and Phone with valid values<br>4. Fill in Purpose of Visit and Intended Travel Dates with valid values<br>5. Click the Submit button | An error message is displayed indicating that the Passport Expiry Date is required; the application is not submitted | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-051 |  | Submit visa application with maximum length fields | User is on the Visa Application form page | 1. Fill in Full Name with 100 characters<br>2. Enter a valid Passport Number with maximum allowed characters<br>3. Set Passport Expiry Date to a valid future date<br>4. Enter Date of Birth with a valid date<br>5. Select Nationality from the dropdown<br>6. Enter a valid Email and Phone number<br>7. Fill in Purpose of Visit with maximum allowed characters<br>8. Set Intended Travel Dates to valid future dates<br>9. Upload required documents including passport copy and photographs<br>10. Click the Submit button | The application is submitted successfully, and a confirmation message is displayed; the user can track the application status in the dashboard | medium |

---

## User Dashboard

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-052 |  | View upcoming bookings in My Bookings section | User is logged into the User Dashboard | 1. Navigate to the My Bookings section<br>2. Observe the list of upcoming bookings | User sees a list of upcoming bookings with booking reference, service type, travel dates, and status | high |
| TC-053 |  | Edit personal information in My Profile section | User is logged into the User Dashboard | 1. Navigate to the My Profile section<br>2. Click the Edit button<br>3. Update First Name and Last Name<br>4. Click Save | User's personal information is updated successfully and a confirmation message is displayed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-054 |  | Attempt to cancel a booking that is already cancelled | User is logged into the User Dashboard, User has a booking with status 'Cancelled' | 1. Navigate to the My Bookings section<br>2. Locate the cancelled booking<br>3. Click the Cancel button | An error message is displayed indicating that the booking cannot be cancelled again | high |
| TC-055 |  | Try to modify a booking that is in 'Pending' status | User is logged into the User Dashboard, User has a booking with status 'Pending' | 1. Navigate to the My Bookings section<br>2. Locate the pending booking<br>3. Click the Modify button | An error message is displayed indicating that the booking cannot be modified at this time | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-056 |  | View transaction history with no transactions | User is logged into the User Dashboard, User has no transaction history | 1. Navigate to the Wallet/Credits section | User sees a message indicating that there are no transactions available | medium |
| TC-057 |  | Change password with a new password that is the same as the old password | User is logged into the User Dashboard | 1. Navigate to the Settings section<br>2. Click on Change Password<br>3. Enter the current password<br>4. Enter the same password in the New Password field<br>5. Click Save | An error message is displayed indicating that the new password must be different from the current password | medium |

---

## Booking Management

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-058 |  | View booking details with valid confirmation number | User is logged in, User has a valid booking | 1. Navigate to the Booking Management section<br>2. Enter a valid confirmation number in the search field<br>3. Click the Search button | User sees the booking details including confirmation number, service information, traveler details, payment information, and current booking status | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-059 |  | Attempt to modify booking with invalid traveler information | User is logged in, User has a valid booking | 1. Navigate to the Booking Management section<br>2. Enter a valid confirmation number in the search field<br>3. Click the Modify button<br>4. Change the traveler information to invalid values (e.g., empty name)<br>5. Click Save Changes | An error message is displayed indicating that the traveler information is invalid; changes are not saved | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-060 |  | Cancel a booking with a non-refundable policy | User is logged in, User has a valid booking with a non-refundable policy | 1. Navigate to the Booking Management section<br>2. Enter a valid confirmation number in the search field<br>3. Click the Cancel button<br>4. Confirm the cancellation in the confirmation dialog | User sees a message indicating that the booking has been canceled and that no refund will be issued; the booking status is updated accordingly | medium |
| TC-061 |  | Modify booking with maximum allowed special requests | User is logged in, User has a valid booking | 1. Navigate to the Booking Management section<br>2. Enter a valid confirmation number in the search field<br>3. Click the Modify button<br>4. Add the maximum number of special requests allowed<br>5. Click Save Changes | User sees a success message indicating that the booking has been modified with the special requests; the updated details are displayed | medium |

---

## Payment Processing

Total: **5** (positive: 2, negative: 2, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-062 |  | Complete payment with valid credit card details | User is on the Payment page with a full booking summary displayed | 1. Enter valid Cardholder Name<br>2. Enter a valid Card Number<br>3. Select a valid Expiration Date<br>4. Enter a valid CVV<br>5. Check the option to save the card for future use<br>6. Click the Pay Now button | User is redirected to the booking confirmation page with a reference number; an invoice is available for download, and a confirmation email is sent | high |
| TC-065 |  | Complete payment using PayPal | User is on the Payment page with a full booking summary displayed | 1. Select PayPal as the payment method<br>2. Click the Pay Now button<br>3. Log in to PayPal account with valid credentials<br>4. Confirm the payment | User is redirected to the booking confirmation page with a reference number; an invoice is available for download, and a confirmation email is sent | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-063 |  | Attempt payment with an expired credit card | User is on the Payment page with a full booking summary displayed | 1. Enter valid Cardholder Name<br>2. Enter a valid Card Number<br>3. Select an Expiration Date that is in the past<br>4. Enter a valid CVV<br>5. Click the Pay Now button | An error message is displayed indicating that the card is expired; the user remains on the payment page | high |
| TC-066 |  | Attempt payment with invalid credit card number | User is on the Payment page with a full booking summary displayed | 1. Enter valid Cardholder Name<br>2. Enter an invalid Card Number (e.g., 1234 5678 9012 3456)<br>3. Select a valid Expiration Date<br>4. Enter a valid CVV<br>5. Click the Pay Now button | An error message is displayed indicating that the card number is invalid; the user remains on the payment page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-064 |  | Complete payment with a credit card that has a zero balance | User is on the Payment page with a full booking summary displayed | 1. Enter valid Cardholder Name<br>2. Enter a valid Card Number with zero balance<br>3. Select a valid Expiration Date<br>4. Enter a valid CVV<br>5. Click the Pay Now button | An error message is displayed indicating 'Insufficient funds'; the user remains on the payment page | medium |

---

## Currency & Language Selection

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-067 |  | Select a different currency and verify price updates | User is on any page of the PHPTravels site | 1. Click on the currency selector dropdown<br>2. Select <desired currency> from the list<br>3. Observe the prices displayed on the page | All prices on the page are updated to reflect the selected currency without losing the current search context | high |
| TC-068 |  | Change the language and verify interface updates | User is on any page of the PHPTravels site | 1. Click on the language selector dropdown<br>2. Select <desired language> from the list<br>3. Observe the navigation labels and content on the page | The entire site interface updates to the selected language, including navigation labels and form content | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-069 |  | Select an unsupported currency | User is on any page of the PHPTravels site | 1. Click on the currency selector dropdown<br>2. Select <unsupported currency> from the list<br>3. Observe the prices displayed on the page | An error message is displayed indicating that the selected currency is not supported; prices remain unchanged | high |
| TC-070 |  | Select a language that is not available | User is on any page of the PHPTravels site | 1. Click on the language selector dropdown<br>2. Select <unsupported language> from the list<br>3. Observe the interface updates | An error message is displayed indicating that the selected language is not available; the interface remains in the current language | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-071 |  | Select a currency and language in quick succession | User is on any page of the PHPTravels site | 1. Click on the currency selector dropdown<br>2. Select <desired currency><br>3. Immediately click on the language selector dropdown<br>4. Select <desired language> | The site updates to reflect the selected currency and language without any errors or loss of context | medium |
| TC-072 |  | Change language and currency while logged in | User is logged into their account and on any page of the PHPTravels site | 1. Click on the currency selector dropdown<br>2. Select <desired currency><br>3. Click on the language selector dropdown<br>4. Select <desired language> | The site updates to reflect the selected currency and language, and the preferences are saved to the user's profile | medium |

---

## Search & Filters

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-073 |  | Apply multiple filters for hotel search and verify results | User is on the Hotels listing page | 1. Adjust the price range slider to select a range of $100 to $300<br>2. Select 4-star and 5-star ratings<br>3. Check the amenities for 'Free Wi-Fi' and 'Pool'<br>4. Click the Apply Filters button | Results update dynamically to show hotels within the selected price range and ratings, displaying only those with the selected amenities | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-074 |  | Attempt to apply filters with invalid input | User is on the Flights listing page | 1. Select 'One-way' as the trip type<br>2. Enter invalid departure and arrival cities (e.g., 'XYZ City')<br>3. Click the Apply Filters button | An error message is displayed indicating that the selected cities are invalid; no results are shown | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-075 |  | Apply maximum number of filters for car rentals | User is on the Cars listing page | 1. Select the car type as 'SUV'<br>2. Choose 'Automatic' for transmission<br>3. Select 'Full' for fuel policy<br>4. Choose a rental company from the list<br>5. Click the Apply Filters button | Results update to show available SUVs with automatic transmission, full fuel policy, and from the selected rental company; the result count updates accordingly | medium |
| TC-076 |  | Reset all filters and verify results | User has applied multiple filters on the Tours listing page | 1. Click the Reset all filters button | All filters are cleared, and the results revert to show all available tours without any filters applied | medium |

---

## Reviews & Ratings

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-077 |  | Submit a review with valid inputs after completing a booking | User is logged in and has completed a booking | 1. Navigate to the dashboard<br>2. Click on the 'Write a Review' button for the completed booking<br>3. Select a star rating for overall experience and for categories (Cleanliness, Service, Location)<br>4. Enter written feedback in the comments section<br>5. Optionally upload guest photos<br>6. Click the Submit button | The review is successfully submitted, and a confirmation message is displayed; the review appears in the Reviews section of the item | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-078 |  | Submit a review without selecting a rating | User is logged in and has completed a booking | 1. Navigate to the dashboard<br>2. Click on the 'Write a Review' button for the completed booking<br>3. Leave the star rating fields empty<br>4. Enter written feedback in the comments section<br>5. Click the Submit button | An error message is displayed indicating that a rating must be selected; the review is not submitted | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-079 |  | Submit a review with maximum character limit in comments | User is logged in and has completed a booking | 1. Navigate to the dashboard<br>2. Click on the 'Write a Review' button for the completed booking<br>3. Select a star rating for overall experience and for categories (Cleanliness, Service, Location)<br>4. Enter a comment that reaches the maximum character limit allowed<br>5. Click the Submit button | The review is successfully submitted, and a confirmation message is displayed; the review appears in the Reviews section of the item | medium |
| TC-080 |  | Filter reviews by date with no reviews available | User is on the detail page of an item with no reviews | 1. Scroll to the Reviews section<br>2. Select a date filter option (e.g., Last 30 days)<br>3. Click the Apply Filter button | A message is displayed indicating that no reviews are available for the selected date range | medium |

---

## Offers & Deals

Total: **5** (positive: 3, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-081 |  | View promotional banners and featured deal cards | User is on the Offers page | 1. Observe the promotional banners at the top of the page<br>2. Scroll down to view featured deal cards | Promotional banners and deal cards are displayed with titles, images, discount percentages, validity periods, and a Book Now button | high |
| TC-082 |  | Filter offers by service type and destination | User is on the Offers page | 1. Select 'Hotels' from the service type filter<br>2. Enter <destination> in the destination field<br>3. Click the Apply Filters button | The page refreshes to show only hotel offers for the selected destination | high |
| TC-085 |  | Click Book Now on a deal card | User is on the Offers page and sees available deals | 1. Click the Book Now button on a featured deal card | User is redirected to the booking flow with the promotional code applied or a pre-filled search with discounted rates | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-083 |  | Attempt to subscribe to the newsletter with an invalid email format | User is on the Offers page | 1. Enter 'invalid-email' in the newsletter subscription field<br>2. Click the Subscribe button | An error message is displayed indicating that the email format is invalid; subscription is not processed | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-084 |  | Filter offers with no results | User is on the Offers page | 1. Select 'Flights' from the service type filter<br>2. Enter a destination that has no available offers<br>3. Click the Apply Filters button | A message is displayed indicating that no offers are available for the selected criteria | medium |

---

## Logout

Total: **3** (positive: 1, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-086 |  | Logout successfully from the application | User is logged into the PHPTravels application | 1. Click the Logout button in the navigation menu | User is redirected to the home page; session is terminated and sensitive data is cleared | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-087 |  | Attempt to access a protected page after logout | User is logged into the PHPTravels application, User has logged out | 1. Try to navigate to a protected page (e.g., My Bookings) | User is redirected to the login page; access to the protected page is denied | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-088 |  | Logout while a session is still active and immediately try to refresh the page | User is logged into the PHPTravels application | 1. Click the Logout button in the navigation menu<br>2. Immediately refresh the page | User is redirected to the home page; session is terminated and sensitive data is cleared | medium |

---
