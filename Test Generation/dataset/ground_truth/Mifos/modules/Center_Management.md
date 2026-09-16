# Mifos Banking System Test Cases — Ground Truth

Source: dataset/ground_truth/Mifos/Mifos.md

## Center Management

### Functional Tests

| TC ID         | Test Case                  | Preconditions                              | Steps                                                                                                     | Expected Result                                          | Priority |
| ------------- | -------------------------- | ------------------------------------------ | --------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | -------- |
| MF-CENTER-001 | View centers list          | User logged in                             | 1. Navigate to Centers page                                                                               | Centers list loads with center information               | High     |
| MF-CENTER-002 | Create center successfully | Office exists                              | 1. Click Create Center<br>2. Select office<br>3. Enter center name<br>4. Set submission data<br>5. Submit | Center is created in pending state                       | High     |
| MF-CENTER-003 | Activate center            | Pending center exists                      | 1. Open center detail<br>2. Click Activate<br>3. Enter activation date<br>4. Submit                       | Center becomes Active                                    | High     |
| MF-CENTER-004 | View center detail         | Center exists                              | 1. Open center                                                                                            | Center profile shows details, groups, staff, and actions | High     |
| MF-CENTER-005 | View existing group associations in Edit Center form | Center exists with linked groups | 1. Open center detail<br>2. Click Edit action button | Edit Center form opens pre-populated with the center's current Name, Office, Staff, External Id, Submitted On, and selected Groups | Medium   |
| MF-CENTER-006 | Assign staff to center     | Center and staff exist                     | 1. Edit center<br>2. Select staff<br>3. Submit                                                            | Staff assignment is saved                                | Medium   |
| MF-CENTER-007 | Transfer center            | Active center and destination office exist | 1. Open center<br>2. Click Transfer<br>3. Select destination office<br>4. Submit                          | Center is transferred successfully                       | Medium   |
| MF-CENTER-008 | Close center               | Center eligible for closure                | 1. Open center<br>2. Click Close<br>3. Submit with closure details                                        | Center status changes to Closed                          | Medium   |

### Negative Tests

| TC ID         | Test Case                                         | Preconditions                                      | Steps                                                | Expected Result                                   | Priority |
| ------------- | ------------------------------------------------- | -------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------- | -------- |
| MF-CENTER-009 | Create center without office                      | None                                               | 1. Leave office empty in create form<br>2. Submit    | Validation error shown for office                 | High     |
| MF-CENTER-010 | Create center without center name                 | None                                               | 1. Leave name empty<br>2. Submit                     | Validation error shown for center name            | High     |
| MF-CENTER-011 | Activate center using date before submission date | Pending center exists                              | 1. Enter invalid activation date<br>2. Submit        | Activation is prevented                           | High     |
| MF-CENTER-012 | Create Center blocked when no Office exists in system | No Offices exist in the system | 1. Ensure zero Offices are available for selection<br>2. Navigate to Centers page<br>3. Attempt to click Create Center | Create Center control is disabled or not visible; if clicking is possible, the form shows no selectable Office and cannot be submitted; no center is created | Medium   |
| MF-CENTER-013 | Unauthenticated user cannot access Centers page   | User is not authenticated                          | 1. Ensure the user session is logged out<br>2. Attempt to navigate to the Centers page via the Institution menu or direct URL | User is redirected to the login page or shown an authentication-required UI; the Centers list is not displayed | High     |

### Additional Coverage Tests

| TC ID         | Test Case                           | Preconditions                           | Steps                                                 | Expected Result                              | Priority |
| ------------- | ----------------------------------- | --------------------------------------- | ----------------------------------------------------- | -------------------------------------------- | -------- |
| MF-CENTER-014 | Download Centers import template from Import Center dialog | Centers page is accessible | 1. Navigate to Centers page<br>2. Click Import Center button to open the Bulk Import Centers dialog<br>3. Click Download Template button | The centers import template file is downloaded by the browser | Medium   |
| MF-CENTER-015 | Import centers via file upload (happy path) | A valid centers import file is available | 1. Navigate to Centers page<br>2. Click Import Center button<br>3. Upload valid centers import file<br>4. Click Import button | Success notification is displayed confirming the import and the Centers table shows rows for the imported centers | Medium   |
| MF-CENTER-016 | Bulk Import Centers blocked when File upload left blank | None | 1. Navigate to Centers page<br>2. Click Import Center button<br>3. Leave File upload blank<br>4. Click Import button | Inline validation error appears on the File field indicating it is required; the import does not proceed and no centers are imported | Medium   |
| MF-CENTER-017 | View Group detail from Center's Groups tab | Center has at least one Group member | 1. Open center detail<br>2. Click Groups tab<br>3. Click View Group action for target group | Group Detail page opens showing the group's title and member list | Medium   |
| MF-CENTER-018 | Generate Collection Sheet from Center's Calendar/Meeting tab | Center has one or more Groups with clients and account data | 1. Open center detail<br>2. Click Calendar/Meeting tab<br>3. Click Generate Collection Sheet button | Collection sheet is displayed showing all groups and their clients with loan repayment and savings deposit amounts for batch data entry | Low      |
