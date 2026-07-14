# Moodle Student Test Cases — Ground Truth

Source: dataset/ground_truth/MoodleStudent/MoodleStudent.md

## Profile

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-PROFILE-001 | Student profile details displayed | Student is logged in | 1. Open Profile | Initials icon, full name, message button, and optional description are visible | High |
| MS-PROFILE-002 | Profile information cards displayed | Profile page is open | 1. Inspect information cards | User details, privacy/policies, course details, miscellaneous, reports, and login activity are visible | High |
| MS-PROFILE-003 | Edit profile form opens | Profile page is open | 1. Click "Edit profile" | Edit profile form opens | High |
| MS-PROFILE-004 | Update own profile | Edit profile form is open for `student1` | 1. Edit City/town to `Dhaka QA` and Description to `Student profile update check`<br>2. Click "Update profile"<br>3. Reopen Profile | City/town and description updates are visible on `student1` profile | High |
| MS-PROFILE-005 | Upload own profile picture | Edit profile form is open | 1. Upload `student-avatar.png` under 10 MB<br>2. Click "Update profile"<br>3. Reopen Profile | Student profile picture changes from initials to the uploaded image preview | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-PROFILE-006 | Profile blocked while unauthenticated | User is logged out | 1. Navigate directly to profile URL | User is redirected to login | High |
| MS-PROFILE-007 | Student cannot edit another user's profile | Student opens another user's profile | 1. Inspect profile controls<br>2. Navigate directly to that user's edit-profile URL | Edit controls are not rendered and direct edit URL shows access denied before the edit form renders | High |
| MS-PROFILE-008 | Required profile field empty | Edit profile form is open | 1. Clear First name, Last name, or Email<br>2. Save | Required-field validation blocks save | High |
| MS-PROFILE-009 | Invalid profile email | Edit profile form is open | 1. Enter invalid email<br>2. Save | Email validation blocks save | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-PROFILE-010 | Cancel edit profile | Edit profile form has unsaved changes | 1. Click "Cancel" | Unsaved changes are discarded | Medium |
| MS-PROFILE-011 | Missing optional description | Student profile has no description | 1. Open Profile | Profile page renders initials, full name, and information cards; description area is empty and no placeholder error is shown | Low |
| MS-PROFILE-012 | Very long Description field (200+ chars) accepted or blocked with visible feedback | Edit profile form is open for `student1` | 1. Enter a 200+ character string in the Description field<br>2. Click "Update profile" | Either the description is saved and visible on the profile page, or a clear validation message explains the length limit; no silent data loss or crash occurs | Low |
| MS-PROFILE-013 | Non-Latin Unicode and emoji in First/Last name fields accepted or blocked with visible feedback | Edit profile form is open for `student1` | 1. Enter `জন 🎓` in the First name field and `ডো 🎓` in the Last name field<br>2. Click "Update profile" | Either the names are saved and rendered correctly on the profile page, or a clear validation message explains the character restriction; no garbled text or silent failure occurs | Low |
| MS-PROFILE-014 | Rapid re-submit of Update profile does not create duplicate profile records | Edit profile form is open for `student1` with a change ready | 1. Click "Update profile" rapidly twice | Profile is saved once; no duplicate profile record is created and no duplicate success/error message is stacked | Medium |
