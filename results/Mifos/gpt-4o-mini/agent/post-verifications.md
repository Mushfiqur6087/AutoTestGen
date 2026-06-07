# Post-Verification Specifications

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Clients page`
- **Observe**:
  - client list does not contain the new client with the unique external ID

**Post-Check**
- **Navigate To**: `Clients page`
- **Observe**:
  - client list contains the new client with the unique external ID
  - status is 'Pending'

**Expected Change**: A new client entry is created with the correct details and is in Pending status.

---

### [TC-004] Rapid logout attempts
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Click on 'Log Out'
3. 3. Immediately click on the User Profile Icon again
4. 4. Click on 'Log Out' again

**Original Expected Result:** Second logout attempt is blocked; user remains on the login page without a second session being created.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Management -> Client Detail`
- **Observe**:
  - status badge is 'Pending'

**Post-Check**
- **Navigate To**: `Client Management -> Client Detail`
- **Observe**:
  - status badge is 'Active'

**Expected Change**: The client status changes from 'Pending' to 'Active' after the activation process.

---

### [TC-005] Navigate to authenticated page after logout
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Management -> Clients List`
- **Observe**:
  - client status is 'Pending'
  - client details do not reflect the new value for <field>

**Post-Check**
- **Navigate To**: `Client Management -> Clients List`
- **Observe**:
  - client status remains 'Pending'
  - client details reflect the updated value for <field>

**Expected Change**: The client details are updated with the new value for <field> while the status remains 'Pending'.

---

### [TC-006] Attempt to start all jobs when none are scheduled
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Start All

**Original Expected Result:** No jobs started; error message displayed indicating there are no scheduled jobs to start

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Management -> Client List`
- **Observe**:
  - client status is 'Pending'

**Post-Check**
- **Navigate To**: `Client Management -> Client List`
- **Observe**:
  - client status is 'Rejected'

**Expected Change**: The client's status changes from 'Pending' to 'Rejected' after the rejection action is confirmed.

---

### [TC-007] Attempt to stop all jobs when none are running
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Stop All

**Original Expected Result:** No jobs stopped; error message displayed indicating there are no jobs currently running

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Management -> Client List`
- **Observe**:
  - client status is 'Pending'

**Post-Check**
- **Navigate To**: `Client Management -> Client List`
- **Observe**:
  - client status is 'Withdrawn'

**Expected Change**: The client's status changes from 'Pending' to 'Withdrawn' after the withdrawal action.

---

### [TC-008] Add maximum allowed entries to Column Definitions
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a valid Data Table Name in the Data_Table_Name field
2. 2. Select an Application Table Name from the dropdown
3. 3. Add exactly maximum allowed entries to the Column Definitions repeating group

**Original Expected Result:** Form submits successfully; custom data table is created with the maximum number of column definitions

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Management -> Client List`
- **Observe**:
  - client status is 'Active'
  - client is listed under current office

**Post-Check**
- **Navigate To**: `Client Management -> Client List`
- **Observe**:
  - client status is 'Active'
  - client is listed under new destination office

**Expected Change**: The client is successfully transferred to the new destination office and remains in 'Active' status.

---

### [TC-009] Attempt to add one more entry to Column Definitions
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a valid Data Table Name in the Data_Table_Name field
2. 2. Select an Application Table Name from the dropdown
3. 3. Add maximum allowed entries to the Column Definitions repeating group
4. 4. Attempt to add one more entry to the Column Definitions

**Original Expected Result:** Attempt to add entry is blocked; visible error shown indicating maximum entries reached

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Management -> Active Clients`
- **Observe**:
  - client status is 'Active'

**Post-Check**
- **Navigate To**: `Client Management -> Closed Clients`
- **Observe**:
  - client status is 'Closed'

**Expected Change**: The client status changes from 'Active' to 'Closed' and is no longer visible in the Active Clients list.

---

### [TC-010] Enter maximum length for Name in Column Definitions
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a valid Data Table Name in the Data_Table_Name field
2. 2. Select an Application Table Name from the dropdown
3. 3. Add an entry to the Column Definitions repeating group
4. 4. Enter exactly maximum length for the Name field

**Original Expected Result:** Form submits successfully; custom data table is created with the maximum length Name

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Detail Page`
- **Observe**:
  - charges list does not contain the new charge

**Post-Check**
- **Navigate To**: `Client Detail Page`
- **Observe**:
  - charges list contains the new charge
  - charge details are correct

**Expected Change**: A new charge entry is created for the client with the correct details.

---

### [TC-011] Enter one character less than maximum length for Name in Column Definitions
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a valid Data Table Name in the Data_Table_Name field
2. 2. Select an Application Table Name from the dropdown
3. 3. Add an entry to the Column Definitions repeating group
4. 4. Enter one character less than the maximum length for the Name field

**Original Expected Result:** Form submits successfully; custom data table is created with the Name field accepted

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Profile -> Loans`
- **Observe**:
  - loan list does not contain the new loan entry

**Post-Check**
- **Navigate To**: `Client Profile -> Loans`
- **Observe**:
  - loan list contains the new loan entry
  - loan status is 'Pending Approval'

**Expected Change**: A new loan entry is created for the client with the correct details and status.

---

### [TC-012] Enter long text in Data Table Name
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a very long string (200+ characters) in the Data_Table_Name field

**Original Expected Result:** Form submission is either accepted or truncated with a visible indicator

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Profile -> Savings Accounts`
- **Observe**:
  - savings accounts list does not contain the new savings account

**Post-Check**
- **Navigate To**: `Client Profile -> Savings Accounts`
- **Observe**:
  - savings accounts list contains the new savings account
  - status is 'Active'

**Expected Change**: A new savings account is created for the active client with the correct details.

---

### [TC-013] Enter special characters in Data Table Name
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter special characters in the Data_Table_Name field

**Original Expected Result:** Form submission is either accepted or a specific error shown

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Profile -> Share Accounts`
- **Observe**:
  - list does not contain the new share account

**Post-Check**
- **Navigate To**: `Client Profile -> Share Accounts`
- **Observe**:
  - list contains the new share account
  - account status is 'Active'

**Expected Change**: A new share account is created for the active client with the correct details.

---

### [TC-014] Enter leading/trailing whitespace in Data Table Name
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a value with leading/trailing spaces in the Data_Table_Name field

**Original Expected Result:** Leading/trailing whitespace is trimmed; saved value shown on detail page has no extra spaces

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Management -> Closed Clients`
- **Observe**:
  - client status is 'Closed'

