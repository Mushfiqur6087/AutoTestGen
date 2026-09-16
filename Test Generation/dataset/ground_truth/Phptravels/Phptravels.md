# PHPTravels Test Cases

**Website URL:** https://phptravels.com/demo
**Test Suite Version:** 1.0

---

## Table of Contents
1. [Home Page And Search](#1-home-page-and-search)
2. [Registration](#2-registration)
3. [Login](#3-login)
4. [Forgot Password](#4-forgot-password)
5. [Hotels Search And Listing](#5-hotels-search-and-listing)
6. [Hotel Details And Booking](#6-hotel-details-and-booking)
7. [Flights Search And Booking](#7-flights-search-and-booking)
8. [Tours Search And Booking](#8-tours-search-and-booking)
9. [Cars Search And Booking](#9-cars-search-and-booking)
10. [Visa Services](#10-visa-services)
11. [User Dashboard And Booking Management](#11-user-dashboard-and-booking-management)
12. [Payment Processing](#12-payment-processing)
13. [Currency And Language Selection](#13-currency-and-language-selection)
14. [Search And Filters](#14-search-and-filters)
15. [Reviews And Ratings](#15-reviews-and-ratings)
16. [Offers And Deals](#16-offers-and-deals)
17. [Logout](#17-logout)

---

## 1. Home Page And Search

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HOME-001 | Search widget with Hotels/Flights/Tours/Cars tabs is visible and functional | None | 1. Navigate to the PHPTravels home page<br>2. Select each of the Hotels, Flights, Tours, and Cars tabs | Each tab's search form fields are visible and accept input; searches can be submitted from every tab | High |
| HOME-002 | Hotel search from home page | None | 1. Select the Hotels tab<br>2. Enter destination<br>3. Select valid check-in and check-out dates<br>4. Set guests and rooms<br>5. Click "Search" | User is redirected to the hotel listing page with matching search criteria summary | High |
| HOME-003 | Flight search from home page | None | 1. Select the Flights tab<br>2. Enter origin and destination<br>3. Select valid dates and class<br>4. Click "Search" | User is redirected to the flight listing page with results matching the search criteria | High |
| HOME-004 | Tour search from home page | None | 1. Select the Tours tab<br>2. Enter destination<br>3. Select travel date<br>4. Click "Search" | User is redirected to the tour listing page with matching results | Medium |
| HOME-005 | Car search from home page | None | 1. Select the Cars tab<br>2. Enter pick-up and drop-off data<br>3. Select valid date and time values<br>4. Click "Search" | User is redirected to the car listing page with matching results | Medium |
| HOME-006 | Featured content sections displayed | None | 1. Scroll through the home page | Featured hotels, popular destinations, and promotional sections are visible | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HOME-007 | Hotel search with required fields missing | None | 1. Select Hotels tab<br>2. Leave destination or required dates empty<br>3. Click "Search" | Validation message is shown and search is not submitted | High |
| HOME-008 | Flight search with required fields missing | None | 1. Select Flights tab<br>2. Leave origin or destination empty<br>3. Click "Search" | Validation message is shown and search is not submitted | High |
| HOME-009 | Invalid hotel date range | None | 1. Select Hotels tab<br>2. Choose check-out before check-in<br>3. Click "Search" | Search is blocked or date validation feedback is displayed | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HOME-010 | Flight search Departure City accepts special characters and emoji | None | 1. Select the Flights tab<br>2. Enter a Departure City value containing special characters and emoji<br>3. Fill other required fields with valid values<br>4. Click "Search" | Search succeeds; the search summary on the Flights listing page displays the Departure City value with special characters and emoji preserved | Medium |
| HOME-011 | Hotels Destination accepts very long free-text input | None | 1. Select the Hotels tab<br>2. Enter a very long string (200+ characters) in the Destination field<br>3. Fill other required fields with valid values<br>4. Click "Search" | Search succeeds; the search summary on the Hotels listing page displays the full entered Destination string with no truncation | Low |

---

## 2. Registration

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REG-001 | Registration page elements displayed | None | 1. Navigate to the signup page | Required fields, mobile number country code selector, terms checkbox, and "Sign Up" button are visible | High |
| REG-002 | Successful registration | Email address is not already registered | 1. Enter valid required data<br>2. Accept terms and conditions<br>3. Click "Sign Up" | Account is created and success message or post-registration redirect is shown | High |
| REG-003 | Registration blocked while already authenticated | User is already authenticated and has access to the Dashboard | 1. While authenticated, navigate to the Registration page or click the Register link in navigation | Registration is blocked for authenticated users: the Registration form or Register button is not presented; no ability to submit a new registration is available while authenticated | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REG-004 | First name empty | None | 1. Leave first name empty<br>2. Fill other required fields<br>3. Submit form | Validation error is displayed for first name | High |
| REG-005 | Invalid email format | None | 1. Enter invalid email format<br>2. Fill other required fields<br>3. Submit form | Validation error indicates email format is invalid | High |
| REG-006 | Password mismatch | None | 1. Enter password<br>2. Enter different confirm password<br>3. Submit form | Validation error indicates passwords do not match | High |
| REG-007 | Duplicate email | Existing user with same email already exists | 1. Enter already-registered email<br>2. Fill other valid data<br>3. Submit form | Registration is blocked and duplicate-email error is displayed | High |
| REG-008 | Terms and conditions unchecked | None | 1. Fill valid registration data<br>2. Leave terms unchecked<br>3. Submit form | Registration is blocked and user is prompted to accept terms | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REG-009 | Very long First Name accepted (200+ characters) | Visitor is not authenticated and is on the Registration form | 1. Enter a string of 200+ characters in the First Name field<br>2. Fill other required fields with valid values<br>3. Submit form | Form submission succeeds; no inline field errors are displayed for First Name (registration proceeds) | Low |
| REG-010 | Mobile number with selected country code | None | 1. Select country code<br>2. Enter valid number at expected length boundary | Number is accepted in the expected format | Low |

---

## 3. Login

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGIN-001 | Successful login | Registered user exists | 1. Navigate to login page<br>2. Enter valid email<br>3. Enter valid password<br>4. Click "Login" | User is redirected to the dashboard or prior protected page | High |
| LOGIN-002 | Login action unavailable while already authenticated | User is already authenticated with an active session | 1. While authenticated, navigate to Account/Login or the Login page | Login action is not available: the Login button/form is not visible; user is not presented the login form | Medium |
| LOGIN-003 | Login page alternate options displayed | None | 1. Navigate to login page | Forgot password link, signup link, and any enabled social login buttons are visible | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGIN-004 | Invalid email or password | None | 1. Enter invalid email or password<br>2. Click "Login" | Error message is displayed and login does not succeed | High |
| LOGIN-005 | Empty email | None | 1. Leave email empty<br>2. Enter password<br>3. Click "Login" | Validation or login error is displayed | High |
| LOGIN-006 | CAPTCHA left blank when required is rejected | Multiple consecutive failed login attempts have made CAPTCHA required and visible | 1. Enter registered email<br>2. Enter correct password<br>3. Leave the CAPTCHA field blank<br>4. Click "Login" | CAPTCHA field displays an inline validation error indicating it is required; login is blocked and the form does not submit | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGIN-007 | Email retained after failed login | None | 1. Enter email<br>2. Enter invalid password<br>3. Click "Login" | Email remains populated while password is cleared | Medium |
| LOGIN-008 | Multiple failed login attempts | None | 1. Submit invalid credentials repeatedly | Site consistently handles repeated failures and may activate additional protection such as CAPTCHA | Low |

---

## 4. Forgot Password

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FP-001 | Request password reset with existing email | Registered user exists | 1. Open Forgot Password page<br>2. Enter registered email<br>3. Click submit | Confirmation message indicates reset email was sent | High |
| FP-002 | Reset password with valid link | Valid reset link is available | 1. Open reset password page from email link<br>2. Enter valid new password<br>3. Confirm password<br>4. Submit | Password is changed and user is returned to login with success feedback | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FP-003 | Unknown email address | None | 1. Enter non-existent email on Forgot Password page<br>2. Submit | Error message indicates no account exists for that email | High |
| FP-004 | Empty email field | None | 1. Leave email field empty<br>2. Submit | Validation error is displayed | High |
| FP-005 | Reset password mismatch | Valid reset link is available | 1. Enter new password<br>2. Enter different confirm password<br>3. Submit | Password reset is blocked and mismatch error is displayed | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FP-006 | Expired reset link | Expired reset link is available | 1. Open expired reset link | Link is rejected and user is prompted to request a new reset email | Medium |

---

## 5. Hotels Search And Listing

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HOTEL-001 | Hotel listing page displays search summary and results count | Valid hotel search has been submitted | 1. View hotel listing page | Search summary, total results count, filters, and sorting controls are visible | High |
| HOTEL-002 | Hotel cards display expected content | Valid hotel search has been submitted | 1. View hotel listing page | Each hotel card shows image, name, location, rating, price, and action button | High |
| HOTEL-003 | Sort hotels by price | Valid hotel search has been submitted | 1. Change sort to "Price: Low to High" or "Price: High to Low" | Hotel results reorder according to selected sort | Medium |
| HOTEL-004 | Filter hotels by star rating or facilities | Valid hotel search has been submitted | 1. Apply star or facility filters | Hotel results update to match selected filters | High |
| HOTEL-005 | Open hotel details from listing | Valid hotel search has been submitted | 1. Click hotel name or "View Details" | Hotel details page opens | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HOTEL-006 | Search with non-matching destination | None | 1. Search for destination with no available properties | Empty-state or no-results feedback is shown | Medium |
| HOTEL-007 | Invalid hotel date range from listing edit | Listing page is open with editable search summary | 1. Set check-out before check-in<br>2. Apply search | Validation prevents invalid search update | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HOTEL-008 | Price range slider minimum and maximum bounds | Hotel listing page is open | 1. Drag slider to minimum and maximum ends | Result set updates correctly at both range extremes | Low |
| HOTEL-009 | Clear all hotel filters | One or more filters are active | 1. Click "Clear All Filters" | Filters reset and full unfiltered listing returns | Medium |

---

## 6. Hotel Details And Booking

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

---

## 7. Flights Search And Booking

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FLIGHT-001 | Flight listing displays itinerary cards | Valid flight search has been submitted | 1. View flight listing page | Airline, times, stops, price, and selection controls are displayed for each result | High |
| FLIGHT-002 | Flight filters work | Valid flight search has been submitted | 1. Apply airline, stops, or departure-time filters | Flight results update to match selected filters | High |
| FLIGHT-003 | View flight details from listing | Valid flight search has been submitted | 1. Click "View Details" | Expanded or detailed fare information is displayed | Medium |
| FLIGHT-004 | Proceed to flight booking with valid passenger data | Flight has been selected | 1. Enter valid passenger details<br>2. Accept terms if required<br>3. Continue | User proceeds to payment step | High |
| FLIGHT-005 | Round-trip search summary displays both outbound and return travel dates | Valid round-trip flight search has been submitted with departure and return dates | 1. Review the Flights Listing page header | The search summary shows the selected origin, destination, and both the outbound and return travel dates | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FLIGHT-006 | Required passenger field missing | Flight booking form is open | 1. Leave a required passenger field empty<br>2. Continue | Validation error is displayed | High |
| FLIGHT-007 | Passport expiry too soon | Flight booking form is open for travel requiring passport | 1. Enter passport expiry less than six months from travel date<br>2. Continue | Validation error indicates passport validity is insufficient | High |
| FLIGHT-008 | Invalid passport number format | Flight booking form is open | 1. Enter invalid passport format<br>2. Continue | Validation error is displayed | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FLIGHT-009 | Continue is blocked without a selected itinerary and passenger count | User is on the Flight Booking page without a selected flight itinerary and/or passenger count | 1. Fill all required traveler and lead contact fields with valid values<br>2. Click "Continue" | Continue is blocked; the page shows an error indicating a flight itinerary and passenger count must be selected before proceeding; user remains on the Flight Booking page | Low |

---

## 8. Tours Search And Booking

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| TOUR-001 | Tour listing cards displayed | Valid tour search has been submitted | 1. View tours listing page | Tour cards show image, title, destination, duration, price, and rating | High |
| TOUR-002 | Filter tours by destination or type | Valid tour search has been submitted | 1. Apply destination or tour-type filters | Tours list updates to match selected filters | Medium |
| TOUR-003 | Tour Details page displays title, image, price and booking call-to-action | Visitor has performed a tour search | 1. Click View Details on a tour result card | Tour Details page opens showing the tour title, main image, starting price, and a visible booking call-to-action | High |
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

---

## 9. Cars Search And Booking

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
| CAR-006 | Very long License Number input is rejected | Car booking form is open | 1. Enter a very long string (significantly longer than typical license numbers) in the License Number field<br>2. Fill other required fields with valid values<br>3. Click "Confirm Booking" | An inline error is displayed indicating the License Number exceeds the allowed length; form submission is blocked | High |
| CAR-007 | Terms and conditions unchecked | Car booking form is open | 1. Fill valid data<br>2. Leave terms unchecked<br>3. Continue | Booking does not proceed and terms validation is shown | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| CAR-008 | Access Cars Listings page directly without performing a search is blocked | User has not performed a search and has not supplied pick-up/drop-off locations or dates | 1. Navigate directly to the Cars Listings page URL without submitting the Cars Search form | The page does not display car listings for a search; the Search form is shown or an inline notice indicates search criteria are required; no Book Now buttons are visible or enabled | Low |

---

## 10. Visa Services

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| VISA-001 | Visa requirements form displayed | None | 1. Open the Visa page | Nationality selector, Destination selector, and requirement lookup action are visible | High |
| VISA-002 | Check visa requirements for selected route | None | 1. Select nationality<br>2. Select destination<br>3. Click "Check Requirements" or equivalent action | Visa requirement details, processing time, validity, required documents, and fees are displayed | High |
| VISA-003 | Submit visa application when application form is available | Visa application form is enabled and user has required documents | 1. Complete visa application fields<br>2. Upload required documents<br>3. Submit application | Visa application is submitted and application status or confirmation is displayed | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| VISA-004 | Nationality not selected | None | 1. Leave nationality empty<br>2. Select destination<br>3. Submit requirement check | Validation message is displayed | High |
| VISA-005 | Destination not selected | None | 1. Select nationality<br>2. Leave destination empty<br>3. Submit requirement check | Validation message is displayed | High |
| VISA-006 | Missing required visa application fields | Visa application form is enabled | 1. Leave one or more required applicant fields empty<br>2. Submit application | Validation errors are displayed and application is not submitted | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| VISA-007 | Supporting Documents can be added and removed from the repeating group before submission | Visa application form is enabled with Nationality and Destination Country selected | 1. Add two entries to the Supporting Documents repeating group, uploading a file to each<br>2. Remove both entries, leaving zero entries<br>3. Fill all other required fields and submit the application | Form submits successfully; the created application appears in the user's Dashboard bookings and shows no Supporting Documents listed | Low |

---

## 11. User Dashboard And Booking Management

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

---

## 12. Payment Processing

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| PAY-001 | Payment summary displayed | User is on payment page | 1. Review payment page | Booking summary, price breakdown, payment methods, and terms checkbox are visible | High |
| PAY-002 | Apply valid promo code | Valid promo code exists | 1. Enter valid promo code<br>2. Click "Apply" | Discount is applied and total updates | Medium |
| PAY-003 | Successful card payment | User is on payment page and uses valid card | 1. Select card payment<br>2. Enter valid cardholder, card number, expiry, and CVV<br>3. Accept terms<br>4. Click "Pay Now" | Payment succeeds and booking confirmation page is displayed | High |
| PAY-004 | Successful wallet payment | User has enough wallet balance | 1. Select wallet or credits payment<br>2. Confirm payment | Payment succeeds and booking confirmation page is displayed | Medium |
| PAY-005 | Confirmation page displayed after successful payment | Payment was successful | 1. Review confirmation page | Booking reference and follow-up actions such as invoice or voucher download are visible | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| PAY-006 | Invalid card number | User is on payment page | 1. Enter invalid card number<br>2. Submit payment | Card validation error is displayed | High |
| PAY-007 | Expired card | User is on payment page | 1. Enter past expiry date<br>2. Submit payment | Expiry validation error is displayed | High |
| PAY-008 | Invalid CVV | User is on payment page | 1. Enter invalid CVV length or format<br>2. Submit payment | CVV validation error is displayed | High |
| PAY-009 | Terms unchecked | User is on payment page | 1. Fill valid payment data<br>2. Leave terms unchecked<br>3. Submit payment | Payment does not proceed and terms validation is displayed | High |
| PAY-010 | Payment declined or insufficient funds | User is on payment page | 1. Submit payment with failing payment source | Error message is displayed with retry or alternate-payment options | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| PAY-011 | Retry Payment action is not available when previous attempt did not fail | A completed booking/reservation is present; payment intent is initiated; Payment_Last_Attempt is not Failed | 1. Open the Payment page for a booking where the previous attempt did not fail<br>2. Attempt to locate a Retry Payment button or control | Retry Payment control is not visible on the Payment page; user cannot initiate a retry action from this state | Medium |
| PAY-012 | Download Invoice/Voucher actions are not available before successful booking confirmation | User is on the Payment page or pre-confirmation state (payment not successful) | 1. Open the Payment page for a booking before completing payment<br>2. Attempt to locate the Download Invoice and Download Voucher actions | Download Invoice and Download Voucher actions are not visible prior to a successful booking confirmation; no download is initiated | Low |

---

## 13. Currency And Language Selection

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| PREF-001 | Currency selector updates displayed prices | None | 1. Change currency from the top navigation | Prices across the current page update to the selected currency | High |
| PREF-002 | Language selector updates interface text | None | 1. Change language from the top navigation | Interface text updates to the selected language | High |
| PREF-003 | Arabic or RTL language applies RTL layout | RTL language option is available | 1. Select Arabic or another RTL language | Page layout and text direction switch to RTL where applicable | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| PREF-005 | Unsupported preference value cannot be applied | None | 1. Attempt to select unavailable currency or language option | Invalid selection is not applied | Low |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| PREF-006 | Currency preference persists across page navigation | None | 1. Change currency<br>2. Navigate to another page | Selected currency remains active across navigation | Medium |
| PREF-007 | Authenticated language selection persists to profile preferences | User is authenticated and on any page with an active session; Account/Preferences page is available | 1. Open the Language selector<br>2. Select a language different from the current site language<br>3. Navigate to the Account or Preferences page | The Account/Preferences page visibly shows the newly selected language as the saved preference; the site continues to display the chosen language across pages | Low |

---

## 14. Search And Filters

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FILTER-001 | Filter sidebar controls displayed on listing pages | User is on a hotels, flights, tours, or cars listing page | 1. Review the listing page sidebar | Filter groups and sort controls are visible | High |
| FILTER-002 | Result count updates after applying filter | User is on a listing page with available filters | 1. Apply one or more filters | Result count updates to reflect the filtered result set | High |
| FILTER-003 | Active filter tag can be removed | One or more filters are active | 1. Remove an active filter tag | Corresponding filter is cleared and results refresh | Medium |
| FILTER-004 | Clear all filters resets listing | One or more filters are active | 1. Click "Clear All Filters" | All active filters are cleared and listing resets to the default state | Medium |
| FILTER-005 | Sorting control reorders results | User is on a listing page | 1. Select a different sort option | Result ordering updates according to the selected sort | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FILTER-006 | Filter combination returns no results | User is on a listing page | 1. Apply a restrictive combination of filters | Empty-state or zero-results feedback is displayed | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FILTER-007 | Reset all filters is blocked when no search has been executed | User is on a listing page but has not executed a search and no results are loaded | 1. Locate the "Reset all filters" control in the Active Filters Summary panel<br>2. Click the "Reset all filters" button | Reset all filters is blocked: the control is disabled or an inline message indicates a search must be executed first; results are not refreshed | Low |

---

## 15. Reviews And Ratings

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

---

## 16. Offers And Deals

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| OFFER-001 | Offers page content displayed | None | 1. Open Offers page | Hero banner, category filters, destination controls, and offer cards are visible | High |
| OFFER-002 | Filter offers by category | Offers page is open | 1. Select a category tab or filter | Visible offers update to match selected category | Medium |
| OFFER-003 | Offer Book Now action applies deal | Valid offer exists | 1. Click "Book Now" on an offer | Offer is applied and user is redirected to relevant booking or listing flow | High |
| OFFER-004 | Newsletter subscription with valid email | Offers page is open | 1. Enter valid email<br>2. Click "Subscribe" | Subscription confirmation message is displayed | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| OFFER-005 | Newsletter subscription with invalid email | Offers page is open | 1. Enter invalid email<br>2. Click "Subscribe" | Validation error is displayed | Medium |
| OFFER-006 | Book Now blocked when booking/payment subsystem is unavailable | Offers page is open, booking and/or payment subsystems are unavailable | 1. Locate an offer row in the Offers list<br>2. Click the Book Now button for that offer | Clicking Book Now is blocked: a visible error banner or modal indicates the booking/payment subsystem is unavailable; the user is not redirected | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| OFFER-007 | Offer validity date boundary | Offer expires today or at a known cut-off time | 1. Attempt to use the offer near expiration time | Offer acceptance or rejection matches the documented validity boundary | Low |

---

## 17. Logout

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGOUT-001 | Logout from user dropdown | User is logged in | 1. Open user menu<br>2. Click "Logout" | Session ends and the home page shows Login and Signup links again | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGOUT-002 | Access protected page after logout | User has logged out | 1. Attempt to open dashboard or booking-management URL | User is redirected to login page and cannot access protected content | High |
