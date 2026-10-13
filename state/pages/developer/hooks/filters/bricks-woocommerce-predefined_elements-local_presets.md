*Filters local WooCommerce predefined element presets.*

Filters local WooCommerce predefined element presets after Bricks loads JSON presets.

## Parameters

- `$presets` (array): Local preset payloads.

## Example usage

```php
add_filter( 'bricks/woocommerce/predefined_elements/local_presets', function( $presets ) {
    return $presets;
} );
```