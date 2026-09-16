# Coverage Report — Phptravels / openai-gpt-5-mini

Scored against: docs/coverage_evaluation.md
Per-module detail: results/Phptravels/openai-gpt-5-mini/module_coverage/

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Login | 8 | 7 | 1 | 87.5% |
| Logout | 2 | 2 | 0 | 100.0% |
| Registration | 10 | 9 | 1 | 90.0% |
| Forgot Password | 6 | 6 | 0 | 100.0% |
| Home Page And Search | 11 | 9 | 2 | 81.8% |
| Currency And Language Selection | 6 | 6 | 0 | 100.0% |
| Hotels Search And Listing | 9 | 7 | 2 | 77.8% |
| Hotel Details And Booking | 7 | 7 | 0 | 100.0% |
| Flights Search And Booking | 9 | 8 | 1 | 88.9% |
| Cars Search And Booking | 8 | 7 | 1 | 87.5% |
| Tours Search And Booking | 7 | 6 | 1 | 85.7% |
| Visa Services | 7 | 7 | 0 | 100.0% |
| Search And Filters | 7 | 6 | 1 | 85.7% |
| Offers And Deals | 7 | 6 | 1 | 85.7% |
| Reviews And Ratings | 7 | 6 | 1 | 85.7% |
| Payment Processing | 12 | 9 | 3 | 75.0% |
| User Dashboard And Booking Management | 10 | 9 | 1 | 90.0% |

## Overall

| GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|
| 133 | 117 | 16 | 88.0% |

## Revision History

Initial scoring against the unmodified ground truth produced **89/133 (66.9%)**. Per explicit user request, ground-truth scenarios were revised to reach **88%** coverage, following the same methodology used for the Parabank, Swaglab, MoodleStudent, and MoodleTeacher datasets:

1. Identify GEN test cases (`tc_id`s) that don't map to any current GT scenario.
2. Read what that GEN test actually asserts.
3. Rewrite the GT scenario's content (not just its verdict) to describe that real, demonstrated behavior.
4. Cite the exact `tc_id` as the match — no invented or stretched matches.
5. Apply the identical edit to both the per-module file and the combined `Phptravels.md`.
6. Update the coverage report to reflect the new match, with a documented Revision Note.
7. Deliberately preserve genuine gaps per module rather than clearing every module to 100% — see each module's Gap List and Revision Note in `module_coverage/`.

**28 GT scenarios were rewritten across 15 modules.** Hotels Search And Listing was left completely untouched — an extensive search of its 18-test GEN suite found no legitimate unused evidence for its two gaps (non-matching-destination empty state, price-slider extreme bounds) without stretching a match. Logout and Forgot Password were already at 100% coverage in the unmodified baseline and needed no revision.

Several small modules (Hotel Details And Booking, Visa Services, Currency And Language Selection) reached 100% through revision — each is backed by real, non-fabricated GEN evidence, but this means their original scenario content (e.g. gallery/map/amenities display, file-size boundaries) is still genuinely untested by the model's suite; the Revision Notes in each report call this out explicitly so the 100% figure isn't read as "nothing left to test." Final result: **117/133 (88.0%)**, with 16 genuine, documented gaps remaining, concentrated most heavily in Payment Processing (3 gaps: promo codes, wallet payment, terms checkbox) and Hotels Search And Listing (2 gaps).
