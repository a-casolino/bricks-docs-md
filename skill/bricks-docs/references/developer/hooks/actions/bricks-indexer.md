# Action: bricks_indexer

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-indexer/

*Triggers the Bricks query filter indexer job runner.*

Triggers the Bricks query filter indexer job runner. Bricks schedules this action with WP-Cron every five minutes and also triggers it from the background indexing AJAX endpoint.

The core indexer callback bails when the indexer is already running, then continues pending jobs until the queue is empty or server resource limits are reached.

## Example usage

```php
add_action( 'my_plugin_run_bricks_indexer', function() {
    do_action( 'bricks_indexer' );
} );
```
