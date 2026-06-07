# Post-Verification Specifications

### [TC-001] Authenticated user clicks Logout and is returned to Home page
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button in the action bar

**Original Expected Result:** terminates current session; clears sensitive session data; redirects to home page; subsequent attempts to access protected pages redirect to login page. The Home page is displayed after logout.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Home page (or Login page)`
- **Observe**:
  - Top navigation displays 'Login' and 'Signup' links indicating no active session
  - Dashboard header, user avatar, 'My Bookings' or other authenticated-only links are not present

**Post-Check**
- **Navigate To**: `User Dashboard -> My Profile (or Dashboard main page)`
- **Observe**:
  - Dashboard header or welcome message is visible indicating an authenticated session
  - User display name shows <valid first name> <valid last name>
  - Account email in profile or header matches <unique valid email>
  - Logout link or user avatar is visible and protected pages (e.g., 'My Bookings') are accessible without redirecting to login

**Expected Change**: A new user account has been created and the user is automatically logged in; the Dashboard and profile show the registered user's name and email, and authenticated-only pages are accessible.

---

### [TC-002] Logged-out user attempting to open a protected page is redirected to Login page
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `partial`

**Coverage Note**: *The presence of the user account and its unverified state can be confirmed in-app (login/forgot-password responses). Actual delivery of the verification email and click-through in the user's external inbox cannot be verified from within the application.*

**Original Steps:**
1. 1. Attempt to navigate to <protected page> (enter protected page URL or click link to protected page)

**Original Expected Result:** The Login page is displayed; the Login form is visible, and access to the requested protected page is not granted.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Login page -> Forgot Password`
- **Observe**:
  - Submitting the <unique valid email> on Forgot Password returns 'No account found' or an equivalent message indicating the email is not registered

**Post-Check**
- **Navigate To**: `Login page (and optionally Forgot Password)`
- **Observe**:
  - Attempting to log in with the newly registered <unique valid email> and <valid password> is blocked and shows a message indicating email verification is required (e.g., 'Please verify your email before logging in')
  - Submitting the same <unique valid email> on Forgot Password now indicates an account exists (e.g., 'Reset link sent' or no 'No account found' message), demonstrating the account record was created

**Expected Change**: A new user account has been created for the provided email and is marked as unverified; the application blocks sign-in and displays an instruction to verify the email until the verification step is completed.

---

### [TC-001] Authenticated user clicks Logout and is returned to Home page
**Category**: `positive` | **Verification Type**: `other` | **Coverage**: `partial`

**Coverage Note**: *The application UI shows a confirmation message which can be verified in-app, but the actual dispatch and delivery of the reset email is performed by external email infrastructure and cannot be confirmed from within the application without access to the recipient inbox or mail server logs.*

**Original Steps:**
1. 1. Click the Logout button in the action bar

**Original Expected Result:** terminates current session; clears sensitive session data; redirects to home page; subsequent attempts to access protected pages redirect to login page. The Home page is displayed after logout.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Forgot Password page`
- **Observe**:
  - Email input field is present and empty
  - No success or 'reset link sent' confirmation message is visible

**Post-Check**
- **Navigate To**: `Forgot Password page (or Login page if the flow redirects after submission)`
- **Observe**:
  - UI displays a confirmation message such as 'If an account exists for this email, a password reset link has been sent' or 'Reset link sent to your email'
  - Email input retains submitted value or is cleared according to application behavior

**Expected Change**: The UI displays a confirmation message stating that a reset link has been sent (or that an email will be sent if the address exists). The presence of this confirmation indicates the application accepted the request, but actual email delivery cannot be verified without access to the recipient inbox or external mail system logs.

---

### [TC-002] Logged-out user attempting to open a protected page is redirected to Login page
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to <protected page> (enter protected page URL or click link to protected page)

**Original Expected Result:** The Login page is displayed; the Login form is visible, and access to the requested protected page is not granted.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Login page`
- **Observe**:
  - No 'Password changed' success message is present
  - Attempting to authenticate using the <new password> is rejected (shows invalid credentials) — establishes baseline that the new password is not yet active

**Post-Check**
- **Navigate To**: `Login page`
- **Observe**:
  - Login attempt using the <new password> succeeds and user is redirected to the dashboard or protected landing page
  - Login attempt using the old password is rejected (shows invalid credentials)

**Expected Change**: The user's password has been updated in the backend: the new password allows successful authentication while the old password no longer authenticates.

---

### [TC-003] Attempt to invoke Logout action when user is not authenticated (precondition not met)
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is signed out (no active session)
2. 2. Navigate directly to the Logout URL / click the Logout endpoint link (attempt to trigger Logout while unauthenticated)

