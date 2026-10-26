*Filters the numeric starting result position reported by Query Results Summary. Changes summary metadata only, without offsetting or slicing results.*

The `bricks/query/result_start` filter changes the numeric starting position stored in `$query->start`. [Query Results Summary](https://academy.bricksbuilder.io/builder/elements/query/query-results-summary/) reads this value for its `%start%` placeholder.

This filter changes summary metadata only. It does not change the returned items, skip the first item, limit the rendered cards, change the total count, or fetch another page.

## Parameters

- `$start` (*int*): The current starting result position. Native post, term, and user queries normally calculate one-based positions. The value can be `0` when no range has been populated, including in provider-backed ACF loops.
- `$query` (`Bricks\Query`): The query instance. Use its public `$element_id` property to scope the filter to a specific loop element.

## Example usage

This example adds one to the starting position reported for a specific loop. It changes only the summary number; the first item still renders.

Replace `abc123` with the loop element's raw Bricks ID, without the `brxe-` prefix or a `#`.

```php
add_filter( 'bricks/query/result_start', function( $start, $query ) {
    if ( $query->element_id === 'abc123' ) {
        // Adjust the summary's starting position only.
        return $start + 1;
    }

    return $start;
}, 10, 2 );
```

For example, if `$start` is `1`, the summary reports `2`. All returned items still render in their original order, and `%end%` and `%total%` remain unchanged.

## Change the actual results

Use the [Query Loop controls](https://academy.bricksbuilder.io/builder/dynamic-content/query-loop/) for native query limits and offsets, or [`bricks/query/result`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-result/) to modify fetched results.

For an ACF loop that returns an array, a result filter scoped to the loop element can use `array_slice()` to skip or limit items. This changes the returned array while preserving the saved ACF entries and the editorial order of the retained items. See the [ACF array example](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-result/#slice-an-acf-array).