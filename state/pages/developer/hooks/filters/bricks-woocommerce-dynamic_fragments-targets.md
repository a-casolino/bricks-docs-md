*Filters WooCommerce dynamic fragment targets before rendering.*

Filters WooCommerce dynamic fragment targets before Bricks renders the fragments.

## Parameters

- `$targets` (array): Mounted fragment targets from the current page.

## Example usage

```php
add_filter( 'bricks/woocommerce/dynamic_fragments/targets', function( $targets ) {
    return $targets;
} );
```