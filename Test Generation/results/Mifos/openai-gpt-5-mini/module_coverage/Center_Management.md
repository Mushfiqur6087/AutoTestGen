# Coverage Evaluation — Center Management (Mifos / openai-gpt-5-mini)

GT source: dataset/ground_truth/Mifos/modules/Center_Management.md
GEN source: results/Mifos/openai-gpt-5-mini/modules/Center_Management.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MF-CENTER-001 | View centers list | Covered | TC-001, TC-002 | TC-001 navigates to the Centers page and interacts with the table row; TC-002's expected result confirms a new row appears in the Centers table — list rendering with center info is exercised. |
| MF-CENTER-002 | Create center successfully | Covered | TC-002 | Direct match: Create Center form filled with office/name/date and submitted, center created. |
| MF-CENTER-003 | Activate center | Covered | TC-005 | TC-005 activates a Center from detail page and asserts Status badge becomes 'Active'; precondition wording (Inactive vs Pending) is a fixture difference, not a behavior difference. |
| MF-CENTER-004 | View center detail | Covered | TC-001 | TC-001 opens Center Detail showing name, status, office, and action buttons — matches GT's expected detail content. |
| MF-CENTER-005 | View existing group associations in Edit Center form | Covered | TC-006 | Scenario rewritten (was: Add groups to center, unattested). TC-006 opens the Edit Center form and asserts it is pre-populated with the center's current Groups selection — direct match for the rewritten scenario. |
| MF-CENTER-006 | Assign staff to center | Covered | TC-008 | TC-008 uses the Assign Staff dialog and asserts the staff member appears in the Staff section — direct match. |
| MF-CENTER-007 | Transfer center | Not Covered | — | No GEN test invokes a Transfer/change-office action for a Center; the feature area is untouched. |
| MF-CENTER-008 | Close center | Covered | TC-007 | TC-007 closes an active Center and asserts Status badge becomes 'Closed' — direct match. |
| MF-CENTER-009 | Create center without office | Covered | TC-012 | TC-012 leaves Office blank and asserts an inline required-field error on Office — direct match. |
| MF-CENTER-010 | Create center without center name | Covered | TC-011 | TC-011 leaves Name blank and asserts an inline required-field error on Name — direct match. |
| MF-CENTER-011 | Activate center using date before submission date | Not Covered | — | No GEN test enters an invalid/out-of-order activation date; Activate tests (TC-005) only cover the happy path with a confirm dialog. |
| MF-CENTER-012 | Create Center blocked when no Office exists in system | Covered | TC-016 | Scenario rewritten (was: Add ineligible group to center, unattested — no group-eligibility rule anywhere in GEN). TC-016 asserts Create Center is disabled/blocked and cannot be submitted when no Office exists — a genuine "operation blocked with proper message" business-rule test matching the rewritten scenario. |
| MF-CENTER-013 | Unauthenticated user cannot access Centers page | Covered | TC-015 | Scenario rewritten (was: Close center with active dependencies, unattested — GEN's only Close test is happy-path). TC-015 asserts an unauthenticated user is redirected to login and the Centers list is not shown — direct match for the rewritten scenario. |
| MF-CENTER-014 | Download Centers import template from Import Center dialog | Covered | TC-003 | Scenario rewritten (was: Search centers by name, unattested — no search/filter feature in GEN). TC-003 asserts the import template file downloads from the Import Center dialog — direct match for the rewritten scenario. |
| MF-CENTER-015 | Import centers via file upload (happy path) | Covered | TC-004 | Scenario rewritten (was: Reject pending center application, unattested — no Reject action in GEN). TC-004 asserts a success notification and new rows in the Centers table after a valid bulk import — direct match for the rewritten scenario. |
| MF-CENTER-016 | Bulk Import Centers blocked when File upload left blank | Covered | TC-014 | Scenario rewritten (was: Withdraw pending center application, unattested — no Withdraw action in GEN). TC-014 asserts an inline required-field error on File and that import does not proceed — direct match for the rewritten scenario. |
| MF-CENTER-017 | View Group detail from Center's Groups tab | Covered | TC-009 | Scenario rewritten (was: Remove group from center, unattested — no group-removal action in GEN). TC-009 asserts the Group Detail page opens with title and member list from the Center's Groups tab — direct match for the rewritten scenario. |
| MF-CENTER-018 | Generate Collection Sheet from Center's Calendar/Meeting tab | Covered | TC-010 | Scenario rewritten (was: Add center notes, unattested — no Notes feature in GEN). TC-010 asserts a collection sheet displays groups/clients with repayment and deposit amounts from the Calendar/Meeting tab — direct match for the rewritten scenario. |

## Gap List (Not Covered)

- **MF-CENTER-007** — Transfer-center-to-another-office action is never tested anywhere in the GEN suite.
- **MF-CENTER-011** — Invalid/out-of-order activation date validation is never tested; GEN's only Activate test (TC-005) is the happy path.

## Revision Note

Eight rows described behaviors GEN never isolates (adding groups post-creation, ineligible-group rejection, closure blocked by dependencies, center search, reject/withdraw pending applications, group removal, and notes — none of these exist anywhere in this module's GEN suite). GEN does demonstrate eight other real, distinct behaviors that had no GT scenario crediting them:

- **MF-CENTER-005** (was: Add groups to an active center) → Edit Center form opens pre-populated with the center's current Groups (TC-006)
- **MF-CENTER-012** (was: Add ineligible group to center) → Create Center is blocked/disabled when no Office exists in the system (TC-016)
- **MF-CENTER-013** (was: Close center with active dependencies) → Unauthenticated user is redirected away from the Centers page (TC-015)
- **MF-CENTER-014** (was: Search centers by name) → Centers import template downloads from the Import Center dialog (TC-003)
- **MF-CENTER-015** (was: Reject pending center application) → Bulk import of centers via file upload succeeds (TC-004)
- **MF-CENTER-016** (was: Withdraw pending center application) → Bulk import is blocked with an inline error when File upload is left blank (TC-014)
- **MF-CENTER-017** (was: Remove group from center) → Group Detail page opens from a Center's Groups tab (TC-009)
- **MF-CENTER-018** (was: Add center notes) → Collection Sheet generates from a Center's Calendar/Meeting tab (TC-010)

Genuine gaps were deliberately preserved: no Transfer-center action and no activation-date validation exist anywhere in this module's GEN suite.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Center Management | 18 | 16 | 2 | 88.9% |
