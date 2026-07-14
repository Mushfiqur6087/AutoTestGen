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
| MF-SHARE-010 | Redeem more shares than held                   | Active share account exists   | 1. Attempt redemption exceeding holdings    | Transaction is blocked                         | High     |
| MF-SHARE-011 | Purchase or redeem on non-active share account | Account not active            | 1. Attempt transaction                      | Action is blocked                              | High     |
| MF-SHARE-012 | Activate share account with invalid date order | Approved share account exists | 1. Activate with invalid date               | Validation prevents activation                 | Medium   |

### Additional Coverage Tests

| TC ID        | Test Case                                                                 | Preconditions                | Steps                                             | Expected Result                                              | Priority |
| ------------ | ------------------------------------------------------------------------- | ---------------------------- | ------------------------------------------------- | ------------------------------------------------------------ | -------- |
| MF-SHARE-013 | Reject share account application                                          | Pending share account exists | 1. Open account<br>2. Reject                      | Account status changes to Rejected                           | Medium   |
| MF-SHARE-014 | Share balance and nominal/market value display updates after transactions | Share account exists         | 1. Purchase or redeem shares<br>2. Reopen summary | Summary values reflect updated holdings and valuation inputs | Medium   |
| MF-SHARE-015 | Dividend posting respects eligible holdings and effective rules           | Dividend run configured      | 1. Post dividend                                  | Dividend amount aligns with eligible share holdings/rules    | Medium   |
