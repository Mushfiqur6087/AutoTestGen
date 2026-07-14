# Mifos Banking System Test Cases — Ground Truth

Source: dataset/ground_truth/Mifos/Mifos.md

## Tax Management

### Functional Tests

| TC ID      | Test Case                                                   | Preconditions                         | Steps                                                               | Expected Result                                 | Priority |
| ---------- | ----------------------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------- | ----------------------------------------------- | -------- |
| MF-TAX-001 | View tax components list                                    | Tax feature enabled                   | 1. Navigate to tax management                                       | Tax components and groups are displayed         | High     |
| MF-TAX-002 | Create tax component successfully                           | Tax feature enabled                   | 1. Create tax component with name and percentage/value<br>2. Submit | Tax component is created successfully           | High     |
| MF-TAX-003 | Create tax group successfully                               | Tax components exist                  | 1. Create tax group and add components<br>2. Submit                 | Tax group is created successfully               | High     |
| MF-TAX-004 | Link tax group to applicable charge/product where supported | Charges/products and tax config exist | 1. Edit applicable configuration<br>2. Assign tax group<br>3. Save  | Tax configuration is saved successfully         | Medium   |
| MF-TAX-005 | View tax configuration details                              | Tax components/groups exist           | 1. Open tax component/group                                         | Details display correct rates and applicability | Medium   |

### Negative Tests

| TC ID      | Test Case                                                          | Preconditions | Steps                                  | Expected Result                           | Priority |
| ---------- | ------------------------------------------------------------------ | ------------- | -------------------------------------- | ----------------------------------------- | -------- |
| MF-TAX-006 | Create tax component without mandatory fields                      | None          | 1. Omit required fields<br>2. Submit   | Validation error shown                    | High     |
| MF-TAX-007 | Create tax component with invalid rate                             | None          | 1. Enter invalid tax rate<br>2. Submit | Validation error shown                    | High     |
| MF-TAX-008 | Create tax group without components where at least one is required | None          | 1. Leave group empty<br>2. Submit      | Validation or business rule prevents save | Medium   |

### Additional Coverage Tests

| TC ID      | Test Case                                                       | Preconditions                           | Steps                                            | Expected Result                                                                | Priority |
| ---------- | --------------------------------------------------------------- | --------------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------ | -------- |
| MF-TAX-010 | Tax is applied correctly on configured charge transaction       | Tax-linked charge exists                | 1. Trigger charge transaction                    | Tax amount is computed and posted according to configuration                   | High     |
| MF-TAX-011 | Updating tax rate affects future transactions only              | Tax component already used historically | 1. Update tax rate<br>2. Trigger new transaction | Historical transactions remain unchanged and new transactions use updated rate | High     |
| MF-TAX-012 | Tax breakdown is visible in transaction details where supported | Tax-applied transaction exists          | 1. Open transaction detail                       | Tax component breakdown is shown correctly                                     | Medium   |
