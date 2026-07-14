# Coverage Evaluation — Register (Parabank / openai-gpt-5-mini)

GT source: dataset/ground_truth/Parabank/modules/Register.md
GEN source: results/Parabank/openai-gpt-5-mini/modules/Register.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria, incl. Rule 6 N-field equivalence)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MW-REG-001 | Successful registration | Covered | TC-001 | Exact match |
| MW-REG-003 | State dropdown shows all US states | Not Covered | — | No GEN test asserts the dropdown's full content list; tests only select *a* state, they never verify all US states are present |
| MW-REG-004 | Phone auto-formatting | Covered | TC-002, TC-018 | Exact match, reinforced by the 10-digit boundary test |
| MW-REG-005 | SSN auto-formatting | Covered | TC-003, TC-020 | Exact match, reinforced by the 9-digit boundary test |
| MW-REG-006 | First Name empty | Covered | TC-005 | Exact match (explicit representative blank-field test) |
| MW-REG-007 | Last Name empty | Covered | TC-005, TC-006 | TC-006's "all fields blank" test explicitly names Last_Name among the fields asserted to show an inline required error (Rule 6 N-field equivalence) |
| MW-REG-008 | Street Address empty | Covered | TC-006 | Explicitly named in TC-006's per-field assertion |
| MW-REG-009 | City empty | Covered | TC-006 | Explicitly named in TC-006's per-field assertion |
| MW-REG-010 | State not selected | Covered | TC-007, TC-006 | TC-007 direct match; TC-006 also names State |
| MW-REG-011 | ZIP Code empty | Covered | TC-006 | Explicitly named in TC-006's per-field assertion |
| MW-REG-012 | Invalid ZIP format | Covered | TC-011, TC-017 | Exact match, reinforced by the 4-digit boundary test |
| MW-REG-013 | Valid 5+4 ZIP | Covered | TC-004 | Exact match: 5+4 format explicitly tested and accepted |
| MW-REG-014 | Phone Number empty | Covered | TC-006 | Explicitly named in TC-006's per-field assertion |
| MW-REG-015 | Invalid Phone format | Covered | TC-012, TC-019 | Exact match, reinforced by the 9-digit boundary test |
| MW-REG-016 | SSN empty | Covered | TC-006 | Explicitly named in TC-006's per-field assertion |
| MW-REG-017 | Invalid SSN format | Covered | TC-013 | Exact match |
| MW-REG-018 | Username not email format | Covered | TC-008 | Exact match |
| MW-REG-019 | Password less than 8 chars | Covered | TC-009, TC-015 | Exact match, reinforced by the one-below-minimum boundary test |
| MW-REG-020 | Password mismatch | Covered | TC-010, TC-021 | Exact match, reinforced by the whitespace-difference boundary test |
| MW-REG-021 | Confirm Password empty | Covered | TC-006 | Explicitly named in TC-006's per-field assertion |
| MW-REG-022 | All fields empty | Covered | TC-006 | Exact match |
| MW-REG-023 | Minimum valid inputs (all fields) succeed | Covered | TC-014, TC-016, TC-018, TC-020 | Each field's minimum-boundary case is independently proven to succeed (password, ZIP, phone digit count, SSN digit count); jointly they satisfy the combined GT scenario (Rule 4) |
| MW-REG-024 | Maximum length inputs handled gracefully | Not Covered | — | No GEN test enters an excessively long string into any field — untouched |
| MW-REG-025 | Email with leading/trailing spaces trimmed and accepted | Not Covered | — | GEN only tests whitespace on Confirm_Password (rejected as a mismatch) — a different field, different validation logic, and an opposite expected outcome (trim-and-accept vs. reject); not the same equivalence class |
| MW-REG-026 | Registration session timeout | Not Covered | — | No GEN test simulates a stale/expired session — untouched |

## Gap List (Not Covered)

- **MW-REG-003** — State dropdown's full US-states content list never verified
- **MW-REG-024** — Maximum-length/long-string input handling
- **MW-REG-025** — Email leading/trailing whitespace trimming (distinct from the tested Confirm_Password whitespace rejection)
- **MW-REG-026** — Registration session timeout handling

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Register | 25 | 21 | 4 | 84.0% |
