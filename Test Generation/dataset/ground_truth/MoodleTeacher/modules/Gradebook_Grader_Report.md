# Moodle Teacher Test Cases — Ground Truth

Source: dataset/ground_truth/MoodleTeacher/MoodleTeacher.md

## Gradebook Grader Report

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-GRADE-001 | Grader report table displayed | Teacher opens Grades tab | 1. Open Grader report | Activity columns, student rows, grade cells, and average row are visible | High |
| MT-GRADE-002 | Switch report type | Report selector is visible | 1. Change report type to User report or Overview report | Selected report opens | Medium |
| MT-GRADE-003 | Search/filter gradebook users | Gradebook includes `student1` | 1. Search for `student1` in gradebook user search/filter controls | Grade table shows `student1` row and hides non-matching student rows | High |
| MT-GRADE-004 | Edit individual grade cell | Edit mode is enabled and `student1` has a grade item | 1. Open `student1` grade cell for `Essay Draft`<br>2. Enter `90`<br>3. Save changes<br>4. Reload Grader report | `student1` shows grade `90` for `Essay Draft`; the course total row refreshes and does not show a stale previous total | High |
| MT-GRADE-005 | Edit activity grade settings | Column action menu is visible | 1. Open activity column menu<br>2. Select grade settings action | Grade settings page/dialog opens | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-GRADE-006 | Gradebook blocked while unauthenticated | User is logged out | 1. Navigate directly to gradebook URL | User is redirected to the login page before grader report rows or grade cells render | High |
| MT-GRADE-007 | Out-of-range grade blocked | Edit mode is enabled | 1. Enter grade `101` for `student1` on `Essay Draft`<br>2. Save | Invalid value is flagged, save is blocked, and the previous `Essay Draft` grade remains unchanged after reload | High |
| MT-GRADE-008 | Student cannot access grader report | Student account exists | 1. Log in as student<br>2. Navigate to Grader report URL | Full grader report is not accessible | High |
| MT-GRADE-011 | Edit a Grade cell when Edit Mode is disabled | Grader report is visible and Edit mode is off | 1. Click a student's grade cell | Cell remains read-only; no inline input field or save controls appear | High |
| MT-GRADE-012 | Enter non-numeric value into Grade cell | Grader report is visible and Edit mode is on | 1. Enter `A+` in a grade cell<br>2. Click Save changes | Save is blocked by numeric validation error on the modified cell | High |
| MT-GRADE-014 | Grade one unit above activity maximum | Grader report is visible and Edit mode is on | 1. Enter `101` in a grade cell where max is `100`<br>2. Click Save changes | Save is blocked by maximum value validation error on the modified cell | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-GRADE-009 | Minimum valid grade | Edit mode is enabled | 1. Enter grade `0` for `student1` on `Essay Draft`<br>2. Save and reload Grader report | Grade `0` remains visible for `student1` on `Essay Draft` after reload | Medium |
| MT-GRADE-010 | Decimal grade precision | Grade item is configured for one decimal place | 1. Enter grade `89.5`<br>2. Save and reload Grader report | Grade displays as `89.5` and is not rounded to a whole number | Low |
| MT-GRADE-013 | Grade exactly equals activity maximum | Grader report is visible and Edit mode is on | 1. Enter `100` in a grade cell where max is `100`<br>2. Click Save changes | Grade saves successfully without out-of-bounds error | Medium |
| MT-GRADE-015 | Grade exactly equals activity minimum | Grader report is visible and Edit mode is on | 1. Enter `0` in a grade cell where min is `0`<br>2. Click Save changes | Grade saves successfully without out-of-bounds error | Medium |
| MT-GRADE-016 | Very long comment in grade cell | Grader report is visible and Edit mode is on | 1. Enter a 200+ character comment for a grade<br>2. Click Save changes | Comment is saved successfully and is accessible without breaking the grader report grid | Low |