**Post-Check**
- **Navigate To**: `Client Management -> Active Clients`
- **Observe**:
  - client status is 'Active'

**Expected Change**: The client status changes from 'Closed' to 'Active' after reactivation.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Groups page`
- **Observe**:
  - group list does not contain the new group

**Post-Check**
- **Navigate To**: `Groups page`
- **Observe**:
  - group list contains the new group
  - group name is '<valid group name>'
  - status is 'Pending'

**Expected Change**: A new group entry is created with the specified name and office.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Groups Management -> Groups List`
- **Observe**:
  - list does not contain the newly imported groups

**Post-Check**
- **Navigate To**: `Groups Management -> Groups List`
- **Observe**:
  - list contains the newly imported groups
  - status badge indicates 'Active'

**Expected Change**: The groups imported from the file are now visible in the groups list with the correct status.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Group Management -> Group List`
- **Observe**:
  - group status is 'Pending'

**Post-Check**
- **Navigate To**: `Group Management -> Group List`
- **Observe**:
  - group status is 'Active'

**Expected Change**: The group status changes from 'Pending' to 'Active' after activation.

---

### [TC-004] Rapid logout attempts
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Click on 'Log Out'
3. 3. Immediately click on the User Profile Icon again
4. 4. Click on 'Log Out' again

**Original Expected Result:** Second logout attempt is blocked; user remains on the login page without a second session being created.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Group Management -> View Group Details`
- **Observe**:
  - group name
  - group description
  - group members

**Post-Check**
- **Navigate To**: `Group Management -> View Group Details`
- **Observe**:
  - updated group name
  - updated group description
  - group members

**Expected Change**: The group details reflect the updated information as submitted.

---

### [TC-005] Navigate to authenticated page after logout
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Groups page`
- **Observe**:
  - group status is 'Active'

**Post-Check**
- **Navigate To**: `Groups page`
- **Observe**:
  - group status is 'Closed'

**Expected Change**: The group status changes from 'Active' to 'Closed' after the closure action.

---

### [TC-006] Attempt to start all jobs when none are scheduled
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Start All

**Original Expected Result:** No jobs started; error message displayed indicating there are no scheduled jobs to start

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Group Management -> Group Details`
- **Observe**:
  - staff list does not include the newly assigned staff

**Post-Check**
- **Navigate To**: `Group Management -> Group Details`
- **Observe**:
  - staff list includes the newly assigned staff
  - status message confirms assignment

**Expected Change**: The staff member is now listed as assigned to the group.

---

### [TC-007] Attempt to stop all jobs when none are running
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Stop All

**Original Expected Result:** No jobs stopped; error message displayed indicating there are no jobs currently running

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Group Management -> Group Details`
- **Observe**:
  - list of clients in the group
  - Transfer Clients button is visible

**Post-Check**
- **Navigate To**: `Group Management -> Group Details`
- **Observe**:
  - list of clients no longer includes the transferred clients
  - status of transferred clients is updated in their respective profiles

**Expected Change**: The selected clients are no longer listed in the group, confirming they have been successfully transferred.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Centers page`
- **Observe**:
  - list of centers does not contain the new center name

**Post-Check**
- **Navigate To**: `Centers page`
- **Observe**:
  - list of centers contains the new center name
  - status is 'Active'

**Expected Change**: A new center entry is created with the specified name and is visible in the centers list.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Centers page`
- **Observe**:
  - list of centers is empty or does not contain the newly imported centers

**Post-Check**
- **Navigate To**: `Centers page`
- **Observe**:
  - list of centers contains the newly imported centers
  - success notification is displayed

**Expected Change**: The centers list is updated to include the newly imported centers from the uploaded file.

---

### [TC-004] Rapid logout attempts
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Click on 'Log Out'
3. 3. Immediately click on the User Profile Icon again
4. 4. Click on 'Log Out' again

**Original Expected Result:** Second logout attempt is blocked; user remains on the login page without a second session being created.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Center Management -> Center Detail`
- **Observe**:
  - status badge is 'Inactive'

**Post-Check**
- **Navigate To**: `Center Management -> Center Detail`
- **Observe**:
  - status badge is 'Active'

**Expected Change**: The center status changes from 'Inactive' to 'Active' after activation.

---

### [TC-005] Navigate to authenticated page after logout
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Center Management -> Center Detail`
- **Observe**:
  - center name
  - center status
  - center details

**Post-Check**
- **Navigate To**: `Center Management -> Center Detail`
- **Observe**:
  - center name updated to <new value>
  - status badge is 'Active'

**Expected Change**: The center details reflect the updated information with the new value for the modified field.

---

### [TC-006] Attempt to start all jobs when none are scheduled
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Start All

**Original Expected Result:** No jobs started; error message displayed indicating there are no scheduled jobs to start

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Centers page`
- **Observe**:
  - Center status is 'Active'

**Post-Check**
- **Navigate To**: `Centers page`
- **Observe**:
  - Center status is 'Closed'

**Expected Change**: The center status changes from 'Active' to 'Closed' after the closure action is confirmed.

---

### [TC-007] Attempt to stop all jobs when none are running
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Stop All

**Original Expected Result:** No jobs stopped; error message displayed indicating there are no jobs currently running

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Center Detail page`
- **Observe**:
  - staff assignment list does not contain the newly assigned staff member

**Post-Check**
- **Navigate To**: `Center Detail page`
- **Observe**:
  - staff assignment list contains the newly assigned staff member

**Expected Change**: The staff member is successfully assigned to the center and appears in the staff assignment list.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Products page`
- **Observe**:
  - data table displays existing loan products
  - Edit option is available for the selected loan product

**Post-Check**
- **Navigate To**: `Loan Product detail view`
- **Observe**:
  - loan product details are displayed
  - Edit fields are populated with existing data

**Expected Change**: The detail view of the loan product opens, showing all relevant information for editing.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Products page`
- **Observe**:
  - no new loan product entry in the list

**Post-Check**
- **Navigate To**: `Loan Products page`
- **Observe**:
  - new loan product entry is not yet visible until Step 2 is completed

**Expected Change**: The user is still on the Loan Products page, and the new loan product has not been created until Step 2 is completed.

---

### [TC-004] Rapid logout attempts
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Click on 'Log Out'
3. 3. Immediately click on the User Profile Icon again
4. 4. Click on 'Log Out' again

**Original Expected Result:** Second logout attempt is blocked; user remains on the login page without a second session being created.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Products page`
- **Observe**:
  - no new loan product entry in the list

