# Mifos Banking System Test Cases — Ground Truth

Source: dataset/ground_truth/Mifos/Mifos.md

## Reports

### Functional Tests

| TC ID         | Test Case                                                      | Preconditions                    | Steps                                                    | Expected Result                                               | Priority |
| ------------- | -------------------------------------------------------------- | -------------------------------- | -------------------------------------------------------- | ------------------------------------------------------------- | -------- |
| MF-REPORT-001 | View reports list                                              | User with reporting permission   | 1. Navigate to Reports                                   | Reports page displays available report definitions/categories | High     |
| MF-REPORT-002 | Run report with valid parameters                               | Parameterized report exists      | 1. Open report<br>2. Enter required parameters<br>3. Run | Report output is generated successfully                       | High     |
| MF-REPORT-003 | Run report without parameters when not required                | Non-parameterized report exists  | 1. Open report<br>2. Run report                          | Report output is generated                                    | Medium   |
| MF-REPORT-004 | Export report where supported                                  | Generated report exists          | 1. Run report<br>2. Export to available format           | Export file is generated successfully                         | Medium   |
| MF-REPORT-005 | View report data with large result set pagination or scrolling | Report with large dataset exists | 1. Run report                                            | Results remain readable and usable                            | Medium   |

### Negative Tests

| TC ID         | Test Case                                             | Preconditions                | Steps                                                         | Expected Result                                | Priority |
| ------------- | ----------------------------------------------------- | ---------------------------- | ------------------------------------------------------------- | ---------------------------------------------- | -------- |
| MF-REPORT-006 | Run parameterized report without mandatory parameters | Parameterized report exists  | 1. Open report<br>2. Leave required parameter blank<br>3. Run | Validation error shown                         | High     |
| MF-REPORT-007 | Run report with invalid date range                    | Date-parameter report exists | 1. Provide invalid date range<br>2. Run                       | Validation or backend error handled gracefully | Medium   |

### Additional Coverage Tests

| TC ID         | Test Case                                                            | Preconditions                        | Steps                                | Expected Result                                            | Priority |
| ------------- | -------------------------------------------------------------------- | ------------------------------------ | ------------------------------------ | ---------------------------------------------------------- | -------- |
| MF-REPORT-009 | Unauthenticated user cannot access the Reports page | User is not authenticated | 1. Navigate to the Reports page URL or click Reports in top navigation | Access is blocked; the user is redirected to the login screen; the Reports page is not displayed | Low      |
| MF-REPORT-010 | Export actions are unavailable before a report has been run | No report has been run in the current session | 1. Open a report's Parameters form<br>2. Do not click Run Report<br>3. Attempt to locate or click Export to Excel or other export buttons | Export actions are not visible or are disabled when no output table exists; no file download is initiated | Low      |
| MF-REPORT-011 | Run Report when system contains no relevant data shows an empty-result indicator | System contains no relevant transactional/master data for the selected parameters | 1. Open a report's Parameters form and fill valid values<br>2. Click Run Report | Report generation produces no rows; a visible message informs the user no data is available for the selected parameters | High     |
