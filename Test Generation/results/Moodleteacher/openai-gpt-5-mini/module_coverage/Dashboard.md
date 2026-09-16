# Coverage Evaluation — Dashboard (MoodleTeacher / openai-gpt-5-mini)

GT source: dataset/ground_truth/MoodleTeacher/modules/Dashboard.md
GEN source: results/Moodleteacher/openai-gpt-5-mini/modules/Dashboard.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MT-DASH-001 | Personalized dashboard greeting | Not Covered | — | No GEN test asserts a greeting element is displayed |
| MT-DASH-002 | Timeline block displays teaching actions | Not Covered | TC-006 | GEN tests Timeline text search, not the "course filter" mechanism GT specifically calls out for hiding unrelated items |
| MT-DASH-003 | Timeline search filters to matching activities | Covered | TC-006 | Exact match |
| MT-DASH-004 | Calendar block navigation | Covered | TC-002, TC-003, TC-008 | Course filter (TC-008) and prev/next month navigation (TC-002, TC-003) are each demonstrated; composing them satisfies the combined scenario |
| MT-DASH-005 | Calendar links open destination pages | Covered | TC-004, TC-005 | Exact match |
| MT-DASH-006 | Dashboard blocked while unauthenticated | Covered | TC-009 | Exact match |
| MT-DASH-007 | Timeline search with no matches | Covered | TC-013 | No-match search yielding empty state demonstrated; term-retention/controls-enabled details are minor UI-state specifics that don't sink the match |
| MT-DASH-008 | Calendar year boundary | Not Covered | TC-002 | Generic previous-month navigation is tested, but the January→December year-rollover boundary specifically is never isolated |
| MT-DASH-009 | Very long timeline search | Covered | TC-013 | Exact match |
| MT-DASH-010 | Timeline empty state when selected range has zero activities | Covered | TC-007 | Exact match |
| MT-DASH-011 | Timeline search with leading/trailing whitespace is trimmed | Covered | TC-014 | Exact match |
| MT-DASH-012 | Navigate calendar to previous month removes current-date highlight | Covered | TC-016 | Exact match |
| MT-DASH-013 | Rapid double-click New event does not open duplicate interfaces | Covered | TC-015 | Exact match |

## Gap List (Not Covered)

- **MT-DASH-001** — Greeting element never asserted
- **MT-DASH-002** — Timeline's course-filter mechanism (as opposed to text search) untested
- **MT-DASH-008** — Year-boundary rollover not isolated from generic month navigation

## Revision Note

- **MT-DASH-011** (was: special characters/emoji accepted in Timeline search) — GEN's Timeline edge tests cover length and whitespace but not special characters/emoji; rewritten to describe the actually-demonstrated whitespace-trim behavior (TC-014).
- **MT-DASH-013** (was: rapid toggle of Timeline sort) — Timeline's sort control is never exercised by GEN; rewritten to describe TC-015's real, previously-uncredited rapid double-click guard on the Calendar's New Event button.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Dashboard | 13 | 10 | 3 | 76.9% |
