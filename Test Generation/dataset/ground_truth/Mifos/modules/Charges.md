# Mifos Banking System Test Cases — Ground Truth

Source: dataset/ground_truth/Mifos/Mifos.md

## Charges

### Functional Tests

| TC ID         | Test Case                                   | Preconditions                          | Steps                                                                                                               | Expected Result                                                 | Priority |
| ------------- | ------------------------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | -------- |
| MF-CHARGE-001 | View charges list                           | User logged in with permission         | 1. Navigate to Charges                                                                                              | Charges list displays configured charge definitions             | High     |
| MF-CHARGE-002 | Create flat charge successfully             | None                                   | 1. Click Create Charge<br>2. Enter name, currency, flat amount, applicable time/type and target entity<br>3. Submit | Charge is created successfully                                  | High     |
| MF-CHARGE-003 | Create percentage-based charge successfully | None                                   | 1. Create charge with percentage amount and valid basis                                                             | Charge is created successfully with percentage configuration    | High     |
| MF-CHARGE-004 | Edit charge definition                      | Existing charge exists and is editable | 1. Open charge<br>2. Click Edit<br>3. Update allowed fields<br>4. Submit                                            | Updated values are saved                                        | High     |
| MF-CHARGE-005 | Create loan disbursement charge             | Loan charge applicability supported    | 1. Create charge applicable to loans at disbursement                                                                | Charge is available for relevant loan product/account workflows | High     |
| MF-CHARGE-006 | Create savings withdrawal charge            | Savings applicability supported        | 1. Create charge applicable to savings withdrawals                                                                  | Charge can be linked to savings products/accounts               | Medium   |
| MF-CHARGE-007 | Create client-level charge                  | Client charges supported               | 1. Create charge applicable to clients                                                                              | Charge is available for client charge assignment                | Medium   |
| MF-CHARGE-008 | View charge details                         | Charge exists                          | 1. Open charge record                                                                                               | Detail page shows amount, type, applicability, and timing       | Medium   |

### Negative Tests

| TC ID         | Test Case                                                      | Preconditions | Steps                                                                     | Expected Result                           | Priority |
| ------------- | -------------------------------------------------------------- | ------------- | ------------------------------------------------------------------------- | ----------------------------------------- | -------- |
| MF-CHARGE-009 | Create charge without name                                     | None          | 1. Leave name empty<br>2. Submit                                          | Validation error shown for charge name    | High     |
| MF-CHARGE-010 | Create charge without amount or percentage                     | None          | 1. Omit required amount field<br>2. Submit                                | Validation error prevents save            | High     |
| MF-CHARGE-011 | Create percentage charge above supported limit                 | None          | 1. Enter invalid percentage value<br>2. Submit                            | Validation error shown                    | High     |
| MF-CHARGE-012 | Create charge with incompatible applicability/time combination | None          | 1. Choose invalid target entity and event timing combination<br>2. Submit | Validation or business rule prevents save | Medium   |

### Additional Coverage Tests

| TC ID         | Test Case                                                              | Preconditions                     | Steps                                                              | Expected Result                                                                    | Priority |
| ------------- | ---------------------------------------------------------------------- | --------------------------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------------------------- | -------- |
| MF-CHARGE-014 | Inactivate charge definition                                           | Charge exists and can be disabled | 1. Open charge<br>2. Disable or inactivate                         | Charge is unavailable for future assignments while historical usage remains intact | Medium   |
| MF-CHARGE-015 | Charge linked to product appears during account lifecycle              | Product linked to charge exists   | 1. Create account from linked product<br>2. Trigger relevant event | Charge is assessed according to configuration                                      | High     |
| MF-CHARGE-016 | Charge collected from account updates accounting and balance correctly | Charge applied to active account  | 1. Collect due charge                                              | Charge balance reduces and transaction entries are posted correctly                | High     |
| MF-CHARGE-017 | Waive charge from applicable account                                   | Applied charge exists             | 1. Open charge on account<br>2. Waive charge                       | Charge outstanding amount is reduced according to waived amount                    | Medium   |
