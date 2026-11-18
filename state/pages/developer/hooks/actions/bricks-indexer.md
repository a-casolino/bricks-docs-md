*Triggers the Bricks query filter indexer job runner.*

Triggers the Bricks query filter indexer job runner. Bricks schedules this action with WP-Cron every five minutes and also triggers it from the background indexing AJAX endpoint.

The core callback processes pending jobs until the queue is empty or server resource limits are reached. From Bricks 2.5, workers and full-reindex requests share a database lock. The worker exits when another index operation holds that lock.

This action continues existing jobs. To request a full rebuild, use [`bricks/query_filters/reindex`](https://academy.bricksbuilder.io/developer/hooks/actions/bricks-query_filters-reindex/) (Bricks 2.5). Running `bricks_indexer` with an empty queue does not create new indexing work.

## Example usage

```php
add_action( 'my_plugin_run_bricks_indexer', function() {
    do_action( 'bricks_indexer' );
} );
```