**Post-Check**
- **Navigate To**: `Loan Products page`
- **Observe**:
  - new loan product entry appears in the list
  - status is 'Pending'

**Expected Change**: A new loan product entry is created with the selected currency and specified parameters.

---

### [TC-005] Navigate to authenticated page after logout
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Products -> Create Loan Product -> Step 4`
- **Observe**:
  - Step 4 is not displayed
  - User is still on Step 3

**Post-Check**
- **Navigate To**: `Loan Products -> Create Loan Product -> Step 4`
- **Observe**:
  - Step 4 is displayed
  - Repayment Strategy is set to <Repayment Strategy>
  - Grace Period is <Grace Period>
  - Arrears Tolerance is <Arrears Tolerance>

**Expected Change**: The user successfully proceeds to Step 4 of the Create Loan Product process with the selected repayment strategy and entered values.

---

### [TC-006] Attempt to start all jobs when none are scheduled
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Start All

**Original Expected Result:** No jobs started; error message displayed indicating there are no scheduled jobs to start

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Products -> Create Loan Product -> Step 5`
- **Observe**:
  - Step 5 is not displayed
  - User remains on Step 4

**Post-Check**
- **Navigate To**: `Loan Products -> Create Loan Product -> Step 5`
- **Observe**:
  - Step 5 is displayed
  - All entered values are retained

**Expected Change**: The user successfully proceeds to Step 5 of the Create Loan Product process.

---

### [TC-008] Add maximum allowed entries to Column Definitions
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a valid Data Table Name in the Data_Table_Name field
2. 2. Select an Application Table Name from the dropdown
3. 3. Add exactly maximum allowed entries to the Column Definitions repeating group

**Original Expected Result:** Form submits successfully; custom data table is created with the maximum number of column definitions

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Products List`
- **Observe**:
  - loan product does not appear in the list

**Post-Check**
- **Navigate To**: `Loan Products List`
- **Observe**:
  - loan product appears in the list
  - success message displayed

**Expected Change**: A new loan product is created and displayed in the loan products list.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Savings Products page`
- **Observe**:
  - list does not contain the new savings product

**Post-Check**
- **Navigate To**: `Savings Products page`
- **Observe**:
  - list contains the new savings product
  - product name matches <valid product name>
  - short name matches <valid short name>

**Expected Change**: A new savings product is created and displayed in the list with the correct name and details.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Savings Products page`
- **Observe**:
  - list does not contain the new fixed deposit product

**Post-Check**
- **Navigate To**: `Savings Products page`
- **Observe**:
  - list contains the new fixed deposit product
  - product name is <valid product name>
  - status is 'Active'

**Expected Change**: A new fixed deposit product is created and displayed in the savings products list with the correct name and status.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Savings Products page`
- **Observe**:
  - list does not contain the new recurring deposit product

**Post-Check**
- **Navigate To**: `Savings Products page`
- **Observe**:
  - list contains the new recurring deposit product
  - status is 'Active'

**Expected Change**: A new recurring deposit product is created and displayed in the list with the correct status.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Products page`
- **Observe**:
  - list of existing share products does not contain the new product

**Post-Check**
- **Navigate To**: `Share Products page`
- **Observe**:
  - list of existing share products contains the new product
  - product name is <valid product name>
  - status is 'Active'

**Expected Change**: A new share product entry is created with the specified details and is visible in the share products list.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Products page`
- **Observe**:
  - existing product name
  - existing short name
  - existing description

**Post-Check**
- **Navigate To**: `Share Products page`
- **Observe**:
  - updated product name
  - updated short name
  - updated description

**Expected Change**: The share product details are updated with the new product name, short name, and description.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Products page`
- **Observe**:
  - list of share products includes the deleted product

**Post-Check**
- **Navigate To**: `Share Products page`
- **Observe**:
  - list of share products does not include the deleted product
  - success message displayed

**Expected Change**: The deleted share product is no longer listed on the Share Products page.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Charges List`
- **Observe**:
  - Charge Name <Charge Name> not present in the list

**Post-Check**
- **Navigate To**: `Charges List`
- **Observe**:
  - Charge Name <Charge Name> present in the list
  - Charge status is 'Active'

**Expected Change**: A new charge definition is created and displayed in the charges list with the correct details.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Charges Table`
- **Observe**:
  - Charge Name field displays the original charge name

**Post-Check**
- **Navigate To**: `Charges Table`
- **Observe**:
  - Charge Name field displays the updated charge name

**Expected Change**: The charge definition is updated with the new charge name.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Charges page`
- **Observe**:
  - charge entry in the Charges Table

**Post-Check**
- **Navigate To**: `Charges page`
- **Observe**:
  - charge entry is no longer present in the Charges Table

**Expected Change**: The charge is successfully deleted and does not appear in the Charges Table.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Floating Rates page`
- **Observe**:
  - list of existing floating rates does not include the new rate

**Post-Check**
- **Navigate To**: `Floating Rates page`
- **Observe**:
  - list of existing floating rates includes the new rate
  - new rate name is '<Floating Rate Name>'
  - interest rate is '<Interest Rate>'

**Expected Change**: A new floating rate entry is created with the specified name and interest rate.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Floating Rates List`
- **Observe**:
  - <Floating Rate Name> in the list

**Post-Check**
- **Navigate To**: `Floating Rates List`
- **Observe**:
  - <Modified Floating Rate Name> in the list

**Expected Change**: The floating rate name is updated to the modified value in the list.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Delinquency Management -> Delinquency Ranges`
- **Observe**:
  - list of delinquency ranges does not contain the new range

**Post-Check**
- **Navigate To**: `Delinquency Management -> Delinquency Ranges`
- **Observe**:
  - list of delinquency ranges contains the new range
  - classification is <valid classification>
  - minimum age days is <valid minimum age days>
  - maximum age days is <valid maximum age days>

**Expected Change**: A new delinquency range is created with the specified classification and age days.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Delinquency Management -> Delinquency Buckets`
- **Observe**:
  - list of delinquency buckets does not contain the new bucket

**Post-Check**
- **Navigate To**: `Delinquency Management -> Delinquency Buckets`
- **Observe**:
  - list of delinquency buckets contains the new bucket
  - bucket name is '<valid bucket name>'
  - minimum age days is '<valid minimum age days>'
  - maximum age days is '<valid maximum age days>'

