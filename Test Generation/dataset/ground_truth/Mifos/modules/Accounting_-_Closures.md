# Mifos Banking System Test Cases — Ground Truth

Source: dataset/ground_truth/Mifos/Mifos.md

## Accounting - Closures

### Functional Tests

| TC ID        | Test Case                              | Preconditions                              | Steps                                                                     | Expected Result                                | Priority |
| ------------ | -------------------------------------- | ------------------------------------------ | ------------------------------------------------------------------------- | ---------------------------------------------- | -------- |
| MF-CLOSE-001 | View accounting closures list          | Accounting admin logged in                 | 1. Navigate to Accounting Closures                                        | Existing closures are displayed by office/date | High     |
| MF-CLOSE-002 | Create accounting closure successfully | No conflicting closure for same scope/date | 1. Click Create Closure<br>2. Select office and closing date<br>3. Submit | Closure is created successfully                | High     |
| MF-CLOSE-003 | View closure details                   | Closure exists                             | 1. Open closure                                                           | Closure details display office/date metadata   | Medium   |

### Negative Tests

| TC ID        | Test Case                                                 | Preconditions                      | Steps                                                        | Expected Result                                  | Priority |
| ------------ | --------------------------------------------------------- | ---------------------------------- | ------------------------------------------------------------ | ------------------------------------------------ | -------- |
| MF-CLOSE-004 | Create duplicate closure for same office/date constraints | Closure exists                     | 1. Attempt duplicate closure                                 | Validation or business rule prevents duplicate   | High     |
| MF-CLOSE-005 | Create closure without required office/date               | None                               | 1. Omit mandatory fields<br>2. Submit                        | Validation error shown                           | High     |
| MF-CLOSE-006 | Backdated transaction after closure is blocked            | Closure exists for relevant period | 1. Attempt transaction/manual journal entry in closed period | System blocks posting according to closure rules | High     |

### Additional Coverage Tests

| TC ID        | Test Case                                                              | Preconditions                             | Steps                                          | Expected Result                                  | Priority |
| ------------ | ---------------------------------------------------------------------- | ----------------------------------------- | ---------------------------------------------- | ------------------------------------------------ | -------- |
| MF-CLOSE-007 | Closure impacts all relevant accounting transactions for scoped office | Closure exists and transactions attempted | 1. Try various posting workflows after closure | Restricted transactions are blocked consistently | High     |
| MF-CLOSE-008 | Closure list can be filtered or sorted where supported                 | Multiple closures exist                   | 1. Use available list controls                 | Expected closures are shown                      | Low      |
