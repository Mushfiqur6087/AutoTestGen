# Mifos Banking System Test Cases — Ground Truth

Source: dataset/ground_truth/Mifos/Mifos.md

## Share Products

### Functional Tests

| TC ID         | Test Case                                    | Preconditions            | Steps                                                                                                                                                                                             | Expected Result                                             | Priority |
| ------------- | -------------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | -------- |
| MF-SHPROD-001 | View share products list                     | Share module enabled     | 1. Navigate to Share Products                                                                                                                                                                     | Share products list displays configured products            | High     |
| MF-SHPROD-002 | Create share product successfully            | Required setup exists    | 1. Click Create Share Product<br>2. Fill mandatory fields including product name, short name, currency, total shares, nominal price, market price, accounting mappings if applicable<br>3. Submit | Share product is created successfully                       | High     |
| MF-SHPROD-003 | View share product detail                    | Share product exists     | 1. Open product                                                                                                                                                                                   | Product detail displays pricing, share limits, and settings | High     |
| MF-SHPROD-004 | Edit share product                           | Share product exists     | 1. Open product<br>2. Edit allowed fields<br>3. Submit                                                                                                                                            | Product changes are saved successfully                      | High     |
| MF-SHPROD-005 | Configure dividend settings on share product | Dividend feature enabled | 1. Create or edit product with dividend settings                                                                                                                                                  | Product retains dividend configuration                      | Medium   |
| MF-SHPROD-006 | Configure share purchase limits              | Share product exists     | 1. Set minimum/maximum share purchase limits<br>2. Save                                                                                                                                           | Limits are saved successfully                               | Medium   |

### Negative Tests

| TC ID         | Test Case                                                      | Preconditions          | Steps                                                                             | Expected Result                | Priority |
| ------------- | -------------------------------------------------------------- | ---------------------- | --------------------------------------------------------------------------------- | ------------------------------ | -------- |
| MF-SHPROD-007 | Create share product without mandatory name                    | None                   | 1. Leave product name empty<br>2. Submit                                          | Validation error shown         | High     |
| MF-SHPROD-008 | Create share product with invalid share limits                 | None                   | 1. Set min shares greater than max shares<br>2. Submit                            | Validation error prevents save | High     |
| MF-SHPROD-009 | Missing accounting mappings when accounting rule requires them | GL accounts incomplete | 1. Configure accounting-requiring product without mandatory mappings<br>2. Submit | Validation blocks save         | High     |

### Additional Coverage Tests

| TC ID         | Test Case                                                                     | Preconditions         | Steps                                                           | Expected Result                                            | Priority |
| ------------- | ----------------------------------------------------------------------------- | --------------------- | --------------------------------------------------------------- | ---------------------------------------------------------- | -------- |
| MF-SHPROD-010 | Inactivate share product for future use                                       | Product exists        | 1. Disable/inactivate product                                   | Product is unavailable for new share accounts              | Medium   |
| MF-SHPROD-011 | Dividend configuration is available only when feature is enabled              | Feature toggles exist | 1. Inspect share product form under different configurations    | Dividend settings behave according to feature availability | Low      |
| MF-SHPROD-012 | Share product pricing updates affect new purchase behavior according to rules | Product exists        | 1. Change allowed pricing field<br>2. Create new share purchase | New transactions use updated configuration as designed     | Medium   |