**Expected Change**: A new delinquency bucket is created with the specified name and age range.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Dashboard`
- **Observe**:
  - loan application list does not contain the new loan application

**Post-Check**
- **Navigate To**: `Loan Dashboard`
- **Observe**:
  - loan application list contains the new loan application
  - status is 'Submitted'

**Expected Change**: A new loan application entry is created with the correct details and status.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Actor A (Role: `loan officer`)**
- **Action**: Approve the loan application as per the core test case steps.

**Actor B (Role: `loan manager`)**
- **Session**: `new_session`
- **Navigate To**: `Loan Management -> Approved Loans`
- **Action**: 
- **Observe**:
  - loan application status
  - approved amount
  - approved on date
  - expected disbursement date

**Expected Change**: The loan application status changes to 'Approved' with the correct approved amount and dates displayed.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Actor A (Role: `loan officer`)**
- **Action**: Reject the loan application from the Loan Detail page.

**Actor B (Role: `loan manager`)**
- **Session**: `new_session`
- **Navigate To**: `Loan Management -> Rejected Applications`
- **Action**: 
- **Observe**:
  - loan application status
  - loan application details

**Expected Change**: The loan application is listed under Rejected Applications with the status updated to 'Rejected'.

---

### [TC-004] Rapid logout attempts
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Click on 'Log Out'
3. 3. Immediately click on the User Profile Icon again
4. 4. Click on 'Log Out' again

**Original Expected Result:** Second logout attempt is blocked; user remains on the login page without a second session being created.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Loan Applications`
- **Observe**:
  - loan application status is 'Pending Approval'

**Post-Check**
- **Navigate To**: `User Dashboard -> My Loan Applications`
- **Observe**:
  - loan application status is 'Withdrawn'

**Expected Change**: The loan application status changes from 'Pending Approval' to 'Withdrawn' after the withdrawal action.

---

### [TC-005] Navigate to authenticated page after logout
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Management -> Pending Applications`
- **Observe**:
  - loan application is listed with status 'Pending Approval'

**Post-Check**
- **Navigate To**: `Loan Management -> Pending Applications`
- **Observe**:
  - loan application is no longer listed

**Expected Change**: The loan application is successfully deleted and does not appear in the pending applications list.

---

### [TC-006] Attempt to start all jobs when none are scheduled
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Start All

**Original Expected Result:** No jobs started; error message displayed indicating there are no scheduled jobs to start

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Dashboard`
- **Observe**:
  - loan application status is 'Approved'
  - loan disbursement history is empty

**Post-Check**
- **Navigate To**: `Loan Dashboard`
- **Observe**:
  - loan application status is 'Active'
  - loan disbursement history shows new entry with correct amount and date

**Expected Change**: The loan application status changes to 'Active' and a new disbursement entry is recorded in the loan disbursement history.

---

### [TC-007] Attempt to stop all jobs when none are running
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Stop All

**Original Expected Result:** No jobs stopped; error message displayed indicating there are no jobs currently running

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - transaction history does not contain the new repayment entry

**Post-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - transaction history contains the new repayment entry
  - outstanding balance is updated accordingly

**Expected Change**: A new repayment entry is created in the transaction history with the correct transaction date and amount, and the outstanding balance is reduced.

---

### [TC-008] Add maximum allowed entries to Column Definitions
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a valid Data Table Name in the Data_Table_Name field
2. 2. Select an Application Table Name from the dropdown
3. 3. Add exactly maximum allowed entries to the Column Definitions repeating group

**Original Expected Result:** Form submits successfully; custom data table is created with the maximum number of column definitions

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - interest amount displayed
  - interest waiver option is available

**Post-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - interest amount is updated to reflect waived interest
  - interest waiver confirmation message is displayed

**Expected Change**: The interest amount is reduced to reflect the waived interest, and a confirmation message is shown indicating the successful waiver.

---

### [TC-009] Attempt to add one more entry to Column Definitions
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a valid Data Table Name in the Data_Table_Name field
2. 2. Select an Application Table Name from the dropdown
3. 3. Add maximum allowed entries to the Column Definitions repeating group
4. 4. Attempt to add one more entry to the Column Definitions

**Original Expected Result:** Attempt to add entry is blocked; visible error shown indicating maximum entries reached

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - loan status is 'Active'

**Post-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - loan status is 'Written Off'
  - write-off reason is displayed

**Expected Change**: The loan status changes from 'Active' to 'Written Off', indicating the loan has been successfully written off.

---

### [TC-010] Enter maximum length for Name in Column Definitions
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a valid Data Table Name in the Data_Table_Name field
2. 2. Select an Application Table Name from the dropdown
3. 3. Add an entry to the Column Definitions repeating group
4. 4. Enter exactly maximum length for the Name field

**Original Expected Result:** Form submits successfully; custom data table is created with the maximum length Name

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - status badge shows 'Active'

**Post-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - status badge shows 'Closed'

**Expected Change**: The loan status changes from 'Active' to 'Closed' after the closure action is confirmed.

---

### [TC-011] Enter one character less than maximum length for Name in Column Definitions
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a valid Data Table Name in the Data_Table_Name field
2. 2. Select an Application Table Name from the dropdown
3. 3. Add an entry to the Column Definitions repeating group
4. 4. Enter one character less than the maximum length for the Name field

**Original Expected Result:** Form submits successfully; custom data table is created with the Name field accepted

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - current due date
  - status is 'Active'

**Post-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - new adjusted due date
  - status reflects rescheduled state

**Expected Change**: The loan's adjusted due date is updated to the new date provided, and the status indicates that the loan has been rescheduled.

---

### [TC-012] Enter long text in Data Table Name
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a very long string (200+ characters) in the Data_Table_Name field

**Original Expected Result:** Form submission is either accepted or truncated with a visible indicator

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - outstanding balance shows the original loan amount
  - no prepayment transaction listed

**Post-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - outstanding balance reflects the new amount after prepayment
  - prepayment transaction listed in transaction history

**Expected Change**: The outstanding balance is reduced by the prepayment amount, and a new transaction entry for the prepayment is visible in the transaction history.

---

### [TC-013] Enter special characters in Data Table Name
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter special characters in the Data_Table_Name field

**Original Expected Result:** Form submission is either accepted or a specific error shown

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - Loan status is 'Active'

**Post-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - Loan status is 'Foreclosed'

**Expected Change**: The loan status changes from 'Active' to 'Foreclosed' after the foreclosure action is confirmed.

---

### [TC-014] Enter leading/trailing whitespace in Data Table Name
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a value with leading/trailing spaces in the Data_Table_Name field

**Original Expected Result:** Leading/trailing whitespace is trimmed; saved value shown on detail page has no extra spaces

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - loan status is 'Active'

