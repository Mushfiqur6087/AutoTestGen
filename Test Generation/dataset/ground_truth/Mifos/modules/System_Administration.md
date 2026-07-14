# Mifos Banking System Test Cases — Ground Truth

Source: dataset/ground_truth/Mifos/Mifos.md

## System Administration

### Functional Tests

| TC ID      | Test Case                                                  | Preconditions                    | Steps                                                                              | Expected Result                             | Priority |
| ---------- | ---------------------------------------------------------- | -------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------- | -------- |
| MF-SYS-001 | View system administration modules                         | Admin user logged in             | 1. Navigate to system administration area                                          | Available admin modules are displayed       | High     |
| MF-SYS-002 | Manage data tables                                         | Data table feature enabled       | 1. Navigate to Data Tables<br>2. View existing tables                              | Data tables list is displayed correctly     | Medium   |
| MF-SYS-003 | Create or register data table where supported              | Data table feature enabled       | 1. Create/register new data table configuration<br>2. Save                         | Data table is created successfully          | Medium   |
| MF-SYS-004 | Manage hooks/webhooks configuration                        | Hook feature enabled             | 1. Open hooks configuration<br>2. Create or edit hook endpoint/settings<br>3. Save | Hook configuration is saved successfully    | Medium   |
| MF-SYS-005 | View scheduler jobs                                        | Scheduler feature enabled        | 1. Navigate to Scheduler Jobs                                                      | Jobs list and status are displayed          | High     |
| MF-SYS-006 | Run a schedulable job manually where supported             | Eligible job exists              | 1. Trigger manual execution                                                        | Job execution starts/completes successfully | Medium   |
| MF-SYS-007 | Manage password preferences or security settings           | Security settings accessible     | 1. Open password/security preferences<br>2. Update policy settings<br>3. Save      | Security preferences are saved successfully | High     |
| MF-SYS-008 | Manage external services or configurations where supported | Feature enabled                  | 1. Open external service configuration<br>2. View/edit supported settings          | Changes are saved successfully              | Low      |
| MF-SYS-009 | Manage maker-checker settings                              | Maker-checker feature accessible | 1. Open maker-checker settings<br>2. Enable or configure                           | Configuration is saved successfully         | High     |
| MF-SYS-010 | View audit or application logs where supported             | Feature enabled                  | 1. Navigate to log/audit section                                                   | Available logs/audit metadata are displayed | Low      |

### Negative Tests

| TC ID      | Test Case                                | Preconditions                | Steps                                                                          | Expected Result                           | Priority |
| ---------- | ---------------------------------------- | ---------------------------- | ------------------------------------------------------------------------------ | ----------------------------------------- | -------- |
| MF-SYS-012 | Save invalid hook endpoint configuration | Hook feature enabled         | 1. Enter invalid endpoint/config values<br>2. Save                             | Validation or connectivity error is shown | Medium   |
| MF-SYS-014 | Set invalid password policy values       | Security settings accessible | 1. Enter invalid values such as unsupported lengths or combinations<br>2. Save | Validation error shown                    | High     |

### Additional Coverage Tests

| TC ID      | Test Case                                                          | Preconditions                                      | Steps                                                                  | Expected Result                                               | Priority |
| ---------- | ------------------------------------------------------------------ | -------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------- | -------- |
| MF-SYS-015 | Scheduler job execution updates last-run status correctly          | Schedulable job exists                             | 1. Run job<br>2. Refresh job list                                      | Last run metadata and status reflect execution outcome        | Medium   |
| MF-SYS-016 | Maker-checker workflow holds pending action until checker approval | Maker-checker enabled and applicable action exists | 1. Perform maker action<br>2. Inspect pending approvals                | Action remains pending until checker approves                 | High     |
| MF-SYS-017 | Checker approval completes pending maker action                    | Pending maker-checker action exists                | 1. Login as checker<br>2. Approve action                               | Underlying business operation completes successfully          | High     |
| MF-SYS-018 | Checker rejection cancels pending maker action                     | Pending maker-checker action exists                | 1. Reject pending action                                               | Pending action is not executed and status updates accordingly | High     |
| MF-SYS-019 | Hook invocation occurs on configured business event                | Valid hook configured                              | 1. Trigger linked event such as client creation or repayment           | Hook is invoked according to event configuration              | Medium   |
| MF-SYS-020 | Password policy update affects subsequent user password operations | Password policy modified                           | 1. Update security policy<br>2. Create/reset password using new values | System enforces updated policy on future operations           | High     |
