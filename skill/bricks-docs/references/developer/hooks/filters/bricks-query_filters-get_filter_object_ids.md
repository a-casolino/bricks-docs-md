# Filter: bricks/query_filters/get_filter_object_ids

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters-get_filter_object_ids/

*Filters the object IDs used to build query filter counts.*

Filters the object IDs used to build query filter counts. Use it when an integration needs to supply or alter the base object IDs for a query/filter source.

## Parameters

- `$all_object_ids` (array): The object IDs Bricks has collected.
- `$query_id` (string): The query element ID.
- `$query_type` (string): The query type being processed.
- `$source` (string): The filter source.

## Example usage

```php
add_filter( 'bricks/query_filters/get_filter_object_ids', function( $all_object_ids, $query_id, $query_type, $source ) {
    return $all_object_ids;
}, 10, 4 );
```