**Post-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - loan status is 'Charged Off'
  - charge off reason is displayed

**Expected Change**: The loan status changes from 'Active' to 'Charged Off' after the charge off action is confirmed.

---

### [TC-015] Create Holiday with From_Date one day before To_Date
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click + Create Holiday
2. 2. Enter a valid Name in the Name field
3. 3. Enter today's date in the From_Date field
4. 4. Enter tomorrow's date in the To_Date field
5. 5. Click Submit

**Original Expected Result:** Holiday is created successfully; From_Date is today and To_Date is tomorrow

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - current loan officer is not <new loan officer>

**Post-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - current loan officer is <new loan officer>

**Expected Change**: The loan officer assigned to the loan application has changed to <new loan officer>.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Detail page -> Savings Accounts`
- **Observe**:
  - savings account list does not contain the new account

**Post-Check**
- **Navigate To**: `Client Detail page -> Savings Accounts`
- **Observe**:
  - savings account list contains the new account
  - status is 'Submitted and Pending Approval'

**Expected Change**: A new savings account entry is created with the correct details and status.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Savings Account Detail`
- **Observe**:
  - current balance before deposit

**Post-Check**
- **Navigate To**: `Savings Account Detail`
- **Observe**:
  - current balance after deposit
  - transaction history shows new deposit entry

**Expected Change**: The current balance reflects the deposit amount added to the previous balance.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Savings Account Detail`
- **Observe**:
  - current balance is greater than or equal to the withdrawal amount
  - transaction history does not show the recent withdrawal

**Post-Check**
- **Navigate To**: `Savings Account Detail`
- **Observe**:
  - current balance is decreased by the withdrawal amount
  - transaction history shows the recent withdrawal transaction

**Expected Change**: The current balance reflects the withdrawal amount deducted, and the transaction history includes the new withdrawal entry.

---

### [TC-004] Rapid logout attempts
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Click on 'Log Out'
3. 3. Immediately click on the User Profile Icon again
4. 4. Click on 'Log Out' again

**Original Expected Result:** Second logout attempt is blocked; user remains on the login page without a second session being created.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Savings Account Details`
- **Observe**:
  - current balance
  - interest not yet posted

**Post-Check**
- **Navigate To**: `Savings Account Details`
- **Observe**:
  - current balance reflects interest posted
  - interest transaction in transaction history

**Expected Change**: The savings account balance increases by the amount of interest posted, and a new transaction entry for the interest posting is visible in the transaction history.

---

### [TC-006] Attempt to start all jobs when none are scheduled
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Start All

**Original Expected Result:** No jobs started; error message displayed indicating there are no scheduled jobs to start

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Savings Account Details`
- **Observe**:
  - account status is 'Active'

**Post-Check**
- **Navigate To**: `Savings Account List`
- **Observe**:
  - account status is 'Closed'
  - account is no longer listed in active accounts

**Expected Change**: The savings account is successfully closed and no longer appears in the active accounts list.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Dashboard -> My Share Accounts`
- **Observe**:
  - list does not contain the new share account application

**Post-Check**
- **Navigate To**: `Client Dashboard -> My Share Accounts`
- **Observe**:
  - list contains the new share account application
  - status is 'Pending Approval'

**Expected Change**: A new share account application is created with the correct status and details.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Actor A (Role: `approver`)**
- **Action**: Approve Share Account with valid data

**Actor B (Role: `client`)**
- **Session**: `new_session`
- **Navigate To**: `Client Profile -> Share Accounts`
- **Action**: 
- **Observe**:
  - share account status
  - approved shares count
  - approval date

**Expected Change**: The share account status changes to 'Active' with the correct number of approved shares and the approval date.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Actor A (Role: `approver`)**
- **Action**: Reject the share account that is in Pending status.

**Actor B (Role: `user`)**
- **Session**: `new_session`
- **Navigate To**: `My Accounts -> Share Accounts`
- **Action**: 
- **Observe**:
  - account status is 'Rejected'
  - account is no longer in the Pending list

**Expected Change**: The share account status changes to 'Rejected' and it is removed from the list of Pending accounts.

---

### [TC-004] Rapid logout attempts
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Click on 'Log Out'
3. 3. Immediately click on the User Profile Icon again
4. 4. Click on 'Log Out' again

**Original Expected Result:** Second logout attempt is blocked; user remains on the login page without a second session being created.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Account Detail`
- **Observe**:
  - status badge is 'Approved'

**Post-Check**
- **Navigate To**: `Share Account Detail`
- **Observe**:
  - status badge is 'Active'

**Expected Change**: The share account status changes from 'Approved' to 'Active' after activation.

---

### [TC-005] Navigate to authenticated page after logout
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Accounts`
- **Observe**:
  - account status is 'Approved'

**Post-Check**
- **Navigate To**: `Share Accounts`
- **Observe**:
  - account status is 'Pending'

**Expected Change**: The account status changes from 'Approved' to 'Pending' after the undo approval action.

---

### [TC-006] Attempt to start all jobs when none are scheduled
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Start All

**Original Expected Result:** No jobs started; error message displayed indicating there are no scheduled jobs to start

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Account`
- **Observe**:
  - current shares count is <initial count>

**Post-Check**
- **Navigate To**: `Share Account`
- **Observe**:
  - current shares count is <initial count + valid number of additional shares>

**Expected Change**: The total number of shares in the account increases by the valid number of additional shares applied.

---

### [TC-007] Attempt to stop all jobs when none are running
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Stop All

**Original Expected Result:** No jobs stopped; error message displayed indicating there are no jobs currently running

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Dashboard -> Share Account`
- **Observe**:
  - current share balance
  - current unit price

**Post-Check**
- **Navigate To**: `Client Dashboard -> Savings Account`
- **Observe**:
  - savings account balance reflects the redemption amount

**Expected Change**: The savings account balance increases by the calculated redemption amount based on the shares redeemed and the current unit price.

---

### [TC-008] Add maximum allowed entries to Column Definitions
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a valid Data Table Name in the Data_Table_Name field
2. 2. Select an Application Table Name from the dropdown
3. 3. Add exactly maximum allowed entries to the Column Definitions repeating group

**Original Expected Result:** Form submits successfully; custom data table is created with the maximum number of column definitions

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Dashboard -> My Share Accounts`
- **Observe**:
  - share account status is 'Active'

**Post-Check**
- **Navigate To**: `Client Dashboard -> My Share Accounts`
- **Observe**:
  - share account status is 'Closed'

**Expected Change**: The share account status changes from 'Active' to 'Closed' after the closure action.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Accounts`
- **Observe**:
  - FD account list does not contain the new Fixed Deposit account

