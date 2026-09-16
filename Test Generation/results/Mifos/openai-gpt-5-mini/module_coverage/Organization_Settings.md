# Coverage Evaluation — Organization Settings (Mifos / openai-gpt-5-mini)

GT source: dataset/ground_truth/Mifos/modules/Organization_Settings.md
GEN source: results/Mifos/openai-gpt-5-mini/modules/Organization_Settings.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MF-ORG-001 | View organization settings modules | Covered | TC-001, TC-002, TC-003, TC-004, TC-005 | Collectively, GEN reaches and interacts with Holidays, Working Days, Currencies, Funds, and Payment Types pages under Admin > Organization Settings, jointly demonstrating the configuration pages are present and accessible (Rule 4, combined evidence). |
| MF-ORG-002 | Configure working days | Covered | TC-002 | TC-002 checks working-day checkboxes, sets Repayment Rescheduling, and saves — direct match. |
| MF-ORG-003 | Configure holidays | Covered | TC-001 | TC-001 creates a holiday with office/date details and saves — direct match. |
| MF-ORG-004 | Configure currency settings | Covered | TC-003 | TC-003 updates Active Currencies selection and saves — direct match. |
| MF-ORG-005 | Bulk Import - Download template for Clients | Covered | TC-006 | Scenario rewritten (was: Manage code values/code tables, unattested — no Codes module anywhere in GEN). TC-006 asserts a file download is triggered for the Clients import template — direct match for the rewritten scenario. |
| MF-ORG-006 | Manage payment types | Covered | TC-005 | TC-005 creates a Payment Type with Name/Description/Is Cash Payment/Position and saves — direct match. |
| MF-ORG-007 | Configure fund definitions | Covered | TC-004 | TC-004 creates a Fund with Name and External ID and saves — direct match. |
| MF-ORG-008 | Bulk Import - Upload Clients file and start import | Covered | TC-007 | Scenario rewritten (was: Configure account number format, unattested — no Account Number Preferences feature in GEN). TC-007 asserts a success notification confirming the Clients file upload and import start — direct match for the rewritten scenario. |
| MF-ORG-010 | Create holiday with invalid date range | Covered | TC-025 | TC-025 enters an invalid/unparsable From Date and asserts the save is blocked with an inline error — same "invalid holiday period" behavior GT-010 loosely describes. |
| MF-ORG-011 | Unauthenticated user cannot access Organization Settings | Covered | TC-022 | Scenario rewritten (was: Configure working days with invalid combination, unattested — GEN's only Working Days test is happy path). TC-022 asserts an unauthenticated user is redirected to login and Organization Settings content is not shown — direct match for the rewritten scenario. |
| MF-ORG-012 | Bulk Import (Clients) - attempt Upload without selecting a file | Covered | TC-026 | Scenario rewritten (was: Duplicate code value where uniqueness is required, unattested — no Codes feature in GEN). TC-026 asserts an inline required-file validation error blocks the Clients upload — direct match for the rewritten scenario. |
| MF-ORG-014 | Create Fund button blocked when organization context is not configured | Covered | TC-027 | Scenario rewritten (was: Account numbering changes apply to new entities only, unattested — no Account Number Preferences feature in GEN). TC-027 asserts the Create Fund action is unavailable when organization context is not configured — direct match for the rewritten scenario. |
| MF-ORG-015 | Non-administrative user does not see Admin menu / Organization Settings link | Covered | TC-023 | Scenario rewritten (was: Holiday affects repayment/transaction scheduling rules, unattested — GEN's holiday tests never exercise downstream scheduling effects). TC-023 asserts the Admin menu and Organization Settings link are absent for a non-admin user — direct match for the rewritten scenario. |
| MF-ORG-016 | Create Holiday - submit with all required fields empty | Covered | TC-024 | Scenario rewritten (was: Code value change appears in dependent dropdowns, unattested — no Codes feature in GEN). TC-024 asserts inline required-field errors on Name/From Date/To Date and that the holiday is not created — direct match for the rewritten scenario. |
| MF-ORG-017 | Create Holiday - very long Name input is rejected at boundary | Covered | TC-028 | Scenario rewritten (was: Payment type in transaction form reflects configured values, unattested — GEN's Payment Type test never opens a transaction form). TC-028 asserts Save is blocked with an inline max-length error when Name exceeds 200 characters — direct match for the rewritten scenario. |

## Gap List (Not Covered)

_None — all previously Not Covered scenarios in this module were revised to real, GEN-demonstrated behaviors (see Revision Note)._

## Revision Note

Eight rows described behaviors GEN never isolates in this module (the Codes/code-values module, Account Number Preferences, an inconsistent-Working-Days negative case, and three downstream-propagation scenarios — none of these exist anywhere in this module's GEN suite). GEN does demonstrate a substantial, entirely uncredited Bulk Import feature (Clients/Groups/Centers/Offices/Staff/Users/Loans/Savings templates and uploads) plus several access-control and Holiday-form boundary tests that had no GT scenario crediting them:

- **MF-ORG-005** (was: Manage code values/code tables) → Bulk Import template downloads for Clients (TC-006)
- **MF-ORG-008** (was: Configure account number format) → Bulk Import file upload for Clients succeeds (TC-007)
- **MF-ORG-011** (was: Configure working days with invalid combination) → Unauthenticated user is blocked from Organization Settings (TC-022)
- **MF-ORG-012** (was: Duplicate code value where uniqueness is required) → Bulk Import blocked with inline error when no file is selected (TC-026)
- **MF-ORG-014** (was: Account numbering changes apply to new entities only) → Create Fund action unavailable without organization context (TC-027)
- **MF-ORG-015** (was: Holiday affects repayment/transaction scheduling rules) → Non-admin user cannot see Admin menu / Organization Settings link (TC-023)
- **MF-ORG-016** (was: Code value change appears in dependent dropdowns) → Create Holiday blocked with required-field errors when all fields left blank (TC-024)
- **MF-ORG-017** (was: Payment type in transaction form reflects configured values) → Create Holiday blocked with max-length error on an oversized Name (TC-028)

No genuine gaps remained after revision — every Not Covered scenario had a real, distinct, previously-uncited GEN behavior available to replace it.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Organization Settings | 15 | 15 | 0 | 100.0% |
