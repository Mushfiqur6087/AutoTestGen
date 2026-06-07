# Post-Verification Specifications

### [TC-001] User successfully logs out
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Logout_Button

**Original Expected Result:** terminates the current session and clears sensitive session data; user is redirected to the home page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard`
- **Observe**:
  - user account does not exist in the system

**Post-Check**
- **Navigate To**: `User Dashboard`
- **Observe**:
  - user account is created and visible in the user list
  - welcome message displayed

**Expected Change**: A new user account is created with the provided details and is visible in the user management section.

---

### [TC-001] User successfully logs out
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Logout_Button

**Original Expected Result:** terminates the current session and clears sensitive session data; user is redirected to the home page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Login page`
- **Observe**:
  - Email input field is empty

**Post-Check**
- **Navigate To**: `Login page`
- **Observe**:
  - UI displays 'Reset link sent' message

**Expected Change**: A confirmation message is displayed indicating that the reset link has been sent to the provided email.

---

### [TC-002] Attempt to access a protected page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button

**Original Expected Result:** User is redirected to the login page when attempting to access a protected page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Login page`
- **Observe**:
  - Login form is visible
  - Password reset link is not available

**Post-Check**
- **Navigate To**: `Login page`
- **Observe**:
  - Login form is visible
  - Success message indicates password has been changed

**Expected Change**: The user is redirected to the login page and can now log in with the new password.

---

### [TC-002] Attempt to access a protected page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button

**Original Expected Result:** User is redirected to the login page when attempting to access a protected page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - booking list does not contain the new hotel reservation

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - booking list contains the new hotel reservation
  - status badge is 'Pending'

**Expected Change**: A new booking entry is created for the selected hotel with the correct details.

---

### [TC-001] User successfully logs out
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Logout_Button

**Original Expected Result:** terminates the current session and clears sensitive session data; user is redirected to the home page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - booking list does not contain the new booking entry

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - booking list contains the new booking entry
  - status is 'Pending'

**Expected Change**: A new booking entry is created for the selected stay dates with the correct guest count and user details.

---

### [TC-001] User successfully logs out
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Logout_Button

**Original Expected Result:** terminates the current session and clears sensitive session data; user is redirected to the home page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - booking list does not contain the new booking entry

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - booking list contains the new booking entry
  - status is 'Pending'

**Expected Change**: A new booking entry is created with the correct traveler details and is awaiting payment.

---

### [TC-001] User successfully logs out
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Logout_Button

**Original Expected Result:** terminates the current session and clears sensitive session data; user is redirected to the home page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - booking list does not contain the new tour reservation

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - booking list contains the new tour reservation
  - status badge is 'Pending'

**Expected Change**: A new booking entry is created for the selected tour with the correct departure date and traveler count.

---

### [TC-002] Attempt to access a protected page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button

**Original Expected Result:** User is redirected to the login page when attempting to access a protected page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - booking list does not contain the new vehicle reservation

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - booking list contains the new vehicle reservation
  - status is 'Confirmed'

**Expected Change**: A new booking entry is created for the selected vehicle with the correct details.

---

### [TC-001] User successfully logs out
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Logout_Button

**Original Expected Result:** terminates the current session and clears sensitive session data; user is redirected to the home page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - booking list does not contain the new car rental booking

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - booking list contains the new car rental booking
  - status is 'Pending'

**Expected Change**: A new car rental booking entry is created with the correct details and status.

---

### [TC-001] User successfully logs out
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Logout_Button

**Original Expected Result:** terminates the current session and clears sensitive session data; user is redirected to the home page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - no visa application entry present

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - visa application entry present
  - status is 'Pending'

**Expected Change**: A new visa application entry is created with the correct details and status reflecting the submitted application.

---

### [TC-002] Attempt to access a protected page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button

**Original Expected Result:** User is redirected to the login page when attempting to access a protected page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - booking status is 'Confirmed'

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - booking status is 'Cancelled'
  - success message displayed

**Expected Change**: The booking status changes from 'Confirmed' to 'Cancelled', and a success message is displayed.

---

### [TC-001] User successfully logs out
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Logout_Button

**Original Expected Result:** terminates the current session and clears sensitive session data; user is redirected to the home page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - booking details
  - travel dates
  - special requests
  - traveler information

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - updated travel dates
  - updated special requests
  - updated traveler information

**Expected Change**: The booking details reflect the modifications made, including changes to travel dates, special requests, and traveler information.

---

### [TC-001] User successfully logs out
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Logout_Button

**Original Expected Result:** terminates the current session and clears sensitive session data; user is redirected to the home page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - booking list does not contain the new booking entry

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - booking list contains the new booking entry
  - status is 'Confirmed'

**Expected Change**: A new booking entry is created with the correct details and status after the payment is successfully processed.

---

### [TC-002] Attempt to access a protected page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button

**Original Expected Result:** User is redirected to the login page when attempting to access a protected page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - no recent bookings listed

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - recent booking with reference number displayed
  - status is 'Confirmed'

**Expected Change**: A new booking entry is created with the correct reference number after successful payment via PayPal.

---

### [TC-003] Attempt to click Logout button when already logged out
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button

**Original Expected Result:** No action occurs; user remains on the current page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - booking list does not contain the new booking entry

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - booking list contains the new booking entry
  - status is 'Pending'

**Expected Change**: A new booking entry is created with the correct reference number after the payment submission.

---

### [TC-004] Rapid logout attempts
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button
2. 2. Immediately click the Logout button again

**Original Expected Result:** Second logout attempt is blocked; user remains on the home page without session termination

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - booking list does not contain the new booking entry

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - booking list contains the new booking entry
  - status is 'Confirmed'

**Expected Change**: A new booking entry is created with the correct reference number after the payment is processed.

---

### [TC-001] User successfully logs out
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Logout_Button

**Original Expected Result:** terminates the current session and clears sensitive session data; user is redirected to the home page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Reviews`
- **Observe**:
  - no reviews submitted by the user

**Post-Check**
- **Navigate To**: `User Dashboard -> My Reviews`
- **Observe**:
  - new review entry is displayed
  - status is 'Pending'

**Expected Change**: A new review entry is created with the submitted ratings and feedback.

---

### [TC-002] Attempt to access a protected page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button

**Original Expected Result:** User is redirected to the login page when attempting to access a protected page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Offers page`
- **Observe**:
  - subscription confirmation message is not displayed

**Post-Check**
- **Navigate To**: `Offers page`
- **Observe**:
  - subscription confirmation message is displayed
  - user receives confirmation email

**Expected Change**: The user receives a confirmation message indicating that the email has been submitted for future exclusive deals.

---
