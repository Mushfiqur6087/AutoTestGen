# Moodle Student Test Cases — Ground Truth

Source: dataset/ground_truth/MoodleStudent/MoodleStudent.md

## Logout

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-LOGOUT-001 | Logout from user menu | Student is logged in | 1. Open user menu<br>2. Click "Log out" | Session ends and login page is displayed | High |
| MS-LOGOUT-002 | Protected page requires re-authentication after logout | Student has logged out | 1. Navigate directly to Dashboard, course, or assignment URL | User is redirected to login | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-LOGOUT-003 | Browser back after logout | Student logged out from protected page | 1. Press browser Back | Login page remains active or protected page immediately redirects to login; dashboard/course content is not rendered from browser cache | High |
| MS-LOGOUT-004 | Logout option unavailable while logged out | User is on login page | 1. Inspect user menu area | Authenticated user menu and logout option are absent | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-LOGOUT-005 | Double-click logout | Student is logged in | 1. Double-click "Log out" | Logout completes once without visible error | Low |
| MS-LOGOUT-006 | Session timeout behaves like logout | Student session has expired | 1. Open protected page | User is required to authenticate again | High |
| MS-LOGOUT-007 | Logout in Tab A blocks protected page reload in Tab B — redirect to login | `student1` is logged in on two browser tabs showing a protected page | 1. In Tab A, log out via the user menu<br>2. Switch to Tab B<br>3. Reload the protected page in Tab B | Tab B redirects to the login page; no authenticated content from the previous session is rendered | High |
| MS-LOGOUT-008 | Navigate directly to protected URL after logout redirects to login page | `student1` has just logged out | 1. Type the Dashboard URL directly into the address bar and press Enter | Browser is redirected to the login page; Dashboard content is not rendered | High |
