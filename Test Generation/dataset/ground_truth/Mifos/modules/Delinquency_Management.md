# Mifos Banking System Test Cases — Ground Truth

Source: dataset/ground_truth/Mifos/Mifos.md

## Delinquency Management

### Functional Tests

| TC ID         | Test Case                                                                   | Preconditions               | Steps                                                                                  | Expected Result                                       | Priority |
| ------------- | --------------------------------------------------------------------------- | --------------------------- | -------------------------------------------------------------------------------------- | ----------------------------------------------------- | -------- |
| MF-DELINQ-001 | View delinquency buckets or ranges                                          | Delinquency feature enabled | 1. Navigate to Delinquency configuration                                               | Delinquency ranges/buckets are displayed              | High     |
| MF-DELINQ-002 | Create delinquency bucket successfully                                      | Feature enabled             | 1. Click Create Delinquency Bucket<br>2. Enter name and age/range details<br>3. Submit | Delinquency bucket is created successfully            | High     |
| MF-DELINQ-003 | Edit delinquency bucket                                                     | Existing bucket exists      | 1. Open bucket<br>2. Edit values<br>3. Submit                                          | Changes are saved successfully                        | Medium   |
| MF-DELINQ-004 | View delinquent loans grouped by bucket                                     | Delinquent loans exist      | 1. Open delinquency view/report                                                        | Loans are categorized into correct delinquency ranges | High     |
| MF-DELINQ-005 | Configure delinquency classification linked to loan product where supported | Loan product exists         | 1. Open product delinquency settings<br>2. Link classification<br>3. Save              | Product stores delinquency configuration              | Medium   |

### Negative Tests

| TC ID         | Test Case                                               | Preconditions                         | Steps                                        | Expected Result                               | Priority |
| ------------- | ------------------------------------------------------- | ------------------------------------- | -------------------------------------------- | --------------------------------------------- | -------- |
| MF-DELINQ-006 | Create bucket with overlapping ranges                   | Existing bucket ranges exist          | 1. Create new overlapping range<br>2. Submit | Validation prevents overlapping configuration | High     |
| MF-DELINQ-007 | Create bucket with invalid min/max range                | None                                  | 1. Enter invalid boundaries<br>2. Submit     | Validation error shown                        | High     |
| MF-DELINQ-008 | Delete or disable bucket in active use where restricted | Bucket linked to active configuration | 1. Attempt delete/disable                    | Business rule blocks unsafe change            | Medium   |

### Additional Coverage Tests

| TC ID         | Test Case                                                                        | Preconditions                  | Steps                                                                         | Expected Result                                                                          | Priority |
| ------------- | -------------------------------------------------------------------------------- | ------------------------------ | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | -------- |
| MF-DELINQ-009 | Delinquency categorization updates after repayment                               | Delinquent loan exists         | 1. Post repayment reducing overdue days/amount<br>2. Refresh delinquency view | Loan bucket changes according to updated delinquency state                               | High     |
| MF-DELINQ-010 | Write-off or closure removes loan from active delinquency population as expected | Written-off/closed loan exists | 1. Change loan status appropriately<br>2. Reopen delinquency report           | Loan no longer appears in active delinquency bucket population unless designed otherwise | High     |
