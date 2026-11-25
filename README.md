# Who Gave the Agent That Authority?

An interactive research narrative by Christopher Hayes. The opening reconstructs the local-workbook/public-hosting example, then connects it to the authority atlas, evidence matrix, recorded timing, and practical delegation questions.

This is connected publication edition v1.5. The radial Atlas remains the signature desktop view. A multi-boundary comparison adds source-linked explanations for all 29 disclosures, while two quantitative close-ups examine task framing (R006) and grader responses (R010). A shared case selection connects the Atlas, checkpoint evidence, timeline and response ledger. Readers can optionally compare two cases and copy an illustrative delegation instruction.

The plain-language introduction, author note, title emblem and chapter order are preserved. Phones start with a focused Atlas branch, keeping case names at normal text size. The complete radial view and readable list remain available.

A sculptural boundary emblem sits beside the title, with a subtle animated signal, a pause control and reduced-motion support. It is a visual metaphor, not incident data.

The experience retains the collected 18 November 2026 snapshot and the original Atlas themes reviewed on 19 November. The new multi-boundary coding and quantitative close-ups use 26 report pages re-read on 21 November. The three notices and response records retain the collected snapshot. It is not a live feed.

## Run and build

Open `index.html` in a modern browser, or serve the repository root with a static server. `dist/` contains the equivalent deployment output. The shipped HTML contains all data, styling, SVGs, the embedded title image, and JavaScript. No network-loaded assets or packages are required for the experience itself; source links open externally. Optional explanations and role perspectives use native disclosure controls. The delegation example explains the permissions implied by each choice.

To rebuild and check:

```sh
python3 scripts/build.py
python3 scripts/build_publication.py
python3 scripts/validate.py
python3 scripts/validate_publication.py
```

## Evidence boundaries

- 29 disclosures: 26 reports and 3 notices. They are not 29 confirmed production incidents or necessarily 29 unique runs.
- The six authority themes are analyst interpretations; N001 remains unassigned.
- The matrix separately codes five deliberately contrasting examples: R024, R001, R004, R011 and R020. The other 24 disclosures are available in the atlas and detailed case panels, and have not been checkpoint-coded here. The five checkpoint sources were re-read on 21 November 2026. The additional multi-boundary coding is a separate exercise: a boundary mark does not imply execution, a breach or severity.
- R020 is explicitly non-misaligned; R011 is a controlled experiment; N001 is an unverified allegation.
- Timing preserves day, range, month, and latest-known-date precision. An undated response is not assigned an event date.
- Source reporting, analyst interpretation, proposed control design, and demonstrated effectiveness are distinct.

## Interactions and access

The experience supports chapter navigation, a stepped and scroll-responsive workbook reconstruction, radial/branch/list Atlas views, multi-boundary comparison, search and theme filters, two-case comparison, source/response panels, five-case checkpoint inspection, two quantitative close-ups, 29 timing/response views, a copyable delegation example, and light/dark appearances. A selected case persists across the views. Cases outside the five checkpoint examples are explicitly not reviewed; another case's findings are never substituted.

Keyboard controls, native dialogs, reduced-motion preferences and horizontally scrollable comparison tables are supported. The phone authority table retains a narrow sticky case column. Clipboard failure reveals a selected, read-only instruction for manual copying.


Source provenance is retained in `data/evidence.json`; matrix states, definitions, review date and source URLs are in `data/matrix.json`. New boundary definitions, explanations, review basis and follow-up questions are in `data/authority-comparison.json`; numerical values and qualifications are in `data/closeups.json`. The source-review scope is documented in `research/authority-comparison-review.md`. Each disclosure and response links to its collected source. The original research workbook and wireframe remain separate, unchanged artifacts.

The original transparent emblem and its generation brief are retained in `assets/`. Motion pauses when the opening is out of view or the tab is hidden. Reduced-motion preferences show the static image.

## Read the publication

The essay develops the central argument: completing a task can conceal a decision the user never delegated. The shorter article opens with the workbook example and provides six invitations to inspect specific moments in the experience. Both distinguish source reporting, author interpretation and proposed practices.

| Read or inspect | File |
|---|---|
| Interactive experience | [index.html](index.html) |
| Research essay | [Markdown](publishing/essay.md) · [Reading page](publishing/essay.html) |
| Companion article | [Markdown](publishing/substack.md) · [Reading page](publishing/substack.html) |
| Publication setup and link map | [START_HERE.md](publishing/START_HERE.md) |
| Citations and analytical scope | [Publication evidence map](research/publication-claims.md) |
| Structured source collection | [evidence.json](data/evidence.json) |

Editable Word copies are included under `publishing/`. Their links currently use the private review Site. HTML reading pages use relative links and work locally when the package is extracted. Markdown is convenient for reading on GitHub; the HTML files are the intended interactive navigation route.

The GitHub repository is configured. The public experience URL is not yet configured. See the publication guide to set the final URL once, regenerate the public Substack export, and preserve the stable moment links. The existing review Site remains private to its owner.

## Editing and provenance

Edit the writing in `publishing/source/` and rebuild with `scripts/build_publication.py`. Edit experience content and interactions in `src/`, and rebuild with `scripts/build.py`. Data definitions live in `data/`. The package excludes Site identity, credentials, Git history and temporary QA files.

The published reports remain the work of their respective source publisher. Author analysis, editorial design and implementation are attributed to Christopher Hayes. This package does not assign a new open-source or reuse licence to the material.
