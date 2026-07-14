# Coverage Evaluation — Update Contact Info (Parabank / openai-gpt-5-mini)

GT source: dataset/ground_truth/Parabank/modules/Update_Contact_Info.md
GEN source: results/Parabank/openai-gpt-5-mini/modules/Update_Contact_Info.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria, incl. Rule 6 N-field equivalence)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MW-UCI-001 | Pre-populated form | Covered | TC-001 | Exact match |
| MW-UCI-002 | Successful update | Covered | TC-002 | Exact match |
| MW-UCI-003 | Update First Name | Covered | TC-002 | TC-002 explicitly asserts the refreshed form shows the entered First Name value among all fields updated together |
| MW-UCI-004 | Update Last Name | Covered | TC-002 | Same — Last Name explicitly named in TC-002's post-update assertion |
| MW-UCI-005 | Update Address | Covered | TC-002, TC-011 | TC-002 explicitly named; TC-011 reinforces with the whitespace-trim boundary specific to this field |
| MW-UCI-006 | Update City | Covered | TC-002 | Explicitly named in TC-002's post-update assertion |
| MW-UCI-007 | Update State | Covered | TC-002 | Explicitly named in TC-002's post-update assertion |
| MW-UCI-008 | Update ZIP Code | Covered | TC-002 | Explicitly named in TC-002's post-update assertion |
| MW-UCI-009 | Update Phone | Covered | TC-002, TC-012 | TC-002 explicitly named; TC-012 reinforces with the international-format edge case |
| MW-UCI-010 | First Name empty | Covered | TC-003, TC-004 | TC-004 direct representative match; TC-003 also names it |
| MW-UCI-011 | Last Name empty | Covered | TC-003 | Explicitly named in TC-003's all-fields-empty assertion (Rule 6 N-field equivalence) |
| MW-UCI-012 | Address empty | Covered | TC-003 | Explicitly named |
| MW-UCI-013 | City empty | Covered | TC-003 | Explicitly named |
| MW-UCI-014 | State empty | Covered | TC-003 | Explicitly named |
| MW-UCI-015 | ZIP Code empty | Covered | TC-003 | Explicitly named |
| MW-UCI-016 | Phone empty | Covered | TC-003 | Explicitly named |
| MW-UCI-017 | Invalid ZIP format | Covered | TC-006 | Exact match |
| MW-UCI-018 | Invalid Phone format | Covered | TC-007 | Exact match |
| MW-UCI-019 | Special characters in City | Not Covered | — | No GEN test enters numbers/symbols into the City field; TC-005 tests invalid *name* format on Last Name (different field), and TC-010 tests accepted special characters in names (opposite outcome, different field) — City's own format validation is untouched |
| MW-UCI-020 | Non-US ZIP code format (alphanumeric) | Covered | TC-006 | TC-006's "invalid ZIP/postal code format" fixture is unspecified but the "ZIP/postal code" phrasing and generic invalid-format framing plausibly instantiates as an alphanumeric non-US format (Rule 3 fixture agnosticism) |

## Gap List (Not Covered)

- **MW-UCI-019** — Special characters/numbers in City field rejected (City's own format validation never tested)

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Update Contact Info | 20 | 19 | 1 | 95.0% |
