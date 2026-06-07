# Post-Verification Specifications

### [TC-004] Rapid consecutive logout attempts
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the Logout button
2. 2. Immediately click the Logout button again

**Original Expected Result:** Second logout attempt is ignored; user is redirected to the login page only once

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard`
- **Observe**:
  - Calendar block is visible
  - No new event interface is open

**Post-Check**
- **Navigate To**: `Calendar block`
- **Observe**:
  - New event creation interface is open

**Expected Change**: The new event creation interface is displayed after clicking the New Event Button.

---

### [TC-001] User logs out successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button

**Original Expected Result:** User is redirected to the login page; access to all protected pages requires re-authentication after logout.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `My Courses`
- **Observe**:
  - course grid does not show the starred course at the top

**Post-Check**
- **Navigate To**: `My Courses`
- **Observe**:
  - starred course appears at the top of the course grid

**Expected Change**: The starred course is now pinned to the top of the course grid.

---

### [TC-001] User logs out successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button

**Original Expected Result:** User is redirected to the login page; access to all protected pages requires re-authentication after logout.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Assignment page for Essay Draft`
- **Observe**:
  - submission status shows 'Not submitted'
  - no text in online text editor

**Post-Check**
- **Navigate To**: `Assignment page for Essay Draft`
- **Observe**:
  - submission status shows 'Submitted for grading'
  - submitted text is visible in the submission preview

**Expected Change**: The submission status changes to 'Submitted for grading' and the entered text is displayed in the submission preview.

---

### [TC-002] Unauthenticated user attempts to log out
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure user is not authenticated
2. 2. Click Logout_Button

**Original Expected Result:** Logout action is blocked; user remains on the current page; no session is terminated.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Assignment page for Essay Draft`
- **Observe**:
  - submission status shows 'Not submitted'
  - no uploaded files listed

**Post-Check**
- **Navigate To**: `Assignment page for Essay Draft`
- **Observe**:
  - submission status shows 'Submitted for grading'
  - uploaded file is listed as a downloadable link

**Expected Change**: The submission status changes to 'Submitted for grading' and the uploaded file appears in the submission file list.

---

### [TC-004] Rapid consecutive logout attempts
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the Logout button
2. 2. Immediately click the Logout button again

**Original Expected Result:** Second logout attempt is ignored; user is redirected to the login page only once

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Assignment page for Essay Draft`
- **Observe**:
  - Submission status shows 'Submitted for grading'

**Post-Check**
- **Navigate To**: `Assignment page for Essay Draft`
- **Observe**:
  - Submission edit form is displayed

**Expected Change**: The submission edit form is now visible, allowing the student to modify their submission.

---

### [TC-002] Unauthenticated user attempts to log out
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure user is not authenticated
2. 2. Click Logout_Button

**Original Expected Result:** Logout action is blocked; user remains on the current page; no session is terminated.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Profile`
- **Observe**:
  - First Name field shows previous value
  - Last Name field shows previous value
  - Email Address field shows previous value

**Post-Check**
- **Navigate To**: `Profile`
- **Observe**:
  - First Name field shows <valid first name>
  - Last Name field shows <valid last name>
  - Email Address field shows <valid email>

**Expected Change**: The profile reflects the updated first name, last name, and email address as entered.

---
