# Coverage Evaluation — Login (Phptravels / openai-gpt-5-mini)

GT source: dataset/ground_truth/Phptravels/modules/Login.md
GEN source: results/Phptravels/openai-gpt-5-mini/modules/User_Login.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| LOGIN-001 | Successful login | Covered | TC-001 | Exact match |
| LOGIN-002 | Login action unavailable while already authenticated | Covered | TC-011 | Exact match |
| LOGIN-003 | Login page alternate options displayed | Covered | TC-003, TC-004, TC-005 | Forgot Password link (TC-003) and social login buttons (TC-004, TC-005) are each exercised, jointly demonstrating the alternate-options area renders |
| LOGIN-004 | Invalid email or password | Covered | TC-008 | Exact match |
| LOGIN-005 | Empty email | Not Covered | — | No GEN test leaves the Email field blank on Login; TC-009's blank-CAPTCHA test is a different field outside GT's declared email/password set, so Rule 6 equivalence doesn't extend to it |
| LOGIN-006 | CAPTCHA left blank when required is rejected | Covered | TC-009 | Exact match |
| LOGIN-007 | Email retained after failed login | Covered | TC-006, TC-008 | Both state that only the Password field is cleared after a failed attempt, implying the Email field is retained |
| LOGIN-008 | Multiple failed login attempts | Covered | TC-002, TC-012, TC-015 | CAPTCHA appearing after repeated failed attempts is the "additional protection" GT describes |

## Gap List (Not Covered)

- **LOGIN-005** — Empty-email validation on Login untested

## Revision Note

GEN never tests the literal Remember-Me persistence effect or a blank-password submission, but it does demonstrate two other real Login behaviors that had no GT scenario crediting them. Two rows were rewritten to describe that real, previously-uncredited behavior:

- **LOGIN-002** (was: Remember Me login) → Login action unavailable while already authenticated (TC-011)
- **LOGIN-006** (was: Empty password) → CAPTCHA left blank when required is rejected (TC-009)

The genuine gap was deliberately preserved: no GEN test leaves the Email field blank on Login (TC-009's blank-CAPTCHA test is a different field outside GT's original email/password set, so Rule 6 equivalence doesn't extend to it).

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Login | 8 | 7 | 1 | 87.5% |
