# Test Cases — Mifos

Generated: 2026-07-04T17:13:41.270116Z  
Model: openai/gpt-5-mini  

## Logout

Total: **11** (positive: 4, negative: 3, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Profile Menu reveals logout option | User is currently authenticated with an active session and a valid authentication token. | 1. Click the User Profile icon in the top-right navigation bar. | The User Profile dropdown is visible showing the 'Profile Settings' link and the 'Log Out' button. | low |
| TC-002 | WF-002 | Navigate to Profile Settings from profile menu | User is currently authenticated with an active session and a valid authentication token. | 1. Click the User Profile icon to open the profile menu.<br>2. Click the 'Profile Settings' entry in the dropdown. | The Profile Settings page is displayed (the Profile Settings page content and heading are visible). | medium |
| TC-003 | WF-003 | Log out terminates session and returns to Login page | User is currently authenticated with an active session and a valid authentication token. | 1. Click the User Profile icon to open the profile menu.<br>2. Click the 'Log Out' button in the dropdown. | The Login page is displayed; the user profile icon is no longer present in the top navigation, indicating the user is logged out. | high |
| TC-004 | WF-003 | After logout, attempting to access an authenticated route redirects to Login | User has just logged out and is on the Login page. | 1. In the browser address bar, navigate to an authenticated URL by entering <authenticated route> and pressing Enter. | The Login page is displayed; the requested authenticated page is not shown (the attempt to open <authenticated route> redirects to the Login page). | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-003 | Unauthenticated user cannot reach Log Out (precondition not met) | User is not authenticated (no active session / not logged in) | 1. Open the application landing URL as an unauthenticated user<br>2. Observe the top-right corner of the persistent top navigation bar | The User Profile icon is not visible in the top-right corner and the Log Out option is not available; the Log Out action cannot be invoked from the UI (no Log Out control present) and the Login page / Login form is displayed | high |
| TC-006 | WF-002 | After logging out, navigating to Profile Settings is blocked and redirects to Login | User is authenticated with an active session | 1. Click the User Profile icon in the top-right to reveal the profile dropdown<br>2. Click the Log Out button in the profile dropdown<br>3. In the browser address bar, attempt to navigate to the Profile Settings page by entering <Profile Settings page URL> and pressing Enter | Navigation to the Profile Settings page is blocked: the application redirects to the Login page instead of showing Profile Settings; Profile Settings content is not displayed and no User Profile icon is visible (user remains unauthenticated) | high |
| TC-007 |  | Direct access to the Log Out action while unauthenticated is rejected / redirected | User is not authenticated (no active session) | 1. Open the browser and enter <Log Out action URL> (direct logout endpoint or bookmarked logout link) as an unauthenticated user<br>2. Press Enter to load the URL | The request is rejected/handled as unauthenticated: the Login page is displayed instead of any authenticated page; no logout processing of an active session occurs (there was no active session) and no authenticated UI (User Profile icon) is shown | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (interaction_edge) | WF-003 | Rapid double-click Log Out from profile dropdown | User is authenticated and sees User_Profile_Icon in the top navigation | 1. Click User_Profile_Icon to open User_Profile_Dropdown<br>2. Click Log_Out<br>3. Immediately click Log_Out a second time (second click occurs before redirect completes) | Log out succeeds: the Login page is displayed and the user is not returned to any authenticated page; the second click does not produce a visible error or create a second active session. | medium |
| TC-009 (state_edge) | WF-003 | Press browser Back after successful logout | User is authenticated and sees User_Profile_Icon in the top navigation | 1. Click User_Profile_Icon to open User_Profile_Dropdown<br>2. Click Log_Out<br>3. After being redirected, click the browser Back button | Access is blocked: after pressing Back the Login page is shown (user is not returned to authenticated content and authenticated pages redirect to Login). | medium |
| TC-010 (state_edge) | WF-003 | Manually enter an authenticated-route URL immediately after logout | User is authenticated and sees User_Profile_Icon in the top navigation | 1. Click User_Profile_Icon to open User_Profile_Dropdown<br>2. Click Log_Out<br>3. In the browser address bar, enter the URL of a known authenticated page and press Enter | Navigation is blocked: user is redirected to and shown the Login page instead of the requested authenticated page. | medium |
| TC-011 (interaction_edge) | WF-003 | Click Profile Settings after initiating Log Out from the open dropdown | User is authenticated and sees User_Profile_Icon in the top navigation | 1. Click User_Profile_Icon to open User_Profile_Dropdown<br>2. Click Log_Out<br>3. Immediately click Profile_Settings link in the same dropdown (second click after logout was initiated) | Log out succeeds and navigation to Profile Settings is blocked: the Login page is displayed and the Profile Settings page is not shown. | medium |

---
