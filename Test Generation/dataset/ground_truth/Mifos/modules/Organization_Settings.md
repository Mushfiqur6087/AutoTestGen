# Mifos Banking System Test Cases — Ground Truth

Source: dataset/ground_truth/Mifos/Mifos.md

## Organization Settings

### Functional Tests

| TC ID      | Test Case                          | Preconditions                    | Steps                                                                                 | Expected Result                              | Priority |
| ---------- | ---------------------------------- | -------------------------------- | ------------------------------------------------------------------------------------- | -------------------------------------------- | -------- |
| MF-ORG-001 | View organization settings modules | User with admin permission       | 1. Navigate to Organization settings area                                             | Available configuration pages are displayed  | High     |
| MF-ORG-002 | Configure working days             | Organization settings accessible | 1. Open Working Days<br>2. Set business days and repayment reschedule rule<br>3. Save | Working day settings are saved successfully  | High     |
| MF-ORG-003 | Configure holidays                 | Organization settings accessible | 1. Open Holidays<br>2. Create holiday with office/date details<br>3. Save             | Holiday is created and visible in list       | High     |
| MF-ORG-004 | Configure currency settings        | Settings accessible              | 1. Open currency/configuration module<br>2. Update allowed settings<br>3. Save        | Currency-related settings are saved          | Medium   |
| MF-ORG-005 | Manage code values/code tables     | Code management accessible       | 1. Open codes module<br>2. Add or edit code value<br>3. Save                          | Code values are updated successfully         | High     |
| MF-ORG-006 | Manage payment types               | Payment types accessible         | 1. Open payment types<br>2. Create or edit payment type<br>3. Save                    | Payment type changes are saved               | Medium   |
| MF-ORG-007 | Configure fund definitions         | Fund configuration accessible    | 1. Open funds<br>2. Create/edit fund<br>3. Save                                       | Fund definition is saved                     | Medium   |
| MF-ORG-008 | Configure account number format    | Feature accessible               | 1. Open account number preferences<br>2. Update format/rules<br>3. Save               | Account number format configuration is saved | Medium   |

### Negative Tests

| TC ID      | Test Case                                         | Preconditions              | Steps                                              | Expected Result                           | Priority |
| ---------- | ------------------------------------------------- | -------------------------- | -------------------------------------------------- | ----------------------------------------- | -------- |
| MF-ORG-010 | Create holiday with invalid date range            | Settings accessible        | 1. Enter invalid holiday period<br>2. Save         | Validation error shown                    | High     |
| MF-ORG-011 | Configure working days with invalid combination   | Settings accessible        | 1. Choose inconsistent rule combination<br>2. Save | Validation or business rule prevents save | Medium   |
| MF-ORG-012 | Duplicate code value where uniqueness is required | Existing code value exists | 1. Add duplicate code value                        | Validation or server-side error occurs    | Medium   |

### Additional Coverage Tests

| TC ID      | Test Case                                                                  | Preconditions                                          | Steps                                                    | Expected Result                                                               | Priority |
| ---------- | -------------------------------------------------------------------------- | ------------------------------------------------------ | -------------------------------------------------------- | ----------------------------------------------------------------------------- | -------- |
| MF-ORG-014 | Account numbering changes apply to newly created entities only as designed | Account number format updated                          | 1. Change format<br>2. Create new client/account         | New records follow updated numbering rule without corrupting existing numbers | Medium   |
| MF-ORG-015 | Holiday affects repayment or transaction scheduling rules correctly        | Holiday configured and relevant product/account exists | 1. Attempt transaction or schedule generation on holiday | Behavior follows configured holiday handling rule                             | High     |
| MF-ORG-016 | Code value change appears in dependent dropdowns                           | Code table linked to entity form                       | 1. Add/edit code value<br>2. Open dependent form         | Updated value appears correctly in UI                                         | Medium   |
| MF-ORG-017 | Payment type in transaction form reflects configured values                | Payment types configured                               | 1. Open repayment/deposit form                           | Payment type dropdown matches organization settings                           | Medium   |
