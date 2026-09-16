# Moodle Teacher Test Cases — Ground Truth

Source: dataset/ground_truth/MoodleTeacher/MoodleTeacher.md

## Profile

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-PROFILE-001 | Teacher profile details displayed | Teacher is logged in | 1. Open Profile | Initials icon, full name, message button, and profile description area are visible | High |
| MT-PROFILE-002 | User details and privacy cards displayed | Profile page is open | 1. Inspect information cards | User details, privacy/policies, course details, miscellaneous, reports, and login activity cards are visible | High |
| MT-PROFILE-003 | Course details links open course profiles | Teacher profile lists `QA Automation 101` under Course details | 1. Click the `QA Automation 101` course profile link | Course profile view for `teacher1` in `QA Automation 101` opens and keeps teacher identity visible | Medium |
| MT-PROFILE-004 | Edit profile link opens form | Profile page is open | 1. Click "Edit profile" | Edit profile form opens | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-PROFILE-005 | Profile blocked while unauthenticated | User is logged out | 1. Navigate directly to profile URL | User is redirected to the login page before profile cards render | High |
| MT-PROFILE-006 | Other-user private details restricted | `teacher1` opens another user's profile | 1. Inspect email visibility, login activity, and private details cards | Fields outside `teacher1` permission are not rendered; public name and allowed course details remain visible | Medium |
| MT-PROFILE-009 | Non-Teacher user does not see the Edit profile link | User is logged in with a non-Teacher role (e.g., Student) | 1. Open the top-navigation user menu<br>2. Navigate to Profile | The User details card does not display the "Edit profile" link for this user; no navigation to the Edit profile page is possible | High |
| MT-PROFILE-010 | Non-Teacher user cannot use the Message button | User is logged in with a non-Teacher role (e.g., Student) | 1. Open the top-navigation user menu<br>2. Navigate to Profile<br>3. Attempt to locate and activate the Message button | The Message button is not visible or not enabled for this user; the action to open the message composer is not available | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-PROFILE-007 | Learning plans page opens from Miscellaneous card | Profile page is open | 1. Click the Learning plans link in the Miscellaneous card | The Learning plans page opens showing the "Learning plans" heading and the user's learning plans area | Low |
| MT-PROFILE-008 | Grades overview report opens from Reports card | Profile page is open | 1. Click the Grades overview link in the Reports card | The Grades overview report page opens showing the "Grades overview" heading and the grades overview table or summary area | Low |
| MT-PROFILE-011 | Very long profile description | Teacher profile has a 10,000+ character description | 1. Open Profile | Description renders safely without breaking layout | Low |
| MT-PROFILE-012 | Profile description accepts emoji and extended Unicode characters | Profile page is open | 1. Click Edit profile<br>2. Enter a profile description containing emoji and extended Unicode characters<br>3. Save | Save completes; the Profile page displays the description showing the emoji and Unicode characters verbatim, with no replacement characters or encoding errors | Low |
| MT-PROFILE-013 | Profile picture loading failure | Custom profile picture URL is unreachable | 1. Open Profile | Profile falls back gracefully to displaying the teacher's initials | Low |
| MT-PROFILE-014 | Forum discussions page opens from Miscellaneous card | Profile page is open | 1. Click the Forum discussions link in the Miscellaneous card | The Forum discussions page opens showing the "Forum discussions" heading and the list area for the user's discussions | Low |
