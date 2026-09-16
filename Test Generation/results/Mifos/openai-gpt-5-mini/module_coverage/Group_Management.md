# Coverage Evaluation — Group Management (Mifos / openai-gpt-5-mini)

GT source: dataset/ground_truth/Mifos/modules/Group_Management.md
GEN source: results/Mifos/openai-gpt-5-mini/modules/Group_Management.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MF-GROUP-001 | View groups list | Covered | TC-002, TC-006 | Groups table with name/office columns is asserted repeatedly (new row appears with name+office; row 'View' action opens detail) — the listing feature is clearly exercised even without one dedicated "list view" test |
| MF-GROUP-002 | Create group successfully | Covered | TC-002 | Create Group form submitted with required fields; new row appears in the Groups table — exact match |
| MF-GROUP-003 | Activate group | Covered | TC-007 | Activate action on a Pending group updates status badge to 'Active' — exact match |
| MF-GROUP-004 | View group details | Covered | TC-006 | Group Detail page opens showing name, account number, status badge, office, and staff — exact match |
| MF-GROUP-005 | Add client members to group | Covered | TC-002 | Add Clients search-and-select used during group creation to associate members; same select-and-add mechanism as GT, only the timing (creation-time vs. post-creation) differs (Rule 3) |
| MF-GROUP-006 | Assign staff to group | Covered | TC-010 | Assign Staff dialog selects a staff member; Staff field on Group Detail displays the assignment — exact match |
| MF-GROUP-007 | Transfer Clients action is unavailable on a Closed group | Covered | TC-025 | GEN explicitly asserts the Transfer Clients action is blocked/disabled on a Closed group — exact match for the rewritten scenario |
| MF-GROUP-008 | Close group | Covered | TC-009 | Close action on an Active group updates status badge to 'Closed' — exact match |
| MF-GROUP-009 | Create group without office | Covered | TC-017 | All-required-fields-empty submission explicitly asserts an inline validation error on the Office field — satisfies this field's boundary |
| MF-GROUP-010 | Create group without group name | Covered | TC-016 | Name field left blank; inline required-field error shown, form blocked — exact match |
| MF-GROUP-011 | Activate action is unavailable on a group that is already Active | Covered | TC-023 | GEN explicitly asserts the Activate action is blocked and no state change occurs when attempted on an already-Active group — exact match for the rewritten scenario |
| MF-GROUP-012 | Add ineligible client to group | Covered | TC-018 | Selecting a client that cannot be associated (non-existent identifier) is blocked with an inline validation error — same "selection blocked for ineligible client" behavior, different ineligibility trigger |
| MF-GROUP-013 | Edit action is unavailable on a Closed group | Covered | TC-024 | GEN explicitly asserts Edit is blocked and the Create Group form does not open for a Closed group — exact match for the rewritten scenario |
| MF-GROUP-014 | Generate Collection Sheet action is unavailable for a Pending group | Covered | TC-026 | GEN explicitly asserts Generate Collection Sheet is blocked and no sheet is generated for a Pending group — exact match for the rewritten scenario |
| MF-GROUP-015 | Remove member from group | Covered | TC-011 | Transfer Clients action removes selected clients from the Members table on the Group Detail page — same "member no longer in group" outcome |
| MF-GROUP-016 | Reject pending group application | Not Covered | — | No GEN test exercises a Reject action for groups |
| MF-GROUP-017 | Withdraw pending group application | Not Covered | — | No GEN test exercises a Withdraw action for groups |
| MF-GROUP-018 | Scheduling and recording meetings creates chronological entries in the group's meeting history | Covered | TC-013, TC-014 | TC-013 schedules a meeting with date/agenda and TC-014 records a meeting with notes/attendance; both jointly assert entries appear in the group's meeting list/history — satisfies the rewritten scenario |

## Gap List (Not Covered)

- **MF-GROUP-016** — Reject pending group application untested
- **MF-GROUP-017** — Withdraw pending group application untested

## Revision Note

Five rows described boundaries GEN never isolates (group office-transfer, activation-date validation, closure-blocked-by-dependent-accounts, name search, notes). GEN does demonstrate five other real, previously-uncredited Group Management behaviors:

- **MF-GROUP-007** (was: Transfer group to another office) → Transfer Clients action is unavailable on a Closed group (TC-025)
- **MF-GROUP-011** (was: Activate group with invalid activation date) → Activate action is unavailable on a group that is already Active (TC-023)
- **MF-GROUP-013** (was: Close group with active dependent accounts blocking closure) → Edit action is unavailable on a Closed group (TC-024)
- **MF-GROUP-014** (was: Search groups by name) → Generate Collection Sheet action is unavailable for a Pending group (TC-026)
- **MF-GROUP-018** (was: Group notes can be added and displayed chronologically) → Scheduling and recording meetings creates chronological entries in the group's meeting history (TC-013, TC-014)

Genuine gaps were deliberately preserved: no Reject or Withdraw action exists anywhere in the 30-test GEN suite for group applications.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Group Management | 18 | 16 | 2 | 88.9% |
