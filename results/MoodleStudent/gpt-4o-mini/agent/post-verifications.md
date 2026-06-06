# Post-Verification Specifications

### [TC-004] Unknown Title
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Test Case Description:**
> No description available.

**Original Steps:**
1. 1. Click on the Logout button
2. 2. Immediately click the Logout button again

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard`
- **Observe**:
  - Calendar block
  - New event button

**Post-Check**
- **Navigate To**: `Dashboard`
- **Observe**:
  - Calendar block
  - New event creation interface

**Expected Change**: The New event creation interface is displayed after clicking the New Event button.

---

### [TC-001] Unknown Title
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Test Case Description:**
> No description available.

**Original Steps:**
1. 1. Click the Logout button

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `My Courses`
- **Observe**:
  - list of courses displayed in the course grid

**Post-Check**
- **Navigate To**: `My Courses`
- **Observe**:
  - pinned course at the top of the course grid

**Expected Change**: The starred course appears at the top of the course grid.

---

### [TC-001] Unknown Title
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Test Case Description:**
> No description available.

**Original Steps:**
1. 1. Click the Logout button

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Page -> Assignment`
- **Observe**:
  - Submission status
  - Grading status

**Post-Check**
- **Navigate To**: `Course Page -> Assignment`
- **Observe**:
  - Submission status
  - Grading status

**Expected Change**: Submission status changes to 'Submitted for grading'; Grading status remains 'Not graded'.

---

### [TC-002] Unknown Title
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Test Case Description:**
> No description available.

**Original Steps:**
1. 1. Ensure user is not authenticated
2. 2. Click Logout_Button

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course X -> Activities tab -> Assignments section`
- **Observe**:
  - submission status
  - grading status

**Post-Check**
- **Navigate To**: `Course X -> Activities tab -> Assignments section`
- **Observe**:
  - submission status
  - grading status

**Expected Change**: Submission status changes to 'Submitted for grading' and grading status remains 'Not graded'.

---

### [TC-004] Unknown Title
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Test Case Description:**
> No description available.

**Original Steps:**
1. 1. Click on the Logout button
2. 2. Immediately click the Logout button again

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Assignment page`
- **Observe**:
  - Submission status
  - Grading status
  - Time remaining

**Post-Check**
- **Navigate To**: `Assignment page`
- **Observe**:
  - Submission status
  - Grading status
  - Time remaining

**Expected Change**: Submission status remains 'Submitted for grading'; Grading status remains 'Not graded'; Time remaining is unchanged.

---

### [TC-002] Unknown Title
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Test Case Description:**
> No description available.

**Original Steps:**
1. 1. Ensure user is not authenticated
2. 2. Click Logout_Button

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Profile`
- **Observe**:
  - First Name
  - Last Name
  - Email Address

**Post-Check**
- **Navigate To**: `Profile`
- **Observe**:
  - First Name
  - Last Name
  - Email Address

**Expected Change**: First Name, Last Name, and Email Address fields reflect the updated values entered during the profile edit.

---
