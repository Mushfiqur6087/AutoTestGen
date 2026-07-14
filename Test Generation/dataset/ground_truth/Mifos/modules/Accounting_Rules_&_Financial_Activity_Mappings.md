# Mifos Banking System Test Cases — Ground Truth

Source: dataset/ground_truth/Mifos/Mifos.md

## Accounting Rules & Financial Activity Mappings

### Functional Tests

| TC ID      | Test Case                                         | Preconditions                       | Steps                                                                 | Expected Result                          | Priority |
| ---------- | ------------------------------------------------- | ----------------------------------- | --------------------------------------------------------------------- | ---------------------------------------- | -------- |
| MF-FAM-001 | View financial activity mappings                  | Accounting configuration accessible | 1. Navigate to Financial Activity Mappings                            | Existing mappings are displayed          | High     |
| MF-FAM-002 | Create or update financial activity to GL mapping | GL accounts exist                   | 1. Open financial activity<br>2. Assign GL account mapping<br>3. Save | Mapping is saved successfully            | High     |
| MF-FAM-003 | View accounting rules configuration               | Accounting settings accessible      | 1. Navigate to accounting rules/settings                              | Configured rules are displayed correctly | Medium   |
| MF-FAM-004 | Edit accounting rule setting                      | Editable accounting setting exists  | 1. Update rule value<br>2. Save                                       | Rule change is persisted                 | Medium   |

### Negative Tests

| TC ID      | Test Case                                                    | Preconditions               | Steps                                      | Expected Result                         | Priority |
| ---------- | ------------------------------------------------------------ | --------------------------- | ------------------------------------------ | --------------------------------------- | -------- |
| MF-FAM-005 | Save mapping without required GL account                     | Financial activity selected | 1. Leave required account empty<br>2. Save | Validation error shown                  | High     |
| MF-FAM-006 | Map financial activity to invalid or incompatible GL account | GL account incompatible     | 1. Select invalid account type<br>2. Save  | Validation or business rule blocks save | High     |

### Additional Coverage Tests

| TC ID      | Test Case                                                                          | Preconditions                           | Steps                                        | Expected Result                                                         | Priority |
| ---------- | ---------------------------------------------------------------------------------- | --------------------------------------- | -------------------------------------------- | ----------------------------------------------------------------------- | -------- |
| MF-FAM-008 | Product/account posting uses configured financial activity mapping                 | Mapping exists and relevant txn occurs  | 1. Perform linked transaction                | Journal entries use configured mapped GL account                        | High     |
| MF-FAM-009 | Updating mapping affects future transactions without corrupting historical entries | Existing transactions and mapping exist | 1. Change mapping<br>2. Post new transaction | Historical entries remain unchanged and new entries use updated mapping | High     |
| MF-FAM-010 | Accounting rules visible state matches enabled features                            | Different features enabled/disabled     | 1. Review accounting settings                | Only relevant rules are displayed and editable                          | Low      |
