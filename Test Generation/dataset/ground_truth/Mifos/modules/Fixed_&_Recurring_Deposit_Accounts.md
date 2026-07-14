# Mifos Banking System Test Cases — Ground Truth

Source: dataset/ground_truth/Mifos/Mifos.md

## Fixed & Recurring Deposit Accounts

### Functional Tests

| TC ID      | Test Case                                              | Preconditions                                      | Steps                                                                                                  | Expected Result                                                             | Priority |
| ---------- | ------------------------------------------------------ | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------- | -------- |
| MF-DEP-001 | Create fixed deposit product successfully              | Required accounting and configuration setup exists | 1. Navigate to deposit products<br>2. Create fixed deposit product with mandatory details<br>3. Submit | Fixed deposit product is created successfully                               | High     |
| MF-DEP-002 | Create recurring deposit product successfully          | Required setup exists                              | 1. Create recurring deposit product with mandatory details<br>2. Submit                                | Recurring deposit product is created successfully                           | High     |
| MF-DEP-003 | Open fixed deposit account for client                  | Active client and fixed deposit product exist      | 1. Open client profile<br>2. Create fixed deposit account<br>3. Fill required values<br>4. Submit      | Fixed deposit account is created successfully                               | High     |
| MF-DEP-004 | Open recurring deposit account for client              | Active client and recurring deposit product exist  | 1. Create recurring deposit account from client profile                                                | Recurring deposit account is created successfully                           | High     |
| MF-DEP-005 | Approve deposit account                                | Pending deposit account exists                     | 1. Open deposit account<br>2. Approve                                                                  | Account moves to approved state                                             | High     |
| MF-DEP-006 | Activate deposit account                               | Approved deposit account exists                    | 1. Open account<br>2. Activate with required date                                                      | Account becomes active                                                      | High     |
| MF-DEP-007 | Premature close fixed deposit account                  | Eligible fixed deposit account exists              | 1. Open account<br>2. Initiate premature closure<br>3. Submit                                          | Account closes with premature closure handling applied                      | Medium   |
| MF-DEP-008 | Mature and close fixed deposit account                 | Matured fixed deposit account exists               | 1. Open matured account<br>2. Close on maturity                                                        | Maturity proceeds are handled correctly and account closes                  | High     |
| MF-DEP-009 | Post installment to recurring deposit account          | Active RD account exists                           | 1. Open RD account<br>2. Post deposit installment                                                      | Installment transaction is recorded correctly                               | High     |
| MF-DEP-010 | View deposit account transactions and maturity details | Deposit account exists                             | 1. Open account                                                                                        | Transactions, interest accruals, and maturity information display correctly | Medium   |

### Negative Tests

| TC ID      | Test Case                                              | Preconditions                | Steps                                                     | Expected Result                | Priority |
| ---------- | ------------------------------------------------------ | ---------------------------- | --------------------------------------------------------- | ------------------------------ | -------- |
| MF-DEP-011 | Create deposit product without mandatory name          | None                         | 1. Leave name empty<br>2. Submit                          | Validation error shown         | High     |
| MF-DEP-012 | Create fixed deposit with invalid tenure configuration | None                         | 1. Enter invalid tenure values<br>2. Submit               | Validation prevents save       | High     |
| MF-DEP-013 | Open deposit account without product                   | Active client exists         | 1. Start account creation<br>2. Omit product<br>3. Submit | Validation error shown         | High     |
| MF-DEP-014 | Activate deposit account with invalid date sequence    | Approved account exists      | 1. Use invalid activation date<br>2. Submit               | Validation prevents activation | High     |
| MF-DEP-015 | Post RD installment with invalid amount                | Active RD exists             | 1. Enter invalid installment amount<br>2. Submit          | Validation error shown         | High     |
| MF-DEP-016 | Premature closure on ineligible account                | Deposit account not eligible | 1. Attempt premature closure                              | Business rule blocks action    | Medium   |

### Additional Coverage Tests

| TC ID      | Test Case                                                              | Preconditions                            | Steps                                   | Expected Result                                                           | Priority |
| ---------- | ---------------------------------------------------------------------- | ---------------------------------------- | --------------------------------------- | ------------------------------------------------------------------------- | -------- |
| MF-DEP-017 | Reject deposit account application                                     | Pending deposit account exists           | 1. Open account<br>2. Reject            | Account status changes to Rejected                                        | Medium   |
| MF-DEP-018 | Interest posting or accrual updates deposit account balances correctly | Active deposit account exists            | 1. Trigger interest accrual/posting     | Balances and maturity details update correctly                            | High     |
| MF-DEP-019 | Maturity instructions transfer proceeds according to configured option | Matured account with instructions exists | 1. Process maturity                     | Proceeds are paid out, transferred, or renewed according to configuration | High     |
| MF-DEP-020 | Recurring deposit missed installment behavior follows product rules    | Active RD with missed schedule exists    | 1. Skip installment and inspect account | Penalties or status outcomes follow configured rules                      | Medium   |
