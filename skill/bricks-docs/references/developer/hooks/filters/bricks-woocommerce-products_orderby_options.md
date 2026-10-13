# Filter: bricks/woocommerce/products_orderby_options

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-products_orderby_options/

*Filters WooCommerce product order-by options used by Bricks.*

Filters WooCommerce product order-by options used by Bricks controls.

## Parameters

- `$options` (array): Order-by option keys and labels.

## Example usage

```php
add_filter( 'bricks/woocommerce/products_orderby_options', function( $options ) {
    $options['title'] = esc_html__( 'Sort by title', 'my-plugin' );

    return $options;
} );
```