**Original Expected Result:** Navigation is blocked: the application redirects to the Login page and displays the login form. The Logout action is not performed (no session termination occurs because there is no active session). No protected content is shown.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Flight Booking page -> Traveler list / Itinerary Summary`
- **Observe**:
  - Traveler 1 row shows no Meal preference selected or displays 'Not selected'
  - Traveler 1 row shows no Seat selection or displays 'Not selected'

**Post-Check**
- **Navigate To**: `Flight Booking page -> Traveler list / Itinerary Summary`
- **Observe**:
  - Traveler 1 row displays the selected Meal preference (the value chosen as <Meal_Preference>)
  - Traveler 1 row displays the selected Seat (the value chosen as <Seat_Selection>)

**Expected Change**: Traveler 1's itinerary summary row shows the Meal preference and Seat selection chosen in the traveler form; the displayed values match the selections made.

---

### [TC-004] Unauthenticated state shows no action buttons (Logout not visible)
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is signed out (no active session)
2. 2. Open the application UI area that normally contains session actions (header, user menu, or action bar)

**Original Expected Result:** The action bar / user menu does not display a 'Logout' button or any authenticated-only actions. There is no clickable Logout control visible in the Unauthenticated state (no action buttons are present).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Flight Booking page -> Travelers section`
- **Observe**:
  - travelers list does not contain a row for <Title> <First_Name> <Last_Name>
  - no traveler row shows Passport Number: <Passport_Number>
  - no traveler row shows Passport Expiry: <Passport_Expiry>

**Post-Check**
- **Navigate To**: `Flight Booking page -> Travelers section`
- **Observe**:
  - travelers list contains a row for <Title> <First_Name> <Last_Name>
  - that row displays Passport Number: <Passport_Number>
  - that row displays Passport Expiry: <Passport_Expiry>

**Expected Change**: A new traveler row is added to the Travelers list displaying the entered Title, First Name, Last Name, Passport Number, and Passport Expiry for the added traveler.

---

### [TC-003] Attempt to invoke Logout action when user is not authenticated (precondition not met)
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is signed out (no active session)
2. 2. Navigate directly to the Logout URL / click the Logout endpoint link (attempt to trigger Logout while unauthenticated)

