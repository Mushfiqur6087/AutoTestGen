# Mifos Banking System Test Cases — Ground Truth

Source: dataset/ground_truth/Mifos/Mifos.md

## Group Management

### Functional Tests

| TC ID        | Test Case                        | Preconditions                             | Steps                                                                                                  | Expected Result                                                               | Priority |
| ------------ | -------------------------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------- | -------- |
| MF-GROUP-001 | View groups list                 | User logged in                            | 1. Navigate to Groups page                                                                             | Groups list loads with group name, account number, office, staff, and status  | High     |
| MF-GROUP-002 | Create group successfully        | Office exists                             | 1. Click Create Group<br>2. Select office<br>3. Enter group name<br>4. Set submitted date<br>5. Submit | Group is created in pending status                                            | High     |
| MF-GROUP-003 | Activate group                   | Pending group exists                      | 1. Open group detail<br>2. Click Activate<br>3. Set activation date<br>4. Submit                       | Group status changes to Active                                                | High     |
| MF-GROUP-004 | View group details               | Group exists                              | 1. Open a group record                                                                                 | Group profile displays general details, members, accounts, notes, and actions | High     |
| MF-GROUP-005 | Add client members to group      | Active group and active clients exist     | 1. Open group<br>2. Add members<br>3. Select eligible clients<br>4. Submit                             | Selected clients become group members                                         | High     |
| MF-GROUP-006 | Assign staff to group            | Group and staff exist                     | 1. Edit group<br>2. Select staff member<br>3. Submit                                                   | Staff assignment is saved                                                     | Medium   |
| MF-GROUP-007 | Transfer group to another office | Active group and destination office exist | 1. Open group<br>2. Click Transfer<br>3. Select office<br>4. Submit                                    | Group office is updated successfully                                          | Medium   |
| MF-GROUP-008 | Close group                      | Group has no blocking active constraints  | 1. Open active group<br>2. Click Close<br>3. Provide closure details<br>4. Submit                      | Group status changes to Closed                                                | Medium   |

### Negative Tests

| TC ID        | Test Case                                                   | Preconditions                                        | Steps                                                                                    | Expected Result                                              | Priority |
| ------------ | ----------------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------ | -------- |
| MF-GROUP-009 | Create group without office                                 | None                                                 | 1. Open Create Group form<br>2. Leave office empty<br>3. Enter other fields<br>4. Submit | Validation error is shown for office                         | High     |
| MF-GROUP-010 | Create group without group name                             | None                                                 | 1. Open Create Group form<br>2. Leave group name empty<br>3. Submit                      | Validation error is shown for group name                     | High     |
| MF-GROUP-011 | Activate group with invalid activation date                 | Pending group exists                                 | 1. Activate group<br>2. Enter date before submission date<br>3. Submit                   | Validation or business rule prevents activation              | High     |
| MF-GROUP-012 | Add ineligible client to group                              | Client not eligible due to status/office constraints | 1. Add member to group<br>2. Select ineligible client                                    | Selection is blocked or submission fails with proper message | Medium   |
| MF-GROUP-013 | Close group with active dependent accounts blocking closure | Group has active dependent accounts                  | 1. Attempt close action                                                                  | Closure is prevented with business-rule error                | High     |

### Additional Coverage Tests

| TC ID        | Test Case                                              | Preconditions                    | Steps                                                      | Expected Result                                  | Priority |
| ------------ | ------------------------------------------------------ | -------------------------------- | ---------------------------------------------------------- | ------------------------------------------------ | -------- |
| MF-GROUP-014 | Search groups by name                                  | Groups exist                     | 1. Search on Groups page using partial name                | Matching groups are returned                     | Medium   |
| MF-GROUP-015 | Remove member from group                               | Active group with members exists | 1. Open group members tab<br>2. Remove member<br>3. Submit | Member is removed according to business rules    | Medium   |
| MF-GROUP-016 | Reject pending group application                       | Pending group exists             | 1. Open group<br>2. Click Reject<br>3. Submit              | Group status changes to Rejected                 | Medium   |
| MF-GROUP-017 | Withdraw pending group application                     | Pending group exists             | 1. Open group<br>2. Click Withdraw<br>3. Submit            | Group status changes to Withdrawn                | Medium   |
| MF-GROUP-018 | Group notes can be added and displayed chronologically | Group exists                     | 1. Add note to group                                       | Note is persisted and displayed in notes section | Low      |
