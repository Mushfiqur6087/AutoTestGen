# Mifos Banking System Test Cases — Ground Truth

Source: dataset/ground_truth/Mifos/Mifos.md

## Users & Roles

### Functional Tests

| TC ID       | Test Case                      | Preconditions                   | Steps                                                                                                                           | Expected Result                                                    | Priority |
| ----------- | ------------------------------ | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | -------- |
| MF-USER-001 | View users list                | Admin user logged in            | 1. Navigate to Users                                                                                                            | Users list displays username, office, roles, and status            | High     |
| MF-USER-002 | Create new user successfully   | Office and role exist           | 1. Click Create User<br>2. Enter username, first name, last name, email if applicable, office, roles, and password<br>3. Submit | User is created successfully and appears in users list             | High     |
| MF-USER-003 | View user details              | User exists                     | 1. Open user record                                                                                                             | User profile displays office, assigned roles, status, and metadata | High     |
| MF-USER-004 | Edit user details              | Editable user exists            | 1. Open user<br>2. Click Edit<br>3. Update allowed fields<br>4. Submit                                                          | User details are updated successfully                              | High     |
| MF-USER-005 | Assign additional role to user | User and role exist             | 1. Edit user roles<br>2. Add role<br>3. Submit                                                                                  | New role is assigned successfully                                  | High     |
| MF-USER-006 | Remove role from user          | User with multiple roles exists | 1. Edit user roles<br>2. Remove role<br>3. Submit                                                                               | Role is removed successfully according to business rules           | Medium   |
| MF-USER-007 | Disable user                   | Active user exists              | 1. Open user<br>2. Disable/inactivate user                                                                                      | User becomes inactive and cannot authenticate                      | High     |
| MF-USER-008 | Re-enable disabled user        | Disabled user exists            | 1. Open disabled user<br>2. Enable user                                                                                         | User is restored to active status                                  | Medium   |
| MF-USER-009 | View roles list                | Admin user logged in            | 1. Navigate to Roles                                                                                                            | Roles list loads with role names and status                        | High     |
| MF-USER-010 | Create role successfully       | Admin permissions available     | 1. Click Create Role<br>2. Enter role name and permissions<br>3. Submit                                                         | Role is created successfully                                       | High     |
| MF-USER-011 | Edit role permissions          | Existing role exists            | 1. Open role<br>2. Update permission mappings<br>3. Submit                                                                      | Role permissions are updated successfully                          | High     |

### Negative Tests

| TC ID       | Test Case                                    | Preconditions                  | Steps                                  | Expected Result                                             | Priority |
| ----------- | -------------------------------------------- | ------------------------------ | -------------------------------------- | ----------------------------------------------------------- | -------- |
| MF-USER-013 | Create user without username                 | None                           | 1. Leave username empty<br>2. Submit   | Validation error shown for username                         | High     |
| MF-USER-014 | Create user without office                   | None                           | 1. Omit office selection<br>2. Submit  | Validation error shown for office                           | High     |
| MF-USER-015 | Create user without password                 | None                           | 1. Leave password blank<br>2. Submit   | Validation error shown                                      | High     |
| MF-USER-016 | Duplicate username                           | Existing username exists       | 1. Create user using existing username | Validation or server-side uniqueness error occurs           | High     |
| MF-USER-018 | Disable own currently logged-in user account | Admin logged in as target user | 1. Attempt to disable own account      | System blocks or handles safely according to business rules | Medium   |

### Additional Coverage Tests

| TC ID       | Test Case                                        | Preconditions         | Steps                                                                       | Expected Result                                                | Priority |
| ----------- | ------------------------------------------------ | --------------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------- | -------- |
| MF-USER-019 | Password reset for existing user                 | User exists           | 1. Open user<br>2. Reset password<br>3. Submit                              | User password is updated and old password becomes invalid      | High     |
| MF-USER-021 | Maker-checker permissions assigned through roles | Maker-checker enabled | 1. Assign maker/checker permissions to role<br>2. Perform relevant workflow | User can create or approve actions according to permission set | Medium   |
