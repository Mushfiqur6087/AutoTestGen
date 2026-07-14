# Mifos Banking System Test Cases — Ground Truth

Source: dataset/ground_truth/Mifos/Mifos.md

## Teller & Cashier Management

### Functional Tests

| TC ID         | Test Case                  | Preconditions                                  | Steps                                                                                                       | Expected Result                                                   | Priority |
| ------------- | -------------------------- | ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | -------- |
| MF-TELLER-001 | View tellers list          | Teller feature enabled and user has permission | 1. Navigate to Tellers                                                                                      | Teller list is displayed with office and status details           | High     |
| MF-TELLER-002 | Create teller successfully | Office and required setup exist                | 1. Click Create Teller<br>2. Enter teller details including office and cash limits if required<br>3. Submit | Teller is created successfully                                    | High     |
| MF-TELLER-003 | View cashier assignments   | Tellers and users exist                        | 1. Navigate to Cashiers or teller detail page                                                               | Cashier assignments are displayed correctly                       | High     |
| MF-TELLER-004 | Assign cashier to teller   | Teller and eligible user exist                 | 1. Open teller<br>2. Assign cashier/user with start and end time if required<br>3. Submit                   | Cashier assignment is saved successfully                          | High     |
| MF-TELLER-005 | Allocate cash to cashier   | Active teller and cashier assignment exist     | 1. Open cashier allocation workflow<br>2. Enter amount<br>3. Submit                                         | Cash allocation transaction is recorded successfully              | High     |
| MF-TELLER-006 | Settle cashier balance     | Active cashier with transactions exists        | 1. Open settle or close cashier workflow<br>2. Submit settlement                                            | Cashier is settled and balances are reconciled according to rules | High     |
| MF-TELLER-007 | View cashier transactions  | Cashier transaction history exists             | 1. Open cashier transactions/history                                                                        | Allocation, settlement, and cash transactions are displayed       | Medium   |
| MF-TELLER-008 | Close or deactivate teller | Teller eligible for closure                    | 1. Open teller<br>2. Deactivate or close                                                                    | Teller status is updated successfully                             | Medium   |

### Negative Tests

| TC ID         | Test Case                                        | Preconditions              | Steps                                                                                    | Expected Result                                         | Priority |
| ------------- | ------------------------------------------------ | -------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------- | -------- |
| MF-TELLER-009 | Create teller without mandatory office           | None                       | 1. Omit office while creating teller<br>2. Submit                                        | Validation error shown                                  | High     |
| MF-TELLER-010 | Assign cashier with invalid overlapping schedule | Existing assignment exists | 1. Create overlapping cashier assignment for same user/teller if restricted<br>2. Submit | Validation or business rule prevents overlap            | High     |
| MF-TELLER-011 | Allocate negative or zero cash amount            | Active cashier exists      | 1. Enter invalid amount<br>2. Submit                                                     | Validation error shown                                  | High     |
| MF-TELLER-012 | Settle cashier with inconsistent cash balance    | Cashier imbalance exists   | 1. Attempt settlement without resolving discrepancy if required                          | Process is blocked or discrepancy is surfaced correctly | High     |

### Additional Coverage Tests

| TC ID         | Test Case                                                                  | Preconditions                   | Steps                                                     | Expected Result                                                        | Priority |
| ------------- | -------------------------------------------------------------------------- | ------------------------------- | --------------------------------------------------------- | ---------------------------------------------------------------------- | -------- |
| MF-TELLER-014 | Cash allocation impacts cashier available balance immediately              | Active cashier exists           | 1. Allocate cash<br>2. Refresh cashier detail             | Available cash/balance reflects allocation                             | High     |
| MF-TELLER-015 | Settlement closes cashier session for further transactions where required  | Cashier settled                 | 1. Settle cashier<br>2. Attempt additional cashier action | Further cashier activity is blocked or requires new assignment/session | Medium   |
| MF-TELLER-016 | Teller and cashier list filters work                                       | Multiple tellers/cashiers exist | 1. Search/filter by office or status                      | Matching records are displayed                                         | Low      |
| MF-TELLER-017 | Cashier transaction audit trail shows maker/checker metadata where enabled | Maker-checker enabled           | 1. Perform teller workflow                                | Audit details are recorded correctly                                   | Medium   |
