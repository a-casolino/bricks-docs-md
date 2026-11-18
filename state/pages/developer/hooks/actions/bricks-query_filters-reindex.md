*Rebuild the Query Filters index from PHP after an import or on a recurring WP-Cron schedule.*

Starting with **Bricks 2.5**, use `bricks/query_filters/reindex` to request a full rebuild of the [Query Filters index](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#filter-index) from PHP. This is useful after a bulk import or a third-party update that bypasses the WordPress hooks Bricks uses to keep indexed values current.

Enable **Bricks > Settings > Query filters > Enable query sort / filter / live search** first. The action is registered only when Query Filters are enabled. Call it after Bricks has loaded, such as from an import-completion callback or a WP-Cron event.

## Parameters and Return Value

The action accepts no parameters. It requests a rebuild for the current site's indexable global filter definitions and standalone filter elements. Standalone filters must belong to published or private content. Linked elements reuse their global filter's index.

`do_action()` does not return the reindex result. Use the [PHP method](#php-result) below when your integration needs a status or error.

## Request a Rebuild {#request}

Run this inside your importer's completion callback, after it has saved the content:

```php
do_action( 'bricks/query_filters/reindex' );
```

A new rebuild clears the filter value index and queues background jobs. Filter values and counts can be incomplete until those jobs finish. The request returning does not mean indexing has finished.

If jobs are already queued, Bricks preserves their progress and requests continued processing. It does not clear the index or restart those jobs. A request made while another worker holds the index lock also leaves that work intact.

The full rebuild uses registered filter settings. If the stored filter-element metadata itself is missing or stale, use **Fix corrupted database** under **Bricks > Settings > Query filters** before requesting a rebuild.

## Read the PHP Result {#php-result}

Call `\Bricks\Query_Filters::get_instance()->reindex()` when you need to inspect the result. This example belongs inside an integration callback that runs after Bricks has loaded:

```php
if ( class_exists( '\Bricks\Query_Filters' ) ) {
    $result = \Bricks\Query_Filters::get_instance()->reindex();

    if ( is_wp_error( $result ) ) {
        error_log(
            sprintf(
                'Query filter reindex failed (%s): %s',
                $result->get_error_code(),
                $result->get_error_message()
            )
        );
    } else {
        $status = $result['status'];
        $queued_jobs = $result['queued_jobs'];
    }
}
```

Successful results contain `status` and `queued_jobs`:

| Status | Meaning |
| --- | --- |
| `started` | Bricks initialized a new rebuild and queued indexing jobs. |
| `in_progress` | Pending jobs or a running index operation prevented a new rebuild. Existing work is preserved. |
| `complete` | The rebuild required no indexing jobs. |

`queued_jobs` counts queued jobs, not indexed posts, terms, or users. If another operation holds the lock, the method returns `in_progress` with `queued_jobs: 0` without inspecting the queue. That zero does not mean indexing is complete.

The method can return these `WP_Error` codes:

| Code | Meaning |
| --- | --- |
| `bricks_query_filters_disabled` | Query Filters are disabled. |
| `bricks_query_filters_lock_unavailable` | Bricks could not acquire a safe database lock because the locking operation failed. A busy lock returns `in_progress` instead. |
| `bricks_query_filters_tables_unavailable` | Required filter tables are still unavailable after Bricks attempted to create or update them. |

The action and PHP method are intended for trusted server-side code. A custom HTTP endpoint that calls them must perform its own authorization and nonce checks. The built-in admin action still requires `manage_options` and a valid nonce.

## Schedule a Daily Rebuild {#daily}

Bricks does not automatically schedule recurring full rebuilds. Add this example to your [child theme's](https://academy.bricksbuilder.io/developer/guides/child-theme/) `functions.php` if an external import requires a daily refresh:

```php
add_action( 'init', function() {
    if ( ! has_action( 'bricks/query_filters/reindex' ) ) {
        return;
    }

    if ( ! wp_next_scheduled( 'mysite_daily_query_filter_reindex' ) ) {
        wp_schedule_event(
            time() + DAY_IN_SECONDS,
            'daily',
            'mysite_daily_query_filter_reindex'
        );
    }
} );

add_action( 'mysite_daily_query_filter_reindex', function() {
    do_action( 'bricks/query_filters/reindex' );
} );

add_action( 'switch_theme', function() {
    wp_clear_scheduled_hook( 'mysite_daily_query_filter_reindex' );
} );
```

The first rebuild is scheduled for about 24 hours after the code first runs. The `wp_next_scheduled()` check prevents duplicate recurring events. The theme-switch callback removes the schedule when you switch away from this theme.

If you remove the snippet while keeping the theme active, also clear `mysite_daily_query_filter_reindex` once with `wp_clear_scheduled_hook()` or a cron management tool. For plugin-based integrations, clean up the event on plugin deactivation instead. See [WordPress's scheduling guidance](https://developer.wordpress.org/plugins/cron/scheduling-wp-cron-events/).

## Background Processing {#background}

Bricks processes jobs in bounded batches. Authenticated admin requests can start a background AJAX worker. Requests without browser authentication cookies, such as WP-Cron and CLI calls, register a processing pass at shutdown. Bricks also schedules a one-time WP-Cron wake-up and retains the regular five-minute indexer event to continue pending work.

These background events continue queued jobs. They do not schedule another full rebuild. Keep the custom daily event above only while your integration needs it.

WP-Cron depends on WordPress being able to run due events. On a low-traffic site, events can run later than their scheduled time. If page-load cron is disabled, configure a server scheduler to run WordPress cron. See the [WordPress WP-Cron documentation](https://developer.wordpress.org/plugins/cron/).

For indexing that remains pending, check **Continue index job** under **Bricks > Settings > Query filters** and the [indexer troubleshooting notes](https://academy.bricksbuilder.io/builder/setup/known-issues/#query-filter-indexer-no-progress).

## Reindex or Continue Jobs? {#continue}

Use `bricks/query_filters/reindex` to request a full rebuild. Use [`bricks_indexer`](https://academy.bricksbuilder.io/developer/hooks/actions/bricks-indexer/) to process jobs that are already queued. Running `bricks_indexer` with an empty queue does not create a new rebuild.

## Abilities API {#abilities}

The existing `bricks/reindex-filters` ability uses the same reindex method and still requires `manage_options`. In Bricks 2.5, its `reindexed` value is `false` when existing work is preserved, with `pending` and `progress` describing the asynchronous queue. This is not an indexing failure. A `true` value means a new rebuild was requested successfully, including an immediate `complete` result; check `pending` before treating it as finished.