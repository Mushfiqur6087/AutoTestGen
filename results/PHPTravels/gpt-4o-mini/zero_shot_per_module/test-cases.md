# Test Cases — PHPTravels

Generated: 2026-06-04T15:04:51.301065Z  
Model: gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 21 | 133 | 34 | 48 | 51 | 76 | 46 | 11 |

## Home Page & Search

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Search for Hotels with valid inputs | User is on the home page, User selects the Hotels tab | 1. Enter destination as 'New York'<br>2. Select check-in date as '2023-12-01'<br>3. Select check-out date as '2023-12-05'<br>4. Enter number of rooms as '1'<br>5. Enter guest count as '2 adults, 1 child'<br>6. Click on the Search button | User is redirected to the Hotels results listing page with relevant results displayed. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Search for Hotels with missing destination | User is on the home page, User selects the Hotels tab | 1. Leave destination field empty<br>2. Select check-in date as '2023-12-01'<br>3. Select check-out date as '2023-12-05'<br>4. Enter number of rooms as '1'<br>5. Enter guest count as '2 adults, 1 child'<br>6. Click on the Search button | Inline error message appears indicating that the destination is required. | high |
| TC-004 |  | Search for Tours with invalid travel date range | User is on the home page, User selects the Tours tab | 1. Enter destination as 'Paris'<br>2. Select travel date range with start date '2023-12-10' and end date '2023-12-05'<br>3. Click on the Search button | Inline error message appears indicating that the end date must be after the start date. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Search for Flights with maximum passenger count | User is on the home page, User selects the Flights tab | 1. Select trip type as 'Round-trip'<br>2. Enter departure city as 'Los Angeles'<br>3. Enter arrival city as 'New York'<br>4. Select travel dates as '2023-12-01' to '2023-12-10'<br>5. Enter passenger count as '9 adults, 0 children, 0 infants'<br>6. Select cabin class as 'Economy'<br>7. Click on the Search button | User is redirected to the Flights results listing page with relevant results displayed. | medium |
| TC-005 |  | Search for Cars with empty pick-up and drop-off locations | User is on the home page, User selects the Cars tab | 1. Leave pick-up location empty<br>2. Leave drop-off location empty<br>3. Select pick-up date and time as '2023-12-01 10:00 AM'<br>4. Select drop-off date and time as '2023-12-05 10:00 AM'<br>5. Click on the Search button | Inline error messages appear indicating that both pick-up and drop-off locations are required. | high |

---

## User Registration

