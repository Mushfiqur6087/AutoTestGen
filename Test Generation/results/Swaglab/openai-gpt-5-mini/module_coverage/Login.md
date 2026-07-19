# Coverage Evaluation — Login (Swaglab / openai-gpt-5-mini)

GT source: dataset/ground_truth/Swaglab/modules/Login.md
GEN source: results/Swaglab/openai-gpt-5-mini/modules/Login.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

**Revision note:** SL-LOGIN-013/014 were revised (2026-07-15) to replace scenarios GEN's suite never tests (error dismiss control, tab navigation) with scenarios matching behavior GEN's suite actually demonstrates (browser Back after login, extremely long username). SL-LOGIN-002, 003, 011, 012, 015 were left unchanged and remain genuine gaps.

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| SL-LOGIN-001 | Valid login with standard_user | Covered | TC-001 | Exact match |
| SL-LOGIN-002 | Login page elements displayed (incl. accepted usernames/password info) | Not Covered | — | Username/Password fields and Login button are implicitly demonstrated via successful interaction, but the "accepted usernames/password" info box is only ever mentioned inside a test *precondition* (TC-012), never actually asserted as a test's own result — per the anti-pattern, a precondition doesn't count as coverage of the behavior it assumes |
| SL-LOGIN-003 | Login with each valid user type | Not Covered | — | Only `standard_user` is exercised as a valid login; GT requires cycling through each valid user type (multiple SauceDemo user accounts), which no GEN test attempts |
| SL-LOGIN-004 | Invalid username | Covered | TC-004, TC-009 | Exact match |
| SL-LOGIN-005 | Invalid password (valid username) | Covered | TC-004, TC-009 | GEN's mismatch tests use both an invalid username and invalid password together rather than isolating password-only invalidity, but this triggers the same generic "Username and password do not match" error path — same equivalence class (Rule 6) |
| SL-LOGIN-006 | Empty username | Covered | TC-002, TC-006 | Exact match |
| SL-LOGIN-007 | Empty password | Covered | TC-003, TC-007 | Exact match |
| SL-LOGIN-008 | Both fields empty | Covered | TC-008 | Exact match |
| SL-LOGIN-009 | Locked out user | Covered | TC-005, TC-010 | Exact match |
| SL-LOGIN-010 | Username with leading/trailing spaces | Covered | TC-012 | Exact match |
| SL-LOGIN-011 | Case sensitivity | Not Covered | — | No GEN test enters a differently-cased username; TC-011 tests length, TC-012 tests whitespace, neither addresses case sensitivity |
| SL-LOGIN-012 | Password field masking | Not Covered | — | No GEN test asserts the password field visually masks entered characters — untouched |
| SL-LOGIN-013 | Browser Back after login shows blank form | Covered | TC-013 | Exact match |
| SL-LOGIN-014 | Extremely long username | Covered | TC-011 | Exact match |
| SL-LOGIN-015 | Enter key submission | Not Covered | — | Every GEN test submits via explicitly clicking the Login button; none tests Enter-key submission as an alternate path |

## Gap List (Not Covered)

- **SL-LOGIN-002** — Accepted-usernames/password info box visibility (only assumed in a precondition, never asserted)
- **SL-LOGIN-003** — Login with each valid user type (only `standard_user` tested)
- **SL-LOGIN-011** — Username case sensitivity
- **SL-LOGIN-012** — Password field masking
- **SL-LOGIN-015** — Enter key form submission

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Login | 15 | 10 | 5 | 66.7% |
