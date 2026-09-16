# Coverage Evaluation — Employees (Mifos / openai-gpt-5-mini)

GT source: dataset/ground_truth/Mifos/modules/Employees.md
GEN source: results/Mifos/openai-gpt-5-mini/modules/Employees.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MF-EMP-001 | View employees list | Covered | TC-001, TC-002 | Employees table rows are asserted to show Name, Office, Is Loan Officer indicator, and Status after creation — the listing feature with office/status is clearly exercised |
| MF-EMP-002 | Create employee successfully | Covered | TC-001 | Create Employee form submitted with Office/First Name/Last Name; new row appears in the Employees table — exact match |
| MF-EMP-003 | Edit employee details | Covered | TC-004 | Mobile Number and Office/Status edited and saved; Employee Detail page displays the updated values — exact match, including the save/persist assertion |
| MF-EMP-004 | View employee profile | Covered | TC-003 | Employee Detail page shows Name, Office, Is Loan Officer, Mobile Number, Joining Date, External ID, and Status — exact match |
| MF-EMP-005 | Assign employee to office correctly | Covered | TC-001, TC-004 | Office selected at creation (TC-001) and changeable at edit time (TC-004), with the Office value persisted and displayed — same linkage-saved behavior |
| MF-EMP-006 | Create employee without first name | Covered | TC-005 | First Name left blank; inline required-field error shown, form blocked — exact match |
| MF-EMP-007 | Create employee without office | Covered | TC-006 | All-required-fields-empty submission explicitly asserts an inline validation error on the Office field — satisfies this field's boundary |

## Gap List (Not Covered)

None — all 7 GT scenarios are Covered.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Employees | 7 | 7 | 0 | 100.0% |