Total: **8** (positive: 1, negative: 4, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Successful registration with valid inputs |  | 1. Navigate to the registration page.<br>2. Fill in First Name, Last Name, Email, Password, Confirm Password, Mobile Number, Address, and select Country.<br>3. Check the Terms and Conditions checkbox.<br>4. Click on the Submit button. | User account is created, user is logged in and redirected to their dashboard. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 |  | Registration with missing required fields |  | 1. Navigate to the registration page.<br>2. Leave First Name and Email fields empty.<br>3. Fill in the rest of the fields with valid data.<br>4. Check the Terms and Conditions checkbox.<br>5. Click on the Submit button. | Inline error messages appear for First Name and Email fields indicating they are required. | high |
| TC-008 |  | Registration with non-matching passwords |  | 1. Navigate to the registration page.<br>2. Fill in First Name, Last Name, Email, Password, and a different Confirm Password.<br>3. Fill in the rest of the fields with valid data.<br>4. Check the Terms and Conditions checkbox.<br>5. Click on the Submit button. | Inline error message appears indicating that the passwords do not match. | high |
| TC-009 |  | Registration with invalid email format |  | 1. Navigate to the registration page.<br>2. Fill in First Name, Last Name, and an invalid Email format.<br>3. Fill in the rest of the fields with valid data.<br>4. Check the Terms and Conditions checkbox.<br>5. Click on the Submit button. | Inline error message appears indicating that the email format is invalid. | high |
| TC-010 |  | Registration with already registered email | An account with the email already exists. | 1. Navigate to the registration page.<br>2. Fill in First Name, Last Name, and the already registered Email.<br>3. Fill in the rest of the fields with valid data.<br>4. Check the Terms and Conditions checkbox.<br>5. Click on the Submit button. | Inline error message appears indicating that the email is already in use. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 |  | Registration with maximum length inputs |  | 1. Navigate to the registration page.<br>2. Fill in First Name and Last Name with maximum allowed characters.<br>3. Fill in a valid Email, Password, and Confirm Password with maximum allowed characters.<br>4. Fill in Mobile Number, Address, and select Country.<br>5. Check the Terms and Conditions checkbox.<br>6. Click on the Submit button. | User account is created successfully without any errors. | medium |
| TC-012 |  | Registration with empty fields |  | 1. Navigate to the registration page.<br>2. Leave all fields empty.<br>3. Click on the Submit button. | Inline error messages appear for all required fields indicating they are required. | high |
| TC-013 |  | Registration with only required fields filled |  | 1. Navigate to the registration page.<br>2. Fill in only First Name, Last Name, Email, Password, Confirm Password, and check the Terms and Conditions checkbox.<br>3. Click on the Submit button. | User account is created successfully, user is logged in and redirected to their dashboard. | medium |

---

## User Login

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-014 |  | Successful login with valid credentials | User has a registered account with valid email and password. | 1. Navigate to the login page.<br>2. Enter valid email in the Email field.<br>3. Enter valid password in the Password field.<br>4. Click on the Login button. | User is redirected to their dashboard or the page they were previously trying to access. | high |
| TC-019 |  | Successful login with Remember Me option checked | User has a registered account with valid email and password. | 1. Navigate to the login page.<br>2. Enter valid email in the Email field.<br>3. Enter valid password in the Password field.<br>4. Check the Remember Me checkbox.<br>5. Click on the Login button. | User is redirected to their dashboard, and their login information is remembered for future sessions. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 |  | Unsuccessful login with invalid credentials | User is on the login page. | 1. Enter invalid email in the Email field.<br>2. Enter invalid password in the Password field.<br>3. Click on the Login button. | An error message is displayed, and the password field is cleared. | high |
| TC-016 |  | Unsuccessful login with empty fields | User is on the login page. | 1. Leave the Email field empty.<br>2. Leave the Password field empty.<br>3. Click on the Login button. | An error message is displayed indicating that fields cannot be empty. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-017 |  | Login with maximum length email and password | User has a registered account with maximum length email and password. | 1. Enter a maximum length email in the Email field.<br>2. Enter a maximum length password in the Password field.<br>3. Click on the Login button. | User is redirected to their dashboard or the page they were previously trying to access. | medium |
| TC-018 |  | Login after multiple failed attempts triggering CAPTCHA | User has entered invalid credentials multiple times. | 1. Enter invalid email in the Email field.<br>2. Enter invalid password in the Password field.<br>3. Click on the Login button multiple times to trigger CAPTCHA.<br>4. Complete CAPTCHA verification if prompted. | User is either allowed to attempt login again after CAPTCHA or receives an error message if CAPTCHA is not completed. | low |

---

## Forgot Password

Total: **5** (positive: 1, negative: 1, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-020 |  | Valid email submission | User is on the Forgot Password page, User has a registered email address | 1. Enter a valid registered email address in the Email field<br>2. Click the Reset Password button | A confirmation message is shown, and a reset link is sent to the email address. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-021 |  | Invalid email submission | User is on the Forgot Password page | 1. Enter an unregistered email address in the Email field<br>2. Click the Reset Password button | An error message is displayed indicating the email is not found, and the form remains editable. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-022 |  | Empty email field submission | User is on the Forgot Password page | 1. Leave the Email field empty<br>2. Click the Reset Password button | An error message is displayed indicating that the email field cannot be empty, and the form remains editable. | medium |
| TC-023 |  | Email field with maximum length | User is on the Forgot Password page | 1. Enter an email address that is at the maximum allowed length (e.g., 254 characters)<br>2. Click the Reset Password button | A confirmation message is shown, and a reset link is sent to the email address if it exists. | medium |
| TC-024 |  | Email field with special characters | User is on the Forgot Password page | 1. Enter an email address with special characters (e.g., test.email+filter@example.com)<br>2. Click the Reset Password button | A confirmation message is shown, and a reset link is sent to the email address if it exists. | medium |

---

## Hotels Search & Listing

Total: **8** (positive: 2, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-025 |  | Successful hotel search with valid inputs | User is on the hotels search page | 1. Enter a valid destination.<br>2. Select valid check-in and check-out dates.<br>3. Specify the number of rooms and guest count (adults and children).<br>4. Click on the 'Search' button. | User is redirected to the listing page showing hotel cards with details. | high |
| TC-030 |  | Filter results by price range | User is on the listing page with search results | 1. Expand the price range filter in the left sidebar.<br>2. Set a specific price range.<br>3. Click on the 'Apply' button. | The listing updates to show only hotels within the specified price range. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-026 |  | Search with missing destination | User is on the hotels search page | 1. Leave the destination field empty.<br>2. Select valid check-in and check-out dates.<br>3. Specify the number of rooms and guest count (adults and children).<br>4. Click on the 'Search' button. | An error message is displayed indicating that the destination is required. | high |
| TC-027 |  | Search with invalid check-out date | User is on the hotels search page | 1. Enter a valid destination.<br>2. Select a check-in date.<br>3. Select a check-out date that is before the check-in date.<br>4. Specify the number of rooms and guest count (adults and children).<br>5. Click on the 'Search' button. | An error message is displayed indicating that the check-out date must be after the check-in date. | high |
| TC-031 |  | Filter results with invalid star rating | User is on the listing page with search results | 1. Expand the star rating filter in the left sidebar.<br>2. Select an invalid star rating (e.g., a non-numeric value).<br>3. Click on the 'Apply' button. | An error message is displayed indicating that the star rating is invalid. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-028 |  | Search with maximum number of guests | User is on the hotels search page | 1. Enter a valid destination.<br>2. Select valid check-in and check-out dates.<br>3. Specify the maximum number of rooms allowed.<br>4. Set the guest count to the maximum allowed (e.g., 10 adults, 10 children).<br>5. Click on the 'Search' button. | User is redirected to the listing page showing hotel cards with details. | medium |
| TC-029 |  | Search with empty fields | User is on the hotels search page | 1. Leave all fields (destination, dates, rooms, guest count) empty.<br>2. Click on the 'Search' button. | An error message is displayed indicating that all fields are required. | high |
| TC-032 |  | Reset all filters | User is on the listing page with active filters | 1. Click on the 'Reset all' button in the filters section. | All active filters are cleared, and the original search results are displayed. | low |

---

## Hotel Details & Booking

Total: **6** (positive: 1, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-033 |  | Successful room booking with valid details | User is logged in, User has selected a room | 1. Navigate to the hotel details page.<br>2. Select a room type.<br>3. Fill in the booking form with valid First Name, Last Name, Email, Phone Number, and optional Special Requests.<br>4. Click on 'Book Now'. | User is redirected to the payment page with booking details displayed. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-034 |  | Booking attempt without being logged in | User has selected a room | 1. Navigate to the hotel details page.<br>2. Select a room type.<br>3. Click on 'Book Now' without logging in. | User sees an error message prompting them to log in. | high |
| TC-035 |  | Booking attempt with missing required fields | User is logged in, User has selected a room | 1. Navigate to the hotel details page.<br>2. Select a room type.<br>3. Fill in the booking form with missing First Name and Last Name.<br>4. Click on 'Book Now'. | User sees an error message indicating that First Name and Last Name are required. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-036 |  | Booking with maximum length input | User is logged in, User has selected a room | 1. Navigate to the hotel details page.<br>2. Select a room type.<br>3. Fill in the booking form with First Name and Last Name of maximum allowed length (e.g., 50 characters).<br>4. Fill in a valid Email and Phone Number.<br>5. Click on 'Book Now'. | User is redirected to the payment page with booking details displayed. | medium |
| TC-037 |  | Booking with special requests exceeding character limit | User is logged in, User has selected a room | 1. Navigate to the hotel details page.<br>2. Select a room type.<br>3. Fill in the booking form with valid First Name, Last Name, Email, Phone Number.<br>4. Enter a Special Request that exceeds the character limit (e.g., 256 characters).<br>5. Click on 'Book Now'. | User sees an error message indicating that the Special Request exceeds the character limit. | medium |
| TC-038 |  | Booking with empty fields | User is logged in, User has selected a room | 1. Navigate to the hotel details page.<br>2. Select a room type.<br>3. Leave all fields in the booking form empty.<br>4. Click on 'Book Now'. | User sees error messages indicating that all fields are required. | high |

---

## Flights Search & Listing

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-039 |  | Successful one-way flight search | User is on the flights search page | 1. Select trip type as 'One-way'.<br>2. Enter departure city as 'New York'.<br>3. Enter arrival city as 'Los Angeles'.<br>4. Select travel date as '2023-12-15'.<br>5. Set passenger count: 1 adult, 0 children, 0 infants.<br>6. Select cabin class as 'Economy'.<br>7. Click on the 'Search Flights' button. | User is redirected to the listing page showing available flights. | high |
| TC-044 |  | Successful round-trip flight search | User is on the flights search page | 1. Select trip type as 'Round-trip'.<br>2. Enter departure city as 'Boston'.<br>3. Enter arrival city as 'Miami'.<br>4. Select departure date as '2023-12-01' and return date as '2023-12-10'.<br>5. Set passenger count: 2 adults, 1 child.<br>6. Select cabin class as 'Premium Economy'.<br>7. Click on the 'Search Flights' button. | User is redirected to the listing page showing available round-trip flights. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-040 |  | Search with missing departure city | User is on the flights search page | 1. Select trip type as 'Round-trip'.<br>2. Leave departure city field empty.<br>3. Enter arrival city as 'Chicago'.<br>4. Select travel dates.<br>5. Set passenger count.<br>6. Select cabin class.<br>7. Click on the 'Search Flights' button. | An error message is displayed indicating that the departure city is required. | high |
| TC-041 |  | Search with invalid travel dates | User is on the flights search page | 1. Select trip type as 'Multi-city'.<br>2. Enter departure city as 'Miami'.<br>3. Enter arrival city as 'Toronto'.<br>4. Select travel date as '2023-02-30'.<br>5. Set passenger count.<br>6. Select cabin class.<br>7. Click on the 'Search Flights' button. | An error message is displayed indicating that the travel date is invalid. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-042 |  | Search with maximum passenger count | User is on the flights search page | 1. Select trip type as 'Round-trip'.<br>2. Enter departure city as 'San Francisco'.<br>3. Enter arrival city as 'Seattle'.<br>4. Select travel dates.<br>5. Set passenger count: 9 adults, 0 children, 0 infants.<br>6. Select cabin class as 'Business'.<br>7. Click on the 'Search Flights' button. | User is redirected to the listing page showing available flights for 9 passengers. | medium |
| TC-043 |  | Search with empty fields | User is on the flights search page | 1. Leave all fields empty.<br>2. Click on the 'Search Flights' button. | An error message is displayed indicating that all fields are required. | high |

---

## Flight Booking

Total: **0** (positive: 0, negative: 0, edge: 0)

---

## Tours Search & Listing

Total: **7** (positive: 2, negative: 3, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-045 |  | Successful search with valid inputs | User is on the tours search page. | 1. Enter a valid destination.<br>2. Select valid travel dates.<br>3. Choose a tour type.<br>4. Specify duration.<br>5. Set a budget range.<br>6. Click on the search button. | User is redirected to the listing page showing relevant tours. | high |
| TC-050 |  | Filter results by price range | User is on the listing page with search results. | 1. Set a price range using the sidebar filter.<br>2. Click on the apply filter button. | The listing updates to show only tours within the specified price range. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-046 |  | Search with missing destination | User is on the tours search page. | 1. Leave the destination field empty.<br>2. Select valid travel dates.<br>3. Choose a tour type.<br>4. Specify duration.<br>5. Set a budget range.<br>6. Click on the search button. | An error message is displayed indicating that the destination is required. | high |
| TC-047 |  | Search with invalid travel dates | User is on the tours search page. | 1. Enter a valid destination.<br>2. Select an end date that is before the start date.<br>3. Choose a tour type.<br>4. Specify duration.<br>5. Set a budget range.<br>6. Click on the search button. | An error message is displayed indicating that the travel dates are invalid. | high |
| TC-051 |  | Filter results with invalid price range | User is on the listing page with search results. | 1. Set a price range where the minimum is greater than the maximum.<br>2. Click on the apply filter button. | An error message is displayed indicating that the price range is invalid. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-048 |  | Search with maximum length inputs | User is on the tours search page. | 1. Enter a destination with maximum allowed characters.<br>2. Select valid travel dates.<br>3. Choose a tour type.<br>4. Specify maximum duration.<br>5. Set a budget range with maximum values.<br>6. Click on the search button. | User is redirected to the listing page showing relevant tours. | medium |
| TC-049 |  | Search with empty fields | User is on the tours search page. | 1. Leave all fields empty.<br>2. Click on the search button. | An error message is displayed indicating that all fields are required. | high |

---

## Tour Details & Booking

Total: **6** (positive: 1, negative: 3, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-052 |  | Successful booking with valid inputs | User is on the tour details page, User is authenticated | 1. Select a departure date<br>2. Specify number of travelers (2 adults, 1 child)<br>3. Click 'Book Now'<br>4. Fill in traveler names and contact details<br>5. Submit the booking form | Booking confirmation page is displayed with total cost breakdown | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-053 |  | Booking attempt without selecting a departure date | User is on the tour details page, User is authenticated | 1. Leave the departure date field empty<br>2. Specify number of travelers (1 adult)<br>3. Click 'Book Now' | Error message indicating that a departure date must be selected | high |
| TC-054 |  | Booking attempt with invalid contact details | User is on the tour details page, User is authenticated | 1. Select a departure date<br>2. Specify number of travelers (1 adult)<br>3. Click 'Book Now'<br>4. Fill in traveler names and provide invalid contact details (e.g., missing '@')<br>5. Submit the booking form | Error message indicating that the contact details are invalid | high |
| TC-057 |  | Unauthenticated user attempts to book a tour | User is on the tour details page, User is not logged in | 1. Select a departure date<br>2. Specify number of travelers (1 adult)<br>3. Click 'Book Now' | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-055 |  | Booking with maximum number of travelers | User is on the tour details page, User is authenticated | 1. Select a departure date<br>2. Specify number of travelers (10 adults, 5 children)<br>3. Click 'Book Now'<br>4. Fill in traveler names and contact details<br>5. Submit the booking form | Booking confirmation page is displayed with total cost breakdown for maximum travelers | medium |
| TC-056 |  | Booking with special requirements field left empty | User is on the tour details page, User is authenticated | 1. Select a departure date<br>2. Specify number of travelers (1 adult)<br>3. Click 'Book Now'<br>4. Fill in traveler names and contact details<br>5. Leave special requirements field empty<br>6. Submit the booking form | Booking confirmation page is displayed with total cost breakdown, special requirements are optional | low |

---

## Cars Search & Listing

Total: **7** (positive: 2, negative: 3, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-058 |  | Valid search with all fields filled | User is on the car rental search page | 1. Enter a valid pick-up location.<br>2. Enter a valid drop-off location.<br>3. Select a valid pick-up date and time.<br>4. Select a valid drop-off date and time.<br>5. Enter a valid driver age. | User is redirected to the listing page with relevant car listings displayed. | high |
| TC-063 |  | Filter results by car type | User is on the listing page with results displayed | 1. Select a car type filter (e.g., Economy). | The listing updates to show only Economy cars. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-059 |  | Search with missing pick-up location | User is on the car rental search page | 1. Leave the pick-up location field empty.<br>2. Enter a valid drop-off location.<br>3. Select valid pick-up and drop-off dates and times.<br>4. Enter a valid driver age. | An error message is displayed indicating that the pick-up location is required. | high |
| TC-060 |  | Search with invalid driver age | User is on the car rental search page | 1. Enter a valid pick-up location.<br>2. Enter a valid drop-off location.<br>3. Select valid pick-up and drop-off dates and times.<br>4. Enter an invalid driver age (e.g., below minimum age). | An error message is displayed indicating that the driver must meet the minimum age requirement. | high |
| TC-064 |  | Filter results with no available cars | User is on the listing page with results displayed | 1. Select a filter that has no available cars. | A message is displayed indicating that no cars are available for the selected filters. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-061 |  | Search with maximum length inputs | User is on the car rental search page | 1. Enter a pick-up location with maximum allowed characters.<br>2. Enter a drop-off location with maximum allowed characters.<br>3. Select valid pick-up and drop-off dates and times.<br>4. Enter a valid driver age. | User is redirected to the listing page with relevant car listings displayed. | medium |
| TC-062 |  | Search with empty fields | User is on the car rental search page | 1. Leave all fields empty. | An error message is displayed indicating that all fields are required. | high |

---

## Car Booking

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-065 |  | Successful car booking with valid details | User is on the car booking page, User has selected a vehicle and rental period | 1. Enter valid driver full name.<br>2. Enter valid age (e.g., 30).<br>3. Enter valid license number.<br>4. Select license issue country.<br>5. Enter valid email address.<br>6. Enter valid phone number.<br>7. Select insurance plan.<br>8. Accept terms and conditions.<br>9. Click Confirm Booking. | User is redirected to the payment page with a confirmation message. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-066 |  | Booking with missing driver full name | User is on the car booking page, User has selected a vehicle and rental period | 1. Leave driver full name field empty.<br>2. Enter valid age.<br>3. Enter valid license number.<br>4. Select license issue country.<br>5. Enter valid email address.<br>6. Enter valid phone number.<br>7. Select insurance plan.<br>8. Accept terms and conditions.<br>9. Click Confirm Booking. | Inline error message displayed for missing driver full name, and booking is blocked. | high |
| TC-067 |  | Booking with invalid email format | User is on the car booking page, User has selected a vehicle and rental period | 1. Enter valid driver full name.<br>2. Enter valid age.<br>3. Enter valid license number.<br>4. Select license issue country.<br>5. Enter invalid email address (e.g., 'user@domain').<br>6. Enter valid phone number.<br>7. Select insurance plan.<br>8. Accept terms and conditions.<br>9. Click Confirm Booking. | Inline error message displayed for invalid email format, and booking is blocked. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-068 |  | Booking with maximum length fields | User is on the car booking page, User has selected a vehicle and rental period | 1. Enter a driver full name with maximum allowed characters.<br>2. Enter age as 100.<br>3. Enter a license number with maximum allowed characters.<br>4. Select license issue country.<br>5. Enter a valid email address with maximum allowed characters.<br>6. Enter a valid phone number with maximum allowed digits.<br>7. Select insurance plan.<br>8. Accept terms and conditions.<br>9. Click Confirm Booking. | User is redirected to the payment page with a confirmation message. | medium |
| TC-069 |  | Booking with empty fields | User is on the car booking page, User has selected a vehicle and rental period | 1. Leave all fields empty.<br>2. Click Confirm Booking. | Inline error messages displayed for all required fields, and booking is blocked. | high |

---

## Visa Services

Total: **8** (positive: 2, negative: 4, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-070 |  | Valid visa requirement retrieval | User is on the Visa Services page | 1. Select a valid Nationality from the dropdown<br>2. Select a valid Destination Country from the dropdown<br>3. Click on 'View Visa Requirements' button | The system displays the visa requirements including visa type, processing time, required documents, and fees. | high |
| TC-076 |  | Successful document upload | User is on the document upload section of the visa application form | 1. Upload a valid passport copy file<br>2. Click on 'Upload' button | The system confirms that the document has been uploaded successfully. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-071 |  | Invalid nationality selection | User is on the Visa Services page | 1. Select an invalid Nationality from the dropdown<br>2. Select a valid Destination Country from the dropdown<br>3. Click on 'View Visa Requirements' button | The system shows an error message indicating that the nationality is invalid. | high |
| TC-072 |  | Missing required fields in visa application form | User is on the visa application form | 1. Leave all fields empty<br>2. Click on 'Submit' button | The system displays error messages for all required fields indicating they cannot be empty. | high |
| TC-075 |  | Invalid file type upload | User is on the document upload section of the visa application form | 1. Attempt to upload a file with an unsupported file type (e.g., .exe)<br>2. Click on 'Upload' button | The system shows an error message indicating that the file type is not supported. | high |
| TC-077 |  | Invalid email format | User is on the visa application form | 1. Enter an invalid email format (e.g., 'user@domain')<br>2. Click on 'Submit' button | The system shows an error message indicating that the email format is invalid. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-073 |  | Maximum length input for personal information | User is on the visa application form | 1. Enter a full name with 255 characters<br>2. Enter a passport number with 20 characters<br>3. Enter a valid passport expiry date<br>4. Enter a valid date of birth<br>5. Enter a valid email address<br>6. Enter a valid phone number<br>7. Click on 'Submit' button | The system accepts the input and submits the application successfully. | medium |
| TC-074 |  | Boundary values for travel dates | User is on the visa application form | 1. Enter intended travel dates that are exactly one year from today<br>2. Enter a duration of stay of 365 days<br>3. Click on 'Submit' button | The system accepts the input and submits the application successfully. | medium |

---

## User Dashboard

Total: **10** (positive: 3, negative: 4, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-078 |  | View details of a confirmed booking | User is logged in, User has at least one confirmed booking | 1. Navigate to My Bookings section<br>2. Click on 'View Details' for a confirmed booking | User sees detailed information about the booking including reference, service type, travel dates, and status. | high |
| TC-081 |  | Edit user profile information | User is logged in, User is on My Profile section | 1. Click on 'Edit' button<br>2. Update personal information<br>3. Save changes | User sees a confirmation message that the profile has been updated successfully. | high |
| TC-084 |  | Add a review for a completed booking | User is logged in, User has completed bookings | 1. Navigate to Reviews section<br>2. Select a completed booking<br>3. Rate and write a review<br>4. Submit the review | User sees a confirmation message that the review has been submitted successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-079 |  | Attempt to cancel a booking that cannot be canceled | User is logged in, User has a booking that is not eligible for cancellation | 1. Navigate to My Bookings section<br>2. Click on 'Cancel' for the non-cancellable booking | User sees an error message indicating that the booking cannot be canceled. | high |
| TC-082 |  | Attempt to save profile with empty required fields | User is logged in, User is on My Profile section | 1. Click on 'Edit' button<br>2. Leave required fields empty<br>3. Click on 'Save' | User sees an error message indicating that required fields cannot be empty. | high |
| TC-085 |  | Submit a review without a rating | User is logged in, User has completed bookings | 1. Navigate to Reviews section<br>2. Select a completed booking<br>3. Leave rating empty and write a review<br>4. Submit the review | User sees an error message indicating that a rating must be provided. | high |
| TC-087 |  | Logout without saving changes | User is logged in, User has unsaved changes in profile or settings | 1. Click on 'Logout' | User is logged out, and unsaved changes are lost without any warning. | low |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-080 |  | View details of a booking with maximum length reference | User is logged in, User has a booking with maximum length reference number | 1. Navigate to My Bookings section<br>2. Click on 'View Details' for the booking with maximum length reference | User sees detailed information about the booking without any layout issues. | medium |
| TC-083 |  | View transaction history with maximum length description | User is logged in, User has transactions with maximum length descriptions | 1. Navigate to Wallet/Credits section<br>2. View full transaction history | User sees the transaction history displayed correctly without truncation or layout issues. | medium |
| TC-086 |  | Change password with maximum length input | User is logged in, User is on Settings section | 1. Click on 'Change Password'<br>2. Enter maximum length password<br>3. Confirm the new password<br>4. Save changes | User sees a confirmation message that the password has been changed successfully. | medium |

---

## Booking Management

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-088 |  | View booking details successfully | User is logged in, User has an existing booking | 1. Navigate to the booking management page.<br>2. Select a booking from the list. | The booking details view displays confirmation number, service information, traveler details, payment information, and current booking status. | high |
| TC-089 |  | Modify booking details successfully | User is logged in, User has an existing booking with modify permissions | 1. Navigate to the booking management page.<br>2. Select a booking from the list.<br>3. Click on the Modify button.<br>4. Change travel dates and add special requests.<br>5. Submit the changes. | The booking is updated successfully, and a confirmation message is displayed. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-090 |  | Attempt to modify booking without permissions | User is logged in, User has an existing booking without modify permissions | 1. Navigate to the booking management page.<br>2. Select a booking from the list.<br>3. Attempt to click on the Modify button. | The Modify button is disabled or an error message is displayed indicating that modification is not allowed. | high |
| TC-091 |  | Cancel booking without confirmation | User is logged in, User has an existing booking | 1. Navigate to the booking management page.<br>2. Select a booking from the list.<br>3. Click on the Cancel button. | A cancellation confirmation flow is displayed, and the booking is not canceled until the user confirms. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-092 |  | Modify booking with maximum length special requests | User is logged in, User has an existing booking with modify permissions | 1. Navigate to the booking management page.<br>2. Select a booking from the list.<br>3. Click on the Modify button.<br>4. Enter a special request with maximum allowed characters.<br>5. Submit the changes. | The booking is updated successfully, and a confirmation message is displayed. | medium |
| TC-093 |  | Cancel booking with no refund applicable | User is logged in, User has an existing booking with no refund policy | 1. Navigate to the booking management page.<br>2. Select a booking from the list.<br>3. Click on the Cancel button.<br>4. Confirm the cancellation. | The booking is canceled, and a message indicates that no refund will be processed. | medium |

---

## Payment Processing

Total: **7** (positive: 2, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-094 |  | Successful payment with valid credit card | User is on the payment page, User has a valid credit card | 1. Enter valid cardholder name<br>2. Enter valid card number<br>3. Enter valid expiration date<br>4. Enter valid CVV<br>5. Click on 'Pay Now' button | User is redirected to the booking confirmation page with a reference number and options to download the invoice or voucher. | high |
| TC-100 |  | Successful payment using PayPal | User is on the payment page, User has a valid PayPal account | 1. Select PayPal as the payment method<br>2. Click on 'Pay Now' button<br>3. Log in to PayPal account<br>4. Confirm payment | User is redirected to the booking confirmation page with a reference number and options to download the invoice or voucher. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-095 |  | Payment failure due to card decline | User is on the payment page, User has a card that is known to be declined | 1. Enter valid cardholder name<br>2. Enter declined card number<br>3. Enter valid expiration date<br>4. Enter valid CVV<br>5. Click on 'Pay Now' button | An error message 'Card declined' is displayed, and the user can retry without losing booking details. | high |
| TC-096 |  | Payment failure due to insufficient funds | User is on the payment page, User has a card with insufficient funds | 1. Enter valid cardholder name<br>2. Enter card number with insufficient funds<br>3. Enter valid expiration date<br>4. Enter valid CVV<br>5. Click on 'Pay Now' button | An error message 'Insufficient funds' is displayed, and the user can retry without losing booking details. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-097 |  | Payment with maximum length cardholder name | User is on the payment page | 1. Enter a cardholder name with maximum allowed characters<br>2. Enter valid card number<br>3. Enter valid expiration date<br>4. Enter valid CVV<br>5. Click on 'Pay Now' button | User is redirected to the booking confirmation page with a reference number and options to download the invoice or voucher. | medium |
| TC-098 |  | Payment with empty card number | User is on the payment page | 1. Enter valid cardholder name<br>2. Leave card number field empty<br>3. Enter valid expiration date<br>4. Enter valid CVV<br>5. Click on 'Pay Now' button | An error message indicating that the card number is required is displayed. | high |
| TC-099 |  | Payment with expired card | User is on the payment page | 1. Enter valid cardholder name<br>2. Enter valid card number<br>3. Enter an expired expiration date<br>4. Enter valid CVV<br>5. Click on 'Pay Now' button | An error message indicating that the card is expired is displayed. | high |

---

## Currency & Language Selection

Total: **8** (positive: 2, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-101 |  | Select a valid currency | User is on the homepage, User is authenticated | 1. Click on the currency selector<br>2. Choose 'USD' from the dropdown menu | All prices on the site are updated to USD without losing the current search context. | high |
| TC-102 |  | Select a valid language | User is on the homepage, User is authenticated | 1. Click on the language selector<br>2. Choose 'Spanish' from the dropdown menu | The entire site interface is switched to Spanish. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-103 |  | Select an invalid currency | User is on the homepage, User is authenticated | 1. Click on the currency selector<br>2. Choose 'InvalidCurrency' from the dropdown menu | An error message is displayed indicating that the currency selection is invalid. | medium |
| TC-104 |  | Select an invalid language | User is on the homepage, User is authenticated | 1. Click on the language selector<br>2. Choose 'InvalidLanguage' from the dropdown menu | An error message is displayed indicating that the language selection is invalid. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-105 |  | Select currency with maximum length | User is on the homepage, User is authenticated | 1. Click on the currency selector<br>2. Enter a currency code with maximum allowed length (e.g., 'CURR12345') | The system accepts the input but displays an error message indicating that the currency code is not recognized. | low |
| TC-106 |  | Select language with maximum length | User is on the homepage, User is authenticated | 1. Click on the language selector<br>2. Enter a language code with maximum allowed length (e.g., 'LANGUAGE12345') | The system accepts the input but displays an error message indicating that the language code is not recognized. | low |
| TC-107 |  | Select currency with empty input | User is on the homepage, User is authenticated | 1. Click on the currency selector<br>2. Leave the selection empty | An error message is displayed indicating that a currency must be selected. | low |
| TC-108 |  | Select language with empty input | User is on the homepage, User is authenticated | 1. Click on the language selector<br>2. Leave the selection empty | An error message is displayed indicating that a language must be selected. | low |

---

## Search & Filters

Total: **7** (positive: 2, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-109 |  | Apply valid price range filter | User is on the listing page, There are listings available | 1. Locate the price range slider<br>2. Adjust the slider to a valid range<br>3. Observe the results grid | The results grid updates to show listings within the selected price range, and the result count reflects the number of listings. | high |
| TC-110 |  | Select multiple filters for Hotels | User is on the Hotels listing page, There are listings available | 1. Expand the facilities/amenities filter<br>2. Select multiple amenities<br>3. Click on the apply button<br>4. Observe the results grid | The results grid updates to show only hotels that match the selected amenities, and the result count reflects the number of listings. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-111 |  | Apply invalid price range filter | User is on the listing page | 1. Locate the price range slider<br>2. Adjust the slider to an invalid range (e.g., min > max)<br>3. Observe the results grid | An error message is displayed indicating that the price range is invalid, and the results grid remains unchanged. | high |
| TC-112 |  | Select no filters and expect all results | User is on the listing page, There are listings available | 1. Ensure no filters are selected<br>2. Click on the apply button<br>3. Observe the results grid | The results grid displays all available listings, and the result count reflects the total number of listings. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-113 |  | Apply maximum length filter for car type | User is on the Cars listing page, There are listings available | 1. Expand the car type filter<br>2. Enter a car type name at maximum character length<br>3. Click on the apply button<br>4. Observe the results grid | The results grid updates to show listings that match the maximum length car type entered, and the result count reflects the number of listings. | medium |
| TC-114 |  | Reset all filters | User has applied multiple filters, User is on the listing page | 1. Click on the 'Reset all filters' button<br>2. Observe the results grid | All filters are cleared, and the results grid displays all available listings, with the result count reflecting the total number of listings. | medium |
| TC-115 |  | Apply filter with empty fields | User is on the listing page | 1. Leave all filter fields empty<br>2. Click on the apply button<br>3. Observe the results grid | An error message is displayed indicating that filters cannot be empty, and the results grid remains unchanged. | low |

---

## Reviews & Ratings

Total: **6** (positive: 1, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-116 |  | Submit a valid review with all required fields | User is authenticated, User has completed a booking | 1. Navigate to the dashboard.<br>2. Click on 'Submit a Review'.<br>3. Fill in the overall rating and category-specific ratings.<br>4. Enter written comments.<br>5. Click 'Submit'. | The review is submitted successfully, and a confirmation message is displayed. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-117 |  | Submit a review without required fields | User is authenticated, User has completed a booking | 1. Navigate to the dashboard.<br>2. Click on 'Submit a Review'.<br>3. Leave the overall rating blank.<br>4. Click 'Submit'. | An error message is displayed indicating that the overall rating is required. | high |
| TC-118 |  | Submit a review as an unauthenticated user | User is not logged in | 1. Navigate to the review submission page.<br>2. Attempt to fill in the review form.<br>3. Click 'Submit'. | An error message is displayed indicating that the user must be logged in to submit a review. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-119 |  | Submit a review with maximum character limit for comments | User is authenticated, User has completed a booking | 1. Navigate to the dashboard.<br>2. Click on 'Submit a Review'.<br>3. Fill in the overall rating and category-specific ratings.<br>4. Enter a comment with the maximum allowed characters.<br>5. Click 'Submit'. | The review is submitted successfully, and a confirmation message is displayed. | medium |
| TC-120 |  | Filter reviews by date with no reviews available | User is on the detail page of an item with no reviews | 1. Navigate to the Reviews section.<br>2. Select a date filter.<br>3. Click 'Apply Filter'. | A message is displayed indicating that no reviews are available for the selected date. | medium |
| TC-121 |  | Filter reviews by rating with all ratings available | User is on the detail page of an item with multiple reviews | 1. Navigate to the Reviews section.<br>2. Select a specific rating filter (e.g., 5 stars).<br>3. Click 'Apply Filter'. | Only reviews with the selected rating are displayed. | medium |

---

## Offers & Deals

Total: **8** (positive: 3, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-122 |  | View promotional banners and deal cards | User is on the Offers page | 1. Load the Offers page.<br>2. Observe the promotional banners and deal cards. | Promotional banners and deal cards are displayed with correct titles, images, discount percentages, validity periods, and Terms and Conditions links. | high |
| TC-123 |  | Filter offers by service type | User is on the Offers page | 1. Select 'Hotels' from the service type filter.<br>2. Observe the displayed offers. | Only hotel offers are displayed. | high |
| TC-124 |  | Subscribe to newsletter with valid email | User is on the Offers page | 1. Enter a valid email address in the newsletter subscription field.<br>2. Click the 'Subscribe' button. | User receives a confirmation message indicating successful subscription. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-125 |  | Subscribe to newsletter with invalid email | User is on the Offers page | 1. Enter an invalid email address in the newsletter subscription field.<br>2. Click the 'Subscribe' button. | An error message is displayed indicating the email address is invalid. | high |
| TC-126 |  | Attempt to book without selecting an offer | User is on the Offers page | 1. Click the 'Book Now' button without selecting any offer. | An error message is displayed indicating that an offer must be selected to proceed. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-127 |  | Filter offers with maximum length destination input | User is on the Offers page | 1. Enter a destination with the maximum allowed character length in the filter.<br>2. Click the filter button. | Offers are filtered based on the maximum length destination input without errors. | low |
| TC-128 |  | Submit newsletter subscription with empty email | User is on the Offers page | 1. Leave the email field empty.<br>2. Click the 'Subscribe' button. | An error message is displayed indicating that the email field cannot be empty. | medium |
| TC-129 |  | Click Book Now on a deal with no validity period | User is on the Offers page and sees a deal with no validity period | 1. Click the 'Book Now' button for the deal. | User is redirected to the booking flow with the promotional code applied, despite the missing validity period. | low |

---

## Logout

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-130 |  | Successful Logout | User is logged into the application. | 1. Click on the Logout button. | User is redirected to the home page and session data is cleared. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-131 |  | Access Protected Page After Logout | User is logged out. | 1. Attempt to access a protected page. | User is redirected to the login page. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-132 |  | Logout While Session is Already Expired | User's session has expired. | 1. Click on the Logout button. | User is redirected to the home page without any error. | medium |
| TC-133 |  | Logout with Multiple Concurrent Sessions | User is logged in from multiple devices. | 1. Click on the Logout button from one device. | User is logged out from that device, but remains logged in on other devices. | medium |

---
