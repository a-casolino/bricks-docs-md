---
name: bricks-docs
description: Bricks Builder (WordPress) documentation and data-model reference. Use when building, editing or debugging a site with Bricks Builder, writing Bricks element JSON, global classes, variables, query loops, dynamic data, conditions, interactions, hooks or custom elements, or when using the Bricks MCP abilities.
---

# Bricks Builder documentation

Complete, daily-refreshed copy of the official Bricks Academy (https://academy.bricksbuilder.io/) in `references/`, pages grouped by topic (for example `developer-hooks-1.md`, `builder-elements.md`). Content © Bricks.

## How to use

1. Find the right page in the section indexes below (each lists page title, the file containing it and a one-line summary), or search across all pages, e.g. `grep -il "query loop" references/*.md`.
2. Read only the pages you need: inside a file every page starts with `# <title>` and its source URL, so search for the title (`grep -n "^# Query Loop" references/*.md`) and read from that line.
3. For element/control/global settings JSON (what the builder stores and what the Bricks MCP abilities read and write), use the **Schema** section (files `developer-schema-*.md`).
4. Prefer what these pages say over memory: Bricks changes often. When a page and the live site disagree (for example ability names exposed by the Bricks MCP server), trust the live site.

## Sections

- **Home** (1 pages): `references/_index-home.md`
- **Getting Started** (13 pages): `references/_index-getting-started.md`
- **Builder** (220 pages): `references/_index-builder.md`
- **Developer** (333 pages): `references/_index-developer.md`
- **Schema (Bricks Data Model)** (231 pages): `references/_index-schema.md`
- **Integrations** (28 pages): `references/_index-integrations.md`
