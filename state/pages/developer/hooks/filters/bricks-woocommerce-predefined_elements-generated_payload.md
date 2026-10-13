*Filters a generated WooCommerce predefined element payload.*

Filters a generated WooCommerce predefined element payload before Bricks returns it.

## Parameters

- `$response` (array): The generated payload response.
- `$preset` (string): The preset ID being generated.
- `$context` (array): Generation context for the preset.

## Example usage

```php
add_filter( 'bricks/woocommerce/predefined_elements/generated_payload', function( $response, $preset, $context ) {
    return $response;
}, 10, 3 );
```