# Bricks Builder docs in Markdown

Unofficial, automatically updated Markdown export of the [Bricks Builder Academy](https://academy.bricksbuilder.io/), meant as context for AI assistants that build Bricks sites (for example alongside the Bricks 2.4 MCP abilities).

| File | Content |
| --- | --- |
| [`bricks-docs.md`](bricks-docs.md) | Every page in one file |
| [`sections/getting-started.md`](sections/getting-started.md) | Getting Started |
| [`sections/builder.md`](sections/builder.md) | Builder: elements, styling, dynamic data, features |
| [`sections/developer.md`](sections/developer.md) | Developer: hooks, filters, custom elements, functions |
| [`sections/schema.md`](sections/schema.md) | Bricks Data Model: JSON schema of elements, controls, global classes, variables |
| [`sections/integrations.md`](sections/integrations.md), … | Other sections |
| [`llms.txt`](llms.txt) | Index of the files above |

Public URLs:

- https://raw.githubusercontent.com/a-casolino/bricks-docs-md/main/bricks-docs.md
- https://a-casolino.github.io/bricks-docs-md/bricks-docs.md (once GitHub Pages is enabled)

Replace `bricks-docs.md` with `sections/<name>.md` or `llms.txt` for the other files.

## How it works

- `scrape.py` reads the Academy's `content-index.json`, downloads the Markdown source each page publishes (`<page>.md`), removes Astro/Starlight syntax (frontmatter, MDX imports, components, `:::` callouts) and writes the files above. Pages without a Markdown source fall back to HTML conversion. One request per second, `robots.txt` respected.
- `.github/workflows/update.yml` runs every day at 04:17 UTC and commits only when the content changed (each file stores a SHA-256 of its content).
- Run it manually from the **Actions** tab (*Run workflow*) or locally:

```bash
pip install -r requirements.txt
python scrape.py --out-dir .
```

## GitHub Pages

Settings → Pages → Source: *Deploy from a branch*, branch `main`, folder `/ (root)`.
The `.nojekyll` file makes Pages serve the `.md` files as-is.

Content © Bricks. This repository only mirrors the public documentation for convenience.
