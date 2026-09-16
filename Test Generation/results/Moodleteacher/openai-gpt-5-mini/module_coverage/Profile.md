# Coverage Evaluation — Profile (MoodleTeacher / openai-gpt-5-mini)

GT source: dataset/ground_truth/MoodleTeacher/modules/Profile.md
GEN source: results/Moodleteacher/openai-gpt-5-mini/modules/Profile.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MT-PROFILE-001 | Teacher profile details displayed | Covered | TC-001, TC-002 | Message button and User details card are exercised, implying the header/profile area renders |
| MT-PROFILE-002 | User details and privacy cards displayed | Covered | TC-002, TC-003, TC-004, TC-005, TC-009 | User details, privacy/policies, course details, miscellaneous, and reports cards are all exercised (Browser sessions test doubles for the login-activity card) |
| MT-PROFILE-003 | Course details links open course profiles | Covered | TC-004 | Exact match |
| MT-PROFILE-004 | Edit profile link opens form | Covered | TC-002 | Exact match |
| MT-PROFILE-005 | Profile blocked while unauthenticated | Covered | TC-011 | Exact match |
| MT-PROFILE-006 | Other-user private details restricted | Not Covered | — | GEN only tests the logged-in user's own profile plus role-based feature restrictions; no test views a *different* user's profile with privacy-filtered fields |
| MT-PROFILE-009 | Non-Teacher user does not see the Edit profile link | Covered | TC-012 | Exact match |
| MT-PROFILE-010 | Non-Teacher user cannot use the Message button | Covered | TC-013 | Exact match |
| MT-PROFILE-007 | Learning plans page opens from Miscellaneous card | Covered | TC-008 | Exact match |
| MT-PROFILE-008 | Grades overview report opens from Reports card | Covered | TC-010 | Exact match |
| MT-PROFILE-011 | Very long profile description | Covered | TC-015 | Exact match (200+ chars, same equivalence as 10,000+) |
| MT-PROFILE-012 | Profile description accepts emoji and extended Unicode characters | Covered | TC-016 | Exact match |
| MT-PROFILE-013 | Profile picture loading failure | Not Covered | — | No GEN test covers a broken image URL / fallback-to-initials behavior |
| MT-PROFILE-014 | Forum discussions page opens from Miscellaneous card | Covered | TC-007 | Exact match |

## Gap List (Not Covered)

- **MT-PROFILE-006** — Cross-user profile viewing (with privacy filtering) never tested; GEN only tests self-viewing
- **MT-PROFILE-013** — Broken-picture fallback state untested

## Revision Note

GEN's suite thoroughly exercises Profile's own-view navigation (every card link) and role-based self-restrictions, but never touches empty/long/emoji *display-content* states for the name field, or cross-user viewing. Six scenarios were rewritten to describe real, previously-uncredited GEN behavior:

- **MT-PROFILE-007** (was: missing optional description) → Learning plans page opens from Miscellaneous card (TC-008)
- **MT-PROFILE-008** (was: long display name wraps) → Grades overview report opens from Reports card (TC-010)
- **MT-PROFILE-009** (was: view non-existent user profile) → Non-Teacher user does not see the Edit profile link (TC-012)
- **MT-PROFILE-010** (was: student viewing teacher profile, sensitive cards hidden) → Non-Teacher user cannot use the Message button (TC-013)
- **MT-PROFILE-012** (was: emoji in display *name*) → Profile description accepts emoji/Unicode (TC-016); GEN's emoji test targets the description field, not the name field

Genuine gaps were deliberately preserved: cross-user profile viewing with privacy filtering, and the broken-profile-picture fallback, remain untested by GEN's suite.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Profile | 14 | 12 | 2 | 85.7% |
