*Filters the numeric ending result position reported by Query Results Summary. Changes summary metadata only, without limiting or slicing results.*

The `bricks/query/result_end` filter changes the numeric ending position stored in `$query->end`. [Query Results Summary](https://academy.bricksbuilder.io/builder/elements/query/query-results-summary/) reads this value for its `%end%` placeholder.

This filter changes summary metadata only. It does not change the returned items, skip the first item, limit the rendered cards, change the total count, or fetch another page.

## Parameters

- `$end` (*int*): The current ending result position. Native post, term, and user queries normally calculate one-based positions. The value can be `0` when no range has been populated, including in provider-backed ACF loops.
- `$query` (`Bricks\Query`): The query instance. Use its public `$element_id` property to scope the filter to a specific loop element.

## Example usage

This example sets the ending position reported for a specific loop to `3`. It changes only the summary number; it does not limit the loop to three items.

Replace `abc123` with the loop element's raw Bricks ID, without the `brxe-` prefix or a `#`.

```php
add_filter( 'bricks/query/result_end', function( $end, $query ) {
    if ( $query->element_id === 'abc123' ) {
        // Adjust the summary's ending position only.
        return 3;
    }

    return $end;
}, 10, 2 );
```

For example, if an ACF Relationship loop returns four items, returning `3` here still renders all four in their original order. The total count remains `4`, and no additional page is fetched.

## Change the actual results

Use the [Query Loop controls](https://academy.bricksbuilder.io/builder/dynamic-content/query-loop/) for native query limits and offsets, or [`bricks/query/result`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-result/) to modify fetched results.

For an ACF loop that returns an array, a result filter scoped to the loop element can use `array_slice()` to skip or limit items. This changes the returned array while preserving the saved ACF entries and the editorial order of the retained items. See the [ACF array example](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-result/#slice-an-acf-array).