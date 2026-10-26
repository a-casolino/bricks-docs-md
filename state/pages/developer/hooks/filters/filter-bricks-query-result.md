*Modify fetched Bricks query results, including sorting posts or slicing an array returned by an ACF loop.*

Available since Bricks 1.8, `bricks/query/result` lets you modify fetched query results before the loop renders them. The result type depends on the query: a native post query returns a `WP_Query` object, while an ACF loop can return an array. Use [`bricks/query/run`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-run/) when adding a custom query type.

## Sort post results

```php
// Use this filter to rearrange it by post title (PHP way instead of query orderby)
add_filter( 'bricks/query/result', function( $result, $query_obj ){
  // Return: Element ID is not "djvsvi", nor is it a post query
  if ( $query_obj->element_id !== 'djvsvi' || $query_obj->object_type !== 'post' ) {
    return $result;
  }

  // Sort by post title (descending)
  // Result is WP_Query object with posts
  if ( $result->have_posts() ) {
    $posts = $result->posts;

    usort( $posts, function( $a, $b ) {
      return strcmp( $b->post_title, $a->post_title );
    });

    $result->posts = $posts;
  }

  return $result;
}, 10, 2 );
```

## Slice an ACF array

For an ACF Relationship loop that returns an array, use a result filter scoped to the loop element to skip or limit items. Replace `abc123` with the loop element's raw Bricks ID, without the `brxe-` prefix or a `#`.

This example skips the first item and returns up to three of the remaining items:

```php
add_filter( 'bricks/query/result', function( $result, $query ) {
    if ( $query->element_id !== 'abc123' || ! is_array( $result ) ) {
        return $result;
    }

    return array_slice( $result, 1, 3 );
}, 10, 2 );
```

With four items in the ACF array, the loop renders the second, third, and fourth items in their existing editorial order. The saved ACF entries remain unchanged. To keep the first item and display up to three items, use `array_slice( $result, 0, 3 )` instead.

Slicing here does not automatically recalculate the query's total count, maximum number of pages, or summary positions. If the loop has a summary or pagination, keep that metadata consistent with the intended behavior using [`bricks/query/result_count`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-result_count/), [`bricks/query/result_max_num_pages`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-result_max_num_pages/), [`bricks/query/result_start`](https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query-result_start/), and [`bricks/query/result_end`](https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query-result_end/). A fixed slice does not fetch another page.

For native query limits and offsets, use the [Query Loop controls](https://academy.bricksbuilder.io/builder/dynamic-content/query-loop/). The `result_start` and `result_end` filters change summary metadata only; they do not slice the results.