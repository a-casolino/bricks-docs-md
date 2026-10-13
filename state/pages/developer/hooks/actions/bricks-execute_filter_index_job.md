*Runs before a query filter index job is executed.*

Runs before a query filter index job is executed. Bricks uses this point so integrations can prepare context, such as switching language, before indexing starts.

## Parameters

- `$job` (array): The index job data that is about to be processed.

## Example usage

```php
add_action( 'bricks_execute_filter_index_job', function( $job ) {
    // Prepare integration context before this index job runs.
}, 10, 1 );
```