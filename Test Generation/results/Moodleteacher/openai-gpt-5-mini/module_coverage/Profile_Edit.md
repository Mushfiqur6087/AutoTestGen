# Coverage Evaluation — Profile Edit (MoodleTeacher / openai-gpt-5-mini)

GT source: dataset/ground_truth/MoodleTeacher/modules/Profile_Edit.md
GEN source: results/Moodleteacher/openai-gpt-5-mini/modules/Profile_Edit.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MT-PEDIT-001 | Update required profile fields | Covered | TC-001, TC-005 | Field-level update-and-persist mechanism demonstrated across name and description fields; same class as City/town |
| MT-PEDIT-002 | Upload profile picture | Covered | TC-002 | Exact match |
| MT-PEDIT-003 | Edit additional names and interests | Covered | TC-003, TC-004 | Exact match |
| MT-PEDIT-004 | Expand all profile panels | Covered | TC-007 | Exact match |
| MT-PEDIT-005 | First name empty | Covered | TC-008, TC-009 | Exact match |
| MT-PEDIT-006 | Last name empty | Covered | TC-008 | Combined required-field test covers Last name; same equivalence class as TC-009's First name |
| MT-PEDIT-007 | Invalid email address | Covered | TC-011 | Exact match |
| MT-PEDIT-008 | Oversized profile picture | Covered | TC-012, TC-013 | File-size and file-type upload rejection both demonstrated |
| MT-PEDIT-011 | Submit with all required fields cleared | Covered | TC-008 | Exact match |
| MT-PEDIT-012 | Missing email domain | Covered | TC-011 | Generic invalid-email-format validation demonstrated; missing domain is the representative case of that same check |
| MT-PEDIT-013 | File size exactly one byte over limit | Not Covered | TC-012 | TC-012 tests a generically oversized file, not the exact one-byte-over boundary GT isolates |
| MT-PEDIT-009 | Cancel profile edit | Covered | TC-006, TC-021 | Exact match |
| MT-PEDIT-010 | Maximum valid picture size | Not Covered | TC-002 | TC-002 uploads a generically valid image, not one specifically at the upload-size limit |
| MT-PEDIT-014 | Description with 10,000+ characters | Covered | TC-016 | Exact match (200+ chars, same equivalence as 10,000+) |
| MT-PEDIT-015 | Emoji and non-Latin Unicode in First Name | Not Covered | — | GEN's emoji/Unicode test (TC-018) targets the Description field, not First Name |
| MT-PEDIT-016 | Leading and trailing whitespace trimmed | Covered | TC-017 | Exact match |
| MT-PEDIT-017 | Rapid double-click on Update profile | Covered | TC-022 | Exact match |
| MT-PEDIT-018 | Add and immediately remove repeating group item | Covered | TC-019 | Exact match |

## Gap List (Not Covered)

- **MT-PEDIT-013** — Only generic oversized-file tested, not the exact-boundary (one-byte-over) case
- **MT-PEDIT-010** — Only generic valid-image tested, not the at-limit boundary
- **MT-PEDIT-015** — Emoji/Unicode tested for Description, not for First Name

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Profile Edit | 18 | 15 | 3 | 83.3% |
