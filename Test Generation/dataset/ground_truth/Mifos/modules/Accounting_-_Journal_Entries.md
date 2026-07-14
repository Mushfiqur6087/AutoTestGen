# Mifos Banking System Test Cases — Ground Truth

Source: dataset/ground_truth/Mifos/Mifos.md

## Accounting - Journal Entries

### Functional Tests

| TC ID      | Test Case                                          | Preconditions                    | Steps                                                                                                        | Expected Result                                                                             | Priority |
| ---------- | -------------------------------------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- | -------- |
| MF-JRN-001 | View journal entries list                          | User with accounting permission  | 1. Navigate to Journal Entries                                                                               | Journal entries list is displayed with date, office, transaction ID, debit, and credit data | High     |
| MF-JRN-002 | Create manual journal entry                        | Eligible GL accounts exist       | 1. Click Create Journal Entry<br>2. Select office/date<br>3. Add balanced debit and credit rows<br>4. Submit | Journal entry is posted successfully                                                        | High     |
| MF-JRN-003 | Reverse manual journal entry where supported       | Existing reversible entry exists | 1. Open journal entry<br>2. Reverse it                                                                       | Reversal entry is created and reflected in list                                             | High     |
| MF-JRN-004 | Filter journal entries by date range               | Journal entries exist            | 1. Apply date filter                                                                                         | Only entries within date range are displayed                                                | Medium   |
| MF-JRN-005 | Filter journal entries by office or transaction ID | Journal entries exist            | 1. Apply office/ID filter                                                                                    | Matching entries are displayed                                                              | Medium   |

### Negative Tests

| TC ID      | Test Case                                          | Preconditions              | Steps                                                         | Expected Result                           | Priority |
| ---------- | -------------------------------------------------- | -------------------------- | ------------------------------------------------------------- | ----------------------------------------- | -------- |
| MF-JRN-006 | Submit unbalanced journal entry                    | Eligible GL accounts exist | 1. Add debit and credit rows with unequal totals<br>2. Submit | Validation prevents posting               | High     |
| MF-JRN-007 | Submit journal entry without mandatory office/date | None                       | 1. Omit required fields<br>2. Submit                          | Validation error shown                    | High     |
| MF-JRN-008 | Use restricted GL account for manual entry         | Restricted account exists  | 1. Add account not allowed for manual posting<br>2. Submit    | Validation or business rule prevents save | High     |
| MF-JRN-009 | Reverse already reversed entry                     | Reversed entry exists      | 1. Attempt second reversal                                    | Operation is blocked                      | Medium   |

### Additional Coverage Tests

| TC ID      | Test Case                                                | Preconditions             | Steps                                    | Expected Result                                        | Priority |
| ---------- | -------------------------------------------------------- | ------------------------- | ---------------------------------------- | ------------------------------------------------------ | -------- |
| MF-JRN-010 | View journal entry detail drill-down                     | Entry exists              | 1. Open entry detail                     | Entry lines and metadata are shown accurately          | Medium   |
| MF-JRN-011 | Backdated journal entry follows accounting closure rules | Closure exists for period | 1. Attempt manual entry in closed period | Operation is blocked if closure rules disallow posting | High     |
