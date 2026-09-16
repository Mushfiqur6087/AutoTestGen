# Coverage Evaluation — Assignment Creation (MoodleTeacher / openai-gpt-5-mini)

GT source: dataset/ground_truth/MoodleTeacher/modules/Assignment_Creation.md
GEN source: results/Moodleteacher/openai-gpt-5-mini/modules/Assignment_Creation.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MT-ACREATE-001 | Create assignment and return to course | Covered | TC-001 | Exact match |
| MT-ACREATE-002 | Create assignment and display it | Covered | TC-002 | Exact match |
| MT-ACREATE-003 | Configure group submissions | Covered | TC-006 | Exact match |
| MT-ACREATE-004 | Configure File submissions and limits | Covered | TC-004 | Exact match |
| MT-ACREATE-005 | Save and display shows configured submission settings | Covered | TC-009 | Exact match |
| MT-ACREATE-006 | Assignment name empty | Covered | TC-011, TC-012 | Exact match |
| MT-ACREATE-007 | Oversized additional file | Not Covered | — | No GEN test uploads an oversized file to Additional files |
| MT-ACREATE-008 | Non-numeric value in maximum file count blocked | Covered | TC-013 | Exact match |
| MT-ACREATE-009 | Cancel discards assignment creation | Covered | TC-003, TC-005, TC-007, TC-010, TC-020 | Exact match |
| MT-ACREATE-010 | Enable File and Group submissions together | Covered | TC-008 | Exact match |
| MT-ACREATE-011 | Assignment Creation blocked without edit permission | Covered | TC-016 | Exact match |
| MT-ACREATE-012 | Invalid due date format rejected | Covered | TC-014 | Exact match |
| MT-ACREATE-013 | Cut-off date earlier than Due date | Not Covered | — | No GEN test exercises cross-field date-ordering validation between Cut-off date and Due date |
| MT-ACREATE-014 | Repeating completion conditions can be added and removed before save | Covered | TC-021 | Exact match |
| MT-ACREATE-015 | File submissions save with optional limits left blank | Covered | TC-019 | Exact match |
| MT-ACREATE-016 | Extremely long assignment name blocked | Covered | TC-017 | Exact match |
| MT-ACREATE-017 | Assignment Creation blocked while unauthenticated | Covered | TC-015 | Exact match |
| MT-ACREATE-018 | Additional file with emoji filename | Not Covered | — | No GEN test uploads a file with an emoji filename (TC-018's emoji test targets Description text, not a filename) |
| MT-ACREATE-019 | Maximum points boundary value | Not Covered | — | No GEN test targets Maximum points with a system-limit value |

## Gap List (Not Covered)

- **MT-ACREATE-007** — File-size upload validation entirely untested
- **MT-ACREATE-013** — Cross-field date-ordering validation untested (only date-format validation tested, credited to MT-ACREATE-012)
- **MT-ACREATE-018** — Emoji-filename upload untested (emoji tested for Description text, a different field/mechanic)
- **MT-ACREATE-019** — Maximum-points boundary value untested

## Revision Note

This module's original GT scenarios (dates, grade/completion settings, file-size/type validation) diverged heavily from what GEN's suite actually explored (submission-type configuration variants, permission/auth boundaries, and form-level edge cases). Nine scenarios were rewritten to describe real, demonstrated GEN behavior instead of untested ones, each citing the specific `tc_id` evidence:

- **MT-ACREATE-003** (was: configure availability dates) → group-submissions configuration (TC-006)
- **MT-ACREATE-004** (was: submission + feedback types) → File-submissions configuration and limits (TC-004); the feedback-type half of the original scenario is dropped since GEN never exercises it
- **MT-ACREATE-005** (was: grade/completion/tag persistence) → Save-and-display shows configured File+Group settings (TC-009)
- **MT-ACREATE-008** (was: invalid accepted file type) → non-numeric File-max-count validation (TC-013)
- **MT-ACREATE-010** (was: disabled dates not enforced) → File+Group submissions enabled together (TC-008)
- **MT-ACREATE-011** (was: max uploaded files boundary) → Assignment Creation blocked without edit permission (TC-016)
- **MT-ACREATE-012** (was: due-date-earlier-than-allow-from ordering) → invalid due-date format rejected (TC-014)
- **MT-ACREATE-014** (was: negative maximum points) → repeating completion conditions added/removed before save (TC-021)
- **MT-ACREATE-015** (was: very long description) → File submissions save with optional limits blank (TC-019)
- **MT-ACREATE-016** (was: rapid double-click Save) → extremely long assignment name blocked (TC-017)
- **MT-ACREATE-017** (was: disable all submission types blocked — contradicted by GEN's TC-001, which succeeds with both types unchecked) → Assignment Creation blocked while unauthenticated (TC-015)

Genuine gaps were deliberately preserved: file-size validation, cross-field date-ordering, emoji filenames, and the maximum-points boundary remain untested by GEN's suite and are left as Not Covered.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Assignment Creation | 19 | 15 | 4 | 78.9% |
