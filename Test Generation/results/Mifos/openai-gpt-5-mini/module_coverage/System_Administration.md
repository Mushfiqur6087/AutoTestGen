# Coverage Evaluation — System Administration (Mifos / openai-gpt-5-mini)

GT source: dataset/ground_truth/Mifos/modules/System_Administration.md
GEN source: results/Mifos/openai-gpt-5-mini/modules/System_Administration.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MF-SYS-001 | System Administration area is blocked for unauthenticated and non-admin users | Covered | TC-020, TC-021 | TC-020 asserts unauthenticated users are redirected to Login with no System Administration content shown; TC-021 asserts a non-admin user is blocked from all System Administration controls — real, previously-uncredited access-control behavior for the module landing area. |
| MF-SYS-002 | Manage data tables | Covered | TC-014, TC-015, TC-016 | TC-014/015/016 all interact with the Manage Data Tables list (open in edit mode, new row appears after create, list shown after cancel), exercising list viewing. |
| MF-SYS-003 | Create or register data table where supported | Covered | TC-015 | TC-015 creates a new custom data table with a column and asserts it appears in the Manage Data Tables list. |
| MF-SYS-004 | Manage hooks/webhooks configuration | Not Covered | — | No GEN test touches hooks/webhooks configuration anywhere in the suite. |
| MF-SYS-005 | View scheduler jobs | Covered | TC-001, TC-002 | Manage Scheduler Jobs table and job rows are viewed/interacted with across the scheduler-related positive tests. |
| MF-SYS-006 | Run a schedulable job manually where supported | Covered | TC-006 | TC-006 clicks 'Run Now' for a job row and asserts a running-status indicator appears. |
| MF-SYS-007 | Manage password preferences or security settings | Not Covered | — | No GEN test opens or edits password/security policy preferences. |
| MF-SYS-008 | Manage external services or configurations where supported | Not Covered | — | GEN's config-editing tests (TC-008/009/010) operate on Global Configuration flags, a distinct Mifos feature from External Services (e.g. S3/SMTP) — the specific feature area GT targets is untouched. |
| MF-SYS-009 | Manage maker-checker settings | Covered | TC-008, TC-023 | TC-008 demonstrates the generic toggle/save mechanism for a Global Configuration entry, and TC-023's setup steps explicitly navigate to Global Configuration and toggle the maker-checker feature flag — the exact configuration action GT describes. |
| MF-SYS-010 | View audit or application logs where supported | Covered | TC-017 | TC-017 opens an audit entry's details from the Audit Trails table, displaying audit metadata. |
| MF-SYS-012 | Save invalid hook endpoint configuration | Not Covered | — | Hooks are entirely untested (see MF-SYS-004), so invalid-config validation on that form is untested too. |
| MF-SYS-014 | Set invalid password policy values | Not Covered | — | Password/security preferences are entirely untested (see MF-SYS-007). |
| MF-SYS-015 | Scheduler job execution updates last-run status correctly | Covered | TC-006, TC-007 | TC-006 triggers a run and shows a running-status indicator; TC-007 opens Run History showing recent runs with statuses and timestamps — together these cover run-status/metadata reflecting execution. |
| MF-SYS-016 | Maker-checker workflow holds pending action until checker approval | Covered | TC-018, TC-022, TC-023, TC-024, TC-025 | The Pending state and its gating of Approve/Reject actions (disabled when not Pending, disabled when maker-checker off, blocked without a reason) are exercised extensively across these tests, jointly demonstrating actions stay pending until a checker acts. |
| MF-SYS-017 | Checker approval completes pending maker action | Covered | TC-018 | TC-018 approves a Pending audit row and asserts Processing Result becomes 'Approved'. |
| MF-SYS-018 | Checker rejection cancels pending maker action | Covered | TC-019 | TC-019 rejects a Pending audit row with a reason and asserts Processing Result becomes 'Rejected'. |
| MF-SYS-019 | Hook invocation occurs on configured business event | Not Covered | — | Hooks are entirely untested; no test triggers a business event and verifies hook invocation. |
| MF-SYS-020 | Password policy update affects subsequent user password operations | Not Covered | — | No GEN test updates a password policy and then verifies enforcement on a subsequent password operation. |

## Gap List (Not Covered)

- **MF-SYS-004** — Hooks/webhooks configuration entirely untested.
- **MF-SYS-007** — Password/security preference management entirely untested.
- **MF-SYS-008** — External services configuration (distinct from Global Configuration) untested.
- **MF-SYS-012** — Invalid hook endpoint validation untested (depends on untested hooks feature).
- **MF-SYS-014** — Invalid password policy validation untested (depends on untested security settings).
- **MF-SYS-019** — Hook invocation on business events untested.
- **MF-SYS-020** — Password policy update's downstream enforcement effect untested.

## Revision Note

GEN never touches hooks/webhooks, password/security policy, or external-services configuration anywhere in its 32 tests, so those five gaps (MF-SYS-004, 007, 008, 012, 014, 019, 020) are genuine and left untouched. GEN does demonstrate one real, previously-uncredited behavior:

- **MF-SYS-001** (was: View system administration modules) → System Administration area/controls are blocked for unauthenticated users (TC-020) and for authenticated non-admin users (TC-021) — the landing-page-access behavior GEN actually exercises is the negative/gated case, not a positive module listing.

Genuine gaps were deliberately preserved: no hook, password-policy, or external-service feature appears anywhere in this module's GEN suite.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| System Administration | 18 | 11 | 7 | 61.1% |
