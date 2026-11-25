# Validation — connected publication v1.5

Completed 21 November 2026.

- Both publication drafts were reviewed against nine official source pages. Reporting, interpretation and proposed practices remain distinct. The evidence collection and existing matrix data are unchanged.
- Source/data validation and Node syntax checks pass, including eight unique moment routes with valid cases and DOM targets.
- Browser checks covered all eight moment destinations, case selection, the R020/R024 comparison, direct case R010 opening and reload, copy-case-link feedback and clipboard contents, article-to-exhibit navigation and browser Back.
- The workbook moment opens at step 3 on desktop and at the scene in a 390 × 844 CSS-pixel phone frame. The phone reading page and linked scene were visually reviewed. This is responsive QA, not physical-device or cross-browser certification.
- Word exports were rendered and every page inspected: seven essay pages and four article pages, including references. Hyperlink relationships and removal of title borders were checked programmatically.
- Publication validation checks the six article links, eight essay links, citation suffixes, relative file destinations, Word link targets and the pending public-URL state.
- Temporary QA pages are excluded from deployment and packaging. The package allowlist excludes hosting identity, credentials and Git metadata; its ZIP integrity and file hashes are verified by the packaging script.
- No application-origin error appeared in inspected console entries. Browser-extension errors were unrelated to the app.

Public GitHub hosting and Substack editor/email rendering are pending. Current Word links use the private review Site. HTML reading-page links work within the extracted package and are portable to public hosting.

## Earlier verification

# Validation — connected exploration edition v1.4

Completed 21 November 2026.

- Integrity checks pass for all 29 disclosures, 29 source-mapped boundary rows, six boundary definitions, correct notice/report review basis, preserved exceptions, the two numerical close-ups and five checkpoint rows. Original `data/evidence.json` and `data/matrix.json` are unchanged.
- R006 preserves approximate 10%/16% rubric-item shares, a labelled 0–20% axis and the absence of a raw denominator. R010 preserves three grader units and two accepted claims. Browser checks confirmed the rendered values and expandable grader explanations.
- Browser-tested all 29 timing selections: the selected-case badge and timeline title match each record. Exactly 24 selections identify checkpoint coding as not reviewed; no fallback row is highlighted for those cases.
- The unfiltered authority view renders 29 rows and 174 selectable cells. The Collaboration filter includes R024 through its additional boundary coding. Tested no-match search and clearing filters.
- Checked source-linked boundary receipts for R024, the explicitly non-misaligned R020, and the unresolved N001 claim. The notice receipt states that its dated detail was not refreshed. Keyboard activation works; closing a regenerated table cell's receipt returns focus to that cell.
- Two-case comparison excludes the selected case from its 28 comparison choices and displays separate task/action/outcome/limit text. Uncoded cases retain explicit not-reviewed checkpoint labels.
- Response checks cover reported action, source status and evidence/gap for R011 and R024; proposed follow-up questions stay separate from claims of demonstrated effectiveness.
- Copy instruction succeeds in the desktop preview and phone iframe. The clipboard text matches the rendered approved-service/fallback instruction. Manual-copy fallback was code-reviewed, not fault-injected in the browser.
- Reviewed desktop and responsive 360 × 844 / 760 × 844 CSS-pixel iframes, including light/dark appearances. Phone/tablet document client and scroll widths match at 345/745 pixels after scrollbars. The phone comparison table scrolls inside its 288-pixel region; the sticky case column measures 146 pixels.
- Phone checks cover branch mode as the default, changing branch, keyboard-opening the simulated case, chapter navigation, grader explanation, response selection and copying. The paired dot chart uses native-size text instead of shrinking SVG labels.
- No application-origin console errors appeared in the inspected entries. Browser-extension metadata errors were unrelated to the experience.
- The build passes JavaScript syntax, unique IDs, navigation targets, resolved fragments, embedded image integrity and locked-section checks. The nine-minute reading guide is an editorial estimate, not a timed study.

Limits: responsive browser testing, not physical-device, cross-browser or assistive-technology certification. The 26 report pages were re-read for new authority coding, while the three notice accounts, timelines and response records retain their collected snapshot. Data integrity checks do not independently verify publisher claims.

# Validation — reader introduction edition v1.3

Completed 21 November 2026.

- Reviewed the orientation beneath the title and the new author-purpose/reader-benefit preface at desktop size and in a 360 × 844 CSS-pixel phone iframe. The phone document has matching client/scroll widths of 345 pixels after the scrollbar; the preface stacks without whole-document horizontal overflow.
- Checked that the three stated takeaways correspond to the existing reconstruction, evidence comparison and delegation exercise. The author note introduces no new career history or incident findings.
- The reading estimate is now about seven minutes. The opening adds 171 words over v1.2; the main narrative is approximately 1,400 words using the earlier narrative estimate plus the opening revisions. This is an editorial estimate at 200 words per minute, not a timed reader study.
- Existing integrity validation passes for all 29 disclosures, five matrix rows, source mappings, locked sections, navigation, embedded image and built JavaScript syntax. The evidence files and JavaScript are unchanged.
- This is a copy and responsive-layout update. Previous interaction checks remain the baseline and were not all repeated.

