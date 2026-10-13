# Filter: bricks/dynamic_data/register_providers

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-dynamic_data-register_providers/

*Filters the dynamic data providers registered by Bricks.*

Filters the dynamic data providers registered by Bricks. Use it to add, remove, or reorder provider keys before Bricks registers them.

## Parameters

- `$providers` (array): Provider keys such as cmb2, wp, woo, acf, pods, metabox, toolset, and jetengine.

## Example usage

```php
add_filter( 'bricks/dynamic_data/register_providers', function( $providers ) {
    $providers[] = 'my_provider';

    return $providers;
} );
```
