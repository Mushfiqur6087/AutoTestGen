# ParaBank Test Cases — Ground Truth

Source: dataset/ground_truth/Parabank/Parabank.md

## Support Center

### Secure Message Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MW-SC-001 | Send message successfully | User logged in | 1. Enter Subject<br>2. Select Category<br>3. Enter Message Body<br>4. Click "Send Message" | "Message sent successfully." with ticket ID | High |
| MW-SC-002 | Send with attachment | User logged in | 1. Fill required fields<br>2. Attach valid file<br>3. Submit | Message sent with attachment | Medium |
| MW-SC-003 | Empty subject | User logged in | 1. Leave Subject empty<br>2. Submit | Validation error | High |
| MW-SC-004 | Empty message body | User logged in | 1. Leave Message Body empty<br>2. Submit | Validation error | High |
| MW-SC-005 | Invalid attachment type | User logged in | 1. Attach invalid file type<br>2. Submit | Validation error | Medium |
| MW-SC-006 | Category dropdown | User logged in | 1. Click Category dropdown | Options: Account, Technical, Security, Other | Medium |

### Schedule Callback Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MW-SC-007 | Schedule callback | User logged in | 1. Select Reason for Call<br>2. Select Preferred Date (next business day+)<br>3. Select Time Window<br>4. Verify/edit Phone Number<br>5. Click "Request Callback" | "Callback request submitted." | High |
| MW-SC-008 | Phone pre-filled | User logged in | 1. View callback form | Phone number pre-filled from profile | Medium |
| MW-SC-009 | Date too soon | User logged in | 1. Select today's date or next non-business day<br>2. Submit | Validation error: date must be next business day or later | High |
| MW-SC-010 | Invalid phone format | User logged in | 1. Enter invalid phone<br>2. Submit | Validation error | High |
| MW-SC-011 | Email confirmation | MW-SC-007 completed | Check email | Confirmation email received | Medium |
| MW-SC-012 | Callback preferred time overlapping cutoff | User logged in | 1. Select time exactly at EOD | Validated and processed | Medium |
| MW-SC-013 | Concurrent message submissions | User logged in | 1. Submit message from 2 tabs simultaneously | Handled gracefully | Low |
| MW-SC-014 | Extremely large attachment | User logged in | 1. Attach file > 50MB | Validation error: file too large | High |
