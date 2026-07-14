# Moodle Teacher Test Cases — Ground Truth

Source: dataset/ground_truth/MoodleTeacher/MoodleTeacher.md

## Logout

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-LOGOUT-001 | Logout from user menu | Teacher is logged in | 1. Open user menu<br>2. Click "Log out" | Session ends and login page is displayed | High |
| MT-LOGOUT-002 | Protected page requires re-authentication after logout | Teacher has logged out | 1. Navigate directly to Dashboard or course URL | User is redirected to login | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-LOGOUT-003 | Browser back after logout | Teacher logged out from protected page | 1. Press browser Back | Login page remains active or protected page immediately redirects to login; dashboard/course content is not rendered from browser cache | High |
| MT-LOGOUT-004 | Logout action unavailable while logged out | User is on login page | 1. Inspect user menu area | Authenticated user menu and logout option are not visible | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-LOGOUT-005 | Double-click logout | Teacher is logged in | 1. Double-click "Log out" | Logout completes once without error or duplicate redirect loops | Low |
| MT-LOGOUT-006 | Session timeout behaves like logout | Teacher session has expired | 1. Open protected page | User is required to authenticate again | High |
| MT-LOGOUT-007 | Concurrent sessions log out | Teacher has two browser tabs open | 1. Log out in tab 1<br>2. Attempt action in tab 2 | Tab 2 redirects to login upon interaction | High |
| MT-LOGOUT-008 | Logout URL CSRF protection | User is logged in | 1. Manually navigate to `logout.php` without token | Action is blocked and requires confirmation to prevent CSRF logout | Medium |
| MT-LOGOUT-009 | Rapid navigation during logout | Teacher clicks logout | 1. Click "Log out"<br>2. Rapidly click a navigation link before redirect | Logout proceeds and user ends up unauthenticated on the destination or login page | Low |
