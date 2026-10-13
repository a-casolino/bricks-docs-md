# Filter: bricks/woocommerce/dynamic_fragments/html

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-dynamic_fragments-html/

*Filters rendered HTML for a WooCommerce dynamic fragment.*

Filters rendered HTML for a single WooCommerce dynamic fragment.

## Parameters

- `$html` (string): Rendered fragment HTML.
- `$target` (array): The fragment target being rendered.
- `$render_data` (array): Bricks render data used for the fragment.

## Example usage

```php
add_filter( 'bricks/woocommerce/dynamic_fragments/html', function( $html, $target, $render_data ) {
    return $html;
}, 10, 3 );
```
