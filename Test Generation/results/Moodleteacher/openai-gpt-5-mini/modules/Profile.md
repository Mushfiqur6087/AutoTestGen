# Test Cases — Moodleteacher

Generated: 2026-07-04T16:52:18.651847Z  
Model: openai/gpt-5-mini  

## Profile

Total: **17** (positive: 10, negative: 4, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open messaging composer via Message button | User logged in as <Teacher> | 1. Navigate to the Profile page via the user menu<br>2. Click the Message button in the profile action bar | A message composition interface is displayed on-screen showing the 'To' field, 'Subject' field, message body editor and a Send button | high |
| TC-002 | WF-002 | Navigate to Edit profile from User details card | User logged in as <Teacher> | 1. Navigate to the Profile page via the user menu<br>2. Click the Edit profile link in the User details card | The Edit profile page is shown with editable fields such as Full name, Email, Description and a visible Save button | high |
| TC-003 | WF-003 | Open Data retention summary from Privacy and policies card | User logged in as <Teacher> | 1. Navigate to the Profile page via the user menu<br>2. Click the Data retention summary link in the Privacy and policies card | The Data retention summary page is displayed with a page heading 'Data retention summary' and the data retention content area visible | medium |
| TC-004 | WF-004 | Open a course profile from Course details | User logged in as <Teacher>, Profile has at least one associated course profile link | 1. Navigate to the Profile page via the user menu<br>2. Click the first Course profile link in the Course details card | The selected course profile page opens, showing the course title and the user's profile content for that course | medium |
| TC-005 | WF-005 | View Blog entries from Miscellaneous card | User logged in as <Teacher> | 1. Navigate to the Profile page via the user menu<br>2. Click the Blog entries link in the Miscellaneous card | The Blog entries page opens showing the page heading 'Blog entries' and the list area for the user's blog posts | medium |
| TC-006 | WF-006 | View Forum posts from Miscellaneous card | User logged in as <Teacher> | 1. Navigate to the Profile page via the user menu<br>2. Click the Forum posts link in the Miscellaneous card | The Forum posts page opens showing the page heading 'Forum posts' and the list area for the user's forum posts | medium |
| TC-007 | WF-007 | View Forum discussions from Miscellaneous card | User logged in as <Teacher> | 1. Navigate to the Profile page via the user menu<br>2. Click the Forum discussions link in the Miscellaneous card | The Forum discussions page opens showing the page heading 'Forum discussions' and the list area for the user's discussions | medium |
| TC-008 | WF-008 | Open Learning plans from Miscellaneous card | User logged in as <Teacher> | 1. Navigate to the Profile page via the user menu<br>2. Click the Learning plans link in the Miscellaneous card | The Learning plans page opens showing the page heading 'Learning plans' and the user's learning plans area | medium |
| TC-009 | WF-009 | Open Browser sessions report from Reports card | User logged in as <Teacher> | 1. Navigate to the Profile page via the user menu<br>2. Click the Browser sessions link in the Reports card | The Browser sessions report page is displayed showing a sessions table (columns such as device, IP and timestamps) or a visible sessions list area | medium |
| TC-010 | WF-010 | Open Grades overview report from Reports card | User logged in as <Teacher> | 1. Navigate to the Profile page via the user menu<br>2. Click the Grades overview link in the Reports card | The Grades overview report page opens showing the 'Grades overview' heading and the grades overview table or summary area | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 |  | Unauthenticated user cannot open the Profile page (redirect to login) | User is not authenticated (no active session) | 1. As an unauthenticated user, navigate to the Profile page URL or click the top-navigation user menu -> Profile | User is redirected to the <login page>; the Profile page content (initials icon, full name, cards) is not displayed. | high |
| TC-012 | WF-002 | Non-Teacher user does not see the Edit profile link on Profile page | Authenticated session as a non-Teacher role (e.g., Student or Guest) | 1. Log in as a user with a role other than Teacher<br>2. Open the top-navigation user menu and navigate to Profile | The User details card does not display the 'Edit profile' link for users without the Teacher role; the link is not clickable and no navigation to the Edit profile page is possible from the Profile page. | high |
| TC-013 | WF-001 | Non-Teacher user does not see or cannot use the Message button | Authenticated session as a non-Teacher role (e.g., Student or Guest) | 1. Log in as a user with a role other than Teacher<br>2. Open the top-navigation user menu and navigate to Profile<br>3. Attempt to locate and activate the Message button in the Profile action bar | The Message button is not visible or not enabled for users without the Teacher role; the action to open the message composer is not available from the Profile page. | high |
| TC-014 | WF-002 | Unauthenticated direct access to Edit profile is blocked (redirect to login) | User is not authenticated (no active session) | 1. As an unauthenticated user, navigate directly to the Edit profile page URL (e.g., the target URL behind the 'Edit profile' link) | User is redirected to the <login page>; the Edit profile page is not displayed and no editing controls are accessible. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 (input_edge) |  | Very long profile description (200+ characters) saved and displayed | Authenticated session as a teacher (logged in), On the Profile page | 1. Click the Edit profile link on the User details card<br>2. Enter a very long string (200+ characters) into the Profile description field<br>3. Click the Save changes button<br>4. Observe the Profile page and the displayed profile description | Save completes; the Profile page displays the full entered profile description text (no truncation shown in the visible profile description area) | medium |
| TC-016 (input_edge) |  | Profile description accepts emoji and extended Unicode characters | Authenticated session as a teacher (logged in), On the Profile page | 1. Click the Edit profile link on the User details card<br>2. Enter a profile description containing emoji and extended Unicode characters (e.g., multi-codepoint emoji and non-Latin scripts)<br>3. Click the Save changes button<br>4. Observe the Profile page and the displayed profile description | Save completes; the Profile page displays the profile description showing the emoji and Unicode characters verbatim (no replacement characters or visible encoding errors) | low |
| TC-017 (interaction_edge) | WF-001 | Rapid double-click on Message button does not open duplicate composers | Authenticated session as a teacher (logged in), On the Profile page | 1. Click the Message button on the Profile action bar<br>2. Immediately click the Message button again (second click within a short interval) | A single message composition interface is visible; the UI does not open a second composer instance and the second click is ignored or disabled (no duplicate composer windows/modals are shown) | medium |

---
