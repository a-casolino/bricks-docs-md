*Filters WooCommerce dynamic fragments before the AJAX response is sent.*

Filters WooCommerce dynamic fragments before Bricks returns the AJAX response.

## Parameters

- `$fragments` (array): Selector-keyed fragment HTML.
- `$targets` (array): Mounted fragment targets from the current page.

## Example usage

```php
add_filter( 'bricks/woocommerce/dynamic_fragments/fragments', function( $fragments, $targets ) {
    return $fragments;
}, 10, 2 );
```