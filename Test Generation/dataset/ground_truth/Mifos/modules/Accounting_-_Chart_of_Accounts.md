# Mifos Banking System Test Cases — Ground Truth

Source: dataset/ground_truth/Mifos/Mifos.md

## Accounting - Chart of Accounts

### Functional Tests

| TC ID      | Test Case                     | Preconditions                             | Steps                                                                  | Expected Result                                                                | Priority |
| ---------- | ----------------------------- | ----------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------ | -------- |
| MF-COA-001 | View chart of accounts        | User with accounting permission           | 1. Navigate to Chart of Accounts                                       | GL accounts tree/list is displayed grouped by account type                     | High     |
| MF-COA-002 | Create header account         | Accounting access available               | 1. Create new GL account as header<br>2. Submit                        | Header account is created successfully                                         | High     |
| MF-COA-003 | Create non-header account     | Parent/header account exists where needed | 1. Create new GL account with type, usage, classification<br>2. Submit | GL account is created and visible in chart                                     | High     |
| MF-COA-004 | Edit GL account               | Editable GL account exists                | 1. Open GL account<br>2. Edit details<br>3. Submit                     | Changes are saved successfully                                                 | High     |
| MF-COA-005 | Disable or close GL account   | Eligible account exists                   | 1. Open account<br>2. Disable/close                                    | Account status changes and account is unavailable for future use as configured | Medium   |
| MF-COA-006 | View GL account usage details | GL account exists                         | 1. Open GL account detail                                              | Details show account classification, usage type, and relationships             | Medium   |

### Negative Tests

| TC ID      | Test Case                                                | Preconditions               | Steps                                            | Expected Result                                   | Priority |
| ---------- | -------------------------------------------------------- | --------------------------- | ------------------------------------------------ | ------------------------------------------------- | -------- |
| MF-COA-007 | Create GL account without name                           | None                        | 1. Leave name empty<br>2. Submit                 | Validation error shown                            | High     |
| MF-COA-008 | Create GL account without account type                   | None                        | 1. Omit account type/classification<br>2. Submit | Validation error shown                            | High     |
| MF-COA-009 | Duplicate GL account code                                | Existing code exists        | 1. Create another GL account using same code     | Validation or server-side uniqueness error occurs | High     |
| MF-COA-010 | Disable GL account that is constrained by business rules | Account linked or protected | 1. Attempt disable/close action                  | Operation is blocked with correct error message   | Medium   |

### Additional Coverage Tests

| TC ID      | Test Case                                                        | Preconditions     | Steps                                                       | Expected Result                                       | Priority |
| ---------- | ---------------------------------------------------------------- | ----------------- | ----------------------------------------------------------- | ----------------------------------------------------- | -------- |
| MF-COA-011 | Manual entries allowed only for accounts with correct usage type | GL account exists | 1. Attempt journal entry on restricted and allowed accounts | Only accounts eligible for manual posting can be used | High     |
