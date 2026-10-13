# Filter: bricks/query_api/headers

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_api-headers/

*Filters the headers used by a Query API element request.*

Filters the headers used by a Query API element request before Bricks sends it.

## Parameters

- `$headers` (array): HTTP request headers.
- `$element_id` (string): The Query API element ID.
- `$query_api` (object): The Query API integration instance.

## Example usage

```php
add_filter( 'bricks/query_api/headers', function( $headers, $element_id, $query_api ) {
    $headers['X-Client'] = 'my-site';

    return $headers;
}, 10, 3 );
```
