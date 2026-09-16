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
| MF-SHPROD-006 | Unauthenticated user cannot open the Create Share Product wizard | User is not authenticated | 1. Navigate to the Share Products listing page URL without being logged in<br>2. Click '+ Create Share Product' | User is redirected to the Login page; the Create Share Product wizard is not opened | Medium   |

### Negative Tests

| TC ID         | Test Case                                                      | Preconditions          | Steps                                                                             | Expected Result                | Priority |
| ------------- | -------------------------------------------------------------- | ---------------------- | --------------------------------------------------------------------------------- | ------------------------------ | -------- |
| MF-SHPROD-007 | Create share product without mandatory name                    | None                   | 1. Leave product name empty<br>2. Submit                                          | Validation error shown         | High     |
| MF-SHPROD-008 | Create button hidden for user without product-management privileges | Authenticated user without product-management privileges | 1. Login as a user account without product-management privileges<br>2. Navigate to the Share Products listing page | The '+ Create Share Product' button is not visible; Edit/Delete row actions are not available to this user role | High     |
| MF-SHPROD-009 | Missing accounting mappings when accounting rule requires them | GL accounts incomplete | 1. Configure accounting-requiring product without mandatory mappings<br>2. Submit | Validation blocks save         | High     |

### Additional Coverage Tests

| TC ID         | Test Case                                                                     | Preconditions         | Steps                                                           | Expected Result                                            | Priority |
| ------------- | ----------------------------------------------------------------------------- | --------------------- | --------------------------------------------------------------- | ---------------------------------------------------------- | -------- |
| MF-SHPROD-010 | Inactivate share product for future use                                       | Product exists        | 1. Disable/inactivate product                                   | Product is unavailable for new share accounts              | Medium   |
| MF-SHPROD-011 | Unauthenticated user cannot access Edit on an existing share product | User is not authenticated; an existing share product exists | 1. Navigate directly to an existing Share Product detail page URL while not logged in<br>2. Attempt to click the Edit action | User is redirected to the Login page; the edit action is blocked | Low      |
| MF-SHPROD-012 | Direct navigation to Step 7 without completing Step 1 is blocked | Authenticated user on Share Products listing page | 1. Click + Create Share Product<br>2. Click the Step 7 tab/header directly without entering data in Step 1 | Navigation to Step 7 is prevented; the stepper shows a validation indicator and Step 1 remains active | Medium   |
