*Filters Woo setup wizard presets.*

Filters Woo setup wizard presets before Bricks registers them. Use it to add or override one-click setup JSON presets.

## Parameters

- `$presets` (array): Preset data grouped by area and preset ID.

## Example usage

```php
add_filter( 'bricks/woo_setup_wizard/register_presets', function( $presets ) {
    $presets['checkout']['my-preset'] = [
        'label' => 'My checkout preset',
    ];

    return $presets;
} );
```