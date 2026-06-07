# Post-Verification Specifications

### [TC-001] Send a secure message successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <valid subject> in the Subject field
2. 2. Select 'Technical' from the Category dropdown
3. 3. Enter <valid message body> in the Message Body field
4. 4. Click 'Send Message'

**Original Expected Result:** Message sent successfully with ticket ID

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Login page`
- **Observe**:
  - Login form is displayed
  - No user account exists for the provided email

**Post-Check**
- **Navigate To**: `Login page`
- **Observe**:
  - Login form is displayed
  - User can now log in with the new account credentials

**Expected Change**: The user can log in with the newly registered account using the provided credentials.

---

### [TC-001] Send a secure message successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <valid subject> in the Subject field
2. 2. Select 'Technical' from the Category dropdown
3. 3. Enter <valid message body> in the Message Body field
4. 4. Click 'Send Message'

**Original Expected Result:** Message sent successfully with ticket ID

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - account list does not contain the new Checking account

**Post-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - account list contains the new Checking account
  - status badge is 'Active'

**Expected Change**: A new Checking account entry is created with an initial deposit of $25 and is marked as 'Active'.

---

### [TC-002] Request a callback successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Select <valid reason for call> from the Reason for Call dropdown
2. 2. Enter <valid date> in the Preferred Date field
3. 3. Enter <valid time window> in the Preferred Time Window field
4. 4. Verify the Phone Number field is pre-filled
5. 5. Click 'Request Callback'

**Original Expected Result:** Callback request submitted and email confirmation sent

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - list of accounts does not include the new Savings account

**Post-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - list of accounts includes the new Savings account
  - Savings account balance is $100
  - Status is 'Active'

**Expected Change**: A new Savings account is created with an initial deposit of $100 and is displayed in the accounts overview.

---

### [TC-001] Send a secure message successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <valid subject> in the Subject field
2. 2. Select 'Technical' from the Category dropdown
3. 3. Enter <valid message body> in the Message Body field
4. 4. Click 'Send Message'

**Original Expected Result:** Message sent successfully with ticket ID

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - balance of Checking account before transfer

**Post-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - balance of Checking account after transfer
  - transaction history shows recent transfer

**Expected Change**: The Checking account balance is decreased by the transfer amount, and a new transaction entry is created in the transaction history.

---

### [TC-002] Request a callback successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Select <valid reason for call> from the Reason for Call dropdown
2. 2. Enter <valid date> in the Preferred Date field
3. 3. Enter <valid time window> in the Preferred Time Window field
4. 4. Verify the Phone Number field is pre-filled
5. 5. Click 'Request Callback'

**Original Expected Result:** Callback request submitted and email confirmation sent

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - Savings account balance

**Post-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - Savings account balance has decreased by <valid amount>

**Expected Change**: The Savings account balance reflects the deducted transfer amount to the external account.

---

### [TC-001] Send a secure message successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <valid subject> in the Subject field
2. 2. Select 'Technical' from the Category dropdown
3. 3. Enter <valid message body> in the Message Body field
4. 4. Click 'Send Message'

**Original Expected Result:** Message sent successfully with ticket ID

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - source account balance before payment

**Post-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - source account balance after payment
  - payment transaction in transaction history

**Expected Change**: The source account balance is reduced by the payment amount, and a new transaction entry is created in the transaction history.

---

### [TC-001] Send a secure message successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <valid subject> in the Subject field
2. 2. Select 'Technical' from the Category dropdown
3. 3. Enter <valid message body> in the Message Body field
4. 4. Click 'Send Message'

**Original Expected Result:** Message sent successfully with ticket ID

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - loan account not listed

**Post-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - loan account listed
  - loan amount matches submitted amount
  - status is 'Active'

**Expected Change**: A new personal loan account is created with the correct loan amount and status.

---

### [TC-002] Request a callback successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Select <valid reason for call> from the Reason for Call dropdown
2. 2. Enter <valid date> in the Preferred Date field
3. 3. Enter <valid time window> in the Preferred Time Window field
4. 4. Verify the Phone Number field is pre-filled
5. 5. Click 'Request Callback'

**Original Expected Result:** Callback request submitted and email confirmation sent

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - loan account not listed
  - total balance unchanged

**Post-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - new auto loan account listed
  - total balance reflects new loan amount

**Expected Change**: A new auto loan account is created and displayed in the Accounts Overview with the correct loan amount and down payment reflected in the total balance.

---

### [TC-003] Leave the Message Body field blank and submit
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Leave the Message Body field blank
2. 2. Fill in Subject and Category with valid values
3. 3. Click Send Message

**Original Expected Result:** Inline validation error appears on the Message Body field indicating it is required

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - list of existing loan accounts
  - loan amount not equal to the submitted amount

**Post-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - list of existing loan accounts
  - new home loan entry with the correct amount
  - status badge is 'Active'

**Expected Change**: A new home loan entry is created with the submitted loan amount and down payment.

---

### [TC-001] Send a secure message successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <valid subject> in the Subject field
2. 2. Select 'Technical' from the Category dropdown
3. 3. Enter <valid message body> in the Message Body field
4. 4. Click 'Send Message'

**Original Expected Result:** Message sent successfully with ticket ID

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> Update Contact Info`
- **Observe**:
  - First Name field contains existing value
  - Last Name field contains existing value
  - Street Address field contains existing value
  - City field contains existing value
  - State dropdown is pre-selected
  - ZIP Code field contains existing value
  - Phone Number field contains existing value

**Post-Check**
- **Navigate To**: `User Dashboard -> Update Contact Info`
- **Observe**:
  - First Name field contains <valid first name>
  - Last Name field contains <valid last name>
  - Street Address field contains <valid street address>
  - City field contains <valid city>
  - State dropdown is set to <valid state>
  - ZIP Code field contains <valid ZIP code>
  - Phone Number field contains <valid phone number>

