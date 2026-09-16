# Mifos Banking System Test Cases — Ground Truth

Source: dataset/ground_truth/Mifos/Mifos.md

## Provisioning

### Functional Tests

| TC ID       | Test Case                     | Preconditions                     | Steps                                                                 | Expected Result                                        | Priority |
| ----------- | ----------------------------- | --------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------ | -------- |
| MF-PROV-001 | View provisioning criteria    | Provisioning feature enabled      | 1. Navigate to Provisioning                                           | Provisioning criteria and history are displayed        | High     |
| MF-PROV-002 | Create provisioning criteria  | Feature enabled                   | 1. Create criteria with delinquency ranges and percentages<br>2. Save | Criteria are saved successfully                        | High     |
| MF-PROV-003 | Generate provisioning entries | Criteria and eligible loans exist | 1. Run provisioning process                                           | Provisioning entries/report are generated successfully | High     |
| MF-PROV-004 | View provisioning history     | Provisioning runs exist           | 1. Open provisioning history                                          | Past generated entries are displayed                   | Medium   |

### Negative Tests

| TC ID       | Test Case                                                        | Preconditions            | Steps                                        | Expected Result                       | Priority |
| ----------- | ---------------------------------------------------------------- | ------------------------ | -------------------------------------------- | ------------------------------------- | -------- |
| MF-PROV-005 | Non-privileged user cannot submit Provisioning Criteria | Logged in as a user without accounting/administrative privileges | 1. Open the Provisioning Criteria form<br>2. Fill Criteria Name and at least one Definitions row with valid values<br>3. Click Create | Create action is blocked; a visible permission/access error is shown and the form remains open; the criteria is not saved | High     |
| MF-PROV-006 | Create criteria with invalid percentage                          | None                     | 1. Enter invalid percentage value<br>2. Save | Validation error shown                | High     |
| MF-PROV-007 | Submitting Provisioning Criteria with zero Definitions rows is blocked | Provisioning Criteria creation form can be opened | 1. Enter a valid Criteria Name<br>2. Add then remove a Definitions row so zero rows remain<br>3. Click Create | Form submission is blocked; a visible inline error indicates at least one Definitions row is required; no new criteria appears in the listing | Medium   |

### Additional Coverage Tests

| TC ID       | Test Case                                                                  | Preconditions                  | Steps                                                                        | Expected Result                                  | Priority |
| ----------- | -------------------------------------------------------------------------- | ------------------------------ | ---------------------------------------------------------------------------- | ------------------------------------------------ | -------- |
| MF-PROV-008 | Unauthenticated user cannot create a Provisioning Entry | Not logged in (no authenticated session) | 1. Navigate to the Provisioning Entries page<br>2. Click the + Create Provisioning Entry button | Action is blocked; user is redirected to login or shown an authentication prompt; no provisioning entries are generated | High     |
| MF-PROV-009 | Generated provisioning creates expected accounting impact where configured | Accounting integration enabled | 1. Run provisioning                                                          | Related accounting entries are created correctly | High     |
