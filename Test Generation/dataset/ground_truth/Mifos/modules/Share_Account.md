# Mifos Banking System Test Cases — Ground Truth

Source: dataset/ground_truth/Mifos/Mifos.md

## Share Account

### Functional Tests

| TC ID        | Test Case                               | Preconditions                                        | Steps                                                                                                 | Expected Result                                        | Priority |
| ------------ | --------------------------------------- | ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | -------- |
| MF-SHARE-001 | Create share account for client         | Active client and share product exist                | 1. Open client profile<br>2. Create new share account<br>3. Select product and submit required values | Share account is created successfully                  | High     |
| MF-SHARE-002 | Approve share account application       | Pending share account exists                         | 1. Open share account<br>2. Approve application                                                       | Share account moves to approved state                  | High     |
| MF-SHARE-003 | Activate share account                  | Approved share account exists                        | 1. Open account<br>2. Activate                                                                        | Share account becomes active                           | High     |
| MF-SHARE-004 | Purchase shares                         | Active share account exists                          | 1. Open share account<br>2. Purchase shares with quantity/date<br>3. Submit                           | Purchase transaction is posted and holdings increase   | High     |
| MF-SHARE-005 | Redeem shares                           | Active share account with sufficient holdings exists | 1. Open share account<br>2. Redeem shares<br>3. Submit                                                | Redemption transaction is posted and holdings decrease | High     |
| MF-SHARE-006 | View share transactions                 | Share account with activity exists                   | 1. Open transactions section                                                                          | Purchase/redemption/dividend history is displayed      | Medium   |
| MF-SHARE-007 | Post dividend to eligible share account | Dividend-capable share product/account exists        | 1. Trigger or post dividend action                                                                    | Dividend transaction is recorded correctly             | Medium   |
| MF-SHARE-008 | Close share account                     | Eligible account exists                              | 1. Open account<br>2. Close with required details                                                     | Share account status changes to closed                 | Medium   |

### Negative Tests

| TC ID        | Test Case                                      | Preconditions                 | Steps                                       | Expected Result                                | Priority |
| ------------ | ---------------------------------------------- | ----------------------------- | ------------------------------------------- | ---------------------------------------------- | -------- |
| MF-SHARE-009 | Purchase shares below minimum allowed quantity | Active share account exists   | 1. Attempt purchase below minimum threshold | Validation or business rule blocks transaction | High     |
| MF-SHARE-010 | Redeem blocked when client has no linked savings account for crediting redemption | Active share account exists; client has no active savings accounts linked for charges/crediting | 1. Open share account<br>2. Click Redeem Shares action<br>3. Enter valid number of Shares to Redeem<br>4. Click Redeem/Submit button | Dialog does not submit; a visible error/notice indicates there is no linked savings account to credit redemption (or Redeem button is disabled); no redemption is processed and holdings remain unchanged | High     |
| MF-SHARE-011 | Purchase or redeem on non-active share account | Account not active            | 1. Attempt transaction                      | Action is blocked                              | High     |
| MF-SHARE-012 | Undo Approval on an Approved share account reverts it to Pending | Approved share account exists | 1. Open share account<br>2. Click Undo Approval action<br>3. Confirm on the Undo Approval dialog | Share Account Detail page displays status badge 'Pending'; Approved-state fields such as Approved Date are no longer shown as current | Medium   |

### Additional Coverage Tests

| TC ID        | Test Case                                                                 | Preconditions                | Steps                                             | Expected Result                                              | Priority |
| ------------ | ------------------------------------------------------------------------- | ---------------------------- | ------------------------------------------------- | ------------------------------------------------------------ | -------- |
| MF-SHARE-013 | Reject share account application                                          | Pending share account exists | 1. Open account<br>2. Reject                      | Account status changes to Rejected                           | Medium   |
| MF-SHARE-014 | Share balance and nominal/market value display updates after transactions | Share account exists         | 1. Purchase or redeem shares<br>2. Reopen summary | Summary values reflect updated holdings and valuation inputs | Medium   |
| MF-SHARE-015 | Dividend posting respects eligible holdings and effective rules           | Dividend run configured      | 1. Post dividend                                  | Dividend amount aligns with eligible share holdings/rules    | Medium   |