**Original Expected Result:** Navigation is blocked: the application redirects to the Login page and displays the login form. The Logout action is not performed (no session termination occurs because there is no active session). No protected content is shown.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - My Bookings does not contain a booking for the selected Tour with the chosen Departure Date

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings -> Open the newly created booking (or filter by date/tour to locate it)`
- **Observe**:
  - Booking list contains a new entry for the selected Tour with the chosen Departure Date
  - Booking detail shows Travelers list length equals the combined count of Adults and Children submitted
  - Contact details in booking (email and phone) match the values submitted on the Booking Form
  - Total cost breakdown in booking detail equals the calculated total shown on the Booking Form at submission
  - Booking status is displayed (e.g., 'Confirmed' or 'Pending') and a booking reference is present

**Expected Change**: A new booking record for the selected Tour and Departure Date appears in My Bookings; the booking details list exactly the combined number of Travelers (Adults + Children), contact details match the submitted values, and the Total cost breakdown matches the calculated total from the Booking Form.

---

### [TC-005] After Logout, accessing a protected page is blocked and redirects to login
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `partial`

**Coverage Note**: *Clicking 'Book Now' often only opens the booking flow/booking form and does not create a persistent booking record until the user completes the booking (e.g., submits payment). The UI can verify that the flow was initiated and that form fields are prefilled; whether a draft/pending booking entry appears in My Bookings depends on backend implementation and may not be created at this step.*

**Original Steps:**
1. 1. Sign in as <role> to create an authenticated session
2. 2. Click the Logout action to terminate the session
3. 3. After logout completes, navigate to a known protected page URL (direct URL entry or bookmarked link)

**Original Expected Result:** Access is blocked: the application redirects to the Login page and displays the login form. Protected page content is not displayed; the terminated session is not restored by the navigation.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - My Bookings list does not contain a booking for the vehicle to be selected in the test (no existing draft or pending booking for that vehicle)
  - If booking references are shown, note current count of bookings for later comparison

**Post-Check**
- **Navigate To**: `Car Listing -> Booking Form (after clicking 'Book Now') and User Dashboard -> My Bookings`
- **Observe**:
  - Booking form page is displayed (confirmation that booking flow was initiated)
  - Vehicle name/model on the booking form matches the selected listing
  - Pick-up and drop-off location and dates are prefilled or reflect the selection from the listing
  - Price breakdown or rental total is shown on the booking form
  - User Dashboard -> My Bookings contains a new entry for the vehicle with status 'Draft' or 'Pending' (if the system creates a persistent draft booking at initiation)

**Expected Change**: Clicking 'Book Now' navigates the user to the car booking form with the selected vehicle and selection details prefilled. If the application creates a persistent draft/pending booking at flow initiation, a new booking entry for the selected vehicle will appear in My Bookings with matching vehicle, dates, and a status such as 'Draft' or 'Pending'. If the app only opens the booking form without persisting, the booking form prefilled details are visible but no My Bookings entry will exist until the booking is completed.

---

### [TC-001] Authenticated user clicks Logout and is returned to Home page
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button in the action bar

**Original Expected Result:** terminates current session; clears sensitive session data; redirects to home page; subsequent attempts to access protected pages redirect to login page. The Home page is displayed after logout.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - booking list does not contain an entry for the selected vehicle and rental period
  - no recent booking with status 'Pending Payment' for this vehicle

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - booking list contains a new entry for the selected vehicle and exact rental period
  - new booking row displays customer name, vehicle name, rental dates, and total price
  - booking status is 'Pending Payment' or otherwise indicates payment is required
  - booking entry shows a booking reference or a link/button to proceed to Payment page

**Expected Change**: A new booking record is created for the selected vehicle and rental period; it appears in My Bookings with the lead driver name, rental dates, a booking reference, and a status indicating payment is required (e.g., 'Pending Payment'), and provides a link to continue to payment.

---

### [TC-002] Logged-out user attempting to open a protected page is redirected to Login page
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to <protected page> (enter protected page URL or click link to protected page)

**Original Expected Result:** The Login page is displayed; the Login form is visible, and access to the requested protected page is not granted.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - bookings list does not contain a row with Full Name '<Full_Name>' and Passport Number '<Passport_Number>'
  - no recent 'Visa Application' entry is present with status 'Pending'

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - bookings list contains a new row with Full Name '<Full_Name>'
  - the new row's status badge text equals 'Pending'
  - the new row is identified as a 'Visa Application' (service/type column or details link) and opens details showing uploaded passport copy and photographs

**Expected Change**: A new Visa Application entry is created in the user's Bookings dashboard showing Full Name '<Full_Name>' with its status set to 'Pending', and the booking details include the uploaded passport copy and photograph attachments.

---

### [TC-003] Attempt to invoke Logout action when user is not authenticated (precondition not met)
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is signed out (no active session)
2. 2. Navigate directly to the Logout URL / click the Logout endpoint link (attempt to trigger Logout while unauthenticated)

**Original Expected Result:** Navigation is blocked: the application redirects to the Login page and displays the login form. The Logout action is not performed (no session termination occurs because there is no active session). No protected content is shown.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - bookings list does not contain an entry with Full Name '<Full_Name>'
  - no visa application row exists with Passport Number '<Passport_Number>'

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - bookings list contains a new entry with Full Name '<Full_Name>'
  - the new booking row shows a status badge with text 'Pending'
  - open the new booking's details and observe the documents list contains the uploaded 'Passport_Copy' and the uploaded supporting document file (matches '<valid supporting document file>')

**Expected Change**: A new visa application booking is created for <Full_Name> (matching the submitted Passport Number) and appears in My Bookings with a 'Pending' status; viewing the booking details shows the Passport_Copy and the added supporting document in the application's document list.

---

### [TC-002] Logged-out user attempting to open a protected page is redirected to Login page
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to <protected page> (enter protected page URL or click link to protected page)

**Original Expected Result:** The Login page is displayed; the Login form is visible, and access to the requested protected page is not granted.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - Row for the target booking (identify by booking reference, property name, or date) is present
  - Status badge for that row shows 'Pending'
  - A 'Cancel' action/button is visible and enabled for that row

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings (reload page or navigate away and back to ensure fresh data)`
- **Observe**:
  - Row for the same booking is present
  - Status badge for that row shows 'Cancelled'
  - The 'Cancel' action/button is no longer available or is disabled for that row
  - Optional: Booking detail view (opened from the row) shows cancellation confirmation or cancellation timestamp

**Expected Change**: The booking's status changes from 'Pending' to 'Cancelled' for the specific booking row, and the Cancel action is removed or disabled indicating the cancellation has been persisted.

---

### [TC-008] Logout in one tab then quickly access protected page in another tab
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Tab A, click the Logout button
2. 2. Immediately in Tab B, attempt to navigate to a protected page (click a protected page link or enter its URL)

