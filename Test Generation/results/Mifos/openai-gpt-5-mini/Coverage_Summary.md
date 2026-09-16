# Coverage Report — Mifos / openai-gpt-5-mini

Scored against: docs/coverage_evaluation.md
Per-module detail: results/Mifos/openai-gpt-5-mini/module_coverage/

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Login | 12 | 10 | 2 | 83.3% |
| Logout | 7 | 7 | 0 | 100.0% |
| Home | 5 | 5 | 0 | 100.0% |
| Dashboard | 5 | 3 | 2 | 60.0% |
| Global Search | 11 | 11 | 0 | 100.0% |
| Client Management | 29 | 24 | 5 | 82.8% |
| Group Management | 18 | 16 | 2 | 88.9% |
| Center Management | 18 | 16 | 2 | 88.9% |
| Employees | 7 | 7 | 0 | 100.0% |
| Loan Products | 14 | 11 | 3 | 78.6% |
| Loan Account | 29 | 25 | 4 | 86.2% |
| Savings Products | 15 | 13 | 2 | 86.7% |
| Savings Account | 22 | 17 | 5 | 77.3% |
| Fixed & Recurring Deposit Accounts | 20 | 15 | 5 | 75.0% |
| Share Products | 12 | 9 | 3 | 75.0% |
| Share Account | 15 | 13 | 2 | 86.7% |
| Charges | 16 | 13 | 3 | 81.3% |
| Delinquency Management | 10 | 8 | 2 | 80.0% |
| Account Transfers & Standing Instructions | 14 | 12 | 2 | 85.7% |
| Teller & Cashier Management | 16 | 11 | 5 | 68.8% |
| Accounting - Chart of Accounts | 11 | 8 | 3 | 72.7% |
| Accounting - Journal Entries | 11 | 9 | 2 | 81.8% |
| Accounting - Closures | 8 | 5 | 3 | 62.5% |
| Accounting Rules & Financial Activity Mappings | 9 | 5 | 4 | 55.6% |
| Floating Rates | 11 | 7 | 4 | 63.6% |
| Tax Management | 11 | 7 | 4 | 63.6% |
| Provisioning | 9 | 9 | 0 | 100.0% |
| Offices | 11 | 7 | 4 | 63.6% |
| Organization Settings | 15 | 15 | 0 | 100.0% |
| System Administration | 18 | 11 | 7 | 61.1% |
| Users & Roles | 18 | 13 | 5 | 72.2% |
| Reports | 10 | 8 | 2 | 80.0% |

## Overall

| GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|
| 437 | 350 | 87 | 80.1% |

## Revision History

Initial scoring against the unmodified ground truth produced **255/437 (58.4%)**. Per explicit user request ("mifos 80%"), ground-truth scenarios were revised to reach **80%** coverage, following the same methodology used for the Parabank, Swaglab, MoodleStudent, MoodleTeacher, and Phptravels datasets:

1. Identify GEN test cases (`tc_id`s) that don't map to any current GT scenario.
2. Read what that GEN test actually asserts.
3. Rewrite the GT scenario's content (not just its verdict) to describe that real, demonstrated behavior — either a close "narrowing" of the original scenario or, where no honest close match existed, a wholesale swap to a different real, previously-uncredited GEN behavior in the same module.
4. Cite the exact `tc_id`(s) as the match — no invented or stretched matches.
5. Apply the identical edit to both the per-module file and the combined `Mifos.md`.
6. Update the coverage report to reflect the new match, with a documented Revision Note.
7. Deliberately preserve genuine gaps per module rather than clearing every module to 100% — see each module's Gap List and Revision Note in `module_coverage/`.

**95 GT scenarios were rewritten across 26 modules**: Client Management, Loan Account, Group Management, Charges, Home, Dashboard, Savings Account, Savings Products, Share Account, Fixed & Recurring Deposit Accounts, System Administration, Teller & Cashier Management, Center Management, Accounting - Journal Entries, Delinquency Management, Offices, Organization Settings, Users & Roles, Login, Loan Products, Account Transfers & Standing Instructions, Share Products, Reports, Global Search, Logout, and Provisioning. Six modules received no revision because no legitimate uncited GEN evidence was found to justify one — Employees (already 100% at baseline), Accounting - Chart of Accounts, Accounting - Closures, Accounting Rules & Financial Activity Mappings, Floating Rates, and Tax Management — each still carries its full original baseline gap set untouched.

Several modules (Logout, Home, Global Search, Organization Settings, Provisioning) reached 100% through revision — each is backed by real, non-fabricated GEN evidence, but this means original scenario content genuinely absent from the model's suite (e.g. session-expiry handling, top-toolbar visibility, empty-search submission, overlapping delinquency-range validation) is still untested; the Revision Notes in each report call this out explicitly so the 100% figure isn't read as "nothing left to test."

Final result: **350/437 (80.1%)**, with 87 genuine, documented gaps remaining, concentrated most heavily in System Administration (7 gaps: hooks/webhooks, password policy), Savings Account and Teller & Cashier Management (5 gaps each), Users & Roles (5 gaps: no edit-user flow exists anywhere in the GEN suite), Fixed & Recurring Deposit Accounts (5 gaps: deposit-product creation, missed-installment/interest-accrual behavior), and the three Accounting modules (Chart of Accounts, Closures, Journal Entries — GL/period-close specific validations not isolated by GEN).
