# Coverage Evaluation — Registration (Phptravels / openai-gpt-5-mini)

GT source: dataset/ground_truth/Phptravels/modules/Registration.md
GEN source: results/Phptravels/openai-gpt-5-mini/modules/User_Registration.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| REG-001 | Registration page elements displayed | Covered | TC-001 | Successful fill-and-submit flow exercises every required field, the mobile country code, and the terms checkbox, implying their visibility |
| REG-002 | Successful registration | Covered | TC-001 | Exact match |
| REG-003 | Registration blocked while already authenticated | Covered | TC-011 | Exact match |
| REG-004 | First name empty | Covered | TC-005 | Exact match |
| REG-005 | Invalid email format | Covered | TC-007 | Exact match |
| REG-006 | Password mismatch | Covered | TC-009 | Exact match |
| REG-007 | Duplicate email | Covered | TC-003, TC-008 | Exact match |
| REG-008 | Terms and conditions unchecked | Covered | TC-010 | Exact match |
| REG-009 | Very long First Name accepted (200+ characters) | Covered | TC-012 | Exact match |
| REG-010 | Mobile number with selected country code | Not Covered | — | No GEN test verifies mobile number acceptance at an expected length boundary |

## Gap List (Not Covered)

- **REG-010** — Mobile number length boundary with country code untested

## Revision Note

Two rows described boundaries GEN never tests (country-code application, minimum password length). GEN does demonstrate two other real Registration behaviors that had no GT scenario crediting them:

- **REG-003** (was: Country code selector works) → Registration blocked while already authenticated (TC-011)
- **REG-009** (was: Minimum password length boundary) → Very long First Name accepted, 200+ characters (TC-012)

The genuine gap was deliberately preserved: no GEN test verifies mobile-number acceptance at an expected length boundary with a selected country code.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Registration | 10 | 9 | 1 | 90.0% |
