*Set the cleanup age for finished Bricks drafts and version publish undo points while keeping active work.*

Since Bricks 2.5, `bricks/drafts/keep_days` changes when Bricks removes finished draft records and publish undo points during automatic cleanup.

## Parameter and return value

- `$days` (*int*): The cleanup age in days, measured from each record's last update. Default: `30`.
- Return the desired number of days. Bricks casts it to an integer and uses a minimum of `1`. Returning `0` or `false` does not mean unlimited retention or immediate deletion.

## Example usage

Keep eligible records for 60 days after their last update:

```php
add_filter( 'bricks/drafts/keep_days', function( $days ) {
    return 60;
} );
```

Add the filter in a plugin or child theme that loads during WP-Cron requests.

## What cleanup removes

Once a record's last update is older than the configured period, cleanup can remove:

- Finished records marked published or discarded.
- Publish undo points, including undo points that are still available under **Versions > Undo a publish**.

Cleanup also removes the stored items and review-link records belonging to those removed records. This is separate from a review link's own expiry.

Active editable [page drafts](https://academy.bricksbuilder.io/builder/interface/drafts/) and [site versions](https://academy.bricksbuilder.io/builder/interface/site-versions/) are not removed by age. A named site version stays active after publishing, so it remains available for later work; its publish undo points still have the cleanup window above.

Cleanup runs on a scheduled daily WP-Cron task while Drafts is enabled. Changing the filter does not delete records immediately. Undo points older than the configured window can be removed on the next cleanup; increasing the period cannot recover an undo point already removed.

For the independent retention rules governing individual shared-item history, see [`bricks/global_history/keep_days`](https://academy.bricksbuilder.io/developer/hooks/filters/bricks-global_history-keep_days/).