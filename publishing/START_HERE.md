# Publication guide

The essay, article and experience are prepared. The GitHub repository has been created. The public experience URL has not yet been configured or verified. Nothing has been posted to Substack.

## Read now

Extract the complete package, then open `index.html`. The Sources and method chapter links to both reading pages. You can also open `publishing/essay.html` or `publishing/substack.html` directly. Their links return to the relevant moment in the local experience. Keep the directory structure together.

The Word copies are editable review documents. Their experience links currently use the owner's existing private Site. Those links require the owner's access and should be replaced before public publication.

## Prepare GitHub

Suggested repository name: `who-gave-the-agent-authority`.

Suggested description:

> The decisions hidden inside AI workarounds. An interactive Atlas, research essay and companion article by Christopher Hayes, connecting 29 selected OpenAI disclosures to questions of delegated authority, evidence and practical system design.

Upload the extracted files with `index.html` at the repository root. Uploading only this ZIP does not expose its contents as a website. To host the experience publicly with GitHub Pages, select **Settings → Pages → Deploy from a branch**, then the branch containing the files and **/(root)**. The included `.nojekyll` file supports serving the prepared static files. Use the actual address GitHub returns; the project does not assume a domain or repository name.

GitHub's [publishing-source instructions](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) explain the current setup. Check the resulting site without signing in before placing its links in Substack.

## Set the public destination once

After the experience is live, enter its exact HTTPS address in `public_experience_url` in `publishing/publication.json`. Optionally record the repository address in `repository_url`. Then run:

```sh
python3 scripts/build_publication.py
python3 scripts/export_documents.py
python3 scripts/validate.py
python3 scripts/validate_publication.py
```

Word export requires the packages in `requirements-documents.txt`. The experience and reading-page builds use the Python standard library; the experience validator also uses Node to check JavaScript syntax. Word layout should be rechecked after text or formatting changes.

The publication builder updates the Markdown and creates `publishing/substack-ready-to-publish.md` only when a public destination is configured. Word links use that same destination. The HTML reading pages keep portable relative links, so they work both locally and on the public site.

## Place the article in Substack

Use the title, subtitle and body from the article. Preserve the six bold links in their existing positions. In the Substack editor, use the links as text links or buttons; the interactive charts open in the experience. The delivered article does not depend on an embedded interactive chart being supported by Substack.

Send a preview to yourself and check all six links on a phone. Each should open the named moment and select the intended case. The experience offers eight stable moment links in total, plus individual case links such as `#case-R024`.

| Article invitation | Fragment | Selected case |
|---|---|---|
| Sharing decision | `#workbook-boundary` | R024 |
| Atlas boundary comparison | `#authority-comparison` | R024 |
| Grader responses | `#grader-authority` | R010 |
| Matched-task comparison | `#framing-gap` | R006 |
| Evidence stages | `#evidence-stages` | R001 |
| Delegation exercise | `#design-delegation` | R024 |

The essay also links to `#supported-restart` and `#response-evidence`. Preserve these fragment names in later versions so previously published links continue to work.
