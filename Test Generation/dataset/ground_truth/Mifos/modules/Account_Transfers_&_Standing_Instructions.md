# Mifos Banking System Test Cases — Ground Truth

Source: dataset/ground_truth/Mifos/Mifos.md

## Account Transfers & Standing Instructions

### Functional Tests

| TC ID      | Test Case                                                       | Preconditions                                           | Steps                                                                                                                                       | Expected Result                                                   | Priority |
| ---------- | --------------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | -------- |
| MF-TRF-001 | Transfer funds between eligible own accounts                    | Client has eligible source and destination accounts     | 1. Open transfer workflow<br>2. Select source and destination accounts<br>3. Enter amount/date<br>4. Submit                                 | Transfer is completed and reflected in both accounts              | High     |
| MF-TRF-002 | Transfer from savings to loan repayment                         | Active savings and loan accounts exist                  | 1. Select savings as source and loan as destination<br>2. Submit transfer                                                                   | Savings is debited and loan repayment transaction is posted       | High     |
| MF-TRF-003 | Transfer between client accounts across supported account types | Eligible account types exist                            | 1. Perform supported transfer                                                                                                               | Transfer succeeds according to supported combinations             | Medium   |
| MF-TRF-004 | Create standing instruction successfully                        | Eligible source/destination accounts exist              | 1. Navigate to Standing Instructions<br>2. Create instruction with frequency, amount/rule, start date, source, and destination<br>3. Submit | Standing instruction is created successfully                      | High     |
| MF-TRF-005 | Execute due standing instruction                                | Active standing instruction exists and due date reached | 1. Trigger scheduled execution or inspect executed run                                                                                      | Transfer posts successfully according to standing instruction     | High     |
| MF-TRF-006 | View standing instructions list                                 | Standing instructions exist                             | 1. Navigate to Standing Instructions                                                                                                        | Standing instruction list displays status and rule details        | Medium   |
| MF-TRF-007 | Disable or delete standing instruction                          | Existing standing instruction exists                    | 1. Open instruction<br>2. Disable/delete                                                                                                    | Instruction status changes accordingly and future execution stops | Medium   |

### Negative Tests

| TC ID      | Test Case                                                                         | Preconditions                                  | Steps                                                                 | Expected Result                                                     | Priority |
| ---------- | --------------------------------------------------------------------------------- | ---------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------- | -------- |
| MF-TRF-008 | Transfer amount exceeds allowed source balance                                    | Eligible accounts exist but insufficient funds | 1. Enter excessive transfer amount<br>2. Submit                       | Transfer is blocked with proper validation or business-rule message | High     |
| MF-TRF-009 | Transfer between unsupported account types                                        | Unsupported combination selected               | 1. Attempt unsupported transfer                                       | Action is blocked                                                   | High     |
| MF-TRF-010 | Create standing instruction with invalid schedule                                 | Eligible accounts exist                        | 1. Enter invalid start/end date or frequency combination<br>2. Submit | Validation error shown                                              | High     |
| MF-TRF-011 | Standing instruction execution fails when source account has insufficient balance | Active standing instruction exists             | 1. Allow due execution with insufficient funds                        | Execution fails gracefully and failure status/history is recorded   | High     |

### Additional Coverage Tests

| TC ID      | Test Case                                                                         | Preconditions                   | Steps                                         | Expected Result                                | Priority |
| ---------- | --------------------------------------------------------------------------------- | ------------------------------- | --------------------------------------------- | ---------------------------------------------- | -------- |
| MF-TRF-013 | Transfer transaction appears in both source and destination histories             | Successful transfer exists      | 1. Open both accounts                         | Matching debit/credit entries are visible      | High     |
| MF-TRF-014 | Standing instruction can be paused and resumed where supported                    | Instruction exists              | 1. Pause instruction<br>2. Resume instruction | Execution behavior follows updated status      | Medium   |
| MF-TRF-015 | Duplicate standing instruction detection where business rules restrict duplicates | Same instruction already exists | 1. Attempt duplicate creation                 | Validation or business rule prevents duplicate | Low      |
