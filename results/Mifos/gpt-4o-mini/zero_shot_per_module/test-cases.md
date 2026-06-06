# Test Cases — Mifos

Generated: 2026-06-04T14:55:03.662796Z  
Model: gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 31 | 198 | 54 | 70 | 74 | 114 | 79 | 5 |

## Login

Total: **6** (positive: 1, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Successful login with valid credentials | User is on the login page, User has valid credentials | 1. Select a tenant from the Tenant dropdown<br>2. Enter a valid username<br>3. Enter a valid password<br>4. Click the Login button | User is redirected to the Dashboard | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Login attempt with invalid credentials | User is on the login page, User has invalid credentials | 1. Select a tenant from the Tenant dropdown<br>2. Enter an invalid username<br>3. Enter an invalid password<br>4. Click the Login button | An error message is displayed indicating invalid credentials | high |
| TC-003 |  | Login attempt with empty required fields | User is on the login page | 1. Leave the Tenant dropdown as default<br>2. Leave the Username field empty<br>3. Leave the Password field empty<br>4. Click the Login button | Inline validation messages are shown for empty required fields | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Login attempt with maximum length username and password | User is on the login page | 1. Select a tenant from the Tenant dropdown<br>2. Enter a username with maximum allowed length<br>3. Enter a password with maximum allowed length<br>4. Click the Login button | User is redirected to the Dashboard if credentials are valid, or an error message is shown if invalid | medium |
| TC-005 |  | Login attempt with special characters in username and password | User is on the login page | 1. Select a tenant from the Tenant dropdown<br>2. Enter a username with special characters<br>3. Enter a password with special characters<br>4. Click the Login button | User is redirected to the Dashboard if credentials are valid, or an error message is shown if invalid | medium |
| TC-006 |  | Login attempt with whitespace in username and password | User is on the login page | 1. Select a tenant from the Tenant dropdown<br>2. Enter a username with leading and trailing spaces<br>3. Enter a password with leading and trailing spaces<br>4. Click the Login button | User is redirected to the Dashboard if credentials are valid after trimming spaces, or an error message is shown if invalid | medium |

---

## Home Page

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 |  | Display welcome message | User is logged in successfully. | 1. Navigate to the Home page. | The welcome card displays the message 'Welcome, mifos!' | high |
| TC-008 |  | Search activity with valid input | User is logged in successfully., Recent activities exist. | 1. Enter a valid search term in the 'Search Activity' input field.<br>2. Press Enter or click the search button. | The system displays the relevant recent activities based on the search term. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 |  | Search activity with empty input | User is logged in successfully. | 1. Leave the 'Search Activity' input field empty.<br>2. Press Enter or click the search button. | The system shows an error message indicating that the search term cannot be empty. | high |
| TC-010 |  | Search activity with invalid input | User is logged in successfully. | 1. Enter an invalid search term that does not match any activities.<br>2. Press Enter or click the search button. | The system shows a message indicating no activities found. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 |  | Search activity with maximum length input | User is logged in successfully. | 1. Enter a search term that is at the maximum character limit for the input field.<br>2. Press Enter or click the search button. | The system processes the search and displays relevant activities or a message indicating no activities found. | medium |
| TC-012 |  | Check system version information display | User is logged in successfully. | 1. Navigate to the Home page. | The system displays the version information for Mifos and Fineract at the bottom of the page. | low |

---

## Dashboard

Total: **5** (positive: 2, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 |  | Access Dashboard Successfully | User is on the Home page, User is logged in | 1. Click on the 'Dashboard' button<br>2. Observe the Dashboard page | The Dashboard page is displayed with 'Search Activity' field and 'Client Trends' chart. | high |
| TC-016 |  | View Client Trends Chart | User is on the Dashboard page, Data is available for the selected office | 1. Observe the 'Client Trends' chart<br>2. Check the legends for 'New Clients' and 'Closed Clients' | The 'Client Trends' chart is displayed with correct data and legends. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-014 |  | Search Activity with Invalid Input | User is on the Dashboard page | 1. Enter invalid input in the 'Search Activity' field<br>2. Click on the search button | An error message is displayed indicating invalid input. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 |  | Search Activity with Empty Input | User is on the Dashboard page | 1. Leave the 'Search Activity' field empty<br>2. Click on the search button | An error message is displayed indicating that the field cannot be empty. | medium |
| TC-017 |  | View Summary Cards with No Data | User is on the Dashboard page, No data is available for the selected office | 1. Observe the summary cards below the chart | The summary cards display 'No Data'. | low |

---

## Global Search

Total: **6** (positive: 1, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-018 |  | Successful search with valid input | User is logged in, User is on any page with the search icon | 1. Click on the search icon in the top toolbar<br>2. Type a valid search term that matches an entity (e.g., 'Client A') | Matching results appear in a dropdown grouped by entity type, showing entity name, identifier, and status. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-019 |  | Search with no input | User is logged in, User is on any page with the search icon | 1. Click on the search icon in the top toolbar<br>2. Leave the search input field empty and press Enter | No results found message is displayed. | high |
| TC-020 |  | Search with invalid input | User is logged in, User is on any page with the search icon | 1. Click on the search icon in the top toolbar<br>2. Type a random string that does not match any entity (e.g., 'xyz123') | No results found message is displayed. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-021 |  | Search with maximum length input | User is logged in, User is on any page with the search icon | 1. Click on the search icon in the top toolbar<br>2. Type a string that reaches the maximum input length allowed (e.g., 255 characters) | Matching results appear in a dropdown or a 'No results found' message if no matches exist. | medium |
| TC-022 |  | Search with case-insensitive input | User is logged in, User is on any page with the search icon | 1. Click on the search icon in the top toolbar<br>2. Type a valid search term in different cases (e.g., 'client a', 'CLIENT A', 'Client A') | Matching results appear in a dropdown grouped by entity type, showing entity name, identifier, and status. | medium |
| TC-023 |  | Search with partial input | User is logged in, User is on any page with the search icon | 1. Click on the search icon in the top toolbar<br>2. Type a partial name that matches an entity (e.g., 'Client') | Matching results appear in a dropdown grouped by entity type, showing entity name, identifier, and status. | medium |

---

## Client Management

Total: **8** (positive: 2, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-024 |  | Successfully create a new client with valid details | User is logged in, User is on the Create Client form | 1. Fill in all required fields with valid data.<br>2. Click on the 'Submit' button. | The client is created successfully and is displayed in Pending status on the Clients page. | high |
| TC-029 |  | Filter clients by status | User is logged in, User is on the Clients page | 1. Select 'Active' from the status filter.<br>2. Click on the filter button. | Only clients with Active status are displayed in the data table. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-025 |  | Fail to create a new client with missing required fields | User is logged in, User is on the Create Client form | 1. Leave the First Name and Last Name fields empty.<br>2. Click on the 'Submit' button. | An error message is displayed indicating that required fields must be filled. | high |
| TC-026 |  | Fail to create a new client with a non-unique External ID | User is logged in, User is on the Create Client form, An existing client has the same External ID | 1. Fill in all required fields with valid data including the existing External ID.<br>2. Click on the 'Submit' button. | An error message is displayed indicating that the External ID must be unique. | high |
| TC-030 |  | Attempt to activate a client without an Activation Date | User is logged in, User is on the Client Detail page of a Pending client | 1. Click on the 'Activate' button without entering an Activation Date. | An error message is displayed indicating that Activation Date is required. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-027 |  | Create a client with maximum length fields | User is logged in, User is on the Create Client form | 1. Fill in all fields with maximum allowed character lengths.<br>2. Click on the 'Submit' button. | The client is created successfully without any errors. | medium |
| TC-028 |  | Search for a client with an empty search field | User is logged in, User is on the Clients page | 1. Leave the search field empty.<br>2. Click on the search button. | All clients are displayed in the data table. | low |
| TC-031 |  | Attempt to close a client with active accounts | User is logged in, User is on the Client Detail page of an Active client | 1. Click on the 'Close' button.<br>2. Enter a closure reason.<br>3. Click on the 'Submit' button. | An error message is displayed indicating that the client cannot be closed with active accounts. | high |

---

## Group Management

Total: **7** (positive: 2, negative: 3, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-032 |  | Create a new group with valid inputs | User is logged in, User is on the Groups page | 1. Click on 'Create Group' button<br>2. Fill in the 'Name' field with a valid group name<br>3. Select an 'Office' from the dropdown<br>4. Fill in the 'Submitted On' field with a valid date<br>5. Check the 'Active' checkbox<br>6. Click 'Submit' | A new group is created successfully, and the user is redirected to the Groups page with the new group listed. | high |
| TC-037 |  | View group details and tabs | User is logged in, User is on the Groups page, At least one group exists | 1. Click on a group name link in the Groups table<br>2. Observe the Group Detail page and its tabs | The Group Detail page displays the correct group information and all tabs are visible. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-033 |  | Attempt to create a new group without required fields | User is logged in, User is on the Groups page | 1. Click on 'Create Group' button<br>2. Leave the 'Name' field empty<br>3. Leave the 'Office' field empty<br>4. Click 'Submit' | An error message is displayed indicating that 'Name' and 'Office' are required fields. | high |
| TC-035 |  | Attempt to upload an invalid file format in Bulk Import | User is logged in, User is on the Bulk Import Groups page | 1. Click on the file picker in the Groups Upload panel<br>2. Select a file with an unsupported format (e.g., .txt)<br>3. Click 'Upload' | An error message is displayed indicating that the file format is not supported. | high |
| TC-038 |  | Attempt to create a group with a duplicate name | User is logged in, User is on the Groups page, A group with the same name already exists | 1. Click on 'Create Group' button<br>2. Fill in the 'Name' field with the name of the existing group<br>3. Select an 'Office' from the dropdown<br>4. Fill in the 'Submitted On' field with a valid date<br>5. Click 'Submit' | An error message is displayed indicating that the group name must be unique. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-034 |  | Create a new group with maximum length name | User is logged in, User is on the Groups page | 1. Click on 'Create Group' button<br>2. Fill in the 'Name' field with a string of maximum allowed length<br>3. Select an 'Office' from the dropdown<br>4. Fill in the 'Submitted On' field with a valid date<br>5. Click 'Submit' | A new group is created successfully, and the user is redirected to the Groups page with the new group listed. | medium |
| TC-036 |  | Upload a file with maximum allowed size | User is logged in, User is on the Bulk Import Groups page | 1. Click on the file picker in the Groups Upload panel<br>2. Select a file that is at the maximum allowed size<br>3. Click 'Upload' | The file is uploaded successfully, and the import history table is updated. | medium |

---

## Center Management

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-039 |  | Create Center with valid inputs | User is logged in, User is on the Centers page | 1. Click on 'Create Center' button.<br>2. Fill in the 'Name' field with a valid name.<br>3. Select an 'Office' from the dropdown.<br>4. Fill in the 'External Id' field with a valid ID.<br>5. Check the 'Active' checkbox.<br>6. Fill in the 'Submitted On' field with a valid date.<br>7. Select groups from the 'Select and Add groups' dropdown.<br>8. Click on 'Submit' button. | A new center is created successfully, and the user is redirected to the Centers page with a success message. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-040 |  | Create Center with missing required fields | User is logged in, User is on the Centers page | 1. Click on 'Create Center' button.<br>2. Leave the 'Name' field empty.<br>3. Leave the 'Office' field empty.<br>4. Click on 'Submit' button. | An error message is displayed indicating that 'Name' and 'Office' are required fields. | high |
| TC-042 |  | Create Center with invalid date format | User is logged in, User is on the Centers page | 1. Click on 'Create Center' button.<br>2. Fill in the 'Name' field with a valid name.<br>3. Select an 'Office' from the dropdown.<br>4. Fill in the 'External Id' field with a valid ID.<br>5. Check the 'Active' checkbox.<br>6. Fill in the 'Submitted On' field with an invalid date format.<br>7. Select groups from the 'Select and Add groups' dropdown.<br>8. Click on 'Submit' button. | An error message is displayed indicating that the date format is invalid. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-041 |  | Create Center with maximum length name | User is logged in, User is on the Centers page | 1. Click on 'Create Center' button.<br>2. Fill in the 'Name' field with a string of maximum allowed length.<br>3. Select an 'Office' from the dropdown.<br>4. Fill in the 'External Id' field with a valid ID.<br>5. Check the 'Active' checkbox.<br>6. Fill in the 'Submitted On' field with a valid date.<br>7. Select groups from the 'Select and Add groups' dropdown.<br>8. Click on 'Submit' button. | A new center is created successfully, and the user is redirected to the Centers page with a success message. | medium |
| TC-043 |  | Create Center with empty fields in optional fields | User is logged in, User is on the Centers page | 1. Click on 'Create Center' button.<br>2. Fill in the 'Name' field with a valid name.<br>3. Select an 'Office' from the dropdown.<br>4. Leave 'Staff' and 'External Id' fields empty.<br>5. Check the 'Active' checkbox.<br>6. Fill in the 'Submitted On' field with a valid date.<br>7. Select groups from the 'Select and Add groups' dropdown.<br>8. Click on 'Submit' button. | A new center is created successfully, and the user is redirected to the Centers page with a success message. | medium |

---

## Loan Products

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-044 |  | Create a new loan product with valid details | User is logged in, User is on the Loan Products page | 1. Click on '+ Create Loan Product' button.<br>2. Fill in all required fields in Step 1 with valid data.<br>3. Proceed through all steps with valid data.<br>4. Click 'Finish' to create the loan product. | The loan product is created successfully and appears in the data table. | high |
| TC-049 |  | Edit an existing loan product | User is logged in, User is on the Loan Products page, At least one loan product exists | 1. Click on an existing loan product name.<br>2. Click on 'Edit' option.<br>3. Modify the required fields.<br>4. Click 'Save' to update the loan product. | The loan product is updated successfully and changes are reflected in the data table. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-045 |  | Attempt to create a loan product without required fields | User is logged in, User is on the Loan Products page | 1. Click on '+ Create Loan Product' button.<br>2. Leave the Product Name and Short Name fields empty.<br>3. Click 'Finish' to create the loan product. | Inline validation errors are displayed for Product Name and Short Name fields. | high |
| TC-047 |  | Create a loan product with invalid currency selection | User is logged in, User is on the Loan Products page | 1. Click on '+ Create Loan Product' button.<br>2. Fill in all required fields in Step 1 with valid data.<br>3. In Step 2, select an invalid currency.<br>4. Click 'Next' to proceed. | An error message is displayed indicating the currency selection is invalid. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-046 |  | Create a loan product with maximum length fields | User is logged in, User is on the Loan Products page | 1. Click on '+ Create Loan Product' button.<br>2. Fill in the Product Name and Short Name with maximum allowed characters.<br>3. Fill in other fields with valid data.<br>4. Click 'Finish' to create the loan product. | The loan product is created successfully with maximum length fields. | medium |
| TC-048 |  | Create a loan product with minimum values for numeric fields | User is logged in, User is on the Loan Products page | 1. Click on '+ Create Loan Product' button.<br>2. Fill in all required fields in Step 1 with valid data.<br>3. In Step 2, set Principal Amount to minimum value.<br>4. In Step 4, set Number of Repayments to minimum value.<br>5. Click 'Finish' to create the loan product. | The loan product is created successfully with minimum values for numeric fields. | medium |

---

## Savings Products

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-050 |  | Create Savings Product with all valid inputs | User is logged in, User is on the Savings Products page | 1. Click on '+ Create Savings Product' button.<br>2. Fill in all required fields in Step 1 (Details) with valid data.<br>3. Proceed to Step 2 (Currency) and select valid currency and decimal places.<br>4. Proceed to Step 3 (Terms) and fill in all fields with valid data.<br>5. Proceed to Step 4 (Settings) and fill in all fields with valid data.<br>6. Proceed to Step 5 (Charges) and add predefined charges.<br>7. Proceed to Step 6 (Accounting) and select Cash-based with valid GL account mappings.<br>8. Submit the form. | Savings Product is created successfully and user is redirected to the Savings Products page with a success message. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-051 |  | Create Savings Product with missing required fields | User is logged in, User is on the Savings Products page | 1. Click on '+ Create Savings Product' button.<br>2. Leave Product Name and Short Name fields empty in Step 1 (Details).<br>3. Attempt to proceed to Step 2 (Currency). | Error message is displayed indicating that Product Name and Short Name are required. | high |
| TC-053 |  | Create Savings Product with invalid currency | User is logged in, User is on the Savings Products page | 1. Click on '+ Create Savings Product' button.<br>2. Fill in all required fields in Step 1 (Details) with valid data.<br>3. In Step 2 (Currency), select an invalid currency.<br>4. Attempt to proceed to Step 3 (Terms). | Error message is displayed indicating that the selected currency is invalid. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-052 |  | Create Savings Product with maximum length inputs | User is logged in, User is on the Savings Products page | 1. Click on '+ Create Savings Product' button.<br>2. Fill in Product Name and Short Name with maximum allowed characters.<br>3. Fill in Description with maximum allowed characters.<br>4. Fill in External Id with maximum allowed characters.<br>5. Proceed through all steps with valid maximum length inputs.<br>6. Submit the form. | Savings Product is created successfully with maximum length inputs without any errors. | medium |
| TC-054 |  | Create Savings Product with boundary values for interest rate | User is logged in, User is on the Savings Products page | 1. Click on '+ Create Savings Product' button.<br>2. Fill in all required fields in Step 1 (Details) with valid data.<br>3. In Step 3 (Terms), set Nominal Annual Interest Rate to 0% and 100%.<br>4. Proceed through all steps with valid inputs.<br>5. Submit the form. | Savings Product is created successfully with boundary values for interest rate without any errors. | medium |

---

## Share Products

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-055 |  | Create a new share product with valid details | User is logged in, User is on the Share Products page | 1. Click on the '+ Create Share Product' button.<br>2. Fill in the Product Name, Short Name, and Description in Step 1.<br>3. Proceed to Step 2 and fill in Currency, Decimal Places, and Currency In Multiples Of.<br>4. In Step 3, fill in Total Number of Shares, Shares to be Issued, and Nominal/Unit Price.<br>5. Complete Steps 4, 5, 6, and 7 with valid data.<br>6. Click 'Finish' to create the share product. | The new share product is created successfully and displayed in the data table. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-056 |  | Attempt to create a share product with missing required fields | User is logged in, User is on the Share Products page | 1. Click on the '+ Create Share Product' button.<br>2. Leave the Product Name, Short Name, and Description fields empty in Step 1.<br>3. Attempt to proceed to Step 2. | An error message is displayed indicating that required fields must be filled. | high |
| TC-058 |  | Create a share product with invalid currency format | User is logged in, User is on the Share Products page | 1. Click on the '+ Create Share Product' button.<br>2. Fill in valid Product Name, Short Name, and Description.<br>3. In Step 2, enter an invalid format for Currency.<br>4. Attempt to proceed to Step 3. | An error message is displayed indicating that the currency format is invalid. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-057 |  | Create a share product with maximum length fields | User is logged in, User is on the Share Products page | 1. Click on the '+ Create Share Product' button.<br>2. Fill in the Product Name, Short Name, and Description with maximum allowed characters.<br>3. Proceed through all steps with valid data.<br>4. Click 'Finish' to create the share product. | The new share product is created successfully with maximum length fields and displayed in the data table. | medium |
| TC-059 |  | Create a share product with zero shares | User is logged in, User is on the Share Products page | 1. Click on the '+ Create Share Product' button.<br>2. Fill in valid Product Name, Short Name, and Description.<br>3. In Step 3, enter '0' for Total Number of Shares.<br>4. Fill in other required fields with valid data.<br>5. Click 'Finish' to create the share product. | The share product is created successfully with zero shares and displayed in the data table. | medium |

---

## Charges

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-060 |  | Create a valid charge | User is logged in, User is on the Charges page | 1. Click on the '+ Create Charge' button.<br>2. Fill in the Charge Name with 'Service Fee'.<br>3. Select 'Loan' for Charge Applies To.<br>4. Select 'USD' for Currency.<br>5. Select 'Specified Due Date' for Charge Time Type.<br>6. Select 'Flat' for Charge Calculation Type.<br>7. Enter '100' for Amount.<br>8. Check the 'Is Penalty' checkbox.<br>9. Check the 'Is Active' checkbox.<br>10. Select a Tax Group from the dropdown.<br>11. Select 'Regular' for Payment Mode.<br>12. Click on 'Submit'. | The charge is created successfully, and the user is redirected to the Charges page with a success message. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-061 |  | Create charge without required fields | User is logged in, User is on the Charges page | 1. Click on the '+ Create Charge' button.<br>2. Leave all fields empty.<br>3. Click on 'Submit'. | The system displays error messages indicating that required fields must be filled. | high |
| TC-062 |  | Create charge with invalid amount | User is logged in, User is on the Charges page | 1. Click on the '+ Create Charge' button.<br>2. Fill in the Charge Name with 'Service Fee'.<br>3. Select 'Loan' for Charge Applies To.<br>4. Select 'USD' for Currency.<br>5. Select 'Specified Due Date' for Charge Time Type.<br>6. Select 'Flat' for Charge Calculation Type.<br>7. Enter '-50' for Amount.<br>8. Click on 'Submit'. | The system displays an error message indicating that the amount must be a positive value. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-063 |  | Create charge with maximum length name | User is logged in, User is on the Charges page | 1. Click on the '+ Create Charge' button.<br>2. Fill in the Charge Name with a string of 255 characters.<br>3. Select 'Loan' for Charge Applies To.<br>4. Select 'USD' for Currency.<br>5. Select 'Specified Due Date' for Charge Time Type.<br>6. Select 'Flat' for Charge Calculation Type.<br>7. Enter '100' for Amount.<br>8. Click on 'Submit'. | The charge is created successfully, and the user is redirected to the Charges page. | medium |
| TC-064 |  | Create charge with empty Charge Applies To | User is logged in, User is on the Charges page | 1. Click on the '+ Create Charge' button.<br>2. Fill in the Charge Name with 'Service Fee'.<br>3. Leave Charge Applies To empty.<br>4. Select 'USD' for Currency.<br>5. Select 'Specified Due Date' for Charge Time Type.<br>6. Select 'Flat' for Charge Calculation Type.<br>7. Enter '100' for Amount.<br>8. Click on 'Submit'. | The system displays an error message indicating that Charge Applies To is required. | high |

---

## Floating Rates

Total: **6** (positive: 1, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-065 |  | Create a new floating rate with valid inputs | User is logged in, User is on the Floating Rates page | 1. Click on the '+ Create Floating Rate' button<br>2. Enter a valid Floating Rate Name<br>3. Check the 'Is Base Lending Rate' checkbox<br>4. Check the 'Is Active' checkbox<br>5. Add a row in the Rate Periods table with valid From Date and Interest Rate<br>6. Click 'Save' | The new floating rate is created successfully and displayed in the data table. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-066 |  | Attempt to create a floating rate without a name | User is logged in, User is on the Floating Rates page | 1. Click on the '+ Create Floating Rate' button<br>2. Leave the Floating Rate Name field empty<br>3. Click 'Save' | An error message is displayed indicating that the Floating Rate Name is required. | high |
| TC-067 |  | Attempt to create a second base lending rate | User is logged in, User is on the Floating Rates page, A base lending rate already exists | 1. Click on the '+ Create Floating Rate' button<br>2. Enter a valid Floating Rate Name<br>3. Check the 'Is Base Lending Rate' checkbox<br>4. Click 'Save' | An error message is displayed indicating that only one base lending rate can exist at a time. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-068 |  | Create a floating rate with maximum length name | User is logged in, User is on the Floating Rates page | 1. Click on the '+ Create Floating Rate' button<br>2. Enter a Floating Rate Name with maximum allowed characters<br>3. Check the 'Is Active' checkbox<br>4. Add a row in the Rate Periods table with valid From Date and Interest Rate<br>5. Click 'Save' | The new floating rate is created successfully and displayed in the data table. | medium |
| TC-069 |  | Create a floating rate with an empty Rate Periods table | User is logged in, User is on the Floating Rates page | 1. Click on the '+ Create Floating Rate' button<br>2. Enter a valid Floating Rate Name<br>3. Check the 'Is Base Lending Rate' checkbox<br>4. Check the 'Is Active' checkbox<br>5. Click 'Save' | The floating rate is created successfully without any rate periods, and it is displayed in the data table. | medium |
| TC-070 |  | Create a floating rate with a differential rate | User is logged in, User is on the Floating Rates page | 1. Click on the '+ Create Floating Rate' button<br>2. Enter a valid Floating Rate Name<br>3. Check the 'Is Base Lending Rate' checkbox<br>4. Check the 'Is Active' checkbox<br>5. Add a row in the Rate Periods table with valid From Date, Interest Rate, and check 'Is Differential Rate'<br>6. Click 'Save' | The new floating rate with a differential rate is created successfully and displayed in the data table. | medium |

---

## Delinquency Management

Total: **7** (positive: 2, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-071 |  | Create Delinquency Range with valid inputs | User is logged in, User is on the Delinquency Ranges page | 1. Click on 'Create Delinquency Range'<br>2. Enter 'Classification' as 'Late Payment'<br>3. Enter 'Minimum Age Days' as '30'<br>4. Leave 'Maximum Age Days' blank<br>5. Click 'Submit' | Delinquency Range is created successfully and displayed in the data table. | high |
| TC-074 |  | Create Delinquency Bucket with valid inputs | User is logged in, User is on the Delinquency Buckets page | 1. Click on 'Create Delinquency Bucket'<br>2. Enter 'Bucket Name' as 'High Risk'<br>3. Add delinquency ranges: '1-29 days', '30-59 days', '60+ days'<br>4. Click 'Submit' | Delinquency Bucket is created successfully and displayed in the data table. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-072 |  | Create Delinquency Range with missing required fields | User is logged in, User is on the Delinquency Ranges page | 1. Click on 'Create Delinquency Range'<br>2. Leave 'Classification' blank<br>3. Enter 'Minimum Age Days' as '30'<br>4. Click 'Submit' | Error message is displayed indicating that 'Classification' is required. | high |
| TC-075 |  | Create Delinquency Bucket with missing Bucket Name | User is logged in, User is on the Delinquency Buckets page | 1. Click on 'Create Delinquency Bucket'<br>2. Leave 'Bucket Name' blank<br>3. Click 'Submit' | Error message is displayed indicating that 'Bucket Name' is required. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-073 |  | Create Delinquency Range with maximum length classification | User is logged in, User is on the Delinquency Ranges page | 1. Click on 'Create Delinquency Range'<br>2. Enter 'Classification' as a string of 255 characters<br>3. Enter 'Minimum Age Days' as '1'<br>4. Leave 'Maximum Age Days' blank<br>5. Click 'Submit' | Delinquency Range is created successfully and displayed in the data table. | medium |
| TC-076 |  | Create Delinquency Bucket with maximum length bucket name | User is logged in, User is on the Delinquency Buckets page | 1. Click on 'Create Delinquency Bucket'<br>2. Enter 'Bucket Name' as a string of 255 characters<br>3. Add delinquency ranges: '1-29 days', '30-59 days', '60+ days'<br>4. Click 'Submit' | Delinquency Bucket is created successfully and displayed in the data table. | medium |
| TC-077 |  | Create Delinquency Range with Minimum Age Days as 0 | User is logged in, User is on the Delinquency Ranges page | 1. Click on 'Create Delinquency Range'<br>2. Enter 'Classification' as 'No Payment'<br>3. Enter 'Minimum Age Days' as '0'<br>4. Leave 'Maximum Age Days' blank<br>5. Click 'Submit' | Delinquency Range is created successfully and displayed in the data table. | medium |

---

## Loan Account

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-078 |  | Submit a valid loan application | User is logged in, User is on the Client Detail page | 1. Navigate to the Loan Application form.<br>2. Fill in all required fields with valid data.<br>3. Click on the 'Submit' button. | Loan application is created with status 'Submitted and Pending Approval'. | high |
| TC-083 |  | Approve a loan application | User is logged in as a loan officer, Loan application is in 'Submitted and Pending Approval' status | 1. Navigate to the Loan Detail page of the loan application.<br>2. Click on the 'Approve' button.<br>3. Fill in the approval details.<br>4. Click on the 'Confirm' button. | Loan application status changes to 'Approved'. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-079 |  | Submit loan application with missing required fields | User is logged in, User is on the Client Detail page | 1. Navigate to the Loan Application form.<br>2. Leave required fields empty.<br>3. Click on the 'Submit' button. | Error messages are displayed for the missing required fields. | high |
| TC-081 |  | Submit loan application with invalid interest rate | User is logged in, User is on the Client Detail page | 1. Navigate to the Loan Application form.<br>2. Enter an interest rate below the minimum allowed for the selected product.<br>3. Fill in all other required fields with valid data.<br>4. Click on the 'Submit' button. | Error message is displayed indicating the interest rate is below the minimum allowed. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-080 |  | Submit loan application with maximum principal amount | User is logged in, User is on the Client Detail page | 1. Navigate to the Loan Application form.<br>2. Enter the maximum principal amount allowed for the selected product.<br>3. Fill in all other required fields with valid data.<br>4. Click on the 'Submit' button. | Loan application is created with status 'Submitted and Pending Approval'. | medium |
| TC-082 |  | Submit loan application with empty external ID | User is logged in, User is on the Client Detail page | 1. Navigate to the Loan Application form.<br>2. Fill in all required fields with valid data except for External ID.<br>3. Click on the 'Submit' button. | Loan application is created with status 'Submitted and Pending Approval' despite External ID being empty. | medium |

---

## Savings Account

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-084 |  | Create a new savings account with valid inputs | User is logged in, User is on the Client Detail page | 1. Select a product from the Product Name dropdown.<br>2. Fill in the Field Officer field.<br>3. Select a date in the Submitted On field.<br>4. Enter a valid Nominal Annual Interest Rate.<br>5. Select the Interest Compounding Period.<br>6. Select the Interest Posting Period.<br>7. Select the Interest Calculated Using option.<br>8. Enter a valid Days in Year value.<br>9. Enter a valid Minimum Opening Balance.<br>10. Enter a valid Lock-in Period.<br>11. Check the Allow Overdraft checkbox.<br>12. Click on Submit. | The account is created with status 'Submitted and Pending Approval'. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-085 |  | Attempt to create a savings account with missing required fields | User is logged in, User is on the Client Detail page | 1. Leave the Product Name dropdown unselected.<br>2. Click on Submit. | An error message is displayed indicating that the Product Name is required. | high |
| TC-087 |  | Attempt to withdraw more than available balance without overdraft | User is logged in, User has an active savings account with a balance of $100, User is on the Savings Account Detail page | 1. Click on Withdraw.<br>2. Enter a Transaction Date.<br>3. Enter a Transaction Amount of $150.<br>4. Select Payment Type as Cash.<br>5. Click on Submit. | An error message is displayed indicating that the withdrawal exceeds the available balance. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-086 |  | Create a savings account with maximum length inputs | User is logged in, User is on the Client Detail page | 1. Select a product from the Product Name dropdown.<br>2. Fill in the Field Officer field with maximum allowed characters.<br>3. Select the maximum date in the Submitted On field.<br>4. Enter the maximum valid Nominal Annual Interest Rate.<br>5. Select the maximum length Interest Compounding Period.<br>6. Select the maximum length Interest Posting Period.<br>7. Select the maximum length Interest Calculated Using option.<br>8. Enter the maximum valid Days in Year value.<br>9. Enter the maximum valid Minimum Opening Balance.<br>10. Enter the maximum valid Lock-in Period.<br>11. Check the Allow Overdraft checkbox.<br>12. Click on Submit. | The account is created successfully with status 'Submitted and Pending Approval'. | medium |
| TC-088 |  | Create a savings account with zero as Minimum Opening Balance | User is logged in, User is on the Client Detail page | 1. Select a product from the Product Name dropdown.<br>2. Fill in the Field Officer field.<br>3. Select a date in the Submitted On field.<br>4. Enter a valid Nominal Annual Interest Rate.<br>5. Select the Interest Compounding Period.<br>6. Select the Interest Posting Period.<br>7. Select the Interest Calculated Using option.<br>8. Enter 0 as Minimum Opening Balance.<br>9. Enter a valid Lock-in Period.<br>10. Check the Allow Overdraft checkbox.<br>11. Click on Submit. | The account is created successfully with status 'Submitted and Pending Approval'. | medium |

---

## Share Account

Total: **6** (positive: 1, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-089 |  | Create Share Account with valid inputs | User is logged in, User is on the Client Detail page | 1. Select a valid Share Product from the dropdown.<br>2. Enter a valid Submitted On date.<br>3. Enter a number of Requested Shares within the product's min/max limits.<br>4. Enter a valid Application Date.<br>5. Select a valid Savings Account for Charges from the dropdown.<br>6. Enter a valid External ID.<br>7. Click on the Submit button. | The share account is created with status 'Submitted and Pending Approval'. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-090 |  | Create Share Account with invalid Requested Shares | User is logged in, User is on the Client Detail page | 1. Select a valid Share Product from the dropdown.<br>2. Enter a valid Submitted On date.<br>3. Enter a number of Requested Shares below the product's minimum limit.<br>4. Enter a valid Application Date.<br>5. Select a valid Savings Account for Charges from the dropdown.<br>6. Enter a valid External ID.<br>7. Click on the Submit button. | An error message is displayed indicating that the Requested Shares are below the minimum limit. | high |
| TC-091 |  | Create Share Account with missing required fields | User is logged in, User is on the Client Detail page | 1. Leave the Share Product dropdown unselected.<br>2. Leave the Submitted On date empty.<br>3. Leave the Requested Shares field empty.<br>4. Leave the Application Date empty.<br>5. Leave the Savings Account for Charges dropdown unselected.<br>6. Leave the External ID empty.<br>7. Click on the Submit button. | Error messages are displayed for each missing required field. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-092 |  | Create Share Account with maximum length External ID | User is logged in, User is on the Client Detail page | 1. Select a valid Share Product from the dropdown.<br>2. Enter a valid Submitted On date.<br>3. Enter a number of Requested Shares within the product's min/max limits.<br>4. Enter a valid Application Date.<br>5. Select a valid Savings Account for Charges from the dropdown.<br>6. Enter an External ID with maximum allowed length.<br>7. Click on the Submit button. | The share account is created successfully with the maximum length External ID. | medium |
| TC-093 |  | Create Share Account with boundary values for Requested Shares | User is logged in, User is on the Client Detail page | 1. Select a valid Share Product from the dropdown.<br>2. Enter a valid Submitted On date.<br>3. Enter the minimum number of Requested Shares.<br>4. Enter a valid Application Date.<br>5. Select a valid Savings Account for Charges from the dropdown.<br>6. Enter a valid External ID.<br>7. Click on the Submit button. | The share account is created successfully with the minimum number of Requested Shares. | medium |
| TC-094 |  | Create Share Account with maximum number of Requested Shares | User is logged in, User is on the Client Detail page | 1. Select a valid Share Product from the dropdown.<br>2. Enter a valid Submitted On date.<br>3. Enter the maximum number of Requested Shares.<br>4. Enter a valid Application Date.<br>5. Select a valid Savings Account for Charges from the dropdown.<br>6. Enter a valid External ID.<br>7. Click on the Submit button. | The share account is created successfully with the maximum number of Requested Shares. | medium |

---

## Fixed & Recurring Deposit Accounts

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-095 |  | Create Fixed Deposit with valid inputs | User is logged in, User is on the Client Detail page | 1. Select a Fixed Deposit Product from the dropdown<br>2. Enter a valid Deposit Amount<br>3. Enter a valid Deposit Period<br>4. Select Maturity Instructions<br>5. Click on 'Submit' | FD Account is created successfully and user is redirected to the FD Account Detail page showing the correct details. | high |
| TC-098 |  | Create Recurring Deposit with valid inputs | User is logged in, User is on the Client Detail page | 1. Select a Recurring Deposit Product from the dropdown<br>2. Enter a valid Mandatory Deposit Amount per installment<br>3. Enter a valid Deposit Period<br>4. Select Deposit Frequency<br>5. Enter a valid Expected First Deposit On date<br>6. Click on 'Submit' | RD Account is created successfully and user is redirected to the RD Account Detail page showing the correct details. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-096 |  | Create Fixed Deposit with invalid Deposit Amount | User is logged in, User is on the Client Detail page | 1. Select a Fixed Deposit Product from the dropdown<br>2. Enter an invalid Deposit Amount (e.g., negative value)<br>3. Enter a valid Deposit Period<br>4. Select Maturity Instructions<br>5. Click on 'Submit' | An error message is displayed indicating that the Deposit Amount is invalid. | high |
| TC-099 |  | Create Recurring Deposit with missing Expected First Deposit On date | User is logged in, User is on the Client Detail page | 1. Select a Recurring Deposit Product from the dropdown<br>2. Enter a valid Mandatory Deposit Amount per installment<br>3. Enter a valid Deposit Period<br>4. Select Deposit Frequency<br>5. Leave Expected First Deposit On date empty<br>6. Click on 'Submit' | An error message is displayed indicating that the Expected First Deposit On date is required. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-097 |  | Create Fixed Deposit with maximum length Deposit Amount | User is logged in, User is on the Client Detail page | 1. Select a Fixed Deposit Product from the dropdown<br>2. Enter a maximum length Deposit Amount (e.g., 999999999)<br>3. Enter a valid Deposit Period<br>4. Select Maturity Instructions<br>5. Click on 'Submit' | FD Account is created successfully and user is redirected to the FD Account Detail page showing the correct details. | medium |
| TC-100 |  | Create Recurring Deposit with maximum length Mandatory Deposit Amount | User is logged in, User is on the Client Detail page | 1. Select a Recurring Deposit Product from the dropdown<br>2. Enter a maximum length Mandatory Deposit Amount (e.g., 999999999)<br>3. Enter a valid Deposit Period<br>4. Select Deposit Frequency<br>5. Enter a valid Expected First Deposit On date<br>6. Click on 'Submit' | RD Account is created successfully and user is redirected to the RD Account Detail page showing the correct details. | medium |

---

## Accounting — Chart of Accounts

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-101 |  | Create a new GL Account with valid inputs | User is logged in, User is on the Chart of Accounts page | 1. Click on the '+ Create GL Account' button.<br>2. Fill in the Account Type with 'Assets'.<br>3. Select a Parent Account from the dropdown.<br>4. Enter a unique GL Code.<br>5. Enter a valid Account Name.<br>6. Select 'Detail' for Account Usage.<br>7. Check the 'Manual Entries Allowed' checkbox.<br>8. Enter a Description.<br>9. Select a Tag from the dropdown.<br>10. Click on the 'Save' button. | The new GL Account is created successfully and appears in the Chart of Accounts tree. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-102 |  | Attempt to create a GL Account with a duplicate GL Code | User is logged in, User is on the Chart of Accounts page, A GL Account with the same GL Code already exists | 1. Click on the '+ Create GL Account' button.<br>2. Fill in the Account Type with 'Liabilities'.<br>3. Select a Parent Account from the dropdown.<br>4. Enter the duplicate GL Code.<br>5. Enter a valid Account Name.<br>6. Select 'Header' for Account Usage.<br>7. Click on the 'Save' button. | An error message is displayed indicating that the GL Code must be unique. | high |
| TC-103 |  | Attempt to create a GL Account without required fields | User is logged in, User is on the Chart of Accounts page | 1. Click on the '+ Create GL Account' button.<br>2. Leave the Account Type field empty.<br>3. Click on the 'Save' button. | An error message is displayed indicating that the Account Type is required. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-104 |  | Create a GL Account with maximum length fields | User is logged in, User is on the Chart of Accounts page | 1. Click on the '+ Create GL Account' button.<br>2. Fill in the Account Type with 'Expenses'.<br>3. Select a Parent Account from the dropdown.<br>4. Enter a GL Code with maximum allowed characters.<br>5. Enter an Account Name with maximum allowed characters.<br>6. Select 'Detail' for Account Usage.<br>7. Check the 'Manual Entries Allowed' checkbox.<br>8. Enter a Description with maximum allowed characters.<br>9. Select a Tag from the dropdown.<br>10. Click on the 'Save' button. | The new GL Account is created successfully with maximum length fields and appears in the Chart of Accounts tree. | medium |
| TC-105 |  | Create a GL Account with empty fields for optional inputs | User is logged in, User is on the Chart of Accounts page | 1. Click on the '+ Create GL Account' button.<br>2. Fill in the Account Type with 'Assets'.<br>3. Select a Parent Account from the dropdown.<br>4. Enter a unique GL Code.<br>5. Enter a valid Account Name.<br>6. Select 'Header' for Account Usage.<br>7. Leave the Description field empty.<br>8. Leave the Tag dropdown unselected.<br>9. Click on the 'Save' button. | The new GL Account is created successfully with optional fields left empty and appears in the Chart of Accounts tree. | medium |

---

## Accounting — Journal Entries & Closures

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-106 |  | Successfully add a journal entry with valid data | User is logged in, User is on the Journal Entries page | 1. Click on the '+ Add Journal Entry' button.<br>2. Fill in the required fields: Office, Currency, Transaction Date.<br>3. Add at least one entry line with GL Account and Amount.<br>4. Click on the 'Submit' button. | The journal entry is successfully added, and the user is redirected to the Journal Entries page with a success message. | high |
| TC-109 |  | Successfully create a closure with valid data | User is logged in, User is on the Closing Entries page | 1. Click on the '+ Create Closure' button.<br>2. Fill in the required fields: Office, Closing Date.<br>3. Click on the 'Submit' button. | The closure is successfully created, and the user is redirected to the Closing Entries page with a success message. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-107 |  | Fail to add a journal entry with missing required fields | User is logged in, User is on the Journal Entries page | 1. Click on the '+ Add Journal Entry' button.<br>2. Leave the required fields (Office, Currency, Transaction Date) empty.<br>3. Click on the 'Submit' button. | An error message is displayed indicating that required fields must be filled. | high |
| TC-110 |  | Fail to create a closure with missing required fields | User is logged in, User is on the Closing Entries page | 1. Click on the '+ Create Closure' button.<br>2. Leave the required fields (Office, Closing Date) empty.<br>3. Click on the 'Submit' button. | An error message is displayed indicating that required fields must be filled. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-108 |  | Add a journal entry with maximum allowed characters in comments | User is logged in, User is on the Journal Entries page | 1. Click on the '+ Add Journal Entry' button.<br>2. Fill in the required fields: Office, Currency, Transaction Date.<br>3. Add at least one entry line with GL Account and Amount.<br>4. Fill the Comments field with the maximum allowed characters.<br>5. Click on the 'Submit' button. | The journal entry is successfully added, and the user is redirected to the Journal Entries page. | medium |
| TC-111 |  | Create a closure with a closing date set to today | User is logged in, User is on the Closing Entries page | 1. Click on the '+ Create Closure' button.<br>2. Fill in the required fields: Office, Closing Date (set to today's date).<br>3. Click on the 'Submit' button. | The closure is successfully created, and the user is redirected to the Closing Entries page. | medium |

---

## Accounting Rules & Financial Activity Mappings

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-112 |  | Create a new accounting rule successfully | User is logged in, User is on the Accounting Rules page | 1. Click on the '+ Create Rule' button<br>2. Select an Office from the dropdown<br>3. Enter a valid Rule Name<br>4. Select one or more Debit Accounts<br>5. Select one or more Credit Accounts<br>6. Click on the 'Save' button | The new accounting rule is created and displayed in the data table | high |
| TC-115 |  | Create a new financial activity mapping successfully | User is logged in, User is on the Financial Activity Mappings page | 1. Click on the '+ Create Mapping' button<br>2. Select a Financial Activity from the dropdown<br>3. Select a GL Account from the dropdown<br>4. Click on the 'Save' button | The new financial activity mapping is created and displayed in the data table | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-113 |  | Attempt to create a rule without a Rule Name | User is logged in, User is on the Accounting Rules page | 1. Click on the '+ Create Rule' button<br>2. Select an Office from the dropdown<br>3. Leave the Rule Name field empty<br>4. Select one or more Debit Accounts<br>5. Select one or more Credit Accounts<br>6. Click on the 'Save' button | An error message is displayed indicating that the Rule Name is required | high |
| TC-116 |  | Attempt to create a mapping for an already mapped financial activity | User is logged in, User is on the Financial Activity Mappings page, A mapping already exists for the selected financial activity | 1. Click on the '+ Create Mapping' button<br>2. Select the already mapped Financial Activity from the dropdown<br>3. Select a GL Account from the dropdown<br>4. Click on the 'Save' button | An error message is displayed indicating that the financial activity is already mapped | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-114 |  | Create a rule with maximum length Rule Name | User is logged in, User is on the Accounting Rules page | 1. Click on the '+ Create Rule' button<br>2. Select an Office from the dropdown<br>3. Enter a Rule Name with maximum allowed characters<br>4. Select one or more Debit Accounts<br>5. Select one or more Credit Accounts<br>6. Click on the 'Save' button | The new accounting rule is created successfully and displayed in the data table | medium |
| TC-117 |  | Create a mapping with maximum length GL Account | User is logged in, User is on the Financial Activity Mappings page | 1. Click on the '+ Create Mapping' button<br>2. Select a Financial Activity from the dropdown<br>3. Select a GL Account with maximum allowed characters<br>4. Click on the 'Save' button | The new financial activity mapping is created successfully and displayed in the data table | medium |

---

## Provisioning

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-118 |  | Create Provisioning Criteria with valid inputs | User is logged in, User is on the Provisioning Criteria page | 1. Click on the '+ Create' button<br>2. Enter a valid Criteria Name<br>3. Add a row in the Definitions table with valid Loan Product, Category, Minimum Age, Maximum Age, Provisioning Percentage, Liability Account, and Expense Account<br>4. Click on the 'Save' button | The new provisioning criteria is saved successfully and displayed in the data table. | high |
| TC-123 |  | Review a Provisioning Entry | User is logged in, User is on the Provisioning Entries page, At least one provisioning entry exists | 1. Click on the review button for an existing provisioning entry | The detailed breakdown of the selected provisioning entry is displayed. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-119 |  | Attempt to create Provisioning Criteria without Criteria Name | User is logged in, User is on the Provisioning Criteria page | 1. Click on the '+ Create' button<br>2. Leave the Criteria Name field empty<br>3. Add a row in the Definitions table with valid inputs<br>4. Click on the 'Save' button | An error message is displayed indicating that the Criteria Name is required. | high |
| TC-121 |  | Create Provisioning Entry with no criteria defined | User is logged in, User is on the Provisioning Entries page | 1. Click on the '+ Create Provisioning Entry' button | An error message is displayed indicating that no provisioning criteria are defined. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-120 |  | Create Provisioning Criteria with maximum length Criteria Name | User is logged in, User is on the Provisioning Criteria page | 1. Click on the '+ Create' button<br>2. Enter a Criteria Name with maximum allowed characters<br>3. Add a row in the Definitions table with valid inputs<br>4. Click on the 'Save' button | The new provisioning criteria is saved successfully and displayed in the data table. | medium |
| TC-122 |  | Create Provisioning Entry with maximum number of criteria | User is logged in, User has defined the maximum number of provisioning criteria | 1. Click on the '+ Create Provisioning Entry' button | The system processes the entries and displays the journal entries correctly. | medium |

---

## Offices

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-124 |  | Create Office with valid inputs | User is logged in, User is on the Offices page | 1. Click on the '+ Create Office' button.<br>2. Fill in the Office Name with a valid name.<br>3. Select a Parent Office from the dropdown.<br>4. Enter a valid Opening Date.<br>5. Optionally, enter a valid External ID.<br>6. Click on the 'Save' button. | A new office is created, and the user is redirected to the Offices page with the new office listed. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-125 |  | Create Office with missing required fields | User is logged in, User is on the Offices page | 1. Click on the '+ Create Office' button.<br>2. Leave the Office Name field empty.<br>3. Leave the Parent Office field empty.<br>4. Leave the Opening Date field empty.<br>5. Click on the 'Save' button. | An error message is displayed indicating that all required fields must be filled. | high |
| TC-127 |  | Create Office with invalid Opening Date | User is logged in, User is on the Offices page | 1. Click on the '+ Create Office' button.<br>2. Fill in the Office Name with a valid name.<br>3. Select a Parent Office from the dropdown.<br>4. Enter an invalid Opening Date (e.g., future date).<br>5. Optionally, enter a valid External ID.<br>6. Click on the 'Save' button. | An error message is displayed indicating that the Opening Date is invalid. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-126 |  | Create Office with maximum length Office Name | User is logged in, User is on the Offices page | 1. Click on the '+ Create Office' button.<br>2. Fill in the Office Name with a string of maximum allowed length.<br>3. Select a Parent Office from the dropdown.<br>4. Enter a valid Opening Date.<br>5. Optionally, enter a valid External ID.<br>6. Click on the 'Save' button. | A new office is created successfully, and the user is redirected to the Offices page with the new office listed. | medium |
| TC-128 |  | Create Office with special characters in Office Name | User is logged in, User is on the Offices page | 1. Click on the '+ Create Office' button.<br>2. Fill in the Office Name with special characters (e.g., @#$%^&*).<br>3. Select a Parent Office from the dropdown.<br>4. Enter a valid Opening Date.<br>5. Optionally, enter a valid External ID.<br>6. Click on the 'Save' button. | An error message is displayed indicating that the Office Name contains invalid characters. | medium |

---

## Employees

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-129 |  | Create Employee with valid data | User is logged in, User is on the Employees page | 1. Click on '+ Create Employee' button<br>2. Fill in all required fields with valid data<br>3. Click 'Save' button | Employee is created successfully and appears in the Employees data table | high |
| TC-134 |  | Edit Employee details | User is logged in, User is on the Employees page, At least one employee exists | 1. Click on the Name link of an existing employee<br>2. Click on 'Edit' option<br>3. Modify some details<br>4. Click 'Save' button | Employee details are updated successfully and reflected in the Employees data table | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-130 |  | Create Employee without required fields | User is logged in, User is on the Employees page | 1. Click on '+ Create Employee' button<br>2. Leave required fields (Office, First Name, Last Name) empty<br>3. Click 'Save' button | Error messages are displayed for the empty required fields | high |
| TC-132 |  | Create Employee with invalid mobile number | User is logged in, User is on the Employees page | 1. Click on '+ Create Employee' button<br>2. Fill in all required fields with valid data<br>3. Enter an invalid mobile number format<br>4. Click 'Save' button | Error message is displayed for the invalid mobile number | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-131 |  | Create Employee with maximum length fields | User is logged in, User is on the Employees page | 1. Click on '+ Create Employee' button<br>2. Fill in all fields with maximum allowed characters<br>3. Click 'Save' button | Employee is created successfully and appears in the Employees data table | medium |
| TC-133 |  | Create Employee with empty optional fields | User is logged in, User is on the Employees page | 1. Click on '+ Create Employee' button<br>2. Fill in required fields only<br>3. Click 'Save' button | Employee is created successfully with optional fields left empty | low |

---

## Teller & Cashier Management

Total: **9** (positive: 3, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-135 |  | Create a new teller with valid inputs | User is logged in as a manager or admin | 1. Navigate to the Tellers page.<br>2. Click on the '+ Create Teller' button.<br>3. Fill in the required fields: Office, Teller Name, Start Date.<br>4. Click on the 'Save' button. | A new teller is created, and the user is redirected to the Tellers page where the new teller is listed. | high |
| TC-138 |  | Allocate a cashier with valid inputs | User is logged in as a manager or admin, At least one teller exists | 1. Navigate to the Tellers page.<br>2. Click on a Teller Name to view details.<br>3. Click on the '+ Allocate Cashier' button.<br>4. Fill in the required fields: Staff, Start Date.<br>5. Click on the 'Allocate' button. | A new cashier is allocated, and the user is redirected to the Teller Detail page where the new cashier is listed. | high |
| TC-141 |  | Settle cash with valid inputs | User is logged in as a manager or admin, At least one cashier exists | 1. Navigate to the Cashier Detail page.<br>2. Click on the 'Settle Cash' button.<br>3. Fill in the Amount, Currency, and Transaction Date fields.<br>4. Click on the 'Submit' button. | The cash is settled successfully, and the Cashier Transactions list is updated. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-136 |  | Attempt to create a teller without required fields | User is logged in as a manager or admin | 1. Navigate to the Tellers page.<br>2. Click on the '+ Create Teller' button.<br>3. Leave the required fields (Office, Teller Name, Start Date) empty.<br>4. Click on the 'Save' button. | An error message is displayed indicating that required fields must be filled. | high |
| TC-139 |  | Attempt to allocate a cashier without required fields | User is logged in as a manager or admin, At least one teller exists | 1. Navigate to the Tellers page.<br>2. Click on a Teller Name to view details.<br>3. Click on the '+ Allocate Cashier' button.<br>4. Leave the required fields (Staff, Start Date) empty.<br>5. Click on the 'Allocate' button. | An error message is displayed indicating that required fields must be filled. | high |
| TC-142 |  | Attempt to settle cash without required fields | User is logged in as a manager or admin, At least one cashier exists | 1. Navigate to the Cashier Detail page.<br>2. Click on the 'Settle Cash' button.<br>3. Leave the required fields (Amount, Currency, Transaction Date) empty.<br>4. Click on the 'Submit' button. | An error message is displayed indicating that required fields must be filled. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-137 |  | Create a teller with maximum length name | User is logged in as a manager or admin | 1. Navigate to the Tellers page.<br>2. Click on the '+ Create Teller' button.<br>3. Fill in the Office with a valid entry.<br>4. Enter a Teller Name with the maximum allowed characters.<br>5. Fill in a valid Start Date.<br>6. Click on the 'Save' button. | A new teller is created successfully, and the user is redirected to the Tellers page. | medium |
| TC-140 |  | Allocate a cashier with maximum length staff name | User is logged in as a manager or admin, At least one teller exists | 1. Navigate to the Tellers page.<br>2. Click on a Teller Name to view details.<br>3. Click on the '+ Allocate Cashier' button.<br>4. Enter a Staff name with the maximum allowed characters.<br>5. Fill in a valid Start Date.<br>6. Click on the 'Allocate' button. | A new cashier is allocated successfully, and the user is redirected to the Teller Detail page. | medium |
| TC-143 |  | Settle cash with maximum amount | User is logged in as a manager or admin, At least one cashier exists | 1. Navigate to the Cashier Detail page.<br>2. Click on the 'Settle Cash' button.<br>3. Fill in the Amount with the maximum allowed value.<br>4. Fill in a valid Currency and Transaction Date.<br>5. Click on the 'Submit' button. | The cash is settled successfully, and the Cashier Transactions list is updated. | medium |

---

## Users & Roles

Total: **10** (positive: 2, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-144 |  | Create a new user with valid details | User is logged in with appropriate permissions | 1. Click on the '+ Create User' button.<br>2. Fill in the Username, First Name, Last Name, Email, Office, Password, and Repeat Password fields with valid data.<br>3. Select roles from the Roles multi-select checkboxes.<br>4. Click on the 'Submit' button. | The user is created successfully, and a confirmation message is displayed. | high |
| TC-151 |  | Create a role with valid details | User is logged in with appropriate permissions | 1. Click on the '+ Create Role' button.<br>2. Fill in the Role Name and Description fields with valid data.<br>3. Click on the 'Submit' button. | The role is created successfully, and a confirmation message is displayed. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-145 |  | Attempt to create a user with a duplicate username | User is logged in with appropriate permissions, A user with the same username already exists | 1. Click on the '+ Create User' button.<br>2. Fill in the Username field with the existing username.<br>3. Fill in the other required fields with valid data.<br>4. Click on the 'Submit' button. | An error message is displayed indicating that the username must be unique. | high |
| TC-146 |  | Create a user without filling required fields | User is logged in with appropriate permissions | 1. Click on the '+ Create User' button.<br>2. Leave all required fields empty.<br>3. Click on the 'Submit' button. | Error messages are displayed for all required fields indicating they must be filled. | high |
| TC-149 |  | Create a user with mismatched passwords | User is logged in with appropriate permissions | 1. Click on the '+ Create User' button.<br>2. Fill in all required fields with valid data.<br>3. Enter a different value in the Repeat Password field.<br>4. Click on the 'Submit' button. | An error message is displayed indicating that the passwords do not match. | high |
| TC-152 |  | Create a role without filling required fields | User is logged in with appropriate permissions | 1. Click on the '+ Create Role' button.<br>2. Leave all required fields empty.<br>3. Click on the 'Submit' button. | Error messages are displayed for all required fields indicating they must be filled. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-147 |  | Create a user with maximum length username | User is logged in with appropriate permissions | 1. Click on the '+ Create User' button.<br>2. Fill in the Username field with a maximum length valid username.<br>3. Fill in the other required fields with valid data.<br>4. Click on the 'Submit' button. | The user is created successfully, and a confirmation message is displayed. | medium |
| TC-148 |  | Create a user with an invalid email format | User is logged in with appropriate permissions | 1. Click on the '+ Create User' button.<br>2. Fill in the Email field with an invalid email format.<br>3. Fill in the other required fields with valid data.<br>4. Click on the 'Submit' button. | An error message is displayed indicating that the email format is invalid. | high |
| TC-150 |  | Create a user with a very long password | User is logged in with appropriate permissions | 1. Click on the '+ Create User' button.<br>2. Fill in all required fields with valid data.<br>3. Enter a very long password that meets the password policy.<br>4. Enter the same value in the Repeat Password field.<br>5. Click on the 'Submit' button. | The user is created successfully, and a confirmation message is displayed. | medium |
| TC-153 |  | Create a role with maximum length name | User is logged in with appropriate permissions | 1. Click on the '+ Create Role' button.<br>2. Fill in the Role Name field with a maximum length valid name.<br>3. Fill in the Description field with valid data.<br>4. Click on the 'Submit' button. | The role is created successfully, and a confirmation message is displayed. | medium |

---

## Reports

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-154 |  | Generate report with valid parameters | User is logged in, User is on the Reports page | 1. Click on a report name (e.g., Loans Awaiting Disbursal)<br>2. Fill in all required fields with valid data<br>3. Click on 'Run Report' button | The report is generated and displayed as a data table with sorting and pagination options. | high |
| TC-159 |  | Export report to PDF | User is logged in, User has generated a report | 1. Click on the 'Export' button<br>2. Select 'PDF' from the output options<br>3. Confirm the export | The report is successfully exported as a PDF file. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-155 |  | Attempt to generate report with missing required fields | User is logged in, User is on the Reports page | 1. Click on a report name (e.g., Active Loans Summary)<br>2. Leave required fields empty<br>3. Click on 'Run Report' button | An error message is displayed indicating that required fields must be filled. | high |
| TC-157 |  | Generate report with invalid date range | User is logged in, User is on the Reports page | 1. Click on a report name (e.g., Loans Pending Approval)<br>2. Set the start date to a later date than the end date<br>3. Click on 'Run Report' button | An error message is displayed indicating that the date range is invalid. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-156 |  | Generate report with maximum length input | User is logged in, User is on the Reports page | 1. Click on a report name (e.g., Portfolio at Risk)<br>2. Fill in fields with maximum allowed character length<br>3. Click on 'Run Report' button | The report is generated successfully without any errors. | medium |
| TC-158 |  | Generate report with empty fields | User is logged in, User is on the Reports page | 1. Click on a report name (e.g., Active Loans Details)<br>2. Leave all fields empty<br>3. Click on 'Run Report' button | An error message is displayed indicating that at least one field must be filled. | medium |

---

## Account Transfers & Standing Instructions

Total: **9** (positive: 2, negative: 4, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-160 |  | Successful account transfer | User is logged in, User has sufficient balance | 1. Navigate to Account Transfers form<br>2. Fill in all required fields with valid data<br>3. Click on 'Submit' | Transfer is processed successfully, and a confirmation message is displayed. | high |
| TC-165 |  | Create standing instruction successfully | User is logged in | 1. Navigate to Standing Instructions page<br>2. Click on '+ Create Standing Instruction'<br>3. Fill in all required fields with valid data<br>4. Click on 'Submit' | Standing instruction is created successfully, and it appears in the listing. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-161 |  | Transfer amount exceeds available balance | User is logged in, User has insufficient balance | 1. Navigate to Account Transfers form<br>2. Fill in all required fields with valid data but set Transfer Amount greater than available balance<br>3. Click on 'Submit' | An error message is displayed indicating insufficient funds. | high |
| TC-162 |  | Missing required transfer amount | User is logged in | 1. Navigate to Account Transfers form<br>2. Fill in all fields except Transfer Amount<br>3. Click on 'Submit' | An error message is displayed indicating that Transfer Amount is required. | high |
| TC-166 |  | Missing required fields in standing instruction | User is logged in | 1. Navigate to Standing Instructions page<br>2. Click on '+ Create Standing Instruction'<br>3. Fill in all fields except Name<br>4. Click on 'Submit' | An error message is displayed indicating that Name is required. | high |
| TC-168 |  | Delete standing instruction | User is logged in, At least one standing instruction exists | 1. Navigate to Standing Instructions page<br>2. Locate an existing standing instruction<br>3. Click on 'Delete' for that instruction<br>4. Confirm deletion | Standing instruction is deleted successfully, and it no longer appears in the listing. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-163 |  | Transfer amount is zero | User is logged in, User has sufficient balance | 1. Navigate to Account Transfers form<br>2. Fill in all required fields with valid data and set Transfer Amount to 0<br>3. Click on 'Submit' | An error message is displayed indicating that Transfer Amount must be greater than zero. | medium |
| TC-164 |  | Maximum length of description | User is logged in | 1. Navigate to Account Transfers form<br>2. Fill in all required fields with valid data and set Description to maximum allowed length<br>3. Click on 'Submit' | Transfer is processed successfully, and a confirmation message is displayed. | medium |
| TC-167 |  | Create standing instruction with maximum length name | User is logged in | 1. Navigate to Standing Instructions page<br>2. Click on '+ Create Standing Instruction'<br>3. Fill in all required fields with Name at maximum allowed length<br>4. Click on 'Submit' | Standing instruction is created successfully, and it appears in the listing. | medium |

---

## Tax Management

Total: **5** (positive: 2, negative: 2, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-169 |  | Create a valid Tax Component | User is logged in, User is on the Tax Components page | 1. Click on the '+ Create Tax Component' button.<br>2. Fill in the Name field with 'Sales Tax'.<br>3. Fill in the Percentage field with '10'.<br>4. Select 'Asset' for Debit Account Type.<br>5. Enter a valid GL account for Debit Account.<br>6. Select 'Liability' for Credit Account Type.<br>7. Enter a valid GL account for Credit Account.<br>8. Fill in the Start Date with today's date.<br>9. Click on the 'Save' button. | The Tax Component is created successfully and appears in the data table. | high |
| TC-173 |  | Create a valid Tax Group | User is logged in, User is on the Tax Groups page | 1. Click on the '+ Create Tax Group' button.<br>2. Fill in the Name field with 'Income Tax Group'.<br>3. Add a Tax Component with a valid Start Date and End Date.<br>4. Click on the 'Save' button. | The Tax Group is created successfully and appears in the data table. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-170 |  | Create a Tax Component with missing required fields | User is logged in, User is on the Tax Components page | 1. Click on the '+ Create Tax Component' button.<br>2. Leave the Name field empty.<br>3. Leave the Percentage field empty.<br>4. Click on the 'Save' button. | An error message is displayed indicating that Name and Percentage are required fields. | high |
| TC-172 |  | Create a Tax Component with invalid Percentage | User is logged in, User is on the Tax Components page | 1. Click on the '+ Create Tax Component' button.<br>2. Fill in the Name field with 'Service Tax'.<br>3. Fill in the Percentage field with '110'.<br>4. Select 'Asset' for Debit Account Type.<br>5. Enter a valid GL account for Debit Account.<br>6. Select 'Liability' for Credit Account Type.<br>7. Enter a valid GL account for Credit Account.<br>8. Fill in the Start Date with today's date.<br>9. Click on the 'Save' button. | An error message is displayed indicating that the Percentage must be between 0 and 100. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-171 |  | Create a Tax Component with maximum length Name | User is logged in, User is on the Tax Components page | 1. Click on the '+ Create Tax Component' button.<br>2. Fill in the Name field with a string of 255 characters.<br>3. Fill in the Percentage field with '5'.<br>4. Select 'Expense' for Debit Account Type.<br>5. Enter a valid GL account for Debit Account.<br>6. Select 'Income' for Credit Account Type.<br>7. Enter a valid GL account for Credit Account.<br>8. Fill in the Start Date with today's date.<br>9. Click on the 'Save' button. | The Tax Component is created successfully and appears in the data table. | medium |

---

## Organization Settings

Total: **12** (positive: 4, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-174 |  | Create Holiday with valid inputs | User is logged in as Admin, User is on the Holidays page | 1. Click on the '+ Create Holiday' button.<br>2. Fill in the Name field with 'New Year'.<br>3. Select From Date as '2024-01-01'.<br>4. Select To Date as '2024-01-01'.<br>5. Select Rescheduling Type from the dropdown.<br>6. Fill in the Description field with 'New Year Holiday'.<br>7. Select applicable Offices.<br>8. Click on the 'Save' button. | A new holiday 'New Year' is created and displayed in the Holidays table. | high |
| TC-177 |  | Configure Working Days successfully | User is logged in as Admin, User is on the Working Days page | 1. Check the checkboxes for Monday, Tuesday, and Wednesday.<br>2. Select a Repayment Rescheduling option from the dropdown.<br>3. Click on the 'Save' button. | The selected working days are saved successfully. | medium |
| TC-180 |  | Create Fund with valid inputs | User is logged in as Admin, User is on the Funds page | 1. Click on the 'Create Fund' button.<br>2. Fill in the Fund Name field with 'Emergency Fund'.<br>3. Fill in the External ID field with 'EF123'.<br>4. Click on the 'Save' button. | A new fund 'Emergency Fund' is created and displayed in the Funds table. | high |
| TC-183 |  | Bulk import data successfully | User is logged in as Admin, User is on the Bulk Import page | 1. Click on the 'Download template' button.<br>2. Fill the template with valid data for Clients.<br>3. Click on the 'Upload' button.<br>4. Select the filled template file.<br>5. Click on the 'Submit' button. | The data is imported successfully, and a success message is displayed. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-175 |  | Create Holiday with missing required fields | User is logged in as Admin, User is on the Holidays page | 1. Click on the '+ Create Holiday' button.<br>2. Leave the Name field empty.<br>3. Select From Date as '2024-01-01'.<br>4. Select To Date as '2024-01-01'.<br>5. Click on the 'Save' button. | An error message is displayed indicating that the Name field is required. | high |
| TC-178 |  | Configure Working Days with no days selected | User is logged in as Admin, User is on the Working Days page | 1. Leave all checkboxes unchecked.<br>2. Click on the 'Save' button. | An error message is displayed indicating that at least one working day must be selected. | high |
| TC-181 |  | Create Fund with missing Fund Name | User is logged in as Admin, User is on the Funds page | 1. Click on the 'Create Fund' button.<br>2. Leave the Fund Name field empty.<br>3. Fill in the External ID field with 'EF123'.<br>4. Click on the 'Save' button. | An error message is displayed indicating that the Fund Name is required. | high |
| TC-184 |  | Bulk import with invalid data | User is logged in as Admin, User is on the Bulk Import page | 1. Click on the 'Download template' button.<br>2. Fill the template with invalid data.<br>3. Click on the 'Upload' button.<br>4. Select the filled template file.<br>5. Click on the 'Submit' button. | An error message is displayed indicating that the data is invalid. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-176 |  | Create Holiday with maximum length Name | User is logged in as Admin, User is on the Holidays page | 1. Click on the '+ Create Holiday' button.<br>2. Fill in the Name field with a string of 255 characters.<br>3. Select From Date as '2024-01-01'.<br>4. Select To Date as '2024-01-01'.<br>5. Select Rescheduling Type from the dropdown.<br>6. Fill in the Description field with 'Holiday Description'.<br>7. Select applicable Offices.<br>8. Click on the 'Save' button. | A new holiday with the maximum length Name is created successfully. | medium |
| TC-179 |  | Select all currencies in Currencies page | User is logged in as Admin, User is on the Currencies page | 1. Select all available currencies from the list.<br>2. Click on the 'Save' button. | All selected currencies are saved successfully. | medium |
| TC-182 |  | Create Payment Type with maximum length Name | User is logged in as Admin, User is on the Payment Types page | 1. Click on the '+ Create' button.<br>2. Fill in the Name field with a string of 255 characters.<br>3. Fill in the Description field with 'Payment Type Description'.<br>4. Set Is Cash Payment to true.<br>5. Click on the 'Save' button. | A new payment type with the maximum length Name is created successfully. | medium |
| TC-185 |  | Bulk import with empty file | User is logged in as Admin, User is on the Bulk Import page | 1. Click on the 'Upload' button.<br>2. Select an empty file.<br>3. Click on the 'Submit' button. | An error message is displayed indicating that the file is empty. | medium |

---

## System Administration

Total: **9** (positive: 3, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-186 |  | Activate a scheduled job | User is logged in as an admin, Manage Scheduler Jobs page is open | 1. Locate the job 'Apply Annual Fee' in the table.<br>2. Toggle the 'Is Active' switch to 'On'. | The job 'Apply Annual Fee' is now active and the toggle reflects the change. | high |
| TC-189 |  | Enable a global configuration feature | User is logged in as an admin, Global Configuration page is open | 1. Locate the configuration 'maker-checker'.<br>2. Toggle the 'Enabled' switch to 'On'. | The configuration 'maker-checker' is now enabled. | high |
| TC-192 |  | View audit trails with filters | User is logged in as an admin, Audit Trails page is open | 1. Enter a valid Action Name in the filter.<br>2. Click on 'Apply Filters'. | The audit trails are filtered and display only the relevant actions. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-187 |  | Edit CRON expression with invalid format | User is logged in as an admin, Manage Scheduler Jobs page is open | 1. Locate the job 'Add Accrual Transactions' in the table.<br>2. Click on the edit button for CRON expression.<br>3. Enter an invalid CRON expression 'invalid_cron' and save. | An error message is displayed indicating the CRON expression is invalid. | high |
| TC-190 |  | Attempt to add a code with missing mandatory fields | User is logged in as an admin, Manage Codes page is open | 1. Click on 'Add Code'.<br>2. Leave mandatory fields empty and click 'Save'. | An error message is displayed indicating that mandatory fields cannot be empty. | high |
| TC-193 |  | Search audit trails with invalid date range | User is logged in as an admin, Audit Trails page is open | 1. Enter an invalid date range (e.g., end date before start date).<br>2. Click on 'Apply Filters'. | An error message is displayed indicating the date range is invalid. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-188 |  | Toggle all jobs with global Start/Stop toggle | User is logged in as an admin, Manage Scheduler Jobs page is open | 1. Locate the global Start/Stop toggle.<br>2. Toggle it to 'Stop'. | All scheduled jobs are now inactive, and their 'Is Active' toggles reflect the change. | medium |
| TC-191 |  | Create a data table with maximum length field | User is logged in as an admin, Manage Data Tables page is open | 1. Click on 'Create Data Table'.<br>2. Enter a Data Table Name and set a column with maximum length (e.g., 255 characters).<br>3. Save the data table. | The data table is created successfully with the column having maximum length. | medium |
| TC-194 |  | Toggle a job while it is currently running | User is logged in as an admin, Manage Scheduler Jobs page is open, Job 'Post Interest for Savings' is currently running | 1. Locate the job 'Post Interest for Savings' in the table.<br>2. Attempt to toggle the 'Is Active' switch. | A warning message is displayed indicating that the job cannot be toggled while it is currently running. | medium |

---

## Logout

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-195 |  | Successful logout | User is logged in, User is on any authenticated page | 1. Click on the user profile icon in the top-right corner.<br>2. Select 'Log Out' from the dropdown. | User is redirected to the login page and sees a confirmation message indicating successful logout. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-196 |  | Logout without being logged in | User is not logged in | 1. Attempt to click on the user profile icon in the top-right corner.<br>2. Select 'Log Out' from the dropdown. | User remains on the login page and sees an error message indicating that they are not logged in. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-197 |  | Logout from the login page | User is on the login page | 1. Click on the user profile icon in the top-right corner.<br>2. Select 'Log Out' from the dropdown. | User remains on the login page without any error, as they are already logged out. | low |
| TC-198 |  | Attempt to access authenticated page after logout | User is logged in, User has successfully logged out | 1. Click on the user profile icon in the top-right corner.<br>2. Select 'Log Out' from the dropdown.<br>3. Attempt to navigate to an authenticated page. | User is redirected to the login page and cannot access the authenticated page. | high |

---
