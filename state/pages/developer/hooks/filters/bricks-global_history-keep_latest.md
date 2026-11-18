*Set the minimum number of recent history entries kept for each shared Bricks item during cleanup.*

Since Bricks 2.5, `bricks/global_history/keep_latest` changes how many of an item's latest [Global Data Revisions](https://academy.bricksbuilder.io/builder/interface/global-data-history/) entries are protected from automatic cleanup.

## Parameter and return value

- `$latest` (*int*): The number of latest entries to keep per resource/item pair. Default: `20`.
- Return the desired count. Bricks casts it to an integer and uses a minimum of `1`. Returning `0` or `false` does not disable retention or request unlimited history.

## Example usage

Keep at least the latest 40 entries for each recorded item:

```php
add_filter( 'bricks/global_history/keep_latest', function( $latest ) {
    return 40;
} );
```

Add the filter in a plugin or child theme that loads during WP-Cron requests.

## How it combines with the age limit

Bricks also keeps every entry within the period set by [`bricks/global_history/keep_days`](https://academy.bricksbuilder.io/developer/hooks/filters/bricks-global_history-keep_days/), which defaults to 90 days. Cleanup deletes an entry only when it is both outside the protected latest count and older than that period.

With the example above, an item can keep more than 40 entries if they are recent. It can also keep 40 entries older than 90 days when those are its latest entries. The count is a minimum retained per item, not a storage cap.

The filter is read during the scheduled daily cleanup. Changing it does not prune records immediately or recover records already removed. WP-Cron must run for scheduled cleanup to take place.