**Post-Check**
- **Navigate To**: `User Dashboard -> My Accounts`
- **Observe**:
  - FD account list contains the new Fixed Deposit account
  - status is 'Active'

**Expected Change**: A new Fixed Deposit account is created with the correct deposit amount and period.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `unverifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `RD Account Creation Form`
- **Observe**:
  - Deposit Frequency field is empty

**Post-Check**
- **Navigate To**: `RD Account Summary or Dashboard`
- **Observe**:
  - No new RD account entry is visible
  - Error message displayed for missing deposit frequency

**Expected Change**: The system should display an error message indicating that the Deposit Frequency is a required field, and no RD account should be created.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> Recurring Deposit Accounts`
- **Observe**:
  - account status is 'Draft'

**Post-Check**
- **Navigate To**: `User Dashboard -> Recurring Deposit Accounts`
- **Observe**:
  - account status is 'Active'

**Expected Change**: The Recurring Deposit account status changes from 'Draft' to 'Active' after activation.

---

### [TC-004] Rapid logout attempts
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Click on 'Log Out'
3. 3. Immediately click on the User Profile Icon again
4. 4. Click on 'Log Out' again

**Original Expected Result:** Second logout attempt is blocked; user remains on the login page without a second session being created.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Accounts`
- **Observe**:
  - RD account status is 'Active'

**Post-Check**
- **Navigate To**: `User Dashboard -> My Accounts`
- **Observe**:
  - RD account status is 'Closed'
  - RD account closure date is displayed

**Expected Change**: The Recurring Deposit account is successfully closed on maturity and its status is updated to 'Closed'.

---

### [TC-005] Navigate to authenticated page after logout
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `FD Account Detail page`
- **Observe**:
  - status badge shows 'Pending'

**Post-Check**
- **Navigate To**: `FD Account Detail page`
- **Observe**:
  - status badge shows 'Approved'

**Expected Change**: The FD Account status changes from 'Pending' to 'Approved' after the approval action.

---

### [TC-006] Attempt to start all jobs when none are scheduled
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Start All

**Original Expected Result:** No jobs started; error message displayed indicating there are no scheduled jobs to start

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `FD Account Detail page`
- **Observe**:
  - status badge is 'Pending'

**Post-Check**
- **Navigate To**: `FD Account Detail page`
- **Observe**:
  - status badge is 'Active'

**Expected Change**: The FD Account status changes from 'Pending' to 'Active' after activation.

---

### [TC-007] Attempt to stop all jobs when none are running
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Stop All

**Original Expected Result:** No jobs stopped; error message displayed indicating there are no jobs currently running

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `FD Account Detail page`
- **Observe**:
  - account status is 'Active'
  - closure options are available

**Post-Check**
- **Navigate To**: `FD Account Detail page`
- **Observe**:
  - account status is 'Closed'
  - closure date is recorded
  - closure reason is displayed

**Expected Change**: The FD Account status changes from 'Active' to 'Closed' after the premature closure action.

---

### [TC-008] Add maximum allowed entries to Column Definitions
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a valid Data Table Name in the Data_Table_Name field
2. 2. Select an Application Table Name from the dropdown
3. 3. Add exactly maximum allowed entries to the Column Definitions repeating group

**Original Expected Result:** Form submits successfully; custom data table is created with the maximum number of column definitions

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `FD Account Detail page`
- **Observe**:
  - status badge is 'Active'
  - closure options are available

**Post-Check**
- **Navigate To**: `FD Account Detail page`
- **Observe**:
  - status badge is 'Closed'
  - closure date is displayed

**Expected Change**: The FD Account status changes from 'Active' to 'Closed' upon successful closure on maturity.

---

### [TC-009] Attempt to add one more entry to Column Definitions
**Category**: `edge` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a valid Data Table Name in the Data_Table_Name field
2. 2. Select an Application Table Name from the dropdown
3. 3. Add maximum allowed entries to the Column Definitions repeating group
4. 4. Attempt to add one more entry to the Column Definitions

**Original Expected Result:** Attempt to add entry is blocked; visible error shown indicating maximum entries reached

---

#### Verification Plan

**Actor A (Role: `approver`)**
- **Action**: Approve the RD Account from the detail page.

**Actor B (Role: `client`)**
- **Session**: `new_session`
- **Navigate To**: `Client Dashboard -> My Accounts`
- **Action**: 
- **Observe**:
  - RD Account status is 'Active'
  - RD Account approval date is displayed

**Expected Change**: The RD Account status changes to 'Active' indicating successful approval.

---

### [TC-010] Enter maximum length for Name in Column Definitions
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a valid Data Table Name in the Data_Table_Name field
2. 2. Select an Application Table Name from the dropdown
3. 3. Add an entry to the Column Definitions repeating group
4. 4. Enter exactly maximum length for the Name field

**Original Expected Result:** Form submits successfully; custom data table is created with the maximum length Name

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `RD Account Detail page`
- **Observe**:
  - status badge is 'Pending'

**Post-Check**
- **Navigate To**: `RD Account Detail page`
- **Observe**:
  - status badge is 'Active'

**Expected Change**: The RD Account status changes from 'Pending' to 'Active' after activation.

---

### [TC-011] Enter one character less than maximum length for Name in Column Definitions
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a valid Data Table Name in the Data_Table_Name field
2. 2. Select an Application Table Name from the dropdown
3. 3. Add an entry to the Column Definitions repeating group
4. 4. Enter one character less than the maximum length for the Name field

**Original Expected Result:** Form submits successfully; custom data table is created with the Name field accepted

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `RD Account Detail page`
- **Observe**:
  - current balance before deposit

**Post-Check**
- **Navigate To**: `RD Account Detail page`
- **Observe**:
  - updated balance after deposit

**Expected Change**: The balance of the RD Account reflects the deposit amount added to the previous balance.

---

### [TC-012] Enter long text in Data Table Name
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a very long string (200+ characters) in the Data_Table_Name field

**Original Expected Result:** Form submission is either accepted or truncated with a visible indicator

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `RD Account Detail page`
- **Observe**:
  - account status is 'Active'
  - account balance is displayed

**Post-Check**
- **Navigate To**: `RD Account Detail page`
- **Observe**:
  - account status is 'Closed'
  - account balance reflects any penalties or adjustments

**Expected Change**: The RD Account status changes from 'Active' to 'Closed' after the premature closure action.

---

### [TC-013] Enter special characters in Data Table Name
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter special characters in the Data_Table_Name field

**Original Expected Result:** Form submission is either accepted or a specific error shown

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `RD Account Detail page`
- **Observe**:
  - account status is 'Active'
  - maturity date is displayed

**Post-Check**
- **Navigate To**: `RD Account Detail page`
- **Observe**:
  - account status is 'Closed'
  - closure date is displayed
  - final balance reflects closure adjustments

**Expected Change**: The RD Account status changes from 'Active' to 'Closed' upon successful closure on maturity.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounting -> Chart of Accounts`
- **Observe**:
  - list of GL accounts does not contain the new account with <unique GL code>

