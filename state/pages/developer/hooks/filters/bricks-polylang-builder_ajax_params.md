*Filters the Polylang AJAX parameters injected into builder media requests.*

Filters the Polylang AJAX parameters injected into builder media requests. Use it to add or adjust language-aware parameters for the media library in the builder.

## Parameters

- `$params` (array): Parameters added to media AJAX requests.
- `$post_id` (int): The current builder post ID.

## Example usage

```php
add_filter( 'bricks/polylang/builder_ajax_params', function( $params, $post_id ) {
    $params['lang'] = pll_current_language();

    return $params;
}, 10, 2 );
```