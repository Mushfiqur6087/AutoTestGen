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
| MT-PROFILE-009 | View non-existent user profile | Teacher is logged in | 1. Manually edit profile URL to use an invalid user ID (e.g., `?id=99999`) | System displays a standard user-not-found error page | High |
| MT-PROFILE-010 | Student viewing teacher profile | `student1` is logged in | 1. Navigate to `teacher1` profile | Private activity reports and sensitive data cards are hidden from the student | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-PROFILE-007 | Missing optional description | Teacher profile has no description | 1. Open Profile | Profile page renders initials, full name, and information cards; description area is empty and no placeholder error is shown | Low |
| MT-PROFILE-008 | Long display name | Teacher profile full name is 80+ characters | 1. Open Profile | Full name wraps within the profile header, and the message button remains visible below or beside the name | Low |
| MT-PROFILE-011 | Very long profile description | Teacher profile has a 10,000+ character description | 1. Open Profile | Description renders safely without breaking layout | Low |
| MT-PROFILE-012 | Emoji in display name | Teacher profile name contains emoji | 1. Open Profile | Emoji render correctly in the profile header | Low |
| MT-PROFILE-013 | Profile picture loading failure | Custom profile picture URL is unreachable | 1. Open Profile | Profile falls back gracefully to displaying the teacher's initials | Low |
| MT-PROFILE-014 | Enrolled in numerous courses | Teacher is enrolled in 50+ courses | 1. Open Profile | Course details card displays courses in a scrollable list or paginates cleanly | Low |
