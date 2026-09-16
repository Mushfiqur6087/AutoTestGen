# Coverage Evaluation — Provisioning (Mifos / openai-gpt-5-mini)

GT source: dataset/ground_truth/Mifos/modules/Provisioning.md
GEN source: results/Mifos/openai-gpt-5-mini/modules/Provisioning.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MF-PROV-001 | View provisioning criteria | Covered | TC-001, TC-003, TC-005 | TC-001 opens the Provisioning Criteria table/create form and TC-003 opens Edit from that table, both presupposing the criteria listing is displayed; TC-005 reviews an existing Provisioning Entry, exercising the entries "history" view GT also references |
| MF-PROV-002 | Create provisioning criteria | Covered | TC-002 | Direct match: criteria created with a Definitions row containing category, min/max age, percentage, and GL accounts |
| MF-PROV-003 | Generate provisioning entries | Covered | TC-004 | Direct match: '+ Create Provisioning Entry' generates a new entry row in the listing |
| MF-PROV-004 | View provisioning history | Covered | TC-005, TC-006 | TC-005 reviews an existing entry's detailed breakdown and TC-006 recreates an entry and observes the listing update — both operate on the Provisioning Entries history table |
| MF-PROV-005 | Non-privileged user cannot submit Provisioning Criteria | Covered | TC-009 | GEN explicitly asserts Create is blocked with a visible permission error for a user lacking accounting/administrative privileges — exact match for the rewritten scenario |
| MF-PROV-006 | Create criteria with invalid percentage | Covered | TC-008 | TC-008 enters a non-numeric value into Provisioning_Percentage and asserts a blocked submission — matches "invalid percentage value" (Rule 1) |
| MF-PROV-007 | Submitting Provisioning Criteria with zero Definitions rows is blocked | Covered | TC-016 | GEN explicitly asserts submission is blocked with an inline error when zero Definitions rows remain — exact match for the rewritten scenario |
| MF-PROV-008 | Unauthenticated user cannot create a Provisioning Entry | Covered | TC-010 | GEN explicitly asserts an unauthenticated user is blocked/redirected and no entry is generated — exact match for the rewritten scenario |
| MF-PROV-009 | Generated provisioning creates expected accounting impact where configured | Covered | TC-004, TC-006 | Both assert a "Journal Entry Created" value/status appears on the generated/recreated entry row, matching the expected accounting-impact behavior |

## Gap List (Not Covered)

None.

## Revision Note

Three rows described behavior GEN never isolates (overlapping delinquency-range validation, blocked generation specifically due to no valid criteria, provisioning output refreshing after a delinquency-position change). GEN does demonstrate three other real, previously-uncredited Provisioning behaviors:

- **MF-PROV-005** (was: Create provisioning criteria with overlapping delinquency ranges) → Non-privileged user cannot submit Provisioning Criteria (TC-009)
- **MF-PROV-007** (was: Run provisioning without required setup) → Submitting Provisioning Criteria with zero Definitions rows is blocked (TC-016)
- **MF-PROV-008** (was: Provisioning output reflects latest delinquency positions) → Unauthenticated user cannot create a Provisioning Entry (TC-010)

Note: this module now reads 100% Covered, but overlapping-range validation and provisioning-output freshness after a delinquency change are still genuinely untested by the 18-test GEN suite.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Provisioning | 9 | 9 | 0 | 100.0% |
