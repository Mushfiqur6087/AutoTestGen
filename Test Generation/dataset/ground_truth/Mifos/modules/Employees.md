# Mifos Banking System Test Cases — Ground Truth

Source: dataset/ground_truth/Mifos/Mifos.md

## Employees

### Functional Tests

| TC ID      | Test Case                           | Preconditions                     | Steps                                                                                         | Expected Result                                               | Priority |
| ---------- | ----------------------------------- | --------------------------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | -------- |
| MF-EMP-001 | View employees list                 | User with organization permission | 1. Navigate to Employees                                                                      | Employees list is displayed with office and status            | High     |
| MF-EMP-002 | Create employee successfully        | Office exists                     | 1. Click Create Employee<br>2. Enter first name, last name, office, joining date<br>3. Submit | Employee is created successfully                              | High     |
| MF-EMP-003 | Edit employee details               | Employee exists                   | 1. Open employee<br>2. Edit allowed fields<br>3. Submit                                       | Employee updates are saved                                    | High     |
| MF-EMP-004 | View employee profile               | Employee exists                   | 1. Open employee record                                                                       | Employee detail page shows linked office and personal details | Medium   |
| MF-EMP-005 | Assign employee to office correctly | Offices and employee exist        | 1. Create or edit employee with office assignment                                             | Office linkage is saved successfully                          | Medium   |

### Negative Tests

| TC ID      | Test Case                          | Preconditions | Steps                                  | Expected Result        | Priority |
| ---------- | ---------------------------------- | ------------- | -------------------------------------- | ---------------------- | -------- |
| MF-EMP-006 | Create employee without first name | None          | 1. Leave first name blank<br>2. Submit | Validation error shown | High     |
| MF-EMP-007 | Create employee without office     | None          | 1. Omit office<br>2. Submit            | Validation error shown | High     |
