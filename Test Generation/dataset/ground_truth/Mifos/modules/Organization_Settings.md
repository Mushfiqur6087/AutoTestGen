# Mifos Banking System Test Cases — Ground Truth

Source: dataset/ground_truth/Mifos/Mifos.md

## Organization Settings

### Functional Tests

| TC ID      | Test Case                          | Preconditions                    | Steps                                                                                 | Expected Result                              | Priority |
| ---------- | ---------------------------------- | -------------------------------- | ------------------------------------------------------------------------------------- | -------------------------------------------- | -------- |
| MF-ORG-001 | View organization settings modules | User with admin permission       | 1. Navigate to Organization settings area                                             | Available configuration pages are displayed  | High     |
| MF-ORG-002 | Configure working days             | Organization settings accessible | 1. Open Working Days<br>2. Set business days and repayment reschedule rule<br>3. Save | Working day settings are saved successfully  | High     |
| MF-ORG-003 | Configure holidays                 | Organization settings accessible | 1. Open Holidays<br>2. Create holiday with office/date details<br>3. Save             | Holiday is created and visible in list       | High     |
| MF-ORG-004 | Configure currency settings        | Settings accessible              | 1. Open currency/configuration module<br>2. Update allowed settings<br>3. Save        | Currency-related settings are saved          | Medium   |
| MF-ORG-005 | Bulk Import - Download template for Clients | User logged in as Administrator, Organization context configured | 1. Navigate to Admin > Organization Settings and open the Bulk Import page<br>2. Under Clients, click the 'Download template' button | A file download is triggered in the browser for the Clients import template | Medium   |
| MF-ORG-006 | Manage payment types               | Payment types accessible         | 1. Open payment types<br>2. Create or edit payment type<br>3. Save                    | Payment type changes are saved               | Medium   |
| MF-ORG-007 | Configure fund definitions         | Fund configuration accessible    | 1. Open funds<br>2. Create/edit fund<br>3. Save                                       | Fund definition is saved                     | Medium   |
| MF-ORG-008 | Bulk Import - Upload Clients file and start import | User logged in as Administrator, Organization context configured, a valid Clients import file is available | 1. Navigate to Admin > Organization Settings and open the Bulk Import page<br>2. Under Clients, click the Upload/File control<br>3. Select valid Clients import file in the file chooser<br>4. Click the button to start the upload/import | A success notification is displayed confirming the Clients file was uploaded and the import has started | Medium   |

### Negative Tests

| TC ID      | Test Case                                         | Preconditions              | Steps                                              | Expected Result                           | Priority |
| ---------- | ------------------------------------------------- | -------------------------- | -------------------------------------------------- | ----------------------------------------- | -------- |
| MF-ORG-010 | Create holiday with invalid date range            | Settings accessible        | 1. Enter invalid holiday period<br>2. Save         | Validation error shown                    | High     |
| MF-ORG-011 | Unauthenticated user cannot access Organization Settings | User is not authenticated | 1. Open the application in a browser<br>2. Navigate to the Admin > Organization Settings URL directly | Access is blocked; user is redirected to the login page or shown a login prompt; Organization Settings content is not visible | High     |
| MF-ORG-012 | Bulk Import (Clients) - attempt Upload without selecting a file | Administrator logged in with existing organization context | 1. Navigate to Admin > Organization Settings > Bulk Import<br>2. In the Clients group, click the Upload control without choosing a file<br>3. Click the action that starts the upload/import | Upload is blocked; import does not start; Clients Upload/File field displays an inline validation error indicating a file must be selected | High     |

### Additional Coverage Tests

| TC ID      | Test Case                                                                  | Preconditions                                          | Steps                                                    | Expected Result                                                               | Priority |
| ---------- | -------------------------------------------------------------------------- | ------------------------------------------------------ | -------------------------------------------------------- | ----------------------------------------------------------------------------- | -------- |
| MF-ORG-014 | Create Fund button blocked when organization context is not configured | Administrator logged in without an existing organization context configured | 1. Navigate to Admin > Organization Settings > Funds<br>2. Observe the top actions area where 'Create Fund' would appear<br>3. Attempt to click 'Create Fund' if visible | Create Fund action is not available; the button is either not visible or disabled and cannot be opened; no fund can be created | High     |
| MF-ORG-015 | Non-administrative user does not see Admin menu / Organization Settings link | Authenticated non-administrative user | 1. Login as a non-administrative user<br>2. Observe the top navigation | Admin menu is not present in the top navigation; the 'Organization Settings' link is not visible to the user | High     |
| MF-ORG-016 | Create Holiday - submit with all required fields empty | Administrator logged in with existing organization context | 1. Navigate to Admin > Organization Settings > Holidays<br>2. Click the '+ Create Holiday' button<br>3. Leave the Name field blank<br>4. Leave the From Date field blank<br>5. Leave the To Date field blank<br>6. Click Save | Form does not submit; holiday is not created; inline validation errors appear on the Name, From Date, and To Date fields indicating they are required | High     |
| MF-ORG-017 | Create Holiday - very long Name input is rejected at boundary | Administrator logged in with existing organization context, Holidays page is visible | 1. Click the '+ Create Holiday' button<br>2. In the Name field enter a very long string (>200 characters)<br>3. Enter a valid From Date<br>4. Enter a valid To Date (on or after the From Date)<br>5. Click Save | Save is blocked; the Name field shows an inline validation error indicating the value exceeds the maximum allowed length | Medium   |
