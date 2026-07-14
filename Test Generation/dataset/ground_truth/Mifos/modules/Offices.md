# Mifos Banking System Test Cases — Ground Truth

Source: dataset/ground_truth/Mifos/Mifos.md

## Offices

### Functional Tests

| TC ID         | Test Case                  | Preconditions                       | Steps                                                                                    | Expected Result                                             | Priority |
| ------------- | -------------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------- | -------- |
| MF-OFFICE-001 | View offices list          | User with organization permission   | 1. Navigate to Offices                                                                   | Offices hierarchy/list is displayed                         | High     |
| MF-OFFICE-002 | Create office successfully | Parent office exists if required    | 1. Click Create Office<br>2. Enter office name, parent office, opening date<br>3. Submit | Office is created successfully                              | High     |
| MF-OFFICE-003 | Edit office details        | Office exists                       | 1. Open office<br>2. Edit details<br>3. Submit                                           | Office details are updated successfully                     | High     |
| MF-OFFICE-004 | View office hierarchy      | Multiple parent-child offices exist | 1. Open Offices page                                                                     | Parent-child structure is displayed correctly               | Medium   |
| MF-OFFICE-005 | Close office               | Office eligible for closure         | 1. Open office<br>2. Close office with closure date and reason                           | Office status changes to closed/inactive according to rules | Medium   |

### Negative Tests

| TC ID         | Test Case                                              | Preconditions                                         | Steps                                                                   | Expected Result                           | Priority |
| ------------- | ------------------------------------------------------ | ----------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------- | -------- |
| MF-OFFICE-006 | Create office without name                             | None                                                  | 1. Leave office name blank<br>2. Submit                                 | Validation error shown                    | High     |
| MF-OFFICE-007 | Create office without opening date                     | None                                                  | 1. Omit opening date<br>2. Submit                                       | Validation error shown                    | High     |
| MF-OFFICE-008 | Create office with invalid parent hierarchy            | Existing office hierarchy exists                      | 1. Set invalid parent causing cyclic hierarchy if possible<br>2. Submit | Validation or business rule prevents save | High     |
| MF-OFFICE-009 | Close office with active dependencies blocking closure | Office has active clients/users or dependent entities | 1. Attempt to close office                                              | Operation is blocked with correct error   | High     |

### Additional Coverage Tests

| TC ID         | Test Case                                         | Preconditions                        | Steps                                            | Expected Result                                      | Priority |
| ------------- | ------------------------------------------------- | ------------------------------------ | ------------------------------------------------ | ---------------------------------------------------- | -------- |
| MF-OFFICE-010 | Transfer dependent entities before office closure | Source and destination offices exist | 1. Move required dependencies<br>2. Close office | Closure succeeds only after dependencies are handled | Medium   |
| MF-OFFICE-011 | Search/filter offices list                        | Multiple offices exist               | 1. Search for office by name                     | Matching office is returned                          | Low      |
