# Test Cases — Mifos

Generated: 2026-06-04T14:54:55.751407Z  
Model: gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 31 | 155 | 46 | 53 | 56 | 107 | 47 | 1 |

## Login

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Login with valid credentials | User is on the Login page, User has valid credentials | 1. Select 'default' from the Tenant dropdown<br>2. Enter a valid Username in the Username field<br>3. Enter a valid Password in the Password field<br>4. Check the 'Remember me' checkbox<br>5. Click the Login button | User is redirected to the Dashboard | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Login with invalid credentials | User is on the Login page, User has invalid credentials | 1. Select 'default' from the Tenant dropdown<br>2. Enter an invalid Username in the Username field<br>3. Enter an invalid Password in the Password field<br>4. Click the Login button | An error message is displayed indicating invalid credentials; user remains on the Login page | high |
| TC-003 |  | Attempt to login with empty required fields | User is on the Login page | 1. Select 'default' from the Tenant dropdown<br>2. Leave the Username field empty<br>3. Leave the Password field empty<br>4. Click the Login button | Inline validation messages are displayed for empty required fields; user remains on the Login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Login with maximum length username and password | User is on the Login page | 1. Select 'default' from the Tenant dropdown<br>2. Enter a Username with maximum allowed length in the Username field<br>3. Enter a Password with maximum allowed length in the Password field<br>4. Click the Login button | User is redirected to the Dashboard if credentials are valid; otherwise, an error message is displayed | medium |
| TC-005 |  | Login with special characters in username and password | User is on the Login page, User has credentials with special characters | 1. Select 'default' from the Tenant dropdown<br>2. Enter a Username with special characters in the Username field<br>3. Enter a Password with special characters in the Password field<br>4. Click the Login button | User is redirected to the Dashboard if credentials are valid; otherwise, an error message is displayed | medium |

---

## Home Page