**Post-Check**
- **Navigate To**: `Accounting -> Chart of Accounts`
- **Observe**:
  - list of GL accounts contains the new account with <unique GL code>
  - account name is <account name>
  - account type is <account type>

**Expected Change**: A new GL Account is created successfully with the specified GL code and account name.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounting -> Chart of Accounts`
- **Observe**:
  - <field> displays old value

**Post-Check**
- **Navigate To**: `Accounting -> Chart of Accounts`
- **Observe**:
  - <field> displays new value

**Expected Change**: The GL Account details are updated with the new value.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Chart of Accounts`
- **Observe**:
  - <account name> is displayed in the list of GL Accounts

**Post-Check**
- **Navigate To**: `Chart of Accounts`
- **Observe**:
  - <account name> is not displayed in the list of GL Accounts

**Expected Change**: The GL Account is removed from the Chart of Accounts after deletion.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Journal Entries page`
- **Observe**:
  - list of journal entries does not contain the new entry

**Post-Check**
- **Navigate To**: `Journal Entries page`
- **Observe**:
  - list of journal entries contains the new entry
  - entry shows correct office, currency, transaction date, and amount

**Expected Change**: A new journal entry is created with the correct details, and the total debits equal total credits.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounting Closures`
- **Observe**:
  - no closures listed for the selected office
  - no journal entries posted for the closing date

**Post-Check**
- **Navigate To**: `Accounting Closures`
- **Observe**:
  - new closure listed for the selected office
  - no journal entries posted for dates on or before the closing date

**Expected Change**: A new closure entry is created for the selected office with the correct closing date, preventing any journal entries from being posted for dates on or before the closing date.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounting Rules page`
- **Observe**:
  - list of accounting rules does not contain the new rule

**Post-Check**
- **Navigate To**: `Accounting Rules page`
- **Observe**:
  - list of accounting rules contains the new rule
  - new rule name is <valid rule name>

**Expected Change**: The new accounting rule is successfully created and displayed in the Accounting Rules Table.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Financial Activity Mappings`
- **Observe**:
  - list does not contain the new mapping

**Post-Check**
- **Navigate To**: `Financial Activity Mappings`
- **Observe**:
  - list contains the new mapping
  - mapping details match the created values

**Expected Change**: The new financial activity mapping is successfully created and displayed in the mappings table.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounting -> Accounting Rules`
- **Observe**:
  - existing rule name in the table

**Post-Check**
- **Navigate To**: `Accounting -> Accounting Rules`
- **Observe**:
  - updated rule name in the table

**Expected Change**: The accounting rule details are updated, and the Accounting Rules Table displays the new rule name.

---

### [TC-004] Rapid logout attempts
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Click on 'Log Out'
3. 3. Immediately click on the User Profile Icon again
4. 4. Click on 'Log Out' again

**Original Expected Result:** Second logout attempt is blocked; user remains on the login page without a second session being created.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounting -> Accounting Rules`
- **Observe**:
  - existing accounting rule in the table

**Post-Check**
- **Navigate To**: `Accounting -> Accounting Rules`
- **Observe**:
  - accounting rule no longer present in the table

**Expected Change**: The accounting rule has been successfully deleted and is no longer visible in the Accounting Rules Table.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Provisioning Criteria List`
- **Observe**:
  - criteria list does not contain the new criteria name

**Post-Check**
- **Navigate To**: `Provisioning Criteria List`
- **Observe**:
  - criteria list contains the new criteria name
  - criteria details match the submitted values

**Expected Change**: A new provisioning criteria entry is created with the specified name, age range, and provisioning percentage.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Provisioning Entries page`
- **Observe**:
  - no recent provisioning entries listed

**Post-Check**
- **Navigate To**: `Provisioning Entries page`
- **Observe**:
  - new provisioning entries listed
  - entries reflect current loan portfolio status

**Expected Change**: New provisioning entries are generated and displayed based on the current loan portfolio status.

---

### [TC-005] Navigate to authenticated page after logout
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Provisioning Entries`
- **Observe**:
  - list of provisioning entries
  - status of the entry to be recreated

**Post-Check**
- **Navigate To**: `Provisioning Entries`
- **Observe**:
  - newly recreated provisioning entry
  - status of the entry reflects the correct state

**Expected Change**: A new provisioning entry is created with the same parameters as the original entry.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Offices page`
- **Observe**:
  - offices list does not contain the new office name

**Post-Check**
- **Navigate To**: `Offices page`
- **Observe**:
  - offices list contains the new office name
  - status is 'Active'

**Expected Change**: A new office entry is created with the correct name and status.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Employees page`
- **Observe**:
  - employee details are displayed
  - edit action is available

**Post-Check**
- **Navigate To**: `Employees page`
- **Observe**:
  - employee edit form is displayed
  - employee details can be modified

**Expected Change**: The employee edit form is displayed, allowing for modifications to employee details.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Employees page`
- **Observe**:
  - employee list does not contain the new employee

**Post-Check**
- **Navigate To**: `Employees page`
- **Observe**:
  - employee list contains the new employee with the correct first and last name
  - status is 'Active'

**Expected Change**: A new employee entry is created with the specified first name and last name, and is listed as active.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Tellers page`
- **Observe**:
  - teller list does not contain the new teller

**Post-Check**
- **Navigate To**: `Tellers page`
- **Observe**:
  - teller list contains the new teller
  - teller name is '<valid teller name>'
  - office is '<valid office>'

**Expected Change**: A new teller entry is created with the specified name and office.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Teller Management`
- **Observe**:
  - cashier list does not contain the newly allocated cashier

**Post-Check**
- **Navigate To**: `Teller Management`
- **Observe**:
  - cashier list contains the newly allocated cashier
  - cashier status is 'Active'

