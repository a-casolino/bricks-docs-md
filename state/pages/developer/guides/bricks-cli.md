*Use Bricks CLI commands through WP-CLI to run builder-related maintenance tasks from the command line.*

Bricks 1.8.1+ integrates with the [WP-CLI](https://wp-cli.org/) (WordPress Command Line Interface). Allowing you to perform specific tasks from your server's command line interface instead of the GUI (Graphical User Interface).

## Drafts and site versions

Since Bricks 2.5, the `wp bricks drafts` commands inspect, publish, and discard saved [page drafts](https://academy.bricksbuilder.io/builder/interface/drafts/), [site versions](https://academy.bricksbuilder.io/builder/interface/site-versions/), and publish undo points.

Run commands from the WordPress installation directory. Replace `site-admin` with an existing WordPress user login and draft IDs with values from your site.

### List and review

```sh
wp bricks drafts list
wp bricks drafts list --status=all --format=json
wp bricks drafts review DRAFT_ID
```

`list` defaults to `--status=active`. Supported status values are `active`, `published`, `discarded`, and `all`. Output formats are `table` (default), `json`, and `csv`. The `kind` column distinguishes page drafts (`page`), site versions (`site`), and publish undo points (`backup`).

`review` shows a table of saved pending changes:

| Status | Meaning |
| --- | --- |
| `ready` | Bricks can apply the change without an unresolved conflict. |
| `same` | The live value already matches the draft. |
| `conflict` | The change needs a choice between live and draft values. |

The CLI reads saved changes; it does not save unsaved edits from an open Builder tab. Use the Builder's publish dialog when you need a visual comparison before choosing between conflicting values.

### Publish or undo a publish

After reviewing, publish as a user who can edit the draft and publish each included change:

```sh
wp bricks drafts publish DRAFT_ID --user=site-admin
```

This runs immediately, without a confirmation prompt. Bricks checks the current changes again and stops if conflicts remain unresolved. It also stops for missing or closed drafts, insufficient permissions, or another save or publish holding the required lock.

For conflicts, use `--keep-live` or `--keep-draft` with comma-separated `resource:itemId` keys from the reported conflicts. Only include keys you have reviewed:

```sh
wp bricks drafts publish DRAFT_ID --keep-live="globalClasses:abc123" --user=site-admin
```

These flags resolve conflicts; they do not limit publication to the listed items. Other ready changes are published too.

When publication replaces live values, the success message includes an undo version ID. Review that ID with `wp bricks drafts review`, then publish it with the same `publish` command to restore those replaced values. Later edits can cause conflicts during undo.

### Discard saved changes

```sh
wp bricks drafts discard DRAFT_ID --user=site-admin
```

This immediately discards the pending changes, without a confirmation prompt. It requires permission to edit the draft and leaves live data in place, including new shared items that had already been saved live. The CLI does not offer the Builder's option to delete newly created, unused shared items during discard.

## Regenerates CSS Files

Requires the Bricks "CSS loading method" to be set to "external files".

`wp bricks regenerate_assets`

## Global data revisions

Since Bricks 2.5, the `wp bricks history` commands inspect and recover recorded [global data revisions](https://academy.bricksbuilder.io/builder/interface/global-data-history/).

Run commands from the WordPress installation directory. Replace `site-admin` with an existing WordPress user login and item and entry IDs with values from your site.

### Inspect items and entries

Start by listing items with recorded history, then list one item's entries and inspect the entry you want to restore:

```sh
wp bricks history list globalClasses
wp bricks history list globalClasses abc123
wp bricks history show 42
```

`globalClasses` is a resource key. Other examples include `globalVariables`, `components`, `colorPalettes`, and `themeStyles`. An unknown resource key returns an error listing the supported keys.

`list` accepts `--format=table`, `--format=json`, or `--format=csv`; the default is `table`. It lists up to 200 items, or up to 100 entries when you provide an item ID. `show` prints one entry as JSON, including its stored value.

### Restore one item

After inspecting the entry, restore it as a WordPress user with permission to change that resource:

```sh
wp bricks history restore 42 --user=site-admin
```

This restores that item's stored value immediately, preserving other items. The restore uses Bricks' save permissions and conflict checks. Restoring executable code also requires code execution permission. Missing entries and entries without a restorable value return an error.

### Rebuild a resource

Use `rebuild` to replace an entire resource with its recorded values, for example when recovering a damaged class collection. Inspect the relevant history and take a site backup before replacing a whole collection.

```sh
wp bricks history rebuild globalClasses --user=site-admin
```

The default is to rebuild from the latest recorded values. Use `--at` to select an earlier UTC date and time:

```sh
wp bricks history rebuild globalClasses --at="2026-11-01 12:00:00" --user=site-admin
```

Rebuilding requires the WordPress `manage_options` capability. History containing executable code also requires code execution permission. Bricks refuses a rebuild if the retained history cannot establish the complete collection order; restore individual items instead.

### Clear recorded history

```sh
wp bricks history clear
```

This deletes all global data history for the site, leaving the current global data in place. Deleted history is no longer available for recovery.

Both `rebuild` and `clear` ask for confirmation. Their optional `--yes` flag skips that prompt.