# Bricks Builder docs in Markdown

Unofficial, automatically updated Markdown export of the [Bricks Builder Academy](https://academy.bricksbuilder.io/).

**File:** [`bricks-docs.md`](bricks-docs.md)

- Raw URL: https://raw.githubusercontent.com/a-casolino/bricks-docs-md/main/bricks-docs.md
- GitHub Pages URL (once Pages is enabled): https://a-casolino.github.io/bricks-docs-md/bricks-docs.md

## How it works

- `scrape.py` reads the site's sitemap, downloads every page (one request per second, respecting `robots.txt`), converts the content to Markdown and joins all pages into a single file, following the sidebar order.
- `.github/workflows/update.yml` runs every day at 04:17 UTC. A commit is made only when the documentation content changed (a SHA-256 of the content is stored in the file).
- Run it manually from the **Actions** tab with *Run workflow*, or locally:

```bash
pip install -r requirements.txt
python scrape.py --output bricks-docs.md
```

## GitHub Pages

Settings → Pages → Source: *Deploy from a branch*, branch `main`, folder `/ (root)`.
The `.nojekyll` file makes Pages serve the `.md` file as-is.

Content © Bricks. This repository only mirrors the public documentation for convenience.