**Expected Change**: A new cashier entry is created for the selected staff with the correct start date.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Tellers list`
- **Observe**:
  - teller details show old office information

**Post-Check**
- **Navigate To**: `Tellers list`
- **Observe**:
  - teller details show updated office information
  - success message displayed

**Expected Change**: The teller's office information is updated to the new valid office.

---

### [TC-004] Rapid logout attempts
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Click on 'Log Out'
3. 3. Immediately click on the User Profile Icon again
4. 4. Click on 'Log Out' again

**Original Expected Result:** Second logout attempt is blocked; user remains on the login page without a second session being created.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Cashier Detail page`
- **Observe**:
  - cash balance is unchanged
  - no recent allocation transactions

**Post-Check**
- **Navigate To**: `Cashier Detail page`
- **Observe**:
  - cash balance reflects allocated amount
  - recent allocation transaction is listed

**Expected Change**: The cash balance is increased by the allocated amount, and a new transaction entry for the cash allocation is visible.

---

### [TC-005] Navigate to authenticated page after logout
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Cashier Detail page`
- **Observe**:
  - current cash balance
  - settlement history is empty

**Post-Check**
- **Navigate To**: `Cashier Detail page`
- **Observe**:
  - current cash balance reflects the settled amount
  - settlement history includes the new transaction

**Expected Change**: The cash balance is updated to include the settled amount, and the settlement history shows the new transaction with the correct details.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Users Management`
- **Observe**:
  - <unique username> not present in users list

**Post-Check**
- **Navigate To**: `Users Management`
- **Observe**:
  - <unique username> present in users list
  - success message displayed

**Expected Change**: A new user entry is created with the specified username and details.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Roles Management`
- **Observe**:
  - list of roles does not contain the new role

**Post-Check**
- **Navigate To**: `Roles Management`
- **Observe**:
  - list of roles contains the new role
  - role name is '<role name>'
  - description is '<description>'

**Expected Change**: A new role is created with the specified name and description.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Account Overview`
- **Observe**:
  - <valid From Account> balance before transfer
  - <valid To Account> balance before transfer

**Post-Check**
- **Navigate To**: `Account Overview`
- **Observe**:
  - <valid From Account> balance after transfer
  - <valid To Account> balance after transfer

**Expected Change**: <valid From Account> balance should be decreased by <valid Transfer Amount> and <valid To Account> balance should be increased by <valid Transfer Amount>.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Tax Management -> Tax Components`
- **Observe**:
  - list does not contain the new tax component

**Post-Check**
- **Navigate To**: `Tax Management -> Tax Components`
- **Observe**:
  - list contains the new tax component
  - tax component name is '<valid name>'
  - tax percentage is '<valid percentage>'

**Expected Change**: A new tax component is created with the specified name and percentage, and it appears in the tax components list.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Tax Management -> Tax Groups`
- **Observe**:
  - tax group list does not contain the new tax group with the entered name

**Post-Check**
- **Navigate To**: `Tax Management -> Tax Groups`
- **Observe**:
  - tax group list contains the new tax group with the entered name
  - tax group details show the entered values

**Expected Change**: A new tax group is created with the specified name and associated components.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Holidays Management`
- **Observe**:
  - holiday list does not contain the new holiday entry

**Post-Check**
- **Navigate To**: `Holidays Management`
- **Observe**:
  - holiday list contains the new holiday entry
  - holiday name is '<valid holiday name>'
  - holiday dates are '<valid start date>' to '<valid end date>'

**Expected Change**: A new holiday entry is created that affects loan repayment schedules.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Organization Settings -> Working Days`
- **Observe**:
  - Monday checkbox is unchecked
  - Tuesday checkbox is unchecked

**Post-Check**
- **Navigate To**: `Organization Settings -> Working Days`
- **Observe**:
  - Monday checkbox is checked
  - Tuesday checkbox is checked

**Expected Change**: The working days configuration now includes Monday and Tuesday as selected days.

---

### [TC-005] Navigate to authenticated page after logout
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Funds Management -> Fund List`
- **Observe**:
  - fund list does not contain the new fund entry

**Post-Check**
- **Navigate To**: `Funds Management -> Fund List`
- **Observe**:
  - fund list contains the new fund entry
  - fund name matches <valid fund name>
  - external ID matches <valid external ID>

**Expected Change**: A new fund entry is created with the specified fund name and external ID.

---

### [TC-006] Attempt to start all jobs when none are scheduled
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Start All

**Original Expected Result:** No jobs started; error message displayed indicating there are no scheduled jobs to start

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Payment Types page`
- **Observe**:
  - list of existing payment types does not include the new payment type

**Post-Check**
- **Navigate To**: `Payment Types page`
- **Observe**:
  - list of existing payment types includes the new payment type
  - new payment type name is displayed
  - new payment type description is displayed

**Expected Change**: A new payment type is added to the list with the correct name and description.

---

### [TC-008] Add maximum allowed entries to Column Definitions
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a valid Data Table Name in the Data_Table_Name field
2. 2. Select an Application Table Name from the dropdown
3. 3. Add exactly maximum allowed entries to the Column Definitions repeating group

**Original Expected Result:** Form submits successfully; custom data table is created with the maximum number of column definitions

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Bulk Import page`
- **Observe**:
  - data import history is empty
  - no recent uploads listed

**Post-Check**
- **Navigate To**: `Bulk Import page`
- **Observe**:
  - data import history shows the new upload entry
  - status indicates 'Pending' or 'Processing'

**Expected Change**: A new entry is created in the data import history reflecting the uploaded file, indicating that the upload process has started.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `System Administration -> Scheduled Jobs`
- **Observe**:
  - list of scheduled jobs
  - status is 'Inactive'

**Post-Check**
- **Navigate To**: `System Administration -> Scheduled Jobs`
- **Observe**:
  - list of scheduled jobs
  - status is 'Active'

**Expected Change**: All scheduled jobs are now active and running.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Scheduled Jobs Management`
- **Observe**:
  - list of active scheduled jobs

**Post-Check**
- **Navigate To**: `Scheduled Jobs Management`
- **Observe**:
  - no active scheduled jobs listed
  - status indicator shows 'Stopped' for all jobs

**Expected Change**: All scheduled jobs are no longer active and the status reflects that they have been stopped.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Manage Data Tables`
- **Observe**:
  - Data Table Name field is empty
  - No custom data tables listed

**Post-Check**
- **Navigate To**: `Manage Data Tables`
- **Observe**:
  - Custom data table with <Data Table Name> appears in the list
  - Column definitions include <Column Name>

**Expected Change**: A new custom data table is created and displayed in the list with the specified column definitions.

---
