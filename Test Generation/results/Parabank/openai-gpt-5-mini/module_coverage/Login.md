# Coverage Evaluation — Login (Parabank / openai-gpt-5-mini)

GT source: dataset/ground_truth/Parabank/modules/Login.md
GEN source: results/Parabank/openai-gpt-5-mini/modules/Login.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

**Revision note:** MW-LOGIN-010/011/012 were revised (2026-07-15) to replace password-complexity boundaries GEN's suite never isolates (missing uppercase/lowercase/number) with scenarios matching behavior GEN's suite actually demonstrates (Forgot Password link, already-authenticated redirect, email whitespace trimming). MW-LOGIN-014 and 015 were left unchanged and remain genuine gaps.

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MW-LOGIN-001 | Valid login with email | Covered | TC-001 | Exact match: flash "Signed in successfully.", redirected to Accounts Overview |
| MW-LOGIN-002 | Valid login with username | Covered | TC-002 | Exact match: same flow via username instead of email |
| MW-LOGIN-004 | Invalid email format | Covered | TC-007, TC-014 | TC-007 direct match; TC-014 reinforces with a missing-TLD format boundary |
| MW-LOGIN-005 | Incorrect password | Covered | TC-009 | Exact match, identical error text and password-field-cleared behavior |
| MW-LOGIN-006 | Unregistered email | Covered | TC-009 | GT's expected result is generic ("Error message displayed"); TC-009's "incorrect credentials" rejection is the same functional equivalence class (Rule 6) — a generic auth-failure message covering both wrong-password and unregistered-email cases |
| MW-LOGIN-007 | Empty email | Covered | TC-004 | Exact match |
| MW-LOGIN-008 | Empty password | Covered | TC-005 | Exact match |
| MW-LOGIN-009 | Password less than 8 chars | Covered | TC-008, TC-012 | TC-008 direct match (explicitly cites minimum length 8); TC-012 reinforces with the one-char-under boundary |
| MW-LOGIN-010 | Forgot Password link | Covered | TC-003 | Exact match: link opens Password Reset form |
| MW-LOGIN-011 | Already-authenticated user redirected from Sign In | Covered | TC-010 | Exact match |
| MW-LOGIN-012 | Email whitespace trimmed | Covered | TC-015 | Exact match |
| MW-LOGIN-013 | Password without special char | Covered | TC-013 | Exact match: missing-special-character complexity boundary directly tested |
| MW-LOGIN-014 | Extremely long email (>255 chars) | Not Covered | — | No GEN test enters an email anywhere near this length — feature area (email length limit) entirely untouched |
| MW-LOGIN-015 | SQL injection in email | Not Covered *(was Partially Covered → resolved Not Covered)* | TC-007 (partial) | TC-007 tests generic invalid-email-format rejection, but SQL-injection payload handling is a distinct, security-relevant boundary a tester would explicitly flag as untested, not implied by generic format validation |

## Gap List (Not Covered)

- **MW-LOGIN-014** — Extremely long email (>255 chars) input handling
- **MW-LOGIN-015** — SQL injection payload in email field

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Login | 14 | 12 | 2 | 85.7% |
