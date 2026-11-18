*Set the age window that protects all recent global data history entries from automatic cleanup.*

Since Bricks 2.5, `bricks/global_history/keep_days` changes the age window used when cleaning up [Global Data Revisions](https://academy.bricksbuilder.io/builder/interface/global-data-history/).

## Parameter and return value

- `$days` (*int*): The number of days of recent history to keep. Default: `90`.
- Return the desired number of days. Bricks casts it to an integer and uses a minimum of `1`. Returning `0` or `false` does not delete all history or disable cleanup.

## Example usage

Protect all history recorded within the last 30 days:

```php
add_filter( 'bricks/global_history/keep_days', function( $days ) {
    return 30;
} );
```

Add the filter in a plugin or child theme that loads during WP-Cron requests.

## How it combines with the entry count

The age window is not a maximum age for every stored entry. Bricks also protects each item's latest entries through [`bricks/global_history/keep_latest`](https://academy.bricksbuilder.io/developer/hooks/filters/bricks-global_history-keep_latest/), which defaults to 20.

Cleanup removes an entry only when it is older than the configured age window and outside that latest-entry count. With the example above and the default count, an item retains all entries from the last 30 days plus its latest 20 entries, even when some of those 20 are older.

The filter is read during scheduled daily cleanup. Changing it does not remove entries immediately. Cleanup depends on WP-Cron running, and increasing the period cannot recover entries already pruned.

This filter does not control page revisions or draft undo points. For finished drafts and version undo points, see [`bricks/drafts/keep_days`](https://academy.bricksbuilder.io/developer/hooks/filters/bricks-drafts-keep_days/).