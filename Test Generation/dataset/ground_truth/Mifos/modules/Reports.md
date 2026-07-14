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
| MF-REPORT-009 | Search/filter reports catalog                                        | Multiple reports exist               | 1. Search report name                | Matching reports displayed                                 | Low      |
| MF-REPORT-010 | Scheduled or background report definition visibility where supported | Feature available                    | 1. Open reports admin/settings       | Available scheduled/report metadata is displayed correctly | Low      |
| MF-REPORT-011 | Report output reflects latest committed transactions                 | Report depends on recent transaction | 1. Post transaction<br>2. Run report | Report includes latest data after commit                   | High     |
