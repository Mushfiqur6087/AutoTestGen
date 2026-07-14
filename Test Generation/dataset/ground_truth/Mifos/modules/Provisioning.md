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
| MF-PROV-005 | Create provisioning criteria with overlapping delinquency ranges | Criteria ranges exist    | 1. Enter overlapping ranges<br>2. Save       | Validation prevents overlapping setup | High     |
| MF-PROV-006 | Create criteria with invalid percentage                          | None                     | 1. Enter invalid percentage value<br>2. Save | Validation error shown                | High     |
| MF-PROV-007 | Run provisioning without required setup                          | No valid criteria exists | 1. Attempt generate process                  | Process is blocked with proper error  | Medium   |

### Additional Coverage Tests

| TC ID       | Test Case                                                                  | Preconditions                  | Steps                                                                        | Expected Result                                  | Priority |
| ----------- | -------------------------------------------------------------------------- | ------------------------------ | ---------------------------------------------------------------------------- | ------------------------------------------------ | -------- |
| MF-PROV-008 | Provisioning output reflects latest delinquency positions                  | Delinquent loans exist         | 1. Change delinquency state via repayment or aging<br>2. Re-run provisioning | Output reflects current delinquency categories   | High     |
| MF-PROV-009 | Generated provisioning creates expected accounting impact where configured | Accounting integration enabled | 1. Run provisioning                                                          | Related accounting entries are created correctly | High     |
