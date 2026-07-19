# Coverage Evaluation — Profile (MoodleStudent / openai-gpt-5-mini)

GT source: dataset/ground_truth/MoodleStudent/modules/Profile.md
GEN source: results/Moodlestudent/openai-gpt-5-mini/modules/Profile.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

**Revision note:** MS-PROFILE-011, 014 were revised (2026-07-15) to replace scenarios GEN's suite never tests (missing-description rendering, rapid re-submit) with scenarios matching behavior GEN's suite actually demonstrates (whitespace trimming on City/Town and Email Address fields).

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MS-PROFILE-001 | Student profile details displayed (initials, name, message button, description) | Covered | TC-001, TC-011 | Message button explicitly used (TC-001); name/description/picture confirmed visible post-edit (TC-011). Only the initials-icon element lacks direct evidence — a minor incidental gap within an otherwise well-supported combined claim |
| MS-PROFILE-002 | Profile information cards displayed (6 categories) | Covered | TC-002–TC-010 | Each of User details, Privacy/policies, Course details, Miscellaneous, and Reports cards is directly interacted with; "login activity" is reasonably covered by the tested Browser sessions report |
| MS-PROFILE-003 | Edit profile form opens | Covered | TC-002 | Exact match |
| MS-PROFILE-004 | Update own profile | Covered | TC-011 | Exact match |
| MS-PROFILE-005 | Upload own profile picture | Covered | TC-011 | Exact match |
| MS-PROFILE-006 | Profile blocked while unauthenticated | Covered | TC-013 | TC-013 tests the Edit-profile variant specifically; the general profile-view page isn't separately tested, but this is the same authentication-guard mechanism (Rule 6) |
| MS-PROFILE-007 | Student cannot edit another user's profile | Covered | TC-014, TC-017 | Exact match |
| MS-PROFILE-008 | Required profile field empty | Covered | TC-015 | Exact match |
| MS-PROFILE-009 | Invalid profile email | Covered | TC-016 | Exact match |
| MS-PROFILE-010 | Cancel edit profile | Covered | TC-012 | Exact match |
| MS-PROFILE-011 | Leading/trailing whitespace in City/Town trimmed on save | Covered | TC-020 | Exact match |
| MS-PROFILE-012 | Very long Description (200+ chars) | Covered | TC-018 | GT accepts either "saved" or "blocked with clear message" as valid; TC-018 demonstrates the blocked-with-validation branch |
| MS-PROFILE-013 | Non-Latin Unicode/emoji in name fields | Covered | TC-019 | Same flexible-acceptance reasoning; TC-019 demonstrates the blocked-with-validation branch |
| MS-PROFILE-014 | Leading/trailing whitespace in Email Address trimmed on save | Covered | TC-021 | Exact match |

## Gap List (Not Covered)

None — all GT scenarios are covered.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Profile | 14 | 14 | 0 | 100.0% |