Total: **5** (positive: 2, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Display welcome message after successful login | User has successfully logged in | 1. Observe the Home page after login | The welcome card displays the message 'Welcome, mifos!' | high |
| TC-007 |  | Access dashboard from Home page | User has successfully logged in | 1. Click the 'Dashboard' button on the Home page | User is redirected to the Dashboard view | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 |  | Attempt to search activity without entering a search term | User has successfully logged in | 1. Leave the 'Search Activity' input field empty<br>2. Click the search button | An error message is displayed indicating that a search term is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 |  | Search activity with a very long string | User has successfully logged in | 1. Enter a string of 256 characters in the 'Search Activity' input field<br>2. Click the search button | The system processes the input and displays relevant results or an appropriate error message if the input exceeds limits | medium |
| TC-010 |  | Check system version information display | User has successfully logged in | 1. Scroll to the bottom of the Home page | System version information for Mifos and Fineract is displayed correctly | medium |

---

## Dashboard

Total: **3** (positive: 1, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 |  | View the Dashboard with valid office selection | User logged in, User has access to at least one office | 1. Navigate to the Home page<br>2. Click the Dashboard button<br>3. Select a valid office from the dropdown | The Dashboard displays the Client Trends chart and summary cards for the selected office | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 |  | Attempt to view the Dashboard without selecting an office | User logged in | 1. Navigate to the Home page<br>2. Click the Dashboard button | An error message is displayed stating that an office must be selected; the Dashboard does not load | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 |  | View the Dashboard for an office with no client data | User logged in, User has access to an office with no client data | 1. Navigate to the Home page<br>2. Click the Dashboard button<br>3. Select the office with no client data | The Client Trends chart displays with no data, and summary cards show 'No Data' for both Amount Pending / Disbursed and Amount Collected | medium |

---

## Global Search

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-014 |  | Search for a client by a valid name | User logged in, At least one client exists in the system | 1. Click on the search icon in the top toolbar<br>2. Enter a valid client name in the search input field<br>3. Observe the dropdown results | Matching client results appear in the dropdown, showing the client name, identifier, and status | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 |  | Search for a non-existent client | User logged in | 1. Click on the search icon in the top toolbar<br>2. Enter a name that does not match any client in the search input field<br>3. Observe the dropdown results | A 'No results found' message is displayed in the dropdown | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-016 |  | Search using a partial name that matches multiple entities | User logged in, Multiple clients, groups, loans, and savings accounts exist with similar names | 1. Click on the search icon in the top toolbar<br>2. Enter a partial name that is common among multiple entities in the search input field<br>3. Observe the dropdown results | Results are grouped by entity type, showing all matching clients, groups, loans, and savings accounts | medium |
| TC-017 |  | Search using an empty input field | User logged in | 1. Click on the search icon in the top toolbar<br>2. Leave the search input field empty<br>3. Observe the dropdown results | No results are displayed, and the dropdown remains empty | low |

---

## Client Management

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-018 |  | Create a new client with valid details | User logged in as Admin, User is on the Clients page | 1. Click the Create Client button<br>2. Fill in all required fields in Step 1 (General Details)<br>3. Click Next to proceed to Step 2 (Address Details)<br>4. Fill in all required fields in Step 2<br>5. Click Next to proceed to Step 3 (Family Members)<br>6. Fill in family member details if applicable<br>7. Click Next to proceed to Step 4 (Identifiers)<br>8. Fill in Document Type and Document Key<br>9. Click Submit | A new client is created with Pending status and is displayed in the Clients page data table | high |
| TC-021 |  | Import clients using a valid Excel file | User logged in as Admin, User is on the Clients page, A valid client Excel file is prepared | 1. Click the Import Client button<br>2. Click the Download template link to get the format<br>3. Fill in the template with valid client data<br>4. Upload the completed file<br>5. Click Submit | Clients are imported successfully, and the import history shows the new records with success counts | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-019 |  | Attempt to create a client with a duplicate External ID | User logged in as Admin, User is on the Clients page, A client with a specific External ID already exists | 1. Click the Create Client button<br>2. Fill in all required fields in Step 1 (General Details) including the existing External ID<br>3. Click Next to proceed to Step 2 (Address Details)<br>4. Fill in all required fields in Step 2<br>5. Click Next to proceed to Step 3 (Family Members)<br>6. Fill in family member details if applicable<br>7. Click Next to proceed to Step 4 (Identifiers)<br>8. Fill in Document Type and Document Key<br>9. Click Submit | An error message is displayed stating that the External ID must be unique; the client is not created | high |
| TC-022 |  | Attempt to import clients using an invalid Excel file | User logged in as Admin, User is on the Clients page, An invalid client Excel file is prepared | 1. Click the Import Client button<br>2. Upload the invalid file<br>3. Click Submit | An error message is displayed indicating the file format is invalid; no clients are imported | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-020 |  | Search for a client using a partial name | User logged in as Admin, User is on the Clients page, At least one client exists with a name containing the search term | 1. Enter a partial name in the search field<br>2. Click the Search button | The Clients page displays a filtered list of clients whose names contain the search term | medium |
| TC-023 |  | Create a client with maximum length fields | User logged in as Admin, User is on the Clients page | 1. Click the Create Client button<br>2. Fill in all required fields in Step 1 (General Details) with maximum length values<br>3. Click Next to proceed to Step 2 (Address Details)<br>4. Fill in all required fields in Step 2 with maximum length values<br>5. Click Next to proceed to Step 3 (Family Members)<br>6. Fill in family member details with maximum length values if applicable<br>7. Click Next to proceed to Step 4 (Identifiers)<br>8. Fill in Document Type and Document Key with maximum length values<br>9. Click Submit | A new client is created with Pending status and is displayed in the Clients page data table | medium |

---

## Group Management

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-024 |  | Create a new group with valid details | User logged in as Admin, User is on the Groups page | 1. Click the Create Group button<br>2. Enter a valid Group Name in the Name field<br>3. Select a valid Office from the dropdown<br>4. Select a valid Staff member from the Staff dropdown<br>5. Enter a valid date in the Submitted On field<br>6. Check the Active checkbox<br>7. Click Submit | A new group is created and displayed in the Groups table with the correct details | high |
| TC-027 |  | Import groups using a valid template file | User logged in as Admin, User is on the Bulk Import Groups page, A valid groups template file is available | 1. Click the Download button to get the Groups Template<br>2. Fill in the template with valid group data<br>3. Upload the filled template using the file picker<br>4. Click the Upload button | Groups are imported successfully, and an import history entry is created | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-025 |  | Attempt to create a new group without a required field | User logged in as Admin, User is on the Create Group form | 1. Leave the Name field empty<br>2. Select a valid Office from the dropdown<br>3. Select a valid Staff member from the Staff dropdown<br>4. Enter a valid date in the Submitted On field<br>5. Click Submit | An error message is displayed indicating that the Name field is required; the group is not created | high |
| TC-028 |  | Attempt to import groups using an invalid file format | User logged in as Admin, User is on the Bulk Import Groups page | 1. Upload a file that is not in the required format (e.g., .txt instead of .csv)<br>2. Click the Upload button | An error message is displayed indicating that the file format is invalid; no groups are imported | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-026 |  | Create a new group with the maximum allowed characters in the Group Name | User logged in as Admin, User is on the Create Group form | 1. Enter a Group Name with the maximum allowed characters (e.g., 255 characters)<br>2. Select a valid Office from the dropdown<br>3. Select a valid Staff member from the Staff dropdown<br>4. Enter a valid date in the Submitted On field<br>5. Click Submit | A new group is created successfully with the maximum length Group Name displayed correctly in the Groups table | high |
| TC-029 |  | Import groups with the maximum number of entries in the template | User logged in as Admin, User is on the Bulk Import Groups page, A valid groups template file with maximum entries is prepared | 1. Upload the filled template with the maximum allowed number of groups<br>2. Click the Upload button | All groups are imported successfully, and the import history reflects the maximum entries | high |

---

## Center Management

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-030 |  | Create a new center with valid details | User logged in as Admin, User is on the Centers page | 1. Click the Create Center button<br>2. Enter a valid Name in the Name field<br>3. Select a valid Office from the Office dropdown<br>4. (Optional) Select Staff from the Staff dropdown<br>5. Check the Active checkbox<br>6. Enter a valid External Id in the External Id field<br>7. Enter a valid date in the Submitted On field<br>8. Select and add groups from the dropdown<br>9. Click Submit | A new center is created and displayed in the Centers page with the correct details | high |
| TC-033 |  | Activate a center that is currently inactive | User logged in as Admin, An inactive center exists | 1. Navigate to the Center Detail page of the inactive center<br>2. Click the Activate button<br>3. Confirm the activation | The center status updates to 'Active' and is reflected on the Centers page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-031 |  | Attempt to create a center without a required field | User logged in as Admin, User is on the Create Center form | 1. Click the Create Center button<br>2. Leave the Name field empty<br>3. Select a valid Office from the Office dropdown<br>4. Click Submit | An error message is displayed indicating that the Name field is required; the center is not created | high |
| TC-034 |  | Attempt to activate an already active center | User logged in as Admin, An active center exists | 1. Navigate to the Center Detail page of the active center<br>2. Click the Activate button<br>3. Confirm the activation | An error message is displayed stating the center is already active; no changes are made | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-032 |  | Create a center with maximum length name | User logged in as Admin, User is on the Create Center form | 1. Click the Create Center button<br>2. Enter a Name with the maximum allowed length in the Name field<br>3. Select a valid Office from the Office dropdown<br>4. (Optional) Select Staff from the Staff dropdown<br>5. Check the Active checkbox<br>6. Enter a valid External Id in the External Id field<br>7. Enter a valid date in the Submitted On field<br>8. Select and add groups from the dropdown<br>9. Click Submit | A new center is created successfully with the maximum length name and displayed in the Centers page | medium |
| TC-035 |  | Create a center with a very long external ID | User logged in as Admin, User is on the Create Center form | 1. Click the Create Center button<br>2. Enter a valid Name in the Name field<br>3. Select a valid Office from the Office dropdown<br>4. (Optional) Select Staff from the Staff dropdown<br>5. Check the Active checkbox<br>6. Enter a very long External Id in the External Id field<br>7. Enter a valid date in the Submitted On field<br>8. Select and add groups from the dropdown<br>9. Click Submit | An error message is displayed indicating the External Id exceeds the maximum length; the center is not created | medium |

---

## Loan Products

Total: **6** (positive: 1, negative: 3, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-036 |  | Create a new loan product with all required fields filled | User logged in as Admin | 1. Navigate to the Loan Products page<br>2. Click the '+ Create Loan Product' button<br>3. Fill in the Product Name and Short Name fields<br>4. Complete all other required fields in the stepper wizard<br>5. Click Submit | New loan product is created and displayed in the loan products table | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-037 |  | Attempt to create a loan product without filling required fields | User logged in as Admin | 1. Navigate to the Loan Products page<br>2. Click the '+ Create Loan Product' button<br>3. Leave the Product Name and Short Name fields empty<br>4. Click Submit | Inline validation errors are displayed for the empty required fields; loan product is not created | high |
| TC-039 |  | Attempt to create a loan product with invalid currency selection | User logged in as Admin | 1. Navigate to the Loan Products page<br>2. Click the '+ Create Loan Product' button<br>3. Fill in the Product Name and Short Name fields<br>4. Select an invalid currency from the currency dropdown<br>5. Click Submit | An error message is displayed indicating the currency selection is invalid; loan product is not created | high |
| TC-041 |  | Attempt to create a loan product with negative Nominal Interest Rate | User logged in as Admin | 1. Navigate to the Loan Products page<br>2. Click the '+ Create Loan Product' button<br>3. Fill in the Product Name and Short Name fields<br>4. Enter a negative value for Nominal Interest Rate<br>5. Click Submit | An error message is displayed indicating that the Nominal Interest Rate cannot be negative; loan product is not created | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-038 |  | Create a loan product with maximum length for Product Name and Short Name | User logged in as Admin | 1. Navigate to the Loan Products page<br>2. Click the '+ Create Loan Product' button<br>3. Enter a Product Name and Short Name with maximum allowed characters<br>4. Fill in all other required fields<br>5. Click Submit | New loan product is created successfully and displayed in the loan products table | medium |
| TC-040 |  | Create a loan product with minimum and maximum values for Principal Amount | User logged in as Admin | 1. Navigate to the Loan Products page<br>2. Click the '+ Create Loan Product' button<br>3. Fill in the Product Name and Short Name fields<br>4. Enter the minimum Principal Amount<br>5. Click Next and enter the maximum Principal Amount<br>6. Click Submit | New loan product is created successfully with minimum and maximum Principal Amount values | medium |

---

## Savings Products

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-042 |  | Create a Savings Product with valid details | User logged in as Admin | 1. Navigate to the Savings Products page<br>2. Click the '+ Create Savings Product' button<br>3. Fill in the Product Name, Short Name, and Description in Step 1<br>4. Select Currency and fill in Decimal Places and Currency In Multiples Of in Step 2<br>5. Enter Nominal Annual Interest Rate and select Interest Compounding Period in Step 3<br>6. Fill in Minimum Opening Balance and other required fields in Step 4<br>7. Add predefined charges in Step 5<br>8. Select None or Cash-based in Step 6 and complete the GL account mappings if Cash-based is selected<br>9. Click Submit | The new Savings Product is created and displayed in the Savings Products list | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-043 |  | Attempt to create a Savings Product without required fields | User logged in as Admin | 1. Navigate to the Savings Products page<br>2. Click the '+ Create Savings Product' button<br>3. Leave Product Name and Short Name fields empty in Step 1<br>4. Click Submit | An error message is displayed indicating that Product Name and Short Name are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-044 |  | Create a Savings Product with maximum character limits | User logged in as Admin | 1. Navigate to the Savings Products page<br>2. Click the '+ Create Savings Product' button<br>3. Fill in the Product Name and Short Name with maximum allowed characters in Step 1<br>4. Fill in all other fields with valid data<br>5. Click Submit | The new Savings Product is created successfully with maximum character limits | medium |
| TC-045 |  | Create a Fixed Deposit Product with minimum and maximum deposit terms | User logged in as Admin | 1. Navigate to the Savings Products page<br>2. Click the '+ Create Savings Product' button<br>3. Select Fixed Deposit Product type<br>4. Fill in the Minimum and Maximum Deposit Term with valid values<br>5. Click Submit | The Fixed Deposit Product is created with specified deposit terms | medium |

---

## Share Products

Total: **3** (positive: 1, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-046 |  | Create a new Share Product with valid details | User logged in as Admin | 1. Navigate to the Share Products page<br>2. Click the '+ Create Share Product' button<br>3. Enter 'Valid Product Name' in the Product Name field<br>4. Enter 'Valid Short Name' in the Short Name field<br>5. Enter 'This is a valid description.' in the Description field<br>6. Click Next to proceed through the wizard with valid inputs for each step<br>7. Click Submit on the final step | New Share Product is created and displayed in the Share Products data table | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-047 |  | Attempt to create a Share Product with missing required fields | User logged in as Admin | 1. Navigate to the Share Products page<br>2. Click the '+ Create Share Product' button<br>3. Leave the Product Name field empty<br>4. Leave the Short Name field empty<br>5. Leave the Description field empty<br>6. Click Submit | Error messages are displayed indicating that Product Name, Short Name, and Description are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-048 |  | Create a Share Product with maximum length fields | User logged in as Admin | 1. Navigate to the Share Products page<br>2. Click the '+ Create Share Product' button<br>3. Enter a Product Name with maximum allowed characters in the Product Name field<br>4. Enter a Short Name with maximum allowed characters in the Short Name field<br>5. Enter a Description with maximum allowed characters in the Description field<br>6. Click Next and fill in valid data for all subsequent steps<br>7. Click Submit | New Share Product is created successfully without any errors | medium |

---

## Charges

Total: **3** (positive: 1, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-049 |  | Create a new charge with valid inputs | User logged in as Admin | 1. Navigate to the Charges page<br>2. Click the '+ Create Charge' button<br>3. Enter 'Service Fee' in the Charge Name field<br>4. Select 'Loan' from the Charge Applies To dropdown<br>5. Select 'USD' from the Currency dropdown<br>6. Select 'Specified Due Date' from the Charge Time Type dropdown<br>7. Select 'Flat' from the Charge Calculation Type dropdown<br>8. Enter '50' in the Amount field<br>9. Check the Is Penalty checkbox<br>10. Check the Is Active checkbox<br>11. Select 'None' from the Tax Group dropdown<br>12. Select 'Regular' from the Payment Mode dropdown<br>13. Click Submit | A new charge 'Service Fee' is created and displayed in the Charges table | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-050 |  | Attempt to create a charge without a Charge Name | User logged in as Admin | 1. Navigate to the Charges page<br>2. Click the '+ Create Charge' button<br>3. Leave the Charge Name field empty<br>4. Select 'Loan' from the Charge Applies To dropdown<br>5. Select 'USD' from the Currency dropdown<br>6. Select 'Specified Due Date' from the Charge Time Type dropdown<br>7. Select 'Flat' from the Charge Calculation Type dropdown<br>8. Enter '50' in the Amount field<br>9. Click Submit | An error message is displayed stating that the Charge Name is required; the charge is not created | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-051 |  | Create a charge with maximum length Charge Name | User logged in as Admin | 1. Navigate to the Charges page<br>2. Click the '+ Create Charge' button<br>3. Enter a Charge Name with 255 characters in the Charge Name field<br>4. Select 'Loan' from the Charge Applies To dropdown<br>5. Select 'USD' from the Currency dropdown<br>6. Select 'Specified Due Date' from the Charge Time Type dropdown<br>7. Select 'Flat' from the Charge Calculation Type dropdown<br>8. Enter '50' in the Amount field<br>9. Click Submit | A new charge with the maximum length Charge Name is created and displayed in the Charges table | medium |

---

## Floating Rates

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-052 |  | Create a new floating rate with valid details | User logged in as Admin, User is on the Floating Rates page | 1. Click the '+ Create Floating Rate' button<br>2. Enter a valid Floating Rate Name in the Floating Rate Name field<br>3. Check the Is Base Lending Rate checkbox<br>4. Check the Is Active checkbox<br>5. Add a row in the Rate Periods table with valid From Date and Interest Rate<br>6. Click Submit | The new floating rate is added to the data table and is visible on the Floating Rates page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-053 |  | Attempt to create a base lending rate when one already exists | User logged in as Admin, A base lending rate already exists | 1. Click the '+ Create Floating Rate' button<br>2. Enter a valid Floating Rate Name in the Floating Rate Name field<br>3. Check the Is Base Lending Rate checkbox<br>4. Click Submit | An error message is displayed stating that only one base lending rate can exist at a time; the floating rate is not created | high |
| TC-055 |  | Attempt to create a floating rate without a name | User logged in as Admin, User is on the Floating Rates page | 1. Click the '+ Create Floating Rate' button<br>2. Leave the Floating Rate Name field empty<br>3. Click Submit | An error message is displayed stating that the Floating Rate Name is required; the floating rate is not created | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-054 |  | Create a floating rate with maximum length name | User logged in as Admin, User is on the Floating Rates page | 1. Click the '+ Create Floating Rate' button<br>2. Enter a Floating Rate Name with maximum allowed characters in the Floating Rate Name field<br>3. Check the Is Active checkbox<br>4. Add a row in the Rate Periods table with valid From Date and Interest Rate<br>5. Click Submit | The new floating rate is added to the data table and is visible on the Floating Rates page | medium |
| TC-056 |  | Create a floating rate with a differential rate | User logged in as Admin, User is on the Floating Rates page | 1. Click the '+ Create Floating Rate' button<br>2. Enter a valid Floating Rate Name in the Floating Rate Name field<br>3. Check the Is Base Lending Rate checkbox<br>4. Add a row in the Rate Periods table with valid From Date, Interest Rate, and check the Is Differential Rate checkbox<br>5. Click Submit | The new floating rate is added to the data table with the differential rate configuration | medium |

---

## Delinquency Management

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-057 |  | Create a Delinquency Range with valid inputs | User logged in as Admin, User is on the Delinquency Ranges page | 1. Click the Create Delinquency Range button<br>2. Enter <valid classification> in the Classification field<br>3. Enter <valid minimum age days> in the Minimum Age Days field<br>4. (Optional) Enter <valid maximum age days> in the Maximum Age Days field<br>5. Click Submit | New Delinquency Range is added to the data table with the correct details | high |
| TC-060 |  | Create a Delinquency Bucket with valid inputs | User logged in as Admin, User is on the Delinquency Buckets page | 1. Click the Create Delinquency Bucket button<br>2. Enter <valid bucket name> in the Bucket Name field<br>3. Add multiple delinquency ranges in sequence<br>4. Click Submit | New Delinquency Bucket is added to the data table with the correct details and associated ranges | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-058 |  | Attempt to create a Delinquency Range with missing required fields | User logged in as Admin, User is on the Delinquency Ranges page | 1. Click the Create Delinquency Range button<br>2. Leave the Classification field blank<br>3. Leave the Minimum Age Days field blank<br>4. Click Submit | Error messages are displayed indicating that Classification and Minimum Age Days are required fields; no new Delinquency Range is created | high |
| TC-061 |  | Attempt to create a Delinquency Bucket with missing required fields | User logged in as Admin, User is on the Delinquency Buckets page | 1. Click the Create Delinquency Bucket button<br>2. Leave the Bucket Name field blank<br>3. Click Submit | An error message is displayed indicating that Bucket Name is a required field; no new Delinquency Bucket is created | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-059 |  | Create a Delinquency Range with maximum boundary values | User logged in as Admin, User is on the Delinquency Ranges page | 1. Click the Create Delinquency Range button<br>2. Enter <valid classification> in the Classification field<br>3. Enter 0 in the Minimum Age Days field<br>4. Enter 99999 in the Maximum Age Days field<br>5. Click Submit | New Delinquency Range is added to the data table with the correct details, including the extreme values | medium |
| TC-062 |  | Create a Delinquency Bucket with maximum boundary values for bucket name | User logged in as Admin, User is on the Delinquency Buckets page | 1. Click the Create Delinquency Bucket button<br>2. Enter a bucket name with maximum allowed characters in the Bucket Name field<br>3. Add multiple delinquency ranges in sequence<br>4. Click Submit | New Delinquency Bucket is added to the data table with the correct details, including the maximum length bucket name | medium |

---

## Loan Account

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-063 |  | Successfully submit a new loan application with valid inputs | User logged in as Admin, A client exists with valid details | 1. Navigate to the Client Detail page of the client<br>2. Click on 'Apply for Loan'<br>3. Fill in the Loan Application form with valid details in all steps<br>4. Click Submit | Loan application is created with status 'Submitted and Pending Approval' | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-064 |  | Attempt to submit a loan application with an invalid principal amount | User logged in as Admin, A client exists with valid details | 1. Navigate to the Client Detail page of the client<br>2. Click on 'Apply for Loan'<br>3. Fill in the Loan Application form with an invalid principal amount (below product min or above product max)<br>4. Click Submit | An error message is displayed indicating the principal amount is invalid; loan application is not created | high |
| TC-066 |  | Attempt to submit a loan application without selecting a loan product | User logged in as Admin, A client exists with valid details | 1. Navigate to the Client Detail page of the client<br>2. Click on 'Apply for Loan'<br>3. Leave the Product Name dropdown unselected<br>4. Fill in the rest of the Loan Application form with valid details<br>5. Click Submit | An error message is displayed indicating that a loan product must be selected; loan application is not created | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-065 |  | Submit a loan application with the maximum allowed number of repayments | User logged in as Admin, A client exists with valid details | 1. Navigate to the Client Detail page of the client<br>2. Click on 'Apply for Loan'<br>3. Fill in the Loan Application form with the maximum allowed number of repayments<br>4. Click Submit | Loan application is created with status 'Submitted and Pending Approval' | medium |
| TC-067 |  | Submit a loan application with the minimum allowed interest rate | User logged in as Admin, A client exists with valid details | 1. Navigate to the Client Detail page of the client<br>2. Click on 'Apply for Loan'<br>3. Fill in the Loan Application form with the minimum allowed interest rate<br>4. Click Submit | Loan application is created with status 'Submitted and Pending Approval' | medium |

---

## Savings Account

Total: **3** (positive: 1, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-068 |  | Create a new savings account with valid inputs | User logged in as Admin, A client exists | 1. Navigate to the Client Detail page of the client<br>2. Click on Create Savings Account<br>3. Select <valid product name> from the Product Name dropdown<br>4. Select <valid field officer> from the Field Officer dropdown<br>5. Enter <valid submitted on date> in the Submitted On field<br>6. Verify that Nominal Annual Interest Rate, Interest Compounding Period, Interest Posting Period, Interest Calculated Using, Days in Year are auto-populated<br>7. Enter <valid minimum opening balance> in the Minimum Opening Balance field<br>8. Enter <valid lock-in period> in the Lock-in Period field<br>9. Check Allow Overdraft checkbox if applicable<br>10. Review Charges section and add any additional charges if necessary<br>11. Click Submit | Savings account is created with status 'Submitted and Pending Approval'; user is redirected to the Savings Account Detail page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-069 |  | Attempt to create a savings account without selecting a product | User logged in as Admin, A client exists | 1. Navigate to the Client Detail page of the client<br>2. Click on Create Savings Account<br>3. Leave the Product Name dropdown unselected<br>4. Fill in other required fields with valid data<br>5. Click Submit | An error message is displayed stating that the Product Name is required; the savings account is not created | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-070 |  | Create a savings account with the minimum opening balance set to zero | User logged in as Admin, A client exists | 1. Navigate to the Client Detail page of the client<br>2. Click on Create Savings Account<br>3. Select <valid product name> from the Product Name dropdown<br>4. Select <valid field officer> from the Field Officer dropdown<br>5. Enter <valid submitted on date> in the Submitted On field<br>6. Verify that Nominal Annual Interest Rate, Interest Compounding Period, Interest Posting Period, Interest Calculated Using, Days in Year are auto-populated<br>7. Enter 0 in the Minimum Opening Balance field<br>8. Enter <valid lock-in period> in the Lock-in Period field<br>9. Check Allow Overdraft checkbox if applicable<br>10. Review Charges section and add any additional charges if necessary<br>11. Click Submit | Savings account is created with status 'Submitted and Pending Approval'; user is redirected to the Savings Account Detail page | high |

---

## Share Account

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-071 |  | Create a new share account with valid inputs | User logged in as Admin, A client exists with an active savings account | 1. Navigate to the Client Detail page of the client<br>2. Click on the Create Share Account button<br>3. Select a valid Share Product from the dropdown<br>4. Enter a valid Submitted On date<br>5. Enter a valid number of Requested Shares within the product min/max limits<br>6. Enter a valid Application Date<br>7. Select a Savings Account for Charges from the dropdown<br>8. Enter a valid External ID<br>9. Fill in the Charges section if applicable<br>10. Click Submit | A new share account is created with status 'Submitted and Pending Approval'; confirmation message is displayed. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-072 |  | Attempt to create a share account with invalid requested shares | User logged in as Admin, A client exists with an active savings account | 1. Navigate to the Client Detail page of the client<br>2. Click on the Create Share Account button<br>3. Select a valid Share Product from the dropdown<br>4. Enter a valid Submitted On date<br>5. Enter an invalid number of Requested Shares (exceeds max limit)<br>6. Enter a valid Application Date<br>7. Select a Savings Account for Charges from the dropdown<br>8. Enter a valid External ID<br>9. Fill in the Charges section if applicable<br>10. Click Submit | An error message is displayed indicating that the requested shares exceed the maximum limit; share account is not created. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-073 |  | Create a share account with the minimum requested shares | User logged in as Admin, A client exists with an active savings account | 1. Navigate to the Client Detail page of the client<br>2. Click on the Create Share Account button<br>3. Select a valid Share Product from the dropdown<br>4. Enter a valid Submitted On date<br>5. Enter the minimum number of Requested Shares allowed by the product<br>6. Enter a valid Application Date<br>7. Select a Savings Account for Charges from the dropdown<br>8. Enter a valid External ID<br>9. Fill in the Charges section if applicable<br>10. Click Submit | A new share account is created with status 'Submitted and Pending Approval'; confirmation message is displayed. | medium |
| TC-074 |  | Create a share account with the maximum requested shares | User logged in as Admin, A client exists with an active savings account | 1. Navigate to the Client Detail page of the client<br>2. Click on the Create Share Account button<br>3. Select a valid Share Product from the dropdown<br>4. Enter a valid Submitted On date<br>5. Enter the maximum number of Requested Shares allowed by the product<br>6. Enter a valid Application Date<br>7. Select a Savings Account for Charges from the dropdown<br>8. Enter a valid External ID<br>9. Fill in the Charges section if applicable<br>10. Click Submit | A new share account is created with status 'Submitted and Pending Approval'; confirmation message is displayed. | medium |

---

## Fixed & Recurring Deposit Accounts

Total: **3** (positive: 1, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-075 |  | Create a Fixed Deposit account with valid details | User logged in as Admin, A client exists | 1. Navigate to the Client Detail page of the client<br>2. Click on Create Fixed Deposit Account<br>3. Select a valid Fixed Deposit Product from the dropdown<br>4. Enter a valid Deposit Amount<br>5. Enter a valid Deposit Period in numeric and select unit (Days, Months, Years)<br>6. Select Maturity Instructions from the options<br>7. Click Submit | A new Fixed Deposit account is created and displayed on the Client Detail page with correct details | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-076 |  | Attempt to create a Fixed Deposit account with invalid Deposit Amount | User logged in as Admin, A client exists | 1. Navigate to the Client Detail page of the client<br>2. Click on Create Fixed Deposit Account<br>3. Select a valid Fixed Deposit Product from the dropdown<br>4. Enter an invalid Deposit Amount (e.g., negative value)<br>5. Enter a valid Deposit Period<br>6. Select Maturity Instructions from the options<br>7. Click Submit | An error message is displayed indicating that the Deposit Amount must be a positive value; the account is not created | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-077 |  | Create a Recurring Deposit account with maximum Deposit Period | User logged in as Admin, A client exists | 1. Navigate to the Client Detail page of the client<br>2. Click on Create Recurring Deposit Account<br>3. Select a valid Recurring Deposit Product from the dropdown<br>4. Enter a valid Mandatory Deposit Amount per installment<br>5. Enter the maximum valid Deposit Period in numeric and select unit (Years)<br>6. Select Deposit Frequency (e.g., Yearly)<br>7. Enter a valid Expected First Deposit On date<br>8. Click Submit | A new Recurring Deposit account is created with the specified maximum Deposit Period and displayed on the Client Detail page | medium |

---

## Accounting — Chart of Accounts

Total: **3** (positive: 1, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-078 |  | Create a new GL Account with valid details | User logged in as Admin, User is on the Chart of Accounts page | 1. Click the '+ Create GL Account' button<br>2. Select 'Assets' from the Account Type dropdown<br>3. Select a valid Parent Account from the dropdown<br>4. Enter a unique GL Code<br>5. Enter a valid Account Name<br>6. Select 'Detail' for Account Usage<br>7. Check the 'Manual Entries Allowed' checkbox<br>8. Enter a description<br>9. Select a tag from the dropdown<br>10. Click Submit | The new GL Account is created and displayed in the Chart of Accounts tree with the correct details | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-079 |  | Attempt to create a GL Account with a duplicate GL Code | User logged in as Admin, User is on the Chart of Accounts page, A GL Account with the same GL Code exists | 1. Click the '+ Create GL Account' button<br>2. Select 'Liabilities' from the Account Type dropdown<br>3. Select a valid Parent Account from the dropdown<br>4. Enter the duplicate GL Code<br>5. Enter a valid Account Name<br>6. Select 'Header' for Account Usage<br>7. Click Submit | An error message is displayed stating that the GL Code must be unique; the GL Account is not created | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-080 |  | Create a GL Account with maximum length fields | User logged in as Admin, User is on the Chart of Accounts page | 1. Click the '+ Create GL Account' button<br>2. Select 'Expenses' from the Account Type dropdown<br>3. Select a valid Parent Account from the dropdown<br>4. Enter a GL Code with maximum allowed length<br>5. Enter an Account Name with maximum allowed length<br>6. Select 'Detail' for Account Usage<br>7. Check the 'Manual Entries Allowed' checkbox<br>8. Enter a description with maximum allowed length<br>9. Select a tag from the dropdown<br>10. Click Submit | The new GL Account is created successfully with maximum length fields and displayed in the Chart of Accounts tree | medium |

---

## Accounting — Journal Entries & Closures

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-081 |  | Add a valid journal entry with all required fields | User logged in as Admin, User is on the Journal Entries page | 1. Click the '+ Add Journal Entry' button<br>2. Select a valid Office from the dropdown<br>3. Select a valid Currency from the dropdown<br>4. Enter a valid Reference Number<br>5. Enter a valid Transaction Date<br>6. Select a valid Payment Type<br>7. Add at least one entry line with a valid GL Account and Amount<br>8. Click Submit | The new journal entry is displayed in the Journal Entries table with the correct details | high |
| TC-084 |  | Create a closure with valid details | User logged in as Admin, User is on the Closing Entries page | 1. Click the '+ Create Closure' button<br>2. Select a valid Office from the dropdown<br>3. Enter a valid Closing Date<br>4. Enter comments in the Comments field<br>5. Click Submit | The new closure is displayed in the Closing Entries table with the correct details | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-082 |  | Attempt to add a journal entry with missing required fields | User logged in as Admin, User is on the Journal Entries page | 1. Click the '+ Add Journal Entry' button<br>2. Leave the Office field empty<br>3. Leave the Currency field empty<br>4. Enter a valid Transaction Date<br>5. Click Submit | An error message is displayed indicating that Office and Currency are required fields; the journal entry is not created | high |
| TC-085 |  | Attempt to create a closure with missing required fields | User logged in as Admin, User is on the Closing Entries page | 1. Click the '+ Create Closure' button<br>2. Leave the Office field empty<br>3. Leave the Closing Date field empty<br>4. Click Submit | An error message is displayed indicating that Office and Closing Date are required fields; the closure is not created | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-083 |  | Add a journal entry with maximum allowed entry lines | User logged in as Admin, User is on the Journal Entries page | 1. Click the '+ Add Journal Entry' button<br>2. Select a valid Office from the dropdown<br>3. Select a valid Currency from the dropdown<br>4. Enter a valid Reference Number<br>5. Enter a valid Transaction Date<br>6. Select a valid Payment Type<br>7. Add the maximum number of entry lines with valid GL Accounts and Amounts<br>8. Click Submit | The new journal entry is displayed in the Journal Entries table with the correct details, including all entry lines | medium |
| TC-086 |  | Create a closure with a closing date set to today | User logged in as Admin, User is on the Closing Entries page | 1. Click the '+ Create Closure' button<br>2. Select a valid Office from the dropdown<br>3. Set the Closing Date to today's date<br>4. Enter comments in the Comments field<br>5. Click Submit | The new closure is displayed in the Closing Entries table with today's date as the closing date | medium |

---

## Accounting Rules & Financial Activity Mappings

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-087 |  | Create a new accounting rule with valid inputs | User logged in as Admin, User is on the Accounting Rules page | 1. Click the '+ Create Rule' button<br>2. Select an Office from the dropdown<br>3. Enter a valid Rule Name<br>4. Select one or more Debit Accounts from the GL account dropdown<br>5. Check the 'Allow Multiple Debit Entries' checkbox<br>6. Select one or more Credit Accounts from the GL account dropdown<br>7. Check the 'Allow Multiple Credit Entries' checkbox<br>8. Click Submit | The new accounting rule is added to the table and is visible in the Accounting Rules list | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-088 |  | Attempt to create a new accounting rule without a Rule Name | User logged in as Admin, User is on the Accounting Rules page | 1. Click the '+ Create Rule' button<br>2. Select an Office from the dropdown<br>3. Leave the Rule Name field empty<br>4. Select one or more Debit Accounts from the GL account dropdown<br>5. Select one or more Credit Accounts from the GL account dropdown<br>6. Click Submit | An error message is displayed indicating that the Rule Name is required; the rule is not created | high |
| TC-090 |  | Attempt to create a mapping for an already mapped financial activity | User logged in as Admin, User is on the Financial Activity Mappings page, A financial activity is already mapped | 1. Click the '+ Create Mapping' button<br>2. Select the already mapped Financial Activity from the dropdown<br>3. Select a GL Account from the dropdown<br>4. Click Submit | An error message is displayed stating that the financial activity is already mapped; the mapping is not created | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-089 |  | Create a mapping for a financial activity with maximum length GL account name | User logged in as Admin, User is on the Financial Activity Mappings page | 1. Click the '+ Create Mapping' button<br>2. Select a Financial Activity from the dropdown<br>3. Select a GL Account with the maximum allowed name length from the dropdown<br>4. Click Submit | The mapping is created successfully and appears in the Financial Activity Mappings table | medium |
| TC-091 |  | Create a mapping with an empty GL account selection | User logged in as Admin, User is on the Financial Activity Mappings page | 1. Click the '+ Create Mapping' button<br>2. Select a Financial Activity from the dropdown<br>3. Leave the GL Account dropdown empty<br>4. Click Submit | An error message is displayed indicating that a GL Account must be selected; the mapping is not created | high |

---

## Provisioning

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-092 |  | Create a new provisioning criteria with valid inputs | User logged in as Admin, User is on the Provisioning Criteria page | 1. Click the '+ Create' button<br>2. Enter a valid Criteria Name in the Criteria Name field<br>3. Add a row in the Definitions table with valid Loan Product, Category, Minimum Age, Maximum Age, Provisioning Percentage, Liability Account, and Expense Account<br>4. Click Submit | The new provisioning criteria is added to the data table and is visible on the Provisioning Criteria page | high |
| TC-095 |  | Generate provisioning entries based on current loan portfolio | User logged in as Admin, User is on the Provisioning Entries page, Provisioning criteria are configured | 1. Click the '+ Create Provisioning Entry' button<br>2. Confirm the generation of provisioning entries | New provisioning entries are created and listed on the Provisioning Entries page with correct details | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-093 |  | Attempt to create provisioning criteria without a Criteria Name | User logged in as Admin, User is on the Provisioning Criteria page | 1. Click the '+ Create' button<br>2. Leave the Criteria Name field empty<br>3. Add a row in the Definitions table with valid inputs<br>4. Click Submit | An error message is displayed stating that the Criteria Name is required; the criteria is not created | high |
| TC-096 |  | Attempt to generate provisioning entries without configured criteria | User logged in as Admin, User is on the Provisioning Entries page, No provisioning criteria are configured | 1. Click the '+ Create Provisioning Entry' button<br>2. Confirm the generation of provisioning entries | An error message is displayed stating that no provisioning criteria are configured; no entries are created | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-094 |  | Create provisioning criteria with maximum allowed rows in Definitions table | User logged in as Admin, User is on the Provisioning Criteria page | 1. Click the '+ Create' button<br>2. Enter a valid Criteria Name in the Criteria Name field<br>3. Add the maximum number of rows allowed in the Definitions table with valid inputs for each row<br>4. Click Submit | The new provisioning criteria is added to the data table with all rows in the Definitions table correctly saved | medium |
| TC-097 |  | Review a provisioning entry with maximum detail breakdown | User logged in as Admin, User is on the Provisioning Entries page, At least one provisioning entry exists | 1. Click on the action button to review a provisioning entry<br>2. Check the detailed breakdown by loan product and category | The detailed breakdown is displayed correctly with all relevant information shown | medium |

---

## Offices

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-098 |  | Create a new office with valid details | User logged in as Admin, User is on the Offices page | 1. Click the '+ Create Office' button<br>2. Enter a valid Office Name in the Office Name field<br>3. Select 'Head Office' as the Parent Office<br>4. Enter a valid date in the Opened On Date field<br>5. Enter a valid External ID<br>6. Click Submit | The new office is created and displayed in the hierarchical table with the correct details | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-099 |  | Attempt to create a new office without a required field | User logged in as Admin, User is on the Offices page | 1. Click the '+ Create Office' button<br>2. Leave the Office Name field empty<br>3. Select 'Head Office' as the Parent Office<br>4. Enter a valid date in the Opened On Date field<br>5. Enter a valid External ID<br>6. Click Submit | An error message is displayed indicating that the Office Name is required; the office is not created | high |
| TC-101 |  | Attempt to create a new office with an invalid Opened On Date | User logged in as Admin, User is on the Offices page | 1. Click the '+ Create Office' button<br>2. Enter a valid Office Name in the Office Name field<br>3. Select 'Head Office' as the Parent Office<br>4. Enter an invalid date in the Opened On Date field (e.g., future date)<br>5. Enter a valid External ID<br>6. Click Submit | An error message is displayed indicating that the Opened On Date is invalid; the office is not created | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-100 |  | Create an office with maximum length Office Name | User logged in as Admin, User is on the Offices page | 1. Click the '+ Create Office' button<br>2. Enter a maximum length Office Name in the Office Name field<br>3. Select 'Head Office' as the Parent Office<br>4. Enter a valid date in the Opened On Date field<br>5. Enter a valid External ID<br>6. Click Submit | The new office is created successfully and displayed in the hierarchical table with the correct details | medium |
| TC-102 |  | Create an office with an External ID that is a very long string | User logged in as Admin, User is on the Offices page | 1. Click the '+ Create Office' button<br>2. Enter a valid Office Name in the Office Name field<br>3. Select 'Head Office' as the Parent Office<br>4. Enter a valid date in the Opened On Date field<br>5. Enter a very long string in the External ID field<br>6. Click Submit | The new office is created successfully and displayed in the hierarchical table with the correct details, assuming the system allows long External IDs | medium |

---

## Employees

Total: **3** (positive: 1, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-103 |  | Create a new employee with all required fields filled | User logged in as Admin, User is on the Employees page | 1. Click the '+ Create Employee' button<br>2. Enter a valid Office in the Office field<br>3. Enter a valid First Name in the First Name field<br>4. Enter a valid Last Name in the Last Name field<br>5. Check the Is Loan Officer checkbox if applicable<br>6. Enter a valid Mobile Number in the Mobile Number field<br>7. Check the Is Active checkbox if applicable<br>8. Enter a valid Joining Date<br>9. Enter a valid External ID<br>10. Click Submit | The new employee is added to the Employees data table and a success message is displayed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-104 |  | Attempt to create a new employee without filling required fields | User logged in as Admin, User is on the Employees page | 1. Click the '+ Create Employee' button<br>2. Leave the Office field empty<br>3. Leave the First Name field empty<br>4. Leave the Last Name field empty<br>5. Click Submit | An error message is displayed indicating that required fields must be filled; the employee is not created | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-105 |  | Create an employee with maximum length fields | User logged in as Admin, User is on the Employees page | 1. Click the '+ Create Employee' button<br>2. Enter a valid Office with maximum allowed characters<br>3. Enter a First Name with maximum allowed characters<br>4. Enter a Last Name with maximum allowed characters<br>5. Check the Is Loan Officer checkbox<br>6. Enter a Mobile Number with maximum allowed digits<br>7. Check the Is Active checkbox<br>8. Enter a valid Joining Date<br>9. Enter a valid External ID with maximum allowed characters<br>10. Click Submit | The new employee is added to the Employees data table and a success message is displayed | medium |

---

## Teller & Cashier Management

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-106 |  | Create a new Teller with valid details | User logged in as Admin, User is on the Tellers page | 1. Click the '+ Create Teller' button<br>2. Enter a valid Office in the Office field<br>3. Enter a valid Teller Name in the Teller Name field<br>4. Enter a valid Description in the Description field<br>5. Enter a valid Start Date in the Start Date field<br>6. Select 'Active' from the Status dropdown<br>7. Click Submit | New Teller is added to the Tellers data table and is visible with the correct details | high |
| TC-109 |  | Allocate a Cashier to a Teller with valid details | User logged in as Admin, A Teller exists in the system | 1. Navigate to the Teller Detail page of the existing Teller<br>2. Click the '+ Allocate Cashier' button<br>3. Select a valid Staff member from the Staff dropdown<br>4. Enter a valid Start Date in the Start Date field<br>5. Enter a valid End Date in the End Date field<br>6. Check the Is Full Day checkbox<br>7. Click Submit | Cashier is allocated to the Teller and appears in the Cashiers section with correct details | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-107 |  | Attempt to create a Teller without required fields | User logged in as Admin, User is on the Tellers page | 1. Click the '+ Create Teller' button<br>2. Leave the Office field empty<br>3. Leave the Teller Name field empty<br>4. Enter a valid Description in the Description field<br>5. Enter a valid Start Date in the Start Date field<br>6. Click Submit | Error messages are displayed indicating that Office and Teller Name are required fields; Teller is not created | high |
| TC-110 |  | Attempt to allocate a Cashier without required fields | User logged in as Admin, A Teller exists in the system | 1. Navigate to the Teller Detail page of the existing Teller<br>2. Click the '+ Allocate Cashier' button<br>3. Leave the Staff field empty<br>4. Enter a valid Start Date in the Start Date field<br>5. Click Submit | Error message is displayed indicating that Staff is a required field; Cashier is not allocated | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-108 |  | Create a Teller with maximum length name | User logged in as Admin, User is on the Tellers page | 1. Click the '+ Create Teller' button<br>2. Enter a valid Office in the Office field<br>3. Enter a Teller Name with maximum allowed characters in the Teller Name field<br>4. Enter a valid Description in the Description field<br>5. Enter a valid Start Date in the Start Date field<br>6. Select 'Active' from the Status dropdown<br>7. Click Submit | New Teller is added to the Tellers data table with the maximum length name displayed correctly | medium |
| TC-111 |  | Allocate a Cashier with the same Start and End Date | User logged in as Admin, A Teller exists in the system | 1. Navigate to the Teller Detail page of the existing Teller<br>2. Click the '+ Allocate Cashier' button<br>3. Select a valid Staff member from the Staff dropdown<br>4. Enter the same date in both Start Date and End Date fields<br>5. Click Submit | Cashier is allocated to the Teller with the same Start and End Date, and appears in the Cashiers section | medium |

---

## Users & Roles

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-112 |  | Create a new user with valid details | User logged in as Admin, No existing user with the same username | 1. Navigate to the Users page<br>2. Click the '+ Create User' button<br>3. Enter a unique Username<br>4. Enter First Name<br>5. Enter Last Name<br>6. Enter a valid Email address<br>7. Select an Office from the dropdown<br>8. Select a Staff member from the dropdown<br>9. Enter a valid Password that meets the policy<br>10. Repeat the Password<br>11. Select Roles using multi-select checkboxes<br>12. Check the 'Send Password to Email' checkbox<br>13. Click Submit | A new user is created, and the user appears in the Users data table with the correct details. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-113 |  | Attempt to create a user with a duplicate username | User logged in as Admin, A user with the same username already exists | 1. Navigate to the Users page<br>2. Click the '+ Create User' button<br>3. Enter the existing Username<br>4. Enter First Name<br>5. Enter Last Name<br>6. Enter a valid Email address<br>7. Select an Office from the dropdown<br>8. Select a Staff member from the dropdown<br>9. Enter a valid Password that meets the policy<br>10. Repeat the Password<br>11. Click Submit | An error message is displayed stating that the username must be unique; the user is not created. | high |
| TC-115 |  | Attempt to create a user with an invalid email format | User logged in as Admin, No existing user with the same username | 1. Navigate to the Users page<br>2. Click the '+ Create User' button<br>3. Enter a unique Username<br>4. Enter First Name<br>5. Enter Last Name<br>6. Enter an invalid Email address (e.g., 'invalid-email')<br>7. Select an Office from the dropdown<br>8. Select a Staff member from the dropdown<br>9. Enter a valid Password that meets the policy<br>10. Repeat the Password<br>11. Click Submit | An error message is displayed indicating the email format is invalid; the user is not created. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-114 |  | Create a user with the maximum length of each field | User logged in as Admin, No existing user with the same username | 1. Navigate to the Users page<br>2. Click the '+ Create User' button<br>3. Enter a unique Username with maximum length<br>4. Enter First Name with maximum length<br>5. Enter Last Name with maximum length<br>6. Enter a valid Email address with maximum length<br>7. Select an Office from the dropdown<br>8. Select a Staff member from the dropdown<br>9. Enter a valid Password that meets the policy with maximum length<br>10. Repeat the Password<br>11. Click Submit | A new user is created successfully, and the user appears in the Users data table with the correct details. | medium |
| TC-116 |  | Create a user with a password that is exactly at the minimum length | User logged in as Admin, No existing user with the same username | 1. Navigate to the Users page<br>2. Click the '+ Create User' button<br>3. Enter a unique Username<br>4. Enter First Name<br>5. Enter Last Name<br>6. Enter a valid Email address<br>7. Select an Office from the dropdown<br>8. Select a Staff member from the dropdown<br>9. Enter a Password that meets the policy and is at the minimum length<br>10. Repeat the Password<br>11. Click Submit | A new user is created successfully, and the user appears in the Users data table with the correct details. | medium |

---

## Reports

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-117 |  | Generate a report for Active Loans Summary | User logged in as Admin, User is on the Reports page | 1. Click on the Active Loans Summary report link<br>2. Fill in the parameters form with valid selections for Office, Branch, Currency, Loan Product, Date Range, Loan Officer, and Fund<br>3. Click the Run Report button | The report is generated and displayed as a data table with sorting and pagination options | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-118 |  | Attempt to generate a report without selecting required parameters | User logged in as Admin, User is on the Reports page | 1. Click on the Loans Pending Approval report link<br>2. Leave all parameters fields empty<br>3. Click the Run Report button | An error message is displayed indicating that required parameters must be filled in; the report is not generated | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-119 |  | Generate a report with the maximum allowed date range | User logged in as Admin, User is on the Reports page | 1. Click on the Portfolio at Risk report link<br>2. Fill in the parameters form with valid selections and set the Date Range to the maximum allowed (e.g., 1 year)<br>3. Click the Run Report button | The report is generated successfully and displayed as a data table with sorting and pagination options | medium |
| TC-120 |  | Export a report to CSV format | User logged in as Admin, User has generated a report | 1. Click on the Active Loans Details report link<br>2. Fill in the parameters form with valid selections<br>3. Click the Run Report button<br>4. Click the Export to CSV button | The report is downloaded in CSV format | medium |

---

## Account Transfers & Standing Instructions

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-121 |  | Successfully transfer funds between accounts | User logged in as Admin, From account has sufficient balance | 1. Navigate to the Account Transfers page<br>2. Select the From Office and From Client<br>3. Choose From Account Type as Savings Account<br>4. Select the From Account<br>5. Select the To Office and To Client<br>6. Choose To Account Type as Loan Account<br>7. Select the To Account<br>8. Enter a valid Transfer Amount<br>9. Enter a valid Transfer Date<br>10. Optionally enter a Description<br>11. Click Submit | Transfer is processed successfully; the From Account is debited and the To Account is credited with the transfer amount. | high |
| TC-124 |  | Create a standing instruction successfully | User logged in as Admin, From and To accounts are valid | 1. Navigate to the Standing Instructions page<br>2. Click on '+ Create Standing Instruction'<br>3. Enter a valid Name<br>4. Select From Account and To Account<br>5. Choose Transfer Type and Priority<br>6. Select Instruction Type as Fixed<br>7. Enter a valid Amount<br>8. Set Validity From and Till dates<br>9. Choose Recurrence Type as Periodic<br>10. Enter Recurrence Frequency and Interval<br>11. Click Submit | Standing instruction is created successfully and appears in the listing with status 'Active'. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-122 |  | Attempt to transfer funds exceeding available balance | User logged in as Admin, From account has insufficient balance | 1. Navigate to the Account Transfers page<br>2. Select the From Office and From Client<br>3. Choose From Account Type as Savings Account<br>4. Select the From Account<br>5. Select the To Office and To Client<br>6. Choose To Account Type as Loan Account<br>7. Select the To Account<br>8. Enter a Transfer Amount greater than the available balance<br>9. Enter a valid Transfer Date<br>10. Click Submit | An error message is displayed stating that the transfer amount exceeds the available balance; no transfer is processed. | high |
| TC-125 |  | Attempt to create a standing instruction with missing required fields | User logged in as Admin | 1. Navigate to the Standing Instructions page<br>2. Click on '+ Create Standing Instruction'<br>3. Leave the Name field empty<br>4. Select From Account and To Account<br>5. Choose Transfer Type and Priority<br>6. Select Instruction Type as Fixed<br>7. Enter a valid Amount<br>8. Set Validity From and Till dates<br>9. Choose Recurrence Type as Periodic<br>10. Enter Recurrence Frequency and Interval<br>11. Click Submit | An error message is displayed stating that the Name field is required; no standing instruction is created. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-123 |  | Submit a transfer with a zero transfer amount | User logged in as Admin, From account has sufficient balance | 1. Navigate to the Account Transfers page<br>2. Select the From Office and From Client<br>3. Choose From Account Type as Savings Account<br>4. Select the From Account<br>5. Select the To Office and To Client<br>6. Choose To Account Type as Loan Account<br>7. Select the To Account<br>8. Enter a Transfer Amount of 0<br>9. Enter a valid Transfer Date<br>10. Click Submit | An error message is displayed stating that the transfer amount must be greater than zero; no transfer is processed. | high |
| TC-126 |  | Create a standing instruction with maximum allowed values | User logged in as Admin, From and To accounts are valid | 1. Navigate to the Standing Instructions page<br>2. Click on '+ Create Standing Instruction'<br>3. Enter a Name with maximum allowed characters<br>4. Select From Account and To Account<br>5. Choose Transfer Type and Priority<br>6. Select Instruction Type as Dues<br>7. Enter the maximum allowed Amount<br>8. Set Validity From and Till dates to the maximum range<br>9. Choose Recurrence Type as As Per Dues<br>10. Enter maximum allowed Recurrence Frequency and Interval<br>11. Click Submit | Standing instruction is created successfully with maximum values and appears in the listing. | high |

---

## Tax Management

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-127 |  | Create a new Tax Component with valid details | User logged in as Admin | 1. Navigate to the Tax Components page<br>2. Click the '+ Create Tax Component' button<br>3. Enter a valid Name in the Name field<br>4. Enter a valid Percentage in the Percentage field<br>5. Select a valid Debit Account Type from the dropdown<br>6. Select a valid Debit Account from the GL account dropdown<br>7. Select a valid Credit Account Type from the dropdown<br>8. Select a valid Credit Account from the GL account dropdown<br>9. Enter a valid Start Date<br>10. Click Submit | The new Tax Component is added to the Tax Components table and is visible in the list | high |
| TC-130 |  | Create a new Tax Group with valid details | User logged in as Admin | 1. Navigate to the Tax Groups page<br>2. Click the '+ Create Tax Group' button<br>3. Enter a valid Name in the Name field<br>4. Add at least one Tax Component with valid Start Date and End Date<br>5. Click Submit | The new Tax Group is added to the Tax Groups table and is visible in the list | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-128 |  | Attempt to create a Tax Component with missing required fields | User logged in as Admin | 1. Navigate to the Tax Components page<br>2. Click the '+ Create Tax Component' button<br>3. Leave the Name field empty<br>4. Leave the Percentage field empty<br>5. Click Submit | An error message is displayed indicating that Name and Percentage are required fields; the Tax Component is not created | high |
| TC-131 |  | Attempt to create a Tax Group with missing required fields | User logged in as Admin | 1. Navigate to the Tax Groups page<br>2. Click the '+ Create Tax Group' button<br>3. Leave the Name field empty<br>4. Click Submit | An error message is displayed indicating that Name is a required field; the Tax Group is not created | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-129 |  | Create a Tax Component with maximum length Name | User logged in as Admin | 1. Navigate to the Tax Components page<br>2. Click the '+ Create Tax Component' button<br>3. Enter a Name with maximum allowed characters in the Name field<br>4. Enter a valid Percentage in the Percentage field<br>5. Select a valid Debit Account Type from the dropdown<br>6. Select a valid Debit Account from the GL account dropdown<br>7. Select a valid Credit Account Type from the dropdown<br>8. Select a valid Credit Account from the GL account dropdown<br>9. Enter a valid Start Date<br>10. Click Submit | The new Tax Component is added to the Tax Components table and is visible in the list | high |
| TC-132 |  | Create a Tax Group with maximum length Name | User logged in as Admin | 1. Navigate to the Tax Groups page<br>2. Click the '+ Create Tax Group' button<br>3. Enter a Name with maximum allowed characters in the Name field<br>4. Add at least one Tax Component with valid Start Date and End Date<br>5. Click Submit | The new Tax Group is added to the Tax Groups table and is visible in the list | high |

---

## Organization Settings

Total: **12** (positive: 4, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-133 |  | Create a holiday with valid details | User logged in as Admin, User is on the Holidays page | 1. Click the '+ Create Holiday' button<br>2. Enter 'New Year' in the Name field<br>3. Select '2024-01-01' in the From Date field<br>4. Select '2024-01-02' in the To Date field<br>5. Select 'Reschedule to next working day' in the Rescheduling Type dropdown<br>6. Enter 'New Year Holiday' in the Description field<br>7. Select applicable offices from the multi-select dropdown<br>8. Click Submit | Holiday is created and displayed in the Holidays table with status 'Active' | high |
| TC-136 |  | Configure working days successfully | User logged in as Admin, User is on the Working Days page | 1. Check the checkboxes for Monday, Tuesday, Wednesday, Thursday, and Friday<br>2. Select 'Reschedule to next working day' in the Repayment Rescheduling dropdown<br>3. Click Save | Working days are updated successfully and a confirmation message is displayed | high |
| TC-139 |  | Create a new payment type successfully | User logged in as Admin, User is on the Payment Types page | 1. Click the '+ Create' button<br>2. Enter 'Credit Card' in the Name field<br>3. Enter 'Payment via credit card' in the Description field<br>4. Check the 'Is Cash Payment' checkbox<br>5. Set the Position to 1<br>6. Click Submit | New payment type 'Credit Card' is created and displayed in the Payment Types list | high |
| TC-142 |  | Import data for clients successfully | User logged in as Admin, User is on the Bulk Import page | 1. Click the 'Download template' button for Clients<br>2. Fill in the template with valid client data<br>3. Click the 'Upload' button<br>4. Select the filled template file<br>5. Click Submit | Clients are imported successfully, and a confirmation message is displayed with the number of clients imported | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-134 |  | Attempt to create a holiday without required fields | User logged in as Admin, User is on the Holidays page | 1. Click the '+ Create Holiday' button<br>2. Leave the Name field empty<br>3. Select '2024-01-01' in the From Date field<br>4. Select '2024-01-02' in the To Date field<br>5. Click Submit | An error message is displayed indicating that the Name field is required; the holiday is not created | high |
| TC-137 |  | Attempt to save working days without selecting any days | User logged in as Admin, User is on the Working Days page | 1. Leave all checkboxes unchecked<br>2. Select 'Reschedule to next working day' in the Repayment Rescheduling dropdown<br>3. Click Save | An error message is displayed indicating that at least one working day must be selected; the settings are not saved | high |
| TC-140 |  | Attempt to create a payment type without a name | User logged in as Admin, User is on the Payment Types page | 1. Click the '+ Create' button<br>2. Leave the Name field empty<br>3. Enter 'Payment via credit card' in the Description field<br>4. Click Submit | An error message is displayed indicating that the Name field is required; the payment type is not created | high |
| TC-143 |  | Attempt to import data with an invalid file format | User logged in as Admin, User is on the Bulk Import page | 1. Click the 'Upload' button<br>2. Select an invalid file format (e.g., .txt)<br>3. Click Submit | An error message is displayed indicating that the file format is not supported; no data is imported | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-135 |  | Create a holiday with the same From and To date | User logged in as Admin, User is on the Holidays page | 1. Click the '+ Create Holiday' button<br>2. Enter 'Single Day Holiday' in the Name field<br>3. Select '2024-01-01' in the From Date field<br>4. Select '2024-01-01' in the To Date field<br>5. Click Submit | Holiday is created and displayed in the Holidays table with status 'Active' for a single day | medium |
| TC-138 |  | Configure working days with only Sunday selected | User logged in as Admin, User is on the Working Days page | 1. Check the checkbox for Sunday only<br>2. Select 'Reschedule to next working day' in the Repayment Rescheduling dropdown<br>3. Click Save | Working days are updated successfully with only Sunday selected; a confirmation message is displayed | medium |
| TC-141 |  | Create a payment type with maximum length name | User logged in as Admin, User is on the Payment Types page | 1. Click the '+ Create' button<br>2. Enter a name with 255 characters in the Name field<br>3. Enter 'Payment via credit card' in the Description field<br>4. Click Submit | Payment type is created successfully with the maximum length name and displayed in the Payment Types list | medium |
| TC-144 |  | Import data with maximum number of clients in a single file | User logged in as Admin, User is on the Bulk Import page | 1. Click the 'Download template' button for Clients<br>2. Fill in the template with maximum allowed number of clients<br>3. Click the 'Upload' button<br>4. Select the filled template file<br>5. Click Submit | Clients are imported successfully, and a confirmation message is displayed with the number of clients imported | medium |

---

## System Administration

Total: **8** (positive: 3, negative: 3, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-145 |  | Activate a scheduled job successfully | User logged in as Admin, A scheduled job exists in inactive status | 1. Navigate to the Manage Scheduler Jobs page<br>2. Locate the scheduled job in the table<br>3. Toggle the Is Active switch to 'On'<br>4. Click Save | The job status updates to 'Active' and the toggle reflects the change | high |
| TC-148 |  | Enable a global Start/Stop scheduler toggle | User logged in as Admin | 1. Navigate to the Global Configuration page<br>2. Toggle the Start/Stop scheduler switch to 'On'<br>3. Click Save | All scheduled jobs are set to execute, and the toggle reflects the change | high |
| TC-151 |  | View audit trails with filters applied | User logged in as Admin | 1. Navigate to the Audit Trails page<br>2. Apply filters for Action Name and Date Range<br>3. Click Apply Filters | The audit trails table updates to show only the filtered results | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-146 |  | Attempt to save an invalid CRON expression | User logged in as Admin, A scheduled job exists | 1. Navigate to the Manage Scheduler Jobs page<br>2. Locate the scheduled job in the table<br>3. Edit the CRON Expression field with an invalid expression<br>4. Click Save | An error message is displayed indicating the CRON expression is invalid; the job remains unchanged | high |
| TC-149 |  | Attempt to deactivate a job that is currently running | User logged in as Admin, A scheduled job is currently running | 1. Navigate to the Manage Scheduler Jobs page<br>2. Locate the currently running job<br>3. Toggle the Is Active switch to 'Off'<br>4. Click Save | An error message is displayed stating the job cannot be deactivated while running; the job status remains active | high |
| TC-152 |  | Attempt to approve a command without maker-checker enabled | User logged in as Admin, Maker-checker feature is disabled | 1. Navigate to the Audit Trails page<br>2. Locate a pending command<br>3. Click Approve | An error message is displayed stating that maker-checker is not enabled; the command remains pending | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-147 |  | Edit a job with a maximum length CRON expression | User logged in as Admin, A scheduled job exists | 1. Navigate to the Manage Scheduler Jobs page<br>2. Locate the scheduled job in the table<br>3. Edit the CRON Expression field with a maximum length valid expression<br>4. Click Save | The job is updated successfully with the new CRON expression | medium |
| TC-150 |  | Add a custom data table with maximum length field names | User logged in as Admin | 1. Navigate to the Manage Data Tables page<br>2. Click Add New Data Table<br>3. Enter a Data Table Name and Application Table Name<br>4. Check Multi Row checkbox<br>5. Add column definitions with maximum length field names<br>6. Click Save | The custom data table is created successfully with the specified field names | medium |

---

## Logout

Total: **3** (positive: 1, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-153 |  | Successfully log out from the application | User logged in to the application | 1. Click on the user profile icon in the top-right corner<br>2. Select 'Log Out' from the dropdown menu | User is redirected to the login page and the session is terminated | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-154 |  | Attempt to access an authenticated page after logging out | User logged in to the application, User has logged out | 1. Try to navigate to an authenticated page (e.g., Client Detail page) | User is redirected to the login page with no access to the authenticated page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-155 |  | Log out while a long-running process is active | User logged in to the application, A long-running process is initiated (e.g., generating a report) | 1. Click on the user profile icon in the top-right corner<br>2. Select 'Log Out' from the dropdown menu | User is redirected to the login page, and the long-running process is terminated | medium |

---