**Original Expected Result:** Logout in Tab A succeeds: session is terminated and Tab A redirects to the home page. Access attempt in Tab B is blocked: navigation to the protected page redirects to the login page (no protected content is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - the target booking row is present (identify by booking reference, property/flight/tour name, or travel dates)
  - status badge for that booking is 'Confirmed'
  - 'Cancel' action/button is visible and enabled for that booking

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - the same booking row is present (same booking reference or identifying details)
  - status badge for that booking is 'Cancelled'
  - 'Cancel' action/button is no longer available or is disabled for that booking
  - cancellation metadata is shown on the row or in booking details (cancellation date or note), if provided

**Expected Change**: The booking's status for the same booking reference changes from 'Confirmed' to 'Cancelled' in My Bookings; the Cancel action is removed or disabled and any available cancellation metadata is displayed.

---

### [TC-017] Rapid resubmission after redirect: attempt to create duplicate review by using browser Back and Submit again
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the Review Submission Form and fill all required fields (Overall_Rating and any visible category ratings)
2. 2. Click Submit and wait for the success redirect to the item or review confirmation
3. 3. Press the browser Back button to return to the Review Submission Form
4. 4. Immediately click Submit again without modifying fields

**Original Expected Result:** Second submission attempt is blocked; a visible blocking message is shown indicating the review cannot be duplicated and only one review is associated with the booking (is blocked / error shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Profile (view mode) before editing`
- **Observe**:
  - Displayed profile fields show the current values prior to edit (e.g., current First Name, Last Name, Phone, etc.)
  - The profile does NOT contain the new values that will be entered in step 1
  - My Profile is currently in view mode (edit controls not persisted)

**Post-Check**
- **Navigate To**: `User Dashboard -> My Profile (navigate away then return or reload page) after saving`
- **Observe**:
  - Profile fields display the updated values entered in step 1 (e.g., the edited First Name/Last Name/Phone show the new values)
  - My Profile section is in view mode (edit inputs hidden and edit button available)
  - Optional: Success confirmation is shown (e.g., 'Profile updated' toast or inline success message) if the UI provides one

**Expected Change**: The profile fields now persist and display the new values entered and saved in step 1, and the My Profile section has exited edit mode.

---

### [TC-020] Change Sort_By reorders results
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `partial`

**Coverage Note**: *Some deployments queue reviews for moderation or require background processing; the review might not appear in public listings immediately. The test can fully verify persistence if the user's booking-details or 'My Reviews' area shows the submission; otherwise only an in-app confirmation is verifiable.*

**Original Steps:**
1. 1. Open the Sort By dropdown
2. 2. Select <sort option> from the Sort By dropdown
3. 3. Observe the Results grid ordering and the Sort By control state

**Original Expected Result:** Results grid reorders according to <sort option>; the Sort By control shows <sort option> as the selected option and the visible ordering of result items updates accordingly

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings -> Open the target Booking -> Reviews section (or My Reviews)`
- **Observe**:
  - reviews list does not contain a review with the same submitted review text and rating
  - record the current review count for the booking (e.g., X reviews)

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings -> Open the target Booking -> Reviews section (or My Reviews)`
- **Observe**:
  - reviews list contains a new review entry with the submitted rating and submitted review text
  - a confirmation message or toast such as 'Review submitted' or 'Review saved' is visible after submission
  - the booking's review count has increased by 1 compared to the pre_check value

**Expected Change**: A new review entry for the booking appears containing the submitted rating and review text and the booking's review count increments by one; if moderation delays public visibility, at minimum the UI shows a success confirmation indicating the review was saved.

---

### [TC-022] Departure time range end is before start (invalid time-range) is rejected
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Expand 'Flights Filters' in the left sidebar
2. 2. Set Departure_Time_Range start to <start time>
3. 3. Set Departure_Time_Range end to <end time earlier than start>
4. 4. Click outside the control or wait for the widget to apply changes

**Original Expected Result:** Departure_Time_Range field displays an inline validation error on the time-range control indicating end time must be after start time (e.g. 'End time must be after start time'); the Results grid does not update and Result_Count remains unchanged; the invalid time-range is not applied as a filter.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> Settings`
- **Observe**:
  - Current saved values for Default Currency, Default Language, and Notification Preferences are visible (capture their values before change)

**Post-Check**
- **Navigate To**: `User Dashboard -> Settings (after clicking 'Save Settings'; then reload the page or log out and log back in and return to Settings)`
- **Observe**:
  - Default Currency is set to the selected <Default_Currency>
  - Default Language is set to the selected <Default_Language>
  - Notification Preferences toggles/checkboxes reflect the selected <Notification_Preferences>
  - A visible success confirmation message is displayed indicating settings were saved

**Expected Change**: The Settings page displays the newly selected Default Currency, Default Language, and Notification Preferences after saving, and these values remain persisted after page reload or logout/login.

---

### [TC-001] Authenticated user clicks Logout and is returned to Home page
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `partial`

**Coverage Note**: *The UI can verify updated dates, special requests, added traveler row, fee line item, and success notification. The outbound email notification referenced in the expected result is sent via external email delivery and cannot be verified from within the application UI.*

**Original Steps:**
1. 1. Click the Logout button in the action bar

**Original Expected Result:** terminates current session; clears sensitive session data; redirects to home page; subsequent attempts to access protected pages redirect to login page. The Home page is displayed after logout.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings -> Booking Details (for the existing booking to be modified)`
- **Observe**:
  - current travel dates shown on the booking (original travel dates)
  - special requests field shows the pre-modification text (or is empty if none existed)
  - traveler updates repeating section does not contain the new traveler update details
  - fee/charges line items do not include a modification fee for the requested change (or show the pre-modification fee state)
  - booking status is 'default' or current pre-modification status

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings -> Booking Details (open the same booking after modification completes)`
- **Observe**:
  - travel dates reflect the newly entered travel dates
  - special requests text includes the newly entered special requests
  - traveler updates repeating section contains a row with the newly added traveler update details
  - a visible fee/charge line item is present for modification fees with an amount and label indicating it is a modification charge
  - a success/confirmation notification was displayed after save (e.g., 'Modifications applied' or equivalent)

**Expected Change**: The booking details persistently show the updated travel dates, include the new special requests and the newly added traveler update row, and display a fee line item for any applicable modification charges; a success notification is shown after the save action. (Email notification is expected to be sent but is not verifiable in-app.)

---

### [TC-002] Logged-out user attempting to open a protected page is redirected to Login page
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `partial`

**Coverage Note**: *The UI can verify booking status change and displayed refund amount, but external side-effects mentioned in the expected result (actual payment refund to the original payment method and delivery of the cancellation email) cannot be independently verified from within the application UI.*

**Original Steps:**
1. 1. Attempt to navigate to <protected page> (enter protected page URL or click link to protected page)

**Original Expected Result:** The Login page is displayed; the Login form is visible, and access to the requested protected page is not granted.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings -> Open Booking Detail for the existing booking`
- **Observe**:
  - status badge shows the booking in its pre-cancellation state (e.g., 'Confirmed' or 'Default')
  - no Refund_Amount field or refund value is shown in the booking detail prior to cancellation
  - Cancel action/button is present in the action bar (indicating cancellation is allowed per policy)

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings -> Open Booking Detail for the same booking`
- **Observe**:
  - status badge shows 'Cancelled'
  - Refund_Amount field is present and displays a monetary value
  - A success notification is displayed referencing cancellation and refund (contains text such as 'cancellation' and 'refund' or the application's configured success message)

**Expected Change**: The booking's status changes from its pre-cancellation state to 'Cancelled', the booking detail now includes a Refund_Amount showing the calculated refund, and the UI shows a success notification confirming the cancellation (though actual payment refund processing and outgoing cancellation email delivery are external and not verifiable in-app).

---

### [TC-001] Authenticated user clicks Logout and is returned to Home page
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button in the action bar

**Original Expected Result:** terminates current session; clears sensitive session data; redirects to home page; subsequent attempts to access protected pages redirect to login page. The Home page is displayed after logout.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - booking entry for the booking-to-be-paid exists identified by item/details and amount
  - booking status is 'Awaiting Payment' or 'Pending Payment'
  - no confirmed booking reference number is present for that booking

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - booking entry for the same booking is present
  - booking status is 'Confirmed' (or equivalent confirmed state)
  - a booking reference number is displayed for that booking
  - payment method for the booking shows 'Credit/Debit Card' and/or masked card (last 4 digits)
  - saved-card indicator or token is present if 'Save Card For Future Use' was checked

**Expected Change**: The booking's status changes from 'Awaiting Payment' to 'Confirmed', a booking reference number is assigned and displayed, and the payment method (masked card / last4) is recorded; saved-card token/indicator is persisted if the user opted to save the card.

---

### [TC-002] Logged-out user attempting to open a protected page is redirected to Login page
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to <protected page> (enter protected page URL or click link to protected page)

**Original Expected Result:** The Login page is displayed; the Login form is visible, and access to the requested protected page is not granted.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings (locate the booking awaiting payment)`
- **Observe**:
  - booking row for the booking exists
  - status is 'Awaiting Payment' or 'Pending Payment'
  - no booking reference number is present in the booking row/details
  - price breakdown matches the expected amount shown on the Payment Page

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings -> View Details (or open Booking Confirmation page after payment)`
- **Observe**:
  - booking row status is 'Confirmed' or 'Paid'
  - a booking reference number is displayed (non-empty)
  - payment method or payment note indicates 'PayPal' where shown
  - booking detail/confirmation shows payment date/time and total matching the prior price

**Expected Change**: The booking status changes from 'Awaiting Payment'/'Pending Payment' to 'Confirmed' or 'Paid', a booking reference number is assigned and visible in the confirmation and booking details, and the payment method is recorded as PayPal.

---

### [TC-003] Attempt to invoke Logout action when user is not authenticated (precondition not met)
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is signed out (no active session)
2. 2. Navigate directly to the Logout URL / click the Logout endpoint link (attempt to trigger Logout while unauthenticated)

**Original Expected Result:** Navigation is blocked: the application redirects to the Login page and displays the login form. The Logout action is not performed (no session termination occurs because there is no active session). No protected content is shown.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings -> Open the booking pending payment (or Payment Page if still in-flow)`
- **Observe**:
  - booking row/status shows 'Pending Payment' or 'Awaiting Payment'
  - no 'Download Invoice' button or invoice PDF link is present for this booking
  - price breakdown is visible and payment method selection is available

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings -> Open the confirmed booking (or Booking Confirmation page)`
- **Observe**:
  - status badge displays 'Confirmed' or 'Paid' for the booking
  - 'Download Invoice' button/link is present on the Booking Confirmation or Booking Details page
  - clicking the 'Download Invoice' button initiates a file download and a PDF file is received (filename or PDF content references the booking reference)

**Expected Change**: The booking status changes from 'Pending Payment' to 'Confirmed'/'Paid' and an invoice PDF becomes available for that booking; clicking 'Download Invoice' returns a downloadable PDF containing the booking reference.

---

### [TC-004] Unauthenticated state shows no action buttons (Logout not visible)
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is signed out (no active session)
2. 2. Open the application UI area that normally contains session actions (header, user menu, or action bar)

**Original Expected Result:** The action bar / user menu does not display a 'Logout' button or any authenticated-only actions. There is no clickable Logout control visible in the Unauthenticated state (no action buttons are present).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Payment Page for the specific booking (before submitting payment)`
- **Observe**:
  - payment form is visible (cardholder name, card number, expiry, CVV fields)
  - booking shows status 'Pending Payment' or equivalent
  - no 'Download Voucher' button or voucher link is present on the confirmation/booking detail (voucher not yet generated)

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings -> Open the Booking Details (or revisit the Booking Confirmation page)`
- **Observe**:
  - booking status is 'Confirmed' or 'Paid'
  - 'Download Voucher' button or link is present on the Booking Confirmation or Booking Details page
  - activating the 'Download Voucher' control initiates a downloadable file with .pdf extension or the HTTP response has Content-Type: application/pdf

**Expected Change**: After completing card payment and returning to booking context, the booking status changes from 'Pending Payment' to 'Confirmed' or 'Paid', and a voucher PDF becomes available via a visible 'Download Voucher' button/link which, when activated, initiates a PDF download.

---

### [TC-005] After Logout, accessing a protected page is blocked and redirects to login
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Sign in as <role> to create an authenticated session
2. 2. Click the Logout action to terminate the session
3. 3. After logout completes, navigate to a known protected page URL (direct URL entry or bookmarked link)

**Original Expected Result:** Access is blocked: the application redirects to the Login page and displays the login form. Protected page content is not displayed; the terminated session is not restored by the navigation.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings -> Booking (Pending Payment) -> Booking Details / Payment Page`
- **Observe**:
  - booking status is 'Pending Payment' or 'Awaiting Payment'
  - no invoice link or invoice number is present on the booking details
  - payment method shows PayPal not yet completed

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings -> Booking (most recent) -> Booking Details / Booking Confirmation page`
- **Observe**:
  - booking status is 'Confirmed' or similar success status
  - 'Download Invoice' button or invoice link is present on the Booking Confirmation or Booking Details page
  - an invoice number or invoice entry is displayed in the booking details (e.g., 'Invoice #:')
  - clicking 'Download Invoice' initiates a download or shows a success/download started indicator

**Expected Change**: After completing payment via PayPal and returning to the Booking Confirmation, the booking status changes from 'Pending Payment' to 'Confirmed' and a downloadable invoice PDF is available (invoice link/button and invoice number are present); clicking the Download Invoice control initiates the invoice download.

---

### [TC-006] Double-click Logout rapidly (duplicate click race)
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `partial`

**Coverage Note**: *The PayPal payment processing occurs externally and the exact transaction details cannot be verified in-app. The presence of a downloadable voucher link and that a PDF download is initiated can be verified, but the contents of the PDF and server-side voucher storage integrity require backend or file-system checks outside the UI.*

**Original Steps:**
1. 1. From the authenticated session, click the Logout button
2. 2. Immediately (within milliseconds) click the Logout button again

**Original Expected Result:** First click succeeds: session termination runs, user is redirected to the home page. Second click is ignored (no duplicate logout or error shown). Subsequent navigation attempts to protected pages are blocked and redirect to the login page.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings -> (select the booking awaiting payment)`
- **Observe**:
  - booking row/status shows 'Pending Payment' or 'Awaiting Payment'
  - no 'Download Voucher' button or voucher link is present on the booking detail

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings -> View Details for the completed booking (or open Booking Confirmation page)`
- **Observe**:
  - booking status shows 'Confirmed' or 'Paid'
  - 'Download Voucher' button or link is present on the booking detail or confirmation page
  - clicking the 'Download Voucher' link/button initiates a .pdf file download and the downloaded file size is greater than 0 bytes (or browser download shows a successful file save)

**Expected Change**: After completing payment via PayPal, the booking status changes to 'Confirmed' (or 'Paid') and a downloadable voucher PDF link/button appears on the Booking Confirmation or My Bookings -> Booking Detail page; initiating that link starts a non-empty .pdf download.

---

### [TC-002] Logged-out user attempting to open a protected page is redirected to Login page
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to <protected page> (enter protected page URL or click link to protected page)

**Original Expected Result:** The Login page is displayed; the Login form is visible, and access to the requested protected page is not granted.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Any page with the top-navigation Currency selector (e.g., Home page)`
- **Observe**:
  - currency selector displays the current/default currency (not <currency>)
  - sample prices on the page show the current/default currency symbol/format

**Post-Check**
- **Navigate To**: `Reload the current page (and optionally navigate to another page, e.g., Hotel listing) to confirm persistence`
- **Observe**:
  - currency selector displays <currency>
  - sample prices on the page show <currency> symbol/format

**Expected Change**: After selecting <currency> and reloading the page, the currency selector and visible prices remain set to <currency>, proving the selection persisted across page reload/navigation.

---

### [TC-006] Double-click Logout rapidly (duplicate click race)
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. From the authenticated session, click the Logout button
2. 2. Immediately (within milliseconds) click the Logout button again

**Original Expected Result:** First click succeeds: session termination runs, user is redirected to the home page. Second click is ignored (no duplicate logout or error shown). Subsequent navigation attempts to protected pages are blocked and redirect to the login page.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Any page with the top Language dropdown (e.g., User Dashboard or top navigation)`
- **Observe**:
  - language dropdown selected value is not 'Arabic'
  - example UI text (e.g., top navigation labels such as 'My Bookings') is displayed in the current non-Arabic language

**Post-Check**
- **Navigate To**: `Reload the current page (browser refresh) where the Language dropdown is located`
- **Observe**:
  - language dropdown selected value is '<language>' (English or Spanish or French)
  - example UI text (e.g., top navigation labels such as 'My Bookings') is displayed in '<language>'
  - page layout remains left-to-right (no RTL layout applied)

**Expected Change**: After selecting <language> and reloading, the Language dropdown remains set to <language> and visible UI text updates to the selected <language>, demonstrating that the language preference persisted across the page reload.

---

### [TC-011] Travel_Dates Start set one day after End should be blocked
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Offers_Filters form to open filter controls
2. 2. In Travel_Dates, set Start = <date B>
3. 3. In Travel_Dates, set End = <date A> where <date B> is exactly one day after <date A>
4. 4. Click Apply Filters

**Original Expected Result:** Travel_Dates field displays an inline error indicating the start date is after the end date and Apply Filters is blocked (error shown); Promotions_List is not changed

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Page containing the Language dropdown (top navigation) while logged in`
- **Observe**:
  - language dropdown shows the current selected language (e.g., English or site default) and Arabic is NOT selected
  - page layout/text direction is LTR (where applicable)

**Post-Check**
- **Navigate To**: `Reload the same page (or navigate away and return) containing the Language dropdown`
- **Observe**:
  - language dropdown displays 'Arabic' as the selected language
  - page UI text is presented in Arabic or layout switches to RTL where applicable

**Expected Change**: After selecting Arabic and reloading, the language dropdown remains set to Arabic and the UI reflects Arabic/RTL behavior, demonstrating persistence of the language selection.

---

### [TC-003] Attempt to invoke Logout action when user is not authenticated (precondition not met)
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is signed out (no active session)
2. 2. Navigate directly to the Logout URL / click the Logout endpoint link (attempt to trigger Logout while unauthenticated)

**Original Expected Result:** Navigation is blocked: the application redirects to the Login page and displays the login form. The Logout action is not performed (no session termination occurs because there is no active session). No protected content is shown.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Item Detail Page -> Reviews section`
- **Observe**:
  - reviews list does not contain an entry with the expected written feedback text submitted by the current user
  - no review entry exists showing the specific combination of Overall, Cleanliness, Service and Location ratings to be submitted

**Post-Check**
- **Navigate To**: `Item Detail Page -> Reviews section`
- **Observe**:
  - a new review entry authored by the current user is present
  - overall rating displays the submitted Overall rating
  - category ratings display the submitted Cleanliness, Service and Location values
  - written feedback text matches the submitted feedback
  - uploaded photo thumbnails appear in the review entry
  - reviews count or list position reflects the new review (e.g., count incremented or new row visible)

**Expected Change**: A new review is created and appears in the item's Reviews section showing the submitted Overall rating, the Cleanliness, Service and Location category ratings, the written feedback text, and the uploaded photo thumbnails; the reviews list/count reflects the added review.

---

### [TC-004] Unauthenticated state shows no action buttons (Logout not visible)
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `partial`

**Coverage Note**: *Some deployments moderate or queue submitted reviews and/or asynchronously process uploaded images. The success notification can be shown while the review is not immediately visible in the public Reviews section; image thumbnails may appear after processing.*

**Original Steps:**
1. 1. Ensure the user is signed out (no active session)
2. 2. Open the application UI area that normally contains session actions (header, user menu, or action bar)

**Original Expected Result:** The action bar / user menu does not display a 'Logout' button or any authenticated-only actions. There is no clickable Logout control visible in the Unauthenticated state (no action buttons are present).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Item Detail page -> Reviews section (or Dashboard -> My Reviews)`
- **Observe**:
  - record current total review count for the item
  - no review entry exists matching the expected reviewer username and the expected written feedback text
  - no recent review with the expected overall rating and photos (if photos will be uploaded)

**Post-Check**
- **Navigate To**: `Item Detail page -> Reviews section (refresh the page if necessary)`
- **Observe**:
  - a new review entry exists matching the reviewer username
  - the new review displays the entered overall rating value
  - the new review displays the entered written feedback text
  - any uploaded photos are shown as thumbnails or attachments on the review entry (if photos were uploaded)
  - category-specific rating fields are not displayed on the review entry (since applicable categories are absent)
  - total review count for the item has increased by 1 compared to pre_check (if the review is publicly visible)

**Expected Change**: A new review is created and associated with the item: the Reviews section contains an entry showing the submitted Overall Rating, the provided written feedback, and any uploaded photos; category-specific rating fields are not present on the review entry. If moderation or asynchronous processing is enabled, the UI may still show the success notification while the review or photos appear after a delay.

---

### [TC-003] Attempt to invoke Logout action when user is not authenticated (precondition not met)
**Category**: `negative` | **Verification Type**: `other` | **Coverage**: `partial`

**Coverage Note**: *The application displays an on-page success notification, but the persistent subscriber record is stored in backend systems or an external mailing service and there is no documented admin UI in the application to view subscriber lists. Delivery of a confirmation email can be checked in an external inbox, which provides partial verification of backend processing.*

**Original Steps:**
1. 1. Ensure the user is signed out (no active session)
2. 2. Navigate directly to the Logout URL / click the Logout endpoint link (attempt to trigger Logout while unauthenticated)

**Original Expected Result:** Navigation is blocked: the application redirects to the Login page and displays the login form. The Logout action is not performed (no session termination occurs because there is no active session). No protected content is shown.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Offers page -> Newsletter subscription section`
- **Observe**:
  - Email input field is empty or does not contain the test email
  - No on-page confirmation message reading 'subscribed to newsletter' is visible for the test email
  - No visible 'Subscribed' indicator in My Profile (if a newsletter preference exists) for the test email

**Post-Check**
- **Navigate To**: `Offers page -> Newsletter subscription section; additionally check the test user's external email inbox`
- **Observe**:
  - On-page success notification with text 'subscribed to newsletter' is visible
  - If the application sends a confirmation email, the test email inbox contains a new message from the application's email address referencing newsletter subscription (subject or body contains 'subscribe'/'subscription'/'newsletter')

**Expected Change**: After submitting the newsletter form the Offers page displays a 'subscribed to newsletter' confirmation notification and the test email receives a confirmation email if the system sends one; this provides partial evidence that the subscription was processed by the backend, but the actual subscriber record in the backend or external mailing list cannot be inspected within the application.

---

### [TC-001] Authenticated user clicks Logout and is returned to Home page
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button in the action bar

**Original Expected Result:** terminates current session; clears sensitive session data; redirects to home page; subsequent attempts to access protected pages redirect to login page. The Home page is displayed after logout.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard / My Bookings (an authenticated-only page)`
- **Observe**:
  - Top navigation shows authenticated user menu/avatar or 'My Account' label
  - Logout button is present in the user menu or header
  - Dashboard content (e.g., booking list, profile summary) is visible
  - Protected actions/links (My Bookings, Wallet, Settings) are accessible

**Post-Check**
- **Navigate To**: `Home page, then attempt to open a protected page (e.g., My Bookings or Dashboard)`
- **Observe**:
  - User is on the Home page (hero content or landing elements visible)
  - Top navigation shows Login and Signup links (no user avatar or 'My Account' menu)
  - Logout button is no longer present
  - Direct navigation to a protected URL (Dashboard / My Bookings) redirects to the Login page or shows an authentication prompt

**Expected Change**: The user session is terminated: the UI returns to the Home page showing unauthenticated navigation (Login/Signup) and user-specific menu/Logout are removed; attempts to access protected pages redirect to the Login page, confirming the session was cleared.

---
