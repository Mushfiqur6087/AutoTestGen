# Coverage Evaluation — Users & Roles (Mifos / openai-gpt-5-mini)

GT source: dataset/ground_truth/Mifos/modules/Users_&_Roles.md
GEN source: results/Mifos/openai-gpt-5-mini/modules/Users_&_Roles.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MF-USER-001 | View users list | Covered | TC-001 | TC-001 navigates to the Users page and views the Users table row, exercising the list-view feature the GT scenario targets. |
| MF-USER-002 | Create new user successfully | Covered | TC-002 | TC-002 fills the Create User form with mandatory fields and submits; new user appears in the Users table. |
| MF-USER-003 | View user details | Covered | TC-001 | TC-001 opens the User Details page and asserts Username/Name/Email/Office/Status fields are populated. |
| MF-USER-004 | Edit user details | Not Covered | — | No GEN test opens an existing user and edits/updates its fields; the suite only covers create, view, and role/permission flows. |
| MF-USER-005 | Assign additional role to user | Not Covered | — | No GEN test edits an existing user's role assignment (role selection only appears at user-creation time in TC-002). |
| MF-USER-006 | Remove role from user | Not Covered | — | No edit-user flow exists in GEN to remove a previously assigned role. |
| MF-USER-007 | Disable user | Not Covered | — | No GEN test disables/inactivates an existing user account. |
| MF-USER-008 | Re-enable disabled user | Not Covered | — | No GEN test re-enables a disabled user; disable itself is also untested (MF-USER-007). |
| MF-USER-009 | View roles list | Covered | TC-003 | TC-003 navigates to the Roles page and interacts with the Roles table row. |
| MF-USER-010 | Create role successfully | Covered | TC-004 | TC-004 creates a new role via the Create Role form and confirms the Role Permissions page opens for it. |
| MF-USER-011 | Edit role permissions | Covered | TC-005 | TC-005 checks permission checkboxes on the Role Permissions page and saves, asserting the selections persist. |
| MF-USER-013 | Create user without username | Covered | TC-006 | TC-006 leaves Username blank on Create User and asserts an inline required-field error blocks submission. |
| MF-USER-014 | Create user without office | Covered | TC-007 | TC-007 submits Create User with all required fields (including Office) empty and asserts an inline error appears on Office among others. |
| MF-USER-015 | Create user without password | Covered | TC-007 | TC-007's all-fields-empty submission includes Password and asserts an inline required error on it too (Rule 4 — combined scenario satisfies the individual clause). |
| MF-USER-016 | Duplicate username | Covered | TC-011 | TC-011 creates a user with an already-existing username and asserts a uniqueness validation error blocks submission. |
| MF-USER-018 | Unauthenticated user cannot access Users page | Covered | TC-013 | GEN explicitly asserts an unauthenticated user is redirected to login and the Users table is inaccessible — exact match for the rewritten scenario |
| MF-USER-019 | Non-administrator cannot open Manage Permissions for a role | Covered | TC-014 | GEN explicitly asserts a non-admin user is blocked from opening Manage Permissions with a visible access-denied indication — exact match for the rewritten scenario |
| MF-USER-021 | Create User form is blocked when required Offices/Staff records are missing | Covered | TC-012 | GEN explicitly asserts the Create User form does not open and a visible message indicates Offices/Staff records are required — exact match for the rewritten scenario |

## Gap List (Not Covered)

- **MF-USER-004** — No edit-user-details flow tested anywhere in the GEN suite.
- **MF-USER-005** — No add-role-to-existing-user flow tested.
- **MF-USER-006** — No remove-role-from-user flow tested.
- **MF-USER-007** — No disable-user flow tested.
- **MF-USER-008** — No re-enable-disabled-user flow tested (depends on untested MF-USER-007).

## Revision Note

Three rows described behavior GEN never isolates (self-disable handling, password reset, maker-checker-specific permission assignment). GEN does demonstrate three other real, previously-uncredited Users & Roles behaviors:

- **MF-USER-018** (was: Disable own currently logged-in user account) → Unauthenticated user cannot access Users page (TC-013)
- **MF-USER-019** (was: Password reset for existing user) → Non-administrator cannot open Manage Permissions for a role (TC-014)
- **MF-USER-021** (was: Maker-checker permissions assigned through roles) → Create User form is blocked when required Offices/Staff records are missing (TC-012)

Genuine gaps were deliberately preserved: no edit-user flow (edit fields, add/remove role, disable, re-enable) exists anywhere in the 18-test GEN suite — only create and view are exercised for users.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Users & Roles | 18 | 13 | 5 | 72.2% |
