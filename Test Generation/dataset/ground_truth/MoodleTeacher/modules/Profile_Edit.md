# Moodle Teacher Test Cases — Ground Truth

Source: dataset/ground_truth/MoodleTeacher/MoodleTeacher.md

## Profile Edit

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-PEDIT-001 | Update required profile fields | Teacher opens Edit profile | 1. Set City/town to `Dhaka QA Teacher`<br>2. Set Description to `Teacher profile update check`<br>3. Click "Update profile"<br>4. Reopen Profile | Profile page shows `Dhaka QA Teacher` and `Teacher profile update check` for `teacher1`; original values are restored during cleanup | High |
| MT-PEDIT-002 | Upload profile picture | Edit profile form is open | 1. Upload `teacher-avatar.png` under 10 MB<br>2. Save and reopen Profile | Teacher profile picture changes from initials to the uploaded image preview | Medium |
| MT-PEDIT-003 | Edit additional names and interests | Edit profile form is open | 1. Enter alternative name `GT Teacher Alias`<br>2. Add interest tag `ground-truth`<br>3. Save and reopen Edit profile | `GT Teacher Alias` and `ground-truth` remain populated in their respective fields | Medium |
| MT-PEDIT-004 | Expand all profile panels | Edit profile form is open | 1. Click "Expand all" | All collapsible sections expand | Low |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-PEDIT-005 | First name empty | Edit profile form is open | 1. Clear First name<br>2. Save | Required-field validation blocks save | High |
| MT-PEDIT-006 | Last name empty | Edit profile form is open | 1. Clear Last name<br>2. Save | Required-field validation blocks save | High |
| MT-PEDIT-007 | Invalid email address | Edit profile form is open | 1. Enter invalid email<br>2. Save | Email validation blocks save | High |
| MT-PEDIT-008 | Oversized profile picture | Edit profile form is open | 1. Upload `oversize-11mb.pdf` in the profile picture upload control | Upload is rejected with file-type or file-size validation feedback and no new profile picture is saved | Medium |
| MT-PEDIT-011 | Submit with all required fields cleared | Edit profile form is open | 1. Clear First name, Last name, and Email<br>2. Click "Update profile" | Multiple validation errors appear simultaneously and form is not submitted | High |
| MT-PEDIT-012 | Missing email domain | Edit profile form is open | 1. Enter `teacher1@`<br>2. Save | Email validation explicitly rejects the missing domain | High |
| MT-PEDIT-013 | File size exactly one byte over limit | Edit profile form is open | 1. Upload an image one byte over the site maximum<br>2. Save | Upload is explicitly rejected for exceeding the max upload size | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-PEDIT-009 | Cancel profile edit | Edit profile form has unsaved changes | 1. Click "Cancel" | Unsaved changes are discarded | Medium |
| MT-PEDIT-010 | Maximum valid picture size | Edit profile form is open | 1. Upload `teacher-avatar-10mb.png` at the configured image upload limit<br>2. Save and reopen Profile | Uploaded image displays as the teacher profile picture after reload | Low |
| MT-PEDIT-014 | Description with 10,000+ characters | Edit profile form is open | 1. Enter 10,000+ chars into description<br>2. Save | Profile saves successfully and text is visible | Low |
| MT-PEDIT-015 | Emoji and non-Latin Unicode in First Name | Edit profile form is open | 1. Enter emoji into First name<br>2. Save | Profile saves and emoji are preserved | Low |
| MT-PEDIT-016 | Leading and trailing whitespace trimmed | Edit profile form is open | 1. Enter `   teacher   ` as First name<br>2. Save | Whitespace is automatically trimmed upon save | Low |
| MT-PEDIT-017 | Rapid double-click on Update profile | Edit profile form is open | 1. Rapidly double-click "Update profile" | Form submits exactly once without duplicate requests | Medium |
| MT-PEDIT-018 | Add and immediately remove repeating group item | Edit profile form is open | 1. Add an Additional name item<br>2. Immediately remove it<br>3. Save | Save succeeds without leaving ghost entries for the additional name | Medium |
