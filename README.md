# Who Gave the Agent That Authority?

An interactive research narrative by Christopher Hayes about AI agents, delegated authority, and the decisions hidden inside getting a task done. The opening reconstructs a local-workbook/public-hosting example, then connects it to an authority atlas, evidence matrix, recorded timing, and practical delegation choices.

## Read the interactive experience

[**Open the live HTML experience →**](https://chrisdhayes.github.io/who-gave-the-agent-authority/)

Explore the story, inspect selected published disclosures, compare how authority is framed, and try a short exercise for defining what an agent may decide. The experience is designed to work on desktop and phones, with keyboard navigation and reduced-motion support.

This is connected publication edition v1.5. The radial Atlas remains the signature desktop view. A multi-boundary comparison adds source-linked explanations for all 29 disclosures, while quantitative close-ups examine selected examples. The plain-language introduction, author note, title emblem, and chapter order are preserved.

## Run and build

Open `index.html` in a modern browser, or serve the repository root with a static server. `dist/` contains the equivalent deployment output. The shipped HTML contains the data, styling, SVGs, and JavaScript needed for the experience.

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
- The matrix separately codes five deliberately contrasting examples: R024, R001, R004, R011, and R020. The other 24 disclosures are available in the atlas and detailed case panels, and have not been independently coded in the matrix.
- R020 is explicitly non-misaligned; R011 is a controlled experiment; N001 is an unverified allegation.
- Timing preserves day, range, month, and latest-known-date precision. An undated response is not assigned an event date.
- Source reporting, analyst interpretation, proposed control design, and demonstrated effectiveness are distinct.

## Interactions and access

The experience supports chapter navigation, a stepped and scroll-responsive workbook reconstruction, radial/branch/list Atlas views, multi-boundary comparison, search and theme filters, two-case comparison, quantitative close-ups, and a delegation exercise. Keyboard controls, native dialogs, reduced-motion preferences, and horizontally scrollable comparison tables are supported.

Source provenance is retained in `data/evidence.json`; matrix states, definitions, review date, and source URLs are in `data/matrix.json`. Boundary definitions, explanations, review basis, and figures are documented in the corresponding data and research files. The original transparent emblem and its generation brief are retained in `assets/`.

## Read the publication

The essay develops the central argument: completing a task can conceal a decision the user never delegated. The shorter companion article opens with the workbook example and provides invitations to explore specific moments in the experience.

| Read or inspect | File |
|---|---|
| **Live interactive experience** | [Open the HTML experience](https://chrisdhayes.github.io/who-gave-the-agent-authority/) |
| Interactive experience source | [index.html](index.html) |
| Research essay | [Markdown](publishing/essay.md) · [Reading page](publishing/essay.html) |
| Companion article | [Markdown](publishing/substack.md) · [Reading page](publishing/substack.html) |
| Publication setup and link map | [START_HERE.md](publishing/START_HERE.md) |
| Citations and analytical scope | [Publication evidence map](research/publication-claims.md) |
| Structured source collection | [evidence.json](data/evidence.json) |

Editable Word copies are included under `publishing/`. Their links may use a private review site and require the owner's access; the public HTML experience link above is the live GitHub Pages site.

## Editing and provenance

Edit the writing in `publishing/source/` and rebuild with `scripts/build_publication.py`. Edit experience content and interactions in `src/`, and rebuild with `scripts/build.py`. Data definitions and source records are maintained in `data/`.

The published reports remain the work of their respective source publishers. Author analysis, editorial design, and implementation are attributed to Christopher Hayes. This package does not assign a rate or prevalence claim to the selected disclosures.
