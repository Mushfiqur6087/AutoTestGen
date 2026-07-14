# Mifos Banking System Test Cases — Ground Truth

Source: dataset/ground_truth/Mifos/Mifos.md

## Floating Rates

### Functional Tests

| TC ID        | Test Case                         | Preconditions                              | Steps                                                                                | Expected Result                                            | Priority |
| ------------ | --------------------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------ | ---------------------------------------------------------- | -------- |
| MF-FRATE-001 | View floating rates list          | Floating rate feature enabled              | 1. Navigate to Floating Rates                                                        | Existing floating rates and periods are displayed          | High     |
| MF-FRATE-002 | Create floating rate successfully | Feature enabled                            | 1. Click Create Floating Rate<br>2. Enter name and required details<br>3. Submit     | Floating rate is created successfully                      | High     |
| MF-FRATE-003 | Add floating rate period          | Floating rate exists                       | 1. Open floating rate<br>2. Add new period with effective date and rate<br>3. Submit | New floating rate period is saved                          | High     |
| MF-FRATE-004 | View floating rate history        | Floating rate with multiple periods exists | 1. Open floating rate details                                                        | Historical effective periods and rates are shown correctly | Medium   |
| MF-FRATE-005 | Edit floating rate metadata       | Floating rate exists                       | 1. Open floating rate<br>2. Edit metadata<br>3. Submit                               | Changes are saved successfully                             | Medium   |

### Negative Tests

| TC ID        | Test Case                                             | Preconditions        | Steps                                                            | Expected Result                           | Priority |
| ------------ | ----------------------------------------------------- | -------------------- | ---------------------------------------------------------------- | ----------------------------------------- | -------- |
| MF-FRATE-006 | Create floating rate without mandatory name           | None                 | 1. Leave required name field empty<br>2. Submit                  | Validation error shown                    | High     |
| MF-FRATE-007 | Add rate period with overlapping effective date range | Floating rate exists | 1. Add period overlapping existing effective period<br>2. Submit | Validation or business rule prevents save | High     |
| MF-FRATE-008 | Add rate period with invalid rate value               | Floating rate exists | 1. Enter invalid or out-of-range rate<br>2. Submit               | Validation error shown                    | Medium   |

### Additional Coverage Tests

| TC ID        | Test Case                                                                                                 | Preconditions                         | Steps                                                             | Expected Result                                                  | Priority |
| ------------ | --------------------------------------------------------------------------------------------------------- | ------------------------------------- | ----------------------------------------------------------------- | ---------------------------------------------------------------- | -------- |
| MF-FRATE-009 | Loan product linked to floating rate uses latest applicable period                                        | Linked loan product exists            | 1. Configure product with floating rate<br>2. Create/inspect loan | Linked rate is resolved according to effective date rules        | High     |
| MF-FRATE-010 | Future-dated floating rate period does not affect current calculations before effective date              | Floating rate has future-dated period | 1. Add future period<br>2. Inspect current-linked calculations    | Current calculations remain unchanged until effective date       | High     |
| MF-FRATE-011 | Floating rate history remains immutable for already effective periods where business rules restrict edits | Existing period history exists        | 1. Attempt restricted update to historical period                 | System blocks invalid modification or handles according to rules | Medium   |
