# Action: bricks/dynamic_data/tags_registered

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-dynamic_data-tags_registered/

*Runs after all core dynamic data tags have been registered. This is the recommended hook for registering custom dynamic data providers or adding logic that.*

Runs after all core dynamic data tags have been registered. This is the recommended hook for registering custom dynamic data providers or adding logic that depends on registered tags.

## Parameters

None.

## Example usage

```php
add_action( 'bricks/dynamic_data/tags_registered', function() {
    // Register custom dynamic data tags or providers here
    // Example: Bricks\Integrations\Dynamic_Data\Providers::register( 'my_custom_provider', $provider_instance );
} );
```