**Expected Change**: The profile information is updated with the new values entered by the user.

---

### [TC-001] Send a secure message successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <valid subject> in the Subject field
2. 2. Select 'Technical' from the Category dropdown
3. 3. Enter <valid message body> in the Message Body field
4. 4. Click 'Send Message'

**Original Expected Result:** Message sent successfully with ticket ID

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Manage Cards`
- **Observe**:
  - no pending card requests

**Post-Check**
- **Navigate To**: `Manage Cards`
- **Observe**:
  - pending card request listed
  - status is 'Pending'

**Expected Change**: A new card request entry is created with the correct details and status.

---

### [TC-002] Request a callback successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Select <valid reason for call> from the Reason for Call dropdown
2. 2. Enter <valid date> in the Preferred Date field
3. 3. Enter <valid time window> in the Preferred Time Window field
4. 4. Verify the Phone Number field is pre-filled
5. 5. Click 'Request Callback'

**Original Expected Result:** Callback request submitted and email confirmation sent

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Manage Cards`
- **Observe**:
  - current spending limit for the selected card

**Post-Check**
- **Navigate To**: `Manage Cards`
- **Observe**:
  - updated spending limit for the selected card
  - travel notice details

**Expected Change**: The spending limit for the selected card is updated to the new valid limit, and the travel notice details are correctly reflected.

---

### [TC-001] Send a secure message successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <valid subject> in the Subject field
2. 2. Select 'Technical' from the Category dropdown
3. 3. Enter <valid message body> in the Message Body field
4. 4. Click 'Send Message'

**Original Expected Result:** Message sent successfully with ticket ID

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Investments -> Portfolio Snapshot`
- **Observe**:
  - portfolio balance
  - recent trades list does not contain the new trade

**Post-Check**
- **Navigate To**: `Investments -> Portfolio Snapshot`
- **Observe**:
  - portfolio balance reflects the new trade
  - recent trades list contains the new trade with order ID

**Expected Change**: The portfolio balance is updated to reflect the executed trade, and the recent trades list includes the new trade entry.

---

### [TC-002] Request a callback successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Select <valid reason for call> from the Reason for Call dropdown
2. 2. Enter <valid date> in the Preferred Date field
3. 3. Enter <valid time window> in the Preferred Time Window field
4. 4. Verify the Phone Number field is pre-filled
5. 5. Click 'Request Callback'

**Original Expected Result:** Callback request submitted and email confirmation sent

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Investments -> Recurring Investment Plans`
- **Observe**:
  - no plans listed

**Post-Check**
- **Navigate To**: `Investments -> Recurring Investment Plans`
- **Observe**:
  - new recurring investment plan listed
  - fund symbol
  - contribution amount
  - frequency
  - start date

**Expected Change**: A new recurring investment plan is created with the specified fund symbol, contribution amount, frequency, and start date.

---

### [TC-002] Request a callback successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Select <valid reason for call> from the Reason for Call dropdown
2. 2. Enter <valid date> in the Preferred Date field
3. 3. Enter <valid time window> in the Preferred Time Window field
4. 4. Verify the Phone Number field is pre-filled
5. 5. Click 'Request Callback'

**Original Expected Result:** Callback request submitted and email confirmation sent

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Profile -> Security Settings`
- **Observe**:
  - paperless checkbox is unchecked
  - email field is empty

**Post-Check**
- **Navigate To**: `User Profile -> Security Settings`
- **Observe**:
  - paperless checkbox is checked
  - email field contains the valid email address

**Expected Change**: The e-Statement preference is updated to opt into paperless statements with the provided email address.

---

### [TC-001] Send a secure message successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <valid subject> in the Subject field
2. 2. Select 'Technical' from the Category dropdown
3. 3. Enter <valid message body> in the Message Body field
4. 4. Click 'Send Message'

**Original Expected Result:** Message sent successfully with ticket ID

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Security Settings -> Change Password`
- **Observe**:
  - Current Password field is empty
  - New Password field is empty
  - Confirm New Password field is empty

**Post-Check**
- **Navigate To**: `Login page`
- **Observe**:
  - UI displays 'Password changed successfully.' message

**Expected Change**: The user can now log in with the new password, confirming that the password has been successfully updated.

---

### [TC-001] Send a secure message successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <valid subject> in the Subject field
2. 2. Select 'Technical' from the Category dropdown
3. 3. Enter <valid message body> in the Message Body field
4. 4. Click 'Send Message'

**Original Expected Result:** Message sent successfully with ticket ID

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Support Center -> My Messages`
- **Observe**:
  - no recent messages

**Post-Check**
- **Navigate To**: `Support Center -> My Messages`
- **Observe**:
  - message with ticket ID
  - subject matches <valid subject>
  - category is 'Technical'

**Expected Change**: A new message entry is created with the correct subject and category, and a ticket ID is generated.

---

### [TC-002] Request a callback successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Select <valid reason for call> from the Reason for Call dropdown
2. 2. Enter <valid date> in the Preferred Date field
3. 3. Enter <valid time window> in the Preferred Time Window field
4. 4. Verify the Phone Number field is pre-filled
5. 5. Click 'Request Callback'

**Original Expected Result:** Callback request submitted and email confirmation sent

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Support Center -> Schedule Callback`
- **Observe**:
  - Phone Number field is pre-filled with user's phone number

**Post-Check**
- **Navigate To**: `Support Center -> Scheduled Callbacks`
- **Observe**:
  - Callback request listed with correct details
  - Confirmation email received

**Expected Change**: A new callback request is displayed in the Scheduled Callbacks section, confirming the user's request.

---
