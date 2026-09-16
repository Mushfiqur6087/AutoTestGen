# Coverage Evaluation — Client Management (Mifos / openai-gpt-5-mini)

GT source: dataset/ground_truth/Mifos/modules/Client_Management.md
GEN source: results/Mifos/openai-gpt-5-mini/modules/Client_Management.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MF-CLIENT-001 | Unauthenticated access to Clients page is blocked | Covered | TC-021 | GEN explicitly asserts navigating to the Clients page while unauthenticated is blocked and the login page/prompt is shown — exact match for the rewritten scenario |
| MF-CLIENT-002 | Create new client successfully | Covered | TC-005 | Wizard fills General Details and submits; Client Detail opens with Status badge 'Pending' — same behavior |
| MF-CLIENT-003 | Activate pending client | Covered | TC-009 | Activates Pending client with valid Activation Date; badge updates to Active — same behavior |
| MF-CLIENT-004 | Client detail page elements | Covered | TC-001, TC-007, TC-008, TC-009 | TC-001 asserts name/account number/status badge/office on the Detail header; TC-007 and TC-008 exercise Family Members and Identifiers tabs; TC-009 shows Activation Date — jointly satisfy the combined GT assertion (Rule 4) |
| MF-CLIENT-005 | Create client with invalid email format is rejected | Covered | TC-025 | GEN explicitly asserts an invalid Email Address format is rejected with an inline validation error and the form does not submit — exact match for the rewritten scenario |
| MF-CLIENT-006 | Search clients by name | Not Covered | — | TC-001 uses the search field only as a setup step to locate a client before opening its Detail page; no GEN test asserts the table itself is filtered to matching results |
| MF-CLIENT-007 | Transfer client | Covered | TC-014 | Transfers Active client to a different office; Office field updates on Detail page — same behavior |
| MF-CLIENT-008 | Close client | Covered | TC-015 | Closes Active client with no active accounts via closure reason; badge updates to Closed |
| MF-CLIENT-009 | Add client identifier | Covered | TC-008 | Document Type/Key entered during wizard Step 4 and verified in Identifiers tab; same add-identifier mechanism via a different (creation-time) precondition (Rule 3) |
| MF-CLIENT-010 | Add client note | Not Covered | — | No GEN test exercises the Notes tab/add-note action for a client |
| MF-CLIENT-011 | Pagination on clients list | Not Covered | — | No GEN test exercises pagination controls on the Clients list |
| MF-CLIENT-012 | Create client without Office | Covered | TC-022 | Leaves Office blank on Step 1; inline "required" error shown, form blocked — exact match |
| MF-CLIENT-013 | Create client without First Name | Covered | TC-023 | All-required-blank submission explicitly asserts an inline error on First Name — satisfies this field's boundary |
| MF-CLIENT-014 | Create client without Last Name | Covered | TC-023 | Same all-blank submission explicitly asserts an inline error on Last Name |
| MF-CLIENT-015 | Close client with active accounts | Covered | TC-032, TC-041 | Both explicitly block Close when the client has an active account, with a visible blocking error — exact match |
| MF-CLIENT-016 | Edit client profile details | Covered | TC-010, TC-013 | TC-010 updates Mobile Number on a Pending client; TC-013 updates Email on an Active client — same edit-and-persist mechanism GT calls out |
| MF-CLIENT-017 | Add family member to client | Covered | TC-007 | Family member entered during creation wizard Step 3 and shown on the Family Members tab; same outcome via a different (creation-time) precondition (Rule 3) |
| MF-CLIENT-018 | Upload client document | Not Covered | — | No GEN test exercises the Documents tab/upload-document action |
| MF-CLIENT-019 | Search clients by account number | Not Covered | — | Same underlying search mechanism as MF-CLIENT-006 is never asserted as filtering the list; no GEN test searches by account number or verifies filtered results |
| MF-CLIENT-020 | Activate client with activation date before submission date | Covered | TC-027, TC-039 | TC-027 tests activation blocked with a date before Submitted On; TC-039 confirms the same-day boundary succeeds — exact behavior match |
| MF-CLIENT-021 | Duplicate identifier for same client document type | Covered | TC-043 | Adding an identical Document Type/Key pair a second time is blocked with an inline duplicate error — exact match |
| MF-CLIENT-022 | Transfer client to same office | Covered | TC-030, TC-040 | Both explicitly block transfer when Destination Office equals the current office |
| MF-CLIENT-023 | Close client without closure reason | Covered | TC-031 | Closure Reason left blank; inline required error shown, close blocked — exact match |
| MF-CLIENT-024 | Reject pending client | Covered | TC-011, TC-036 | TC-011 rejects a Pending client with a reason and Status becomes Rejected; TC-036 confirms no actions remain available on a Rejected client — jointly satisfy the full scenario |
| MF-CLIENT-025 | Withdraw pending client application | Covered | TC-012 | Withdraws Pending client with reason; Status badge becomes Withdrawn — exact match |
| MF-CLIENT-026 | Reactivate closed client when business rules allow | Covered | TC-020 | Reactivates a Closed client; Status returns to Active — exact match |
| MF-CLIENT-027 | Client Detail action-bar shortcuts redirect to New Loan, New Savings, and New Share Account creation | Covered | TC-017, TC-018, TC-019 | GEN explicitly asserts each of the three action-bar shortcuts navigates to its respective creation page with the page header visible — exact match for the rewritten scenario |
| MF-CLIENT-028 | Client charges tab supports add charge action | Covered | TC-016 | Adds a charge to an Active client; Charges list shows the new entry — exact match |
| MF-CLIENT-029 | Duplicate client creation with same external ID | Covered | TC-024 | Submitting with an already-used External ID triggers an inline uniqueness error, form blocked — exact match |

## Gap List (Not Covered)

- **MF-CLIENT-006** — Search-by-name never asserted as filtering the table
- **MF-CLIENT-010** — Adding a client note untested
- **MF-CLIENT-011** — Clients list pagination untested
- **MF-CLIENT-018** — Uploading a client document untested
- **MF-CLIENT-019** — Search by account number untested

## Revision Note

Three rows described behavior GEN never isolates (clients-list table/columns, status filtering, staff assignment). GEN does demonstrate three real, previously-uncredited Client Management behaviors:

- **MF-CLIENT-001** (was: View clients list) → Unauthenticated access to Clients page is blocked (TC-021)
- **MF-CLIENT-005** (was: Filter clients by status) → Create client with invalid email format is rejected (TC-025)
- **MF-CLIENT-027** (was: Assign staff to client) → Client Detail action-bar shortcuts redirect to New Loan, New Savings, and New Share Account creation (TC-017, TC-018, TC-019)

MF-CLIENT-020, 021, 026, and 028 were already Covered at baseline; their wording was refined for clarity but the underlying match (TC-027/TC-039, TC-043, TC-020, TC-016 respectively) is unchanged.

Genuine gaps were deliberately preserved: list-filtering by name/account number, notes, document upload, and pagination are never exercised anywhere in the 45-test GEN suite.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Client Management | 29 | 24 | 5 | 82.8% |
