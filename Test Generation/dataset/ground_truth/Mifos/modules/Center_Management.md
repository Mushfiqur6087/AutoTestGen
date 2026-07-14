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
| MF-CENTER-005 | Add groups to center       | Active center and eligible groups exist    | 1. Open center<br>2. Add groups<br>3. Select groups<br>4. Submit                                          | Groups are associated with the center                    | Medium   |
| MF-CENTER-006 | Assign staff to center     | Center and staff exist                     | 1. Edit center<br>2. Select staff<br>3. Submit                                                            | Staff assignment is saved                                | Medium   |
| MF-CENTER-007 | Transfer center            | Active center and destination office exist | 1. Open center<br>2. Click Transfer<br>3. Select destination office<br>4. Submit                          | Center is transferred successfully                       | Medium   |
| MF-CENTER-008 | Close center               | Center eligible for closure                | 1. Open center<br>2. Click Close<br>3. Submit with closure details                                        | Center status changes to Closed                          | Medium   |

### Negative Tests

| TC ID         | Test Case                                         | Preconditions                                      | Steps                                                | Expected Result                                   | Priority |
| ------------- | ------------------------------------------------- | -------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------- | -------- |
| MF-CENTER-009 | Create center without office                      | None                                               | 1. Leave office empty in create form<br>2. Submit    | Validation error shown for office                 | High     |
| MF-CENTER-010 | Create center without center name                 | None                                               | 1. Leave name empty<br>2. Submit                     | Validation error shown for center name            | High     |
| MF-CENTER-011 | Activate center using date before submission date | Pending center exists                              | 1. Enter invalid activation date<br>2. Submit        | Activation is prevented                           | High     |
| MF-CENTER-012 | Add ineligible group to center                    | Group does not meet eligibility rules              | 1. Add group to center<br>2. Select ineligible group | Operation is blocked or fails with proper message | Medium   |
| MF-CENTER-013 | Close center with active dependencies             | Center has active linked entities blocking closure | 1. Attempt closure                                   | Closure is rejected by business rule              | High     |

### Additional Coverage Tests

| TC ID         | Test Case                           | Preconditions                           | Steps                                                 | Expected Result                              | Priority |
| ------------- | ----------------------------------- | --------------------------------------- | ----------------------------------------------------- | -------------------------------------------- | -------- |
| MF-CENTER-014 | Search centers by name              | Centers exist                           | 1. Search centers page                                | Matching centers are listed                  | Medium   |
| MF-CENTER-015 | Reject pending center application   | Pending center exists                   | 1. Open center<br>2. Reject application               | Center status changes to Rejected            | Medium   |
| MF-CENTER-016 | Withdraw pending center application | Pending center exists                   | 1. Open center<br>2. Withdraw application             | Center status changes to Withdrawn           | Medium   |
| MF-CENTER-017 | Remove group from center            | Active center with linked groups exists | 1. Open center<br>2. Remove linked group<br>3. Submit | Group is removed according to business rules | Medium   |
| MF-CENTER-018 | Add center notes                    | Center exists                           | 1. Open notes section<br>2. Add note                  | Note is saved and displayed                  | Low      |