# Validation — opening edition v1.2

Completed 21 November 2026.

- Reviewed the revised opening in light and dark appearances. The transparent emblem loads at its full source dimensions and stays separate from the title and evidence reconstruction.
- Checked desktop at 1,348 pixels of document width and 360 × 844 / 760 × 844 CSS-pixel responsive iframes. The iframe documents measured 345 / 745 pixels after their scrollbars, with matching scroll widths and no whole-document horizontal overflow. The emblem does not overlap the first two title lines on the narrow phone layout.
- Browser-tested pause and play: labels, pressed states and animation classes update correctly. Leaving the opening pauses the emblem; returning resumes it when motion is enabled.
- Reviewed the CSS and JavaScript reduced-motion branches: the decorative trace is hidden, animation disabled and the control labelled Motion off. This was source inspection, not a browser preference-emulation test.
- The standalone build embeds the original PNG bytes. Validation checks the embedded bytes against the source image, disclosure integrity, locked sections, internal navigation and built JavaScript syntax.
- No application-origin console errors appeared in the inspected entries. Browser-extension metadata errors were unrelated to the experience.
- The evidence dataset, matrix coding and visualizations are unchanged from v1.1. Earlier evidence/interaction checks below remain the baseline; they were not all repeated for this opening-only edit.

Limits: responsive browser testing, not physical-device, cross-browser or assistive-technology certification. The new motion has not been assessed in an audience study.

# Validation — audience edition v1.1

Completed 21 November 2026. Recommendations D01–D08 are recorded in DECISIONS.md.

- Kept the eight-section order, existing visual forms, atlas classifications and all 29 disclosure records.
- Re-read the five matrix source pages through the official OpenAI pages on 21 November. Store action-specific evidence states, scope, source section and reviewed URL in data/matrix.json. This was not a refresh of all 29 source records.
- Data validation covers disclosure and category counts, source and response mappings, date precision, five complete matrix rows, source identity, special case labels, locked section order, navigation targets and built JavaScript syntax.
- Browser-tested all 20 matrix cells: each opens the correct case, event, coding review date and source URL. The supported migration stays explicitly non-misaligned; the simulated delivery stays qualified by its setting.
- Exercised all four delegation combinations. The local fallback stays local; a named-recipient service is explicitly a hypothetical expansion of the original task. Feedback preserves the difference between upload success and recipient delivery.
- Tested a case outside the matrix: R002 retains its source panel and states that it was not re-reviewed for the expansion. The comparison explicitly identifies its fallback row instead of assigning unknown markers to an uncoded case.
- Reviewed desktop opening and matrix in dark/light appearances, and a 390 × 844 CSS-pixel phone iframe. Phone document client/scroll width both 375 pixels (excluding its scrollbar); no whole-document horizontal overflow. The existing matrix scrolls inside its own container.
- Phone checks included navigation, colour toggle, search, a new matrix evidence receipt, explanation expansion and local fallback feedback. Native disclosure controls keep optional reading out of the main narrative.
- The default main narrative plus default evidence text was approximately 1,183 words using rendered DOM content from the relevant narrative, matrix and timeline elements. The six-minute estimate uses an assumed 200 words per minute and excludes optional explanations/source inspection. It is not a timed reader study and does not estimate exploration time.
- No application-origin errors appeared in the inspected browser console entries.

Limits: responsive browser testing, not physical-device or cross-browser certification; no assistive-technology certification or audience comprehension study. The source snapshot remains 18 November and authority themes remain the 19 November review. Only the five matrix examples were re-reviewed on 21 November.

## Earlier baseline verification

# Validation — working narrative v1.0

Completed 21 November 2026.

- Data checks: exactly 29 distinct disclosure IDs, 26 reports and 3 notices, expected category counts, source/response mapping, valid dates, date-limit preservation, internal navigation targets, and unique HTML IDs.
- The JavaScript extracted from the built standalone HTML passes Node syntax validation.
- Browser rendering reviewed at desktop size and in a 390 × 844 CSS-pixel iframe. The narrow layout has no whole-document horizontal overflow; the comparison table and optional radial view scroll within their own regions.
- Checked the opening composition, mobile typography, mobile source panel, desktop matrix, and light/dark appearance.
- Browser interaction checks: mobile search and case opening; mobile chapter navigation and closing; source/response panels; R020, R011, and N001 qualifiers; all eight matrix cells; all 29 timeline selections; delegation options.
- Timing review found and corrected a loss of “by this date” information: the three date-limit entries now retain their upper bounds and use a distinct triangle marker.
- The matrix is intentionally limited to two separately reviewed examples. Uncoded disclosures are not marked unknown.

This is browser-based responsive testing, not physical-device or cross-browser certification. Source URLs were preserved and mapped to their records; the external source websites were not re-audited during this design build.

The source snapshot remains 18 November 2026, with authority coding reviewed on 19 November 2026.
