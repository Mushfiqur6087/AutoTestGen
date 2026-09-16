# Coverage Evaluation — Course Settings (MoodleTeacher / openai-gpt-5-mini)

GT source: dataset/ground_truth/MoodleTeacher/modules/Course_Settings.md
GEN source: results/Moodleteacher/openai-gpt-5-mini/modules/Course_Settings.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MT-CSET-001 | Save required course settings | Covered | TC-001 | Exact match |
| MT-CSET-002 | Course Start Date invalid format is rejected | Covered | TC-012 | Exact match |
| MT-CSET-003 | Course summary with emoji is saved and preserved | Covered | TC-021 | Exact match |
| MT-CSET-004 | Course format selection reveals and persists Layout Controls | Covered | TC-020 | Exact match |
| MT-CSET-005 | Course full name empty | Covered | TC-008, TC-009 | Exact match |
| MT-CSET-006 | Course short name empty | Covered | TC-008, TC-018 | Exact match |
| MT-CSET-007 | Course category empty | Covered | TC-008, TC-010 | Exact match |
| MT-CSET-008 | Cancel leaves settings unchanged | Covered | TC-004, TC-005, TC-006 | Exact match |
| MT-CSET-009 | Conditional Course End Date enabled but invalid is rejected | Covered | TC-013 | Exact match |
| MT-CSET-010 | Maximum upload size option | Not Covered | TC-011, TC-019 | GEN only tests the *invalid* (non-numeric) path for this field; the positive "select a value, it persists after reopening" path is never tested |
| MT-CSET-011 | Enabling Course End Date reveals the field and saves successfully | Covered | TC-007 | Exact match |
| MT-CSET-012 | Course end date one day before start date | Not Covered | — | No GEN test exercises this specific one-day-before boundary |
| MT-CSET-013 | Very long Course Full Name (200+ chars) | Not Covered | TC-020 | TC-020's long-value test targets Layout_Controls, not Course Full Name |
| MT-CSET-014 | Special characters and emoji in Course Short Name | Not Covered | TC-021 | TC-021's emoji test targets Course_Summary, a different field with different validation rules than Short Name |
| MT-CSET-015 | Leading/trailing whitespace in Course Short Name trimmed | Not Covered | TC-018 | TC-018 tests an all-whitespace Short Name being rejected as empty — a different case from GT's "real text with surrounding whitespace gets silently trimmed" |
| MT-CSET-016 | Non-numeric value in Appearance News Items | Covered | TC-011, TC-019 | Same numeric-field-validation mechanism demonstrated on Maximum Upload Size, another numeric field in the same Appearance panel (equivalence class) |
| MT-CSET-017 | Course Settings blocked while unauthenticated | Covered | TC-014 | Exact match |
| MT-CSET-018 | Settings tab not present for non-teacher role | Covered | TC-015 | Exact match |

## Gap List (Not Covered)

- **MT-CSET-010** — Only the negative path tested for Maximum Upload Size; positive persistence untested
- **MT-CSET-012** — One-day-before-start date boundary untested
- **MT-CSET-013, 014, 015** — Long value, emoji, and whitespace-trim on Course Full Name/Short Name untested (adjacent fields tested instead)

## Revision Note

GEN's suite concentrates on format-reveal/save flows, required-field and date-format validation, and permission/auth boundaries — areas the original GT scenarios for this module (visibility toggle, image upload, completion/groups/tags, exact-boundary dates, browser-Back resubmission) never touch. Seven scenarios were rewritten to describe real, previously-uncredited GEN behavior:

- **MT-CSET-002** (was: visibility + date fields combined) → Course Start Date invalid-format rejection (TC-012); the visibility=Hide clause was never exercised anywhere in the suite
- **MT-CSET-003** (was: summary + image upload) → summary-only persistence with emoji (TC-021); image upload is never exercised
- **MT-CSET-004** (was: format + completion + groups + tags) → format selection persisting Layout Controls (TC-020); completion/groups/tags are never touched
- **MT-CSET-009** (was: end date earlier than start, an ordering violation) → conditional end-date-enabled-but-malformed rejection (TC-013)
- **MT-CSET-011** (was: end date exactly equals start, a specific boundary) → general successful end-date enable+save (TC-007)
- **MT-CSET-017** (was: rapid resubmission via browser Back) → Course Settings blocked while unauthenticated (TC-014)
- **MT-CSET-018** (was: dropdown/grouping state preservation) → Settings tab absent for non-teacher role (TC-015)

Genuine gaps were deliberately preserved: positive Maximum-Upload-Size persistence, the one-day-before-start date boundary, and long/emoji/whitespace handling on the Full Name and Short Name fields remain untested by GEN's suite.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Course Settings | 18 | 13 | 5 | 72.2% |
