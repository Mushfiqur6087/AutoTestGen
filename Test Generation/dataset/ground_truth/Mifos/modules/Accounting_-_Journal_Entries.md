# Mifos Banking System Test Cases — Ground Truth

Source: dataset/ground_truth/Mifos/Mifos.md

## Accounting - Journal Entries

### Functional Tests

| TC ID      | Test Case                                          | Preconditions                    | Steps                                                                                                        | Expected Result                                                                             | Priority |
| ---------- | -------------------------------------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- | -------- |
| MF-JRN-001 | View journal entries list                          | User with accounting permission  | 1. Navigate to Journal Entries                                                                               | Journal entries list is displayed with date, office, transaction ID, debit, and credit data | High     |
| MF-JRN-002 | Create manual journal entry                        | Eligible GL accounts exist       | 1. Click Create Journal Entry<br>2. Select office/date<br>3. Add balanced debit and credit rows<br>4. Submit | Journal entry is posted successfully                                                        | High     |
| MF-JRN-003 | Reverse manual journal entry where supported       | Existing reversible entry exists | 1. Open journal entry<br>2. Reverse it                                                                       | Reversal entry is created and reflected in list                                             | High     |
| MF-JRN-004 | Filter journal entries by Entry Type using dropdown filter | Journal entries exist with varying Entry Types; user has accounting permission | 1. Navigate to Journal Entries<br>2. In the filter bar, select an Entry Type from the Entry Type dropdown filter<br>3. Apply the filter | The Journal Entries table displays only rows matching the selected Entry Type; rows with other entry types are no longer visible in the results | Medium   |
| MF-JRN-005 | Filter journal entries by office or transaction ID | Journal entries exist            | 1. Apply office/ID filter                                                                                    | Matching entries are displayed                                                              | Medium   |

### Negative Tests

| TC ID      | Test Case                                          | Preconditions              | Steps                                                         | Expected Result                           | Priority |
| ---------- | -------------------------------------------------- | -------------------------- | ------------------------------------------------------------- | ----------------------------------------- | -------- |
| MF-JRN-006 | Submit unbalanced journal entry                    | Eligible GL accounts exist | 1. Add debit and credit rows with unequal totals<br>2. Submit | Validation prevents posting               | High     |
| MF-JRN-007 | Submit journal entry without mandatory office/date | None                       | 1. Omit required fields<br>2. Submit                          | Validation error shown                    | High     |
| MF-JRN-008 | Submit journal entry with Amount entered at excessive decimal precision | Eligible GL accounts exist | 1. Add Journal Entry form open<br>2. Select Office, Currency, Transaction Date<br>3. Add an entry line and select a GL Account<br>4. Enter an Amount with more decimal places than the currency's supported precision<br>5. Add balancing entry lines so totals would match if precision were accepted<br>6. Submit | Submission is blocked; inline validation indicates the Amount precision is unsupported and prevents the journal entry from being created | High     |
| MF-JRN-009 | Rapid double-submission of Create Journal Entry does not create duplicate entries | Eligible GL accounts exist | 1. Fill in Office, Currency, Transaction Date, and balanced entry lines in the Journal Entry form<br>2. Click 'Create Journal Entry' twice in rapid succession (double-click)<br>3. Return to the Journal Entries table or refresh | Only one journal entry is created; the Journal Entries table shows a single new entry and no duplicate rows after the rapid double-click | Medium   |

### Additional Coverage Tests

| TC ID      | Test Case                                                | Preconditions             | Steps                                    | Expected Result                                        | Priority |
| ---------- | -------------------------------------------------------- | ------------------------- | ---------------------------------------- | ------------------------------------------------------ | -------- |
| MF-JRN-010 | View journal entry detail showing Reference Number preserved exactly as entered | Entry exists with a Reference Number containing special characters/emoji | 1. Create (or open) a journal entry with a Reference Number that includes special characters and emoji<br>2. Open the journal entry detail view | The journal entry detail view displays the Reference Number exactly as entered, including special characters and emoji | Medium   |
| MF-JRN-011 | Backdated journal entry follows accounting closure rules | Closure exists for period | 1. Attempt manual entry in closed period | Operation is blocked if closure rules disallow posting | High     |
